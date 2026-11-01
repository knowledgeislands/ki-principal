# [Model](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › finished-tidy

**🤖 → 👤 Handoff to supervisor · Run report at 01:01 GMT · last mark 00:53 GMT**

---

## Done

- Applied the FINISHED-TIDY-KICK a) wording ([drafted note](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/finished-tidy-kick.md), Kris's choice on 1 November 2026 in the [decisions log](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/decisions.md)) to `ki-coordination` and `ki-work-package`. It is committed as `54b15997` on the local branch `finished-tidy` in the worktree `/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness-finished-tidy`, based on `main` at `a2ea2b05`. The commit has not been pushed or merged, as the brief asked.
- Checks: `bun run test` passed (1508 tests). `bunx tsc --noEmit` was clean. Focused audits of `ki-coordination`, `ki-work-package`, `ki-skills` and `ki-repo-harness` passed in an isolated home. The two COORD-8 warnings came from that empty test home, not from this change. The pre-commit hook passed and left no backup stash.
- Diff summary (7 files, 26 insertions, 27 deletions):
  - **`ki-work-package` standard, Tidying the work folder.** **Who** gains the one exception for a finished work's folder. **Close-out** gains the full territory close-out:
    - an owner-authorised mark whose report names the folder;
    - administrative only;
    - the checks: finished, decisions and durable facts homed, `design/` resolved, findings settled, no open query, empty `messages.md`, no run running or queued;
    - `ki agent close` under the strict gate first, never `--reconciled`;
    - then one `docs(work): <id> close-out` commit by explicit path;
    - if any check fails, nothing is deleted and one query goes into territory work's own `queries.md`.

    It quotes Kris's words of 30 October and records the adoption on 1 November.
  - **`ki-work-package` standard, Removal lifecycle.** The finishing coordinator deletes the folder, or territory work does at its own mark when the folder outlives the finishing thread.
  - **`ki-coordination` standard.**
    - Finishing Project work, step 4, gains the territory close-out sentence with Kris's words.
    - Pruning the work folder, Flagging, now lists "every finished work's folder", and territory work closes such a folder itself instead of sending a message line.
    - The output-style source line gains the same exception.
    - Addition beyond the draft: the Working rules **Flags** bullet ("it never prunes another work folder itself") now names the same exception. Without it, that bullet would contradict the new rule.
  - **Generated `output-styles/ki-coordinator.md`.** Regenerated from the standard.
  - **FOLDER-4 rubric check.** It is renamed from `outlivesClosingMark` to `awaitsCloseOut` and now flags every `finished` folder, whatever its mark.
    - Title: "no finished work's folder is left standing".
    - The description, guidance and message now say who closes the folder.
    - The sources add `#tidying-the-work-folder`.
    - The test now expects a flag for a finished folder whose mark is before its finish, and for one with no mark.
    - `references/rubric.md` was regenerated.
- How it was regenerated: the `--write` publishers write only to a dev-linked checkout. So the output style was rendered through the generator module, and the rubric through `ki dev skill rubric ki-work-package --write` in an isolated home dev-linked to the worktree. Both now verify clean.

## In Progress

- Nothing is running. The commit is waiting for the independent review Kris's decision requires, which the coordinator arranges. After approval, `finished-tidy` fast-forwards onto `main` and is pushed. The worktree stays in place for that review.

Outstanding - no action requested now:

- KA-CLOSE (the stranded knowledge-acquisition folder) is untouched. It is still parked with Kris in [ki.sop.main's queries](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.sop.main/queries.md).
- Optional follow-up from the blind review, not in this change: the FOLDER-4 listing could tell a folder still waiting for its closing mark apart from one that is overdue.

## Queries

No outstanding queries

### 🤖 → 👤 Handoff to supervisor · since 01:01 GMT

👤 1 with you

- [with you] independent review of `finished-tidy` (`54b15997`) · coordinator · since 01:01

🧵 ki.prj.ways-of-working
