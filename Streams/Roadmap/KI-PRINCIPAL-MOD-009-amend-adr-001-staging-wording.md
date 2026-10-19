---
note_type: stream-roadmap
id: KI-PRINCIPAL-MOD-009
area: MOD
title: Amend ADR-KI-PRINCIPAL-001 staging wording
kind: deliver
project: knowledge-acquisition
component: model
tags:
  - topic/knowledge-islands
  - topic/acquisition
status: triage
blocks: []
blocked_by: []
baseline_ref: null
created_at: 2026-10-17T22:50:00Z
updated_at: 2026-10-18T00:35:00Z
---

# Amend ADR-KI-PRINCIPAL-001 Staging Wording

## Goal

Amend the staging wording of [[ADR-KI-PRINCIPAL-001-provider-neutral-knowledge-acquisition|ADR-KI-PRINCIPAL-001]] so it matches how acquisition stages material today.

## Context

The ADR's decision says `ki acquire import --adapter <provider>` stages material in the receiving island's `+` Harbour. Granola captures now stage in the shared private `acquire` repository, where `captures/<territory>/granola/` holds each capture and `.acquire/granola/ledger.json` holds the checkpoint state; the 2026-10-10 consolidation retired the per-island Harbour staging, including this island's `+/_ACQUIRE/granola/`. The six-stage model (discover, acquire, stage, harvest, durable knowledge, archive or delete source) still holds, so this is wording drift, not a contradiction.

[KI-PRINCIPAL-MOD-006 (pruned)](https://github.com/knowledgeislands/ki-principal/blob/37b5f55/Streams/Roadmap/KI-PRINCIPAL-MOD-006-knowledge-acquisition-lifecycle.md) found the mismatch and, as its record instructed, left the ADR unchanged. Kris decided on 2026-10-17 (ADR-HARBOUR): "Capture a small follow-up record to amend ADR-KI-PRINCIPAL-001's staging wording to match acquire." The evidence is in the Acquisition Process note delivered by that record and in the `acquire` ledger and migration manifest it cites.

## Boundary

- Wording of the staging location only; the six-stage model, the provenance requirements and the provider boundaries stay as they are.
- The ADR is under `Admin/Governance/`, so the amendment runs through the [[Admin/Operations/Processes/Enactment Process|Enactment Process]] and needs the exact wording confirmed before it is written.
- No change to `acquire`, `tools-ki` or any adapter.

## Discussion

- Decide whether the ADR names `acquire` as the staging home or states the principle (staging in a Git-backed holding area owned outside the receiving island) and lets the Acquisition Process note carry the location.
- Check the other wording that follows from the same sentence: the Context paragraph on the Harbour, and the ADR's consequences about `tools-ki` owning staging mechanics.
- Keep the [[Acquisition Process]] note consistent with the amended wording.
- Widen the amendment to cover the end-to-end flow Kris accepted on 2026-10-18 and recorded in the [[Acquisition Process#End-to-end flow|Acquisition Process]] note: dispatch into the receiving island's inbound area, acquire retiring its copy once dispatched (keeping the receipt and fingerprints, with returned items coming back as rejected knowledge), and "the port" as the name of acquire's function, with "harbour" kept for the island imagery.
