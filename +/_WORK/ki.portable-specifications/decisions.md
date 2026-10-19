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

## 2026-10-20 23:58 BST - owner decision, VALID-SKILL

Kris: "VA:LID_SKILL as recommended"

Read back taken: VALID-SKILL a) - every added field of `knowledge` and `acquire` sits in `metadata`, `omissions` as one string with a defined separator, and the valid-skill claim stays, qualified that the entry file is presented as `SKILL.md`; `work` lists its fields as a difference. Draft 0.2 already reads so.

## 2026-10-20 00:01 BST - owner definition, KNOWLEDGE-AS-SKILL (answers CURATION-OWNER)

Kris: "Acquire into the knowledge package isn't really a transition between the two; it's where we want to condense or take a piece of knowledge out of a particular area and factorize it into a skill, effectively. But it the focus of that skill is the knowledge rather than doing something or learning something or being able to perform an action. So really that's what I said about it being a skill extension, really, first and foremost."

Read back taken: KNOWLEDGE-AS-SKILL - a knowledge package is first and foremost an Agent Skills extension: a skill into which a piece of knowledge from a particular area is condensed and factored, whose focus is the knowledge rather than doing, learning or performing an action (his earlier "in a similar way to the way that skills work"). `acquire` does not feed `knowledge` as a pipeline stage, so CURATION-OWNER's premise falls: condensing and factoring is what making a knowledge package is, owned by the `knowledge` spec under `ki-knowledge-package`, and the drafts drop the acquire-to-knowledge transition. Authorises: revise-3, chained after revise-2, reframing `knowledge` and `specs.md` to this.
