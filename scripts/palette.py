#!/usr/bin/env python3
"""Checks that the colors in Brand.md match the Lrssn color palette.

The palette is defined in src/colors/Colors.md of the Style-guide repository.
The check fails if a color is missing, extra or different, or if a contrast
ratio in the contrast table does not match the colors.

Usage:
    scripts/palette.py              Fetch Colors.md from the Style-guide repo.
    scripts/palette.py <Colors.md>  Use a local copy of Colors.md.
"""

import pathlib
import re
import sys
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
BRAND = ROOT / 'src' / 'brand' / 'Brand.md'
COLORS_URL = (
    'https://raw.githubusercontent.com/Lrssn-blog/Style-guide/main/'
    'src/colors/Colors.md'
)

# The backgrounds of the contrast table, in column order.
BACKGROUNDS = ('White', 'Light grey', 'Dark grey', 'Black')

# A line of Colors.md ends with the HSV, HEX and RGB values of a color.
SOURCE_LINE = re.compile(
    r'\((\d+, \d+, \d+)\) \((#[0-9A-F]{6})\) \((\d+, \d+, \d+)\)$'
)
# A row of the palette table: name, role, HEX, RGB and HSV.
PALETTE_ROW = re.compile(
    r'^\| ([^|`]+) \| [^|`]+ \| `(#[0-9A-F]{6})` \| ([\d, ]+) \| ([\d, ]+) \|$'
)
# A row of the contrast table: the text color and four ratios.
CONTRAST_ROW = re.compile(
    r'^\| ([A-Za-z ]+) \| ([\d.]+) \| ([\d.]+) \| ([\d.]+) \| ([\d.]+) \|$'
)


def parse_source(text: str) -> dict[str, tuple[str, str]]:
    """Returns the colors of Colors.md as {hex: (rgb, hsv)}."""
    colors = {}
    for line in text.splitlines():
        match = SOURCE_LINE.search(line.strip())
        if match:
            hsv, hex_value, rgb = match.groups()
            colors[hex_value] = (rgb, hsv)
    return colors


def parse_palette(text: str) -> dict[str, tuple[str, str, str]]:
    """Returns the palette table of Brand.md as {name: (hex, rgb, hsv)}."""
    palette = {}
    for line in text.splitlines():
        match = PALETTE_ROW.match(line)
        if match:
            name, hex_value, rgb, hsv = match.groups()
            palette[name] = (hex_value, rgb, hsv)
    return palette


def parse_contrast(text: str) -> dict[str, tuple[float, ...]]:
    """Returns the contrast table of Brand.md as {name: ratios}."""
    contrast = {}
    for line in text.splitlines():
        match = CONTRAST_ROW.match(line)
        if match:
            contrast[match.group(1)] = tuple(
                float(ratio) for ratio in match.groups()[1:]
            )
    return contrast


def luminance(hex_value: str) -> float:
    """Returns the WCAG relative luminance of a color such as '#D96C36'."""
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
    """Returns the WCAG contrast ratio of two colors."""
    lighter, darker = sorted((luminance(first), luminance(second)))[::-1]
    return (lighter + 0.05) / (darker + 0.05)


def check_palette(
    source: dict[str, tuple[str, str]],
    palette: dict[str, tuple[str, str, str]],
) -> list[str]:
    """Compares the palette table with the colors of Colors.md."""
    errors = []
    seen = set()
    for name, (hex_value, rgb, hsv) in palette.items():
        seen.add(hex_value)
        if hex_value not in source:
            errors.append(f'{name}: {hex_value} is not in Colors.md')
        elif source[hex_value] != (rgb, hsv):
            want_rgb, want_hsv = source[hex_value]
            errors.append(
                f'{name}: RGB {rgb} and HSV {hsv} should be '
                f'RGB {want_rgb} and HSV {want_hsv}'
            )
    for hex_value in source:
        if hex_value not in seen:
            errors.append(f'{hex_value} is in Colors.md but not in Brand.md')
    return errors


def check_contrast(
    palette: dict[str, tuple[str, str, str]],
    contrast: dict[str, tuple[float, ...]],
) -> list[str]:
    """Compares the contrast table with the ratios of the palette colors."""
    errors = []
    for name in BACKGROUNDS:
        if name not in palette:
            errors.append(f'Background {name} is not in the palette table')
    if errors:
        return errors
    for name in palette:
        if name not in contrast:
            errors.append(f'{name} is not in the contrast table')
    for name, ratios in contrast.items():
        if name not in palette:
            errors.append(f'{name} is in the contrast table, not the palette')
            continue
        for background, shown in zip(BACKGROUNDS, ratios, strict=True):
            want = contrast_ratio(palette[name][0], palette[background][0])
            if f'{want:.2f}' != f'{shown:.2f}':
                errors.append(
                    f'{name} on {background}: {shown:.2f} should be {want:.2f}'
                )
    return errors


def read_source() -> str:
    """Reads Colors.md from the path in argv, or from GitHub."""
    if len(sys.argv) > 1:
        return pathlib.Path(sys.argv[1]).read_text()
    try:
        with urllib.request.urlopen(COLORS_URL, timeout=30) as response:
            text: str = response.read().decode('utf-8')
    except urllib.error.URLError as e:
        raise SystemExit(f'Cannot fetch {COLORS_URL}: {e}') from e
    return text


def main() -> None:
    """Runs the checks, and exits with 1 if one of them fails."""
    brand = BRAND.read_text()
    source = parse_source(read_source())
    palette = parse_palette(brand)
    if not source:
        raise SystemExit('Found no colors in Colors.md')
    if not palette:
        raise SystemExit(f'Found no palette table in {BRAND.name}')
    errors = check_palette(source, palette)
    errors += check_contrast(palette, parse_contrast(brand))
    for error in errors:
        print(error)
    if errors:
        sys.exit(1)
    print(f'{len(palette)} colors and their contrast ratios match.')


if __name__ == '__main__':
    main()
