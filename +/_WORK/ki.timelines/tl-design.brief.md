# tl-design - ki-work-design run for the Timelines skill

You are a background agent for the ki.timelines work package in /Users/krisbrown/workspaces/knowledge-islands/ki-principal (`+/_WORK/ki.timelines/`). Read `work.md`, `decisions.md` and `design/survey.md` first, then load and follow the `ki-work-design` skill to shape the timeline and calendar skill: a design brief, independent reviews and one merged report, all committed under `+/_WORK/ki.timelines/design/`. Stop before the owner's decisions and the piloted rollout; return the open design choices as queries.

Settled by Kris on 19 October (see `decisions.md`, take them as fixed):

- The calendar is milestone-centred: key dates, due dates and milestones. A span (waiting on something, elapsed time for a piece of work) never takes busy time in a subscriber's calendar. Spans may show in the timeline view; how a feed carries one, if at all, is yours to propose.
- Per-item `busy`, default free, mapped to `TRANSP` and the client busy-status properties; firmness (legal's `hard`) is a separate field.
- One source: the dated items generate both the timeline view and the feeds; no second editable list of dates.
- Optional time of day per item and one time zone per calendar set; untimed items stay all-day; never invent a time or duration.

Open for the design (return each as a query with a recommendation): where a base without a site serves its feeds, private dates included (the base's own site, the Observatory, a private-feed host); one skill or a skill plus a view; the name (`ki-calendars`, `ki-timelines` or `ki-key-dates`); the code home (harness, `tools-ki` or a shared package); the adoption order for legal-principal, personal-principal and 5G Emerge.

Evidence: the 5G Emerge phase 3 component in /Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase3 (apps/site: src/_data/calendars.json5, lib/ics.ts, List / Months / Runway views); legal-principal in /Users/krisbrown/workspaces/legal/legal-principal (dated Items, the "FR Timeline to FDR" gantt); personal-principal in /Users/krisbrown/workspaces/personal/personal-principal; KI-HARNESS-GOV-222 at /Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-222-timeline-and-calendar-skill.md.

Authority: write only under `+/_WORK/ki.timelines/design/`; read anything else, change nothing else, including the 5G component, legal's gantt and the harness record. Commit your own paths by explicit path under `ki-git`, with `docs(work): ki.timelines design ...` subjects; do not push. Every query whose recommendation is medium or low confidence notes that the coordinator will send it for blind review.

**Report** to `/Users/krisbrown/.local/state/ki/agents/timelines/tl-design.report.md`, in the run's state folder and nowhere else, as an owner report: `# [Foundations](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/foundations.md) › [Timelines](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/timelines.md) › tl-design`, the bold line `**🤖 → 👤 Handoff to supervisor · Run report at <local time> · last mark 19:03 BST**`, one `---`, then `## Done`, `## In Progress` and `## Queries`, each query with **Context**, **Query** and lettered **Options**, `a) (recommended, confidence <level> - <reason>)` first, then the glyph banner with no send line. Run tools quietly and report each outcome in one line.
