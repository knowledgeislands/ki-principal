# pin-links

Work: ki.chezmoi (KI > Rig > chezmoi). Repository: /Users/krisbrown/.local/share/chezmoi, on Sol.

Authority: OVERNIGHT, Kris on 20 October at 00:30 BST; PIN-LINKS, routed from ki.tools-burndown at 01:45 BST.

Task: in [KB-DOTFILES-UE-098](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-098-workspaces-git-audit-roots.md) (around line 36), repoint every link to KI-MCP-GIT-FND-006's live file to its accepted revision, <https://github.com/knowledgeislands/mcp-git-audit/blob/2d4054d5516863dbce078bb594b20e486196a800/docs/roadmap/KI-MCP-GIT-FND-006-ground-roots-in-workspaces.md>, written as `KI-MCP-GIT-FND-006 (pruned)` if the ki-work link rules ask for that form. Search the rest of the repository for other links to that file and repoint them the same way. Change nothing else. One local `docs(roadmap)` commit.

Constraints: no `chezmoi apply`, restart, kill, `launchctl` change, push or fetch; never write `launchctl bootout` with an empty label; do not stage `bin/chezmoi/json`; never run `ki repo conform` without `--dry-run`; CAPTURE-GATE: no new records; commit by explicit path, retrying on `index.lock`; leave no `.git/*.lock`. Gate: `ki repo audit --repo .`, `node --test tests/*.test.mjs`, `rumdl check .`; the permitted baseline is the 22 warnings in `~/.local/state/ki/agents/chezmoi/ready-rest-3.baseline.json` plus `CLAUDEBIND-1`.

Report: the run report form, heading `# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › pin-links`, every record linked by its full identifier, each query with options, a recommendation and its confidence.
