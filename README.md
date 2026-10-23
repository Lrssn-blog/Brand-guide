# Brand-guide

This repo holds the Lrssn brand guide.
It is a companion to the [Lrssn style guides](https://github.com/Lrssn-blog/Style-guide).
The [Lrssn design system](https://github.com/Lrssn-blog/Design-system) turns this guide and the colour themes into tokens and components that a page can use.

## [Brand](./src/brand/Brand.md)

A guide for the Lrssn brand: name, logo, colours, typography, and voice and tone.
It is a written copy of the public [Brand guide](https://lrssn.com/brand) of the Lrssn website, and the colours come from the [Lrssn colour themes](https://github.com/Lrssn-blog/Color-theme): Lrssn Shore, which is light, and Lrssn Hearth, which is dark.
Items that are not decided yet are marked **TODO**.

## Checks

Pull requests run these checks via GitHub Actions:

- [markdownlint](https://github.com/DavidAnson/markdownlint-cli2) on the Markdown files.
- [Ruff](https://docs.astral.sh/ruff/) and [mypy](https://mypy-lang.org/) on the scripts.
- A palette check that compares the colours and contrast ratios in the guide with the website's tokens in the [Lrssn colour themes](https://github.com/Lrssn-blog/Color-theme/blob/main/website/_theme.scss).
- A link check with [lychee](https://github.com/lycheeverse/lychee).

To run them locally:

```bash
npx markdownlint-cli2
ruff check && ruff format --check
mypy scripts
scripts/palette.py
lychee --config .lychee.toml '**/*.md'
```

The palette check fetches `website/_theme.scss` from the `main` branch of the Color-theme repository.
Pass the path of a local copy to use that instead, for example `scripts/palette.py ../Color-theme/website/_theme.scss`.

## Licence

Copyright (C) 2026 Lrssn-blog.

The brand guide is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](./LICENSE) (CC BY-SA 4.0).
The scripts in `scripts/` are free software: you can redistribute them and modify them under the terms of the [GNU Affero General Public License](./LICENSE-CODE), either version 3 of the License or (at your option) any later version.
Neither licence gives permission to use the Lrssn name or logo.
