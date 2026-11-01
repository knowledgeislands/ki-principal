# Brief: hook-nostash (ki.prj.ways-of-working)

Kris decided HOOK-STASH - a on 1 November 2026 (see `/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/decisions.md`): the never-stash rule covers lint-staged's automatic backup stash. In `/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness`:

1. Find every canonical pre-commit hook asset (the `ki-repo-*` skills and any others) that runs `lint-staged --quiet`; change each to `lint-staged --quiet --no-stash`, and update the rubrics that check the hook text.
2. Test in a scratch repository, with the installed lint-staged: a formatter failure (the commit stops, no reset, working files untouched), an interrupted hook (no stash left), and a partly staged file (record exactly what happens to its unstaged part). Put the findings in your report.
3. State in the `ki-delegation` standard and the coordinator style source, in one sentence each, that hooks run with `--no-stash` and that a leftover `lint-staged automatic backup` stash is reported, never dropped; regenerate with `ki dev skill generate ki-coordination --write`.
4. Run the tests, type check and audits; commit by explicit path; push `main` fast-forward only. Do not conform other repositories: each takes the change through its normal conformance route. Never force, `--no-verify`, rebase, reset or stash. Report as your run packet directs.
