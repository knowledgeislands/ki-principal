---
note_type: streams/project
slug: mac-studio-setup
title: Mac Studio setup
outcome: Kris's Mac Studio, unused for over a month, is back to full estate capability - chezmoi applied, Rig declarations reconciled, Homebrew `ki` and `mgit` installed, the workspace cloned and registered, and Claude Code and Zed ready to resume any thread there.
theme: rig
lifecycle: active
lead: Kris Brown
target: null
updated: 2026-10-19T23:16:23Z
author: Written with Claude
---

# Mac Studio setup

## Outcome

Kris's Mac Studio, unused for over a month, is back to full estate capability. The test: chezmoi is applied from the current source, `rig status` and `rig doctor` show the declared machine, Homebrew `ki` passes `ki doctor`, every workspace repository is cloned and in the `ki` registry, and a Claude Code or Zed thread there can resume any checkpoint in [Projects](Projects.md).

This Project sits in [Rig](../Themes/rig.md), because the Mac Studio, `sol` on the tailnet, is Kris's own hardware: Rig and chezmoi build and maintain it as Kris's rig on another machine, with the `studio` profile on `core`, declared in the chezmoi source. Techne may deploy onto it later but never owns its build recipe, and it is separate from Techne's [agent-host](agent-host.md) Project.

Under [GDR-KI-PRINCIPAL-004](../../Admin/Governance/Decisions/GDR-KI-PRINCIPAL-004-techne-focus-on-the-agent-host-and-the-mac-studio.md) it is one of the two hosts the Techne Programme Focus keeps in scope, as a remote agent host: agents administer it over Tailscale and SSH, with Kris approving each step.

---

## Notes

- The bootstrap is delivered: chezmoi applied on `sol`, Rig declarations reconciled, the released `ki` installed and passing `ki doctor`, and agents can reach `sol` over Tailscale and SSH, with GitHub through agent forwarding.
- **Remaining: a restart test.** FileVault is on, so a reboot leaves `sol` offline until Kris unlocks it in person. Kris restarts it, no earlier than Monday evening 2026-10-12, and the Project stays open until Tailscale is proven to relaunch and reconnect after the unlock.
- 1Password-backed chezmoi targets render only at `sol`'s screen, so Kris applies those there.
- Follow-ups are handed on and none blocks this Project: software removal, Dock items, self-updating apps, undeclared software decisions and the later workstation items to [Rig](../Themes/rig.md); tolerating missing template tools to the chezmoi thread; rendering `.zshenv` on the agent host to chezmoi's roadmap under [agent-host](agent-host.md).
- [Hosts, Roles and Layers](<../../Pillars/Engineering Practice/Architecture/Hosts, Roles and Layers.md>) names the estate's machines - `vega`, `sol` and `terra` - and their machine types, from which the Rig profiles and the Cheztoi host profile take their names.
- **Idea: remote access and continuity in Rig.** A Rig profile could declare whether its machines accept screen sessions and who may connect, and on macOS Handoff (with Universal Clipboard) and Universal Control; `rig doctor` would report drift, `rig apply` set what macOS allows without the GUI, and Rig show the manual steps for the rest. Findings so far: recent macOS restricts enabling Screen Sharing from a script; Handoff and Universal Control are per-user preferences whose `defaults` keys need confirming; on Linux, GNOME Remote Desktop (`grdctl`) or xrdp. Today `sol` has Screen Sharing on and `terra` off, set by hand as the chezmoi source's macOS workstation guide describes; restricting listeners to the tailnet stays with the Rig firewall work. Kept as an idea on 2026-10-14 in place of a cancelled work record.
- **Rig note: shared-failure reporting (R2).** On `sol`, `rig upgrade` reported one shared cause, Command Line Tools older than macOS, as 84 separate failures; it showed an app Kris had deleted by hand as "failed" rather than missing; and a hand-run upgrade left no receipt to read afterwards. Rig's `apply` and `upgrade` could stop or collapse when a provider fails the same way for every item, report a removed declared app as missing, and keep a receipt for interactive runs. Kept as a note on Kris's approval of 2026-10-14; Rig's own roadmap holds any work on error reporting and receipts.
- **Rig note: PATH shadowing check (R4).** On `sol`, an old mise `claude` shim, from a global npm package in an inactive Node, came first on PATH ahead of Homebrew's `claude`. `rig doctor` could warn when another PATH entry shadows a declared tool's executable. Pruning old runtimes stays with the chezmoi source. Kept as a note on the same approval; Rig's own roadmap holds any work on runtime tooling.
- **Rig difference: GitHub Desktop's repository list.** GitHub Desktop keeps its repository list in an app database, so chezmoi cannot declare it, and on `sol` it held stale paths from an older layout until the thread's gh-desktop run reset it by hand to the 56 territory checkouts on 2026-10-15. A Rig step that adds every mgit territory checkout through the `github` shim, add-only and pausing between opens, is captured in Rig's roadmap on Kris's approval of 2026-10-15.
- **Known World part, 2026-10-15.** On 15 October Kris placed the foundations model in [Known World](<../../Pillars/Philosophy/Emerging Concepts/Known World.md>) and gave this Project its part: building `sol` as the hub, with all eight territories checked out and the hub's service set. It depends on the territory seat table.

