---
note_type: stream-roadmap
id: KI-PRINCIPAL-MOD-009
area: MOD
title: Amend ADR-KI-PRINCIPAL-001 staging wording
kind: deliver
theme: model
component: model
tags:
  - topic/knowledge-islands
  - topic/acquisition
priority: medium
size: m
status: draft
horizon: now
blocks: []
blocked_by: []
baseline_ref: null
created_at: 2026-10-17T22:50:00Z
updated_at: 2026-10-20T04:14:07Z
---

# Amend ADR-KI-PRINCIPAL-001 Staging Wording

## Goal

Amend the staging wording of [ADR-KI-PRINCIPAL-001](../../Admin/Governance/Decisions/ADR-KI-PRINCIPAL-001-provider-neutral-knowledge-acquisition.md) so it matches how acquisition stages material today, and bring the [Acquisition Process](<../../Pillars/Philosophy/Model/Processes/Acquisition Process/Acquisition Process.md>) note into line with Acquire as it stands on 20 October 2026.

## Context

The ADR's decision says `ki acquire import --adapter <provider>` stages material in the receiving island's `+` Harbour. Granola captures now stage in the shared private `acquire` repository, where `captures/<territory>/granola/` holds each capture and `.acquire/granola/ledger.json` holds the checkpoint state; the 2026-10-10 consolidation retired the per-island Harbour staging, including this island's `+/_ACQUIRE/granola/`. The six-stage model (discover, acquire, stage, harvest, durable knowledge, archive or delete source) still holds, so this is wording drift, not a contradiction.

On 20 October 2026 Acquire simplified further: it keeps no ledger, the `.acquire/` state and the `intake/` receipts are removed, there is no return route, and dispatch into a receiving principal's `+/_ACQUIRED/` is acceptance, the receiver's commit with Acquire's removal commit being the only record. That model now lives only in Acquire's dispatch guide (`docs/guides/operator/dispatch.md`), AGENTS.md and guides, while the Acquisition Process note still describes intake writing a receipt, retirement keeping receipts and fingerprints, the Granola ledger as provenance evidence, returned items coming back as rejected knowledge, and links the removed `CAPTURE-CHATGPT.md`. Kris took METHOD-NOTE a) on 20 October, through the Knowledge acquisition close-out, to widen this record to cover the note.

[KI-PRINCIPAL-MOD-006 (pruned)](https://github.com/knowledgeislands/ki-principal/blob/37b5f55/Streams/Roadmap/KI-PRINCIPAL-MOD-006-knowledge-acquisition-lifecycle.md) found the mismatch and, as its record instructed, left the ADR unchanged. Kris decided on 2026-10-17 (ADR-HARBOUR): "Capture a small follow-up record to amend ADR-KI-PRINCIPAL-001's staging wording to match acquire." The evidence is in the Acquisition Process note delivered by that record and in the `acquire` ledger and migration manifest it cites.

## Boundary

- The ADR's staging wording, and the Acquisition Process note brought into line with the 20 October model: no ledger, no intake receipts, no return route, delivery into `+/_ACQUIRED/` as acceptance, and the removed `CAPTURE-CHATGPT.md` link replaced by Acquire's `CAPTURE.md` entry point.
- The intake trial's method points, adopted into the note: a drop is cleared only once every item is verified at its destination; images stay in Git, while material outside Git, video included, goes to the external source store at the mirrored package path (Acquire's files still say video drops are held, so the wording is checked against Acquire at enactment); and territory context is provider-free.
- The six-stage model, the provenance requirements and the provider boundaries stay as they are, beyond the receipt and ledger evidence the 20 October model removed.
- The ADR is under `Admin/Governance/` and the Acquisition Process note under `Pillars/`, so each amendment runs through the [Enactment Process](<../../Admin/Operations/Processes/Enactment Process.md>) and needs the exact wording confirmed before it is written.
- No change to `acquire`, `tools-ki` or any adapter.

## Discussion

- Decide whether the ADR names `acquire` as the staging home or states the principle (staging in a Git-backed holding area owned outside the receiving island) and lets the Acquisition Process note carry the location.
- Check the other wording that follows from the same sentence: the Context paragraph on the Harbour, and the ADR's consequences about `tools-ki` owning staging mechanics.
- Keep the [Acquisition Process](<../../Pillars/Philosophy/Model/Processes/Acquisition Process/Acquisition Process.md>) note consistent with the amended wording.
- Widen the amendment to cover the end-to-end flow Kris accepted on 2026-10-18 and recorded in the [Acquisition Process](<../../Pillars/Philosophy/Model/Processes/Acquisition Process/Acquisition Process.md#end-to-end-flow>) note: dispatch into the receiving island's inbound area and "the port" as the name of acquire's function, with "harbour" kept for the island imagery. The receipt, fingerprints and returned-items parts of that flow are superseded by the 20 October model.
- Open point for Kris at enactment, CUSTOMS-WORDS: on 18 October Kris adopted **Customs** for the facility, the **clearance area** and **clearance** as words for Acquire, recorded only in the retired intake-trial note. Since then Kris has called Acquire "simply a sorting office", which the dispatch guide uses, and the [Glossary](../../Admin/Governance/Conventions/Glossary.md) already uses Customs for an island's boundary rules. Recommendation: drop "Customs" and "clearance"; "the port" and "sorting office" stand.
