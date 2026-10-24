# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › firewall-apply

**🤖 → 👤 Handoff to supervisor · Run report at 01:03 BST · last mark 23:45 BST · blocked**

---

## Done

- `sudo -n true` needs a password on terra, so I did every step that needs no root and changed nothing on the machine: no firewall change and no backup yet.
- Preflight without root passed. Tailscale.app (`io.tailscale.ipn.macsys`) is connected on `utun2` with `100.96.126.29` and `fd7a:115c:a1e0::ba36:7e1e`, and there is no `tailscaled`. NordVPN NordLynx is disconnected. Both checksums still match the attended-prep values (anchor `8255a1b2…98ce`, plist `a4c60b37…7b43`), and the daemon last exited 0.
- Step 7 probes from sol, all fresh connections: `ssh terra` answered `terra`, T22 and T5900 were ok, LAN5900 was blocked and LAN22 was ok. sol is on the same LAN (`192.168.1.37`). The LAN block shows the old 14 October rules are loaded and working on terra right now.
- `rig show firewall:screen-sharing-tailnet` reports `drifted (anchor-changed,exposed-beyond-tailnet)`. The baseline `rig doctor`, with stdin closed and stderr visible, reports findings=2: this firewall and `dock.workstation`.
- [KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md): corrected the Context wording, since both Macs run Tailscale.app, and added this evidence under Outstanding concerns. Committed as `eeec7a7` in tools-rig, pushed. Gate: the full tools-rig gate (audit, shellcheck, `bash -n`, assemble check, benchmark, native-provider smoke, all 645 bats tests, mandoc, `git diff --check`) and rumdl all passed.
- Dry-tested the paste block below against simulated pf output. The pass path reaches "ALL OK", and an apply that leaves the old rules stops at step 10 and runs R-A.

## In Progress

Waiting for you at terra's console. Paste this one block into a terminal on terra. It asks for your password once, prints each step's output beside what to expect, stops at the first failed check (steps 2–8), and runs R-A itself if anything fails after the apply (steps 9–11). Every locator is written out in full, with no shell variables and no `bootout`.

