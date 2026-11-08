# [Foundations](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Themes/foundations.md) › [Stoa](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/stoa.md) › stoa-capture-draft

**Run report at 12:27 GMT · last mark 12:22 GMT**

---

## Done

- Read all 14 request lines in the brief's range, plus the two newer release reports (STOA-UPSTREAM, STOA-DUOTONE), and checked each against packages-stoa `main` at `9c657a3`, which is Stoa 0.35.0, not 0.33.0 as the brief said.
- Wrote 15 draft records and an index in `/Users/krisbrown/.local/state/ki/agents/ki-prj-stoa/tmp/records/`: 3 defects, 7 small asks and 5 designs. Four lines need no record: STOA-TOOLING item 2 (done in 0.33.0), STOA-HANDOVER, STOA-LEGAL and the two release reports.
- Defects still present at 0.35.0: the Calendar cuts a one-off multi-day event to its first day (`seriesSpan` in `calendar/view.js`); no unit paints its upgraded form first; the Theme Menu's colour pairs are not measured.
- Partly met: the Header's named slots now stay visible when the menu folds, but none sits beside the brand (STOA-HDR-002). The Diagram Viewer has an Explore dialog, but no overlay (STOA-DIAG-001). The gallery became the workbench, and whether it still clips needs a look (STOA-WB-001).
- Checks: all 15 drafts share one frontmatter field set, STOA-CMD-001's fields plus `assignee`, with `baseline_ref: null`. Every inbox line appears in the index. packages-stoa's working tree is clean, and nothing was written to any repository. The read-only roadmap audit was skipped: the drafts sit outside the repository, and the draining steering asked me to finish quickly.
- Steering at 12:22 GMT (the host move, put the drafts in the report): applied. The drafts are carried in full under Findings.

## In Progress

Nothing. The coordinator captures the records. Before it writes them, each new area code needs a line in `.ki.toml` and a reservation in `docs/roadmap/_ISSUES.md` (see STOA-AREAS).

## Findings

### STOA-DRAFTS - draft roadmap records for the Stoa inbox

**Goal:** draft one triage record for each distinct piece of work in the Stoa inbox, for the coordinator to review and capture under STOA-WINDOW.

**Scope:** the `## Inbound` request lines in `ki.prj.stoa/messages.md`, checked against packages-stoa `9c657a3`.

**As of:** 8 November 2026, 12:25 GMT.

| Inbox line | Ask | Draft record | Class | Order |
| ---------- | --- | ------------ | ----- | ----- |
| STOA-LINES (6 Nov) | 1 multi-day event on its first day only | STOA-CAL-001 | small (defect) | 1 |
| STOA-LINES (6 Nov) | 2 no-script first frame causes layout shift | STOA-BASE-001 | small (defect, six units; may split) | 2 |
| STOA-THEME-MENU-CONTRAST (2 Nov) | Theme Menu pairs unmeasured | STOA-THEME-001 | small (defect) | 3 |
| STOA-HEADER (2 Nov) | 1 most-specific current link | STOA-HDR-001 | small | 4 |
| STOA-CANCELLED (1 Nov) | cancelled status | STOA-CAL-002 | small | 5 |
| STOA-ICAL-MAPPING (1 Nov) | 1 omit unknown STATUS; 2 site CATEGORIES | STOA-CAL-003 | small | 6 |
| STOA-ICAL-MAPPING (1 Nov) | 3 rising SEQUENCE | STOA-CAL-004 | small if the site supplies the number, else design | 7 |
| STOA-HEADER (2 Nov) | 2 always-visible slot beside the brand | STOA-HDR-002 | small (partly met: named slots stay in the row) | 8 |
| STOA-TOOLING (2 Nov) | 1 Biome 2.6 Markdown, Syncpack keywords | STOA-TOOL-001 | small (README note; Stoa has no consumer template) | 9 |
| STOA-TOOLING (2 Nov) | 3 gallery clips at narrow widths | STOA-WB-001 | small (may already be met; needs a look) | 10 |
| STOA-NO-CONSUMERS and addendum (1 Nov) | drop the register; discover by estate scan | STOA-REG-001 | design (release rule, history question) | 11 |
| STOA-LINES (6 Nov) and PAGE-TYPES-ADOPT (6 Nov) | 3 page types, adopted in principle | STOA-PAGE-001 | design | 12 |
| STOA-HEADING-LINKS (7 Nov) | durable heading links | STOA-LINK-001 | design | 13 |
| STOA-DIAGRAM-OVERLAY (2 Nov) | opt-in diagram overlay | STOA-DIAG-001 | design | 14 |
| PRINT-LAYOUT (1 Nov) | print layout | STOA-PRINT-001 | design (low priority) | 15 |
| STOA-TOOLING (2 Nov) | 2 default checkout path | none | met in 0.33.0: `packages/stoa/tooling/stoa.js` reads `STOA_CHECKOUT` or `../packages-stoa` | — |
| STOA-HANDOVER (2 Nov) | — | none | explains where the STOA-* lines came from | — |
| STOA-LEGAL (4 Nov) | — | none | notice that Legal will use more of Stoa; no ask | — |
| STOA-UPSTREAM (8 Nov) | — | none | reports 0.34.0, already released; its consumer-register note feeds STOA-REG-001 | — |
| STOA-DUOTONE (8 Nov) | — | none | reports 0.35.0, already released | — |

