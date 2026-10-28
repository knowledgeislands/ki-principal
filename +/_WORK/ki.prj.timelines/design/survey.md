# ki.timelines survey

Read-only survey for the Timelines Project, run `tl-seed`, 19 October 2026. Facts only; the closing list holds the open questions. Nothing outside `ki-principal` was changed.

## 1. 5G Emerge phase 3 calendar component

Repository `/Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase3`, `apps/site`, an Eleventy site on Cloudflare Workers static assets at `https://phase3.5g-emerge.io`. Built on 9 and 10 October 2026 (commits `39dd21c`, `0914814`, `b977d4b`).

### Files

| File | Role |
| --- | --- |
| [calendars.json5](/Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase3/apps/site/src/_data/calendars.json5) | The registry, 212 lines; its header comment documents every field. |
| [ics.ts](/Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase3/apps/site/lib/ics.ts) | Types, date-span parsing and the RFC 5545 feed builder, 204 lines, no dependency. |
| [calendars.ts](/Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase3/apps/site/lib/calendars.ts) | Kind and status vocabulary, month grouping, subscribe links, merged agenda, next and upcoming dates, view JSON, 258 lines. |
| [eleventy.config.ts](/Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase3/apps/site/eleventy.config.ts) | Calendars section (about lines 311-373): build-time `today`, filters and the `icsFeed` filter. |
| [feed.njk](/Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase3/apps/site/src/content/tools/calendars/feed.njk) | Paginates the registry into `/calendars/<id>.ics`. |
| [calendar.njk](/Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase3/apps/site/src/content/tools/calendars/calendar.njk), [index.njk](/Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase3/apps/site/src/content/tools/calendars/index.njk) | One page per calendar at `/tools/calendars/<id>/`; the landing page at `/tools/calendars/`. |
| [calendars-view.js](/Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase3/apps/site/src/assets/js/calendars-view.js), [calendars.js](/Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase3/apps/site/src/assets/js/calendars.js) | Months and Runway drawing, toggles and popovers (610 lines); past-marking by the reader's date, upcoming lists and copy buttons (46 lines). |
| [calendar-macros.njk](/Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase3/apps/site/src/_includes/partials/calendar-macros.njk) | `calendarPointer` and related macros, used by scenario pages, the Technology Catalogue and Programme Status. |
| `src/assets/css/partials/calendars.css`, `calendars-view.css`, `tokens.css` | Styling; eight colour slots `--cal-<n>-*`. |
| [calendars.test.ts](/Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase3/apps/site/tests/calendars.test.ts) | 33 tests, 499 lines. |
| [site-authoring.md](/Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase3/docs/guides/developer/site-authoring.md) | "Add a calendar entry" and "Add a calendar" procedures. |
| [cloudflare.md](/Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase3/docs/guides/developer/cloudflare.md) | The Access bypass for `/calendars/*`. |

### Data shape

A JSON5 array of calendars. Six exist: `phase3-programme` (11 entries) and `scenario-a` to `scenario-d` and `technology-tracks` (no entries yet).

