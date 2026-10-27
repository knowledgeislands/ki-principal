# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.observatory/work.md) › obs-answers-2

**🤖 → 👤 Handoff to supervisor · Run report at 20:12 BST · last mark 20:12 BST**

---

## Done

- [KI-OBSERVA-APP-044](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md): no longer retires [PDR-KI-OBSERVA-002](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/decisions/PDR-KI-OBSERVA-002-observatory-design-language.md)'s 760 px rule or width test; retiring them is now out of scope, DESIGN-NARROW a) stands, LARGE-SCREEN-REVISIT read back.
- [KI-OBSERVA-BCN-008 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/22ea8dcbf7fba0806f1370899cd506a6705c3741/docs/roadmap/KI-OBSERVA-BCN-008-beacon-signal-anatomy.md), [KI-OBSERVA-VIS-030 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/0966ac3e/docs/roadmap/KI-OBSERVA-VIS-030-known-lands-chart.md), [KI-OBSERVA-VIS-031 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/24c4bd8bfb1956c5ee9e0e2beef846bd06e298a5/docs/roadmap/KI-OBSERVA-VIS-031-who-is-working.md): LARGE-SCREEN text reworded to "first for large screens, not only"; rule and test kept, new tables declare survivors and drops, nothing working removed.
- [KI-OBSERVA-VIS-042 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/20061964d6e424dac55199dc393653fecc774299/docs/roadmap/KI-OBSERVA-VIS-042-diagram-overlay-everywhere.md): the Interactive button opens a viewer only on a matching hash receipt, else shows it stale, for committed and locally built viewers alike; open question replaced by OVERLAY-SYNC; depends on [KI-HARNESS-GOV-224 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/7378f88a323454339ae61bab6bd1bdb03104a8eb/docs/roadmap/KI-HARNESS-GOV-224-diagram-viewer-receipts.md), linked.
- Commit 9f56976 on main, local only; `ki repo audit` on the roadmap FAIL=0 with the 15 warnings already there; rumdl clean. Service not restarted, as briefed.

## In Progress

Nothing.

## Queries

**Context:** [PDR-KI-OBSERVA-002](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/decisions/PDR-KI-OBSERVA-002-observatory-design-language.md)'s width test requires every instrument that renders a table to declare which columns survive and which drop at 760 px. Keeping the test means every new table still pays that cost, which sits a little against "narrow layouts only where cheap". I left the requirement unchanged and wrote it into the records.

**Query:** Should new tables keep declaring their dropped columns, or may a new table opt out of the declaration?

**Options:** a) (recommended, confidence medium - one line per table is cheap and keeps the test whole) keep the requirement as it is · b) let a new table declare "no narrow plan", which the test accepts while still enforcing no horizontal scroll · c) decide when the first consolidation is delivered
