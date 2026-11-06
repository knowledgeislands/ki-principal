---
title: Agora Atlas information architecture
status: proposed
updated: 2026-11-06
owner: ki.prj.agora
author: Claude Design (information architect)
---

# Agora Atlas information architecture

The names: **Agora Atlas** is the desktop app (this pack), **Agora Beacon** the menu-bar tray on each Mac (page 0.2), and **Agora Lantern** the iPhone app (its own pack, `lantern/`). The shell is page [0.4](0.4.html) (0.4a ★), after Kris's review of 22:55 to 23:20 GMT. 0.3's sidebar is superseded by 0.4; 0.3's toolbar, tabs, context control, tray and bottom pane still stand. 0.1's rail is superseded.

## The sidebar

Home is not in the sidebar: it is reached by clicking the **Agora Atlas logo** in the toolbar, as on a website. The logo is underlined while Home is open and says "Home" on hover (0.4c). Every place sits in a **section**, and every section has an **eyebrow**.

| Section | Eyebrow (folded to icons) | Place | What it is for |
| --- | --- | --- | --- |
| (the logo) | | Home | What needs a look, who holds what, and roles yours to approve (9.1) |
| Agora | AGO | Who's doing what | Every agent on both Macs, its focus, whether it listens (2.1, 2.2) |
| | | What's being said | Everything said between agents and to Kris, both layers, newest first (3.1) |
| | | Broadcasts | What Kris said to everyone and who heard it (3.2) |
| | | Waits on you | Every query only Kris can answer (4.1) |
| | | Macs and the portal | The rigs, the portal between them and what crossed it (5.1) |
| | | Checkouts | Every kept checkout not level, side by side (5.2) |
| Work | WRK | Known Lands | The map of territories, islands and workers; where work is and what waits (1; it was Home) |
| | | Roadmap | Every work record on the lands, filtered by summary counts and chips (7.1) |
| | | Jobs | Every scheduled job and service, by territory and repository (7.2) |
| | | Art gallery · later | The illustrator's islands and each island's artefacts (13) |
| Guilds | GLD | Guilds | The guilds and their skills, and a skill's documents (8.1, 8.2) |
| Observatory | OBS | Repositories, Activity | The Observatory's instruments, embedded (12.1, 12.2) |
| KIV · soon | KIV | Captured, Context, Curated, Actions, Graph atlas, Tending, Key | The KIV's areas and tools (10.1 to 10.7) |
| System | SYS | Accounts, Settings, Updates | Each Mac's accounts, Agora's settings, this build (11.1 to 11.3); at the foot |
| Foot, below SYS | | The portal line | sol ⇄ terra, open or not, when last heard; Beacon on this Mac; Lantern when last heard |

- **Eyebrows** are 9.5-point capitals with a fold chevron. Every section folds, SYS included; the active place's section always opens; the choice is remembered. A folded section shows its count of places and, edged in gold with words, how many inside want a look ("1 to look at"), so a fold never hides a count.
- **Folded to icons** (⌘\\), each section keeps a three-letter eyebrow: AGO, WRK, GLD, OBS, KIV, SYS. A folded section there is a dashed box with its letters and a chevron (0.4b). A count becomes a small badge on its icon.
- A **count** sits beside a place only when something waits or wants a look (Waits on you 34, Checkouts 1, Jobs 1 failed, Accounts 1 to act on). Never a plain total.
- **Known Lands'** glyph is an old chart rolled at its left edge with a dotted path to an X, so it reads as a map, not as a graph.
- **Art gallery** has no section of Kris's six, so it sits in Work, muted and marked later (an open question in the README).

## The shell rules

The window, top to bottom: **toolbar** (N1), then the **tab strip** (N4) with the **context control** (C1) at its right, then the **page** (P), with the **bottom pane** (B1) under it and the **right tray** (T1) beside both.

