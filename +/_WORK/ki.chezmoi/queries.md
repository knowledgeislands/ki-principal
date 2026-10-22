# ki.chezmoi queries

## Open

- RIG-APPLY (Needs: decision, Kris; replaces TOWER-APPLY and GITUP-APPLY): `chezmoi apply ~/.config/rig/conf.d/10-applications.toml ~/.config/rig/conf.d/16-homebrew.toml ~/.config/rig/conf.d/40-macos.toml ~/bin/scheduled/rig-tower-save-nudge && rig doctor`; candidate doctor 6 → 3 (gitup, gitup-formula, dock clear; firewall, `.toml` handler, 19 October failure remain), nothing new; undo from `eb5f69a`. a) apply (recommended, high); b) Rig files now, nudge script after the move; c) do not apply.
- ORCA-HOOKS (in blind review, orca-hooks-blind): Orca wrote `ORCA_AGENT_HOOK_*` hooks into live `~/.claude/settings.json` and `~/.codex/hooks.json`; an unscoped apply would strip them.
- TOWER-PATH (Needs: decision, Kris): Rig has no fallback-path form, so the artefact and Dock path stay `~/Applications` until the move. a) keep until Kris moves it, then one follow-up commit switches both (recommended, high); b) switch now and accept drift; c) raise a tools-rig any-of path item.
- TOWER-MOVE (Needs: attendance, Kris): quit Tower Assistant, `bash apps/macos-tower-companion/build.sh install` in `~/workspaces/personal/apps-tower.midnight.ninja` (admin), launch `/Applications/Tower Assistant.app`, check Permissions… reads Allowed, re-enable Start at Login, remove `~/Applications/Tower Assistant.app`.
- Not raised: CORE-SET-COMMENTS (stays in the worksheet); FIREWALL-EXPOSURE (transient, re-check 05:18 showed only `anchor-changed`); RAT-UNCONFIRMED, RAT-READING (superseded by Decisions 179 and 181).

## Parked

None.