The REFRESH and ACK lines are skipped. STOA-UPSTREAM and STOA-DUOTONE arrived after the brief's range and are listed for completeness.

#### Before capture

- Areas `CAL`, `HDR`, `THEME`, `BASE`, `TOOL`, `WB`, `REG`, `LINK`, `PAGE`, `PRINT` and `DIAG` are new: each needs a line in `.ki.toml`'s `[skills.ki-work-roadmap.areas]` and a ledger entry in `docs/roadmap/_ISSUES.md`, reserved before its record is written.
- Frontmatter follows STOA-CMD-001's fields, plus `assignee` (required on open records; CMD-001's lack of it was its one audit warning) and with `baseline_ref: null` until implementation starts.
- `purpose`: `capability` throughout, `governance` for STOA-REG-001; the house vocabulary has no defect value I could confirm.
- Related records: STOA-PAGE-001 meets STOA-BASE-001 (first paint), STOA-LINK-001 (outline ids) and STOA-REG-001 (adoption record); STOA-PRINT-001 follows STOA-PAGE-001. Dependencies are left for planning.

#### STOA-BASE-001-paint-the-upgraded-form-first.md

````markdown
---
id: STOA-BASE-001
area: BASE
title: Paint each unit's upgraded form first when scripts run
kind: deliver
purpose: capability
priority: high
size: m
assignee: work/ki.prj.stoa
status: triage
blocks: []
blocked_by: []
baseline_ref: null
created_at: 2026-11-08T12:25:34Z
updated_at: 2026-11-08T12:25:34Z
---

# Paint each unit's upgraded form first when scripts run

## Request

STOA-LINES (MSG-d7d46e9f), from HNR > SoP (hnr.sop.main), 6 November 2026 02:40 GMT, item 2, at Kris's word: "Stoa's Header, Calendar, Filter Bar and Diagram Viewer paint a different no-script first frame before their scripts upgrade them, causing layout shift; P2MS3 works round it site-side under 5GE-P2MS3-SITE-014 (`shell.css` scripting media query, `data-needs-script`)."

The site's record, 5GE-P2MS3-SITE-014, adds the line it meant for this work: "Header, Theme Menu, mode switch, Calendar and Diagram Viewer: each paints no-script form, or `hidden` controls, differs from upgraded form, so page shifts scripts run ... Could each unit's first paint match upgraded form scripting enabled, example `@media (scripting: enabled)` rules in its own stylesheet, `hidden` kept no-script case?" The measured jump: the Header painted 232 px tall with each group's links listed, then 63 px once its script ran, moving the page up 169 px.

## Goal

With scripting enabled, each unit's first paint is its upgraded layout, so nothing moves when its script runs; the no-script form stays for browsers without scripts.

## Current state

At Stoa 0.35.0 (`9c657a3`) no Stoa stylesheet has a `scripting` media query, and the units render their script-only controls `hidden` until the script runs.

## Boundary

The styles and render functions of the Header, Theme Menu, Mode Switch, Calendar, Filter Bar and Diagram Viewer, their tests, a first-paint check and the workbench. Changes to rendered markup must stay additive for sites. Page layouts are STOA-PAGE-001's. No release or re-vendor.

## Class

Small: a defect with a proven site-side fix to raise into the units; it spans six units, so planning may split it.
````

