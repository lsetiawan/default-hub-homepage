---
name: Schmidt Observatory System Science Symposium JupyterHub
description: The symposium hub's sign-in page, set as a page of the event's own website, with a dark theme taken from that site's footer.
colors:
  paper: "#ffffff"
  paper-band: "#f5f6f8"
  ink: "#15191e"
  ink-soft: "#434b53"
  muted: "#5f6870"
  rule: "#e4e7ea"
  hairline: "#eef0f2"
  signal-teal: "#0a8f93"
  teal-ink: "#087c80"
  error: "#b42318"
  error-bg: "#fdf1f0"
  error-rule: "#f2c9c4"
  night-footer: "#0e1216"
  footer-text: "#aab3bb"
  footer-link: "#d5dbe0"
  footer-small: "#8e979f"
  dark-page: "#12171c"
  dark-band: "#0e1216"
  dark-surface: "#171d23"
  dark-ink: "#eef1f3"
  dark-ink-soft: "#b9c1c8"
  dark-muted: "#949da5"
  dark-rule: "rgba(255, 255, 255, 0.13)"
  dark-hairline: "rgba(255, 255, 255, 0.08)"
  dark-signal-teal: "#0fb5b5"
  dark-teal-ink: "#3cc6c6"
  dark-error: "#ffb4ab"
  dark-footer: "#0a0d10"
  dark-logo-plate: "#dfe3e7"
typography:
  display:
    fontFamily: "Newsreader, Iowan Old Style, Georgia, serif"
    fontSize: "clamp(2.2rem, 3.7vw, 3.3rem)"
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: "-0.01em"
  headline:
    fontFamily: "Newsreader, Iowan Old Style, Georgia, serif"
    fontSize: "clamp(1.9rem, 3.4vw, 2.7rem)"
    fontWeight: 400
    lineHeight: 1.12
    letterSpacing: "-0.01em"
  title:
    fontFamily: "Newsreader, Iowan Old Style, Georgia, serif"
    fontSize: "1.75rem"
    fontWeight: 500
    lineHeight: 1.12
    letterSpacing: "-0.01em"
  body:
    fontFamily: "Hanken Grotesk, -apple-system, Segoe UI, sans-serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.62
  ui:
    fontFamily: "Hanken Grotesk, -apple-system, Segoe UI, sans-serif"
    fontSize: "0.96rem"
    fontWeight: 600
    lineHeight: 1.4
  label:
    fontFamily: "Hanken Grotesk, -apple-system, Segoe UI, sans-serif"
    fontSize: "0.72rem"
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: "0.14em"
rounded:
  sm: "3px"
  md: "6px"
spacing:
  gutter-mobile: "20px"
  gutter: "28px"
  stack: "18px"
  card: "34px"
  section: "92px"
  container: "1140px"
components:
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    typography: "{typography.ui}"
    rounded: "{rounded.md}"
    padding: "13px 24px"
    width: "100%"
  button-primary-hover:
    backgroundColor: "{colors.teal-ink}"
    textColor: "{colors.paper}"
  button-primary-dark:
    backgroundColor: "{colors.dark-ink}"
    textColor: "{colors.ink}"
  button-primary-dark-hover:
    backgroundColor: "{colors.dark-signal-teal}"
    textColor: "{colors.ink}"
  input-text:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "12px 14px"
    width: "100%"
  card-signin:
    backgroundColor: "{colors.paper}"
    rounded: "{rounded.md}"
    padding: "34px 34px 30px"
    width: "420px"
  info-list:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink-soft}"
    rounded: "{rounded.md}"
    padding: "24px 28px"
  logo-plate:
    backgroundColor: "{colors.paper}"
    rounded: "{rounded.md}"
    height: "64px"
    padding: "0 18px"
  logo-plate-dark:
    backgroundColor: "{colors.dark-logo-plate}"
  alert-error:
    backgroundColor: "{colors.error-bg}"
    textColor: "{colors.error}"
    rounded: "{rounded.md}"
    padding: "10px 14px"
---

# Design System: Schmidt Observatory System Science Symposium JupyterHub

## Overview

**Creative North Star: "The Symposium's Own Page"**

