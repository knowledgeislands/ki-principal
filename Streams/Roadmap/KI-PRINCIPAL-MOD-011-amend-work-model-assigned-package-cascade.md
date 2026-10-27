---
note_type: stream-roadmap
id: KI-PRINCIPAL-MOD-011
area: MOD
title: Amend work model cascade
kind: deliver
purpose: governance
project: ways-of-working
component: model
tags:
  - topic/knowledge-islands
priority: medium
size: m
status: draft
horizon: now
blocks: []
blocked_by: []
baseline_ref: null
created_at: 2026-10-26T22:13:22Z
updated_at: 2026-10-27T05:37:23Z
---

# Amend the Work Process Note and GDR-KI-PRINCIPAL-009 to the Assigned-Package Cascade

## Goal

The [Work Process](<../../Pillars/Philosophy/Model/Processes/Work Process/Work Process.md>) note and [GDR-KI-PRINCIPAL-009](../../Admin/Governance/Decisions/GDR-KI-PRINCIPAL-009-the-work-model.md) describe the work model as Kris decided it on 25 and 26 October 2026: one State of play thread may look after several Project packages by explicit, committed assignment and acknowledged handover; each package keeps its own state, mark, queries and decisions; every package below the territory's main work names its coordinating parent; a host requirement is a fact about the work, never a committed seat; and the commit cadence and standing push rule replace "only sends and receives commit". Both documents say the same thing as the harness standards at revision `1af72f2e`, each citing the other rather than restating it.

## Context

The ways-of-working Project designed the shape under `ki-work-design`: the brief, two independent reviews and the merged [model shape report](<../../+/_WORK/ki.ways-of-working/design/model-shape-report.md>) of 25 October 2026. Kris decided CASCADE-STEWARD, CASCADE-REPORT, RELATIONS, HOST-SEAT and HOST-TARGET on 25 October, each as its recommended option, with COMMIT-CADENCE and PACKAGE-PUSH the same night, as the [ways-of-working decisions log](<../../+/_WORK/ki.ways-of-working/decisions.md>) records. Harness commit `1af72f2e` carries them in `ki-coordination`, `ki-work-package`, `ki-work-roadmap` and `ki-delegation`, with target dates (DUE-FIELD) and the package homes, leaving STEWARD-FIELD a marked placeholder.

The report's rollout plan names, as its second step, one Knowledge Islands Principal record amending the Work Process note's Levels, inbox, Words and "Git is the logbook" sections and GDR-KI-PRINCIPAL-009 in place. Kris answered SINGLE-THREAD a) on 26 October 2026 at 21:25 GMT, read back in the decisions log as "capture the Principal record amending the Work Process note and GDR-KI-PRINCIPAL-009 through the Enactment Process, and open a one-wave Valle Armonia pilot on one named VA Project package". This is that record; the pilot is proposed to Valle Armonia's State of play by a message, not by this record.

The Work Process note already carries the commit cadence and standing push wording from the earlier amendment that cited COMMIT-CADENCE and PACKAGE-PUSH; this record checks the rest of the note against the decided model rather than assuming the gap.

## Boundary

- In: the Work Process note's Levels and forms of work, Homes, Routing and stewardship, Words and Git is the logbook wording; GDR-KI-PRINCIPAL-009's Decision and Consequences, amended in place and dated, with the prior wording kept as history in Git only. Both are canonical, so the exact wording goes through the [Enactment Process](<../../Admin/Operations/Processes/Enactment Process.md>) and is confirmed before it is written.
- In: the Glossary's thread and session entries where the note holds them, so a thread is who acts on a package and a session only the channel.
- Out: STEWARD-FIELD, the assignment's field and file, which stays open with Kris; until it lands, the assignment is logged in the stewarding work's decisions, as the harness standard says. The record notes the placeholder and does not choose for it.
- Out: the harness standards, `tools-ki` readers, the Observatory and `ki agent`; each is handled by its own repository under the rollout plan's third and fourth steps.
- Out: the Valle Armonia pilot and its exit conditions, which run in the va package; its lessons may feed a later amendment, not this one.
- Out: any change to the seven states, the roles, the banner or the roadmap mapping, which the decided model leaves as they are.

## Current state

