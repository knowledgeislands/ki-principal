# [KI](/Users/krisbrown/workspaces/knowledge-islands/ki-principal) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.observatory/work.md) › obs-audit-fix

**🤖 → 👤 Handoff to supervisor · Run report at 23:13 BST**

---

## Done

- Cause: a record change today, not a new rule. The 23:07 prune (`fa16595`) removed the done [KI-OBSERVA-APP-042 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/22ea8dcbf7fba0806f1370899cd506a6705c3741/docs/roadmap/KI-OBSERVA-APP-042-design-tokens-and-glyphs.md) without first clearing the `blocked_by` entries in three open records or pinning their links, unlike the earlier [KI-OBSERVA-APP-043 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/691b93814809b293f3b06fd6c5535dfea2cd5ce0/docs/roadmap/KI-OBSERVA-APP-043-shell-polish-without-regrouping.md) prune.
- Findings 1–2, [KI-OBSERVA-INT-003](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-INT-003-extensions-switchboard.md): the dependency doesn't exist and the link isn't reciprocal. Fixed by dropping [KI-OBSERVA-APP-042 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/22ea8dcbf7fba0806f1370899cd506a6705c3741/docs/roadmap/KI-OBSERVA-APP-042-design-tokens-and-glyphs.md) from `blocked_by`.
- Findings 3–5, [KI-OBSERVA-VIS-030](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-030-known-lands-chart.md): the dependency doesn't exist, the link isn't reciprocal, and an active item has a blocker that isn't done. Fixed the same way. The blocker was done before it was pruned.
- Findings 6–7, [KI-OBSERVA-VIS-041 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/c1f008346dc085a0c25026ea5c9a08b383ef1d5b/docs/roadmap/KI-OBSERVA-VIS-041-git-view-replaces-repositories.md): the dependency doesn't exist and the link isn't reciprocal. Fixed the same way.
- Body links to [KI-OBSERVA-APP-042 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/22ea8dcbf7fba0806f1370899cd506a6705c3741/docs/roadmap/KI-OBSERVA-APP-042-design-tokens-and-glyphs.md) in those three records, and the one in the done [KI-OBSERVA-VIS-031 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/24c4bd8bfb1956c5ee9e0e2beef846bd06e298a5/docs/roadmap/KI-OBSERVA-VIS-031-who-is-working.md) (a link-only change), now point to its last revision on origin/main (`02cb729`). This matches the earlier [KI-OBSERVA-APP-043 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/691b93814809b293f3b06fd6c5535dfea2cd5ce0/docs/roadmap/KI-OBSERVA-APP-043-shell-polish-without-regrouping.md) pin. The three open records got a new `updated_at`. No scope, status or record was changed or deleted.
- Commit `fc1864d` `fix(roadmap): drop pruned KI-OBSERVA-APP-042 from blocked_by and pin its links`, local only and not pushed. The commit hooks passed.
- `ki repo audit` now passes with 0 failures. The 24 warnings that were already there remain (record `size`, the Husky hooks, `.rumdl.toml` drift and the CI pin).

## In Progress

Nothing.

## Queries

No outstanding queries.
