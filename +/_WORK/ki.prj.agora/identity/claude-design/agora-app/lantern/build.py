"""Agora Lantern: the iPhone app's one screen, "Who is listening".

Writes mocks/<artboard>-<night|light>.html (393 x 852 CSS px each) and, once shots/regions.json exists, index.html.
Run: python3 build.py && node shoot.js && python3 build.py

Tokens are copied from ../build/app.css (read only). The roster is a snapshot of ../build/data.py (6 Nov 2026),
held here so this folder stays stable while the main pack's build changes.
"""
import json
import os
import re
from html import escape

HERE = os.path.dirname(os.path.abspath(__file__))
MOCKS = os.path.join(HERE, 'mocks')
STAMP = '2026-11-06'
NOW = '04:20'

# ------------------------------------------------------------------ tokens, copied from the pack
css_src = open(os.path.join(HERE, '..', 'build', 'app.css'), encoding='utf-8').read()
TOKENS = re.search(r':root, \[data-theme="night"\] \{.*?\}\n\[data-theme="light"\] \{.*?\}', css_src, re.S).group(0)

# ------------------------------------------------------------------ roster (snapshot of build/data.py)
TERR = {'ki': 'Knowledge Islands', 'hnr': 'Humans Not Robots', 'personal': 'Personal'}
# id, mac, territory, focus (primary first), listening, last heard, waiting count, waiting query ids
R = [
    ('ki.prj.agora', 'sol', 'ki', ['send', 'jobs', 'voice', 'identity', 'emerging'], 'call', '04:12', 10),
    ('ki.sop.main', 'sol', 'ki', ['themes', 'acceptance', 'chain', 'emerging'], 'call', '04:05', 18),
    ('personal.reg.inbox-sol', 'sol', 'personal', ['method', 'kiv', 'coordination'], 'call', '04:10', 3),
    ('personal.reg.household-sol', 'sol', 'personal', ['rig', 'install', 'settings'], 'poll', '04:01', 0),
    ('personal.reg.watchman-sol', 'sol', 'personal', ['portal'], 'call', '04:10', 0),
    ('personal.reg.inbox-terra', 'terra', 'personal', ['method', 'records'], 'call', '04:08', 1),
    ('personal.reg.household-terra', 'terra', 'personal', ['rig', 'install'], 'call', '04:06', 0),
    ('personal.reg.watchman-terra', 'terra', 'personal', ['portal'], 'call', '04:09', 0),
    ('hnr.sop.main', 'terra', 'hnr', ['routing', 'acceptance'], 'silent', '02:10', 2),
    ('hnr.prj.5g-emerge-phase3', 'terra', 'hnr', ['delivery', 'reporting'], 'open', '03:30', 0),
    ('hnr.prj.5g-emerge-p2ms3', 'terra', 'hnr', ['delivery'], 'call', '03:58', 0),
    ('hnr.prj.site-robots', 'terra', 'hnr', ['site', 'content'], 'silent', '02:10', 0),
]
AGENTS = [dict(id=a, mac=m, terr=t, focus=f, listen=l, at=at, waits=w) for a, m, t, f, l, at, w in R]
WAITS = {'hnr.sop.main': [('SITE-DOMAIN', 'Which domain the new site answers on'),
                          ('P2MS3-DATES', 'The dates for the P2MS3 milestone')]}
MAC_HEARD = {'sol': '04:20', 'terra': '04:20'}

STATE = {  # word, glyph, colour class
    'call': ('listening', 'stone', 'ok'), 'poll': ('listening', 'stone', 'ok'),
    'open': ('on open', 'hollow', 'acc'), 'silent': ('silent', 'slashed', 'warn'),
}
RANK = {'silent': 0, 'open': 1, 'call': 2, 'poll': 2}

GLYPH = {
    'stone': '<circle cx="6" cy="6" r="3.8" fill="currentColor"/>',
    'hollow': '<circle cx="6" cy="6" r="3.6" fill="none" stroke="currentColor" stroke-width="1.4"/>',
    'slashed': '<circle cx="6" cy="6" r="3.6" fill="none" stroke="currentColor" stroke-width="1.4"/>'
               '<path d="M3.3 8.7 L8.7 3.3" stroke="currentColor" stroke-width="1.4"/>',
    'unknown': '<circle cx="6" cy="6" r="3.6" fill="none" stroke="currentColor" stroke-width="1.6" stroke-dasharray="2.2 1.6"/>',
}


