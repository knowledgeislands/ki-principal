"""The Agora app mock-ups: the shell and every view, as HTML artboards 1440 points wide.

Each region worth discussing carries data-region (its code, such as P3) and data-label, so the board can draw
its box. Shell pages mark only N; view pages mark only P, as the annotated-board standard asks.
"""
from html import escape
import map_view as MV
from data import AGENTS, LISTEN_WORDS, AGORA_QUERIES, SOP_QUERIES, SAID, CHECKOUTS, NOW

# ---------------------------------------------------------------- glyphs (24 grid, 1.5 stroke, line only)
def glyph(name, cls=''):
    paths = {
        'ring': '<path d="M7.7 20.2 A9 9 0 1 1 16.3 20.2" fill="none"/><circle cx="12" cy="6.9" r="1.9" fill="currentColor" stroke="none"/><circle cx="16.1" cy="14.1" r="1.9" fill="currentColor" stroke="none"/><circle cx="7.9" cy="14.1" r="1.9" fill="currentColor" stroke="none"/>',
        'home': '<path d="M8.2 19.6 A8 8 0 1 1 15.8 19.6" fill="none"/><circle cx="12" cy="12" r="1.6" fill="currentColor" stroke="none"/>',
        'here': '<path d="M9 7h11M9 12h11M9 17h11"/><path d="M4.5 5.2l.8 1.6 1.7.2-1.3 1.2.4 1.7-1.6-.9-1.5.9.3-1.7L2 7l1.7-.2z" fill="currentColor" stroke="none"/><circle cx="4.5" cy="12" r="1.3" fill="currentColor" stroke="none"/><circle cx="4.5" cy="17" r="1.3" fill="currentColor" stroke="none"/>',
        'said': '<circle cx="5" cy="12" r="1.8" fill="currentColor" stroke="none"/><circle cx="19" cy="12" r="1.8" fill="currentColor" stroke="none"/><path d="M9 8.5a5 5 0 0 1 0 7M12 6a8.5 8.5 0 0 1 0 12" fill="none"/>',
        'broadcast': '<circle cx="12" cy="12" r="1.8" fill="currentColor" stroke="none"/><path d="M8.5 8.5a5 5 0 0 0 0 7M15.5 8.5a5 5 0 0 1 0 7M5.6 5.6a9 9 0 0 0 0 12.8M18.4 5.6a9 9 0 0 1 0 12.8" fill="none"/>',
        'waits': '<path d="M7 3.5h10M7 20.5h10M8 3.5c0 5 8 5 8 8.5s-8 3.5-8 8.5M16 3.5c0 5-8 5-8 8.5s8 3.5 8 8.5" fill="none"/>',
        'macs': '<path d="M6.5 6l4 2.3v4.6l-4 2.3-4-2.3V8.3zM17.5 8.8l4 2.3v4.6l-4 2.3-4-2.3v-4.6z" fill="none"/><path d="M10.5 11.5h3" stroke-dasharray="1 1.5"/>',
        'checkouts': '<circle cx="6" cy="5.5" r="1.8" fill="none"/><circle cx="6" cy="18.5" r="1.8" fill="none"/><circle cx="18" cy="9" r="1.8" fill="none"/><path d="M6 7.3v9.4M18 10.8c0 4-6 3-11.2 6.4" fill="none"/>',
        'inbox': '<path d="M3.5 13.5l2.5-8h12l2.5 8v5h-17z M3.5 13.5h5l1 2.5h5l1-2.5h5" fill="none"/>',
        'insight': '<circle cx="10.5" cy="10.5" r="6" fill="none"/><path d="M15 15l5.5 5.5"/>',
        'away': '<path d="M15.5 4.5a8 8 0 1 0 4 11.6A7 7 0 0 1 15.5 4.5z" fill="none"/>',
        'ping': '<circle cx="12" cy="12" r="2.2" fill="none"/><path d="M12 3.5v3M12 17.5v3M3.5 12h3M17.5 12h3"/>',
        'mark': '<path d="M5 20.5V4M5 4.5h12l-2.5 4 2.5 4H5" fill="none"/>',
        'portal': '<path d="M14 2.5c-3 2-3 9 0 11M26 2.5c3 2 3 9 0 11" fill="none"/><path d="M15.5 8h9" stroke-dasharray="1.5 1.5"/>',
    }
    vb = '0 0 40 16' if name == 'portal' else '0 0 24 24'
    return (f'<svg class="{cls}" viewBox="{vb}" fill="none" stroke="currentColor" stroke-width="1.5" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths[name]}</svg>')


def mark(kind):
    return {
        'stone': '<svg class="g" viewBox="0 0 12 12"><circle cx="6" cy="6" r="3.8" fill="currentColor"/></svg>',
        'hollow': '<svg class="g" viewBox="0 0 12 12"><circle cx="6" cy="6" r="3.6" fill="none" stroke="currentColor" stroke-width="1.4"/></svg>',
        'slashed': '<svg class="g" viewBox="0 0 12 12"><circle cx="6" cy="6" r="3.6" fill="none" stroke="currentColor" stroke-width="1.4"/><path d="M3.3 8.7 L8.7 3.3" stroke="currentColor" stroke-width="1.4"/></svg>',
        'diamond': '<svg class="g" viewBox="0 0 12 12"><path d="M6 1.5 L10.5 6 L6 10.5 L1.5 6 Z" fill="currentColor"/></svg>',
    }[kind]


def R(code, label):
    """The attributes that mark a region for the board."""
    return f'data-region="{code}" data-label="{escape(label)}"'


# ---------------------------------------------------------------- the shell
NAV = [
    ('Home', 'home', ''),
    ("Who's doing what", 'here', '12'),
    ("What's being said", 'said', ''),
    ('Broadcasts', 'broadcast', ''),
    ('Waits on you', 'waits', '34'),
    ('Macs and the portal', 'macs', '2'),
    ('Checkouts', 'checkouts', '1'),
]
LATER = [('Inbox', 'inbox', 'from the KIV'), ('Insight', 'insight', 'from the Observatory')]


def rail(active, mark_shell, portal='open'):
    m = (lambda code, label: R(code, label)) if mark_shell else (lambda code, label: '')
    navs = ''.join(
        f'<div class="nav{" on" if label == active else ""}">{glyph(g)}<span class="label">{escape(label)}</span>'
        f'<span class="n">{n}</span></div>' for label, g, n in NAV)
    later = ''.join(
        f'<div class="nav later">{glyph(g)}<span class="label">{label} <span class="muted">· later</span></span></div>'
        for label, g, _ in LATER)
    portal_text = {
        'open': ('sol ⇄ terra', 'Portal open · heard 04:20'),
        'unheard': ('sol ⇢ terra', 'terra not heard from since 03:41'),
        'away': ('sol', 'Not in the Agora: not listening'),
    }[portal]
    portal_cls = {'open': 'teal', 'unheard': 'bad', 'away': 'bad'}[portal]
    return f'''<aside class="rail">
  <div class="brand" {m("N1", "Brand")}>{glyph("ring")}<div class="text"><div class="name">Agora</div><div class="where">on sol, this Mac</div></div></div>
  <nav class="group" aria-label="Views" {m("N2", "Views")}>{navs}</nav>
  <nav class="group" aria-label="Later" {m("N3", "Later")}><h4>Later</h4>{later}</nav>
  <div class="speak" {m("N4", "Speak to everyone")}><h4>Speak to everyone</h4>
    <div class="row"><span class="btn">{glyph("broadcast")}<span class="label">Broadcast…</span></span><span class="btn">{glyph("away")}<span class="label">Away…</span></span></div>
    <div class="row"><span class="btn">{glyph("ping")}<span class="label">Ping</span></span><span class="btn">{glyph("mark")}<span class="label">Mark all</span></span></div>
  </div>
  <div class="portal" {m("N5", "The portal")}><div class="line"><span class="{portal_cls}">{glyph("portal")}</span><span class="text"><b>{portal_text[0]}</b><br><span class="muted">{portal_text[1]}</span></span></div></div>
</aside>'''


def tabs_bar(tabs, mark_shell):
    m = R('N6', 'Tabs') if mark_shell else ''
    items = ''.join(f'<span class="tab{" on" if on else ""}">{escape(t)}{" <span class=x>×</span>" if closable else ""}</span>' for t, on, closable in tabs)
    return f'<div class="tabs" {m}>{items}<span class="tab add">+</span></div>'


DEFAULT_TABS = None


# The first pack's views (pages 1 to 6) now sit in the revised Atlas shell (0.4); the rail is drawn only for 0.1's own boards.
PAGE_PLACES = {'Home': 'lands', "Who's doing what": 'here', "What's being said": 'said', 'Broadcasts': 'broadcasts',
               'Waits on you': 'waits', 'Macs and the portal': 'macs', 'Checkouts': 'checkouts'}


def page(active, content, contracted=False, mark_shell=False, theme='night', portal='open', title='Agora', tabs=None):
    if not (mark_shell or contracted or portal != 'open') and active in PAGE_PLACES:
        # The map was Home; it is Known Lands now, under Work (0.4).
        content = content.replace('<h1>Home</h1>', '<h1>Known Lands</h1>')
        if tabs is not None:
            tabs = [('Known Lands' if t == 'Home' else t, on, x) for t, on, x in tabs]
        return atlas_page(PAGE_PLACES[active], content, tabs=tabs, theme=theme, height=None)
    if tabs is None:
        tabs = [(active, True, False), ('ki.prj.agora · messages.md', False, True), ('Agora app pack · README', False, True)]
    return f'''<!doctype html><html lang="en-GB" data-theme="{theme}"><head><meta charset="utf-8">
<title>{escape(title)}</title><link rel="stylesheet" href="../build/app.css"></head><body>
<div class="app{" contracted" if contracted else ""}">{rail(active, mark_shell, portal)}<main>{tabs_bar(tabs, mark_shell)}{content}</main></div>
</body></html>'''


def head(code, title, summary, tools=''):
    return (f'<header class="pagehead" {R(code, "Page header")}><h1>{escape(title)}</h1>'
            f'<span class="summary">{summary}</span><span class="tools">{tools}</span></header>')


# ---------------------------------------------------------------- shared pieces
def listen_cell(a):
    how, when, kind = LISTEN_WORDS[a['listen']]
    cls = ' class="bad"' if a['listen'] == 'silent' else ''
    return f'<td{cls}>{mark(kind)}{how}<span class="sub">{when.format(at=a["at"])}</span></td>'


def focus_cell(a):
    rest = ', '.join(a['focus'][1:])
    return f'<td><span class="star">★</span> <b>{a["focus"][0]}</b>{", " + rest if rest else ""}</td>'


def waits_cell(a):
    if not a['waits']:
        return '<td class="muted">Nothing</td>'
    q = 'query' if a['waits'] == 1 else 'queries'
    return f'<td><b>{a["waits"]} {q}</b><span class="sub">{a["first"]}…</span></td>'


def roster_rows(selected='ki.prj.agora', compact=False):
    out = []
    for mac, note in (('sol', 'this Mac · present · 5 agents'), ('terra', 'present · heard 04:20 · 7 agents')):
        out.append(f'<tr class="group"><td colspan="{4 if compact else 5}">{mark("stone")}{mac} <span class="muted">· {note}</span></td></tr>')
        for a in AGENTS:
            if a['mac'] != mac:
                continue
            sel = ' class="sel"' if a['id'] == selected else ''
            terr = '' if compact else f'<td>{a["terr"]}</td>'
            out.append(f'<tr{sel}><td><span class="id">{a["id"]}</span><span class="sub">{a["title"]}</span></td>{terr}'
                       f'{focus_cell(a)}{listen_cell(a)}{waits_cell(a)}</tr>')
    return ''.join(out)


def roster_table(code='P3', label='Agents by Mac', selected='ki.prj.agora', compact=False):
    th = '<th>Agent</th>' + ('' if compact else '<th>Territory</th>') + '<th>Focus areas</th><th>Listening</th><th>Waits on you</th>'
    return f'<section class="panel" {R(code, label)}><table><thead><tr>{th}</tr></thead><tbody>{roster_rows(selected, compact)}</tbody></table></section>'


