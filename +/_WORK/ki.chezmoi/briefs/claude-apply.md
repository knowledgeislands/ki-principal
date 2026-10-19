# claude-apply

Work: ki.chezmoi (KI > Rig > chezmoi). Repository: /Users/krisbrown/.local/share/chezmoi, on Sol.

Authority: Kris on 19 October, 23:33 BST, "yes" to CLAUDE-APPLY a): an agent shows the targeted diff, then applies `~/.claude/settings.json` and `~/.claude/output-styles/ki-coordinator.md` and verifies. Kris approved on the understanding that the diff is empty ([parked-three](/Users/krisbrown/.local/state/ki/agents/chezmoi/parked-three.report.md), chezmoi `7ac9047`, `d5ac9c9`).

Task:

1. `git -C /Users/krisbrown/.local/share/chezmoi status --short`; stop if the working tree is dirty with anything touching these two targets.
2. Run only `chezmoi diff ~/.claude/settings.json ~/.claude/output-styles/ki-coordinator.md`. Never run a full `chezmoi diff`. If it is not empty, do not apply: stop and report the diff as a query.
3. If it is empty, run `chezmoi apply ~/.claude/settings.json ~/.claude/output-styles/ki-coordinator.md` and nothing wider.
4. Verify:
   - `~/.local/state/chezmoi/claude-code-additional-directories.json` exists and `jq length` equals the number of `claude-code` entries declared in `trusted-folders.yaml`;
   - `chezmoi status ~/.claude/settings.json ~/.claude/output-styles/ki-coordinator.md` prints nothing;
   - `ls -L ~/.claude/output-styles/ki-coordinator.md` resolves and the apply printed no output-style warning;
   - `~/.claude/settings.json` content is unchanged apart from nothing (compare a private before copy, then delete the copy).

Constraints:

- Apply nothing else; no `rig apply`, no scripts, no push.
- Never run `ki repo conform` without `--dry-run` (HOOK-GUARD).
- If anything fails, restore `~/.claude/settings.json` from the before copy and report.
- Leave no temporary files and no `.git/*.lock`.

Report: the run report form, heading `# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › claude-apply`. Include the targeted diff output (expected empty).
