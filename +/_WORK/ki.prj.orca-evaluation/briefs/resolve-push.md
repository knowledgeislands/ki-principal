# Brief: resolve-push (ki.prj.orca-evaluation)

Bounded resolve run. In /Users/krisbrown/workspaces/knowledge-islands/ki-principal, local main is ahead 1 and behind 1 of origin/main: local-only f233597c "docs(work): ki.prj.orca-evaluation draft Orca trial plan" (touches only +/_WORK/ki.prj.orca-evaluation/design/orca-trial-plan.md), remote-only 94f69b5a (ki.prj.observatory message). The paths are disjoint.

Publish f233597c on top of origin/main without disturbing the primary checkout's working tree: create a temporary worktree from origin/main (git worktree add under /tmp), cherry-pick f233597c there, push that HEAD to origin main fast-forward only, then remove the temporary worktree with git worktree remove. Then in the primary checkout run `git pull --ff-only`; if it still cannot fast-forward because the local commit is now duplicated, report that and stop. Never stash, rebase or reset in the primary checkout, never force-push or use --no-verify, and touch no other files. If the cherry-pick conflicts, stop and report.

Report: one line on the outcome and the primary checkout's final status line.
