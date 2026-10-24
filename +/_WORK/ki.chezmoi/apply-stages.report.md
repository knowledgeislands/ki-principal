# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.chezmoi/work.md) › apply-stages

**🤖 → 👤 Handoff to supervisor · Run report at 19:08 BST · last mark 08:51 BST**

---

## Done

Stages 1 and 2 of APPLY-PLAN are done on terra. I ran no unscoped `rig apply`, no bare `chezmoi apply` and no `chezmoi diff`. No source changed, so there is nothing to commit.

**The hold (RIG-CASKS).** The Rig in use is 0.8.0, run straight from the `tools-rig` checkout (`~/.local/bin/rig` links to it) at `87fa261`, level with `origin/main` as of the last fetch. It contains the cask fix `671c864` ("resolve cask auto-update metadata without a cask tap", 14 October), which first shipped in v0.6.3. So the fixed code is installed. Two caveats: it is the untagged v0.8.0 candidate (the newest tag is v0.7.0), not a Homebrew-installed release; and nothing on record names `671c864` as the bug behind the hold, so I've inferred that link from the date and subject. Today's targeted `rig apply` installed two Homebrew packages cleanly. The hold is yours to lift; it is still on.

**Stage 1**

- `rig doctor` before: 6 findings, the same six the plan listed (GitUp app and formula, the `.toml` handler on Warp, Dock order, firewall anchor, and the old `.toml` apply failure).
- Backup in `/tmp/apply-plan-backup`: `.zshrc`, Zed `settings.json`, `rig-tower-save-nudge` and the whole `conf.d`. All files existed.
- Scoped `chezmoi apply` of the 12 named targets: done, and a scoped `chezmoi status` of them is now clean. One difference from the plan: `~/.zsh/60_territory` now includes `557af1d` (the standard three-tab territory set), committed after the plan was written. Undo: copy the backup back and `rm -r ~/.config/starship ~/.config/ghostty ~/.zsh/60_territory ~/.zsh/99_starship ~/.zsh/completions/_starship`.
- Installs were done **through Rig**: `rig apply --scope tools --target starship --target font-symbols-only-nerd-font`. A dry run first showed exactly those two planned and nothing else. Both completed: Starship 1.27.0 and the Symbols Nerd Font (regular and mono). Undo: `brew uninstall starship && brew uninstall --cask font-symbols-only-nerd-font`.
- Shell: `zsh -i -c exit` starts with no errors. Starship loads with the `kris` variant, and `starship-variant` and `territory` are defined. I haven't tried a real Ghostty or Zed window.

**Stage 2: Warp retired**

- Nothing was running inside Warp. Warp itself was not running, so I quit nothing.
- Rig route: Rig _can_ remove a cask. You declare a `[remove.ID]` and then run `rig remove --target ID --apply`, which asks you to type `remove`. I didn't use it, because Rig lacked four things this job needed, and these go to RIG-REMOVAL:
  - It adds no zap: "Rig adds no force, zap or retained-data cleanup".
  - It doesn't handle login items.
  - It doesn't quit the app.
  - It needs a new `[remove.warp]` source declaration and an apply of that declaration, which the task doesn't name.
- Login item "Warp" removed through System Events. Undo: add it again in System Settings › General › Login Items.
- The 11 `~/.warp` targets were pending deletion under `.chezmoiremove`. A scoped `chezmoi apply` of the 11 named files removed them. A copy of the whole `~/.warp` is in `/tmp/apply-plan-backup/warp-dotdir`.
- `brew uninstall --zap --cask warp`: done. It removed `/Applications/Warp.app` and sent `~/.warp`, the Application Support data, the logs, the plist and the saved state to the Trash.
- Verified: no Warp app, cask, login item or process.
- Who now holds the file types:
  - `.toml`: **VS Code** (`com.microsoft.VSCode`), not Zed and not nothing (KI-TOOL-RIG-CORE-069).
  - `.sh` and `.zsh`: Ghostty, as expected until stage 3.
- No undo beyond `brew install --cask warp` and signing in again. Until the Trash is emptied, the zapped files can be put back from it.

**`rig doctor` after both stages: 6 findings** (the brief expected 4; the plan expected 6).

- `default-application.sh` and `default-application.zsh`: Ghostty instead of Zed. These are new, as the plan expected, because the source now declares the handlers. Stage 3 fixes them.
- `default-application.toml`: VS Code instead of Zed. Before, it was Warp. Stage 3 fixes it.
- `dock.workstation`: order drift. Stage 3 fixes it.
- `firewall.screen-sharing-tailnet`: anchor changed and exposed beyond the tailnet. This is held under NORDVPN-HOLD and FW-EXPOSURE (ki.mac-studio-setup) and was there before.
- One historical apply failure, `default-application:toml` (19 October). It clears when a later `.toml` apply succeeds.
- Gone: both GitUp findings. Starship and the font now check healthy.

## In Progress

Nothing.

- Left in place on purpose, because the task doesn't name them:
  - The Dock still has a broken Warp tile. Stage 3's Dock apply replaces it, or you can drag it out by hand.
  - Warp leftovers the zap doesn't cover: `~/Library/Group Containers/2BBY89MBSN.dev.warp`, `~/Library/Caches/dev.warp.Warp-Stable`, `~/Library/Caches/dev.warp.Warp-Preview` and two `~/Library/Logs/warp_preview.log.old.*` files.
- `/tmp/apply-plan-backup` is kept as the undo for stage 1. It clears at reboot, or delete it once you're happy.

## Queries

**HOLD-LIFT.**

**Context:** The fixed cask code, `671c864` (in Rig since v0.6.3), is in the Rig on terra, which runs from the `tools-rig` checkout at the v0.8.0 candidate. A targeted `rig apply` worked cleanly today. Stage 3, the handler and Dock apply, waits on this hold.

**Query:** Lift the both-Mac `rig apply` hold?

**Options:**

a) (recommended, confidence medium - the fix is present and a scoped apply behaved, but nothing on record ties the hold to that exact commit, and sol's Rig version wasn't checked) Lift it for terra now and run stage 3's targeted apply. Lift it for sol once sol's Rig is confirmed at the same commit or later.

b) Lift it on both Macs now.

c) Keep it until v0.8.0 is tagged and installed as a release.

**WARP-LEFTOVERS.**

**Context:** Warp's zap left 49 MB of Group Container data, two cache folders and the preview logs behind.

**Query:** Delete them?

**Options:**

a) (recommended, confidence high - you use nothing in Warp, and reinstalling recreates them) Yes. Move them to the Trash with the rest.

b) Leave them.
