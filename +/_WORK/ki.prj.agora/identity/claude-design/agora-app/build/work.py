"""Agora Atlas pages 7.1 Roadmap, 7.2 Jobs and 8.1 Guilds, drawn in the 0.3 shell (atlas_page).

The data follows what the built app reads (apps-agora.local, src/app/roadmap.ts, jobs.ts, guilds.ts): a work record's
front matter (status, priority, size, horizon, area, kind, assignee, blocks, blocked by), a job as Rig declares it with
its runs' outcome, one-line summary and finish time, and each skill in its harness's guild folder. Values are
illustrative; ids, titles, statuses and skill names are taken from the lands where they exist.

The shared pattern is the summary-filter bar (sf_bar): tallies that count and filter, chips, one Filter menu, words to
find, and Group. Roadmap and Jobs both use it; the guild badges on Guilds are its tallies in another shape.
"""
from html import escape

import mocks as M
from mocks import R, head, aglyph, tray_frame, bottom_frame, atlas_page

NOW = '04:20'

# ---------------------------------------------------------------- small marks (12 grid): shape carries the meaning, colour repeats it
def smark(kind):
    p = {
        'in-progress': '<circle cx="6" cy="6" r="4" fill="currentColor"/>',
        'awaiting-review': '<path d="M6 1.5 L10.5 6 L6 10.5 L1.5 6 Z" fill="currentColor"/>',
        'ready': '<circle cx="6" cy="6" r="3.8" fill="none" stroke="currentColor" stroke-width="1.4"/>',
        'draft': '<circle cx="6" cy="6" r="3.8" fill="none" stroke="currentColor" stroke-width="1.3" stroke-dasharray="2 1.6"/>',
        'triage': '<rect x="2.3" y="2.3" width="7.4" height="7.4" rx="1" fill="none" stroke="currentColor" stroke-width="1.4"/>',
        'done': '<path d="M2.5 6.3 L5 8.8 L9.8 3.4" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>',
        'cancelled': '<circle cx="6" cy="6" r="3.8" fill="none" stroke="currentColor" stroke-width="1.3"/><path d="M3.3 8.7 L8.7 3.3" stroke="currentColor" stroke-width="1.3"/>',
        # job outcomes
        'ok': '<circle cx="6" cy="6" r="4" fill="currentColor"/>',
        'findings': '<path d="M6 1.8 L10.2 6 L6 10.2 L1.8 6 Z" fill="none" stroke="currentColor" stroke-width="1.4"/>',
        'failed': '<circle cx="6" cy="6" r="3.8" fill="none" stroke="currentColor" stroke-width="1.4"/><path d="M3.3 8.7 L8.7 3.3" stroke="currentColor" stroke-width="1.4"/>',
        'unreadable': '<circle cx="6" cy="6" r="3.8" fill="none" stroke="currentColor" stroke-width="1.3" stroke-dasharray="2 1.6"/>',
        'never': '<path d="M3 6h6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>',
        'disabled': '<path d="M3 6h6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><circle cx="6" cy="6" r="4.4" fill="none" stroke="currentColor" stroke-width="1"/>',
        'service': '<path d="M2 6h2l1.3-3 2 6 1.3-3H10" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linejoin="round"/>',
        'all': '<path d="M2 3.5h8M2 6h8M2 8.5h8" stroke="currentColor" stroke-width="1.3"/>',
        'hidden': '<path d="M1.5 6c1.3-2.2 2.8-3.2 4.5-3.2S9.2 3.8 10.5 6c-1.3 2.2-2.8 3.2-4.5 3.2S2.8 8.2 1.5 6z" fill="none" stroke="currentColor" stroke-width="1.1"/><path d="M2 10L10 2" stroke="currentColor" stroke-width="1.1"/>',
    }[kind]
    return f'<svg class="sm sm-{kind}" viewBox="0 0 12 12" aria-hidden="true">{p}</svg>'


STATUS_WORDS = {'in-progress': 'In progress', 'awaiting-review': 'Awaiting review', 'ready': 'Ready', 'draft': 'Draft',
                'triage': 'Triage', 'done': 'Done', 'cancelled': 'Cancelled'}
STATUS_ORDER = ['in-progress', 'awaiting-review', 'ready', 'draft', 'triage']


def status_pill(s):
    return f'<span class="st st-{s}">{smark(s)}{STATUS_WORDS[s]}</span>'


STANDING_WORDS = {'failed': 'Failed', 'unreadable': 'Unreadable', 'findings': 'Findings', 'ok': 'OK',
                  'never': 'No run yet', 'disabled': 'Off', 'service': 'Service'}


def standing_pill(s):
    return f'<span class="st js-{s}">{smark(s)}{STANDING_WORDS[s]}</span>'


# ---------------------------------------------------------------- the summary-filter bar (component 7.1.1)
def tally(key, n, words, on=False, attn=False, zero=False, glyph=None, note=''):
    cls = 'tally' + (' on' if on else '') + (' attn' if attn else '') + (' zero' if zero or n == 0 else '')
    g = smark(glyph or key)
    note_html = f'<span class="tn">{note}</span>' if note else ''
    return (f'<span class="{cls}" data-tally="{key}" title="{escape(words)}: keep only these; ⌘-click to add">'
            f'<span class="v">{g}<b>{n}</b>{note_html}</span><span class="k">{escape(words)}</span></span>')


def ctx_chip(field, value):
    return (f'<span class="fchip ctx" data-chip="ctx" title="Set by the context control, top right">'
            f'{f"<span class=f>{field}</span>" if field else ""}{escape(value)}<span class="from">context</span></span>')


def chosen_chip(field, value):
    return (f'<span class="fchip" data-chip="chosen"><span class="f">{field}</span>{escape(value)}'
            f'<span class="x" title="Remove">×</span></span>')


def filter_button(open_=False, n=0):
    lab = f'Filter{f" · {n}" if n else ""}'
    return f'<span class="btn fbtn{" open" if open_ else ""}" data-chip="field">{aglyph("chev")}{lab}</span>'


def find_box(words='', hint='Words in an id or title'):
    inner = f'<b>{escape(words)}</b>' if words else escape(hint)
    return f'<span class="find sffind">{aglyph("search")}{inner}</span>'


def group_seg(options, on):
    segs = ''.join(f'<span{" class=on" if o == on else ""}>{o}</span>' for o in options)
    return f'<span class="sfgroup"><span class="lbl">Group</span><span class="seg">{segs}</span></span>'


def sf_bar(tallies, chips, find, group, menu='', code='P2', note=''):
    note_html = f'<span class="sfnote">{note}</span>' if note else ''
    return (f'<section class="sf" {R(code, "Summary and filters")}><div class="sf-tallies">{"".join(tallies)}</div>'
            f'<div class="sf-row"><span class="sfchips">{"".join(chips)}</span>{find}{note_html}<span class="sp"></span>{group}</div>{menu}</section>')


