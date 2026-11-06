"""Agora Atlas page 9.1 Home: who holds what, what needs a look, and the roles yours to approve.

Home leaves the sidebar in 0.4 and is reached from the Agora Atlas logo. It answers three questions in one window:
what needs a look (each item says what it is and what to do), who holds which role in each live package, and which
roles the guild catalogue names that nobody holds yet. The roster is build/data.py's twelve agents (sol 5, terra 7) and
two doers; the roles, tiers and the catalogue's disagreements are illustrative.

The role and state glyphs are Kris's emoji (review 22:55 to 23:20 GMT), drawn as emoji. Each is always beside its word.
"""
from html import escape

from mocks import R, head, tray_frame, atlas_page, aglyph

ROLES = {
    'governor': ('🏛️', 'Governor'), 'guildmaster': ('⚖️', 'Guildmaster'), 'housekeeper': ('🏠', 'Housekeeper'),
    'keeper': ('📡', "Agora's keeper"), 'warden': ('⚒️', 'Warden'), 'quartermaster': ('🧰', 'Quartermaster'),
    None: ('', 'No role'),
}
STATES = {
    'working': ('🤖', 'Working', 'A run is going now'),
    'with-you': ('👤', 'With you', 'Kris is in a session with it'),
    'idle': ('💤', 'Idle', 'Listening, nothing running'),
    'silent': ('🔕', 'Silent', 'Calls unanswered'),
}
TERR = {'ki': 'Knowledge Islands', 'hnr': 'Humans Not Robots', 'personal': 'Personal'}
TIER_ORDER = ('Leader', 'Manager', 'Doer')

# (package, role, tier, rig, territory, focus [(name, primary, scheduled)], state, footnote mark on (cell, mark))
HOLDERS = [
    ('ki.sop.main', 'governor', 'Leader', 'sol', 'ki', [('themes', 1, 0), ('acceptance', 0, 0), ('chain', 0, 1), ('_emerging', 0, 0)], 'working', None),
    ('personal.reg.inbox-sol', 'governor', 'Leader', 'sol', 'personal', [('method', 1, 0), ('kiv', 0, 1), ('coordination', 0, 0)], 'working', ('role', '†')),
    ('hnr.sop.main', 'governor', 'Leader', 'terra', 'hnr', [('routing', 1, 0), ('acceptance', 0, 1)], 'silent', None),
    ('ki.prj.agora', 'keeper', 'Manager', 'sol', 'ki', [('send', 1, 0), ('jobs', 0, 1), ('voice', 0, 0), ('identity', 0, 0)], 'with-you', None),
    ('personal.reg.household-sol', 'housekeeper', 'Manager', 'sol', 'personal', [('rig', 1, 0), ('install', 0, 0), ('settings', 0, 1)], 'idle', None),
    ('personal.reg.household-terra', 'housekeeper', 'Manager', 'terra', 'personal', [('rig', 1, 0), ('install', 0, 1)], 'idle', None),
    ('personal.reg.watchman-sol', 'warden', 'Manager', 'sol', 'personal', [('portal', 1, 1)], 'working', None),
    ('personal.reg.watchman-terra', 'warden', 'Manager', 'terra', 'personal', [('portal', 1, 1)], 'working', None),
    ('personal.reg.inbox-terra', None, 'Manager', 'terra', 'personal', [('method', 1, 0), ('records', 0, 1)], 'idle', ('role', '‡')),
    ('hnr.prj.5g-emerge-phase3', None, 'Manager', 'terra', 'hnr', [('delivery', 1, 0), ('reporting', 0, 1)], 'idle', None),
    ('hnr.prj.5g-emerge-p2ms3', None, 'Manager', 'terra', 'hnr', [('delivery', 1, 0)], 'working', None),
    ('hnr.prj.site-robots', None, 'Manager', 'terra', 'hnr', [('site', 1, 0), ('content', 0, 0)], 'silent', ('tier', '§')),
    ('Claude Design', None, 'Doer', 'sol', 'ki', [('design pack', 1, 0), ('Atlas shell', 0, 0)], 'working', None),
    ('Build run · Atlas Guilds', None, 'Doer', 'sol', 'ki', [('8.2 Guilds', 1, 0)], 'working', None),
]
DOER_WITH = {'Claude Design': 'ki.prj.agora', 'Build run · Atlas Guilds': 'ki.prj.agora'}
FOOTNOTES = [
    ('†', 'personal.reg.inbox-sol', 'Its work.md calls its role "assistant". The guild catalogue has no assistant role; it names Personal\'s leader Governor, so the row shows Governor.'),
    ('‡', 'personal.reg.inbox-terra', 'Its work.md says Governor. The catalogue allows one Governor in a territory, and Personal\'s is inbox-sol, so the catalogue gives this one no role.'),
    ('§', 'hnr.prj.site-robots', 'Its work.md says tier Leader. The catalogue makes a project package a Manager under its territory\'s Governor.'),
]
TO_APPROVE = [
    ('guildmaster', 'Manager', 'Knowledge Islands', 'ki.reg.guilds', 'sol', 'Keeps the guild catalogue and each guild\'s skills'),
    ('guildmaster', 'Manager', 'Humans Not Robots', 'hnr.reg.guilds', 'terra', 'Keeps Humans Not Robots\' own skills'),
    ('quartermaster', 'Manager', 'Personal', 'personal.reg.quartermaster', 'sol', 'Keeps accounts, licences and the tools each rig needs'),
]
# What needs a look: (level, what it is, what to do, action words). level is 'urgent' or 'look'.
NEEDS = [
    ('urgent', '<b>hnr.sop.main is silent</b> on terra: 2 calls unanswered since 02:10.', 'Ping it; if it stays silent, open a session on terra.', 'Ping'),
    ('look', '<b>2 checkouts must settle</b>: ki-principal is diverged on terra, hnr-principal is ahead on sol.', 'Agora will not resolve them. Settle each in a terminal on its rig.', 'Show checkouts'),
    ('look', '<b>The job sop-digest failed</b> on sol at 04:00.', 'Read its last run, then fix it in Rig.', 'Show its runs'),
    ('look', '<b>34 queries wait on you</b>, 18 of them ki.sop.main\'s.', 'Answer them in Waits on you, oldest first.', 'Open Waits on you'),
]


