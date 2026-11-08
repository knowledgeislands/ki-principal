---
role: governor
id: ki.sop.main
level: territory
covers:
  - ki.prj.agent-host
  - ki.reg.agora
  - ki.prj.baseline-rollout
  - ki.prj.chezmoi
  - ki.prj.estate-factorisation
  - ki.prj.knowledge-acquisition
  - ki.prj.mac-studio-setup
  - ki.prj.observatory
  - ki.prj.orca-evaluation
  - ki.prj.paperclip-capture-and-rebuild
  - ki.prj.portable-specifications
  - ki.prj.stoa
  - ki.prj.timelines
  - ki.prj.ways-of-working
  - ki.prj.website
  - ki.reg.guilds
  - ki.reg.main
title: 'KI > SoP'
theme: null
description: >-
  State of play, the territory's single dispatch coordinator: routes each new unit of work to one work, keeps the
  Project-work queue and coordinates continual improvement of the method, executing nothing. Takes units with no
  clear owner, method improvements and Project-work queueing. Not for executing any Project's work (ki.prj.<project>),
  method and guild work (ki.reg.guilds) or recurring and ad hoc work (ki.reg.main).
worker: agent
supervisor: owner
created_at: 2026-10-06T21:07:00Z
---

# ki.sop.main

> **Moved.** Since 9 November 2026 this package lives in the Agora store, `krisb/ki-agora-store`, at `work/ki/ki.sop.main/`, and is edited only there (WP-STORE). This copy stays only so that `ki` and the hooks can still find it.

## Goals

- Coordinate the Knowledge Islands territory the [Charter](/Users/krisbrown/kis/knowledge-islands/ki-principal/Admin/Governance/Charter.md) declares, as its State of play: the coordinator of the coordinators, executing nothing.
- Route every new unit of work with no clear owner to one work, once, so that nothing bounces between works.
- Keep the ordered Project-work queue and its cap, opening Project work in turn.
- Coordinate every work's continual improvement of the method, routing method changes to ki.reg.guilds (RENAME-GUILDS).

## Scope

- In: owner dumps, handoffs with no owning work, cross-work items whose owner is unclear, `METHOD` lines and other method improvements, the Project-work queue and cap, territory-wide dated reviews of held records, and route lines into each work's `messages.md`.
- Out: executing any Project's work (ki.prj.baseline-rollout, ki.prj.chezmoi, ki.prj.knowledge-acquisition, ki.prj.mac-studio-setup, ki.prj.observatory, ki.prj.portable-specifications, ki.prj.timelines, ki.prj.tools-burndown, ki.prj.ways-of-working); recurring and ad hoc work (ki.reg.main); method design and guild work (ki.reg.guilds); tools-ki (ki.prj.tools-burndown); units that already have an owner, which go to it direct.
- Members homed elsewhere: [ki.reg.guilds](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/+/_WORK/ki.reg.guilds/work.md), member-homed in ki-agentic-harness, as Kris set under OPEN-GUILD and RENAME-GUILDS on 6 November 2026.

## Focus

1. `acceptance` — acceptance questions on delivered records across the territory.
2. `chain` — the `mgit chain` command and its acceptance.
3. `themes`⭐ — the territory's theme map, routing and overlaps, and theme registries.
4. `_emerging` — anything outside the others.