def g(name):
    return f'<svg class="g" viewBox="0 0 12 12" aria-hidden="true">{GLYPH[name]}</svg>'


def reg(code, label, on=True):
    return f' data-region="{code}" data-label="{escape(label)}"' if on else ''


def listening_count(rows):
    return sum(1 for a in rows if a['listen'] in ('call', 'poll'))


def tally(rows):
    n = {'listening': listening_count(rows), 'on open': sum(1 for a in rows if a['listen'] == 'open'),
         'silent': sum(1 for a in rows if a['listen'] == 'silent')}
    return n


def tally_words(rows):
    n = tally(rows)
    parts = [f'{len(rows)} agents', f'{n["listening"]} listening']
    if n['on open']:
        parts.append(f'{n["on open"]} on open')
    if n['silent']:
        parts.append(f'{n["silent"]} silent')
    return ' · '.join(parts)


# ------------------------------------------------------------------ pieces
def focus_html(a, annot, n=2):
    f = [x for x in a['focus']]
    shown = f[:n]
    more = len(f) - len(shown)
    txt = '★ ' + ' · '.join(escape(x) for x in shown) + (f' +{more}' if more else '')
    return f'<span class="f"{reg("L6", "Focus areas, primary starred", annot)}>{txt}</span>'


def row_html(a, annot=False, show_mac=False, show_terr=True, open_=False, detail=''):
    word, gl, cls = STATE[a['listen']]
    meta = []
    if show_mac:
        meta.append(f'<span class="t"{reg("L12", "Mac", annot)}>{a["mac"]}</span>')
    if show_terr:
        meta.append(f'<span class="t"{reg("L5", "Territory", annot)}>{TERR[a["terr"]]}</span>')
    sep = '<span class="dot">·</span>'
    meta_html = sep.join(meta)
    if meta_html:
        meta_html += sep
    waits = (f'<span class="w"{reg("L8", "Waiting on you", annot)}>{a["waits"]} waiting</span>' if a['waits'] else '')
    klass = f'row {cls}' + (' open' if open_ else '')
    return (f'<li class="{klass}"><div class="l1"><span class="id"{reg("L4", "Package id", annot)}>{a["id"]}</span>'
            f'<span class="state {cls}"{reg("L7", "Listening state: glyph and word", annot)}>{g(gl)}{word}</span></div>'
            f'<div class="l2">{meta_html}{focus_html(a, annot, 1 if (show_mac and show_terr) else 2)}{waits}</div>{detail}</li>')


CHEV_R = '<svg class="chev" viewBox="0 0 12 12"><path d="M4 2.5 L8 6 L4 9.5" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>'
CHEV_D = '<svg class="chev" viewBox="0 0 12 12"><path d="M2.5 4 L6 8 L9.5 4" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>'


def mac_header(mac, rows, collapsed=False, state='present', sub=None):
    word, gl, cls = ('present', 'stone', 'ok') if state == 'present' else ('unknown', 'unknown', 'warn')
    sub = sub or f'{tally_words(rows)} · heard {MAC_HEARD[mac]}'
    return (f'<div class="gh"{reg("L2", "Group header")}><div class="gl"><span class="name">{mac}</span>'
            f'<span class="pres {cls}">{g(gl)}{word}</span><span class="sp"></span>{CHEV_R if collapsed else CHEV_D}</div>'
            f'<div class="gs">{sub}</div></div>')


def sorted_rows(rows):
    return sorted(rows, key=lambda a: RANK[a['listen']])


def group(header, rows_html, annot_label='Agent rows'):
    return f'<section>{header}<ul class="rows"{reg("L3", annot_label)}>{rows_html}</ul></section>'


