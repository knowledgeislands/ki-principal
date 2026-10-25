# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › review-surface

**🤖 → 👤 Handoff to supervisor · Run report at 18:46 BST · last mark 18:12 BST**

---

## Done

- Standard: the [ki-coordination standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md) now has a "Raising the holdings" paragraph under Work awaiting review, quoting Kris's REVIEW-SURFACE words of 19 October. It says territory work lists every `+/_WORK_REVIEW/` item at bootstrap, resume and re-anchoring and raises them as one `REVIEW-HOLD` query with a live-or-dead recommendation for each item: a live item moves into `+/_WORK/` as a work package, and a dead item is deleted with Git keeping its history. The query comes back each time until the area is empty. A matching step was added to Bootstrap (new step 5) and to Re-anchoring (new step 3), and the Mechanical boundary paragraph now mentions the warning.
- Rubric: the holding area was already counted, so the change fitted cleanly. A non-empty `+/_WORK_REVIEW/` now gives a WARN under COORD-3 instead of an INFO. The COORD-3 description, the generated `references/rubric.md` and the test were updated; the test checks that an empty area gives no warning and a non-empty one does.
- Generated surfaces: `ki dev skill generate ki-coordination` reported them in sync, but `references/rubric.md` was out of date and needed `ki dev skill rubric ki-coordination --write`; both now pass.
- Checks: `bun run test` passed (1286 tests), `bunx tsc --noEmit` passed, `ki repo audit --skill ki-skills` passed, and `ki repo audit --skill ki-coordination` gave FAIL=0 and one WARN. That WARN is the new rule firing on the harness's own holding area.
- Harness commit `eff6163b` `feat(ki-coordination): territory work raises work-review holdings` is on origin. It was my only commit ahead when pushed.
- Items in each holding area (README.md not counted; no other workspace has one):
  - hnr-principal: 1 (hnr.developer-experience-and-build-pipelines)
  - ki-principal: 5 (ki.agent-host, ki.baseline-rollout, ki.estate-factorisation, ki.paperclip-capture-and-rebuild, ki.regular.command-centre)
  - ki-agentic-harness: 1 (ki.regular.skill-reviews)
  - personal-principal: 3 (personal.personal-capture, personal.regular.acquire-dispatch, personal.regular.personal-rig)
- REVIEW-HOLD lines added, one per repository, to these territory works' `messages.md`:
  - `hnr`: commit `92eb08d`, on origin.
  - `kb`: commit `30cb22b7`, on origin.
  - `ki`: two lines, one for ki-principal and one for ki-agentic-harness, since the harness sits in the KI territory.
- The `ki` lines went in under another session's commit. My first ki-principal commit was rejected because commitlint does not allow the upper-case `REVIEW-HOLD` in a subject. While I retried with a lower-case subject, the coordinator's commit `f91c51f5` `docs(work): ki.ways-of-working ALIGN-NO-GATE` included my staged file, so the two lines are on origin under that commit and I made no ki-principal commit of my own. The hnr and personal commits kept the subject the brief gave, since their hooks accepted it.
- Nothing written in tools-ki, and no other file in those works was touched. Net change in work records: 0 in every repository.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- The lines use the brief's wording, so they read "1 items" for hnr-principal and ki-agentic-harness.
- Until each holding area is emptied, `ki repo audit --skill ki-coordination` will warn in each of the four repositories that have one. That is the intended signal.

## Queries

No outstanding queries

### 🤖 → 👤 Handoff to supervisor · since 18:46 BST

👤 0 with you

- [committed] harness standard and rubric, pushed
- [committed] REVIEW-HOLD lines in hnr, personal and ki, pushed