#### STOA-CAL-001-show-multi-day-events-on-every-day.md

````markdown
---
id: STOA-CAL-001
area: CAL
title: Show a multi-day event on every day it covers
kind: deliver
purpose: capability
priority: high
size: s
assignee: work/ki.prj.stoa
status: triage
blocks: []
blocked_by: []
baseline_ref: null
created_at: 2026-11-08T12:25:34Z
updated_at: 2026-11-08T12:25:34Z
---

# Show a multi-day event on every day it covers

## Request

STOA-LINES (MSG-d7d46e9f), from HNR > SoP (hnr.sop.main), 6 November 2026 02:40 GMT, item 1, at Kris's word: "The Stoa Calendar shows a multi-day event on its first day only (found in 5GE-P2MS3-SITE-010)."

The site's record, 5GE-P2MS3-SITE-010, gives the cause: "`seriesSpan` in `calendar/view.js` cuts a one-off date that spans several days to its first day. The List view and each calendar's page show the Geneva week, HNR in Geneva and the fine-tuning under their first day only, and mark them past after that day. The Months and Runway views draw them in full."

## Goal

A one-off entry that spans several days shows its whole span in the List view and on each calendar's page, and counts as past only after its last day.

## Current state

Still present at Stoa 0.35.0 (`9c657a3`). `seriesSpan` in `packages/stoa/src/calendar/view.js` takes the last of `occurrences(entry)`, which for a one-off entry is only its first day, so it cuts the span to that day. The Months and Runway views read `first` and `last` from `calendarView` and are right.

## Boundary

The Calendar's span handling (`view.js`, and `dates.js` if needed), its tests and the workbench Calendar story's sample. Weekly series keep their present span. No release or re-vendor.

## Class

Small: a defect with a known cause.
````

#### STOA-CAL-002-publish-cancelled-events.md

````markdown
---
id: STOA-CAL-002
area: CAL
title: Publish cancelled calendar events
kind: deliver
purpose: capability
priority: medium
size: s
assignee: work/ki.prj.stoa
status: triage
blocks: []
blocked_by: []
baseline_ref: null
created_at: 2026-11-08T12:25:34Z
updated_at: 2026-11-08T12:25:34Z
---

# Publish cancelled calendar events

## Request

STOA-CANCELLED, from HNR > SoP (5ge) (hnr.sop.5ge), 1 November 2026: "please add a cancelled status to the Stoa Calendar (`STATUS:CANCELLED` in feeds, the event kept under its UID, and shown cancelled on pages), so the Phase 3 site can publish a cancelled meeting instead of omitting it, as Kris agreed on 1 November 2026 that cancelled calendar rows keep their ID; the site omits cancelled occurrences until it ships (5GE-P3-SITE-113). Tell hnr.sop.5ge when it ships."

## Goal

A calendar entry can be cancelled: its feed event keeps its UID and carries `STATUS:CANCELLED`, and every Calendar view shows it as cancelled rather than dropping it.

## Current state

Not met at Stoa 0.35.0 (`9c657a3`): `STATUSES` in `packages/stoa/src/calendar/contract.js` has no cancelled status, and `ics.js` writes `CONFIRMED` or `TENTATIVE` only.

## Boundary

The Calendar contract, ICS writer, views and styles, the Today Board and Timeline where they show entries, their tests, `calendar-feeds.md`, the README and the workbench Calendar story. Cancelling one occurrence of a weekly series is in scope only if planning finds it small. No release or re-vendor.

## Class

Small: one status through contract, feed and views.
````

#### STOA-CAL-003-feed-status-and-categories.md

````markdown
---
id: STOA-CAL-003
area: CAL
title: Leave unknown status out of feeds and take categories from the site
kind: deliver
purpose: capability
priority: medium
size: s
assignee: work/ki.prj.stoa
status: triage
blocks: []
blocked_by: []
baseline_ref: null
created_at: 2026-11-08T12:25:34Z
updated_at: 2026-11-08T12:25:34Z
---

# Leave unknown status out of feeds and take categories from the site

## Request

