# [Knowledge Islands](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/Themes.md) › State of play › techne-focus

**🤖 → 👤 Handoff to supervisor · Run report at 23:51 BST · last mark 23:46 BST**

---

## Done

- Captured [KI-PRINCIPAL-GOV-035](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-GOV-035-turn-the-techne-programme-hold-into-a-focus-rule.md), Turn the Techne Programme Hold into a focus rule, as a draft at horizon `now`, holding the exact replacement policy wording and the rewrite of [GDR-KI-PRINCIPAL-004](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/GDR-KI-PRINCIPAL-004-standing-agent-host-exemption-from-the-techne-programme-hold.md); commits `49849f87` (identifier reserved), `6143b6b0` (record) and `ee568843` (one ambiguous link qualified); the audit scoped to the record passes.
- The issue ledger stood at GOV 033 although KI-ARCADIA-GOV-034 was issued and pruned on 9 October, so the reservation moved it to 035 rather than reusing 034.
- Nothing canonical changed: the [policy](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Policies/Techne%20Programme%20Hold.md), the GDR, the Charter and every other note are untouched. Nothing pushed.

## In Progress

Nothing is running. Delivery of KI-PRINCIPAL-GOV-035 waits on TECHNE-WORDING.

Outstanding - no action requested now:

- Follow-ups, not captured under CAPTURE-GATE: hand off to `ki-techne-harness` and `tools-techne` the update of their `README.md`, `AGENTS.md`, operator and user guides and roadmap records that cite the hold (the harness operator guide links the policy by its path on `main`, which the rename breaks); rewrite the Agent Host Prototype Rollout note, the `agent-host` Project outcome and the Techne theme direction, which all name the hold. The record's Steps already carry the in-island sweep.
- The canonical notes name the agent host `ki-techne-agent-host`, but the harness guide, stack checks and Hosts, Roles and Layers now name it `vega`; the draft uses `vega`.
- The whole-tree audit shows failures that are not this run's: GDR-KI-PRINCIPAL-014 and GDR-KI-PRINCIPAL-015 link outside the decisions collection, GDR-KI-PRINCIPAL-005 and GDR-KI-PRINCIPAL-010 cite higher-numbered GDRs, work-package schema findings across `+/_WORK/`, and an MD032 lint finding in another session's uncommitted `+/_WORK/ki.portable-specifications/decisions.md`, which I left alone.

## Queries

### TECHNE-WORDING - Approve the Techne focus policy and decision wording

**Context:** Kris answered TECHNE-FOCUS a) on 19 October, from the 14 October words "the hold is gone, but for now we're only focusing on setting up and running the Mac Studio and the agent host [...] keep them as ideas". [KI-PRINCIPAL-GOV-035](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-GOV-035-turn-the-techne-programme-hold-into-a-focus-rule.md) drafts the wording below. Four judgement calls are built in. First, the decision is rewritten in place as GDR-KI-PRINCIPAL-004 under a new title rather than as a new superseding record: `ki-decision-records` forbids supersession chains and gaps in serials, and the live agent-host AWS resources are tagged `ki-authority=GDR-KI-PRINCIPAL-004`, so a new identifier would mean renumbering GDR-KI-PRINCIPAL-005 to GDR-KI-PRINCIPAL-016 and retagging live resources. Second, the hold's three prerequisites retire as general gates; the remote-delivery policy survives as a condition on taking up any remote idea. Third, the hold allowed local Techné tool-building generally; following Kris's words, active building narrows to the two hosts, with both repositories kept building and passing their checks as upkeep. Fourth, the policy note is renamed to Techne Programme Focus; the archived `ki-techne-principal` pointer to the old path cannot be updated, and a pinned Provenance link keeps the old wording readable. All bounds carry forward: one cloud host and the Mac Studio, no public inbound, Tailscale SSH, owner-opened sessions only, the access rules, kill switch, teardown, and no change to the controller or other remote services. Delivery fills `<delivery time>`, `<delivery date>` and `<delivery link>`.

The policy, as `Admin/Governance/Policies/Techne Programme Focus.md`:

````markdown
---
note_type: admin/governance/policy
updated: <delivery time>
author: AI-assisted
---

# Techne Programme Focus

## Authority

Knowledge Islands Principal sets the focus of the Techné programme across its independent harness and CLI products, `ki-techne-harness` and `tools-techne`. The island owner is the accountable human owner of this rule and changes it only through the [[Admin/Operations/Processes/Enactment Process|Enactment Process]]. [[GDR-KI-PRINCIPAL-004-techne-focus-on-the-agent-host-and-the-mac-studio|GDR-KI-PRINCIPAL-004]] records the decision.

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

[[Agent Host Prototype Rollout]] illustrates the kill switch and teardown.

## Term

The rule has no automatic lapse and no fixed review date. It stands until the island owner changes it through the Enactment Process.

## Retired Techné principal

The former `knowledgeislands/ki-techne-principal` was retired on 4 October 2026 and is archived read-only; its snapshots, closed work records, frozen ledger and preserved candidate branches remain readable there as historical evidence. Its candidates for remote agent working-style work, `0f77071572aa649a936be3069f635ab8ea721858` and `eb7292a1f1bd515fcb7c44715caac48bfe5770ad`, were never accepted; any later use must be captured afresh by an owning repository. [[Engineering Practice/Engineering Practice|Engineering Practice]] owns Techné's canonical engineering knowledge.

## Provenance

This rule replaced the Techne Programme Hold through [KI-PRINCIPAL-GOV-035](<delivery link>). The hold as it last stood is preserved in [Techne Programme Hold](https://github.com/knowledgeislands/ki-principal/blob/49849f87/Admin/Governance/Policies/Techne%20Programme%20Hold.md), and the broader original hold in [the source instruction](https://github.com/knowledgeislands/ki-techne-principal/blob/b25e9c950fd87715d12f76b69bb2079c3a4fc054/AGENTS.md#techne-holding-position).
````

The decision, as `Admin/Governance/Decisions/GDR-KI-PRINCIPAL-004-techne-focus-on-the-agent-host-and-the-mac-studio.md`:

````markdown
---
id: GDR-KI-PRINCIPAL-004
title: 'Techne focus on the agent host and the Mac Studio'
date: <delivery date>
updated: <delivery date>
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

- [[SDR-KI-PRINCIPAL-004-the-enactment-process|SDR-KI-PRINCIPAL-004]] - the Enactment Process through which the focus is changed.
````

**Query:** Do you approve this policy and decision wording, so KI-PRINCIPAL-GOV-035 becomes ready for delivery?

**Options:**

a) (recommended, confidence medium - it follows your 14 October words and the decision-records standard, but the four judgement calls have not been blind-reviewed) Approve both as drafted; the record goes ready and delivery rewrites the policy and GDR-KI-PRINCIPAL-004 in place and sweeps this island's citations.
b) Approve with the changes you name, for example keeping the prerequisites as gates, keeping local tool-building open, or keeping the note's old name.
c) Land the decision as a new GDR-KI-PRINCIPAL-017 superseding GDR-KI-PRINCIPAL-004, accepting the renumbering of the GDR series and a retag of the live agent-host resources.

### 🤖 → 👤 Handoff to supervisor · since 23:51 BST

👤 1 with you

- [with you] TECHNE-WORDING · owner · since 23:51
- [committed] KI-PRINCIPAL-GOV-035 record and ledger reservation
- [unpushed] ki-principal, 3 commits
