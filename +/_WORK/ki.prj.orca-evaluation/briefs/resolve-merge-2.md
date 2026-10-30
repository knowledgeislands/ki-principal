# Brief: resolve-merge-2 (ki.prj.orca-evaluation)

Bounded resolve run. The primary ki-principal checkout (/Users/krisbrown/workspaces/knowledge-islands/ki-principal) has local main diverged from origin/main: some local commits are patch duplicates of commits already on origin/main (published by cherry-pick), others are unpublished ki.prj.orca-evaluation work-package commits. Other sessions share this checkout and have uncommitted files there; do not touch them.

1. `git fetch`. Create a temporary worktree under /tmp on a new branch at local `main` (`git worktree add -b resolve-merge-2-tmp /tmp/ki-resolve-merge-2 main`).
2. In it, `git merge --no-edit origin/main`. If it conflicts, abort, report and stop.
3. Push that HEAD to origin main fast-forward only (`git push origin HEAD:main`); never force, never --no-verify. If origin moved, fetch and repeat step 2 once.
4. In the primary checkout run only `git pull --ff-only`. Never stash, rebase, reset or checkout files there.
5. Remove the temporary worktree with `git worktree remove /tmp/ki-resolve-merge-2` and delete branch resolve-merge-2-tmp.

Report: one line on the outcome and the primary checkout's final `git status -sb` first line.

Conflicts: if a conflict touches only files under +/_WORK/ki.prj.orca-evaluation/briefs/ (spent briefs), resolve by deleting them; any other conflict, abort and stop.

When finished, send the coordinator a status message with the one-line outcome through Orca (`orca orchestration send`), then end.
