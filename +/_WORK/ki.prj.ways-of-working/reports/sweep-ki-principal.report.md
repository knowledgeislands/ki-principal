# [Model](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › sweep-ki-principal

**🤖 → 👤 Handoff to supervisor · Run report at 00:29 GMT · last mark 00:24 GMT**

---

## Done

- `.gitignore` re-includes `+/_WORK/*/reports/` and `+/_WORK_REVIEW/*/reports/`, added straight after the `reports/` rule in its own commit (`2a9be781`); the commit hook's repository audit passed.
- `ki.prj.mac-studio-setup`: 4 reports moved, all tracked, so no `git add` needed; 5 links repointed in `queries.md` and `state.md`; REPORTS-MOVED line added (`567affa0`).
- `ki.prj.observatory`: 42 reports moved, all tracked, so no `git add` needed; 17 links repointed in `queries.md`, `design/observatory-sync-report.md` and three moved reports (`away-finalise`, `drain-20261029`, `mark-summary`), plus one in `ki.prj.tools-burndown/messages.md` and one in `ki.prj.ways-of-working/design/host-sync-report.md`, both pointing at Observatory reports and committed with that folder; REPORTS-MOVED line added (`3b09eba9`).
- `ki.sop.main`: 7 reports moved (3 tracked, 4 untracked that were moved and then added); 2 links repointed in `queries.md`; REPORTS-MOVED line added (`8c71c7c6`).
- No name clashes. Nothing deleted. None of the moved reports has a relative link to a file that was not moved, so the moves broke no outgoing links. All commits pushed to `main`.
- Left unchanged on purpose, because editing them would change what the text records: file lists in commit receipts (``- `A` `+/_WORK/ki.prj.observatory/...` `` in `away-audience-assessment.report.md`), bare file names in prose (`ki.prj.observatory/decisions.md`, `ki.prj.mac-studio-setup/queries.md` line 35), links pinned to a GitHub revision, which still resolve, and links into `+/_THREADS/` or `~/.local/state`, which do not point at moved files. Repointed absolute links keep their old `/Users/krisbrown/workspaces/...` prefix, which was already out of date before this run; only `reports/` was added to the path.

## In Progress

- Skipped `ki.prj.ways-of-working` (31 top-level reports, all untracked) because `ki agent status` showed this work's live sweep runs, including this one. Those reports and the links to them stay as they are until its coordinator sweeps them or sends a follow-up run.

Outstanding - no action requested now

- Pre-existing files in the `reports/` folders, such as the untracked files in `ki.prj.ways-of-working/reports/`, now show as untracked because the ignore rule changed. They were left alone.

## Queries

No outstanding queries.
