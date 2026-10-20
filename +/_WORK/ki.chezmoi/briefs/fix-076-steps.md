# fix-076-steps

Work: ki.chezmoi (KI > Rig > chezmoi). Repository: /Users/krisbrown/.local/share/chezmoi, on Sol.

Authority: OVERNIGHT, Kris on 20 October at 00:30 BST; UE-076-STEPS, raised by [roadmap-gaps](/Users/krisbrown/.local/state/ki/agents/chezmoi/roadmap-gaps.report.md).

Task: `ki repo audit --repo .` fails ITEM-3 on [KB-DOTFILES-UE-076](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-076-always-run-latest-source.md): commit `1999865` left non-task lines under `## Steps`. Move those lines to the section the ki-work record rules intend (Discussion, Approach or similar), keeping every word of their content, so `## Steps` holds only task-list entries. Change nothing else, and touch no other record (other runs are editing KB-DOTFILES-UE-093 and KB-DOTFILES-UE-077). Confirm the ITEM-3 failure is gone. One local `docs(roadmap)` commit.

Constraints: no `chezmoi apply`, restart, kill, `launchctl` change, push or fetch; never write `launchctl bootout` with an empty label; do not stage `bin/chezmoi/json`; never run `ki repo conform` without `--dry-run`; CAPTURE-GATE: no new records; commit by explicit path, retrying on `index.lock`; leave no `.git/*.lock`. Gate: `ki repo audit --repo .`, `node --test tests/*.test.mjs`, `rumdl check .`; the permitted baseline is the 22 warnings in `~/.local/state/ki/agents/chezmoi/ready-rest-3.baseline.json` plus `CLAUDEBIND-1`.

Report: the run report form, heading `# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › fix-076-steps`, every record linked by its full identifier, each query with options, a recommendation and its confidence.