# ================================================================ 7.1 Roadmap
# (id, title, island, area, status, priority, size, horizon, kind, assignee, updated)
RECORDS = [
    ('KI-OBSERVA-SIG-012', 'Signals land in their view', 'apps-observatory.local', 'SIG', 'in-progress', 'high', 's', 'now', 'deliver', 'work/ki.prj.observatory', '40 min'),
    ('KI-HARN-GLD-003', 'The guild catalogue', 'ki-agentic-harness', 'GLD', 'in-progress', 'medium', 'm', 'now', 'deliver', 'work/ki.reg.guilds', '2 h'),
    ('KI-AGORA-TRY-001', 'Menu-bar identity', 'apps-agora.local', 'TRY', 'awaiting-review', 'medium', 'm', 'now', 'deliver', 'work/ki.prj.agora', '3 d'),
    ('KI-AGORA-WRK-007', 'Floating doers', 'apps-agora.local', 'WRK', 'ready', 'medium', 'l', 'next', 'deliver', None, '1 d'),
    ('KI-TOOL-KI-CLI-181', 'ki agent status as JSON', 'tools-ki', 'CLI', 'ready', 'high', 's', 'next', 'deliver', None, '2 d'),
    ('KI-DESIGN-TOK-009', 'Tray and pane tokens', 'ki-design', 'TOK', 'ready', 'medium', 'm', 'next', 'deliver', None, '3 d'),
    ('KI-OBSERVA-APP-044', 'Instrument restructure decision', 'apps-observatory.local', 'APP', 'draft', None, 'm', 'now', 'decide', None, '8 d'),
    ('KI-OBSERVA-VIS-045', 'Workers instrument', 'apps-observatory.local', 'VIS', 'draft', None, 'm', 'hold', 'deliver', None, '15 d'),
    ('KI-OBSERVA-VIS-034', 'Streams instrument', 'apps-observatory.local', 'VIS', 'draft', None, 'm', 'hold', 'deliver', None, '18 d'),
    ('KI-AGORA-WRK-004', 'Run the rig’s scheduled jobs', 'apps-agora.local', 'WRK', 'triage', 'high', 'l', None, None, 'work/ki.prj.agora', '4 h'),
    ('KI-AGORA-LVL-001', 'Check host settings against Rig', 'apps-agora.local', 'LVL', 'triage', 'medium', 'm', None, None, 'work/ki.prj.agora', '5 h'),
    ('KI-AGORA-WRK-003', 'Keep the host awake while work runs', 'apps-agora.local', 'WRK', 'triage', 'medium', 'm', None, None, 'work/ki.prj.agora', '5 h'),
    ('KI-TOOL-KI-CLI-178', 'Sent pass and forward-match logging', 'tools-ki', 'CLI', 'triage', 'medium', 'm', None, None, 'work/ki.sop.main', '7 h'),
    ('KI-AGORA-WRK-002', 'Switch Claude accounts', 'apps-agora.local', 'WRK', 'triage', 'high', 'm', None, None, None, '1 d'),
    ('KI-TOOL-KI-CLI-176', 'Git-style extension veneer', 'tools-ki', 'CLI', 'triage', 'medium', 'm', None, None, None, '1 d'),
]
BYID = {r[0]: r for r in RECORDS}
STATUS_COUNT = {'in-progress': 2, 'awaiting-review': 1, 'ready': 3, 'draft': 9, 'triage': 23}
CLOSED_COUNT = 44


def record_row(r, selected=None, show_island=True):
    rid, title, island, area, st, pri, size, hor, *_ = r
    cls = 'rec' + (' sel' if rid == selected else '')
    pri_html = f'<span class="pri pri-{pri}">{pri}</span>' if pri else '<span class="muted">—</span>'
    isl = f'<td class="mono muted isl">{island}</td>' if show_island else ''
    return (f'<tr class="{cls}" data-row="{rid}"><td class="id">{rid}</td><td class="ttl">{escape(title)}</td>{isl}'
            f'<td>{status_pill(st)}</td><td class="nowrap">{pri_html}<span class="muted"> · {size.upper()}</span></td>'
            f'<td class="muted nowrap upd">{r[10]}</td></tr>')


def group_row(key, words, n, cols, glyph=None, sub=''):
    g = smark(glyph) if glyph else ''
    sub_html = f'<span class="muted gsub">{sub}</span>' if sub else ''
    return (f'<tr class="group grp" data-grp="{key}"><td colspan="{cols}">{aglyph("chev", "gchev")}{g}<b>{escape(words)}</b>'
            f'<span class="gn">{n}</span>{sub_html}</td></tr>')


def more_row(n, words, cols):
    return f'<tr class="more"><td colspan="{cols}">Show {n} more {words}</td></tr>'


def record_table(rows_html, code='P3', show_island=True):
    isl = '<th>Island</th>' if show_island else ''
    return (f'<section class="panel tablepanel" {R(code, "Records")}><table class="records">'
            f'<thead><tr><th>Record</th><th>Title</th>{isl}<th>Status</th><th>Priority · size</th><th>Updated</th></tr></thead>'
            f'<tbody>{rows_html}</tbody></table></section>')


def roadmap_tallies(on=None, counts=None, closed_note='hidden', attn=True):
    counts = counts or STATUS_COUNT
    total = sum(counts.values())
    t = [tally('all', total, 'All open', on=on is None, glyph='all')]
    for s in STATUS_ORDER:
        t.append(tally(s, counts[s], STATUS_WORDS[s], on=(on == s or (isinstance(on, tuple) and s in on)),
                       attn=(s == 'awaiting-review' and attn and counts[s] > 0)))
    t.append(tally('closed', CLOSED_COUNT, 'Closed', glyph='hidden', note=closed_note, zero=True))
    return t


def roadmap_grouped(selected=None, fold=(2, 3)):
    """Grouped by status: each group's heading with its count; a long group folds after a few rows."""
    out = []
    for s in STATUS_ORDER:
        rows = [r for r in RECORDS if r[4] == s]
        out.append(group_row(s, STATUS_WORDS[s], STATUS_COUNT[s], 6, glyph=s))
        limit = {'draft': fold[0], 'triage': fold[1]}.get(s, 99)
        if s == 'triage' and selected in [r[0] for r in rows[limit:]]:
            limit = 99
        out += [record_row(r, selected) for r in rows[:limit]]
        if STATUS_COUNT[s] > limit:
            out.append(more_row(STATUS_COUNT[s] - limit, STATUS_WORDS[s].lower() + ' records', 6))
    return ''.join(out)


