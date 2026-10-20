# ff-review - blind review of six roadmap-growth queries

Blind review. Do not read any `+/_WORK/` file (no queries.md, decisions.md, design note), and no run report. You may read the standards in ki-agentic-harness (`ki-next`, `ki-work-roadmap`, `ki-delegation`, `ki-accept`, `ki-coordination`) and Git history of KI repositories under `/Users/krisbrown/workspaces/`. No edits, commits, launches or network calls. For each query choose an option (or propose another), give a confidence (high, medium, low), a one-line reason and any condition.

Background: across 50 roadmap repositories the open record count rose from 198 to 330 between 13 and 20 October (+67%): 370 created, 212 closed; triage 30 to 106, awaiting-review 13 to 55. Of the 370 new records: 102 handoffs and sweeps, 97 opened at delivery, 85 citing an owner answer, 55 other captures, 22 run findings, 9 splits or merges. The owner wants roadmaps going down. On 19 October the owner set no roadmap size cap and no weekly cap measure.

## NET-DOWN

**Context:** A weekly direction target would expect each repository's open count to fall week on week. It is a direction measure, not a size limit, but narrows the 19 October "no weekly measure" decision. **Query:** Should each repository's open count be expected to fall week on week? **Options:** (unranked)

- Show week-on-week change per repository at each territory mark; a repository that grew gets one burn query to its owning work; no block on adoption.
- Show counts only, no target or burn query.
- Hard rule: no adoption into Now in a repository whose open count grew over the past week.

## WIP-CAP

**Context:** The roadmap standard says of Now "there is no cap". A separate agreed check warns when a work holds over about eight awaiting-acceptance records and open queries. Today apps-observatory.local alone holds 9 awaiting-review and 11 Now or awaiting-review records. **Query:** What should a per-work cap count, and at what number? **Options:** (unranked)

- One count per work (Now plus awaiting-review records plus open queries) capped at eight; over it a work only accepts, cancels, merges, prunes, finishes in-progress work and fixes blockers.
- Two caps: at most three records in progress per work, and eight awaiting-review and open queries.
- No cap; the banner shows counts only.

## CAPTURE-ORIGIN

**Context:** An existing gate says runs create no new records except blockers, defects or owner-directed items. 27 records were created after the gate, 21 from one sweep under a blanket approval. Making the gate checkable would add `origin: blocker | defect | owner` and `origin_ref` fields to the work-item format, changing `ki-work-roadmap` and the `tools-ki` model, with a rubric warning on new triage records lacking them. **Query:** Should the capture gate become a standard rule checked by an `origin` field? **Options:** (unranked)

- Write the rule into the standards with the `origin` and `origin_ref` fields and a rubric warning.
- Write the rule as prose in `ki-next` and `ki-delegation` only, with no field and no check.

## HANDOFF-AS-MESSAGE

**Context:** 102 of the week's new records came from handoffs and sweeps: one diagram redraw became records in seven repositories, one design handoff became 33 records across two. Five repositories' AGENTS.md carry a cross-repository choreography section letting several repositories add handoff items to one another's roadmaps; that would change. A receiver would lose a record visible in its own roadmap. **Query:** Should a sweep be one record in its owning repository, and a handoff a `messages.md` line rather than a record? **Options:** (unranked)

- One record per sweep in the owning repository; handoffs as `messages.md` lines; one record per product design handoff.
- Keep handoff records, but at most one per receiving repository per sweep, with steps inside it.

## STALE-SWEEP

**Context:** 39 Future drafts have a median of 51 days since update; er-agentic-harness holds 21. **Query:** Should drafts untouched for a period get a cancel-or-keep query per repository, and at what age? **Options:** (unranked)

- Yes, at 30 days, recommending cancel unless the idea is kept.
- Yes, at 60 days.
- No sweep; records stay until their lane reviews them.

## ACCEPT-BUNDLE

**Context:** 55 records await the owner's acceptance. `ki-accept` already counts "a standing human grant ... quoted source" that "covers the exact record". Bundling would put a work's awaiting-review records into one acceptance query the owner answers once. **Query:** May a work bring its awaiting-review records as one acceptance query, answered in one word, as approval of exactly the records listed? **Options:** (unranked)

- Yes: one acceptance query per work at handoff, oldest first, one line of outcome and concern per record, the answer quoting the record list in the decisions log.
- Keep one acceptance per record.

## Report

Owner report: Done (per query pick, confidence, reason, conditions), In Progress, Queries.
