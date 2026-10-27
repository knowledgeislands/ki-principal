---
title: When overloaded
status: draft
---

# When overloaded

**Goal:** get the owner back to a sensible level when too much has been said and too much is waiting for them, without losing anything. Drafted from Kris's words on 27 October 2026 in the [decisions log](<../decisions.md>), 00:25 GMT onward: "there's so much that's been said, and I've completely lost and can't follow it all ... I need to get back down to a sensible level", and "this can be generalized into a process for what we do with being overloaded".

**Scope:** what a coordinator does, in order, when the owner says they are overloaded. A draft for Kris's review; it changes no skill and adopts nothing. Each step names the skill that already owns it.

**As of:** 2026-10-27 02:50 GMT.

## The signal

The owner says, in any words, that they cannot follow it all or that too much is waiting on them. Treat it as a standing steer, not a query: stop launching discretionary work, stop asking questions, and start here.

## Steps

1. **Say the goal simply.** One or two plain sentences on where we are trying to get to, before any list, table or tag. Every later message keeps that habit: the goal first, in simple language, then the detail.
2. **Review what is there.** Count and group, in plain words, the open queries, the records awaiting review and the work running or queued. A sweep run writes it as a design note with buckets and a one-line bulk answer per bucket, as the query sweep and the roadmap sweep did.
3. **Accept what is done.** Close every record in awaiting review whose evidence holds, and prune the closed ones, so the owner's queue holds only live matters.
4. **Consolidate.** Merge duplicate records and queries, and drop queries that a standing rule already answers or that events have overtaken.
5. **Postpone rather than delete.** Move overbuilt or not yet qualified records out of the roadmap into the holding zone, full text kept, until they are brought back: "we don't need to get rid of them or delete them until we've really qualified them". The holding zone is the ideas area the holding-zone run is shaping; cancellation stays for records that are genuinely dead.
6. **Do the low-hanging fruit.** Run the quick wins the sweep found that need no decision from the owner, as bounded background runs.
7. **Put an action plan in front of the owner.** Numbered steps, one line each, saying what each needs from the owner, if anything. Nothing else runs until the plan is agreed, apart from the one thing the owner names.
8. **Ask few questions, and only then.** Bring only the questions the plan needs, as bulk one-line answers where the sweep allows. Where an answer reads one way, take that reading and log it rather than ask: "you are asking me too many questions again".
9. **Work through the plan one step at a time.** Report each step done in a line, then strike the mark.

## Where each step lives

| Step | Owning skill | What it already provides |
| --- | --- | --- |
| 1, 7, 8, 9 | `ki-coordination` | Reply forms, the Summary, queries with one recommended option, the decisions log and the mark |
| 2 | `ki-coordination` and `ki-delegation` | A sweep as a bounded run writing a design note in the work folder |
| 3 | `ki-accept` | Acceptance of awaiting-review records and the prune-only commit |
| 4 | `ki-next` and `ki-work-roadmap` | Deduplication, cancellation with a resolution, record shape |
| 5 | `ki-next` and `ki-work-roadmap` | Defer and hold moves; ideas held outside the roadmap |
| 6 | `ki-batch` and `ki-delegation` | A bounded authority envelope over an exact set of records; detached runs |

## Open points for Kris

- Whether the holding zone is `_IDEAS.md`, the owning Project note, or a new `Ideas` horizon, which the holding-zone run will propose.
- Whether step 7's gate, nothing runs until the plan is agreed, should hold for every overload or only when the owner says so.
- Where this note graduates to, if adopted: `ki-coordination` as a working rule, or the Work Process note.