# ------------------------------------------------------------------ chrome
STATUS = f'''<div class="status"><span class="clock">{NOW}</span>
<span class="icons"><svg width="18" height="12" viewBox="0 0 18 12" aria-hidden="true"><rect x="0" y="8" width="3" height="4" rx="0.8" fill="currentColor"/><rect x="5" y="5.5" width="3" height="6.5" rx="0.8" fill="currentColor"/><rect x="10" y="3" width="3" height="9" rx="0.8" fill="currentColor"/><rect x="15" y="0" width="3" height="12" rx="0.8" fill="currentColor"/></svg>
<svg width="17" height="12" viewBox="0 0 17 12" aria-hidden="true"><path d="M1 4.2 Q8.5 -1.6 16 4.2 M3.6 7 Q8.5 3 13.4 7" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><circle cx="8.5" cy="10" r="1.5" fill="currentColor"/></svg>
<svg width="27" height="13" viewBox="0 0 27 13" aria-hidden="true"><rect x="0.7" y="0.7" width="22.6" height="11.6" rx="3.6" fill="none" stroke="currentColor" stroke-width="1" opacity="0.5"/><rect x="2.4" y="2.4" width="16" height="8.2" rx="2" fill="currentColor"/><rect x="24.5" y="4.3" width="1.8" height="4.4" rx="0.9" fill="currentColor" opacity="0.5"/></svg></span></div>
<div class="island"></div>'''


def ping_bar(note, label='Ping everyone'):
    return (f'<div class="bar"{reg("L9", "Ping bar, in the thumb zone")}><div class="barnote">{note}</div>'
            f'<button class="brass" type="button">{label}</button></div><div class="home"></div>')


def head(summary, key_html, extra=''):
    return (f'<header class="top"{reg("L1", "Summary and key")}><h1>Who is listening</h1>'
            f'<div class="sum">{summary}</div>{key_html}{extra}</header>')


def key_row(rows):
    n = tally(rows)
    return (f'<div class="key"><span class="ok">{g("stone")}{n["listening"]} listening</span>'
            f'<span class="acc">{g("hollow")}{n["on open"]} on open</span>'
            f'<span class="warn">{g("slashed")}{n["silent"]} silent</span></div>')


SUMMARY = '12 agents on 2 Macs · 9 listening'


def page(theme, title, body, bar):
    css = CSS.replace('/*TOKENS*/', TOKENS)
    return (f'<!doctype html><html lang="en-GB" data-theme="{theme}"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=393, initial-scale=1"><title>{escape(title)} · {theme}</title>'
            f'<style>{css}</style></head><body><div class="screen">{STATUS}<main class="scroll">{body}</main>'
            f'<div class="fade"></div>{bar}</div></body></html>')


# ------------------------------------------------------------------ the artboards
def board_a():
    sol = [a for a in AGENTS if a['mac'] == 'sol']
    terra = sorted_rows([a for a in AGENTS if a['mac'] == 'terra'])
    s = group(mac_header('sol', sol), ''.join(row_html(a, annot=(i == 0)) for i, a in enumerate(sorted_rows(sol))))
    t = group(mac_header('terra', terra), ''.join(row_html(a) for a in terra))
    return head(SUMMARY, key_row(AGENTS)) + s + t, ping_bar('Last ping 04:05 · 8 answered, 2 silent')


def board_b():
    out = ''
    first = True
    for k in ('ki', 'hnr', 'personal'):
        rows = sorted_rows([a for a in AGENTS if a['terr'] == k])
        hdr = (f'<div class="gh"{reg("L2", "Group header")}><div class="gl"><span class="name">{TERR[k]}</span><span class="sp"></span>{CHEV_D}</div>'
               f'<div class="gs">{tally_words(rows)}</div></div>')
        out += group(hdr, ''.join(row_html(a, annot=(first and i == 0), show_mac=True, show_terr=False)
                                  for i, a in enumerate(rows)))
        first = False
    return head(SUMMARY, key_row(AGENTS)) + out, ping_bar('Last ping 04:05 · 8 answered, 2 silent')


def board_c():
    out = ''
    first = True
    for word, keys, sub in (('Silent', ('silent',), 'Agora\'s call went unanswered'),
                            ('On open', ('open',), 'Reads its messages when it next starts'),
                            ('Listening', ('call', 'poll'), 'Answered Agora\'s call')):
        rows = [a for a in AGENTS if a['listen'] in keys]
        gl = STATE[keys[0]][1]
        cls = STATE[keys[0]][2]
        hdr = (f'<div class="gh"{reg("L2", "Group header")}><div class="gl {cls}"><span class="name">{g(gl)}{word}</span>'
               f'<span class="cnt">{len(rows)}</span><span class="sp"></span></div><div class="gs">{sub}</div></div>')
        out += group(hdr, ''.join(row_html(a, annot=(first and i == 0), show_mac=True) for i, a in enumerate(rows)))
        first = False
    macs = (f'<div class="macs"><span class="ok">{g("stone")}sol present</span><span class="ok">{g("stone")}terra present</span></div>')
    return head(SUMMARY, key_row(AGENTS), macs) + out, ping_bar('Last ping 04:05 · 8 answered, 2 silent')


