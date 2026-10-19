---
id: ki.knowledge-acquisition
level: project
title: 'KI > Model > Knowledge acquisition'
project: knowledge-acquisition
theme: model
description: >-
  Develops the provider-neutral knowledge acquisition model and method, with Acquire as the port that takes in,
  preserves and dispatches knowledge. Takes acquisition lifecycle design, capture contracts and provider skills,
  intake tie-up and receipt retention, acquisition-state placement and dispatch-and-return design. Not for tools-ki
  importers (ki.tools-burndown), the Observatory (ki.observatory), chezmoi and trades (ki.chezmoi) or the acquire
  specification (ki.portable-specifications).
worker: agent
supervisor: owner
created_at: 2026-10-08T08:35:00Z
---

# ki.knowledge-acquisition

## Goals

- Deliver the [Knowledge acquisition](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/knowledge-acquisition.md) Project's outcome.
- Develop the acquisition method through conversational exchange and faithful intake, then return to ordinary intake and distribution once the approach settles.
- One common `ki-acquire` contract, thin provider skills and a single `CAPTURE.md` entry, with intake receipts, capture packages, routing context and technical acquisition state kept distinct, each with one owner.
- Verify new source bytes directly where available and reuse existing captures; never reopen completed source imports.
- Agree a minimal surviving-proof model and its destination before any tooling change, state relocation, receipt pruning or prototype disposal.

## Scope

- In: the acquisition model and its design notes; the common `ki-acquire` contract and provider skills; Acquire's `captures/<territory>/<source-or-ingress>/` and `context/<territory>/` layout and mirrored Git/source-store locators; intake tie-up and receipt retention; `.acquire/` state placement; the binary prototype's disposition; dispatch and return design; the KB-ACQUIRE records this Project coordinates.
- Out: day-to-day intake in Acquire (kb.regular.acquire-intake, personal territory); tools-ki importers and `ki work status` (ki.tools-burndown); the Observatory (ki.observatory); chezmoi and the trades review (ki.chezmoi); the `acquire` specification (ki.portable-specifications); the work model (ki.ways-of-working); the Project cap and territory dispatch (ki).
