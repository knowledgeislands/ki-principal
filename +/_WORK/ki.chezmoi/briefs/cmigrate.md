# cmigrate

Work: ki.chezmoi (KI > Rig > chezmoi). Repository: /Users/krisbrown/.local/share/chezmoi, on Sol.

Authority: CONSUMER-MIGRATE (state.md next step) and OVERNIGHT, Kris on 20 October at 00:30 BST: progress high-confidence work autonomously.

Task: mgit v0.18.0 is released. Read its CHANGELOG and any migration guide in /Users/krisbrown/workspaces/knowledge-islands/tools-mgit, read-only, and find what this chezmoi source owes as a consumer: configuration, completions, templates or documentation. If the change is small, reversible, source-only and high confidence, make it, gate and commit locally. Otherwise make no change and report the needed change as a query. Change nothing in tools-mgit.

Constraints: no `chezmoi apply`, restart, kill, `launchctl` change, push or fetch; never write `launchctl bootout` with an empty label; do not stage `bin/chezmoi/json`; never run `ki repo conform` without `--dry-run`; CAPTURE-GATE: no new records; commit by explicit path, retrying on `index.lock`; leave no `.git/*.lock`. Gate: `ki repo audit --repo .`, `node --test tests/*.test.mjs`, `rumdl check .`; the permitted baseline is the 22 warnings in `~/.local/state/ki/agents/chezmoi/ready-rest-3.baseline.json` plus `CLAUDEBIND-1`.

Report: the run report form, heading `# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › cmigrate`, every record linked by its full identifier, each query with options, a recommendation and its confidence.
