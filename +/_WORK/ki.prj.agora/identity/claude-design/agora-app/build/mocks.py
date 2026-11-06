"""The Agora app mock-ups: the shell and every view, as HTML artboards 1440 points wide.

Each region worth discussing carries data-region (its code, such as P3) and data-label, so the board can draw
its box. Shell pages mark only N; view pages mark only P, as the annotated-board standard asks.
"""
from html import escape
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
    ("Who's doing what", 'here', '10'),
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


def page(active, content, contracted=False, mark_shell=False, theme='night', portal='open', title='Agora'):
    return f'''<!doctype html><html lang="en-GB" data-theme="{theme}"><head><meta charset="utf-8">
<title>{escape(title)}</title><link rel="stylesheet" href="../build/app.css"></head><body>
<div class="app{" contracted" if contracted else ""}">{rail(active, mark_shell, portal)}<main>{content}</main></div>
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
    for mac, note in (('sol', 'this Mac · present · 4 agents'), ('terra', 'present · heard 04:20 · 6 agents')):
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
    return f'''{head("P1", "Home", "10 agents on 2 Macs · 2 need a look · 34 queries wait on you", tools)}
<div class="grid" style="grid-template-columns: 1fr 360px;">
  <section class="panel" {R("P2", "The two squares")}><header><h2>Here now</h2><span class="muted">each Mac's square, its agents, and the portal between them</span></header><div class="body">{island_svg()}
  <p class="foot" style="margin:4px 0 0">Solid stone: listening. Hollow: reads on open. Slashed: silent. The table under Who's doing what is the same picture as text.</p></div></section>
  <div class="grid" style="align-content:start">{attention_panel("P3")}{waits_panel("P4", n=4)}</div>
</div>
{said_table("P5", "Just said", limit=6, title="Just said")}'''


def home_b():
    stats = ''.join(f'<div class="panel stat"><span class="v">{v}</span><span class="k">{k}</span></div>' for v, k in
                    (('10', 'agents on 2 Macs'), ('7', 'listening, 2 silent'), ('2', 'need a look'), ('34', 'queries wait on you')))
    return f'''{head("P1", "Home", "Friday 6 November, 04:20")}
<div class="grid" style="grid-template-columns: repeat(4, 1fr);" {R("P2", "Summary figures")}>{stats}</div>
{attention_panel("P3")}
{roster_table("P4", "Agents by Mac", selected=None, compact=True)}'''


def home_c():
    side = ''.join(f'<li>{mark("slashed" if a["listen"] == "silent" else "hollow" if a["listen"] == "open" else "stone")}<span class="id">{a["id"]}</span> <span class="muted">· {a["mac"]}</span></li>' for a in AGENTS)
    return f'''{head("P1", "Home", "10 agents on 2 Macs · All words since 03:30")}
<div class="grid" style="grid-template-columns: 1fr 340px;">
  {said_table("P2", "What's being said", title="What's being said")}
  <section class="panel" {R("P3", "Who is here")}><header><h2>Who is here</h2><span class="muted">10</span></header><ul class="plain body">{side}</ul></section>
</div>'''


def here_a():
    tools = '<span class="seg"><span class="on">Both Macs</span><span>sol</span><span>terra</span></span><span class="find">Who looks after <b>a focus, such as identity</b></span>'
    a = AGENTS[0]
    return f'''{head("P1", "Who's doing what", "10 agents on 2 Macs · 7 listening · 1 on open · 2 silent", tools)}
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
    return f'''{head("P1", "Who's doing what", "By focus: the address book · 19 focus areas across 10 agents", tools)}
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
        ('04:19', 'Away until 08:00', 'away', '9 of 10', 'hnr.prj.site-robots'),
        ('04:05', 'Ping', 'ping', '8 of 10', 'hnr.sop.main, hnr.prj.site-robots'),
        ('03:26', 'Away until 08:00 (ki.sop.main)', 'away', '1 of 1', ''),
        ('01:45', 'Mark and summarise', 'mark', '7 of 9', 'hnr.sop.main, hnr.prj.5g-emerge-phase3'),
    ]
    trs = ''.join(f'<tr{" class=sel" if i == 1 else ""}><td class="mono">{t}</td><td>{w}</td><td>{k}</td><td>{h}</td><td class="bad">{s or "<span class=muted>None</span>"}</td></tr>' for i, (t, w, k, h, s) in enumerate(rows))
    ans = ''.join(f'<li>{mark("slashed" if a["listen"] == "silent" else "stone")}<span class="id">{a["id"]}</span> <span class="muted">· {a["mac"]} · {"silent" if a["listen"] == "silent" else "answered 04:0" + str(5 + i % 4)}</span></li>' for i, a in enumerate(AGENTS))
    return f'''{head("P1", "Broadcasts", "Sent from this Mac and received from terra · today", '<span class="btn">Broadcast…</span><span class="btn">Ping</span><span class="btn">Mark all</span>')}
<div class="grid" style="grid-template-columns: 1fr 380px;">
<section class="panel" {R("P2", "Broadcasts sent")}><table><thead><tr><th>Sent</th><th>What</th><th>Kind</th><th>Heard</th><th>Silent</th></tr></thead><tbody>{trs}</tbody></table></section>
<section class="panel" {R("P3", "Who heard the ping")}><header><h2>Ping at 04:05</h2><span class="muted">8 answered, 2 silent</span></header><ul class="plain body">{ans}</ul><div class="body"><span class="btn">Ping the 2 silent again</span></div></section>
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
    sol = mac_panel('P3', 'sol, this Mac', [('Presence', f'{mark("stone")}present'), ('Listens on', '<span class="mono">100.64.0.1:1676</span>'), ('Agora', '0.9.0 · up since 2026-11-05 22:40'), ('Agents', '4, all listening'), ('Checkouts', '64 level, 1 ahead'), ('Last review', '2026-11-06 04:20')])
    terra = mac_panel('P5', 'terra', [('Presence', f'{mark("stone")}present · heard 04:20'), ('Listens on', '<span class="mono">100.64.0.2:1676</span>'), ('Agora', '0.9.0 · up since 2026-11-06 03:20'), ('Agents', '6 · 2 silent'), ('Checkouts', '58 level, 1 diverged'), ('Last review', '2026-11-06 04:18')])
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
