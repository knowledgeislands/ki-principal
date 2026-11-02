---
note_type: work/handover
created_at: 2026-11-02T15:40:00Z
author: Written with Claude
---

# Mac Studio setup handover

## Overview

Kris decided on 1 November (HANDOVER-HOUSEHOLD, with PS-STUDIO "Into household" and HOUSEHOLD-NAMES, in [ki.prj.ways-of-working decisions](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/decisions.md)) that [ki.prj.mac-studio-setup](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.mac-studio-setup/work.md) hands over to the household works, which now live in the chezmoi source:

- [personal.reg.household-sol](/Users/krisbrown/.local/share/chezmoi/+/_WORK/personal.reg.household-sol/work.md) takes everything at sol's screen and sol's upkeep. It is the main receiver, as PS-STUDIO set.
- [personal.reg.household-terra](/Users/krisbrown/.local/share/chezmoi/+/_WORK/personal.reg.household-terra/work.md) takes what is left at terra's screen, and the reply on its two Rig asks.

The household works exclude Rig tooling changes, so the tools-rig records, ideas and capture requests this work carried go to the tools-rig owner. No other work names tools-rig, so until Kris names one (query TOOLS-RIG-LANE in the handover run report), the tools-rig owner below means [ki.sop.main](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.sop.main/state.md).

Every item was checked read-only on sol on 2 November 2026 at about 15:30 GMT, against tools-rig at `8f77dd5`, chezmoi at `ee3ca84`, `rig doctor` (Rig 0.8.0, 12 findings), `ki doctor`, the OneDrive folders and sol's applications. terra was not reachable from this run, so terra-only items rest on records, not live checks.

Verdicts: `settled` (done, with what settled it), `superseded` (overtaken by later work), `partly`, `live` (still owed) or `unknown` (not provable from sol).

## Open and parked queries

