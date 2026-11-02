# Timelines skill: merged report

**Brief:** [timelines-skill-brief.md](timelines-skill-brief.md) · **Reviews:** [timelines-skill-review-fable.md](timelines-skill-review-fable.md), [timelines-skill-review-astra.md](timelines-skill-review-astra.md) · **Date:** 2026-10-19

The design belongs to the Project work `ki.timelines`. Disputes are settled here by re-reading the sources, not by counting reviewers, and Kris's recorded words in [decisions.md](../decisions.md) win wherever they speak. Evidence is local code and documentation unless marked as prior knowledge. Case content from legal-principal is not reproduced.

## Summary

Both reviews keep the brief's centre, and so does this report: one skill governs the **dated item**, with three types (milestone, event, span), a per-item `busy` flag that defaults to free, firmness kept separate, two declared source shapes (a registry file, or dated frontmatter on the owning note), and generated views and feeds. Its code lives in the skill's own `scripts/` in the harness.

The re-reading leads to three main changes:

1. **Private publication is not ready.** The brief assumed account sync through `mcp-gsuite` and `mcp-m365`. Neither connector can do it today: Google's create takes only timed RFC 3339 times, with no transparency, all-day or UID field, and Microsoft has no update tool and no calendar selector. The claim that subscribed calendars do not count towards free/busy rests on prior knowledge, not local evidence. So private publication becomes a separate adapter that has to be proved before it is promised. Until then private sets stay unpublished and the base's generated view serves them.
2. **Identity, time and "today" get precise rules.** UIDs are permanent logical keys and keep 5G's host suffix. A local time that does not exist on a clock-change day is rejected, and an ambiguous one needs an explicit offset. "Today" is judged in the set's declared time zone, as legal's Guide requires. A timed busy item needs a real end.
3. **Adoption gains verification steps without changing who adopts.** 5G stays the pilot, cut down to vendoring plus a parity check, with its timeline collapse as a separate record. legal gets a local half early and its sync half last. The private adapter is proved first on synthetic and then on personal data, before legal publishes anything. In legal, the timeline becomes a view of the existing Command Centre artifact.

## Corrections to the brief

