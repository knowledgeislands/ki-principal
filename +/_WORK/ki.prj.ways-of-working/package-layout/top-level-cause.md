# [Model](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › top-level-cause

**🤖 → 👤 Handoff to supervisor · Run report at 23:42 GMT · last mark 13:55 GMT**

---

## Done

- Diagnosed why run reports land beside the five package files. This was a read-only diagnosis: no file changed in any repository and nothing was committed. Every check was a read, plus one scratch Git test in the run's temporary folder.
- **Cause:** nothing in the system treats a top-level report as wrong. The launcher in `tools-ki` writes each report to `+/_WORK/<id>/<name>.report.md` by design. All three standards and the `ki-work-package` rubric list that path as allowed. Kris's PACKAGE-LAYOUT direction of 30 October, "only five top-level files", was logged, but its rollout is waiting on the open LAYOUT-SHAPE query, so no rule, check or tool ever changed.
- **Scale:** 17 work folders in 5 repositories hold 182 top-level reports (142 tracked, 40 untracked). Two packages also hold hand-made `reports/` folders with 38 files, which the current rubric fails.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- The `tools-ki` change goes to [ki.prj.tools-burndown](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.tools-burndown/messages.md) as one `messages.md` line, but only after TOP-LEVEL-NOW is answered. The draft line is under Findings.

## Findings

### TOP-LEVEL-CAUSE - Why reports land at a work folder's top level, and the smallest fix

**Goal:** find which code and rules put reports beside the five package files, and propose the smallest change set that stops it.

**Scope:** `tools-ki` at `2970714c`, the `ki-agentic-harness` source at `fb19794d` (skills `ki-work-package`, `ki-coordination`, `ki-delegation` and `ki-repo`, and the output style), and every `+/_WORK/` folder under `/Users/krisbrown/kis/*/*/`.

**As of:** 31 October 2026, 23:40 GMT.

**1. Code that writes reports at the top level (all in `tools-ki`)**

| Where | What it does |
| --- | --- |
| `src/core/agent/thread.ts:90-91` | `reportPath` returns `<work folder>/<name>.report.md`. This is the single place that decides the destination. |
| `src/core/agent/events.ts:697-722`, triggered at `:863` | `homeReport` copies the state-folder report to `reportPath` when it first sees `DONE`. Its guard against overwriting uncommitted copies relies on `git status --porcelain` (`:714-716`). |
| `src/core/agent/thread.ts:169-205` | `adoptStateFiles`, called from `close.ts:184` and from `decide` at `thread.ts:531`, moves any `*.report.md` into `join(threadPath, file)`, which is also the top level. |
| `src/core/agent/thread.ts:497-511` | `ki agent decide '<TAG> - <letter>'` looks up the option wording by reading `*.report.md` only at the work folder's top level. |
| `src/core/agent/events.ts:690-696` | `reportOf` reads the report back from `reportPath`. |
| `src/core/agent/runs.ts:162-186` | Refuses a brief that names `+/_WORK/<id>/<name>.report.md`. The pattern at `:173` matches the top level only, so a brief naming `…/reports/<name>.report.md` would get a warning, not a refusal. |
| `src/core/agent/runs.ts:628`, `:655-660` | Name-taken and relaunch checks look for the report at the top level. |
| `src/core/agent/selection.ts:184` | The acceptance check expects the reviewer's report at `workHome/<agent>.report.md`. |
| `man/ki.commands.json:486`, `:490`, `:546`, `:554`; `man/ki.1:1703-1812` | Document this behaviour as the contract. |

`ki agent home` (`thread.ts:362`) only records which folder is the home; it writes no files. No harness hook or script writes into a work folder: the only writer found is the launcher.

**2. What the standards say a work folder may hold**

