---
id: ki.chezmoi
state: with-worker
since: 2026-10-22T06:42:00Z
received: 2026-10-20T01:30:00Z
beat: null
mark: 2026-10-21T22:56:00Z
method_read: beb56729
---

# ki.chezmoi state

## Now

- radar-design done: ring needs tools-rig to reach doctor and the site; RADAR-DESIGN with Kris (high); RADAR-PUBLIC in blind review (radar-public-blind). terminal-retire, starship-classic running; zed-nerd-font queued after terminal-retire.
- handover-route done (Decision 206): NORDVPN-HOLD, FW-EXPOSURE, HANDLER-FAIL to ki.mac-studio-setup (`30018774`), HOOK-ROLLOUT to ki.tools-burndown (`ee440eef`); TOWER-MOVE is kb.regular.site-tower's; all 'unpushed' commits were already on origin; both receiving works are on hold. route-2 done: RIG-APP-FOOTPRINT (important) to ki.mac-studio-setup (`7f70fb40`), TOWER-PATH-WAIT to kb.regular.site-tower (`c9fac6b`), SITE-REVIEW to kb.regular.personal-rig (`74d17e6`), all pushed.
- orca-eval done: Orca replaces Zed's Delta app; partly CodexBar, GitHub Desktop, Codex app; not Zed or Ghostty; telemetry on and agent permission bypass by default; ORCA-ADOPT reviewed and with Kris.
- apply-check done: combined terra apply verified (RIG-APPLY with Kris); `~/.claude/settings.json` and `~/.codex/hooks.json` left out because Orca added hooks live (ORCA-HOOKS, blind review running).
- starship-preview done: `starship-variant --all` (or `-a`, with `--status`/`--duration`) previews every variant in the current directory without switching; kris variants recoloured for Ghostty's dark default and light themes (backup in the kit); contrast findings passed to starship-adopt and terminal-retire.
- terminal-retire (run `chezmoi`, after starship-adopt) makes Ghostty primary and retires iTerm2 and Warp (Decision 205, TERMINALS a) with Warp now).
- starship-adopt done: in source, four unpushed commits, default `kris`, UE-104 accepted; STARSHIP-APPLY with Kris. starship-classic adds `classic` and `--all`.
- terminal-review done: Warp is the one in use (216 launches; signed-in account, telemetry on, cloud conversations, managed `dot_warp/` with per-territory tabs, holds `.toml`); Ghostty 7 launches, unconfigured, no account or telemetry, built-in Nerd Font glyphs; iTerm2 unused since April 2025, unmanaged, stale shell-integration line in `dot_zshrc.tmpl:13`; Terminal.app built in. terminal-blind (Codex, high effort) agreed with Ghostty primary after a week's trial: TERMINALS is with Kris at high (reviewed).
- motion-remove done: Motion (direct download, never in Rig) uninstalled on terra into `~/.Trash/motion-remove-202610220753` with its 696 MB data and prefs (undo recorded), noted in KB-DOTFILES-UE-086 B6c (`f035d70`); no target changed, so no apply (MOTION-APPLY not raised, a high). Sol: check for Motion and remove the same way.
- gitup-remove done: both GitUps (the `gitup` formula and GitUp.app, cask `gitup-app`) uninstalled and zapped on terra, stale `/usr/local/bin/gitup` link removed, retired in chezmoi `0ec53fa`; gate green; live `rig doctor` 6 until applied. Sol: `brew uninstall --cask --zap gitup-app`, `brew uninstall gitup`, `rm /usr/local/bin/gitup` if present, then the same apply. apply-check (after motion-remove) verifies one combined Rig apply (Tower, Orca, GitUp, Motion) against a candidate `rig doctor`.
- starship-trial done (Decision 200): verified Starship v1.27.0 kit at `~/.local/state/ki/trials/starship/`; Kris runs `source ~/.local/state/ki/trials/starship/try.zsh` in one window, leaves with `exec zsh` or by closing it, and removes the kit with `~/.local/state/ki/trials/starship/remove.sh`. STARSHIP-REVIEW waits on his trial. Kris tried it (okay) and wants richer, two-line variants: starship-variants (run `chezmoi`) builds them (Decision 202). starship-variants done: v1.27.0 still latest; variants two-line, dev, pure, rainbow, one-line switchable with `starship-variant <name>`; no Nerd Font installed (Ghostty's built-in font has the glyphs, Warp's does not). starship-kris done: `kris` (default) and `kris-nerd` variants in the kit, 28–38 ms median; host dimmed, `territory › repo/subpath`, git with `wt:`/`detached:` markers, runtimes where used, right prompt exit/duration/time; over SSH a bold yellow `ssh` marker (SSH-MARKER not raised: kept as is unless Kris asks).
- orca-install done (Decision 199): Orca vetted (MIT, signed and notarised, vendor tap `stablyai/orca`, no helper or login item, opt-out PostHog telemetry), declared `[tool.orca]` on the laptop profile (chezmoi `a3b9736`), gate green; terra `rig doctor` 4 before (same four). Not applied or installed: ORCA-INSTALL with Kris, sequenced after tower-finish because both change `~/.config/rig/conf.d/10-applications.toml`.
- nudge-remove done (Decision 198): the old app (`uk.me.kris.tower-save-nudge`) is gone from terra: Trash bundle, `~/.cache/tower-save-nudge/`, its defaults domain and Launch Services registration. Left: possible old TCC grant (tccutil could not resolve it; Kris removes by hand), the retired LaunchAgent's log, the `tower-save-nudge` job names on purpose, and the old "Tower Save Nudge" signing certificate (deleted under OLD-CERT a). Terra `rig doctor` 4: `.toml` handler, firewall exposure, the 19 October handler failure, and new `dock.workstation` drift from Kris pinning Tower Assistant, which he wants; declare it in the Dock with the `/Applications` path change.
- tower-finish done: Tower Assistant 2.0 runs from `~/Applications`, signed, its probes report Accessibility and Screen Recording granted. chezmoi `db7aef1` makes the save-nudge wrapper prefer `/Applications` (fallback `~/Applications`) and declares `tower-assistant` in `dock.workstation` after The Tower at its current path; gate green; candidate `rig doctor` 4 → 3 (Dock drift cleared, nothing new). The `tool.tower-assistant` artefact stays at `~/Applications` (Rig has no fallback form; TOWER-PATH). cert-delete done (OLD-CERT a): the "Tower Save Nudge Local Signing" identity and its trust setting are gone from terra; only Tower Assistant Local Signing remains and `~/Applications/Tower Assistant.app` still verifies.
- VS Code workspaces rebuilt with `ki`, committed and applied on sol (Decision 184); the trust change also feeds the Claude Desktop config and `~/bin/rig-bringup-check`, now applied.
- drift-apply applied all eight drifted targets on sol (Decision 185); `chezmoi status` clean, `rig doctor` 4 before and after (attended only). Claude Desktop keeps 102 undeclared trust grants (88 for paths that no longer exist): Kris chose to revoke all 102 (Decision 186); trust-revoke did so, TRUST-RETURNED closed (Decisions 193, 195); the monthly scan now lists undeclared grants (chezmoi `a3a9dda`).
- Accepted (Decision 194): KB-DOTFILES-UE-098 (`efcd49b`); Still awaiting attended steps on terra and sol: KB-DOTFILES-UE-090, KB-DOTFILES-UE-100.
- All touched repositories are level with their upstreams on sol (checked 01:41 BST, no fetch). On terra, chezmoi `main` is level with origin at `eb5f69a` after a fetch (23:55 BST), so PUSH-TERRA needs nothing.

