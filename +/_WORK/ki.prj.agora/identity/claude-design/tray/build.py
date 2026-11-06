"""Builds the tray menu mockup sheet, tray-menu.html, from the three states below.

Run: python3 build.py   (then open tray-menu.html; tray-menu.png is a screenshot of it)

The menu is drawn to look like the native macOS menu Agora uses (Electron's Menu), so its colours are the
system's, not ki-design tokens; the sheet around it uses the ki-design paper (light) and navy (night).
The menu-bar symbol is the shipped meeting ring from apps-agora.local/assets/tray/svg.
"""
from html import escape

RING = {
    'present': '''<path d="M5.16 15.15 A7.25 7.25 0 1 1 12.84 15.15" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
      <circle cx="9" cy="5.2" r="1.6" fill="currentColor"/><circle cx="12.29" cy="10.9" r="1.6" fill="currentColor"/><circle cx="5.71" cy="10.9" r="1.6" fill="currentColor"/>''',
    'present-look': '''<mask id="lk{n}"><rect width="18" height="18" fill="#fff"/><path d="M14.6 -0.25 L18.25 3.4 L14.6 7.05 L10.95 3.4 Z" fill="#000" stroke="#000" stroke-width="1" stroke-linejoin="round"/></mask>
      <g mask="url(#lk{n})"><path d="M5.16 15.15 A7.25 7.25 0 1 1 12.84 15.15" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></g>
      <path d="M14.6 0.85 L17.15 3.4 L14.6 5.95 L12.05 3.4 Z" fill="currentColor" stroke="currentColor" stroke-width="0.6" stroke-linejoin="round"/>
      <circle cx="9" cy="5.2" r="1.6" fill="currentColor"/><circle cx="12.29" cy="10.9" r="1.6" fill="currentColor"/><circle cx="5.71" cy="10.9" r="1.6" fill="currentColor"/>''',
    'unheard': '''<path d="M5.16 15.15 A7.25 7.25 0 1 1 12.84 15.15" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
      <circle cx="9" cy="5.2" r="1.6" fill="currentColor"/><circle cx="12.29" cy="10.9" r="1.1" fill="none" stroke="currentColor" stroke-width="1"/><circle cx="5.71" cy="10.9" r="1.6" fill="currentColor"/>''',
}

# Small template marks for exception rows, drawn like the tray's own marks.
MARK = {
    'look': '<svg class="mk" viewBox="0 0 12 12"><path d="M6 1.5 L10.5 6 L6 10.5 L1.5 6 Z" fill="currentColor"/></svg>',
    'unheard': '<svg class="mk" viewBox="0 0 12 12"><circle cx="6" cy="6" r="3.6" fill="none" stroke="currentColor" stroke-width="1.4"/></svg>',
    'listening': '<svg class="mk" viewBox="0 0 12 12"><circle cx="6" cy="6" r="3.6" fill="currentColor"/></svg>',
    'silent': '<svg class="mk" viewBox="0 0 12 12"><circle cx="6" cy="6" r="3.6" fill="none" stroke="currentColor" stroke-width="1.4"/><path d="M3.5 8.5 L8.5 3.5" stroke="currentColor" stroke-width="1.4"/></svg>',
}

SEP = ('sep',)


def item(label, sub=None, submenu=False, disabled=False, header=False, mark=None, check=False, open_=False, strong=False):
    return ('item', dict(label=label, sub=sub, submenu=submenu, disabled=disabled, header=header, mark=mark,
                         check=check, open=open_, strong=strong))


def actions(away=None):
    rows = [item('Broadcast…')]
    rows.append(item("I'm back", sub=f'Away until {away}') if away else item('Away…', submenu=True))
    rows += [item('Ping'), item('Mark all', submenu=True)]
    return rows


def detail(open_=None, news_new=0):
    labels = ['Agents', 'Macs and checkouts', 'Runs', 'Broadcasts', f'News · {news_new} new' if news_new else 'News']
    return [item(label, submenu=True, open_=(open_ == label.split(' ·')[0])) for label in labels]


def tail(mac='sol'):
    return [SEP, item('Sync now'), item('Open log'), SEP, item('About Agora'), item('Quit Agora', sub=f'{mac} leaves the Agora')]


