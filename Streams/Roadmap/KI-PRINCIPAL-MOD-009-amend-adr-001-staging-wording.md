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
status: done
blocks: []
blocked_by: []
baseline_ref: 9452900cfb19bb802d60f70563690259f9d889bd
created_at: 2026-10-17T22:50:00Z
updated_at: 2026-10-26T22:11:14Z
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

## Current state

Kris approved CUSTOMS-WORDS a) on 23 October 2026 at 02:12 BST: "Yeah, I approve all of those things you've requested in line with your recommendations as you see fit." The [ways-of-working decisions log](../../+/_WORK/ki.ways-of-working/decisions.md) records the bounded grant to draft and enact this wording. The current Acquire instructions, capture entry point and dispatch guide have been read locally; there are no dependencies on another repository's delivery.

## Steps

- [x] Align the ADR's Context, Decision and Consequences with staging outside the receiving island and delivery into `+/_ACQUIRED/`.
- [x] Bring the Acquisition Process and its displayed flow into line with the 20 October model, retaining dated provenance observations and the provider-side retirement boundary.
- [x] Use the port and sorting office for Acquire; preserve the Glossary's island-boundary meaning of Customs.
- [x] Verify the bounded changes, record evidence and leave this record awaiting review.

## Files touched

- [ADR-KI-PRINCIPAL-001](../../Admin/Governance/Decisions/ADR-KI-PRINCIPAL-001-provider-neutral-knowledge-acquisition.md).
- [Acquisition Process](<../../Pillars/Philosophy/Model/Processes/Acquisition Process/Acquisition Process.md>).
- This record.

## Verify

Run the repository audit, the audit scoped to these paths, Markdown checks and normal commit hooks. Check the staging and dispatch wording against Acquire's current local instructions, confirm the Glossary is unchanged, and check that no current Acquire term uses Customs or clearance. Record pre-existing failures separately from this delivery.

## Dependencies / blocks

None. No Acquire, adapter or runtime change is part of this delivery.

## Review

### Delivered

The approved ADR staging amendment, the 20 October Acquire process alignment and CUSTOMS-WORDS a) are delivered from immutable baseline `9452900cfb19bb802d60f70563690259f9d889bd`. Staging remains outside the receiving island until whole packages reach its principal's `+/_ACQUIRED/`. Delivery is package acceptance; canonical acceptance remains with the receiving island. No Acquire, adapter or runtime file was changed.

### Change Summary

- The ADR's Context, Decision and Consequences distinguish the external staging area from the receiving Harbour and assign staging and dispatch to Acquire.
- The Acquisition Process uses the port and sorting office, removes the receipt and return route from its displayed flow, and dates the earlier ledger and provenance observations as historical evidence.
- Drop retirement requires destination verification; images remain in Git and externally stored originals use a declared source store at the mirrored package path. No binding or held-drop movement is authorised here. Territory context remains provider-free.
- The current Mermaid flow replaces the obsolete SVG reference. The stored SVG and workflow JSON exports are unchanged historical assets, not the displayed current flow.
- The Glossary's island-boundary sense of Customs is unchanged. TAGS-NEXT is a separate bounded owner-approved convention change, not added to this record's scope.

### Verification

- `ki repo audit --repo . --concise --progress never`: baseline failed with 77 existing findings across five skill verdicts; no unrelated repair was attempted.
- Repository audit scoped to the three delivery paths and the separate Tags convention: passed with zero scoped failures or warnings; the wider evaluation still reported the same 77 failures and 74 warnings.
- `rumdl check` on the four changed Markdown files and `git diff --check`: passed. Normal pre-commit and commit-message hooks are required for the delivery commit.
- Exact content checks passed: tag assignments retained, Glossary unchanged, no Customs or clearance term in the ADR or Acquisition Process, no removed capture-entry link, and current displayed flow has no intake receipt or return route.
- Acquire's local `AGENTS.md`, `CAPTURE.md`, dispatch guide and ChatGPT ZIP procedure were read without network access. The drop-procedure link anchor was verified against that local guide.

### Outstanding concerns

The repository-wide audit is not clean: its pre-existing failures and warnings remain outside this delivery. The scoped audit is clean. No item-specific concern remains; approval of the delivered wording is for the owner. No push, acceptance or pruning was performed.

### Post-change review

The goal and approved boundary are met. The six-stage lifecycle, faithful preservation requirements and separate provider-side retirement authority remain intact. The main regression risk was presenting old receipt and ledger mechanics as current; the displayed flow now matches the guide and older evidence is explicitly dated. The item is ready for owner review, not self-accepted.

### Mini recap

Aligned staging, dispatch and vocabulary with Acquire's current guides, retained provenance history, and verified the bounded paths. The canonical ADR and process note hold the learning; no extra record or process is needed.

## Done

Accepted 2026-10-26 by Kris Brown, who answered the ACCEPT query with "all" at 21:25 GMT, taking its recommended option, "KI-PRINCIPAL-MOD-009 accepted as done", as read back in the [ways-of-working decisions log](../../+/_WORK/ki.ways-of-working/decisions.md), entry "2026-10-26 21:25 GMT". Closed under `ki-accept` by the wow-principal-records run; the record is retained and nothing was pruned.

## Discussion

- Decide whether the ADR names `acquire` as the staging home or states the principle (staging in a Git-backed holding area owned outside the receiving island) and lets the Acquisition Process note carry the location.
- Check the other wording that follows from the same sentence: the Context paragraph on the Harbour, and the ADR's consequences about `tools-ki` owning staging mechanics.
- Keep the [Acquisition Process](<../../Pillars/Philosophy/Model/Processes/Acquisition Process/Acquisition Process.md>) note consistent with the amended wording.
- Widen the amendment to cover the end-to-end flow Kris accepted on 2026-10-18 and recorded in the [Acquisition Process](<../../Pillars/Philosophy/Model/Processes/Acquisition Process/Acquisition Process.md#end-to-end-flow>) note: dispatch into the receiving island's inbound area and "the port" as the name of acquire's function, with "harbour" kept for the island imagery. The receipt, fingerprints and returned-items parts of that flow are superseded by the 20 October model.
- CUSTOMS-WORDS was settled by Kris on 23 October 2026 at 02:12 BST: drop Customs and clearance as Acquire terms; the port and sorting office stand. The Glossary's island-boundary meaning of Customs is unchanged.

## Governance

This record adheres to the [Enactment Process](<../../Admin/Operations/Processes/Enactment Process.md>). Kris's bounded approval recorded above authorises this delivery; acceptance remains a separate review.
