# Decisions - ki.portable-specifications

## Pointer - SPECIFICATIONS-PROJECT

Kris's SPECIFICATIONS-PROJECT, 19 October, in [ki.ways-of-working's decisions](../ki.ways-of-working/decisions.md), sets this Project's scope and the spec handoff.

## 2026-10-19 23:37 BST - owner decision, SPEC-HOME, SPEC-VERSION, CONFORMANCE-LEVELS

Kris: "Go with the recommendations and all the things, I'm happy with that."

Read back taken:

- SPEC-HOME a) - hold each spec as one reference in its owning skill, `ki-work-package` for `work`, `ki-acquire` for `acquire` and a new skill for `knowledge`, in the agentskills.io page format; publish the same text on the website later in this Project, with the path chosen then.
- SPEC-VERSION a) - keep the optional `spec` field, absence meaning version 1 for good, readers rejecting an unsupported major and validation checking the field.
- CONFORMANCE-LEVELS a) - one validity level per spec, soft limits warned.
- "all the things" - the plan run's steps start when it reports, within these answers; nothing is published or pushed on this authority, and the plan's own queries come back first.
- PROJECT-NAME and ENTRY-NAMES are not taken: their blind review disagreed with option a) and Kris had not seen it; asked in one line each.

## 2026-10-19 23:35 BST - owner decision, ENTRY-NAMES

Kris: "Yeah, I think entry name should be uppercase, I think that's a good idea. It seems to be the convention, right?"

Read back taken: ENTRY-NAMES a) - upper-case entry files for all three, `WORK.md`, `KNOWLEDGE.md` and `ACQUIRE.md`, with the house work package renaming `work.md` to `WORK.md`; that rename is ki.ways-of-working's, routed to its `messages.md`.

## 2026-10-19 23:44 BST - owner decision, SPEC-LIVE-READ

Kris: "SPEC-LIVE-READ as recommended"

Read back taken: SPEC-LIVE-READ a) - one read-only run, live-read, reads the live agentskills.io specification, its licence and the `skills-ref` validator source, and writes `design/agentskills-check.md`; nothing else changes.

## 2026-10-19 23:45 BST - owner decision, WORK-PROFILE, KNOWLEDGE-SKILL, MOVE-GATE, SPEC-LOCATION

Kris: "as recommended", then "mark".

Read back taken:

- WORK-PROFILE a) - the house work package stays a mapped profile of `work` with an explicit field and state mapping; the house rules move out of the spec into the profile.
- KNOWLEDGE-SKILL a) - a new governance skill, such as `ki-knowledge-package`, owns the `knowledge` spec and later its rubric.
- MOVE-GATE a) - the Project finishes at publication, with a handoff record in KI Specifications' roadmap that its restart unblocks.
- SPEC-LOCATION a) - `spec` and the other single-value added fields sit in `metadata` as strings; list fields are decided after live-read.
- Authorises: revise, one run chained after live-read, that revises the three drafts in `design/specs/` to every decision so far (plan step 3); nothing outside `design/specs/` changes, nothing is published.

## 2026-10-19 23:58 BST - owner decision, VALID-SKILL

Kris: "VA:LID_SKILL as recommended"

Read back taken: VALID-SKILL a) - every added field of `knowledge` and `acquire` sits in `metadata`, `omissions` as one string with a defined separator, and the valid-skill claim stays, qualified that the entry file is presented as `SKILL.md`; `work` lists its fields as a difference. Draft 0.2 already reads so.

## 2026-10-20 00:01 BST - owner definition, KNOWLEDGE-AS-SKILL (answers CURATION-OWNER)

Kris: "Acquire into the knowledge package isn't really a transition between the two; it's where we want to condense or take a piece of knowledge out of a particular area and factorize it into a skill, effectively. But it the focus of that skill is the knowledge rather than doing something or learning something or being able to perform an action. So really that's what I said about it being a skill extension, really, first and foremost."

Read back taken: KNOWLEDGE-AS-SKILL - a knowledge package is first and foremost an Agent Skills extension: a skill into which a piece of knowledge from a particular area is condensed and factored, whose focus is the knowledge rather than doing, learning or performing an action (his earlier "in a similar way to the way that skills work"). `acquire` does not feed `knowledge` as a pipeline stage, so CURATION-OWNER's premise falls: condensing and factoring is what making a knowledge package is, owned by the `knowledge` spec under `ki-knowledge-package`, and the drafts drop the acquire-to-knowledge transition. Authorises: revise-3, chained after revise-2, reframing `knowledge` and `specs.md` to this.

