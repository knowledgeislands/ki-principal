# Brief: publish ki-principal main (diverged)

Work: ki.prj.orca-evaluation. The primary checkout /Users/krisbrown/kis/knowledge-islands/ki-principal has local `main` 2 ahead and 2 behind `origin/main`. Never stash, rebase or reset in the primary checkout, and never touch its uncommitted files.

1. `git -C /Users/krisbrown/kis/knowledge-islands/ki-principal fetch origin`, then `git worktree add /tmp/kip-resolve-<timestamp> main` from that repository (a detached copy of local main is fine: `--detach main`).
2. In that worktree, `git merge --no-edit origin/main`. If it conflicts, resolve only where both sides add lines (keep both, in order) in `+/_WORK/**/messages.md` or `decisions.md`; any other conflict: abort, report, stop.
3. Push the result to `origin main` fast-forward only (`git push origin HEAD:main`); never force, never `--no-verify`. If the push is rejected because origin moved, fetch and repeat step 2 once.
4. Then in the primary checkout run only `git merge --ff-only origin/main` after a fetch; if it cannot fast-forward, report and stop.
5. Remove the temporary worktree with `git worktree remove /tmp/kip-resolve-<timestamp>`.

Write ~/.local/state/ki/agents/ki-prj-orca-evaluation/resolve-push.report.md with the outcome and the final `git status -sb` line, then call worker_done.
