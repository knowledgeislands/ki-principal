# [chezmoi](/Users/krisbrown/.local/share/chezmoi/README.md) › drift-survey

**🤖 → 👤 Handoff to supervisor · Run report at 11:56 BST**

---

## Done

- Surveyed terra's drift read-only. Nothing was applied, installed, committed or changed, and the temporary files have been removed.
- I skipped `git pull --ff-only` because the run's rules ban every remote call. The source checkout is clean, holds no uncommitted edits from another session and matches the last-fetched `origin/main`, so no target is held by someone else's edit.
- `chezmoi status` shows 37 drifted entries: 22 in group A stage 1, 11 in group A stage 2 (Warp), none in group B, 2 in group C (one of them only reorders), and 1 in group D. No new targets have appeared since the staged plan.
- I did not diff `~/.codex/config.toml`, because its template pulls MCP environment values from 1Password through `mcp-servers-json`. Every other target was diffed individually.
- `rig doctor` reports unhealthy with 6 findings. All of them are mapped in the second table below.

### Drifted targets

| Target | Group | Cause | Proposed action |
| --- | --- | --- | --- |
| `~/.config/starship`, `variants/`, and the 7 variant files (`dev`, `kris-nerd`, `kris`, `one-line`, `pure`, `rainbow`, `two-line`) | A1 | New Starship variants in source | Apply with stage 1 |
| `~/.zsh/99_starship`, `~/.zsh/completions/_starship`, `~/.zsh/60_territory` | A1 | New source fragments | Apply with stage 1 |
| `~/.zshrc` | A1 | Source removes the iTerm2 shell-integration line | Apply with stage 1 |
| `~/.config/ghostty`, `config.ghostty` | A1 | New Ghostty config | Apply with stage 1 |
| `~/.config/zed/settings.json` | A1 | Adds the `Symbols Nerd Font Mono` fallback; Zed has not changed the live file since the last apply | Apply with stage 1 |
| `~/bin/scheduled/rig-tower-save-nudge` | A1 | Looks for `/Applications/Tower Assistant.app` first, then the `~/Applications` copy (where it is today) | Apply with stage 1 |
| `~/.config/rig/conf.d/10-applications.toml` | A1 | Adds the symbols-only Nerd Font and Orca (evaluating); rewrites the Ghostty text; drops GitUp | Apply with stage 1 |
| `~/.config/rig/conf.d/16-homebrew.toml` | A1 | Drops `gitup-formula` | Apply with stage 1 |
| `~/.config/rig/conf.d/40-macos.toml` | A1 | Dock: Ghostty replaces Warp and Tower Assistant is added; `.sh` and `.zsh` files open in Zed | Apply with stage 1 (see Query 1 on losing the Warp Dock pin) |
| `~/.config/rig/conf.d/60-skills.toml` | A1 | Changes the runtimes list | Apply with stage 1 |
| `~/.warp/keybindings.yaml`, `settings.toml`, and `tab_configs/1-personal` … `9-dotfiles` (11 files) | A2 | Source has retired Warp, so apply would delete all 11 | Hold while Warp is in use (Query 2) |
| `~/.claude/settings.json` | C | Orca added its hook. The `modify_` binding keeps it and only reorders it against the coordinator hooks; compared without ordering, the two files are identical | Harmless; apply with stage 1 |
| `~/.codex/hooks.json` | C | Orca added a Codex hook to 9 events. The source is a full template, not a fragment binding | Do not apply as it stands (Query 3) |
| `~/.codex/config.toml` | D | Both sides changed. The live file has 11 hook-trust entries, 9 of them Orca's; the binding preserves undeclared keys, so it would not drop them. The rest of the difference is unknown because the target was not diffed | Attended diff (Query 4) |

### Rig doctor findings

| Finding | Cleared by |
| --- | --- |
| `gitup` missing (`/Applications/GitUp.app`) | Stage 1 apply: source removes the declaration |
| `gitup-formula` missing | Stage 1 apply: same |
| `dock.workstation` drifted (order) | None on its own: a stage 1 apply followed by `rig apply` |
| `default-application.toml` handler is Warp, Zed expected | None: needs `rig apply`. The same target failed an apply on 19 Oct (exit 1); read that failure before rerunning |
| `firewall.screen-sharing-tailnet` drifted (anchor changed) | None: an attended `rig apply --sudo`. This is connection-critical and needs a tested restore path |
| The recorded apply failure (`default-application:toml`, 19 Oct) | Clears once the handler apply succeeds |

### Terra: actionable now