def emo(e, cls='emo'):
    return f'<span class="{cls}" aria-hidden="true">{e}</span>' if e else ''


def role_cell(role, fn=None, doer_with=None):
    if doer_with:
        return f'<span class="muted" title="A doer, brought in by {doer_with}">With <span class="mono">{doer_with}</span></span>'
    e, word = ROLES[role]
    mark = f'<sup class="fn">{fn}</sup>' if fn else ''
    if not role:
        return f'<span class="muted">No role</span>{mark}'
    return f'{emo(e)}<span class="rw">{escape(word)}</span>{mark}'


def focus_cell(focus):
    parts = []
    for name, primary, sched in focus:
        txt = f'<b>{escape(name)}</b>' if primary else escape(name)
        star = '<span class="emo sm" title="Primary">⭐</span>' if primary else ''
        clock = '<span class="emo sm" title="Scheduled">⏰</span>' if sched else ''
        parts.append(f'<span class="fa">{star}{txt}{clock}</span>')
    return '<span class="focusline">' + '<span class="dotsep">·</span>'.join(parts) + '</span>'


def state_cell(state):
    e, word, hint = STATES[state]
    return f'<span class="hstate st-{state}" title="{hint}">{emo(e)}{word}</span>'


def holder_row(h, selected=None, show_rig=True):
    pkg, role, tier, rig, terr, focus, state, fn = h
    fn_cell, fn_mark = fn if fn else (None, None)
    cls = 'holder' + (' sel' if pkg == selected else '') + (' doer' if tier == 'Doer' else '') + (' disagree' if fn else '')
    tier_html = escape(tier) + (f'<sup class="fn">{fn_mark}</sup>' if fn_cell == 'tier' else '')
    pkg_html = f'<span class="mono">{escape(pkg)}</span>' if tier != 'Doer' else escape(pkg)
    rig_td = f'<td class="mono">{rig}</td>' if show_rig else ''
    return (f'<tr class="{cls}" data-holder="{escape(pkg)}"><td class="role">{role_cell(role, fn_mark if fn_cell == "role" else None, DOER_WITH.get(pkg))}</td>'
            f'<td>{tier_html}</td><td>{pkg_html}</td>{rig_td}<td class="focus">{focus_cell(focus)}</td><td>{state_cell(state)}</td></tr>')


