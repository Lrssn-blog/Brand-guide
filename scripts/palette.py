#!/usr/bin/env python3
"""Checks that the colours in Brand.md match the Lrssn colour themes.

The colours are defined in the maps `$theme-light` (Lrssn Shore) and
`$theme-dark` (Lrssn Hearth) of website/_theme.scss in the ColorTheme
repository, which generates them from its palettes for the Lrssn website.
The check fails if a colour in Brand.md is missing from the stylesheet or has
a different value, or if a contrast ratio in Brand.md is wrong.

Usage:
    scripts/palette.py                 Fetch _theme.scss from ColorTheme.
    scripts/palette.py <_theme.scss>   Use a local copy of the stylesheet.
"""

import pathlib
import re
import sys
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
BRAND = ROOT / 'src' / 'brand' / 'Brand.md'
SOURCE_URL = (
    'https://raw.githubusercontent.com/Lrssn-blog/ColorTheme/main/'
    'website/_theme.scss'
)

# The columns of the first contrast table: the theme and the background.
CONTRAST_COLUMNS = (
    ('light', 'background'),
    ('light', 'surface'),
    ('dark', 'background'),
    ('dark', 'surface'),
)

THEMES = ('light', 'dark')

# A colour token in the stylesheet, such as 'primary-color': #fc6600.
SOURCE_TOKEN = re.compile(r"'([\w-]+)':\s*(#[0-9a-fA-F]{3,6})\b")
# A row of a colour table: token, light and dark HEX, and the use.
TOKEN_ROW = re.compile(
    r'^\| `([\w-]+)` \| `(#[0-9a-f]{6})` \| `(#[0-9a-f]{6})` \| [^|]+ \|$'
)
# A row of the first contrast table: token and four ratios.
CONTRAST_ROW = re.compile(
    r'^\| `([\w-]+)` \| ([\d.]+) \| ([\d.]+) \| ([\d.]+) \| ([\d.]+) \|$'
)
# A row of the second contrast table: text on a fill, in both themes.
PAIR_ROW = re.compile(
    r'^\| `([\w-]+)` on `([\w-]+)` \| ([\d.]+) \| ([\d.]+) \|$'
)


def expand_hex(value: str) -> str:
    """Writes a HEX colour with six lowercase digits, such as '#ffffff'."""
    value = value.lower()
    if len(value) == 4:
        return '#' + ''.join(digit * 2 for digit in value[1:])
    return value


def parse_theme(text: str, name: str) -> dict[str, str]:
    """Returns the colours of the map `$<name>` of the stylesheet."""
    match = re.search(r'\$' + re.escape(name) + r': \((.*?)\n\);', text, re.S)
    if not match:
        raise SystemExit(f'Found no ${name} map in the stylesheet')
    return {
        token: expand_hex(value)
        for token, value in SOURCE_TOKEN.findall(match.group(1))
    }


def parse_tokens(text: str) -> dict[str, tuple[str, str]]:
    """Returns the colour tables of Brand.md as {token: (light, dark)}."""
    tokens = {}
    for line in text.splitlines():
        match = TOKEN_ROW.match(line)
        if match:
            token, light, dark = match.groups()
            tokens[token] = (light, dark)
    return tokens


def parse_contrast(text: str) -> dict[str, tuple[float, ...]]:
    """Returns the first contrast table of Brand.md as {token: ratios}."""
    contrast = {}
    for line in text.splitlines():
        match = CONTRAST_ROW.match(line)
        if match:
            contrast[match.group(1)] = tuple(
                float(ratio) for ratio in match.groups()[1:]
            )
    return contrast


def parse_pairs(text: str) -> dict[tuple[str, str], tuple[float, float]]:
    """Returns the second contrast table as {(text, fill): (light, dark)}."""
    pairs = {}
    for line in text.splitlines():
        match = PAIR_ROW.match(line)
        if match:
            foreground, background, light, dark = match.groups()
            pairs[foreground, background] = (float(light), float(dark))
    return pairs


