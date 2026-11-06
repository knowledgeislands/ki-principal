---
title: Agora app design pack
status: proposed
updated: 2026-11-06
owner: ki.prj.agora
author: Claude Design (information architect)
---

# Agora app design pack

The rich Electron app beside the tray, as DESIGN-PACK (MSG-9f90977f, Kris about 05:40 GMT) asks. The tray process on each Mac is the Agora portal. The app first shows what is happening within each Agora and across them; later it takes in the KIV's inbox and the Observatory's insight.

Open [index.html](index.html). It has one page per part, in the app's own order, laid out after the `ki-design-system` annotated board:

| Page | Part | Artboards (preferred marked ★) |
| --- | --- | --- |
| [0.1](0.1.html) | Shell: the window and its rail (superseded by 0.3) | 0.1a expanded, 0.1b contracted, 0.1c terra not heard from, all dropped; components 0.1.1 to 0.1.5 |
| [0.2](0.2.html) | Shell: the tray (Agora Beacon) | 0.2a all well, 0.2b one problem, 0.2c a Mac missing; components 0.2.1 to 0.2.3 |
| [0.3](0.3.html) | Atlas shell (sidebar superseded by 0.4) | 0.3a Grouped sidebar ★ (0.3b Guilds with the bottom pane, 0.3c folded with the territory menu, 0.3d tray and bottom pane together), 0.3e Sections across the top; components 0.3.1 to 0.3.6 |
| [0.4](0.4.html) | Atlas shell, revised | 0.4a Sidebar in sections, Known Lands under Work ★ (0.4b folded to icons with three-letter eyebrows, 0.4c the logo hovered: "Home"); 0.4a in light; components 0.4.1 to 0.4.3 |
| [0.5](0.5.html) | Atlas bar, compact | 0.5a Compact bar ★ (0.5b one rig, nothing to look at; 0.5c ten rigs, presence open over a pinned tray, urgent; 0.5d ten rigs, the indicator leading to Home), 0.5e the 0.4 toolbar for comparison; 0.5a in light; components 0.5.1 to 0.5.4 |
| [1](1.html) | Known Lands (was Home) | 1f The working map ★ (1g Everything, 1h closer on one territory), 1a The map of territories (1d sol's plane, 1e terra's plane), 1b The councils, 1c The two squares; components 1.1 to 1.3 |
| [2.1](2.1.html) | Who's doing what | 2.1a By Mac ★, 2.1b By focus: the address book |
| [2.2](2.2.html) | An agent | 2.2a ki.prj.agora ★ |
| [3.1](3.1.html) | What's being said | 3.1a One record, newest first ★, 3.1b By layer |
| [3.2](3.2.html) | Broadcasts | 3.2a Sent and heard ★ |
| [4.1](4.1.html) | Waits on you | 4.1a By agent ★, 4.1b Oldest first |
| [5.1](5.1.html) | Macs and the portal | 5.1a The two Macs and the portal ★ |
| [5.2](5.2.html) | Checkouts | 5.2a Not level, side by side ★ |
| [6](6.html) | A document in a tab | 6a ki.prj.agora · messages.md ★ |
| [7.1](7.1.html) | Roadmap | 7.1a Tallies over a grouped table ★ (7.1c a filter applied, 7.1d a record awaiting review, 7.1e nothing matching), 7.1b The summary beside the table; 7.1a in light; components 7.1.1 to 7.1.4 |
| [7.2](7.2.html) | Jobs | 7.2a By territory and repository ★ (7.2c Failed and Findings chosen, 7.2d a service in the tray), 7.2b Each Mac a column; 7.2a in light; components 7.2.1 to 7.2.3 |
| [8.1](8.1.html) | Guilds | 8.1a Badges across, the guild's skills beneath ★ (8.1c no skill chosen, 8.1d Humans Not Robots, 8.1e a folder tab), 8.1b Guild columns across; 8.1a in light; components 8.1.1 to 8.1.3 |
| [9.1](9.1.html) | Home: who holds what | 9.1a One table by tier ★ (9.1c a row in the tray), 9.1b Grouped by rig; 9.1a in light; components 9.1.1 to 9.1.4 |

Each page opens with a note on what it is for and why it matters, then the fields the view shows. Where there are alternatives, each states what it gains and what it costs. The preferred one is outlined in brass, with its reason. Region boxes carry codes to quote, such as "1a P2" or "0.1b N4": `N` marks the rail, `T` the tray and `P` page content. A tick hides the boxes. `board.json` holds every artboard's size and coded regions.