The hub does not look like a hosted service with an event logo pasted on. It reads as one more page of https://symposium.schmidtobservatorysystem.org/: the same editorial serif for display, the same quiet grotesk for everything functional, white ground with pale grey bands, 1px hairlines, near-black controls and teal reserved for links, focus and one moving point. Density is low and calm; the sign-in form is the only thing that asks for action.

Depth comes from rules and tonal bands rather than shadows. The one decorative signature is astronomical and drawn in the same hairline as everything else: two concentric orbit rings centred on the sign-in card, with a single teal dot travelling the inner ring. The dark theme is not an inversion. The event site's footer palette becomes the page, so night mode stays in the same family of blue-black inks.

The build follows the event website, which is the pinned direction for this hub.

**Key Characteristics:**
- Newsreader display over Hanken Grotesk body and UI; the serif carries the headings, the grotesk carries the work.
- White and #f5f6f8 bands separated by 1px hairlines, with 6px corners throughout.
- Near-black primary buttons that turn teal on hover.
- Teal in two strengths: a darker ink teal for text, a brighter signal teal for accents and focus.
- Hairline orbit rings with one teal dot as the signature.
- Full light and dark themes, switched by JupyterHub's `data-bs-theme`.

## Colors

A cool, near-monochrome palette of blue-black inks and pale greys, with a single teal accent used in two strengths.

### Primary
- **Ink Teal** (teal-ink): all running-text links, the roman "JupyterHub" accent in the hero title, and the light-theme button hover. It exists because the event site's teal is only 3.9:1 on white; this one is 5.1:1. In dark theme it lifts to dark-teal-ink.
- **Signal Teal** (signal-teal): the event site's own teal, kept for non-text accents only: focus outlines, the input focus border and its 16% halo, text selection, the caret, the orbit dot and the faint 7% radial wash at the top right of the hero. In dark theme it becomes dark-signal-teal, which is also the dark button hover.

### Neutral
- **Paper** (paper): page ground, card and info-list surface, input fill, logo plates in light theme.
- **Paper Band** (paper-band): the alternate band under the hero (the "About this hub" section) and announcement boxes.
- **Ink** (ink): headings, labels, body copy in the hero, and the primary button fill in light theme.
- **Soft Ink** (ink-soft): long-form answers in the info list and the terms line.
- **Muted** (muted): the tracked nav lockup text.
- **Rule** (rule): card, input, info-list and logo-plate borders; the nav lockup divider; the inner orbit ring.
- **Hairline** (hairline): the lightest separator: nav bottom border, band top border, rows inside the info list, the outer orbit ring.
- **Night Footer** (night-footer): the footer in light theme, with footer-text for body, footer-link for links (white on hover) and footer-small for the infrastructure line.

### Dark theme
- **Dark Page / Band / Footer** (dark-page, dark-band, dark-footer): three stepped blue-blacks, page lightest, footer darkest. The band below the hero is darker than the page, matching the light theme's pattern of the band being a step off the ground.
- **Dark Surface** (dark-surface): card and info-list surface, one step lighter than the page.
- **Dark Inks** (dark-ink, dark-ink-soft, dark-muted): the text ramp. dark-ink is also the primary button fill, with ink as its label.
- **Dark Rule / Hairline** (dark-rule, dark-hairline): translucent white at 13% and 8%.
- **Logo Plate** (dark-logo-plate): a pale grey plate behind the Jupyter and RStudio marks, whose artwork is built for light grounds. Plates lose their border in dark theme.

### Error
- **Error** (error, error-bg, error-rule): the sign-in error box, a red ink on a pale red field with a pale red rule. Dark theme uses dark-error on an 18% red field.

### Named Rules
**The Two Teals Rule.** Text that is teal uses teal-ink; signal-teal never sets text on paper. Signal teal is for outlines, borders, dots and washes.

**The Footer Becomes the Page Rule.** Dark theme colours come from the footer's blue-black family, never from a neutral grey or pure black.

## Typography

**Display Font:** Newsreader (with Iowan Old Style, Georgia, serif), weights 400 and 500, optical sizing 6 to 72
**Body Font:** Hanken Grotesk (with -apple-system, Segoe UI, sans-serif), weights 400 to 700

**Character:** A literary, slightly condensed serif for anything that names a place or a thing, paired with a clean, open grotesk that does all the work of forms, labels and answers.

