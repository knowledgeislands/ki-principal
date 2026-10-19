---
id: ki.mac-studio-setup
state: handoff-to-supervisor
since: 2026-10-19T18:52:00Z
received: 2026-10-19T18:51:00Z
beat: null
mark: 2026-10-19T18:01:00Z
method_read: 2026-10-19T18:01:00Z
---

# ki.mac-studio-setup state

## Now

- Handoff to supervisor since 19:52 BST on 19 October; marked at 19:01 BST on 19 October.
- Nothing is running. query-review received at 19:51 BST: SOL-FW-TEST shows both views, PUSH-STACK reviewed to high; RIG-ORDER, high and not destructive, was not reviewed.
- FIRST-STEP done: `ki-work-package` and all five files re-read, description, Goals and Scope confirmed as drafted, `method_read` set.
- REPORT-SWEEP received: the four kept reports stay, their outcomes not yet homed; rig-lane's query is RIG-ORDER, and the other three are the held at-screen steps below.
- Decisions not yet struck at this mark; the next mark takes it as a run.
- Run reports sit in `~/.local/state/ki/agents/mac-studio-setup/`, retired ones in its `archive/`.

## Next steps

1. With Kris, ADOBE-RESTART first (deferred, "remind me another day"): restart sol, run [`./adobe-remove.sh`](design/adobe-remove.sh) as a dry run (apps and add-ons none, nothing under What is left), then `ls -d /Applications/Adobe* /Applications/Utilities/Adobe* ~/Pictures/Lightroom/*.lrcat`, which should show only the catalogue.
2. Then RIG-ORDER (`queries.md`, refreshed on 19 October in [rig-lane](rig-lane.report.md)), and SOL-FW-TEST.
3. Then put the parked queries in `queries.md` back one at a time, each with a recommendation and its reason.

## Held

- At sol's screen: key-only SSH ([ssh-keyonly](ssh-keyonly.report.md)), KB-DOTFILES-UE-086 steps 0-12 ([ue086-walk](ue086-walk.report.md)), the UTM swap (UTM-SOL), the Observatory restart (OBS-RESTART) and the KI-TOOL-RIG-CORE-047 live firewall test - until Kris is at sol's screen.
- At terra's screen: pull tools-rig and upgrade Rig past 0.6.3; pull chezmoi and run `chezmoi apply ~/.config/rig && rig doctor`; HOSTKEY-APPLY steps 6-9 ([hostkey-check](hostkey-check.report.md)); then key-only SSH - until Kris is at terra's screen.
- Anywhere: the Headroom favicon request ([favicons-headroom.svg](design/favicons-headroom.svg)) - until Kris takes it up.
- FW-LIVE's reboot check - at terra's next natural restart.
- ZED-MD - later, at sol.
- FW-LINUX-LIVE - until a Linux host is available.
- KEYCHAIN-SSH - with ki.chezmoi, to which it was handed (looks resolved; the worker judges).
