---
note_type: streams/design
updated: 2026-10-25T00:38:00Z
author: Written with Claude
---

# Model shape: one State of play, many packages: brief

**Status:** draft brief under `ki-work-design`, awaiting its two independent reviews. Nothing here is a standard; no standard or Pillars note has changed.

**Owner:** Kris Brown · **Owning repository:** knowledgeislands/ki-principal · **Owning work:** `ki.ways-of-working` · **Date:** 2026-10-25

## Problem

The Work Process note and the `ki-coordination` and `ki-work-package` standards assume one coordinating session per piece of coordinating work: territory work coordinates coordinators, each Project's package has its own coordination thread, and State of play reaches a Project only by writing one line into its `messages.md`. In use, Kris runs a territory such as Valle Armonia through one State of play thread, and the Project packages either sit idle or are worked by a thread that is not theirs. Four things follow from the current text:

- a State of play acting for a Project has no standing to write that Project's state, queries or decisions, so its work lands in the wrong package or nowhere;
- nothing records whether a Project has its own live thread, so State of play cannot know when to step in or stay out;
- a package names its Project and theme but not its State of play, except on a secondary, and the secondary's `covers` points down where every other link points up;
- host-limited work, such as `ki.chezmoi` lines prefixed `terra:` or `sol:`, has no sanctioned form, because the work-package standard says a package names no host while the same standard lets a label carry a `(<host>)` suffix.

Kris added a fifth on 25 October: one package is written by many sessions, and its changes sit uncommitted and unpushed long enough that checkouts drift and conflict.

## Owner's proposal

Kris, 24 October, as carried in State of play's VA-CONSOLIDATE entry and this work's SINGLE-THREAD, SOP-PROJECT-CARE and COORDINATOR-HOST lines:

> looking into how we can effectively do everything through a state of play thread alone. So sometimes it might not have anything to coordinate with, in which case it can delegate down the structure and it can deal with things. It should always still deal with things in the right work package, regardless of whether which thread is dealing with it, right? So there's a difference between work packages and threads, which are things working on the work packages. And basically, I think the idea is that we're taking stuff from effectively the road maps, we're creating then stuff within a work package related to the project that the roadmap item is in, for example. I know it probably is something that we need to get mapped out in terms of a lot of this and there's a lot of documentation to do really. ... I think the basic idea is that for something like Valley Armonia, we really only need to direct it through one single thread, which is focus at the state of play level, and it can then cascade down and deal with all of the work across the work packages that are within all of that.

On the State of play caring for Project packages:

> when you've got a state of play which is running, it also looks after any of the project work packages that are part of that and keeps those sorted out, unless, of course, I've got their own coordination thread, which it should know about somehow. I think one of the key things is that we need to add to the metadata of the threads, what it's related to, so that when we're using the coordination skill we know that and we can find it and look it up. But also it should probably be able to sort of keep a good eye on what it is anyway.

On hosts:

> coordination teams should use a hostname to understand who they're running on. Presumably, they do that already, but if that's not explicit in the skill usage of it, so that you can apply if there's things targeted to particular machines or categories of machines, then we should deal with that.

Kris, 25 October 01:30 BST:

> when there's a lot of changes in the work folder, the work is sitting there for a while and it's not getting committed. This makes it really difficult to keep the Git repositories in sync with the origin and other things which are also modifying the work packages because it's not regularly getting updates, pushes, and pulls.

VA-CONSOLIDATE's seven points also cover a lean Summary since the mark, one command per move and Tending's working-area clean-up. Those three belong to the coord-standard and tending-fold units and are out of this brief, except where the cascade changes what a Summary carries.

## Established facts

