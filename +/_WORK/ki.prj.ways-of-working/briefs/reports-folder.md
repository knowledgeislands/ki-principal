# Brief: reports-folder (ki.prj.ways-of-working)

Kris decided TOP-LEVEL-NOW on 1 November 2026: run reports go into a `reports/` folder inside each work package now; LAYOUT-SHAPE stays open. The diagnosis, with every file and line, is `/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/package-layout/top-level-cause.md` ("Proposed change set, by owner").

In `/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness`:

1. `ki-work-package`: closed list Run report row becomes `reports/<name>.report.md`, with the other lines the diagnosis names; the rubric allows `reports/` holding only `*.report.md`, and flags a top-level `*.report.md` as a stray file at WARN during a tolerance window (say until the sweep is done), with the brief-received check reading `reports/` and the old place.
2. `ki-delegation` and `ki-coordination` (and the output-style source; then `ki dev skill generate ki-coordination --write`): the launcher homes reports in the work folder's `reports/`; prune wording to match.
3. `ki-repo` managed ignore block: add `!/+/_WORK/*/reports/` and `!/+/_WORK_REVIEW/*/reports/` after the `reports/` rule; test that `+/_WORK/<id>/reports/x.report.md` is tracked and `x/reports/` stays ignored. Run the tests, type check and audits; commit by explicit path (Conventional Commits); fetch and push `main` fast-forward only.

Then append one line to `/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.tools-burndown/messages.md`, adapted from the draft in the diagnosis: home run reports into `+/_WORK/<id>/reports/<name>.report.md` under TOP-LEVEL-NOW (Kris, 1 Nov), changing `reportPath` and every path that bypasses it, reading both old and new places during tolerance, citing the harness commit that landed the ignore exception. Mark it IMPORTANT: Kris asked for priority. Commit it as `docs(work): ki.prj.tools-burndown message from ki.prj.ways-of-working` and push; on a pull that cannot fast-forward, merge `origin/main` in a temporary worktree, never rebase.

Never force, never `--no-verify`, never stash, rebase or reset. Do not move existing reports (a separate decision). Report as your run packet directs.
