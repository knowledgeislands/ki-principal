# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.observatory/work.md) › obs-link-pins

**🤖 → 👤 Handoff to supervisor · Run report at 23:33 BST**

---

## Done

- Commit `b6bd1f9` in apps-observatory.local, local only, five records by explicit path, link targets and `updated_at` only, following fc1864d. Pinned to `22ea8dc`, where all six pruned files exist:
  - [KI-OBSERVA-BRG-004](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-004-turn-feedback-sending-on.md): one link to KI-OBSERVA-BRG-002.
  - [KI-OBSERVA-VIS-029](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-029-sessions-from-every-host.md): one link to KI-OBSERVA-VIS-023.
  - [KI-OBSERVA-VIS-033](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-033-waiting-for-you.md): one link each to KI-OBSERVA-VIS-024 and KI-OBSERVA-BRG-002.
  - [KI-OBSERVA-VIS-041](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-041-git-view-replaces-repositories.md): one link to KI-OBSERVA-INT-004.
  - [KI-OBSERVA-APP-044](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md): Workers now points to KI-OBSERVA-VIS-045, not KI-OBSERVA-VIS-031.
- Swept all records, including those shaped in caa4d63 and VIS-045 from 24c4bd8: no relative links to the six pruned records remain.
- Commit hooks: passed. `ki repo audit`: FAIL=0, with 14 pre-existing warnings (Husky hooks, size on three records) and none in the touched records.
- Not pushed. The service restart is not needed for a roadmap-only change.

## In Progress

Nothing.

## Queries

**Context:** The brief asked to pin two links in the done KI-OBSERVA-VIS-031, but af4d39d pruned that record before this run, so there is no file to edit. That prune also left relative links to KI-OBSERVA-VIS-031 that no longer resolve: [KI-OBSERVA-VIS-044](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-044-commit-authors-in-tables.md) line 22 and [KI-OBSERVA-VIS-030](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-030-known-lands-chart.md) line 40. They were outside this brief's six records, so I left them.
**Query:** Should the KI-OBSERVA-VIS-031 links be pinned too?
**Options:** a) (recommended, confidence high - same mechanical fix, and the pruned file is at af4d39d^) Pin both to `blob/af4d39d^`'s commit in one follow-up commit. b) Leave them as they are. c) Repoint the VIS-030 out-of-scope link to KI-OBSERVA-VIS-045 instead, which is a wording judgement.
