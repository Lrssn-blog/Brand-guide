# Brand-guide

This repo holds the Lrssn brand guide.
It is a companion to the [Lrssn style guides](https://github.com/Lrssn-blog/Style-guide).

## [Brand](./src/brand/Brand.md)

A guide for the Lrssn brand: name, logo, colors, typography, and voice and tone.
The colors use the [color palette](https://github.com/Lrssn-blog/Style-guide/blob/main/src/colors/Colors.md).
Items that are not decided yet are marked **TODO**.

## Checks

Pull requests run these checks via GitHub Actions:

- [markdownlint](https://github.com/DavidAnson/markdownlint-cli2) on the Markdown files.
- [Ruff](https://docs.astral.sh/ruff/) and [mypy](https://mypy-lang.org/) on the scripts.
- A palette check that compares the colors and contrast ratios in the guide with the [color palette](https://github.com/Lrssn-blog/Style-guide/blob/main/src/colors/Colors.md).
- A link check with [lychee](https://github.com/lycheeverse/lychee).

To run them locally:

```bash
npx markdownlint-cli2
ruff check && ruff format --check
mypy scripts
scripts/palette.py
lychee --config .lychee.toml '**/*.md'
```

The palette check fetches `Colors.md` from the `main` branch of the Style-guide repository.
Pass the path of a local copy to use that instead, for example `scripts/palette.py ../Style-guide/src/colors/Colors.md`.
