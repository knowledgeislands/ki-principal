# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-vis041-unpushed

**🤖 → 👤 Handoff to supervisor · Run report at 01:24 BST**

---

## Done

- The review's claim holds. In a temporary repository, a branch with one local commit that then merged a newer upstream commit was 2 ahead. Splitting the log at 2 listed the merge and the upstream commit as unpushed and left the local commit out. `git log @{upstream}..HEAD` listed the merge and the local commit.
- The repository detail now reads unpushed commits by reachability with `git log -<ahead, at most 50> @{upstream}..HEAD`. Earlier commits are the five newest of the rest of the recent log. That second read runs only when the branch is ahead of an upstream, so a branch with no upstream behaves as before. The ten-commit list is unchanged (TEN-COMMITS is still with Kris). There is no git-bridge path for history: the audit bridge reports counts only, so the read goes through the same process port as the detail's existing reads. A failure is reported by exit code, as the log read already does.
- Added a real-repository regression test for the merge case. Updated the split unit test, the mocked detail tests and the site's HTTP boundary test, which now expects two log reads.
- Corrected the [KI-OBSERVA-VIS-041 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/c1f008346dc085a0c25026ea5c9a08b383ef1d5b/docs/roadmap/KI-OBSERVA-VIS-041-git-view-replaces-repositories.md) sentence. It sits under Outstanding concerns in the Review section, line 155, not at line 165. The record stays at Awaiting review.
- Commit `86f2a13` `fix(evidence): select unpushed commits by upstream reachability`, local only, not pushed.
- Tests: pass. Typecheck: pass. Biome lint: pass. Roadmap audit: no failures; 3 warnings about missing `size` on VIS-027, VIS-028 and VIS-030, all from before this run.
- Service restarted as the brief asked. `http://127.0.0.1:1675/` answers 200. Repository AGENTS.md says a detached run never restarts the service, so I treated the brief's explicit step as the authority for this restart.

## In Progress

- Nothing.

## Queries

- None.
