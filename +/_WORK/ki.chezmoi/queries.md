# ki.chezmoi queries

## Open

- ORCA-INSTALL (Needs: decision, Kris): after tower-finish, one scoped `chezmoi apply ~/.config/rig/conf.d/10-applications.toml` covering Orca and Tower, `brew install --cask stablyai/orca/orca` (adds the vendor tap), `rig doctor` after, open Orca. a) do it, decline telemetry and the `~/.claude`/`~/.codex` import (recommended, high); b) same but accept the import; c) apply the Rig file only; d) hold. Undo: `brew uninstall --cask stablyai/orca/orca && brew untap stablyai/orca`, revert `a3b9736`, re-apply the file.
- STARSHIP-REVIEW (Needs: decision, Kris): accept [KB-DOTFILES-UE-104](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-104-evaluate-starship-with-chezmoi-drift.md) (Awaiting review)? Recommended (high confidence): a) accept it, then capture one Starship adoption record on hold until [KB-DOTFILES-UE-102](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-102-prompt-notice-for-unapplied-pulls.md) settles the cache contract, carrying UE-104's other three prerequisites as its steps; b) send it back for more investigation.
- Not raised: CORE-SET-COMMENTS (stays in the worksheet); FIREWALL-EXPOSURE (transient, re-check 05:18 showed only `anchor-changed`); RAT-UNCONFIRMED, RAT-READING (superseded by Decisions 179 and 181).

## Parked

None.
