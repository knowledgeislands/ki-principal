# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-review-5

**🤖 → 👤 Handoff to supervisor · Run report at 01:17 BST · last mark 22:50 BST, 19 October**

---

## Done

- Recommend **c) Shorten it to commits older than the earlier five**, where those lists are visible. Keep the existing ten when there are no unpushed commits. When the new lists already cover all ten, omit the third list altogether.
- **Confidence: medium** - this removes duplicate rows while preserving the existing history depth; the best presentation remains a design judgement.
- The ten are not wholly redundant. With one to four unpushed commits, they include four to one older commits absent from the new lists. With no unpushed commits, both new lists are hidden, making the ten the only visible history. Dropping them alone would remove history from synchronised branches and branches without an upstream. See the [panel visibility and rendering](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/instruments/src/repositories.ts:732) and [history splitting](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/evidence/src/repositories.ts:387).
- Factual qualification to the brief: the earlier five are not always displayed. The overlap exists when unpushed commits are present; it does not make the ten redundant in every branch state.
- Factual correction to the [Review](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-041-git-view-replaces-repositories.md:165): splitting a log at the ahead count is not generally equivalent to selecting commits by upstream reachability. That equivalence needs the unpushed commits to form the log's leading segment, which merged histories need not guarantee. The [reader](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/evidence/src/repositories.ts:410) does not establish that condition.
- Read-only checks: six exact source predicates and representative ahead-count cases passed. No test suite run, repository files changed, commits created or remote calls made.

## In Progress

Nothing running. This review does not implement or accept a change.

## Queries

None. The recommendation returns TEN-COMMITS to the supervisor for disposition.
