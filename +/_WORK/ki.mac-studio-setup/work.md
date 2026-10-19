---
id: ki.mac-studio-setup
level: project
title: 'KI > Rig > Mac Studio setup'
project: mac-studio-setup
theme: rig
worker: agent
supervisor: owner
state: handoff-to-supervisor
since: 2026-10-19T10:20:00Z
received: 2026-10-19T10:04:00Z
beat: null
mark: 2026-10-18T01:20:00Z
created_at: 2026-10-08T08:45:00Z
---

# ki.mac-studio-setup

## Next steps

- **Status:** handoff to supervisor since 2026-10-19 11:20 BST. Running: nothing.
- **With Kris, one at a time:** ADOBE-RESTART (restart sol, then the dry-run and catalogue checks), then RIG-ORDER (refreshed 2026-10-19 in rig-lane.report.md; recommended: plan and deliver KI-TOOL-RIG-CORE-063 in the background, plan KI-TOOL-RIG-CORE-062 and KI-TOOL-RIG-CLI-027, and Kris takes the Wave 0 acceptances, KI-TOOL-RIG-CORE-042 and KI-TOOL-RIG-CORE-047, at the next sol session after KB-DOTFILES-UE-091 lands).
- **Then:** the remaining parked items, each with a recommendation and its reason.

## Messages

- MIGRATED - this file was `+/_CHECKPOINTS/rig.mac-studio-setup.md` until the work migration of 2026-10-18. At your next mark, cut it to next steps, Messages and the tags of parked queries, each linked to its report; move anything else to its durable home, then remove this line.

## Parked

Parked at the 2026-10-18 hold (Kris; put back one at a time, with a recommendation and reason):

- **`RIG-ORDER`** - the tools-rig burndown order in rig-lane.report.md. Recommended a): first clear the review queue (KI-TOOL-RIG-CORE-060 and KI-TOOL-RIG-CORE-047, Kris), then deliver KI-TOOL-RIG-CORE-042, then ready KI-TOOL-RIG-CORE-052, KI-TOOL-RIG-CORE-054 and KI-TOOL-RIG-CORE-055 in one ki-plan sitting, then KI-TOOL-RIG-CORE-058. b) puts the correctives first.
- **`ADOBE-RESTART`** - deferred, "remind me another day". Restart sol, run `./adobe-remove.sh` as a dry run (apps and add-ons none, nothing under What is left), then `ls -d /Applications/Adobe* /Applications/Utilities/Adobe* ~/Pictures/Lightroom/*.lrcat`, which should show only the catalogue.
- **`ADOBE-DATA`** - about 8 GB of leftover Adobe data on sol, including the Lightroom catalogue. Recommended: keep the catalogue and delete the rest at a sol screen session (it needs sudo). Not deleted on Kris's broad "get rid of everything".
- **At sol's screen:** key-only SSH (ssh-keyonly.report.md), KB-DOTFILES-UE-086 steps 0-12 (ue086-walk.report.md), the UTM swap (UTM-SOL), the Observatory restart (OBS-RESTART), and the KI-TOOL-RIG-CORE-047 live firewall test.
- **At terra's screen:** pull tools-rig and upgrade Rig past 0.6.3; pull chezmoi and run `chezmoi apply ~/.config/rig && rig doctor`; HOSTKEY-APPLY steps 6-9 (hostkey-check.report.md); then key-only SSH.
- **Anywhere:** the Headroom favicon request.

Parked (Kris, 2026-10-14), each described in the run folder reports `old-trees`, `sol-build` and `records`: `FW-LIVE` (terra rule comparison; reboot check at the next natural restart), `SOL-FW-TEST`, `UE-089-SHAPE`, `OLD-ORPHANS` (four repositories GitHub no longer serves), `MGIT-PRESEED` (an unfinished `tools-mgit` change saved as a patch in terra's run folder), `SOL-SOURCES`, `SOL-HNR-HARNESS`, `SOL-WHATSAPP`, `SOL-KI-CONFIG-DRIFT`.

No action now: `ZED-MD` (later, at `sol`), `FW-LINUX-LIVE` (needs a Linux host), `KEYCHAIN-SSH` (with rig.chezmoi).
