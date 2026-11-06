"""Home as one viewport-sized map (MSG-62774774, Kris's vision): the territories and their islands, the work
packages and workers placed where they work, each one's primary focus, the island portal on each island, the
threads of talk up to each territory's principal portal and across, and the planar portal between the planes
(Kris's three portals, MSG-cccabc3c). The planar portal is its own island, ki-portal, in Personal, kept by the
watchman beside the housekeeper (the household, on dotfiles) and the assistant (on inbox).

Islands are repositories, drawn as clusters of pointy-top hexes in the flat chart's manner. Hosts are crews, not
islands: each worker carries its host (sol or terra). Colours are ki-design tokens.

territory_map() draws the plain map (1a, 1d, 1e). working_map() draws the working map of the preferred home
(1f, 1g, 1h): active islands prominent, Focused or Everything, queued work and waiting messages on each island,
one island selected, and zoom with labels kept at reading size.
"""
import math
from html import escape

S = 30  # hex size: centre to corner
SQ3 = math.sqrt(3)
W, H = 900, 720  # the map's own units

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
    'hnr-site': ('hnr', (630, 440), [(0, 0)]),
    'dotfiles': ('personal', (110, 566), [(0, 0), (1, 0)]),
    'inbox': ('personal', (340, 566), [(0, 0), (1, 0)]),
    'assistant': ('personal', (566, 566), [(0, 0)]),
    'ki-portal': ('personal', (694, 566), [(0, 0), (1, 0)]),
}

TERRITORIES = {
    'ki': ('Knowledge Islands', (40, 24, 580, 356)),
    'hnr': ('Humans Not Robots', (590, 40, 885, 490)),
    'personal': ('Personal', (40, 498, 885, 714)),
}

# Each territory's principal island, where its council meets at the principal portal.
COUNCILS = {'ki': 'ki-principal', 'hnr': 'hnr-principal', 'personal': 'inbox'}
PLANAR = 'ki-portal'  # the island that holds the planar portal

# Workers: label, island, role, host, primary focus, listening, offset of the marker from the island portal, label side.
WORKERS = [
    ('ki.sop.main', 'ki-principal', 'council', 'sol', 'themes', 'call', (-34, 30), 'l'),
    ('ki.prj.agora', 'apps-agora.local', 'enabler', 'sol', 'send', 'call', (-26, 26), 'l'),
    ('Claude Design', 'apps-agora.local', 'doer', 'sol', 'identity', 'open', (-26, 54), 'l'),
    ('ChatGPT', 'apps-agora.local', 'doer', 'sol', 'identity', 'open', (-26, 82), 'l'),
    ('personal.reg.inbox-sol', 'inbox', 'council', 'sol', 'method', 'call', (-40, 50), 'r'),
    ('personal.reg.inbox-terra', 'inbox', 'enabler', 'terra', 'method', 'call', (-40, 88), 'r'),
    ('personal.reg.household-sol', 'dotfiles', 'enabler', 'sol', 'rig', 'poll', (-40, 50), 'r'),
    ('personal.reg.household-terra', 'dotfiles', 'enabler', 'terra', 'rig', 'call', (-40, 88), 'r'),
    ('personal.reg.watchman-sol', 'ki-portal', 'enabler', 'sol', 'portal', 'call', (-40, 50), 'r'),
    ('personal.reg.watchman-terra', 'ki-portal', 'enabler', 'terra', 'portal', 'call', (-40, 88), 'r'),
    ('hnr.sop.main', 'hnr-principal', 'council', 'terra', 'routing', 'silent', (-30, 30), 'l'),
    ('hnr.prj.5g-emerge-phase3', '5g-emerge', 'enabler', 'terra', 'delivery', 'open', (-30, 30), 'l'),
    ('hnr.prj.5g-emerge-p2ms3', '5g-emerge', 'enabler', 'terra', 'delivery', 'call', (-30, 62), 'l'),
    ('hnr.prj.site-robots', 'hnr-site', 'enabler', 'terra', 'site', 'silent', (-26, 30), 'l'),
]

