# [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.observatory/work.md) › obs-build-vis043

**🤖 → 👤 Handoff to supervisor · Run report at 00:06 BST**

---

## Done

- [KI-OBSERVA-VIS-043 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/c1f008346dc085a0c25026ea5c9a08b383ef1d5b/docs/roadmap/KI-OBSERVA-VIS-043-review-queue-reads-queries.md) planned to Ready (`94f1db1`) and delivered to Awaiting review (`f81db93`). The Review queue now lists each work package's open queries from its `queries.md`. Unmigrated work is still read from its reports. A query that is in both a report and `queries.md` is listed once, and a parked one is not listed.
- Planning check: the installed `ki work status` does not report queries, so the Review queue reads `queries.md` itself. The record names the switch-over for when `ki` does.
- Tests: pass, all 8 tasks, including the new Review queue tests and the degraded check.
- Typecheck: passes.
- Lint: no errors, and no findings in the changed files.
- Roadmap audit: FAIL=0. Its 3 warnings are on other records' `size` fields and were there before this change.
- Live check: I restarted the service and <http://127.0.0.1:1675/> answers. Of the 56 open queries across the estate, 43 now come from `queries.md`. The page fits at 1,440 px and 760 px with no sideways scroll.
- Another session pruned [KI-OBSERVA-VIS-033 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/94f1db12709fc7db2d3c5e9d04f7cec91d5a0886/docs/roadmap/KI-OBSERVA-VIS-033-waiting-for-you.md) (`ddef90c`) during this run. It touched none of my files, and I left it alone.

## In Progress

Nothing. The record waits for your `ki-accept` review. Nothing was pushed.

## Queries

None. One minor point is recorded in the record's review notes: a query dated by its `since` line shows as 01:00 local time while British Summer Time is in effect.
