# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-timeline

**🤖 → 👤 Handoff to supervisor · Run report at 08:49 BST**

---

## Done

- Captured [KI-HARNESS-GOV-222](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-222-timeline-and-calendar-skill.md) as a triage record. It quotes Kris's DIAGRAM-GANTT words, names the candidates `ki-calendars`, `ki-timelines` and `ki-key-dates` under ADR-KI-HARNESS-SKILLS-003, names legal-principal (the `FR Timeline to FDR` gantt), personal-principal and 5G Emerge as first adopters, and leaves where subscriptions are homed as an open question. Priority and size are left for the harness to set.
- Commits `3149690f` (reserves the number in the ledger) and `7ed13f9c` (the record) were pushed fast-forward to `origin/main`. Only my own commits were pushed.
- Roadmap audit: no failures, after I fixed my ledger edit. The 19 warnings are all from the fleet-wide migration window asking each record to declare a size. One of them is about the new record, because its size is left unset on purpose.
- Component survey (read-only, nothing changed): it lives in `apps/site` of 5g-emerge-phase3. Dates are kept in one data registry, `src/_data/calendars.json5`, which holds six calendars. Each entry has a permanent id and a date at day, month or year precision, plus a kind, how firm the date is, and its sources. No date is ever invented.
- The component renders a page for each calendar and a landing page with List, Months and Runway views.
- `lib/ics.ts` publishes one subscribable RFC 5545 `.ics` feed per calendar, with webcal, Google and Outlook subscribe links. Feeds hold all-day events only, refresh every 12 hours, and are still valid when empty.
- Busy status is not modelled: every event is written as `TRANSP:TRANSPARENT`, so it shows as free. Kris's improvement would add a busy status to each item and map it to the feed. Any item that should block time would also need start and end times or a stated all-day rule.
- The programme timeline under `programme-model/timeline/` is a second date list, kept separately from the calendar registry. The record asks the extraction to decide whether one source should feed both.

## In Progress

Nothing is running.

## Queries

No outstanding queries
