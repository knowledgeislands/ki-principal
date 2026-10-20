# ground-076

Work: ki.chezmoi (KI > Rig > chezmoi). Repository: /Users/krisbrown/.local/share/chezmoi, on Sol.

Authority: OVERNIGHT, Kris on 20 October at 00:30 BST; recommended by the read-only survey [next-scan](/Users/krisbrown/.local/state/ki/agents/chezmoi/next-scan.report.md) - read it first.

Task: under `ki-plan`, ground [KB-DOTFILES-UE-076](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-076-always-run-latest-source.md) in its record only: record the current source facts (`bin/scheduled/executable_rig-update`, how `chezmoi update` and pulls happen today, the absence of any behind-check), then set out where the check could live and how a refusal could behave as options for Kris's decision, each with consequences and a recommendation with confidence. Do not implement, fetch or pull. One local commit.

Constraints: no `chezmoi apply`, restart, kill, `launchctl` change, push or fetch; never write `launchctl bootout` with an empty label; do not stage `bin/chezmoi/json`; never run `ki repo conform` without `--dry-run`; CAPTURE-GATE: no new records; commit by explicit path, retrying on `index.lock`; leave no `.git/*.lock`. Gate: `ki repo audit --repo .`, `node --test tests/*.test.mjs`, `rumdl check .`; the permitted baseline is the 22 warnings in `~/.local/state/ki/agents/chezmoi/ready-rest-3.baseline.json` plus `CLAUDEBIND-1`.

Report: the run report form, heading `# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › ground-076`, every record linked by its full identifier, each query with options, a recommendation and its confidence.
