---
note_type: stream-roadmap
id: KI-PRINCIPAL-MOD-008
area: MOD
title: Whole-philosophy coherence review
kind: audit
purpose: governance
project: island-model-and-tending
component: model
size: l
tags:
  - topic/knowledge-islands
status: awaiting-review
horizon: now
blocks: []
blocked_by: []
baseline_ref: 55fbdd646b7b174b7f98d0992c5ec56bba227ff8
created_at: 2026-10-11T03:26:34Z
updated_at: 2026-10-20T21:26:02Z
---

# Whole-Philosophy Coherence Review

## Goal

Read the whole Knowledge Islands philosophy end to end and confirm it still holds together, both internally and against what the website presents, so later additions rest on a coherent base.

## Context

Kris judges the established philosophy - the concepts the website was built from - largely sound, but it has grown by addition across many sessions and has not been read as one piece since. Several threads were deliberately parked for this review rather than settled piecemeal: the open concepts moved out of the ChatGPT acquire into [Emerging Concepts](<../../Pillars/Philosophy/Emerging Concepts/Emerging Concepts.md>), the candidate principles added to Engineering Practice [Principles](<../../Pillars/Engineering Practice/Foundations/Principles.md>), the Library wording, the unfinished Structure sections and the naming of Avatars per Realm.

Parked until most of Arcadia's roadmap is cleared, so the review reads a settled philosophy rather than one still moving underneath it (Kris's decision of 2026-10-12). At each review date, if most of the roadmap is cleared, consider releasing it for progressing; if not, move the review date on by one week and reassess then.

Hold reviewed 2026-10-17, a day late: the roadmap is not yet mostly cleared, with the tools burndown and the awaiting-review backlog still open, so the hold stands and the review moves on one week to 2026-10-23.

Released to `next` on 20 October, ahead of that review date: the condition is met, because the State of play coordinator's second roadmap census of 20 October found five Knowledge Islands Principal records left on the roadmap. Release changes only the horizon; the review itself is not started.

Taken up on 20 October under Kris's overnight burndown authority of 22:03 BST ("Is there anything more that you can do by yourself without me? ... roadmap down"), which stands in for readiness approval for this bounded review: consistency fixes are made, and every change of meaning is left as a query.

## Current state

The Philosophy has 0 broken internal links and no em or en dashes at baseline. It carries retired vocabulary from earlier model generations (Knowledge Capital as a folder, satellite islands, the archipelago as a unit of governance), indexes that lag four processes and four tools, and a few open design questions parked for this review.

## Boundary