STOA-ICAL-MAPPING, from HNR > SoP (5ge) (hnr.sop.5ge), 1 November 2026, asks 1 and 2 of 3: "the Phase 3 calendar workbook's iCalendar Mapping (RFC 5545) asks three things the Stoa Calendar feed cannot yet do: (1) omit STATUS on an event whose status is unknown, where today every non-confirmed entry is written TENTATIVE; (2) write CATEGORIES from a label the site supplies (the workbook's Category, such as Steering or Scenario D) rather than the entry kind ... Please release these, then tell hnr.sop.5ge; the site edits no vendored Stoa."

## Goal

A feed event whose status is unknown carries no `STATUS` line, and a site can supply the label written as `CATEGORIES`, with the entry kind kept as the default.

## Current state

Not met at Stoa 0.35.0 (`9c657a3`): `packages/stoa/src/calendar/ics.js` writes `STATUS:CONFIRMED` for confirmed entries and `STATUS:TENTATIVE` for every other, and `CATEGORIES` from `entry.kind`. Which statuses count as unknown (for example `to-confirm`, or a site vocabulary flag) is for planning.

## Boundary

The Calendar contract and ICS writer, their tests, `calendar-feeds.md` and the README. No change to page views. SEQUENCE is STOA-CAL-004. No release or re-vendor.

## Class

Small: two contained feed changes.
````

#### STOA-CAL-004-feed-sequence.md

````markdown
---
id: STOA-CAL-004
area: CAL
title: Raise SEQUENCE when a published event is revised
kind: deliver
purpose: capability
priority: medium
size: s
assignee: work/ki.prj.stoa
status: triage
blocks: []
blocked_by: []
baseline_ref: null
created_at: 2026-11-08T12:25:34Z
updated_at: 2026-11-08T12:25:34Z
---

# Raise SEQUENCE when a published event is revised

## Request

STOA-ICAL-MAPPING, from HNR > SoP (5ge) (hnr.sop.5ge), 1 November 2026, ask 3 of 3: "(3) keep a SEQUENCE that rises when a published event is revised. Please release these, then tell hnr.sop.5ge; the site edits no vendored Stoa."

## Goal

Each feed event carries a `SEQUENCE` that rises whenever the published event is revised, so subscribers' calendars take the update.

## Current state

Not met at Stoa 0.35.0 (`9c657a3`): `ics.js` writes no `SEQUENCE`. A static build has no memory of what it published before, so the number must come from the site's data, such as a per-entry revision the workbook keeps, or from state the build stores; planning chooses, and if neither fits a contained change, this record becomes a design for Kris's look.

## Boundary

The Calendar contract and ICS writer, their tests, `calendar-feeds.md` and the README. No release or re-vendor.

## Class

Small if the site supplies the number; design if Stoa must remember earlier builds.
````

#### STOA-DIAG-001-interactive-diagram-overlay.md

````markdown
---
id: STOA-DIAG-001
area: DIAG
title: Opt-in interactive diagram overlay
kind: deliver
purpose: capability
priority: medium
size: m
assignee: work/ki.prj.stoa
status: triage
blocks: []
blocked_by: []
baseline_ref: null
created_at: 2026-11-08T12:25:34Z
updated_at: 2026-11-08T12:25:34Z
---

# Opt-in interactive diagram overlay

## Request

STOA-DIAGRAM-OVERLAY, from HNR > SoP (hnr.sop.main), 2 November 2026: "Kris wants Stoa to support the interactive diagram overlay (expand icon, 'Interactive' label) that is site-local today in the 5G Emerge Phase 2 and Phase 3 sites (30 October); take it from those two only and build it as an opt-in Stoa capability for hnr.sop.sites' full rollout. Tell hnr.sop.sites when it ships."

## Goal

The Diagram Viewer can, by opt-in, mark an inline diagram with an expand icon and an "Interactive" label that opens it, taken from the Phase 2 and Phase 3 sites' own overlays.

## Current state

Partly related at Stoa 0.35.0 (`9c657a3`): the Diagram Viewer renders an "Explore" button that opens the diagram in a dialog, but no overlay on the inline diagram. The two sites' overlays have not yet been compared.

## Boundary

The Diagram Viewer's render, element, styles, tests, README and workbench story, from the Phase 2 and Phase 3 overlays only. No release or site adoption.

## Class

Design: Kris named it a design to look at, and the two sites' overlays must be reconciled first.
````

#### STOA-HDR-001-most-specific-current-link.md