def board_a_detail():
    sol = [a for a in AGENTS if a['mac'] == 'sol']
    terra = sorted_rows([a for a in AGENTS if a['mac'] == 'terra'])
    s = f'<section>{mac_header("sol", sol, collapsed=True)}</section>'
    rows = ''
    for i, a in enumerate(terra):
        if a['id'] == 'hnr.sop.main':
            wl = ''.join(f'<li><span class="qid">{q}</span><span class="qt">{escape(t)}</span></li>' for q, t in WAITS[a['id']])
            foc = ' '.join(f'<span class="fa">{"★ " if j == 0 else ""}{escape(x)}</span>' for j, x in enumerate(a['focus']))
            detail = (f'<div class="detail"{reg("L10", "Agent detail")}>'
                      f'<dl><dt>Focus areas</dt><dd class="fas">{foc}</dd>'
                      f'<dt>Last heard</dt><dd>02:10 · 2 calls unanswered since then</dd>'
                      f'<dt>Waits on Kris · {a["waits"]}</dt><dd><ul class="q">{wl}</ul></dd>'
                      f'<dt>Runs on</dt><dd>terra · {g("stone")}present</dd></dl>'
                      f'<button class="ghost" type="button">Ping hnr.sop.main</button></div>')
            rows += row_html(a, annot=True, open_=True, detail=detail)
        else:
            rows += row_html(a)
    t = group(mac_header('terra', terra), rows)
    return head(SUMMARY, key_row(AGENTS)) + s + t, ping_bar('Last ping 04:05 · 8 answered, 2 silent')


def board_a_empty():
    macs = ''
    for m, at in (('sol', '04:02'), ('terra', '04:01')):
        macs += (f'<li class="mrow"><div class="l1"><span class="name">{m}</span><span class="state warn">{g("unknown")}unknown</span></div>'
                 f'<div class="l2"><span class="f">Last heard {at} · 5 agents last seen</span></div></li>'
                 if m == 'sol' else
                 f'<li class="mrow"><div class="l1"><span class="name">{m}</span><span class="state warn">{g("unknown")}unknown</span></div>'
                 f'<div class="l2"><span class="f">Last heard {at} · 7 agents last seen</span></div></li>')
    msg = (f'<div class="msg"{reg("L11", "No Mac reachable: what to do")}><h2>No Mac reachable</h2>'
           '<p>Lantern cannot reach your tailnet, so it cannot ask who is listening.</p>'
           '<ol><li>Check that Tailscale is on, and signed in as you.</li><li>Check that sol and terra are awake.</li><li>Try again.</li></ol>'
           '<p class="muted">An unknown Mac may still be running work. Nothing is taken to have stopped.</p></div>')
    h = head('No Mac reachable · 0 of 2 heard', '')
    body = h + f'<section><div class="gh plain"{reg("L2", "Group header")}><div class="gl"><span class="name">Macs</span></div><div class="gs">Both are unknown. Agents are hidden until a Mac answers.</div></div><ul class="rows"{reg("L3", "Mac rows")}>{macs}</ul></section>' + msg
    return body, ping_bar('Last tried 04:20 · nothing answered', 'Try again')


BOARDS = [
    ('a', 'Grouped by Mac', board_a), ('b', 'Grouped by territory', board_b), ('c', 'Listening first', board_c),
    ('a-detail', 'Grouped by Mac, a row open', board_a_detail), ('a-empty', 'Grouped by Mac, no Mac reachable', board_a_empty),
]

