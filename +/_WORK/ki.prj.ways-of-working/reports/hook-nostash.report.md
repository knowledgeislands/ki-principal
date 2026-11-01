# [Model](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › hook-nostash

**🤖 → 👤 Handoff to supervisor · Run report at 00:57 GMT · last mark 00:57 GMT**

---

## Done

- HOOK-STASH a) delivered in the harness as `a2ea2b05`, `feat(ki-repo,ki-engineering): run lint-staged with --no-stash in every canonical pre-commit`, on `main` and published. Kris's decision is in the [ways-of-working decisions log](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/decisions.md).
- Hook files: all eight canonical package pre-commit assets (`ki-repo-harness`, `-homebrew-tap`, `-kb`, `-mcp`, `-project`, `-specifications`, `-tools` and `-website`) and the harness's own `.githooks/pre-commit` now run `lint-staged --quiet --no-stash`. The package-less hooks don't run lint-staged, so they were left alone.
- Rubrics: `ki-repo` HOOK-4 now builds the new line when it composes a hook. `ki-engineering` SCR-11 now requires `--no-stash`: it fails the old `lint-staged` and `lint-staged --quiet` forms, and its conform step adds the flag back without touching other lines. Old Husky content still only warns. The SCR-11 rubric text, its generated `rubric.md`, the `ki-engineering` standard and SKILL.md, and the `ki-repo` standard all describe the new line. Tests cover the change.
- Rule sentence added, as the brief asked: one sentence in the `ki-delegation` background-runs standard (Pushing) and one in the `ki-coordination` style source. Both say hooks run lint-staged with `--no-stash` and that a leftover `lint-staged automatic backup` stash is reported, never dropped. I regenerated `output-styles/ki-coordinator.md` with `ki dev skill generate ki-coordination --write`.
- Checks: `bun run test` passed (1508 tests, 0 failures). `bunx tsc --noEmit` passed. The focused audits for `ki-engineering`, `ki-repo`, `ki-repo-harness`, `ki-coordination`, `ki-delegation`, `ki-skills` and `ki-authoring` all passed with no failures. They ran in an isolated home, following the worktree audit recipe. Their only warnings came from the setup (the worktree's linked `node_modules`, territory policy not being available, the user's coordinator binding, maturity not declared); none came from this change. The commit's own pre-commit hook, already using `--no-stash`, passed.
- Scratch tests are done; results are under Findings. Nothing was stashed, reset, rebased or forced. I removed the worktree, its branch and the temporary files.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Other repositories are unchanged, as the brief required. Until each one's own conformance route catches up, `ki-repo` HOOK-4 will report its pre-commit as drifted and `ki-engineering` SCR-11 will fail its old `lint-staged --quiet` line. SCR-11's conform step repairs that line, and hook composition writes the whole canonical hook.

## Findings

### HOOK-NOSTASH-TEST - How lint-staged 17.6.0 behaves under `--quiet --no-stash`

**Goal:** Check, in a scratch repository, what the new hook line does when a check fails, when the hook is interrupted, and when a file is only partly staged.

**Scope:** The installed lint-staged 17.6.0 from the harness's `node_modules`. The scratch Git repository was bound to a pre-commit hook that runs `lint-staged --quiet --no-stash || exit 1`. One check-only task fails when a staged `.txt` file contains `BAD` and sleeps 30 seconds when it contains `SLOW`. The scratch repository has since been deleted.

**As of:** 1 November 2026, 00:40-00:50 GMT.

| Case | What happened | Stash left | Working file |
| --- | --- | --- | --- |
| Check fails | The commit stopped (exit 1) and the failure printed; nothing was reset | none | untouched, still staged as before |
| Ctrl-C equivalent (SIGINT to the whole commit process group) | The commit stopped; nothing was reset | none | untouched, still staged |
| SIGTERM to the process group | The commit stopped | none | untouched, still staged |
| SIGKILL to lint-staged alone | The hook failed and the commit stopped; the task kept running until it was killed separately | none | untouched (whole file staged) |
| SIGINT to the lint-staged process alone | lint-staged ignored it and waited for its task; the task passed and the **commit landed** | none | committed |
| Partly staged, both parts clean | Commit landed with only the staged part; the unstaged part stays unstaged | none | unstaged part kept |
| Partly staged, unstaged part bad | Commit landed: the check sees only the staged content | none | unstaged part kept |
| Partly staged, staged part bad and the unstaged edit removes it | Commit refused: the check sees the staged content, not the working file | none | unstaged edit kept |
| Partly staged, hook interrupted by SIGINT to the group mid-check | Commit stopped; the unstaged part was put back | none | unstaged part restored |
| Partly staged, lint-staged killed (SIGKILL) mid-check | Commit stopped; **the unstaged part was missing from the working file** | none | unstaged part saved only in `.git/lint-staged/<id>/unstaged.patch`; `git apply` of that patch restored it exactly |

In plain terms: `--no-stash` stops lint-staged from making its backup stash, and the repository's stash list stayed empty in every case. Even with `--no-stash`, lint-staged 17 still hides the unstaged part of a partly staged file while its checks run, so the checks judge exactly what will be committed. It keeps that hidden part in a patch file under `.git/lint-staged/`, not in a stash. If lint-staged is killed outright during that window, the unstaged edits disappear from the working file and survive only in that patch. A normal Ctrl-C, which reaches the whole process group, restores them. A SIGINT sent to lint-staged alone does not stop the commit.

## Queries

### HOOK-PATCH - Treat a leftover lint-staged patch like a leftover stash

**Context:** With `--no-stash`, lint-staged no longer makes a backup stash. While its checks run, it still sets aside the unstaged part of any partly staged file, and it now keeps that part in a patch file at `.git/lint-staged/<id>/unstaged.patch`. In the scratch test, killing lint-staged at that moment left the working file without those edits. Only the patch held them, and `git apply` brought them back exactly. A normal Ctrl-C did not cause this. The standards now cover a leftover `lint-staged automatic backup` stash, but they say nothing about this patch, so an agent tidying `.git` could delete someone's only copy of their unstaged edits.

**Query:** Should the `ki-delegation` standard and the coordinator style also say that a leftover `.git/lint-staged/` patch is reported, never deleted or applied by an agent?

**Options:**

a) (recommended, confidence medium - the loss was reproduced in the scratch repository, but needing a hard kill makes it rare) Add it to the same sentence in both places, so a leftover patch is reported to its owner like a leftover stash and never deleted or applied by an agent, in a small follow-up run.

b) Leave the standards as they are and rely on the general rule against touching other sessions' files.

### 🤖 → 👤 Handoff to supervisor · since 00:57 GMT

👤 1 with you

- [with you] HOOK-PATCH · owner · since 00:57

🧵 ki.prj.ways-of-working
