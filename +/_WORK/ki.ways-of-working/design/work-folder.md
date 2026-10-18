# Work folder: inventory, writers and ownership

Design note for the ways-of-working work, written by the `work-folder-design` run on 18 October 2026 under Kris's message of that morning, logged as "owner message, work-folder skill": "we want a skill that's managing things that are under +/_WORK/ID, right? ... what skill is responsible for making sure that it's clean and tidy ... we just need to consider what the confidence is in terms of other files or things that might change things in there."

Status: draft, for the owner's decision under WORK-FOLDER-OWNER, WORK-FOLDER-NAME and WORK-FOLDER-CHECKS in the run report. It changes no skill, code or record.

Citations are `<repository>:<path>:<line>` at these revisions: ki-agentic-harness `0b95efbb`, tools-ki `857d53ca`, apps-observatory.local `db28ae3`. The renames of `ki-pmo` to `ki-coordination` and `ki-pmo-design` to `ki-work-design` were in flight, uncommitted, in the harness working tree while this note was written, so citations use the committed `ki-pmo` paths. Shorthands: `pmo` is `ki-agentic-harness:skills/change-management/ki-pmo/references/standards-pmo.md`, `wf` is `ki-agentic-harness:skills/governance/ki-checkpoint/references/standards-checkpoints.md`, `run` is `ki-agentic-harness:skills/governance/ki-delegation/references/standards-background-runs.md`.

## 1. Inventory

Only Knowledge Islands Principal has live `+/_WORK/` folders today (eight). `+/_WORK_REVIEW/` exists in Knowledge Islands Principal (five folders) and the KI Agentic Harness (one). Every other territory still holds `+/_THREADS/` or `+/_CHECKPOINTS/` for the tolerance window: Equal Remedy, Humans Not Robots, Legal, Personal (and `acquire`), Sacred Inquiry, TechMedix and Valle Armonia.

| Kind | Path | What it is | Live evidence |
| --- | --- | --- | --- |
| Work file | `work.md` | Current state: closed front matter, `Next steps`, `Messages`, `Parked` | Every folder |
| Messages line | `work.md` `## Messages` items | A send from other work, `FIRST-STEP` first | `ki.tools-burndown` holds a `FIRST-STEP` from ways of working; all nine work files hold a `MIGRATED` line in a non-standard shape |
| Decisions log | `decisions.md` | Owner decisions, in their words, for the work's whole life | Every folder but `ki.regular`; headings are mixed: ways of working has 200 `## Decision <n> (<time>)` entries to 17 October, then 59 `## 2026-10-18 10:05 BST - owner answers, ...` entries under the work model |
| Run report | `<name>.report.md` | An agent's final owner report, homed by the launcher | 116 across five folders: `ki.tools-burndown` 44, `ki.ways-of-working` 35, `ki.chezmoi` 18, `ki` 14, `ki.mac-studio-setup` 5 |
| Coordinator-saved report | `<name>.report.md` | A coordinator's own Summary saved beside run reports | `overnight-summary`, `morning-summary`, `morning-refresh`, `wrap-ways-20261018`, `resume-20261016` |
| Brief | `briefs/<run>.md` | A run's brief while its handoff is open | `ki.chezmoi/briefs/host-locals-sol.md`, `ki.tools-burndown/briefs/next-worker.md`, `ki.ways-of-working/briefs/work-migration.md` (migration done) |
| Design note | `design/<slug>-*.md` | Options papers, briefs, reviews, merged reports, stage decisions | `ki`, `ki.mac-studio-setup`, `ki.tools-burndown`, `ki.ways-of-working` |
| Design artefact | `design/*.svg`, `design/*.architecture.json` | Diagram sources and renders | `ki.ways-of-working/design/work-model.*`, `change-management-skills.*` |
| Design subfolder | `design/<subject>/` | Nested design sets | `bring-up/`, `migration-plan/{capital,territory}/`, `themes/`, `observatory-goals/` |
| Scratch under design | `design/scratch/`, `design/screens/` | Scripts and screenshots | harness `+/_WORK_REVIEW/ki.regular.skill-reviews/design/scratch/` holds `dump.ts`, `shoot.ts`, `old/`, `old-png/` |
| Review index | `+/_WORK_REVIEW/README.md` | One line per folder awaiting review | Both review areas |
| Review folder | `+/_WORK_REVIEW/<id>/` | Migrated work not yet judged live, same shape | Six folders |