### Remit

Kris widened the remit on 2026-10-14 (Kris, 2026-10-14: "I want to add to this projects remit that it needs to look at the rig differences"):

- **RIG-DIFF:** compare `sol` with the laptop, read-only, across Rig profiles, tools, skill links, Dock extras and undeclared set-up such as Headroom, then settle each difference.
- **SOL-SCOPE:** `sol` manages all seven workspace groups, and joins the `ki` registry after a dry-run against the laptop's 52 entries.
- **LOCAL-MODE-CHECK:** re-run `ki dev local on` on `sol` if its `ki` configuration no longer shows in `chezmoi status`.

### Decisions in force

The decisions that still guide `sol`, the Mac Studio, as they stand. The full decisions log is the work's tracked log; its earlier machine-local copy at `~/.local/state/ki/agents/mac-studio-setup/decisions.md` matched it on 18 October and is superseded.

#### Ownership and access

- `sol` is Kris's own hardware. Rig and chezmoi build and maintain it as Kris's rig on another machine, on the `studio` profile, which builds on `core`. Techne may deploy onto it but never owns its build.
- Remote agent use of `sol` is within the Techne Programme Focus under [GDR-KI-PRINCIPAL-004](../../Admin/Governance/Decisions/GDR-KI-PRINCIPAL-004-techne-focus-on-the-agent-host-and-the-mac-studio.md). Agents administer it over Tailscale and SSH, with Kris approving each step.
- The laptop's SSH key passes through to `sol` by agent forwarding, for `sol` only, so remote sessions there can reach GitHub.
- The HNR harness stays on `sol` and in its `ki` registry.

#### Restarts and login

- Any reboot of `sol` needs Kris present, because FileVault keeps it offline until Kris unlocks it in person.
- Tailscale stays the GUI app, set to open at login. Swapping it for `tailscaled` is a later Rig item.
- 1Password-backed chezmoi targets are applied at `sol`'s screen, not over SSH.

#### Software

- One software list serves every machine: `core` holds what both Macs share, and `laptop` and `studio` add only what is particular to each.
- `sol` matches the laptop. DaVinci Resolve is the only studio-only app, and both machines use Spark Desktop in place of the old Spark.
- DaisyDisk comes from the App Store on both machines, because of its licence.
- App Store and hand-installed copies are swapped for the declared source by Kris deleting them at `sol`'s screen and running `rig apply`. Rig reports such a mismatch but never deletes anything itself.
- chezmoi always runs from the latest source; pulling it on `sol` is always fine.

#### Close

- The Project closes only after the restart test, which Kris runs at `sol` no earlier than Monday evening 2026-10-12. It stays open until Tailscale is proven to relaunch and reconnect after the unlock.

### Close-out assessment

As of 27 October 2026, the recorded bootstrap delivered chezmoi application, reconciled Rig declarations and workspace access on `sol`; subsequent machine-alignment work is recorded in the Mac Studio and chezmoi work packages. This does not prove the full Outcome: the required attended restart, unlock and Tailscale reconnect test has no confirmed completion in the evidence reviewed, and remaining machine checks and firewall work have their existing Rig and chezmoi owners. Keep the Project open, preserving the Mac Studio work's hold until Kris releases it; Kris should confirm the restart test and the remaining setup evidence through that work before deciding whether to close. The wider Rig ideas above survive independently of that decision.