| Item | Verdict | Evidence | Who takes it |
| --- | --- | --- | --- |
| RIG-069-PROBE: attended probe at sol for [KI-TOOL-RIG-CORE-069](/Users/krisbrown/kis/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-069-dynamic-type-handler-fallback.md) | live | 069 is still draft; sol's `rig doctor` still shows `default-application.toml` drifted (VS Code, Zed expected) | household-sol runs the probe with Kris at sol; the tools-rig owner then approves 069 to Ready |
| RIG-ASKS: GUIDE-FIELD and RIG-RETIRE-ONE | live | Neither is in the tools-rig roadmap or ideas; household-terra lists both as waiting on this work ([paperclip-out](/Users/krisbrown/.local/share/chezmoi/+/_WORK/personal.reg.household-terra/aside/paperclip-out.report.md)) | Kris answers; the tools-rig owner captures; household-terra is told the outcome |
| RIG-INTAKE: the retained Rig capability lines | live | Blind-reviewed at high; none captured yet; per-line table in [rig-intake](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.mac-studio-setup/setup/rig-intake.report.md) | Kris answers; the tools-rig owner captures |
| PLAN068-VERIFY-GRANT, [KI-TOOL-RIG-CORE-068](/Users/krisbrown/kis/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-068-replaced-pf-root-ruleset-bypass.md) | live | 068 still draft | tools-rig owner, with Kris |
| PLAN068-UNPRIV | partly | sol's `rig doctor` already reports `kernel-rules-unverified`, the wording option a) recommends (tools-rig `00f6886`); the plan question itself is unanswered | tools-rig owner, with Kris |
| PLAN068-READY | live | 068 still draft; its implementation gate is the attended NordVPN check, and NordVPN runs on terra (NORDVPN-HOLD) | Kris decides; household-terra runs the attended check when asked |
| RIG-TRIAGE: eight undecided Rig records | settled | 053, 056 and 067 done and pruned; 057 cancelled (rejected); DIST-011 cancelled (obsolete); 064 moved to ideas; 068 and 069 in Now. See the pruned links below | Nobody; close it |
| ADOBE-DATA: about 8 GB of Adobe leftovers on sol | live | sol still holds 6.2 GB in `~/Library/Application Support/Adobe`, 1.3 GB in `/Library/Application Support/Adobe` and `~/Pictures/Lightroom`; ADOBE-DATA (15 October) wants an agent's per-folder list for Kris to approve | household-sol |
| FW-LIVE: terra's pf anchor loaded | settled | FW-VERIFY (15 October) proved the rules loaded; terra's re-apply completed on 24 October ([KI-TOOL-RIG-CORE-047](/Users/krisbrown/kis/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md) Current state) | Nobody; close it |
| UE-089-SHAPE: channel model | live | [PERSONAL-DOTFILES-UE-089](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/PERSONAL-DOTFILES-UE-089-ki-tool-release-channels.md) is still draft, Future | ki.prj.chezmoi (folding into the household works under PS-CHEZMOI) |
| OLD-ORPHANS: four repositories once only on sol | unknown | No checkout or bundle of them under `~/kis`, `~/workspaces` or OneDrive on sol; State of play's OLD-ORPHANS asks Kris where they are | Kris answers in ki.sop.main |
| MGIT-PRESEED: unfinished `mgit repair` change | unknown | The patch is no longer at its cited path (`~/.local/state/ki/agents/mac-studio-bootstrap/`) and no tools-mgit record cites it | ki.sop.main routes it to ki.prj.tools-burndown, or Kris drops it |
| SOL-SOURCES: OneDrive source stores on sol | settled | All `sources-*` folders are present on sol, including both named in option a) and the five kit groups | Nobody; close it |
| SOL-HNR-HARNESS | settled | `~/.local/share/ki/harnesses/humansnotrobots/hnr-agentic-harness` is installed; `ki doctor` counts two harnesses | Nobody; close it |
| SOL-WHATSAPP | live | sol's `~/.mcporter/mcporter.json` still lists the WhatsApp server, with no linked device on sol | household-sol (the inventory change through ki.prj.chezmoi) |
| SOL-KI-CONFIG-DRIFT | settled | Overtaken: the HNR Harness is installed and `ki-pmo-design` settled by SKILLS-CONFIG; State of play judged it obsolete. A different `ki doctor` failure is new: the active `ki-agentic-harness` root does not match the configured local source | Nobody for the old query; household-sol takes the new `ki doctor` finding |
| C56-TICK | settled | C5 and C6 are ticked in [PERSONAL-DOTFILES-UE-086](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/PERSONAL-DOTFILES-UE-086-finish-software-alignment.md) | Nobody; close it |
| C8-WORDING | settled | C8 now expects Keynote, Numbers and Pages catalogue-only | Nobody; close it |

## State lines