- Shadowlab Spark launcher `/Applications/Spark.app` (`com.xenonium.Spark`) is still installed, although the catalogue retired it on 20 Oct (`955faf5`). Remove it through the `ki-self` lifecycle. Spark Desktop stays.
- [KB-DOTFILES-UE-086](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-086-finish-software-alignment.md) B6a: Clockology, Prime Video and Nitro are still installed (`sudo mas uninstall`).
- KB-DOTFILES-UE-086 B6b: BlueStacks and its multi-instance manager are still installed.
- KB-DOTFILES-UE-086 B6d/B6e: the Homebrew `cloudflare-wrangler` and `node` formulae are still installed.
- KB-DOTFILES-UE-086 B1–B5: the mise Python/uv switch has not been done; Homebrew `uv` and `python@3.10` are still installed.
- KB-DOTFILES-UE-086 B7: Mercury Weather is already gone. The step only needs ticking.
- KB-DOTFILES-UE-086 C7i (terra part): Adobe Creative Cloud is still installed.
- [KB-DOTFILES-UE-090](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-090-close-rig-bring-up-gaps.md): `~/bin/rig-bringup-check` is already applied, with no drift. What remains is the attended run at the screen and the guide's checks.
- [KB-DOTFILES-UE-100](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-100-mcporter-daemon-child-leak.md): the attended Terra mcporter evidence collection is still open.
- Not actionable yet: KB-DOTFILES-UE-086 B8a (UTM cask receipt), which first needs a removal method that keeps the app. No host-conditional template branches exist; `seats.yaml` and the empty `cheztoi` values need nothing.

## In Progress

Nothing.

## Queries

**Query 1 — stage 1 apply**

**Context:** 22 stage 1 targets are clean, source-ahead changes, and the harmless `~/.claude/settings.json` reorder would go with them. A stage 1 apply followed by a non-sudo `rig apply` clears both GitUp findings and the Dock finding. The Dock change removes the Warp pin while you still use Warp.

**Query:** Apply stage 1 now, including `~/.claude/settings.json`, and then run `rig apply` without sudo?

**Options:** a) (recommended, confidence medium - everything is source-ahead with no live edits; the only cost is the Warp Dock pin) Apply stage 1 plus `~/.claude/settings.json`, then `rig apply`, after reading the 19 Oct handler failure. b) As a), but first keep a Warp Dock item in `40-macos.toml` until Warp is retired. c) Hold.

**Query 2 — Warp stage 2**

**Context:** The stage 2 apply would delete `~/.warp/keybindings.yaml`, `~/.warp/settings.toml` and all 9 `tab_configs` files. Warp would lose its keybindings, settings and tab layouts. The source keeps them only in Git history.

**Query:** When should the 11 Warp targets go?

**Options:** a) (recommended, confidence high - Warp is still in use) Hold stage 2 until Warp is retired. b) Apply now and accept losing the Warp configuration.

**Query 3 — Orca's Codex hooks**

**Context:** `~/.codex/hooks.json` is a full template. Applying it removes Orca's hook from SessionStart, UserPromptSubmit, PreToolUse, PermissionRequest, PostToolUse, SubagentStart, SubagentStop, Stop and Interrupt, which breaks Orca's Codex integration until Orca writes them back. Orca is declared as being evaluated.

**Query:** How should `~/.codex/hooks.json` treat Orca's hooks?

**Options:** a) (recommended, confidence high - matches how `~/.claude/settings.json` already preserves them) Leave the target out of applies for now, and capture a record to convert it to a `modify_` fragment binding that owns only the coordinator hooks. b) Apply now and let Orca reinstall its hooks. c) Reverse-merge Orca's hooks into the template; not advised, because they are Orca-generated and machine-specific.

**Query 4 — Codex config.toml**

**Context:** Both sides have changed. I did not diff it because rendering it reads 1Password-backed MCP values. The binding preserves undeclared keys, so Orca's trust entries would survive.

**Query:** May the diff be run at the screen?

**Options:** a) (recommended, confidence medium - the content of the difference is unknown) You run `chezmoi diff ~/.codex/config.toml` while attending, then decide. b) Apply it with stage 1 without reviewing.

**Query 5 — firewall and handler**

**Context:** The Screen Sharing firewall anchor has drifted. Fixing it needs `rig apply --sudo` and is connection-critical: it governs Screen Sharing over Tailscale.

**Query:** Fix the firewall now?

**Options:** a) (recommended, confidence medium) Do it in a separate attended session with a tested restore path, after reading the `rig doctor` anchor detail. b) Leave it until the next Rig session.

**Query 6 — terra removals**

**Context:** The terra items above are all removals that you attend: the Spark launcher, Clockology, Prime Video, Nitro, BlueStacks, the `cloudflare-wrangler` formula and Creative Cloud.

**Query:** Run them now?

**Options:** a) (recommended, confidence high - each is already decided in KB-DOTFILES-UE-086 or the catalogue) One attended removal run through `ki-self`, ticking KB-DOTFILES-UE-086 B6a, B6b, B6d, B7 and the terra part of C7i. b) Leave them for the KB-DOTFILES-UE-086 session.
