# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › migrate-pass

**🤖 → 👤 Handoff to supervisor · Run report at 14:47 BST · last mark 13:37 BST**

---

## Done

- I committed the `.ki.toml` switch from `[skills.ki-work-folder]` to `[skills.ki-work-package]` on its own as `6f258c74`. The gate passed: the harness's ki-coordination already names `ki-work-package` in its working tree, so I didn't need to wait for work-package-standard to report DONE.
- The pilot, [ki.ways-of-working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/work.md), is migrated and committed on its own as `940021aa`.
  - **Carried over:** the state fields and every Next steps line were moved word for word. PAPERCLIP-REQ went to Held and the Markdown-flavour tangent to `## Parked`.
  - **Queries:** MGIT-RELEASE is open. DESK-CAM is parked, because the old file listed it as "not this work's". PUSH-STACKED is open but its text could not be recovered. The decisions log names it open at 14:17 BST, but its text was only in an unsaved Summary.
  - **Checks:** the uncommitted harness `ki-work-package` rubric passes the folder. `ki work status` cannot read it.
  - **Left alone:** the coordinator's uncommitted `decisions.md` and `design/spec-areas.md`.
- Nine more Knowledge Islands folders are migrated, one commit each. The work was done by six in-session subagents in parallel, and each folder's last commit was checked against the launch baseline before its commit. The table below gives each folder's before, after and commit.
- I wrote the two reader requests, each committed on its own with the path alone, and each cites the work-package standard's migration section:
  - `527d1a91`, in [ki.tools-burndown](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown/messages.md): `ki work status`, its help text and the man page read both shapes.
  - `5763aed5`, in [ki.observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.observatory/messages.md): the Observatory reads both shapes, `review.ts` dating moves to `state.md`, and the Work Instrument is confirmed unchanged.
  - The lines run to 67 and 62 words, a soft warning against the 60-word limit.
- **Work-package rubric:** no FAIL on any migrated folder. The soft warnings are:
  - `decisions.md` over 400 lines in `ki` and `ki.mac-studio-setup`;
  - message lines over 60 words in `ki.regular.registry-removal` and `ki.tools-burndown`, carried over word for word.
  - The only FAILs are in `ki.specifications`, another session's folder.
- **Full `ki repo audit` on ki-principal:** fails. One failure is new fallout: `ki-repo-kb` NOTE-1c rejects every `state.md` for missing `note_type`, because it exempts `queries.md` and `messages.md` but not `state.md`. The rest were already there: MD-mech on ki.chezmoi's dirty `work.md` and on `design/spec-areas.md`, ki-decision-records DEPENDS-4 and BODY-11, ki-coordination COORD-7 on ki.chezmoi's reports, and RECORD-2 in ki.specifications. Every per-commit scoped gate passed.
- **`ki work status`:** fallout. The installed reader does not read `state.md`, so the ten migrated works show only as warnings and drop out of every view. Only ki.chezmoi, still in the old shape, is listed. This lasts until ki.tools-burndown lands its both-shape reader.
- **Push:** not pushed. 32 commits are stacked on ki-principal's `origin/main`, and six belong to other sessions: ki.specifications `cd388627` and `f1e98117`; ki.knowledge-acquisition `585a7d1d` and `9011db12`; ki.chezmoi `82db4e67`. Under the brief's push rule I made no pull or push.
- **Outside this territory:** no other Knowledge Islands repository has a `+/_WORK/` folder, and the other territories were left for territories-package.