# Queued work and waiting messages on each island (placeholders until the live roster supplies them).
COUNTS = {
    'ki-principal': (5, 3), 'apps-agora.local': (4, 2), 'ki-design': (1, 0), 'ki-agentic-harness': (0, 0),
    'tools-ki': (2, 0), 'apps-observatory.local': (3, 1), 'hnr-principal': (2, 4), '5g-emerge': (3, 1),
    'hnr-site': (1, 2), 'dotfiles': (1, 0), 'inbox': (6, 3), 'assistant': (0, 0), 'ki-portal': (0, 1),
}

# Threads of talk: island portal up to its principal portal (thin), principal portals across (thick).
THREADS = [('apps-agora.local', 'ki-principal', 1.5), ('5g-emerge', 'hnr-principal', 1.5), ('hnr-site', 'hnr-principal', 1.5),
           ('dotfiles', 'inbox', 1.5), ('ki-portal', 'inbox', 1.5),
           ('ki-principal', 'hnr-principal', 3), ('ki-principal', 'inbox', 3), ('hnr-principal', 'inbox', 3)]

# Where the zoom goes: a territory's frame in map units, at the map's own proportions.
ZOOMS = {'hnr': (447, 30, 580, 464)}


def hex_centre(base, q, r):
    return base[0] + SQ3 * S * (q + r / 2), base[1] + 1.5 * S * r


def hexagon(cx, cy, s=S):
    return ' '.join(f'{cx + s * math.cos(math.radians(60 * i - 30)):.1f},{cy + s * math.sin(math.radians(60 * i - 30)):.1f}' for i in range(6))


def meeting_point(name):
    _, base, cells = ISLANDS[name]
    pts = [hex_centre(base, q, r) for q, r in cells]
    return sum(p[0] for p in pts) / len(pts), sum(p[1] for p in pts) / len(pts) - 8


def portal_size(name):
    return 15 if name == PLANAR else 14 if name in COUNCILS.values() else 11


def ring(cx, cy, r, colour, width=2.0, lit=True):
    a = math.radians(26)
    stones = ''.join(
        f'<circle cx="{cx + r * 0.55 * math.cos(math.radians(t)):.1f}" cy="{cy + r * 0.55 * math.sin(math.radians(t)):.1f}" r="{r * 0.17:.1f}" fill="{colour}"/>'
        for t in (-90, 30, 150))
    return (f'<path d="M{cx - r * math.sin(a):.1f} {cy + r * math.cos(a):.1f} A{r} {r} 0 1 1 {cx + r * math.sin(a):.1f} {cy + r * math.cos(a):.1f}" '
            f'fill="none" stroke="{colour}" stroke-width="{width}" stroke-linecap="round"/>{stones if lit else ""}')


def text(x, y, s, size=11.5, weight=400, fill='var(--ink)', anchor='start', italic=False, k=1.0):
    style = ' font-style="italic"' if italic else ''
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size * k:.2f}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{style} '
            f'paint-order="stroke" stroke="var(--paper)" stroke-width="{3.5 * k:.2f}" stroke-linejoin="round">{escape(s)}</text>')


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


def thread(a, b, w, opacity='.85'):
    (x1, y1), (x2, y2) = meeting_point(a), meeting_point(b)
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2 - 18
    return f'<path d="M{x1:.1f} {y1:.1f} Q{mx:.1f} {my:.1f} {x2:.1f} {y2:.1f}" fill="none" stroke="var(--gold)" stroke-width="{w}" stroke-linecap="round" opacity="{opacity}"/>'


def planar_thread(width=5):
    """The planar portal's own thread: from ki-portal out past the map's edge, to the other plane."""
    x, y = meeting_point(PLANAR)
    return (f'<path d="M{x:.1f} {y:.1f} C{x + 70:.1f} {y - 6:.1f} {W - 60} {y - 40:.1f} {W + 4} {y - 52:.1f}" '
            f'fill="none" stroke="var(--gold)" stroke-width="{width}" stroke-linecap="round"/>')


def planar_label(plane, k=1.0):
    px, py = meeting_point(PLANAR)
    other = 'terra' if plane == 'sol' else 'sol'
    second = 'sol ⇄ terra · open · heard 04:20' if plane == 'both' else f"{plane}'s plane · {other} dimmed"
    return text(px - 29, py + 128, 'The planar portal', size=12, weight=600, k=k) + text(px - 29, py + 143, second, size=11, fill='var(--muted)', k=k)


