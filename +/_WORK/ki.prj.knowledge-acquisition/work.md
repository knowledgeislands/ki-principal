---
id: ki.prj.knowledge-acquisition
parent: ki.sop.main
level: project
title: 'KI > Model > Knowledge acquisition'
project: knowledge-acquisition
theme: model
description: >-
  Develops the provider-neutral knowledge acquisition model and method, with Acquire as the port that takes in,
  preserves and dispatches knowledge. Takes acquisition lifecycle design, capture contracts and provider skills,
  and dispatch design. Not for tools-ki
  importers (ki.tools-burndown), the Observatory (ki.observatory), chezmoi and trades (ki.chezmoi) or the acquire
  specification (ki.portable-specifications). Not taking new units.
worker: agent
supervisor: owner
created_at: 2026-10-08T08:35:00Z
---

# ki.prj.knowledge-acquisition

## Goals

- Deliver the [Knowledge acquisition](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/knowledge-acquisition.md) Project's outcome.
- Develop the acquisition method through conversational exchange and faithful intake, then return to ordinary intake and distribution once the approach settles.
- One common `ki-acquire` contract, thin provider skills and a single `CAPTURE.md` entry, with intake receipts, capture packages, routing context and technical acquisition state kept distinct, each with one owner.
- Verify new source bytes directly where available and reuse existing captures; never reopen completed source imports.
- Agree a minimal surviving-proof model and its destination before any tooling change, state relocation, receipt pruning or prototype disposal.

## Scope

- In: the acquisition model and its design notes; the common `ki-acquire` contract and provider skills; Acquire's `captures/<territory>/<source-or-ingress>/` and `context/<territory>/` layout and mirrored Git/source-store locators; intake tie-up and receipt retention; `.acquire/` state placement; the binary prototype's disposition; dispatch and return design; the PERSONAL-ACQUIRE records this Project coordinates.
- Out: day-to-day intake in Acquire (personal.regular.acquire-intake, personal.sop.main territory); tools-ki importers and `ki.sop.main work status` (ki.prj.tools-burndown); the Observatory (ki.prj.observatory); chezmoi and the trades review (ki.prj.chezmoi); the `acquire` specification (ki.prj.portable-specifications); the work model (ki.ways-of-working); the Project cap and territory dispatch (ki.sop.main).
