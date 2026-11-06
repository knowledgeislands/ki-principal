---
title: Agora Atlas information architecture
status: proposed
updated: 2026-11-06
owner: ki.prj.agora
author: Claude Design (information architect)
---

# Agora Atlas information architecture

The names: **Agora Atlas** is the desktop app (this pack), **Agora Beacon** the menu-bar tray on each Mac (page 0.2), and **Agora Lantern** the iPhone app (its own pack, `lantern/`). The shell is page [0.3](0.3.html); 0.3a ★ is the preferred shell, and 0.1's rail is superseded.

## The sidebar

| Group | Place | What it is for |
| --- | --- | --- |
| Agora | Home | The map of territories, islands and workers; where work is and what waits (1) |
| | Who's doing what | Every agent on both Macs, its focus, whether it listens (2.1, 2.2) |
| | What's being said | Everything said between agents and to Kris, both layers, newest first (3.1) |
| | Broadcasts | What Kris said to everyone and who heard it (3.2) |
| | Waits on you | Every query only Kris can answer (4.1) |
| | Macs and the portal | The rigs, the portal between them and what crossed it (5.1) |
| | Checkouts | Every kept checkout not level, side by side (5.2) |
| Work | Roadmap | Every work record on the lands, filtered by summary counts and chips (7.1) |
| | Jobs | Every scheduled job and service, by territory and repository (7.2) |
| (alone) | Guilds | The guilds and their skills, and a skill's documents (8.1) |
| Observatory | Repositories | The Observatory's repository instrument, embedded (9.1) |
| | Activity | The Observatory's activity instrument, embedded (9.2) |
| KIV · soon | Captured, Context, Curated, Actions | The KIV's knowledge areas (10.1 to 10.4) |
| | Graph atlas, Tending, Key | The KIV's tools (10.5 to 10.7) |
| Coming | Art gallery | The illustrator's islands and each island's artefacts (12) |
| Foot | Accounts | Each Mac's Claude and Codex accounts, windows and expiry (11.1) |
| | Settings | Agora's settings on this Mac, read only (11.2) |
| | Updates | This build against its origin (11.3) |
| Foot, below | The portal line | sol ⇄ terra, open or not, when last heard; Beacon on this Mac; Lantern when last heard |

- A **count** sits beside a place only when something waits or wants a look (Waits on you 34, Checkouts 1, Jobs 1 failed, Accounts 1 to act on). Never a plain total.
- A **group folds** to its heading with its count of places. The KIV is folded while it is coming; the active place's group always opens; the choice is remembered.
- **Folded to icons** (⌘\\), every group opens, since 56-point icons fit; a count becomes a small badge.
- A group with one place (Guilds) has no heading, only rules above and below.

## The shell rules

The window, top to bottom: **toolbar** (N1), then the **tab strip** (N4) with the **context control** (C1) at its right, then the **page** (P), with the **bottom pane** (B1) under it and the **right tray** (T1) beside both.

- **Toolbar.** Agora Atlas, the rigs, one word on the whole (All well, 1 needs a look, Beacon not answering), the search, Mark all, Away…, Broadcast…, the time, pin and theme. The same on every page. No brass here: the one brass action belongs to the page.
- **Tabs.** A sidebar click replaces the current tab; ⌘-click or a document opens a new one. A tab keeps its own selection, tray and pane.
- **Context control.** The territory (a menu: All territories, then each territory, ⌘1 to ⌘4) and the plane (sol, terra, Both). It belongs to the window, so every tab and page shares it. A page that reads it shows it as its first chip ("Territory: Knowledge Islands · from the context"), so a filter is never hidden. A dimension the page ignores is greyed, never removed, so the control does not move. Home's plane switch moves here; Focused and Everything stay on Home's own toolbar.
- **Right tray.** The facts of **one selected thing**: a record, a job, an island, a worker, an account. It opens when a row or mark is chosen, 360 points wide, and pushes the page narrower rather than covering it. Header: what it is and where (small capitals), then its name, then ×. Body: a key-value table, then short sections. Foot: at most three actions, at most one brass, and only when Kris must act. Closes with × or Escape; choosing another thing replaces it.
- **Bottom pane.** The selected thing's **documents or long readings**, in tabs: a skill's files, a job's runs and log, later a record's full text. It opens on an explicit choice (a skill, Show runs), never on a plain selection, under the page and left of the tray, about 40 % of the height; drag its top edge to resize. Closes with × or Escape (Escape closes the tray first).
- **Which one.** Facts that fit in 360 points go in the tray. Anything to read at length, or with several files, goes in the bottom pane. A page may use both at once (0.3d).
- **Page.** The page owns its header (P1: title, one summary line, its tools at the right) and its content (P2 onwards). Tables, not cards.
- **Lists: the summary-filter bar** (7.1.1, settled with Roadmap and Jobs). A list page puts one bar under its header: a row of **tallies**, each a count that is also its filter (a click keeps only that value, ⌘-click adds one, All clears), then one row of **chips**, a single **Filter** menu, **words to find** and **Group**. The tallies count what the other filters keep. A tally edged in gold wants a look (awaiting review, failed, findings); the edge is never the only sign, the mark and word say it too. Values hidden by default (done and cancelled) are one tally of their own, marked hidden. Guilds uses the same idea in another shape: its badges are its tallies.
- **The context as a chip.** The context shows as one dashed chip, first, marked "context" (Territory Knowledge Islands; All territories · both planes). It is removed only at the context control, and a field the context sets is not offered again in the Filter menu.
- **Groups fold.** A group heading carries its count and what inside wants a look (2 jobs · 1 failed) and folds to that one line; a long group shows its first rows and "Show 20 more". So every heading fits one window, and a scroll is a choice.
- **Bottom pane without the tray.** When the chosen thing is mostly documents (a skill), the pane opens on the choice alone and the tray stays shut; the thing's facts (its front matter, where it lives) head the pane's first tab. A thing with facts and readings (a job) opens the tray first, and the pane from the tray's own action, shown pressed while the pane is open (Show runs).

