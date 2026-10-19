# Work package: brief

**Owner:** Kris Brown · **Owning repository:** knowledgeislands/ki-principal · **Owning work:** `ki.ways-of-working` · **Date:** 2026-10-19

Design note under `ki-work-design`, stage one (brief), revised after Kris's answers at 13:37 BST on 19 October: the concept and skill are the work package, `ki-work-package`; a package has four files and no state file; and the live folders migrate in one approved pass. Superseded text, including the two reviews' targets, is in Git. Draft; it graduates when its decisions have homes in `ki-work-package` (renamed from `ki-work-folder`), `ki-coordination`, the Work Process note and GDR-KI-PRINCIPAL-009, and is deleted in the same change.

## Contents

- [Problem](#problem)
- [Owner's proposal](#owners-proposal)
- [Owner's answers](#owners-answers)
- [Established facts](#established-facts)
  - [Stocktake](#stocktake)
  - [Findings](#findings)
  - [Governing sources](#governing-sources)
  - [Live sessions and rename inventory](#live-sessions-and-rename-inventory)
- [Reflection](#reflection)
  - [Name](#name)
  - [The package](#the-package)
  - [What each file holds](#what-each-file-holds)
  - [Front matter](#front-matter)
  - [Progressive reveal: who reads what, when](#progressive-reveal-who-reads-what-when)
  - [Size limits](#size-limits)
  - [Routing and method stewardship](#routing-and-method-stewardship)
  - [Fit with the owning skills and the Work Process note](#fit-with-the-owning-skills-and-the-work-process-note)
  - [The rename](#the-rename)
  - [Migration](#migration)
- [Open decisions](#open-decisions)

## Problem

A work folder is meant to let a fresh agent, or State of play, understand a piece of work quickly. Today it does not. The work file, `work.md`, is defined as the minimal current state, yet in practice it carries everything that has no other home: run evidence, logs of what happened since the last mark, open query tags whose text lives somewhere else, messages from other work weeks old, held to-dos and ideas. Nothing in it says what the work is for or what work it takes, so State of play cannot route a new unit of work by reading the folder; it relies on titles and memory.

Kris has now agreed that State of play is the single dispatch coordinator, routing each new unit of work to an existing work. Routing needs every work to declare, in a few lines, what it is and what it takes, readable without loading its whole state. That is the skill-package idea: a short front-matter description for selection, a body for the definition, and the detail in files read only when needed.

## Owner's proposal

Kris, 19 October 2026, 12:09 BST, "owner request, WORK-ROUTING model" in the [decisions log](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/decisions.md), speech lightly cleaned:

> your ways of working is really good. You've got multiple reviewers for the recommendations and I don't think other threads are doing that. Also, there's now a number of active threads, and I think somehow we need to mark them as active so that we know that we can push work to them, because we don't want to just create any thread to do any work ... if a thread is parked, that's fine, we can also push work into it ... the state of play decides [which] thread of work and the work package ... you can give me a prompt for me to ask it. If it then decides it's your work, you have to accept it. And as we make improvements to the ways of working, presumably we need a thread to periodically refresh itself from the ways of working ... how would we do that? And also, if a thread has a potential way to improve the way of working, it should also ask me to give that to the ways of working ... ways of working and state of play probably overlap ... Perhaps there's two high-level coordination pieces: one which is state of play, and one which is ways of working. What do you think?

Kris, 19 October 2026, 12:24 BST, "owner answers, WORK-ROUTING and WOW-REFRESH; request WORK-PACKAGE":

> I agree about the split of state of play. I think ways of working goes away and actually then usually state of play is a dispatch agent overall. So actually improvements should really go back to state of play. The exception to that obviously is whilst we're defining the ways of working, that ways of working can directly do that into the other [works], like we say on the refresh, whereas ordinarily that would come from [state of play] ... looking at the work folders ... Are they work packages? ... the work package needs a really clear understanding ... like we talked about before with skills and also with knowledge ... work should have a package idea and it should be clear about what its goals are and maybe a description to help things route it, so we've got that kind of progressive reveal capability ... think about what the file structures are within it, like a skill has. So we have a work.md file which defines what it is. Currently a lot of the work.md files have got loads of stuff in them ... maybe that should be another file so it's really quite straightforward ... like the decisions one, there should be a Q one ... take a bit of a stock take really. Can you take all this into account please and think what we should do? Maybe get a review on it as well from some high-level models.

Read back and taken, same entry:

> - WORK-ROUTING - split agreed, amended: State of play is the single dispatch coordinator; it routes work and receives method improvements from every work. Ways of working is finite: once the method is defined it goes away, and its stewardship passes to State of play.
> - WOW-REFRESH - a) for now: while the method is being defined, Ways of working writes refresh lines straight into live work files; afterwards refreshes come from State of play.
> - WORK-PACKAGE - design the work folder as a package, as a skill is: `work.md` defines the work (name, goals, a routing description for progressive reveal), with state, next steps, queries, decisions and parked items in their own files; settle the name; stocktake every current work folder.

## Owner's answers

Kris, 19 October 2026, 13:37 BST, "owner answers, work package; mark" in the decisions log:

> None of the other threads are active at the minute, so I think we [change] the work package to what we've now described with the different files in it. work.md, queries.md, messages.md and decisions.md. Also, I want `ki-work-package` please, where it lives is a folder. Take that into account and then come back with revised queries.

Read back and taken, same entry:

> - PACKAGE-NAME - the idea and its skill are the work package, `ki-work-package` (renamed from `ki-work-folder`); the place it lives is still called the work folder, `+/_WORK/<id>/`.
> - FILES - a work package has four files: `work.md`, `queries.md`, `messages.md` and `decisions.md`. No `state.md`: state, next steps and held items stay in `work.md` (taken; confirmed in the revised queries).
> - MIGRATE-NOW - no other thread is active, so the live folders can move in one pass rather than each at its own mark; the exact steps come back as revised queries before any migration run.

These answers settle PACKAGE-NAME and MESSAGES-FILE, replace STATE-FILE's two options with a confirmation, and replace MIGRATE-PATH's per-mark path with a one-pass path. Everything the reviews agreed and these answers do not touch is unchanged below.

## Established facts

### Stocktake

Taken read-only at 12:20 BST on 19 October 2026 from every `+/_WORK/` in the registered workspaces: the 11 live folders in ki-principal and one in `personal/acquire`. Content kinds are what the work file actually holds, whatever its heading says.

| Work | Level · state | Files beside `work.md` and `decisions.md` | `work.md` lines · words | What `work.md` holds | Stale or duplicated | `decisions.md` lines · entries |
| --- | --- | --- | --- | --- | --- | --- |
| `ki` | territory · handoff to supervisor | 2 reports, 12 design files | 40 · 459 | state line; restart order (Project-work queue); dated queue of hold reviews; backlog ("Later"); follow-ups; 4 parked queries with recommendations | mark 15 October, four days old; no guidance-read line | 1,102 · 259 (17,869 words) |
| `ki.baseline-rollout` | project · handoff to supervisor | none | 34 · 171 | guidance-read line above `Next steps`; state; seed scope (a definition); query tag WAVE-1 named, its text nowhere in the folder | an older folder of the same id sits in `+/_WORK_REVIEW/` with 11 decisions | 10 · 1 |
| `ki.chezmoi` | project · handoff to supervisor, blocking | 25 reports, 5 briefs | 62 · 1,577 | six paragraphs of run evidence (commit SHAs, test counts, an artefact hash, doctor output): history; 11 Messages; 6 parked entries mixing open queries, a resolved item and held work | 7 Messages dated 18 October still present, including MIGRATED, FIRST-STEP and RENAME-CHECKPOINT; 12 reports carry query headings; the 14 answered reports AUDIT-TIDY asked to prune remain | 447 · 101 |
| `ki.knowledge-acquisition` | project · on hold | 1 report, 2 design notes | 50 · 610 | guidance-read line; five numbered steps that state scope and method (a definition); 8 parked one-line queries pointing into a design note | PUBLISH-STACK lists nine other sessions' commit SHAs; decisions in two formats | 169 · 67 |
| `ki.mac-studio-setup` | project · handoff to supervisor | 4 reports, 3 design files | 42 · 424 | state line; next steps; parked section mixing queries (RIG-ORDER, ADOBE-*), at-a-screen to-do lists and 9 tags whose text lives in retired run-folder reports | MIGRATED line since 18 October; `design/adobe-remove.sh` is outside the closed list; mark 18 October | 639 · 160 (9,161 words) |
| `ki.observatory` | project · handoff to supervisor | 4 reports, 2 briefs, 3 design files | 35 · 253 | `Next steps` is an append-only dated log of seven entries since 08:39 BST; 11 open query tags, text in reports and Summaries | earlier "Open with Kris" lists superseded by later ones in the same section | 17 · 16 (list form) |
| `ki.regular.registry-removal` | regular · on hold, paused | none | 42 · 400 | an old "Messages from Master" block inside `Next steps`, citing retired `ki-pmo` paths; a hold note; two near-duplicate resume instructions; waiting-on prose under `Parked` | MIGRATED line since 18 October | 13 · 2 |
| `ki.regular` | regular · on hold, more expected | no `decisions.md` | 30 · 103 | one next step | MIGRATED line since 18 October | none |
| `ki.timelines` | project · handoff to supervisor | 1 design note | 33 · 113 | guidance-read line above `Next steps`; state; 7 query tags, text in `design/survey.md` and the Summary | none | 3 · 1 (list form) |
| `ki.tools-burndown` | project · handoff to supervisor | 7 design files, 4 of them JSON evidence | 37 · 449 | numbered log (1) to (5) with (3a) to (3c), mostly done items; 5 query tags whose text sits in state-folder reports outside the repository; 1 Message; 1 parked query | no `mark` field (mark only in prose); JSON evidence in `design/` is outside the closed list | 44 · 7 |
| `ki.ways-of-working` | project · with worker | 2 reports, 43 design files | 39 · 323 | state; next steps 1 to 8 including done items and other works' outstanding items; a held item and a 9 October idea under `Parked` | no guidance-read line; run reports said to sit in the state folder | 269 · 42 (5,045 words) |
| `kb.regular.acquire-intake` (`personal/acquire`) | regular · on hold | 1 report, 1 design note | 37 · 338 | the work's remit and method inside `Next steps` (a definition) | none found | 339 · 50 |

Outside the live set: ki-principal's `+/_WORK_REVIEW/` holds five folders (`ki.agent-host`, `ki.baseline-rollout`, `ki.estate-factorisation`, `ki.paperclip-capture-and-rebuild`, `ki.regular.command-centre`) and ki-agentic-harness's holds one (`ki.regular.skill-reviews`). Seven other Capitals still hold old-shape records: 20 checkpoints under `+/_CHECKPOINTS/` (hnr-principal 10, personal-principal 4, va-principal 2, er-, legal-, si- and tmx-principal 1 each) and 18 entries under `+/_THREADS/` (hnr-principal 10, personal-principal 7, legal-principal 1).

### Findings

1. **The work file is a catch-all.** Live work files run from 103 to 1,577 words, about 440 on average, against a standard that wants minimal current state. The largest bulk is not state but evidence and history.
2. **`Next steps` doubles as a log** in four of eleven (`ki.chezmoi`, `ki.observatory`, `ki.tools-burndown`, `ki.ways-of-working`): what happened since the last move, done items, commit SHAs. Between moves there is nowhere else to write it.
3. **Queries have no home in the repository.** Six of eleven name open query tags in `Next steps` whose text lives in a run report, a state-folder report outside the repository (`ki.tools-burndown`, `ki.ways-of-working`), a design note (`ki.timelines`) or only the last Summary (`ki.baseline-rollout` WAVE-1). Reports are kept alive only to hold their queries: 12 of `ki.chezmoi`'s 25.
4. **`Parked` holds five different things:** parked queries, held work with a release condition, to-do lists for a particular screen, ideas, and items already resolved.
5. **Messages go stale and sit in the owner's own file.** Five of eleven still carry the 18 October MIGRATED line; `ki.chezmoi` carries 11 lines, 7 from 18 October; `ki.regular.registry-removal` keeps a pre-migration message block inside `Next steps`. Every sender writes into the same file the owner rewrites at each move.
6. **No work says what it is for or what it takes.** Scope appears ad hoc inside next steps (`ki.baseline-rollout`, `ki.knowledge-acquisition`, `kb.regular.acquire-intake`). The only stated goal is a Project note's `outcome`, outside the folder; all 22 Project notes carry one, but regular and territory work have no Project note. Routing has nothing to match against.
7. **Guidance revision is recorded unevenly.** Three of eleven carry a `ki-coordination read at <revision>` line, all placed above `Next steps`, outside the exact heading sequence; the rest, Ways of working included, record nothing, so a targeted refresh cannot tell who is behind.
8. **Decisions logs are large and unstruck.** `ki` holds 1,102 lines with its last mark on 15 October, `ki.mac-studio-setup` 639, `ki.chezmoi` 447; three logs use list entries, the rest H2 entries, and two mix both.
9. **The closed list is breached in `design/`:** a shell script (`ki.mac-studio-setup`) and JSON evidence files (`ki.tools-burndown`).
10. **One id has two folders:** `ki.baseline-rollout` is live in `+/_WORK/` and also held in `+/_WORK_REVIEW/`.

### Governing sources

- The [work-folder standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-work-folder/references/standards-work-folder.md) owns the folder's closed list, entry points, tidy rules, Messages line shape and the work file's exact form: closed front matter (id, level, title, project, theme, worker, supervisor, state, target, hold, blocking, since, received, beat, mark, created_at) and the body `Next steps`, `Messages`, `Parked`, nothing else.
- The [coordination standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md) owns tidy timing, the decisions log, the owner report, Messages between work (any coordinating work in the same Capital may send; territory work routes the owner's dumps and anything with no owning work), territory work's cap and queue, Bootstrap and the refresh rule.
- The [Work Process](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Processes/Work Process/Work Process.md>) note, decided by [GDR-KI-PRINCIPAL-009](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/GDR-KI-PRINCIPAL-009-the-work-model.md), names the work file "current state, next steps, Messages and parked query tags", keeps links pointing upward (the work file names its Project; the Project note never links down) and reads Observatory fields through `ki work status` (`ki/work-status/v1`).
- The [Project registry standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-work/references/standards-project-registry.md) gives every Project note an `outcome`, one sentence naming the finite outcome, and `lifecycle`.
- The [Agent Skills standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/keystone/ki-skills/references/standards-agent-skills.md) gives the package model: `name` and `description` (at most 1,024 characters, capability plus trigger, with explicit non-triggers) as the only always-loaded metadata, about 100 tokens; a `SKILL.md` body under 500 lines and about 5,000 tokens; `references/` read on demand; budgets soft, linted as warnings. The [ki-work-design skill](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-work-design/SKILL.md) shows the shape in use.
- No written "knowledge package" definition was found in ki-principal, the harness or the work folders. The nearest are the knowledge base's same-name index note, which "contextualises and points rather than duplicating content" ([knowledge-base standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-kb/references/standards-knowledge-base.md#index-note-shape)), and Acquire's source packages. This brief rests the analogy on the skill package and the index note.
- The blind review [query-review-2](/Users/krisbrown/.local/state/ki/agents/ways-of-working/query-review-2.report.md) (Codex), WORK-ROUTING and WOW-REFRESH sections: derive the register from work files rather than duplicating status; receivers must acknowledge and own disposition, but routing grants no execution authority, and scope, capacity or authority conflicts are flagged back; preserve paused holds while more-expected holds use their existing release; do not route already-owned routine items through the hub; refresh by one dated line linking the standard, revision and practical effect, reread at the next safe checkpoint, revision recorded, changes coalesced, held work left pending without waking; pilot with one active and one held receiver.

### Live sessions and rename inventory

Checked read-only at 13:42 BST on 19 October 2026.

- **Runs.** `ki agent status` lists agents in one work only, `ki.ways-of-working`: this revision and `query-review-3`, held until it finishes. No other work has a run running or queued.
- **States.** `ki.ways-of-working` is the only work With worker. Seven are Handoff to supervisor (`ki`, `ki.baseline-rollout`, `ki.chezmoi`, `ki.mac-studio-setup`, `ki.observatory`, `ki.timelines`, `ki.tools-burndown`) and three On hold (`ki.knowledge-acquisition`, `ki.regular.registry-removal`, `ki.regular`); `kb.regular.acquire-intake` in `personal/acquire` is On hold.
- **Recent moves.** `ki` sent to Kris at 13:31 BST and `ki.knowledge-acquisition` at 13:23 BST, so their sessions may still be open, holding the old shape in memory. "Not active" therefore means no run and no worker's move outstanding, not that no session is open.
- **Dirty files.** `ki.chezmoi` holds another session's uncommitted changes: `decisions.md` modified, `apply-owned-drift.report.md`, `briefs/apply-owned-drift.md` and `coverage-implement.report.md` new, last touched at 11:16 BST.
- **Rename inventory.** `ki-work-folder` appears in 44 files in ki-agentic-harness (the skill directory, its standard, rubric and scripts, cross-references in other skills, a hook test, diagrams, the skills README and `.ki.toml`); 5 in tools-ki (the man page, `man/ki.commands.json`, the CHANGELOG and records KI-TOOL-KI-CLI-150 and KI-TOOL-KI-CLI-152); in ki-principal's `.ki.toml` and historical work-folder notes; and as a `[skills.ki-work-folder]` declaration in ten `.ki.toml` files, eight of them outside this territory (er-principal, hnr-principal, `personal/acquire`, si-principal, legal-principal, personal-principal, tmx-principal, va-principal). The chezmoi source holds no literal reference; `~/.claude` holds it only in backups.

## Reflection

Each numbered point is one claim a reviewer can agree with, differ from or extend.

### Name

1. **The concept and its skill are the work package, `ki-work-package`, renamed from `ki-work-folder`; the place a package lives is still the work folder, `+/_WORK/<id>/`.** A work package is one piece of work above a work item, packaged as a skill is: a definition read first and detail files read when needed. The Words table defines it once and says that it is not the project-management work package, the lowest deliverable of a breakdown, which in this model is the work item, the one level with no package.
2. **"Work file" keeps naming `work.md`,** which now holds the definition and the state together. There is no state file. The Work Process Words table changes accordingly.

### The package

3. A work package has exactly four files, with run material beside them as today, mirroring `SKILL.md` and `references/`:

```text
+/_WORK/<id>/
├── work.md          definition and state: routing description and state fields in front matter;
│                    Goals, Scope, then Now, Next steps, Held
├── queries.md       every open and parked query in full, Needs-tagged
├── messages.md      inbox: dated lines from other work and State of play
├── decisions.md     the owner's decisions not yet durable elsewhere (unchanged)
├── <run>.report.md  run reports, kept until their outcome is homed
├── briefs/<run>.md  open briefs (unchanged)
└── design/          design notes and diagram sources (unchanged)
```

4. **All four files are required at creation,** `queries.md`, `messages.md` and `decisions.md` starting as `None`. A reader never meets a missing file, and a sender never creates one. The folder is created by State of play when it seeds the work, as the Seeding rule already says. `ki.regular`, which has no decisions log today, gains one at migration.
5. **The logbook splits by kind.** `git log -- queries.md`, `messages.md` and `decisions.md` each give one history. `work.md` keeps definition and moves in one history, the cost of Kris's four files over a separate state file; because Goals and Scope sit above the state sections and change rarely, a move's diff stays in the lower half of the file.

### What each file holds

6. **`work.md`, the work file.** Front matter carries identity, supervision, the routing `description` and the state fields. The body has exactly `# <id>`, `## Goals`, `## Scope`, `## Now`, `## Next steps` and `## Held`; territory work adds `## Queue` after `## Now` for its ordered Project-work queue. The first two sections are the definition, the rest the state.
   - `## Goals` - the standing goals of this work, stable across its waves, as few as it needs. For Project work the first line links the Project note's `outcome` and never restates it; for regular work it links the Activity note; for territory work, the Charter. Links point upward, as now.
   - `## Scope` - `In:` and `Out:` lines naming what the work takes and what belongs to which other work, by id. This is what State of play reads when two descriptions both match.
   - `## Now` - at most five lines: what is running, what lies with whom, since when. Rewritten in place at every move; it holds the present only.
   - `## Next steps` - what the worker does when the work is next in its hands, numbered. Done items leave at the move that completes them; the commit message carries them.
   - `## Held` - work waiting on a named release condition, one line each with the condition. Ideas go to the Project note's Notes or to a record through `ki-next`, not here.
7. **History stays out of `work.md`.** The recap since the mark reads `git log -- +/_WORK/<id>/` and the run reports, so nothing needs a dated log in `## Now` or `## Next steps`. Evidence (commit SHAs, test counts, artefact hashes) lives in the run report and the commit; the state sections may link one, not copy it.
8. **`queries.md`, the Q file beside `decisions.md`.** Two sections, `## Open` and `## Parked`. Each query is a `### <TAG> - <title>` block carrying **Context**, **Query** and **Options** exactly as the owner report renders them, with one line beneath the heading giving `since <date>` and its source report, if any. Parking moves the whole block from Open to Parked with its reason and release; putting back moves it again. A parked tangent, an owner side topic not yet shaped as a query, is a one-line entry under `## Parked`. When the owner answers, the read-back goes into `decisions.md` and the block is deleted in the same commit, Git keeping it. The owner report's `## Queries` section is rendered from `## Open`, so the two cannot diverge.
9. **Copying queries in at receive decouples reports from the tidy.** When the coordinator receives a run report, it copies each query into `queries.md`; the report then stays only until its outcome is homed, not until its queries are answered. On today's evidence that would let `ki.chezmoi` drop most of its 25 reports at its next tidy.
10. **`messages.md`, the inbox.** One line per message, in today's Messages line shape (`- <date> · <TAG> · <sender title>: <words, links>`, about 60 words). Other work and State of play may append one line, or replace their own line not yet acted on, and commit that path alone; that is their only write into the folder, now checkable at the file level. Appends and removals are committed one at a time. The receiver records each line's disposition where it lands (see 25), names it in the commit that removes the line, and only then removes it.
11. **`Parked` is dissolved.** Parked queries and tangents go to `queries.md` `## Parked`; held work to `work.md` `## Held`, each with its release condition; ideas to the Project note's Notes or a record; resolved items are deleted by the work's own worker. No separate `parked.md`, which would recreate the catch-all.
12. **`decisions.md` keeps its life cycle** under `ki-coordination`, with one entry format (H2 entries, the majority form today) settled at each work's migration.

### Front matter

13. `work.md` front matter, closed set:

```yaml
---
id: ki.observatory
level: project
title: 'KI > Model > Observatory'
project: observatory
theme: model
description: >-
  Builds and runs the local Observatory in apps-observatory.local, the territory's read-only view of work, runs
  and diagrams, and the diagram rollout that feeds it. Takes Observatory features, its design system, diagram
  conversion records and `ki work status` consumers. Not for timelines and calendars (ki.timelines) or the work
  model itself (ki.ways-of-working).
worker: agent
supervisor: owner
state: handoff-to-supervisor
target: null
hold: null
blocking: false
since: 2026-10-19T11:25:41Z
received: 2026-10-19T07:14:00Z
beat: null
mark: 2026-10-19T07:47:18Z
method_read: 1a2b3c4
created_at: 2026-10-13T23:50:00Z
---
```

   `id`, `level`, `title`, `project`, `theme`, `label`, `worker`, `supervisor`, `state`, `target`, `hold`, `blocking`, `since`, `received`, `beat`, `mark` and `created_at` keep today's rules. Two fields are new: `description`, required at every level, and `method_read`, the short ki-agentic-harness revision whose `ki-coordination` and `ki-work-package` guidance the worker last read in its harness checkout. `method_read` replaces the uneven body line and makes refresh targetable (see 29).

14. **The description is written for routing,** in the skill description's voice: third person, what the work does, then "Takes ..." naming the kinds of unit it accepts, then "Not for ..." naming the neighbouring works by id. The work's steward writes it at seeding with State of play, and only the steward edits it; State of play may propose a change by a line in `messages.md`. Its exact shape is open (DESCRIPTION-SHAPE).

15. **No `active` or `accepts` field.** Whether a work can take a routed unit is derived from its state: every state except `finished` can receive; `on-hold` receives without waking (see 26). A work winding down says "Not taking new units" in its description, as Ways of working will before it closes.

16. **The holder and its role stay derived from `work.md` alone,** as today. Because the state fields do not move, `ki work status` keeps reading them where it reads them now and its `ki/work-status/v1` output is unchanged for the Observatory; it gains `description`, `method_read` and a pending-message count from `messages.md` as additive fields.

### Progressive reveal: who reads what, when

17. Four levels, by analogy with the skill's metadata, body and references:

| Level | Files | Size per work | Who reads it, when |
| --- | --- | --- | --- |
| 1. Register | `work.md` front matter | to be measured; expected about 150 tokens | State of play at each routing; `ki work status`, the Observatory and `ki work` views; an opener |
| 2. Definition | `work.md` `## Goals` and `## Scope` | under 300 words | State of play when two descriptions match; the owner checking a routing; a new session before it reads state |
| 3. Pick-up | all of `work.md`, `messages.md`, `queries.md`, `decisions.md` | as small as the limits below keep them | the work's own worker at bootstrap, re-anchoring, each owner message and each move |
| 4. On demand | reports, briefs, `design/` | unbounded | only when `work.md` or `queries.md` names one |

18. **Routing reads level 1 only.** Across today's 11 works that is a few thousand tokens at most, against about 5,000 words of work files now. A sender reads nothing in the receiver's folder: it appends to `messages.md`. A run reads its brief and what the brief names.

19. **Pick-up stays within the turn budget.** One read of the package's four files counts as one call, and a write to its files with a brief counts as one write set, so the five-call budget is not spent before the first launch. After bootstrap the coordinator reads only what changed since its last read, plus the entries that bear on the question, not every decision and query at each owner message. The `ki-coordinator` output style's "reads limited to the work file ..." and "writes limited to the work file, the decisions log and a brief" become "the work package" (PICKUP-READS).

### Size limits

20. Soft limits, linted as warnings like the skill budgets, never failures:

| File | Limit | Today's worst |
| --- | --- | --- |
| `description` | at most 500 characters, one to three sentences | absent everywhere |
| `work.md` `## Goals` and `## Scope` | at most 300 words | none exists |
| `work.md` state sections | at most 400 words; `## Now` at most five lines | 1,577 words in `ki.chezmoi` |
| `messages.md` | each line at most 60 words; a line older than 7 days on work that is not on hold | 8 lines from 18 October in `ki.chezmoi` |
| `decisions.md` | more than 400 lines, or a mark older than 7 days on live work | 1,102 lines and a 15 October mark in `ki` |

   More than eight open queries is a coordination smell rather than a shape fault, so it moves to the `ki-coordination` rubric (today's worst: 11 open tags in `ki.observatory`).

21. **A history check** on `work.md`'s state sections warns on bulk history, dated "since" or "received" log lines, runs of commit SHAs or test counts, the patterns findings 2 and 3 show; a single link to a report or a commit does not trip it.

### Routing and method stewardship

22. **State of play is the single dispatch coordinator,** as Kris agreed. Every new unit of work - an owner dump, a handoff with no owning work, a cross-work item whose owner is unclear, and every method improvement - comes to State of play, by Kris pasting a prompt there or by a line in State of play's own `messages.md`.
23. **Already-owned units go direct.** A work's own follow-ups, an item in a record that already names its work, and a reply to a message do not pass through the hub; State of play routes only what has no clear owner, as the review advised.
24. **State of play matches the unit against the register** (level 1) and, if needed, the definitions (level 2), chooses one work and writes one dated line in that work's `messages.md`: `- <date> · ROUTE · <Territory> > SoP: <the unit in the owner's words, with links>`. Where nothing matches, it proposes to Kris either a new piece of work, within the cap, or a record captured through `ki-next`. The register is derived from the work folders by `ki work status`; State of play keeps no copy of it, and shows lines nobody has picked up.
25. **Receipt is compulsory; execution authority is not conferred.** The receiving worker acts on each line at its next bootstrap or owner message, as now, and records one disposition: taken into `work.md` next steps where its existing authority covers it; turned into a query in `queries.md` where it needs Kris's authority, capacity or a scope change; or sent back to State of play's `messages.md` with the reason where it is outside the work's scope. A unit is returned once: if State of play cannot place it elsewhere, it goes to Kris as a query rather than round again. Kris's "you have to accept it" is read as owning the disposition, never as authority to execute what the work's decisions do not cover.
26. **Held work keeps its hold.** A line routed to work On hold, paused, waits in `messages.md` without waking it; its count shows in State of play's register. Work On hold, more expected, is released by new work arriving under the existing rule, moving to Handoff to worker, and State of play gives Kris its resume line. If a paused work's line is urgent, State of play asks Kris to lift the hold.
27. **Method improvements go to State of play from every work,** by a `METHOD` line in its `messages.md`. While Ways of working exists, State of play routes them to it like any other unit, its description saying it takes method changes. That keeps one dispatch point and needs no exception.
28. **While the method is being defined, Ways of working sends refresh lines directly** into each affected live work's `messages.md`, under WOW-REFRESH a). Afterwards State of play sends them.
29. **Refresh is targeted and recorded.** After an approved method change lands, the sender writes one dated `REFRESH` line, only to works whose `method_read` predates the change and whom the change affects, linking the standard at its revision and stating the practical effect in a sentence. One revision vouches for `ki-coordination` and `ki-work-package` together in the harness checkout. A sender may replace its own earlier `REFRESH` line not yet acted on, so changes coalesce, and the replacement keeps every pending effect of the line it replaces. The receiver rereads at its next safe point, before launching further work, and sets `method_read`; updating the field is the confirmation, so no acknowledgement message is sent. Held work is not woken; the line waits. The existing bootstrap and update revision checks stay as the fallback.
30. **When Ways of working closes,** its description says "Not taking new units" for its last wave; at Finished, State of play's `work.md` description gains method stewardship and its Scope names where method changes go next (open decision STEWARD-HOME). State of play still executes nothing.

### Fit with the owning skills and the Work Process note

31. **`ki-work-package`**, renamed from `ki-work-folder`, owns the change: the closed list gains `queries.md` and `messages.md`; the work file's exact form gains `## Goals`, `## Scope`, `## Now`, `## Held` and territory `## Queue`, and loses `## Messages` and `## Parked`; the front matter gains `description` and `method_read`; the entry-point table gives other work one write, appending or replacing its own line in `messages.md`; the tidy keeps a report until its outcome is homed, its queries having been copied at receive; the rubric's RECORD-2 and LIFECYCLE-1 follow the new files, and new criteria check the description, the size limits and the history heuristic. Its description keeps the old `+/_CHECKPOINTS/` tolerance and adds the old work-file shape for the migration window.
32. **`ki-coordination`** keeps timing and judgement: Messages between work points at `messages.md`; Parking tangents and Putting work on hold park into `queries.md`; the owner report's Queries are rendered from `queries.md`; Territory work gains a Dispatch section (points 22 to 27); Refreshing this guidance gains targeted refresh and `method_read`; Bootstrap step 4 reads `messages.md`; the rubric gains the open-query count. The `ki-coordinator` output style's references to the work file's Messages section and its turn budget follow (point 19).
33. **`ki-delegation`** gains one line: at receive, the coordinator copies a report's queries into `queries.md`. The launcher still homes reports and never deletes.
34. **The Work Process note** changes its Words table (work package, work folder, work file as definition and state, queries, messages), its Homes tree, its work-file paragraph and its skill name; GDR-KI-PRINCIPAL-009 is refined in place, since it owns the work model. Under the Enactment Process that needs one ki-principal roadmap record for the note, the Decision Record and ki-principal's `.ki.toml` declaration together.
35. **`tools-ki`** keeps `ki work status` reading `work.md` (output schema unchanged, three additive fields), adds a routing view listing each work's id, state, pending-message count and description, the register State of play reads, and renames the skill in its help text and man page. One tools-ki record.
36. **Records:** one harness record covering the rename, `ki-work-package`, `ki-coordination`, `ki-delegation` and the output style; one tools-ki record; one ki-principal record. Folded into existing records where one fits, under the fewest-records rule.

### The rename

37. **What is renamed:** every place the text names the skill or the concept, `ki-work-folder` becoming `ki-work-package` and "work folder" as the concept becoming "work package". **What is not:** "work folder" where it names the directory `+/_WORK/<id>/`, which stays; and historical text, meaning decisions logs, past design notes, CHANGELOG entries and done records, which keeps the name it was written with.
38. **Order:** first, one harness change moves `skills/governance/ki-work-folder/` to `ki-work-package/` and rewrites its standard to the package shape in the same series, so each file moves once, updating every cross-reference, the diagrams, the skills README and the harness `.ki.toml`; the harness accepts `[skills.ki-work-folder]` as a deprecated alias of `ki-work-package` for a tolerance window. Second, ki-principal's `.ki.toml`, the Work Process note and GDR-KI-PRINCIPAL-009 under one Enactment record. Third, tools-ki's help text and man page, and its additive status fields. Fourth, the payload is reinstalled and checked: no stale `ki-work-folder` skill installed, `ki repair` clean and `chezmoi diff` showing no drift. Then the migration pass (point 41 onwards).
39. **Other territories' declarations** change at each repository's own pace: the eight `.ki.toml` files outside this territory receive a handoff through their own works or State of play, never a write from here, and the alias covers them until they do. The alias, and with it the old skill name, is removed when the inventory shows no declaration left.

### Migration

40. **One pass, because no other thread is active** (MIGRATE-NOW). The state fields stay in `work.md`, so `ki work status` and the Observatory keep working through the pass; only the `## Messages` and `## Parked` sections, the definition sections and the two new files change. The tolerance window therefore shrinks to the pass itself for the live folders, and stays open only for the folders outside it (point 45). A folder holds one authoritative copy of each kind at a time: until it is migrated, senders write to its `## Messages` section; once `messages.md` exists, there and never both.
41. **Gate.** The pass launches only when all of these hold: the rename and the new standard (point 38) have landed and been installed; `ki agent status` shows no agent running or queued in any work except the pass itself; no work other than `ki.ways-of-working` is With worker; every target folder is clean, the pass refusing any folder with uncommitted changes, so `ki.chezmoi`'s other-session files are committed by their session or the folder is skipped by Kris's decision; Kris confirms that no other session will be resumed until the pass has committed, and that any session left open is resumed only through its send line, which re-reads from the files; and Kris approves the exact folder set.
42. **Steps, per folder, mechanical, one commit each, `docs(work): <id> package migration`:**
    - front matter: `description` drafted from the Project note's `outcome` and the scope text findings 6 found, and `method_read: null`, so the work's own next bootstrap reads the new standard and sets it; state fields, hold and mark unchanged;
    - body: `## Goals` and `## Scope` drafted; `## Now` from the current state lines; `## Next steps` cut to what is still to do, history left to Git; held items to `## Held`; territory work's queue to `## Queue`;
    - `## Messages` to `messages.md`, dropping only the 18 October MIGRATED line, which the pass itself discharges; every other line kept for its receiver; plus one `FIRST-STEP` line asking the worker to re-read `ki-work-package` and confirm the drafted description, Goals and Scope;
    - `## Parked` to `queries.md` `## Parked` or `work.md` `## Held` by kind; an item that looks resolved is carried and flagged, not deleted, because judging it is the worker's;
    - every open query tag resolved to its full text from wherever it lives today (reports, state-folder reports, design notes, the last Summary) into `queries.md` `## Open`; a tag whose text cannot be recovered becomes one `## Open` entry saying so and asking Kris, never dropped;
    - `decisions.md` created where missing;
    - nothing else: no report or brief pruned, no decision struck, no design file moved; those wait for each work's own next mark, which the copied queries now make possible;
    - after each folder: the rubric passes on the new shape and `ki work status` shows the same state and holder as before; the pass stops at the first failure and reports.
43. **Order within the pass:** `ki.ways-of-working` first, as the pilot, with exit checks (the rubric passes, `ki work status` unchanged, an owner report renders from `queries.md`); then `ki`, State of play, whose description and Scope every routing is matched against; then the held works; then the works with Kris.
44. **This session's part.** `ki.ways-of-working` is the only work With worker and its coordinator is live. It records Kris's approval in `decisions.md` and commits before launch, waits until `query-review-3` has finished and its report has been received, then launches the pass and writes nothing in its own folder until the pass reports. At receive it re-anchors from the new files (`work.md`, `queries.md`, `messages.md`, `decisions.md`) before any write, and acts on its own `FIRST-STEP` line.
45. **Outside the pass:** `kb.regular.acquire-intake` in `personal/acquire`, another territory, migrates with the personal territory through its own work; the six `+/_WORK_REVIEW/` folders migrate when they leave review; `ki.baseline-rollout`'s review-held twin is Kris's to resolve, not the pass's; the seven Capitals still on `+/_CHECKPOINTS/` and `+/_THREADS/` move straight to the package shape at their own territory migration, skipping the intermediate form. The rubric's tolerance for the old shape closes on an inventory covering live, review-held and old-shape folders, not live folders alone.
46. Per-folder starting points, from the stocktake:

| Work | Description drafted from | Main moves |
| --- | --- | --- |
| `ki` | Charter and Territory work | queue to `## Queue`; dated reviews to `## Held`; 4 parked queries to `queries.md`; decisions mark overdue, left for its own mark |
| `ki.baseline-rollout` | Project outcome; seed scope | seed scope to Scope; WAVE-1 query block rebuilt from its proposed scope and the last Summary into `queries.md` |
| `ki.chezmoi` | Project outcome | six evidence paragraphs to Git; 11 messages carried; parked entries split; reports left for its own tidy; skipped if still dirty |
| `ki.knowledge-acquisition` | Project outcome; numbered steps | method steps to Goals and Scope; 8 queries in full from the design note |
| `ki.mac-studio-setup` | Project outcome | queries to `queries.md`; screen to-do lists to `## Held`; 9 tags recovered from retired reports or raised as lost |
| `ki.observatory` | Project outcome | dated log to Git; 11 open queries in full |
| `ki.regular.registry-removal` | regular work's purpose | old message block to `messages.md`; duplicate resume text dropped |
| `ki.regular` | Work Process regular work | `decisions.md` created; otherwise minimal |
| `ki.timelines` | Project outcome | 7 queries from `design/survey.md` |
| `ki.tools-burndown` | Project outcome | numbered log to Git; 5 queries recovered from state-folder reports |
| `ki.ways-of-working` | Project outcome | done items to Git; pilot |

   The closed-list breaches in `design/` (`ki.mac-studio-setup`'s script, `ki.tools-burndown`'s JSON evidence) are left for each work's own mark.

## Open decisions

Settled by Kris at 13:37 BST: PACKAGE-NAME (work package, `ki-work-package`, place still the work folder) and MESSAGES-FILE (`messages.md` is one of the four files). The revised queries, with their full Context and options, are in the `work-package-revise` run report; in brief:

### STATE-FILE - Confirm that state stays in `work.md`

- a) (recommended, confidence high - Kris named four files and no state file; it also leaves `ki work status` unchanged) State fields in `work.md` front matter; `## Now`, `## Next steps`, `## Held` (and territory `## Queue`) below Goals and Scope.
- b) Reinstate a separate `state.md` as a fifth file.

### FILES-AT-CREATION - Whether all four files exist from creation

- a) (recommended, confidence high - Kris described the package as four files, and the fifth file Codex objected to has gone) All four at creation, three starting as `None`.
- b) `work.md` only at creation; the others created when first written.

### QUERIES-FILE - Full text in `queries.md`

- a) (recommended, confidence high - reviewed: Codex and Fable agree) Every open and parked query in full; owner report rendered from it; reports pruned once their outcome is homed.
- b) An index of tags pointing at reports.

### PARKED-HOME - Where parked items go

- a) (recommended, confidence high - reviewed: Codex and Fable agree) Parked queries and tangents in `queries.md` `## Parked`; held work in `work.md` `## Held` with its release; ideas to the Project note or a record; no `parked.md`.
- b) One `parked.md`, a fifth file.

### DESCRIPTION-SHAPE - The routing description

- a) (recommended, confidence medium - routing reads only descriptions first, so exclusions must be there) Up to 500 characters, "Takes ... Not for ..." by id, plus `## Scope`, tested against ambiguous examples.
- b) About 300 characters of plain prose, ids in `## Scope` only.
- c) Route on the Project `outcome` alone.

### ROUTE-RECEIPT - What a routed work must do

- a) (recommended, confidence high - reviewed: Codex and Fable agree) Compulsory disposition at the next bootstrap or owner message; no conferred authority; one return, then a query to Kris.
- b) Only at the next mark.

### REFRESH-TARGET - Targeted refresh

- a) (recommended, confidence high - reviewed: Codex and Fable agree) `method_read` in `work.md`; one coalescing, lossless `REFRESH` line to affected works behind.
- b) Broadcast with acknowledgements.

### INBOX-CHECK - Check the inbox at each wake

- a) (recommended, confidence medium - one comparison per wake) Each wake compares `messages.md` and the method revision with the last read; State of play shows unread age for works not waking.
- b) As a), plus a 15-minute inbox-only wake while the work is with Kris.
- c) No standing rule.

### PICKUP-READS - The turn budget for a package

- a) (recommended, confidence medium - both reviewers' fixes, compatible) One read of the four files counts as one call; after bootstrap read only what changed.
- b) Keep the budget and accept fewer launches.
- c) A `ki work` command printing the package and its changes since the last read.