```sh
sudo -v && (
  ra() {  # R-A: put the old anchor back, then show the 8 old 100.64.0.0/10-to-100.64.0.0/10 rules
    sudo install -o root -g wheel -m 0644 /var/root/rig-firewall-backup/20261025/uk.me.kris.rig.firewall.screen-sharing /etc/pf.anchors/uk.me.kris.rig.firewall.screen-sharing
    sudo pfctl -a com.apple/uk.me.kris.rig.firewall.screen-sharing -f /etc/pf.anchors/uk.me.kris.rig.firewall.screen-sharing
    sudo pfctl -a com.apple/uk.me.kris.rig.firewall.screen-sharing -s rules
  }
  stop() { echo "STOP at step $1: $2"; exit 1; }
  fail_ra() { echo "FAILED at step $1: $2 -- running R-A"; ra; echo "R-A done: expect the 8 old rules above. Stop here."; exit 1; }

  echo "== 2  pf enabled (expect: Status: Enabled)"
  sudo pfctl -s info 2>/dev/null | head -1
  sudo pfctl -s info 2>/dev/null | head -1 | grep -q '^Status: Enabled' || stop 2 "pf is not enabled; applying would switch pf on machine-wide"

  echo "== 3  root rules (expect exactly Apple's two lines)"
  sudo pfctl -sr 2>/dev/null
  [ "$(sudo pfctl -sr 2>/dev/null)" = 'scrub-anchor "com.apple/*" all fragment reassemble
anchor "com.apple/*" all' ] || stop 3 "root ruleset is not Apple's two lines"

  echo "== 4  root anchors (expect com.apple, maybe NordVPN; NordVPN must be empty)"
  sudo pfctl -s Anchors 2>/dev/null
  sudo pfctl -s Anchors 2>/dev/null | grep -v -x -E '[[:space:]]*(com\.apple|NordVPN)' | grep -q . && stop 4 "unexpected root anchor"
  [ -z "$(sudo pfctl -a NordVPN -sr 2>/dev/null)" ] || stop 4 "NordVPN anchor holds rules"

  echo "== 5  com.apple sub-anchors (expect 200.AirDrop, 250.ApplicationFirewall, uk.me.kris.rig.firewall.screen-sharing; first two empty)"
  sudo pfctl -a com.apple -s Anchors 2>/dev/null
  [ "$(sudo pfctl -a com.apple -s Anchors 2>/dev/null | sed 's/^[[:space:]]*//' | sort)" = 'com.apple/200.AirDrop
com.apple/250.ApplicationFirewall
com.apple/uk.me.kris.rig.firewall.screen-sharing' ] || stop 5 "com.apple sub-anchors differ"
  [ -z "$(sudo pfctl -a com.apple/200.AirDrop -sr 2>/dev/null)" ] || stop 5 "AirDrop anchor holds rules"
  [ -z "$(sudo pfctl -a com.apple/250.ApplicationFirewall -sr 2>/dev/null)" ] || stop 5 "ApplicationFirewall anchor holds rules"

  echo "== 6  Rig anchor before (expect 8 old rules: from 100.64.0.0/10 to 100.64.0.0/10)"
  sudo pfctl -a com.apple/uk.me.kris.rig.firewall.screen-sharing -s rules 2>/dev/null
  n=$(sudo pfctl -a com.apple/uk.me.kris.rig.firewall.screen-sharing -s rules 2>/dev/null | grep -c .)
  [ "$n" -eq 8 ] || echo "NOTE step 6: $n rules loaded, not 8 (apply is still safe; tell the agent)"

  echo "== 8  backup (expect 8255a1b2...98ce, then a4c60b37...7b43)"
  sudo mkdir -p /var/root/rig-firewall-backup/20261025
  sudo cp -p /etc/pf.anchors/uk.me.kris.rig.firewall.screen-sharing /var/root/rig-firewall-backup/20261025/
  sudo shasum -a 256 /var/root/rig-firewall-backup/20261025/uk.me.kris.rig.firewall.screen-sharing
  shasum -a 256 /Library/LaunchDaemons/uk.me.kris.rig.firewall.screen-sharing.plist
  sudo shasum -a 256 /var/root/rig-firewall-backup/20261025/uk.me.kris.rig.firewall.screen-sharing | grep -q '^8255a1b2df943de3262cf996f112ec568fed3189468e12ee35714d2b239e98ce ' || stop 8 "backup checksum differs"
  shasum -a 256 /Library/LaunchDaemons/uk.me.kris.rig.firewall.screen-sharing.plist | grep -q '^a4c60b37e40a2084d82f61b21e4ce20f79412046f5aa983802621e0dda267b43 ' || stop 8 "daemon plist checksum differs"

  echo "== 9  apply (expect completed=1 failed=0)"
  rig apply --sudo --target firewall:screen-sharing-tailnet </dev/null || fail_ra 9 "rig apply failed"

  echo "== 10 Rig anchor after (expect 8 rules: 2 'to 100.96.126.29', 2 'to fd7a:115c:a1e0::ba36:7e1e')"
  sudo pfctl -a com.apple/uk.me.kris.rig.firewall.screen-sharing -s rules 2>/dev/null
  r=$(sudo pfctl -a com.apple/uk.me.kris.rig.firewall.screen-sharing -s rules 2>/dev/null)
  [ "$(printf '%s\n' "$r" | grep -c .)" -eq 8 ] || fail_ra 10 "rule count is not 8"
  [ "$(printf '%s\n' "$r" | grep -c 'to 100.96.126.29 ')" -eq 2 ] || fail_ra 10 "IPv4 own-address rules missing"
  [ "$(printf '%s\n' "$r" | grep -c 'to fd7a:115c:a1e0::ba36:7e1e ')" -eq 2 ] || fail_ra 10 "IPv6 own-address rules missing"

  echo "== 11 pf still enabled, root unchanged, Rig anchor still listed"
  sudo pfctl -s info 2>/dev/null | head -1 | grep -q '^Status: Enabled' || fail_ra 11 "pf no longer enabled"
  [ "$(sudo pfctl -sr 2>/dev/null)" = 'scrub-anchor "com.apple/*" all fragment reassemble
anchor "com.apple/*" all' ] || fail_ra 11 "root ruleset changed"
  sudo pfctl -a com.apple -s Anchors 2>/dev/null | grep -q 'com.apple/uk.me.kris.rig.firewall.screen-sharing' || fail_ra 11 "Rig anchor not listed"
  echo "ALL OK through step 11 -- hand back to the agent for steps 12, 13 and 15"
)
```

What you should see: step 2 `Status: Enabled`; step 3 Apple's two lines only; step 4 `com.apple`, perhaps an empty `NordVPN`; step 5 the three `com.apple/…` anchors; step 6 the 8 old `100.64.0.0/10 to 100.64.0.0/10` rules (a `NOTE` there is not a stop); step 8 `8255a1b2…98ce` then `a4c60b37…7b43`; step 9 completed=1 failed=0; step 10 8 rules naming `to 100.96.126.29` and `to fd7a:115c:a1e0::ba36:7e1e`; then `ALL OK through step 11`. A `STOP at step N` line means nothing has changed beyond the backup. A `FAILED … running R-A` line means the old anchor is back; stop and tell me.