def territory_map(width=W, height=H, plane='both'):
    """The plain map (1a, and its planes 1d and 1e)."""
    on_plane = (lambda host: plane == 'both' or host == plane)
    out = [f'<svg viewBox="0 0 {width} {height}" width="100%" role="img" aria-label="The territories, their islands, the work packages and workers on them, and the threads of talk between their portals">']
    for key, (label, (x1, y1, x2, y2)) in TERRITORIES.items():
        out.append(f'<rect x="{x1}" y="{y1}" width="{x2 - x1}" height="{y2 - y1}" rx="28" fill="none" stroke="var(--rule)" stroke-width="1.5" stroke-dasharray="2 6"/>')
        out.append(text(x1 + 18, y1 + 22, label.upper(), size=11, weight=600, fill='var(--muted)'))
    for name, (terr, base, cells) in ISLANDS.items():
        for q, r in cells:
            cx, cy = hex_centre(base, q, r)
            out.append(f'<polygon points="{hexagon(cx, cy)}" fill="var(--land)" stroke="var(--boundary)" stroke-width="1"/>')
    for a, b, w in THREADS:
        out.append(thread(a, b, w))
    out.append(planar_thread())
    joined = {w[1] for w in WORKERS if on_plane(w[3])}
    for name in ISLANDS:
        x, y = meeting_point(name)
        lit = name in joined
        r = portal_size(name)
        out.append(ring(x, y, r, 'var(--ink)' if lit else 'var(--muted)', 2.2 if lit else 1.4, lit=lit))
        if name == PLANAR:
            out.append(ring(x, y, r + 7, 'var(--gold)', 1.6, lit=False))
        out.append(text(x, y - r - (14 if name == PLANAR else 8), name, size=11, fill='var(--muted)', anchor='middle'))
    out.append(planar_label(plane))
    for label, island, role, host, focus, listen, (dx, dy), side in WORKERS:
        x, y = meeting_point(island)
        mx, my = x + dx, y + dy
        if not on_plane(host):
            out.append(f'<g opacity=".28">{marker(mx, my, role, listen)}</g>')
            continue
        out.append(marker(mx, my, role, listen))
        right = side == 'r'
        tx = mx + (11 if right else -11)
        anchor = 'start' if right else 'end'
        fill = 'var(--bad)' if listen == 'silent' else 'var(--ink)'
        out.append(text(tx, my + 1, label, size=11.5, weight=600 if role == 'council' else 400, fill=fill, anchor=anchor))
        tail = {'silent': ' · silent', 'open': ' · on open'}.get(listen, '')
        out.append(text(tx, my + 15, f'★ {focus} · {host}{tail}', size=10.5, fill='var(--muted)', anchor=anchor))
    px, py = meeting_point('ki-principal')
    out.append(text(px - 45, py + 64, '+14 work packages not in the Agora', size=10.5, fill='var(--muted)', anchor='end', italic=True))
    out.append('</svg>')
    return ''.join(out)


# ---------------------------------------------------------------- the working map (1f, 1g, 1h)
def count_glyph(kind, x, y, k=1.0):
    """Queued work: a stack of three bars. Waiting messages: an envelope. Drawn 10 units square at (x, y)."""
    s = 10 * k
    if kind == 'queued':
        return ''.join(f'<path d="M{x:.1f} {y + s * f:.1f} h{s:.1f}" stroke="var(--ink)" stroke-width="{1.5 * k:.2f}" stroke-linecap="round"/>' for f in (0.15, 0.5, 0.85))
    return (f'<rect x="{x:.1f}" y="{y + s * 0.1:.1f}" width="{s:.1f}" height="{s * 0.8:.1f}" rx="{1 * k:.1f}" fill="none" stroke="var(--ink)" stroke-width="{1.3 * k:.2f}"/>'
            f'<path d="M{x:.1f} {y + s * 0.15:.1f} L{x + s / 2:.1f} {y + s * 0.55:.1f} L{x + s:.1f} {y + s * 0.15:.1f}" fill="none" stroke="var(--ink)" stroke-width="{1.3 * k:.2f}"/>')


