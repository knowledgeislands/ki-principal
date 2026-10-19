---
note_type: stream-roadmap
id: KI-PRINCIPAL-GOV-035
area: GOV
title: Turn the Techne Programme Hold into a focus rule
kind: deliver
purpose: governance
theme: techne
component: governance
tags:
  - topic/knowledge-islands
  - topic/techne
status: ready
horizon: now
priority: high
size: m
blocks: []
blocked_by: []
baseline_ref: null
created_at: 2026-10-19T22:48:36Z
updated_at: 2026-10-19T23:10:00Z
---

# Turn the Techne Programme Hold into a Focus Rule

## Goal

Replace the [[Techne Programme Hold]] with a focus rule: Techné builds and runs the agent host and the Mac Studio only, keeps every other piece of work as an idea, and keeps the operating bounds the hold's exemption set. Rewrite [[GDR-KI-PRINCIPAL-004-standing-agent-host-exemption-from-the-techne-programme-hold|GDR-KI-PRINCIPAL-004]] to record the focus in place of the exemption.

## Context

On 14 October Kris said, in a session routed to Acquire intake: "the hold is gone, but for now we're only focusing on setting up and running the Mac Studio and the agent host, and that any other pieces of work are not something that we're building as part of Techné just now [...] keep them as ideas". On 19 October Kris answered TECHNE-FOCUS a): revise the policy through the [[Admin/Operations/Processes/Enactment Process|Enactment Process]] into a focus rule, Mac Studio and agent host only, with all other Techné work kept as ideas and the hold's operating bounds carried forward. Kris approves the exact wording before anything canonical changes.

The hold today restricts every remote agent run and every act of remote-environment management until three prerequisites are evidenced, and carries one standing exemption for the agent host `ki-techne-agent-host` and the Mac Studio `sol`. It permits local Techné tool-building generally. The focus rule reverses that shape: no general restriction on remote operation, but active Techné work narrowed to the two hosts, locally and remotely.

The decision keeps its identifier. `ki-decision-records` keeps Decision Records as living present-state records edited in place, with no supersession chain, and serials contiguous; and the live agent-host resources carry `ki-authority=GDR-KI-PRINCIPAL-004` as an AWS tag, set by the `ki-techne-harness` stack, `provision.sh`, the `agent-host` recipe and its checks. Keeping the identifier leaves those tags true with no remote change. The record is retitled, so its filename changes and every citation moves with it.

## Approval

On 20 October Kris answered TECHNE-WORDING a) in these words: "Let's get on with the technique word in, yes." ("technique word in" is speech-to-text for "Techné wording".) That approves both texts below exactly as drafted, and with them the retirement of the two readiness gates, the review-to-live-main and recovery prerequisite and the Paperclip capability review, and the `Idea:` storage rule.

## Current state

The policy is `Admin/Governance/Policies/Techne Programme Hold.md` and the decision is `GDR-KI-PRINCIPAL-004-standing-agent-host-exemption-from-the-techne-programme-hold.md`, both as they stand at `49849f87`. About forty live notes in this island cite one or the other by name, path or wikilink.

## Boundary

- Changes the policy note and GDR-KI-PRINCIPAL-004 to the wording below, once Kris approves it, and sweeps the citations in this island.
- Grants nothing beyond the bounds below. Running agents unattended or on a schedule stays outside them.
- No remote operation: no change to the agent host, the Mac Studio, the controller instance, AWS tags or the tailnet.
- Other repositories' references are handed off, not edited from here.

## Proposed wording

### Policy

The note is renamed from `Techne Programme Hold.md` to `Techne Programme Focus.md` in `Admin/Governance/Policies/`.

```markdown
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
```

### Decision Record

GDR-KI-PRINCIPAL-004 is rewritten in place and renamed to `GDR-KI-PRINCIPAL-004-techne-focus-on-the-agent-host-and-the-mac-studio.md`.

```markdown
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
```

## Steps

