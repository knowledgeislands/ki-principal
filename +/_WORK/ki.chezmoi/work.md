---
id: ki.chezmoi
level: project
title: 'KI > Rig > chezmoi'
project: chezmoi
theme: rig
description: >-
  Works the open KB-DOTFILES-UE records in the chezmoi source, keeping Kris's workstations accurate, tidy and
  observable, with every apply held for Kris's `chezmoi diff` review. Takes chezmoi source records, managed
  coverage and drift, host-local config migrations and reviewed applies on terra and sol. Not for Rig itself and
  the Mac Studio bring-up (ki.mac-studio-setup), tools-ki and tools-mgit (ki.tools-burndown) or the work model
  (ki.ways-of-working).
worker: agent
supervisor: owner
created_at: 2026-10-08T08:40:00Z
---

# ki.chezmoi

## Goals

- Deliver the [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) Project's outcome.
- Keep the chezmoi source and the live targets on terra and sol level, with no apply made before Kris has reviewed its `chezmoi diff` and approved it.
- Bring tool configuration that other work hands over, such as mgit's learnt templates and completions, into the source for Kris's review.

## Scope

- In: the chezmoi source (`~/.local/share/chezmoi`, GitHub `krisb/dotfiles`) and its `docs/roadmap/` KB-DOTFILES-UE records; managed and unmanaged coverage and `.chezmoiignore`; drift between source and targets; the chezmoi side of host-local KI config, such as the `[locals]` migration; reviewed, scripts-excluded applies on terra and sol.
- Out: Rig, its records and the at-screen bring-up of sol and terra (ki.mac-studio-setup); tools-ki and tools-mgit and their releases (ki.tools-burndown); the work model and harness guidance (ki.ways-of-working); territory dispatch (ki).