AGENTS_FLYOUT = [
    item('sol · this Mac', header=True),
    item('ki.prj.agora · ★ send', mark='listening'),
    item('ki.sop.main · ★ themes', mark='listening'),
    item('personal.reg.inbox-sol · ★ method', mark='listening'),
    item('personal.reg.household-sol · ★ rig', mark='listening'),
    SEP,
    item('terra', header=True),
    item('hnr.sop.main · ★ hnr', mark='listening'),
    item('hnr.prj.5g-emerge-phase3 · ★ delivery', mark='listening'),
    item('hnr.prj.5g-emerge-p2ms3 · ★ delivery', mark='listening'),
    item('hnr.prj.site-robots · ★ site', mark='listening'),
    item('personal.reg.inbox-terra · ★ method', mark='listening'),
    item('personal.reg.household-terra · ★ rig', mark='listening'),
    SEP,
    item('Who’s doing what…'),
]

LOOK_FLYOUT = [
    item('Ahead 1, behind 2 of origin/main', disabled=True),
    item('Agora has left it as it is', disabled=True),
    item('Called hnr.sop.main at 04:12 to settle it', disabled=True),
    SEP,
    item('Call hnr.sop.main again'),
    item('Show in Finder'),
]

MAC_FLYOUT = [
    item('Last heard at 03:41', disabled=True),
    item('Its 6 agents are not counted until it is back', disabled=True),
    item('1 broadcast waits for it', disabled=True),
    item('Nothing it holds is taken over', disabled=True),
    SEP,
    item('Ask after terra now'),
]

STATES = [
    dict(key='all-well', title='All well', icon='present', flyout_at='Agents', flyout=AGENTS_FLYOUT,
         rows=[item('10 agents on 2 Macs', strong=True), item('All well', strong=True), SEP,
               *actions(), SEP, *detail(open_='Agents'), *tail()]),
    dict(key='one-problem', title='One problem', icon='present-look', flyout_at='hnr-principal on terra is diverged',
         flyout=LOOK_FLYOUT,
         rows=[item('10 agents on 2 Macs', strong=True), item('1 needs a look', strong=True),
               item('hnr-principal on terra is diverged', submenu=True, mark='look', open_=True), SEP,
               *actions(), SEP, *detail(news_new=2), *tail()]),
    dict(key='mac-missing', title='A Mac missing', icon='unheard', flyout_at='terra not heard from since 03:41',
         flyout=MAC_FLYOUT,
         rows=[item('4 agents on 1 Mac', strong=True), item('1 needs a look', strong=True),
               item('terra not heard from since 03:41', submenu=True, mark='unheard', open_=True), SEP,
               *actions(away='08:00'), SEP, *detail(), *tail()]),
]


def render_rows(rows):
    out = []
    for row in rows:
        if row[0] == 'sep':
            out.append('<div class="sep"></div>')
            continue
        r = row[1]
        cls = ['it']
        if r['disabled']:
            cls.append('dis')
        if r['header']:
            cls.append('hdr')
        if r['open']:
            cls.append('open')
        if r['strong']:
            cls.append('strong')
        mark = MARK[r['mark']] if r['mark'] else ''
        chev = '<span class="chev">›</span>' if r['submenu'] else ''
        sub = f'<span class="sub">{escape(r["sub"])}</span>' if r['sub'] else ''
        label = escape(r['label']).replace('★', '<span class="star">★</span>')
        out.append(f'<div class="{" ".join(cls)}"><span class="lbl">{mark}{label}{sub}</span>{chev}</div>')
    return '\n'.join(out)


def flyout_offset(rows, at):
    """The flyout's top, in px, so it lines up with the open row (5 px panel padding, rows 22 px, separators 11 px)."""
    y = 5
    for row in rows:
        if row[0] == 'sep':
            y += 11
            continue
        r = row[1]
        if r['label'] == at or r['label'].split(' ·')[0] == at:
            return y - 5
        y += 22 + (14 if r['sub'] else 0)
    return 0


