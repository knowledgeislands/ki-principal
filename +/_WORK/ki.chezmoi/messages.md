# ki.chezmoi messages

None.

- sol: pick up Orca there, not on terra: ORCA-ADOPT and ORCA-PER-PANE in KB-DOTFILES-UE-107 (Kris, 24 October).
- sol: FIREWALL-REAPPLY on sol (KI-TOOL-RIG-CORE-047), learnings from terra 24 October; terra's paste block is `~/.local/state/ki/agents/chezmoi/firewall-apply.sh` on terra, adapt step 10 to sol's addresses:
  - sol: observed 24 October, read-only over SSH: macOS 27.0.1. Tailscale.app (`io.tailscale.ipn.macsys`) is connected with `100.90.130.74` and `fd7a:115c:a1e0::b636:824c`, and there is no `tailscaled`. This matches terra, so the shared rule holds: Rig discovers the tailnet addresses from the interface, not from the daemon.
  - sol: observed: sol's anchor file and daemon plist have the same checksums as terra's old ones (`8255a1b2…98ce` and `a4c60b37…7b43`, both dated 19 October). sol therefore carries the same pre-KI-TOOL-RIG-CORE-062 rules, passing any tailnet address to any tailnet address, and needs the same re-apply. The new rules will name sol's own addresses, `100.90.130.74` and `fd7a:115c:a1e0::b636:824c`, so a sol block must check for those in step 10, not terra's.
  - sol: observed: `sudo -n` on sol also needs a password, so a background agent there will stop at the same point. Plan on a paste block at sol's console.
  - sol: observed: over a non-interactive `ssh sol`, `rig` was not on PATH. Run Rig steps in a login shell at sol's console. Not verified: whether `rig` is installed and at which version.
  - sol: observed: 22 and 5900 listen on every address on sol, as they do on terra. sol's LAN address is `192.168.1.37`, so the LAN probe from terra is `nc -z -G 3 192.168.1.37 5900 || echo LAN5900 blocked`.
  - sol: sol-specific, from the record and not re-observed tonight: on 19 October sol had pf disabled before its first apply and was undone with `pfctl -d`. Whether pf is enabled now is unverified. If step 2 shows `Disabled`, the terra block stops there. For sol that may be expected rather than a fault, but the anchor-only R-A would then not undo the global enable. Decide that case explicitly; do not just remove the stop.
  - sol: sol-specific, from the record: NordVPN's helper keeps a root `NordVPN` anchor on sol that root does not call. Step 4's "anchor present but empty" check is written for this. Not verified tonight: NordVPN's connection state on sol.
  - sol: shared: the step 5 check expects exactly three `com.apple` sub-anchors. After the 19 October undo, macOS keeps empty anchor names listed until a restart, which is harmless here. Test contents, not names (lesson recorded in KI-TOOL-RIG-CORE-047).
  - sol: shared: on terra, the probes come from sol. On sol, run them from terra with fresh connections (`ssh terra 'ssh sol hostname -s; nc …'`), (no held SSH session needed when Kris is at both consoles, Kris 24 October).
  - sol: shared: use a separate backup folder under `/var/root/rig-firewall-backup/` on sol, and write the locator literally. Never run `bootout system/` without the full label.
