# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › review-cli150

**🤖 → 👤 Handoff to supervisor · Run report at 08:07 BST · last mark 20:20 BST**

---

## Done

- I reviewed tools-ki `949ff512` and ki-agentic-harness `1fe52516` against the launch part of [KI-TOOL-KI-CLI-150](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-150-work-folder-entry-points.md) and its review packet. The review was read-only: I made no edits, commits, pushes or acceptance. Net records: 0 in every repository.
- Verdict: clean. Every acceptance criterion holds, the recorded deviation is sound, and there are no blocking findings. I found three minor points (below), and none needs fixing before acceptance.
- Verify 1 (the skeleton names the state-folder report path): holds. `newPrompt` fills in `stateReport`, and the test asserts the full draft.
- Verify 2 (launch, queue and relaunch refuse with exit 1 and write nothing): holds. The refusal runs before the run's home is recorded, before any `mkdir`, before a relaunch sets the earlier packet aside, and before the queue's `copyFile`. The test covers an absolute path, a path as written and another work folder's path, and checks that the state folder, temporary folder and queue are empty. The message matches Decision 2.
- Verify 3 (warnings): holds. Citing another agent's report and a bare name draw nothing, and a `docs/` path still warns.
- Verify 4 (the dispatcher): holds. The dispatcher logs the refusal as `failed` with its text, and the next queued agent launches. The test covers both.
- Verify 5 (harness): holds. Both commits are on `origin/main` (I checked local refs only and did not fetch). The `ki dev skill generate ki-coordination` check reports the generated surfaces in sync. The skeleton and prompt shape carry the agreed wording.
- Verify 6 (no live brief sends its own report into a work folder), which I reran: holds across all 21 queued briefs and 3 common-rules files under `~/.local/state/ki/agents/`. I read the five rewritten step-2 files, and each names its own state-folder path. `work-folder-design.queued.md` names none. The work file's next step 4 records step 2 as done, which closes the cli150-deliver report's open item.
- The deviation (the refusal runs before the run's home is written): sound. With `write` false, `threadHome` only reads (`readThread`, `runWorkFolder`) and writes nothing. Without the deviation, a refused first launch would leave `thread.json`, which breaks Decision 2's "before anything is written". The cost is that the home is resolved twice, which is cheap.
- Checks I reran: the `ki agent` tests passed (58), and `tsc --noEmit`, Biome on the changed files and `mandoc` lint were clean, all on a clean `949ff512` tree. The full `test:coverage` run passed (1,350 tests, thresholds met). That run happened after another session left uncommitted Biome-fix edits in the tree (`biome.json`, `src/commands/acquire/index.ts`, `src/core/kb/authority.ts` and four test files), so it tested 949ff512 plus those edits. I did not touch those files. Repo-wide `biome check .` is the known drift that BIOME-DRIFT a) already covers.
- Minor 1, a scope gap the record allows: Decision 1 refuses only reports placed directly in a work folder. A brief naming `+/_WORK/<id>/design/<name>.report.md`, `+/_WORK_REVIEW/...` or `$D/<name>.report.md` gets a warning, not a refusal. This matches the record, and the coordinators' move removed every live `$D/<your name>` line.
- Minor 2, a leftover file: when the dispatcher refuses a queued brief, its `<name>.queued.md` copy stays in the state folder. Every other dispatcher launch failure already leaves it the same way. It does no harm, because the copy does not take the name.
- Minor 3, an unhelpful message: for a run whose recorded home is a retired `+/_THREADS/<run>/` with no work folder to follow, a brief naming `+/_THREADS/<run>/<name>.report.md` is refused with "the launcher homes it in .../+/_THREADS/<run>". A clearer error would say the run names no work folder. This case is rare, nothing is written, and the outcome is still a refusal.

## In Progress

- Nothing. Acceptance of KI-TOOL-KI-CLI-150 waits for Kris (CLI-150-ACCEPT). The release under KI-RELEASE-NEXT a) should rerun Verify 6 first, as planned.

## Queries

### CLI-150-ACCEPT - Accept KI-TOOL-KI-CLI-150's launch part

**Context:** The independent review found every Verify item met by tools-ki `949ff512` and ki-agentic-harness `1fe52516`. The deviation (the refusal runs before the run's home is written) is sound. The three minor points are within the record's scope or already true before this change. Coverage, types, the changed files' lint and the harness generator all pass, and the repo-wide Biome failure is left to BIOME-DRIFT.

**Query:** Do you accept KI-TOOL-KI-CLI-150 as delivered, so that `ki-accept` can close it and the v0.11.4 release can go ahead?

**Options:** a) (recommended, confidence high - every criterion verified independently, and no finding blocks) Accept as delivered, recording the three minor points as known limits rather than follow-up records. b) Accept, and capture one tools-ki record for Minor 1 (also refuse subfolders of a work folder and `+/_WORK_REVIEW/`). c) Hold acceptance until Minor 3's message names the missing work folder.
