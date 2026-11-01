# [Model](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › reports-folder

**🤖 → 👤 Handoff to supervisor · Run report at 00:22 GMT · last mark 13:55 GMT**

---

## Done

- **Ignore exception (`ki-repo`), `c273a1fb`:** the managed ignore block now has `!/+/_WORK/*/reports/` and `!/+/_WORK_REVIEW/*/reports/` straight after `reports/`. The harness's own `.gitignore` and the repository standard are updated to match. A new test confirms with `git check-ignore` that `+/_WORK/<id>/reports/x.report.md` and the review-area equivalent are tracked while `x/reports/` stays ignored.
- **`ki-work-package`, `58e1d128`:**
  - The closed list's Run report row is now `reports/<name>.report.md`. The launcher's entry-point row, the tidy's "What goes" line and the opening paragraph say the same, and a new paragraph cites TOP-LEVEL-NOW (Kris, 1 November) and the tolerance window.
  - The rubric allows `reports/` holding only `*.report.md`. A top-level `*.report.md` now gets a WARN under FOLDER-1 as a stray file until the sweep is done; anything else fails as before.
  - The answered-report check (FOLDER-2) and the brief-received check (FOLDER-3) read both `reports/` and the old place. The FOLDER-1 and FOLDER-3 descriptions and `rubric.md` are updated.
- **`ki-delegation` and `ki-coordination`, `30584fd2`:**
  - The launcher wording now says reports are homed in the work folder's `reports/`. The prune wording in the coordination standard and the output style now refers to `reports/` and to the top level during the tolerance window.
  - The link check (COORD-7) now also reads `reports/`, with a test. `ki dev skill generate ki-coordination --write` reports the generated files in sync.
- **Checks:**
  - `bun run test` passed (1506 tests) and `bunx tsc --noEmit` passed.
  - The focused audits of `ki-work-package`, `ki-coordination`, `ki-delegation`, `ki-repo` and `ki-skills` passed, and so did the full `ki repo audit`, with no failures. All audits ran in an isolated home in the worktree; the remaining warnings come from that setup (for example COORD-8 finding no user bindings) or were already there.
  - The three harness commits are on `main` and pushed.
- **Message to [ki.prj.tools-burndown](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.tools-burndown/messages.md), `0ea6d225`:** sent as one IMPORTANT line (REPORTS-FOLDER) asking `tools-ki` to:
  - home reports in `+/_WORK/<id>/reports/<name>.report.md` under TOP-LEVEL-NOW;
  - change `reportPath` and every path that bypasses it, as the diagnosis lists them;
  - read both the old and the new places during tolerance.

  It cites `c273a1fb` and is pushed. Existing reports were not moved.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Until `tools-ki` lands its change, the launcher still writes reports at the top level. They now get the tolerance WARN under FOLDER-1 rather than passing silently.
- The rubric does not yet turn the tolerance WARN into a FAIL. That switch waits for the sweep (TOP-LEVEL-SWEEP, still open with Kris).
- `ki dev skill rubric` follows the installed harness, which points at the primary checkout, so it could not regenerate `rubric.md` from inside the worktree. The two `rubric.md` lines were edited by hand to match, and the `ki-skills` audit passed on that result.

## Queries

No outstanding queries
