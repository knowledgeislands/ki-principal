# branch-tidy: reconcile and remove spent branches across Knowledge Islands

Authority: Kris, 24 October 21:36 BST (BRANCH-TIDY, in `+/_WORK/ki/decisions.md`): "look at all the branches that are available in Knowledge Islands and reconcile them and get rid of things if we don't need them". Host: terra. Kris is about to move to Sol, so work quickly.

## Scope

Every repository `mgit` lists from `/Users/krisbrown/workspaces/knowledge-islands` (24). For each: `git fetch --prune`, then list every local branch, every remote branch on `origin` and every worktree, other than the default branch (`main`; paperclip's `ki/stable`, where upstream Paperclip branches are out of scope and left alone).

Known now: ki-agentic-harness has `docs/whitepaper-authoring-learning` (checked out in a worktree), `fold-harness/pre-rebase-main` (a safety ref left by fold-harness) and `sop-secondary` (merged locally as 41b391d61; `origin/sop-secondary` also exists); tools-ki has `fix/prompts-coverage` (checked out in a worktree) and `sop-secondary`.

## Rules

- Live runs first. Check `ki agent status`. Do not touch tools-ki while `fold-tools-ki` is running: do every other repository first, then poll `ki agent status` every 30 seconds for up to 30 minutes; if it is still running, leave tools-ki untouched and say so. Never touch a branch or worktree any other running agent is using.
- Make sure main is level first: pull with rebase, fast-forward only. If main is not level with origin, report it and skip deletions in that repository.
- Delete a branch only if all its content is already on main: either `git merge-base --is-ancestor <branch> origin/main`, or, for a squashed, rebased or cherry-picked branch, `git diff <merge-base-equivalent>` shows every change already present on `origin/main` (check with `git cherry origin/main <branch>` and a content diff). Use `git branch -d`, falling back to `-D` only where you have proved the content is on main. Delete the matching remote branch with `git push origin --delete <branch>` under the same proof.
- A worktree: remove it with `git worktree remove <path>` (no `--force`) only if it is clean and its branch qualifies for deletion. A dirty worktree, or one with untracked files other than `node_modules` and build output, is kept and reported with `git status --short`.
- Anything with work not on main, a conflict, or an intent you cannot read with confidence: do not merge it, do not delete it; report it with what it holds (commit list, files) and a recommendation.
- `fold-harness/pre-rebase-main` is a recovery ref for the fold; delete it only if every commit on it is on `origin/main` in substance.
- Never force-push, never `--no-verify`, never rewrite main. Do not delete untracked files. Stashes: list them, do not drop them.
- No records: CAPTURE-GATE.

## Report

Write only to `/Users/krisbrown/.local/state/ki/agents/ki/branch-tidy.report.md`: a table per repository with branch or worktree, local/remote, disposition (deleted, kept + why), proof used; stashes found; then any query for Kris with Context, Query and Options, recommended first with its confidence. End with CLEAN or NOT CLEAN and what remains.