| Source | Says |
| --- | --- |
| `ki-work-package` `references/standards-work-package.md:3`, `:62-82` (closed list; Run report row `:74`) | Run reports are `<name>.report.md` at the top level. Briefs go in `briefs/<run>.md` and design in `design/`. There is no `reports/` entry. |
| same file, `:98-99` | The launcher writes `<name>.report.md`, and a run never writes its report into the folder itself. |
| same file, `:129-138` | The tidy deletes reports one by one, by explicit path, once each outcome has a home. |
| `ki-delegation` `references/standards-background-runs.md:77`, `:81`, `:125` | The launcher copies the report into "the owning work folder", and the brief sits in `briefs/<name>.md`. |
| `ki-coordination` `references/standards-coordination.md:826` and Pruning the work folder (`:1117-1123`); `output-styles/ki-coordinator.md:131` | The prune keeps "the five package files, reports whose outcome is not yet homed, open briefs and live design notes". |
| `ki-work-package` rubric `scripts/rubric/items/folder.ts:8-25` (FOLDER-1, FAIL, can be lowered to WARN) and `contexts/work-folder.ts:16`, `:22-24`, `:82-92` | A top-level `*.report.md` passes. Subfolders other than `findings/`, `briefs/`, `feedback/` and `design/` fail, so both hand-made `reports/` folders fail FOLDER-1. |
| FOLDER-2 (`folder.ts:27-50`, WARN, heuristic) | Lists reports whose queries are all answered as candidates for the tidy. It never blocks. |

The three standards, the rubric and the tool agree with one another. Together they contradict PACKAGE-LAYOUT (`decisions.md:829`, 30 October). Nothing stopped the build-up because no rule considers a top-level report a fault, and the only related check (FOLDER-2) is advisory. The direction was logged as standing but parked behind LAYOUT-SHAPE (`queries.md:207`) and its pilot (`state.md:23`), so it was never applied to the rules or the tool. Slow tidying explains the volume: 142 of the reports are tracked and still there. Reports the launcher has homed but no coordinator has yet received explain the 40 untracked files, because the launcher never commits.

**3. Whether the ignore rules push reports to the top level**

Not directly: the launcher writes to the top level whatever the ignore file says. But the ignore rule blocks the obvious fix. The `ki-repo` managed block (`skills/keystone/ki-repo/scripts/rubric/contexts/gitignore.ts:70-71`, rendered as `.gitignore:6` in `ki-principal`) ignores `reports/` at any depth. That is why the 29 October hold commit `515b2adf` had to force-add 35 reports into `ki.prj.ways-of-working/reports/`. Two of its 37 files are still ignored, including `accept-by-criteria.report.md`. If reports moved into `reports/` with no exception, Git would no longer see them. The coordinator would then never commit or prune them, and the launcher's overwrite guard would see no uncommitted changes and overwrite. A negation line `!/+/_WORK/*/reports/` fixes this: in a scratch repository it re-included `+/_WORK/<id>/reports/` while `x/reports/` stayed ignored.

**4. Work folders with files other than the five at the top level**

Every stray file found is a `*.report.md`. No other kind of file appeared.

| Repository | Work folders | With extras | Reports tracked | Reports untracked | Hand-made `reports/` |
| --- | --- | --- | --- | --- | --- |
| `knowledge-islands/ki-principal` | 16 | 4 | 49 | 29 | 1 (37 files, 35 tracked) |
| `humans-not-robots/hnr-principal` | 26 | 7 | 59 | 0 | 1 (1 file, tracked) |
| `personal/personal-principal` | 10 | 4 | 32 | 11 | 0 |
| `legal/legal-principal` | 1 | 1 | 1 | 0 | 0 |
| `valle-armonia/va-principal` | 4 | 1 | 1 | 0 | 0 |
| `equal-remedy/er-principal`, `personal/acquire`, `sacred-inquiry/si-principal`, `techmedix/tmx-principal` | 1 each | 0 | 0 | 0 | 0 |

The folders with the most are `ki.prj.observatory` (42), `ki.prj.ways-of-working` (25), `hnr.prj.developer-experience-and-build-pipelines` (23), `personal.reg.tower` (21), `personal.reg.rig-terra` (20) and `hnr.prj.5g-emerge-p2ms3` (16). After them come `hnr.sop.main` (9), `ki.sop.main` (7), `hnr.prj.5g-emerge-phase2` (5), `ki.prj.mac-studio-setup` (4) and seven folders with one or two each.

**5. Smallest fix that works with today's kind-first folders, without settling LAYOUT-SHAPE**

The fix is to move the report destination from the top level to `reports/<name>.report.md`. This matches layout A and is the first half of layout B (a `reports/` folder inside each group). Under layout C the reports would move a second time, into a group folder. It is the only target the launcher can work out without knowing a group, and in the tool it is essentially one function, `reportPath`, plus the places that bypass it. Nothing about grouping is decided by it. The tolerance step warns, rather than fails, on reports still at the top level, so the sweep can follow.

**Proposed change set, by owner**