- **Toolbar.** Agora Atlas, the rigs, one word on the whole (All well, 1 needs a look, Beacon not answering), the search, Mark all, Away…, Broadcast…, the time, pin and theme. The same on every page. No brass here: the one brass action belongs to the page.
- **Tabs.** A sidebar click replaces the current tab; ⌘-click or a document opens a new one. A tab keeps its own selection, tray and pane.
- **Context control.** The territory (a menu: All territories, then each territory, ⌘1 to ⌘4) and the plane (sol, terra, Both). It belongs to the window, so every tab and page shares it. A page that reads it shows it as its first chip ("Territory: Knowledge Islands · from the context"), so a filter is never hidden. A dimension the page ignores is greyed, never removed, so the control does not move. Known Lands' plane switch moves here; Focused and Everything stay on Known Lands' own toolbar.
- **Right tray.** The facts of **one selected thing**: a record, a job, an island, a worker, an account. It opens when a row or mark is chosen, 360 points wide, and pushes the page narrower rather than covering it. Header: what it is and where (small capitals), then its name, then ×. Body: a key-value table, then short sections. Foot: at most three actions, at most one brass, and only when Kris must act. Closes with × or Escape; choosing another thing replaces it.
- **Bottom pane.** The selected thing's **documents or long readings**, in tabs: a skill's files, a job's runs and log, later a record's full text. It opens on an explicit choice (a skill, Show runs), never on a plain selection, under the page and left of the tray, about 40 % of the height; drag its top edge to resize. Closes with × or Escape (Escape closes the tray first).
- **Which one.** Facts that fit in 360 points go in the tray. Anything to read at length, or with several files, goes in the bottom pane. A page may use both at once (0.3d).
- **Page.** The page owns its header (P1: title, one summary line, its tools at the right) and its content (P2 onwards). Tables, not cards.
- **Lists: the summary-filter bar** (7.1.1, settled with Roadmap and Jobs). A list page puts one bar under its header: a row of **tallies**, each a count that is also its filter (a click keeps only that value, ⌘-click adds one, All clears), then one row of **chips**, a single **Filter** menu, **words to find** and **Group**. The tallies count what the other filters keep. A tally edged in gold wants a look (awaiting review, failed, findings); the edge is never the only sign, the mark and word say it too. Values hidden by default (done and cancelled) are one tally of their own, marked hidden. Guilds uses the same idea in another shape: its badges are its tallies.
- **The context as a chip.** The context shows as one dashed chip, first, marked "context" (Territory Knowledge Islands; All territories · both planes). It is removed only at the context control, and a field the context sets is not offered again in the Filter menu.
- **Groups fold.** A group heading carries its count and what inside wants a look (2 jobs · 1 failed) and folds to that one line; a long group shows its first rows and "Show 20 more". So every heading fits one window, and a scroll is a choice.
- **Bottom pane without the tray.** When the chosen thing is mostly documents (a skill), the pane opens on the choice alone and the tray stays shut; the thing's facts (its front matter, where it lives) head the pane's first tab. A thing with facts and readings (a job) opens the tray first, and the pane from the tray's own action, shown pressed while the pane is open (Show runs).

## Page numbering

Pages keep the sidebar's order where they can. Two changes this round, said plainly: **Home is now 9.1** (reached from the logo, not the sidebar), and page **1 is Known Lands**, the map that was Home. To make room for 9.1, **the Observatory moves from 9.1 and 9.2 to 12.1 and 12.2**, and **the Art gallery moves from 12 to 13**. Nothing else is renumbered: the KIV keeps 10.1 to 10.7 and SYS keeps 11.1 to 11.3. Old references to "9.1 Repositories" or "12 Art gallery" mean 12.1 and 13.