[IA.md](IA.md) holds the information architecture: the sidebar tree, the shell rules for the tray, the bottom pane and the context control, the page numbers for the pages still to come, and the shell function the next designers call.

## How it is built

Mock-ups, not screenshots of a running app: the app is not built yet. The annotated-board shape is kept so the same codes carry over once it is.

- `build/plan.py` holds the pages, notes, fields, artboards and trade-offs, and writes the mock-up HTML into `mocks/`.
- `build/map_view.py` draws the map of territories on home.
- `build/home.py` draws Home, who holds what (9.1).
- `build/work.py` draws Roadmap, Jobs and Guilds (7.1, 7.2, 8.1) and the summary-filter bar they share, for the data the built app reads (`src/app/roadmap.ts`, `jobs.ts`, `guilds.ts` in apps-agora.local).
- `build/mocks.py` draws each view in the Instrument dialect of `ki-design`: tokens only, system type, tables not cards, night first. `atlas_page(active, content, tray=None, bottom=None, context=None, …)` draws the Atlas shell around any page, with `tray_frame` and `bottom_frame` for the tray and the pane (IA.md).
- `build/data.py` holds the illustrative data.
- `build/shoot.js` takes each screenshot and measures each `data-region` with Playwright.
- `build/board.py` writes the pages.

To rebuild: `python3 build/plan.py && node build/shoot.js build/plan.json shots && python3 build/board.py`.

## Choices

