# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › attended-prep

**🤖 → 👤 Handoff to supervisor · Run report at 00:40 BST · last mark 23:45 BST**

---

## Done

- Read [KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md), the [firewall-blind review](/Users/krisbrown/.local/state/ki/agents/chezmoi/firewall-blind.report.md), the [terra-removals-blind review](/Users/krisbrown/.local/state/ki/agents/chezmoi/terra-removals-blind.report.md), [KB-DOTFILES-UE-086](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-086-finish-software-alignment.md), the `[firewall.screen-sharing-tailnet]` declaration in [55-ports](/Users/krisbrown/.local/share/chezmoi/dot_config/rig/conf.d/private_55-ports.toml:50) and Rig's [apply path](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/src/rig/29-firewall.bash:546).
- Read-only firewall preflight on terra (macOS 27.0.1, Rig 0.8.0 at tools-rig `6ecdd04`): Tailscale is up at `100.96.126.29` / `fd7a:115c:a1e0::ba36:7e1e`. LAN address is `192.168.1.22`. NordVPN NordLynx shows disconnected, but the NordVPN app and its helper are running. `*.5900` and `*.22` listen on every address. `/etc/pf.conf` and `com.apple` are unchanged.
- Changed assumption: terra now runs Tailscale through Tailscale.app (the `io.tailscale.ipn.macsys` VPN service), not the Homebrew `tailscaled` daemon the record names. There is no `tailscaled` process. The rules match addresses, not interfaces, so the firewall is unaffected, and `sol` already uses the same kind of setup.
- `rig doctor` (finished with stdin closed): unhealthy, fail=2. One finding is `firewall.screen-sharing-tailnet: drifted (anchor-changed)`, with no `exposed-beyond-tailnet` this time. The other is `dock.workstation: drifted (dock-item-path-missing:tower-assistant)`, which belongs to TOWER-INSTALL and not to this work.
- `rig show firewall:screen-sharing-tailnet` shows `drifted (anchor-changed)`. The installed anchor still has the 14 October rule that passes any tailnet address to any tailnet address. The new rules allow only terra's own two tailnet addresses as the destination.
- `rig apply --dry-run --target firewall:screen-sharing-tailnet`: planned=1, and it selects only this target with no dependencies. The apply code ([29-firewall.bash:575](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/src/rig/29-firewall.bash:575)) shows that, because the daemon file is current, the real apply replaces the anchor file only. It then runs `pfctl -E -a … -f` and rereads the loaded rules. There is no bootout or bootstrap.
- Reachability as seen from terra: 22 and 5900 answer on `127.0.0.1`, `100.96.126.29` and `192.168.1.22`. A probe to its own address goes over loopback, which pf always passes, so this proves the listeners are up and nothing about LAN refusal. The LAN test has to come from another device.
- Checksums for the restore: the anchor file is `8255a1b2df943de3262cf996f112ec568fed3189468e12ee35714d2b239e98ce` and the daemon property list is `a4c60b37e40a2084d82f61b21e4ce20f79412046f5aa983802621e0dda267b43`. The daemon is loaded, with 1 run and last exit 0.
- Removal inventory:
  - Clockology, Nitro and Mercury are already gone: no app bundle anywhere, and not in `mas list`.
  - Still installed: Prime Video (App Store 545519333), BlueStacks with BlueStacks Air multi-instance manager, and Adobe Creative Cloud.
  - None of them has a Homebrew cask.
- Nothing was changed. There were no commits, no sudo, no firewall change and no removal. The temporary directory holds only the doctor and dry-run captures.

## In Progress

Nothing is running. Here is the checklist for you at the screen. Type every locator out in full, use no shell variables, and paste one block at a time.

### Part 1 — Firewall re-apply (KI-TOOL-RIG-CORE-047)

**Preflight. Stop at the first failure.**

