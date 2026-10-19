# Timelines skill: brief

**Owner:** Kris Brown · **Owning repository:** knowledgeislands/ki-principal, work `ki.timelines` · **Date:** 2026-10-19

The design is held by the Project work `ki.timelines`, in `+/_WORK/ki.timelines/design/`. The survey beside this brief, [survey.md](survey.md), carries the facts in full; this brief cites it rather than repeating it. Paths are absolute where they leave this repository. Case content from legal-principal is not reproduced.

## Problem

Knowledge bases keep dates in four incompatible ways. 5G Emerge phase 3 has a working calendar component, a registry of calendar sets with subscribable `.ics` feeds and three views, but a second, unlinked list of the same eleven milestones beside it. legal-principal keeps dated fields on Command Centre Items and hand-generates a timeline note with a Mermaid gantt and a JSON copy, with no feed. personal-principal keeps renewal, expiry and travel dates in prose. No harness skill governs any of it, so each base reinvents the date model, the feed and the view, and none states whether an item should take busy time in a subscriber's calendar: the one feed that exists writes every event as free.

## Owner's proposal

Kris, 19 October 2026, TIMELINES-OPEN ([decisions.md](../decisions.md)):

> Scope: a timeline and calendar skill extracted from the 5G Emerge phase 3 calendar component (apps/site: src/_data/calendars.json5, lib/ics.ts, List / Months / Runway views, subscribable .ics feeds), starting from KI-HARNESS-GOV-222 in ki-agentic-harness. Each knowledge base keeps key dates, due dates and milestones and can publish one or more calendar sets to subscribe to; each item states its busy status (today every event is written as free); where subscriptions are homed is open; decide whether the programme timeline and the calendar registry share one source. First adopters: legal-principal (the "FR Timeline to FDR" gantt, kept as Mermaid until this lands), personal-principal, 5G Emerge. ... I have improvements to make to it; ask me for them.

Kris, 19 October 2026, TIMELINE-IMPROVEMENTS:

> the only improvement to the timeline were that we had the ability where you were waiting for things, or whatever the span is, that that shouldn't take up busy time as such in your calendar. So, yeah, it's more that we want a calendar with the milestones than it is that we want a calendar with, you know, kind of elapsed time to do some particular piece of work.

Kris, 19 October 2026, QUERIES-AGREED: "Everything else is high confidence, so let's just get on with it." Taken as settled, and fixed for this design:

- **Milestone-centred.** The calendar carries key dates, due dates and milestones. A span (waiting on something, elapsed time for a piece of work) never takes busy time in a subscriber's calendar; spans may show in the timeline view.
- **Busy status.** Per-item `busy`, default free, mapped to `TRANSP` and the client busy-status properties; firmness is a separate field.
- **One source.** The dated items generate both the timeline view and the feeds; no second editable list of dates.
- **Date model.** Optional time of day per item and one time zone per calendar set; untimed items stay all-day; never invent a time or duration.

Open for this design: where a base without a site serves its feeds, private dates included; one skill or a skill plus a view; the name; the code home; the adoption order.

## Established facts

