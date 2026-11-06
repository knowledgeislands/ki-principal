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
| [0.1](0.1.html) | Shell: the window and its rail | 0.1a expanded, 0.1b contracted, 0.1c terra not heard from; components 0.1.1 to 0.1.4 |
| [0.2](0.2.html) | Shell: the tray | 0.2a all well, 0.2b one problem, 0.2c a Mac missing; components 0.2.1 to 0.2.3 |
| [1](1.html) | Home | 1f The working map ★ (1g Everything, 1h closer on one territory), 1a The map of territories (1d sol's plane, 1e terra's plane), 1b The councils, 1c The two squares; components 1.1 to 1.3 |
| [2.1](2.1.html) | Who's doing what | 2.1a By Mac ★, 2.1b By focus: the address book |
| [2.2](2.2.html) | An agent | 2.2a ki.prj.agora ★ |
| [3.1](3.1.html) | What's being said | 3.1a One record, newest first ★, 3.1b By layer |
| [3.2](3.2.html) | Broadcasts | 3.2a Sent and heard ★ |
| [4.1](4.1.html) | Waits on you | 4.1a By agent ★, 4.1b Oldest first |
| [5.1](5.1.html) | Macs and the portal | 5.1a The two Macs and the portal ★ |
| [5.2](5.2.html) | Checkouts | 5.2a Not level, side by side ★ |
| [6](6.html) | A document in a tab | 6a ki.prj.agora · messages.md ★ |

Each page opens with a note on what it is for and why it matters, then the fields the view shows. Where there are alternatives, each states what it gains and what it costs. The preferred one is outlined in brass, with its reason. Region boxes carry codes to quote, such as "1a P2" or "0.1b N4": `N` marks the rail, `T` the tray and `P` page content. A tick hides the boxes. `board.json` holds every artboard's size and coded regions.

## How it is built

Mock-ups, not screenshots of a running app: the app is not built yet. The annotated-board shape is kept so the same codes carry over once it is.

- `build/plan.py` holds the pages, notes, fields, artboards and trade-offs, and writes the mock-up HTML into `mocks/`.
- `build/map_view.py` draws the map of territories on home.
- `build/mocks.py` draws each view in the Instrument dialect of `ki-design`: tokens only, system type, tables not cards, night first.
- `build/data.py` holds the illustrative data.
- `build/shoot.js` takes each screenshot and measures each `data-region` with Playwright.
- `build/board.py` writes the pages.

To rebuild: `python3 build/plan.py && node build/shoot.js build/plan.json shots && python3 build/board.py`.

## Choices

- **The shell is a rail with the portal at its foot.** The portal line (`sol ⇄ terra · portal open`) answers "are both Macs here?" on every page. Speak to everyone sits on the rail too, so Broadcast, Away, Ping and Mark all are always one click away, as in the tray.
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
- **Tabs** (0.1.5, page 6) let pages and documents open inside the app beside the map, as Orca and Claude Code do.
- **Views follow the five goals.** Who's doing what and an agent (goal 3); what's being said and broadcasts (goals 1 and 4); waits on you (Kris's decisions); Macs and the portal, and checkouts (goal 2). The tray covers goal 5.
- **The two layers are named everywhere** as Git and Agora, so Kris can see what was written to the record and what was only said.
- **Later** shows Inbox (from the KIV) and Insight (from the Observatory) in the rail, greyed, so the app's growth has a place without a view yet.
- **One brass action per view**, only where Kris must act: open an agent's queries.

## Open

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
12. **The watchmen and the counts elsewhere.** Home now counts 12 agents (sol 5, terra 7). The rail, Who's doing what and the other pages still count 10, because the roster in `build/data.py` has no watchman yet. Adding them there is the next step once 11 is settled.
13. **What "active" means.** The working map calls an island active when a worker on the plane is there. Should queued work or waiting messages alone make an island active, so Focused never hides an island where work is piling up?
14. **Where the counts come from.** Queued work and waiting messages per island are placeholders. Waiting messages could be lines in each package's `messages.md` not yet acknowledged; queued work could be its open work items. `ki agent status` or `/v1/state` would need to say which.
15. **Principal portals and the planar portal.** Threads run from ki-portal to Personal's principal portal only. Should every principal portal have its own thread to the planar portal, since that is how talk leaves a plane?
16. **Zoom in a real map.** The zoomed board frames one territory and dims the others. A free pan and zoom, a territory jump (double-click its name), or both?
