---
id: ki.sop.main
level: territory
covers:
  - ki.prj.agent-host
  - ki.prj.baseline-rollout
  - ki.prj.chezmoi
  - ki.prj.estate-factorisation
  - ki.prj.knowledge-acquisition
  - ki.prj.mac-studio-setup
  - ki.prj.observatory
  - ki.prj.paperclip-capture-and-rebuild
  - ki.prj.portable-specifications
  - ki.prj.timelines
  - ki.prj.tools-burndown
  - ki.prj.ways-of-working
  - ki.prj.website
title: 'KI > SoP'
theme: null
description: >-
  State of play, the territory's single dispatch coordinator: routes each new unit of work to one work, keeps the
  Project-work queue and coordinates continual improvement of the method, executing nothing. Takes units with no
  clear owner, method improvements and Project-work queueing. Not for executing any Project's work (ki.<project>),
  method design itself (ki.prj.ways-of-working) or recurring and ad hoc work (ki.regular).
worker: agent
supervisor: owner
created_at: 2026-10-06T21:07:00Z
---

# ki.sop.main

## Goals

- Coordinate the Knowledge Islands territory the [Charter](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Charter.md) declares, as its State of play: the coordinator of the coordinators, executing nothing.
- Route every new unit of work with no clear owner to one work, once, so that nothing bounces between works.
- Keep the ordered Project-work queue and its cap, opening Project work in turn.
- Coordinate every work's continual improvement of the method, routing method changes to ki.prj.ways-of-working while it exists (STEWARD-HOME).

## Scope

- In: owner dumps, handoffs with no owning work, cross-work items whose owner is unclear, `METHOD` lines and other method improvements, the Project-work queue and cap, territory-wide dated reviews of held records, and route lines into each work's `messages.md`.
- Out: executing any Project's work (ki.prj.baseline-rollout, ki.prj.chezmoi, ki.prj.knowledge-acquisition, ki.prj.mac-studio-setup, ki.prj.observatory, ki.prj.portable-specifications, ki.prj.timelines, ki.prj.tools-burndown, ki.prj.ways-of-working); recurring and ad hoc work (ki.regular.main, ki.regular.registry-removal); method design (ki.prj.ways-of-working); `ki.sop.main work status` and tools-ki (ki.prj.tools-burndown); units that already have an owner, which go to it direct.