````markdown
---
id: STOA-HDR-001
area: HDR
title: Let the Header mark only the most specific current link
kind: deliver
purpose: capability
priority: medium
size: s
assignee: work/ki.prj.stoa
status: triage
blocks: []
blocked_by: []
baseline_ref: null
created_at: 2026-11-08T12:25:34Z
updated_at: 2026-11-08T12:25:34Z
---

# Let the Header mark only the most specific current link

## Request

STOA-HEADER, from HNR > SoP (hnr.sop.main), 2 November 2026, ask 1 of 2, from a 5G Emerge consumer site (22 October): "`headerCurrent` marks every link whose path holds the page's, so a page at /a/b/ marks both /a/ and /a/b/; the site strips the shallower `aria-current` marks itself; please consider a most-specific-wins option." Tell hnr.sop.5ge when it ships.

## Goal

A site can choose that only the most specific matching link carries `aria-current`, so it no longer strips the shallower marks itself.

## Current state

Unchanged at Stoa 0.35.0 (`9c657a3`): `headerCurrent` in `packages/stoa/src/header/render.js` returns `page` for an exact match and `location` for every link whose path, or `activeFor` root, holds the page's.

## Boundary

The Header's render function and config type, its tests, README and the workbench Header story. The present behaviour stays the default. No release or re-vendor.

## Class

Small: an opt-in option on one function.
````

#### STOA-HDR-002-always-visible-brand-slot.md

````markdown
---
id: STOA-HDR-002
area: HDR
title: Give the Header an always-visible slot beside the brand
kind: deliver
purpose: capability
priority: medium
size: s
assignee: work/ki.prj.stoa
status: triage
blocks: []
blocked_by: []
baseline_ref: null
created_at: 2026-11-08T12:25:34Z
updated_at: 2026-11-08T12:25:34Z
---

# Give the Header an always-visible slot beside the brand

## Request

STOA-HEADER, from HNR > SoP (hnr.sop.main), 2 November 2026, ask 2 of 2, from a 5G Emerge consumer site (22 October): "the Header's end slot sits in the collapsible panel, so a status marker placed there shows only in the open menu below `collapseAt`; please consider an always-visible slot beside the brand." Tell hnr.sop.5ge when it ships.

## Goal

A site can place a small marker, such as a status badge, beside the brand, where it stays visible when the navigation folds.

## Current state

Partly met at Stoa 0.35.0 (`9c657a3`): the named `tools`, `theme` and `mode` slots now stay in the row when the navigation folds, but they sit at the row's end and are meant for controls; `prefs` and `end` still sit in the panel, and nothing sits beside the brand.

## Boundary

The Header's render function, slot type, styles, tests, README and the workbench Header story. Existing slots keep their places. No release or re-vendor.

## Class

Small: one additive slot.
````

#### STOA-LINK-001-durable-heading-links.md

````markdown
---
id: STOA-LINK-001
area: LINK
title: Durable links to every heading
kind: deliver
purpose: capability
priority: medium
size: l
assignee: work/ki.prj.stoa
status: triage
blocks: []
blocked_by: []
baseline_ref: null
created_at: 2026-11-08T12:25:34Z
updated_at: 2026-11-08T12:25:34Z
---

# Durable links to every heading

## Request

STOA-HEADING-LINKS, from ki.sop.main, 7 November 2026 02:17 GMT. Kris's idea, in his words: "sites that are following the [Stoa] approach, that headings can effectively be linked to directly. And so the links should be durable as well ... a way that doesn't necessarily change based on the ordering of the same text in a heading ... every H1 should be unique, and then H2 under ... different H1s may well have the same text, but effectively the bookmark to it should be qualified by the H1 text or its bookmark value ... when you kind of hovered on the title, in the margin it offered you a link to it. Or maybe after the title is also possible ... more on certain pages ... but probably a lot of the pages."

The shape proposed with it: "ids from heading text, not position; H2 and below qualified by their parent's id; a build check that fails on a duplicate H1 or a duplicate sibling; a hover link in the margin, after the title on narrow screens; an optional explicit id and old-id aliases so a renamed heading keeps its links."

## Goal

On a Stoa site every heading has a durable id built from its text and qualified by its parent's, a build check refuses duplicates, a reader can copy a heading's link from the margin, and a renamed heading keeps its old links.

## Current state

Not met at Stoa 0.35.0 (`9c657a3`): Stoa has no heading-id unit; sites rely on their Markdown renderer's own ids.