def holders_table(rows_html, code='P3', show_rig=True, label='Who holds what', compact=False):
    rig = '<th>Rig</th>' if show_rig else ''
    w = (140, 76, 206, 58, 100) if compact else (190, 84, 236, 58, 116)
    return (f'<section class="panel tablepanel holders" {R(code, label)}><table class="holders">'
            f'<colgroup><col style="width:{w[0]}px"><col style="width:{w[1]}px"><col style="width:{w[2]}px">{f"<col style=width:{w[3]}px>" if show_rig else ""}<col><col style="width:{w[4]}px"></colgroup>'
            f'<thead><tr><th>Role</th><th>Tier</th><th>Package</th>{rig}<th>Focus areas</th><th>State</th></tr></thead>'
            f'<tbody>{rows_html}</tbody></table></section>')


def footnotes(code='P4'):
    items = ''.join(f'<li><sup class="fn">{m}</sup><span class="mono">{p}</span> {escape(t)}</li>' for m, p, t in FOOTNOTES)
    key = '<li class="key"><span class="emo sm">⭐</span>the primary focus, in bold · <span class="emo sm">⏰</span>something scheduled</li>'
    return (f'<section class="footnotes" {R(code, "Footnotes: where a record and the catalogue disagree")}><ol>{key}{items}</ol>'
            f'<p class="muted">The row shows the catalogue; the package\'s record is unchanged until its owner amends it.</p></section>')


def needs_look(code='P2', items=None):
    items = NEEDS if items is None else items
    if not items:
        body = '<p class="muted nothing">Nothing needs a look. Every rig is present, every checkout level, every job ran.</p>'
    else:
        rows = ''.join(
            f'<tr class="need lvl-{lvl}"><td class="lvl">{"▲ Urgent" if lvl == "urgent" else "● Look"}</td><td>{what}</td>'
            f'<td class="muted">{escape(todo)}</td><td class="act"><span class="btn">{escape(act)}</span></td></tr>' for lvl, what, todo, act in items)
        body = f'<table class="needs"><colgroup><col style="width:84px"><col><col style="width:330px"><col style="width:150px"></colgroup><tbody>{rows}</tbody></table>'
    n = len(items)
    return (f'<section class="panel needspanel" id="needs" {R(code, "Needs a look")}><header><h2>Needs a look</h2>'
            f'<span class="muted">{n} {"thing" if n == 1 else "things"} · the toolbar\'s indicator leads here</span></header>{body}</section>')


def to_approve(code='P5', compact=False):
    what_td = (lambda what: '') if compact else (lambda what: f'<td class="muted">{escape(what)}</td>')
    rows = ''.join(
        f'<tr title="{escape(what)}"><td class="role">{emo(ROLES[r][0])}<span class="rw">{ROLES[r][1]}</span></td><td>{tier}</td><td>{escape(terr)}</td>'
        f'<td class="mono">{pkg}</td><td class="mono">{rig}</td>{what_td(what)}<td class="act"><span class="btn">Approve…</span></td></tr>'
        for r, tier, terr, pkg, rig, what in TO_APPROVE)
    if compact:
        cols = '<col style="width:150px"><col style="width:76px"><col style="width:150px"><col><col style="width:50px"><col style="width:110px">'
        th = '<th>Role</th><th>Tier</th><th>Territory</th><th>Proposed package</th><th>Rig</th><th></th>'
        return (f'<section class="panel tablepanel approve" {R(code, "Yours to approve")}><header><h2>Yours to approve</h2>'
                f'<span class="muted">Catalogue roles no package holds yet</span><span class="sp"></span><span class="btn brass">Approve all 3…</span></header>'
                f'<table><colgroup>{cols}</colgroup><thead><tr>{th}</tr></thead><tbody>{rows}</tbody></table></section>')
    return (f'<section class="panel tablepanel approve" {R(code, "Yours to approve")}><header><h2>Yours to approve</h2>'
            f'<span class="muted">Roles the guild catalogue names that no package holds yet; each needs a package created on its rig.</span>'
            f'<span class="sp"></span><span class="btn brass">Approve all 3…</span></header>'
            f'<table><colgroup><col style="width:190px"><col style="width:84px"><col style="width:150px"><col style="width:236px"><col style="width:58px"><col><col style="width:110px"></colgroup>'
            f'<thead><tr><th>Role</th><th>Tier</th><th>Territory</th><th>Proposed package</th><th>Rig</th><th>What it keeps</th><th></th></tr></thead>'
            f'<tbody>{rows}</tbody></table></section>')


