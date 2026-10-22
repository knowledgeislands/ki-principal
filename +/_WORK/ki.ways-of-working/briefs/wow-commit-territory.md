# wow-commit-territory - commit everything across the Knowledge Islands repositories

## Authority

Kris, 2026-10-22 22:50 BST: "get everything fully committed across all of the knowledge islands repos and then we'll have a look at what's outstanding". Kris holds exclusive KI control from 14:03 today. Commit only; Kris did not ask for a push.

## Task

For every Git repository directly under `/Users/krisbrown/workspaces/knowledge-islands/` except `ki-principal` (another run handles it), and the `acquire` checkout at `/Users/krisbrown/workspaces/personal/acquire` apart from its `+/_WORK/kb.regular.acquire-intake/` report copies:

1. Inventory uncommitted changes, untracked files and stashes, and how each relates to the last commits and open roadmap work.
2. Commit coherent units by explicit path with conventional subjects, passing each repository's hooks. Delete only generated junk that is clearly reproducible (build output, temporary files) and not gitignored, and prefer adding a `.gitignore` line where it recurs. Leave a file uncommitted only if it is broken, clearly mid-edit by a live process, or a secret; name each one.
3. Do not touch stashes or other branches beyond listing them; do not commit on a branch other than the checkout's current one, and say if a checkout is not on its default branch.

## Bounds

No push, no `--no-verify`, no force, no rebase or history rewrite, no worktree removal. Credentials never committed. Harness and tools-ki primaries: commit only what is already there; make no code changes.

## Report

First line `VERDICT: DONE|PARTIAL · confidence <level> - <one line>`. Then one line per repository: commits made, what was left and why, branch and ahead-of-remote count.