- The 5G registry, [calendars.json5](/Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase3/apps/site/src/_data/calendars.json5), holds six calendar sets; only `phase3-programme` has entries (eleven). Calendar fields: permanent `id`, `title`, `description`, `group`, `code`, `colour`, `entries`. Entry fields: permanent `id` (the UID), `start` at day, month or year precision, inclusive `end` (day precision only), `kind` (milestone, deadline, review, meeting, event), firmness `status` (confirmed, planned, target, proposed, to-confirm), `sourceStatus`, `description`, `scenarios`, `tracks`, `sources`. The header states "Never invent a date". - registry header comment, lines 1-36.
- Two 5G entries are multi-day events with an `end` (JCB (UK) 3-4 November, IPC (UK) 24-25 November 2026), both `kind: review`; they are occurrences someone attends, not elapsed spans. - registry lines 104-120.
- [ics.ts](/Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase3/apps/site/lib/ics.ts) is dependency-free and writes all-day events only; month-precision entries span their month titled "(day to be confirmed)"; year-precision entries stay off the feed; every event is `TRANSP:TRANSPARENT`; `STATUS` is `CONFIRMED` for confirmed firmness and `TENTATIVE` otherwise; the only 5G-specific string is the `PRODID`. - `ics.ts` lines 10-204; survey section 1.
- [calendars.ts](/Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase3/apps/site/lib/calendars.ts) holds the general view logic (month grouping, merged agenda, next and upcoming, subscribe links, view JSON); the List, Months and Runway views render in browser JavaScript over that JSON, and "today" is the reader's own date. - survey section 1.
- 5G's eleven programme timeline files under `src/_data/programme-model/timeline/` repeat the eleven registry entries with free-text dates (for example "15 Oct 2026") and the source's status words; nothing links the two. - survey section 1; `timeline/weekly-phase-3-consortium-call.json5`.
- 5G's site sits behind Cloudflare Access, but `phase3.5g-emerge.io/calendars/*` is a public bypass so calendar clients can subscribe without signing in; the smoke suite fails a build whose feeds carry an email address. - [cloudflare.md](/Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase3/docs/guides/developer/cloudflare.md) lines 50-70.
- legal-principal's [Command Centre Guide](</Users/krisbrown/workspaces/legal/legal-principal/Pillars/Command Centre/Command Centre Guide.md>) fixes the dated frontmatter fields on Items (`due_at`, `due_on`, `event_at`, `decision_by`, `chase_at`, `review_on`, `target_on`, plus historical `requested_on`, `overdue_since`, `completed_on`), forbids scanning prose for dates, displays timestamps in `Europe/London`, allows several labelled milestones on one Item, and makes Item frontmatter the only mutable feed for derived views. - "Dates and calendar semantics" and "Derived-view contract" sections.
- legal's "FR Timeline to FDR" note is a generated view with a Mermaid gantt and a JSON copy (`fr-timeline/1`) whose rows carry optional `time`, `end_date`, `lane`, `kind` (including `waiting-on-other-side`), `hard` and a progress `status`. Most "waiting on other side" rows are a single date by which another party should act, not a stretch of time. - the note's kinds key and table, lines 114-157; survey section 3.
- personal-principal has no structured future-date field; renewal, expiry, birthday and travel dates sit in prose. - survey section 3.
- No harness skill governs kept dates, feeds or timelines; `ki-diagrams` carries generator scripts inside the skill (`scripts/build-html.ts`); `ki-repo-kb-live-artifacts` governs Markdown-source plus rendered-HTML pairs in a base. - `ki-agentic-harness/skills/governance/ki-diagrams/scripts/`; `skills/repo-structure/ki-repo-kb-live-artifacts/SKILL.md`; survey section 4.
- The Observatory is local-first: its backend binds only the loopback address and the browser receives path-free evidence. - [apps-observatory.local README](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/README.md), "Product boundary".
- `mcp-gsuite` can list and edit Google Calendar events behind an access-level gate; `mcp-m365` can create and cancel Outlook calendar events. - each repository's README.
- [ADR-KI-HARNESS-SKILLS-003](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/decisions/ADR-KI-HARNESS-SKILLS-003-dependency-order-for-multi-skill-composition.md) sets the grammar `ki-<concern>[-<technology>]`, a plural concern for a collection or repeated unit; none of `ki-calendars`, `ki-timelines` or `ki-key-dates` exists among the harness's skills. - "Naming grammar"; `ls skills/*/`.
- Kris's standing preference for shared code: check its distribution first and prefer a vendored canonical copy with a drift check, a pinned Git reference or an existing workspace; ask before publishing to a public registry. - user configuration, "Cross-project preferences".