def roadmap_bar(on=None, chips=None, find='', group='Status', menu='', counts=None, n_filters=0, note=''):
    chips = [ctx_chip('Territory', 'Knowledge Islands')] + (chips or []) + [filter_button(bool(menu), n_filters)]
    return sf_bar(roadmap_tallies(on, counts), chips, find_box(find), group_seg(['Status', 'Island', 'Area', 'None'], group), menu, note=note)


def roadmap_page(selected='KI-AGORA-WRK-004'):
    """7.1a: tallies over a table grouped by status."""
    return (head('P1', 'Roadmap', f'38 open records in Knowledge Islands · 44 done or cancelled, hidden · read {NOW}')
            + roadmap_bar() + record_table(roadmap_grouped(selected), show_island=True))


def record_tray(rid='KI-AGORA-WRK-004'):
    r = BYID[rid]
    rid, title, island, area, st, pri, size, hor, kind, assignee, upd = r
    detail = {
        'KI-AGORA-WRK-004': dict(created='2 Nov', updated='00:18 today', blocks=[('KI-AGORA-WRK-006', 'Run-once jobs')],
                                 blocked=[('KI-AGORA-WRK-001', 'Wake workers')],
                                 goal='Agora starts, stops and reports the rig’s scheduled jobs, so running them no longer needs Rig by hand on each Mac.',
                                 context='Jobs shows each job today but only reads. Moving the running here needs <span class="mono">ki agent</span> to stay the only way a run starts.'),
        'KI-AGORA-TRY-001': dict(created='31 Oct', updated='3 Nov 02:55', blocks=[], blocked=[],
                                 goal='The menu-bar ring says which Agora this is and whether all is well, in one glance, in light and night.',
                                 context='Delivered with Beacon’s ring and its three states. Waits for Kris to accept it or return it with notes.'),
    }[rid]
    def links(items):
        if not items:
            return '<p class="muted">Nothing</p>'
        return ''.join(f'<p class="lnk"><span class="id">{i}</span> {escape(t)}</p>' for i, t in items)
    rows = [('Status', status_pill(st)), ('Priority', pri or '—'), ('Size', size.upper()), ('Horizon', hor or '—'), ('Area', area),
            ('Kind', kind or '—'), ('Assignee', f'<span class="mono">{assignee}</span>' if assignee else '—'),
            ('Territory', 'Knowledge Islands'), ('Island', f'<span class="mono">{island}</span>'),
            ('Created', detail['created']), ('Updated', detail['updated'])]
    kv = ''.join(f'<tr><td>{k}</td><td>{v}</td></tr>' for k, v in rows)
    body = (f'<table class="kv"><tbody>{kv}</tbody></table>'
            f'<h3>Blocked by</h3>{links(detail["blocked"])}<h3>Blocks</h3>{links(detail["blocks"])}'
            f'<h3>Goal</h3><p>{detail["goal"]}</p><h3>Context</h3><p class="muted clamp">{detail["context"]}</p>')
    if st == 'awaiting-review':
        acts = [('brass', 'Open to review'), ('', 'Read in full'), ('', 'Show on Home')]
    else:
        acts = [('', 'Open the file'), ('', 'Read in full'), ('', 'Show on Home')]
    return tray_frame(f'Work record · {island}', f'<span class="id">{rid}</span><span class="tsub">{escape(title)}</span>', body, actions=acts)


def roadmap_filtered():
    """7.1c: a tally and a chip applied, the Filter menu open, grouped by island."""
    keep = ['KI-AGORA-WRK-004', 'KI-AGORA-WRK-002', 'KI-TOOL-KI-CLI-185', 'KI-OBSERVA-NET-007']
    extra = {
        'KI-TOOL-KI-CLI-185': ('KI-TOOL-KI-CLI-185', 'Machine contract for agent runs', 'tools-ki', 'CLI', 'triage', 'high', 's', None, None, None, '2 d'),
        'KI-OBSERVA-NET-007': ('KI-OBSERVA-NET-007', 'Read Agora’s state endpoint', 'apps-observatory.local', 'NET', 'triage', 'high', 'm', None, None, None, '4 d'),
    }
    recs = [BYID.get(k) or extra[k] for k in keep]
    rows = []
    for isl in ('apps-agora.local', 'apps-observatory.local', 'tools-ki'):
        mine = [r for r in recs if r[2] == isl]
        rows.append(group_row(isl, isl, len(mine), 5))
        rows += [record_row(r, show_island=False) for r in mine]
    menu = '''<div class="fmenu" data-chip="menu"><div class="fcol"><div class="fh">Field</div>
<div class="fo on">Priority<span class="n">1</span></div><div class="fo">Horizon</div><div class="fo">Area</div><div class="fo">Size</div><div class="fo">Island</div><div class="fo">Kind</div><div class="fo">Assignee</div></div>
<div class="fcol vals"><div class="fh">Priority, in triage</div>
<div class="fo"><span class="box"></span>critical<span class="n">0</span></div><div class="fo on"><span class="box">✓</span>high<span class="n">4</span></div>
<div class="fo"><span class="box"></span>medium<span class="n">16</span></div><div class="fo"><span class="box"></span>low<span class="n">2</span></div><div class="fo"><span class="box"></span>none<span class="n">1</span></div>
<div class="fhint">Counts follow the other filters. The context sets the territory.</div></div></div>'''
    counts = {'in-progress': 1, 'awaiting-review': 0, 'ready': 1, 'draft': 0, 'triage': 4}
    bar = roadmap_bar(on='triage', chips=[chosen_chip('Priority', 'high')], group='Island', menu=menu, counts=counts, n_filters=1)
    return (head('P1', 'Roadmap', '4 shown of 38 open records in Knowledge Islands · Triage, priority high')
            + bar + record_table(''.join(rows), show_island=False))


def roadmap_empty():
    """7.1e: nothing matches."""
    counts = {s: 0 for s in STATUS_ORDER}
    bar = roadmap_bar(chips=[chosen_chip('Priority', 'critical')], find='keychain', counts=counts, n_filters=1)
    empty = (f'<section class="panel emptypanel" {R("P3", "No records")}><div class="emptybody">'
             f'<b>No open record in Knowledge Islands matches</b>'
             f'<p class="muted">Priority critical and the words “keychain” keep nothing among the 38 open records.</p>'
             f'<p>1 done record matches: <span class="id">KI-AGORA-LVL-000</span> Keychain access for the door. '
             f'<span class="lnkbtn">Show done and cancelled</span></p>'
             f'<p><span class="btn">Clear the filters</span> <span class="btn">Look in All territories</span></p></div></section>')
    return head('P1', 'Roadmap', '0 shown of 38 open records in Knowledge Islands') + bar + empty