### Hierarchy
- **Display** (400, clamp 2.2 to 3.3rem, 1.08): the hero title only, max 17ch, balanced wrap. The second line, "JupyterHub", is set on its own line in roman teal-ink, not italic.
- **Headline** (400, clamp 1.9 to 2.7rem, 1.12): section headings such as the welcome line, max 24ch, balanced wrap.
- **Title** (500, 1.75rem, 1.12): the "Sign in" heading inside the card.
- **Body** (400, 17px, 1.62): page copy. Info-list answers cap at 68ch.
- **UI** (600, 0.96rem): button labels; input text uses the same size at 400. Field labels are 600 at 0.86rem. The date and place line is 500 at 0.96rem, with the date at 700 and a rule-coloured slash between.
- **Label** (600 to 700, 0.72rem, 0.14 to 0.16em, uppercase): only three places: the "Science Symposium" nav lockup, the footer credit labels (Operated by, Funded by, Designed by) and the footer co-brand line ("An initiative of", 400, muted).

### Named Rules
**The Serif Names, Sans Works Rule.** Newsreader is for headings. Everything a person reads to act on (labels, buttons, answers, errors) is Hanken Grotesk.

**The Tracked Caps Stay Put Rule.** Tracked uppercase appears only in the nav lockup and the footer credit labels. It never sits above a heading.

## Layout

A single centred container (1140px max) with 28px side gutters, 20px at 640px and below. The hero is a two-column grid (1.1fr / 0.9fr, 64px gap, vertically centred): title block on the left, sign-in card on the right, so the form sits in the first viewport on desktop. At 900px and below the grid stacks to one column (40px gap) and the form follows the title.

Vertical rhythm is generous and set by section: hero 72px top and 88px bottom (48 / 64 at 900px), the about band 92px (64px at 760px), footer 60px top and 32px bottom. Inside components, form fields stack at 18px. The info list is a definition list in a bordered panel, with a 240px question column and 28px gap, collapsing to one column at 760px. The footer pairs a brand column with a three-column credits grid (two columns at 480px, single column stack at 760px for the top row).

The nav is sticky, 68px high, translucent (86% of the page colour) with a saturate-and-blur backdrop and a hairline bottom border.

## Elevation & Depth

Mostly flat. Depth is carried by tonal bands (paper, paper-band, night footer), 1px rules and the translucent sticky nav. The sign-in card is the only raised surface, with one long, soft, ambient shadow that reads as lift, not as an outline.

### Shadow Vocabulary
- **Card lift** (`box-shadow: 0 24px 60px -36px rgba(20, 30, 45, 0.35)`): the sign-in card only.
- **Focus halo** (`box-shadow: 0 0 0 3px` signal-teal at 16%): text inputs on focus.

### Named Rules
**The One Raised Card Rule.** Only the primary task surface gets a shadow. Every other container is defined by its rule and its band.

## Shapes

Gentle, consistent corners: 6px on cards, inputs, buttons, alerts, announcement boxes, the info panel and logo plates; 3px only on focus outlines. Borders are always 1px. The one curved form is the circle: the orbit rings and the 8px orbit dot.

## Components

### Buttons
Quiet and solid; the only filled control on the page.
- **Shape:** gently rounded (6px), full width of the card.
- **Primary:** ink fill, paper label, Hanken Grotesk 600 at 0.96rem, 13px by 24px padding, 1px transparent border.
- **Hover / Focus:** fill turns teal-ink (dark: dark-signal-teal with ink label) over 0.22s on the system ease (`cubic-bezier(0.22, 0.61, 0.36, 1)`); active nudges down 1px; focus-visible gets the 2px signal-teal outline at 3px offset.
- **Disabled:** 55% opacity with a progress cursor while the sign-in submits.

### Cards / Containers
- **Sign-in card:** surface fill, 1px rule border, 6px corners, card-lift shadow, 34px padding (26px by 22px at 640px), max 420px wide.
- **Info list:** surface fill, 1px rule border, 6px corners, rows divided by hairlines, question in ink 600, answer in soft ink.
- **Sign-in hints:** below the button, after a hairline and 16px of space: 0.86rem soft-ink notes, 10px apart. The first explains the username and password; the second is the AI logging notice, whose "How interactions are handled" link never wraps and jumps to the AI interactions section (scroll-margin clears the sticky nav).
- **Announcement box:** paper-band fill, rule border, 6px corners, 16px by 20px padding, max 52ch.