### STATE-HISTORY - Keeping history out of `work.md`

- a) (recommended, confidence medium - the two reviews address different halves of one rule) Recap reads `git log` of the folder and run reports; the check warns on bulk history in the state sections, not a single link.
- b) A strict pattern check, no stated recap source.

### STEWARD-HOME - Method changes after Ways of working closes

- a) (recommended, confidence medium - reviewed: Codex and Fable agree) State of play keeps a method backlog and dispatches each improvement as small regular work or into the Project it most affects.
- b) A standing regular work under an Activity note, if volume shows the need.

### RENAME-ORDER - Order and scope of the `ki-work-package` rename

- a) (recommended, confidence medium - each file moves once and other territories are not written from here) Points 37 to 39: rename with the standard in one harness change and a deprecated alias; then ki-principal; then tools-ki; then reinstall and check; then the pass.
- b) Migrate the folders under the old name first and rename afterwards.
- c) Rename everywhere, including the eight other territories' `.ki.toml`, in one approved sweep with no alias.

### MIGRATE-PATH - The one-pass migration's steps

- a) (recommended, confidence medium - mechanical moves only, with judgement left to each work) Points 40, 42, 43 and 45.
- b) As a), and the pass also tidies: prunes reports whose queries are copied, strikes decisions, deletes resolved parked items.

### MIGRATE-GATE - What must hold before the pass launches

- a) (recommended, confidence medium - two sessions moved minutes before the answer and one folder is dirty) Point 41, with Kris confirming no other session is resumed until the pass commits.
- b) Launch on `ki agent status` alone, trusting "no other thread is active".

### MIGRATE-SELF - How this live session takes part

- a) (recommended, confidence medium - the coordinator never does the work and must not write over the pass) Point 44: launch the pass with this folder first as the pilot, write nothing in it until the pass reports, then re-anchor.
- b) Migrate this folder in a separate pilot run first, then launch the pass for the other ten after Kris sees the pilot.

### FIELDS-MIGRATE-ORDER - Where the field migration starts (carried from the merge report)

- a) (recommended, confidence medium - a four-record run tests the run's shape cheaply) apps-markhowarth.com first as a mechanical pilot, then personal-principal and the rest.
- b) personal-principal first as the pilot.