CSS = '''
/*TOKENS*/
* { box-sizing:border-box; }
html, body { margin:0; background:var(--paper); color:var(--ink); }
body { width:393px; height:852px; overflow:hidden; font:15px/1.35 -apple-system, BlinkMacSystemFont, "SF Pro Text", Inter, "Segoe UI", sans-serif; -webkit-font-smoothing:antialiased; }
.screen { position:relative; width:393px; height:852px; overflow:hidden; background:var(--paper); }
.mono, .id { font-family:ui-monospace, "SF Mono", Menlo, monospace; }
.muted { color:var(--muted); }
.ok { color:var(--ok); } .acc { color:var(--accent); } .warn { color:var(--warn); }
[data-theme="night"] .acc { color:var(--accent); }
.g { width:12px; height:12px; flex:0 0 12px; }

/* phone chrome */
.status { position:absolute; left:0; right:0; top:0; height:54px; z-index:5; background:var(--paper); display:flex; justify-content:space-between; align-items:center; padding:6px 34px 0 44px; font-weight:600; font-size:16px; }
.status .icons { display:flex; gap:6px; align-items:center; }
.island { position:absolute; top:11px; left:50%; width:126px; height:37px; margin-left:-63px; border-radius:20px; background:#0a0f18; z-index:6; }
.home { position:absolute; bottom:8px; left:50%; width:134px; height:5px; margin-left:-67px; border-radius:3px; background:var(--ink); opacity:.85; z-index:8; }

/* scrolling list */
.scroll { position:absolute; top:54px; left:0; right:0; bottom:0; overflow:hidden; padding-bottom:20px; }
.top { padding:6px 16px 12px; border-bottom:1px solid var(--rule); }
.top h1 { margin:0 0 2px; font-size:28px; line-height:1.15; font-weight:700; letter-spacing:-.2px; }
.sum { font-size:16px; font-weight:500; }
.key { display:flex; gap:14px; margin-top:8px; font-size:13px; font-weight:500; white-space:nowrap; }
.key span, .macs span { display:inline-flex; align-items:center; gap:5px; }
.macs { display:flex; gap:14px; margin-top:6px; font-size:13px; font-weight:500; }
.gh { padding:12px 16px 6px; background:var(--paper); border-bottom:1px solid var(--rule); }
.gl { display:flex; align-items:center; gap:8px; min-height:26px; }
.gl .name { font-size:19px; font-weight:700; display:inline-flex; align-items:center; gap:7px; }
.gl .name .g { width:14px; height:14px; flex:0 0 14px; }
.gl .cnt { font-size:15px; color:var(--muted); font-weight:500; }
.pres { display:inline-flex; align-items:center; gap:5px; font-size:13px; font-weight:500; }
.sp { flex:1; }
.chev { width:14px; height:14px; color:var(--muted); }
.gs { font-size:12.5px; color:var(--muted); margin-top:1px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; padding-bottom:4px; }
ul.rows { list-style:none; margin:0; padding:0; }
.row, .mrow { color:var(--ink); padding:9px 16px; min-height:62px; border-bottom:1px solid var(--rule); display:flex; flex-direction:column; justify-content:center; gap:3px; }
.row .id { color:var(--ink); }
.row.warn { background:var(--wash-warn); box-shadow:inset 3px 0 0 var(--warn); }
.l1 { display:flex; justify-content:space-between; align-items:center; gap:10px; }
.id { font-size:14.5px; font-weight:600; min-width:0; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }
.mrow .name { font-size:17px; font-weight:600; }
.state { display:inline-flex; align-items:center; gap:5px; font-size:13px; font-weight:600; flex:none; }
.l2 { display:flex; gap:6px; font-size:12.5px; color:var(--muted); min-width:0; white-space:nowrap; align-items:baseline; }
.l2 .t, .l2 .dot { flex:none; }
.l2 .f { flex:1 1 auto; min-width:0; overflow:hidden; text-overflow:ellipsis; }
.l2 .w { flex:none; margin-left:auto; color:var(--warn); font-weight:600; }
.row.open { background:var(--surface); }
.row.open.warn { background:var(--wash-warn); }

/* expanded detail */
.detail { margin-top:8px; padding-top:8px; border-top:1px solid var(--rule); }
.detail dl { margin:0; display:grid; grid-template-columns:96px 1fr; gap:7px 8px; font-size:13.5px; }
.detail dt { font-size:11.5px; font-weight:600; color:var(--muted); padding-top:2px; }
.detail dd { margin:0; min-width:0; }
.detail dd .g { vertical-align:-1px; margin:0 4px 0 0; color:var(--ok); }
.fas { display:flex; flex-wrap:wrap; gap:4px 12px; }
.fa { white-space:nowrap; }
ul.q { list-style:none; margin:0; padding:0; display:flex; flex-direction:column; gap:6px; }
ul.q li { display:flex; flex-direction:column; }
.qid { font-family:ui-monospace, "SF Mono", Menlo, monospace; font-size:12.5px; font-weight:600; color:var(--warn); }
.qt { font-size:13px; }
.ghost { margin-top:10px; width:100%; height:44px; border-radius:10px; border:1px solid var(--boundary); background:transparent; color:var(--ink); font:600 15px -apple-system, BlinkMacSystemFont, sans-serif; }

/* empty state */
.msg { padding:16px 16px 0; }
.msg h2 { margin:0 0 6px; font-size:20px; font-weight:700; }
.msg p { margin:0 0 10px; font-size:15px; }
.msg ol { margin:0 0 12px; padding-left:22px; font-size:15px; }
.msg li { margin:4px 0; }
.gh.plain { border-top:0; }

/* bottom: the thumb zone */
.fade { position:absolute; left:0; right:0; bottom:112px; height:40px; background:linear-gradient(to bottom, transparent, var(--paper)); z-index:3; pointer-events:none; }
.bar { position:absolute; left:0; right:0; bottom:0; height:112px; padding:10px 16px 0; background:var(--paper); border-top:1px solid var(--rule); z-index:4; }
.barnote { font-size:12.5px; color:var(--muted); margin-bottom:8px; }
button.brass { width:100%; height:50px; border-radius:12px; border:0; background:var(--gold); color:var(--on-gold); font:700 17px -apple-system, BlinkMacSystemFont, sans-serif; }
'''


