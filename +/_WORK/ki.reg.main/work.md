---
id: ki.reg.main
parent: ki.sop.main
level: regular
title: 'KI > Regular'
theme: null
description: >-
  Holds the territory's recurring regular work, defined in the Capital's Activity notes and self-coordinating, and
  the ad hoc pieces it holds as ki.reg.<slug>; it creates work items in any repository. Takes Activity occurrences
  and small one-off work with no Project. Not for territory dispatch (ki.sop.main) or Project work and a Project's
  own recurring checks (ki.prj.chezmoi, ki.prj.observatory and the other Project works).
worker: agent
supervisor: owner
created_at: 2026-10-18T03:30:38Z
---

# ki.reg.main

## Goals

- Run the territory's [regular work](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Processes/Work Process/Work Process.md#levels-and-forms-of-work>) as the Work Process defines it.
- Run each occurrence the Capital's [Activity notes](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Operations/Activities/Activities.md) define, sending work items down to the repository that executes them.

## Scope

- In: recurring occurrences under the Capital's Activity notes; new ad hoc regular work, seeded as `ki.reg.<slug>`; the work items these create in any repository.
- Out: territory dispatch and the Project queue (ki.sop.main); Project work and a Project's own recurring checks (ki.prj.chezmoi, ki.prj.observatory, ki.prj.tools-burndown and the other Project works); the work model itself (ki.prj.ways-of-working).