PIVOT = [('apps-agora.local', 0, 1, 1, 0, 8), ('apps-observatory.local', 1, 0, 0, 6, 1), ('tools-ki', 0, 0, 1, 0, 9),
         ('ki-design', 0, 0, 1, 1, 1), ('ki-agentic-harness', 1, 0, 0, 1, 2), ('ki-principal', 0, 0, 0, 1, 2)]


def roadmap_pivot():
    """7.1b: the built app's shape: a summary table beside the records, each cell a filter."""
    heads = ''.join(f'<th title="{STATUS_WORDS[s]}">{smark(s)}</th>' for s in STATUS_ORDER)
    body = []
    for isl, *cells in PIVOT:
        tds = ''.join(f'<td class="c{" on" if isl == "tools-ki" and i == 4 else ""}{" z" if not v else ""}">{v or "·"}</td>' for i, v in enumerate(cells))
        body.append(f'<tr{" class=hl" if isl == "tools-ki" else ""}><td class="rn">{isl}</td>{tds}<td class="c tot">{sum(cells)}</td></tr>')
    tot = ''.join(f'<td class="c">{STATUS_COUNT[s]}</td>' for s in STATUS_ORDER)
    body.append(f'<tr class="tots"><td class="rn">All</td>{tot}<td class="c tot">38</td></tr>')
    side = (f'<section class="panel pivot" {R("P2", "Summary: each cell a filter")}><header><h2>Summary</h2>'
            f'<span class="btn small">Rows: Island{aglyph("chev")}</span></header>'
            f'<table class="pv"><thead><tr><th></th>{heads}<th>All</th></tr></thead><tbody>{"".join(body)}</tbody></table>'
            f'<div class="pvkey">{"".join(f"<span>{smark(s)}{STATUS_WORDS[s]}</span>" for s in STATUS_ORDER)}</div>'
            f'<p class="foot pvfoot">A cell keeps its island and status; a row name its island; a column head its status.</p></section>')
    recs = [r for r in RECORDS if r[2] == 'tools-ki' and r[4] == 'triage'] + [
        ('KI-TOOL-KI-CLI-185', 'Machine contract for agent runs', 'tools-ki', 'CLI', 'triage', 'high', 's', None, None, None, '2 d'),
        ('KI-TOOL-KI-CLI-177', 'Packaged subcommands', 'tools-ki', 'CLI', 'triage', 'low', 'l', None, None, None, '1 d'),
        ('KI-TOOL-KI-CLI-172', 'Group VS Code workspaces', 'tools-ki', 'CLI', 'triage', 'medium', 'm', None, None, None, '10 d'),
        ('KI-TOOL-KI-CLI-179', 'Age from last touch in mcp-m365', 'tools-ki', 'CLI', 'triage', 'medium', 'm', None, None, 'work/ki.sop.main', '7 h')]
    rows = ''.join(record_row(r, show_island=False) for r in recs) + more_row(3, 'in tools-ki', 5)
    chips = (f'<div class="sf-row" {R("P3", "Chips and words")}><span class="sfchips">{ctx_chip("Territory", "Knowledge Islands")}{chosen_chip("Island", "tools-ki")}'
             f'{chosen_chip("Status", "triage")}<span class="btn">{aglyph("chev")}Priority</span><span class="btn">{aglyph("chev")}Horizon</span>'
             f'<span class="btn">{aglyph("chev")}Area</span><span class="btn">{aglyph("chev")}Size</span></span>{find_box()}'
             f'<span class="sp"></span><label class="chk"><span class="box"></span>Done and cancelled</label></div>')
    right = f'<div class="pvright">{chips}{record_table(rows, code="P4", show_island=False)}</div>'
    return (head('P1', 'Roadmap', '9 shown of 38 open records in Knowledge Islands · tools-ki, triage')
            + f'<div class="pvsplit">{side}{right}</div>')


# ================================================================ 7.2 Jobs
# Territory, then repository; each job: (id, name, kind, schedule, macs [(rig, outcome)], last, next, standing)
JOBS = [
    ('Knowledge Islands', [
        ('apps-agora.local', [('agora', 'Agora', 'service', 'Kept running', [('sol', 'service'), ('terra', 'service')], '—', '—', 'service')]),
        ('apps-observatory.local', [('observatory', 'Observatory', 'service', 'Kept running', [('sol', 'service')], '—', '—', 'service')]),
        ('ki-principal', [
            ('ki-sop-digest', 'State of play digest', 'job', 'Daily at 06:40', [('sol', 'ok')], '22 h ago on sol', '06:40', 'ok'),
            ('ki-territory-audit', 'Territory audit', 'job', 'Daily at 02:10', [('terra', 'findings')], '2 h ago on terra', 'Sat 02:10', 'findings'),
            ('ki-weekly-recap', 'Weekly recap', 'job', 'Mondays at 09:00', [('sol', 'never')], 'none recorded', 'Mon 09:00', 'never')]),
        ('tools-ki', [('ki-roadmap-index', 'Roadmap index', 'job', 'Every 1 h', [('sol', 'ok')], '20 min ago on sol', '05:00', 'ok')]),
    ]),
    ('Humans Not Robots', [
        ('hnr-principal', [
            ('hnr-email-route-drift', 'Email route drift', 'job', 'Weekdays at 07:15', [('sol', 'failed')], '21 h ago on sol', '07:15', 'failed'),
            ('hnr-sop-digest', 'State of play digest', 'job', 'Daily at 06:45', [('sol', 'ok')], '22 h ago on sol', '06:45', 'ok')]),
    ]),
    ('Personal', [
        ('inbox', [
            ('kiv', 'KIV', 'service', 'Kept running', [('sol', 'service')], '—', '—', 'service'),
            ('kiv-capture-sweep', 'Capture sweep', 'job', 'Every 30 min', [('sol', 'ok'), ('terra', 'ok')], '8 min ago on terra', '04:30', 'ok')]),
        ('dotfiles', [
            ('good-morning', 'Good morning', 'job', 'Weekdays at 08:00', [('sol', 'ok'), ('terra', 'never')], '20 h ago on sol', '08:00', 'ok'),
            ('brew-update', 'Homebrew update', 'job', 'Sundays at 03:00', [('sol', 'ok'), ('terra', 'ok')], '5 d ago on terra', 'Sun 03:00', 'ok'),
            ('dock-autohide', 'Dock autohide', 'job', 'Weekdays at 09:00', [], 'declared for laptop', '—', 'disabled')]),
    ]),
]
JOB_COUNTS = dict(all=13, failed=1, findings=1, ok=6, never=1, disabled=1, service=3)


