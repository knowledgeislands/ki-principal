# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Initiatives/rig.md) › [Mac Studio setup](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/mac-studio-setup/mac-studio-setup.md) › rig-lane

**Run report at 23:50 BST · last mark 22:33 BST**

---

## Done

- Read all 13 open tools-rig records and the root orientation, read-only. Nothing in tools-rig was edited, staged or committed, and another session's unpushed [KI-TOOL-RIG-CORE-060 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/9752f6821938b67bc4177fa88b1c5bc529700dba/docs/roadmap/KI-TOOL-RIG-CORE-060-single-target-operation-speed.md) commits were left alone.
- Proposed a burndown order in five waves, below. SOL-APPLY, SOL-CLT and TERRA-READ are treated as answered, under the RIG-LANE approval.
- Told state-of-play through its inbox that this thread has started the tools-rig burndown lane (Master's RIG-OWNER), where the proposal is, and that nothing has changed yet.
- This report is committed locally in ki-principal by explicit path. It is not pushed.

### Proposed order

**Wave 0: clear the review queue (Kris).** These records are already delivered. Accepting them first keeps the lane from building on unaccepted work.

1. [KI-TOOL-RIG-CORE-060 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/9752f6821938b67bc4177fa88b1c5bc529700dba/docs/roadmap/KI-TOOL-RIG-CORE-060-single-target-operation-speed.md) Single-target operation speed. Awaiting review. It goes first because the work is done and later records build on its faster targeted runs. **Blocked on Kris and on another session:** acceptance needs Kris's word through `ki-accept`, and its commits must be pushed first (RIG-STACK-PUSH).
2. [KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md) Tailnet-only listener firewall. Awaiting review. Kris has approved the review, and closing it closes the Project. **Blocked on Kris at sol's screen:** a connection-critical `rig apply --sudo` live test is needed first. The terra rule comparison (FW-LIVE) needs terra.

**Wave 1: the Ready prerequisite and the small doctor fixes.** All of this can be done offline in isolated tests.

3. [KI-TOOL-RIG-CORE-042 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/abb734b12bca7e5836254741564c3ac093192524/docs/roadmap/KI-TOOL-RIG-CORE-042-profile-filtered-dock-items.md) Profile-filtered Dock items. Ready and in Now, with its plan approved, so `ki-implement` can start straight away. [KI-TOOL-RIG-CORE-053](https://github.com/knowledgeislands/tools-rig/blob/223ba459/docs/roadmap/KI-TOOL-RIG-CORE-053-macos-menu-bar-declarations.md) reuses its filtering, and chezmoi's [PERSONAL-DOTFILES-UE-091 (pruned)](https://github.com/krisb/dotfiles/blob/1b34ac10c35711d225a63a010ec13a9031a0e291/docs/roadmap/KB-DOTFILES-UE-091-shared-dock-tool-links.md) waits for it to reach Awaiting review. **Acceptance needs Kris at sol's screen:** the Dock apply there (decided 14 October).
4. [KI-TOOL-RIG-CORE-055 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/7ba751395a9c5492ed7664fb60cccf56ef52e5d3/docs/roadmap/KI-TOOL-RIG-CORE-055-interpreter-port-owner-matching.md) Interpreter port owner matching. Triage. This is a small corrective for a false `conflicting` finding, the noisiest gap left in `rig doctor`. The Headroom declaration itself stays with chezmoi under [PERSONAL-DOTFILES-UE-090](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/PERSONAL-DOTFILES-UE-090-close-rig-bring-up-gaps.md).
5. [KI-TOOL-RIG-CORE-052 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/7ba751395a9c5492ed7664fb60cccf56ef52e5d3/docs/roadmap/KI-TOOL-RIG-CORE-052-doctor-service-launch-prerequisites.md) Doctor service launch prerequisites. Triage. This is a small doctor check that sits beside [KI-TOOL-RIG-CORE-055 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/7ba751395a9c5492ed7664fb60cccf56ef52e5d3/docs/roadmap/KI-TOOL-RIG-CORE-055-interpreter-port-owner-matching.md) in the same port and service findings. Plan the two in one sitting.
6. [KI-TOOL-RIG-CORE-054 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/7ba751395a9c5492ed7664fb60cccf56ef52e5d3/docs/roadmap/KI-TOOL-RIG-CORE-054-command-line-tools-check.md) Command Line Tools check. Triage. This is a small doctor check, and sol's 82-of-84 upgrade failures already supply the evidence. It goes last in the wave because SOL-CLT has fixed the case that prompted it.

**Wave 2: the larger corrective.**

7. [KI-TOOL-RIG-CORE-058 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/6ac358fb607629ca9f9ff32d1694afdec112737d/docs/roadmap/KI-TOOL-RIG-CORE-058-apply-lock-handler-history.md) Apply lock, handler history. Triage. This is a real race: a scheduled `rig-update` can run alongside `apply`. It is wider than the doctor fixes, because it touches the locking and apply history that every apply and upgrade uses, so it needs planning of its own. It sits after Wave 1 so it does not collide with [KI-TOOL-RIG-CORE-042 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/abb734b12bca7e5836254741564c3ac093192524/docs/roadmap/KI-TOOL-RIG-CORE-042-profile-filtered-dock-items.md)'s apply-path changes.

**Wave 3: the remaining capability records.**

8. [KI-TOOL-RIG-CORE-057 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/74140e53/docs/roadmap/KI-TOOL-RIG-CORE-057-github-desktop-repository-list.md) GitHub Desktop repository list. Triage. sol is already fixed by hand, so this only pays off on the next new machine. It reads tools-mgit's territory manifests, so it depends on another repository's file format, though nothing blocks it.
9. [KI-TOOL-RIG-CORE-053](https://github.com/knowledgeislands/tools-rig/blob/223ba459/docs/roadmap/KI-TOOL-RIG-CORE-053-macos-menu-bar-declarations.md) macOS menu bar declarations. Triage, and the largest capability record. It must follow [KI-TOOL-RIG-CORE-042 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/abb734b12bca7e5836254741564c3ac093192524/docs/roadmap/KI-TOOL-RIG-CORE-042-profile-filtered-dock-items.md), whose profile filtering it reuses. **Acceptance needs Kris at a Mac's screen** to compare the real menu bar.

**Wave 4: the follow-up investigation.**

10. [KI-TOOL-RIG-CORE-056 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/63d1ac92d4a19fc0b8b7bd980b0dc831858e5efb/docs/roadmap/KI-TOOL-RIG-CORE-056-menu-bar-order-persistence.md) Menu bar order persistence. Future, investigate. The record says to do it after [KI-TOOL-RIG-CORE-053](https://github.com/knowledgeislands/tools-rig/blob/223ba459/docs/roadmap/KI-TOOL-RIG-CORE-053-macos-menu-bar-declarations.md) ships. It closes on a written finding, and observing across restarts needs Kris at the screen.

**Held: outside the lane until the hold lifts (each is reviewed on 2026-11-16).**

11. [KI-TOOL-RIG-CORE-048 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/63d1ac92d4a19fc0b8b7bd980b0dc831858e5efb/docs/roadmap/KI-TOOL-RIG-CORE-048-signed-release-install-kind.md) Signed-release install kind. **Blocked on vega and another repository:** it waits for vega to be rebuilt and for ki-techne-harness [KI-TECHNE-OPS-018](/Users/krisbrown/workspaces/knowledge-islands/ki-techne-harness/docs/roadmap/KI-TECHNE-OPS-018-converge-tools-through-rig.md) to come off hold.
12. [KI-TOOL-RIG-DIST-011 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/74140e53/docs/roadmap/KI-TOOL-RIG-DIST-011-stale-terra-rig-link.md) Stale vega rig link. **Blocked on vega:** it waits for the Techne Programme Hold to lift. The fix is a single step on the host once that happens.
13. [KI-TOOL-RIG-CLI-026 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/74140e53/docs/roadmap/KI-TOOL-RIG-CLI-026-per-tool-development-mode-switch.md) Per-tool development mode switch. Parked. **Blocked on Kris:** it waits for Rig's Techne-boundary work to resume, or for Kris to adopt it sooner.

## In Progress

Nothing. No record has been selected, planned or changed.

## Queries

### RIG-ORDER - where the tools-rig burndown starts

**Context:** tools-rig has 13 open records: 2 awaiting review, 1 Ready, 7 untriaged or Future, and 3 on hold. The order above puts the review queue first, then the Ready Dock record with the small doctor fixes, then the apply-lock corrective, then the capability records. Wave 0 needs Kris and the push of the other session's [KI-TOOL-RIG-CORE-060 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/9752f6821938b67bc4177fa88b1c5bc529700dba/docs/roadmap/KI-TOOL-RIG-CORE-060-single-target-operation-speed.md) commits. Waves 1 to 4 can run as background agents, with tests isolated from the machine, until each record's acceptance check at the screen.

**Query:** Which order does the lane follow?

**Options:** a) (recommended) Follow the proposed order. Start with [KI-TOOL-RIG-CORE-042 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/abb734b12bca7e5836254741564c3ac093192524/docs/roadmap/KI-TOOL-RIG-CORE-042-profile-filtered-dock-items.md) under `ki-implement` once RIG-STACK-PUSH has landed, since it is Ready and two other records wait on it. In parallel, plan [KI-TOOL-RIG-CORE-055 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/7ba751395a9c5492ed7664fb60cccf56ef52e5d3/docs/roadmap/KI-TOOL-RIG-CORE-055-interpreter-port-owner-matching.md), [KI-TOOL-RIG-CORE-052 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/7ba751395a9c5492ed7664fb60cccf56ef52e5d3/docs/roadmap/KI-TOOL-RIG-CORE-052-doctor-service-launch-prerequisites.md) and [KI-TOOL-RIG-CORE-054 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/7ba751395a9c5492ed7664fb60cccf56ef52e5d3/docs/roadmap/KI-TOOL-RIG-CORE-054-command-line-tools-check.md) to Ready in one `ki-plan` sitting. Kris takes Wave 0 at the next screen session. b) Put the correctives first: plan and deliver [KI-TOOL-RIG-CORE-058 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/6ac358fb607629ca9f9ff32d1694afdec112737d/docs/roadmap/KI-TOOL-RIG-CORE-058-apply-lock-handler-history.md), then the three doctor fixes, then [KI-TOOL-RIG-CORE-042 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/abb734b12bca7e5836254741564c3ac093192524/docs/roadmap/KI-TOOL-RIG-CORE-042-profile-filtered-dock-items.md) and the capability waves. This puts the apply race ahead of the Dock work.

```text
RIG-ORDER - a) follow the proposed order: start KI-TOOL-RIG-CORE-042 under ki-implement once RIG-STACK-PUSH has landed, and plan KI-TOOL-RIG-CORE-055, KI-TOOL-RIG-CORE-052 and KI-TOOL-RIG-CORE-054 to Ready in one ki-plan sitting in parallel; Kris takes Wave 0 (accepting KI-TOOL-RIG-CORE-060, and the KI-TOOL-RIG-CORE-047 live test on sol) at the next screen session
```

```text
╭─ run report · 2026-10-17T22:50:16Z ──────────────╮
│                                                  │
│  █▀▀▄ █▀▀▀ █▀▀▀ ▀▀█▀   · run done                │
│  █▀▀▄ █▀▀  ▀▀▀█   █    · report local            │
│  █  █ █▄▄▄ ▄▄▄█   █    · 1 query                 │
│                                                  │
╰──────────────────────────────────────────────────╯
```

- [at rest] rig-lane finished; nothing running from this run
- [waiting] RIG-ORDER
- [waiting] RIG-STACK-PUSH
- [unpushed] thread folder

Resume Rig: mac-studio-setup under current ki-pmo and ki-delegation since 2026-10-17T21:33Z: re-bootstrap, mark, fresh summary with carried-forward open points, take stock, restart authorised work, then banner.

## Update 2026-10-19

Since the hold, the 17 October order has largely been delivered. [KI-TOOL-RIG-CORE-060 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/9752f6821938b67bc4177fa88b1c5bc529700dba/docs/roadmap/KI-TOOL-RIG-CORE-060-single-target-operation-speed.md), [KI-TOOL-RIG-CORE-052 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/7ba751395a9c5492ed7664fb60cccf56ef52e5d3/docs/roadmap/KI-TOOL-RIG-CORE-052-doctor-service-launch-prerequisites.md), [KI-TOOL-RIG-CORE-054 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/7ba751395a9c5492ed7664fb60cccf56ef52e5d3/docs/roadmap/KI-TOOL-RIG-CORE-054-command-line-tools-check.md), [KI-TOOL-RIG-CORE-055 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/7ba751395a9c5492ed7664fb60cccf56ef52e5d3/docs/roadmap/KI-TOOL-RIG-CORE-055-interpreter-port-owner-matching.md) and [KI-TOOL-RIG-CORE-058 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/6ac358fb607629ca9f9ff32d1694afdec112737d/docs/roadmap/KI-TOOL-RIG-CORE-058-apply-lock-handler-history.md) have been accepted and pruned, along with the new [KI-TOOL-RIG-CORE-061 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/6ac358fb607629ca9f9ff32d1694afdec112737d/docs/roadmap/KI-TOOL-RIG-CORE-061-removal-lock-diagnostics.md). Rig v0.7.0 has been released and main CI is green again. RIG-STACK-PUSH has landed: local `main` matches its tracking branch, though this was not fetched to confirm. [KI-TOOL-RIG-CORE-042 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/abb734b12bca7e5836254741564c3ac093192524/docs/roadmap/KI-TOOL-RIG-CORE-042-profile-filtered-dock-items.md) is delivered and Awaiting review, as is [KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md). Both gained live read-only evidence from sol and terra today. Five new records have arrived in Triage.

### Refreshed order

**Wave 0: close what is delivered (Kris).**

1. [KI-TOOL-RIG-CORE-042 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/abb734b12bca7e5836254741564c3ac093192524/docs/roadmap/KI-TOOL-RIG-CORE-042-profile-filtered-dock-items.md) Profile-filtered Dock items. **Blocked on chezmoi, then on Kris at sol's screen.** First, [PERSONAL-DOTFILES-UE-091 (pruned)](https://github.com/krisb/dotfiles/blob/1b34ac10c35711d225a63a010ec13a9031a0e291/docs/roadmap/KB-DOTFILES-UE-091-shared-dock-tool-links.md), still a draft, has to move the personal Dock layout to `core` and link its items, leaving `chatgpt-current` unlinked. Then a live `rig apply` on sol must show Zed in its place, with terra still `present`. Kris accepts through `ki-accept`.
2. [KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md) Tailnet-only listener firewall. **Needs Kris at sol, and terra by SSH.** The remaining checks are connection-critical: `rig apply --sudo` on sol with a tested restore path, the privileged `pfctl` read of terra's loaded rules, `vnc://` over the tailnet, a refused LAN connection from another device, and NordVPN on and off. terra already carries the anchor, installed outside Rig's records. Accepting this record closes the Project's firewall slice.
3. [KI-TOOL-RIG-DIST-012 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/f7ef0fdeb9893ec1fec407e19ff1e8370820e170/docs/roadmap/KI-TOOL-RIG-DIST-012-green-main-ci.md) Green main CI. Done. It only needs pruning, on Kris's word, under `ki-accept`.

**Wave 1: offline debt and the firewall follow-up.** These can run as background agents, with tests isolated from the machine.

4. [KI-TOOL-RIG-CORE-063 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/735a8e8560f951afeaa0194df52c5dffa26a3797/docs/roadmap/KI-TOOL-RIG-CORE-063-fatal-bats-assertions.md) Fatal Bats assertions. Triage. 64 non-fatal assertions mean failing checks can pass silently, so this goes first and makes every later delivery's tests trustworthy. The work is mechanical, but may expose latent faults.
5. [KI-TOOL-RIG-CORE-062](https://github.com/knowledgeislands/tools-rig/blob/223ba459/docs/roadmap/KI-TOOL-RIG-CORE-062-own-address-firewall-destination.md) Own-address firewall destination. Triage. This narrows the residual `100.64.0.0/10` risk that terra carries today. It can be planned now, but should be delivered after [KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md) is accepted, because it changes the same anchor. **Live acceptance needs sudo on both Macs.**
6. [KI-TOOL-RIG-CLI-027](https://github.com/knowledgeislands/tools-rig/blob/4ca939fa230b3e9eb02d9a170491a544a51b3651/docs/roadmap/KI-TOOL-RIG-CLI-027-command-line-convention-departures.mdCLI-027) Command-line convention departures. Triage. Four small option-parsing departures, all testable offline.

**Wave 2: capability.**

7. [KI-TOOL-RIG-CORE-053](https://github.com/knowledgeislands/tools-rig/blob/223ba459/docs/roadmap/KI-TOOL-RIG-CORE-053-macos-menu-bar-declarations.md) macOS menu bar declarations. Triage. It is now unblocked, because [KI-TOOL-RIG-CORE-042 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/abb734b12bca7e5836254741564c3ac093192524/docs/roadmap/KI-TOOL-RIG-CORE-042-profile-filtered-dock-items.md)'s profile filtering is delivered. **Acceptance needs Kris at a Mac's screen.**
8. [KI-TOOL-RIG-CORE-057 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/74140e53/docs/roadmap/KI-TOOL-RIG-CORE-057-github-desktop-repository-list.md) GitHub Desktop repository list. Triage. It only pays off on the next new machine.
9. [KI-TOOL-RIG-CORE-064](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-064-unmanaged-configuration-scan.md) Unmanaged configuration scan. Triage. **Needs a boundary decision from Kris before planning:** the scan sits between chezmoi, which owns configuration, and Rig, which would own the managed applications.

**Wave 3:** [KI-TOOL-RIG-CORE-056 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/63d1ac92d4a19fc0b8b7bd980b0dc831858e5efb/docs/roadmap/KI-TOOL-RIG-CORE-056-menu-bar-order-persistence.md) Menu bar order persistence. Future. It follows [KI-TOOL-RIG-CORE-053](https://github.com/knowledgeislands/tools-rig/blob/223ba459/docs/roadmap/KI-TOOL-RIG-CORE-053-macos-menu-bar-declarations.md), and **observing across restarts needs Kris at the screen**.

**Held, unchanged, each reviewed on 2026-11-16:** [KI-TOOL-RIG-CORE-048 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/63d1ac92d4a19fc0b8b7bd980b0dc831858e5efb/docs/roadmap/KI-TOOL-RIG-CORE-048-signed-release-install-kind.md), [KI-TOOL-RIG-DIST-011 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/74140e53/docs/roadmap/KI-TOOL-RIG-DIST-011-stale-terra-rig-link.md) and [KI-TOOL-RIG-CLI-026 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/74140e53/docs/roadmap/KI-TOOL-RIG-CLI-026-per-tool-development-mode-switch.md).

### RIG-ORDER - where the refreshed burndown starts

This query replaces the RIG-ORDER of 17 October.

**Context:** tools-rig has 13 open records. 2 are Awaiting review and need Kris at the screen. 1 is done and needs only pruning. 6 are in Triage, 1 is Future, and 3 are on hold. None of the open records is Ready, so every background delivery starts with `ki-plan`.

**Query:** Which order does the lane follow?

**Options:** a) (recommended, confidence high - it makes the tests trustworthy before more delivery, and keeps the screen work in one sitting) Plan and deliver [KI-TOOL-RIG-CORE-063 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/735a8e8560f951afeaa0194df52c5dffa26a3797/docs/roadmap/KI-TOOL-RIG-CORE-063-fatal-bats-assertions.md) in the background now, then plan [KI-TOOL-RIG-CORE-062](https://github.com/knowledgeislands/tools-rig/blob/223ba459/docs/roadmap/KI-TOOL-RIG-CORE-062-own-address-firewall-destination.md) and [KI-TOOL-RIG-CLI-027](https://github.com/knowledgeislands/tools-rig/blob/4ca939fa230b3e9eb02d9a170491a544a51b3651/docs/roadmap/KI-TOOL-RIG-CLI-027-command-line-convention-departures.mdCLI-027). Kris takes all of Wave 0 at the next sol session, after [PERSONAL-DOTFILES-UE-091 (pruned)](https://github.com/krisb/dotfiles/blob/28e0091bc70ae0245cc24827fa5953cedb35cf93/docs/roadmap/KB-DOTFILES-UE-091-shared-dock-tool-links.md) has landed. b) Put capability first: plan [KI-TOOL-RIG-CORE-053](https://github.com/knowledgeislands/tools-rig/blob/223ba459/docs/roadmap/KI-TOOL-RIG-CORE-053-macos-menu-bar-declarations.md) now that it is unblocked, ahead of the Wave 1 debt. c) Hold the lane until Wave 0 is accepted, so nothing builds on unaccepted work.
