# chezmoi › apply-check

**🤖 → 👤 Handoff to supervisor · Run report at 08:12 BST**

---

## Done

- Waited for motion-remove, which finished at 08:04 BST. Its only commit changes a roadmap record under the ignored `docs/` folder, so Motion adds no targets to the apply.
- Checked the host: this is terra. Changed nothing on the machine or in the repository.
- Baseline `rig doctor` has 6 findings. I read each one:
  - `gitup` and `gitup-formula` are reported missing. The GitUp retirement removed them from the machine but its declaration is not yet applied.
  - `dock.workstation` has drifted in its order. Tower Assistant is already pinned in the Dock, but the live declaration does not list it yet.
  - `default-application.toml` is drifted: `.toml` files open in Warp, but Zed is declared. This was already there.
  - `firewall.screen-sharing-tailnet` is drifted: its anchor changed and Screen Sharing is exposed beyond the tailnet. This was already there.
  - There is 1 historical apply failure, for `default-application:toml` on 19 October.
- Four targets are in scope, and each pending diff matches its commits line for line (49 Rig lines and 10 script lines):
  - `~/.config/rig/conf.d/10-applications.toml` (GitUp and Orca)
  - `~/.config/rig/conf.d/16-homebrew.toml` (GitUp)
  - `~/.config/rig/conf.d/40-macos.toml` (Tower Dock)
  - `~/bin/scheduled/rig-tower-save-nudge` (Tower)
- Two targets are out of scope, and I left them alone: `~/.claude/settings.json` and `~/.codex/hooks.json`. Both show as changed on both sides (`MM`) because Orca has added its own agent hooks (`ORCA_AGENT_HOOK_*`) to the live files. Applying them would strip those hooks, so they are not in the command. See ORCA-HOOKS.
- Candidate check: I rendered the three Rig files with `chezmoi cat` into a temporary copy of `~/.config/rig` and ran `RIG_CONFIG_HOME=<copy> rig doctor` read-only. Findings go from 6 to 3:
  - `gitup`, `gitup-formula` and `dock.workstation` clear.
  - Only the firewall finding, the `.toml` handler finding and the historical failure remain.
  - Nothing new appears, and passing checks go from 244 to 246.
- Orca's CLI link raises no finding. `orca` is observed as present and self-updating. The live `/opt/homebrew/bin/orca` is the cask's own symlink to `/Applications/Orca.app/Contents/Resources/bin/orca`, which is exactly the declared source. Because `owner = "provider"`, Rig treats Homebrew as the link's owner and leaves the link alone.

## In Progress

Nothing.

## Queries

**RIG-APPLY: combined apply on terra**

**Context:** The apply changes four files and nothing else.

- In the Rig declarations, it drops the `gitup` cask and `gitup` formula entries, adds Orca (laptop profile only, with its provider-owned CLI link), and adds Tower Assistant to `dock.workstation` after The Tower.
- In `rig-tower-save-nudge`, it makes the script prefer `/Applications/Tower Assistant.app` and fall back to `~/Applications`.

`chezmoi apply` only writes these files. It does not run `rig apply`, so no package, Dock or firewall state changes. Expected `rig doctor` findings go from 6 to 3:

- These clear: `gitup`, `gitup-formula` and `dock.workstation`.
- These remain and were already there: the firewall drift (`firewall.screen-sharing-tailnet`), the `.toml` handler set to Warp rather than Zed, and the historical failure from 19 October.

`rig doctor` will still exit non-zero because of those 3.

The command is:

`chezmoi apply ~/.config/rig/conf.d/10-applications.toml ~/.config/rig/conf.d/16-homebrew.toml ~/.config/rig/conf.d/40-macos.toml ~/bin/scheduled/rig-tower-save-nudge && rig doctor`

To undo it, restore the earlier files from Git. None of these sources is a template, so each file can be copied straight back from commit `eb5f69a`:

- `git -C ~/.local/share/chezmoi show eb5f69a:dot_config/rig/conf.d/private_<name>.toml > ~/.config/rig/conf.d/<name>.toml`, once for each of `10-applications`, `16-homebrew` and `40-macos`
- `git -C ~/.local/share/chezmoi show eb5f69a:bin/scheduled/executable_rig-tower-save-nudge > ~/bin/scheduled/rig-tower-save-nudge`

**Query:** Run the combined apply?

**Options:** a) (recommended, confidence high - the candidate check shows 6 to 3 findings with nothing new, and each diff matches its commits exactly) Run the command above. b) Apply only the Rig declarations now, and apply the nudge script after Tower Assistant moves to `/Applications`. c) Do not apply.

**ORCA-HOOKS: Orca wrote hooks into managed agent settings**

**Context:** Orca has added agent hooks to the live `~/.claude/settings.json` and `~/.codex/hooks.json`. Both are managed by chezmoi and also have source changes waiting. A future unscoped `chezmoi apply` would remove Orca's hooks.

**Query:** How should Orca's hooks be handled?

**Options:** a) (recommended, confidence medium - the repository has a reverse-merge pattern for runtime-changed configuration) Start a separate run to decide whether Orca's hooks belong in the source, and reverse-merge them if so. b) Let Orca's hooks be overwritten while it is being evaluated. c) Leave both files unapplied for now.