## Page numbering

Pages keep the sidebar's order, so the pack reads as the app does.

| Number | Page | Status |
| --- | --- | --- |
| 0.1 | Shell: the window and its rail | superseded by 0.3 |
| 0.2 | Shell: the tray (Agora Beacon) | kept |
| 0.3 | Atlas shell | this round |
| 1 | Home | kept |
| 2.1, 2.2 | Who's doing what, an agent | kept |
| 3.1, 3.2 | What's being said, Broadcasts | kept |
| 4.1 | Waits on you | kept |
| 5.1, 5.2 | Macs and the portal, Checkouts | kept |
| 6 | A document in a tab | kept |
| 7.1 | Roadmap | this round (7.1a ★) |
| 7.2 | Jobs | this round (7.2a ★) |
| 8.1 | Guilds (a skill opens in the bottom pane, so no 8.2 is needed yet) | this round (8.1a ★) |
| 9.1, 9.2 | Observatory: Repositories, Activity | later |
| 10.1 to 10.7 | KIV: Captured, Context, Curated, Actions, Graph atlas, Tending, Key | later |
| 11.1, 11.2, 11.3 | Accounts, Settings, Updates | later |
| 12 | Art gallery | later |

Artboards are lettered within a page (7.1a, 7.1b); components are numbered (7.1.1). Lantern keeps its own numbering in `lantern/`.

## The shell function

Every new page's artboards call one function in `build/mocks.py`:

```python
atlas_page(active, content, tray=None, bottom=None, context=None, tabs=None, folded=False,
           collapsed=('kiv',), mark_shell=False, theme='night', standing=('ok', 'All well'),
           variant='sidebar', title='Agora Atlas', height=900) -> str   # a whole HTML document
```

- `active`: the place id: `home`, `here`, `said`, `broadcasts`, `waits`, `macs`, `checkouts`, `roadmap`, `jobs`, `guilds`, `repositories`, `activity`, `kiv-captured` … `kiv-key`, `gallery`, `accounts`, `settings`, `updates`.
- `content`: the page's HTML. Start with `head('P1', title, summary, tools)` and mark your own regions with `R('P2', 'Label')`.
- `tray`: `tray_frame(kind, title, body, actions=(), code='T1')`, where `actions` are `('', words)` or `('brass', words)`.
- `bottom`: `bottom_frame(kind, title, tabs, body, code='B1', height=360)`, where `tabs` are `(words, on)`.
- `context`: `dict(territory='All territories', plane='both', open=False)`. What each page reads is in `ATLAS_CONTEXT`; add your page there.
- `tabs`: `[(words, on, closable)]`; by default the active place alone.
- `standing`: the toolbar's word, `('ok' | 'look' | 'bad', words)`.
- `mark_shell`: leave it off on view pages, so only P, T and B are boxed; 0.3 turns it on.

In `plan.py`, give the artboard `zones=['page', 'tray', 'bottom']` (as it uses them) and `make=lambda: M.atlas_page('roadmap', M.my_page(), tray=M.my_tray())`.

Roadmap, Jobs and Guilds live in `build/work.py`, which 0.3a, 0.3b, 0.3d and 0.3e now draw too. A list page builds its bar with `sf_bar(tallies, chips, find, group, menu='')`, from `tally(key, n, words, on=False, attn=False)`, `ctx_chip(field, value)`, `chosen_chip(field, value)`, `filter_button(open_, n)`, `find_box(words, hint)` and `group_seg(options, on)`; `group_row` and `more_row` draw a group heading and its fold. The old placeholders in `mocks.py` (`atlas_roadmap`, `atlas_jobs`, `atlas_guilds` and their trays) are no longer drawn.
