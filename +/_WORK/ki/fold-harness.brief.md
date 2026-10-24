# fold-harness: reconcile and fold all branches into ki-agentic-harness main

Repository: /Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness. main is 8 ahead of origin/main and 1 behind.

1. OAuth (Kris chose this): rebase local main onto origin/main. Keep origin's 76f7e7d3d "fix(ki-binding): accept OAuth markers on URL MCP entries" as the base, with its stricter BIND-2 wording and negative tests. From local fceb8dc2e "feat(ki-binding): allow auth: oauth on URL entries" fold in only what it adds beyond origin: the YAML and multi-client input coverage, the BIND-1 audit exercising baseUrl, and the documentation that an absent source marker stays absent in mcporter. Do not duplicate equivalent parser code; keep each adapter's existing declarations. Replay the other local commits. A plain rebase flattens the sop-secondary merge, so compare the final tree with today's local main (57226cdea or its current tip) and with origin to confirm nothing is lost. Do not touch live authentication.
2. White paper (Kris chose to fold it in): branch `docs/whitepaper-authoring-learning`, commit 26e46c185, in worktree ~/.local/state/ki/agents/fourth-white-paper/harness-authoring-review. It is based on an old revision; its inventory test expects 800 criteria while main expects 833. Integrate it onto main keeping all current-main changes, recompute inventory expectations from the combined catalogue, regenerate and verify rubric publication (`ki dev skill generate` where applicable). Leave the worktree and its untracked node_modules alone.
3. Every other unmerged branch: as the rules below.

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

Write your report only to /Users/krisbrown/.local/state/ki/agents/ki/fold-harness.report.md: a table per repository of branch, disposition (merged, already on main, not merged + why), checks run and result, pushed yes/no; then any query for Kris with Context, Query and Options, recommended first with confidence. End with LEVEL or NOT LEVEL and the repositories still not level.