def summary():
    working = sum(1 for h in HOLDERS if h[6] == 'working')
    silent = sum(1 for h in HOLDERS if h[6] == 'silent')
    return (f'12 packages and 2 doers on 2 rigs · 🤖 {working} working · 👤 1 with you · 🔕 {silent} silent · '
            f'3 records disagree with the catalogue · 3 roles yours to approve')


def ordered():
    return sorted(HOLDERS, key=lambda h: (TIER_ORDER.index(h[2]), h[3], h[0]))


def home_page(selected=None, needs=None):
    rows = ''.join(holder_row(h, selected) for h in ordered())
    c = selected is not None  # the tray is open, so the page is 360 points narrower
    return (f'{head("P1", "Home", summary(), tools="<span class=\"btn\">Show as the map</span>")}'
            f'{needs_look(items=needs)}{holders_table(rows, compact=c)}{footnotes()}{to_approve(compact=c)}')


def home_by_rig():
    rows = ''
    for rig in ('sol', 'terra'):
        hs = [h for h in ordered() if h[3] == rig]
        n_w = sum(1 for h in hs if h[6] == 'working')
        n_s = sum(1 for h in hs if h[6] == 'silent')
        sub = f'{len(hs)} · {n_w} working' + (f' · {n_s} silent' if n_s else '')
        rows += (f'<tr class="group grp" data-rig="{rig}"><td colspan="5">{aglyph("chev", "gchev")}<b>{rig}</b>'
                 f'<span class="muted gsub">{"this Mac" if rig == "sol" else "the other Mac, heard 04:20"} · {sub}</span></td></tr>')
        rows += ''.join(holder_row(h, show_rig=False) for h in hs)
    return (f'{head("P1", "Home", summary(), tools="<span class=\"btn\">Show as the map</span>")}'
            f'{needs_look()}{holders_table(rows, show_rig=False, label="Who holds what, by rig")}{footnotes()}{to_approve()}')


def holder_tray(pkg='personal.reg.inbox-terra'):
    h = next(x for x in HOLDERS if x[0] == pkg)
    pkg, role, tier, rig, terr, focus, state, fn = h
    e, word = ROLES[role]
    se, sw, sh = STATES[state]
    foc = ''.join(f'<p>{"⭐ " if p else ""}{"<b>" + n + "</b>" if p else n}{" ⏰ <span class=muted>scheduled, daily 07:30</span>" if s else ""}</p>' for n, p, s in focus)
    rows = [('Role', f'{emo(e)} {word} <sup class="fn">‡</sup>'), ('Tier', tier), ('Territory', TERR[terr]), ('Rig', f'<span class="mono">{rig}</span>'),
            ('State', f'{emo(se)} {sw} <span class="muted">· answered 04:08</span>'), ('Waits on you', '1 query, FOOTER-OWNER')]
    kv = ''.join(f'<tr><td>{k}</td><td>{v}</td></tr>' for k, v in rows)
    body = (f'<table class="kv"><tbody>{kv}</tbody></table><h3>Focus areas</h3>{foc}'
            f'<h3>Record and catalogue <sup class="fn">‡</sup></h3>'
            f'<table class="kv cmp"><tbody><tr><td></td><td class="muted">work.md</td><td class="muted">Catalogue</td></tr>'
            f'<tr><td>Role</td><td>🏛️ Governor</td><td><b>No role</b></td></tr><tr><td>Tier</td><td>Manager</td><td>Manager</td></tr></tbody></table>'
            f'<p class="muted">Personal has one Governor, inbox-sol. The record changes only when its owner amends it.</p>')
    return tray_frame(f'{word} · {TERR[terr]} · {rig}', f'<span class="id">{pkg}</span>', body,
                      actions=[('', 'Open its package'), ('', 'Show its record'), ('', 'Ping')])


def ab_home(theme='night'):
    return atlas_page('home', home_page(), theme=theme, height=None, tabs=[('Home', True, False), ('Roadmap', False, True)])


def ab_home_by_rig():
    return atlas_page('home', home_by_rig(), height=None, tabs=[('Home', True, False), ('Roadmap', False, True)])


def ab_home_selected():
    return atlas_page('home', home_page(selected='personal.reg.inbox-terra'), tray=holder_tray(), height=None,
                      tabs=[('Home', True, False), ('Roadmap', False, True)])