- **"The smoke suite fails a build whose feeds carry an email address"** - the check is the "publication boundary" test in `apps/site/tests/site.test.ts` (about lines 1974-2012), run under `bun test` after a build. It covers every published `.ics`, `.html`, `.json` and similar file, and catches phone numbers as well as emails. There is no separate smoke suite. It catches contact details only, so it cannot prove that private narrative is absent. (Fable, Astra; verified in the test file.)
- **"the List, Months and Runway views render in browser JavaScript over that JSON"** - only Months and Runway do. List is rendered at build time by Nunjucks (`src/content/tools/calendars/index.njk` lines 112-131, `calendar.njk` lines 46-68), with `is-past` set from a build-time `today`, and `calendars.js` re-marks past items by the reader's date. The survey already said this. (Astra; verified.)
- **"permanent `id` (the UID)"** - the emitted UID is `<id>@<host>` (`lib/ics.ts` line 174, `UID:${entry.id}@${host}`). Extraction must keep the host part, or every subscriber's events duplicate. (Astra; verified.)
- **"the only 5G-specific string is the `PRODID`"** - true of literal strings, but the entry type still carries `scenarios` and `tracks`, and `FeedOptions` supplies `statusLabel` and `describeSource` (`ics.ts` lines 168-169). Extraction therefore needs some adapter work. (Astra; verified.)
- **5G's eleven timeline files "repeat" the registry** - they hold the same eleven milestones, but some carry fields the registry lacks. `industry-day-paris.json5`, for example, has a `seeAlso` citation of `MR-003`, and the status words are written separately. The collapse has to reconcile them rather than delete the files. (Astra; verified.)
- **Point 6, "legal's `hard: true` reads as `confirmed`"** - holds for `true`. But `hard: false` does not mean tentative: the FR Timeline schema defines `hard` as "true if fixed by the order, the court or an appointment". Its `status` values `waiting`, `proposed` and `scheduled` are judged "as at `as_of`" and partly authored by hand, so not all of them come from the clock. (Astra; verified in the note's schema table.)
- **Point 12, `<item_id>.<field>` as the UID** - the Guide lists `due_at` and `due_on` together as "obligations or cut-offs" (Guide line 173). Re-dating an obligation from a day to a timestamp under that scheme would leave the old all-day UID beside a new one. The key must be logical, not the field name. (Astra; verified.)
- **Points 16 and 17, free/busy and account sync** - point 16 is prior knowledge, which both reviewers say and neither could check locally. Point 17 does not work with the current connectors. In `mcp-gsuite`, `gsuite_calendar_event_create` takes RFC 3339 timed `start` and `end` and requires `end` (`src/tools/calendar/index.ts` lines 86-98), and no handler sets transparency, all-day dates or `iCalUID`. In `mcp-m365` there is no update tool, create posts to `me/events` only (`src/main/calendar/create.ts` line 20) with no calendar selector, and there is no `showAs` field. (Fable, Astra; verified.)
- **Point 20, a live artifact pair in legal** - the Guide says of the `legal-command-centre` artifact: "Future changes must update that artifact rather than create a second one" (Guide line 209), and that artifact already provides "a Calendar using only explicit date fields and labelled milestone types" (line 230). (Fable; verified.)
- **Point 21, reader-local "today"** - the Guide says: "The Today boundary is calculated from the current `Europe/London` calendar date, not from a UTC ISO date" (line 187). (Astra; verified.)
- **Point 23, "`ki-timelines` collides with the timeline diagram type `ki-diagrams` and Archify already own"** - `ki-diagrams` never mentions timelines (no match anywhere in the skill), while the Archify skill does list timeline among its diagram types. ADR-KI-HARNESS-SKILLS-003 allows all three names. Fable adds a fact the brief missed: `ki-repo-kb` already uses "calendar" for the `Calendar/` zone and its `calendar/*` note types (`standards-frontmatter.md` lines 63-69). (Fable, Astra; verified.)
- **Missing from the brief: legal already has a duration field.** The Guide makes `duration_minutes` "a numeric duration, not a date" (line 185). It is the real end a timed busy event can take without inventing one. Neither review found it; it came from this merge's re-read.
- **Missing from the brief: `hearing_date`.** Per the survey, 13 legal Area notes carry `hearing_date`, which the Guide does not list. The generator will not see those dates until legal migrates them to `event_at` or adds the field. (Fable.)
- **Shared-code preference citation** - the line is in Kris's Claude user configuration under "Cross-project preferences" and in the Codex configuration under a heading about publishing to package registries. Both carry the same rule, so this is only a label that varies by runtime. (Astra, Fable; checked against the Claude configuration loaded for this run.)

## Model

### Dated item

- **Fields:** a permanent logical `id`; `title`; `start` at day, month or year precision, or a local date and time; an optional end; `type`; optional `firmness`; `busy`; an optional free per-base `category` (5G's `kind`, legal's `kind` and `lane`); `description`; source citations; and the calendar sets it belongs to.
- **End:** for date-only items the end is the inclusive last day. For timed items it is an exclusive end instant, taken only from the source (an explicit end time, or legal's `duration_minutes`). An end is never invented, even when a provider asks for one.
- **Types:**
  - `milestone` is a point: a key date, due date, deadline or decision point.
  - `event` is something someone attends, on one day or several, timed or untimed.
  - `span` is elapsed or waiting time.
  - Mapping: 5G's `milestone` and `deadline` become `milestone`, and its `review`, `meeting` and `event` become `event`. legal's `event_at` becomes `event`, and its other live fields become `milestone`.
- **Identity:**
  - **Form:** the UID is `<base-namespace>.<logical id>`. A registry entry keeps its existing `id`. An Item milestone is `<item_id>.<milestone key>`, where the key is logical (`due`, `event`, `decision`, `chase`, `review`, `target`) rather than the field name, and `due_at` takes precedence over `due_on` for the same obligation.
  - **5G:** its emitted UIDs are kept exactly, `<id>@phase3.5g-emerge.io`.
  - **Life cycle:** rescheduling keeps the UID. Removal, cancellation and becoming undated each have a defined effect on the projection.
  - **Provenance:** the source field is recorded separately from the UID.
- **Busy:** `busy: true` writes `TRANSP:OPAQUE` and `X-MICROSOFT-CDO-BUSYSTATUS:BUSY`; absent or false writes `TRANSP:TRANSPARENT` and `...:FREE`. These properties express intent. Whether a subscriber's scheduling tool honours them is unproven. An untimed busy item blocks the whole day. A timed busy item without a real end is the subject of decision 8. The rubric fails `busy: true` on a span or on a month- or year-precision item.
- **Firmness:**
  - **Values:** 5G's five, `confirmed`, `planned`, `target`, `proposed` and `to-confirm`, are the vocabulary. Each source maps into them through a reviewed mapping.
  - **Feed:** `confirmed` writes `STATUS:CONFIRMED` and every other value writes `TENTATIVE`.
  - **legal:** `hard: true` maps to `confirmed`. `hard: false` maps to nothing, so firmness stays absent rather than being inferred.
  - **Progress:** `open`, `waiting`, `overdue`, `done` and the like belong to the base. They stay out of the date core and are shown only as metadata carried from the source.
- **Precision:** 5G's rules stay. A month-precision item spans its month as a free placeholder titled "(day to be confirmed)". A year-precision item stays off feeds. A month placeholder is uncertainty, not a span, so the span rules do not reject it.
- **Time:**
  - **Zone:** each set declares one IANA zone. Timed items are converted to UTC at build, using the offset on the item's own date, not the build date's, and also write `X-WR-TIMEZONE` as metadata. A timestamp that already carries an offset stays that instant. Date-only values are never converted to UTC, and floating times are never written.
  - **Clock changes:** a local time that does not exist (Europe/London 2026-03-29 01:30) is rejected. An ambiguous one (2026-10-25 01:30) needs an explicit offset.
  - **Several sets:** an item in two sets keeps one instant, resolved in its source's zone.
  - **Library:** conversion may use the runtime's `Intl` rather than a hand-written library. The supported runtime is pinned.
- **Recurrence** is out of v1. Birthdays and renewals are authored as dated instances, and the tool never rolls them forward.

### One source

"One source" means one editable home per date. A base declares its source shape (a registry file, or dated frontmatter on named note types) and its calendar sets. The generator reads only what is declared and never scans prose (legal Guide line 187).

The audit is not a generator stamp. It checks a declared source manifest, regenerates deterministically and compares the result with the committed output, records provenance and schema version, and flags undeclared duplicate lists for a human to check. A failed or partial source read never produces an empty calendar. That matters most for sync, where an empty read would delete events.

### Sets, visibility and targets

- **Audience and target:** each set declares an audience, `public` or `private`. Each base declares its publication targets, and the visibility of each target. A path alone cannot tell you visibility: 5G's preview URLs have no Access bypass, while production does.
- **Refusal:** the generator refuses to write a private set to a public target.
- **Public feeds:** they carry an allowlist of fields, with the contact-detail test kept as a backstop. A public set with a site is served as static `.ics` at a permanent path, as 5G does.
- **Private sets:** they stay unpublished until a private adapter is proved (decision 1). Account sync and a capability URL are both disclosures, one to a provider and its delegates, the other to whoever holds the URL, so each needs Kris's explicit approval for each base.
- **Observatory:** the current Observatory cannot host a feed, because it listens on loopback only (README "Product boundary"). A future cross-base view there is ki.observatory's call.

### Views

The timeline view is generated from the same items.

- **On a site:** 5G's List (build-rendered), Months and Runway (browser-drawn) over the view JSON.
- **In a base:** a view of an existing live artifact where the base has one (legal, decision 7). Otherwise a live artifact pair under `ki-repo-kb-live-artifacts`, whose Markdown owns the view's descriptor, the sources it selects and its presentation. Generated data sections are labelled and rebuilt; they never become a new input.
- **On the timeline:** spans show as bars and milestones as marks.
- **Past and today:** classified in the set's declared zone, with reader-local time used only to display timed items.
- **Mermaid gantt:** it may remain one generated rendering until ki.observatory's Archify redraw (LGL-PRINCIPAL-OPS-028) decides otherwise.

### Skill and code

- **One skill**, name per decision 4, with standard, rubric and audit. It owns dated-item meaning and the projection contracts. Website rendering stays with `ki-repo-website-content`, base rendering with `ki-repo-kb-live-artifacts`, and provider input and output with the connector repositories.
- **Code** lives in the skill's `scripts/`, following `ki-diagrams/scripts/` (`build-html.ts`, `export-svg.ts`, `rubric/`, `shared/`). A pure core holds the model, validation and deterministic `.ics` and view-JSON projection. Separate modules hold the source readers and any provider adapter.
- **Dependencies:** the small `.ics` core stays dependency-free. Parsing YAML or JSON5 may reuse the harness's existing parsing.
- **5G:** it vendors the core with source provenance and a drift check run in its local `bun test`, since Workers Builds has no harness checkout.
- **No publication:** no npm package, and no `tools-ki` command unless a stable machine contract is later needed.

## Agreement and difference

| Point | Reviews | Settlement and evidence |
| --- | --- | --- |
| 1 | Fable Agree · Astra Add | Kept, with Astra's identity, precision and end rules added (Model, Dated item). |
| 2 | Agree · Agree | Kept; Fable's type mapping adopted. |
| 3 | Differ · Differ | Both read TIMELINE-IMPROVEMENTS correctly: "how a feed carries one, if at all" was left to design. Keeping spans off feeds becomes a v1 rule, not a reading of Kris's words. Whether to add an opt-in now is decision 2. |
| 4 | Agree · Add | Kept. Firmness needs a mapping for each source; `hard: false` maps to nothing (FR schema). |
| 5 | Agree+Add · Add | Both add the zero-duration case for a timed item with no end (RFC 5545 section 3.6.1, prior knowledge). Settled as "never invent an end"; legal's `duration_minutes` (Guide line 185) supplies real ends; the remaining choice is decision 8. |
| 6 | Agree · Differ | Astra upheld on evidence: `hard` and the `status` values in the FR schema do not map fully to firmness, and some progress is authored by hand. Progress stays out of the core and may be carried as presentation metadata. |
| 7 | Agree · Agree | Kept; a month placeholder is uncertainty, not a span. |
| 8 | Agree · Add | Kept, with clock-change handling, the item-date offset and the rule never to convert date-only values to UTC. Both rely on prior protocol knowledge; the client check sits in the private-adapter record. |
| 9 | Agree · Add | Kept; birthdays and renewals become dated instances with no roll-forward. |
| 10 | Agree · Agree | Kept. |
| 11 | Agree+Add · Add | Kept. The collapse becomes its own 5G record (Fable) and reconciles `seeAlso` and status wording (Astra; `industry-day-paris.json5`). |
| 12 | Agree+Add · Differ | Astra upheld: logical milestone keys with alias precedence, not field names (Guide line 173). Fable's `hearing_date` gap added. |
| 13 | Agree · Add | Kept; dates authored and checked by the owner, never inferred. |
| 14 | Agree+Add · Add | Kept, with audience separated from target and targets declared by the base (Fable: 5G preview URLs); the contact test is a backstop (Astra; `site.test.ts`). |
| 15 | Agree · Agree | Kept. |
| 16 | Agree (prior knowledge) · Differ | Settled as unverified. Both reviewers rely on prior knowledge only; Astra rightly refuses to treat it as established. A hands-on acceptance matrix goes into the private-adapter record before any promise to protect time. |
| 17 | Agree+Add · Differ | Neither connector can do it today (verified: gsuite create is timed-only and requires `end`, with no transparency or UID; m365 has no update tool and posts to `me/events` only). Private publication becomes a separate adapter that needs connector work (decision 1). Fable's bonus point stands as prior knowledge: a dedicated Google calendar has its own secret address, which would restore subscription on Kris's other devices. |
| 18 | Agree+Add · Agree | Kept as an option the base may choose (Fable), as bearer access that needs Kris's acceptance of the disclosure (Astra). |
| 19 | Agree · Add | Kept, limited to the current Observatory. |
| 20 | Differ · Add | Fable upheld for legal (Guide lines 209 and 230); Astra's split of what the Markdown owns adopted for bases without an artifact. Decision 7. |
| 21 | Agree · Differ | Astra upheld (Guide line 187): past and today classified in the set's zone. |
| 22 | Agree · Agree | One skill. Decision 3. |
| 23 | Agree+Add · Add | Both like `ki-key-dates`. Collisions corrected: Archify yes, `ki-diagrams` no, `Calendar/` zone yes; the ADR allows all three. Decision 4. |
| 24 | Agree+Add · Add | Kept, with Astra's core-and-adapter split and Fable's drift check in `bun test`. Decision 5. |
| 25 | Agree+Add · Differ | Astra upheld: a stamp proves nothing. Regeneration against a manifest, and a failed read never producing an empty output. |
| 26 | Agree+Add · Add | 5G pilot, after the harness skill exists (GOV-222 boundary): vendoring plus golden parity only, with a fixed build clock, UIDs, paths, anchors, escaping and folding kept. Decision 6. |
| 27 | Agree+Add · Differ | Compatible once combined: legal's local half early (read-only comparison, then a generated view inside the existing artifact), legal publication last. Decision 6. |
| 28 | Agree · Differ | Astra's order adopted for the private adapter: synthetic, then a small personal set Kris approves, then legal. personal's authoring can run at any time. Decision 6. |
| 29 | Agree · Agree | The harness owns KI-HARNESS-GOV-222. |
| Add | Fable | `DTSTAMP` changes on every build, so sync compares content, not stamps. Adopted for the sync adapter. |
| Add | Fable | Private items carry note title and `item_id`, never a filesystem path. Adopted. |
| Add | Fable | One hands-on client check. Adopted, widened to Astra's acceptance matrix, inside the private-adapter record. |
| Add | merge | legal's `duration_minutes` (Guide line 185) supplies real ends for timed events. |

## Rollout plan

Records are captured through `ki-next` from Kris's decisions, each stating them in its Context. Each receiving repository owns its own records.

1. **ki-agentic-harness: KI-HARNESS-GOV-222**, the skill itself: standard, rubric, audit, core scripts, both source readers and synthetic fixtures for every new rule (timed items, clock changes, aliases, spans, private refusal, failed reads). Moving it to `project: timelines` and setting its priority is the harness's call. This design sends it the decisions, not edits.
2. **5G Emerge, pilot**: vendor the core with provenance and a drift check, with golden parity at a fixed build clock. Feeds stay unchanged apart from `PRODID` (or kept through options) and the new busy properties. UIDs, feed paths and page anchors are kept. Only after GOV-222 is ready.
3. **5G Emerge, second record**: collapse `programme-model/timeline/` into the registry, reconciling `seeAlso` and the source wording.
4. **legal-principal, local half**: add `hearing_date` to the Guide or migrate it to `event_at`; set the milestone keys; compare read-only against the current FR Timeline; then generate the timeline as a view of the existing `legal-command-centre` artifact. The current Working Note and Mermaid gantt stay until legal's owner confirms the replacement is complete.
5. **mcp-gsuite and/or mcp-m365, connector records** (only if decision 1 picks account sync): all-day writes, transparency or `showAs`, a calendar selector, update by provider id, and a way to identify events the tool created.
6. **Private adapter**: the harness's sync runner as an Activity under `ki-repo-kb-activities`. It covers dry-run comparison, mapping provider ids to UIDs, sole ownership of the events it creates, safe removal, and comparing content rather than stamps. It is proved on a synthetic calendar, with the client acceptance matrix (Google and Microsoft; own, dedicated and subscribed calendars; free, busy, all-day and timed). Kris runs the matrix, or grants it explicitly, because it makes remote calls.
7. **personal-principal**: Kris authors dates into frontmatter. Then a small private set Kris approves becomes the adapter's first real use.
8. **legal-principal, sync half**: private publication, only after records 6 and 7 pass.

The pilot comes before any parallel wave, and its lessons are written into each later brief. Records 3 and 4 may run in parallel once the pilot is accepted.

## Decisions

1. **FEED-HOME - where a private base without a site publishes** - Options:
   - a) Keep private sets unpublished in v1, served by the base's generated view. Build account sync as a separate adapter, proved on synthetic and then personal data, after connector work, and use the provider calendar's own secret address for subscription on Kris's other devices.
   - b) Account sync now, as the brief proposed.
   - c) A capability URL on a public host, as an opt-in for each base.
   - d) A private feed host behind a token-checking Worker.

   Recommendation: a). The connectors cannot do sync today (verified), and the free/busy benefit is unproven. Kris's words, "can publish one or more calendar sets to subscribe to", are still honoured through the provider's secret address once proved.
