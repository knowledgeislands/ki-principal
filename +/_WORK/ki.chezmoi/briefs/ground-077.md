# ground-077

Work: ki.chezmoi (KI > Rig > chezmoi). Repository: /Users/krisbrown/.local/share/chezmoi, on Sol.

Authority: OVERNIGHT, Kris on 20 October at 00:30 BST; recommended by the read-only survey [next-scan](/Users/krisbrown/.local/state/ki/agents/chezmoi/next-scan.report.md) - read it first.

Task: under `ki-plan`, ground and plan [KB-DOTFILES-UE-077](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-077-reorganise-1password-vaults-safely.md) in its record only: the source leftovers (docs/guides/tools/chezmoi.md, tests/op-cache.test.mjs, the possible false match in dot_warp/tab_configs/1-personal.toml) and the Automation-account guidance, as source-only Steps; per-Mac op-cache disposal as Kris's attended step. Do not implement the steps. Run no `op` command, and read no cache contents, item values or vault data. Bring it to the plan state the record rules allow without Kris's approval, and name what Kris must approve for Ready. Do not touch the record's `size` unless the plan makes it plain. One local commit.

Constraints: no `chezmoi apply`, restart, kill, `launchctl` change, push or fetch; never write `launchctl bootout` with an empty label; do not stage `bin/chezmoi/json`; never run `ki repo conform` without `--dry-run`; CAPTURE-GATE: no new records; commit by explicit path, retrying on `index.lock`; leave no `.git/*.lock`. Gate: `ki repo audit --repo .`, `node --test tests/*.test.mjs`, `rumdl check .`; the permitted baseline is the 22 warnings in `~/.local/state/ki/agents/chezmoi/ready-rest-3.baseline.json` plus `CLAUDEBIND-1`.

Report: the run report form, heading `# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › ground-077`, every record linked by its full identifier, each query with options, a recommendation and its confidence.
