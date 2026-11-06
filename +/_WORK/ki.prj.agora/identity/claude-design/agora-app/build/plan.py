"""The Agora app design pack: every page, artboard and component, with the note, fields and trade-offs for each.

python3 plan.py writes the mock-up HTML into ../mocks and plan.json beside this file; shoot.js then takes the
screenshots and measures the regions; board.py builds the pages, the index and board.json.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tray'))
import mocks as M  # noqa: E402
import build as TRAY  # noqa: E402  (the tray mock-up's builder, ../../tray/build.py)

HERE = os.path.dirname(os.path.abspath(__file__))
MOCKS = os.path.join(HERE, '..', 'mocks')

PAGES = [
    dict(id='0.1', title='Shell: the window and its rail', zones=['navigation'],
         note='The frame every view sits in: the brand, the views, what is coming from the KIV and the Observatory, '
              'the four ways to speak to everyone, and the portal\'s state at the foot. It matters because it is what '
              'Kris sees first and last: the portal line answers "are both Macs here?" on every page.',
         fields=['Brand: the meeting ring, "Agora", which Mac this is',
                 'Views: Home, Who\'s doing what, What\'s being said, Broadcasts, Waits on you, Macs and the portal, Checkouts, each with a count where one helps',
                 'Later: Inbox (from the KIV), Insight (from the Observatory), shown but not yet live',
                 'Speak to everyone: Broadcast…, Away… (I\'m back while away), Ping, Mark all',
                 'The portal: the two Macs and whether the portal is open, with when the other was last heard',
                 'Tabs: Home first, then each page or document opened, closable']),
    dict(id='0.2', title='Shell: the tray', zones=['tray'],
         note='The menu-bar menu, the quiet everyday face of Agora (DESIGN-2). The app opens from its first line. '
              'It matters because most days Kris only ever sees this: two lines must say whether all is well.',
         fields=['Line 1: agents and Macs heard from', 'Line 2: All well, or how many need a look',
                 'Exception rows: at most 3, each with what Agora saw, what it did, at most two actions',
                 'Speak to everyone', 'Detail one level down: Agents, Macs and checkouts, Runs, Broadcasts, News',
                 'Agora itself: Sync now, Open log, About, Quit']),
    dict(id='1', title='Home', zones=['page'],
         note='One view that fits the window with no scrolling (MSG-62774774, Kris\'s vision): the territories and their '
              'islands, the work packages and workers placed where they work, the primary focus of each, the meeting '
              'point on each island, the threads of talk up to each territory\'s council and across, and the great portal '
              'between the Macs. It matters because it is the page the app opens on, and it should show the whole '
              'distributed Agora as one place.',
         fields=['Territories, each a faint boundary with its name', 'Islands (repositories), drawn as hexes',
                 'Meeting point on each island: on (lit) or off', 'Workers by role: council, enabler, doer; each with its primary focus and rig', 'Planes: sol, terra or both, since each rig is a plane over the same islands',
                 'Listening by shape: solid listening, hollow on open, slashed silent',
                 'Threads of talk: work packages up to their council, councils across', 'The great portal: sol and terra, open or not',
                 'At a glance: agents by host, what needs a look, what waits on Kris, the portal; the key; Show as a list']),
    dict(id='2.1', title="Who's doing what", zones=['page'],
         note='Every live agent on both Macs, what each looks after, whether it listens, and what waits on Kris; and '
              'the address book for routing by focus. It matters because routing an idea to the right agent depends '
              'on it, and because listening is shown from answers, not from what an agent says of itself.',
         fields=['Agent: work id and title', 'Mac (as the group row)', 'Territory', 'Focus areas, primary first (★)',
                 'Listening: how (Agora\'s call, polling, on open, off) and last answer', 'Waits on you: count and first ids']),
    dict(id='2.2', title='An agent', zones=['page'],
         note='One agent closer up: its focus areas with what each covers, its listening over the last two hours, '
              'the run and doers with it now, what was said with it, and its queries. It matters when an agent '
              'goes silent or holds many queries: everything needed to act is on one page.',
         fields=['Focus areas with descriptions', 'Listening: method, recent answers, next check',
                 'With it now: run, doers, checkouts', 'Said with it: last hour, both directions',
                 'Waits on you: query, what, focus, since, recommended answer']),
    dict(id='3.1', title="What's being said", zones=['page'],
         note='Everything said between agents and to Kris on both Macs, newest first, in both layers. It matters '
              'because "everyone hears" is Agora\'s first goal: this is where Kris sees what was said and whether '
              'it was heard. It is a record to look along, not a chat.',
         fields=['Time', 'From → to', 'Kind: message, call, broadcast, ping, mark, health, pushed',
                 'Layer: Git (durable) or Agora (conversational)', 'What was said, in a line', 'Heard: when, or silent']),
    dict(id='3.2', title='Broadcasts', zones=['page'],
         note='What Kris said to everyone, and who heard it. It matters because a broadcast such as Away opens an '
              'unattended window: Kris needs to know every agent took it.',
         fields=['Sent', 'What', 'Kind: message, away, back, ping, mark', 'Heard: answered of reached',
                 'Silent: who did not answer', 'For the selected one: each agent, answered or silent']),
    dict(id='4.1', title='Waits on you', zones=['page'],
         note='Every query waiting on Kris across all agents, gathered in one place. It matters because these are '
              'the decisions only Kris can make, and today they sit in ten separate discussions files.',
         fields=['Query id', 'What, in a line', 'Focus', 'Since', 'Recommended answer', 'Agent']),
    dict(id='5.1', title='Macs and the portal', zones=['page'],
         note='The two Macs and the portal between them: presence, where each listens, its Agora, agents and '
              'checkouts, and what crossed the portal this hour. It matters when something is not getting across.',
         fields=['Per Mac: presence, address, Agora version and uptime, agents, checkouts, last review',
                 'The portal: network, last heard and round trip, traffic this hour, queued, state swapped']),
    dict(id='5.2', title='Checkouts', zones=['page'],
         note='Every kept checkout on both Macs, side by side, showing only those not level by default. It matters '
              'because "everyone is level" is Agora\'s second goal, and a diverged checkout blocks an agent.',
         fields=['Repository', 'Condition on sol', 'Condition on terra', 'Whether the Macs agree',
                 'For the selected one: what Agora did and who was called']),
    dict(id='6', title='A document in a tab', zones=['page'],
         note='Pages and documents open inside the app as tabs, as in Orca and Claude Code, so a message, a decision or a record '
              'can be read beside the map without bringing in the KIV\'s and the Observatory\'s views first.',
         fields=['Tabs: Home stays first; each opened page or document after it, closable', 'The document, read only, with where it lives and when it changed',
                 'About this document: its package, how Agora uses it, where it was opened from']),
]

# Each artboard: page, letter, title, the mock-up to draw, its zones, and for alternatives the trade-off.
ARTBOARDS = [
    dict(id='0.1a', page='0.1', title='Rail expanded, both Macs here', make=lambda: M.page('Home', M.shell_blank('10 agents on 2 Macs · All well'), mark_shell=True), zones=['navigation']),
    dict(id='0.1b', page='0.1', title='Rail contracted', make=lambda: M.page('Home', M.shell_blank('10 agents on 2 Macs · All well'), contracted=True, mark_shell=True), zones=['navigation']),
    dict(id='0.1c', page='0.1', title='Rail expanded, terra not heard from', make=lambda: M.page('Home', M.shell_blank('4 agents on 1 Mac · 1 needs a look'), mark_shell=True, portal='unheard'), zones=['navigation']),
    dict(id='0.2a', page='0.2', title='Tray, all well', tray='all-well', zones=['tray']),
    dict(id='0.2b', page='0.2', title='Tray, one problem', tray='one-problem', zones=['tray']),
    dict(id='0.2c', page='0.2', title='Tray, a Mac missing', tray='mac-missing', zones=['tray']),
    dict(id='1a', page='1', title='The map of territories', make=lambda: M.page('Home', M.home_map()), zones=['page'], preferred=True,
         why='It is the picture Kris described: islands and territories, workers placed where they work, meeting points joined by '
             'threads, the great portal; it fits one window, and the key and Show as a list give its text equivalent.',
         gains='The whole distributed Agora in one look; the hierarchy of talk is visible; hosts read as crews on the same islands.',
         costs='Placing islands needs a layout rule (the Territory Map\'s, ideally); labels crowd on a busy island; silent workers are small.'),
    dict(id='1d', page='1', title="1a on sol's plane", make=lambda: M.page('Home', M.home_map('sol')), zones=['page']),
    dict(id='1e', page='1', title="1a on terra's plane", make=lambda: M.page('Home', M.home_map('terra')), zones=['page']),
    dict(id='1b', page='1', title='The councils', make=lambda: M.page('Home', M.home_council()), zones=['page'],
         gains='The hierarchy of talk is exact and legible: each council with who talks up to it; scales to many work packages.',
         costs='No islands or geography, so it is a diagram, not the place; the great portal becomes a band.'),
    dict(id='1c', page='1', title='The two squares', make=lambda: M.page('Home', M.home_a()), zones=['page'],
         gains='Host-centred: each Mac\'s Agora and the portal between them, with what needs a look and what was just said.',
         costs='Hides territories and islands, which Kris\'s vision puts first; treats hosts as places, not crews.'),
    dict(id='2.1a', page='2.1', title='By Mac', make=lambda: M.page("Who's doing what", M.here_a()), zones=['page'], preferred=True,
         why='Rows stay where Kris learnt them (by Mac, territory, work id), listening and queries read across '
             'each row, and the address book is one search away in the same view.',
         gains='Stable order; every fact about an agent on one row; the selected agent\'s detail below without leaving the page.',
         costs='Finding who covers a focus needs the search box; an agent with many focus areas wraps.'),
    dict(id='2.1b', page='2.1', title='By focus: the address book', make=lambda: M.page("Who's doing what", M.here_b()), zones=['page'],
         gains='Routing by focus is the primary act; shared focus areas and their primary owner show at once.',
         costs='An agent appears on several rows; listening and queries are per focus, not per agent; weak for "is everyone here?".'),
    dict(id='2.2a', page='2.2', title='ki.prj.agora', make=lambda: M.page("Who's doing what", M.agent_a()), zones=['page'], preferred=True,
         why='One page holds everything needed to act on one agent, with the single brass action for what waits on Kris.',
         gains='Complete; the listening bars make a lapse obvious.', costs='Long for an agent with many queries; the bars need a legend.'),
    dict(id='3.1a', page='3.1', title='One record, newest first', make=lambda: M.page("What's being said", M.said_a()), zones=['page'], preferred=True,
         why='One record with a layer column and filters keeps the order of events, which matters when a push, a call '
             'and a reply follow one another across the portal.',
         gains='Time order is kept across layers; filters narrow to Git or Agora, one Mac or both.',
         costs='Busy hours make it long; the layer is a column, not a place.'),
    dict(id='3.1b', page='3.1', title='By layer', make=lambda: M.page("What's being said", M.said_b()), zones=['page'],
         gains='Teaches the two layers: what was written to the record and what was only said.',
         costs='Breaks the order of events across the two columns; a push and the call it causes sit apart.'),
    dict(id='3.2a', page='3.2', title='Sent and heard', make=lambda: M.page('Broadcasts', M.broadcasts_a()), zones=['page'], preferred=True,
         why='Pairs each broadcast with who heard it, and offers the one useful next step: ping the silent again.',
         gains='Answers "did everyone take the Away?" directly.', costs='Received broadcasts from terra need their own section below.'),
    dict(id='4.1a', page='4.1', title='By agent', make=lambda: M.page('Waits on you', M.waits_a()), zones=['page'], preferred=True,
         why='Kris answers a query in its agent\'s thread, so grouping by agent matches where the answer goes; oldest first '
             'within each keeps the longest-waiting at the top.',
         gains='Matches how queries are answered; each agent\'s load is visible.',
         costs='The oldest query overall can sit under a later agent; switch to Oldest first to see it.'),
    dict(id='4.1b', page='4.1', title='Oldest first, all together', make=lambda: M.page('Waits on you', M.waits_b()), zones=['page'],
         gains='The longest wait is always at the top; good for a morning sweep.',
         costs='Jumps between agents row to row; related queries (all of SCHED-) scatter.'),
    dict(id='5.1a', page='5.1', title='The two Macs and the portal', make=lambda: M.page('Macs and the portal', M.macs_a()), zones=['page'], preferred=True,
         why='The same two squares as home, with each Mac and the portal as a small table of facts below it.',
         gains='Facts sit under the picture they belong to.', costs='Repeats the picture from home.'),
    dict(id='5.2a', page='5.2', title='Not level, side by side', make=lambda: M.page('Checkouts', M.checkouts_a()), zones=['page'], preferred=True,
         why='Both Macs side by side make a disagreement plain, and showing only what is not level keeps the page short.',
         gains='Disagreements stand out; what Agora did is beside the checkout.', costs='A Mac that carries a repository the other does not needs a dash.'),
    dict(id='6a', page='6', title='ki.prj.agora · messages.md', make=lambda: M.doc_tab(), zones=['page'], preferred=True,
         why='A tab keeps the document beside the map, one click from home.', gains='Read without leaving the app.',
         costs='Read only for now; editing stays in the owner\'s tools.'),
]

COMPONENTS = [
    dict(id='0.1.1', page='0.1', title='Brand', selector='[data-region="N1"]', states=[('expanded', '0.1a'), ('contracted', '0.1b')]),
    dict(id='0.1.2', page='0.1', title='Views', selector='[data-region="N2"]', states=[('expanded', '0.1a'), ('contracted', '0.1b')]),
    dict(id='0.1.3', page='0.1', title='Speak to everyone', selector='[data-region="N4"]', states=[('expanded', '0.1a'), ('contracted', '0.1b')]),
    dict(id='0.1.4', page='0.1', title='The portal', selector='[data-region="N5"]', states=[('open', '0.1a'), ('terra not heard from', '0.1c'), ('away', 'away')]),
    dict(id='0.1.5', page='0.1', title='Tabs', selector='.tabs', states=[('home', '0.1a'), ('a document open', '6a')]),
    dict(id='0.2.1', page='0.2', title='Summary lines', selector='[data-region="T1"]', states=[('all well', '0.2a'), ('one problem', '0.2b'), ('a Mac missing', '0.2c')]),
    dict(id='0.2.2', page='0.2', title='Exception row', selector='[data-region="T2"]', states=[('a checkout', '0.2b'), ('a Mac', '0.2c')]),
    dict(id='0.2.3', page='0.2', title='Speak to everyone', selector='[data-region="T3"]', states=[('Away…', '0.2a'), ("I'm back", '0.2c')]),
]


def tray_page(key):
    """A tray state as an artboard, its blocks wrapped as T regions."""
    state = next(s for s in TRAY.STATES if s['key'] == key)
    rows = state['rows']
    seps = [i for i, r in enumerate(rows) if r[0] == 'sep']
    blocks = [rows[:seps[0]], rows[seps[0] + 1:seps[1]], rows[seps[1] + 1:seps[2]], rows[seps[2] + 1:]]
    summary, exceptions = blocks[0][:2], blocks[0][2:]
    parts = [f'<div {M.R("T1", "Summary lines")}>{TRAY.render_rows(summary)}</div>']
    if exceptions:
        parts.append(f'<div {M.R("T2", "Exceptions")}>{TRAY.render_rows(exceptions)}</div>')
    parts += ['<div class="sep"></div>', f'<div {M.R("T3", "Speak to everyone")}>{TRAY.render_rows(blocks[1])}</div>',
              '<div class="sep"></div>', f'<div {M.R("T4", "Detail")}>{TRAY.render_rows(blocks[2])}</div>',
              '<div class="sep"></div>', f'<div {M.R("T5", "Agora itself")}>{TRAY.render_rows(blocks[3])}</div>']
    ring = TRAY.RING[state['icon']].replace('{n}', '1')
    return f'''<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><style>{TRAY.CSS}
body {{ width:760px; padding:20px 28px 28px; }} .panel {{ margin:0; }}</style></head><body>
<figure class="panel light" {M.R("T0", "Whole tray")}><div class="bar"><span class="clock">Fri 6 Nov 04:20</span><svg class="ring" viewBox="0 0 18 18">{ring}</svg></div>
<div class="menus"><div class="menu">{''.join(parts)}</div></div></figure></body></html>'''


def main():
    os.makedirs(MOCKS, exist_ok=True)
    shots = []
    for ab in ARTBOARDS:
        html = tray_page(ab['tray']) if 'tray' in ab else ab['make']()
        path = os.path.join(MOCKS, f'{ab["id"]}.html')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        shots.append(dict(shot=ab['id'], html=os.path.abspath(path), width=760 if 'tray' in ab else 1440))
    # A shell state used only for a component: this Agora away.
    away = os.path.join(MOCKS, 'away.html')
    with open(away, 'w', encoding='utf-8') as f:
        f.write(M.page('Home', M.shell_blank('Not in the Agora'), mark_shell=True, portal='away'))
    shots.append(dict(shot='away', html=os.path.abspath(away), width=1440, hidden=True))
    # The preferred home in light, for comparison.
    light = os.path.join(MOCKS, '1a-light.html')
    with open(light, 'w', encoding='utf-8') as f:
        f.write(M.page('Home', M.home_map(), theme='light'))
    shots.append(dict(shot='1a-light', html=os.path.abspath(light), width=1440, hidden=True))
    components = [dict(id=c['id'], selector=c['selector'], states=c['states']) for c in COMPONENTS]
    plan = dict(pages=PAGES, artboards=[{k: v for k, v in ab.items() if k != 'make'} for ab in ARTBOARDS],
                components=components, shots=shots)
    with open(os.path.join(HERE, 'plan.json'), 'w', encoding='utf-8') as f:
        json.dump(plan, f, indent=2, ensure_ascii=False)
    print(f'{len(shots)} mock-ups, {len(COMPONENTS)} components')


if __name__ == '__main__':
    main()
