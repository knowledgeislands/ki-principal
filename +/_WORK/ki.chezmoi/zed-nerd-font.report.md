# [chezmoi dotfiles](/Users/krisbrown/.local/share/chezmoi/README.md) › Terminal apps › zed-nerd-font

**🤖 → 👤 Handoff to supervisor · Run report at 08:35 BST**

---

## Done

- **Diagnosis confirmed.** Rendering `rainbow` with the trial kit's Starship gave 11 private-use glyphs. The variant file uses 44, from the Nerd Font ranges for Powerline, Seti/Devicons, Font Awesome, Font Logos, Octicons and Material Design. Zed has no built-in symbol font, so it draws them as boxes.
- **Font chosen: `font-symbols-only-nerd-font`, used as a fallback.** Zed's docs list `terminal.font_fallbacks`. The terminal keeps the editor font and adds `Symbols Nerd Font Mono` as its fallback. The Mono face keeps each symbol one cell wide, so the prompt stays aligned. No patched font family is needed.
- **Rig:** declared `tool.font-symbols-only-nerd-font` (cask, `core`, with both font files as artifacts and a rationale that says why it is there), and added it to the catalogue test's later additions (`768c59a`).
- **Zed:** added `font_fallbacks` to [the managed settings](/Users/krisbrown/.local/share/chezmoi/dot_config/zed/private_settings.json). I checked the live file against the source first and nothing needed merging back. I also added a "Terminal font" section to [the Zed guide](/Users/krisbrown/.local/share/chezmoi/docs/guides/tools/zed.md) (`768c59a`).
- **Starship guide:** the old "Nerd Font variants in Ghostty" section is now "Nerd Font variants", with a terminal table: Ghostty draws them from its built-in font, Zed once the font is installed, Terminal.app only with a Nerd Font set as its profile font, and Warp does not (`45bd78d`).
- **Checks:** `ki repo audit` passed with 0 failures (5 warnings, all there before); `node --test` 347 of 349 passed, 0 failed, 2 skipped; `rumdl` clean. `rig doctor` on a candidate render went from 7 to 8 findings. The one new finding is the expected `font-symbols-only-nerd-font: missing`, which clears once the font is installed.
- **Existing `rig doctor` findings, read but not fixed:** `starship` missing (waiting on its install); the `.sh`, `.zsh` and `.toml` handler drift plus the old `.toml` apply failure (waiting on terminal-retire's apply); `dock.workstation` order drift; and `firewall.screen-sharing-tailnet` drift. Each needs an install or an apply, which this run had no authority to do.
- Nothing changed in `$HOME`. No apply, no install and no push. No lock files are left behind.

## In Progress

Nothing.

## Queries

**ZED-FONT-APPLY · Needs: decision**

**Context:** The font has to be installed and Zed's settings applied before Zed's terminal draws the symbols. The Rig file `~/.config/rig/conf.d/10-applications.toml` also carries other runs' unapplied changes: Ghostty's new rationale, Warp and GitUp removed, and Orca added. Applying it lands all of them. Zed only needs the font and its own settings file; the Rig file only records the intent.

**Query:** Shall I install the font and apply Zed's settings now, leaving the Rig file to go with terminal-retire's apply?

**Options:** a) (recommended, confidence high - Zed needs only these two steps, and the Rig file stays with the other runs' pending changes) Run `brew install --cask font-symbols-only-nerd-font`, then `chezmoi apply ~/.config/zed/settings.json`, then close and reopen Zed's terminal panel (or restart Zed) and run `starship-variant rainbow` there. Apply `~/.config/rig/conf.d/10-applications.toml` together with terminal-retire's apply, then run `rig doctor`; the `font-symbols-only-nerd-font` finding should not appear. b) Apply everything now: `brew install --cask font-symbols-only-nerd-font`, then `chezmoi apply ~/.config/zed/settings.json ~/.config/rig/conf.d/10-applications.toml && rig doctor`, then restart Zed's terminal. This also lands the Ghostty, Warp, GitUp and Orca Rig changes. c) Hold.

Undo: `brew uninstall --cask font-symbols-only-nerd-font`, then `git revert 768c59a` in the chezmoi source and `chezmoi apply ~/.config/zed/settings.json` (and the Rig file, if it was applied). Zed with no fallback font goes back to drawing boxes, with no other effect.
