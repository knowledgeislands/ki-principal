# resolve: reconcile ki-principal main with origin

Authority: ki-principal only. Local `main` is ahead 17 and behind 1 of `origin/main` (origin added `3ad515ab`, a ways-of-working queue commit; local holds commits from several sessions). Other sessions and runs are committing in this checkout now.

1. If a merge, rebase or cherry-pick is already in progress, or `.git/index.lock` exists, wait up to two minutes; if it persists, stop and report.
2. `git fetch`, then integrate with a merge commit (`git pull --no-rebase --no-edit`), subject `chore(git): reconcile main with origin/main` with the line `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. Never rebase, reset, stash or force, and never `--no-verify`.
3. If the merge conflicts in `messages.md` files, keep both sides' lines (queue union, no duplicates). On any other conflict, `git merge --abort` and report the paths.
4. Push fast-forward only. If origin moved again, repeat 2 to 4 at most three times, then stop and report.
5. Leave uncommitted files alone and name them.

Report to `/Users/krisbrown/.local/state/ki/agents/ki-sop-main/resolve.report.md`: short owner-report form. Plain British English, no em-dashes.