## Pointer - OVERNIGHT-AUTONOMY

Kris's overnight authority of 20 October, "You can do anything on a high confidence level that you recommend", under which LINK-FIELDS, CATALOGUE-WRITE and HOMING-REVIEW were taken below; it ended at HOLD-STOCKTAKE. Full text in Git history.

## 2026-10-20 00:28 BST - decided under OVERNIGHT-AUTONOMY, LINK-FIELDS

Query (revise-3): should the drafts keep `metadata.acquired-with` and `metadata.produces` removed, rather than keep a one-way citation field? Recommended a), confidence medium; query-review-5 (Codex, blind) recommended a), confidence high: "the existing provenance contract is sufficient; a second citation index adds synchronisation and validation obligations without a demonstrated consumer", noting a profile can establish such a need before the core standardises it.

Taken: LINK-FIELDS a), reviewed, confidence high - both link fields stay removed and the knowledge package's provenance contract is its required Sources section. The drafts say neither spec defines or requires a metadata field linking it to the other, rather than forbidding one, so profile keys stay open. Authorises revise-4 with draft-review-2's findings.

## 2026-10-20 01:13 BST - decided under OVERNIGHT-AUTONOMY, CATALOGUE-WRITE, HOMING-REVIEW

Queries (home-plan), each recommended a), confidence medium; query-review-6 (Codex, blind) recommended a) for both, confidence high, with corrections kept in [query-review-6.report.md](https://github.com/knowledgeislands/ki-principal/blob/1e930f1b/+/_WORK/ki.prj.portable-specifications/query-review-6.report.md).

Taken:

- CATALOGUE-WRITE a), reviewed, confidence high - the 6c brief allows exactly one write-mode `ki repo conform --skill ki-repo-harness` in ki-agentic-harness, every other conform staying dry-run: audit first, dry-run, check the complete proposed path set and diff, stop on any unbriefed write, re-audit after generation and after the separate SVG export. Package manifests, lockfiles and hook directories stay outside its authority. HOOK-GUARD is recorded as superseded by HOOKS-MIGRATION in ki.tools-burndown and ki.mac-studio-setup; this is a scoped exception, not a lifting of other briefs' bans.
- HOMING-REVIEW a), reviewed, confidence high - one run deduplicates and captures three harness triage records under ki-next, one each for 6a, 6b and 6c, re-reading and advancing the ledger; capture authorises no delivery. After SPEC-TEXT, each record is adopted, planned to Ready and delivered to Awaiting review with its review packet; one blind Codex review per candidate, plus the harness's tests, type-check and focused audits, replaces the plan's Steward gate for this coordinator route; Kris accepts under ki-accept. Parallel homing runs use separate worktrees and serialise integration; 6a keeps the ENTRY-NAMES prerequisite.
- Authorises now: home-amend, amending `design/home-plan.md` to these corrections, and home-records, capturing the three triage records in ki-agentic-harness, committed by explicit path and not pushed.

## 2026-10-20 02:05 BST - owner decision, HOLD-STOCKTAKE

Kris: "pause - take stock. Go On hold under current ki-coordination: drain (let a run that will end within about 15 minutes finish, stop any other at a safe point and record where), launch nothing new, commit your own work by explicit path and push only as the standard allows, park every open query, and set state.md to on-hold with reason \"take stock on ways of working\" and release \"Kris says resume\". Before the hold report, write design/retro-2026-10-20.md in your work folder with three headings, Working well, Not working and Would change, in five to ten plain bullets that cite real incidents from this work, and commit it with the hold. Then give the hold report and its resume line."

Read back taken: HOLD-STOCKTAKE - no run is active, so nothing to drain or stop; SPEC-TEXT and HOMING-EDITS are parked; state goes on-hold, reason "take stock on ways of working", release "Kris says resume"; the retro is written to `design/retro-2026-10-20.md` and committed with the hold. No push: other sessions' commits are stacked in ki-principal and ki-agentic-harness. OVERNIGHT-AUTONOMY ends with Kris's return.

## Pointer - SPEC-REVIEW (received 2026-10-28)

State of play's decision, logged on 12 October at 06:45 BST and homed here under DECISION-HOMES (Kris, 25 October), as routed by ki.prj.ways-of-working on 25 October: SPEC-REVIEW starts only once the known Knowledge Islands roadmap records are near zero; its KI-RELEASE half is spent. Received under BASELINE-CLEAN; State of play may strike its entry to a pointer here.