## Reflection

### The item model

1. The unit is the **dated item**: a permanent id, a title, one date or date-and-time, optional inclusive end, a type, firmness, `busy`, optional description and source citation, and the calendar sets it belongs to. Everything else (views, feeds, the gantt) is generated from it.
2. The item has three **types**, because Kris's span rule needs the line drawn in the data, not inferred: `milestone` (a point: key date, due date, deadline, decision point), `event` (an occurrence someone attends, one day or several, untimed or timed, such as 5G's JCB on 3-4 November) and `span` (elapsed or waiting time between two points). 5G's `kind` and legal's `kind` and `lane` survive as a free per-base **category**, not as the type.
3. A `span` is **never busy and never a feed event**; it appears only in timeline views. Where a span's end matters (a reply due, a report expected), that end is its own `milestone` item, which may be in a feed. The rubric fails `busy: true` on a span. This reads Kris's rule as "spans are timeline furniture, milestones are calendar content".
4. Legal's "waiting on other side" rows are mostly milestones in this model (a date by which someone else should act), with firmness from `hard`; only the stretch before them is a span, and legal need not record it.
5. **Busy** maps as settled: `busy: true` writes `TRANSP:OPAQUE` and `X-MICROSOFT-CDO-BUSYSTATUS:BUSY`; absent or false writes `TRANSP:TRANSPARENT` and `X-MICROSOFT-CDO-BUSYSTATUS:FREE`. An untimed busy item blocks the whole day, which is the stated all-day blocking rule KI-HARNESS-GOV-222 asked for; no duration is ever guessed to narrow it.
6. **Firmness** stays separate and keeps 5G's five values (`confirmed`, `planned`, `target`, `proposed`, `to-confirm`), mapping to `STATUS:CONFIRMED` for confirmed and `TENTATIVE` otherwise; legal's `hard: true` reads as `confirmed`. Progress (`open`, `waiting`, `overdue`, `done`) is the base's own state and not part of the dated item, because it is derived from "today" and from the owning record.
7. **Precision** keeps 5G's day, month and year, with its feed rules (month spans the month as a free all-day block titled "(day to be confirmed)", year stays off the feed). A month-precision item is never busy, for the same reason a span is not.
8. **Time.** An item may carry a local time of day and, for an event, an end time; the calendar set declares one IANA time zone (legal: `Europe/London`). Timed items are written with that zone; untimed items stay `VALUE=DATE`. Feeds write timed instants as UTC computed at build from the set's zone, so no hand-written `VTIMEZONE` is needed; the set's zone also goes in `X-WR-TIMEZONE`. Reviewers should test this against client behaviour.
9. **Recurrence is out** of the first version: no `RRULE`. 5G's "weekly consortium call" is recorded as one dated instance today, and recurring obligations already belong to `ki-work-recurring`.

### One source

10. "One source" means **one editable home per date, not one file format**. The skill defines the dated-item model and two source shapes that produce it: a **registry file** (5G's shape, for programmes whose dates have no other home) and **dated frontmatter on the owning note** (legal's shape, where each date belongs to an Item or subject note). A base declares its source shape and its calendar sets; the generator reads the declared source and nothing else, and never scans prose.
11. In 5G the registry stays the source, and the eleven `programme-model/timeline/` files collapse into it: the timeline page is generated from the registry, carrying `sourceStatus` for the source's words. That change is 5G's own work at adoption.
12. In legal the Item frontmatter stays the source, each labelled field (`due_on`, `event_at` and the rest) becoming one dated item with UID `<item_id>.<field>`; `fr-timeline.json` and the gantt become generated outputs, not a second list. The Command Centre Guide's derived-view contract already says this; the skill adopts it.
13. In personal-principal the first step is **authoring**, not extraction: move the dates that matter (vehicle tax, MOT, insurance, renewals, birthdays, travel) from prose into frontmatter on their notes. Nothing is inferred from prose by a tool.

