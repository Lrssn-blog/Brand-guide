# Brand Style Guide

A style guide for the Lrssn brand: its name, logo, colors, typography and voice.
It is for anyone who makes something that carries the brand, such as a website, a document, a slide deck or a repository.
The colors come from the [color palette](https://github.com/Lrssn-blog/Style-guide/blob/main/src/colors/Colors.md) of the [Lrssn style guides](https://github.com/Lrssn-blog/Style-guide), and the voice follows the writing rules of the [Markdown style guide](https://github.com/Lrssn-blog/Style-guide/blob/main/src/markdown/Markdown.md).

Items marked **TODO** are not decided yet.
Do not invent an answer for them, and replace the marker once the decision is made.

## Table of contents

[TOC]

## Principles

- **Be consistent.**
  The same name, colors and voice everywhere make the brand easy to recognize.
- **Have one source for each fact.**
  The palette lives in one file, and every other document links to it instead of copying it.
- **Be accessible.**
  A color or a style that a person cannot read is not on brand.
- **Keep it simple.**
  Use few colors and few fonts, and use them the same way each time.
- **Be plain and direct.**
  Say what you mean in short sentences.

When this guide does not cover something, choose the option that best serves these principles.

## Brand overview

**TODO**: Describe the brand in a few sentences.

| Item | Value |
| --- | --- |
| Name | Lrssn |
| Purpose | **TODO** |
| Audience | **TODO** |
| Personality | Plain, direct, precise |

## Name

The brand name is **Lrssn**.
**TODO**: Confirm the exact spelling and casing, and whether the name is ever written in all capitals or all lowercase.

- Write the name the same way every time, in running text and in titles.
- Do not translate, abbreviate or add a suffix to the name.
- Do not turn the name into a verb or a plural.
- Do not break the name over two lines.

## Logo

**TODO**: There is no logo yet.
Add the files to an `images` folder next to this guide, with lowercase names and hyphens between words, for example `images/logo-primary.svg`.

### Variants

**TODO**: Define each variant and when to use it.

- Primary logo
- Logo on a dark background
- Single color logo
- Icon, for small sizes

Prefer SVG, and use PNG only where SVG is not supported.

### Clear space and minimum size

**TODO**: Define the clear space around the logo as a fraction of its height, and the smallest size at which it stays legible.

Until then, keep clear space around the logo that is at least as large as the logo's lettering is tall.

### Misuse

Do not:

- Change the colors of the logo to colors outside the [palette](#colors).
- Stretch, squash, rotate or skew the logo.
- Add shadows, outlines or effects to the logo.
- Place the logo on a background that makes it hard to read.
- Redraw the logo or rearrange its parts.

## Colors

The palette has two brand colors, five neutrals and four status colors.
The palette is defined in [Colors.md](https://github.com/Lrssn-blog/Style-guide/blob/main/src/colors/Colors.md), and that file is the source of truth.
If the two differ, `Colors.md` is right, and this guide must be updated.

### Palette

| Name | Role | HEX | RGB | HSV |
| --- | --- | --- | --- | --- |
| Orange | Primary | `#D96C36` | 217, 108, 54 | 20, 75, 85 |
| Turquoise | Secondary | `#36D9CB` | 54, 217, 203 | 175, 75, 85 |
| Black | Neutral | `#000000` | 0, 0, 0 | 215, 100, 0 |
| Dark grey | Neutral | `#242A33` | 36, 42, 51 | 215, 30, 20 |
| Grey | Neutral | `#525A66` | 82, 90, 102 | 215, 20, 40 |
| Light grey | Neutral | `#DAE4F2` | 218, 228, 242 | 215, 10, 95 |
| White | Neutral | `#FFFFFF` | 255, 255, 255 | 215, 0, 100 |
| Green | Success | `#36D951` | 54, 217, 81 | 130, 75, 85 |
| Yellow | Warning | `#D9D936` | 217, 217, 54 | 60, 75, 85 |
| Red | Danger | `#D93636` | 217, 54, 54 | 0, 75, 85 |
| Blue | Information (neutral) | `#366CD9` | 54, 108, 217 | 220, 75, 85 |

HSV is written as hue in degrees, then saturation and value in percent.

### Using the colors

- Use **orange** as the main accent: links, buttons, highlights and the logo.
- Use **turquoise** as the second accent, to support orange and never to compete with it.
  Use it most on dark backgrounds.
- Use the **neutrals** for text, backgrounds, borders and surfaces.
  Most of any layout should be neutral.
- Use **green**, **yellow**, **red** and **blue** only for status, such as success, warning, danger and information.
  Do not use them as decoration.
- Do not add colors that are not in the palette.
  Do not use tints or shades of palette colors, except to show a hover or a disabled state.
- Never use color as the only way to show something.
  Add text, an icon or a shape.

### Contrast

Text must have enough contrast against its background.
The ratios below are calculated with the [WCAG 2.2 contrast formula](https://www.w3.org/TR/WCAG22/#contrast-minimum).
Body text needs a ratio of at least 4.5, and large text needs at least 3.
Large text is 24 px or more, or 19 px or more in bold.

| Text color | On white | On light grey | On dark grey | On black |
| --- | --- | --- | --- | --- |
| Black | 21.00 | 16.36 | 1.45 | 1.00 |
| Dark grey | 14.44 | 11.25 | 1.00 | 1.45 |
| Grey | 6.97 | 5.43 | 2.07 | 3.01 |
| Light grey | 1.28 | 1.00 | 11.25 | 16.36 |
| White | 1.00 | 1.28 | 14.44 | 21.00 |
| Orange | 3.42 | 2.66 | 4.23 | 6.15 |
| Turquoise | 1.76 | 1.37 | 8.21 | 11.94 |
| Green | 1.87 | 1.46 | 7.70 | 11.20 |
| Yellow | 1.51 | 1.17 | 9.58 | 13.93 |
| Red | 4.63 | 3.61 | 3.12 | 4.53 |
| Blue | 4.88 | 3.80 | 2.96 | 4.30 |

The pairs that follow from the table:

- **Body text**: dark grey, black or grey on white or light grey.
  Light grey or white on dark grey or black.
  Turquoise, green or yellow on dark grey or black.
  Orange on black.
  Red or blue on white.
- **Large text only**: orange on white or dark grey.
  Red or blue on light grey.
  Red on dark grey.
- **Never for text**: turquoise, green or yellow on white or light grey.
  Orange on light grey.

For text on an orange background, use black.
White on orange has a ratio of 3.42, so use it only for large text.

## Typography

**TODO**: Choose the typefaces.
Use one family for text and one monospace family for code, and set them in this table.

| Use | Typeface |
| --- | --- |
| Headings | **TODO** |
| Body text | **TODO** |
| Code | **TODO** |

The [LaTeX style guide](https://github.com/Lrssn-blog/Style-guide/blob/main/src/latex/Latex.md) loads fonts through `fontspec`, so any typeface that is chosen here should be available as a system font.

### Hierarchy

- Use at most three heading levels in one piece of content.
- Make each level clearly different from the next in size or weight.
- Use sentence case for headings, as in the [Markdown style guide](https://github.com/Lrssn-blog/Style-guide/blob/main/src/markdown/Markdown.md#heading-text).
- Use bold for emphasis, and italics for gentle stress.
  Do not underline text that is not a link.
- Do not set long passages in capitals.

### Size and spacing

- Set body text at 16 px or the print equivalent of 11 pt, or larger.
- Use a line height of 1.5 times the font size for body text, and 1.2 to 1.3 times for headings.
- Keep a line of text to about 60 to 80 characters.
- Align text to the left.
  Do not justify text on screen.

## Voice and tone

The brand sounds like the style guides: plain, direct and precise.
It explains what to do, and it does not sell.

- Write for a reader who is new to the topic.
- Use the second person ("you") and the present tense.
- Use the active voice.
- Keep sentences short, and put the most important information first.
- Use "must", "should" and "may" in the same way as the [Markdown style guide](https://github.com/Lrssn-blog/Style-guide/blob/main/src/markdown/Markdown.md#writing-style).
- Do not use hype, filler or exclamation marks.
- Do not use jargon without explaining it the first time.

```text
Good: Run the checks before you open a pull request.

Bad: It is highly recommended that all checks be run prior to the
     submission of a pull request!
```

The tone changes with the situation, but the voice does not.

| Situation | Tone |
| --- | --- |
| Documentation | Neutral and exact |
| Errors and warnings | Calm, and say how to fix it |
| Announcements | Warm and brief |
| Community and conduct | Respectful and clear |

**TODO**: Add the words and phrases the brand uses and avoids, and the language or languages the brand writes in.

## Anti-patterns

| Anti-pattern | Instead |
| --- | --- |
| Writing the name in different ways | Use the spelling in [Name](#name) every time. |
| Recoloring the logo to match a design | Use a variant that fits the background. |
| A color that is close to a palette color | Use the exact HEX value from the [palette](#palette). |
| Orange or turquoise text on a light background | Check the [contrast](#contrast), and use a neutral. |
| Status colors used as decoration | Use orange, turquoise or a neutral. |
| Showing an error or a success with color only | Add text or an icon. |
| Copying the palette into other documents | Link to [Colors.md](https://github.com/Lrssn-blog/Style-guide/blob/main/src/colors/Colors.md). |
| Hype and exclamation marks in text | Say what it does, in plain words. |

## See also

- [Lrssn style guides](https://github.com/Lrssn-blog/Style-guide)
- [Color palette](https://github.com/Lrssn-blog/Style-guide/blob/main/src/colors/Colors.md)
- [Markdown style guide](https://github.com/Lrssn-blog/Style-guide/blob/main/src/markdown/Markdown.md)
- [LaTeX style guide](https://github.com/Lrssn-blog/Style-guide/blob/main/src/latex/Latex.md)
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