## Next steps

1. On terra: RIG-APPLY (combined apply, `rig doctor` after); once kb.regular.site-tower's attended move to `/Applications` is done, a short follow-up moves the artefact and Dock path (TOWER-PATH a).
2. On terra: pull chezmoi, then remove Shadowlab Spark with Kris at the machine: `rig doctor` before; scoped diff then apply of `~/.config/rig/conf.d/10-applications.toml` only; open Spark, Stop Spark Daemon, quit; check the cask receipt, then `brew uninstall --cask --zap spark-app`, `defaults delete com.xenonium.Spark`, and Kris removes `~/Library/Group Containers/3DT6DNJE39.com.xenonium.Spark`; verify bundle, cask, login item and helper absent, `rig doctor` after. Never touch readdle-spark or Spark Desktop.
3. Attended steps for KB-DOTFILES-UE-090 and KB-DOTFILES-UE-100 on terra and sol, then their acceptance.
4. TRUST-COMPLETE (Decision 187): record it as a chezmoi Decision Record.
5. Evaluate Orca (Decisions 199, 202 ORCA-INSTALL, 207: first impressions very good; orca-eval maps overlaps): Kris installs it on terra with `brew install --cask stablyai/orca/orca` (declined: telemetry, `~/.claude`/`~/.codex` import), tries it alongside Claude Code and Codex, then decides: adopt (widen beyond the `laptop` profile, record why) or retire (`brew uninstall --cask stablyai/orca/orca && brew untap stablyai/orca`, revert chezmoi `a3b9736`). The live Rig file `~/.config/rig/conf.d/10-applications.toml` is applied with the tower-finish change in one reviewed step.
6. Starship: adopted (Decision 204); starship-adopt implements; Kris reviews the diff and approves install and apply on terra, then sol.

## Held

- Both-Mac Rig apply - until Kris lifts it.
- Privacy and rationale audits - until the owner resumes them.
- WhatsApp refresh (KB-DOTFILES-UE-035) - until Kris takes it up.
