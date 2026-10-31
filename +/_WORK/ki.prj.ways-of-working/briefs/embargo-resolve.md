# Brief: embargo-resolve

Work: ki.prj.ways-of-working; window AWAY-31-OCT. In `/Users/krisbrown/workspaces/humans-not-robots/hnr-principal` and `/Users/krisbrown/workspaces/personal/personal-principal`, this work's EMBARGO add and withdraw commits sit unpublished on local `main`. They cancel out, and the repositories had moved on.

For each repository:

1. `git fetch`.
2. In a temporary worktree from local `main`, `git merge origin/main`, making a merge commit with no rebase.
3. Push to `origin main` fast-forward only.
4. Fast-forward the primary checkout only if that is clean for the merged paths. Leave other sessions' uncommitted files untouched; if the fast-forward cannot proceed because of them, leave the primary as it is and say so.

Never force, never `--no-verify`, never reset, rebase or stash. Remove each worktree with `git worktree remove`. If a merge has any conflict, abort that repository and report it. Report in plain English.