2. **SPAN-FEED - spans in feeds** - Options:
   - a) Spans stay off feeds in v1. An end that matters becomes its own milestone, and the rubric fails a busy span.
   - b) As a), plus a per-set opt-in now that writes spans as free all-day blocks (Fable).
   - c) Feeds carry a span's two endpoints as free markers.

   Recommendation: a). Both reviews agree on off by default, it matches "a calendar with the milestones", and an opt-in can be added later without a model change.
3. **SKILL-SHAPE - one skill or two** - Options:
   - a) One skill that owns the item, the feeds and the view-JSON contract, with rendering left to the website and live-artifact skills.
   - b) A dated-items skill plus a view skill.

   Recommendation: a). Both reviews agree.
4. **SKILL-NAME** - Options:
   - a) `ki-key-dates`.
   - b) `ki-calendars`.
   - c) `ki-timelines`.

   Recommendation: a). It names the kept thing. `ki-calendars` would share a word with the `Calendar/` zone in every base and suggests busy-time calendars. "Timeline" is an Archify diagram type, though not a `ki-diagrams` one. Kris's own words, "a calendar with the milestones", keep b) a fair choice.
5. **CODE-HOME** - Options:
   - a) The skill's `scripts/` in the harness, a pure core plus separate adapters, which 5G vendors with a drift check in `bun test`.
   - b) A `ki` command in `tools-ki`.
   - c) A shared package through a workspace or a pinned Git reference.

   Recommendation: a). It follows the `ki-diagrams` precedent and Kris's shared-code preference, and both reviews agree.