- Territory work "coordinates coordinators, routes new work and stewards method, executes nothing", and "Other work and State of play write into package only by adding a line to its `messages.md`, or replacing own line not yet acted on" - [Work Process](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Processes/Work Process/Work Process.md>), Levels table and The inbox is a queue.
- Each State of play "does project management only: it runs no delivery itself and routes all real work to Project work" - `ki-coordination` [Territory work](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md#territory-work).
- Project work is opened "only where there is active work to drive", and the only package State of play may create is an On hold one "solely to queue its first message" - `ki-coordination` [Coordinating work](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md#coordinating-work) and Seeding.
- The steward entry point is "its coordinator, or for regular and ad hoc work the session working it"; other work and State of play write "One line in `messages.md`" and "Never" anything else - `ki-work-package` [Entry points](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-work-package/references/standards-work-package.md#entry-points).
- The work file's closed field set carries `project` and `theme`; `parent` and `covers` are "required on a secondary State of play, else absent"; the territory is only the id's first segment - `ki-work-package` [Work file](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-work-package/references/standards-work-package.md#work-file).
- "Links point upward: the package names its Project, and the Project note never links down" - same section; the Work Process note's Homes says the same.
- `state.md` carries `beat`, "UTC time of the last heartbeat while with a worker", and nothing that says which thread, if any, is working the package - `ki-work-package` [State file](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-work-package/references/standards-work-package.md#state-file).
- A native session's binding lives "only in a machine-local runtime file, `~/.local/state/ki/threads/<repository>/<slug>.json`", is never committed and never moved between hosts; "Until the `ki thread` tooling and its hook registration ship, no binding is written" - `ki-work-package` [Work identity and native sessions](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-work-package/references/standards-work-package.md#work-identity-and-native-sessions).
- A package has "no vendor-session field, conversation URL, runtime identifier ... and no host" - `ki-work-package` [Prohibited payloads and claims](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-work-package/references/standards-work-package.md#prohibited-payloads-and-claims); yet the optional `label` is "the title with a `(<host>)` suffix, only for work limited to that machine" - Work file, and `ki-coordination` Work naming: "the machine is only added if its limited to that machine".
- "Neither file names a host; where a territory is seated is host data, not work state" - `ki-coordination` [Picking work up](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md#picking-work-up); a hold "never says which host the work comes back up on" - Putting work on hold.
- A roadmap record may carry `project`, "a Project registry slug, optionally territory-qualified", and it is optional - `ki-work-roadmap` [work item format](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-work-roadmap/references/standards-work-item-format.md).
- A sender "commits that path alone and pushes at once"; the steward commits "at every send, every owner receive, every mark and hold"; a session pushes only when "only its own commits are stacked", otherwise "leaves the push to the owner" - `ki-coordination` Messages between work, Committing the work folder and Pushing beneath other sessions, under Kris's words of 14 October.
- Runs "pull `--ff-only` before committing" and coordinators and short work-package runs "stay on primary `main`" - `ki-delegation` [Coordination](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-delegation/references/standards-background-runs.md#coordination).
- On 25 October at the start of this run, ki-principal's primary checkout held an unresolved merge of `+/_WORK/ki/messages.md` from another session, cleared by that session minutes later: the hot file in a shared package is `messages.md`.
- Kris took COMMIT-CADENCE on 25 October 01:30 BST, read back as "the coordinator commits at every package write, pulls with rebase at every wake, and pushes whenever only its own commits are stacked; runs commit each step as they go", with the standard change drafted by wow-coord-standard as a query - [decisions](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/decisions.md).

## The model

```text
                       Kris (supervisor)
                             |
            one front door: State of play thread  <- a thread is a session, never committed
                             |
          +------------------+-------------------+
          | acts as steward                      | sends a line only
          v                                      v
  +_WORK/va.<project>/   (steward: work/va)   +_WORK/va.<other>/   (steward: self, own thread)
  work.md  parent: va                         work.md  parent: va
  state.md queries.md decisions.md            ...
  messages.md  briefs/  <run>.report.md
          |
          | briefs and launches
          v
        runs  --> work product in its owning repository, report homed into the package it did work for
          ^
          | project: <slug> on the record selects the package
  Streams/Roadmap/ and member roadmaps: records
```

### Units, boundaries and hand-offs

| Unit | What it is | Boundary | Hands off by |
| --- | --- | --- | --- |
| State of play | Territory work: the main package `+/_WORK/<territory>/`, and any secondary `<territory>.sop.<name>` | The territory's registry, priorities, queue, routing, acceptance bundles and method stewardship; and, new, stewardship of each Project package that has no thread of its own | Route lines to stewarded-elsewhere packages; direct steward writes to its own cascaded packages; queries to Kris |
| Project package | `+/_WORK/<territory>.<project>/`, the five files and its reports, briefs and design notes | One Project's state, queries, decisions, messages and runs, whichever thread acts on it | Its queries to Kris through whichever thread stewards it; lines to other packages; reports in from runs |
| Thread | A native session working one package, its seat; it may act in others under the cascade | Runtime only: machine-local, never committed, rebuilt on each host | Owner reports to Kris; briefs to runs; commits to the packages it acts in |
| Run | A detached background agent, worker to the thread that launched it | Its brief's scope; its work product in its owning repository | Its report, homed by the launcher into the package whose work it did |
| Record | A work item in a repository's roadmap | One deliverable; its `project` field names the Project whose package coordinates it | Its status moves; acceptance bundles per package |

The distinction Kris drew is the spine: **a package is where the work lives, a thread is who is acting on it now**. Every write goes to the package the work belongs to, whichever thread makes it.

### How one State of play cascades

1. **Default steward.** A Project package with no thread of its own is stewarded by the State of play that covers it: the secondary whose coverage holds it, else the main. The State of play is then that package's coordinator for every entry-point purpose: it reads all five files, acts on its `messages.md`, writes its `state.md`, `queries.md` and `decisions.md`, keeps its briefs and reports in that folder and tidies it at that package's own sends and marks.
2. **Own thread.** When Kris opens a Project's own coordination thread, that thread becomes steward and the State of play steps back to the one-line write it has today. Closing the thread, or a hold, hands stewardship back.
3. **Knowing which.** The package records its current steward in `state.md` as a holder, `steward: self` or `steward: work/<sop id>` (query CASCADE-STEWARD). It is work state, not runtime identity: it names a work, never a host or session. The machine-local thread binding, once `ki thread` ships, is local evidence a thread is live; the committed field is the cross-host truth. A State of play finding `steward: self` with no move or beat for a day flags it rather than taking over.
4. **Delegating down.** Where a Project has nothing that needs coordinating judgement, the State of play briefs runs straight into that package: the brief in its `briefs/`, the run named under its slug, the report homed into its folder. `ki agent` needs a way to launch a run for a named package other than the launching thread's own.
5. **Reporting.** The State of play's Summary keeps the territory heading and banner, and each item names the package it belongs to; each query keeps its Project's tag and lives in that Project's `queries.md`; Kris's answer, given in the State of play thread, is logged in that Project's `decisions.md` (query CASCADE-REPORT). Acceptance bundles stay one per package.
6. **Cap.** The cap of three or four active Project works keeps counting packages that are neither On hold nor Finished, whoever stewards them; it limits Kris's attention, not sessions.
7. **Hold.** A territory hold drains each cascaded package as its steward, Project packages first and territory work last, as today.
8. **Commits.** A steward write is committed in the package acted in, its subject naming that package and the acting work, as in `docs(work): va.markhowarth-launch send to owner, by va`.

### How records flow

- A record's `project` field selects its package: `project: markhowarth-launch` in any Valle Armonia repository means `+/_WORK/va.markhowarth-launch/`. A territory-qualified value, such as `ki/agent-host`, selects that territory's package.
- Selection under `ki-next` into `now` puts the record into the package's `state.md` next steps by link; the package never copies the record's status, which stays in the record.
- If the package does not exist, the State of play creates it with the five files and `steward: work/<sop id>`, in `with-worker` when it is about to launch, widening today's On hold-only seeding exception.
- A record with no `project` goes to the main State of play's own package, which routes it as an owner-less unit; Tending's mechanical list should flag it, as Valle Armonia found with [VA-WEBSITE-SANC-011](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-SANC-011-add-reviews-edit-button.md).
- Runs, reports, acceptance bundles and decisions for the record all go to that package; nothing for a Project's record lands in the State of play's own folder.

### Relationship metadata

- **Packages point up.** Every package below the main records the State of play it answers to as `parent` in `work.md`: a Project, regular or ad hoc package names its secondary or the main, and a secondary names the main as today (query PARENT-UP). With `project` and `theme` already present and the territory being the id's first segment, a package read alone says what it relates to.
- **Coverage is derived.** A secondary's `covers` list is then the set of packages whose `parent` names it, which `ki work status` can derive; `covers` is the only downward link in the model and would be retired after a tolerance window, or kept and checked for agreement.
- **Threads carry no committed metadata.** A thread's relationship is its seat, the work id in its machine-local binding, from which `parent`, `project` and `theme` are one read away. The binding may carry the host because it never leaves the host.

### Host-bound work

The prohibitions protect one thing: a package must never say where its thread sits or will resume, because that is runtime fact and goes stale at every move between hosts. That is the **seat**. Work that genuinely needs a particular machine, or a category of machine, is a different thing: a **requirement**, and it is a fact about the work.

- **Seat, never committed.** A thread establishes its host at bootstrap and at re-anchoring, `hostname -s`, and keeps it in session and in its machine-local binding. No package, hold or report says which host the work comes back up on.
- **Requirement, committed where it applies.** A message line may carry a host or category tag after its date, such as `- 2026-10-25 · @sol · TAG · sender: ...` or `@mac-studio`; a brief and a record may carry the same. A whole package limited to one machine keeps the existing `label` suffix. A thread acts only on lines untagged or tagged for its own host or category, and leaves the rest queued, counted in its banner (query HOST-TARGET).
- **Categories.** The host and category names come from the territory's own machine inventory, which Rig owns for Knowledge Islands; the coordination standard names no machine.

This resolves the internal clash between "no host" and the `(<host>)` label: the prohibition narrows to the seat, and the label is one form of requirement.

### Many sessions writing one package

A package's writers are its steward thread, the launcher homing reports, design runs writing `design/`, other works and State of play adding lines to `messages.md`, and Kris through the Observatory. Several of them share one primary checkout on one host, and others write the same package from another host through Git. The model:

1. **Commit at the write.** Every writer commits its own paths by explicit path at the moment it writes, never batching across a turn: the steward at every package write, as COMMIT-CADENCE now runs; a sender its line alone; a run each design step; and the launcher each report it homes, which today it copies in uncommitted.
2. **Pull before the write.** Every writer pulls with rebase, or fast-forward only when its tree is clean, immediately before it commits, and the steward also at every wake, so a package is never more than one write behind its remote on any host.
3. **Push the package promptly.** The stall Kris describes is the push rule meeting many writers: on a shared checkout, another session's commits are nearly always stacked, so nobody may push and the package drifts. A commit touching only `+/_WORK/` paths is package state, not product. The model proposes that any session may push a fast-forward stack made only of work-folder commits, whoever made them, after its pull and the repository's hooks, while product commits keep the own-commits-only rule (query PACKAGE-PUSH, to be answered with wow-coord-standard's COMMIT-CADENCE query).
4. **One steward at a time.** The `steward` field means only one thread writes `state.md`, `queries.md` and `decisions.md`; the others write only their own kinds. Conflicts can then arise only in `messages.md`, where many append and one removes.
5. **The hot file.** `messages.md` conflicts are append-against-append or append-against-remove. A union merge driver for `+/_WORK/*/messages.md` would resolve them without a stop, but can resurrect a line the receiver has just removed; one file per message would end conflicts but changes the closed list and every reader (query MESSAGES-MERGE).

## Conflicts with the current text, and what would change

Each change goes through the Enactment Process: the Work Process note through a Knowledge Islands Principal record in `Streams/Roadmap/` with [GDR-KI-PRINCIPAL-009](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/GDR-KI-PRINCIPAL-009-the-work-model.md), the work-model decision, amended in place; the harness standards through ki-agentic-harness records under `ki-next`, delivered by this work's coord-standard successor; and the `ki` tooling through a line to `ki.tools-burndown`.

| # | Current text | Conflict | Proposed change |
| --- | --- | --- | --- |
| 1 | Work Process note, Levels table: territory work "coordinates coordinators ... executes nothing" | The cascade makes State of play a Project's coordinator when no thread is open | Territory work coordinates coordinators and stewards each Project package with no thread of its own; it still executes nothing, since runs execute |
| 2 | Work Process note, The inbox is a queue: State of play writes "only by adding line to its `messages.md`" | A stewarding State of play writes the package's own files | The one-line limit applies to a package with its own steward; a stewarding State of play writes as its steward |
| 3 | Work Process note, Roles and Words: no word for the package-thread split | Kris's "difference between work packages and threads" has no term | Add **thread** (a session working a package, its seat) and **steward** (the work whose thread may write a package's own files) to Words |
| 4 | `ki-coordination` Territory work: "runs no delivery itself and routes all real work to Project work" | State of play may brief runs straight into a stewarded package | It routes real work to Project packages, and for a package it stewards briefs that work's runs itself |
| 5 | `ki-coordination` Coordinating work, Opening and Seeding; `ki-work-package` Entry points, first-message exception | Seeding allows only an On hold package for a first message | State of play may create a package it will steward, in any state, with `steward: work/<sop id>`; a Project thread is opened only when Kris wants one |
| 6 | `ki-work-package` Entry points: steward is "its coordinator" | Does not say who coordinates when no thread is open | Steward is the work named in `state.md`'s `steward`: the package's own thread, or the State of play acting for it |
| 7 | `ki-work-package` State file: closed field set | No way to know whether a Project has its own thread | Add `steward`, a holder, `self` or `work/<id>` |
| 8 | `ki-work-package` Work file: `parent` and `covers` only on a secondary | Packages do not say what they relate to; `covers` points down against "Links point upward" | `parent` on every package below the main; `covers` derived, retired after a tolerance window |
| 9 | `ki-work-package` Prohibited payloads: "and no host"; Work file `label` allows `(<host>)` | The standard contradicts itself, and host-targeted lines have no form | Prohibit the seat only; allow a host or category requirement on a message line, brief or record, beside the label suffix |
| 10 | `ki-coordination` Picking work up: "Neither file names a host"; Putting work on hold: never says which host it comes back up on | COORDINATOR-HOST needs a coordinator to know its host and filter lines | Keep both as seat rules; add to Bootstrap and Re-anchoring that the coordinator establishes its host and acts only on lines for its host or category |
| 11 | `ki-work-package` Messages lines: line shape has no requirement slot | Host-tagged lines are ad hoc today | Add an optional `@<host or category>` after the date |
| 12 | `ki-coordination` Pushing beneath other sessions: push only when own commits alone are stacked, under Kris's words of 14 October | Shared packages cannot be pushed promptly | A stack of only `+/_WORK/` commits may be pushed by any session; product commits unchanged |
| 13 | `ki-work-package` Entry points: launcher writes reports, commit not stated | Homed reports sit uncommitted | The launcher commits each report it homes, by explicit path |
| 14 | `ki-coordination` Report forms and Owner report | A single thread reporting several packages has no form | State of play's Summary names each item's package; queries stay in each package's `queries.md` with its tag; answers logged in that package |
| 15 | `ki-coordination` Bootstrap, step 3: level must match the opener | A State of play thread working a Project package is not a mismatch | The level check applies to the seat; acting in a stewarded package is not a re-bootstrap |
| 16 | `ki-work-roadmap` work item format: `project` optional | A record with no Project has no package to flow into | Keep it optional; route a Project-less record to the main State of play and flag it in Tending |

Tooling consumers named as changed: `ki work status` (the `steward` and `parent` fields, derived coverage, held host-tagged lines), `ki agent launch` (a run for a named package), `ki agent prompts`, the launcher's report homing, and the `ki-work-package` and `ki-coordination` rubrics.

## Reflection

1. A package is where work lives and a thread is who acts on it; every write goes to the package the work belongs to, whichever thread makes it.
2. A Project package with no thread of its own is stewarded by the State of play that covers it, with the full steward entry point, not the one-line write.
3. Whether a Project has its own thread is recorded in `state.md` as `steward`, a holder naming a work, which is work state and not runtime identity.
4. The machine-local thread binding is local evidence of a live thread, never the cross-host truth.
5. State of play may brief runs straight into a package it stewards, and those runs' briefs and reports live in that package.
6. Queries raised for a Project live in that Project's `queries.md` and Kris's answers in its `decisions.md`, even when asked and answered in the State of play thread.
7. The active-work cap counts packages, not threads.
8. A record's `project` field selects its package, and the package references the record without copying its status.
9. State of play may create a package it will steward in any state, widening the first-message seeding exception.
10. Every package below the main names its State of play as `parent`; `covers` becomes derived, keeping links pointing upward.
11. A thread carries no committed metadata; its relationship is its seat's work id.
12. The no-host rule protects the seat; a host or category requirement on a line, brief, record or label is a fact about the work and may be committed.
13. A coordinator establishes its host at bootstrap and re-anchoring and acts only on lines for its host or category, leaving the rest queued.
14. Every writer of a package commits its own paths at the moment of writing and pulls immediately before.
15. A stack made only of work-folder commits may be pushed by any session; product commits keep the own-commits rule.
16. With one steward at a time, only `messages.md` can conflict, and its merge needs a deliberate mechanism.
17. The pilot is Valle Armonia, which already runs as one State of play thread: one Project package stewarded by `va` through one wave, before any other territory adopts it.

## Rollout sketch

1. Two independent reviews of this brief, on different models or runtimes, then the merged report and Kris's decisions.
2. One Knowledge Islands Principal record for the Work Process note and [GDR-KI-PRINCIPAL-009](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/GDR-KI-PRINCIPAL-009-the-work-model.md), and one ki-agentic-harness record covering `ki-coordination` and `ki-work-package`, captured under `ki-next` from the decisions.
3. A line to `ki.tools-burndown` for the tooling consumers.
4. The Valle Armonia pilot, its lessons written into the wave brief for the other territories.