The existing amendment is selected into Now as a draft through ki-next under the current owner authority and coordinator adoption-timing reading: keep bringing deferred work back, consolidate ways-of-working functionality and act on high confidence. This takes the already-decided/live amendment forward now; it is not a fabricated option-a answer. The original writer is DONE and the seven required Project assessments are complete without Project closure. The actual base and Streams preflight cleared on 27 October 2026 without failures or warnings.

The harness carries the decided cascade; the canonical Work Process and GDR still need the bounded amendment. The [proposed wording](<../../+/_WORK/ki.ways-of-working/design/mod011-wording.md>) is a reviewable working-area input only. Exact wording and plan approval remain with Kris through Enactment, so this record stays draft, with no implementation baseline or invented readiness.

## Steps

- [ ] Obtain Kris's Enactment review of the exact two-document wording and bounded plan, keeping STEWARD-FIELD excluded and pilot conditions with rollout work; only then consider Ready through ki-plan.
- [ ] Re-ground both canonical files and the record, confirm the approved patch still matches, then use the authorised implementation lifecycle for this record.
- [ ] Amend the Work Process note and GDR-KI-PRINCIPAL-009 together, in place and dated, preserving identities and decided scope; introduce no assignment field or host syntax.
- [ ] Verify Markdown, exact-case relative links, adapter integrity and semantic parity against the approved model; retain excluded pilots and repository-owned rollout authority.
- [ ] Present implementation evidence for separate review and acceptance; do not self-accept, close a Project or prune.

## Files touched

Planning: this exact existing record and [mod011-wording.md](<../../+/_WORK/ki.ways-of-working/design/mod011-wording.md>) only. Proposed later implementation, only after Enactment approval: [Work Process](<../../Pillars/Philosophy/Model/Processes/Work Process/Work Process.md>) and [GDR-KI-PRINCIPAL-009](<../../Admin/Governance/Decisions/GDR-KI-PRINCIPAL-009-the-work-model.md>). No package files, findings, skills or other records belong to this run.

## Verify

Run `ki repo audit --skill ki-work --repo <git-root>` and the actual selected `ki-repo-kb-streams` adapter preflight without any FAIL/WARN bypass. After shaping, run the focused roadmap/Streams and authoring checks over the changed paths and exact-case local-link assertions, including proposed canonical links in their destination context. Check the proposed patch with `git apply --check` without applying it. Required commit hooks must pass; inspect post-hook changed names against the explicit two-path allowance. Semantic review must cover assignment/handover, per-package moves and marks, reporting homes, routing without authority, parent/covers, host boundaries, cadence and publication, with STEWARD-FIELD and pilots excluded.

## Dependencies / blocks

No record dependency is asserted: the seven assessments repaired preflight without closing Projects. Necessary owner approval of this exact wording and plan remains an Enactment gate, not a fabricated completed prerequisite. STEWARD-FIELD remains unresolved but outside the proposed amendment; no choice is made for it. The Valle Armonia and host pilots and other repositories' readers/standards remain separate rollout work, not this run's delivery or acceptance.

## Documentation impact

### Decision Records

Amend the existing GDR-KI-PRINCIPAL-009 in place after owner approval, with a dated amendment and retained Git history; no new Decision Record or new model acceptance.

### Specifications

No software contract, host syntax or assignment-field schema is introduced. Describe the already-decided cascade and preserve the seven states and roadmap mapping.

### Guides

Bring the canonical Work Process narrative into line with the decided cascade, citing harness operational standards and retaining the existing cadence rather than duplicating its mechanism.

### Roadmap

Keep this one amendment as Now/draft while approval is pending. Do not create records, close Projects, adopt other repositories' work or accept pilots; later delivery and acceptance remain separate lifecycle moves.

## Discussion

- Shape the amendment as one pass over both documents so the note and the record cannot drift apart; the GDR gains a dated amendment paragraph in its Decision rather than a new record, since the model is the same model extended.
- The decided model's eight headings in the report, Package and thread, Stewardship, Runs, Records, Relationships, Hosts, Shared writing and Reporting, are the checklist for the note; the report's Agreement and difference table gives the evidence for each.
- Proposed planning boundary: pilot exit conditions stay with the rollout plan; the canonical amendment acknowledges that boundary without performing or accepting a pilot. Kris reviews this wording with the bounded plan before Ready.

### Governance

This record adheres to the [Enactment Process](<../../Admin/Operations/Processes/Enactment Process.md>). Kris's SINGLE-THREAD a) answer of 26 October 2026 authorises its capture; adoption, the exact wording and acceptance are separate owner decisions.