6. **ADOPTION-ORDER** - Options:
   - a) The rollout plan above: the 5G parity pilot, then the 5G collapse and legal's local half, the private adapter proved on synthetic and then personal data, and legal's sync last.
   - b) The brief's order: 5G, then all of legal, then personal.
   - c) legal first.

   Recommendation: a). It keeps Kris's three adopters, delivers legal's time-critical view early without credentials, and keeps the first real provider write away from court dates.
7. **LEGAL-VIEW - where legal's generated timeline lives** - Options:
   - a) A view of the existing `legal-command-centre` artifact, with the Working Note and gantt kept until legal's owner confirms the replacement.
   - b) A generated Working Note, as today.
   - c) A new live artifact pair.

   Recommendation: a). The Guide forbids a second artifact (line 209), and the artifact already has a Calendar view (line 230).
8. **TIMED-BUSY - a timed busy item with no end** - Options:
   - a) The rubric requires a real end for a timed busy item, taken from the source (an end time, or legal's `duration_minutes`), and otherwise fails it.
   - b) Write it as an all-day busy item.
   - c) Allow it and write zero duration.

   Recommendation: a). It keeps "never invent a time or duration" while making `busy` mean something. b) would block a whole day for a short appointment, and c) blocks nothing.

## Models and runtimes

