# Repair links, then prune three tools-ki records

Nobody else is working tonight. Kris, 20 October, granted overnight acceptance and pruning: "if you can quickly now accept ... accepting new things that are waiting with you and pruning those ... getting the roadmaps down to zero". This run is launched under the `prune` tier.

Records to prune: KI-TOOL-KI-CLI-152, KI-TOOL-KI-CLI-165 and KI-TOOL-KI-CLI-167 (tools-ki, done; tools-ki `main` is now level with its remote). Live links survive in ki-principal work packages and design notes and in the harness records KI-HARNESS-GOV-200 and KI-HARNESS-GOV-225 (read `/Users/krisbrown/.local/state/ki/agents/ways-of-working/accept4-tools-ki.report.md`). Harness link edits are committed locally only; do not push the harness. The archived ki-techne-principal checkout is unavailable: say so rather than claim an exhaustive scan.

For each record:

1. Find every live link to it across the Knowledge Islands checkouts under `/Users/krisbrown/workspaces/knowledge-islands/` (tracked Markdown, including `+/_WORK/*/` work packages and design notes in ki-principal).
2. Make sure the record's last revision is on the remote (`git branch -r --contains`). If it is only local because other sessions' commits are stacked ahead of it, do not push them: skip that record and report it.
3. Rewrite each live link in the `ki-coordination` pruned form, `[<FULL-ID> (pruned)](https://github.com/<owner>/<repo>/blob/<last revision>/<path>)`, with the revision being the last commit in which the file existed after your prune commit, verified to exist on the remote once pushed. Where a link cites the record as the home of live guidance, point it at the durable home the record names instead and say so.
4. Prune the record under `ki-work-roadmap`, commit by explicit path, then commit the link repairs.

Edits to other works' packages are limited to these link rewrites. Pull with rebase and push fast-forward only, pushing only when every commit ahead of the remote is from this programme tonight; otherwise leave it local and report it. Never `--no-verify` or force-push. CAPTURE-GATE: follow-ups as `messages.md` lines. HOOK-GUARD. British English, ASCII hyphens. Report per record: pruned or skipped, why, links repaired, commits, pushed.
