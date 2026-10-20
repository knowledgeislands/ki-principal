---
note_type: streams/theme
slug: techne
title: Techne
direction: Take the agent host and the Mac Studio to ready and run governed agent work on them, within the Techne Programme Focus.
updated: 2026-10-19T23:16:23Z
author: Written with Claude
---

# Techne

## Direction

Techne is a theme because taking a host to ready and running agents on it is one concern, whatever the host: its base (provisioning, patching, identity, secrets delivery, the operator user and lifecycle) and its workspace (the repository set, `ki bootstrap` and working rules, through `ki`). [Rig](rig.md) then applies the host's role, and the shared toolchain belongs to [Foundations](foundations.md). Techne also moves agent work into a governed footprint and makes the agent fleet deliver reviewed work.

What matters is that remote work stays governed. The [Techne Programme Focus](<../../Admin/Governance/Policies/Techne Programme Focus.md>) narrows Techné to the agent host `vega` and the Mac Studio `sol`, within its operating bounds, and keeps every other piece of Techné work as an idea. Taking an idea up needs the island owner's decision through the Enactment Process, and a remote idea also needs its own remote-delivery policy. Knowledge Islands Principal owns the engineering decisions, while `ki-techne-harness` and `tools-techne` own their implementation.

The `agent-host` recipe is the AWS base for a remote agentic rig. `vega` stays on Ubuntu LTS, for its security-only update channel, Livepatch and ready-made images. The appliance role has no recipe while it stays an idea.

[Hosts, Roles and Layers](<../../Pillars/Engineering Practice/Architecture/Hosts, Roles and Layers.md>) explains the layers and roles in plain language.

---

## Notes

- There is no projectless upkeep and no recurring Activity.
- **Ideas under the focus.** The [Techne Programme Focus](<../../Admin/Governance/Policies/Techne Programme Focus.md>) keeps the pieces of Techné work below as ideas, from 20 October 2026, when Kris approved the focus wording (TECHNE-WORDING a)). None is built or run; taking one up needs the island owner's decision through the Enactment Process. Remote Paperclip is kept as an idea on [paperclip-capture-and-rebuild](../Projects/paperclip-capture-and-rebuild.md).
- **Idea: Kitteth and Avatars.** Kitteth and any other Avatar holding delegated agency. The open questions about Avatar capability, events and telemetry sit in [Avatar Roles and Oversight](<../../Pillars/Philosophy/Emerging Concepts/Avatar Roles and Oversight.md>).
- **Idea: messaging channels.** Telegram and every other messaging channel for Techné agents. The controller's existing Telegram dispatch path stays as it is.
- **Idea: wider K3s and controller changes.** Any change to K3s or to the controller instance `ki-techne-ops-007-primary`, its stack and its dispatch path; the controller as a recipe is noted on [agent-host](../Projects/agent-host.md).
- **Idea: the execution fabric.** The AI Execution Fabric and its provider-neutral isolated agent execution, as [ADR-KI-PRINCIPAL-004](../../Admin/Governance/Decisions/ADR-KI-PRINCIPAL-004-provider-neutral-isolated-agent-execution.md) records.
- **Idea: other environments.** Every environment other than `vega` and `sol`, including the appliance role and anything in the organisation or its management account.