def write_mocks():
    os.makedirs(MOCKS, exist_ok=True)
    for bid, title, fn in BOARDS:
        body, bar = fn()
        for theme in ('night', 'light'):
            with open(os.path.join(MOCKS, f'{bid}-{theme}.html'), 'w', encoding='utf-8') as f:
                f.write(page(theme, f'Lantern {bid} {title}', body, bar))



BOARD_CSS = """
:root { --paper:#f5efe0; --ink:#1a2030; --muted:#4a5568; --accent:#1b3a5c; --rule:#d4c9b4; --boundary:#9a8358; --gold:#c8963c; --surface:#eef1f5; }
* { box-sizing:border-box; }
body { margin:0; background:var(--paper); color:var(--ink); font:14px/1.5 -apple-system, BlinkMacSystemFont, Inter, "Segoe UI", sans-serif; }
.wrap { max-width:1280px; margin:0 auto; padding:24px 32px 64px; }
h1 { font-size:24px; margin:0 0 6px; font-weight:600; }
h2 { font-size:18px; margin:36px 0 10px; font-weight:600; }
.note { max-width:860px; }
.stamp { color:var(--muted); font-size:12px; }
.fields { max-width:860px; margin:6px 0 0; padding-left:18px; }
.fields li { margin:2px 0; }
.toggle { display:inline-flex; gap:6px; align-items:center; font-size:13px; color:var(--muted); margin:14px 0 4px; }
table.codes { border-collapse:collapse; margin-top:8px; font-size:13px; }
table.codes th, table.codes td { text-align:left; padding:4px 14px 4px 0; border-bottom:1px solid var(--rule); vertical-align:top; }
table.codes th { font-size:12px; color:var(--muted); }
figure.ab { margin:32px 0 0; padding:0; }
figure.ab > header { display:flex; align-items:baseline; gap:12px; flex-wrap:wrap; margin-bottom:8px; }
figure.ab h3 { font-size:16px; margin:0; font-weight:600; }
.pref { background:var(--gold); color:var(--ink); font-weight:600; font-size:12px; padding:2px 8px; border-radius:10px; }
.tradeoff { display:grid; grid-template-columns:repeat(3, minmax(0, 1fr)); gap:16px; max-width:1200px; margin:0 0 14px; font-size:13px; }
.tradeoff div { border-top:2px solid var(--rule); padding-top:6px; }
.tradeoff .why { border-top-color:var(--gold); }
.tradeoff b { display:block; font-size:12px; color:var(--muted); }
.pair { display:flex; gap:28px; flex-wrap:wrap; padding:6px; }
figure.preferred .pair { outline:3px solid var(--gold); outline-offset:6px; border-radius:2px; width:fit-content; padding:0; margin:6px; }
.shot { margin:0; }
.shot figcaption { font-size:12px; color:var(--muted); margin-top:6px; }
.frame { position:relative; width:393px; height:852px; border:1px solid var(--rule); border-radius:3px; }
.frame img { display:block; width:393px; height:852px; }
.ov { position:absolute; border:1.5px dashed #2fb5b0; border-radius:3px; pointer-events:none; }
.ov .badge { position:absolute; top:-1px; right:-1px; transform:translateY(-100%); font-size:10.5px; font-weight:700; background:#2fb5b0; color:#10202a;
  padding:0 5px; border-radius:3px 3px 0 0; white-space:nowrap; line-height:15px; }
.ov.below .badge { top:auto; bottom:-1px; transform:translateY(100%); border-radius:0 0 3px 3px; }
body.plain .ov { display:none; }
a { color:var(--accent); }
"""