**R-A, put the old anchor back by hand** (the block's `ra` does the same):

```sh
sudo install -o root -g wheel -m 0644 /var/root/rig-firewall-backup/20261025/uk.me.kris.rig.firewall.screen-sharing /etc/pf.anchors/uk.me.kris.rig.firewall.screen-sharing
sudo pfctl -a com.apple/uk.me.kris.rig.firewall.screen-sharing -f /etc/pf.anchors/uk.me.kris.rig.firewall.screen-sharing
sudo pfctl -a com.apple/uk.me.kris.rig.firewall.screen-sharing -s rules
```

R-B (emergency removal) and R-C (console) are unchanged from the [attended-prep checklist](/Users/krisbrown/.local/state/ki/agents/chezmoi/attended-prep.report.md). The backup folder keeps the checklist's name, `20261025`, so its R-A and R-B text still apply word for word. Leave NordVPN off until step 15 is done.

After `ALL OK`, an agent runs step 12 (plist checksum and last exit), step 13 (the probes from sol with fresh connections), step 15 (`rig show` should say `present (kernel-rules-unverified)` and `rig doctor` should leave only `dock.workstation`), and records the evidence in KI-TOOL-RIG-CORE-047.

## For sol

- sol: observed 24 October, read-only over SSH: macOS 27.0.1. Tailscale.app (`io.tailscale.ipn.macsys`) is connected with `100.90.130.74` and `fd7a:115c:a1e0::b636:824c`, and there is no `tailscaled`. This matches terra, so the shared rule holds: Rig discovers the tailnet addresses from the interface, not from the daemon.
- sol: observed: sol's anchor file and daemon plist have the same checksums as terra's old ones (`8255a1b2…98ce` and `a4c60b37…7b43`, both dated 19 October). sol therefore carries the same pre-KI-TOOL-RIG-CORE-062 rules, passing any tailnet address to any tailnet address, and needs the same re-apply. The new rules will name sol's own addresses, `100.90.130.74` and `fd7a:115c:a1e0::b636:824c`, so a sol block must check for those in step 10, not terra's.
- sol: observed: `sudo -n` on sol also needs a password, so a background agent there will stop at the same point. Plan on a paste block at sol's console.
- sol: observed: over a non-interactive `ssh sol`, `rig` was not on PATH. Run Rig steps in a login shell at sol's console. Not verified: whether `rig` is installed and at which version.
- sol: observed: 22 and 5900 listen on every address on sol, as they do on terra. sol's LAN address is `192.168.1.37`, so the LAN probe from terra is `nc -z -G 3 192.168.1.37 5900 || echo LAN5900 blocked`.
- sol: sol-specific, from the record and not re-observed tonight: on 19 October sol had pf disabled before its first apply and was undone with `pfctl -d`. Whether pf is enabled now is unverified. If step 2 shows `Disabled`, the terra block stops there. For sol that may be expected rather than a fault, but the anchor-only R-A would then not undo the global enable. Decide that case explicitly; do not just remove the stop.
- sol: sol-specific, from the record: NordVPN's helper keeps a root `NordVPN` anchor on sol that root does not call. Step 4's "anchor present but empty" check is written for this. Not verified tonight: NordVPN's connection state on sol.
- sol: shared: the step 5 check expects exactly three `com.apple` sub-anchors. After the 19 October undo, macOS keeps empty anchor names listed until a restart, which is harmless here. Test contents, not names (lesson recorded in KI-TOOL-RIG-CORE-047).
- sol: shared: on terra, the probes come from sol. On sol, run them from terra with fresh connections (`ssh terra 'ssh sol hostname -s; nc …'`), and keep one held `ssh -t sol` session from terra open through the apply.
- sol: shared: use a separate backup folder under `/var/root/rig-firewall-backup/` on sol, and write the locator literally. Never run `bootout system/` without the full label.

## Queries

### TERRA-SUDO-BLOCK — Root steps for the re-apply

**Context:** terra's sudo needs a password, so the background run stopped before anything changed. Everything without root checks out, and sol shows the old rules are actually blocking LAN 5900 on terra.

**Query:** Will you paste the block above at terra's console now?

**Options:**

a) (recommended, confidence high - every non-root precondition holds and the block stops or restores on its own) Paste it now, then reply "ALL OK" or the first STOP/FAILED line, and an agent finishes steps 12, 13 and 15.

b) Paste only up to step 8 (preflight and backup), and do the apply in a later session.

c) Hold the re-apply. terra's old rules already block LAN 5900; what is missing is the narrower own-address destination match.

### 🤖 → 👤 Handoff to supervisor · since 01:03 BST

👤 1 with you · 🤖 0 running

- [with you] FIREWALL-REAPPLY root paste block, steps 2–6 and 8–11 · Kris · since 01:03 BST

🧵 Coordination thread · chezmoi (ki.chezmoi)
