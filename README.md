# Brand-guide

This repo holds the Lrssn brand guide.
It is a companion to the [Lrssn style guides](https://github.com/Lrssn-blog/Style-guide).

## [Brand](./src/brand/Brand.md)

A guide for the Lrssn brand: name, logo, colours, typography, and voice and tone.
It is a written copy of the public [Brand guide](https://lrssn.com/brand) of the Lrssn website, and the colours come from the website's [design tokens](https://gitea.lrssn.se/Lrssn/Lrssn-com/src/branch/main/src/styles/_variables.scss).
Items that are not decided yet are marked **TODO**.

## Checks

Pull requests run these checks via GitHub Actions:

- [markdownlint](https://github.com/DavidAnson/markdownlint-cli2) on the Markdown files.
- [Ruff](https://docs.astral.sh/ruff/) and [mypy](https://mypy-lang.org/) on the scripts.
- A palette check that compares the colours and contrast ratios in the guide with the website's [design tokens](https://gitea.lrssn.se/Lrssn/Lrssn-com/src/branch/main/src/styles/_variables.scss).
- A link check with [lychee](https://github.com/lycheeverse/lychee).

To run them locally:

```bash
npx markdownlint-cli2
ruff check && ruff format --check
mypy scripts
scripts/palette.py
lychee --config .lychee.toml '**/*.md'
```

The palette check fetches `_variables.scss` from the `main` branch of the Lrssn-com repository.
Pass the path of a local copy to use that instead, for example `scripts/palette.py ../Lrssn-com/src/styles/_variables.scss`.
