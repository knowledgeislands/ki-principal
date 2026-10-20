# harness-tidy - remove the finished harness-fix worktree

Work: `ki.ways-of-working`. Repository: `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness`.

The harness-fix run (report `/Users/krisbrown/.local/state/ki/agents/ways-of-working/harness-fix.report.md`) left a worktree on branch `run/harness-fix`.

1. Confirm that every commit on `run/harness-fix` is reachable from local `main` (`git branch --merged main`) and that the worktree has no uncommitted or untracked changes.
2. If both hold, remove it with `git worktree remove` and delete the branch with `git branch -d` (never `-D`), then `git worktree prune`.
3. If either fails, change nothing and report exactly what is unmerged or dirty.

Do not push, fetch or touch any other worktree, branch or file. Report in the owner-report shape (Done, In Progress, Queries) at your report path.
