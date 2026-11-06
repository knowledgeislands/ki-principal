"""Home as one viewport-sized map (MSG-62774774, Kris's vision): the territories and their islands, the work
packages and workers placed where they work, each one's primary focus, the summit portal on each island, the
threads of talk up to each territory's principal portal and across, and the planar portal between the planes (Kris's three portals, MSG-cccabc3c).

Islands are repositories, drawn as clusters of pointy-top hexes in the flat chart's manner. Hosts are crews, not
islands: each worker carries its host (sol or terra). Colours are ki-design tokens.
"""
import math
from html import escape

S = 30  # hex size: centre to corner
SQ3 = math.sqrt(3)

# Islands: name, territory, centre of the first hex, axial offsets of its hexes.
ISLANDS = {
    'ki-principal': ('ki', (240, 175), [(0, 0), (1, 0), (0, 1), (-1, 1)]),
    'apps-agora.local': ('ki', (452, 96), [(0, 0), (1, 0)]),
    'ki-design': ('ki', (140, 120), [(0, 0)]),
    'ki-agentic-harness': ('ki', (92, 300), [(0, 0), (1, 0)]),
    'tools-ki': ('ki', (360, 318), [(0, 0)]),
    'apps-observatory.local': ('ki', (520, 250), [(0, 0)]),
    'hnr-principal': ('hnr', (712, 150), [(0, 0), (1, 0), (0, 1)]),
    '5g-emerge': ('hnr', (780, 330), [(0, 0), (1, 0)]),
    'hnr-site': ('hnr', (640, 448), [(0, 0)]),
    'dotfiles': ('personal', (250, 556), [(0, 0), (1, 0), (0, 1)]),
    'inbox': ('personal', (480, 538), [(0, 0), (1, 0)]),
    'assistant': ('personal', (770, 628), [(0, 0)]),
}

TERRITORIES = {
    'ki': ('Knowledge Islands', (40, 30, 580, 350)),
    'hnr': ('Humans Not Robots', (590, 70, 885, 500)),
    'personal': ('Personal', (150, 508, 820, 698)),
}

# Where each meeting point stands: the island's centre of mass, nudged up.
COUNCILS = {'ki': 'ki-principal', 'hnr': 'hnr-principal', 'personal': 'inbox'}

# Workers: label, island, role, host, primary focus, listening, offset of the marker from the meeting point.
WORKERS = [
    ('ki.sop.main', 'ki-principal', 'council', 'sol', 'themes', 'call', (-34, 30)),
    ('ki.prj.agora', 'apps-agora.local', 'enabler', 'sol', 'send', 'call', (-26, 26)),
    ('Claude Design', 'apps-agora.local', 'doer', 'sol', 'identity', 'open', (-26, 54)),
    ('ChatGPT', 'apps-agora.local', 'doer', 'sol', 'identity', 'open', (-26, 82)),
    ('personal.reg.inbox-sol', 'inbox', 'council', 'sol', 'method', 'call', (-30, 26)),
    ('personal.reg.inbox-terra', 'inbox', 'enabler', 'terra', 'method', 'call', (30, 40)),
    ('personal.reg.household-sol', 'dotfiles', 'enabler', 'sol', 'rig', 'poll', (-40, 22)),
    ('personal.reg.household-terra', 'dotfiles', 'enabler', 'terra', 'rig', 'call', (40, 44)),
    ('hnr.sop.main', 'hnr-principal', 'council', 'terra', 'routing', 'silent', (-30, 30)),
    ('hnr.prj.5g-emerge-phase3', '5g-emerge', 'enabler', 'terra', 'delivery', 'open', (-30, 30)),
    ('hnr.prj.5g-emerge-p2ms3', '5g-emerge', 'enabler', 'terra', 'delivery', 'call', (-30, 62)),
    ('hnr.prj.site-robots', 'hnr-site', 'enabler', 'terra', 'site', 'silent', (-26, 30)),
]


def hex_centre(base, q, r):
    return base[0] + SQ3 * S * (q + r / 2), base[1] + 1.5 * S * r


def hexagon(cx, cy, s=S):
    return ' '.join(f'{cx + s * math.cos(math.radians(60 * i - 30)):.1f},{cy + s * math.sin(math.radians(60 * i - 30)):.1f}' for i in range(6))


