# cpin

Work: ki.chezmoi (KI > Rig > chezmoi). Repository: /Users/krisbrown/.local/share/chezmoi, on Sol.

Authority: CMIGRATE-PIN a), taken at 00:36 BST under OVERNIGHT (Kris, 20 October at 00:30 BST: progress high-confidence work autonomously), confidence high after blind review ([cmigrate](/Users/krisbrown/.local/state/ki/agents/chezmoi/cmigrate.report.md), [cpin-blind](/Users/krisbrown/.local/state/ki/agents/chezmoi/cpin-blind.report.md)).

Task: in `dot_config/rig/conf.d/private_16-homebrew.toml`, move the Linux variant of `tool.mgit` from v0.16.0 to v0.18.0 and replace its checksum. First confirm the checksum yourself from the v0.18.0 tag in /Users/krisbrown/workspaces/knowledge-islands/tools-mgit (expected `sha256:0d8e6231506cd97608903d31d4ff0877cef629723d134f274cb22f9fd425a20c`), and confirm read-only that ki-techne-harness's converge script uses none of the changed mgit flags; stop if either fails. Capture `rig doctor`'s findings before and after and treat any new finding as caused by this change. Source only: nothing is rendered or applied for vega.

Constraints: no `chezmoi apply`, restart, kill, `launchctl` change, push or fetch; never write `launchctl bootout` with an empty label; do not stage `bin/chezmoi/json`; never run `ki repo conform` without `--dry-run`; CAPTURE-GATE: no new records; commit by explicit path, retrying on `index.lock`; leave no `.git/*.lock`. Gate: `ki repo audit --repo .`, `node --test tests/*.test.mjs`, `rumdl check .`; the permitted baseline is the 22 warnings in `~/.local/state/ki/agents/chezmoi/ready-rest-3.baseline.json` plus `CLAUDEBIND-1`.

Report: the run report form, heading `# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › cpin`, every record linked by its full identifier, each query with options, a recommendation and its confidence.
