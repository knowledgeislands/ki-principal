---
id: ki.mac-studio-setup
level: project
title: 'KI > Rig > Mac Studio setup'
project: mac-studio-setup
theme: rig
worker: agent
supervisor: owner
state: on-hold
hold:
  reason: paused
  release: after the work migration lands
since: 2026-10-18T03:30:38Z
received: null
beat: null
mark: 2026-10-18T01:20:00Z
created_at: 2026-10-08T08:45:00Z
---

# ki.mac-studio-setup

## Next steps

- **Status:** hold, 2026-10-18 02:20 BST (mark 2026-10-18T01:20Z), drained for the ways-of-working updates at Kris's request. Running: nothing.
- **Resume line:** `Resume Rig: mac-studio-setup from its checkpoint under current ki-pmo and ki-delegation since 2026-10-18T01:20Z: re-bootstrap, read the pick-up block, take stock, put the parked queries back, restart authorised work, then banner.`
- **Next:** first REMIND Kris of the deferred sol restart (ADOBE-RESTART). Then put the parked queries back one at a time, each with a recommendation and its reason (Kris 2026-10-17: step by step), starting with RIG-ORDER.

On resume: remind Kris of ADOBE-RESTART, then put RIG-ORDER back first, step by step.

## Messages

- 2026-10-18 · THREADS-REGRESSION · KI > Model > Ways of working: your `mac-studio-setup` run is still homed in the retired `+/_THREADS/mac-studio-setup/` (`~/.local/state/ki/agents/mac-studio-setup/thread.json`), so the installed `ki` copies every report there; briefs such as `adobe-clear` named `+/_THREADS/mac-studio-setup/` report paths, and a `decisions.md` still sits in the run's state folder for `ki agent decide` to adopt. Before your next launch run `ki agent home mac-studio-setup --work ki.mac-studio-setup` from this repository and write report paths as `+/_WORK/ki.mac-studio-setup/`, never `+/_THREADS/` or `+/_CHECKPOINTS/`. The next `ki` release follows a retired home automatically, under [KI-TOOL-KI-CLI-150](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-150-work-folder-entry-points.md), and the audit now fails either folder beside `+/_WORK/`, under [KI-HARNESS-GOV-200](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-200-thread-folder-closed-list.md).
- MIGRATED - this file was `+/_CHECKPOINTS/rig.mac-studio-setup.md` until the work migration of 2026-10-18. At your next mark, cut it to next steps, Messages and the tags of parked queries, each linked to its report; move anything else to its durable home, then remove this line.

## Parked

Parked at the 2026-10-18 hold (Kris; put back one at a time, with a recommendation and reason):

- **`RIG-ORDER`** - the tools-rig burndown order in rig-lane.report.md. Recommended a): first clear the review queue (KI-TOOL-RIG-CORE-060 and KI-TOOL-RIG-CORE-047, Kris), then deliver KI-TOOL-RIG-CORE-042, then ready KI-TOOL-RIG-CORE-052, KI-TOOL-RIG-CORE-054 and KI-TOOL-RIG-CORE-055 in one ki-plan sitting, then KI-TOOL-RIG-CORE-058. b) puts the correctives first.
- **`ADOBE-RESTART`** - deferred, "remind me another day". Restart sol, run `./adobe-remove.sh` as a dry run (apps and add-ons none, nothing under What is left), then `ls -d /Applications/Adobe* /Applications/Utilities/Adobe* ~/Pictures/Lightroom/*.lrcat`, which should show only the catalogue.
- **`ADOBE-DATA`** - about 8 GB of leftover Adobe data on sol, including the Lightroom catalogue. Recommended: keep the catalogue and delete the rest at a sol screen session (it needs sudo). Not deleted on Kris's broad "get rid of everything".
- **At sol's screen:** key-only SSH (ssh-keyonly.report.md), KB-DOTFILES-UE-086 steps 0-12 (ue086-walk.report.md), the UTM swap (UTM-SOL), the Observatory restart (OBS-RESTART), and the KI-TOOL-RIG-CORE-047 live firewall test.
- **At terra's screen:** pull tools-rig and upgrade Rig past 0.6.3; pull chezmoi and run `chezmoi apply ~/.config/rig && rig doctor`; HOSTKEY-APPLY steps 6-9 (hostkey-check.report.md); then key-only SSH.
- **Anywhere:** the Headroom favicon request and the desk kit.
- **`FOOTER-RECORD`** - approved, held until another session's tools-ki rebase clears (stuck since 2026-10-16 08:51). Then an agent commits only the KI-TOOL-KI-CLI-134 note locally (launcher-footer.report.md).

Parked (Kris, 2026-10-14), each described in the run folder reports `old-trees`, `sol-build` and `records`: `FW-LIVE` (terra rule comparison; reboot check at the next natural restart), `SOL-FW-TEST`, `UE-089-SHAPE`, `OLD-ORPHANS` (four repositories GitHub no longer serves), `MGIT-PRESEED` (an unfinished `tools-mgit` change saved as a patch in terra's run folder), `SOL-SOURCES`, `SOL-HNR-HARNESS`, `SOL-WHATSAPP`, `SOL-KI-CONFIG-DRIFT`.

No action now: `ZED-MD` (later, at `sol`), `FW-LINUX-LIVE` (needs a Linux host), `KEYCHAIN-SSH` (with rig.chezmoi).
