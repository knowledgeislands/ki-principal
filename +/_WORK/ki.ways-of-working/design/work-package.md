# Work package: brief

**Owner:** Kris Brown · **Owning repository:** knowledgeislands/ki-principal · **Owning work:** `ki.ways-of-working` · **Date:** 2026-10-19

Design note under `ki-work-design`, stage one (brief). Reviews follow as `work-package-review-<reviewer>.md` beside it, then `work-package-report.md` and `work-package-decisions.md`. Draft; it graduates when its decisions have homes in `ki-work-folder`, `ki-coordination`, the Work Process note and GDR-KI-PRINCIPAL-009, and is deleted in the same change.

## Contents

- [Problem](#problem)
- [Owner's proposal](#owners-proposal)
- [Established facts](#established-facts)
  - [Stocktake](#stocktake)
  - [Findings](#findings)
  - [Governing sources](#governing-sources)
- [Reflection](#reflection)
  - [Name](#name)
  - [The package](#the-package)
  - [What each file holds](#what-each-file-holds)
  - [Front matter](#front-matter)
  - [Progressive reveal: who reads what, when](#progressive-reveal-who-reads-what-when)
  - [Size limits](#size-limits)
  - [Routing and method stewardship](#routing-and-method-stewardship)
  - [Fit with the owning skills and the Work Process note](#fit-with-the-owning-skills-and-the-work-process-note)
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

## Reflection

Each numbered point is one claim a reviewer can agree with, differ from or extend.

### Name

1. **Keep "work folder" as the name of the directory and the skill, and describe its shape as packaged like a skill; do not adopt "work package" as a term.** Three reasons. The name was settled under WORK-FOLDER-NAME on 18 October, and the renames that followed are still being cleaned up (`ki.chezmoi`'s RENAME-CHECKPOINT and USER-SKILL-STALE messages, a failing `ki repair`). "Work package" already means something in project management: in a work breakdown structure it is the lowest-level deliverable, which in this model is the work item, the one level that has no folder; borrowing it would invert the cascade. And the package is a property of the folder's shape, which the standard can state without a new noun.
2. **"Work file" keeps naming `work.md`, whose meaning changes from current state to definition;** the state moves to a new **state file**, `state.md`. The Work Process Words table changes accordingly.

### The package

3. The work folder becomes a package with one definition file, read first and changed rarely, and detail files read only when a reader needs them, mirroring `SKILL.md` and `references/`:

```text
+/_WORK/<id>/
├── work.md          definition: what the work is, its goals, what it takes; routing description in front matter
├── state.md         where the work lies: state fields in front matter; Now, Next steps, Held
├── queries.md       every open and parked query in full, Needs-tagged
├── messages.md      inbox: dated lines from other work and State of play
├── decisions.md     the owner's decisions not yet durable elsewhere (unchanged)
├── <run>.report.md  run reports, kept until their outcome is homed
├── briefs/<run>.md  open briefs (unchanged)
└── design/          design notes and diagram sources (unchanged)
```

4. **Required at creation:** `work.md`, `state.md`, `queries.md`, `messages.md` and `decisions.md`, the last three starting as `None`. A reader never meets a missing file, and a sender never creates one. The folder is created by State of play when it seeds the work, as the Seeding rule already says.
5. **Separating definition from state splits the logbook usefully:** `git log -- work.md` becomes the history of what the work is, and `git log -- state.md` the history of its moves. Today both are interleaved in one file.

### What each file holds

6. **`work.md`, the definition.** Front matter carries identity, supervision and the routing `description`. The body has exactly `# <id>`, `## Goals` and `## Scope`:
   - `## Goals` - two to four standing goals of this work, stable across its waves. For Project work the first line links the Project note's `outcome` and never restates it; for regular work it links the Activity note; for territory work, the Charter. Links point upward, as now.
   - `## Scope` - `In:` and `Out:` lines naming what the work takes and what belongs to which other work, by id. This is what State of play reads when two descriptions both match.
   - Nothing else: no state, next steps, evidence or history.
7. **`state.md`, where the work lies.** Front matter carries the state fields that move. The body has exactly `# <id> state`, `## Now`, `## Next steps` and `## Held`:
   - `## Now` - at most five lines: what is running, what lies with whom, since when. Rewritten in place at every move.
   - `## Next steps` - what the worker does when the work is next in its hands, numbered. Done items leave at the move that completes them; the commit message carries them.
   - `## Held` - work waiting on a named release condition, one line each with the condition. Ideas go to the Project note's Notes or to a record through `ki-next`, not here.
   - No dated log entries, commit SHAs, test counts or artefact hashes: evidence lives in the run report and the commit, which `state.md` may link.
8. **`queries.md`, the Q file beside `decisions.md`.** Two sections, `## Open` and `## Parked`. Each query is a `### <TAG> - <title>` block carrying **Context**, **Query** and **Options** exactly as the owner report renders them, with one line beneath the heading giving `since <date>` and its source report, if any. Parking moves the whole block from Open to Parked with its reason and release; putting back moves it again. When the owner answers, the read-back goes into `decisions.md` and the block is deleted in the same commit, Git keeping it. The owner report's `## Queries` section is rendered from `## Open`, so the two cannot diverge.
9. **Copying queries in at receive decouples reports from the tidy.** When the coordinator receives a run report, it copies each query into `queries.md`; the report then stays only until its outcome is homed, not until its queries are answered. On today's evidence that would let `ki.chezmoi` drop most of its 25 reports at its next tidy.
10. **`messages.md`, the inbox.** One line per message, in today's Messages line shape (`- <date> · <TAG> · <sender title>: <words, links>`, about 60 words). Other work and State of play append one line and commit that path alone; that is their only write into the folder, now checkable at the file level. The receiver removes each line it has acted on, recording its disposition where it lands (see 25).
11. **`Parked` is dissolved.** Parked queries go to `queries.md` `## Parked`; held work to `state.md` `## Held`; ideas to the Project note's Notes or a record; resolved items are deleted. No separate `parked.md`, which would recreate the catch-all.
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
created_at: 2026-10-13T23:50:00Z
---
```

   `id`, `level`, `title`, `project`, `theme`, `label`, `worker`, `supervisor` and `created_at` keep today's rules; `description` is new and required at every level.

14. **The description is written for routing,** in the skill description's voice: third person, what the work does, then "Takes ..." naming the kinds of unit it accepts, then "Not for ..." naming the neighbouring works by id. The work's steward writes it at seeding with State of play, and only the steward edits it; State of play may propose a change by a Messages line.

15. `state.md` front matter, closed set: `state`, `target`, `hold`, `blocking`, `since`, `received`, `beat`, `mark`, with today's rules, plus one new field, `method_read`, the short ki-agentic-harness revision whose `ki-coordination` and `ki-work-folder` guidance the worker last read. It replaces the uneven body line and makes refresh targetable (see 29).

16. **No `active` or `accepts` field.** Whether a work can take a routed unit is derived from its state: every state except `finished` can receive; `on-hold` receives without waking (see 26). A work winding down says "Not taking new units" in its description, as Ways of working will before it closes.

17. **The holder and its role stay derived,** now across two files: `worker` and `supervisor` from `work.md`, `state` and `target` from `state.md`. `ki work status` keeps its `ki/work-status/v1` output, so the Observatory sees no change; only its reader changes.

### Progressive reveal: who reads what, when

18. Four levels, by analogy with the skill's metadata, body and references:

| Level | Files | Size per work | Who reads it, when |
| --- | --- | --- | --- |
| 1. Register | `work.md` front matter and `state.md` front matter | about 150 tokens | State of play at each routing; `ki work status`, the Observatory and `ki work` views; an opener |
| 2. Definition | `work.md` body | under 300 words | State of play when two descriptions match; the owner checking a routing; a new session before it reads state |
| 3. Pick-up | `state.md`, `messages.md`, `queries.md`, `decisions.md` | as small as the limits below keep them | the work's own worker at bootstrap, re-anchoring, each owner message and each move |
| 4. On demand | reports, briefs, `design/` | unbounded | only when `state.md` or `queries.md` names one |

19. **Routing reads level 1 only.** Across today's 11 works that is under 2,000 tokens, against about 5,000 words of work files now. A sender reads nothing in the receiver's folder: it appends to `messages.md`. A run reads its brief and what the brief names.

### Size limits

20. Soft limits, linted as warnings like the skill budgets, never failures:

| File | Limit | Today's worst |
| --- | --- | --- |
| `description` | at most 500 characters, one to three sentences | absent everywhere |
| `work.md` body | at most 300 words | none exists |
| `state.md` body | at most 400 words; `## Now` at most five lines | 1,577 words in `ki.chezmoi` |
| `messages.md` | each line at most 60 words; a line older than 7 days on work that is not on hold | 7 lines from 18 October in `ki.chezmoi` |
| `queries.md` | more than eight open queries | 11 open tags in `ki.observatory` |
| `decisions.md` | more than 400 lines, or a mark older than 7 days on live work | 1,102 lines and a 15 October mark in `ki` |

21. **A heuristic history check** on `state.md` warns on dated "since" or "received" log lines, commit SHAs and test counts, the patterns findings 2 and 3 show.

### Routing and method stewardship

22. **State of play is the single dispatch coordinator,** as Kris agreed. Every new unit of work - an owner dump, a handoff with no owning work, a cross-work item whose owner is unclear, and every method improvement - comes to State of play, by Kris pasting a prompt there or by a line in State of play's own `messages.md`.
23. **Already-owned units go direct.** A work's own follow-ups, an item in a record that already names its work, and a reply to a message do not pass through the hub; State of play routes only what has no clear owner, as the review advised.
24. **State of play matches the unit against the register** (level 1) and, if needed, the definitions (level 2), chooses one work and writes one dated line in that work's `messages.md`: `- <date> · ROUTE · <Territory> > SoP: <the unit in the owner's words, with links>`. Where nothing matches, it proposes to Kris either a new piece of work, within the cap, or a record captured through `ki-next`. The register is derived from the work folders by `ki work status`; State of play keeps no copy of it.
25. **Receipt is compulsory; execution authority is not conferred.** The receiving worker acts on each line at its next bootstrap or owner message, as now, and records one disposition: taken into `state.md` next steps where its existing authority covers it; turned into a query in `queries.md` where it needs Kris's authority, capacity or a scope change; or sent back to State of play's `messages.md` with the reason where it is outside the work's scope. A unit is returned once: if State of play cannot place it elsewhere, it goes to Kris as a query rather than round again. Kris's "you have to accept it" is read as owning the disposition, never as authority to execute what the work's decisions do not cover.
26. **Held work keeps its hold.** A line routed to work On hold, paused, waits in `messages.md` without waking it; its count shows in State of play's register. Work On hold, more expected, is released by new work arriving under the existing rule, moving to Handoff to worker, and State of play gives Kris its resume line. If a paused work's line is urgent, State of play asks Kris to lift the hold.
27. **Method improvements go to State of play from every work,** by a `METHOD` line in its `messages.md`. While Ways of working exists, State of play routes them to it like any other unit, its description saying it takes method changes. That keeps one dispatch point and needs no exception.
28. **While the method is being defined, Ways of working sends refresh lines directly** into each affected live work's `messages.md`, under WOW-REFRESH a). Afterwards State of play sends them.
29. **Refresh is targeted and recorded.** After an approved method change lands, the sender writes one dated `REFRESH` line, only to works whose `method_read` predates the change and whom the change affects, linking the standard at its revision and stating the practical effect in a sentence. A sender may replace its own earlier `REFRESH` line not yet acted on, so changes coalesce. The receiver rereads at its next safe point, before launching further work, and sets `method_read`; updating the field is the confirmation, so no acknowledgement message is sent. Held work is not woken; the line waits. The existing bootstrap and update revision checks stay as the fallback.
30. **When Ways of working closes,** its description says "Not taking new units" for its last wave; at Finished, State of play's `work.md` description gains method stewardship and its Scope names where method changes go next (open decision STEWARD-HOME). State of play still executes nothing.

### Fit with the owning skills and the Work Process note

31. **`ki-work-folder`** owns the change: the closed list gains `state.md`, `queries.md` and `messages.md`; the work file's exact form becomes the definition form; the entry-point table gives other work one write, a line in `messages.md`; the tidy keeps a report until its outcome is homed, its queries having been copied at receive; the rubric's RECORD-2 and LIFECYCLE-1 move to the new files, and new criteria check the description, the size limits and the history heuristic.
32. **`ki-coordination`** keeps timing and judgement: Messages between work points at `messages.md`; Parking tangents and Putting work on hold park into `queries.md`; the owner report's Queries are rendered from `queries.md`; Territory work gains a Dispatch section (points 22 to 27); Refreshing this guidance gains targeted refresh and `method_read`; Bootstrap step 4 reads `messages.md`. The `ki-coordinator` output style's references to the work file's Messages section follow.
33. **`ki-delegation`** gains one line: at receive, the coordinator copies a report's queries into `queries.md`. The launcher still homes reports and never deletes.
34. **The Work Process note** changes its Words table (work file, state file, queries, messages), its Homes tree and the source of the Observatory fields; GDR-KI-PRINCIPAL-009 is refined in place, since it owns the work model. Under the Enactment Process that needs one ki-principal roadmap record for the note and the Decision Record together.
35. **`tools-ki`** changes `ki work status` to read `state.md` (output schema unchanged) and adds a routing view listing each work's id, state, pending-message count and description, the register State of play reads. One tools-ki record.
36. **Records:** one harness record covering `ki-work-folder`, `ki-coordination`, `ki-delegation` and the output style; one tools-ki record; one ki-principal record. Folded into existing records where one fits, under the fewest-records rule.

### Migration

37. **Tolerance and readers first.** Before any folder splits, the standard, the rubric and every reader of the work file (`ki work status`, openers, hooks) accept both shapes, telling them apart by whether `state.md` exists, so no work and no territory view breaks while it migrates. A folder holds one authoritative copy of each kind at a time: until it switches, senders write to its `## Messages` section; once `messages.md` exists, there and never both. The window closes when every live folder in every Capital has migrated.
38. **Pilot two folders together:** `ki.ways-of-working` (active, and the author of the method) and `ki.regular.registry-removal` (On hold, paused, with stale messages), the one-active and one-held pilot the review asked for, also proving held-work routing and refresh.
39. **Each live work then migrates itself at its own next mark,** because only a folder's own work writes or deletes there, and a session holding the old shape in memory would rewrite a folder migrated from outside. Its steward lets its runs finish, rechecks the folder's current contents and switches once. State of play names each unmigrated folder in that folder's Messages at its own mark.
40. **Held works migrate by one owner-approved mechanical run,** since they have no session to do it: `ki`'s territory hold precedent of 15 October and the 18 October work migration both did this. The run touches only work On hold with no live session, splits files mechanically, keeps the hold and mark unchanged, drafts each description for the steward to confirm at release, and resolves nothing else.
41. **The split is mechanical per folder:** old front matter divides between `work.md` and `state.md`; Goals and Scope are drafted from the Project note's `outcome` and the scope text findings 6 found in next steps; `Next steps` is cut to what is still to do, history dropped to Git; Messages move to `messages.md`, with the MIGRATED line removed by the migration itself; every open query tag is resolved to its text from wherever it lives today (reports, state-folder reports, design notes) into `queries.md`, and a tag whose text cannot be recovered becomes one `## Open` entry saying so and asking Kris, never dropped; held items go to `## Held`; then a tidy. One commit per folder, `docs(work): <id> package migration`.
42. Per-folder starting points, from the stocktake:

| Work | Description drafted from | Main moves |
| --- | --- | --- |
| `ki` | Charter and Territory work | queue and dated reviews to `state.md`; 4 parked queries to `queries.md`; decisions mark overdue |
| `ki.baseline-rollout` | Project outcome; seed scope | seed scope to Scope; WAVE-1 text recovered into `queries.md`; resolve the `+/_WORK_REVIEW/` twin |
| `ki.chezmoi` | Project outcome | six evidence paragraphs to Git; 11 messages acted on or kept; parked entries split; most of 25 reports pruned |
| `ki.knowledge-acquisition` | Project outcome; numbered steps | method steps to Goals and Scope; 8 queries in full from the design note |
| `ki.mac-studio-setup` | Project outcome | queries to `queries.md`; screen to-do lists to `## Held`; 9 tags recovered from retired reports or raised as lost; script out of `design/` |
| `ki.observatory` | Project outcome | dated log to Git; 11 open queries in full |
| `ki.regular.registry-removal` | regular work's purpose | old message block and duplicate resume text removed; pilot |
| `ki.regular` | Work Process regular work | minimal |
| `ki.timelines` | Project outcome | 7 queries from `design/survey.md` |
| `ki.tools-burndown` | Project outcome | numbered log to Git; 5 queries recovered from state-folder reports; JSON evidence out of `design/` |
| `ki.ways-of-working` | Project outcome | done items to Git; pilot |

43. **`kb.regular.acquire-intake`** migrates with the personal territory; the `+/_WORK_REVIEW/` folders migrate when they leave review; the seven Capitals still on `+/_CHECKPOINTS/` and `+/_THREADS/` move straight to the package shape at their own territory migration, skipping the intermediate form.

## Open decisions

### PACKAGE-NAME - What to call the packaged folder

- a) (recommended, confidence medium - the name was settled a day ago and renames are still being cleaned up, and "work package" means the lowest WBS deliverable, our work item) Keep "work folder" and `ki-work-folder`; describe the shape as packaged like a skill.
- b) Adopt "work package" as the concept and rename the skill `ki-work-package`, path unchanged; matches Kris's word, at the cost of another rename across harness, `ki`, chezmoi links and configuration.
- c) Use "work package" in prose only, skill unchanged; two names for one thing.

### STATE-FILE - Where the moving state fields live

- a) (recommended, confidence medium - matches Kris's "state ... in their own files", keeps `work.md` stable like `SKILL.md` and splits the logbook, at the cost of one `ki work status` and rubric change) State fields in `state.md` front matter, with `## Now`, `## Next steps` and `## Held`; `work.md` holds only definition.
- b) State fields stay in `work.md` front matter and only the prose moves to `state.md`; no reader change, but `work.md` changes at every move.

### QUERIES-FILE - The Q file

- a) (recommended, confidence high - six of eleven works have open queries with no text in the repository, and reports are kept alive only for their queries) `queries.md` holds every open and parked query in full; the owner report's Queries are rendered from it; reports are pruned once their outcome is homed.
- b) `queries.md` as an index of tags pointing to their reports; less copying, but the report coupling and the state-folder gap remain.

### PARKED-HOME - Where parked items go

- a) (recommended, confidence medium - today's `Parked` mixes five kinds, and a separate file would keep the mix) Parked queries in `queries.md` `## Parked`, held work in `state.md` `## Held`, ideas in the Project note or a record; no `parked.md`.
- b) A separate `parked.md` for everything parked, as Kris floated.

### MESSAGES-FILE - Where the inbox lives

- a) (recommended, confidence high - senders today write into the file the owner rewrites at every move, and a separate file makes the one permitted write checkable by path) `messages.md` beside `work.md`; other work appends one line there and nowhere else.
- b) Keep a `## Messages` section, moved into `state.md`.

### DESCRIPTION-SHAPE - The routing description

- a) (recommended, confidence medium - a skill-style description is what routing can match, and the Project `outcome` states the end, not what the work takes) A required `description` in `work.md`, at most 500 characters, "does ... Takes ... Not for ..." naming neighbours by id, steward-written; Goals link the Project `outcome` rather than copy it.
- b) Route on the Project note's `outcome` alone, no description in the folder; one fewer field, but regular and territory work have no Project note and the outcome says nothing about intake.

### ROUTE-RECEIPT - What a routed work must do

- a) (recommended, confidence high - Kris's "you have to accept it" with the review's no-authority and held-work rules) The receiver must act on every routed line at its next bootstrap or owner message and record a disposition (next step, query to Kris, or reasoned return to State of play); routing confers no execution authority; paused work keeps the line pending, more-expected work is released by it; already-owned units do not pass through the hub.
- b) The receiver acts on routed lines only at its next mark; less interruption, slower routing.

### REFRESH-TARGET - How method refresh reaches works

- a) (recommended, confidence high - dated lines and revision checks already exist; this adds the missing field and targeting) Record `method_read` in `state.md`; send one coalescing `REFRESH` line only to affected works behind the change; the field update is the confirmation; held work waits; bootstrap checks stay as the fallback.
- b) Broadcast every method change to every live work and ask for a one-line acknowledgement; simpler to send, noisier to receive.

### STEWARD-HOME - Who carries method changes after Ways of working closes

- a) (recommended, confidence low - the volume of method change after the definition settles is unknown, so start with the lightest home and revisit) State of play keeps the method backlog and dispatches each accepted improvement as ad hoc regular work, `ki.regular.<slug>`, or into the Project it most affects, using `ki-work-design` reviews for shape changes.
- b) A standing regular work for method upkeep, defined by an Activity note with a periodic review of incoming improvements.

### MIGRATE-PATH - How the live folders move

- a) (recommended, confidence medium - pilots one active and one held work as the review asked, and respects that only a folder's own work writes in it) Tolerance window first; pilot `ki.ways-of-working` and `ki.regular.registry-removal`; then each live work migrates at its own next mark; held works by one owner-approved mechanical run; other Capitals straight to the package at their own migration.
- b) One owner-approved mechanical sweep of all eleven folders at once after the pilot; faster, but writes into active works' folders from outside.