def mac_chip(rig, outcome):
    words = {'ok': 'ok', 'findings': 'findings', 'failed': 'failed', 'never': 'no run yet', 'service': 'running', 'unreadable': 'unreadable'}[outcome]
    return f'<span class="mac m-{outcome}" title="{rig}: last run {words}">{smark(outcome)}{rig}</span>'


def job_row(j, selected=None):
    jid, name, kind, sched, macs, last, nxt, standing = j
    cls = 'job' + (' sel' if jid == selected else '')
    pills = '<span class="tag">service</span>' if kind == 'service' else ('<span class="tag">off</span>' if standing == 'disabled' else '')
    mac_html = ''.join(mac_chip(*m) for m in macs) or f'<span class="muted">{"declared for laptop" if standing == "disabled" else "—"}</span>'
    last_html = last if standing != 'disabled' else '—'
    return (f'<tr class="{cls}" data-job="{jid}"><td class="jn"><b>{escape(name)}</b>{pills}<span class="sub mono">{jid}</span></td>'
            f'<td class="muted nowrap">{sched}</td><td class="nowrap macs">{mac_html}</td><td class="muted nowrap">{last_html}</td>'
            f'<td class="mono nowrap">{nxt}</td><td class="nowrap">{standing_pill(standing)}</td></tr>')


def job_rows(selected=None, fold=(), only=None):
    out = []
    for terr, repos in JOBS:
        jobs = [j for _, js in repos for j in js if not only or j[7] in only]
        if not jobs:
            continue
        n_job = sum(1 for j in jobs if j[2] == 'job')
        n_svc = len(jobs) - n_job
        worst = next((s for s in ('failed', 'findings') if any(j[7] == s for j in jobs)), None)
        sub = f'{n_job} job{"s" if n_job != 1 else ""}' + (f', {n_svc} service{"s" if n_svc != 1 else ""}' if n_svc else '')
        if worst:
            sub += ' · 1 failed' if worst == 'failed' else ' · 1 with findings'
        shut = terr in fold
        out.append(f'<tr class="group grp terr{" shut" if shut else ""}" data-grp="{escape(terr)}"><td colspan="6">{aglyph("chevr" if shut else "chev", "gchev")}<b>{escape(terr)}</b>'
                   f'<span class="muted gsub">{sub}</span></td></tr>')
        if shut:
            continue
        for repo, js in repos:
            js = [j for j in js if not only or j[7] in only]
            if not js:
                continue
            own = ' <span class="muted">· Rig’s own, declared here</span>' if repo == 'dotfiles' else ''
            out.append(f'<tr class="repo" data-repo="{repo}"><td colspan="6"><span class="mono">{repo}</span>{own}</td></tr>')
            out += [job_row(j, selected) for j in js]
    return ''.join(out)


def jobs_bar(on=None, plane='Both', group='Repository', counts=None):
    c = counts or JOB_COUNTS
    t = [tally('all', c['all'], 'All', on=on is None, glyph='all')]
    for k in ('failed', 'findings', 'ok', 'never', 'disabled', 'service'):
        words = {'failed': 'Failed', 'findings': 'Findings', 'ok': 'OK', 'never': 'No run yet', 'disabled': 'Off', 'service': 'Services'}[k]
        t.append(tally(k, c[k], words, on=bool(on and k in on), attn=(k in ('failed', 'findings') and c[k] > 0)))
    chips = [ctx_chip('', f'All territories · {"both planes" if plane == "Both" else plane}'), filter_button()]
    return sf_bar(t, chips, find_box(hint='Words in a job or repository'), group_seg(['Repository', 'Mac', 'None'], group))


def jobs_table(rows, code='P3'):
    return (f'<section class="panel tablepanel" {R(code, "Jobs by territory and repository")}><table class="records jobs">'
            f'<thead><tr><th>Job</th><th>Schedule</th><th>Macs</th><th>Last run</th><th>Next</th><th>How it stands</th></tr></thead>'
            f'<tbody>{rows}</tbody></table></section>')


def jobs_page(selected='hnr-email-route-drift', fold=('Knowledge Islands', 'Personal')):
    return (head('P1', 'Jobs', '10 jobs and 3 services; 1 last ended badly · running them stays with Rig')
            + jobs_bar() + jobs_table(job_rows(selected, fold)))


def job_tray(jid='hnr-email-route-drift', runs_open=True):
    if jid == 'observatory':
        kv = [('Id', '<span class="mono">service.observatory</span>'), ('Schedule', 'Kept running'), ('Declared', 'running'),
              ('Profiles', 'core'), ('Provider', 'launchd'), ('Label', '<span class="mono">uk.me.kris.rig.observatory</span>'),
              ('Works in', '<span class="mono">~/kis/knowledge-islands/apps-observatory.local</span>'), ('Program', '<span class="mono">bun</span>')]
        macs = ('<h3>sol</h3><p class="muted">A service reports no runs. Its service answers on 127.0.0.1:1675.</p>'
                '<h3>terra · not selected there</h3><p class="muted">Declared for core; terra’s profile leaves it out.</p>')
        lead = f'<div class="tlead">{standing_pill("service")}</div><p>The Observatory’s local service: the instruments Atlas embeds.</p>'
        acts = [('', 'Open its file'), ('', 'Open Repositories')]
        return tray_frame('Service · apps-observatory.local', 'Observatory', lead + f'<table class="kv"><tbody>{"".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k, v in kv)}</tbody></table>' + macs, actions=acts)
    kv = [('Id', '<span class="mono">scheduled-job.hnr-email-route-drift</span>'), ('Schedule', 'Weekdays at 07:15'),
          ('Next', 'Today 07:15, by its schedule'), ('Declared', 'enabled'), ('Profiles', 'core'), ('Provider', 'launchd'),
          ('Label', '<span class="mono">uk.me.kris.rig.hnr-email-route-drift</span>'),
          ('Works in', '<span class="mono">~/kis/humans-not-robots/hnr-principal</span>'), ('Program', '<span class="mono">~/bin/ki</span>')]
    ticks = ''.join(f'<i class="t-{o}" title="{o}">{smark(o)}</i>' for o in ['ok', 'ok', 'findings', 'ok', 'ok', 'ok', 'ok', 'findings', 'ok', 'failed'])
    lead = (f'<div class="tlead">{standing_pill("failed")}<span class="muted">21 h ago on sol</span></div>'
            f'<p>Reports mail that drifted from its routing rules in the HNR mailbox.</p>')
    macs = (f'<h3>sol · last 10 runs, oldest first</h3><div class="runticks">{ticks}</div>'
            f'<p class="lastline"><span class="bad">Failed</span> Thu 5 Nov 07:15 · Microsoft 365 sign-in has expired; run m365 auth</p>'
            f'<h3>terra · not selected there</h3><p class="muted">Declared for core; no run recorded on terra.</p>')
    acts = [('on' if runs_open else '', 'Show runs'), ('', 'Open its file'), ('', 'Show on Home')]
    body = lead + f'<table class="kv"><tbody>{"".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k, v in kv)}</tbody></table>' + macs
    t = tray_frame('Scheduled job · hnr-principal', 'Email route drift', body, actions=[a for a in acts])
    return t.replace('<span class="btn">Show runs</span>', '<span class="btn pressed">Show runs</span>')


