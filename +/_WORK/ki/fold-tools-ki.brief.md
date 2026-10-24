# fold-tools-ki: fold all branches into tools-ki main

Repository: /Users/krisbrown/workspaces/knowledge-islands/tools-ki. The checkout is on `sop-secondary` (0f150967), 2 commits ahead of main (bcb66c0c), a clean fast-forward: the secondary States of play support with `ki agent prompts`, and an inbox hand-in. Kris chose to merge it. Its stricter work-definition validation may exclude malformed packages from status output: run representative `ki agent status` and review warnings. Keep the inbox hand-in as a hand-in; do not implement its proposed fix. Then switch the checkout back to main. Then every other unmerged branch, as the rules below. Note in the report that the installed `ki` on each host needs reinstalling separately.

## Rules for every repository

- Fetch first. Work on `main` (paperclip: its default `ki/stable`; never merge upstream Paperclip branches there, only branches made for Knowledge Islands work).
- List every local and remote branch not merged into main, and every worktree with its branch. For each, decide: real work not yet on main → merge it; already on main in substance (superseded, cherry-picked, squashed) → do not merge, note it; intent unclear or a conflict you cannot resolve with both intents clear → do not merge, report it.
- Merge with a normal merge or rebase onto current main, whichever keeps history clearest; check the resulting content against main before it, so nothing on main is lost.
- Run the repository's full checks (tests, coverage gate, type check, focused audits) and let the commit hooks run. Never `--no-verify`, never force-push. Push main fast-forward only. Pushing other sessions' commits stacked on main is authorised (LEVEL-FOR-SOL).
- A checkout on another branch: once its branch is merged and pushed, switch it back to main if the tree is clean. Do not touch a dirty tree; report it.
- Do not delete any branch, remote branch, worktree or untracked file (leave `node_modules` alone).
- Respect live runs: check `ki agent status`; do not merge a branch a running agent is working on.
- Work quickly: Kris is waiting to move to Sol.

## Report

Write your report only to /Users/krisbrown/.local/state/ki/agents/ki/fold-tools-ki.report.md: a table per repository of branch, disposition (merged, already on main, not merged + why), checks run and result, pushed yes/no; then any query for Kris with Context, Query and Options, recommended first with confidence. End with LEVEL or NOT LEVEL and the repositories still not level.