## Boundary

A new build-time unit and its styles, tests, README, decision record and workbench story. STOA-PAGE-001's Page Outline would read these ids, so the two should agree. No release or site adoption.

## Class

Design: it changes how every site's headings and links are built.
````

#### STOA-PAGE-001-page-types.md

````markdown
---
id: STOA-PAGE-001
area: PAGE
title: Stoa-owned page types
kind: deliver
purpose: capability
priority: high
size: l
assignee: work/ki.prj.stoa
status: triage
blocks: []
blocked_by: []
baseline_ref: null
created_at: 2026-11-08T12:25:34Z
updated_at: 2026-11-08T12:25:34Z
---

# Stoa-owned page types

## Request

STOA-LINES (MSG-d7d46e9f), from HNR > SoP (hnr.sop.main), 6 November 2026 02:40 GMT, item 3: "Proposal: Stoa owns shared page-type layouts (dashboard, docs with a wide variant, info, wide, standalone), drafted in `apps-io.5g-emerge.p2ms3/docs/design/page-types.md`; adoption across the HNR sites stays Kris's decision."

PAGE-TYPES-ADOPT (MSG-8b4360dd), from HNR > SoP (hnr.sop.main), 6 November 2026 22:40 GMT: "Kris adopts p2ms3's four page types in principle as Stoa-owned, per `apps-io.5g-emerge.p2ms3/docs/design/page-types.md`; HNR's 5G Emerge Phase 2 and Phase 3 sites adopt them after Geneva, through Stoa. Source: Kris's PAGE-TYPES-ADOPT a) 'Adopt via Stoa', 6 November 2026 22:32 GMT."

## Goal

Stoa names four page types, `dashboard`, `docs` (with a wide variant), `wide` and `standalone`, chosen by `layout: <type>` with `wide` the default and marked `data-page-type` on `<html>`, and supplies the layout tokens, styles and two build-time units (Section Navigation and Page Outline) that let a site's thin layouts render each type's final layout at first paint.

## Current state

Not met at Stoa 0.35.0 (`9c657a3`): Stoa has `--stoa-content-width` and `--stoa-page-pad` only, no layout, measure or side-column token and no decision record. The design note lists six things Stoa would need; its fifth, the units' first paint, is STOA-BASE-001. The note's `units.json5` and `consumers.json5` adoption step meets STOA-REG-001.

## Boundary

A decision record, layout tokens, component styles, the two units, tests, a workbench story per type and the README. The layouts stay with each site. No release or site adoption.

## Class

Design: it changes how sites are built; adopted in principle, the shape still needs Kris's look.
````

#### STOA-PRINT-001-print-layout.md

````markdown
---
id: STOA-PRINT-001
area: PRINT
title: Print every page as a clean PDF
kind: deliver
purpose: capability
priority: low
size: m
assignee: work/ki.prj.stoa
status: triage
blocks: []
blocked_by: []
baseline_ref: null
created_at: 2026-11-08T12:25:34Z
updated_at: 2026-11-08T12:25:34Z
---

# Print every page as a clean PDF

## Request

PRINT-LAYOUT, from HNR > SoP (sites) (hnr.sop.sites), 1 November 2026: "Kris wants a print layout on every site, so any page prints as a sensible PDF without menus or navigation; low priority, 'should go as a roadmap item', built into sites in general, possibly as a Stoa package. Please capture it as a Stoa roadmap record (print stylesheet in Stoa), and tell hnr.sop.sites when it ships so the HNR sites adopt it."

## Goal

Any page on a Stoa site prints as a sensible PDF: no Header, Command Bar, menus or navigation, readable type and colour on paper, and links and page breaks handled.

## Current state

Not met at Stoa 0.35.0 (`9c657a3`): no Stoa stylesheet has print rules.

## Boundary

A print stylesheet in Stoa's layers, print rules for each unit, tests, a workbench print preview and the README. How each page type prints should follow STOA-PAGE-001. No release or site adoption.

## Class

Design: it touches every unit and every page, and wants Kris's look at what a printed page keeps.
````

#### STOA-REG-001-drop-the-consumer-register.md

````markdown
---
id: STOA-REG-001
area: REG
title: Drop the consumer register and find consumers in the local estate
kind: deliver
purpose: governance
priority: medium
size: m
assignee: work/ki.prj.stoa
status: triage
blocks: []
blocked_by: []
baseline_ref: null
created_at: 2026-11-08T12:25:34Z
updated_at: 2026-11-08T12:25:34Z
---