def meeting_point(name):
    _, base, cells = ISLANDS[name]
    pts = [hex_centre(base, q, r) for q, r in cells]
    return sum(p[0] for p in pts) / len(pts), sum(p[1] for p in pts) / len(pts) - 8


def ring(cx, cy, r, colour, width=2.0, lit=True):
    a = math.radians(26)
    stones = ''.join(
        f'<circle cx="{cx + r * 0.55 * math.cos(math.radians(t)):.1f}" cy="{cy + r * 0.55 * math.sin(math.radians(t)):.1f}" r="{r * 0.17:.1f}" fill="{colour}"/>'
        for t in (-90, 30, 150))
    return (f'<path d="M{cx - r * math.sin(a):.1f} {cy + r * math.cos(a):.1f} A{r} {r} 0 1 1 {cx + r * math.sin(a):.1f} {cy + r * math.cos(a):.1f}" '
            f'fill="none" stroke="{colour}" stroke-width="{width}" stroke-linecap="round"/>{stones if lit else ""}')


def text(x, y, s, size=11.5, weight=400, fill='var(--ink)', anchor='start', italic=False):
    style = ' font-style="italic"' if italic else ''
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{style} '
            f'paint-order="stroke" stroke="var(--paper)" stroke-width="3.5" stroke-linejoin="round">{escape(s)}</text>')


def marker(x, y, role, listen):
    colour = 'var(--bad)' if listen == 'silent' else 'var(--ink)'
    if role == 'doer':
        return f'<rect x="{x - 5}" y="{y - 5}" width="10" height="10" rx="1.5" fill="none" stroke="{colour}" stroke-width="1.8"/>'
    if listen == 'silent':
        return (f'<circle cx="{x}" cy="{y}" r="6" fill="none" stroke="{colour}" stroke-width="2"/>'
                f'<path d="M{x - 4} {y + 4} L{x + 4} {y - 4}" stroke="{colour}" stroke-width="2"/>')
    if listen == 'open':
        return f'<circle cx="{x}" cy="{y}" r="5.5" fill="none" stroke="{colour}" stroke-width="2"/>'
    r = 7.5 if role == 'council' else 6
    extra = f'<circle cx="{x}" cy="{y}" r="{r + 3.5}" fill="none" stroke="{colour}" stroke-width="1.2"/>' if role == 'council' else ''
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{colour}"/>{extra}'