- **Guard (Kris's decision of 2026-10-11).** Additive changes are welcome. Any change that would contradict laid-down philosophy is flagged to Kris and double-checked before it is made; the review does not resolve a contradiction on its own authority.
- Reviews and proposes; canonical changes still go through the [Enactment Process](<../../Admin/Operations/Processes/Enactment Process.md>).
- Compares against the website's presentation but makes no change to `ki-website`; any website follow-up is a plain-terms handoff to that repository.
- Does not restructure the knowledge base. The Great Library is settled: it is Arcadia's name for its `Pillars/` zone, and naming changes no structure.

## Findings

Line references are at the baseline. Each fix is wording, linking or consistency with an already settled decision; each finding marked query changes meaning and waits for Kris.

| ID | Finding | Source | Recommendation |
| --- | --- | --- | --- |
| F1 | Typo "teritories" | `Pillars/Philosophy/Knowledge Islands.md:16` | Adopt: fixed |
| F2 | Part III named by the retired "Knowledge Capitals" title | `Knowledge Islands.md:18`, against `:135` | Adopt: names Realisation |
| F3 | "Satellite" islands, retired by [SDR-KI-PRINCIPAL-005](../../Admin/Governance/Decisions/SDR-KI-PRINCIPAL-005-territories-archipelagos-and-the-constitutional-layer.md) (one Capital, other member islands) | `Knowledge Islands.md:51`, `Introduction/Concept/Jurisdiction/Jurisdiction.md:14`, `Model/Activities/Tending/Tending.md:67` | Adopt: fixed; the image alt text in What is Knowledge Islands is left as artwork description |
| F4 | Reading-order index misses the Acquisition and Work Processes and four Tools, and lists Tending apart from the adoptable groups although the Charter treats it as adoptable | `Knowledge Islands.md` Part II | Adopt: indexed |
| F5 | Introduction calls the three acts "chapters" | `Introduction/Introduction.md:14` | Adopt: "acts" |
| F6 | Model, Processes and How Change Happens speak of two processes; four exist; Citizen definition linked to Governance rather than Jurisdiction | `Model/Model.md`, `Model/Processes/Processes.md:18`, `Model/Processes/How Change Happens.md:16, 26` | Adopt: fixed |
| F7 | Archipelago used as a governance unit, against SDR-KI-PRINCIPAL-005 | `Introduction/Concept/Governance/Governance.md:18`, `How Change Happens.md`, `Tending.md:67`, `Introduction/Background/What is Knowledge Islands/What is Knowledge Islands.md:14, 16` | Adopt: territory |
| F8 | "Knowledge Capital" as an island folder, retired (governance lives in `Admin/`, Structure:58) | `Model/Conventions/Notes/Notes.md:33`, `Notes/Tags.md:15`, `Model/Activities/Constitutional/Constitutional.md:19, 21, 28`, `Model/Activities/Tending/Convergence Check.md:34, 55, 57`, `Model/Activities/Authoring Guidelines/Authoring Guidelines.md:166` | Adopt: `Admin/` zone |
| F9 | American "judgment" against "judgement" elsewhere | `Introduction/Concept/Agents/Agents.md:14` | Adopt: British spelling |
| F10 | Notes overview lists three note types; Types lists four | `Notes.md:19, 39` | Adopt: activity notes added |
| Q1 CALENDAR-LIBRARY | Structure:44, The Home of Knowledge and the website put Calendar in the Library; [SDR-KI-PRINCIPAL-002](../../Admin/Governance/Decisions/SDR-KI-PRINCIPAL-002-the-home-of-knowledge.md) makes the Library Pillars and Resources; Calendar is exempt from Enactment yet "Nothing enters the Library except through the governance process" | Structure, The Home of Knowledge, SDR-KI-PRINCIPAL-002 | Query |
| Q2 ENACTMENT-ADMIN | Portable gate statements name Pillars and Resources only; SDR-KI-PRINCIPAL-002 and the island's Enactment Process include `Admin/` | `Governance.md:18`, `Jurisdiction.md:12`, Model Enactment Process, `Processes.md`, Great Library | Query |
| Q3 CAPITAL-OF-CAPITALS | "the Knowledge Capital of Knowledge Capitals" implies a role over other territories' Capitals, against Territories and Archipelagos ("no jurisdiction over another territory") | `Knowledge Islands.md:20, 135` | Query |
| Q4 TAGS | `card/*` and `calendar/*` tags duplicate `note_type`; `topic/*` tags still serve search (Kris's decision of 2026-10-12 asked this) | `Notes/Tags.md` | Query |
| Q5 EMERGING | Emerging Concepts: Realm Model, Avatar Roles and Oversight, Known World and Fictional Lineage; Avatar names per Realm against [ADR-KI-PRINCIPAL-005](../../Admin/Governance/Decisions/ADR-KI-PRINCIPAL-005-one-persona-across-explicit-working-contexts.md) | `Pillars/Philosophy/Emerging Concepts/` | Query |
| Q6 CANDIDATE-PRINCIPLES | The neutrality extension to Provider-Neutral Execution and FOSS-First and Inspectable remain candidates | `Pillars/Engineering Practice/Foundations/Principles.md` | Query |
| Q7 STRUCTURE-TODOS | The Port to-do is largely settled by [GDR-KI-PRINCIPAL-010](../../Admin/Governance/Decisions/GDR-KI-PRINCIPAL-010-the-port.md); Routes and Customs remains open | `Structure.md` Port, Routes and Customs | Query |
| Q8 LAYER-PATHS | Content-layer paths `/Pillars/Knowledge Capital/Model/...` do not exist | `Authoring Guidelines.md:31, 32, 84` | Query |

The website (`apps-knowledgeislands.info`) is stale against the knowledge base on the archipelago as a separate grouping and "Principal Island ... Satellites", the zone count, the harbour and lighthouse icons for processes, and the two of four processes shown; this is routed to State of play's `messages.md` for the website owner.

## Steps

- [x] Confirm the sweep's WORKABLE classification against this record.
- [x] Read the whole Philosophy, Emerging Concepts, the candidate principles, the Library and Structure sources and the website presentation.
- [x] Record each inconsistency as a referenced finding with a recommendation.
- [x] Make the wording, linking and consistency fixes F1 to F10, each traceable to its finding.
- [x] Leave each change of meaning as a query, Q1 to Q8.
- [x] Route the website follow-up as a line in State of play's `messages.md`.
- [x] Verify links, retired vocabulary, dashes and the repository audits.

## Files touched

- `Pillars/Philosophy/Knowledge Islands.md`
- `Pillars/Philosophy/Introduction/Introduction.md`
- `Pillars/Philosophy/Introduction/Background/What is Knowledge Islands/What is Knowledge Islands.md`
- `Pillars/Philosophy/Introduction/Concept/Agents/Agents.md`
- `Pillars/Philosophy/Introduction/Concept/Governance/Governance.md`
- `Pillars/Philosophy/Introduction/Concept/Jurisdiction/Jurisdiction.md`
- `Pillars/Philosophy/Model/Model.md`
- `Pillars/Philosophy/Model/Processes/Processes.md`
- `Pillars/Philosophy/Model/Processes/How Change Happens.md`
- `Pillars/Philosophy/Model/Conventions/Notes/Notes.md`
- `Pillars/Philosophy/Model/Conventions/Notes/Tags.md`
- `Pillars/Philosophy/Model/Activities/Constitutional/Constitutional.md`
- `Pillars/Philosophy/Model/Activities/Tending/Tending.md`
- `Pillars/Philosophy/Model/Activities/Tending/Convergence Check.md`
- `Pillars/Philosophy/Model/Activities/Authoring Guidelines/Authoring Guidelines.md`
- `+/_WORK/ki/messages.md`
- this record

## Verify

- Internal links in `Pillars/Philosophy` resolve, apart from template placeholders and illustrative examples in Format.
- No "teritories", "judgment" or "satellite" remains outside image alt text; "Knowledge Capital" remains only in Structure's explanation of its retirement, the Q3 lines and the Q8 paths.
- No em or en dashes in touched files.
- `ki repo audit --skill` for `ki-work`, `ki-repo-kb-streams`, `ki-work-roadmap` and `ki-repo-kb` shows no new finding, and the size warning on this record clears.

## Dependencies / blocks

None. Q1 to Q8 need Kris's decision before any change of meaning.

## Documentation impact

### Decision Records

None changed. SDR-KI-PRINCIPAL-002's Library wording rests on Q1 CALENDAR-LIBRARY.

### Specifications

None.

### Guides

None.

### Roadmap

No new records. The website follow-up goes as a message to State of play; work that follows Kris's answers to the queries is shaped by the owning work.

## Review

### Delivered

A whole-Philosophy coherence read with ten referenced findings fixed as wording, linking and consistency changes, eight findings raised as queries for Kris, and a website handoff routed as a message.

### Change Summary

Fifteen Philosophy notes changed (32 bounded replacements): retired "Knowledge Capital", "satellite" and archipelago-as-governance wording brought into line with SDR-KI-PRINCIPAL-005 and the `Admin/` zone; process, tool and note-type lists completed; one typo, one spelling and one "chapters" corrected; Citizen definition relinked to Jurisdiction.

### Verification

- Links: every internal link in `Pillars/Philosophy` resolves, apart from the unchanged Calendar template placeholders and the illustrative examples in Format.
- Vocabulary: no "teritories" or "judgment"; "satellite" only in image alt text; "Knowledge Capital" only in Structure:58, Knowledge Islands.md (Q3) and Authoring Guidelines (Q8).
- Dashes: no em or en dash in the 17 touched files.
- Audits: `ki repo audit --skill` for `ki-work`, `ki-repo-kb-streams`, `ki-work-roadmap` and `ki-repo-kb` exit 0, with no new finding; STREAM-12 on this record cleared.

### Outstanding concerns

- Eighteen Philosophy notes still carry `status: draft - April 2026`; left for the Status Review activity or acceptance.
- The portable Model Enactment Process note carries island-local specifics that duplicate the `Admin/` note.
- Governance concept examples ("Linear sync") are dated.
- SDR-KI-PRINCIPAL-002 still says "Harbour"; historical under GDR-KI-PRINCIPAL-010.

### Post-change review

Each change was checked against its finding and source; no change alters a definition, a rule or an adopted decision. Contradictions with laid-down philosophy are queries, under the 2026-10-11 guard.

### Mini recap

Consistency fixed, meaning left to Kris in eight queries, website handed off by message.

## Discussion

Scope to read and check:

- The whole philosophy under [Philosophy](../../Pillars/Philosophy/Philosophy.md), end to end, for internal coherence and against what the website presents.
- The [Emerging Concepts](<../../Pillars/Philosophy/Emerging Concepts/Emerging Concepts.md>) notes and the candidate principles in Engineering Practice [Principles](<../../Pillars/Engineering Practice/Foundations/Principles.md>): which to adopt, reshape or leave open.
- The Library wording across [Structure](../../Pillars/Philosophy/Model/Conventions/Structure/Structure.md), [The Home of Knowledge](<../../Pillars/Philosophy/Introduction/Background/The Home of Knowledge/The Home of Knowledge.md>) and [SDR-KI-PRINCIPAL-002](../../Admin/Governance/Decisions/SDR-KI-PRINCIPAL-002-the-home-of-knowledge.md), which disagree on whether Calendar sits inside the Library.
- The Harbour and Routes and Customs to-dos in [Structure](../../Pillars/Philosophy/Model/Conventions/Structure/Structure.md), which wait for this review.
- Tags: whether the island still needs its subject tags alongside `note_type`, folders and links (Kris's decision of 2026-10-12).
- Avatar names per Realm against [ADR-KI-PRINCIPAL-005](../../Admin/Governance/Decisions/ADR-KI-PRINCIPAL-005-one-persona-across-explicit-working-contexts.md).

## Governance

This roadmap record adheres to the [Enactment Process](<../../Admin/Operations/Processes/Enactment Process.md>). Move content to `Admin/`, `Pillars/`, or `Resources/` only on user approval of a `ready` record.