def said_rows(rows=SAID, limit=None):
    out = []
    for t, frm, to, kind, layer, words, heard in rows[:limit]:
        chip = f'<span class="chip {"durable" if layer == "durable" else "talk"}">{"Git" if layer == "durable" else "Agora"}</span>'
        hcls = ' class="bad"' if heard == 'silent' or 'silent' in heard else ''
        out.append(f'<tr><td class="mono">{t}</td><td>{escape(frm)} <span class="muted">→</span> {escape(to)}</td>'
                   f'<td>{kind}</td><td>{chip}</td><td>{escape(words)}</td><td{hcls}>{escape(heard)}</td></tr>')
    return ''.join(out)


def said_table(code, label, limit=None, title=None):
    h = f'<header><h2>{title}</h2><span class="muted">last hour, both Macs</span></header>' if title else ''
    return (f'<section class="panel" {R(code, label)}>{h}<table><thead><tr><th>Time</th><th>From → to</th><th>Kind</th>'
            f'<th>Layer</th><th>What was said</th><th>Heard</th></tr></thead><tbody>{said_rows(limit=limit)}</tbody></table></section>')


def attention_panel(code='P2', label='Needs a look'):
    return f'''<section class="panel" {R(code, label)}><header><h2>Needs a look</h2><span class="muted">2</span></header>
<ul class="plain body">
<li class="warn">{mark("diamond")}<b>hnr-principal on terra is diverged</b><span class="sub">Ahead 1, behind 2 · hnr.sop.main called 04:12, silent</span></li>
<li class="bad">{mark("slashed")}<b>hnr.prj.site-robots is silent</b><span class="sub">Its listener lapsed at 02:10 · 2 calls unanswered</span></li>
</ul></section>'''


def waits_panel(code='P4', label='Waits on you', n=5):
    rows = ''.join(f'<li><span class="mono">{q}</span> <span class="muted">· {focus} · ki.prj.agora</span><span class="sub">{escape(t)}</span></li>'
                   for q, t, focus, since, rec in AGORA_QUERIES[:n])
    return (f'<section class="panel" {R(code, label)}><header><h2>Waits on you</h2><span class="muted">34 queries, 5 agents</span></header>'
            f'<ul class="plain body">{rows}<li class="muted">and 29 more</li></ul></section>')


