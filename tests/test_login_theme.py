"""Browser regressions using JupyterHub's real templates and static assets."""

from collections import Counter
from contextlib import contextmanager
from copy import deepcopy
import os
from pathlib import Path
import unittest
from urllib.parse import unquote, urlparse

import html5lib
from jinja2 import ChoiceLoader, Environment, FileSystemLoader, PrefixLoader
from jupyterhub._data import DATA_FILES_PATH
from playwright.sync_api import expect, sync_playwright


ROOT = Path(__file__).resolve().parents[1]
HUB_DATA = Path(DATA_FILES_PATH)
CUSTOM = {
    "redirect_to": None,
    "org": {
        "name": "Schmidt Observatory System Science Symposium",
        "url": "https://example.org/",
        "logo_url": "/hub/static/extra-assets/images/sos-logo-white.png",
    },
    **{
        key: {"name": "Example Org", "url": "https://example.org/", "custom_html": ""}
        for key in ("operated_by", "funded_by", "designed_by")
    },
}


def render(custom=None, **context):
    env = Environment(
        loader=ChoiceLoader([
            PrefixLoader({"templates": FileSystemLoader(HUB_DATA / "templates")}, "/"),
            FileSystemLoader([ROOT / "templates", HUB_DATA / "templates"]),
        ]),
        autoescape=True,
    )
    return env.get_template("login.html").render(
        custom=CUSTOM if custom is None else custom,
        static_url=lambda path, **kwargs: "/hub/static/" + path,
        authenticator_login_url="/hub/login?next=%2Fhub%2F",
        authenticator={"request_otp": False},
        base_url="/hub/", prefix="/hub/", username="",
        xsrf="test-xsrf", xsrf_token="test-xsrf", **context,
    )


class LoginThemeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.playwright = sync_playwright().start()
        cls.addClassCleanup(cls.playwright.stop)
        cls.browser = cls.playwright.chromium.launch(
            executable_path=os.environ.get("PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH"),
        )
        cls.addClassCleanup(cls.browser.close)

    @contextmanager
    def page(self, html, theme="light", width=1440):
        context = self.browser.new_context(
            color_scheme=theme, viewport={"width": width, "height": 1000},
            reduced_motion="reduce",
        )
        errors = []
        failures = []

        def route_request(route):
            url = urlparse(route.request.url)
            if url.hostname == "hub.invalid" and url.path == "/hub/login":
                route.fulfill(body=html, content_type="text/html")
            elif url.hostname == "hub.invalid" and url.path.startswith("/hub/static/"):
                asset = unquote(url.path.removeprefix("/hub/static/"))
                file = ROOT / asset if asset.startswith("extra-assets/") else HUB_DATA / "static" / asset
                if file.is_file():
                    route.fulfill(path=str(file))
                else:
                    failures.append(asset)
                    route.fulfill(status=404)
            elif route.request.is_navigation_request():
                route.fulfill(body="<!doctype html><title>Redirect destination</title>", content_type="text/html")
            else:
                # Local tests use fallback fonts and never contact external hosts.
                route.abort()

        context.route("**/*", route_request)
        page = context.new_page()
        page.on("pageerror", lambda error: errors.append(str(error)))
        try:
            yield page
            self.assertEqual(failures, [], "Missing local static assets")
            self.assertEqual(errors, [], "Uncaught browser JavaScript errors")
        finally:
            context.close()

    def test_theme_toggle_and_persistence_at_desktop_and_phone_widths(self):
        for width in (1440, 390, 320):
            for theme in ("light", "dark"):
                with self.subTest(width=width, theme=theme), self.page(render(), theme, width) as page:
                    page.goto("https://hub.invalid/hub/login", wait_until="networkidle")
                    expect(page.locator("html")).to_have_attribute("data-bs-theme", theme)
                    toggle = page.get_by_role("button", name="Toggle dark mode")
                    expect(toggle).to_be_visible()
                    self.assertEqual(page.locator("#dark-theme-toggle").count(), 1)
                    opposite = "dark" if theme == "light" else "light"
                    toggle.click()
                    expect(page.locator("html")).to_have_attribute("data-bs-theme", opposite)
                    self.assertEqual(page.evaluate("localStorage.getItem('jupyterhub-bs-theme')"), opposite)
                    page.reload(wait_until="networkidle")
                    expect(page.locator("html")).to_have_attribute("data-bs-theme", opposite)
                    page.emulate_media(color_scheme=theme)
                    expect(page.locator("html")).to_have_attribute("data-bs-theme", opposite)
                    toggle.focus()
                    toggle.press("Space")
                    expect(page.locator("html")).to_have_attribute("data-bs-theme", theme)
                    # The existing FAQ logo row overflows at 320px; keep that
                    # unrelated baseline issue separate from the header checks.
                    if width >= 390:
                        self.assertTrue(page.evaluate("document.documentElement.scrollWidth <= innerWidth"))
                    lockup = page.locator(".sym-lockup").bounding_box()
                    control = toggle.bounding_box()
                    self.assertLessEqual(lockup["x"] + lockup["width"], control["x"])
                    self.assertLessEqual(control["x"] + control["width"], width)
                    self.assertGreaterEqual(control["width"], 44)
                    self.assertGreaterEqual(control["height"], 44)
                    expect(page.locator("input[name=username]")).to_be_visible()
                    expect(page.locator("input[name=password]")).to_be_visible()
                    expect(page.locator("form")).to_have_attribute("method", "post")
                    expect(page.locator("form")).to_have_attribute("action", "/hub/login?next=%2Fhub%2F")
                    expect(page.locator("input[name=_xsrf]")).to_have_value("test-xsrf")

    def test_system_theme_changes_without_stored_preference(self):
        with self.page(render()) as page:
            page.goto("https://hub.invalid/hub/login", wait_until="networkidle")
            page.emulate_media(color_scheme="dark")
            expect(page.locator("html")).to_have_attribute("data-bs-theme", "dark")
            page.emulate_media(color_scheme="light")
            expect(page.locator("html")).to_have_attribute("data-bs-theme", "light")

    def test_render_variants_are_valid_and_run_without_script_errors(self):
        custom = deepcopy(CUSTOM)
        custom.update(announcements=["<p>Welcome!</p>"], learn_more="<b>Details</b>")
        custom["operated_by"]["custom_html"] = "<b>Operator</b>"
        for name, html in (
            ("password", render()),
            ("oauth", render(login_service="Example")),
            ("login-error", render(login_error="Invalid password")),
            ("custom-content", render(custom)),
        ):
            with self.subTest(name=name):
                self.assert_valid_html(html)
                with self.page(html) as page:
                    page.goto("https://hub.invalid/hub/login", wait_until="networkidle")
                    expect(page.get_by_role("button", name="Toggle dark mode")).to_be_visible()

    def assert_valid_html(self, html):
        parser = html5lib.HTMLParser(namespaceHTMLElements=False)
        doc = parser.parse(html)
        self.assertEqual(parser.errors, [])
        ids = Counter(el.attrib["id"] for el in doc.iter() if "id" in el.attrib)
        self.assertEqual([key for key, count in ids.items() if count > 1], [])
        return doc

    def test_redirects_keep_header_hidden_and_preserve_destinations(self):
        # Redirect-only hubs need no organization or footer configuration.
        html = render({"redirect_to": "https://landing.invalid/welcome"})
        doc = self.assert_valid_html(html)
        header = doc.find(".//header")
        self.assertIsNotNone(header)
        self.assertIn("hidden", header.attrib)
        self.assertEqual(len(doc.findall(".//*[@id='dark-theme-toggle']")), 1)
        for query, expected in (
            ("", "https://landing.invalid/welcome"),
            ("?next=%2Fhub%2F", "https://landing.invalid/welcome"),
            ("?next=%2Fuser%2Falice&extra=1", "https://hub.invalid/oauth_login?next=%2Fuser%2Falice&extra=1"),
        ):
            with self.subTest(query=query), self.page(html) as page:
                page.goto("https://hub.invalid/hub/login" + query)
                page.wait_for_url(expected)


if __name__ == "__main__":
    unittest.main()