RUNS = [('Thu 5 Nov 07:15', 'sol', 'failed', 'Microsoft 365 sign-in has expired; run m365 auth'),
        ('Wed 4 Nov 07:15', 'sol', 'ok', 'No drift: 212 messages checked'),
        ('Tue 3 Nov 07:15', 'sol', 'findings', '3 messages outside their routing rules'),
        ('Mon 2 Nov 07:15', 'sol', 'ok', 'No drift: 187 messages checked'),
        ('Fri 30 Oct 07:15', 'sol', 'ok', 'No drift: 240 messages checked'),
        ]


def job_bottom():
    words = {'ok': 'OK', 'failed': 'Failed', 'findings': 'Findings'}
    rows = ''.join(f'<tr class="r-{o}"><td class="nowrap">{w}</td><td class="mono">{m}</td><td class="nowrap">{standing_pill(o) if o != "ok" else standing_pill("ok")}</td><td>{escape(s)}</td></tr>'
                   for w, m, o, s in RUNS)
    body = (f'<table class="runs"><thead><tr><th>Finished</th><th>Mac</th><th>Outcome</th><th>Summary</th></tr></thead><tbody>{rows}</tbody></table>'
            f'<p class="foot">The reporter keeps 14 days. Agora keeps each run’s outcome and its one line; the output stays with the reporter.</p>')
    return bottom_frame('Runs · hnr-principal', 'Email route drift', [('Runs on both Macs · 5', True), ('Declaration', False)], body, height=330)


def jobs_by_mac():
    """7.2b: each Mac a column, as Checkouts sets the two Macs side by side."""
    def cell(macs, rig, standing, last):
        m = dict(macs)
        if rig not in m:
            return '<td class="muted">not selected</td>'
        o = m[rig]
        if o == 'service':
            return f'<td class="nowrap">{smark("service")}running</td>'
        if o == 'never':
            return f'<td class="muted nowrap">{smark("never")}no run yet</td>'
        when = last.replace(f' on {rig}', '') if rig in last else ('20 h ago' if rig == 'sol' else '6 min ago')
        return f'<td class="nowrap o-{o}">{smark(o)}{STANDING_WORDS[o]}<span class="muted"> · {when}</span></td>'
    out = []
    for terr, repos in JOBS:
        shut = terr == 'Personal'
        out.append(f'<tr class="group grp"><td colspan="5">{aglyph("chevr" if shut else "chev", "gchev")}<b>{escape(terr)}</b>'
                   f'{"<span class=\"muted gsub\">4 jobs, 1 service</span>" if shut else ""}</td></tr>')
        if shut:
            continue
        for repo, js in repos:
            out.append(f'<tr class="repo"><td colspan="5"><span class="mono">{repo}</span></td></tr>')
            for jid, name, kind, sched, macs, last, nxt, standing in js:
                sel = ' class="sel"' if jid == 'hnr-email-route-drift' else ''
                out.append(f'<tr{sel}><td class="jn"><b>{escape(name)}</b><span class="sub mono">{jid}</span></td><td class="muted nowrap">{sched}</td>'
                           f'{cell(macs, "sol", standing, last)}{cell(macs, "terra", standing, last)}<td class="mono">{nxt}</td></tr>')
    table = (f'<section class="panel tablepanel" {R("P3", "Jobs, each Mac a column")}><table class="records jobs bymac">'
             f'<thead><tr><th>Job</th><th>Schedule</th><th>sol · this Mac</th><th>terra</th><th>Next</th></tr></thead><tbody>{"".join(out)}</tbody></table></section>')
    return (head('P1', 'Jobs', '10 jobs and 3 services; 1 last ended badly · running them stays with Rig') + jobs_bar() + table)


def jobs_filtered():
    """7.2c: Failed and Findings chosen (⌘-click), only those kept."""
    c = dict(JOB_COUNTS)
    return (head('P1', 'Jobs', '2 shown of 13 · Failed or Findings · running them stays with Rig')
            + jobs_bar(on=('failed', 'findings'), counts=c) + jobs_table(job_rows(only=('failed', 'findings'))))


# ================================================================ 8.1 Guilds
GUILDS_KI = [
    ('keystone', 'Keystone', 'Ke', 32, 'The foundation: starting Knowledge Islands, the repository contract, and how a skill is written.',
     ['ki-bootstrap', 'ki-repo', 'ki-skills']),
    ('governance', 'Governance', 'Go', 212, 'The standing rules: writing, Git, delegation, decisions, specifications and trades.',
     ['ki-agentic-radar', 'ki-authoring', 'ki-decision-records', 'ki-delegation', 'ki-diagrams', 'ki-engineering', 'ki-git', 'ki-guides',
      'ki-model-radar', 'ki-specs', 'ki-trade', 'ki-trades', 'ki-work-package']),
    ('change-management', 'Change management', 'CM', 152, 'How work moves: captured, planned, done, accepted, coordinated and recapped.',
     ['ki-accept', 'ki-batch', 'ki-coordination', 'ki-implement', 'ki-next', 'ki-plan', 'ki-recap', 'ki-work', 'ki-work-design',
      'ki-work-github-issues', 'ki-work-linear', 'ki-work-recurring', 'ki-work-roadmap']),
    ('repo-structure', 'Repository structure', 'RS', 95, 'The shape of each kind of repository: knowledge bases, tools, websites, harnesses and more.',
     ['ki-repo-dotfiles-chezmoi', 'ki-repo-harness', 'ki-repo-homebrew-tap', 'ki-repo-kb', 'ki-repo-kb-activities', 'ki-repo-kb-live-artifacts',
      'ki-repo-kb-principal', 'ki-repo-kb-streams', 'ki-repo-mcp', 'ki-repo-project', 'ki-repo-specifications', 'ki-repo-tools',
      'ki-repo-website', 'ki-repo-website-app', 'ki-repo-website-cloudflare', 'ki-repo-website-content']),
    ('agentic-systems', 'Agentic systems', 'AS', 270, 'Agents working with agents: subagents, and delegation through Paperclip.',
     ['ki-agent-coordination-paperclip', 'ki-delegation-paperclip', 'ki-subagents', 'ki-subagents-chatgpt', 'ki-subagents-claude']),
    ('environment', 'Environment', 'En', 175, 'The workstation’s AI tools: their MCP bindings, housekeeping and context budgets.',
     ['ki-binding', 'ki-binding-chatgpt', 'ki-binding-chezmoi', 'ki-binding-claude', 'ki-housekeeping-chatgpt', 'ki-housekeeping-claude',
      'ki-tokenomics', 'ki-tokenomics-chatgpt', 'ki-tokenomics-claude']),
    ('acquire', 'Acquire', 'Ac', 130, 'Bringing knowledge in: conversations, meetings and links, captured and curated.',
     ['ki-acquire', 'ki-acquire-chatgpt', 'ki-acquire-granola', 'ki-pulse']),
    ('design', 'Design', 'De', 330, 'How things look: inspiration and the design system.', ['ki-design-inspiration', 'ki-design-system']),
]
GUILDS_HNR = [
    ('hnr-own', 'Humans Not Robots’ own', 'HN', 18, 'The skills hnr-agentic-harness keeps unsorted, standing as one guild of the territory’s own.',
     ['hnr-carbon-baseline', 'hnr-client-brief', 'hnr-email-routing', 'hnr-proposal', 'hnr-sop', 'hnr-workshop-plan']),
]


