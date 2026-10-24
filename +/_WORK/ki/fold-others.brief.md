# fold-others: fold all branches into main across the other Knowledge Islands repositories

Repositories: every Git repository under /Users/krisbrown/workspaces/knowledge-islands/ except ki-agentic-harness and tools-ki (other runs own those). ki-principal included: it is a knowledge base; commit only merges there, and leave any uncommitted file alone. Kris wants all branch-based work back on main before moving to Sol. Survey all of them first, then fold, in the order of most branches first.

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

Write your report only to /Users/krisbrown/.local/state/ki/agents/ki/fold-others.report.md: a table per repository of branch, disposition (merged, already on main, not merged + why), checks run and result, pushed yes/no; then any query for Kris with Context, Query and Options, recommended first with confidence. End with LEVEL or NOT LEVEL and the repositories still not level.