Bound to the folder but outside it: the run state folder `~/.local/state/ki/agents/<slug>/`, whose `thread.json` records the work folder as the run's home; the native-session binding `~/.local/state/ki/threads/<repository>/<slug>.json`; and temporary output under `tmp/<run>/<name>/`.

## 2. Writers, readers and deleters

C create, E edit, R read, D delete.

| Kind | Party | C/E/R/D | Where |
| --- | --- | --- | --- |
| `+/_WORK/` area | `ki-repo` | owns `+/` scaffold; names the split of owners | `ki-agentic-harness:skills/keystone/ki-repo/references/standards-repository.md:128-129`; coverage signal `.../standards-configuration.md:241` |
| | `ki-checkpoint` audit STRUCTURE-1 | R: holds only work folders | `ki-agentic-harness:skills/governance/ki-checkpoint/scripts/rubric/items/structure.ts:7-20`; `wf:34` |
| | `ki-repo-kb` | exempts `work.md` from note front matter | `ki-agentic-harness:skills/repo-structure/ki-repo-kb/references/standards-frontmatter.md:25` |
| `work.md` | Coordinator (ki-pmo) | C at bootstrap or seeding; E at every send, receive, mark and hold; D at the closing mark | `pmo:696`, `pmo:736`, `pmo:634`, `pmo:854`, `pmo:787` |
| | `ki-checkpoint` | defines the schema; UPDATE, RESUME, REMOVE procedures | `wf:30-100`, `wf:136-167`; `ki-agentic-harness:skills/governance/ki-checkpoint/SKILL.md:66-70` |
| | Conversational session | C/E its own ad hoc work file | `pmo:424-428` |
| | `ki-recap checkpoint <id>` | supplies evidence to an UPDATE, no own write | `wf:146-150` |
| | Other work | E: one Messages line, that path alone | `wf:142`; `pmo:745` |
| | Territory work | E: Messages lines naming PMO-9 flags | `pmo:697`, `pmo:836` |
| | Migration run (one-off) | C: moved checkpoints in, wrote `MIGRATED` lines | `+/_WORK/ki.ways-of-working/briefs/work-migration.md` |
| | `ki work status` | R | `tools-ki:src/core/work/status.ts:260-272` |
| | Observatory | R through `ki work status` only | `apps-observatory.local:packages/evidence/src/work.ts:4-8` |
| | `ki agent home`, launch | R: `work.md` presence picks the run's home | `tools-ki:src/core/agent/thread.ts:28-46`, `:257-271` |
| | `ki repo audit` | R: STRUCTURE-1/2, PMO-1, PMO-2, PMO-10, PMO-3 | `structure.ts:7-24`; `ki-agentic-harness:skills/change-management/ki-pmo/scripts/rubric/items/threads.ts:7-61` |
| | Runtime reminder consumer | R, opt-in, not built | `wf:123-134` |
| | `coordinator-reminder.sh` hook | none: reads only `.ki.toml` | `ki-agentic-harness:hooks/coordinator-reminder.sh:42-55` |
| `decisions.md` | Coordinator | C/E by hand in the turn a decision arrives; strikes or points entries at the mark | `pmo:203`, `pmo:680`, `pmo:770`; `run:144` |
| | `ki agent decide` | C (`# Decisions`), E: appends `## Decision <n> (<time>)`, expands `TAG - a` from reports | `tools-ki:src/core/agent/thread.ts:355-414` |
| | `ki agent reconcile` | E: `home:` and `class:` lines | `thread.ts:420-453` |
| | `ki agent decide`, `close` | C: move a state-folder log in if the folder has none | `thread.ts:107-128`; `tools-ki:src/core/agent/close.ts:182` |
| | `ki agent close` gate | R: parses `## Decision <n>` headings only | `thread.ts:296`; `close.ts:85-118` |
| | Design loop | E: its answers also logged here | `pmo:772` |
| | PMO-9 | R: Needs tags to judge reports answered | `threads.ts:125-140`; `ki-agentic-harness:skills/change-management/ki-pmo/scripts/rubric/contexts/pmo.ts:640-677` |
| | Observatory review queue | R: tags only | `apps-observatory.local:packages/evidence/src/review.ts:4-8` |
| `<name>.report.md` | Launcher (`ki agent`) | C/E: copies the state-folder report in on `DONE`; replaces only a Git-clean copy; adopts state-folder reports at decide and close | `tools-ki:src/core/agent/events.ts:152-174`, `:227`; `thread.ts:107-128` |
| | Launcher | R: refuses a name whose report exists; refuses relaunch over an uncommitted report; warns when a brief names another report path | `tools-ki:src/core/agent/runs.ts:300-345`, `:109-118` |
| | Background agent | C: should write only to the state folder; briefs often name the work-folder path too (this run's did) | `run:68`; `runs.ts:109-118` |
| | Coordinator | C: saves own Summaries as reports (observed); D at send and mark, by explicit path | `pmo:831-835`; `run:149` |
| | `ki repo audit` | R: PMO-7, PMO-11, PMO-12, PMO-9 | `threads.ts:74-140` |
| | Observatory | R: Queries tags and one sentence each | `review.ts:4-8` |
| | Recap, full summary | R, including from Git after a prune | `pmo:673`, `pmo:803` |
| `briefs/<run>.md` | Coordinator | C (short brief); D once the report is received | `pmo:178`, `pmo:831` |
| | Background agent | C when the brief needs research | `pmo:178` |
| | `ki agent new`, `queue`, `launch` | none here: drafts, queued briefs and prompts live in the state folder | `runs.ts:685-698`; `run:55-56` |
| | `ki agent sweep` | none here: deletes only spent state-folder briefs and old archives | `tools-ki:src/core/agent/sweep.ts:70-80` |
| | PMO-9 | R: accepts `briefs/` wholesale; does not test a brief's report | `pmo.ts:36-37` |
| `design/` | `ki-pmo-design` | C/E: brief, reviews, merged report, decisions file | `ki-agentic-harness:skills/change-management/ki-pmo-design/SKILL.md:31`; `.../references/standards-pmo-design.md:23` |
| | Design runs | C/E notes and diagrams (this note) | brief practice |
| | Delivery that homes a note | D in the same change on graduation | `pmo:778` |
| | Coordinator at finish | D: resolves `design/` before Finished | `pmo:785` |
| | `ki-repo-kb-streams` | forbids `design/` under `Streams/` | `ki-agentic-harness:skills/repo-structure/ki-repo-kb-streams/references/standards-streams-structure.md:30` |
| | PMO-9 | R: accepts any content | `pmo.ts:36-37` |
| Whole folder | Coordinator | D at the mark that closes finished work | `pmo:787`; `run:151`; `wf:165` |
| | `ki agent close` | R: folder committed and clean, else blocker | `close.ts:120-129` |
| `+/_WORK_REVIEW/` | ki-pmo | owns; owner or the work at its mark moves a folder out by `git mv` or deletes it | `pmo:877-883`; `standards-repository.md:129` |
| | `ki work status`, PMO rubric | R: count only | `status.ts:320-323`; `pmo.ts:441-448` |
| | Observatory | R: name and time, never opened | `review.ts:10`, `:172` |
| | `ki-checkpoint` | skips until the folder leaves review | `wf:34` |
| Any file | Kris by hand | anything; every commit's author is Kris Brown, so authorship gives no signal, only the co-author trailer | `git log -- +/_WORK` |

## 3. Confidence

The prose today puts the folder in three skills and the code in a fourth:

- `ki-checkpoint` owns `work.md` and that `+/_WORK/` holds only folders (`wf:26`, `wf:34`).
- `ki-pmo` owns the closed list, pruning, close-out, the decisions life cycle, design notes and the review area (`pmo:825-836`, `pmo:780-787`, `pmo:877-883`; `standards-repository.md:128-129`).
- `ki-delegation` restates the closed list (`run:68`, `run:70-74`), the prune (`run:149`) and the finishing delete (`run:151`), and says "`ki agent` is the only writer of the decisions log and report files" (`run:76`).
- `tools-ki` holds the only code that writes there.

The restatements already disagree. `run:68` lists `briefs/` where `pmo:829` lists `briefs/<run>.md`. `run:76` makes `ki agent` the log's only writer, but `pmo:203`, the output style and live practice have the coordinator write it by hand. `run:140` says entries carry no numbers, but `ki agent decide` numbers them, and the close gate reads nothing else.

There is one ownership gap. The prune and close-out are written for "each coordinator" (`pmo:835`). Regular and ad hoc work (`ki.regular`, `ki.regular.registry-removal`, the review folders) has a work folder but no coordinator, so nothing tells it how to stay tidy.

Party by party:

| Party | Must it write in the folder? | Confidence that a named entry point holds it | Why |
| --- | --- | --- | --- |
| Folder owner skill | It sets the rules | High | Nothing stops one skill owning shape, naming, closed list, prune, close-out and review area: the consumers only read |
| Coordinator | Yes: `work.md`, `decisions.md`, briefs, deletions | High | It is the folder's steward. The owner skill says how; ki-coordination says when and judges durable homes |
| Launcher (`ki agent`) | Yes: reports, and adopted logs | High | One code path (`homeReport`, `adoptStateFiles`). It already refuses to overwrite uncommitted copies and never deletes |
| Background run | Design notes; reports only via the launcher | Medium | Briefs routinely name the work-folder report path. The launcher only warns (`runs.ts:109-118`), and a run that writes there directly races `homeReport`. Today's uncommitted `harness-followups.report.md` shows reports landing between commits |
| Other work | One Messages line | Medium | The rule exists (`pmo:745`), but the live `MIGRATED` lines and the "None open. Acted on..." item in `ki.tools-burndown` show the shape drifting, and no tool or check holds it |
| `ki-pmo-design` | `design/` contents | Medium | Graduation and deletion are clear (`pmo:778`), but nothing limits what `design/` holds. Scratch scripts and screenshots sit there against the temporary-output rule (`pmo:833`) |
| `ki agent close` | Reads only | Low today | The gate parses only `## Decision <n>` headings. Ways of working's log has 200 such entries, to 17 October. The 59 timestamp-headed entries written under the work model, which the standard requires, pass the gate unchecked |
| Readers (`ki work status`, observatory, rubrics) | No | High | Read-only. They depend on the shape, so a shape change has to list them as consumers |
| Kris by hand | Anything | Not enforceable | Audit catches drift afterwards; the review area expects his `git mv` |

The safe contract is the one the brief proposes, made explicit:

1. **One owner sets the shape and the tidy rules**: closed list per kind, what each entry point may write, when each kind goes, and how a deletion is made (explicit-path `git rm`, one commit).
2. **Every other writer is a named entry point**, with its single permitted kind:
   - the launcher writes `<name>.report.md` and adopts `decisions.md`;
   - the coordinator writes `work.md`, `decisions.md` and `briefs/`;
   - `ki-work-design` and design runs write `design/`;
   - other work writes one Messages line.
3. **Only the folder's own work deletes.** The launcher, runs, other work and tools never delete there.
4. **A check backs each entry point mechanically.** The judgement (has this outcome a durable home?) stays with the work's own steward.

## 4. Recommended division

| Concern | Owner | Notes |
| --- | --- | --- |
| `+/_WORK/` and `+/_WORK_REVIEW/` shape, naming, closed list per kind, entry-point table, tidy rules (prune at send and mark, close-out delete, review in and out, no scratch), Messages line shape | **Work-folder skill** (renamed `ki-checkpoint`) | Absorbs the work-file schema, `pmo:821-836` (committing and pruning), `pmo:877-883` (review area) and close-out step 4; applies to every level, coordinated or not |
| When to tidy (send, mark, hold, finish), judging durable homes, the decisions log's entry form and life cycle, the report forms, acting on Messages | **ki-coordination** (was `ki-pmo`) | Links to the work-folder skill for what is kept and how a prune is made |
| Run packet, state folder, launcher behaviour, brief and report paths for runs, close gate | **ki-delegation** | Drops `run:68-74`, `run:149` and `run:151` to one pointer each; corrects `run:76` to "the launcher is the only writer of report files; the coordinator writes the log"; the run skeleton tells agents to write the report to the state folder only |
| `design/` note life cycle (draft, review, graduate, delete) | **ki-work-design** (was `ki-pmo-design`) | Keeps graduation; the keep-until-graduated rule and the allowed file kinds sit with the work-folder skill |
| Mechanical checks and entry-point commands | **tools-ki** | Below |

`ki repo audit` should enforce, with the rubric moving from ki-pmo's PMO-9 and ki-checkpoint's STRUCTURE items into the work-folder skill:

- FAIL: an entry outside the closed list, including scripts, images other than diagram renders, and `scratch/` under `design/`. Holding areas excepted.
- WARN: a report whose Needs tags the log all names (today's PMO-9).
- WARN: a brief whose report is in the folder or in Git.
- WARN: a `finished` work file still present after a later mark.
- WARN: a Messages line not in the `<date> · <TAG> · <sender>: ...` shape.
- WARN: a review folder with no `README.md` line.
- WARN: a decisions-log heading the close gate cannot parse.

`ki agent` should:

- Parse the work model's timestamped headings in the close gate, or refuse to pass a log it cannot read, rather than pass it.
- Refuse, not warn, at launch when a brief names a work-folder report path.
- Number nothing: `decide` writes the timestamped heading the standard sets.

`ki agent sweep` should stay out of the work folder. It acts on the state root without a work's authority, and a tracked-file delete needs the work's own commit.

Two entry-point commands would make the contract mechanical rather than hoped for:

- `ki work message <id> <line>`: appends one shaped Messages line and commits that path alone.
- `ki work prune <id> [--write]`: lists prune candidates and, with `--write`, runs `git rm` on the named ones in one commit. Run by the work's own steward only.

Folding, under VISIBLE-PUSH: the rubric and skeleton parts fold into [KI-HARNESS-GOV-200](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-200-thread-folder-closed-list.md) (triage, already the closed-list record), and the ownership lines into the rename work under WORK-FOLDER-DEDUP. The close-gate parse and the two commands need one tools-ki record, since [KI-TOOL-KI-CLI-147](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-147-agent-state-folder-tooling.md) is done.

## 5. Name

| Name | For | Against |
| --- | --- | --- |
| `ki-work-folder` (recommended) | The term every source already uses: Work Process note "The work folder", `pmo:821-836`, `run:68`. It covers `work.md` and everything beside it. It names the artefact it governs, as `ki-work-roadmap` does | `ki-work`'s adapters (`ki-work-roadmap`, `ki-work-github-issues`, `ki-work-linear`) share the prefix, so its description must say it is not an adapter. `ki-work-recurring` and `ki-work-design` already break that pattern |
| `ki-work-file` | Short | Names one file, the narrower reading Kris rejected on 18 October |
| `ki-work-pack` | Kris floated it | A new word used nowhere else. "Packet" is already ki-delegation's word for a run's state folder (`run:47-49`), so pack and packet would blur |
| `ki-work-area` | Could cover `_WORK` and `_WORK_REVIEW` | "Working area" is `ki-repo`'s word for all of `+/` and `-/` |
| Keep `ki-checkpoint` | No rename churn | Names the retired thread-model record |
