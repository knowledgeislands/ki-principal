# branch-tidy-2: remove the last spent worktrees and automation branches

Authority: Kris, 24 October 21:36 BST (BRANCH-TIDY): "reconcile them and get rid of things if we don't need them". branch-tidy (report `/Users/krisbrown/.local/state/ki/agents/ki/branch-tidy.report.md`, Q1 and Q2) proved each item below is not needed. Host: terra. Be quick.

1. Worktrees whose branch is wholly on main and whose only untracked content is `node_modules`: re-check each with `git -C <worktree> status --short --ignored` and `git merge-base --is-ancestor <branch> origin/main`. If still true, remove with `git worktree remove --force <path>` and delete the branch with `git branch -d`:
   - ki-agentic-harness: worktree `~/.local/state/ki/agents/fourth-white-paper/harness-authoring-review`, branch `docs/whitepaper-authoring-learning`.
   - tools-ki: worktree `~/workspaces/knowledge-islands/tools-ki-wt-prompts-coverage`, branch `fix/prompts-coverage`.
   If anything other than `node_modules` or build output is untracked, or any tracked change exists, keep it and report.
2. Superseded release-automation branches on origin (single pin bumps to ki v0.10.5 to v0.12.0; both mains are at v0.13.0). First `gh pr list --state open --head <branch>` for each; if an open PR exists, close it with a comment "Superseded: main is on ki v0.13.0". Then `git push origin --delete`:
   - ki-agentic-harness: `automation/ki-v0.10.5`, `automation/ki-v0.11.2`, `automation/ki-v0.11.4`, `automation/ki-v0.12.0`.
   - apps-knowledgeislands.info: `automation/tool-release-ki-v0.11.2`, `-v0.11.3`, `-v0.11.5`, `-v0.12.0` (prefix `automation/tool-release-ki-`).
   Re-check each is still a single commit changing only the version pin before deleting.
3. Confirm with `mgit branch` that only default branches remain.

Never force-push, never `--no-verify`, never touch main. No records.

Report only to `/Users/krisbrown/.local/state/ki/agents/ki/branch-tidy-2.report.md`: one table of item, disposition, proof; end CLEAN or NOT CLEAN.
