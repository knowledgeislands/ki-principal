# tl-review - blind review of four ki.timelines queries

You are a blind reviewer for the ki.timelines work package in /Users/krisbrown/workspaces/knowledge-islands/ki-principal (`+/_WORK/ki.timelines/`), under the ki-coordination standard's Query review section. You are read-only: write nothing except your report. Do not read `+/_WORK/ki.timelines/queries.md` or `state.md`, which carry the coordinator's recommendations; stay blind to them.

Evidence you may check directly: the survey `+/_WORK/ki.timelines/design/survey.md`; the 5G Emerge phase 3 calendar component in /Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase3 (apps/site: src/_data/calendars.json5, lib/ics.ts, the List / Months / Runway views, programme timeline files); legal-principal's dated Items and "FR Timeline to FDR" gantt in /Users/krisbrown/workspaces/legal/legal-principal; personal-principal in /Users/krisbrown/workspaces/personal/personal-principal; KI-HARNESS-GOV-222 in /Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/Streams/Roadmap/. Project scope: a timeline and calendar skill extracted from the 5G component; each knowledge base keeps key dates, due dates and milestones and publishes subscribable calendar sets; first adopters legal-principal, personal-principal and 5G Emerge.

For each query below, check what you can directly, then give your own recommended option (an existing letter, or a new course of your own), a confidence of high, medium or low, and a one-line reason. Say what you verified directly and what you took from the survey.

## FEED-HOME - Where calendar feeds are served

Context: 5G serves its subscribable feeds from its own Cloudflare site, with an Access bypass on `/calendars/*`. legal-principal and personal-principal have no site, and their dates are private. Query: Where should a knowledge base with no site serve its calendar feeds? Options: (x) decide now that each base serves its feeds from its own site; (y) leave it open for the design run, with the base's own site, the Observatory and a private-feed host as candidates.

## BUSY-STATUS - Busy status: values and default

Context: 5G writes every event as free and holds dates only. legal holds some times of day and marks some dates `hard`. Query: Should busy status be a per-item field that defaults to free, with all-day items blocking time only when marked as blocking? Options: (x) default to busy for deadlines and events, free otherwise; (y) per-item `busy` defaulting to free, mapped to `TRANSP` and the client busy-status properties.

## ONE-SOURCE - One source for timeline and calendar list

Context: 5G holds the same 11 milestones twice, as structured registry entries and as free-text programme timeline files, unlinked. legal generates its timeline from the dates on its Items. Query: Should one structured source feed both the timeline view and the calendar feeds? Options: (x) keep two lists and link them by entry id; (y) one source, the dated items, generating both the timeline view and the feeds.

## DATE-MODEL - Dates only, or times and a time zone too

Context: 5G holds dates only, with no time zone. legal's rows carry an optional `HH:MM` time and a file-level time zone. Query: Should the skill model an optional time of day and a time zone? Options: (x) dates only, keeping a time as a label as the Command Centre does with `due_time`; (y) optional time per item and one time zone per calendar set, items without a time staying all-day.

**Report** to `/Users/krisbrown/.local/state/ki/agents/timelines/tl-review.report.md` and nowhere else: a `# KI > Foundations > Timelines › tl-review` heading, then one `##` section per query with your option, confidence, reason and what you verified. Run tools quietly and keep the report short.