def count_badges(x, y, queued, waiting, k=1.0, words=False):
    """Small counts beside an island's name: queued work and waiting messages. Zero is left out."""
    out, cx = [], x
    for kind, n, word in (('queued', queued, 'queued'), ('waiting', waiting, 'waiting')):
        if not n:
            continue
        label = f'{n} {word}' if words else str(n)
        w = (24 + 6.4 * len(label)) * k
        h = 16 * k
        out.append(f'<rect x="{cx:.1f}" y="{y - h + 3 * k:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{8 * k:.1f}" fill="var(--surface)" stroke="var(--boundary)" stroke-width="{1 * k:.2f}"/>')
        out.append(count_glyph(kind, cx + 6 * k, y - h + 6 * k, k))
        out.append(f'<text x="{cx + 20 * k:.1f}" y="{y - 1 * k:.1f}" font-size="{10.5 * k:.2f}" font-weight="600" fill="var(--ink)">{label}</text>')
        cx += w + 4 * k
    return ''.join(out), max(0, cx - x - 4 * k)


def active_islands(plane='both'):
    """An island is active when a worker on the plane is there."""
    return {w[1] for w in WORKERS if plane == 'both' or w[3] == plane}


def working_map(plane='both', focused=True, selected=None, zoom=None):
    """The preferred home's map. Focused hides quiet islands; zoom frames one territory and keeps labels at reading size."""
    on_plane = (lambda host: plane == 'both' or host == plane)
    active = active_islands(plane)
    vx, vy, vw, vh = ZOOMS[zoom] if zoom else (0, 0, W, H)
    k = vw / W  # labels keep their size on screen as the map grows
    detail = zoom is not None

    def dim(terr):
        return zoom is not None and terr != zoom

    def wrap(terr, body, extra=''):
        return f'<g{extra}{" opacity=" + chr(34) + ".35" + chr(34) if dim(terr) else ""}>{body}</g>'

    shown = {n for n in ISLANDS if not focused or n in active}
    out = [f'<svg viewBox="{vx} {vy} {vw} {vh}" width="100%" height="100%" preserveAspectRatio="xMidYMid meet" role="img" '
           f'aria-label="The territories, their islands with queued work and waiting messages, the workers on them, and the threads between their portals">']
    for key, (label, (x1, y1, x2, y2)) in TERRITORIES.items():
        out.append(wrap(key, f'<rect x="{x1}" y="{y1}" width="{x2 - x1}" height="{y2 - y1}" rx="28" fill="none" stroke="var(--rule)" stroke-width="{1.5 * k:.2f}" stroke-dasharray="{2 * k:.1f} {6 * k:.1f}"/>'
                             + text(x1 + 18 * k, y1 + 22 * k, label.upper(), size=11, weight=600, fill='var(--muted)', k=k)))
    # islands: active ones as land, quiet ones as outlines; the selected one edged in the accent
    for name, (terr, base, cells) in ISLANDS.items():
        if name not in shown:
            continue
        is_active = name in active
        fill, stroke, sw = ('var(--land)', 'var(--boundary)', 1.2) if is_active else ('var(--surface)', 'var(--rule)', 1)
        polys = ''.join(f'<polygon points="{hexagon(*hex_centre(base, q, r))}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>' for q, r in cells)
        if name == selected:
            polys = ''.join(f'<polygon points="{hexagon(*hex_centre(base, q, r), s=S + 3.5)}" fill="var(--accent)"/>' for q, r in cells) + polys
        out.append(wrap(terr, polys, f' data-island="{name}"'))
    # threads
    for a, b, w in THREADS:
        if a in shown and b in shown:
            op = '.3' if zoom and (dim(ISLANDS[a][0]) or dim(ISLANDS[b][0])) else '.85'
            out.append(thread(a, b, w, opacity=op))
    if PLANAR in shown:
        out.append(wrap('personal', planar_thread()))
    # island portals, names and counts
    for name, (terr, base, cells) in ISLANDS.items():
        if name not in shown:
            continue
        x, y = meeting_point(name)
        is_active = name in active
        r = portal_size(name)
        parts = [ring(x, y, r, 'var(--ink)' if is_active else 'var(--muted)', 2.2 if is_active else 1.4, lit=is_active)]
        if name == PLANAR:
            parts.append(ring(x, y, r + 7, 'var(--gold)', 1.6, lit=False))
        ny = y - r - (14 if name == PLANAR else 8) - (2 * k if detail else 0)
        q, m = COUNTS[name]
        badges, bw = count_badges(0, 0, q, m, k, words=detail)
        name_w = len(name) * (6.1 if is_active else 5.7) * k
        total = name_w + (6 * k + bw if bw else 0)
        left = x - total / 2
        parts.append(text(left, ny, name, size=11, weight=600 if is_active else 400, fill='var(--ink)' if is_active else 'var(--muted)', k=k))
        if bw:
            parts.append(f'<g transform="translate({left + name_w + 6 * k:.1f} {ny:.1f})">{badges}</g>')
        out.append(wrap(terr, ''.join(parts), f' data-island-head="{name}"'))
    if PLANAR in shown:
        out.append(wrap('personal', planar_label(plane, k)))
    # workers
    for label, island, role, host, focus, listen, (dx, dy), side in WORKERS:
        if island not in shown:
            continue
        x, y = meeting_point(island)
        mx, my = x + dx, y + dy
        if not on_plane(host):
            out.append(f'<g opacity=".28">{marker(mx, my, role, listen)}</g>')
            continue
        g = [marker(mx, my, role, listen) if not detail else
             f'<g transform="translate({mx:.1f} {my:.1f}) scale({k:.3f}) translate({-mx:.1f} {-my:.1f})">{marker(mx, my, role, listen)}</g>']
        right = side == 'r'
        tx = mx + (11 if right else -11) * k
        anchor = 'start' if right else 'end'
        fill = 'var(--bad)' if listen == 'silent' else 'var(--ink)'
        g.append(text(tx, my + 1 * k, label, size=11.5, weight=600 if role == 'council' else 400, fill=fill, anchor=anchor, k=k))
        tail = {'silent': ' · silent', 'open': ' · on open'}.get(listen, '')
        g.append(text(tx, my + 15 * k, f'★ {focus} · {host}{tail}', size=10.5, fill='var(--muted)', anchor=anchor, k=k))
        if detail:
            heard = {'silent': '2 calls unanswered since 02:10', 'open': 'read 03:30', 'call': 'answered 03:58', 'poll': 'answered 04:01'}[listen]
            g.append(text(tx, my + 28 * k, heard, size=10.5, fill='var(--bad)' if listen == 'silent' else 'var(--muted)', anchor=anchor, k=k))
        out.append(wrap(ISLANDS[island][0], ''.join(g)))
    if 'ki-principal' in shown:
        px, py = meeting_point('ki-principal')
        out.append(wrap('ki', text(px - 45, py + 64, '+14 work packages not in the Agora', size=10.5, fill='var(--muted)', anchor='end', italic=True, k=k)))
    if focused and not zoom:
        hidden = [n for n in ISLANDS if n not in shown]
        if hidden:
            queued = sum(COUNTS[n][0] for n in hidden)
            waiting = sum(COUNTS[n][1] for n in hidden)
            x1, y1, x2, y2 = TERRITORIES['ki'][1]
            for i, line in enumerate((f'{len(hidden)} quiet islands hidden', f'{queued} queued, {waiting} waiting among them', 'Everything shows them')):
                out.append(text(x1 + 18, 296 + 14 * i, line, size=10.5, fill='var(--muted)', italic=True))
    out.append('</svg>')
    return ''.join(out)


