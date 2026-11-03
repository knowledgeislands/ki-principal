---
note_type: streams/project
slug: agora
title: Agora
outcome: Each rig runs Agora, the always-on place where a person's territories meet - presence, messages and change notices between rigs, level checkouts, run-once jobs and woken workers - with Git staying the record, so threads only do their package's work.
theme: techne
lifecycle: planned
lead: Kris Brown
target: null
updated: 2026-11-03T22:51:16Z
author: Written with Claude
---

# Agora

## Outcome

Agora is a small menu-bar app on each rig, kept in [`apps-agora.local`](https://github.com/knowledgeislands/apps-agora.local). It knows which rigs are in the group and present, which territories each carries, and when a watched work package has news; it keeps clean checkouts level by fast-forward only and wakes workers through `ki agent`. Listening, syncing and state-keeping move out of the threads into Agora, which writes to Git only to fetch and fast-forward and never edits knowledge. The test: a thread on any rig, reached by voice or text, wakes and acts on news without polling.

Kris opened this Project on 3 November 2026 (AGORA-PROJECT), relayed by personal.reg.assistant-sol: Agora gets its own coordinating thread "focused on the Agora ... so it can carry on, get on with what it needs to get on with". It takes over assistant-sol's `agora` focus.

This Project sits in [Techne](../Themes/techne.md).

---

## Notes

- **Agent host.** Agora is the host agent: one runs on each rig, sol and terra now and `vega` once it joins, which realises much of what [agent-host](agent-host.md) asks of a host's always-on presence. The two stay separate Projects: agent-host owns the `vega` recipe and bindings in the Techne products and is on hold, while Agora is an app in its own repository that runs on every rig, workstations included. Folding would put a live app under an on-hold host recipe, so this Project relates to agent-host rather than absorbing it.
- **Focus.** The [Techne Programme Focus](<../../Admin/Governance/Policies/Techne Programme Focus.md>) narrows work in `ki-techne-harness` and `tools-techne` to the agent host and the Mac Studio; Agora lives in neither, and runs on the Mac Studio within its bounds. How Agora waking workers fits the focus's bound of sessions the binding owner opens is a question for the Project's first Summary.
- **Install.** The households install and update Agora on each rig under AGORA-INSTALL-GRANT; this Project builds and releases it.
- **Design.** The design note `host-agent.md` in krisb/assistant, under personal.reg.assistant-sol's `agora` folder, holds the design as decided in outline in November 2026.
