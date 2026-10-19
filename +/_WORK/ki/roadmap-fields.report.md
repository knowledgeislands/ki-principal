# [Knowledge Islands](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Charter.md) › State of play › roadmap-fields

**🤖 → 👤 Handoff to supervisor · Run report at 13:30 BST · blocked**

---

## Done

- Diagnosis: all 18 records are correct as they stand. `priority` and `size` are supported fields in the harness [work-item format](/Users/krisbrown/.local/share/ki/harnesses/knowledgeislands/ki-agentic-harness/skills/change-management/ki-work-roadmap/references/standards-work-item-format.md) under [GDR-KI-PRINCIPAL-016](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/GDR-KI-PRINCIPAL-016-priority-and-size-on-work-records.md), and `size` is required on every open record. The diagnostic comes from `ki` 0.11.4: in `tools-ki/src/core/work/items.ts` neither field is in the allowed list, so any roadmap record carrying one is rejected. That lag is already captured as [KI-TOOL-KI-CLI-155](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-155-priority-and-size-fields.md), still in triage.
- apps-observatory.local: not changed. [KI-OBSERVA-APP-045](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-045-name-unregistered-territory-member.md) and [KI-OBSERVA-VIS-042](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-042-diagram-overlay-everywhere.md) carry a valid `size`. The `ki` check still reports both. No Messages line was sent to the obs-overlay worker, since there is nothing for it to fix. Nothing to push.
- ki-design: not changed. The `ki` check reports `priority` on all 15 records, KI-DESIGN-OBS-001 to KI-DESIGN-OBS-015, and the field is valid. Nothing to push.
- tools-mgit: not changed. [KI-TOOL-MGIT-CLI-028](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-028-learn-majority-output.md) carries a valid `priority`, and its `size` sits beside it. Nothing to push.

## In Progress

Nothing is running. Outstanding - no action requested now: these diagnostics will clear without any record edit once KI-TOOL-KI-CLI-155 lands in `ki`.

## Queries

### CLI-FIELDS - Fix the tool, not the records

**Context:** Stripping `priority` from the records, or `size` from all three repositories' records, would silence `ki` but go against GDR-KI-PRINCIPAL-016 and the harness format. It would also throw away values Kris set at capture, and the harness checker would then fail the open records for a missing `size`. The real fix is KI-TOOL-KI-CLI-155 in tools-ki. It adds both fields to `items.ts` and its roadmap tests, and is a size `s` to `m` change.

**Query:** Should the records stay as they are while KI-TOOL-KI-CLI-155 is adopted and run in tools-ki, or should the fields be stripped as a stopgap?

**Options:** a) (recommended, confidence high - checked against the standard, the decision and the `ki` source) Leave the records alone, and adopt and run KI-TOOL-KI-CLI-155 in tools-ki so that `ki` accepts `priority` and `size`. b) Strip `priority` and `size` from the 18 records now, which loses the captured values and breaks the harness check, and put them back once `ki` catches up.
