# plan-084

Work: ki.chezmoi (KI > Rig > chezmoi). Repository: /Users/krisbrown/.local/share/chezmoi, on Sol. You may read /Users/krisbrown/workspaces/knowledge-islands/tools-techne read-only.

Authority: OVERNIGHT, Kris on 20 October at 00:30 BST; recommended by [next-scan](/Users/krisbrown/.local/state/ki/agents/chezmoi/next-scan.report.md).

Task: under `ki-plan`, ground and plan [KB-DOTFILES-UE-084](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-084-render-zshenv-on-vega.md) in its record only: check whether vega's harness in tools-techne already sets the XDG variables, then write the plan (the manifest line in `config-fragments/cheztoi/hosts/vega.toml` plus the test in `tests/cheztoi-render.test.mjs`). Do not implement and do not deploy; rollout on vega belongs to the agent-host Project. Bring it as far as the record rules allow without Kris's approval, and name what Kris must approve for Ready. One local commit.

Constraints: no `chezmoi apply`, restart, kill, `launchctl` change, push or fetch; never write `launchctl bootout` with an empty label; do not stage `bin/chezmoi/json`; never run `ki repo conform` without `--dry-run`; CAPTURE-GATE: no new records; commit by explicit path, retrying on `index.lock`; leave no `.git/*.lock`. Gate: `ki repo audit --repo .`, `node --test tests/*.test.mjs`, `rumdl check .`; the permitted baseline is the 22 warnings in `~/.local/state/ki/agents/chezmoi/ready-rest-3.baseline.json` plus `CLAUDEBIND-1`.

Report: the run report form, heading `# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › plan-084`, every record linked by its full identifier, each query with options, a recommendation and its confidence.