- **Calendar:** `id` (permanent; the page and feed URL), `title`, `description`, optional `group` (landing-page heading, first-seen order), `code` (up to three characters shown beside each date, so colour is never the only cue), `colour` (slot 1-8), `entries` (may be empty).
- **Entry:** `id` (permanent; becomes the event UID `<id>@<host>`), `title`, `start` (`YYYY-MM-DD`, or `YYYY-MM` / `YYYY` when the source gives no day), optional `end` (inclusive last day, day precision only), `kind` (`milestone`, `deadline`, `review`, `meeting`, `event`), `status` for firmness (`confirmed`, `planned`, `target`, `proposed`, `to-confirm`), optional `sourceStatus` (the source's own words), `description`, optional `scenarios` and `tracks`, and `sources` as `{ source, at }` citations into `source-register.json5`.
- Rule: never invent a date; an undated item belongs in the programme model's open questions.
- Dates only, never times; no time zone is involved.

### Busy status today

Every `VEVENT` is written `TRANSP:TRANSPARENT`, so every event shows as free. There is no per-entry field for it. `STATUS` is `CONFIRMED` when `status` is `confirmed`, otherwise `TENTATIVE`. No `X-MICROSOFT-CDO-BUSYSTATUS` or similar property is written.

### How feeds are built

`buildFeed` in `ics.ts` writes one feed per calendar at build time:

- Calendar properties: `PRODID:-//5G-EMERGE//<title>//EN`, `METHOD:PUBLISH`, `NAME` and `X-WR-CALNAME`, `DESCRIPTION` and `X-WR-CALDESC`, `URL` (the page), `SOURCE` (the feed), `REFRESH-INTERVAL` and `X-PUBLISHED-TTL` of 12 hours.
- Each event is all-day: `DTSTART;VALUE=DATE`, exclusive `DTEND`, `DTSTAMP` from build time, `SUMMARY`, `DESCRIPTION` (entry text, status label, sources, link), `CATEGORIES` (the kind), `STATUS`, `TRANSP`, `URL` to the entry's anchor.
- Month-precision entries span the month and get "(day to be confirmed)" in the title; year-precision entries are left off the feed and shown on the page only.
- An empty calendar emits a UTC `VTIMEZONE` so the feed stays valid and subscribable.
- Line folding at 75 octets of UTF-8 and TEXT escaping are hand-written and tested.

### How feeds are homed

- Path `/calendars/<id>.ics` on `phase3.5g-emerge.io`, built into `dist/` and served as static assets; Cloudflare serves `.ics` as `text/calendar; charset=utf-8`.
- The site sits behind Cloudflare Access; a separate self-hosted Access application bypasses `phase3.5g-emerge.io/calendars/*` so subscriptions work without sign-in. Preview URLs carry no bypass, so feeds are public only on the production domain.
- The smoke suite fails a build whose feeds carry an email address or phone number.
- Subscribe links per calendar: `https`, `webcal`, Google (`calendar.google.com/calendar/r?cid=`), Outlook 365 and Outlook.com `addfromweb`.

### Views

- **List:** rendered at build time, month-grouped, the complete page without JavaScript; year-only entries under "<year>, date to be confirmed".
- **Months:** one month on narrow screens, three otherwise, drawn in the browser from JSON embedded in the page.
- **Runway:** three months as a horizontal track with Monday ticks and a Today flag.
- Calendar toggles and the chosen view are remembered in `localStorage`; "today" is the reader's own date, so a stale build never shows a passed date as ahead.
- Calendar pages also feed a next-date counter and upcoming list on Programme Status.

### 5G-specific versus general

| General | 5G-specific |
| --- | --- |
| Calendar and entry shape, permanent ids, date precision, inclusive end, kind and firmness vocabularies, "never invent a date" | `scenarios` and `tracks` fields and their pill lookup |
| `ics.ts` as a whole, apart from the `PRODID` string | `PRODID:-//5G-EMERGE//...` |
| Subscribe-link builder, month grouping, agenda, next and upcoming | Source citations resolved against 5G's `source-register.json5` |
| List, Months and Runway view logic | Eleventy filters, Nunjucks templates, site CSS tokens and Lucide icons |
| Empty-feed validity, refresh hints | Cloudflare Access bypass, `phase3.5g-emerge.io` host, smoke-suite PII check |

### A second date list beside the registry

[timeline/_collection.json5](/Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase3/apps/site/src/_data/programme-model/timeline/_collection.json5) and eleven sibling files hold the programme timeline milestones shown on [timeline-milestones.njk](/Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase3/apps/site/src/content/documentation/programme/timeline-milestones.njk). Each file is `{ date, label, status }` with a free-text date (for example "3-4 Nov 2026", written with a dash between the days) and the source's status words; `_collection.json5` gives order and a shared `timelineSource`. The same eleven milestones appear as the eleven `phase3-programme` registry entries, with structured dates there and free text here; nothing links the two. [Q-TIMELINE](/Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase3/apps/site/src/_data/programme-model/open-questions/Q-TIMELINE.json5) records that a detailed delivery timeline is still open.

## 2. KI-HARNESS-GOV-222

[KI-HARNESS-GOV-222 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/ae8a1323ab167cf9ba559e5a1046c1ab98a6a81b/docs/roadmap/KI-HARNESS-GOV-222-timeline-and-calendar-skill.md), "Timeline and calendar skill", status `triage`, project `observatory`, component `governance`, captured 19 October 2026 (commit `7ed13f9c`).

- **Goal:** a harness skill governs the dated things a knowledge base keeps - key dates, due dates and milestones - as one approach extracted from the 5G Emerge component: each base keeps its dated items, may publish one or more subscribable calendar sets, and states each item's busy status.
- **Context:** quotes Kris's DIAGRAM-GANTT words of 19 October 2026 from the [Observatory decisions log](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.observatory/decisions.md); the read-back keeps the legal gantt as it is and hands timelines and calendars out of the Observatory thread. Describes the registry, `ics.ts`, the views and tests as section 1 does; records that busy status is not modelled and that a per-item busy status mapped to `TRANSP` and client busy-status properties would need times or a stated all-day blocking rule; notes the separate programme timeline and asks whether one source feeds both.
- **Boundary in:** a harness skill with standard, rubric and audit for kept dated items, calendar sets, feed publication and per-item busy status; candidate names under [ADR-KI-HARNESS-SKILLS-003](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/decisions/ADR-KI-HARNESS-SKILLS-003-dependency-order-for-multi-skill-composition.md) (`ki-calendars`, `ki-timelines`, `ki-key-dates`); first adopters legal-principal, personal-principal and 5G Emerge.
- **Boundary out:** changing the 5G component or the legal gantt before the skill exists; Archify diagram work, owned by `ki-diagrams`.
- **Discussion:** where feeds are homed and served (a base's own site, the Observatory or elsewhere) and how a private base publishes without exposing its dates; one skill or a skill and a view; busy-status vocabulary and default; whether the extracted code lives in the harness, `tools-ki` or a shared package. The harness owns priority and design.
- The record names `project: observatory`, not `timelines`.

## 3. First adopters

### legal-principal

[FR Timeline to FDR](</Users/krisbrown/workspaces/legal/legal-principal/Pillars/Command Centre/Working Notes/XM-CRITICAL-TIMELINE - Critical Timeline and Preparation Checklist/FR Timeline to FDR.md>), a working note of 202 lines generated on 15 October 2026 by the legal-state-of-play thread's timeline-observatory run, covering 15 October 2026 to 2 February 2027.

- Shape: a critical-path list, a Mermaid `gantt` (`dateFormat YYYY-MM-DD`, six sections: court deadlines, experts, disclosure, MPS, kit actions, contact), a dated table, a stress-test and a data-file section.
- It states it is a generated view, not a status register: status and dates live on the linked Command Centre Items, and correction is to the Item, then regenerate.
- The rows are also written as JSON, schema `fr-timeline/1`, to a working copy in the legal source store (`kit-legal-sources/-/2026-10-15 FR Timeline/fr-timeline.json`), not evidence. Header: `schema`, `generated_at`, `as_of`, `timezone`, `scope`, `status_owner`. Row: `id`, `date`, optional `time` (`HH:MM` local), `end_date`, `title`, `lane` (`court`, `experts`, `disclosure`, `mps`, `kit`, `contact`), `kind` (`court-deadline`, `target`, `waiting-on-other-side`, `kit-action`), `hard` (fixed by order, court or appointment), `status` (`overdue`, `due-today`, `open`, `waiting`, `proposed`, `scheduled` as at `as_of`), optional `critical`, `source_item`, optional `note`.
- Unlike 5G, some rows carry a time of day.
- The source data are Command Centre Items' frontmatter. The [Command Centre Guide](</Users/krisbrown/workspaces/legal/legal-principal/Pillars/Command Centre/Command Centre Guide.md>) "Dates and calendar semantics" section fixes the dated fields: `due_at` and `due_on` (obligations), `event_at` (hearing or appointment), `decision_by`, `chase_at`, `review_on`, `target_on`, `requested_on`, `overdue_since`, `completed_on`; live urgency uses the first seven. `due_time`, `review_trigger` and free-text `duration` are labels only. In the Areas folders, 23 notes carry `due_on`, 13 `hearing_date`, 7 `due_at`, 7 `due_time`.
- Sibling notes: the XM-CRITICAL-TIMELINE note, "Command Centre Observatory Candidates 2026-10" and "Stale Item Re-dating Proposals 2026-10-15". The Archify redraw is tracked by [LGL-PRINCIPAL-OPS-028](/Users/krisbrown/workspaces/legal/legal-principal/Streams/Roadmap/LGL-PRINCIPAL-OPS-028-redraw-mermaid-diagrams-in-archify.md), "redraw Mermaid diagrams in Archify".
- The case content is not reproduced here.

### personal-principal

`/Users/krisbrown/workspaces/personal/personal-principal` holds dated material in these forms; none is in a structured date field meant for a calendar:

- `Calendar/`: periodic notes, 62 in 2024, 44 in 2025, 160 in 2026, including 23 `calendar/meeting` notes; these are records of days, not future dates.
- Relationship interaction notes under `Pillars/Relationships/People/*/Interactions/` carry `date:`; four people notes mention birthdays in prose.
- Renewal and expiry dates sit in prose tables, for example [YP62 LNY Silver Range Rover Evoque](</Users/krisbrown/workspaces/personal/personal-principal/Pillars/Home/Vehicles/YP62 LNY Silver Range Rover Evoque.md>) (vehicle tax and MOT expiry, insurance unknown).
- `Streams/Projects/` has five Projects, all `target: null`; `Streams/Roadmap/` has 36 records with no date field beyond `created_at` and `updated_at`.
- Travel and retreat notes (for example Costa Rica, Path of Love Retreat) mention dates in prose.

### 5G Emerge

Covered in section 1: the registry and its feeds, and the separate programme timeline under `programme-model/timeline/`.

## 4. Existing harness skills and standards touching dates

In `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness`:

- **No skill governs kept dated items, calendar feeds or timelines.** The only record proposing one is KI-HARNESS-GOV-222.
- [standards-design-system.md](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/design/ki-design-system/references/standards-design-system.md) (`ki-design-system`) says it was established by the 5G Emerge Phase 3 calendars page, and its exemplar names `apps/site/tests/calendars.test.ts` as a check. It governs design method, not dates.
- [standards-recurring-work.md](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-work-recurring/references/standards-recurring-work.md) (`ki-work-recurring`): ISO-8601 `cadence` and `grace`, `last-run`, and a schedule evaluator ([schedule.ts](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-work-recurring/scripts/rubric/contexts/schedule.ts)) computing due and overdue boundaries for recurring work.
- [standards-work-item-format.md](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-work-roadmap/references/standards-work-item-format.md) (`ki-work-roadmap`): an optional ISO `review` date on a held record.
- [standards-project-registry.md](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-work/references/standards-project-registry.md) (`ki-work`): a Project's `target` is an ISO date or `null`.
- [standards-frontmatter.md](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-kb/references/standards-frontmatter.md) (`ki-repo-kb`): the `Calendar/` zone note types `calendar/index`, `daily`, `weekly`, `monthly`, `meeting`, `session`, which record past periods rather than future dates.
- [ki-diagrams](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-diagrams/SKILL.md) governs Archify diagrams; it does not mention gantt or timelines. The separate Archify skill lists timeline and waterfall among its diagram types.

## Open questions

1. Where are subscription feeds homed and served for a base with no site (legal-principal, personal-principal), and how does a private base publish without exposing its dates?
2. What is the busy-status vocabulary and its default, and how does it map to `TRANSP` and client busy-status properties for all-day items, given 5G holds dates only and legal holds some times?
3. Does the skill model times of day and a time zone, as legal's `time` and `timezone` do, or dates only, as 5G does?
4. Is the source of truth a registry file (5G) or dated frontmatter on existing notes with generated views (legal Command Centre), or both?
5. Do the 5G programme timeline and the calendar registry collapse to one source, and which way?
6. Whose vocabulary wins for kind and status: 5G's `kind` and firmness `status`, legal's `kind`, `lane`, `hard` and progress `status`, or a merge?
7. Is it one skill, or a skill plus a view component, and where does extracted code live: the harness, `tools-ki` or a shared package?
8. Which of the candidate names under ADR-KI-HARNESS-SKILLS-003 is taken?
9. Should KI-HARNESS-GOV-222 move from `project: observatory` to `project: timelines`? That is the harness's call.
10. What does personal-principal adopt first, given its dates sit in prose rather than fields?
11. What are Kris's improvements to the scope (TIMELINE-IMPROVEMENTS)?