def overview(zoom, width=168):
    """A small overview of the whole map with the zoomed frame drawn on it; dragging the frame pans."""
    h = width * H / W
    s = width / W
    parts = [f'<svg viewBox="0 0 {W} {H}" width="{width}" height="{h:.0f}" aria-label="Overview: where the zoomed map sits">']
    for key, (label, (x1, y1, x2, y2)) in TERRITORIES.items():
        parts.append(f'<rect x="{x1}" y="{y1}" width="{x2 - x1}" height="{y2 - y1}" rx="28" fill="none" stroke="var(--rule)" stroke-width="6"/>')
    active = active_islands()
    for name, (terr, base, cells) in ISLANDS.items():
        for q, r in cells:
            parts.append(f'<polygon points="{hexagon(*hex_centre(base, q, r))}" fill="{"var(--land)" if name in active else "var(--surface)"}"/>')
    vx, vy, vw, vh = ZOOMS[zoom]
    parts.append(f'<rect x="{vx}" y="{vy}" width="{min(vw, W - vx - 4)}" height="{vh}" fill="none" stroke="var(--accent)" stroke-width="{2 / s:.1f}"/>')
    parts.append('</svg>')
    return ''.join(parts)


KEY = [
    ('<circle cx="9" cy="9" r="6" fill="var(--ink)"/>', 'Work package, listening (enabler)'),
    ('<circle cx="9" cy="9" r="5.5" fill="var(--ink)"/><circle cx="9" cy="9" r="8" fill="none" stroke="var(--ink)" stroke-width="1.2"/>', "Territory's council, at the principal portal"),
    ('<rect x="4" y="4" width="10" height="10" rx="1.5" fill="none" stroke="var(--ink)" stroke-width="1.8"/>', 'Doer, brought in by a package'),
    ('<circle cx="9" cy="9" r="5" fill="none" stroke="var(--ink)" stroke-width="2"/>', 'Reads on open'),
    ('<circle cx="9" cy="9" r="5.5" fill="none" stroke="var(--bad)" stroke-width="2"/><path d="M5 13 L13 5" stroke="var(--bad)" stroke-width="2"/>', 'Silent'),
    ('<path d="M6 15 A7 7 0 1 1 12 15" fill="none" stroke="var(--ink)" stroke-width="2"/>', "Island portal, lit when someone listens; larger, the principal portal"),
    ('<path d="M6.5 12.5 A4 4 0 1 1 11.5 12.5" fill="none" stroke="var(--ink)" stroke-width="1.8"/><circle cx="9" cy="9" r="7.5" fill="none" stroke="var(--gold)" stroke-width="1.4"/>', 'Planar portal, on ki-portal, kept by the watchman'),
    ('<path d="M2 12 Q9 4 16 12" fill="none" stroke="var(--gold)" stroke-width="2"/>', 'Thread of talk: up to the principal portal, across, and out through the planar portal'),
]

