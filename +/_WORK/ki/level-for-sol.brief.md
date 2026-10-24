# level-for-sol brief

Run for KI > SoP (`ki`), under LEVEL-FOR-SOL in [decisions.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/decisions.md) (Kris, 24 October). Read that entry first.

## Goal

Kris is moving Knowledge Islands work from terra to Sol. Before that, every Knowledge Islands repository on terra must have `main` pulled, merged and pushed, so that Sol starts from a clean version that is level with origin.

## Scope

Every Git repository directly under `/Users/krisbrown/workspaces/knowledge-islands/`. Include `ki-principal`, `ki-agentic-harness`, `tools-ki`, `tools-rig`, `tools-techne`, `ki-techne-harness`, `ki-specifications` and the rest. Skip any folder that is not a Git repository.

## Per repository

1. `git fetch`, then record the branch, `git status`, and the ahead and behind counts against `origin/main`.
2. If the primary checkout is not on `main`, do not switch it. Bring `main` level with `git fetch` and a fast-forward of the local `main` ref where that is possible, and report the branch it is on. Kris decides what happens to that branch.
3. If `main` is checked out:
   - Pull with `git pull --rebase`.
   - Resolve conflicts:
     - In work-package files (`+/_WORK/**`, `messages.md`, `queries.md`, `decisions.md`, `state.md`), keep both sides' lines in queue order.
     - In front matter, take the newer `since` and `mark`.
     - In code or canonical content, resolve only where both intents are clear. Otherwise abort the rebase (`git rebase --abort`), leave the repository as it was, and report it.
   - Run the repository's commit hooks as they are. Never use `--no-verify`.
4. Push `main` fast-forward only. Kris has authorised pushing other sessions' stacked commits. Never force-push.
5. Do not touch uncommitted changes. If the working tree is dirty, stash nothing and commit nothing: list the files and say whether they block the pull. If they do, skip that repository.
6. List leftover linked worktrees and local branches not merged to `main`, but do not remove them.
7. ki-agentic-harness: local `main` holds the merged main and secondary States of play (SOP-SECONDARY), which have not yet been reconciled with origin. Reconcile them as above.

Other sessions may still be running: check `ki agent status`. Where a live run is working in a repository, pull and push only that repository's `main`, and report the run.

## Output

Write the report to `/Users/krisbrown/.local/state/ki/agents/ki/level-for-sol.report.md` as an owner report under `ki-delegation`. Include one table row per repository: branch, ahead and behind before and after, conflicts and how each was resolved, pushed yes or no, and anything left over. Finish with a single line: LEVEL, or NOT LEVEL with the repositories that are not level.
