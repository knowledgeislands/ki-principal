"""Make the night rendering of a diagram from its light SVG: each ki-design light token becomes its night token.

Usage: python3 night.py 1-one-mac.svg  (writes 1-one-mac-night.svg)
"""
import re, sys

LIGHT_TO_NIGHT = {
    '#f5efe0': '#0f2440',  # paper
    '#1a2030': '#f5efe0',  # ink
    '#4a5568': '#a9b4c4',  # muted
    '#1b3a5c': '#9fbbd8',  # accent (ocean)
    '#2d5a3d': '#8fc4a0',  # ok (forest)
    '#317070': '#7fc2c0',  # teal
    '#8a5a12': '#c8963c',  # warn (text gold)
    '#9b2c1c': '#f0947a',  # bad (rust)
    '#d4c9b4': '#24476e',  # rule
    '#9a8358': '#5f7896',  # boundary
    '#ddddcc': '#1e374c',  # wash ok
    '#f1e8d3': '#1e2d40',  # wash warn
    '#ead8c8': '#2a3147',  # wash bad
    '#eef1f5': '#1e2d40',  # mist, the surface for groups
    'rgb(238, 241, 245)': 'rgb(30, 45, 64)',
    'rgb(221, 221, 204)': 'rgb(30, 55, 76)',
}
def rgb(hex_colour):
    h = hex_colour.lstrip('#')
    return 'rgb({}, {}, {})'.format(int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))

# Mermaid writes some colours as rgb(); map those forms too.
for light, night in list(LIGHT_TO_NIGHT.items()):
    if light.startswith('#'):
        LIGHT_TO_NIGHT[rgb(light)] = rgb(night)

pattern = re.compile('|'.join(re.escape(k) for k in LIGHT_TO_NIGHT), re.IGNORECASE)
src = sys.argv[1]
svg = open(src, encoding='utf-8').read()
out = pattern.sub(lambda m: LIGHT_TO_NIGHT[m.group(0).lower()], svg)
open(src.replace('.svg', '-night.svg'), 'w', encoding='utf-8').write(out)
