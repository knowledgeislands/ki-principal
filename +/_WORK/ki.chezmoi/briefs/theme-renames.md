# theme-renames

Work: ki.chezmoi (KI > Rig > chezmoi). Repository: /Users/krisbrown/.local/share/chezmoi, on Sol.

Authority: OVERNIGHT, Kris on 20 October at 00:30 BST; THEME-REGISTRY a), from [roadmap-gaps](/Users/krisbrown/.local/state/ki/agents/chezmoi/roadmap-gaps.report.md).

Task: on KB-DOTFILES-UE-027, -082, -086 and -087, replace `initiative: knowledge-islands/rig` with `theme: rig`, and add the two registry legacy warnings this exposes (the project registry holding a Project note's `initiative:`, and holding `Streams/Initiatives/`) to the permitted baseline in `ready-rest-3.baseline.json`, with a note that they describe ki-principal's registry and clear when its migration lands. Confirm the audit shows exactly those two new warnings, now permitted, and nothing else new. Change nothing else. One local `docs(roadmap)` commit.

Constraints: no `chezmoi apply`, restart, kill, `launchctl` change, push or fetch; never write `launchctl bootout` with an empty label; do not stage `bin/chezmoi/json`; never run `ki repo conform` without `--dry-run`; CAPTURE-GATE: no new records; commit by explicit path, retrying on `index.lock`; leave no `.git/*.lock`. Gate: `ki repo audit --repo .`, `node --test tests/*.test.mjs`, `rumdl check .`; the permitted baseline is the 22 warnings in `~/.local/state/ki/agents/chezmoi/ready-rest-3.baseline.json` plus `CLAUDEBIND-1`.

Report: the run report form, heading `# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › theme-renames`, every record linked by its full identifier, each query with options, a recommendation and its confidence.
