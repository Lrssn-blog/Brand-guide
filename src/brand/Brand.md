# Brand Style Guide

A style guide for the Lrssn brand: its name, logo, colours, type and voice.
It is for anyone who makes something that carries the brand, such as a web page, a document, a slide or a repository.
It is a written copy of the public [Brand guide](https://lrssn.com/brand) of the Lrssn website, and the colours and typefaces come from the website's [design tokens](https://gitea.lrssn.se/Lrssn/Lrssn-com/src/branch/main/src/styles/_variables.scss).

Items marked **TODO** are not decided yet.
Do not invent an answer for them, and replace the marker once the decision is made.

## Table of contents

[TOC]

## Principles

- **Be consistent.**
  The same name, colours and voice everywhere make the brand easy to recognise.
- **Have one source for each fact.**
  The colours and typefaces are defined in the website's stylesheet, and this guide is checked against it.
- **Be accessible.**
  A colour or a style that a person cannot read is not on brand.
- **Put whitespace first.**
  Separate things with space before a border, and with a border before a shadow.
- **Show one loud thing per view.**
  The brand orange is a fill at most once per screen.
  A thin rule or an underline in orange does not count as a fill.
- **Let type do the work.**
  Use Inter for the interface, Merriweather for reading and Playfair Display for the brand, with real contrast in size between headings and text.
- **Let structure show.**
  Hairline rules, a margin for metadata and a faint dot grid are fine when they organise the content.
- **Leave out decoration.**
  Do not use gradients, decorative icons or emoji.
  An icon that carries meaning is fine.

When this guide does not cover something, choose the option that best serves these principles.

## Brand overview

| Item | Value |
| --- | --- |
| Name | Lrssn |
| Website | [lrssn.com](https://lrssn.com) |
| Personality | An engineer's notebook: curious, exact and plain-spoken |
| Purpose | **TODO** |
| Audience | **TODO** |

## Name

The brand name is **Lrssn**: a capital L, and the rest lowercase.
The username is **Erik Larsson**.

- Show the name and the username through the logo, and never retype them in another typeface.
- Write the name the same way every time, in running text and in titles.
  Do not write it in all capitals or in all lowercase.
- Do not translate, abbreviate or add a suffix to the name.
- Do not turn the name into a verb or a plural.
- Do not break the name over two lines.

## Logo

The mark is a single unbroken line inside a square frame, drawn as a stroke with round ends.
Beside it, the name is set in Playfair Display Bold.
Mark and name always share one colour.

### Variants

| Variant | Use |
| --- | --- |
| Mark and name | The default, as in the header and footer. |
| Mark, name and username | The header, with the username beneath the name. |
| Name below | Square spaces, such as a profile card or a slide. |
| Mark only | Small spaces: the favicon, avatars and app icons. |

### Clear space and minimum size

Keep a quarter of the mark's height clear on every side.
Nothing else goes in that space.

The mark alone must be at least 16 px tall, or 6 mm in print.
The mark with the name must be at least 24 px tall.

### Misuse

Do not:

- Stretch or squash the logo.
- Rotate the logo.
- Draw the logo in another colour.
- Retype the name in another typeface.
- Add shadows, outlines or gradients.

### Files

The logo is available as a mark on a transparent background, as SVG for screens and print, or as a 1024 px PNG.
Download the files from the [Brand guide](https://lrssn.com/brand).
They are named `lrssn-logo-<colour>.<format>`, for example `lrssn-logo-orange.svg`.

| Colour | Token | Use |
| --- | --- | --- |
| Orange | `primary-color` | The default, on light or dark backgrounds. |
| Dark | `text-color` in the light theme | One colour on light backgrounds. |
| Light | `text-color` in the dark theme | One colour on dark backgrounds. |

## Colours

Every colour comes in a light theme and a dark theme.
The brand orange is the same in both.
The secondary colour is tropical teal in the light theme and forest green in the dark theme.

The values below are copied from the website's [design tokens](https://gitea.lrssn.se/Lrssn/Lrssn-com/src/branch/main/src/styles/_variables.scss), and a check in this repository fails if they differ.

### Brand colours

| Token | Light | Dark | Use |
| --- | --- | --- | --- |
| `primary-color` | `#fc6600` | `#fc6600` | Brand orange: the logo, buttons, fills and borders. Not for text. |
| `primary-text` | `#b04600` | `#ff8a3d` | Orange text and links. |
| `primary-soft` | `#ffe8d6` | `#3a1f0e` | Apricot tint for selection and quiet highlights. |
| `secondary-color` | `#00999a` | `#3e8a58` | The cool accent: fills, borders and bars only. |
| `secondary-text` | `#00737a` | `#7fc495` | Text in the secondary colour. |
| `secondary-soft` | `#d4f2ef` | `#14261b` | Tint behind secondary text. |

### Neutrals

| Token | Light | Dark | Use |
| --- | --- | --- | --- |
| `background` | `#f6f7f9` | `#0f1216` | The page. |
| `surface` | `#ffffff` | `#161a20` | Cards, panels and inputs. |
| `border-color` | `#dde2e8` | `#262c34` | Borders and dividers. |
| `text-color` | `#14171c` | `#edf0f4` | Headings and strong text. |
| `text-muted` | `#56606c` | `#9ea7b2` | Secondary text. |
| `text-on-primary` | `#14171c` | `#14171c` | Text on an orange fill. Never white. |

### Status colours

| Token | Light | Dark | Use |
| --- | --- | --- | --- |
| `success-color` | `#2e6b3a` | `#7cc68a` | Success. |
| `danger-color` | `#b3261e` | `#f2867e` | Errors and danger. |

### Using the colours

- Use orange text in `primary-text`, never in `primary-color`.
  The brand orange is too light for text on a light background.
- Use `text-on-primary` for text on an orange fill, and never white.
- Use `primary-color` as a fill at most once per screen.
- Keep the neutrals cool, towards blue-grey.
  Do not use warm or beige greys, because they make the brand read as brown.
- Always write the status in words, as well as showing it in a colour.
- Do not add colours that are not in this guide.

### Themes

- The website has three settings: **System**, which is the default and follows the device, **Light** and **Dark**.
- Check every new screen in both themes.
- Paper is light whatever the theme, so print uses the light values.

### Contrast

Text must have enough contrast against its background.
The ratios below are calculated with the [WCAG 2.2 contrast formula](https://www.w3.org/TR/WCAG22/#contrast-minimum).
Body text needs a ratio of at least 4.5, and large text and graphics need at least 3.
Large text is 24 px or more, or 19 px or more in bold.

| Token | Light page | Light surface | Dark page | Dark surface |
| --- | --- | --- | --- | --- |
| `text-color` | 16.76 | 17.96 | 16.43 | 15.27 |
| `text-muted` | 5.96 | 6.39 | 7.71 | 7.17 |
| `primary-text` | 5.26 | 5.64 | 8.01 | 7.45 |
| `secondary-text` | 5.25 | 5.63 | 9.15 | 8.51 |
| `success-color` | 5.97 | 6.40 | 9.21 | 8.57 |
| `danger-color` | 6.10 | 6.54 | 7.59 | 7.06 |
| `primary-color` | 2.78 | 2.98 | 6.29 | 5.85 |
| `secondary-color` | 3.25 | 3.49 | 4.45 | 4.14 |

Every text token reaches 4.5 on the page and on the surface, in both themes.
`primary-color` and `secondary-color` do not, so they are for fills, borders and bars, and never for text.

The same ratios for text on a tint or a fill:

| Pair | Light | Dark |
| --- | --- | --- |
| `text-on-primary` on `primary-color` | 6.02 | 6.02 |
| `primary-text` on `primary-soft` | 4.77 | 6.48 |
| `secondary-text` on `secondary-soft` | 4.75 | 7.74 |

## Typography

Four typefaces, each with one job.

| Token | Typeface | Used for |
| --- | --- | --- |
| `font-display` | Playfair Display | The logo, and brand moments such as hero lines, section titles and taglines. |
| `font-ui` | Inter | Headings, navigation, buttons, labels, tags and forms. |
| `font-serif` | Merriweather | Running text, such as articles, posts and descriptions. |
| `font-mono` | Geist Mono | Code, and small metadata such as dates and counts. |

Each typeface has a generic fallback: `serif` for Playfair Display and Merriweather, `sans-serif` for Inter and `monospace` for Geist Mono.

### Type scale

| Token | Size | Used for |
| --- | --- | --- |
| `font-size-xs` | `0.75rem` | Mono metadata and labels |
| `font-size-sm` | `0.875rem` | Small interface text and captions |
| `font-size-base` | `1rem` | Interface text |
| `font-size-lg` | `1.125rem` | Running text and ledes |
| `font-size-xl` | `1.25rem` | Level 3 headings |
| `font-size-2xl` | `1.6rem` | Level 2 headings |
| `font-size-3xl` | `clamp(2rem, 4.5vw, 3rem)` | Level 1 headings |
| `font-size-display` | `clamp(2.5rem, 6.5vw, 5.25rem)` | Playfair Display hero lines |

### Line height and measure

- Use a line height of 1.15 for headings, 1.55 for interface text and 1.8 for running text.
- Keep running text to about 65 characters wide.
- Write headings in sentence case.

## Voice

The brand sounds like an engineer's notebook: curious, exact and plain-spoken.
Each rule below has a line to write and a line to avoid.

### Plain and direct

Say what a thing is or does, in the fewest everyday words.
Lead with the point.

- **Write**: Upload the PDF here. Readers download it from the Brand guide.
- **Not**: Seamlessly empower your readers with downloadable brand resources.

### One person, writing

The site is one engineer's notebook.
Write as "I", to "you", and never as a company "we".

- **Write**: I wrote this after the third time the build broke.
- **Not**: At Lrssn, we are passionate about reliable builds.

### Show the working

Name the trade-off and what went wrong, not just the result.
Numbers beat adjectives.

- **Write**: It cut the build from 4 minutes to 50 seconds, at the cost of a bigger image.
- **Not**: It made the build blazingly fast.

### Calm, without hype

Do not use exclamation marks, emoji or superlatives.
Keep confirmations short and factual.

- **Write**: Brand guide updated.
- **Not**: Awesome!! Your brand guide is live!

### British English, sentence case

Use British spelling: colour, licence, organise.
Write headings, buttons and labels in sentence case.
Use capitals only for names and for the site's own terms, such as Post, Article and Series.

- **Write**: Save site owner
- **Not**: Save Site Owner Settings

### Words before icons and colour

Give every icon a label, and write every status colour in words.
A link says where it goes.

- **Write**: Download the CV (PDF, 120 KB)
- **Not**: Click here

## Anti-patterns

| Anti-pattern | Instead |
| --- | --- |
| Writing the name as LRSSN or lrssn | Write Lrssn, with a capital L and the rest lowercase. |
| Retyping the name in another typeface | Use the logo. |
| Drawing the logo in another colour | Use the orange, dark or light logo file. |
| Orange text in `primary-color` | Use `primary-text`. |
| White text on an orange fill | Use `text-on-primary`. |
| More than one orange fill on a screen | Keep one fill, and use a thin rule or an underline for the rest. |
| Warm or beige greys | Use the cool, blue-grey neutrals. |
| A status shown by colour alone | Add words. |
| A gradient, a decorative icon or an emoji | Let type and space do the work. |
| Hype, exclamation marks and "we" | Write plainly, as one person. |

## See also

- [Brand guide on lrssn.com](https://lrssn.com/brand)
- [Design system of the website](https://gitea.lrssn.se/Lrssn/Lrssn-com/src/branch/staging/DESIGN_SYSTEM.md)
- [Design tokens of the website](https://gitea.lrssn.se/Lrssn/Lrssn-com/src/branch/main/src/styles/_variables.scss)
- [Lrssn style guides](https://github.com/Lrssn-blog/Style-guide)
- [Markdown style guide](https://github.com/Lrssn-blog/Style-guide/blob/main/src/markdown/Markdown.md)
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
