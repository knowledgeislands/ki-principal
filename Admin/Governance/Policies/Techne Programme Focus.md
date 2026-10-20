---
note_type: admin/governance/policy
updated: 2026-10-19T23:16:23Z
author: AI-assisted
---

# Techne Programme Focus

## Authority

Knowledge Islands Principal sets the focus of the Techné programme across its independent harness and CLI products, `ki-techne-harness` and `tools-techne`. The island owner is the accountable human owner of this rule and changes it only through the [Enactment Process](<../../Operations/Processes/Enactment Process.md>). [GDR-KI-PRINCIPAL-004](../Decisions/GDR-KI-PRINCIPAL-004-techne-focus-on-the-agent-host-and-the-mac-studio.md) records the decision.

## Focus

Techné carries no programme hold. For now it builds and runs two things only, under the operating bounds below:

- **The agent host.** The single cloud agent host `vega`.
- **The Mac Studio.** The island owner's Mac Studio workstation, reached over the tailnet as `sol`, as an owned remote agent host.

Every other piece of Techné work is kept as an idea: remote Paperclip in any form; Kitteth and any Avatar; Telegram and every other messaging channel; wider K3s or controller changes; the execution fabric; and every other environment. An idea is kept as an `Idea:` line on its Project note or theme page, not as a work record, and is neither built nor run. Taking one up needs the island owner's decision through the Enactment Process, which sets its bounds; for an idea that runs agents remotely or manages a remote environment, that record also settles its remote-delivery policy: destination, visibility, review, integration, synchronisation and recovery.

Local work in `ki-techne-harness` and `tools-techne` serves the two hosts. Both repositories stay building and current with their declared KI repository, engineering and tool-building standards, keeping their lint, typecheck, test, build, package and governance checks passing; ordinary hosted CI that exercises isolated build and test paths continues. Read-only inspection of other remote services continues under normal access and secret-handling rules.

## Operating bounds

- **Agent host scope.** Setting up and operating `vega`, the EC2 instance tagged `ki-agent-host-id=agent-host` in the Techne account `655383751458` in `eu-west-1`, properly and durably: building, rebuilding or replacing that one host through the `ki-techne-harness` stack; its rerunnable workspace setup, updates and status; its operator commands in the `techne` CLI, acting only on that host; its account-local operator role, its `/ki/techne/agent-host/` parameters, its tailnet tag and policy entries; and rotating its credentials.
- **Mac Studio scope.** Bootstrapping and maintaining the Mac Studio, running its tailnet daemon and tailnet entries, administering it remotely over Tailscale SSH and Screen Sharing, and running agents on it. It has no stack, account, parameters or operator role, nothing in the Techne account reaches it, and its identities are its owner's own. Its disk is encrypted at rest, so after a restart it stays unreachable until unlocked in person.
- **Hosts.** Exactly one cloud host, separate from the controller instance, and the one owned host. No public inbound access; the binding owner reaches each with Tailscale SSH.
- **Sessions.** Agents run on either host only in sessions the binding owner opens, with no unattended or scheduled agents. Agents keep the local rules: explicit-path commits, no push unless the binding owner asks, no prune and no acceptance.
- **Access.** The binding owner is the person whose `agent-host` binding operates the host. Building, rebuilding and tearing down the agent host use the binding owner's administrator session in the Techne account; day-to-day operation (start, stop and status) uses the host's account-local operator role. No agent creates access or holds AWS credentials of its own. Each host's GitHub token and Claude login are the binding owner's own identities, because only the binding owner opens sessions there; a machine identity is decided only when unattended agents are taken up.
- **Kill switch.** For the agent host, stopping it with its operator role and removing its tailnet device; for the Mac Studio, ending agent sessions and stopping its tailnet daemon. Both stay documented and available.
- **Teardown.** For the agent host, withdrawing it through the binding owner's administrator session and removing its tailnet device; for the Mac Studio, removing agent credentials and its tailnet node without wiping the workstation. Both stay documented and available.
- **Other remote services.** No change to existing remote services, including the controller instance `ki-techne-ops-007-primary`, its stack and its Telegram dispatch path, and nothing in the organisation or its management account. The agent host carries only its own tags, so its operator role cannot reach the controller.

[Agent Host Prototype Rollout](<Agent Host Prototype Rollout.md>) illustrates the kill switch and teardown.

## Term

The rule has no automatic lapse and no fixed review date. It stands until the island owner changes it through the Enactment Process.

## Retired Techné principal

The former `knowledgeislands/ki-techne-principal` was retired on 4 October 2026 and is archived read-only; its snapshots, closed work records, frozen ledger and preserved candidate branches remain readable there as historical evidence. Its candidates for remote agent working-style work, `0f77071572aa649a936be3069f635ab8ea721858` and `eb7292a1f1bd515fcb7c44715caac48bfe5770ad`, were never accepted; any later use must be captured afresh by an owning repository. [Engineering Practice](<../../../Pillars/Engineering Practice/Engineering Practice.md>) owns Techné's canonical engineering knowledge.

## Provenance

This rule replaced the Techne Programme Hold through [KI-PRINCIPAL-GOV-035](https://github.com/knowledgeislands/ki-principal/blob/ee568843/Streams/Roadmap/KI-PRINCIPAL-GOV-035-turn-the-techne-programme-hold-into-a-focus-rule.md). The hold as it last stood is preserved in [Techne Programme Hold](https://github.com/knowledgeislands/ki-principal/blob/49849f87/Admin/Governance/Policies/Techne%20Programme%20Hold.md), and the broader original hold in [the source instruction](https://github.com/knowledgeislands/ki-techne-principal/blob/b25e9c950fd87715d12f76b69bb2079c3a4fc054/AGENTS.md#techne-holding-position).
