# Second burn pass: tools-rig

Repository `/Users/krisbrown/workspaces/knowledge-islands/tools-rig`, records in `docs/roadmap/`. Read `/Users/krisbrown/.local/state/ki/agents/ways-of-working/accept-tools-rig.report.md` first.

1. KI-TOOL-RIG-CORE-053 (planned): deliver it.
2. The complete gate fails `ki-repo-tools` SHELL-HOOK because `.githooks/pre-commit` runs Bats. If no commit in the last day from another session touches `.githooks/`, move Bats out of the commit hook to the developer or CI gate as the current standard says, by hand; otherwise leave it and report.
3. Then any other open record in priority order that is Ready or plannable without Kris, to awaiting review. Skip KI-TOOL-RIG-CORE-047, -062 and -068 (Kris's attended checks), holds and blocked records.

Nobody else is working tonight; Kris, 20 October, set OVERNIGHT-BURNDOWN: "getting the roadmaps down to zero for all of tools ... committing and pushing as you go". Work in a worktree on `run/<name>` under `ki-git`, fast-forward it into local `main` after the gates pass (WORKTREE-INTEGRATE), pull with rebase and push fast-forward only when every commit ahead of the remote is from this programme tonight, else leave it local and report it. Never accept or prune; set delivered records to awaiting review with a complete packet. Never `--no-verify` or force-push. CAPTURE-GATE: no new records, follow-ups as `messages.md` lines in `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/<id>/`. HOOK-GUARD: no `ki repo conform` without `--dry-run`. British English, ASCII hyphens. Report per record: before, after, commits, pushed.