# The working map's key: short, in one strip under the map.
STRIP = [
    ('<circle cx="9" cy="9" r="6" fill="var(--ink)"/>', 'listening'),
    ('<circle cx="9" cy="9" r="5" fill="var(--ink)"/><circle cx="9" cy="9" r="8" fill="none" stroke="var(--ink)" stroke-width="1.2"/>', 'council'),
    ('<rect x="4" y="4" width="10" height="10" rx="1.5" fill="none" stroke="var(--ink)" stroke-width="1.8"/>', 'doer'),
    ('<circle cx="9" cy="9" r="5" fill="none" stroke="var(--ink)" stroke-width="2"/>', 'on open'),
    ('<circle cx="9" cy="9" r="5.5" fill="none" stroke="var(--bad)" stroke-width="2"/><path d="M5 13 L13 5" stroke="var(--bad)" stroke-width="2"/>', 'silent'),
    ('<path d="M6 15 A7 7 0 1 1 12 15" fill="none" stroke="var(--ink)" stroke-width="2"/>', 'island portal; larger, principal portal'),
    ('<path d="M6.5 12.5 A4 4 0 1 1 11.5 12.5" fill="none" stroke="var(--ink)" stroke-width="1.8"/><circle cx="9" cy="9" r="7.5" fill="none" stroke="var(--gold)" stroke-width="1.4"/>', 'planar portal'),
    ('<path d="M2 12 Q9 4 16 12" fill="none" stroke="var(--gold)" stroke-width="2"/>', 'thread of talk'),
    ('<rect x="0.5" y="2" width="17" height="14" rx="7" fill="var(--surface)" stroke="var(--boundary)"/><path d="M5 6.5h8M5 9h8M5 11.5h8" stroke="var(--ink)" stroke-width="1.3"/>', 'queued work'),
    ('<rect x="0.5" y="2" width="17" height="14" rx="7" fill="var(--surface)" stroke="var(--boundary)"/><rect x="5" y="5.5" width="8" height="7" rx="1" fill="none" stroke="var(--ink)" stroke-width="1.2"/><path d="M5 6 L9 9.5 L13 6" fill="none" stroke="var(--ink)" stroke-width="1.2"/>', 'waiting messages'),
    ('<polygon points="9,1 16,5 16,13 9,17 2,13 2,5" fill="var(--land)" stroke="var(--boundary)"/>', 'active island'),
    ('<polygon points="9,1 16,5 16,13 9,17 2,13 2,5" fill="var(--surface)" stroke="var(--rule)"/>', 'quiet island'),
]