| Folder | Before | After | Commit |
| --- | --- | --- | --- |
| [ki.ways-of-working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/state.md) | single-file `work.md`, with-worker | 5 files; 2 open, 2 parked, 1 held, 1 message (FIRST-STEP) | `940021aa` |
| [ki](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/state.md) | single-file, handoff-to-supervisor, last `8abe39cd` | 5 files; Queue carried; 0 open, 4 parked (PILOT-SEED-HOME, LIVE-MAN-SWITCH, THREADS-CHECKINS, RIG-FULLSCREEN), 5 held | `fdd5f709` |
| [ki.knowledge-acquisition](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.knowledge-acquisition/state.md) | single-file, on-hold, last `9011db12` | 5 files; hold unchanged; 3 open (STATE-PLACEMENT, RECEIPT-RETENTION, PROTOTYPE-DISPOSITION), 6 parked, 2 held | `a8ae561b` |
| [ki.regular](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.regular/state.md) | single-file, on-hold, no `decisions.md`, last `319c169d` | 5 files; `decisions.md` created as `None.`; no queries | `e861e2cc` |
| [ki.regular.registry-removal](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.regular.registry-removal/state.md) | single-file, on-hold, last `6fb55992` | 5 files; THREADS-CLEAR and PMO-7-BACKLOG carried; no queries | `b58673d9` |
| [ki.baseline-rollout](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.baseline-rollout/state.md) | single-file, handoff-to-supervisor, last `7d463f09` | 5 files; seed scope to Scope; 1 open (WAVE-1, rebuilt, its original recommendation lost and said so) | `1bb3b13b` |
| [ki.mac-studio-setup](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.mac-studio-setup/state.md) | single-file, handoff-to-supervisor, last `c99dd05e` | 5 files; 2 open (RIG-ORDER; SOL-FW-TEST text lost, asks Kris); 8 parked blocks from retired reports and 5 one-line entries; 7 held | `730b01f4` |
| [ki.observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.observatory/state.md) | single-file, handoff-to-supervisor, last `21ca69bf` | 5 files; dated log to Git; 10 open, some texts recovered from the coordinator's 11:15 and 12:25 BST Summaries in its transcript, ROLLOUT-PROJECT flagged as looking resolved | `ed9a4af1` |
| [ki.timelines](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.timelines/state.md) | single-file, handoff-to-supervisor, last `49a30464` | 5 files; 7 open from `tl-seed.report.md`, PUSH-STACK flagged as looking resolved | `3f7808e4` |
| [ki.tools-burndown](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown/state.md) | single-file, handoff-to-supervisor, last `15d820ca` | 5 files; numbered log to Git; 5 open, 1 parked (ASK-B), 2 held; no `mark` field, as before | `bc130be2` |
| [ki.chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.chezmoi/work.md) | single-file, blocked, `work.md` dirty | not migrated (CHEZMOI-MIGRATE) | none |

## In Progress

Nothing is running.

Outstanding - no action requested now:

- **ki.chezmoi has uncommitted files from another session, all left untouched:**
  - `work.md` was modified by the finished run chezmoi/sol-locals-complete;
  - `decisions.md` is modified;
  - `briefs/sol-locals-complete.md` and `sol-locals-complete.report.md` are untracked.
- **Other uncommitted file:** ki.ways-of-working's `decisions.md` and `design/spec-areas.md`, which belong to its coordinator.
- **Harness fallout for work-package-standard to fold in:** ki-repo-kb NOTE-1c should exempt `state.md` as it already exempts `queries.md` and `messages.md`. I did not edit the harness.
- **Reader gap:** until ki.tools-burndown releases the both-shape `ki work status`, the migrated works are missing from every status view and from the Observatory.
- **FIRST-STEP:** each migrated folder carries an IMPORTANT FIRST-STEP line asking its worker to re-read `ki-work-package` and all five files, confirm the drafted description, Goals and Scope, and set `method_read`. Its worker owns the entries flagged "looks resolved" and the unrecovered ones (PUSH-STACKED here, SOL-FW-TEST, WAVE-1's recommendation).
- **Your pilot's FIRST-STEP line** also asks you to copy the queries from state-folder reports not yet received into `queries.md` at receive. They are fields-rest, ki-toml-switch, fields-personal-principal, work-package-enact, agentspecs-scan, spec-areas-design and mgit-filter. KITOML-GATE in ki-toml-switch is now moot: the `.ki.toml` commit passed.
- **territories-package** can start: this pass has committed.

## Queries

### CHEZMOI-MIGRATE - Migrating ki.chezmoi once its run's changes are committed

**Context:** I skipped ki.chezmoi, the eleventh live Knowledge Islands folder. Its `work.md` holds uncommitted changes from the finished run chezmoi/sol-locals-complete. They include a new `since`, rewritten next steps, three resolved Messages lines and two new queries, SOURCE-LOCALS-GATE and SOURCE-LOCALS-APPLY. Migrating the committed copy would have overwritten them or forked the state. Its coordinator has not yet received that run.

**Query:** How should ki.chezmoi reach the package shape?

**Options:**

a) (recommended, confidence high - it keeps the run's changes and its coordinator's authority over its own folder) Once ki.chezmoi's coordinator has received sol-locals-complete and committed `work.md`, relaunch a one-folder migrate run from this work. It would use the same recipe, commit on its own and leave reports for ki.chezmoi's own tidy.

b) Ask ki.chezmoi's coordinator to migrate its own folder at that receive, following `design/work-package.md` point 43.

### PUSH-OTHERS - Pushing a stack that holds other sessions' commits

**Context:** ki-principal has 32 local commits ahead of `origin/main` (not fetched). 26 belong to me or ki.ways-of-working's runs. Six belong to other sessions: ki.specifications `cd388627` and `f1e98117`; ki.knowledge-acquisition `585a7d1d` and `9011db12`; ki.chezmoi `82db4e67`. Under the brief, I made no pull or push. Until a push, other machines do not see the migrated folders.

**Query:** Should the whole ki-principal stack be pushed now, including the six other-session commits?

**Options:**

a) (recommended, confidence medium - the other commits are work-folder commits from sessions you opened today, but I did not review them) You look over the six and push the stack fast-forward, or tell this work's coordinator to push it.

b) Leave it until each session pushes its own commits.
