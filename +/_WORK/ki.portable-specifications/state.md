---
id: ki.portable-specifications
state: with-supervisor
blocking: false
since: 2026-10-20T00:17Z
received: 2026-10-19T18:00Z
beat: null
mark: 2026-10-19T22:45Z
method_read: f4d6c521
---

# ki.portable-specifications state

## Now

- Every open query is decided: SPEC-HOME, SPEC-VERSION, CONFORMANCE-LEVELS, ENTRY-NAMES (upper case), PROJECT-NAME (keep apart), SPEC-LIVE-READ, WORK-PROFILE, KNOWLEDGE-SKILL, MOVE-GATE and SPEC-LOCATION, all in [decisions](decisions.md).
- live-read received: [design/agentskills-check.md](design/agentskills-check.md); `skills-ref` rejects unknown top-level keys, the spec text is CC BY 4.0, and Agent Skills sets no case rule beyond `SKILL.md`. It raised VALID-SKILL, now in query-review-4 (Codex) before it reaches Kris. revise received: draft 0.2 of all three and `design/specs/work-house-profile.md`; it already moved every added field into `metadata`, which is VALID-SKILL a) ahead of its answer. draft-review received and revise-2 received: draft 0.3 fixes all eight findings, committed. CURATION-OWNER answered by KNOWLEDGE-AS-SKILL; revise-3 received: draft 0.4 reframes `knowledge` as a skill extension. LINK-FIELDS decided a) under OVERNIGHT-AUTONOMY after query-review-5. draft-review-2 found two must-fix, three should-fix and two nits; revise-4 received: draft 0.5 fixes all seven, with a `package:<name>` notation for package references and a nested-path rule for the review to weigh; draft-review-3 confirmed six of seven fixed and found one must-fix (the validator claim) and four should-fix; revise-5 received: draft 0.6. draft-review-4 confirmed four of five fixed and found two should-fix (house link conversion, acquire omissions); revise-6 received: draft 0.7. draft-review-5 confirmed every earlier fix bar one repeated validator-behaviour claim; revise-7 received: draft 0.8. draft-review-6 found every earlier finding fixed and nothing new: ready for the owner's read. SPEC-TEXT is with Kris, kept his under OVERNIGHT-AUTONOMY; home-plan received: [design/home-plan.md](design/home-plan.md) is ready, raising HOMING-EDITS (high, folded into SPEC-TEXT), CATALOGUE-WRITE and HOMING-REVIEW, both decided a) under OVERNIGHT-AUTONOMY after query-review-6 lifted them to high. home-amend received: [design/home-plan.md](design/home-plan.md) carries both and supersedes the Steward wording in plan.md step 6. home-records received: KI-HARNESS-GOV-228, KI-HARNESS-GOV-229 and KI-HARNESS-GOV-230 captured as triage in ki-agentic-harness, committed locally, not pushed. Sent to Kris: SPEC-TEXT with HOMING-EDITS. Harness reference drift D1 and D2 are for the next `ki-skills` REFRESH.
- Mark struck at 2026-10-19T22:45Z; the Project note is [portable-specifications](../../Streams/Projects/portable-specifications.md) and the plan is [design/plan.md](design/plan.md).

## Next steps

1. On SPEC-TEXT a): adopt and plan KI-HARNESS-GOV-229 and KI-HARNESS-GOV-230 to Ready and deliver them in separate worktrees under [design/home-plan.md](design/home-plan.md); KI-HARNESS-GOV-228 after ki.ways-of-working's ENTRY-NAMES harness run. On b): one revise run and one review, then back to Kris.
2. One blind Codex review per candidate; Kris accepts each under ki-accept.
3. Publication (SPEC-PUBLISH) and the KI Specifications handoff, later.

## Held

None