def luminance(hex_value: str) -> float:
    """Returns the WCAG relative luminance of a colour such as '#fc6600'."""
    channels = []
    for start in (1, 3, 5):
        value = int(hex_value[start : start + 2], 16) / 255
        if value <= 0.03928:
            channels.append(value / 12.92)
        else:
            channels.append(((value + 0.055) / 1.055) ** 2.4)
    red, green, blue = channels
    return 0.2126 * red + 0.7152 * green + 0.0722 * blue


def contrast_ratio(first: str, second: str) -> float:
    """Returns the WCAG contrast ratio of two colours."""
    lighter, darker = sorted((luminance(first), luminance(second)))[::-1]
    return (lighter + 0.05) / (darker + 0.05)


def check_tokens(
    source: dict[str, dict[str, str]],
    tokens: dict[str, tuple[str, str]],
) -> list[str]:
    """Compares the colour tables with the colours of the stylesheet."""
    errors = []
    for token, shown in tokens.items():
        for theme, value in zip(THEMES, shown, strict=True):
            want = source[theme].get(token)
            if want is None:
                errors.append(f'{token}: not in the {theme} theme')
            elif want != value:
                errors.append(f'{token}: {theme} is {value}, should be {want}')
    return errors


def differs(shown: float, want: float) -> bool:
    """Returns whether a ratio in Brand.md differs from the calculated one."""
    return f'{shown:.2f}' != f'{want:.2f}'


def check_contrast(
    source: dict[str, dict[str, str]],
    contrast: dict[str, tuple[float, ...]],
    pairs: dict[tuple[str, str], tuple[float, float]],
) -> list[str]:
    """Compares the contrast tables with the ratios of the stylesheet."""
    errors = []
    for token, ratios in contrast.items():
        for (theme, background), shown in zip(
            CONTRAST_COLUMNS, ratios, strict=True
        ):
            colours = source[theme]
            if token not in colours or background not in colours:
                errors.append(f'{token}: not in the {theme} theme')
                continue
            want = contrast_ratio(colours[token], colours[background])
            if differs(shown, want):
                errors.append(
                    f'{token} on {theme} {background}: '
                    f'{shown:.2f} should be {want:.2f}'
                )
    for (foreground, background), ratios in pairs.items():
        for theme, shown in zip(THEMES, ratios, strict=True):
            colours = source[theme]
            if foreground not in colours or background not in colours:
                errors.append(f'{foreground} on {background}: not in {theme}')
                continue
            want = contrast_ratio(colours[foreground], colours[background])
            if differs(shown, want):
                errors.append(
                    f'{foreground} on {background} in {theme}: '
                    f'{shown:.2f} should be {want:.2f}'
                )
    return errors


def read_source() -> str:
    """Reads the stylesheet from the path in argv, or from Lrssn-com."""
    if len(sys.argv) > 1:
        return pathlib.Path(sys.argv[1]).read_text()
    # Name the check, since some hosts reject the default Python user agent.
    request = urllib.request.Request(
        SOURCE_URL, headers={'User-Agent': 'lrssn-brand-guide-palette-check'}
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            text: str = response.read().decode('utf-8')
    except urllib.error.URLError as e:
        raise SystemExit(f'Cannot fetch {SOURCE_URL}: {e}') from e
    return text


def main() -> None:
    """Runs the checks, and exits with 1 if one of them fails."""
    brand = BRAND.read_text()
    stylesheet = read_source()
    source = {
        theme: parse_theme(stylesheet, f'theme-{theme}') for theme in THEMES
    }
    tokens = parse_tokens(brand)
    contrast = parse_contrast(brand)
    pairs = parse_pairs(brand)
    if not tokens:
        raise SystemExit(f'Found no colour tables in {BRAND.name}')
    if not contrast or not pairs:
        raise SystemExit(f'Found no contrast tables in {BRAND.name}')
    errors = check_tokens(source, tokens)
    errors += check_contrast(source, contrast, pairs)
    for error in errors:
        print(error)
    if errors:
        sys.exit(1)
    print(f'{len(tokens)} colours and their contrast ratios match.')


if __name__ == '__main__':
    main()