- **Harness skills (this work):**
  - `ki-work-package`: change the closed list's Run report row to `reports/<name>.report.md` (`:74`), plus the lines at `:3` and `:98-99` and the tidy wording at `:131-133`.
  - `ki-work-package` rubric: add `reports` to the allowed subfolders, accepting `*.report.md` only (`work-folder.ts:24`). Treat a top-level `*.report.md` as a stray file (`:85`), at WARN during a tolerance window and FAIL after it. Point the brief check at `reports/` (`:127`), and update the FOLDER-1 description (`folder.ts:12`).
  - `ki-delegation`: say "homes it in the work folder's `reports/`" at `:77`, `:81` and `:125`.
  - `ki-coordination`: make the same change in the prune wording (`:826`, `:1117-1123`) and in `output-styles/ki-coordinator.md:131`.
  - `ki-repo` managed ignore block (`gitignore.ts:70-71`): add `!/+/_WORK/*/reports/` and `!/+/_WORK_REVIEW/*/reports/`. `ki-repo` is a harness skill that this work's brief did not list as one it owns, so the coordinator should confirm the owner.
- **`tools-ki` (a `messages.md` line for [ki.prj.tools-burndown](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.tools-burndown/messages.md)), once TOP-LEVEL-NOW is answered:**

  ```text
  From ki.prj.ways-of-working: home run reports into +/_WORK/<id>/reports/<name>.report.md, not the top level, under PACKAGE-LAYOUT (30 Oct). Change reportPath (thread.ts:91) and the paths that bypass it: adoptStateFiles (thread.ts:195), decide's TAG lookup (thread.ts:497-511, reading the old top level too during tolerance), homeReport/heldAs (events.ts:708-722, checking both old and new names so retired reports stay retired), the refusal pattern (runs.ts:171-174, to cover reports/), name and relaunch checks (runs.ts:628, 655-660), reviewer path (selection.ts:184), the man pages and tests. Depends on the ki-repo ignore exception !/+/_WORK/*/reports/ landing first.
  ```

- **One-off sweep (after both changes land):** each folder's own steward runs a tidy at its next mark. It deletes each report whose outcome already has a home, and `git mv`s the rest into `reports/`, one commit per folder by explicit path. State of play sends one `messages.md` line to each of the 17 folders. The two hand-made `reports/` folders already match the target and need only their two ignored files tracked.

## Queries

### TOP-LEVEL-NOW - Move reports into `reports/` now, or wait for the layout decision

**Context:** On 30 October Kris directed that a work package keeps only its five files at the top level. The rules and the launcher were never changed, because the choice of grouping layout (LAYOUT-SHAPE) is still open, so reports keep landing at the top level: 182 of them across 17 folders today. The quickest stop is to have the launcher and the rules put every report in a `reports/` folder inside the package. That needs one change to the shared ignore rules, because `reports/` folders are currently hidden from Git. It fits the "kind-first" layout and the "group with `reports/` inside" layout. If Kris later picks the flat group layout, reports would move a second time.

**Query:** Should reports go into a `reports/` folder now, ahead of the layout decision?

**Options:**

a) (recommended, confidence medium - it carries out the 30 October direction at once with the smallest change and settles nothing about grouping, but may mean a second move if the flat group layout wins) Yes: change the launcher, the rules and the ignore exception to use `reports/` now, and keep LAYOUT-SHAPE open.

b) No: answer LAYOUT-SHAPE first and make one change, to the chosen layout, accepting that reports keep arriving at the top level until then.

c) Neither layout change for now: keep reports at the top level and tidy every package strictly at each mark.

### TOP-LEVEL-SWEEP - How to clear the reports already at the top level

**Context:** 182 reports sit at the top level of 17 work folders in five repositories. Most belong to other work, so each folder has its own steward. Many of these reports probably already have a durable home and could simply be deleted. Deciding that is each steward's judgement, and the rules forbid deleting a whole folder in one go.

**Query:** Once the change lands, who clears the existing reports?

**Options:**

a) (recommended, confidence medium - it keeps each deletion with the steward who can judge it, but takes as long as the slowest package's next mark) Each folder's steward tidies at its next mark, deleting reports with a home and moving the rest into `reports/`, prompted by one `messages.md` line from State of play per folder.

b) One bounded sweep run per repository moves every top-level report into `reports/` with no deletions, and stewards prune later.

---

### 🤖 → 👤 Handoff to supervisor · since 23:42 GMT

👤 2 with you

- [with you] TOP-LEVEL-NOW · owner · since 23:42
- [with you] TOP-LEVEL-SWEEP · owner · since 23:42

🧵 ki.prj.ways-of-working