CODES = [
    ('L1', 'Summary and key', 'The title, the one-line count, and the key that pairs each state with its glyph and word.'),
    ('L2', 'Group header', 'A Mac with its presence (a), a territory (b) or a listening state (c), with counts.'),
    ('L3', 'Agent rows', 'The agents in one group, one row each, about 62 points tall.'),
    ('L4', 'Package id', 'The work package id, in monospace.'),
    ('L5', 'Territory', 'Knowledge Islands, Humans Not Robots or Personal.'),
    ('L6', 'Focus areas', 'The primary one starred, one more, then a count. The detail lists them all.'),
    ('L7', 'Listening state', 'Glyph and word: listening, on open, silent. Colour repeats it and never carries it.'),
    ('L8', 'Waiting on you', 'How many queries wait on Kris, in gold text. Not a button.'),
    ('L9', 'Ping bar', 'The one brass action, in the thumb zone, with the last result above it.'),
    ('L10', 'Agent detail', 'The row opened: focus areas, last heard, what waits on Kris, where it runs.'),
    ('L11', 'No Mac reachable', 'What to check, and the reminder that an unknown Mac may still be working.'),
    ('L12', 'Mac', 'The Mac an agent runs on, where the group is not by Mac.'),
]

ALTS = {
    'a': dict(why='Presence belongs to a Mac. If terra drops off the tailnet, every agent under it goes unknown together, and the header says so once. Silent agents rise to the top of their Mac, and a Mac folds to one line, so trouble is never more than one thumb-swipe down. It also matches the brief and the pack\'s own 2.1a By Mac.',
              gains='The Mac is the unit of presence and of failure, so Mac trouble and agent trouble read as different things. Two headers cover the whole group.',
              costs='Territory is only a line of text on each row, so "how is HNR" means reading down. Trouble on terra starts below sol\'s five rows unless sol is folded.'),
    'b': dict(gains='Work is owned by territory, so Humans Not Robots reads as one body of work: two silent, one on open, one listening.',
              costs='Mac presence has no header. A whole Mac going quiet looks like silent rows scattered under three territories, which hides the very thing Agora exists to report.'),
    'c': dict(gains='Answers "who is not listening" before anything else: the silent agents are the first rows on the screen.',
              costs='Mac and territory repeat on every row, so rows are longer. A row moves when its state changes, under the thumb. Nine listening agents sit in one long, undifferentiated run.'),
}

TITLES = {'a': 'Grouped by Mac', 'b': 'Grouped by territory', 'c': 'Listening first',
          'a-detail': 'a, a row opened', 'a-empty': 'a, no Mac reachable'}

FIELDS = [
    'Summary line: "12 agents on 2 Macs · 9 listening", then a key with a count for each state.',
    'Each Mac (sol, terra): present, or unknown when it cannot be reached, with the time last heard.',
    'Each agent: package id, territory, focus areas with the primary starred, and listening / on open / silent.',
    'How many queries wait on Kris, when any do. Tapping a row opens its detail.',
    'The roster is the pack\'s: 12 agents, sol 5 and terra 7, including the three watchmen. Illustrative data, 6 November 2026.',
]


def overlays(regions):
    out = []
    for r in regions:
        if r['w'] < 10 or r['h'] < 8:
            continue
        label = f'{r["code"]} · {r["label"]}'
        below = ' below' if r['code'] in ('L5', 'L6', 'L8', 'L12') else ''
        out.append(f'<div class="ov{below}" style="left:{r["x"]}px;top:{r["y"]}px;width:{r["w"]}px;height:{r["h"]}px" title="{escape(label)}">'
                   f'<span class="badge">{escape(r["code"])}</span></div>')
    return ''.join(out)


