# chezmoi › drift-resolve

**🤖 → 👤 Handoff to supervisor · Run report at 01:23 BST**

---

## Done

- `rig` resolves to tools-rig `87fa261`; starting `rig doctor` found 3 findings, matching the brief, and `chezmoi status` listed only the two Tower Assistant files.
- `.toml` now opens in Zed (`dev.zed.Zed`). The prompted apply was recorded as failed (exit 1), as expected. Kris accepted the prompt, and a second unprompted apply completed (`reconciled:extension:toml`), which cleared the 19 October failed-apply record. `.sh` and `.zsh` still open in Zed. To undo, re-assign `.toml` to VS Code (`com.microsoft.VSCode`) in Finder's Get Info › Open with › Change All.
- Final `rig doctor`: findings 3 → 1 (exit 1). The one left is `firewall.screen-sharing-tailnet`, which I left alone as briefed. Final `chezmoi status`: the same two held Tower Assistant entries. No source change, no commit.

## In Progress

- **Tower Assistant: held.** `/Applications/Tower Assistant.app` does not exist. The app is still at `~/Applications/Tower Assistant.app`, version 2.0, so I did not run the scoped `chezmoi apply` of `10-applications.toml` and `40-macos.toml` or the `dock:workstation` apply. Both files stay pending until 2.1 is installed in /Applications.
- **Firewall `firewall.screen-sharing-tailnet`: unchanged, read-only findings below.** Owner: ki.mac-studio-setup.
  - **anchor-changed:** `/etc/pf.anchors/uk.me.kris.rig.firewall.screen-sharing` was written on 14 October by an older Rig. Its rules pass tailnet _sources_ (100.64.0.0/10 and fd7a:115c:a1e0::/48) to _any tailnet destination_, and its header comment is different. Since `dae10f2` (feat(firewall): pass tailnet sources only to the Mac's own tailnet addresses), Rig renders the destination as terra's own addresses: 100.96.126.29 and fd7a:115c:a1e0::ba36:7e1e. Because the comment changed too, the finding is `anchor-changed` rather than `tailnet-address-stale`. The LaunchDaemon is current: it last exited 0, its pfctl command is `-E -a com.apple/<locator> -f <anchor>`, and `/etc/pf.conf` keeps the `anchor "com.apple/*"` hook.
  - **exposed-beyond-tailnet:** this only means Screen Sharing listens on all addresses (netstat shows `tcp4/tcp6 *.5900 LISTEN`). Rig adds this flag to any drifted firewall declaration whose port has a wildcard listener. It is not evidence of traffic getting through. If the 14 October anchor is loaded, 5900 from outside the tailnet is still blocked: the older rules are broader on destination only, not on source. I could not confirm that the anchor is loaded or that pf is enabled, because `pfctl -s` needs root and `sudo -n` asks for a password. Loopback tests are not valid, since lo0 is always passed.
  - **Proposed fix (attended, with Kris's approval):** in a terminal on terra, back up the anchor with `sudo cp /etc/pf.anchors/uk.me.kris.rig.firewall.screen-sharing ~/pf-anchor.bak`. Check the kernel state with `sudo pfctl -s info | head -1` and `sudo pfctl -a com.apple/uk.me.kris.rig.firewall.screen-sharing -s rules`. Then run `rig apply --target firewall:screen-sharing-tailnet --sudo --dry-run`, then the apply. Last, test Screen Sharing from another tailnet device, and check that a non-tailnet LAN device is refused on 5900.
  - **Keeping the connection:** SSH (22) and Tailscale are not in this anchor, and the tailnet path to 5900 stays allowed. Kris at the console is unaffected.
  - **Restore:** `sudo cp ~/pf-anchor.bak /etc/pf.anchors/uk.me.kris.rig.firewall.screen-sharing && sudo pfctl -a com.apple/uk.me.kris.rig.firewall.screen-sharing -f /etc/pf.anchors/uk.me.kris.rig.firewall.screen-sharing`. Emergency fallback: `sudo pfctl -a com.apple/uk.me.kris.rig.firewall.screen-sharing -F rules`. This flushes only Rig's anchor, which reopens 5900 and leaves everything else alone. The restore has not been rehearsed yet. The terra rehearsal on 19 October predates this render.

## Queries

**Context:** The firewall anchor on terra predates `dae10f2`. It is probably still blocking non-tailnet access, but that cannot be verified without sudo. **Query:** Should the attended firewall re-apply above be scheduled while you are at terra? **Options:** a) (recommended, confidence medium - low risk with the backup and the anchor-only flush fallback, and it clears the last doctor finding) Run it with ki.mac-studio-setup in an attended session with sudo. b) Leave it until the next Mac rehearsal in KI-TOOL-RIG-CORE-047.

**Context:** Tower Assistant 2.1 is not yet in /Applications; 2.0 is in ~/Applications. **Query:** Who installs 2.1 into /Applications, so that the two held chezmoi files and the Dock item can be applied? **Options:** a) (recommended, confidence high - the declaration already expects /Applications) Install 2.1 through the ki-self application lifecycle, then run the scoped apply. b) Revert the source to ~/Applications until then.
