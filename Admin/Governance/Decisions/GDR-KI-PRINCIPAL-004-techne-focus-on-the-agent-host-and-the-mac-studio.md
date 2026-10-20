---
note_type: admin/governance/decision
id: GDR-KI-PRINCIPAL-004
title: 'Techne focus on the agent host and the Mac Studio'
date: 2026-10-20
updated: 2026-10-20
status: current
decision_type_url: https://knowledgeislands.info/specifications/decision-records/gdr
decision_type: governance
decision_depends_on: ['SDR-KI-PRINCIPAL-004']
---

# GDR-KI-PRINCIPAL-004: Techne focus on the agent host and the Mac Studio

## Context

Techné spans two products, the `ki-techne-harness` harness and the `tools-techne` CLI, and a wider set of possible work: remote Paperclip, Kitteth and Avatars, messaging channels, the execution fabric, K3s and further environments. The island owner needs remotely reachable agent environments now, because connectivity is poor at times and the laptop is swap-bound under its local load, and has capacity to build only those.

Two hosts meet that need. The agent host `vega` is a single EC2 instance in the Techne account, separate from the controller instance `ki-techne-ops-007-primary`, which runs a Telegram dispatcher and busybox-only K3s Jobs, has little headroom and serves a different purpose. The Mac Studio is the island owner's own workstation, reached over the tailnet as `sol`, with more headroom than the laptop.

## Decision

Techné carries no programme hold. It focuses on the agent host and the Mac Studio, and keeps everything else as ideas.

- **Focus.** Techné builds and runs the agent host and the Mac Studio only: setting each up properly and durably, operating it and running agents on it. Local work in `ki-techne-harness` and `tools-techne` serves the two hosts, and both repositories stay building and current with their declared standards.
- **Ideas.** Every other piece of Techné work is kept as an idea, not a work record, and is neither built nor run. Taking one up needs the island owner's decision through the Enactment Process, which sets its bounds and, for remote work, its remote-delivery policy.
- **Hosts.** Exactly one cloud host, separate from the controller instance, and the one owned host, with no public inbound access, reached by the binding owner over Tailscale SSH. The Mac Studio has no stack, account, parameters or operator role, and its identities are its owner's own.
- **Sessions.** Agents run only in sessions the binding owner opens; no agent runs unattended or on a schedule. Agents commit with explicit paths, push only when the binding owner asks, and never prune or accept.
- **Access.** Building, rebuilding and tearing down the agent host use the binding owner's administrator session in the Techne account; day-to-day operation uses the host's account-local operator role. No agent creates access or holds AWS credentials of its own. Each host's GitHub token and Claude login are the binding owner's own; a machine identity is decided only when unattended agents are taken up.
- **Kill switch and teardown.** Each host keeps a documented kill switch and teardown. The Mac Studio's teardown removes agent credentials and its tailnet node without wiping the workstation.
- **Other remote services.** No change to existing remote services, including the controller instance, its stack and its Telegram dispatch path, and nothing in the organisation or its management account.
- **Term.** The focus has no automatic lapse and no fixed review date. It stands until the island owner changes it through the Enactment Process.

## Consequences

- Agent work runs on the two hosts, which can be built, rebuilt and maintained properly. Nothing else is built until the island owner takes it up.
- Remote work beyond the two hosts needs no general prerequisites, but each piece needs its own Enactment decision and remote-delivery policy before it starts.
- The host build and workspace management in `ki-techne-harness`, the operator commands in `tools-techne` and the operator tooling in the binding owner's chezmoi source proceed as work in those repositories. None gains authority beyond these bounds.
- The agent host's resources carry `ki-authority=GDR-KI-PRINCIPAL-004`. The controller instance keeps its name, tags and dispatch path, and the operator role cannot reach it.
- A standing cost for the second instance continues while the agent host stands. Retiring a host means its teardown.
- The Mac Studio's setup proceeds as the `mac-studio-setup` Project. Its role as a workstation is unchanged; the focus adds remote agent use and remote administration only.

## References

- [SDR-KI-PRINCIPAL-004](SDR-KI-PRINCIPAL-004-the-enactment-process.md) - the Enactment Process through which the focus is changed.