| Number | Page | Status |
| --- | --- | --- |
| 0.1 | Shell: the window and its rail | superseded by 0.3 |
| 0.2 | Shell: the tray (Agora Beacon) | kept |
| 0.3 | Atlas shell | its sidebar superseded by 0.4; boards kept |
| 0.4 | Atlas shell, revised | this round (0.4a ★) |
| 1 | Known Lands (was Home) | kept, renamed |
| 2.1, 2.2 | Who's doing what, an agent | kept |
| 3.1, 3.2 | What's being said, Broadcasts | kept |
| 4.1 | Waits on you | kept |
| 5.1, 5.2 | Macs and the portal, Checkouts | kept |
| 6 | A document in a tab | kept |
| 7.1 | Roadmap | 7.1a ★ |
| 7.2 | Jobs | 7.2a ★ |
| 8.1 | Guilds | 8.1a ★ |
| 8.2 | Guilds, revised | this round, another designer (`build/guilds2.py`) |
| 9.1 | Home: who holds what | this round (9.1a ★) |
| 10.1 to 10.7 | KIV: Captured, Context, Curated, Actions, Graph atlas, Tending, Key | later |
| 11.1, 11.2, 11.3 | SYS: Accounts, Settings, Updates | later |
| 12.1, 12.2 | Observatory: Repositories, Activity (were 9.1, 9.2) | later |
| 13 | Art gallery (was 12) | later |

Artboards are lettered within a page (7.1a, 7.1b); components are numbered (7.1.1). Lantern keeps its own numbering in `lantern/`.

## The shell function

Every new page's artboards call one function in `build/mocks.py`:

```python
atlas_page(active, content, tray=None, bottom=None, context=None, tabs=None, folded=False,
           collapsed=('kiv',), mark_shell=False, theme='night', standing=('ok', 'All well'),
           variant='sidebar', title='Agora Atlas', height=900, shell='0.4', logo=None) -> str   # a whole HTML document
```

- `active`: the place id: `home` (the logo; no sidebar place is lit), `here`, `said`, `broadcasts`, `waits`, `macs`, `checkouts`, `lands` (Known Lands), `roadmap`, `jobs`, `gallery`, `guilds`, `repositories`, `activity`, `kiv-captured` … `kiv-key`, `accounts`, `settings`, `updates`.
- `shell`: `'0.4'` by default, the revised sidebar (`ATLAS_SECTIONS4`, `atlas_sidebar4`). `'0.3'` draws the superseded sidebar and is used only by 0.3's own boards. Every other page, including 1 to 6 through `page()`, now draws 0.4.
- `collapsed`: section ids folded to their eyebrow: `agora`, `work`, `guilds`, `observatory`, `kiv`, `sys`. The section holding `active` always opens.
- `logo`: `None`, or `'hover'` to draw the logo's "Home" tooltip.
- `height`: `None` lets a long page grow past 900 points instead of clipping (9.1 uses it).
- `content`: the page's HTML. Start with `head('P1', title, summary, tools)` and mark your own regions with `R('P2', 'Label')`.
- `tray`: `tray_frame(kind, title, body, actions=(), code='T1')`, where `actions` are `('', words)` or `('brass', words)`.
- `bottom`: `bottom_frame(kind, title, tabs, body, code='B1', height=360)`, where `tabs` are `(words, on)`.
- `context`: `dict(territory='All territories', plane='both', open=False)`. What each page reads is in `ATLAS_CONTEXT`; add your page there.
- `tabs`: `[(words, on, closable)]`; by default the active place alone.
- `standing`: the toolbar's word, `('ok' | 'look' | 'bad', words)`.
- `mark_shell`: leave it off on view pages, so only P, T and B are boxed; 0.3 and 0.4 turn it on (0.4 also marks the logo as N5).

In `plan.py`, give the artboard `zones=['page', 'tray', 'bottom']` (as it uses them) and `make=lambda: M.atlas_page('roadmap', M.my_page(), tray=M.my_tray())`.

Home (9.1) lives in `build/home.py`. Roadmap, Jobs and Guilds live in `build/work.py`, which 0.3a, 0.3b, 0.3d and 0.3e now draw too. A list page builds its bar with `sf_bar(tallies, chips, find, group, menu='')`, from `tally(key, n, words, on=False, attn=False)`, `ctx_chip(field, value)`, `chosen_chip(field, value)`, `filter_button(open_, n)`, `find_box(words, hint)` and `group_seg(options, on)`; `group_row` and `more_row` draw a group heading and its fold. The old placeholders in `mocks.py` (`atlas_roadmap`, `atlas_jobs`, `atlas_guilds` and their trays) are no longer drawn.
