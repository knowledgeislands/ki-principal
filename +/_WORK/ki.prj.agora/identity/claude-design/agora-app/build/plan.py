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
import work as W  # noqa: E402  (7.1 Roadmap, 7.2 Jobs, 8.1 Guilds)
import home as H  # noqa: E402  (9.1 Home: who holds what)
import build as TRAY  # noqa: E402  (the tray mock-up's builder, ../../tray/build.py)

HERE = os.path.dirname(os.path.abspath(__file__))
MOCKS = os.path.join(HERE, '..', 'mocks')

PAGES = [
    dict(id='0.1', title='Shell: the window and its rail', zones=['navigation'],
         note='Superseded by 0.3 Atlas shell; kept for the record. The frame every view sits in: the brand, the views, what is coming from the KIV and the Observatory, '
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
    dict(id='0.3', title='Atlas shell (sidebar superseded by 0.4)', zones=['navigation', 'context', 'page', 'tray', 'bottom'],
         note='Its sidebar is superseded by 0.4 Atlas shell, revised (Kris\'s review, 22:55 to 23:20 GMT): Home leaves the sidebar for the logo, '
              'the map becomes Known Lands under Work, and every place sits in a section with a small eyebrow. The toolbar, tabs, context control, '
              'tray and bottom pane here still stand; the boards are kept, drawn in the 0.3 sidebar, for the record. The frame every page of Agora Atlas sits in, now that the app holds far more than the first pack drew: the map, '
              'the work (Roadmap, Jobs), the guilds, the Observatory\'s instruments, the KIV\'s pages, accounts, settings and updates. '
              'It replaces the rail of 0.1. It matters because each page so far brought its own tray, pane and filters; one shell '
              'with fixed places for navigation, context, detail and documents lets Kris learn the window once, and lets the '
              'Roadmap, Jobs and Guilds designers build on the same frame (atlas_page in build/mocks.py; IA.md has the rules).',
         fields=['Toolbar (N1): Agora Atlas, the rigs, one word on the whole, the search, Mark all, Away…, Broadcast…, the time, pin and theme',
                 'Sidebar groups (N2): Agora, Work, Guilds, Observatory, KIV (folded while it is coming), Coming; a count only where something waits',
                 'Sidebar foot (N3): Accounts, Settings, Updates; the portal between the rigs; Beacon in the menu bar and Lantern on the iPhone',
                 'Tabs (N4): the place or document in each tab; a sidebar click replaces the current tab, ⌘-click opens a new one',
                 'Context (C1), top right: the territory and the plane for every page that reads them; greyed, not hidden, where a page ignores one',
                 'Page (P): the page header and its content, which the page owns',
                 'Right tray (T1): the facts of one selected thing; it pushes the page narrower and closes with × or Escape',
                 'Bottom pane (B1): the selected thing\'s documents or long readings, in tabs; drag its top edge to resize']),
    dict(id='0.4', title='Atlas shell, revised', zones=['navigation', 'context', 'page'],
         note='Kris\'s review (22:55 to 23:20 GMT) of the 0.3 sidebar. Home leaves the sidebar and is reached by clicking the Agora Atlas logo, '
              'as on a website; the map that was Home becomes Known Lands, under Work, with an old chart for its glyph. Every place now sits in a '
              'section with a smaller eyebrow, every section folds, and folded to icons each section keeps a three-letter eyebrow: AGO, WRK, GLD, '
              'OBS, KIV, SYS. Accounts, Settings and Updates form SYS at the foot, above the portal line. It matters because the sidebar is on every '
              'page: one rule for every section is quicker to learn than groups, a lone place and a foot that each behaved differently. Every page '
              'in the pack now draws this sidebar, except 0.1\'s and 0.3\'s own boards.',
         fields=['Logo (N5): Agora Atlas in the toolbar is Home; it is underlined while Home is open, and says "Home" on hover',
                 'Sections (N2): AGO Agora, WRK Work (Known Lands, Roadmap, Jobs, Art gallery later), GLD Guilds, OBS Observatory, KIV (folded while it is coming)',
                 'Eyebrow: 9.5-point capitals with a fold chevron; folded, it carries its count of places and, in a gold-edged word, what inside wants a look',
                 'Folded to icons (⌘\\): the three-letter eyebrow heads each section; a folded section is a dashed box with its letters and a chevron',
                 'Foot (N3): SYS (Accounts, Settings, Updates), then the portal between the rigs, Beacon and Lantern',
                 'Known Lands: a curled chart with a dotted path to an X, so it reads as a map and not as a graph']),
    dict(id='1', title='Known Lands (was Home)', zones=['page'],
         note='Known Lands since 0.4: the map that was Home now sits under Work, and Home (9.1) is reached from the logo. '
              'One view that fits the window with no scrolling (MSG-62774774, Kris\'s vision): the territories and their '
              'islands, the work packages and workers placed where they work, the primary focus of each, the island portal on '
              'each island, the threads of talk up to each territory\'s principal portal and across, and the planar portal, '
              'on its own island ki-portal, between the planes. The preferred home (1f) makes it a working map: active islands '
              'stand out, Focused hides the quiet ones, each island carries its queued work and waiting messages, and clicking '
              'an island shows its detail in the right tray. It matters because it is the page the app opens on, and it should '
              'show the whole distributed Agora as one place where Kris can see where work is and pick it up.',
         fields=['Toolbar: Focused or Everything; the plane (sol, terra or both); zoom out, the level, zoom in, Fit; Show as a list',
                 'Territories, each a faint boundary with its name', 'Islands (repositories), drawn as hexes: active as land, quiet as outlines',
                 'On each island: its name, queued work (a stack) and waiting messages (an envelope), each a small count; zero left out',
                 'Island portal on each island: lit when someone there listens; the principal portal larger on each principal island',
                 'The planar portal on ki-portal in Personal, ringed in gold, kept by the watchman; sol and terra, open or not',
                 'Workers by role: council, enabler, doer; each with its primary focus and rig', 'Listening by shape: solid listening, hollow on open, slashed silent',
                 'Threads of talk: island portals up to the principal portal, principal portals across, the planar portal out to the other plane',
                 'Right tray, an island selected: where it is, its portal, checkouts, who works there, queued work, waiting messages, what waits on Kris',
                 'Right tray, nothing selected: at a glance and the key', 'Zoomed: labels stay at reading size and add when each worker last answered; an overview shows where the view sits']),
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
    dict(id='7.1', title='Roadmap', zones=['page', 'tray'],
         note='Every work record on the lands this Mac carries, read from each island\'s docs/roadmap/ or a knowledge base\'s '
              'Streams/Roadmap/ front matter, as the built app reads it (src/app/roadmap.ts). Kris asked for "the roadmap table ... filter it '
              'based on the summary table ... and on different factors", with the details in the right-hand tray. It matters because the '
              'records are spread over a dozen islands: this is the one place to see what is in progress, what waits for review and what '
              'is piling up in triage, and to pick one up. It settles the summary-filter bar (7.1.1) that Jobs shares.',
         fields=['Tallies (P2): All open, then each open status (in progress, awaiting review, ready, draft, triage) with its count; '
                 'a click keeps only that status, ⌘-click adds one; done and cancelled are one tally, hidden until chosen',
                 'Chips (P2): the territory from the context first, then each chosen value, removable; one Filter menu for priority, horizon, '
                 'area, size, island, kind and assignee, each value with its count',
                 'Words to find in an id or title; Group by status, island, area or none',
                 'Records (P3): id, title, island, status (mark and word), priority and size, when it last changed; a long group folds after a few rows',
                 'Right tray (T1), a record chosen: its front matter, what it is blocked by and blocks, its Goal and Context; '
                 'Open the file, Read in full (the bottom pane), Show on Home']),
    dict(id='7.2', title='Jobs', zones=['page', 'tray', 'bottom'],
         note='Every scheduled job and service Rig declares on either Mac, grouped by the territory and then the repository each one works '
              'in, as the built app does (src/app/jobs.ts). Kris asked for "a similar list view ... based on the scheduled jobs, by territory, '
              'and then by repository". It matters because a job that fails at 07:15 on one Mac is otherwise noticed only when its output '
              'is missed. Agora only shows: running, starting or stopping a job stays Rig\'s (KI-AGORA-WRK-004).',
         fields=['Tallies (P2): All, Failed, Findings, OK, No run yet, Off, Services; Failed and Findings carry the gold edge while non-zero',
                 'Chips (P2): territory and plane from the context; one Filter menu for kind, Mac, profile and provider; words; Group by repository, Mac or none',
                 'Jobs (P3): name and Rig id, schedule in words, each Mac that runs it marked by how its last run there ended, last run, next run by its schedule, how it stands',
                 'Right tray (T1), a job chosen: its standing, purpose, the declaration (id, schedule, next, declared, profiles, provider, label, '
                 'works in, program), each Mac\'s last runs as marks and the last one\'s line; Show runs, Open its file, Show on Home',
                 'Bottom pane (B1), after Show runs: every run kept on both Macs, newest first: finished, Mac, outcome, summary; and the declaration',
                 'Never shown: a job\'s environment, arguments or output']),
    dict(id='8.1', title='Guilds', zones=['page', 'bottom'],
         note='The guilds and their skills, read from each *-agentic-harness island on the lands, and a chosen skill\'s documents (src/app/guilds.ts, '
              'skills.ts). Kris asked for "each of the guilds ... some kind of panel with a logo on it, what the guild is about, and then underneath '
              'it a bank of skills". It matters because seventy-odd skills are only findable today by knowing their folder; the badges make the '
              'guilds a place to browse, and the pane reads a skill without leaving Atlas. The territory is the context control\'s. Until the '
              'guildmaster\'s catalogue (ki.reg.guilds) names the guilds, each harness folder stands in, and the page says so.',
         fields=['Guild badges (P2), across: All guilds, then each guild\'s badge: its logo or monogram on its own colour, its name and how many '
                 'skills; a badge is a tally, so choosing it keeps that guild',
                 'Skills (P3): the chosen guild\'s about line and its skills as sub-badges, each with its guild\'s small shield; with All guilds, a ledger, one guild a row',
                 'Words to find a skill by name, description or guild',
                 'Bottom pane (B1), a skill chosen: its guild and harness, its name, and a tab for SKILL.md (front matter, then its '
                 'instructions drawn), each other document and each folder (references/, scripts/, assets/) with its files',
                 'Notices: provisional guilds; a harness without skills; another territory\'s own unsorted skills as one guild']),
    dict(id='9.1', title='Home: who holds what', zones=['page', 'tray'],
         note='Home, reached from the Agora Atlas logo (0.4). Kris\'s review asks for "who holds what": one row per live package with its role, '
              'tier, rig, focus areas and state, with a footnote wherever a package\'s record disagrees with the guild catalogue, and the roles '
              'the catalogue names that nobody holds yet. Needs a look sits above it, each item saying what it is and what to do, so the page '
              'Atlas opens on answers "is anything wrong, and who is on it?" first. It matters because the map shows where work '
              'is; Home shows who answers for it.',
         fields=['Needs a look (P2): urgent or look, each a mark and a word; what it is; what to do; one plain action',
                 'Who holds what (P3): Role (Kris\'s emoji and its word), Tier (Leader, Manager, Doer), Package (the work id), Rig, '
                 'Focus areas on one line (⭐ and bold for the primary, ⏰ for something scheduled), State (🤖 Working, 👤 With you, 💤 Idle, 🔕 Silent)',
                 'Doers appear as Doer rows, with the package that brought them in',
                 'Footnotes (P4): † ‡ § mark the cell where the record and the catalogue disagree; the row shows the catalogue',
                 'Yours to approve (P5): catalogue roles not yet created, with the proposed package and rig; the one brass action approves the section',
                 'Right tray (T1), a row chosen: its facts, its focus areas with their schedule, and the record beside the catalogue']),
]

# Each artboard: page, letter, title, the mock-up to draw, its zones, and for alternatives the trade-off.
ARTBOARDS = [
    dict(id='0.1a', page='0.1', dropped='superseded by 0.3 Atlas shell', title='Rail expanded, both Macs here', make=lambda: M.page('Home', M.shell_blank('12 agents on 2 Macs · All well'), mark_shell=True), zones=['navigation']),
    dict(id='0.1b', page='0.1', dropped='superseded by 0.3 Atlas shell', title='Rail contracted', make=lambda: M.page('Home', M.shell_blank('12 agents on 2 Macs · All well'), contracted=True, mark_shell=True), zones=['navigation']),
    dict(id='0.1c', page='0.1', dropped='superseded by 0.3 Atlas shell', title='Rail expanded, terra not heard from', make=lambda: M.page('Home', M.shell_blank('5 agents on 1 Mac · 1 needs a look'), mark_shell=True, portal='unheard'), zones=['navigation']),
    dict(id='0.2a', page='0.2', title='Tray, all well', tray='all-well', zones=['tray']),
    dict(id='0.2b', page='0.2', title='Tray, one problem', tray='one-problem', zones=['tray']),
    dict(id='0.2c', page='0.2', title='Tray, a Mac missing', tray='mac-missing', zones=['tray']),
    dict(id='0.3a', page='0.3', title='Grouped sidebar: Roadmap, a record in the tray',
         make=lambda: M.atlas_page('roadmap', W.roadmap_page(), tray=W.record_tray(), mark_shell=True, shell='0.3',
                                   context=dict(territory='Knowledge Islands'),
                                   tabs=[('Roadmap', True, True), ('Home', False, True), ('ki.prj.agora · messages.md', False, True)]),
         zones=['navigation', 'context', 'page', 'tray'], preferred=True,
         why='Every place is one click away and stays where Kris learnt it, grouped by what it is about; the KIV, still coming, folds to one line '
             'so the sidebar fits without scrolling. Context, detail and documents each have one fixed place, so every page behaves the same.',
         gains='One look shows all of Atlas; counts in the sidebar say where something waits; the context control sets the territory once for '
               'Home, Roadmap, Jobs, Guilds and the Observatory; the tray and the bottom pane open the same way on every page.',
         costs='Twenty-odd places is a long list: with the KIV unfolded it needs folding elsewhere or a scroll; the sidebar takes 220 points '
               '(56 folded); a greyed context control on Settings or Guilds is one more thing to read past.'),
    dict(id='0.3b', page='0.3', title='Grouped sidebar: Guilds, a skill in the bottom pane',
         make=lambda: M.atlas_page('guilds', W.guilds_page(), bottom=W.skill_pane(), mark_shell=True, shell='0.3',
                                   context=dict(territory='Knowledge Islands'), tabs=[('Guilds', True, True), ('Roadmap', False, True)]),
         zones=['navigation', 'context', 'page', 'bottom']),
    dict(id='0.3c', page='0.3', title='Sidebar folded: Home, the territory menu open',
         make=lambda: M.atlas_page('home', M.atlas_home(), folded=True, mark_shell=True, shell='0.3', context=dict(open=True),
                                   tabs=[('Home', True, False), ('Roadmap', False, True), ('Guilds', False, True)]),
         zones=['navigation', 'context', 'page']),
    dict(id='0.3d', page='0.3', title='Tray and bottom pane together: Jobs, a job and its runs',
         make=lambda: M.atlas_page('jobs', W.jobs_page(), tray=W.job_tray(), bottom=W.job_bottom(), mark_shell=True, shell='0.3',
                                   standing=('look', '1 needs a look'),
                                   tabs=[('Jobs', True, True), ('Home', False, True)]),
         zones=['navigation', 'context', 'page', 'tray', 'bottom']),
    dict(id='0.3e', page='0.3', title='Sections across the top: Work, Roadmap, a record in the tray',
         make=lambda: M.atlas_page('roadmap', W.roadmap_page(), tray=W.record_tray(), mark_shell=True, shell='0.3', variant='sections',
                                   context=dict(territory='Knowledge Islands'),
                                   tabs=[('Roadmap', True, True), ('Home', False, True), ('ki.prj.agora · messages.md', False, True)]),
         zones=['navigation', 'context', 'page', 'tray'],
         gains='The sidebar holds only the section\'s few pages, so it never needs folding or scrolling and leaves more of the window to the page; '
               'the five sections name the app\'s parts plainly; it grows by adding a section.',
         costs='Crossing sections (Roadmap to Home, Jobs to Guilds) takes two clicks and the sidebar changes under the pointer; counts in other '
               'sections are out of sight; Accounts, Settings and Updates hide behind the gear; the toolbar is fuller.'),
    dict(id='0.4a', page='0.4', title='Sidebar in sections: Known Lands under Work, KIV folded',
         make=lambda: M.atlas_page('lands', M.atlas_home('Known Lands'), mark_shell=True,
                                   tabs=[('Known Lands', True, True), ('Home', False, True), ('Roadmap', False, True)]),
         zones=['navigation', 'context', 'page'], preferred=True,
         why='One rule for every section: an eyebrow, a fold, its places. Home is where Kris expects it, on the logo, so the sidebar holds only '
             'places to go; Known Lands sits with the other work it leads to, and the foot is a section like the rest.',
         gains='The sidebar is shorter by one row and reads as six named parts; folding works the same everywhere; folded to icons, the '
                'three-letter eyebrows keep the parts apart; SYS makes Accounts, Settings and Updates foldable like the rest.',
         costs='Home is one more thing to learn for someone who expects it first in the list; the logo must say "Home" on hover (0.4c); '
               'Guilds has an eyebrow over a single place, which repeats its name.'),
    dict(id='0.4b', page='0.4', title='Sidebar folded to icons: three-letter eyebrows, Jobs open, KIV and OBS folded',
         make=lambda: M.atlas_page('jobs', W.jobs_page(), tray=W.job_tray(), folded=True, collapsed=('kiv', 'observatory'), mark_shell=True,
                                   standing=('look', '1 needs a look'), tabs=[('Jobs', True, True), ('Home', False, True)]),
         zones=['navigation', 'context', 'page', 'tray']),
    dict(id='0.4c', page='0.4', title='The logo hovered: "Home", from Roadmap',
         make=lambda: M.atlas_page('roadmap', W.roadmap_page(), tray=W.record_tray(), mark_shell=True, logo='hover', collapsed=('kiv', 'sys'),
                                   context=dict(territory='Knowledge Islands'), tabs=[('Roadmap', True, True), ('Home', False, True)]),
         zones=['navigation', 'context', 'page', 'tray']),
    dict(id='1f', page='1', title='The working map: Focused, an island selected', make=lambda: M.page('Home', M.home_working(focused=True, selected='apps-agora.local')),
         zones=['page'], preferred=True,
         why='It keeps the picture Kris described and makes it the place to act from: Focused shows only where work is, each island says '
             'how much is queued and waiting, and one click opens an island in the tray without leaving the map. It fits one window.',
         gains='Active islands read at once; counts show where work piles up before a worker says so; the tray holds the detail, so the map '
               'keeps few words; the toolbar puts filter, plane, zoom and the list in one place.',
         costs='Focused hides quiet islands, so a forgotten repository with queued work is only a line in the corner; the tray takes 304 '
               'points from the map; counts are two more marks per island to learn.'),
    dict(id='1g', page='1', title='The working map: Everything, the planar portal selected', make=lambda: M.page('Home', M.home_working(focused=False, selected='ki-portal')), zones=['page']),
    dict(id='1h', page='1', title='The working map: closer on Humans Not Robots', make=lambda: M.page('Home', M.home_working(focused=False, selected='hnr-principal', zoom='hnr')), zones=['page']),
    dict(id='1a', page='1', title='The map of territories', make=lambda: M.page('Home', M.home_map()), zones=['page'],
         gains='The whole distributed Agora in one look, with the key always beside it; nothing is hidden, so nothing is missed.',
         costs='Every island weighs the same, active or quiet; no counts, so where work waits needs another page; no selection or zoom, '
               'so a busy island\'s labels crowd and its detail is a page away. Was preferred until 1f.'),
    dict(id='1d', page='1', title="1a on sol's plane", make=lambda: M.page('Home', M.home_map('sol')), zones=['page']),
    dict(id='1e', page='1', title="1a on terra's plane", make=lambda: M.page('Home', M.home_map('terra')), zones=['page']),
    dict(id='1b', page='1', title='The councils', make=lambda: M.page('Home', M.home_council()), zones=['page'],
         gains='The hierarchy of talk is exact and legible: each council with who talks up to it; scales to many work packages.',
         costs='No islands or geography, so it is a diagram, not the place; the planar portal becomes a band.'),
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
    # ---- 7.1 Roadmap
    dict(id='7.1a', page='7.1', title='Tallies over a grouped table: a record in the tray', make=lambda: W.ab_roadmap(), zones=['page', 'tray'], preferred=True,
         why='The counts sit where the eye starts, across the top, and each one is the filter it names, so summary and filter are one '
             'control; the table keeps the full width and groups by status, so what is in progress and what waits for review lead. The same '
             'bar serves Jobs, and the guild badges are its tallies in another shape.',
         gains='One row of counts reads at a glance and filters in one click; chips say every filter in force, the context\'s first; a single '
               'Filter menu keeps the row short beside the tray; long groups fold so every status heading fits one window.',
         costs='Counts by status only: "how much triage on tools-ki?" needs Group by island or a chip, where the pivot answers it in one cell; '
               'folding hides rows behind "Show 20 more"; the Filter menu is one click deeper than a row of menus.'),
    dict(id='7.1b', page='7.1', title='The summary beside the table: a cell as the filter', make=lambda: W.ab_roadmap_pivot(), zones=['page'],
         gains='The built app\'s shape: two dimensions at once (island against status), every cell a filter; a row field switch '
               '(status, priority, area, territory, island) answers most questions without the table.',
         costs='Takes 330 points from the table, and with the tray open the table drops to about 470; numbers in a grid read slower than '
               'words; status columns need a key; a menu per field fills a second row.'),
    dict(id='7.1c', page='7.1', title='7.1a with a filter applied: Triage, priority high, the Filter menu open, by island', make=lambda: W.ab_roadmap_filtered(), zones=['page']),
    dict(id='7.1d', page='7.1', title='7.1a with a record awaiting review in the tray', make=lambda: W.ab_roadmap_review(), zones=['page', 'tray']),
    dict(id='7.1e', page='7.1', title='7.1a with nothing matching', make=lambda: W.ab_roadmap_empty(), zones=['page']),
    # ---- 7.2 Jobs
    dict(id='7.2a', page='7.2', title='By territory and repository: a failed job, its runs below', make=lambda: W.ab_jobs(), zones=['page', 'tray', 'bottom'], preferred=True,
         why='It is Kris\'s grouping, with the same bar as Roadmap, so a failed job is one tally away; each Mac is a marked chip in one '
             'column, so two Macs or one read the same. The tray holds the declaration and the last runs; the whole history opens below only '
             'when asked, as the shell rules say.',
         gains='Territory headings fold and say what is inside (2 jobs, 1 failed), so a quiet territory takes one line; the run marks in the '
               'tray show a pattern (two findings, then a failure) before the history is opened; the next run is worked out from the schedule.',
         costs='A job run on both Macs shows its two outcomes as two small chips, not side by side; tray and pane together leave the table '
               'about ten rows; the next run is derived, not reported.'),
    dict(id='7.2b', page='7.2', title='Each Mac a column', make=lambda: W.ab_jobs_bymac(), zones=['page'],
         gains='Like Checkouts: what ran where, and how it ended, side by side; a job missing from one Mac shows as not selected.',
         costs='Most jobs run on one Mac, so half the cells say not selected; a third Mac widens every row; the per-Mac column takes the '
               'room the standing word had.'),
    dict(id='7.2c', page='7.2', title='7.2a with Failed and Findings chosen', make=lambda: W.ab_jobs_filtered(), zones=['page']),
    dict(id='7.2d', page='7.2', title='7.2a with a service in the tray, Personal folded', make=lambda: W.ab_jobs_service(), zones=['page', 'tray']),
    # ---- 8.1 Guilds
    dict(id='8.1a', page='8.1', title='Badges across, the guild\'s skills beneath: a skill\'s SKILL.md below', make=lambda: W.ab_guilds(), zones=['page', 'bottom'], preferred=True,
         why='Every guild\'s badge fits one row across the page, so all eight are seen at once with no sideways scroll; choosing one shows its '
             'skills as sub-badges large enough to read, and a skill opens below without hiding the badges. It is Kris\'s panel with a logo, '
             'its about line and a bank of skills, laid out so it fits beside the pane.',
         gains='Badges act like the tallies on Roadmap and Jobs, so the pattern is learnt once; the pane has 390 points for a document; '
               'All guilds gives the ledger when Kris wants every skill (8.1c).',
         costs='A guild\'s about line moves from its badge to the line above its skills; ten or more guilds will need a second row or '
               'narrower badges; skills of other guilds are one click away, not in view.'),
    dict(id='8.1b', page='8.1', title='Guild columns across: the built app\'s panels', make=lambda: W.ab_guilds_columns(), zones=['page', 'bottom'],
         gains='Closest to Kris\'s words and to the built page: each guild a panel with its badge, about and skills beneath; several guilds\' '
               'skills in view at once.',
         costs='Five of eight guilds fit, the rest scroll sideways; a guild of sixteen skills shows seven and "9 more"; with the pane open '
               'each column is short.'),
    dict(id='8.1c', page='8.1', title='8.1a with no skill chosen: All guilds as a ledger', make=lambda: W.ab_guilds_rest(), zones=['page']),
    dict(id='8.1d', page='8.1', title='8.1a for another territory: Humans Not Robots from the context', make=lambda: W.ab_guilds_hnr(), zones=['page', 'bottom']),
    dict(id='8.1e', page='8.1', title='8.1a with a folder tab: references/, one document drawn', make=lambda: W.ab_guilds_folder(), zones=['page', 'bottom']),
    dict(id='9.1a', page='9.1', title='One table by tier: needs a look above, yours to approve below', make=lambda: H.ab_home(),
         zones=['page'], preferred=True,
         why='One table answers "who holds what" in one look, Leaders first, so the governors read before the managers and doers they lead; '
             'what needs a look comes first because it is what Kris acts on, and the roles to approve close the page.',
         gains='Every package is one row on one line; a footnote shows each disagreement without a second table; the tier order matches the '
                'catalogue; one brass action for the whole section.',
         costs='Rig and territory are columns, not groups, so "what runs on terra?" means reading down; fourteen rows today, and it grows with '
               'every doer brought in.'),
    dict(id='9.1b', page='9.1', title='Grouped by rig: sol, then terra', make=lambda: H.ab_home_by_rig(), zones=['page'],
         gains='Shows at once what each rig carries and how much of it is working; a missing rig is one heading that says so; drops the Rig column.',
         costs='The governors are split across two groups, so the hierarchy no longer reads top to bottom; a rig heading per host grows with the hosts.'),
    dict(id='9.1c', page='9.1', title='9.1a with a row chosen: personal.reg.inbox-terra in the tray, its record against the catalogue',
         make=lambda: H.ab_home_selected(), zones=['page', 'tray']),
]

COMPONENTS = [
    dict(id='7.1.1', page='7.1', title='Summary-filter bar', selector='.sf',
         states=[('Roadmap at rest', '7.1a'), ('a tally and a chip applied', '7.1c', '.sf-tallies, .sf-row'), ('nothing matching', '7.1e'), ('Jobs', '7.2a'), ('Jobs, two tallies chosen', '7.2c')]),
    dict(id='7.1.2', page='7.1', title='Chips', selector='[data-chip="ctx"]',
         states=[('from the context', '7.1a'), ('chosen, removable', '7.1c', '[data-chip="chosen"]'), ('the Filter button', '7.1a', '[data-chip="field"]'),
                 ('the Filter menu open', '7.1c', '[data-chip="field"], [data-chip="menu"]'), ('territory and plane from the context', '7.2a', '.sfchips')]),
    dict(id='7.1.3', page='7.1', title='Record row', selector='tr.rec.sel',
         states=[('chosen', '7.1a'), ('plain', '7.1a', 'tr[data-row="KI-AGORA-WRK-007"]'), ('awaiting review', '7.1a', 'tr[data-row="KI-AGORA-TRY-001"]'),
                 ('a group heading', '7.1a', 'tr[data-grp="triage"]'), ('a folded group', '7.1a', 'tr.more')]),
    dict(id='7.1.4', page='7.1', title='Record in the tray', selector='[data-region="T1"]',
         states=[('a record', '7.1a'), ('awaiting review, the one brass action', '7.1d')]),
    dict(id='7.2.1', page='7.2', title='Job row', selector='tr.job.sel',
         states=[('failed, chosen', '7.2a'), ('two Macs, ok and no run yet', '7.2-rows', 'tr[data-job="good-morning"]'), ('a service', '7.2-rows', 'tr[data-job="kiv"]'),
                 ('off', '7.2-rows', 'tr[data-job="dock-autohide"]'), ('findings', '7.2c', 'tr[data-job="ki-territory-audit"]'),
                 ('a territory folded', '7.2a', 'tr.terr.shut'), ('a repository heading', '7.2a', 'tr[data-repo="hnr-principal"]')]),
    dict(id='7.2.2', page='7.2', title='Job in the tray', selector='[data-region="T1"]',
         states=[('a failed job, runs shown', '7.2a'), ('a service', '7.2d')]),
    dict(id='7.2.3', page='7.2', title='Run history in the bottom pane', selector='[data-region="B1"]', states=[('runs on both Macs', '7.2a')]),
    dict(id='8.1.1', page='8.1', title='Guild badge', selector='[data-guild="governance"]',
         states=[('chosen', '8.1a'), ('plain', '8.1a', '[data-guild="change-management"]'), ('All guilds, chosen', '8.1c', '[data-guild="all"]'),
                 ('a territory\'s own skills', '8.1d', '[data-guild="hnr-own"]'), ('the strip', '8.1a', '.gstrip')]),
    dict(id='8.1.2', page='8.1', title='Skill badge', selector='[data-skill="ki-git"]',
         states=[('plain', '8.1a'), ('open in the pane', '8.1a', '[data-skill="ki-delegation"]'), ('in the ledger', '8.1c', '[data-ledger="acquire"]')]),
    dict(id='8.1.3', page='8.1', title='Skill in the bottom pane', selector='[data-region="B1"]',
         states=[('SKILL.md', '8.1a'), ('a folder tab', '8.1e')]),
    dict(id='0.4.1', page='0.4', title='Section eyebrow', selector='[data-group="work"] h4',
         states=[('open', '0.4a'), ('folded', '0.4a', '[data-group="kiv"] h4'), ('folded, something inside to look at', '0.4c', '[data-group="sys"] h4'),
                 ('collapsed', '0.4b', '[data-group="work"] h4'), ('collapsed and folded', '0.4b', '[data-group="observatory"] h4')]),
    dict(id='0.4.2', page='0.4', title='Known Lands item', selector='[data-place="lands"]',
         states=[('chosen', '0.4a'), ('plain', '0.4c'), ('collapsed', '0.4b')]),
    dict(id='0.4.3', page='0.4', title='The logo as Home', selector='.at-brand',
         states=[('at rest', '0.4a'), ('hovered, "Home"', '0.4c', '.at-brand, .at-tip'), ('Home open', '9.1a')]),
    dict(id='9.1.1', page='9.1', title='Holder row', selector='tr[data-holder="ki.sop.main"]',
         states=[('working, a Leader', '9.1a'), ('with you', '9.1a', 'tr[data-holder="ki.prj.agora"]'), ('silent', '9.1a', 'tr[data-holder="hnr.sop.main"]'),
                 ('a footnote', '9.1a', 'tr[data-holder="hnr.prj.site-robots"]'), ('a doer', '9.1a', 'tr[data-holder="Claude Design"]'),
                 ('chosen', '9.1c', 'tr.holder.sel')]),
    dict(id='9.1.2', page='9.1', title='Needs a look', selector='[data-region="P2"]',
         states=[('urgent and look', '9.1a'), ('nothing', '9.1-none')]),
    dict(id='9.1.3', page='9.1', title='Yours to approve', selector='[data-region="P5"]', states=[('three roles, one brass action', '9.1a')]),
    dict(id='9.1.4', page='9.1', title='Holder in the tray', selector='[data-region="T1"]', states=[('record against the catalogue', '9.1c')]),
    dict(id='0.1.1', page='0.1', title='Brand', selector='[data-region="N1"]', states=[('expanded', '0.1a'), ('contracted', '0.1b')]),
    dict(id='0.1.2', page='0.1', title='Views', selector='[data-region="N2"]', states=[('expanded', '0.1a'), ('contracted', '0.1b')]),
    dict(id='0.1.3', page='0.1', title='Speak to everyone', selector='[data-region="N4"]', states=[('expanded', '0.1a'), ('contracted', '0.1b')]),
    dict(id='0.1.4', page='0.1', title='The portal', selector='[data-region="N5"]', states=[('open', '0.1a'), ('terra not heard from', '0.1c'), ('away', 'away')]),
    dict(id='0.1.5', page='0.1', title='Tabs', selector='.tabs', states=[('home', '0.1a'), ('a document open', '6a')]),
    dict(id='0.3.1', page='0.3', title='Sidebar group (superseded by 0.4.1)', selector='[data-group="agora"]',
         states=[('open, a count waiting', '0.3a'), ('folded to its heading', '0.3a', '[data-group="kiv"]'),
                 ('a lone place', '0.3a', '[data-group="guilds"]'), ('the sidebar folded', '0.3c', '.at-groups')]),
    dict(id='0.3.2', page='0.3', title='Context control', selector='[data-region="C1"]',
         states=[('territory, plane ignored', '0.3a'), ('territory and plane', '0.3d'), ('the territory menu open', '0.3c', '[data-region="C1"], .at-menu')]),
    dict(id='0.3.3', page='0.3', title='Tray frame', selector='[data-region="T1"]',
         states=[('a work record', '0.3a'), ('a job', '0.3d')]),
    dict(id='0.3.4', page='0.3', title='Bottom pane frame', selector='[data-region="B1"]',
         states=[('a skill\'s documents', '0.3b'), ('a job\'s runs', '0.3d')]),
    dict(id='0.3.5', page='0.3', title='Toolbar', selector='[data-region="N1"]',
         states=[('all well', '0.3a'), ('one needs a look', '0.3d')]),
    dict(id='0.3.6', page='0.3', title='Sidebar foot', selector='[data-region="N3"]',
         states=[('expanded', '0.3a'), ('folded', '0.3c')]),
    dict(id='1.1', page='1', title='Toolbar', selector='[data-region="P2"]', states=[('Focused', '1f'), ('Everything', '1g'), ('closer', '1h')]),
    dict(id='1.2', page='1', title='Island with counts', selector='[data-island="apps-agora.local"], [data-island-head="apps-agora.local"]',
         states=[('active, selected', '1f'),
                 ('principal, messages waiting', '1f', '[data-island="hnr-principal"], [data-island-head="hnr-principal"]'),
                 ('the planar portal', '1g', '[data-island="ki-portal"], [data-island-head="ki-portal"]'),
                 ('quiet', '1g', '[data-island="tools-ki"], [data-island-head="tools-ki"]'),
                 ('closer, counts in words', '1h', '[data-island="5g-emerge"], [data-island-head="5g-emerge"]')]),
    dict(id='1.3', page='1', title='Island detail in the right tray', selector='[data-region="P4"]',
         states=[('an island', '1f'), ('the planar portal', '1g'), ('needs a look', '1h'), ('nothing selected', '1f-none')]),
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
    light = os.path.join(MOCKS, '1f-light.html')
    with open(light, 'w', encoding='utf-8') as f:
        f.write(M.page('Home', M.home_working(focused=True, selected='apps-agora.local'), theme='light'))
    shots.append(dict(shot='1f-light', html=os.path.abspath(light), width=1440, hidden=True))
    # The working map with nothing selected: the tray shows at a glance and the key (a component state only).
    tray = os.path.join(MOCKS, '1f-none.html')
    with open(tray, 'w', encoding='utf-8') as f:
        f.write(M.page('Home', M.home_working(focused=True, selected=None)))
    shots.append(dict(shot='1f-none', html=os.path.abspath(tray), width=1440, hidden=True))
    # Jobs with Personal open and nothing chosen: used only for the job-row component's states.
    rp = os.path.join(MOCKS, '7.2-rows.html')
    with open(rp, 'w', encoding='utf-8') as f:
        f.write(M.atlas_page('jobs', W.jobs_page(selected=None, fold=('Knowledge Islands', 'Humans Not Robots')), standing=('look', '1 needs a look')))
    shots.append(dict(shot='7.2-rows', html=os.path.abspath(rp), width=1440, hidden=True))
    # The preferred Work and Guilds pages in light, for comparison (night is the reference).
    for ab_id, fn in (('7.1a', W.ab_roadmap), ('7.2a', W.ab_jobs), ('8.1a', W.ab_guilds)):
        lp = os.path.join(MOCKS, f'{ab_id}-light.html')
        with open(lp, 'w', encoding='utf-8') as f:
            f.write(fn(theme='light'))
        shots.append(dict(shot=f'{ab_id}-light', html=os.path.abspath(lp), width=1440, hidden=True))
    # 0.4a and 9.1a in light; Home with nothing to look at (a component state only).
    for ab_id, fn in (('0.4a', lambda: M.atlas_page('lands', M.atlas_home('Known Lands'), mark_shell=True, theme='light',
                                                     tabs=[('Known Lands', True, True), ('Home', False, True), ('Roadmap', False, True)])),
                      ('9.1a', lambda: H.ab_home(theme='light')),
                      ('9.1-none', lambda: M.atlas_page('home', H.home_page(needs=[]), height=None))):
        lp = os.path.join(MOCKS, f'{ab_id}-light.html' if ab_id != '9.1-none' else '9.1-none.html')
        with open(lp, 'w', encoding='utf-8') as f:
            f.write(fn())
        shots.append(dict(shot=f'{ab_id}-light' if ab_id != '9.1-none' else ab_id, html=os.path.abspath(lp), width=1440, hidden=True))
    components = [dict(id=c['id'], selector=c['selector'], states=c['states']) for c in COMPONENTS]
    plan = dict(pages=PAGES, artboards=[{k: v for k, v in ab.items() if k != 'make'} for ab in ARTBOARDS],
                components=components, shots=shots)
    with open(os.path.join(HERE, 'plan.json'), 'w', encoding='utf-8') as f:
        json.dump(plan, f, indent=2, ensure_ascii=False)
    print(f'{len(shots)} mock-ups, {len(COMPONENTS)} components')


if __name__ == '__main__':
    main()
