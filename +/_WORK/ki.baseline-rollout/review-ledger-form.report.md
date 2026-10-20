# [Foundations](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/foundations.md) › [Baseline rollout](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/baseline-rollout.md) › review-ledger-form

**🤖 → 👤 Handoff to supervisor · Run report at 23:52 BST · last mark 23:27 BST**

---

## Done

- [5g-emerge-apex](</Users/krisbrown/workspaces/humans-not-robots/5g-emerge-apex/docs/roadmap/_ISSUES.md>): exact superseded body confirmed; allocation GOV 2, HK 0, OPS 0, WEB 1; retained serials fit the ledger.
- [5g-emerge-demos](</Users/krisbrown/workspaces/humans-not-robots/5g-emerge-demos/docs/roadmap/_ISSUES.md>): exact superseded body confirmed; allocation CONTRACT 5, DBD 27, DEPLOY 1; retained serials fit the ledger.
- [5g-emerge-testbed](</Users/krisbrown/workspaces/humans-not-robots/5g-emerge-testbed/docs/roadmap/_ISSUES.md>): exact superseded body confirmed; allocation DATA 4, GOV 8, HK 15, OPS 5; retained serials fit the ledger.
- [apps-kris.me.uk](</Users/krisbrown/workspaces/personal/apps-kris.me.uk/docs/roadmap/_ISSUES.md>): exact superseded body confirmed; allocation last_id 0; retained serials fit the ledger.
- [apps-dafacts.org](</Users/krisbrown/workspaces/equal-remedy/apps-dafacts.org/docs/roadmap/_ISSUES.md>): exact superseded body confirmed; allocation last_id 0; retained serials fit the ledger.
- [er-agentic-harness](</Users/krisbrown/workspaces/equal-remedy/er-agentic-harness/docs/roadmap/_ISSUES.md>): exact superseded body confirmed; allocation last_id 23; retained serials fit the ledger.
- [apps-markhowarth.com](</Users/krisbrown/workspaces/valle-armonia/apps-markhowarth.com/docs/roadmap/_ISSUES.md>): exact superseded body confirmed; allocation last_id 4; retained serials fit the ledger.
- All three 5G-EMERGE ledgers have exactly the configured area codes; their area titles all fail the current title rule.
- [Checker control flow](/Users/krisbrown/.local/share/ki/harnesses/knowledgeislands/ki-agentic-harness/skills/change-management/ki-work-roadmap/scripts/rubric/contexts/roadmap-evidence.ts:360) confirms the knock-on error: an invalid title returns no configuration, and the ledger check then falls through to repository-wide validation.
- [Repair implementation](/Users/krisbrown/.local/share/ki/harnesses/knowledgeislands/ki-agentic-harness/skills/change-management/ki-work-roadmap/scripts/rubric/contexts/roadmap-drafts.ts:45) rewrites only an exact recognised superseded body and passes its parsed allocation unchanged to the canonical renderer.
- Read the local conventions and current reporting standard; no repository writes, commits, remote calls or conform commands were made.

## In Progress

Nothing is running.

Outstanding - no action requested now: repair execution remains with the owning repositories, subject to the current HOOKS-MIGRATION restriction and release readiness; neither conform execution nor the forthcoming release was tested in this read-only review.

## Queries

### LEDGER-FORM - Repair superseded issue ledgers

**Context:** All seven ledgers exactly match the recognised superseded form, retain sufficient allocations and need a body update. The three 5G-EMERGE ledgers already have the correct area codes: their apparent issuing-mode failures follow from the checker rejecting their slug-valued area titles. Retitle those areas before rechecking; do not convert their ledgers to repository-wide mode. The implementation preserves allocations when rewriting recognised superseded bodies. HOOKS-MIGRATION replaced HOOK-GUARD: the estate is moving to committed `.githooks` after the new release, and applied conform remains prohibited until ki.tools-burndown explicitly clears it. This review ran no conform command, including dry-run.

**Query:** Should the ledger repairs follow the area-title work and the migration-cleared conform route, or be hand-edited now?

**Options:**

a) (recommended, confidence high - exact legacy matches, matching area codes and allocation-preserving repair are directly verified) Include the three 5G-EMERGE ledger-body repairs in their planned [AREA-TITLES work](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.baseline-rollout/queries.md:51), keeping every area code and allocation. Repair the other four through a reviewed dry-run followed by applied conform only after ki.tools-burndown clears HOOKS-MIGRATION and confirms the release is ready, one repository at a time on your go. Re-audit each repository and verify allocations are unchanged.

b) Hand-edit all seven ledger bodies now under approved repository conformance records, preserving every allocation and including the three 5G-EMERGE area-title fixes; re-audit each repository. This avoids waiting for conform but requires manually reproducing the canonical body.

### 🤖 → 👤 Handoff to supervisor · since 23:52 BST

👤 1 with you

- [with you] LEDGER-FORM · supervisor · since 23:52 BST
