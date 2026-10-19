---
id: ki.portable-specifications
state: with-worker
blocking: false
since: 2026-10-19T22:45Z
received: 2026-10-19T18:00Z
beat: null
mark: 2026-10-19T22:45Z
method_read: f4d6c521
---

# ki.portable-specifications state

## Now

- Every open query is decided: SPEC-HOME, SPEC-VERSION, CONFORMANCE-LEVELS, ENTRY-NAMES (upper case), PROJECT-NAME (keep apart), SPEC-LIVE-READ, WORK-PROFILE, KNOWLEDGE-SKILL, MOVE-GATE and SPEC-LOCATION, all in [decisions](decisions.md).
- live-read received: [design/agentskills-check.md](design/agentskills-check.md); `skills-ref` rejects unknown top-level keys, the spec text is CC BY 4.0, and Agent Skills sets no case rule beyond `SKILL.md`. It raised VALID-SKILL, now in query-review-4 (Codex) before it reaches Kris. revise received: draft 0.2 of all three and `design/specs/work-house-profile.md`; it already moved every added field into `metadata`, which is VALID-SKILL a) ahead of its answer. draft-review received and revise-2 received: draft 0.3 fixes all eight findings, committed. CURATION-OWNER answered by KNOWLEDGE-AS-SKILL; revise-3 received: draft 0.4 reframes `knowledge` as a skill extension and drops the link fields, raising LINK-FIELDS, now in query-review-5 (Codex). draft-review-2 (Codex) reviews draft 0.4. Then SPEC-TEXT. Harness reference drift D1 and D2 are for the next `ki-skills` REFRESH.
- Mark struck at 2026-10-19T22:45Z; the Project note is [portable-specifications](../../Streams/Projects/portable-specifications.md) and the plan is [design/plan.md](design/plan.md).

## Next steps

1. Receive query-review-5 and draft-review-2; LINK-FIELDS to Kris; any fixes in one revise run.
2. Revised texts to one blind review, then SPEC-TEXT to Kris (plan step 5).
3. On SPEC-TEXT: home the specs in `ki-work-package`, `ki-acquire` and a new `ki-knowledge-package` in ki-agentic-harness, in parallel (plan step 6).

## Held

None