- **The sidebar is revised** (0.4a ★, Kris's review 22:55 to 23:20 GMT). Home leaves the sidebar and is the Agora Atlas logo, as on a website; the logo says "Home" on hover and is underlined while Home is open. The map that was Home is **Known Lands**, under Work, with an old chart for its glyph (a rolled chart, a dotted path, an X). Every place sits in a section with a smaller eyebrow (AGO, WRK, GLD, OBS, KIV, SYS when folded to icons); every section folds, and a folded one still says how many inside want a look. Accounts, Settings and Updates form SYS at the foot. Every page in the pack now draws this sidebar, pages 1 to 6 included; only 0.1's and 0.3's own boards keep theirs, for the record.
- **The bar is compact** (0.5a ★, Kris's review 23:05 GMT): one 36-point row on every page. The rigs are one **presence** control when more than three, its mark the worst rig's state with words ("10 rigs · 1 gone · 1 unheard"), opening the list; up to three show as chips. Every count in the bar is now one **notification indicator**, a bell with the worst state's mark and words ("Nothing", "3 to look at", "4 · 1 urgent"), leading to Home's **Needs a look**. **At a glance** is gone; its contents are on Home. Mark all, Away… and Broadcast… are icon buttons, and every control has a tooltip in words. The alternative kept for comparison is the 0.4 toolbar (0.5e).
- **Pinned and floating** (0.5c, IA.md): the right tray pins (opens on a choice, pushes the page, stays until × or Escape); a pop-out floats (opens from its control, covers without pushing, closes on Escape, a click outside, a choice or its control; one at a time; no brass). Escape closes a pop-out, then the tray, then the bottom pane.
- **Home is who holds what** (9.1a ★). Needs a look comes first, each item saying what it is and what to do; then one table, one row per live package and doer, ordered Leader, Manager, Doer: Role with Kris's emoji and its word, Tier, Package, Rig, Focus areas on one line (⭐ and bold the primary, ⏰ scheduled), State as an emoji and a word (🤖 Working, 👤 With you, 💤 Idle, 🔕 Silent). Where a package's record disagrees with the guild catalogue, a † ‡ § in the disagreeing cell points to a footnote under the table, and the row shows the catalogue. **Yours to approve** lists the catalogue's roles nobody holds yet, with the one brass action for the section (Approve all 3…) and a plain Approve… per row. Choosing a row opens it in the tray with its record beside the catalogue (9.1c). The alternative, **grouped by rig** (9.1b), shows what each rig carries but splits the governors across groups.
- **The app is Agora Atlas** (0.3). The tray is Agora Beacon and the iPhone app Agora Lantern; the shell names both at the sidebar's foot.
- **The shell is a grouped sidebar under one toolbar** (0.3a ★, its sidebar now superseded by 0.4a), replacing 0.1's rail. Groups follow what a place is about: Agora, Work, Guilds, Observatory, KIV (folded while it is coming), Coming; Accounts, Settings and Updates sit at the foot with the portal line. Speak to everyone moves from the rail to the toolbar, as the built app already has it.
  - **Context** (territory and plane) has one place, at the right of the tab strip, shared by every page; a page that ignores a dimension greys it. Home's plane switch moves there.
  - **The right tray** holds one selected thing's facts and pushes the page; **the bottom pane** holds its documents and long readings, in tabs. Both open the same way on every page (IA.md).
  - The alternative, **sections across the top** (0.3e), keeps the sidebar short but costs two clicks between sections and hides the foot behind a gear.
- **The shell was a rail with the portal at its foot** (0.1, superseded by 0.3). The portal line (`sol ⇄ terra · portal open`) answers "are both Macs here?" on every page. Speak to everyone sits on the rail too, so Broadcast, Away, Ping and Mark all are always one click away, as in the tray.
- **Home is one map of territories**, after Kris's vision (MSG-62774774). It fits one window with no scrolling.
  - Each territory is a faint boundary, and its islands (repositories) are hexes in the flat chart's manner.
  - Each island has its **island portal** on its summit, the ring, lit when someone there listens. A principal island's is larger: the **principal portal**, which liaises across territories within one plane (Kris's names, MSG-cccabc3c and MSG-1953e5db).
  - The **planar portal**, which joins the planes, is its own island: **ki-portal**, in Personal, ringed in gold. The **watchman** keeps it, one on each rig, beside the housekeeper (the household, on dotfiles) and the assistant (on inbox). Its thick gold thread leaves the map's edge for the other plane.
  - Work packages and doers are placed where they work. Each carries its primary focus and its rig. Rigs are planes over the same islands (MSG-c027252f), so a switch shows sol's plane, terra's, or both.
  - Each territory's council is ringed.
  - Gold threads run from each island portal up to the principal portal and across between principal portals.
- **The preferred home is the working map** (1f ★). It keeps the picture and makes it the place to act from.
  - A **toolbar** above the map holds Show (Focused or Everything), Plane (sol, terra, both), Zoom (out, the level, in, Fit) and Show as a list.
  - **Active islands** (a worker on the plane is there) are land; **quiet islands** are outlines. **Focused** hides the quiet ones and keeps what touches the active: their threads and principal portals. A line in the corner says how many are hidden and what is queued and waiting among them, so nothing is lost silently.
  - Each island carries two small counts beside its name: **queued work** (a stack) and **waiting messages** (an envelope). Zero is left out. Shape and word carry the meaning, not colour.
  - **Clicking an island** edges it in the accent and opens its detail in the **right tray**: where it is, its portal, checkouts, who works there, queued work, waiting messages and what waits on Kris. The one brass action is there only when something waits on Kris (Open its 10 queries); ki-portal has none. With nothing selected, the tray shows At a glance and the full key (component 1.3).
  - **Zoom** frames one territory (1h, 155 %). Labels stay at reading size while the land grows, so zooming makes room rather than bigger type, and each worker gains when it last answered; counts gain their words. An overview in the corner shows where the view sits; dragging its frame pans. At Fit, a line says drag to pan.
  - The key is a strip under the map, so the tray is free for detail.
  - 1g shows Everything with the planar portal's island selected. 1a keeps the plain map with the key beside it; 1d and 1e are its planes. 1b draws the same hierarchy as columns. 1c keeps the earlier host-centred two squares.
  - Codes were kept, not re-lettered, so comments on 1a to 1e still point to the same boards; the new boards take 1f to 1h, and the preferred is marked ★ where it sits, first on the page.
- **Roadmap is tallies over a grouped table** (7.1a ★). One row of counts, one per open status, sits across the top, and each count is the filter it names; chips under it say every filter in force, the context's territory first; one Filter menu holds priority, horizon, area, size, island, kind and assignee with their counts; words find; Group chooses status, island, area or none. The table keeps the built app's columns (record, title, island, status, priority and size, updated). Awaiting review carries the gold edge, since a review is Kris's to give, and is the only record whose tray has a brass action (Open to review, 7.1d). Done and cancelled are one tally, hidden until chosen, which replaces the built app's checkbox. The alternative, the built app's own **summary beside the table** (7.1b), answers island against status in one cell but costs 330 points of table.
  - **The record's tray** holds its front matter, Blocked by and Blocks (each a link), its Goal and the first lines of its Context, and Open the file, Read in full (the whole record in the bottom pane) and Show on Home.
  - **Status marks**: in progress solid, awaiting review a gold diamond, ready a ring, draft a dashed ring, triage a square; each always with its word.
- **Jobs uses the same bar** (7.2a ★): tallies for Failed, Findings, OK, No run yet, Off and Services, with Failed and Findings edged in gold; the context as one chip (All territories · both planes); Group by repository, Mac or none. Rows are grouped by territory and then repository, as Kris asked; a territory heading folds to one line that still says what is wrong inside it. Each Mac that runs a job is a chip marked by how its last run there ended. The next run is worked out from the schedule.
  - **The job's tray** holds its standing and purpose, Rig's declaration and each Mac's last ten runs as marks with the last one's line; **Show runs** opens the **run history in the bottom pane**, newest first across both Macs, with a Declaration tab. There is no Log tab: Agora never reads a job's output, environment or arguments.
  - No brass on Jobs: Agora only shows jobs, and a failed one is fixed in Rig or the tool it runs.
  - The alternative, **each Mac a column** (7.2b), lines up what ran where, but most jobs run on one Mac, so half its cells say not selected.
- **Guilds are badges across, the chosen guild's skills beneath** (8.1a ★). Each guild is a shield badge with its monogram on its own colour (its logo once the catalogue gives one), its name and its count; All guilds comes first. Choosing a badge shows that guild's about line and its skills as sub-badges, each carrying its guild's small shield; choosing a skill opens it in the bottom pane, with SKILL.md (front matter at the left, instructions drawn at the right), each other document and each folder as tabs. All guilds shows the ledger, one guild a row (8.1c). The territory is the context's (8.1d). The alternative, **guild columns across** (8.1b), is the built app's panels: closest to Kris's words, but only four of eight fit and long guilds are cut.
- **Shell rules settled this round** (IA.md): the summary-filter bar for list pages, the context as one chip, groups that fold, and the bottom pane opening alone for a thing that is mostly documents.
- **Tabs** (0.1.5, page 6) let pages and documents open inside the app beside the map, as Orca and Claude Code do.
- **Views follow the five goals.** Who's doing what and an agent (goal 3); what's being said and broadcasts (goals 1 and 4); waits on you (Kris's decisions); Macs and the portal, and checkouts (goal 2). The tray covers goal 5.
- **The two layers are named everywhere** as Git and Agora, so Kris can see what was written to the record and what was only said.
- **Later** shows Inbox (from the KIV) and Insight (from the Observatory) in the rail, greyed, so the app's growth has a place without a view yet.
- **One brass action per view**, only where Kris must act: open an agent's queries.

## Open

0. **This round's questions** (0.4 and 9.1):
   - **Art gallery's section.** Kris's six sections have no place for it; it sits in Work, muted, marked later. GLD or a seventh section are the other choices.
   - **Guilds under a GLD eyebrow** repeats its own name over one place. Keep it for the rule's sake, or let a lone place drop its eyebrow when open (but keep GLD folded to icons)?
   - **Roles for project packages.** The six roles have none for a project such as hnr.prj.5g-emerge-p2ms3, so those rows say "No role". Does the catalogue have one (a Steward?), or is "no role" right?
   - **The roles and tiers in 9.1 are illustrative.** The pack mapped inbox-sol to Personal's Governor, inbox-terra to no role, the watchmen to Warden and the households to Housekeeper; the catalogue and each work.md should replace them, and the footnotes are examples of the disagreements Home would show.
   - **The emoji** render in Noto Color Emoji here and Apple Color Emoji on the Mac; their colour is decoration, and each sits beside its word, so the rule that colour never carries meaning alone still holds.
   - **"With you"** is drawn as Kris being in a session with the package. Agora would need `ki agent status` to say so.
   - **Three rigs as chips.** The pack folds presence into one control above three rigs at 1440 points. A narrower window should fold sooner; the built bar can measure the room rather than count.
   - **Icon-only speak buttons.** Mark all, Away… and Broadcast… lose their words in the compact bar. If Away… is used often, it could keep its word.
   - **What counts in the indicator.** The pack counts Home's Needs a look items (silent packages, checkouts that must settle, failed jobs, queries). Whether queries belong there, or only in the sidebar's Waits on you, is Kris's call.
   - **Numbering.** Home took 9.1, so the Observatory moved to 12.1 and 12.2 and the Art gallery to 13 (IA.md).

1. **The app and C12.** The specification keeps Agora to small windows. A rich app beside the tray reverses that; the decision to stay on Electron names "the settings screen or a KIV/Agora window grows into a large always-open view" as a trigger to check GPUI first.
2. **Where queries come from.** The pack counts `###` headings in each `discussions.md`; personal.reg.inbox-sol's method may name the true source.
3. **Agent names on the map.** The two squares use short names (`agora`, `ki sop`). A naming rule, such as a short name in each `work.md`, would make them stable.
4. **Doers.** Doers such as this session are shown with the agent that brought them in (2.2a), not as agents of their own.
5. **Personal's council.** Kris named the State of play mains as the councils. Knowledge Islands and Humans Not Robots have one each (ki.sop.main, hnr.sop.main). Personal's is drawn as personal.reg.inbox-sol: is that right?
6. **Gold threads.** Kris asked for threads of golden light. In `ki-design`, gold means attention, so the threads are thin and the only other gold is the one action per view. Keep it, or draw the threads in teal (the conversational layer)?
7. **Placing islands.** The map's islands are placed by hand here. A rule is needed, ideally the Territory Map's hex layout from `ki-design`, so islands stay where Kris learnt them.
8. **The photograph** of Kris's layout has not arrived yet; the map will follow it when it does.
9. **Dropped from home:** the figures-and-table view and the stream of what is being said. Both are listed in `index.md` as dropped. Nothing was dropped in the working-map round: 1a stays as an alternative.
10. **Placeholders.** Times, traffic and most focus areas and queries are invented; the live roster and the read endpoint (`/v1/state`) replace them.
11. **The watchman's work id.** The map names it `personal.reg.watchman-sol` and `-terra`, one per rig like the household and the assistant. Is it one per rig, and is that its id? The repository is drawn as `krisb/ki-portal`; is that where it lives?
12. **The watchmen and the counts elsewhere.** Known Lands now counts 12 agents (sol 5, terra 7). The rail, Who's doing what and the other pages still count 10, because the roster in `build/data.py` has no watchman yet. Adding them there is the next step once 11 is settled.
13. **What "active" means.** The working map calls an island active when a worker on the plane is there. Should queued work or waiting messages alone make an island active, so Focused never hides an island where work is piling up?
14. **Where the counts come from.** Queued work and waiting messages per island are placeholders. Waiting messages could be lines in each package's `messages.md` not yet acknowledged; queued work could be its open work items. `ki agent status` or `/v1/state` would need to say which.
15. **Principal portals and the planar portal.** Threads run from ki-portal to Personal's principal portal only. Should every principal portal have its own thread to the planar portal, since that is how talk leaves a plane?
16. **Zoom in a real map.** The zoomed board frames one territory and dims the others. A free pan and zoom, a territory jump (double-click its name), or both?
17. **Portal or Beacon in the window's words.** The built app says "Portal not answering" for the tray process. With the tray renamed Beacon, the shell says "Beacon on sol" and would say "Beacon not answering", keeping "portal" for the link between the rigs (sol ⇄ terra). Is that the split Kris wants?
18. **Is the context the window's or each tab's?** 0.3 makes it the window's, so switching tabs never surprises. A tab pinned to its own territory is possible later.
19. **KIV places while coming.** The brief calls them coming soon, but the built app already embeds them when the KIV runs. The sidebar shows them muted with "soon" and folds the group; unfold it once they are native views.
20. **What Lantern reports to the shell.** The foot says when Lantern was last heard; that needs the phone's service to say so to Agora.
21. **Owner of a job.** Rig's declaration has no owner. The pack shows the repository a job works in as where it belongs; should a declaration name its owning package (such as `work/hnr.sop.main`), so a failed job can say who to tell?
22. **Next run.** Rig reports no next run; the pack works it out from the calendar or interval. Is that good enough, or should Rig or the reporter state it?
23. **Run history depth.** The pack assumes the reporter keeps 14 days of runs per job. How many does it keep, and should the bottom pane say when the oldest is?
24. **Review as Kris's act.** Awaiting review is edged in gold and given the one brass action (Open to review), on the reading that a review waits on Kris. If reviews are often another agent's, the gold edge should go to the assignee instead.
25. **Folding long groups.** Roadmap folds a group after a few rows so every status heading fits one window. Kris may prefer one long scroll; folding could be remembered per group.
26. **Statuses outside the order.** The built app sorts statuses in-progress, awaiting-review, ready, draft, triage, done, cancelled, and any other after them. A record with another status would need its own tally; the pack assumes none.
27. **Humans Not Robots' skills.** The pack draws an `hnr-agentic-harness` with six unsorted skills; it was not on the lands this pack read. Is there one, and does Personal have its own?
28. **Guild colours.** Each guild's colour is only identity, so it never carries a meaning; with sixteen or more guilds the hues will crowd. The catalogue's logos would replace them.
29. **More than one row of badges.** Eight guilds fit across at 118 points each beside the sidebar. At ten or more, the badges need a second row or a narrower form (shield and name only).