def shield(mono, hue, size=40, all_=False):
    path = 'M20 3 L35 9 V21 C35 30.5 28.6 37.2 20 41 C11.4 37.2 5 30.5 5 21 V9 Z'
    if all_:
        return (f'<svg class="shield all" viewBox="0 0 40 44" width="{size}" height="{size * 1.1:.0f}"><path d="{path}" fill="none" '
                f'stroke="currentColor" stroke-width="1.5" stroke-dasharray="3 2.4"/><text x="20" y="26" text-anchor="middle">{mono}</text></svg>')
    text = f'<text x="20" y="26" text-anchor="middle">{mono}</text>' if size >= 30 else ''
    return (f'<svg class="shield" viewBox="0 0 40 44" width="{size}" height="{size * 1.1:.0f}" style="--h:{hue}"><path d="{path}"/>'
            f'{text}</svg>')


def guild_badge(g, on=False):
    gid, title, mono, hue, about, skills = g
    return (f'<span class="gbadge{" on" if on else ""}" data-guild="{gid}" title="{escape(about)}">{shield(mono, hue)}'
            f'<span class="nm">{escape(title)}</span><span class="ct">{len(skills)} skills</span></span>')


def all_badge(n, on=False):
    return (f'<span class="gbadge allb{" on" if on else ""}" data-guild="all">{shield(str(n), 0, all_=True)}'
            f'<span class="nm">All guilds</span><span class="ct">{n} skills</span></span>')


def skill_badge(name, hue, mono, on=False):
    return (f'<span class="sbadge{" on" if on else ""}" data-skill="{name}"><svg class="sdot" viewBox="0 0 40 44" style="--h:{hue}">'
            f'<path d="M20 3 L35 9 V21 C35 30.5 28.6 37.2 20 41 C11.4 37.2 5 30.5 5 21 V9 Z"/></svg>{name}</span>')


def guild_strip(guilds, chosen=None, code='P2'):
    n = sum(len(g[5]) for g in guilds)
    badges = all_badge(n, on=chosen is None) + ''.join(guild_badge(g, on=(g[0] == chosen)) for g in guilds)
    return f'<section class="gstrip" {R(code, "Guild badges")}>{badges}</section>'


def guilds_head(territory='Knowledge Islands', guilds=GUILDS_KI, harness='ki-agentic-harness', words=''):
    n = sum(len(g[5]) for g in guilds)
    tools = f'<span class="find">{aglyph("search")}{f"<b>{words}</b>" if words else "Words in a skill, its description or guild"}</span>'
    return head('P1', 'Guilds', f'{len(guilds)} guild{"s" if len(guilds) != 1 else ""} · {n} skills in {territory} · from {harness} · read {NOW}', tools)


def guild_bank_one(g, open_skill=None, code='P3'):
    gid, title, mono, hue, about, skills = g
    badges = ''.join(skill_badge(s, hue, mono, on=(s == open_skill)) for s in skills)
    return (f'<section class="gbank" {R(code, "The guild’s skills")}><div class="gbhead"><b>{escape(title)}</b><span class="muted">'
            f'{len(skills)} skills · {escape(about)}</span></div><div class="sbank">{badges}</div></section>')


def guild_ledger(guilds, code='P3'):
    rows = []
    for gid, title, mono, hue, about, skills in guilds:
        badges = ''.join(skill_badge(s, hue, mono) for s in skills)
        rows.append(f'<tr data-ledger="{gid}"><td class="lg"><span class="lgn">{shield(mono, hue, 22)}<b>{escape(title)}</b><span class="gn">{len(skills)}</span></span>'
                    f'</td><td><div class="sbank">{badges}</div></td></tr>')
    return f'<section class="panel ledger" {R(code, "Every guild’s skills")}><table><tbody>{"".join(rows)}</tbody></table></section>'


PROVISIONAL = ('<p class="foot prov">Provisional guilds: each is a folder ki-agentic-harness sorts its skills into, until the guildmaster’s '
               'catalogue (ki.reg.guilds) names them. A guild with no logo yet shows its monogram on its own colour.</p>')


def guilds_page(open_skill='ki-delegation'):
    """8.1a: the guild badges across, the chosen guild's skills beneath, a skill open in the bottom pane."""
    g = GUILDS_KI[1]
    return guilds_head() + guild_strip(GUILDS_KI, chosen='governance') + guild_bank_one(g, open_skill)


def guilds_rest():
    """8.1c: no skill chosen: All guilds, every guild a row of the ledger."""
    return guilds_head() + guild_strip(GUILDS_KI) + guild_ledger(GUILDS_KI) + PROVISIONAL


def guilds_hnr():
    """8.1d: another territory from the context."""
    note = ('<p class="foot prov">hnr-agentic-harness keeps its skills directly under <span class="mono">skills/</span>, so they stand as one guild '
            'of the territory’s own until the catalogue sorts them. Knowledge Islands’ 8 guilds are under All territories or Knowledge Islands.</p>')
    return (guilds_head('Humans Not Robots', GUILDS_HNR, 'hnr-agentic-harness') + guild_strip(GUILDS_HNR, chosen='hnr-own')
            + guild_bank_one(GUILDS_HNR[0], 'hnr-client-brief') + note)