- [x] Kris approves the policy and Decision Record wording above, or the changes to it. Approved as drafted on 20 October; see Approval.
- [ ] Rename and rewrite the policy note; rename and rewrite GDR-KI-PRINCIPAL-004, updating its `Decisions.md` entry.
- [ ] Sweep this island's citations of the hold and of GDR-KI-PRINCIPAL-004's old filename: root `README.md` and `AGENTS.md` (the Techné programme hold section becomes a focus section); `Admin/Admin.md`, `Admin/MEMORY.md`, `Governance.md`, the Charter, Known Lands and `Policies.md`; the Agent Host Prototype Rollout note and its diagram; ADR-KI-PRINCIPAL-003, ADR-KI-PRINCIPAL-006, ADR-KI-PRINCIPAL-007 and ODR-KI-PRINCIPAL-001; the `Pillars/Technē`, `Pillars/Engineering Practice` and Emerging Concepts notes that cite it, and the Great Library of Arcadia note; and the Techne theme page and the Project notes that cite it.
- [ ] Record each piece of Techné work kept as an idea as an `Idea:` line on its Project note or the Techne theme page.
- [ ] Hand off to `ki-techne-harness` and `tools-techne` the update of their `README.md`, `AGENTS.md`, guides and roadmap records that cite the hold; the `ki-authority` tag value stays as it is.
- [ ] Audit with `ki-decision-records` and `ki-repo-kb` and review the result against this record.

## Files touched

- `Admin/Governance/Policies/Techne Programme Hold.md`, renamed to `Techne Programme Focus.md`, and `Policies.md`.
- `Admin/Governance/Decisions/GDR-KI-PRINCIPAL-004-*.md`, renamed, and `Decisions.md`.
- The citing notes the sweep step lists, in `README.md`, `AGENTS.md`, `Admin/`, `Pillars/` and `Streams/Themes/` and `Streams/Projects/`.

## Verify

- No live note outside `+/`, `-/` and this record cites `Techne Programme Hold` as a note or `standing-agent-host-exemption` as a file name; each surviving mention of the hold is historical.
- Every wikilink and Markdown link to the two renamed files resolves.
- `ki repo audit` for `ki-decision-records`, `ki-repo-kb` and `ki-repo-kb-streams` reports no new failure or warning.
- The two canonical texts match the approved wording, with only the placeholders filled.

## Dependencies / blocks

None. The follow-ups in `ki-techne-harness` and `tools-techne` are handed off and do not block acceptance.

## Discussion

- **Identifier.** Rewriting GDR-KI-PRINCIPAL-004 in place, rather than writing a new record that supersedes it, follows `ki-decision-records` and keeps the live AWS tag `ki-authority=GDR-KI-PRINCIPAL-004` true. A new record would mean removing GDR-KI-PRINCIPAL-004, renumbering GDR-KI-PRINCIPAL-005 to GDR-KI-PRINCIPAL-016 and retagging live resources, which is a remote operation.
- **Prerequisites.** The hold's three prerequisites retire as general gates. The third, a remote-delivery policy, survives as a condition on taking up any remote idea; the first two, the review-to-live-main cycle and the Paperclip review, return only if that decision asks for them.
- **Local building.** The hold allowed local Techné tool-building generally; Kris's words narrow active building to the two hosts. Keeping both repositories building and current is upkeep, not new work.
- **Host name.** The hold names the agent host `ki-techne-agent-host`; the `ki-techne-harness` operator guide, stack checks and Hosts, Roles and Layers now name it `vega`, with the same `ki-agent-host-id=agent-host` tag. The draft uses `vega`.
- **Rename.** The retired `ki-techne-principal` is archived read-only and its pointer to the hold's old path cannot be updated; the pinned Provenance link keeps the old wording readable.
- **Projects.** The `agent-host` Project outcome and the Techne theme direction both name the hold; they are rewritten in the sweep. The on-hold Paperclip capture-and-rebuild package is consistent with its work being kept as an idea.

## Governance

This roadmap record adheres to the [[Admin/Operations/Processes/Enactment Process|Enactment Process]]. Move content to `Admin/`, `Pillars/`, or `Resources/` only on user approval of a `ready` record.