def shot_html(bid, theme, regions):
    reg_ = regions.get(f'{bid}-{theme}', [])
    return (f'<figure class="shot"><div class="frame"><img src="shots/{bid}-{theme}.png" width="393" height="852" '
            f'alt="Lantern {bid}, {theme}: {escape(TITLES[bid])}">{overlays(reg_)}</div>'
            f'<figcaption>{bid} · {"night, the reference" if theme == "night" else "light, the paper tokens"}</figcaption></figure>')


def write_board():
    path = os.path.join(HERE, 'shots', 'regions.json')
    if not os.path.exists(path):
        print('no shots/regions.json yet: run node shoot.js, then build.py again for index.html')
        return
    regions = json.load(open(path, encoding='utf-8'))
    figs = ''
    for bid in ('a', 'b', 'c'):
        al = ALTS[bid]
        pref = bid == 'a'
        why = f'<div class="why"><b>Why this one</b>{escape(al["why"])}</div>' if pref else '<div></div>'
        figs += (f'<figure class="ab{" preferred" if pref else ""}" id="{bid}"><header><h3>{bid} · {TITLES[bid]}</h3>'
                 f'{"<span class=pref>★ Preferred</span>" if pref else ""}</header>'
                 f'<div class="tradeoff">{why}<div><b>Gains</b>{escape(al["gains"])}</div><div><b>Costs</b>{escape(al["costs"])}</div></div>'
                 f'<div class="pair">{shot_html(bid, "night", regions)}{shot_html(bid, "light", regions)}</div></figure>')
    states = ''
    for bid, note in (('a-detail', 'A row opened. The silent agent is the one worth opening: it shows when it was last heard and what waits on Kris. sol is folded to one line to make room.'),
                      ('a-empty', 'No Mac reachable. Agents are hidden rather than shown as stale; both Macs read unknown, never gone, and the screen says an unknown Mac may still be working.')):
        states += (f'<figure class="ab" id="{bid}"><header><h3>{bid} · {TITLES[bid]}</h3><span class="stamp">states of the preferred a</span></header>'
                   f'<p class="note">{escape(note)}</p><div class="pair">{shot_html(bid, "night", regions)}{shot_html(bid, "light", regions)}</div></figure>')
    codes = ''.join(f'<tr><td><b>{c}</b></td><td>{escape(n)}</td><td>{escape(d)}</td></tr>' for c, n, d in CODES)
    fields = ''.join(f'<li>{escape(f)}</li>' for f in FIELDS)
    html = f"""<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Agora Lantern · Who is listening</title><style>{BOARD_CSS}</style></head><body><div class="wrap">
<h1>Agora Lantern · Who is listening</h1>
<p class="note">The iPhone companion to the Agora app, with one screen. Kris picks it up, one-handed, to see at a glance which Macs are present and which agents are listening, and to ping everyone if he doubts it. It only shows: it grants no authority and changes nothing in Git. Each artboard is 393 by 852 points, with the status bar, Dynamic Island and home indicator drawn, in night (the reference) and in light. Three groupings are offered; the preferred one is outlined in brass with its reason.</p>
<p class="stamp">Refreshed {STAMP} · source: lantern/build.py · tokens from the pack's app.css</p>
<b>What it shows</b><ul class="fields">{fields}</ul>
<label class="toggle"><input type="checkbox" onclick="document.body.classList.toggle('plain', this.checked)"> Hide the region boxes</label>
<p class="stamp">Quote a region as "a L7" or "a-detail L10". The same code means the same thing on every artboard; a box marks the first example on a screen.</p>
<table class="codes"><thead><tr><th>Code</th><th>Region</th><th>What it is</th></tr></thead><tbody>{codes}</tbody></table>
<h2>Three alternatives</h2>{figs}
<h2>States of the preferred one</h2>{states}
<p class="stamp">Read the <a href="README.md">README</a> for the choices and what is open.</p>
</div></body></html>"""
    with open(os.path.join(HERE, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html)
    print('index.html')


if __name__ == '__main__':
    write_mocks()
    write_board()
