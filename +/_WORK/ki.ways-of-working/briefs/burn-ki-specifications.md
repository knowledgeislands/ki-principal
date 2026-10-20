# Burn pass: ki-specifications

Nobody else is working tonight; Kris, 20 October, set OVERNIGHT-BURNDOWN: "getting the roadmaps down to zero ... and even start to tidy up some of the other ones as well ... committing and pushing as you go". Repository `/Users/krisbrown/workspaces/knowledge-islands/ki-specifications`, its roadmap folder.

1. Inventory every open record: state, priority, blockers.
2. Work them in priority order where Ready or plannable without Kris, delivering each to awaiting review with a complete packet. Skip holds, blocked records and anything needing Kris's eyes, an attended action, publication or another repository's change.
3. Flag any record that is stale, superseded or a duplicate in your report with a recommended disposition; do not cancel it.

Work in a worktree on `run/burn-ki-specifications` under `ki-git`, fast-forward local `main` after the gates pass, pull with rebase and push fast-forward only when every commit ahead of the remote is from this programme tonight, else leave it local and report it. Never accept or prune. Never `--no-verify` or force-push. CAPTURE-GATE: no new records, follow-ups as `messages.md` lines in `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/<id>/`. HOOK-GUARD: no `ki repo conform` without `--dry-run`. British English, ASCII hyphens. Report per record: before, after, commits, pushed; and the open count before and after.
