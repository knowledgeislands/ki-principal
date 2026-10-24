# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-overlay-review

**🤖 → 👤 Handoff to supervisor · Run report at 19:57 BST · last mark 19:02 BST**

---

## Done

**Recommendation: a, strengthened with content verification. Confidence: high.** Reason: content hashes can prove source/viewer agreement; dates and a viewer's presence on this Mac cannot.

Have rendering update the saved HTML and a portable receipt containing source and HTML hashes plus renderer identity together; make audit and the staged-snapshot commit check fail on missing or mismatched proof. Keep `last_checked` for the separate question of whether the diagram still describes its traced code.

The **Interactive** button should open saved viewers when their proof matches the current source and HTML, under the existing sandbox. Otherwise show stale/unverified and withhold the button until rebuilt. Apply the same verification to local builds; the Observatory remains read-only.

Evidence checked directly:

- Harness: all 12 manifest entries opt into committed HTML; [build-html.ts](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-diagrams/scripts/build-html.ts:95) explicitly finalizes and copies it. The audit checks file presence and traced-code history, while the commit hook has no viewer-sync gate.
- Phase 2 and Phase 3: checked both interactive-diagram guides, Eleventy configurations, overlay scripts and commit hooks; rendering is explicit and site builds copy saved HTML. Two tracked Phase 2 delivery receipts already contain source and HTML hashes, both verified against current bytes.
- [KI-OBSERVA-VIS-042](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-042-diagram-overlay-everywhere.md:16) is triage. Its proposed `last_checked` comparison cannot prove viewer freshness; [current local-viewer detection](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/evidence/src/diagrams.ts:179) checks location and file presence, without source matching.
- History check: no later source-content changes found across 12 harness and 17 site pairs; this does not prove their original renders matched. The reviewed tracked paths have no pending changes.

Commits: none created. Repository files unchanged; no network calls, rendering, tests or audit gates run.

## In Progress

Nothing is running.

## Queries

No outstanding queries.

### 🤖 → 👤 Handoff to supervisor · since 19:57 BST

👤 1 with you

- [with you] OVERLAY-COMMITTED blind review · supervisor · since 19:57 BST
