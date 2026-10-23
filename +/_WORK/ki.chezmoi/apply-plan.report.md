# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.chezmoi/work.md) › apply-plan

**🤖 → 👤 Handoff to supervisor · Run report at 08:46 BST · last mark 23:56 BST**

---

## Done

- Read-only plan, built against source `45bd78d`, with nothing applied, installed or committed. Every pending target was checked with a scoped `chezmoi status` or `chezmoi diff`. The Rig candidate was copied to a temporary directory and checked with `rig doctor` and a targeted `rig apply --dry-run`. Temporary copies are removed.
- Gate: `ki repo audit --repo .` passed with 0 failures and 5 old warnings. `node --test tests/*.test.mjs` passed (31 suites). `rumdl check .` passed.
- **Pending on terra, all from committed source.** New targets: `~/.config/ghostty/config.ghostty`, `~/.config/starship/variants/*` (7 files), `~/.zsh/60_territory`, `~/.zsh/99_starship` and `~/.zsh/completions/_starship`. Changed targets:
  - `~/.zshrc` drops the iTerm2 integration line.
  - `~/.config/zed/settings.json` adds `terminal.font_fallbacks = ["Symbols Nerd Font Mono"]`.
  - `~/bin/scheduled/rig-tower-save-nudge` prefers `/Applications` and falls back to `~/Applications`, which is where Tower Assistant is now.
  - Four Rig files change. `10-applications` drops GitUp and Warp and adds Orca, the Nerd Font and Ghostty's new wording. `16-homebrew` drops the gitup formula and adds Starship. `40-macos` changes the Dock (Warp → Ghostty, plus Tower Assistant) and adds the `.sh` and `.zsh` handlers. `60-skills` drops the Warp runtime.
  - The 11 `~/.warp` files are pending deletion.
- **Never run a bare `chezmoi apply`.** `~/.claude/settings.json` and `~/.codex/hooks.json` are also pending, and both hold Orca's hooks (ORCA-HOOKS). Every stage below names its targets.
- **Removing Warp from Rig while Warp is still installed and running is safe.** Rig never uninstalls a tool that is no longer declared. Its retirement covers only services, scheduled jobs and firewall rules, and `rig remove` acts only on an explicitly declared removal. Removing the Warp runtime from `caveman` does nothing, because `~/.warp/skills` does not exist. The only effect is that Warp leaves `rig doctor`'s list of self-updating apps. So the Rig files go in stage 1.
- **The Rig files can't be applied separately.** chezmoi writes each file whole, so RIG-APPLY, STARSHIP-APPLY, ZED-FONT-APPLY and terminal-retire share them. `40-macos` alone carries Tower Assistant, Ghostty and the handlers. One apply of all four files replaces the separate offers.
- **`rig doctor` today: 6 findings.**
  - GitUp and the gitup formula are missing.
  - `default-application.toml` belongs to Warp, not Zed (TOML-HANDLER, accepted).
  - The Dock is out of order.
  - `firewall.screen-sharing-tailnet` has its anchor changed (NORDVPN-HOLD and FW-EXPOSURE, routed to ki.mac-studio-setup).
  - One old apply failure is recorded for the `.toml` handler.
- **`rig doctor` with the candidate files, before the installs: 8 findings.**
  - Gone: both GitUp findings.
  - New: `starship` and `font-symbols-only-nerd-font` missing, and the `.sh` and `.zsh` handlers belonging to Ghostty rather than Zed.
  - Orca and the Tower Assistant Dock item check out healthy.
- **Warp's cask zap trashes, so everything stays recoverable until the Trash is emptied.** It covers `~/.warp`, `~/Library/Application Support/dev.warp.Warp-Stable` (401 MB), `~/Library/Logs/warp.log*`, the preferences plist and the saved state. It leaves behind `~/Library/Group Containers/2BBY89MBSN.dev.warp` (49 MB), `~/Library/Caches/dev.warp.Warp-Stable`, `~/Library/Caches/dev.warp.Warp-Preview` and `~/Library/Logs/warp_preview.log.old.*`. Warp is also a login item.

### The plan

**Stage 1: installs and everything except Warp's files and Rig's handlers and Dock.**

1. Back up the files that will change:

   ```sh
   B=/tmp/apply-plan-backup && mkdir -p $B && cp -p ~/.zshrc ~/.config/zed/settings.json ~/bin/scheduled/rig-tower-save-nudge $B/ && cp -Rp ~/.config/rig/conf.d $B/conf.d
   ```

2. Install Starship and the font:

   ```sh
   brew install starship && brew install --cask font-symbols-only-nerd-font
   ```

3. Apply the targets:

   ```sh
   chezmoi apply ~/.config/starship ~/.zsh/99_starship ~/.zsh/completions/_starship ~/.zsh/60_territory ~/.zshrc ~/.config/ghostty ~/.config/zed/settings.json ~/bin/scheduled/rig-tower-save-nudge ~/.config/rig/conf.d/10-applications.toml ~/.config/rig/conf.d/16-homebrew.toml ~/.config/rig/conf.d/40-macos.toml ~/.config/rig/conf.d/60-skills.toml
   ```