1. **Kris (GUI)** — In the NordVPN menu, confirm it is disconnected, and leave it off until step 16.
2. **Kris (sudo)** — `sudo pfctl -s info | head -1`. You should see `Status: Enabled`. **If it says Disabled, stop.** Applying would switch pf on for the whole machine, and the anchor-only restore cannot undo that.
3. **Kris (sudo)** — `sudo pfctl -sr`. You should see only `scrub-anchor "com.apple/*" all fragment reassemble` and `anchor "com.apple/*" all`. **If there is any other rule (for example NordVPN's), stop.**
4. **Kris (sudo)** — `sudo pfctl -s Anchors`. You should see `com.apple`, and possibly `NordVPN`. If `NordVPN` is listed, `sudo pfctl -a NordVPN -sr` must print nothing; otherwise stop. This test checks contents, not names.
5. **Kris (sudo)** — `sudo pfctl -a com.apple -s Anchors`. You should see `com.apple/200.AirDrop`, `com.apple/250.ApplicationFirewall` and `com.apple/uk.me.kris.rig.firewall.screen-sharing`. Then run `sudo pfctl -a com.apple/200.AirDrop -sr` and `sudo pfctl -a com.apple/250.ApplicationFirewall -sr`. Both should print nothing.
6. **Kris (sudo)** — `sudo pfctl -a com.apple/uk.me.kris.rig.firewall.screen-sharing -s rules`. You should see the 8 old rules, which read `from 100.64.0.0/10 to 100.64.0.0/10`. If it shows 0 rules, the kernel restriction was not loaded. The apply is still safe, but note it.
7. **Kris (GUI)** — Set up the second session. On terra, open Terminal B and run `ssh -t sol`. On `sol`, run `ssh -t terra` and **leave that session open**. In a third terra tab, run `ssh sol 'ssh terra hostname -s; nc -z -G 3 100.96.126.29 22 && echo T22 ok; nc -z -G 3 100.96.126.29 5900 && echo T5900 ok'`. You should see `terra`, `T22 ok` and `T5900 ok`. If `ssh sol 'ipconfig getifaddr en0'` prints a `192.168.1.x` address, also run `ssh sol 'nc -z -G 3 192.168.1.22 5900 || echo LAN5900 blocked; nc -z -G 3 192.168.1.22 22 && echo LAN22 ok'`. You should see `LAN5900 blocked` and `LAN22 ok`.
8. **Kris (sudo)** — Back up the anchor file:

   ```sh
   sudo mkdir -p /var/root/rig-firewall-backup/20261025
   sudo cp -p /etc/pf.anchors/uk.me.kris.rig.firewall.screen-sharing /var/root/rig-firewall-backup/20261025/
   sudo shasum -a 256 /var/root/rig-firewall-backup/20261025/uk.me.kris.rig.firewall.screen-sharing
   shasum -a 256 /Library/LaunchDaemons/uk.me.kris.rig.firewall.screen-sharing.plist
   ```

   The first checksum must be `8255a1b2…98ce`. The second must be `a4c60b37…7b43`, which means the daemon is current and apply will not touch it.

**Restore path. Read it before applying.**

- **R-A: put the old anchor back.** Use this if the apply fails or the new rules misbehave while SSH still works.

  ```sh
  sudo install -o root -g wheel -m 0644 /var/root/rig-firewall-backup/20261025/uk.me.kris.rig.firewall.screen-sharing /etc/pf.anchors/uk.me.kris.rig.firewall.screen-sharing
  sudo pfctl -a com.apple/uk.me.kris.rig.firewall.screen-sharing -f /etc/pf.anchors/uk.me.kris.rig.firewall.screen-sharing
  sudo pfctl -a com.apple/uk.me.kris.rig.firewall.screen-sharing -s rules
  ```

  You should see the 8 old `100.64.0.0/10 to 100.64.0.0/10` rules again, and `rig show firewall:screen-sharing-tailnet` should be back to `drifted (anchor-changed)`. The reload command is the one proven on terra on 19 October (A1: rc 0, reference count unchanged). The byte restore with `install` has not been rehearsed on its own.
- **R-B: emergency removal.** Use this if Screen Sharing over the tailnet breaks, or anything looks wrong.

  ```sh
  sudo launchctl bootout system/uk.me.kris.rig.firewall.screen-sharing
  sudo pfctl -a com.apple/uk.me.kris.rig.firewall.screen-sharing -F rules
  ```

  Then make a fresh SSH connection from sol. This sequence was proven on terra on 19 October (A2), and SSH kept working. To bring the restriction back, run R-A's `install` line if needed, then `sudo launchctl bootstrap system /Library/LaunchDaemons/uk.me.kris.rig.firewall.screen-sharing.plist`, which was also proven in A2. **Never run `bootout system/` without the full name: on 19 October that shut terra down.**
- **R-C: console route, if SSH and Screen Sharing both drop.** pf does not affect logging in at terra's own keyboard. In a local Terminal, run R-B. If SSH still fails, the anchor is not the cause, because it only matches port 5900. Check `tailscale status`, reconnect from the Tailscale.app menu, and confirm NordVPN is disconnected.
  - Last resort: `sudo pfctl -d` switches pf off entirely. Steps 3 and 5 show that nothing else on terra uses pf.
  - Run R-A's `install` line before any restart. The daemon reloads the anchor file at boot, which also switches pf back on.
- **Assumptions behind the restore path:**
  - You are at terra's console with a local admin login.
  - pf was already enabled (step 2), so `-E` only adds a reference.
  - The root ruleset is Apple's and NordVPN is off (steps 1, 3 and 4).
  - The anchor matches only TCP and UDP 5900, so SSH and Tailscale are not matched.
  - The daemon file is current (step 8), so apply does not boot it out.
  - The backup in `/var/root` survives a restart.
  - Existing pf connections survive a reload or flush, so every check below uses a fresh connection.

**Apply.**

9. **Kris (sudo)** — `rig apply --sudo --target firewall:screen-sharing-tailnet`. Leave stderr visible and do not filter the output. You should see completed=1 failed=0. A `loaded rules do not match` failure means: run R-A, then stop.

**Verify.**

10. **Kris (sudo)** — `sudo pfctl -a com.apple/uk.me.kris.rig.firewall.screen-sharing -s rules`. You should see 8 rules naming `to 100.96.126.29` and `to fd7a:115c:a1e0::ba36:7e1e`.
11. **Kris (sudo)** — `sudo pfctl -s info | head -1` should still show Enabled. `sudo pfctl -sr` should still show Apple's two lines. `sudo pfctl -a com.apple -s Anchors` should still list the Rig anchor.
12. **Kris** — `shasum -a 256 /Library/LaunchDaemons/uk.me.kris.rig.firewall.screen-sharing.plist` should still be `a4c60b37…7b43`. `launchctl print system/uk.me.kris.rig.firewall.screen-sharing | grep "last exit"` should show 0.
13. **Kris** — Re-run the step 7 probes from sol, with new connections. You should see `terra`, `T22 ok` and `T5900 ok`, and, if sol is on the same LAN, `LAN5900 blocked` and `LAN22 ok`. The SSH session you left open must still be alive.
14. **Kris (GUI)** — Optional, if you can reach sol's screen: use Finder › Connect to Server › `vnc://100.96.126.29`.
15. **Kris** — `rig show firewall:screen-sharing-tailnet` should show `present (kernel-rules-unverified)`. Then run `rig doctor` with stderr visible; it takes about 5 minutes. The only finding left should be `dock.workstation`.
16. **Kris (GUI)** — NordVPN may be used again. Turning it on bypasses the anchor, which is KI-TOOL-RIG-CORE-068 and not part of this work.
17. **Agent after** — Record the evidence in KI-TOOL-RIG-CORE-047's outstanding concerns, close FIREWALL-REAPPLY in the ki.chezmoi queries, and leave the backup in place until you say otherwise.

### Part 2 — terra removals (KB-DOTFILES-UE-086)

None of these needs a Rig declaration change. Prime Video and BlueStacks are not in the catalogue, so they simply drop off `rig status --unmanaged`. Creative Cloud already has an inert `[retired-application.adobe-creative-cloud]` entry ([10-applications:1237](/Users/krisbrown/.local/share/chezmoi/dot_config/rig/conf.d/private_10-applications.toml:1237)), which stays as it is.

18. **Agent after** — Clockology, Nitro and Mercury are already removed. Tick the Clockology and Nitro parts of B6a and tick B7, after a fresh `mas list` and path check. Nothing is needed from you.
19. **Prime Video (App Store 545519333; its container `~/Library/Containers/com.amazon.aiv.AIVApp` is 17 GB, mostly downloaded media):**
    - **Kris (GUI)** — Open Prime Video, go to Downloads and delete each title, or decide to keep them. Deleting removes the offline media and frees one of Amazon's download-device slots. Copied DRM files will not play anywhere else. Then quit the app.
    - **Kris (sudo)** — `sudo mas uninstall 545519333`. This removes only the app; the container stays.
    - **Kris (GUI), optional** — Move the container above to the Bin. This deletes its settings and any downloads still in it.
20. **BlueStacks and BlueStacks Air multi-instance manager (shared data in `/Users/Shared/Library/Application Support/BlueStacks` is 3.3 GB; the `Tiramisu64` instance was last changed on 15 September):**
    - **Kris** — Decide whether to back up or discard. To back up: `ditto "/Users/Shared/Library/Application Support/BlueStacks" ~/Desktop/BlueStacks-backup-20261025`.
    - **Kris (GUI)** — Open BlueStacks and choose BlueStacks › Uninstall from the menu bar; it asks for an administrator password. This deletes both apps, all instance data, the `com.now.gg.BlueStacks.cleanup` daemon and its helper, and, because BlueAI is not installed, the shared now.gg sign-in. **Do not drag either app to the Bin first:** the cleanup daemon watches both apps and deletes the data anyway.
21. **Adobe Creative Cloud (no Creative Cloud app is installed; Core Sync and CCLibrary Finder extensions, CCXProcess and the installer daemon are present; Adobe's support data is 49 MB; there is no `~/Creative Cloud Files` folder):**
    - **Kris (GUI)** — Open Creative Cloud and check three things: Apps shows nothing installed, Files and Libraries show nothing pending or stored only locally, and which account is signed in. If any of that is unclear, stop.
    - **Kris (GUI), optional** — Sign out, which releases the activation.
    - **Kris (GUI)** — Run `/Applications/Utilities/Adobe Creative Cloud/Utils/Creative Cloud Uninstaller.app` and enter the admin password. This deletes Creative Cloud, Core Sync, CCXProcess, CCLibrary, the Finder extensions and Adobe's launch agents. Do not use a broad Adobe cleaner.
22. **Agent after** — Verify:
    - `/Applications` and `mas list` no longer show any removed app.
    - `launchctl list` and the LaunchAgents and LaunchDaemons folders have no `adobe` or `now.gg` entries.
    - No such processes are running.
    - `rig status --retired` finds no Creative Cloud on terra.
    - `rig status --unmanaged` no longer lists Prime Video or BlueStacks.
    - `rig doctor` and `node --test tests/rig-catalogue.test.mjs` pass.

    Then tick only the completed B6a, B6b and B7 steps and the terra half of C7i in KB-DOTFILES-UE-086, which stays open until `sol` is done, and commit after the full local gate.

## Queries

### TERRA-REMOVALS-DATA — Local data before removal

**Context:** Prime Video holds about 17 GB of downloads, and BlueStacks holds a 3.3 GB instance that its own uninstaller deletes. Both decisions have to be made before steps 19 and 20, and the blind review recommended holding both until you choose.

**Query:** Discard both, or keep a copy of either first?

**Options:**

a) (recommended, confidence medium - you chose to remove both apps, and DRM downloads cannot be reused) Delete the Prime Video downloads in the app, and discard the BlueStacks instance without a backup, unless you know it holds something you still want.

b) Back up the BlueStacks data with step 20's `ditto` first, and delete the Prime Video downloads.

c) Hold Prime Video and BlueStacks for now, and remove only Creative Cloud tonight.

### 🤖 → 👤 Handoff to supervisor · since 00:40 BST

👤 2 with you · 🤖 0 running

- [with you] FIREWALL-REAPPLY at-screen steps 1–16 · Kris · since 00:40 BST
- [with you] TERRA-REMOVALS steps 19–21 and TERRA-REMOVALS-DATA · Kris · since 00:40 BST

🧵 Coordination thread · chezmoi (ki.chezmoi)