# Drop the consumer register and find consumers in the local estate

## Request

STOA-NO-CONSUMERS, from HNR > SoP (sites) (hnr.sop.sites), 1 November 2026: "Kris on 1 November: 'The stowa package should not keep a reference to the things that are using it. There should be no reference out of Knowledge Islands to other territories.' For the new Stoa Project: remove packages-stoa's consumer register and any other reference to HNR or other territories' sites; the unmerged commit acf52ab (drops only the EIT entry) is superseded."

Addendum, same day: "Kris: 'If Stoa needs to do that, it can do something where it knows about looking in the local estate on a given rig, and it can look for patterns that it knows about that would identify that it's been used. It shouldn't have a finite list of them, right?' So: where Stoa needs to know its consumers, it discovers them by scanning the local estate on a Rig host for known usage patterns, never by keeping a list."

STOA-UPSTREAM (8 November) notes that 0.34.0 updated `consumers.json5`, "which STOA-NO-CONSUMERS still asks to remove".

## Goal

packages-stoa names no site or territory outside Knowledge Islands; where it needs its consumers, such as for a release notice, it finds them by scanning the local estate for a `stoa-lock.json` or other known pattern.

## Current state

Not met at Stoa 0.35.0 (`9c657a3`): `consumers.json5` lists the sites, the workbench tests it, and `AGENTS.md`'s core rules and release rule depend on it. Eleven tracked files name HNR or its sites, among them ADR-STOA-049, 050, 052, 054 and 055, two site guides, STOA-CMD-001 and the Help unit's render and test.

## Boundary

`consumers.json5` and its test, `AGENTS.md`'s rules, a discovery tool, and the other references; a decision record. Whether decision records and closed roadmap records are rewritten or left as history, and where the discovery tool lives (Stoa or Rig), are for Kris's look. No release.

## Class

Design: it changes the release rule and how Stoa knows its sites, and the history question needs Kris.
````

#### STOA-THEME-001-measure-the-theme-menu-colour-pairs.md

````markdown
---
id: STOA-THEME-001
area: THEME
title: Measure the Theme Menu's own colour pairs
kind: deliver
purpose: capability
priority: medium
size: s
assignee: work/ki.prj.stoa
status: triage
blocks: []
blocked_by: []
baseline_ref: null
created_at: 2026-11-08T12:25:34Z
updated_at: 2026-11-08T12:25:34Z
---

# Measure the Theme Menu's own colour pairs

## Request

STOA-THEME-MENU-CONTRAST, from HNR > SoP (hnr.sop.main), 2 November 2026, from HNR > 5G Emerge > Phase 2 (29 October): "Stoa does not measure the Theme Menu's own colour pairs. `checkThemeSystem`'s fixed pairs in `src/theme-engine/conformance.js` test `muted-foreground` only on card and background and `primary` only on background, but `styles/theme-menu.css` draws muted-foreground on popover and muted, popover-foreground on muted and accent, and primary on card; Stoa's tests run that check only on synthetic fixtures, never on its default tokens, and the browser contrast gate covers calendar pairs alone. Phase 2 removed its own copies of these checks, so no repository checks the menu now. Whether and how Stoa covers it is the Stoa work's call."

## Goal

Every foreground and background pair the Theme Menu draws is measured by `checkThemeSystem`, and Stoa's own default tokens pass that check in a test.

## Current state

Unchanged at Stoa 0.35.0 (`9c657a3`): the pairs list in `conformance.js` lacks muted-foreground on popover and muted, popover-foreground on muted and accent, and primary on card, all of which `theme-menu.css` uses.

## Boundary

`packages/stoa/src/theme-engine/conformance.js`, its tests, a test over the default tokens, and token fixes if a default pair fails. Sites' own themes are theirs to fix once the check reports them. No release or re-vendor.

## Class

Small: a contained gap in an existing check.
````

#### STOA-TOOL-001-keep-biome-off-consumer-markdown.md

````markdown
---
id: STOA-TOOL-001
area: TOOL
title: Tell consumers how to keep Biome 2.6 off their Markdown
kind: deliver
purpose: capability
priority: low
size: xs
assignee: work/ki.prj.stoa
status: triage
blocks: []
blocked_by: []
baseline_ref: null
created_at: 2026-11-08T12:25:34Z
updated_at: 2026-11-08T12:25:34Z
---

