---
note_type: streams/theme
slug: techne
title: Techne
direction: Take hosts to ready, move agent work into a governed Techne footprint and make the agent fleet useful, within the Techne Programme Hold.
updated: 2026-10-18T03:32:46Z
author: Written with Claude
---

# Techne

## Direction

Techne is a theme because taking a host to ready and running agents on it is one concern, whatever the host: its base (provisioning, patching, identity, secrets delivery, the operator user and lifecycle) and its workspace (the repository set, `ki bootstrap` and working rules, through `ki`). [[Themes/rig|Rig]] then applies the host's role, and the shared toolchain belongs to [[Themes/foundations|Foundations]]. Techne also moves agent work into a governed footprint and makes the agent fleet deliver reviewed work.

What matters is that remote work stays governed. The [[Techne Programme Hold]] bounds what may run remotely, and remote delivery needs its own repository-owned policy. Knowledge Islands Principal owns the engineering decisions, while `ki-techne-harness` and `tools-techne` own their implementation.

The `agent-host` recipe is the AWS base for a remote agentic rig. `vega` stays on Ubuntu LTS, for its security-only update channel, Livepatch and ready-made images. The appliance role has no recipe until the hold is reshaped.

[[Hosts, Roles and Layers]] explains the layers and roles in plain language.

---

## Notes

- There is no projectless upkeep and no recurring Activity.