# ---------------------------------------------------------------- the two squares (home 1a, and 5.1)
def island_svg(width=900, height=330, unheard=False):
    import math

    def hexagon(cx, cy, r):
        pts = [(cx + r * math.cos(math.radians(60 * i - 30)), cy + r * math.sin(math.radians(60 * i - 30))) for i in range(6)]
        return ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts)

    def square(cx, cy, agents, mac, terra=False):
        ring_r = 62
        parts = [f'<polygon points="{hexagon(cx, cy, 150)}" fill="var(--land)" stroke="var(--boundary)" stroke-width="1.5"/>',
                 f'<path d="M{cx - ring_r * math.sin(math.radians(28)):.1f} {cy + ring_r * math.cos(math.radians(28)):.1f} '
                 f'A{ring_r} {ring_r} 0 1 1 {cx + ring_r * math.sin(math.radians(28)):.1f} {cy + ring_r * math.cos(math.radians(28)):.1f}" '
                 f'fill="none" stroke="var(--ink)" stroke-width="2.5" stroke-linecap="round" {"stroke-dasharray=&quot;4 5&quot;" if terra and unheard else ""}/>']
        n = len(agents)
        for i, a in enumerate(agents):
            ang = math.radians(-90 + i * 360 / n + (180 / n if n % 4 == 0 else 0))
            sx, sy = cx + 40 * math.cos(ang), cy + 40 * math.sin(ang)
            lx, ly = cx + 98 * math.cos(ang), cy + 98 * math.sin(ang)
            kind = 'unknown' if terra and unheard else a['listen']
            if kind in ('call', 'poll'):
                parts.append(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="7" fill="var(--ink)"/>')
            elif kind == 'open':
                parts.append(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="6" fill="none" stroke="var(--ink)" stroke-width="2"/>')
            elif kind == 'silent':
                parts.append(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="6" fill="none" stroke="var(--bad)" stroke-width="2"/>'
                             f'<path d="M{sx - 4:.1f} {sy + 4:.1f} L{sx + 4:.1f} {sy - 4:.1f}" stroke="var(--bad)" stroke-width="2"/>')
            else:
                parts.append(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="6" fill="none" stroke="var(--muted)" stroke-width="2" stroke-dasharray="2 2"/>')
            anchor = 'middle' if abs(math.cos(ang)) < 0.3 else ('start' if math.cos(ang) > 0 else 'end')
            parts.append(f'<text x="{lx:.1f}" y="{ly + 4:.1f}" text-anchor="{anchor}" font-size="11.5" fill="var(--ink)">{escape(a["short"])}</text>')
        sub = 'not heard from since 03:41' if terra and unheard else f'{"this Mac · " if not terra else ""}{n} agents'
        parts.append(f'<text x="{cx}" y="{cy + 178}" text-anchor="middle" font-size="14" font-weight="600" fill="var(--ink)">{mac}</text>'
                     f'<text x="{cx}" y="{cy + 196}" text-anchor="middle" font-size="12" fill="var(--muted)">{sub}</text>')
        return ''.join(parts)

    sol = [a for a in AGENTS if a['mac'] == 'sol']
    terra = [a for a in AGENTS if a['mac'] == 'terra']
    cx1, cx2, cy = width * 0.24, width * 0.76, 150
    mid = width / 2
    portal_colour = 'var(--bad)' if unheard else 'var(--teal)'
    portal = (f'<path d="M{mid - 28} {cy - 52} C{mid - 52} {cy - 20} {mid - 52} {cy + 20} {mid - 28} {cy + 52}" fill="none" stroke="var(--ink)" stroke-width="2"/>'
              f'<path d="M{mid + 28} {cy - 52} C{mid + 52} {cy - 20} {mid + 52} {cy + 20} {mid + 28} {cy + 52}" fill="none" stroke="var(--ink)" stroke-width="2"/>'
              f'<path d="M{cx1 + 132} {cy - 10} H{cx2 - 132}" stroke="{portal_colour}" stroke-width="2" stroke-dasharray="6 6"/>'
              f'<path d="M{cx2 - 132} {cy + 10} H{cx1 + 132}" stroke="{portal_colour}" stroke-width="2" stroke-dasharray="6 6" {"opacity=&quot;.35&quot;" if unheard else ""}/>'
              f'<text x="{mid}" y="{cy + 80}" text-anchor="middle" font-size="12.5" font-weight="600" fill="var(--ink)">The portal</text>'
              f'<text x="{mid}" y="{cy + 96}" text-anchor="middle" font-size="11.5" fill="var(--muted)">{"waiting for terra · 1 broadcast queued" if unheard else "open · 14 calls, 2 broadcasts this hour"}</text>')
    return (f'<svg viewBox="0 0 {width} {height}" width="100%" role="img" aria-label="The two squares, sol and terra, and the portal between them">'
            f'{square(cx1, cy, sol, "sol")}{portal}{square(cx2, cy, terra, "terra", terra=True)}</svg>')


# ---------------------------------------------------------------- views
def home_a():
    tools = '<span class="btn">Who looks after…</span>'
    return f'''{head("P1", "Home", "12 agents on 2 Macs · 2 need a look · 34 queries wait on you", tools)}
<div class="grid" style="grid-template-columns: 1fr 360px;">
  <section class="panel" {R("P2", "The two squares")}><header><h2>Here now</h2><span class="muted">each Mac's square, its agents, and the portal between them</span></header><div class="body">{island_svg()}
  <p class="foot" style="margin:4px 0 0">Solid stone: listening. Hollow: reads on open. Slashed: silent. The table under Who's doing what is the same picture as text.</p></div></section>
  <div class="grid" style="align-content:start">{attention_panel("P3")}{waits_panel("P4", n=4)}</div>
</div>
{said_table("P5", "Just said", limit=6, title="Just said")}'''


def home_b():
    stats = ''.join(f'<div class="panel stat"><span class="v">{v}</span><span class="k">{k}</span></div>' for v, k in
                    (('12', 'agents on 2 Macs'), ('9', 'listening, 2 silent'), ('2', 'need a look'), ('34', 'queries wait on you')))
    return f'''{head("P1", "Home", "Friday 6 November, 04:20")}
<div class="grid" style="grid-template-columns: repeat(4, 1fr);" {R("P2", "Summary figures")}>{stats}</div>
{attention_panel("P3")}
{roster_table("P4", "Agents by Mac", selected=None, compact=True)}'''


def home_c():
    side = ''.join(f'<li>{mark("slashed" if a["listen"] == "silent" else "hollow" if a["listen"] == "open" else "stone")}<span class="id">{a["id"]}</span> <span class="muted">· {a["mac"]}</span></li>' for a in AGENTS)
    return f'''{head("P1", "Home", "12 agents on 2 Macs · All words since 03:30")}
<div class="grid" style="grid-template-columns: 1fr 340px;">
  {said_table("P2", "What's being said", title="What's being said")}
  <section class="panel" {R("P3", "Who is here")}><header><h2>Who is here</h2><span class="muted">12</span></header><ul class="plain body">{side}</ul></section>
</div>'''


def here_a():
    tools = '<span class="seg"><span class="on">Both Macs</span><span>sol</span><span>terra</span></span><span class="find">Who looks after <b>a focus, such as identity</b></span>'
    a = AGENTS[0]
    return f'''{head("P1", "Who's doing what", "12 agents on 2 Macs · 9 listening · 1 on open · 2 silent", tools)}
{roster_table("P2", "Agents by Mac")}
<section class="panel" {R("P3", "Selected agent")}><div class="body grid" style="grid-template-columns: 1.2fr 1fr 1fr;">
<div><b class="id">ki.prj.agora</b> · KI › Techne › Agora<span class="sub">On sol, in ki-principal. Builds and runs Agora.</span>
<ul class="plain" style="margin-top:8px"><li><span class="star">★</span> <b>send</b>: the mark broadcast, the KIV send side, waking Orca chats</li><li><b>jobs</b>: scheduled jobs, Claude accounts, keeping the host awake</li><li><b>voice</b>: the voice bard path</li><li><b>identity</b>: Agora's look, and its designer doers</li></ul></div>
<div><b>Listening</b><span class="sub">Agora's call · answered 04:12 · next check 04:50</span><br><b>With it now</b><span class="sub">Run ki-prj-agora, running · doers Claude Design, ChatGPT</span></div>
<div><b>Waits on you</b><span class="sub">10 queries: AGORA-COUNT-PLACE, MARK-WORDS, WAKE-NOTE and 7 more</span><div style="display:flex;gap:8px;margin-top:10px"><span class="btn brass">Open its 10 queries</span><span class="btn">Ping it</span></div></div>
</div></section>'''


def here_b():
    focus = {}
    for a in AGENTS:
        for i, f in enumerate(a['focus']):
            if f == '_emerging':
                continue
            focus.setdefault(f, []).append((a, i == 0))
    rows = []
    for f in sorted(focus):
        owners = focus[f]
        lead = ', '.join(f'<span class="id">{a["id"]}</span>{" <span class=star>★</span>" if p else ""} <span class="muted">· {a["mac"]}</span>' for a, p in owners)
        listening = 'all listening' if all(a['listen'] in ('call', 'poll') for a, _ in owners) else '<span class="bad">one silent</span>' if any(a['listen'] == 'silent' for a, _ in owners) else 'on open'
        sel = ' class="sel"' if f == 'identity' else ''
        rows.append(f'<tr{sel}><td><b>{f}</b></td><td>{lead}</td><td>{len(owners)}</td><td>{listening}</td></tr>')
    tools = '<span class="find">Who looks after <b>identity</b></span>'
    return f'''{head("P1", "Who's doing what", "By focus: the address book · 20 focus areas across 12 agents", tools)}
<section class="panel" {R("P2", "Focus areas and their agents")}><table><thead><tr><th>Focus</th><th>Looked after by (★ primary)</th><th>Agents</th><th>Listening</th></tr></thead><tbody>{''.join(rows)}</tbody></table></section>
<p class="foot" {R("P3", "Routing note")}>An idea about a focus goes to the agent whose focus covers it; where two share one, the agent with it as primary (★) is asked first.</p>'''


def agent_a():
    ticks = ''.join('<i class="miss" style="height:8px"></i>' if i in (7,) else f'<i style="height:{10 + (i * 7) % 10}px"></i>' for i in range(24))
    said = [r for r in SAID if 'ki.prj.agora' in (r[1], r[2])]
    rows = ''.join(f'<tr><td class="mono">{t}</td><td>{escape(f)} → {escape(to)}</td><td>{escape(w)}</td><td>{escape(h)}</td></tr>' for t, f, to, k, l, w, h in said)
    q = ''.join(f'<tr><td class="mono">{i}</td><td>{escape(t)}</td><td>{f}</td><td class="mono">{s}</td><td>{r})</td></tr>' for i, t, f, s, r in AGORA_QUERIES[:6])
    return f'''{head("P1", "ki.prj.agora", "KI › Techne › Agora · on sol · territory ki", '<span class="btn">Ping it</span><span class="btn">Open its folder</span><span class="btn brass">Open its 10 queries</span>')}
<div class="grid" style="grid-template-columns: 1fr 1fr 1fr;">
  <section class="panel" {R("P2", "Focus areas")}><header><h2>Focus areas</h2></header><ul class="plain body"><li><span class="star">★</span> <b>send</b><span class="sub">The mark broadcast, then the KIV send side and waking Orca chats</span></li><li><b>jobs</b><span class="sub">Scheduled jobs, Claude accounts, keeping the host awake</span></li><li><b>voice</b><span class="sub">The voice bard path</span></li><li><b>identity</b><span class="sub">Agora's look in the tray, and its designer doers</span></li><li><b>_emerging</b><span class="sub">What has no focus yet</span></li></ul></section>
  <section class="panel" {R("P3", "Listening")}><header><h2>Listening</h2><span class="muted">Agora's call</span></header><div class="body"><div class="ticks">{ticks}</div><p class="foot">Each bar is a call or ping in the last two hours, answered; the outlined one was missed at 03:10. Next check 04:50.</p></div></section>
  <section class="panel" {R("P4", "With it now")}><header><h2>With it now</h2></header><ul class="plain body"><li>Run <span class="id">ki-prj-agora</span> · running since 01:15</li><li>Doer: Claude Design · identity · on open</li><li>Doer: ChatGPT · identity · on open</li><li>Checkouts: <span class="id">apps-agora.local</span>, <span class="id">ki-principal</span> · level</li></ul></section>
</div>
<section class="panel" {R("P5", "Said with it")}><header><h2>Said with it</h2><span class="muted">last hour</span></header><table><tbody>{rows}</tbody></table></section>
<section class="panel" {R("P6", "Waits on you")}><header><h2>Waits on you</h2><span class="muted">10</span></header><table><thead><tr><th>Query</th><th>What</th><th>Focus</th><th>Since</th><th>Recommended</th></tr></thead><tbody>{q}</tbody></table></section>'''


def said_a():
    tools = '<span class="seg"><span class="on">Everything</span><span>Git</span><span>Agora</span></span><span class="seg"><span class="on">Both Macs</span><span>sol</span><span>terra</span></span>'
    return f'''{head("P1", "What's being said", "Last hour on both Macs · 10 things said · 1 not heard", tools)}
{said_table("P2", "Everything said, newest first")}
<p class="foot" {R("P3", "Layer note")}>Git: written to the record (messages, decisions, announcements). Agora: said through the portal and calls, with no commit (pings, broadcasts, health, pushes signalled).</p>'''


def said_b():
    durable = [r for r in SAID if r[4] == 'durable']
    talk = [r for r in SAID if r[4] == 'talk']

    def col(rows):
        return ''.join(f'<li><span class="mono">{t}</span> {escape(f)} → {escape(to)}<span class="sub">{escape(w)} · {escape(h)}</span></li>' for t, f, to, k, l, w, h in rows)
    return f'''{head("P1", "What's being said", "Last hour on both Macs, by layer")}
<div class="grid" style="grid-template-columns: 1fr 1fr;">
<section class="panel" {R("P2", "Durable: Git")}><header><h2>Written to the record</h2><span class="chip durable">Git</span></header><ul class="plain body">{col(durable)}</ul></section>
<section class="panel" {R("P3", "Conversational: Agora")}><header><h2>Said through Agora</h2><span class="chip talk">Agora</span></header><ul class="plain body">{col(talk)}</ul></section>
</div>'''


def broadcasts_a():
    rows = [
        ('04:19', 'Away until 08:00', 'away', '11 of 12', 'hnr.prj.site-robots'),
        ('04:05', 'Ping', 'ping', '10 of 12', 'hnr.sop.main, hnr.prj.site-robots'),
        ('03:26', 'Away until 08:00 (ki.sop.main)', 'away', '1 of 1', ''),
        ('01:45', 'Mark and summarise', 'mark', '7 of 9', 'hnr.sop.main, hnr.prj.5g-emerge-phase3'),
    ]
    trs = ''.join(f'<tr{" class=sel" if i == 1 else ""}><td class="mono">{t}</td><td>{w}</td><td>{k}</td><td>{h}</td><td class="bad">{s or "<span class=muted>None</span>"}</td></tr>' for i, (t, w, k, h, s) in enumerate(rows))
    ans = ''.join(f'<li>{mark("slashed" if a["listen"] == "silent" else "stone")}<span class="id">{a["id"]}</span> <span class="muted">· {a["mac"]} · {"silent" if a["listen"] == "silent" else "answered 04:0" + str(5 + i % 4)}</span></li>' for i, a in enumerate(AGENTS))
    return f'''{head("P1", "Broadcasts", "Sent from this Mac and received from terra · today", '<span class="btn">Broadcast…</span><span class="btn">Ping</span><span class="btn">Mark all</span>')}
<div class="grid" style="grid-template-columns: 1fr 380px;">
<section class="panel" {R("P2", "Broadcasts sent")}><table><thead><tr><th>Sent</th><th>What</th><th>Kind</th><th>Heard</th><th>Silent</th></tr></thead><tbody>{trs}</tbody></table></section>
<section class="panel" {R("P3", "Who heard the ping")}><header><h2>Ping at 04:05</h2><span class="muted">10 answered, 2 silent</span></header><ul class="plain body">{ans}</ul><div class="body"><span class="btn">Ping the 2 silent again</span></div></section>
</div>'''


def waits_a():
    def block(agent, queries, total):
        trs = ''.join(f'<tr><td class="mono">{i}</td><td>{escape(t)}</td><td>{f}</td><td class="mono">{s}</td><td>{r})</td></tr>' for i, t, f, s, r in sorted(queries, key=lambda q: q[3]))
        more = f'<tr><td colspan="5" class="muted">and {total - len(queries)} more</td></tr>' if total > len(queries) else ''
        return f'<tr class="group"><td colspan="5"><span class="id">{agent}</span> <span class="muted">· {total} · oldest first</span></td></tr>{trs}{more}'
    body = block('ki.sop.main', SOP_QUERIES, 18) + block('ki.prj.agora', AGORA_QUERIES[:5], 10) + \
        '<tr class="group"><td colspan="5"><span class="id">personal.reg.inbox-sol</span> <span class="muted">· 3</span></td></tr><tr><td class="mono">Q21</td><td>How listening is counted</td><td>method</td><td class="mono">2026-11-05</td><td>a)</td></tr>'
    tools = '<span class="seg"><span class="on">By agent</span><span>By focus</span><span>Oldest first</span></span>'
    return f'''{head("P1", "Waits on you", "34 queries from 5 agents · oldest 2026-11-03", tools)}
<section class="panel" {R("P2", "Queries by agent")}><table><thead><tr><th>Query</th><th>What</th><th>Focus</th><th>Since</th><th>Recommended</th></tr></thead><tbody>{body}</tbody></table></section>
<p class="foot" {R("P3", "Answering note")}>Each query opens in its agent's discussions; Kris answers there, or to the agent in Orca. Agora only gathers them.</p>'''


def waits_b():
    allq = [(q + ('ki.prj.agora',)) for q in AGORA_QUERIES] + [(q + ('ki.sop.main',)) for q in SOP_QUERIES]
    allq.sort(key=lambda q: q[3])
    trs = ''.join(f'<tr><td class="mono">{s}</td><td class="mono">{i}</td><td>{escape(t)}</td><td><span class="id">{a}</span></td><td>{f}</td></tr>' for i, t, f, s, r, a in allq)
    tools = '<span class="seg"><span>By agent</span><span>By focus</span><span class="on">Oldest first</span></span>'
    return f'''{head("P1", "Waits on you", "34 queries from 5 agents, oldest first", tools)}
<section class="panel" {R("P2", "Queries oldest first")}><table><thead><tr><th>Since</th><th>Query</th><th>What</th><th>Agent</th><th>Focus</th></tr></thead><tbody>{trs}</tbody></table></section>'''


def macs_a(unheard=False):
    def mac_panel(code, name, rows):
        trs = ''.join(f'<tr><td class="muted">{k}</td><td>{v}</td></tr>' for k, v in rows)
        return f'<section class="panel" {R(code, name)}><header><h2>{name}</h2></header><table><tbody>{trs}</tbody></table></section>'
    sol = mac_panel('P3', 'sol, this Mac', [('Presence', f'{mark("stone")}present'), ('Listens on', '<span class="mono">100.64.0.1:1676</span>'), ('Agora', '0.9.0 · up since 2026-11-05 22:40'), ('Agents', '5, all listening'), ('Checkouts', '64 level, 1 ahead'), ('Last review', '2026-11-06 04:20')])
    terra = mac_panel('P5', 'terra', [('Presence', f'{mark("stone")}present · heard 04:20'), ('Listens on', '<span class="mono">100.64.0.2:1676</span>'), ('Agora', '0.9.0 · up since 2026-11-06 03:20'), ('Agents', '7 · 2 silent'), ('Checkouts', '58 level, 1 diverged'), ('Last review', '2026-11-06 04:18')])
    portal = f'''<section class="panel" {R("P4", "The portal")}><header><h2>The portal</h2><span class="teal">open</span></header><table><tbody>
<tr><td class="muted">Network</td><td>Tailscale, Kris's own</td></tr><tr><td class="muted">Last heard</td><td>04:20 · 18 ms</td></tr>
<tr><td class="muted">This hour</td><td>14 calls · 2 broadcasts · 6 pushes signalled</td></tr><tr><td class="muted">Queued</td><td>Nothing</td></tr>
<tr><td class="muted">State swapped</td><td>04:18</td></tr></tbody></table></section>'''
    return f'''{head("P1", "Macs and the portal", "2 Macs present · the portal is open", '<span class="btn">Sync now</span><span class="btn">Ask after terra now</span>')}
<section class="panel" {R("P2", "The two squares")}><div class="body">{island_svg(height=300)}</div></section>
<div class="grid" style="grid-template-columns: 1fr 1fr 1fr;">{sol}{portal}{terra}</div>'''


def checkouts_a():
    def cond(c):
        cls = 'bad' if 'diverged' in c else 'warn' if ('ahead' in c or 'behind' in c) else ''
        m = mark('diamond') if cls else ''
        return f'<td class="{cls}">{m}{c}</td>'
    trs = ''.join(f'<tr{" class=sel" if "diverged" in t else ""}><td class="mono">{r}</td>{cond(s)}{cond(t)}<td>{"agree" if s == t else "<span class=warn>differ</span>"}</td></tr>' for r, s, t in CHECKOUTS)
    tools = '<span class="seg"><span class="on">Not level</span><span>All 122</span></span><span class="btn">Sync now</span>'
    return f'''{head("P1", "Checkouts", "122 checkouts on 2 Macs · 3 not level", tools)}
<section class="panel" {R("P2", "Checkouts by repository")}><table><thead><tr><th>Repository</th><th>sol</th><th>terra</th><th>The Macs</th></tr></thead><tbody>{trs}</tbody></table></section>
<section class="panel" {R("P3", "Selected checkout")}><div class="body"><b class="mono">hnr/hnr-principal</b> on terra is diverged: ahead 1, behind 2 of origin/main.<span class="sub">The push that went first stands. Agora called hnr.sop.main at 04:12 to bring its commit in on top; it is silent. Agora has left the checkout as it is.</span>
<div style="display:flex;gap:8px;margin-top:10px"><span class="btn">Call hnr.sop.main again</span><span class="btn">Show in Finder</span></div></div></section>'''


def shell_blank(text):
    return f'{head("P1", "Home", text)}<section class="panel"><div class="empty">The page goes here.</div></section>'


# ---------------------------------------------------------------- home as one map (MSG-62774774)
def glance_panel(code='P3'):
    key = ''.join(f'<li><svg viewBox="0 0 18 18">{svg}</svg>{escape(words)}</li>' for svg, words in MV.KEY)
    return f'''<aside class="grid" style="align-content:start; gap:12px" {R(code, "The key")}>
<p class="muted" style="margin:0;font-size:12px">What needs a look, who holds what and the portal now sit on Home (the logo); the toolbar's indicator counts them.</p>
<section class="panel"><header><h2>Key</h2></header><ul class="plain body key">{key}</ul><div class="body"><span class="btn">Show as a list</span></div></section>
</aside>'''


def home_map(plane='both'):
    seg = ''.join(f'<span{" class=on" if plane == k else ""}>{v}</span>' for k, v in (('sol', 'sol'), ('terra', 'terra'), ('both', 'Both planes')))
    summary = {'both': '3 territories · 13 islands · 12 agents on 2 rigs · 2 need a look',
               'sol': "sol's plane · 5 agents and 2 doers at work · terra's 7 dimmed",
               'terra': "terra's plane · 7 agents at work, 2 silent · sol's 5 dimmed"}[plane]
    return f'''{head("P1", "Home", summary, f'<span class="seg" title="Each rig is a plane over the same islands">{seg}</span><span class="btn">Who looks after…</span>')}
<div class="mapwrap"><section class="map" {R("P2", "The map")}>{MV.territory_map(plane=plane)}</section>{glance_panel()}</div>'''


def home_council():
    def col(code, terr, council, focus, host, listen, members):
        rows = ''.join(f'<li>{mark("slashed" if l == "silent" else "hollow" if l == "open" else "stone")}<span class="id">{wid}</span><span class="sub">★ {f} · {h}{" · silent" if l == "silent" else ""}</span></li>' for wid, f, h, l in members)
        c_mark = mark("slashed" if listen == "silent" else "stone")
        return (f'<section class="panel" {R(code, terr)}><header><h2>{terr}</h2></header><div class="body">'
                f'<div class="panel" style="padding:8px 10px; border-color:var(--gold)"><span class="muted" style="font-size:11px">COUNCIL</span><br>{c_mark}<b class="id">{council}</b>'
                f'<span class="sub">★ {focus} · {host}{" · silent" if listen == "silent" else ""}</span></div>'
                f'<div style="border-left:2px solid var(--gold); margin:4px 0 0 14px; padding:4px 0 0 12px"><ul class="plain">{rows}</ul></div></div></section>')
    ki = col('P2', 'Knowledge Islands', 'ki.sop.main', 'themes', 'sol', 'call', [('ki.prj.agora', 'send', 'sol', 'call'), ('Claude Design (doer)', 'identity', 'sol', 'open'), ('ChatGPT (doer)', 'identity', 'sol', 'open')])
    hnr = col('P3', 'Humans Not Robots', 'hnr.sop.main', 'routing', 'terra', 'silent', [('hnr.prj.5g-emerge-phase3', 'delivery', 'terra', 'open'), ('hnr.prj.5g-emerge-p2ms3', 'delivery', 'terra', 'call'), ('hnr.prj.site-robots', 'site', 'terra', 'silent')])
    per = col('P4', 'Personal', 'personal.reg.inbox-sol', 'method', 'sol', 'call', [('personal.reg.inbox-terra', 'method', 'terra', 'call'), ('personal.reg.household-sol', 'rig', 'sol', 'poll'), ('personal.reg.household-terra', 'rig', 'terra', 'call'), ('personal.reg.watchman-sol', 'portal', 'sol', 'call'), ('personal.reg.watchman-terra', 'portal', 'terra', 'call')])
    portal = (f'<section class="panel" {R("P5", "The planar portal")} style="border-color:var(--gold)"><div class="body" style="display:flex; gap:16px; align-items:center">'
              f'<span class="teal">{glyph("portal")}</span><b>The planar portal</b><span class="muted">on its own island, ki-portal, kept by the watchman · sol ⇄ terra · open · heard 04:20 · 14 calls, 2 broadcasts this hour</span></div></section>')
    return f'''{head("P1", "Home", "The councils and who talks to them · 12 agents on 2 Macs")}
<div class="grid" style="grid-template-columns: repeat(3, 1fr);">{ki}{hnr}{per}</div>{portal}
<p class="foot">Work packages talk up to their territory's council; the councils talk to each other on each Mac, through the principal portals; the planar portal, on ki-portal, joins the planes, sol and terra.</p>'''


def doc_tab():
    tabs = [('Home', False, False), ('ki.prj.agora · messages.md', True, True), ('Agora app pack · README', False, True)]
    body = '''<article class="doc panel" style="padding:16px 20px" data-region="P2" data-label="The document">
<div class="muted" style="font-size:12px">ki-principal · +/_WORK/ki.prj.agora/messages.md · read only · updated 04:21</div>
<h2>Inbound</h2><ul>
<li><b>DESIGN-4</b> · from Claude Design (information architect) · 04:19: the Agora app design pack is ready to look at</li>
<li><b>ACK MSG-62774774</b> · from Claude Design · 04:16: reworking the pack's home as one map</li>
<li><b>DESIGN-3</b> · from Claude Design (identity doer) · 04:03: a first sketch of the who's-doing-what window</li>
<li><b>DESIGN-2</b> · from Claude Design (identity doer) · 04:01: the calmer tray menu</li>
<li><b>DESIGN-1</b> · from Claude Design (identity doer) · 03:58: three architecture diagrams</li></ul>
<h2>Outbound</h2><ul>
<li><b>MSG-1088cfd8 HEALTH</b> · to ki.sop.main · listener 120 min · awaiting ACK</li>
<li><b>MSG-1c1bdb12 AWAY-UNTIL-0800</b> · to hnr.sop.main · 03:31 GMT · awaiting ACK</li></ul></article>'''
    side = f'''<aside class="panel" {R("P3", "About this document")}><header><h2>About this document</h2></header><ul class="plain body">
<li>Belongs to <span class="id">ki.prj.agora</span> on sol</li><li>Read by Agora's watch; a new line calls the package</li><li>Opened from 3.1 What's being said</li></ul>
<div class="body" style="display:flex;gap:8px"><span class="btn">Open in the editor</span><span class="btn">Show in Finder</span></div></aside>'''
    content = f'''{head("P1", "ki.prj.agora · messages.md", "A document open in a tab, beside the map")}
<div class="grid" style="grid-template-columns: 1fr 300px;">{body}{side}</div>'''
    return page("What's being said", content, tabs=tabs)


# ---------------------------------------------------------------- the working map: the preferred home (1f, 1g, 1h)
def map_toolbar(focused=True, plane='both', zoom=None, code='P2'):
    """Above the map: the filter, the plane, the zoom, and the list."""
    show = ''.join(f'<span{" class=on" if on else ""}>{w}</span>' for w, on in (('Focused', focused), ('Everything', not focused)))
    planes = ''.join(f'<span{" class=on" if plane == k else ""}>{v}</span>' for k, v in (('sol', 'sol'), ('terra', 'terra'), ('both', 'Both planes')))
    level = '155%' if zoom else '100%'
    return (f'<div class="mapbar" {R(code, "Toolbar")}>'
            f'<span class="lbl">Show</span><span class="seg" title="Focused shows only active islands and what touches them">{show}</span>'
            f'<span class="lbl">Plane</span><span class="seg" title="Each rig is a plane over the same islands">{planes}</span>'
            f'<span class="lbl">Zoom</span><span class="zoomset"><span class="btn icon" aria-label="Zoom out">−</span><span class="mono lvl">{level}</span>'
            f'<span class="btn icon" aria-label="Zoom in">+</span><span class="btn">Fit</span></span>'
            f'<span class="sp"></span><span class="btn">Show as a list</span></div>')


def key_strip(code='P5'):
    items = ''.join(f'<span><svg viewBox="0 0 18 18" aria-hidden="true">{svg}</svg>{escape(w)}</span>' for svg, w in MV.STRIP)
    return f'<div class="strip" {R(code, "Key")}>{items}</div>'


# What the right tray shows for a selected island. Placeholders until the live roster and /v1/state supply them.
ISLAND_DETAIL = {
    'apps-agora.local': dict(
        terr='Knowledge Islands', repo='knowledgeislands/apps-agora.local',
        facts=[('Island portal', 'lit · 1 listening · up to ki-principal'),
               ('Checkouts', 'sol level · terra level')],
        workers=[('stone', 'ki.prj.agora', 'enabler · sol', 'answered 04:12'), ('doer', 'Claude Design', 'doer · sol', 'on open'),
                 ('doer', 'ChatGPT', 'doer · sol', 'on open')],
        queued=[('Run-once jobs', 'ki.prj.agora · since 11-05'), ('Floating doers', 'ki.prj.agora · since 11-05'),
                ('Home as a working map', 'Claude Design · since 04:16'), ('Menu-bar ring', 'Claude Design · since 04:01')],
        waiting=[('DESIGN-4', 'Claude Design · 04:19 · the design pack is ready'), ('MARK-ROLLOUT', 'inbox-terra · 04:08 · terra has the new Agora')],
        waits=('10 queries wait on you', 'AGORA-COUNT-PLACE, MARK-WORDS and 8 more'),
        actions=[('brass', 'Open its 10 queries'), ('', 'Open messages.md')]),
    'ki-portal': dict(
        terr='Personal', repo='krisb/ki-portal', note='Holds the planar portal, which joins the planes, sol and terra.',
        facts=[('Planar portal', '<span class="teal">open</span> · sol ⇄ terra'), ('Last heard', 'terra 04:20 · 18 ms'),
               ('This hour', '14 calls · 2 broadcasts'), ('Queued for terra', 'Nothing'), ('Talks up to', 'principal portal, inbox')],
        workers=[('stone', 'personal.reg.watchman-sol', 'enabler · sol', 'answered 04:10'),
                 ('stone', 'personal.reg.watchman-terra', 'enabler · terra', 'answered 04:09')],
        queued=[],
        waiting=[('PORTAL-ISLAND', 'ki.prj.agora · 04:15 · the planar portal moves here')],
        waits=None,
        actions=[('', 'Ask after terra now'), ('', 'Open Macs and the portal')]),
    'hnr-principal': dict(
        terr='Humans Not Robots', repo='hnr/hnr-principal', note='The principal island: its portal is the principal portal.',
        attention='Diverged on terra: ahead 1, behind 2 · hnr.sop.main silent since 02:10',
        facts=[('Principal portal', 'lit · its council silent'), ('Checkouts', 'sol level · <span class="bad">terra diverged</span>'),
               ('Talks across to', 'ki-principal, inbox')],
        workers=[('slashed', 'hnr.sop.main', 'council · terra', '2 calls unanswered')],
        queued=[('Site domain move', 'hnr.sop.main · since 11-04'), ('P2MS3 dates', 'hnr.sop.main · since 11-05')],
        waiting=[('AWAY-UNTIL-0800', 'ki.prj.agora · 03:31'), ('HEALTH', 'Agora on terra · 03:50'),
                 ('DIVERGED', 'Agora on sol · 04:12'), ('ROUTE-5G', 'ki.sop.main · 04:02')],
        waits=('2 queries wait on you', 'SITE-DOMAIN, P2MS3-DATES'),
        actions=[('brass', 'Open its 2 queries'), ('', 'Call hnr.sop.main again')]),
}


def island_detail(name, code='P4'):
    d = ISLAND_DETAIL[name]
    q, m = MV.COUNTS[name]
    glyphs = {'stone': mark('stone'), 'slashed': mark('slashed'),
              'doer': '<svg class="g" viewBox="0 0 12 12"><rect x="2.2" y="2.2" width="7.6" height="7.6" rx="1" fill="none" stroke="currentColor" stroke-width="1.4"/></svg>'}
    facts = ''.join(f'<tr><td class="muted">{k}</td><td>{v}</td></tr>' for k, v in d['facts'])
    workers = ''.join(f'<tr{" class=bad" if g == "slashed" else ""}><td>{glyphs[g]}<span class="id">{escape(w)}</span><span class="sub">{r} · {h}</span></td></tr>' for g, w, r, h in d['workers'])
    def more(rows, n=2):
        return f'<tr><td class="muted">and {len(rows) - n} more</td></tr>' if len(rows) > n else ''
    queued = (''.join(f'<tr><td>{escape(t)}<span class="sub">{escape(s)}</span></td></tr>' for t, s in d['queued'][:2]) + more(d['queued'])) or '<tr><td class="muted">Nothing queued</td></tr>'
    waiting = (''.join(f'<tr><td><span class="mono">{escape(t)}</span><span class="sub">{escape(s)}</span></td></tr>' for t, s in d['waiting'][:2]) + more(d['waiting'])) or '<tr><td class="muted">Nothing waiting</td></tr>'
    attn = f'<p class="warn attn">{mark("diamond")}<b>Needs a look</b><span class="sub">{escape(d["attention"])}</span></p>' if d.get('attention') else ''
    note = f'<p class="sub tnote">{escape(d["note"])}</p>' if d.get('note') else ''
    waits = (f'<tr class="group"><td>Waits on you</td></tr><tr><td><b>{d["waits"][0]}</b><span class="sub">{d["waits"][1]}</span></td></tr>'
             if d['waits'] else '<tr class="group"><td>Waits on you</td></tr><tr><td class="muted">Nothing</td></tr>')
    acts = ''.join(f'<span class="btn{" brass" if c else ""}">{t}</span>' for c, t in d['actions'])
    return f'''<aside class="panel itray" {R(code, "Island detail")}>
<header><h2><span class="id">{name}</span></h2><span class="x" aria-label="Close">×</span></header>
<div class="tbody"><p class="sub tsub">Island in {d["terr"]}<br><span class="mono nowrap">{d["repo"]}</span></p>{note}{attn}
<table class="kv"><tbody>{facts}</tbody></table>
<table><tbody><tr class="group"><td>Working here <span class="muted">· {len(d["workers"])}</span></td></tr>{workers}
<tr class="group"><td>Queued work <span class="muted">· {q}</span></td></tr>{queued}
<tr class="group"><td>Waiting messages <span class="muted">· {m}</span></td></tr>{waiting}
{waits}</tbody></table></div>
<div class="tacts">{acts}</div></aside>'''


def map_hint(zoom=None, code='P6'):
    if zoom:
        return (f'<div class="mapover" {R(code, "Overview and pan")}><div class="ovtitle">Overview <span class="muted">· drag the frame to pan</span></div>'
                f'{MV.overview(zoom)}</div>')
    return f'<div class="maphint" {R(code, "Pan and zoom")}>Drag to pan · pinch or scroll to zoom · click an island for its detail</div>'


def home_working(focused=True, plane='both', selected='apps-agora.local', zoom=None):
    active = MV.active_islands(plane)
    if zoom:
        summary = 'Closer on Humans Not Robots · 155% · 3 islands, all active · 1 silent, 1 diverged'
    elif focused:
        summary = f'Focused · {len(active)} of {len(MV.ISLANDS)} islands active · 2 need a look · 34 queries wait on you'
    else:
        summary = f'Everything · {len(MV.ISLANDS)} islands in 3 territories, {len(active)} active · 2 need a look · 34 queries wait on you'
    tray = island_detail(selected) if selected else glance_panel('P4')
    return f'''{head("P1", "Home", summary)}
<div class="stage"><section class="mapcol">{map_toolbar(focused, plane, zoom)}
<div class="mapcanvas" {R("P3", "The map")}>{MV.working_map(plane=plane, focused=focused, selected=selected, zoom=zoom)}{map_hint(zoom)}</div>
{key_strip()}</section>{tray}</div>'''


# ================================================================ Agora Atlas: the shell for every page (0.3)
# The shell other designers call: atlas_page(active, content, tray=None, bottom=None, context=...).
# Regions: N1 toolbar, N2 sidebar groups, N3 sidebar foot, N4 tab strip, C1 context control,
# P1/P2... the page's own (the caller marks them), T1 the right tray, B1 the bottom pane.
# The shell marks N and C only when mark_shell=True; T1 and B1 are marked by their frames.

ATLAS_GLYPHS = {
    'roadmap': '<path d="M4 6h16M4 12h10M4 18h13"/><circle cx="19" cy="12" r="1.6" fill="currentColor" stroke="none"/>',
    'jobs': '<circle cx="12" cy="12" r="8.5"/><path d="M12 7v5l3.5 2"/>',
    'guilds': '<path d="M12 3l7.5 3v5.5c0 4.5-3.2 7.8-7.5 9.5-4.3-1.7-7.5-5-7.5-9.5V6z"/>',
    'accounts': '<circle cx="12" cy="8.5" r="3.8"/><path d="M4.5 20c.8-3.8 3.8-6 7.5-6s6.7 2.2 7.5 6"/>',
    'settings': '<circle cx="12" cy="12" r="3"/><path d="M12 2.8v3M12 18.2v3M2.8 12h3M18.2 12h3M5.5 5.5l2.1 2.1M16.4 16.4l2.1 2.1M5.5 18.5l2.1-2.1M16.4 7.6l2.1-2.1"/>',
    'updates': '<path d="M19.5 12a7.5 7.5 0 1 1-2.2-5.3"/><path d="M19.5 4v4h-4"/>',
    'repositories': '<path d="M5 4.5h14M5 9.5h14M5 14.5h14M5 19.5h9"/>',
    'activity': '<path d="M3 12h4l2.5-6 5 12 2.5-6h4"/>',
    'captured': '<rect x="5" y="5" width="14" height="14" rx="1.5"/>',
    'context': '<path d="M12 4l8 8-8 8-8-8z"/>',
    'curated': '<circle cx="12" cy="12" r="7.5"/>',
    'actions': '<path d="M12 4.5l8 14H4z"/>',
    'graph': '<circle cx="6" cy="7" r="2.2"/><circle cx="18" cy="7" r="2.2"/><circle cx="12" cy="18" r="2.2"/><path d="M8 8l3 8M16 8l-3 8M8.2 7h7.6"/>',
    'tending': '<path d="M12 20V10M12 10c0-3.5 2.5-6 6.5-6 0 3.5-2.5 6-6.5 6zM12 13c0-2.8-2-4.8-5.5-4.8 0 2.8 2 4.8 5.5 4.8z"/>',
    'key': '<circle cx="8" cy="12" r="3.8"/><path d="M11.8 12H21M17.5 12v3M20.5 12v2.5"/>',
    'gallery': '<rect x="3.5" y="5" width="17" height="14" rx="1.5"/><path d="M3.5 16l5-5 4 4 3-3 5 5"/>',
    'search': '<circle cx="10.5" cy="10.5" r="6"/><path d="M15 15l5.5 5.5"/>',
    'sidebar': '<rect x="3.5" y="4.5" width="17" height="15" rx="2.5"/><path d="M9 4.5v15"/>',
    'pin': '<path d="M9 3.5h6l-1.2 6 3.6 3.6H6.6l3.6-3.6zM12 13.1V20.5"/>',
    'theme': '<circle cx="12" cy="12" r="8"/><path d="M12 4a8 8 0 0 1 0 16z" fill="currentColor" stroke="none"/>',
    'chev': '<path d="M8 10l4 4 4-4"/>',
    'chevr': '<path d="M10 8l4 4-4 4"/>',
    'lantern': '<path d="M9 3.5h6M12 3.5v2M8 7.5h8l-.8 11H8.8zM8 18.5h8"/><circle cx="12" cy="13" r="1.5" fill="currentColor" stroke="none"/>',
    'beacon': '<circle cx="12" cy="12" r="2" fill="currentColor" stroke="none"/><path d="M12 3.5v3M12 17.5v3M3.5 12h3M17.5 12h3"/><circle cx="12" cy="12" r="5.5"/>',
    # Known Lands: an old chart rolled at its left edge, a dotted path to an X.
    'lands': '<path d="M6.5 4.5H19.5V17"/><path d="M19.5 17a2 2 0 0 1-2 2H4.5V6.5a2 2 0 0 1 4 0V19"/>'
             '<path d="M10.5 16.2l1.8-2.6 2.2.4 1.6-2.8" stroke-dasharray="0 2.3" stroke-width="1.9"/>'
             '<path d="M14.6 6.6l2.8 2.8M17.4 6.6l-2.8 2.8" stroke-width="1.7"/>',
    'bell': '<path d="M6.5 16.5V11a5.5 5.5 0 0 1 11 0v5.5l1.5 2h-14z"/><path d="M10 20.5a2 2 0 0 0 4 0"/>',
    'more': '<circle cx="6" cy="12" r="1.4" fill="currentColor" stroke="none"/><circle cx="12" cy="12" r="1.4" fill="currentColor" stroke="none"/><circle cx="18" cy="12" r="1.4" fill="currentColor" stroke="none"/>',
}


def aglyph(name, cls=''):
    """A glyph from the Atlas set, falling back to the pack's own."""
    if name not in ATLAS_GLYPHS:
        return glyph(name, cls)
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ATLAS_GLYPHS[name]}</svg>')


# The sidebar, top to bottom: (group id, heading or None, collapsible, [(place id, label, glyph, count, note)]).
# A count is shown only where something waits or wants a look; a note is a muted word such as "soon".
ATLAS_GROUPS = [
    ('agora', 'Agora', False, [
        ('home', 'Home', 'home', '', ''),
        ('here', "Who's doing what", 'here', '12', ''),
        ('said', "What's being said", 'said', '', ''),
        ('broadcasts', 'Broadcasts', 'broadcast', '', ''),
        ('waits', 'Waits on you', 'waits', '34', ''),
        ('macs', 'Macs and the portal', 'macs', '', ''),
        ('checkouts', 'Checkouts', 'checkouts', '1', ''),
    ]),
    ('work', 'Work', False, [
        ('roadmap', 'Roadmap', 'roadmap', '', ''),
        ('jobs', 'Jobs', 'jobs', '1', ''),
    ]),
    ('guilds', None, False, [
        ('guilds', 'Guilds', 'guilds', '', ''),
    ]),
    ('observatory', 'Observatory', False, [
        ('repositories', 'Repositories', 'repositories', '', ''),
        ('activity', 'Activity', 'activity', '', ''),
    ]),
    ('kiv', 'KIV', True, [
        ('kiv-captured', 'Captured', 'captured', '', 'soon'),
        ('kiv-context', 'Context', 'context', '', 'soon'),
        ('kiv-curated', 'Curated', 'curated', '', 'soon'),
        ('kiv-actions', 'Actions', 'actions', '', 'soon'),
        ('kiv-graph', 'Graph atlas', 'graph', '', 'soon'),
        ('kiv-tending', 'Tending', 'tending', '', 'soon'),
        ('kiv-key', 'Key', 'key', '', 'soon'),
    ]),
    ('coming', 'Coming', False, [
        ('gallery', 'Art gallery', 'gallery', '', 'later'),
    ]),
]
# The foot: the places about the Mac and the app itself, not the work.
ATLAS_FOOT = [
    ('accounts', 'Accounts', 'accounts', '1', ''),
    ('settings', 'Settings', 'settings', '', ''),
    ('updates', 'Updates', 'updates', '', ''),
]
# Which context each place honours: territory, plane, both or neither (the context control greys what a page ignores).
ATLAS_CONTEXT = {
    'home': ('territory', 'plane'), 'here': ('territory', 'plane'), 'said': ('territory', 'plane'),
    'broadcasts': ('plane',), 'waits': ('territory',), 'macs': ('plane',), 'checkouts': ('territory', 'plane'),
    'roadmap': ('territory',), 'jobs': ('territory', 'plane'), 'guilds': ('territory',),
    'repositories': ('territory',), 'activity': ('territory',), 'accounts': ('plane',),
    'settings': ('plane',), 'updates': ('plane',), 'lands': ('territory', 'plane'),
}
ATLAS_TERRITORIES = ['All territories', 'Knowledge Islands', 'Humans Not Robots', 'Personal']
ATLAS_SECTIONS = [('agora', 'Agora'), ('work', 'Work'), ('guilds', 'Guilds'), ('observatory', 'Observatory'), ('kiv', 'KIV')]


def _place_label(place_id):
    for _, _, _, items in ATLAS_GROUPS:
        for pid, label, *_ in items:
            if pid == place_id:
                return label
    for pid, label, *_ in ATLAS_FOOT:
        if pid == place_id:
            return label
    for *_, items in ATLAS_SECTIONS4:
        for pid, label, *_ in items:
            if pid == place_id:
                return label
    return place_id


def _group_of(place_id):
    for gid, _, _, items in ATLAS_GROUPS:
        if any(pid == place_id for pid, *_ in items):
            return gid
    return None


def _nav_item(pid, label, g, n, note, active):
    note_html = f'<span class="note">{note}</span>' if note else ''
    n_html = f'<span class="n">{n}</span>' if n else ''
    cls = 'at-nav' + (' on' if pid == active else '') + (' soon' if note else '')
    return (f'<div class="{cls}" data-place="{pid}" title="{escape(label)}">{aglyph(g)}<span class="label">{escape(label)}</span>'
            f'{n_html}{note_html}</div>')


def atlas_sidebar(active, collapsed=('kiv',), mark_shell=False, only=None):
    """The grouped sidebar. collapsed names the groups folded to their heading; only keeps one section (alternative 0.3e)."""
    m = (lambda c, l: R(c, l)) if mark_shell else (lambda c, l: '')
    groups = []
    for gid, heading, foldable, items in ATLAS_GROUPS:
        if only and gid != only:
            continue
        shut = gid in collapsed and _group_of(active) != gid
        head = ''
        if heading:
            chev = aglyph('chevr' if shut else 'chev', 'chev') if foldable else ''
            count = f'<span class="n">{len(items)}</span>' if shut else ''
            soon = '<span class="note">soon</span>' if gid == 'kiv' else ''
            head = f'<h4>{chev}<span>{escape(heading)}</span>{soon}{count}</h4>'
        body = '' if shut else ''.join(_nav_item(*it, active) for it in items)
        groups.append(f'<div class="at-group{" shut" if shut else ""}{" lone" if not heading else ""}" data-group="{gid}">{head}{body}</div>')
    foot = ''.join(_nav_item(*it, active) for it in ATLAS_FOOT) if not only else ''
    portal = (f'<div class="at-portal"><span class="teal">{glyph("portal")}</span><span class="text"><b>sol ⇄ terra</b>'
              f'<span class="sub">Portal open · heard 04:20</span></span></div>'
              f'<div class="at-devices"><span title="Agora Beacon, in the menu bar on each Mac">{aglyph("beacon")}<span class="label">Beacon on sol</span></span>'
              f'<span title="Agora Lantern, on the iPhone">{aglyph("lantern")}<span class="label">Lantern 04:18</span></span></div>')
    if only:
        foot_html = f'<div class="at-foot" {m("N3", "Sidebar foot")}>{portal}</div>'
    else:
        foot_html = f'<div class="at-foot" {m("N3", "Sidebar foot")}>{foot}{portal}</div>'
    return (f'<aside class="at-side"><div class="at-groups" {m("N2", "Sidebar groups")}>{"".join(groups)}</div>'
            f'{foot_html}</aside>')


# ---------------------------------------------------------------- the revised sidebar (0.4, Kris's review 22:55 to 23:20 GMT)
# Home leaves the sidebar: the Agora Atlas logo in the toolbar is Home, as on a website. Every place sits in a section
# with a small eyebrow, every section folds, and folded to icons each keeps a three-letter eyebrow.
# (section id, eyebrow, three letters, [(place id, label, glyph, count, note)]). SYS sits at the foot, above the portal line.
ATLAS_SECTIONS4 = [
    ('agora', 'Agora', 'AGO', [
        ('here', "Who's doing what", 'here', '12', ''),
        ('said', "What's being said", 'said', '', ''),
        ('broadcasts', 'Broadcasts', 'broadcast', '', ''),
        ('waits', 'Waits on you', 'waits', '34', ''),
        ('macs', 'Macs and the portal', 'macs', '', ''),
        ('checkouts', 'Checkouts', 'checkouts', '1', ''),
    ]),
    ('work', 'Work', 'WRK', [
        ('lands', 'Known Lands', 'lands', '', ''),
        ('roadmap', 'Roadmap', 'roadmap', '', ''),
        ('jobs', 'Jobs', 'jobs', '1', ''),
        ('gallery', 'Art gallery', 'gallery', '', 'later'),
    ]),
    ('guilds', 'Guilds', 'GLD', [
        ('guilds', 'Guilds', 'guilds', '', ''),
    ]),
    ('observatory', 'Observatory', 'OBS', [
        ('repositories', 'Repositories', 'repositories', '', ''),
        ('activity', 'Activity', 'activity', '', ''),
    ]),
    ('kiv', 'KIV', 'KIV', [
        ('kiv-captured', 'Captured', 'captured', '', 'soon'),
        ('kiv-context', 'Context', 'context', '', 'soon'),
        ('kiv-curated', 'Curated', 'curated', '', 'soon'),
        ('kiv-actions', 'Actions', 'actions', '', 'soon'),
        ('kiv-graph', 'Graph atlas', 'graph', '', 'soon'),
        ('kiv-tending', 'Tending', 'tending', '', 'soon'),
        ('kiv-key', 'Key', 'key', '', 'soon'),
    ]),
    ('sys', 'System', 'SYS', [
        ('accounts', 'Accounts', 'accounts', '1', ''),
        ('settings', 'Settings', 'settings', '', ''),
        ('updates', 'Updates', 'updates', '', ''),
    ]),
]


def _section4(sid, eyebrow, abbr, items, active, collapsed):
    shut = sid in collapsed and not any(pid == active for pid, *_ in items)
    waiting = [n for _, _, _, n, _ in items if n]
    count = f'<span class="n" title="{len(items)} places folded">{len(items)}</span>' if shut else ''
    soon = '<span class="note">soon</span>' if sid == 'kiv' else ''
    flag = (f'<span class="wait" title="{len(waiting)} inside {"wants" if len(waiting) == 1 else "want"} a look">{len(waiting)} to look at</span>'
            if shut and waiting else '')
    head_ = (f'<h4 title="{"Open" if shut else "Fold"} {escape(eyebrow)}">{aglyph("chevr" if shut else "chev", "chev")}'
             f'<span class="full">{escape(eyebrow)}</span><span class="abbr">{abbr}</span>{soon}{flag}{count}</h4>')
    body = '' if shut else ''.join(_nav_item(*it, active) for it in items)
    return f'<div class="at-group{" shut" if shut else ""}" data-group="{sid}">{head_}{body}</div>'


def atlas_sidebar4(active, collapsed=('kiv',), mark_shell=False):
    """The revised sidebar (0.4): sections with eyebrows, every one folding; SYS at the foot above the portal line."""
    m = (lambda c, l: R(c, l)) if mark_shell else (lambda c, l: '')
    groups = ''.join(_section4(*sec, active, collapsed) for sec in ATLAS_SECTIONS4 if sec[0] != 'sys')
    sys_ = _section4(*ATLAS_SECTIONS4[-1], active, collapsed)
    portal = (f'<div class="at-portal"><span class="teal">{glyph("portal")}</span><span class="text"><b>sol ⇄ terra</b>'
              f'<span class="sub">Portal open · heard 04:20</span></span></div>'
              f'<div class="at-devices"><span title="Agora Beacon, in the menu bar on each Mac">{aglyph("beacon")}<span class="label">Beacon on sol</span></span>'
              f'<span title="Agora Lantern, on the iPhone">{aglyph("lantern")}<span class="label">Lantern 04:18</span></span></div>')
    return (f'<aside class="at-side v4"><div class="at-groups" {m("N2", "Sidebar sections")}>{groups}</div>'
            f'<div class="at-foot" {m("N3", "Sidebar foot: SYS and the portal")}>{sys_}{portal}</div></aside>')


def atlas_toolbar(mark_shell=False, standing=('ok', 'All well'), sections=None, brand='', mark_logo=False):
    """The toolbar across the window: the name, the rigs, the word on the whole, the search, speaking to everyone.
    brand: '' (0.3, a name only), 'home' (0.4, the logo is Home), 'here' (0.4, Home is open) or 'hover' (0.4, the tooltip shown)."""
    m = R('N1', 'Toolbar') if mark_shell else ''
    level, words = standing
    secs = ''
    if sections:
        secs = '<span class="seg at-sections">' + ''.join(
            f'<span{" class=on" if sid == sections else ""}>{label}</span>' for sid, label in ATLAS_SECTIONS) + '</span>'
    gear = f'<span class="at-icon" title="Accounts, Settings, Updates">{aglyph("settings")}</span>' if sections else ''
    return f'''<header class="at-top" {m}>
<span class="at-lights"><i></i><i></i><i></i></span>
<span class="at-icon" title="Show or hide the sidebar (⌘\\)">{aglyph("sidebar")}</span>
{_brand(brand, mark_logo)}
{secs}
<span class="at-rigs"><span class="chip rig here">sol</span><span class="chip rig">terra</span></span>
<span class="at-standing {level}"><span class="dot"></span>{escape(words)}</span>
<span class="at-search">{aglyph("search")}<span>{"Find anything" if sections else "Find a place, island, record or skill"}</span><kbd>/</kbd></span>
<span class="sp"></span>
<span class="btn">{glyph("mark")}Mark all</span><span class="btn">{glyph("away")}Away…</span><span class="btn">{glyph("broadcast")}Broadcast…</span>
<span class="mono at-clock">04:20</span>{gear}
<span class="at-icon" title="Keep on top, or snap">{aglyph("pin")}</span><span class="at-icon" title="Theme: follows the Mac">{aglyph("theme")}</span>
</header>'''


def _brand(brand, mark_logo=False):
    if not brand:
        return f'<span class="at-brand">{glyph("ring")}<span class="name">Agora Atlas</span></span>'
    cls = 'at-brand home' + (' here' if brand == 'here' else '') + (' hover' if brand == 'hover' else '')
    tip = '<span class="at-tip" role="tooltip">Home</span>' if brand == 'hover' else ''
    mark = R('N5', 'Logo: Home') if mark_logo else ''
    cur = ' aria-current="page"' if brand == 'here' else ''
    return f'<span class="{cls}" {mark} title="Home"{cur}>{glyph("ring")}<span class="name">Agora Atlas</span>{tip}</span>'


# ================================================================ the compact bar (0.5, Kris's review 23:05 GMT)
# One 36-point row. The rigs become one presence control when they do not fit as chips; the counts become one
# notification indicator that leads to Home's Needs a look; every control says what it is in a tooltip.
HOSTS = {
    1: [('sol', 'present', 'this Mac')],
    2: [('sol', 'present', 'this Mac'), ('terra', 'present', 'heard 04:20')],
    10: [('sol', 'present', 'this Mac'), ('terra', 'present', 'heard 04:20'), ('luna', 'present', 'heard 04:20'),
         ('ceres', 'present', 'heard 04:19'), ('vesta', 'present', 'heard 04:20'), ('pallas', 'present', 'heard 04:18'),
         ('juno', 'unknown', 'last heard 03:12'), ('hygiea', 'present', 'heard 04:20'), ('eris', 'gone', 'said goodbye 5 Nov 22:40'),
         ('io', 'present', 'heard 04:17')],
}
PRESENCE_WORDS = {'present': 'present', 'unknown': 'not heard from', 'gone': 'gone'}
PRESENCE_RANK = {'present': 0, 'unknown': 1, 'gone': 2}
# The notification indicator: (level, count, the tooltip's words). level is 'none', 'look' or 'urgent'.
NOTICES = {
    'none': ('none', 0, 'Nothing needs a look'),
    'look': ('look', 3, '3 need a look: 2 checkouts must settle, the job sop-digest failed, 34 queries wait on you'),
    'urgent': ('urgent', 4, '4 need a look, 1 urgent: hnr.sop.main is silent on terra; 2 checkouts must settle; a job failed; 34 queries wait'),
}
CHIP_ROOM = 3  # at 1440 points, up to three rigs fit as chips; more fold into the presence control


def pmark(state):
    """Presence by shape: present a solid dot, not heard from a dashed ring, gone a slashed ring."""
    return {'present': '<svg class="pm" viewBox="0 0 12 12"><circle cx="6" cy="6" r="3.6" fill="currentColor"/></svg>',
            'unknown': '<svg class="pm" viewBox="0 0 12 12"><circle cx="6" cy="6" r="3.6" fill="none" stroke="currentColor" stroke-width="1.4" stroke-dasharray="2 1.5"/></svg>',
            'gone': '<svg class="pm" viewBox="0 0 12 12"><circle cx="6" cy="6" r="3.6" fill="none" stroke="currentColor" stroke-width="1.4"/><path d="M3.3 8.7 L8.7 3.3" stroke="currentColor" stroke-width="1.4"/></svg>'}[state]


def nmark(level):
    return {'none': '<svg class="nm" viewBox="0 0 12 12"><path d="M2.8 6.3 L5 8.5 L9.4 3.8" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
            'look': '<svg class="nm" viewBox="0 0 12 12"><path d="M6 1.5 L10.5 6 L6 10.5 L1.5 6 Z" fill="currentColor"/></svg>',
            'urgent': '<svg class="nm" viewBox="0 0 12 12"><path d="M6 1.3 L11 10.4 H1 Z" fill="currentColor"/></svg>'}[level]


def tip(words, cls=''):
    return f'<span class="at-tip{(" " + cls) if cls else ""}" role="tooltip">{words}</span>'


def presence_control(hosts, open_=False, show_tip=False, mark=''):
    worst = max(hosts, key=lambda h: PRESENCE_RANK[h[1]])[1]
    bad = [h for h in hosts if h[1] != 'present']
    summary_words = ((f'{hosts[0][0]}, {hosts[0][2]}, present' if len(hosts) == 1 else f'All {len(hosts)} present') if not bad else
                     ', '.join(f'{h[0]} {PRESENCE_WORDS[h[1]]}' for h in bad))
    tip_words = (f'{len(hosts)} {"rig" if len(hosts) == 1 else "rigs"} in the group · {summary_words}. Click for the list.')
    if len(hosts) <= CHIP_ROOM and not open_:
        chips = ''.join(f'<span class="chip rig st-{st}{" here" if i == 0 else ""}">{pmark(st)}{n}</span>' for i, (n, st, _) in enumerate(hosts))
        inner = f'<span class="at-chips">{chips}</span>'
        cls = 'at-presence chips'
    else:
        short = {'gone': 'gone', 'unknown': 'unheard'}
        word = (' · '.join(f'{sum(1 for h in bad if h[1] == k)} {short[k]}' for k in ('gone', 'unknown') if any(h[1] == k for h in bad))
                if bad else 'all present')
        inner = (f'<span class="pbtn st-{worst}">{pmark(worst)}<b>{len(hosts)} rigs</b><span class="pw">{word}</span>{aglyph("chev", "chev")}</span>')
        cls = 'at-presence' + (' open' if open_ else '')
    pop = ''
    if open_:
        rows = ''.join(f'<div class="prow st-{st}">{pmark(st)}<b class="mono">{n}</b><span class="pw">{PRESENCE_WORDS[st]}</span>'
                       f'<span class="muted">{heard}</span></div>' for n, st, heard in sorted(hosts, key=lambda h: (-PRESENCE_RANK[h[1]], h[0] != 'sol', h[0])))
        pop = (f'<div class="at-pop" {R("T2", "Pop-out: floats")}><div class="pophead"><b>{len(hosts)} rigs in the group</b>'
               f'<span class="muted">worst first</span></div>{rows}'
               f'<div class="popfoot"><span class="btn">Open Macs and the portal</span><span class="muted">Esc closes</span></div></div>')
    t = tip(escape(tip_words)) if show_tip and not open_ else ''
    return f'<span class="{cls}" {mark} title="{escape(tip_words)}">{inner}{t}{pop}</span>'


def notice_indicator(kind='urgent', show_tip=False, mark=''):
    level, n, words = NOTICES[kind]
    label = 'Nothing' if level == 'none' else (f'{n} · 1 urgent' if level == 'urgent' else f'{n} to look at')
    t = tip(escape(words) + '<span class="tsub">Click: Home, Needs a look</span>', 'wide right') if show_tip else ''
    return (f'<span class="at-notice lv-{level}" {mark} title="{escape(words)}. Click for Home, Needs a look.">'
            f'{aglyph("bell")}{nmark(level)}<span class="nw">{label}</span>{t}</span>')


def atlas_bar5(mark_shell=False, brand='home', hosts=2, notices='urgent', popout=None, tips=(), mark_logo=False):
    """The compact bar (0.5): 36 points; window lights, sidebar, logo (Home), presence, search, notification indicator,
    speak to everyone as three icon buttons, the time, pin and theme. Every control carries a tooltip in words."""
    m = (lambda c, l: R(c, l)) if mark_shell else (lambda c, l: '')
    hl = HOSTS[hosts] if isinstance(hosts, int) else hosts
    speak = ''.join(f'<span class="at-ibtn" title="{t}">{glyph(g)}</span>' for g, t in (
        ('mark', 'Mark all: tell every listening thread you have read up to now'),
        ('away', 'Away…: open an unattended window for every thread, with an end time'),
        ('broadcast', 'Broadcast…: say something to every listening thread on every rig')))
    speak_tip = tip('Away…: open an unattended window for every thread, with an end time', 'right') if 'speak' in tips else ''
    return f'''<header class="at-top v5" {m("N1", "Compact bar")}>
<span class="at-lights"><i></i><i></i><i></i></span>
<span class="at-icon" title="Show or hide the sidebar (⌘\\)">{aglyph("sidebar")}</span>
{_brand(brand, mark_logo)}
{presence_control(hl, open_=popout == "presence", show_tip="presence" in tips, mark=m("N6", "Presence"))}
<span class="at-search" title="Find a place, island, record or skill (/)">{aglyph("search")}<span>Find</span><kbd>/</kbd></span>
<span class="sp"></span>
{notice_indicator(notices, show_tip="notice" in tips, mark=m("N7", "Notifications"))}
<span class="at-speak" {m("N8", "Speak to everyone")}>{speak}{speak_tip}</span>
<span class="mono at-clock" title="The time on this Mac">04:20</span>
<span class="at-icon" title="Keep on top, or snap">{aglyph("pin")}</span><span class="at-icon" title="Theme: follows the Mac">{aglyph("theme")}</span>
</header>'''


def atlas_tabs(tabs, mark_shell=False):
    m = R('N4', 'Tabs') if mark_shell else ''
    items = ''.join(f'<span class="at-tab{" on" if on else ""}">{escape(t)}{"<span class=x>×</span>" if closable else ""}</span>'
                    for t, on, closable in tabs)
    return f'<div class="at-tabs" {m}>{items}<span class="at-tab add" title="New tab (⌘T)">+</span></div>'


def atlas_context(active, context=None, mark_shell=False):
    """The context control at the top right: the territory and the plane. A dimension the page ignores is greyed, never hidden,
    so the control never moves. context: dict(territory=..., plane='sol'|'terra'|'both', open=False)."""
    ctx = dict(territory='All territories', plane='both', open=False) | (context or {})
    uses = ATLAS_CONTEXT.get(active, ())
    m = R('C1', 'Context') if mark_shell else ''
    t_off = '' if 'territory' in uses else ' off'
    p_off = '' if 'plane' in uses else ' off'
    planes = ''.join(f'<span{" class=on" if ctx["plane"] == k else ""}>{v}</span>' for k, v in (('sol', 'sol'), ('terra', 'terra'), ('both', 'Both')))
    menu = ''
    if ctx['open']:
        rows = ''.join(f'<div class="opt{" on" if t == ctx["territory"] else ""}">{"✓" if t == ctx["territory"] else ""}<span>{t}</span></div>'
                       for t in ATLAS_TERRITORIES)
        menu = (f'<div class="at-menu">{rows}<div class="hint">Every page that reads territories follows this. ⌘1 to ⌘4 choose.</div></div>')
    ignored = []
    if t_off:
        ignored.append('territory')
    if p_off:
        ignored.append('plane')
    title = f' title="{_place_label(active)} does not use the {" or ".join(ignored)}"' if ignored else ''
    return (f'<div class="at-context" {m}{title}>'
            f'<span class="lbl{t_off}">Territory</span><span class="at-select{t_off}{" open" if ctx["open"] else ""}">{escape(ctx["territory"])}{aglyph("chev")}{menu}</span>'
            f'<span class="lbl{p_off}">Plane</span><span class="seg{p_off}">{planes}</span></div>')


def tray_frame(kind, title, body, actions=(), code='T1', label='Tray'):
    """The right tray: one selected thing's facts. kind is the small line above the title (what it is and where);
    actions are (style, words) with style '' or 'brass' (at most one brass in the whole view)."""
    acts = ''.join(f'<span class="btn{" brass" if s == "brass" else ""}">{escape(w)}</span>' for s, w in actions)
    foot = f'<footer>{acts}</footer>' if actions else ''
    return (f'<aside class="at-tray" {R(code, label)}><header><div><div class="kind">{escape(kind)}</div>'
            f'<h2>{title}</h2></div><span class="x" title="Close (Escape)">×</span></header>'
            f'<div class="tbody">{body}</div>{foot}</aside>')


def bottom_frame(kind, title, tabs, body, code='B1', label='Bottom pane', height=360):
    """The bottom pane: the selected thing's documents or long readings, in tabs. tabs are (words, on)."""
    strip = ''.join(f'<span class="ptab{" on" if on else ""}">{escape(t)}</span>' for t, on in tabs)
    return (f'<section class="at-bottom" style="height:{height}px" {R(code, label)}><div class="grip" title="Drag to resize"></div>'
            f'<header><div class="kind">{escape(kind)}</div><h2>{title}</h2><span class="x" title="Close (Escape)">×</span></header>'
            f'<div class="ptabs">{strip}</div><div class="pbody">{body}</div></section>')


def atlas_page(active, content, tray=None, bottom=None, context=None, tabs=None, folded=False,
               collapsed=('kiv',), mark_shell=False, theme='night', standing=('ok', 'All well'),
               variant='sidebar', title='Agora Atlas', height=900, shell='0.4', logo=None,
               bar='0.5', hosts=2, notices='urgent', popout=None, tips=()):
    """One Agora Atlas window, 1440 by `height`, around a page.

    active     the sidebar place id, such as 'roadmap', 'jobs', 'guilds' or 'accounts' (see ATLAS_GROUPS, ATLAS_FOOT)
    content    the page's HTML: start it with head('P1', ...) and mark its own regions P2, P3...
    tray       None, or tray_frame(...): the right tray, which pushes the page narrower
    bottom     None, or bottom_frame(...): the bottom pane, under the page and left of the tray
    context    dict(territory='All territories', plane='both', open=False); greyed where the page ignores it
    tabs       [(words, on, closable)]; by default the active place alone
    folded     the sidebar folded to icons
    collapsed  groups folded to their heading; the active place's group always opens
    mark_shell mark N1 to N4 and C1 for the board (the 0.3 page does; view pages leave it off)
    variant    'sidebar' (0.3a, preferred) or 'sections' (0.3e, the alternative)
    height     the window's height in points; None lets a long page grow (at least 900)
    shell      '0.4' (the default: sections with eyebrows, Home on the logo, Known Lands in Work) or '0.3' (the
               superseded grouped sidebar, kept only for 0.3's own boards)
    logo       None (Home is open when active is 'home'), or 'hover' to show the logo's "Home" tooltip (0.4c)
    bar        '0.5' (the default: the compact bar) or '0.4' (the 48-point toolbar of 0.3 and 0.4); shell='0.3' keeps its own
    hosts      1, 2 or 10 (illustrative groups), or a list of (name, 'present'|'unknown'|'gone', heard)
    notices    'none', 'look' or 'urgent': the notification indicator's worst state (0.5)
    popout     None, or 'presence' to show the presence list floating open (0.5c)
    tips       tooltips to draw: any of 'presence', 'notice', 'speak'
    """
    if tabs is None:
        tabs = [(_place_label(active), True, False)]
    v4 = shell != '0.3' and variant == 'sidebar'
    if folded and not v4:
        collapsed = ()  # 0.3: folded to icons, every group fits, so none is shut
    section = _group_of(active) if variant == 'sections' else None
    if v4:
        side = atlas_sidebar4(active, collapsed, mark_shell)
        brand = 'hover' if logo == 'hover' else 'here' if active == 'home' else 'home'
    else:
        side = atlas_sidebar(active, collapsed, mark_shell, only=section) if variant == 'sidebar' else atlas_sidebar(active, (), mark_shell, only=section or 'agora')
        brand = ''
    cls = 'atlas' + (' folded' if folded else '') + (' sections' if variant == 'sections' else '')
    compact = bar == '0.5' and shell != '0.3' and variant == 'sidebar'
    if compact:
        cls += ' v5'
        top = atlas_bar5(mark_shell, brand, hosts, notices, popout, tips, mark_logo=v4 and mark_shell)
    else:
        top = atlas_toolbar(mark_shell, standing, section, brand, mark_logo=v4 and mark_shell)
    size = f'height:{height}px' if height else 'min-height:900px'
    if not height:
        cls += ' grow'  # a long page: the window grows to it rather than clipping
    work = (f'<div class="at-work{" with-tray" if tray else ""}">'
            f'<div class="at-bar">{atlas_tabs(tabs, mark_shell)}{atlas_context(active, context, mark_shell)}</div>'
            f'<div class="at-body"><div class="at-col"><div class="at-page">{content}</div>{bottom or ""}</div>{tray or ""}</div></div>')
    return f'''<!doctype html><html lang="en-GB" data-theme="{theme}"><head><meta charset="utf-8">
<title>{escape(title)}</title><link rel="stylesheet" href="../build/app.css"></head><body>
<div class="{cls}" style="{size}">{top}{side}{work}</div>
</body></html>'''


# ---------------------------------------------------------------- the 0.3 artboards' pages (placeholders for 7.1, 7.2, 8.1)
ROADMAP_ROWS = [
    ('KI-AGORA-WRK-004', 'Run the rig’s scheduled jobs', 'apps-agora.local', 'now', 'P1', 'M', '04:12'),
    ('KI-AGORA-WRK-002', 'Switch Claude accounts', 'apps-agora.local', 'next', 'P2', 'S', '11-05'),
    ('KI-AGORA-WRK-006', 'Run-once jobs', 'apps-agora.local', 'next', 'P2', 'M', '11-05'),
    ('KI-AGORA-WRK-007', 'Floating doers', 'apps-agora.local', 'ready', 'P2', 'L', '11-05'),
    ('KI-OBS-WRK-012', 'Signals land in their view', 'apps-observatory.local', 'ready', 'P2', 'S', '11-04'),
    ('KI-TOOLS-WRK-031', 'ki agent status as JSON', 'tools-ki', 'draft', 'P3', 'S', '11-04'),
    ('KI-DESIGN-WRK-009', 'Tray and pane tokens', 'ki-design', 'draft', 'P3', 'M', '11-03'),
    ('KI-PRIN-WRK-044', 'The guild catalogue', 'ki-principal', 'triage', 'P2', 'M', '11-03'),
    ('KI-AGORA-WRK-008', 'KIV pages as native views', 'apps-agora.local', 'triage', 'P3', 'L', '11-02'),
    ('KI-OBS-WRK-010', 'Activity by territory', 'apps-observatory.local', 'triage', 'P3', 'S', '11-01'),
]


def atlas_roadmap(selected='KI-AGORA-WRK-004'):
    summary = ''.join(f'<tr><td>{t}</td><td class="mono">{a}</td><td class="mono">{b}</td><td class="mono">{c}</td></tr>' for t, a, b, c in (
        ('apps-agora.local', '1', '2', '1'), ('apps-observatory.local', '·', '·', '1'), ('ki-principal', '·', '·', '·'),
        ('tools-ki', '·', '·', '·'), ('ki-design', '·', '·', '·')))
    rows = ''.join(f'<tr{" class=sel" if i == selected else ""}><td class="id">{i}</td><td>{escape(t)}<span class="sub mono">{isl}</span></td>'
                   f'<td><span class="chip">{s}</span></td><td>{p} · {z}</td><td class="muted">{c}</td></tr>'
                   for i, t, isl, s, p, z, c in ROADMAP_ROWS)
    return f'''{head("P1", "Roadmap", "38 open records in Knowledge Islands · 1 now · 2 next")}
<div class="at-split"><section class="panel" {R("P2", "Summary")}><header><h2>By island</h2><span class="muted">now · next · ready</span></header>
<table class="sumtab"><tbody>{summary}</tbody></table></section>
<section style="display:flex; flex-direction:column; gap:10px; min-width:0" {R("P3", "Filters and records")}>
<div class="at-filters"><span class="chip ctx" title="From the context control">Territory: Knowledge Islands · from the context</span><span class="chip">Status: open ×</span>
<span class="btn">Priority</span><span class="btn">Horizon</span><span class="btn">Area</span><span class="btn">Island</span><span class="find">{aglyph("search")}Words in an id or title</span></div>
<div class="panel"><table><thead><tr><th>Id</th><th>Title and island</th><th>Status</th><th>Priority · size</th><th>Changed</th></tr></thead><tbody>{rows}</tbody></table></div></section></div>'''


def roadmap_tray():
    body = '''<table class="kv"><tbody>
<tr><td>Status</td><td><span class="chip">now</span> since 04:12</td></tr><tr><td>Priority</td><td>P1 · size M · horizon this week</td></tr>
<tr><td>Island</td><td><span class="mono">apps-agora.local</span></td></tr><tr><td>Area</td><td>jobs</td></tr>
<tr><td>Owner</td><td><span class="id">ki.prj.agora</span></td></tr></tbody></table>
<h3>Blocks</h3><p><span class="id">KI-AGORA-WRK-006</span> Run-once jobs</p>
<h3>Blocked by</h3><p class="muted">Nothing</p>
<h3>Goal</h3><p>Agora starts, stops and reports the rig’s scheduled jobs, so running them no longer needs Rig by hand on each Mac.</p>
<h3>Context</h3><p class="muted">Jobs shows each job today but only reads. Moving the running here needs <span class="mono">ki agent</span> to stay the only way a run starts.</p>'''
    return tray_frame('Work record · Knowledge Islands', '<span class="id">KI-AGORA-WRK-004</span>', body,
                      actions=[('', 'Open the file'), ('', 'Show the island on Home')])


GUILDS = [
    ('Ke', 'Keystone', 3, 'The foundation: the repository contract and how a skill is written.', ['ki-bootstrap', 'ki-repo', 'ki-skills']),
    ('Go', 'Governance', 13, 'The standing rules: writing, Git, delegation, decisions and trades.',
     ['ki-authoring', 'ki-delegation', 'ki-diagrams', 'ki-git', 'ki-guides', 'ki-specs', 'ki-trades', '+6']),
    ('CM', 'Change management', 13, 'How work moves: captured, planned, done, accepted and recapped.',
     ['ki-accept', 'ki-batch', 'ki-coordination', 'ki-next', 'ki-plan', 'ki-recap', 'ki-work', '+6']),
    ('RS', 'Repository structure', 16, 'The shape of each kind of repository: knowledge bases, tools, sites.',
     ['ki-repo-harness', 'ki-repo-kb', 'ki-repo-kb-streams', 'ki-repo-homebrew-tap', '+12']),
]


def atlas_guilds(selected='ki-delegation'):
    cards = ''.join(f'''<section class="at-guild"><div class="gh"><span class="mono-badge">{mono}</span><div><b>{name}</b><span class="sub">{n} skills</span></div></div>
<p>{escape(about)}</p><div class="bank">{"".join(f'<span class="chip{" sel" if s == selected else ""}">{s}</span>' for s in skills)}</div></section>'''
                    for mono, name, n, about, skills in GUILDS)
    return f'''{head("P1", "Guilds", "15 guilds · 77 skills · 8 harnesses in Knowledge Islands", '<span class="find">' + aglyph("search") + 'Words in a skill or guild</span>')}
<div class="at-guilds" {R("P2", "Guilds and their skills")}>{cards}</div>
<p class="foot">Provisional guilds: each is a folder a harness sorts its skills into, until the guildmaster’s catalogue (ki.reg.guilds) names them. 11 more guilds to the right.</p>'''


def skill_bottom():
    body = '''<div class="at-doc"><ul class="plain"><li class="on">rubric.md</li><li>sources.md</li><li>standards-background-runs.md</li><li>standards-delegation-packets.md</li></ul>
<div><div class="muted mono" style="margin-bottom:6px">references/rubric.md</div><h4>Generated rubric: delegation packets and background runs</h4>
<p>Line-by-line criteria for auditing ki-delegation. Classifications are derived from item aspects: mechanical, judgement, and hybrid with heuristic mechanical evidence.</p>
<p class="muted">Sources are cited as declared by each canonical item. Edit the definitions under <span class="mono">scripts/rubric/items/</span>, then run the rubric again.</p></div></div>'''
    return bottom_frame('Governance · ki-agentic-harness', '<span class="id">ki-delegation</span>',
                        [('SKILL.md', False), ('references/ 4', True), ('scripts/ 11', False), ('assets/ 7', False)], body, height=400)


def atlas_home(title='Home'):
    import map_view as MV
    bar = map_toolbar(focused=True, plane='both', code='P2').replace(
        '<span class="lbl">Plane</span><span class="seg" title="Each rig is a plane over the same islands"><span>sol</span><span>terra</span><span class=on>Both planes</span></span>', '')
    return f'''{head("P1", title, "Focused · 9 of 13 islands active · 2 need a look · 34 queries wait on you")}
<section class="mapcol at-map">{bar}<div class="mapcanvas" {R("P3", "The map")}>{MV.working_map(plane="both", focused=True, selected=None)}</div></section>'''


JOB_ROWS = [
    ('group', 'Knowledge Islands'),
    ('repo', 'apps-agora.local'),
    ('job', 'agora-review', 'every minute', 'sol ✓ terra ✓', '04:20', 'ok', 'Running'),
    ('job', 'agora-keep-level', 'every 5 minutes', 'sol ✓ terra ✓', '04:15', 'ok', 'Running'),
    ('repo', 'apps-observatory.local'),
    ('job', 'observatory-service', 'kept running', 'sol ✓', '04:01', 'ok', 'Running'),
    ('repo', 'ki-principal'),
    ('job', 'sop-digest', 'daily at 06:40', 'sol ✕', '11-05 06:40', 'bad', 'Failed last run'),
    ('job', 'roadmap-index', 'hourly', 'sol ✓', '04:00', 'ok', 'Running'),
    ('repo', 'tools-ki'),
    ('job', 'ki-territory-audit', 'daily at 02:10', 'terra ✓', '02:11', 'ok', 'Running'),
]


def atlas_jobs(selected='sop-digest'):
    rows = []
    for r in JOB_ROWS:
        if r[0] == 'group':
            rows.append(f'<tr class="group"><td colspan="5">{r[1]}</td></tr>')
        elif r[0] == 'repo':
            rows.append(f'<tr><td colspan="5" class="mono muted" style="padding-left:18px">{r[1]}</td></tr>')
        else:
            _, name, sched, macs, last, lvl, words = r
            mark_ = mark('slashed') if lvl == 'bad' else mark('stone')
            rows.append(f'<tr{" class=sel" if name == selected else ""}><td class="id" style="padding-left:30px">{name}</td><td>{sched}</td><td class="mono">{macs}</td>'
                        f'<td class="muted">{last}</td><td class="{"bad" if lvl == "bad" else ""}">{mark_}{words}</td></tr>')
    return f'''{head("P1", "Jobs", "23 jobs on 2 Macs in Knowledge Islands · 1 failed its last run", '<span class="seg"><span class=on>All</span><span>Scheduled</span><span>Services</span></span>')}
<section class="panel" {R("P2", "Jobs by territory and repository")}><table><thead><tr><th>Job</th><th>Schedule</th><th>Macs</th><th>Last run</th><th>How it stands</th></tr></thead>
<tbody>{"".join(rows)}</tbody></table></section>'''


def job_tray():
    body = '''<table class="kv"><tbody><tr><td>Repository</td><td><span class="mono">ki-principal</span></td></tr>
<tr><td>Schedule</td><td>Daily at 06:40</td></tr><tr><td>Declared in</td><td><span class="mono">conf.d/sop-digest.toml</span></td></tr>
<tr><td>Runs on</td><td>sol · declared for the studio profile</td></tr><tr><td>Last run</td><td class="bad">Failed · 11-05 06:40 · 12 s</td></tr>
<tr><td>Next run</td><td>Today 06:40</td></tr></tbody></table>
<h3>What it says</h3><p>ki sop digest: the State of play could not be read, a lock was held.</p>
<p class="muted">Running, starting or stopping a job stays Rig’s for now (KI-AGORA-WRK-004).</p>'''
    return tray_frame('Scheduled job · ki-principal', '<span class="id">sop-digest</span>', body,
                      actions=[('', 'Open the declaration'), ('', 'Show the island on Home')])


def job_bottom():
    runs = ''.join(f'<tr><td class="mono">{w}</td><td>{m}</td><td class="{c}">{o}</td><td class="mono">{d}</td><td class="muted">{s}</td></tr>' for w, m, c, o, d, s in (
        ('11-05 06:40', 'sol', 'bad', 'Failed', '12 s', 'The State of play could not be read: a lock was held'),
        ('11-04 06:40', 'sol', '', 'Ended well', '41 s', 'Digest written, 14 items'),
        ('11-03 06:40', 'sol', '', 'Ended well', '38 s', 'Digest written, 9 items'),
        ('11-02 06:40', 'sol', '', 'Ended well', '44 s', 'Digest written, 17 items')))
    body = f'<table><thead><tr><th>When</th><th>Mac</th><th>Outcome</th><th>Took</th><th>Summary</th></tr></thead><tbody>{runs}</tbody></table>'
    return bottom_frame('Runs · sop-digest', 'The last four runs', [('Runs', True), ('Declaration', False), ('Log', False)], body, height=260)
