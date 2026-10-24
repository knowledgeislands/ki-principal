# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-next-sweep

**🤖 → 👤 Handoff to supervisor · Run report at 01:39 BST**

---

## Done

Read-only sweep; no file changed in any repository. Of the 22 Observatory records, only two can be moved forward tonight. Everything else is done or awaiting review, excluded, held behind an unmet condition, or touched by another session in the last 12 hours.

1. [KI-OBSERVA-VIS-022](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-022-judge-overdue-against-each-job-schedule.md), Overdue against job schedules (next, draft, size m, no priority, no blockers). Next move: plan it to Ready. Settle its three open choices as recommendations: read the schedule from the job's launchd property list, which Rig renders from `schedule-calendar` (Rig's JSON output does not carry schedules); pick a grace period; and decide that an unparseable schedule falls back to 26 hours with a stated reason. Confidence high: TRIAGE-NEXT-LATER a) promotes it only after its own planning, which is records-only, local and non-destructive, and acceptance is already written. The build after planning is medium, because reading property lists directly sits uneasily with AGENTS.md's consume-stable-contracts rule.
2. [KI-OBSERVA-OPS-003](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-OPS-003-observatory-serving-location.md), Observatory serving location (soon, draft, investigate, size m, no blockers). Next move: plan it to Ready, scoped to the written finding plus this repository's build-identifier and reload-offer half, with the Rig half described only. Confidence medium: the build-identifier half is self-contained and testable, but Kris called this "not a now thing" and the serving-location choice itself is his.

Not progressable (reason):
[KI-OBSERVA-BRG-004](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-004-turn-feedback-sending-on.md) waits for KI-HARNESS-GOV-219 (triage) and BRG-006 acceptance;
[KI-OBSERVA-VIS-042](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-042-diagram-overlay-everywhere.md) waits for KI-HARNESS-GOV-224 (triage);
[KI-OBSERVA-VIS-038](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-038-machine-instrument.md): its tool-storage phase waits for KI-HARNESS-GOV-227 (triage) and its consolidation phase for APP-044;
[KI-OBSERVA-VIS-032](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-032-library-instrument.md), [KI-OBSERVA-VIS-034](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-034-streams-instrument.md) and [KI-OBSERVA-VIS-045](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-045-workers-instrument.md) wait for APP-044 and then Kris's approval (VIS-045 was also captured by another session in the last 12 hours);
[KI-OBSERVA-INT-003](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-INT-003-extensions-switchboard.md) waits for VIS-041 acceptance and then Kris's approval of each phase;
[KI-OBSERVA-VIS-028](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-028-retire-sessions-readers.md) waits for the work migration's phase 5 and for VIS-027.
Excluded as briefed: VIS-030, VIS-027, BRG-005, APP-044, VIS-029 and OPS-004.
Awaiting review: APP-045, APP-046, BRG-006, VIS-041, VIS-043 and VIS-044.

ki-design has no open records in the Observatory lane; [KI-DESIGN-OBS-015](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-OBS-015-banner-glyphs-question.md) is awaiting review. Its open drafts belong to the ki-design lane: ART-002 is a licensing decision for Kris, and ELE-001, MAP-002 and TIL-002 make no reference to the Observatory.

## In Progress

Nothing. One loose end: obs-build-brg005.status has no DONE line and was last marked "held until obs-build-vis044 finish". OBS-CLAIM-FOUR dropped that run, so the coordinator may want to close it.

## Queries

**Context** KI-OBSERVA-OPS-003 sits at `soon`, and Kris said it is "not a now thing". Its build-identifier half is buildable without any machine change.
**Query** Should tonight's overnight authority cover planning KI-OBSERVA-OPS-003, or only KI-OBSERVA-VIS-022?
**Options** a) (recommended, confidence medium - planning is records-only, but it cuts against Kris's own timing) plan KI-OBSERVA-VIS-022 now and send KI-OBSERVA-OPS-003 to blind review as a medium recommendation; b) plan both to Ready tonight; c) plan KI-OBSERVA-VIS-022 only and leave KI-OBSERVA-OPS-003 untouched.
