# chezmoi › motion-remove

**🤖 → 👤 Handoff to supervisor · Run report at 08:03 BST**

---

## Done

- Checked the host: this is terra. Only one candidate exists, `/Applications/Motion.app` (`com.electron.motion` 0.99.0, the usemotion.com calendar and task app). It was a direct download, not a cask or App Store install. It had no login item, launch agent, helper or Dock tile, and nothing in the chezmoi source, `~/bin` or the shell configuration used it. Rig never declared it; only [KB-DOTFILES-UE-086](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-086-finish-software-alignment.md) named it, on the removal list.
- Uninstalled Motion. It was not running. The bundle, `~/Library/Application Support/Motion` (696 MB of local Electron data), the logs, the HTTP storage and cookies, and the caches (including Sparkle) are now in `~/.Trash/motion-remove-202610220753`. I also deleted the `com.electron.motion` preferences domain, and a copy of its plist is in that Bin folder. To undo, move the folder's contents back and run `defaults import com.electron.motion <plist>`. The app's cloud account data was not touched. A leftover `motion-desktop` URL-scheme entry in LaunchServices points at nothing and does no harm; I left it alone because the brief did not name it.
- Checked it is gone: the bundle, the preferences domain, the Spotlight entry and any running process are all absent, and `rig status --unmanaged` no longer lists Motion.
- Recorded the removal in step B6c of KB-DOTFILES-UE-086 (`f035d70`). There were no catalogue or test edits, because Rig never declared Motion.
- Repository checks: `ki repo audit` passed with 0 failures (5 warnings, which were already there); `node --test` passed 329 of 331 with 0 failures; `rumdl` was clean.
- `rig doctor` found 4 problems before and 6 after. Motion caused none of them. The 2 new ones are `gitup` and `gitup-formula` showing as missing, because the gitup-remove commit (`0ec53fa`) is not yet applied. They clear when that run's apply happens.
- The 4 that were already there:
  - The `.toml` file handler is Warp, but Zed is declared. Its last apply failed on 19 October.
  - The Dock order differs from the declaration (the pending Tower change).
  - `firewall.screen-sharing-tailnet` reports anchor-changed and exposed-beyond-tailnet. This is connection-critical, so I left it.
  - A historical apply failure is recorded for the default-application target.

## In Progress

- Nothing. On sol, check whether Motion is installed (UE-086 only knew of it on the laptop). If it is, remove it the same way. sol needs no Rig apply for Motion.

## Queries

**MOTION-APPLY — scoped apply**

**Context:** My commit changed only a roadmap record. `docs/` is in `.chezmoiignore`, so no Rig or other chezmoi target changed, and the scoped diff is empty. I touched neither the Orca file (`10-applications.toml`) nor the Tower file (`40-macos.toml`).

**Query:** Is any apply needed for Motion?

**Options:** a) (recommended, confidence high - no target changed) No apply for Motion; the GitUp apply stays with the gitup-remove run. b) Run `chezmoi diff ~/.config/rig/conf.d && rig doctor` anyway to confirm it is empty.

**firewall.screen-sharing-tailnet** (FW-SCREENSHARE)

**Context:** `rig doctor` reports the screen-sharing firewall anchor as changed and exposed beyond the tailnet. It was already there, and it is connection-critical.

**Query:** Should a separate run look into it, with a tested restore path?

**Options:** a) (recommended, confidence medium - a possible exposure deserves its own run) Queue a separate investigation run. b) Leave it until the both-Mac hold lifts.