def territory_map(width=900, height=700, plane='both'):
    on_plane = (lambda host: plane == 'both' or host == plane)
    out = [f'<svg viewBox="0 0 {width} {height}" width="100%" role="img" aria-label="The territories, their islands, the work packages and workers on them, and the threads of talk between their meeting points">']
    # territories: a faint boundary and a label
    for key, (label, (x1, y1, x2, y2)) in TERRITORIES.items():
        out.append(f'<rect x="{x1}" y="{y1}" width="{x2 - x1}" height="{y2 - y1}" rx="28" fill="none" stroke="var(--rule)" stroke-width="1.5" stroke-dasharray="2 6"/>')
        out.append(text(x1 + 18, y1 + 22, label.upper(), size=11, weight=600, fill='var(--muted)'))
    # islands
    for name, (terr, base, cells) in ISLANDS.items():
        for q, r in cells:
            cx, cy = hex_centre(base, q, r)
            out.append(f'<polygon points="{hexagon(cx, cy)}" fill="var(--land)" stroke="var(--boundary)" stroke-width="1"/>')
    # threads: summit portals up to the principal portal, principal portals across, the planar portal
    gold = 'var(--gold)'
    threads = [('apps-agora.local', 'ki-principal', 1.5), ('5g-emerge', 'hnr-principal', 1.5), ('hnr-site', 'hnr-principal', 1.5),
               ('dotfiles', 'inbox', 1.5), ('ki-principal', 'hnr-principal', 3), ('ki-principal', 'inbox', 3), ('hnr-principal', 'inbox', 3)]
    for a, b, w in threads:
        (x1, y1), (x2, y2) = meeting_point(a), meeting_point(b)
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2 - 18
        out.append(f'<path d="M{x1:.1f} {y1:.1f} Q{mx:.1f} {my:.1f} {x2:.1f} {y2:.1f}" fill="none" stroke="{gold}" stroke-width="{w}" stroke-linecap="round" opacity=".85"/>')
    gx, gy = meeting_point('dotfiles')
    out.append(f'<path d="M{gx:.1f} {gy:.1f} C{gx - 120:.1f} {gy + 10:.1f} {70:.1f} {gy + 40:.1f} 18 {gy + 86:.1f}" fill="none" stroke="{gold}" stroke-width="5" stroke-linecap="round"/>')
    out.append(text(30, gy + 104, 'The planar portal', size=12.5, weight=600))
    out.append(text(30, gy + 120, 'sol ⇄ terra · open · heard 04:20' if plane == 'both' else f'showing {plane}\'s plane · the other rig dimmed', size=11.5, fill='var(--muted)'))
    # summit portals (principal portals larger, the planar portal ringed in gold)
    joined = {w[1] for w in WORKERS if on_plane(w[3])}
    for name in ISLANDS:
        x, y = meeting_point(name)
        lit = name in joined
        r = 15 if name == 'dotfiles' else 14 if name in COUNCILS.values() else 11
        out.append(ring(x, y, r, 'var(--ink)' if lit else 'var(--muted)', 2.2 if lit else 1.4, lit=lit))
        if name == 'dotfiles':
            out.append(ring(x, y, r + 7, gold, 1.6, lit=False))
        out.append(text(x, y - r - 8, name, size=11, fill='var(--muted)', anchor='middle'))
    # workers
    for label, island, role, host, focus, listen, (dx, dy) in WORKERS:
        x, y = meeting_point(island)
        mx, my = x + dx, y + dy
        if not on_plane(host):
            out.append(f'<g opacity=".28">{marker(mx, my, role, listen)}</g>')
            continue
        out.append(marker(mx, my, role, listen))
        right = dx >= 0
        tx = mx + (11 if right else -11)
        anchor = 'start' if right else 'end'
        fill = 'var(--bad)' if listen == 'silent' else 'var(--ink)'
        out.append(text(tx, my + 1, label, size=11.5, weight=600 if role == 'council' else 400, fill=fill, anchor=anchor))
        tail = {'silent': ' · silent', 'open': ' · on open'}.get(listen, '')
        out.append(text(tx, my + 15, f'★ {focus} · {host}{tail}', size=10.5, fill='var(--muted)', anchor=anchor))
    # work packages not in the Agora
    px, py = meeting_point('ki-principal')
    out.append(text(px - 45, py + 64, '+14 work packages not in the Agora', size=10.5, fill='var(--muted)', anchor='end', italic=True))
    out.append('</svg>')
    return ''.join(out)


KEY = [
    ('<circle cx="9" cy="9" r="6" fill="var(--ink)"/>', 'Work package, listening (enabler)'),
    ('<circle cx="9" cy="9" r="5.5" fill="var(--ink)"/><circle cx="9" cy="9" r="8" fill="none" stroke="var(--ink)" stroke-width="1.2"/>', "Territory's council: its State of play main, at the principal portal"),
    ('<rect x="4" y="4" width="10" height="10" rx="1.5" fill="none" stroke="var(--ink)" stroke-width="1.8"/>', 'Doer, brought in by a work package'),
    ('<circle cx="9" cy="9" r="5" fill="none" stroke="var(--ink)" stroke-width="2"/>', 'Reads on open'),
    ('<circle cx="9" cy="9" r="5.5" fill="none" stroke="var(--bad)" stroke-width="2"/><path d="M5 13 L13 5" stroke="var(--bad)" stroke-width="2"/>', 'Silent'),
    ('<path d="M6 15 A7 7 0 1 1 12 15" fill="none" stroke="var(--ink)" stroke-width="2"/>', "Summit portal, on every island; lit when someone there listens. Larger on a principal island: the principal portal"),
    ('<path d="M2 12 Q9 4 16 12" fill="none" stroke="var(--gold)" stroke-width="2"/>', 'Thread of talk: summit portals up to the principal portal, principal portals across; the planar portal joins the planes'),
]
