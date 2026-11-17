---
note_type: stream-roadmap
id: KI-PRINCIPAL-GOV-036
area: GOV
title: Territory alias ownership
priority: low
size: s
status: triage
assignee: owner
blocks: []
blocked_by: []
baseline_ref: null
created_at: 2026-11-17T03:14:23Z
updated_at: 2026-11-17T03:14:23Z
---

# Territory Alias Ownership

## Goal

Each territory's short alias, as listed in [Known Lands](<../../Admin/Governance/Known Lands.md#estate-territories>), has one named durable owner and one source of truth, so that a new or renamed alias is decided in one place and the repositories, work ids and codes that use it follow from there.

## Context

The Estate factorisation Project left territory alias ownership as a governance residual (ALIAS-OWNERS) when Kris chose to retire it on 25 October 2026. The State of play package kept it parked until a Harness or Principal record owned it. When the package was folded into the Cairn store, Kris took ALIAS-OWNERS and GOVERNANCE a) on 17 November 2026: one triage record each in this roadmap, with nothing parked in the store. This is that record.

Today the alias appears in Known Lands' Estate territories table, while the repository standard in the backpack's `ki-repo` sets a territory's handle from its Capital's `territory_prefix` and reserves `personal`; the two may not say the same thing in every case.

## Boundary

- In: deciding where a territory alias is owned and recorded, and whether Known Lands or the Capital's `.ki.toml` is its source of truth.
- Out: renaming any territory, alias or prefix; changing the `ki-repo` standard itself, which belongs to the backpack and would go there as a message.

## Discussion

The first step on adoption is to check whether the residual is still real: the `personal` reservation of 25 October 2026 and the handle rule in `ki-repo` may already settle ownership, in which case this record is cancelled as obsolete.