| Stage | Run | Model and runtime |
| --- | --- | --- |
| Survey | tl-seed | Claude Code, runtime default model (no model or effort recorded in its launch file) |
| Brief | tl-design | Claude Opus 5.5 on Claude Code, high effort |
| Review | tl-review-fable | Claude Fable 5.1 on Claude Code, high effort |
| Review | tl-review-astra | GPT-6 Astra on Codex, high effort; an earlier run on `gpt-6.1-sol` was stopped and discarded (MODEL-RUN) |
| Merge | tl-merge | Claude Opus 5.5 on Claude Code, high effort |

The merge runs on the same model as the brief. Independence rests on the two reviews and on re-reading the source for every dispute settled here.

## Changes after review

- Private publication moved from "account sync, ready" to "a separate adapter, proved before it is promised", and private sets stay unpublished in v1 (Astra on the connector gaps and on point 16; Fable on the costs of sync; verified against the connector code).
- Keeping spans off feeds is restated as a v1 rule, not a reading of Kris's words (Fable, Astra).
- UIDs are now logical keys with alias precedence, and 5G's `@host` suffix is kept (Astra).
- Clock-change handling, the item-date offset and the rule never to convert date-only values to UTC added (Astra); the zero-duration rule for timed busy items added (Fable, Astra), with `duration_minutes` found in the merge's re-read.
- `hard: false` no longer maps to tentative; progress may be carried as presentation metadata (Astra).
- "Today" is classified in the set's zone, not by the reader's clock (Astra; Guide line 187).
- legal's timeline becomes a view of its existing artifact (Fable; Guide lines 209 and 230); for other bases, what the live-artifact Markdown owns is defined (Astra).
- The audit moves from a generator stamp to regeneration against a manifest, and a failed read never produces an empty output (Astra).
- The 5G pilot is cut down to parity; the timeline collapse becomes a separate record that reconciles `seeAlso` (Fable, Astra).
- legal is split into a local half and a sync half, with the private adapter proved on synthetic and then personal data before legal publishes (Fable, Astra).
- Naming evidence corrected: Archify yes, `ki-diagrams` no, `Calendar/` zone yes (Fable, Astra).
- Brief fact corrections: the site test name, List view rendering, the UID host, the `FeedOptions` adapter surface (Fable, Astra).
