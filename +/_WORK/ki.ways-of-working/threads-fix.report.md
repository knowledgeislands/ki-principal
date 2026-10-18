# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › threads-fix

**🤖 → 🧑 Handoff to supervisor · Run report at 18:18 BST · last mark 18:12 BST**

---

## Done

- **Stray report:** `+/_THREADS/chezmoi/host-locals-sol.report.md` was a byte-identical, untracked copy of the report already committed at `+/_WORK/ki.chezmoi/host-locals-sol.report.md` (commit aa89857, 09:17 BST), so I deleted the stray and the empty `+/_THREADS/`; with no tracked change there was nothing to commit.
- **Cause:** `ki agent` copies each finished report into the run's recorded home. Every run group except ways-of-working had `+/_THREADS/<run>/` recorded in its `thread.json`, and a new run only found its work folder by full slug, so the `chezmoi` run never matched `ki.chezmoi`. The chezmoi, observatory and tools-burndown coordinators re-homed their runs between 18:06 and 18:10 BST.
- **tools-ki, [KI-TOOL-KI-CLI-150](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-150-work-folder-entry-points.md), aa55bc49, pushed:**
  - A run now finds its work folder by slug, or for an older run by its id after the territory.
  - A run that names no work folder, or two, is refused, with no `+/_THREADS/` fallback.
  - A recorded retired home is followed into the work folder and recorded there. If there is no work folder to follow, the home can still be read, but `launch`, `decide`, `reconcile`, state-file adoption and report copying all refuse to write into it.
  - The run skeleton fills `+/_WORK/<id>` in.
  - The two "thread home" messages now say "work folder".
  - The manual, changelog and record are updated.
  - Full suite: 1,346 tests pass; the commit gate passes.
- **ki-agentic-harness, [KI-HARNESS-GOV-200](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-200-thread-folder-closed-list.md), 7d9959dc, pushed:**
  - `ki repo audit` STRUCTURE-1 now fails a `+/_THREADS/` or `+/_CHECKPOINTS/` folder that sits beside an existing `+/_WORK/`, tracked or not. Territories that have not migrated keep their tolerance warnings.
  - The work-folder standard and rubric text say so.
  - `ki-recap`'s portable hand-off now resolves only `+/_WORK/<id>/work.md`.
  - 1,253 skills and hooks tests pass; the commit gate passes.
- **ki-principal, b474492, pushed:**
  - Added a THREADS-REGRESSION Messages line to `ki` (state-of-play), `ki.knowledge-acquisition` and `ki.mac-studio-setup`. Each of these works still has its run homed in `+/_THREADS/`, and its older briefs name `+/_THREADS/` report paths. Each line gives the `ki agent home <run> --work <id>` command.
  - Another session's commit cf77950 ("restore blocked handoff after owner mark", 18:14 BST) was stacked beneath mine and went with the push.
- **Writers found, report only:**
  - Pre-migration briefs in knowledge-acquisition, mac-studio-setup and state-of-play, all finished, name `+/_THREADS/` paths.
  - The live ways-of-working briefs mention the retired paths only to forbid them.
  - No harness hook or run asset targets either path.
  - The remaining harness and tools-ki mentions only read the old folders during the tolerance window.
- **Net records:** tools-ki 0, ki-agentic-harness 0, ki-principal 0. Everything was folded into the two existing records.
- **Left alone:** other sessions' uncommitted files in ki-principal: `+/_WORK/ki.chezmoi/decisions.md`, `+/_WORK/ki.chezmoi/briefs/publish-first-step.md` and `+/_WORK/ki.ways-of-working/review-gov194-201.report.md`.
- **Report location:** this report is only in the run's state folder, as the progress protocol says, for the launcher to home and the coordinator to commit.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- The fix does not reach the installed `ki` 0.11.2 until a release. Until then the three messaged works must re-home their runs by hand, or their reports will keep landing in `+/_THREADS/`. Once a report lands there, the audit fails in ki-principal.
- The `desk-kit` run group is still homed in `+/_THREADS/desk-kit/`. No `+/_WORK/` folder names it, and its last activity was 04:29 BST.
- `hnr-build-system` is homed in hnr-principal's `+/_THREADS/`. That territory has not migrated, so the tolerance window still covers it.
- KI-HARNESS-GOV-200 also records that `ki-recap`'s `checkpoint <thread>` argument and its `checkpoint-handoff.ts` model still use the checkpoint names, left for the migration's phase 5.
- `ki agent launch` refuses a home outside `+/_WORK/`. It still does not read report paths a brief writes in its own text; KI-TOOL-KI-CLI-150's state-folder report rule covers that.

## Queries

### THREADS-RELEASE - Release ki with the retired-home fix

**Context:** The tools-ki fix is pushed but not released. Until a release ships, every run still homed in `+/_THREADS/` keeps writing there unless its coordinator re-homes it. Three works have been sent that step as a Messages line. **Query:** Should the next `ki` patch release carry this fix now, rather than waiting for the rest of KI-TOOL-KI-CLI-150? **Options:** a) (recommended, confidence high - small, tested change that stops a recurring regression) Cut a `ki` patch release with this fix in a release run, the way 0.11.2 was cut. b) Hold the release until the rest of KI-TOOL-KI-CLI-150 is built, and rely on the Messages lines meanwhile.

### DESK-KIT-HOME - Home or close the desk-kit run group

**Context:** The `desk-kit` run group's `thread.json` still names `+/_THREADS/desk-kit/`, and no work folder matches it. tools-burndown's `desk-kit-close` run has finished and the queued `desk-kit-sop` run belongs to ways-of-working. A new desk-kit run will be refused once the fix is released. **Query:** Should the ways-of-working coordinator close the `desk-kit` run group with `ki agent close desk-kit`, rather than re-home it? **Options:** a) (recommended, confidence medium - its work appears finished, but I did not check every report it left) Close it with `ki agent close desk-kit` once its gate passes, and launch any further desk-kit work under ways-of-working. b) Re-home it with `ki agent home desk-kit --work ki.ways-of-working`.

### 🤖 → 🧑 Handoff to supervisor · since 18:18 BST

🧑 2 with you

- [with you] THREADS-RELEASE · owner · since 18:18
- [with you] DESK-KIT-HOME · owner · since 18:18
- [committed] tools-ki, ki-agentic-harness and ki-principal, pushed