4. Verify:
   - Run `rig doctor`.
   - Open a new Ghostty window and run `starship-variant`, then `territory ki` (the first use asks for Automation permission).
   - Reopen Zed's terminal and run `starship-variant rainbow`.

**What stage 1 changes:**

- The Starship prompt appears in new shells; Warp keeps its own prompt.
- Ghostty gets its theme and its notice when a long command finishes.
- `territory` and Zed's fallback font become available.
- Rig no longer lists GitUp or Warp, and lists Orca, Starship and the font.
- The nudge script finds Tower Assistant in `~/Applications`.

**Undo:**

- `brew uninstall starship` and `brew uninstall --cask font-symbols-only-nerd-font`.
- Copy `$B/*` and `$B/conf.d/*` back.
- `rm -r ~/.config/starship ~/.config/ghostty ~/.zsh/60_territory ~/.zsh/99_starship ~/.zsh/completions/_starship`.

**Expected `rig doctor` after stage 1: 6 findings.** They are the `.sh`, `.zsh` and `.toml` handlers, the Dock order, the firewall anchor and the old `.toml` failure.

**Stage 2: Kris's attended Warp retirement.** Run it only after Ghostty has proved itself in daily use.

1. List the open Warp sessions and anything running in them.
2. Export Warp Drive (workflows, notebooks, prompts) and its settings, then put the exports in OneDrive.
3. Check on sol whether Warp is signed in to the same account. If it is, keep the cloud data and do not delete the account.
4. Sign out of Warp.
5. Quit Warp.
6. Remove Warp from System Settings › General › Login Items.
7. Remove the managed Warp files:

   ```sh
   chezmoi apply ~/.warp/settings.toml ~/.warp/keybindings.yaml ~/.warp/tab_configs
   ```

   If the `tab_configs` directory target is refused, name the nine files.
8. Uninstall Warp:

   ```sh
   brew uninstall --zap --cask warp
   ```

9. Decide separately whether to delete the leftovers the zap doesn't cover (listed above).
10. Run `rig doctor`.

**Undo:** `brew install --cask warp`, then sign in and import the exports. Before the Trash is emptied, the zapped files can be put back from it.

**Expected `rig doctor` after stage 2: still 6.** The Dock tile for Warp is broken until stage 3; remove it by hand.

**Stage 3: the handler and Dock apply.** Run it only when the both-Mac Rig apply hold is lifted.

1. Run the targeted apply. It leaves out the firewall, which is held under NORDVPN-HOLD:

   ```sh
   rig apply --scope resources --target default-application:sh --target default-application:zsh --target default-application:toml --target dock:workstation
   ```

   This was checked as a dry run against the candidate: all four targets are `planned reconcile`.
2. Verify: run `rig doctor`, open a `.sh` file from Finder (it should open in Zed) and look at the Dock.

**Undo:** set the handler back in Finder › Get Info › Open with › Change All. Rig does not keep a copy of the previous Dock.

**Expected `rig doctor` after stage 3: 1 to 3 findings.** The firewall anchor stays. If the `.toml` handler fails again, as it did on 19 October, it adds two findings: the handler and its recorded failure (TOML-HANDLER, KI-TOOL-RIG-CORE-069).

**Drift until stage 3 runs:**

- `.sh` and `.zsh` files open in Ghostty, which runs them.
- `.toml` files open in Warp, or in whatever app takes them after Warp's zap.
- The Dock still has Warp and lacks Ghostty and Tower Assistant.
- That leaves 6 `rig doctor` findings.

**Gap:** Ghostty has no sidebar and no view of the last command. It offers only prompt-to-prompt navigation and tab titles, so nothing yet replaces Warp's sidebar workflow.

## In Progress

Nothing.

## Queries

**APPLY-PLAN.** This replaces RIG-APPLY, STARSHIP-APPLY and ZED-FONT-APPLY, and settles when WARP-RETIRE's stages run.

**Context:** The four apply offers share the same four Rig files and so can't be applied separately. Removing Warp from Rig is safe while Warp is still installed. Ghostty has no sidebar to replace Warp's.

**Query:** Which order should the stages run in?

**Options:**

a) (recommended, confidence high - reversible, takes Warp out of nothing that is running, and leaves its data in place until Ghostty has proved itself) Run stage 1 now. Run stage 2 later in one attended sitting, once Ghostty has proved itself and sol's account has been checked. Run stage 3 when the both-Mac hold lifts, removing the Warp Dock tile by hand in the meantime.

b) Run stages 1 and 2 together now, in one attended sitting, and stage 3 when the hold lifts.

c) Run stage 1 without the four Rig files and the nudge script. Rig would keep listing GitUp and Warp until stage 3.

d) Hold everything.
