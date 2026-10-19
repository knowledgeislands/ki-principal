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

On 2026-10-19 Kris asked that "work should have a size and a priority, even if its horizon isn't now or next", accepted the recommended vocabularies and migration window, and then answered the field survey: "horizon is about when, and then priority is about how important ... I think it matter more when there is a lot of items in the roadmap and choosing what is next. so lets add it. if there isn't a priority today, default to `medium`"; size "allows us to visualise the efforts involved in the work, and ... its useful in guiding to split work up"; "we should tighten up a little"; and "yes, clean up then please". Under [[SDR-KI-PRINCIPAL-004-the-enactment-process|SDR-KI-PRINCIPAL-004]] this explicit instruction for a bounded change stands in for an Enactment record.

## Decision

**This decision reverses the 15 October PRIORITY-FIELD answer.** Horizon says when work is intended; priority says how important it is, and decides the order among many records at one horizon.

**Every work record carries a priority and a size**, in local roadmaps and Knowledge Base Streams alike, written at capture whatever the horizon:

- `priority` is `high`, `medium` or `low`. An absent priority reads as `medium`, so its absence never warns or fails.
- `size` is `s` (an hour or two; one focused change), `m` (about a day; a few related changes), `l` (several days; several changes that land together) or `xl` (too large for one record; split it before it becomes Ready). It shows effort and guides splitting, and it is required. Owners backfill a missing size by judgement.

**A field migration window tightens the record format.** During it the checkers warn on a missing size, on an adopted open record without `kind`, and on the retired shapes below, and `ki work` lists these gaps. The window closes in the first `ki` release after `ki work` shows no gaps across the estate; the harness checker and `ki` then fail each of them. tools-ki also fails the retired horizons the harness checker already fails.

**Barely used shapes are cleaned up where nothing depends on them.** `initiative`, which the work model replaced with `theme`, and `purpose: adoption`, which no record has used, are retired, tolerated with a warning during the window. Three sparsely used shapes are kept because other rules depend on them:

- `kind: decide`, which the roadmap graduation test names for a decision with an owner and a needed-by date, and which two live records use;
- `resolution_target`, which a duplicate, merged or superseded cancellation needs to name its replacement, and which `ki-accept` requires;
- `task_links`, which the Paperclip coordination standard uses as the durable link from a record to its tasks, held for Paperclip's return under PAPERCLIP-REQ.

## Consequences

- The `ki-work-roadmap` work-item format and repository-roadmap standard, the `ki-repo-kb-streams` structure, the `ki-work` adapter crosswalk and Project registry, `ki-next` capture and selection, and the harness roadmap and Streams checkers carry the fields, the window and the retirements.
- tools-ki receives one handoff for its validator and `ki work`: accept both fields and their vocabularies, read an absent priority as `medium`, list the gaps, require both at capture, warn and then fail as the harness does.
- This decision amends [[GDR-KI-PRINCIPAL-005-the-roadmap-model|GDR-KI-PRINCIPAL-005]]'s `purpose` vocabulary, which no longer includes `adoption`.
- No other repository's records are edited by this decision; each owner backfills its own.
- Closing the window is a harness checker change made in step with the `ki` release that closes it.

## References

- [[GDR-KI-PRINCIPAL-005-the-roadmap-model|GDR-KI-PRINCIPAL-005]] - the roadmap model, whose fields this decision extends.
- [[GDR-KI-PRINCIPAL-009-the-work-model|GDR-KI-PRINCIPAL-009]] - the work model, which replaced `initiative` with `theme`.
- [[SDR-KI-PRINCIPAL-004-the-enactment-process|SDR-KI-PRINCIPAL-004]] - an explicit owner instruction for a bounded change stands in for a proposal.
- [Work-item format, Priority and size](https://github.com/knowledgeislands/ki-agentic-harness/blob/main/skills/change-management/ki-work-roadmap/references/standards-work-item-format.md#priority-and-size) - the standard that carries this decision.
