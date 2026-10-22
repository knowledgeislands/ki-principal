---
id: ki.chezmoi
state: with-worker
since: 2026-10-22T00:59:00Z
received: 2026-10-20T01:30:00Z
beat: null
mark: 2026-10-21T22:56:00Z
method_read: beb56729
---

# ki.chezmoi state

## Now

- starship-trial done (Decision 200): verified Starship v1.27.0 kit at `~/.local/state/ki/trials/starship/`; Kris runs `source ~/.local/state/ki/trials/starship/try.zsh` in one window, leaves with `exec zsh` or by closing it, and removes the kit with `~/.local/state/ki/trials/starship/remove.sh`. STARSHIP-REVIEW waits on his trial. Kris tried it (okay) and wants richer, two-line variants: starship-variants (run `chezmoi`) builds them (Decision 202).
- orca-install done (Decision 199): Orca vetted (MIT, signed and notarised, vendor tap `stablyai/orca`, no helper or login item, opt-out PostHog telemetry), declared `[tool.orca]` on the laptop profile (chezmoi `a3b9736`), gate green; terra `rig doctor` 4 before (same four). Not applied or installed: ORCA-INSTALL with Kris, sequenced after tower-finish because both change `~/.config/rig/conf.d/10-applications.toml`.
- nudge-remove done (Decision 198): the old app (`uk.me.kris.tower-save-nudge`) is gone from terra: Trash bundle, `~/.cache/tower-save-nudge/`, its defaults domain and Launch Services registration. Left: possible old TCC grant (tccutil could not resolve it; Kris removes by hand), the retired LaunchAgent's log, the `tower-save-nudge` job names on purpose, and the old "Tower Save Nudge" signing certificate (deleted under OLD-CERT a). Terra `rig doctor` 4: `.toml` handler, firewall exposure, the 19 October handler failure, and new `dock.workstation` drift from Kris pinning Tower Assistant, which he wants; declare it in the Dock with the `/Applications` path change.
- Kris granted Tower Assistant Accessibility and Screen & System Audio Recording by hand on terra (Decision 201). tower-finish (run `chezmoi`) verifies the grants and install location, moves the Rig artefact, save-nudge wrapper and `dock.workstation` to `/Applications` (TOWER-APP-PATH, apps-tower.midnight.ninja `85ab55a`) and stops at the diff gate. cert-delete done (OLD-CERT a): the "Tower Save Nudge Local Signing" identity and its trust setting are gone from terra; only Tower Assistant Local Signing remains and `~/Applications/Tower Assistant.app` still verifies.
- VS Code workspaces rebuilt with `ki`, committed and applied on sol (Decision 184); the trust change also feeds the Claude Desktop config and `~/bin/rig-bringup-check`, now applied.
- drift-apply applied all eight drifted targets on sol (Decision 185); `chezmoi status` clean, `rig doctor` 4 before and after (attended only). Claude Desktop keeps 102 undeclared trust grants (88 for paths that no longer exist): Kris chose to revoke all 102 (Decision 186); trust-revoke did so, but running Claude Desktop rewrote them back (TRUST-RETURNED, with Kris); the monthly scan now lists undeclared grants (chezmoi `a3a9dda`).
- Rig site rationale filter removed (apps-rig.midnight.ninja `680a95f`, unpushed). roadmap-batch done (chezmoi `4fe2203`, `28e0091`, `7af64b5`: UE-077 and UE-093 accepted, nine terminal records pruned). Tools-shape hooks and CI type check on harness main (`6076a98b`, `3f203c63`, unpushed) after hooks-recover restored the harness metadata. trust-declare done: 82 declared folders (+23: six checkouts incl. HNR, eight territory roots, eight Desktop Projects, `~/.claude`), independent of VS Code workspaces (tools-ki `9252669a`, chezmoi `13458343`); trust-reconcile done (Decision 193): `~/.claude/settings.json` +15 applied; Desktop list reset 149 → exactly 76 declared (94 removed, 21 added), rollback copy beside the config; doctor 4 → 4 identical. After Kris reopened Desktop, trust-check found the 76-folder list held unchanged over 200 seconds (no rewrite); rollback retained. Tools hooks adopted in all five tools repositories: tools-ki `a2e3460d`, tools-techne `3e686b66`, tools-git-almanac `8851d4dc`, and via hooks-bats tools-mgit `78a1b376` and tools-rig `f92d9a1c` (Bats kept in manual gates and CI; Rig's indexed assembly check declared and proved), all unpushed. Overnight-survey stopped (Decision 190 withdrawn); Shadowlab Spark fully removed from sol (Decisions 191, 192; spark-tidy verified; coordinator accepted the inert launchd override entry, SPARK-LAUNCHCTL a); terra after a push (declaration retired, `955faf5`); resources-check reported (Decision 189); Rig comment and kind routed to ki.mac-studio-setup. KI-TOOL-KI-CLI-165 was already accepted and pruned (tools-ki `fde00e97`, `39f1a91d`); accept-ue098 blocked before any change: the new MATURITY-1 audit warning (chezmoi `.ki.toml` declares no maturity) fails UE-098's verify criterion; maturity-accept done: chezmoi declares `maturity = "settled"` (`39f4f85`, Decision 195) and KB-DOTFILES-UE-098 is accepted (`efcd49b`).
- Hook rollout: stages 1 and 3 delivered; stage 2 reached every repository, the tools shape included. KI-TOOL-KI-CLI-165 passed re-review and is Awaiting review; run `ki repo conform` only with `--dry-run` until Kris accepts it.
- Accepted (Decision 194): KB-DOTFILES-UE-098 (`efcd49b`); KI-TOOL-KI-CLI-165 was already accepted and pruned. Still awaiting attended steps on terra and sol: KB-DOTFILES-UE-090, KB-DOTFILES-UE-100.
- All touched repositories are level with their upstreams on sol (checked 01:41 BST, no fetch). On terra, chezmoi `main` is level with origin at `eb5f69a` after a fetch (23:55 BST), so PUSH-TERRA needs nothing.

## Next steps

1. On terra: receive tower-finish and cert-delete; Kris reviews the scoped diff and approves the apply; `rig doctor` after.
2. On terra: pull chezmoi, then remove Shadowlab Spark with Kris at the machine: `rig doctor` before; scoped diff then apply of `~/.config/rig/conf.d/10-applications.toml` only; open Spark, Stop Spark Daemon, quit; check the cask receipt, then `brew uninstall --cask --zap spark-app`, `defaults delete com.xenonium.Spark`, and Kris removes `~/Library/Group Containers/3DT6DNJE39.com.xenonium.Spark`; verify bundle, cask, login item and helper absent, `rig doctor` after. Never touch readdle-spark or Spark Desktop.
3. Attended steps for KB-DOTFILES-UE-090 and KB-DOTFILES-UE-100 on terra and sol, then their acceptance.
4. homeless: TRUST-COMPLETE (Decision 187).
5. Evaluate Orca (Decisions 199, 202 ORCA-INSTALL): Kris installs it on terra with `brew install --cask stablyai/orca/orca` (declined: telemetry, `~/.claude`/`~/.codex` import), tries it alongside Claude Code and Codex, then decides: adopt (widen beyond the `laptop` profile, record why) or retire (`brew uninstall --cask stablyai/orca/orca && brew untap stablyai/orca`, revert chezmoi `a3b9736`). The live Rig file `~/.config/rig/conf.d/10-applications.toml` is applied with the tower-finish change in one reviewed step.
6. Starship prompt (KB-DOTFILES-UE-104, Decisions 200, 202): starship-variants builds switchable variants in the trial kit; then design a bespoke `kris` default fitted to his work, which Kris asked for (02:22 BST) and which was not yet sent to the run: two lines; line 1 host only where it matters (terra, sol, SSH), territory › repository under `~/workspaces/<territory>/<repo>` (territory dimmed, repo bold), git branch, status, ahead/behind, a linked-worktree or detached-HEAD marker, runtimes only where used; right side duration ≥2 s, exit code on failure, time; line 2 the input character; under 50 ms; no chezmoi drift count. Kris tries them in one window, then STARSHIP-REVIEW and, if adopted, one adoption record on hold until KB-DOTFILES-UE-102.

## Held

- Sol's `rig doctor` findings (handler, firewall anchor range, UTM source) - until Kris is at the machine.
- Both-Mac Rig apply - until Kris lifts it.
- The attended NordVPN trial - until a tested restore path exists (KI-TOOL-RIG-CORE-068).
- Privacy and rationale audits - until the owner resumes them.
- WhatsApp refresh and vega rendering - until Kris takes them up.