def panel(state, theme, n):
    ring = RING[state['icon']].replace('{n}', f'{n}')
    top = flyout_offset(state['rows'], state['flyout_at'])
    return f'''<figure class="panel {theme}">
  <div class="bar"><span class="clock">Fri 6 Nov 04:20</span><svg class="ring" viewBox="0 0 18 18">{ring}</svg></div>
  <div class="menus">
    <div class="menu">{render_rows(state["rows"])}</div>
    <div class="menu fly" style="margin-top:{top}px">{render_rows(state["flyout"])}</div>
  </div>
  <figcaption>{escape(state["title"])} · {"light" if theme == "light" else "dark"}</figcaption>
</figure>'''


CSS = '''
:root { --paper:#f5efe0; --ink:#1a2030; --muted:#4a5568; --navy:#0f2440; }
* { box-sizing:border-box; }
body { margin:0; font:13px/1 -apple-system, BlinkMacSystemFont, "SF Pro Text", Inter, "Helvetica Neue", Arial, sans-serif; background:var(--paper); color:var(--ink); }
header { padding:24px 28px 8px; }
h1 { font:600 20px/1.3 inherit; margin:0 0 4px; }
header p { margin:0; color:var(--muted); font-size:13px; line-height:1.5; max-width:880px; }
.row { display:flex; gap:24px; padding:16px 28px 24px; }
.row.dark { background:var(--navy); }
.panel { margin:0; flex:0 0 auto; }
.panel figcaption { margin-top:10px; font-size:12px; color:var(--muted); }
.row.dark figcaption { color:#a9b4c4; }
.bar { height:26px; display:flex; justify-content:flex-end; align-items:center; gap:14px; padding:0 14px; border-radius:6px 6px 0 0; width:300px; }
.light .bar { background:rgba(236,236,236,.95); color:#1d1d1f; }
.dark .bar { background:rgba(40,40,44,.95); color:#f2f2f7; }
.bar .ring { width:18px; height:18px; }
.bar .clock { font-size:13px; }
.menus { display:flex; align-items:flex-start; gap:2px; }
.menu { width:300px; padding:5px; border-radius:9px; box-shadow:0 8px 24px rgba(0,0,0,.22), 0 0 0 .5px rgba(0,0,0,.25); }
.light .menu { background:#f4f4f5; color:#1d1d1f; }
.dark .menu { background:#2e2e32; color:#f2f2f7; box-shadow:0 8px 24px rgba(0,0,0,.5), 0 0 0 .5px rgba(255,255,255,.18); }
.menu.fly { width:300px; }
.it { min-height:22px; padding:4px 10px; border-radius:5px; display:flex; justify-content:space-between; align-items:center; white-space:nowrap; }
.it .lbl { display:flex; align-items:center; flex-wrap:wrap; gap:0 6px; }
.it .sub { flex-basis:100%; font-size:11px; opacity:.6; margin-top:2px; }
.it.strong { font-weight:600; }
.it.dis { opacity:.55; }
.it.hdr { font-size:11px; font-weight:600; opacity:.55; min-height:20px; padding-top:6px; }
.it.open { background:#0a64d6; color:#fff; }
.dark .it.open { background:#1d6bd8; }
.chev { opacity:.6; font-size:15px; line-height:0; margin-left:12px; }
.open .chev { opacity:1; }
.mk { width:11px; height:11px; flex:0 0 11px; }
.star { font-size:11px; }
.sep { height:1px; margin:5px 10px; }
.light .sep { background:rgba(0,0,0,.12); }
.dark .sep { background:rgba(255,255,255,.14); }
'''


def page():
    light = '\n'.join(panel(s, 'light', i) for i, s in enumerate(STATES))
    dark = '\n'.join(panel(s, 'dark', i + 10) for i, s in enumerate(STATES))
    return f'''<!doctype html>
<html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Agora tray menu</title><style>{CSS}</style></head>
<body>
<header>
  <h1>Agora tray menu, proposed</h1>
  <p>Three states, light and dark. Two summary lines, then only what is wrong, then the actions, then detail on demand. The open submenu in each shows what sits one level down. Focus areas marked ★ are the agent's primary; those other than ki.prj.agora's, ki.sop.main's and personal.reg.inbox-sol's are placeholders.</p>
</header>
<section class="row light">{light}</section>
<section class="row dark">{dark}</section>
</body></html>
'''


if __name__ == '__main__':
    with open('tray-menu.html', 'w', encoding='utf-8') as f:
        f.write(page())
