---
id: ki.mac-studio-setup
state: with-worker
since: 2026-10-19T22:30:00Z
received: 2026-10-19T22:27:00Z
beat: null
mark: 2026-10-19T22:36:00Z
method_read: 84b61942
---

# ki.mac-studio-setup state

## Now

- With worker since 23:30 BST on 19 October; marked at 23:36 BST on 19 October.
- rig-capture received 23:31 BST: RIG-UNLOAD-LABEL, every caller proven to guarantee a non-empty label, no record; TOML-HANDLER captured as KI-TOOL-RIG-CORE-069 (Triage); tools-rig commits ccd14ac and 4f97d74, local, unpushed; BOOTOUT-GUARD raised; bootout-review agreed at 23:34 BST, now high and with Kris.
- Running, chained in tools-rig: core063 (plan and deliver KI-TOOL-RIG-CORE-063 to Awaiting review), then plan062 (plan KI-TOOL-RIG-CORE-062), then plan027 (plan KI-TOOL-RIG-CLI-027); local commits only, no push.
- With Kris: SOL-FW-TEST, Kris to restate or confirm it; BOOTOUT-GUARD.
- ki-principal push left to the owning sessions (PUSH-STACK a).
- FIRST-STEP done: `ki-work-package` and all five files re-read, description, Goals and Scope confirmed as drafted, `method_read` set.
- REPORT-SWEEP received: the four kept reports stay, their outcomes not yet homed; rig-lane's query is RIG-ORDER, and the other three are the held at-screen steps below.
- Decisions struck at the 23:36 BST mark by decision-strike (64ddf80f): 139 deleted, three pointers, 24 kept.
- Looks resolved, to confirm with Kris: terra key-only SSH and HOSTKEY-APPLY steps 6-9 (KB-DOTFILES-UE-088 records both applied and verified on both Macs on 16 October), and the parked SOL-HNR-HARNESS (the Project note says the HNR harness stays on sol).
- Run reports sit in `~/.local/state/ki/agents/mac-studio-setup/`, retired ones in its `archive/`.

## Next steps

1. With Kris, ADOBE-RESTART first (deferred, "remind me another day"): restart sol, run [`./adobe-remove.sh`](design/adobe-remove.sh) as a dry run (apps and add-ons none, nothing under What is left), then `ls -d /Applications/Adobe* /Applications/Utilities/Adobe* ~/Pictures/Lightroom/*.lrcat`, which should show only the catalogue.
2. Receive rig-capture, core063, plan062 and plan027; then Kris accepts the two Awaiting-review records at the next sol session; SOL-FW-TEST when Kris restates it.
3. Then put the parked queries in `queries.md` back one at a time, each with a recommendation and its reason.

## Held

- At sol's screen: key-only SSH ([ssh-keyonly](ssh-keyonly.report.md)), KB-DOTFILES-UE-086 steps 0-12 ([ue086-walk](ue086-walk.report.md)), the UTM swap (UTM-SOL), the Observatory restart (OBS-RESTART) and the KI-TOOL-RIG-CORE-047 live firewall test - until Kris is at sol's screen.
- At terra's screen: pull tools-rig and upgrade Rig past 0.6.3; pull chezmoi and run `chezmoi apply ~/.config/rig && rig doctor`; HOSTKEY-APPLY steps 6-9 ([hostkey-check](hostkey-check.report.md)); then key-only SSH - until Kris is at terra's screen.
- Anywhere: the Headroom favicon request ([favicons-headroom.svg](design/favicons-headroom.svg)) - until Kris takes it up.
- FW-LIVE's reboot check - at terra's next natural restart.
- ZED-MD - later, at sol.
- RIG-FULLSCREEN - an idea only (full-screen Rig terminal mode, btop-style panes); no record until Kris asks.
- FW-LINUX-LIVE - until a Linux host is available.
- KEYCHAIN-SSH - with ki.chezmoi, to which it was handed (looks resolved; the worker judges).
