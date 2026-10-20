---
note_type: admin/governance/decision
id: GDR-KI-PRINCIPAL-016
title: 'Priority and size on work records'
date: 2026-10-19
updated: 2026-10-19
status: current
decision_type_url: https://knowledgeislands.info/specifications/decision-records/gdr
decision_type: governance
decision_depends_on: ['GDR-KI-PRINCIPAL-005', 'GDR-KI-PRINCIPAL-009']
---

# GDR-KI-PRINCIPAL-016: Priority and size on work records

## Context

On 15 October Kris answered PRIORITY-FIELD: `priority` came off the records that carried it, the Streams checker and tools-ki warned on unknown record fields, and "horizon stays the only priority signal". The `ki-work` Project registry recorded that answer, and tools-ki began warning on `priority`.

By 19 October the roadmaps held over 300 records, with no field saying how important a record is among the many at one horizon or how much effort it involves. A field survey of all 316 records in the 31 registered repositories found 106 adopted open records without `kind`, 55 still on retired horizons, and several fields and values barely used or never used.

On 2026-10-19 Kris asked that "work should have a size and a priority, even if its horizon isn't now or next", accepted the recommended vocabularies and migration window, and then answered the field survey: "horizon is about when, and then priority is about how important ... I think it matter more when there is a lot of items in the roadmap and choosing what is next. so lets add it. if there isn't a priority today, default to `medium`"; size "allows us to visualise the efforts involved in the work, and ... its useful in guiding to split work up"; "we should tighten up a little"; and "yes, clean up then please". Under [SDR-KI-PRINCIPAL-004](SDR-KI-PRINCIPAL-004-the-enactment-process.md) this explicit instruction for a bounded change stands in for an Enactment record.

Two independent reviews of the fields then found the first size meanings, given in hours, unstable for agent work, the selection order unstated, and the window's close and migration unowned. At 12:04 BST on 2026-10-19 Kris amended this decision in place, answering "do everything recommended" to SIZE-MEANING, SELECTION-ORDER, FIELDS-MIGRATE, FIELDS-CORE and FIELDS-KEPT; that explicit instruction likewise stands in for an Enactment record.

## Decision

**This decision reverses the 15 October PRIORITY-FIELD answer.** Horizon says when work is intended; priority says how important it is among records at the same horizon.

**Every work record carries a priority and a size**, in local roadmaps and Knowledge Base Streams alike, written at capture whatever the horizon:

- `priority` is `high`, a material cost from deferral; `medium`, useful planned progress; or `low`, a discretionary benefit. An absent priority reads as `medium`, so its absence never warns or fails.
- `size` measures relative end-to-end effort - implementation, verification, integration and owner review, not external waiting - and not hours. It is `s`, `m`, `l` or `xl`, with delivery shapes as worked examples: `s` one run, one repository, one commit; `m` one run, several commits and a plan; `l` several chained runs or repositories, with Delegation; `xl` not one record, split before Ready. It guides splitting and capacity, never importance. A size set at capture is provisional and is revisited before Ready, and a `ready` record of size `xl` fails.

**Selection follows one order:** adoption, holds and dependencies first, then horizon, then priority, then size, smallest first. Priority never crosses horizons; a high-priority record at a later horizon prompts a proposal to move its horizon.

**Theme comes from the Project.** A record with a Project does not also name its theme; naming both warns during the window and fails after it. A projectless record may name its theme.

**A field migration window tightens the record format.** During it the checkers warn on an open record without size, on an adopted open record without `kind`, on a theme named beside a Project, and on the retired shapes below, and `ki work` lists these gaps. Closed records, done or cancelled, are exempt from a retrospective size and `kind`. The window's inventory is every registered repository holding roadmap or Streams records. It closes at whichever comes first: a complete scan of that inventory showing no gaps, in which an unavailable repository counts as unknown; or a date backstop 60 days after the `ki` release that accepts the fields. The harness checker and `ki` then fail each of these shapes. tools-ki also fails the retired horizons the harness checker already fails.

**Migration runs one repository at a time, each approved by Kris.** Mechanical changes - a retired horizon to `status: triage` or `horizon: hold`, `initiative` to `theme`, and a theme dropped beside a Project - are applied by the run. `kind` and size are proposed by the run and confirmed by the owner.

**Barely used shapes are cleaned up where nothing depends on them.** `initiative`, which the work model replaced with `theme`, and `purpose: adoption`, which no record has used, are retired, tolerated with a warning during the window. Three sparsely used shapes are kept because other rules depend on them:

- `kind: decide`, which the roadmap graduation test names for a decision with an owner and a needed-by date, and which two live records use;
- `resolution_target`, which a duplicate, merged or superseded cancellation needs to name its replacement, and which `ki-accept` requires;
- `task_links`, which the Paperclip coordination standard uses as the durable link from a record to its tasks, held for Paperclip's return and revisited when PAPERCLIP-REQ returns at Wave F.

## Consequences

- The `ki-work-roadmap` work-item format and repository-roadmap standard, the `ki-repo-kb-streams` structure, the `ki-work` adapter crosswalk and Project registry, `ki-next` capture and selection, and the harness roadmap and Streams checkers carry the fields, the window and the retirements.
- tools-ki receives one handoff for its validator and `ki work`: accept both fields and their vocabularies, read an absent priority as `medium`, list the gaps, require both at capture, warn and then fail as the harness does.
- This decision amends [GDR-KI-PRINCIPAL-005](GDR-KI-PRINCIPAL-005-the-roadmap-model.md)'s `purpose` vocabulary, which no longer includes `adoption`.
- No other repository's records are edited by this decision; each repository's migration is a separate run that Kris approves.
- Closing the window is a harness checker change made in step with the `ki` release that closes it.

## References

- [GDR-KI-PRINCIPAL-005](GDR-KI-PRINCIPAL-005-the-roadmap-model.md) - the roadmap model, whose fields this decision extends.
- [GDR-KI-PRINCIPAL-009](GDR-KI-PRINCIPAL-009-the-work-model.md) - the work model, which replaced `initiative` with `theme`.
- [SDR-KI-PRINCIPAL-004](SDR-KI-PRINCIPAL-004-the-enactment-process.md) - an explicit owner instruction for a bounded change stands in for a proposal.
- [Work-item format, Priority and size](https://github.com/knowledgeislands/ki-agentic-harness/blob/main/skills/change-management/ki-work-roadmap/references/standards-work-item-format.md#priority-and-size) - the standard that carries this decision.
