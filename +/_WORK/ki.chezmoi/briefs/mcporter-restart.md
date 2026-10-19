# mcporter-restart

Work: ki.chezmoi (KI > Rig > chezmoi). Host: this Mac (Sol), user agent only.

Authority: Kris on 19 October, 23:30 BST: "McPorter restart: you can just do it if you need to." The need is the child leak in KB-DOTFILES-UE-100: Sol's mcporter daemon held about 96 children (about 5.2 GB) and was climbing.

Task:

1. Record the daemon's PID, its child-process count and their total RSS.
2. Restart it with the existing `~/bin/launchd/mcporter_restart`. Read the script first; use it as it stands, without editing it.
3. Verify: the daemon is running under its launchd label with a new PID; the old children are gone (no orphans left from the old PID); the child count afterwards; and one MCP call through mcporter succeeds (for example list servers).
4. If the restart fails or the daemon does not come back, do not improvise beyond one retry of the same script; stop and report.

Constraints:

- Do not edit any file under `~/.local/share/chezmoi` or `~/Library/LaunchAgents`, and do not run `chezmoi apply` or `rig apply`.
- Never use `launchctl bootout` with a computed or empty label; write any label literally.
- Never run `ki repo conform` without `--dry-run` (HOOK-GUARD).
- Leave no temporary files behind.

Report: the run report form, heading `# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › mcporter-restart`. Add the before and after numbers as evidence for KB-DOTFILES-UE-100 in the report only; do not edit the record.