### Inputs / Fields
- **Style:** page-colour fill, 1px rule border, 6px corners, 12px by 14px padding, labels above in ink 600 at 0.86rem.
- **Hover:** border darkens toward ink (30% mix).
- **Focus:** border becomes signal-teal with the 3px 16% teal halo; no outline.
- **Error:** an error box above the fields (error ink, error-bg field, error-rule border, 0.9rem 500, left-aligned).

### Links
- **Body links:** teal-ink with a 1px underline at 40% of the text colour, 3px offset; on hover the link turns ink and the underline goes solid.
- **Display links:** the acknowledgment names (Newsreader 500, 1.2rem) stay ink with a 25% currentColor underline, which turns signal-teal on hover and focus. The hero title's org-name link has no underline.
- **Footer links:** footer-link with a 35% underline, white on hover.

### Navigation
A sticky translucent bar holding one lockup: the org logo (42px high, 34px at widths up to 380px), a 1px by 26px rule divider, and "Science Symposium" in tracked uppercase muted text over two lines, which turns ink on hover. In dark theme every org logo swaps to the white version. JupyterHub's native theme control sits at the right with a 44px touch target and the existing focus outline. The header is rendered through the `nav_bar` block and hidden on redirect pages, retaining the control in the DOM for the upstream theme script.

### Logo plates
Jupyter and RStudio marks sit on 64px-high plates with 18px side padding, 1px rule border and 6px corners; the border turns ink on hover. In dark theme the plate is dark-logo-plate with no border.

### Split sections
The AI interactions notice and Acknowledgments sit on the page ground after the FAQ band, each with a hairline top rule and 72px by 80px vertical padding (56px by 64px at 560px). They share one grid, the FAQ's: a 240px heading column (Newsreader 400, 1.5 to 1.85rem) and a content column, 56px apart, stacked at 900px and below.
- **AI notice:** a soft-ink paragraph at 68ch, then the three promises as rule-divided rows, each led by a 600 ink phrase.
- **Acknowledgments:** a 2 by 2 list (one column at 560px) of organization names as display links, each over its parent organization in 0.9rem soft ink, every entry under a 1px rule. The heading drops 14px to line up with the first names. Text only, no logos.

### Footer co-brand
Under the footer logo, 20px down: "An initiative of" in the label style (muted, 0.14em tracking) beside the white Schmidt Sciences logo at 26px, linked to schmidtsciences.org, wrapping on narrow screens. Copied from the event site's own footer.

### Orbit rings (signature)
Two hairline circles centred on the sign-in card and behind it: outer 860px in hairline, inner 540px in rule. One 8px signal-teal dot rides the inner ring on a 60s linear loop, parked at -90deg (mid-left, clear of the card) so it is visible on the first frame. Under reduced motion the loop stops at that parked position. At 900px and below the rings shrink to 640px and 460px, the animation stops and the dot is hidden so it never crosses the stacked title. The rings are decorative (`aria-hidden`) and never take pointer events.

## Do's and Don'ts

### Do:
- **Do** set text links in teal-ink (5.1:1 on paper) and keep signal-teal for focus, borders, the orbit dot and washes.
- **Do** use ink-filled buttons that turn teal-ink on hover in light theme and dark-signal-teal in dark theme.
- **Do** separate sections with tonal bands and 1px hairlines, and keep corners at 6px.
- **Do** set headings in Newsreader 400 or 500 and everything functional in Hanken Grotesk.
- **Do** define every colour for both themes; dark theme uses the footer's blue-blacks (dark-page, dark-band, dark-footer) and puts third-party logos on dark-logo-plate.
- **Do** keep the orbit dot still under reduced motion and hidden once the layout stacks.

### Don't:
- **Don't** put kicker or eyebrow labels above headings; tracked uppercase lives only in the nav lockup and the footer credit labels.
- **Don't** set the hero accent "JupyterHub" in italic; it is roman teal-ink.
- **Don't** set text in signal-teal on a light ground, and don't use it as a button fill behind white text (3.9:1).
- **Don't** add shadows to containers other than the sign-in card.
- **Don't** add a Schmidt Sciences co-brand line ("An initiative of") to the footer.