### Feeds and their homes

14. A calendar set has a **visibility**: `public` (anyone with the URL), `private` (the owner only). The generator refuses to write a private set to a public target, and the 5G smoke check for personal data generalises to every public feed.
15. A base **with a site** serves its public sets as static `.ics` at a permanent path, as 5G does, behind an Access bypass where the site is gated.
16. Subscribed calendars generally do not count towards the subscriber's own free/busy in Google Calendar or Outlook scheduling; `TRANSP` then changes only how the event is drawn. A busy status that actually protects time needs the item written into the owner's own calendar. Reviewers should check this claim against current client documentation; much of the busy-status design leans on it.
17. For a **private** base with no site (legal, personal), recommend a second publication target, **account sync**: write the private sets into a dedicated calendar in the owner's own Google or Microsoft account through the existing `mcp-gsuite` or `mcp-m365` servers, keyed by UID so a re-run updates rather than duplicates. Nothing private reaches a public URL, and `busy` takes real effect. Its cost is a write-capable credential and a run that keeps the calendar current.
18. A **capability URL** (an unguessable feed path on a public host, the "secret address" pattern) is the alternative for private sets. It keeps the subscribe model Kris named but exposes everything to anyone who obtains the URL, which is the wrong default for court dates.
19. **The Observatory cannot serve feeds**: it binds loopback only, so no phone or hosted calendar client could reach it. It may later show a cross-base timeline as an Instrument, which is ki.observatory's call.

### Views

20. The **timeline view** is a generated output with two renderings: on a site, the extracted List, Months and Runway views over the view JSON; in a base, a live artifact pair under `ki-repo-kb-live-artifacts` (Markdown source plus rendered HTML), replacing hand-generated notes such as legal's gantt. The Mermaid gantt may remain one generated rendering until ki.observatory's Archify redraw decides otherwise.
21. Spans render in the timeline view as bars between their points; milestones render as marks; past items are marked against the reader's own today.

### Skill shape, name and code home

22. **One skill**, not a skill plus a view skill: the view is an output contract of the same model, and a second skill would split one concern. The site rendering stays under the site's own stack (`ki-repo-website-content`), and the base rendering under `ki-repo-kb-live-artifacts`, each consuming the view JSON.
23. **Name `ki-key-dates`.** It names the kept thing that the one-source rule makes canonical; `ki-calendars` invites the busy-time calendar Kris set aside, and `ki-timelines` collides with the timeline diagram type `ki-diagrams` and Archify already own. The plural concern fits ADR-KI-HARNESS-SKILLS-003's rule for a collection.
24. **Code home: the skill's own `scripts/`** in the harness, as `ki-diagrams` carries `build-html.ts`: the item model, source readers, rubric, feed builder and view JSON in dependency-free TypeScript, run by bases through the skill. 5G vendors the feed builder and view logic with a drift check rather than taking a package, under Kris's shared-code preference; `tools-ki` gains a command only if a stable machine contract is later needed. No npm publication.
25. The skill carries a **standard, rubric and audit**: every dated item valid, no busy span or busy month-precision item, no private set on a public target, no second editable list (a generated view without its generator stamp fails), UIDs permanent.

### Adoption

26. **Pilot in 5G Emerge**: extraction with parity, golden-tested so the feeds are unchanged apart from `PRODID` and the new busy properties, plus the timeline collapse. It is the lowest-risk proof that the extracted code is the same code, and its host already exists.
27. **Then legal-principal**: the frontmatter source shape, times, spans, private sync and the generated timeline replacing the hand-made one; it carries the most time-critical value (dates through February 2027).
28. **Then personal-principal**: authoring dates into frontmatter first, then private sync.
29. KI-HARNESS-GOV-222 is the harness's record; moving it from `project: observatory` to `project: timelines`, its priority and its plan stay the harness's call. This design hands it the decisions, not edits.
