# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › spark-retire

**🤖 → 👤 Handoff to supervisor · blocked · Run report at 23:52 BST · last mark 05:09 BST**

---

## Done

- Local commit `955faf51ed9084c671ab740694b2fceebfda2769`, `chore(rig): retire Shadowlab Spark launcher`: removed only `[tool.spark]` and updated the existing retirement expectation; explicit paths, runtime-model co-author `gpt-6.1-sol`, committed paths verified.
- `ki repo audit --repo .`: passed before commit, with existing warnings; another run's temporary roadmap-shape failure cleared before committing.
- `node --test tests/*.test.mjs`: passed, 290 passing and 2 skipped; the initial selection-expectation failure was corrected.
- `rumdl check .`: passed before commit.
- Post-apply `node --test tests/rig-catalogue.test.mjs`: passed, 15 passing and 2 skipped.
- Targeted `chezmoi diff --exclude scripts ~/.config/rig/conf.d/10-applications.toml`: reviewed; only the launcher declaration removed. Explicitly authorised targeted apply completed on sol, scripts excluded; source and target are byte-identical and the subsequent targeted diff is empty.
- Baseline identity: `/Applications/Spark.app`, bundle `com.xenonium.Spark`, version 3.3.2, Homebrew cask `spark-app`; no App Store receipt or matching `mas list` entry. Baseline Rig status was `spark: present`.
- Baseline login helper: enabled and running, `3DT6DNJE39.com.xenonium.Spark.agent`, embedded in `Spark.app/Contents/Library/LoginItems/Spark Daemon.app`; no matching standalone user/system LaunchAgent or LaunchDaemon plist found.
- Native ServiceManagement unregister returned false; helper process 62120 remained registered and running. Stopped before quitting, provider uninstall or deleting data; removal is **not complete**.
- After apply, Rig's selected status contains no launcher row; `rig status --unmanaged` still reports `cask:spark-app` and `/Applications/Spark.app`, correctly exposing the pending uninstall. It exits 1 because existing setup problems remain.
- Spark Desktop stays declared and installed as `com.readdle.SparkDesktop`, Homebrew `readdle-spark`; its declaration is unchanged and Rig reports it present. Its bundle and data were not modified.
- No push, fetch, remote call, `op` command, whole-machine `rig apply`, scheduler/credential change or work-record change was performed by this run. Terra was not contacted.
- Final housekeeping: checkout clean at inspection; no Git lock files; task-only temporary outputs cleared before marking the run DONE.

`rig doctor` before: **4 findings**, exit 1, unhealthy; after the declaration apply: **the same 4 findings**, exit 1, unhealthy. Passing observations changed from 242 to 241 because the launcher left selection. Each finding was read and deliberately left for its existing attended work:

- UTM: MAS source mismatch, `source-mismatch:unclassified`; needs attended source review and possibly App Management rights.
- TOML default application: Warp is current, Zed expected; handler reconciliation is outside Spark retirement.
- Screen-sharing firewall: `anchor-changed,exposed-beyond-tailnet`; connection-critical and outside this run's authority, with no tested restore path here.
- Historical failed apply: `default-application:toml`, provider `macos-handlers`, exit 1 at `2026-10-20T03:41:50Z`; retained history, not a new Spark failure.

## In Progress

Nothing is running. Sol's native retirement is blocked by its registered login helper; the source change is committed and rendered, but the app and all three identified data locations remain:

- `~/Library/Application Support/Spark` — explicitly named by the installed Homebrew receipt's zap stanza.
- `~/Library/Preferences/com.xenonium.Spark.plist` — exact launcher bundle identity.
- `~/Library/Group Containers/3DT6DNJE39.com.xenonium.Spark` — exact launcher group identity; this session cannot read inside it (`Operation not permitted`), so its removal may need an attended privacy prompt.

No preference or support file was removed. No Shadowlab cache was found in the inspected standard cache locations. Generic Sparkle updater files and all Readdle/Spark Desktop files were left alone.

Outstanding - no action requested now: after the attended helper stop, the next worker should confirm it is unregistered and no longer running, then use the reviewed native removal and explicit bundle-owned cleanup below. If sudo or a privacy screen is required, stop and return the exact failing command to Kris. Do not claim proper removal until the bundle, cask, active login registration and launch service are absent, data cleanup is accounted for, Rig selection/status is clear, and doctor has no additional findings.

```sh
env HOMEBREW_NO_AUTO_UPDATE=1 HOMEBREW_NO_ANALYTICS=1 brew uninstall --cask --zap spark-app
defaults delete com.xenonium.Spark
rm -rf "$HOME/Library/Group Containers/3DT6DNJE39.com.xenonium.Spark"
rig status --unmanaged
rig doctor
node --test tests/rig-catalogue.test.mjs
```

The installed sol receipt's native removal scope is exactly `Spark.app` plus `~/Library/Application Support/Spark`; it contains no Spark Desktop path. Check the receipt again on terra before using zap there. The protected group cleanup above is an attended handoff, not a claim that permissions were granted or removal succeeded.