# Tell consumers how to keep Biome 2.6 off their Markdown

## Request

STOA-TOOLING, from HNR > SoP (hnr.sop.main), 2 November 2026, item 1 of 3: "fresh installs pull Biome 2.6, which reformats Markdown and broke front matter in the Sky site; Sky excluded Markdown from Biome (rumdl owns it) and kept `keywords` out of syncpack's sort to keep taxonomy order; other consumers will hit this on their next install, so please fold a fix into the consumer template (22 October)." Tell hnr.sop.sites.

## Goal

A site adopting or re-vendoring Stoa is told to switch off Biome's Markdown formatter and linter and to keep `keywords` out of Syncpack's sort.

## Current state

Stoa has no consumer template: sites are set up from the package README's first-vendor section, which says nothing of Biome or Syncpack. Stoa's own `biome.json` already switches off Markdown formatting and linting.

## Boundary

The package README's consumer setup section. Any site template outside packages-stoa belongs to its owner. No release or re-vendor.

## Class

Small: a documentation note.
````

#### STOA-WB-001-workbench-narrow-widths.md

````markdown
---
id: STOA-WB-001
area: WB
title: Stop the workbench clipping content at narrow widths
kind: deliver
purpose: capability
priority: low
size: xs
assignee: work/ki.prj.stoa
status: triage
blocks: []
blocked_by: []
baseline_ref: null
created_at: 2026-11-08T12:25:34Z
updated_at: 2026-11-08T12:25:34Z
---

# Stop the workbench clipping content at narrow widths

## Request

STOA-TOOLING, from HNR > SoP (hnr.sop.main), 2 November 2026, item 3 of 3: "the gallery clips content at narrow widths (gallery only, nothing vendored)." Tell hnr.sop.sites.

## Goal

Every workbench story can be read at phone width without its content clipped.

## Current state

The gallery named in the request became the workbench in `apps/workbench/`. Whether it still clips needs a look at 360 px; the code alone does not settle it. If it does not, this record closes as already met.

## Boundary

`apps/workbench/` styles and stage only; nothing vendored. No release.

## Class

Small: workbench only.
````

## Queries

### STOA-AREAS - eleven new roadmap area codes

**Context:** packages-stoa declares one roadmap area, `CMD`. The drafts use eleven more, one for each unit or concern: `CAL`, `HDR`, `THEME`, `BASE` (first paint across units), `TOOL`, `WB` (workbench), `REG` (consumer register), `LINK` (heading links), `PAGE`, `PRINT` and `DIAG`. An area code is fixed once issued, so this is the moment to choose.

**Query:** Capture with the eleven codes as drafted?

**Options:**

a) (recommended, confidence medium - one code for each unit matches the brief's examples and keeps later records easy to place) Yes, declare all eleven in `.ki.toml` and the ledger.

b) Fold the one-record areas into broader ones, for example `TOOL` and `WB` into `TOOL`, and `LINK` and `PRINT` into `PAGE`.

### STOA-TOOL-SCOPE - Biome fix with no consumer template

**Context:** STOA-TOOLING item 1 asks Stoa to "fold a fix into the consumer template", but packages-stoa has no consumer template. Sites are set up from the package README. STOA-TOOL-001 is drafted as a README note telling sites to switch off Biome's Markdown handling and keep `keywords` out of Syncpack's sort.

**Query:** Is a README note enough?

**Options:**

a) (recommended, confidence medium - Stoa ships no site scaffolding, and a template elsewhere belongs to its owner) Yes, a README note in Stoa, and tell hnr.sop.sites that any site template is theirs to fix.

b) Have Stoa ship a consumer `biome.json` fragment as well, which widens what sites vendor.

```text
STOA-AREAS a
STOA-TOOL-SCOPE a
```

🤖 → 👤

### 🤖 → 👤 Handoff to supervisor · at 12:27 GMT

🤖 0 running · ⏳ 0 queued · 👤 1 with you · ⛔ 0 blocked · 🅿️ 0 parked

- [with you] capture the 15 Stoa draft records from STOA-DRAFTS · coordinator · at 12:27 GMT

🧵 ki.prj.stoa
