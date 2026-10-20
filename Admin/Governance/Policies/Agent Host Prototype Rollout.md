---
note_type: admin/governance/policy
updated: 2026-10-19T23:16:23Z
author: AI-assisted
---

# Agent Host Prototype Rollout

## Overview

This diagram shows the order in which the limited remote agent prototype comes into use, and how it stops. It shows the gates through which the agent host came into use under the exemption the Techne Programme Hold then carried, as [KI-PRINCIPAL-GOV-020](https://github.com/knowledgeislands/ki-principal/blob/fddfca69b4642cb4db4113123aa7dc613c3e92f4/Streams/Roadmap/KI-ARCADIA-GOV-020-limited-remote-agent-prototype.md) defined them, and the kill switch and teardown the [Techne Programme Focus](<Techne Programme Focus.md>) keeps, which [GDR-KI-PRINCIPAL-004](../Decisions/GDR-KI-PRINCIPAL-004-techne-focus-on-the-agent-host-and-the-mac-studio.md) records. It illustrates the policy; where they differ, the focus rule and the Decision Record govern.

![Agent Host Prototype Rollout.svg](<Agent Host Prototype Rollout.svg>)

---

## Governance

Kris accepted the prototype's bounds on 7 October 2026, and the hold was then amended through [GDR-KI-PRINCIPAL-004](../Decisions/GDR-KI-PRINCIPAL-004-techne-focus-on-the-agent-host-and-the-mac-studio.md). That amendment was the gate for every remote step: no remote action, including creating the host or testing a connection, preceded it. On 20 October 2026 the [Techne Programme Focus](<Techne Programme Focus.md>) replaced the hold, carrying the same operating bounds forward, and GDR-KI-PRINCIPAL-004 now records the focus.

## Access and build

Every step in this lane is Kris's alone. The operator role, `ki-techne-agent-host-operator`, is an account-local IAM role in the Techne account. The tailnet policy and a single-use, tagged auth key follow; Kris stores the key in Parameter Store from the clipboard without echoing it, then builds the host with the `ki-techne-harness` provisioning script under the `knowledge-islands-techne` profile. On boot the host joins the tailnet. No agent creates access or uses AWS credentials of its own.

## First use, then work

Kris connects from Zed through the helper, approves the Claude Code login on the Mac and stores a fine-grained GitHub token that expires after 90 days. Only then does agent work begin: editing, committing and auditing in a session Kris opens, with no push unless Kris asks. The GitHub token and Claude login are the binding owner's own identities, because only the binding owner opens sessions there.

## Stop, change or withdraw

The kill switch is available at any time: stop the host with the agent-host profile and remove its tailnet device. The focus has no automatic lapse and no fixed review date: it stands until the island owner changes it through an Enactment record. The prototype review, [KI-PRINCIPAL-GOV-021](https://github.com/knowledgeislands/ki-principal/blob/fac82de591fa6b7fc9bdf711c50dde9d55399a69/Streams/Roadmap/KI-ARCADIA-GOV-021-review-the-agent-host-prototype.md), kept the host as it stood. Only if the island owner retires the host does teardown remove the stack under the admin profile, then the tailnet entries, the tokens and the operator role. Rotating the GitHub token before it expires is part of operating the host.

## Source

The SVG is exported from the Archify source [beside it](<Agent Host Prototype Rollout.archify.json>). To change the diagram, edit the source, run Archify's `finalize` for a `workflow` diagram at `showcase` quality, then export the SVG from the rendered viewer. The rendered HTML is a working file and is not kept.

Return to [Policies](Policies.md).
