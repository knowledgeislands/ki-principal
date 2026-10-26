# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-build-vis044

**🤖 → 👤 Handoff to supervisor · Run report at 00:29 BST · last mark 22:50 BST**

---

## Done

- [KI-OBSERVA-VIS-044 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/c1f008346dc085a0c25026ea5c9a08b383ef1d5b/docs/roadmap/KI-OBSERVA-VIS-044-commit-authors-in-tables.md) planned to Ready (`eebc3d7`), then delivered to Awaiting review (`6fa1837`), both committed locally and not pushed.
- The Repositories and Roadmap tables now have an `authors · 14d` column next to `workers` and separate from it. It lists the Git commit authors per repository, newest first, and links to Activity narrowed to that repository. On Roadmap each entry is marked `repo-level`.
- The data comes from Activity's existing reader and contract, which are unchanged, at the default window. The legend states three limits: only the latest 50 commits are covered, model co-authors are not shown, and authors are not workers.
- A dash's tooltip distinguishes a repository with no commits in the window from one whose commits all fall outside the latest 50. When Activity can't be read the column says `not observed`. The shell's workers chip is untouched.
- The column is dropped at 760 px. The Roadmap and Repositories sections of the operator guide are updated.
- Checks: `bun run test` pass (1,398 tests, 0 fail, including the layout and degraded checks) · typecheck pass · Biome and rumdl clean · browser smoke pass · roadmap audit FAIL=0 (3 older size warnings on other records).
- The local service was restarted and answers at <http://127.0.0.1:1675/>. Both tables read cleanly at 1,440 px and 760 px.

## In Progress

Nothing. VIS-044 is waiting for your acceptance review. I did not accept it myself.

## Queries

None.