def skill_pane(tab='SKILL.md'):
    tabs = [('SKILL.md', tab == 'SKILL.md'), ('references/ 4', tab == 'references/'), ('scripts/ 3', False), ('assets/ 7', False)]
    if tab == 'SKILL.md':
        fm = [('ki-kind', 'governance'), ('ki-applicability', 'declaration-only'), ('ki-depends-on', '—'),
              ('ki-shared-dependencies', '<span class="mono">ki-skills:rubric</span>'),
              ('argument-hint', '<span class="mono">audit &lt;repo&gt; | conform &lt;repo&gt; | educate &lt;work-item&gt; | help | refresh</span>')]
        kv = ''.join(f'<tr><td>{k}</td><td>{v}</td></tr>' for k, v in fm)
        body = (f'<div class="skdoc"><div class="skfm"><div class="fh">Front matter</div><table class="kv"><tbody>{kv}</tbody></table>'
                f'<div class="fh">Where it lives</div><p class="mono small">ki-agentic-harness/skills/governance/ki-delegation</p></div>'
                f'<div class="skbody"><p class="lede">Govern agent delegation: routine detached background runs (run packet, prompt shape, authority footers, '
                f'decisions log, coordination, run queue, monitoring) and durable packets for approved high-risk handoffs.</p>'
                f'<h4>When to use it</h4><p>When delegating to background agents or writing a delegation brief. <span class="mono">ki agent</span> launches runs, '
                f'and <span class="lnk2">ki-coordination</span> governs the coordinating work that launches them.</p>'
                f'<h4>The run packet</h4><p>Every detached run carries its packet: what to do, the authority it holds, where it reports, and the footer it ends with. '
                f'See <span class="lnk2">references/standards-background-runs.md</span>.</p></div></div>')
    else:
        files = ['rubric.md', 'sources.md', 'standards-background-runs.md', 'standards-delegation-packets.md']
        lis = ''.join(f'<li{" class=on" if f == "standards-background-runs.md" else ""}>{f}</li>' for f in files)
        body = (f'<div class="at-doc"><ul class="plain">{lis}</ul><div><div class="muted mono" style="margin-bottom:6px">references/standards-background-runs.md · 9 KB</div>'
                f'<h4>Standards: background runs</h4><p>A background run is detached: no one watches it as it works, so its packet must say everything it may do. '
                f'Each run is launched through <span class="mono">ki agent</span>, recorded in the run queue, and ends with an authority footer and a report.</p>'
                f'<p class="muted">Its rules come from <span class="lnk2">assets/rules-none.md</span> to <span class="lnk2">assets/rules-release.md</span>, one per grant.</p></div></div>')
    return bottom_frame('Governance · ki-agentic-harness', '<span class="id">ki-delegation</span>', tabs, body, height=420)


def hnr_pane():
    tabs = [('SKILL.md', True), ('references/ 2', False), ('assets/ 3', False)]
    fm = [('ki-kind', 'practice'), ('argument-hint', '<span class="mono">draft &lt;client&gt; | review &lt;brief&gt;</span>')]
    kv = ''.join(f'<tr><td>{k}</td><td>{v}</td></tr>' for k, v in fm)
    body = (f'<div class="skdoc"><div class="skfm"><div class="fh">Front matter</div><table class="kv"><tbody>{kv}</tbody></table>'
            f'<div class="fh">Where it lives</div><p class="mono small">hnr-agentic-harness/skills/hnr-client-brief</p></div>'
            f'<div class="skbody"><p class="lede">Write a client brief for a sustainability engagement: the client’s aim, their baseline, what HNR offers and what it will not.</p>'
            f'<h4>When to use it</h4><p>Before a first workshop, or when an enquiry becomes an engagement. The baseline comes from <span class="lnk2">hnr-carbon-baseline</span>.</p></div></div>')
    return bottom_frame('Humans Not Robots’ own · hnr-agentic-harness', '<span class="id">hnr-client-brief</span>', tabs, body, height=330)


def guilds_columns():
    """8.1b: the built app's shape: guild columns across, each with its badge, about and skills beneath; scrolls sideways."""
    cols = []
    for gid, title, mono, hue, about, skills in GUILDS_KI[:4]:
        sk = ''.join(f'<div>{skill_badge(s, hue, mono, on=(s == "ki-delegation"))}</div>' for s in skills[:7])
        more = f'<div class="muted small">{len(skills) - 7} more</div>' if len(skills) > 7 else ''
        cols.append(f'<div class="gcol{" on" if gid == "governance" else ""}"><div class="gch">{shield(mono, hue, 34)}<div><b>{escape(title)}</b>'
                    f'<span class="sub">{len(skills)} skills</span></div></div><p>{escape(about)}</p><div class="gsk">{sk}{more}</div></div>')
    return (guilds_head() + f'<section class="gcols" {R("P2", "Guild columns, sideways")}>{"".join(cols)}'
            f'<div class="gmore">4 more guilds<span class="muted">Agentic systems, Environment, Acquire, Design</span>→</div></section>')


# ================================================================ the artboards' whole windows
CTX_KI = dict(territory='Knowledge Islands')


def ab_roadmap(theme='night'):
    return atlas_page('roadmap', roadmap_page(), tray=record_tray(), context=CTX_KI, theme=theme)


def ab_roadmap_pivot():
    return atlas_page('roadmap', roadmap_pivot(), context=CTX_KI)


def ab_roadmap_filtered():
    return atlas_page('roadmap', roadmap_filtered(), context=CTX_KI)


def ab_roadmap_review():
    return atlas_page('roadmap', roadmap_page(selected='KI-AGORA-TRY-001'), tray=record_tray('KI-AGORA-TRY-001'), context=CTX_KI)


def ab_roadmap_empty():
    return atlas_page('roadmap', roadmap_empty(), context=CTX_KI)


def ab_jobs(theme='night'):
    return atlas_page('jobs', jobs_page(), tray=job_tray(), bottom=job_bottom(), standing=('look', '1 needs a look'), theme=theme)


def ab_jobs_bymac():
    return atlas_page('jobs', jobs_by_mac(), standing=('look', '1 needs a look'))


def ab_jobs_filtered():
    return atlas_page('jobs', jobs_filtered(), standing=('look', '1 needs a look'))


def ab_jobs_service():
    return atlas_page('jobs', jobs_page(selected='observatory', fold=('Personal', 'Humans Not Robots')), tray=job_tray('observatory'), standing=('look', '1 needs a look'))


def ab_guilds(theme='night'):
    return atlas_page('guilds', guilds_page(), bottom=skill_pane(), context=CTX_KI, theme=theme)


def ab_guilds_columns():
    return atlas_page('guilds', guilds_columns(), bottom=skill_pane(), context=CTX_KI)


def ab_guilds_rest():
    return atlas_page('guilds', guilds_rest(), context=CTX_KI)


def ab_guilds_hnr():
    return atlas_page('guilds', guilds_hnr(), bottom=hnr_pane(), context=dict(territory='Humans Not Robots'))


def ab_guilds_folder():
    return atlas_page('guilds', guilds_page(), bottom=skill_pane('references/'), context=CTX_KI)
