# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.observatory/work.md) › obs-answers-2

**🤖 → 👤 Handoff to supervisor · Run report at 20:12 BST · last mark 20:12 BST**

---

## Done

- [KI-OBSERVA-APP-044](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md): no longer retires PDR-KI-OBSERVA-002's 760 px rule or width test; retiring them is now out of scope, DESIGN-NARROW a) stands, LARGE-SCREEN-REVISIT read back.
- [KI-OBSERVA-BCN-008](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BCN-008-beacon-signal-anatomy.md), [KI-OBSERVA-VIS-030](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-030-known-lands-chart.md), [KI-OBSERVA-VIS-031](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-031-who-is-working.md): LARGE-SCREEN text reworded to "first for large screens, not only"; rule and test kept, new tables declare survivors and drops, nothing working removed.
- [KI-OBSERVA-VIS-042](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-042-diagram-overlay-everywhere.md): the Interactive button opens a viewer only on a matching hash receipt, else shows it stale, for committed and locally built viewers alike; open question replaced by OVERLAY-SYNC; depends on [KI-HARNESS-GOV-224](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-224-diagram-viewer-receipts.md), linked.
- Commit 9f56976 on main, local only; `ki repo audit` on the roadmap FAIL=0 with the 15 warnings already there; rumdl clean. Service not restarted, as briefed.

## In Progress

Nothing.

## Queries

**Context:** PDR-KI-OBSERVA-002's width test requires every instrument that renders a table to declare which columns survive and which drop at 760 px. Keeping the test means every new table still pays that cost, which sits a little against "narrow layouts only where cheap". I left the requirement unchanged and wrote it into the records.
**Query:** Should new tables keep declaring their dropped columns, or may a new table opt out of the declaration?
**Options:** a) (recommended, confidence medium - one line per table is cheap and keeps the test whole) keep the requirement as it is · b) let a new table declare "no narrow plan", which the test accepts while still enforcing no horizontal scroll · c) decide when the first consolidation is delivered
