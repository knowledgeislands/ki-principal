# Brief - specifications/revise

Revise the three portable spec drafts in `+/_WORK/ki.portable-specifications/design/specs/` (`specs.md`, `work.md`, `knowledge.md`, `acquire.md`) of `/Users/krisbrown/workspaces/knowledge-islands/ki-principal`, as step 3 of `design/plan.md`. Read first: `work.md` (Kris's definitions), `decisions.md` (every owner decision), `design/plan.md` (its draft review findings) and `design/agentskills-check.md` (the live Agent Skills check).

## Do

1. Apply every decision: entry files `WORK.md`, `KNOWLEDGE.md`, `ACQUIRE.md`; one validity level with soft limits warned; the optional `spec` field and other single-value added fields in `metadata` as strings, list fields placed as `agentskills-check.md` supports; the `knowledge` spec owned by a new `ki-knowledge-package` skill.
2. WORK-PROFILE: strip house ways of working from `work` (message-queue order, query form, decision pointers, `state.md` caps, routing tier) so it infers none of them, and write `design/specs/work-house-profile.md` mapping the house work package (`id`, `since`, seven states, `work.md`) onto the spec, fixing the false claim that the house already conforms.
3. Fix the plan's other findings: `knowledge` gains an audience and depth cue and puts `updated` in the first disclosure tier; `acquire` makes checksums and coverage levels proportionate to learning a tool; correct every claim `agentskills-check.md` contradicts, including "a conforming package is also a valid skill" if it fails.
4. If curation, turning captured material into a knowledge package, needs an owner, raise it as a query rather than deciding it.

Write only in `design/specs/`. Do not commit, push or publish. Never run `ki repo conform` without `--dry-run`.

## Report

Write your report as the run packet directs: Done, one line per draft with what changed; Queries in owner-query form, or `No outstanding queries`.