Outstanding - no action requested now: **terra handoff, after a separately authorised push containing `955faf51ed9084c671ab740694b2fceebfda2769`**. On terra, inspect checkout status first and reconcile any local work before pulling. Record every local doctor finding; review the targeted diff before its apply. Then open Shadowlab Spark, choose **Stop Spark Daemon**, and quit Spark before running the native uninstall/cleanup above. If macOS needs sudo or the screen, stop for Kris. Never select or remove `readdle-spark`, `Spark Desktop.app` or any Readdle data.

```sh
cd "$HOME/.local/share/chezmoi"
git status --short
git pull --ff-only
git merge-base --is-ancestor 955faf51ed9084c671ab740694b2fceebfda2769 HEAD
rig doctor
rig status --unmanaged
chezmoi diff --exclude scripts "$HOME/.config/rig/conf.d/10-applications.toml"
chezmoi apply --exclude scripts "$HOME/.config/rig/conf.d/10-applications.toml"
open /Applications/Spark.app
```

Terra verification: check `/Applications/Spark.app` and `~/Applications/Spark.app` are absent, `brew list --cask --versions spark-app` finds no cask, `launchctl list` has no exact helper label, and `sfltool dumpbtm` has no active Shadowlab login item. Inspect user/system launch-agent and daemon plists for the exact launcher IDs/path. `rig status --unmanaged` must no longer show either launcher identity; retain Spark Desktop's present state. Compare every doctor finding before/after, not just its count.

Outstanding - no action requested now: local-only handoff is **chezmoi on sol, branch main**, containing this run's commit; no publication was attempted. Concurrent roadmap commits `4fe2203` (reconcile approved batch) `28e0091` (pin links before pruning) and `7af64b5` (prune nine terminal records) were observed and left untouched. Trust-revoke's already-existing `a3a9dda` was the starting HEAD. Reconcile this checkout before working from another machine.

Other-run dirty paths observed during the run and left untouched are named below. Their owner committed them; the final checkout inspection was clean.

- `docs/guides/tools/headroom.md`
- `docs/guides/user/setup-mac-rig.md`
- `docs/roadmap/KB-DOTFILES-UE-027-honest-rationales-per-tool.md`
- `docs/roadmap/KB-DOTFILES-UE-071-audit-macos-privacy-permissions.md`
- `docs/roadmap/KB-DOTFILES-UE-077-reorganise-1password-vaults-safely.md`
- `docs/roadmap/KB-DOTFILES-UE-082-tolerate-missing-template-tools.md`
- `docs/roadmap/KB-DOTFILES-UE-084-render-zshenv-on-vega.md`
- `docs/roadmap/KB-DOTFILES-UE-087-manage-headroom-profile-arguments.md`
- `docs/roadmap/KB-DOTFILES-UE-088-ssh-alias-for-sol.md`
- `docs/roadmap/KB-DOTFILES-UE-089-ki-tool-release-channels.md`
- `docs/roadmap/KB-DOTFILES-UE-090-close-rig-bring-up-gaps.md`
- `docs/roadmap/KB-DOTFILES-UE-091-shared-dock-tool-links.md`
- `docs/roadmap/KB-DOTFILES-UE-092-restore-local-skill-projection.md`
- `docs/roadmap/KB-DOTFILES-UE-093-restore-emerge-test-prerequisites.md`
- `docs/roadmap/KB-DOTFILES-UE-094-audit-sol-privacy-permissions.md`
- `docs/roadmap/KB-DOTFILES-UE-095-guide-continuity-check.md`
- `docs/roadmap/KB-DOTFILES-UE-097-configure-gmail-routing-paths.md`
- `docs/roadmap/KB-DOTFILES-UE-101-declare-headroom-user-deployment.md`
- `docs/roadmap/KB-DOTFILES-UE-103-report-absent-mcp-commands.md`

## Queries

### SPARK-ATTENDED - Stop the launcher's login helper on sol

**Context:** macOS refused the native unregister call; the helper is still enabled and running. Deleting the bundle now would not satisfy the requested login-item removal. The installed Spark bundle exposes its own **Stop Spark Daemon** action. No uninstall or data deletion has happened.

**Query:** Open Shadowlab Spark on sol, choose **Stop Spark Daemon**, quit Spark, then return this run to finish native uninstall and verification?

**Options:**

a) (recommended, confidence high - the launcher identity, enabled helper and installed stop action were directly verified) Run `open /Applications/Spark.app`, choose **Stop Spark Daemon**, then quit Spark; return the run to verify the helper stopped and finish the already-authorised removal. Handle any protected-container prompt interactively when reached.

b) Leave the retirement incomplete for now; retain the app and its data while its Rig declaration remains retired.

### 🤖 → 👤 Handoff to supervisor · blocked · since 23:52 BST

👤 1 with you · ⛔ 1 blocked

- [with you] SPARK-ATTENDED: stop Spark's login helper · owner · since 23:52 BST
- [blocked] native uninstall and final removal verification · run/spark-retire · since 23:52 BST
- [unpushed] chezmoi on sol, main: this run's local commit `955faf51ed9084c671ab740694b2fceebfda2769`; no push attempted
