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
| [1](1.html) | Home | 1a The map of territories ★ (1d sol's plane, 1e terra's plane), 1b The councils, 1c The two squares |
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
- **Home is one map of territories** (1a), after Kris's vision (MSG-62774774). It fits one window with no scrolling.
  - Each territory is a faint boundary, and its islands (repositories) are hexes in the flat chart's manner.
  - Each island has a meeting point, the ring, lit when someone there listens.
  - Work packages and doers are placed where they work. Each carries its primary focus and its rig. Rigs are planes over the same islands (MSG-c027252f), so a switch shows sol's plane, terra's, or both.
  - Each territory's council is ringed.
  - Gold threads run up to the councils and across between them. The great portal leaves the dotfiles island, where the households keep it.
  - The key and Show as a list give the text equivalent.
  - 1b draws the same hierarchy as columns. 1c keeps the earlier host-centred two squares.
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
9. **Dropped from home:** the figures-and-table view and the stream of what is being said. Both are listed in `index.md` as dropped.
10. **Placeholders.** Times, traffic and most focus areas and queries are invented; the live roster and the read endpoint (`/v1/state`) replace them.
