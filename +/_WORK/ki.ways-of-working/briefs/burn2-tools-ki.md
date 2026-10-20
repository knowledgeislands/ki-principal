# Second burn pass: tools-ki

Repository `/Users/krisbrown/workspaces/knowledge-islands/tools-ki`, records in `docs/roadmap/`. Read `/Users/krisbrown/.local/state/ki/agents/ways-of-working/accept2-tools-ki.report.md` first.

1. KI-TOOL-KI-CLI-165: fix the extra third-level Review heading that fails ITEM-3, re-check, return to awaiting review.
2. KI-TOOL-KI-CLI-134: repair the immutable-baseline evidence the review found unavailable; leave the three provisional choices as they are (they are with Kris as FOOTER-PROVISIONALS); return to awaiting review.
3. Then work any other open record in priority order that is Ready or plannable without Kris, delivering to awaiting review. Skip holds, blocked records and anything needing Kris's eyes, an attended action or publication.

Nobody else is working tonight; Kris, 20 October, set OVERNIGHT-BURNDOWN: "getting the roadmaps down to zero for all of tools ... committing and pushing as you go". Work in a worktree on `run/<name>` under `ki-git`, fast-forward it into local `main` after the gates pass (WORKTREE-INTEGRATE), pull with rebase and push fast-forward only when every commit ahead of the remote is from this programme tonight, else leave it local and report it. Never accept or prune; set delivered records to awaiting review with a complete packet. Never `--no-verify` or force-push. CAPTURE-GATE: no new records, follow-ups as `messages.md` lines in `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/<id>/`. HOOK-GUARD: no `ki repo conform` without `--dry-run`. British English, ASCII hyphens. Report per record: before, after, commits, pushed.