| Item | Verdict | Evidence | Who takes it |
| --- | --- | --- | --- |
| Now: re-bootstrap, dispatch and method-read lines (30 and 31 October) | settled | History only | Nobody |
| Now: Orca trial evidence to ki.prj.orca-evaluation | settled | Handed over 30 October (`d38088a3`) | Nobody |
| Now: open tools-rig records 047, 068, 069 and [KI-TOOL-RIG-CORE-070](/Users/krisbrown/kis/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-070-handler-read-back-after-confirmation.md) | live | Unchanged, with 070 still awaiting review; two newer triage records, [KI-TOOL-RIG-CORE-075](/Users/krisbrown/kis/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-075-restart-services-after-upgrade.md) and [KI-TOOL-RIG-CORE-076](/Users/krisbrown/kis/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-076-host-defaults-and-power.md), have no owning work | tools-rig owner; 070's acceptance is Kris's |
| Now: the lane, tools-rig and the agent-host hold cluster | live | RIG-OWNER (17 October) gave this work the tools-rig lane; no other work names it | Kris names the next owner (TOOLS-RIG-LANE) |
| Next 2: spec-sched (schedule encoding in `rig show --format json`) | live | Never ran: stopped before start at the 20 October hold; no tools-rig specification describes the encoding yet ([brief](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.mac-studio-setup/setup/spec-sched.brief.md)) | tools-rig owner, with a new go from Kris; ki.prj.observatory is the requester |
| Next 4: ADOBE-RESTART (restart sol and final check) | partly | sol has restarted since (up 9 days); Lightroom, Photoshop and Creative Cloud are gone from `/Applications`; the data clean-up is ADOBE-DATA | household-sol, inside ADOBE-DATA and C7i |
| Next 4: ADOBE-SCRIPT-HOME, [adobe-remove.sh](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.mac-studio-setup/setup/adobe-remove.sh) | live | Still in the package; State of play's ADOBE-SCRIPT-HOME recommends sending it to tools-rig as removal evidence | Kris answers in ki.sop.main; the tools-rig owner keeps the copy |
| Held: KI-TOOL-RIG-CORE-047 on terra (NordVPN checks, `rig apply --sudo`) | partly | terra's re-apply completed on 24 October; sol's own narrowed-address pass is still owed (sol's `rig doctor`: `anchor-changed`, `listening-all-addresses`); the NordVPN check waits on 068's restore path | household-sol for sol's attended re-apply (its FIREWALL-REAPPLY); household-terra for the NordVPN check; the tools-rig owner closes 047 |
| Held at sol: key-only SSH ([ssh-keyonly](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.mac-studio-setup/setup/ssh-keyonly.report.md)) | settled | `/etc/ssh/sshd_config.d/050-ki-key-only.conf` is installed on sol; KEYONLY-SKIP-EXIT is moot on sol | Nobody for sol |
| Held at sol: PERSONAL-DOTFILES-UE-086 steps 0 to 12 ([ue086-walk](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.mac-studio-setup/setup/ue086-walk.report.md)) | partly | Done: C7c (APP-PURGE, 1 November) and the Adobe apps of C7i. Still on sol: `uv` and Homebrew Python (C4), PTGui Pro (C7a), ScanSnap and ABBYY (C7b), Actual, Moom and Ice (C7d), Clicker Writer (C7e), `hermes-agent` with its failing `ai.hermes.gateway` (C7f), `libtiff` and `node` (C7h), then C8 and C9; UE-086's Discussion already holds the sol sitting | household-sol |
| Held at sol: UTM-SOL | live | UTM is not installed at all on sol: `rig doctor` reports it missing via `mas` and the last `rig apply` of it failed on 25 October | household-sol |
| Held at sol: OBS-RESTART | settled | `uk.me.kris.rig.observatory` is running and `http://127.0.0.1:1675/` answers | Nobody |
| Held at terra: HOSTKEY-APPLY steps 6 to 9 ([hostkey-check](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.mac-studio-setup/setup/hostkey-check.report.md)) | unknown | sol's half is applied (`Host terra` in `~/.ssh/config`), though its backup `~/.ssh/config.pre-ue088` is still on sol; terra's half was flagged "looks resolved" on 19 October but not confirmed | household-terra confirms on terra; household-sol deletes the sol backup |
| Held at terra: key-only SSH | unknown | Not checkable from sol | household-terra |
| Held at terra: firewall re-apply | settled | Completed 24 October (047) | Nobody |
| Held anywhere: Headroom favicon request ([favicons-headroom.svg](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.mac-studio-setup/setup/favicons-headroom.svg)) | live | HEADROOM-ICON (15 October): Kris files it on Headroom's GitHub; not filed as far as the package knows | Kris; household-sol keeps the drawing once this package closes |
| Held: FW-LIVE reboot check at terra's next restart | unknown | Not checkable from sol | household-terra |
| Held: ZED-MD at sol | partly | Rig's `default-application` resource shipped, but no `.md` handler is declared in Rig's configuration (only `svg`, `toml`, `sh` and `zsh`) | ki.prj.chezmoi declares it; household-sol applies it |
| Held: FW-LINUX-LIVE | settled | [KI-TOOL-RIG-CORE-051 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/06da52aec5de300f03386efbdb637af1873c18d0/docs/roadmap/KI-TOOL-RIG-CORE-051-linux-tailnet-only-firewall.md) was closed done | Nobody |
| Held: RIG-FULLSCREEN, idea only | live | Folded into RIG-INTAKE's RIG-TUI capture | tools-rig owner |

## Retained Rig lines in `messages.md`

These lines stay in this package's [messages.md](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.mac-studio-setup/messages.md) until RIG-INTAKE is answered; at close-out the coordinator forwards them to the tools-rig owner.

| Item | Verdict | Evidence | Who takes it |
| --- | --- | --- | --- |
| RIG-APP-FOOTPRINT (IMPORTANT), both RIG-NOTIFICATIONS lines, RIG-MACHINE-MANAGEMENT | live | Not in the [KI-TOOL-RIG-CORE-072 idea](/Users/krisbrown/kis/knowledge-islands/tools-rig/docs/ideas/KI-TOOL-RIG-CORE-072-application-configuration-touch-points.md), which does not mention notifications, login items or privacy grants | tools-rig owner, after RIG-INTAKE |
| RIG-COMMENT-KIND | live | Not captured | tools-rig owner, after RIG-INTAKE |
| RIG-CLI-CONSISTENCY | live | Not captured; sol still runs Rig 0.8.0 | tools-rig owner, after RIG-INTAKE |
| RIG-TUI | live | Not captured | tools-rig owner, after RIG-INTAKE |
| RIG-SSH-CHECK | live | Not captured | tools-rig owner, after RIG-INTAKE |
| WAKE-SUBSTRATE | superseded | Rig's share shipped as `scheduled-job`; household-sol's host loop and its HOST-WATCHER message (2 November) now carry the wake | ki.sop.main sends the return line under RIG-INTAKE |
| RIG-REMINDER-DOCTOR | settled | chezmoi registers the coordinator reminder hook on every machine; Rig declines | ki.sop.main sends the return line under RIG-INTAKE |
| REPORTS-MOVED (1 November) | settled | No `reports/` folder is left in the package | Nobody |

## Other files in `setup/`

| File | Verdict | Who takes it |
| --- | --- | --- |
| [design.md](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.mac-studio-setup/setup/design.md) | settled; goes with the package at close-out | Nobody |
| [handover.brief.md](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.mac-studio-setup/setup/handover.brief.md) | settled once this note is received | Nobody |
| [rig-intake.report.md](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.mac-studio-setup/setup/rig-intake.report.md) | live until RIG-INTAKE is answered | tools-rig owner |

## Pruned records cited

- [KI-TOOL-RIG-CORE-053 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/14715c300bb39542107da7fb515281af45fbba16/docs/roadmap/KI-TOOL-RIG-CORE-053-macos-menu-bar-declarations.md), done.
- [KI-TOOL-RIG-CORE-056 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/63d1ac92d4a19fc0b8b7bd980b0dc831858e5efb/docs/roadmap/KI-TOOL-RIG-CORE-056-menu-bar-order-persistence.md), done.
- [KI-TOOL-RIG-CORE-067 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/63d1ac92d4a19fc0b8b7bd980b0dc831858e5efb/docs/roadmap/KI-TOOL-RIG-CORE-067-package-managers-as-catalogue-tools.md), done.
- [KI-TOOL-RIG-CORE-057 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/74140e530fe61ebecb9a687038d76cf3244439b3/docs/roadmap/KI-TOOL-RIG-CORE-057-github-desktop-repository-list.md), cancelled as rejected.
- [KI-TOOL-RIG-DIST-011 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/74140e530fe61ebecb9a687038d76cf3244439b3/docs/roadmap/KI-TOOL-RIG-DIST-011-stale-terra-rig-link.md), cancelled as obsolete.
- [KI-TOOL-RIG-CORE-064](/Users/krisbrown/kis/knowledge-islands/tools-rig/docs/ideas/KI-TOOL-RIG-CORE-064-unmanaged-configuration-scan.md), moved to ideas.
- [PERSONAL-DOTFILES-UE-088 (pruned)](https://github.com/krisb/dotfiles/blob/7cb547a86133325168183bc9c5962fa9550671a5/docs/roadmap/KB-DOTFILES-UE-088-ssh-alias-for-sol.md), the SSH alias and key-only record.

## New on sol, not from this package

`rig doctor` on sol now reports eight npm tools missing (`codex-multi-auth`, `corepack`, `imageoptim-cli`, `npm-check-updates`, `skills-cli`, `turbo`, `typescript`, `wrangler`), which household-sol's 13:15 GMT count of four findings did not include. household-sol takes it.
