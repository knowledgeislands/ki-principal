# [Model](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › acquire-held

**🤖 → 👤 Handoff to supervisor · Run report at 12:41 GMT · last mark 01:41 GMT**

---

## Done

- `ki-acquire` now uses Acquire's final structure (harness `91d8d98a`): `processed/` became `curated/`, `captures/_review/` became `captured/_held/` (holding: material awaiting incorporation; review now means comments, findings and proposed changes), `context/` is described as the routing graph with its typed links and one-way rule, `actions/` is named, and the old intake package id now reads `personal.reg.assistant-terra`. The skill was not renamed.
- `ki-acquire-granola` now sends mixed-territory and unmapped meetings to `<capture_root>/_held/granola/` (same commit).
- Checks: `bun run test` passed (1511 tests); `bunx tsc --noEmit` passed; focused audits for `ki-acquire` and `ki-acquire-granola` passed; Markdown lint passed on the three changed files.
- Line ACQUIRE-HELD sent to [ki.prj.tools-burndown messages](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.tools-burndown/messages.md) (ki-principal `83fec84d`), naming the four tools-ki places still writing `_review`. The messages named no other owner.

## In Progress

Nothing is running.

Outstanding - no action requested now: until tools-ki changes, a Granola import still writes `_review/`, and Acquire moves those packages to `_held/` by hand.

## Queries

### CURATE-STRIKE - The harness still says curation deletes captured items, while Acquire now strikes them through

**Context:** Acquire's own text now says curation strikes each curated part of a capture through, keeping the original text inside the strike, with a note naming where it went, and never deletes an unfinished capture. A capture is deleted only once every part is struck. The harness standard (Staging and curation) and rubric item ACQUIRE-6 still say each curated item is deleted from its capture in the same commit, under the 31 October decision ACQ020-RETIRE. Acquire's text is the authority here for now (ACQ020-OWNER). This run was scoped to names, so the rule was left unchanged.

**Query:** Should a follow-up run bring the harness curation rule and ACQUIRE-6 into line with Acquire's strike-through rule?

**Options:**

a) (recommended, confidence high - Acquire's own text is the authority under ACQ020-OWNER and states the rule plainly) Yes: send a short harness run to rewrite the curation paragraph and ACQUIRE-6 to strike-through, quoting Acquire's text, with tests and audits.

b) No: keep the deletion wording until Acquire intake confirms the strike rule is final.

### 🤖 → 👤 Handoff to supervisor · since 12:41 GMT

👤 1 with you

- [with you] CURATE-STRIKE · owner · since 12:41

🧵 ki.prj.ways-of-working
