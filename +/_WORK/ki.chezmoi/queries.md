# ki.chezmoi queries

## Open

- TOWER-APPLY (Needs: decision, Kris): `chezmoi apply ~/.config/rig/conf.d/40-macos.toml ~/bin/scheduled/rig-tower-save-nudge && rig doctor` (expect 3, Dock cleared). a) apply (recommended, high: candidate doctor 4 → 3, nothing new); b) wait for the post-move path change; c) do not apply.
- TOWER-PATH (Needs: decision, Kris): Rig has no fallback-path form, so the artefact and Dock path stay `~/Applications` until the move. a) keep until Kris moves it, then one follow-up commit switches both (recommended, high); b) switch now and accept drift; c) raise a tools-rig any-of path item.
- TOWER-MOVE (Needs: attendance, Kris): quit Tower Assistant, `bash apps/macos-tower-companion/build.sh install` in `~/workspaces/personal/apps-tower.midnight.ninja` (admin), launch `/Applications/Tower Assistant.app`, check Permissions… reads Allowed, re-enable Start at Login, remove `~/Applications/Tower Assistant.app`.
- STARSHIP-REVIEW (Needs: decision, Kris): accept [KB-DOTFILES-UE-104](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-104-evaluate-starship-with-chezmoi-drift.md) (Awaiting review)? Recommended (high confidence): a) accept it, then capture one Starship adoption record on hold until [KB-DOTFILES-UE-102](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-102-prompt-notice-for-unapplied-pulls.md) settles the cache contract, carrying UE-104's other three prerequisites as its steps; b) send it back for more investigation.
- Not raised: CORE-SET-COMMENTS (stays in the worksheet); FIREWALL-EXPOSURE (transient, re-check 05:18 showed only `anchor-changed`); RAT-UNCONFIRMED, RAT-READING (superseded by Decisions 179 and 181).

## Parked

None.
