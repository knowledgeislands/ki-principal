---
note_type: stream-roadmap
id: KI-PRINCIPAL-MOD-010
area: MOD
title: Work-model terminology sweep after the work migration
kind: deliver
purpose: governance
project: ways-of-working
component: model
horizon: now
status: awaiting-review
tags:
  - topic/knowledge-islands
blocks: []
blocked_by: []
baseline_ref: baffa82170a0d46b1903d3f18e0bd0b7b0a3f328
created_at: 2026-10-18T06:47:00Z
updated_at: 2026-10-18T06:47:00Z
---

# Work-Model Terminology Sweep After the Work Migration

## Goal

Live guidance in this island speaks the work model of [[GDR-KI-PRINCIPAL-009-the-work-model|GDR-KI-PRINCIPAL-009]]: the work file in `+/_WORK/<id>/work.md` carries a piece of work's state, and no live note still names a checkpoint or a thread folder as that instrument.

## Context

The work migration of 2026-10-18 moved every `+/_CHECKPOINTS/` record and `+/_THREADS/` folder into work folders under `+/_WORK/` and `+/_WORK_REVIEW/`. GDR-KI-PRINCIPAL-009 records that "checkpoints and thread folders as separate instruments" no longer govern. Kris, on 18 October: finish merging the ways-of-working concepts first and foremost, then "keep pushing and pushing and get as much done as you can". The roadmap-next run's brief turned that into a sweep for leftover `+/_THREADS/` or checkpoint references in live guidance, stale links and index notes, fixed on main. That instruction is the owner instruction for a bounded change that the [[Admin/Operations/Processes/Enactment Process|Enactment Process]] lets stand in for approval; this record keeps the evidence for review.

## Boundary

- Live guidance only: `Admin/`, `Pillars/`, `Streams/`, the root `AGENTS.md` and `CLAUDE.md`.
- Historical evidence is left as written: Decision Records, run reports and decisions logs in work folders, and quoted owner words.
- The generic sense of "checkpoint" (an environment, controller, provider or acquisition checkpoint) is not the work-model instrument and stays.
- Work files and reports owned by other work get only Messages lines.

## Steps

- [x] Search the live zones for `_THREADS`, `_CHECKPOINTS`, "checkpoint", "thread folder", "pick-up block" and "run state folder", and separate the work-model sense from the generic one.
- [x] Replace the one live work-model use: the Coordination paragraph of [[Known World]] now reads "Git and the work file stay the source of truth".
- [x] Repoint the two links in [[KI-PRINCIPAL-ECO-013-pmo-extraction-pilot|KI-PRINCIPAL-ECO-013]] to the pruned KI-HARNESS-GOV-182 and KI-HARNESS-GOV-188 at their last revisions on GitHub.
- [x] Check every `Streams/` folder for its index note, and that `Projects.md` and `Themes.md` list every Project and theme.
- [x] Remove the empty, untracked `+/_THREADS/ways-of-working/` folder once `ki agent home ways-of-working` resolves to `+/_WORK/ki.ways-of-working`.

## Files touched

- `Pillars/Philosophy/Emerging Concepts/Known World.md`
- `Streams/Roadmap/KI-PRINCIPAL-ECO-013-pmo-extraction-pilot.md`
- `Streams/Roadmap/KI-PRINCIPAL-MOD-010-work-model-terminology-sweep.md`

## Verify

- `git grep -E '_THREADS|_CHECKPOINTS'` over `Admin`, `Pillars`, the root notes and `Streams/Themes` returns nothing; in `Streams/Projects` and `Streams/Roadmap` it returns only GitHub links to deleted reports and historical delivery evidence.
- Every absolute-path Markdown link in `Admin/`, `Pillars/` and `Streams/` resolves to an existing file.
- `ki repo audit` reports no finding on the touched paths.

## Review

Evidence from the roadmap-next run, 2026-10-18:

- The search found one work-model use of "checkpoint" in live guidance, in [[Known World]]; every other hit in `Admin/` and `Pillars/` is the generic sense, and every `_THREADS` hit outside work folders is a GitHub link to a deleted report or past delivery evidence in a record.
- The absolute-link scan over `Admin/`, `Pillars/` and `Streams/` found two broken links, both in KI-PRINCIPAL-ECO-013, now repointed; none remain.
- Every `Streams/` folder has its index note; `Projects.md` and `Themes.md` list every Project and theme.
- `ki agent home ways-of-working` prints `+/_WORK/ki.ways-of-working`, so the empty legacy folder held nothing a launch would use.

## Governance

This roadmap record adheres to the [[Admin/Operations/Processes/Enactment Process|Enactment Process]]. Move content to `Admin/`, `Pillars/`, or `Resources/` only on user approval of a `ready` record.
