---
note_type: streams/design
updated: 2026-10-25T00:48:00Z
author: Written with Claude
---

# Model shape: one State of play, many packages: review by Claude

**Reviewer:** Claude Opus 5.5 in Claude Code · **Date:** 2026-10-25 · **Read-only:** yes, apart from this file

Sources read: the brief, [Work Process](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Processes/Work Process/Work Process.md>), and in ki-agentic-harness `ki-work-design` with its standard and review template, the [coordination standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md) with its `sources.md`, the [work-package standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-work-package/references/standards-work-package.md), the [background-run standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-delegation/references/standards-background-runs.md) and the `ki-work-roadmap` work item format. The checkout and the installed harness copies of the three standards are identical. Not read, as the brief to this review required: the other review, `queries.md`, `decisions.md` and every run report, so COMMIT-CADENCE's wording is taken from the brief unchecked.

## Own view

The spine is right and overdue: a package is where work lives, a thread is who acts on it, and every write goes to the package the work belongs to. The cascade, the record-to-package flow, the seat-versus-requirement split for hosts and commit-at-the-write all follow from it, and I would adopt them.

The brief undercounts what the cascade breaks. Three current rules assume one session, one package, and none is in its conflicts table: the coordination Glossary says "a session works at most one piece of coordinating work" and defines thread as "read as the work it carries", which is the conflation Kris asked to undo; the coordinator turn budget limits reads to "the work package", singular; and both the Work Process note and the work-package Update lifecycle say "Only sends and the supervisor's receives commit", which COMMIT-CADENCE and point 14 overturn. The model also needs a handover rule for runs in flight when stewardship changes hands.

Two mechanisms want simplifying. The steward marker can reuse the existing `worker` party field in `work.md` instead of adding a new `state.md` field, and it avoids putting `self`, which is not a holder value, into the holder vocabulary and overloading "steward", which already means method stewardship. The pull rule as written, "pull with rebase, or fast-forward only when its tree is clean", is inverted for a shared primary checkout: a rebase refuses a dirty tree and the standards forbid stashing another session's changes, so the workable order is fast-forward before the commit and push straight after it, with a rebase only into a clean tree.

PACKAGE-PUSH helps only when every stacked commit is a package commit; one unpushed product commit beneath still blocks the push, so the fuller remedy is that every session also pushes its own product commits at once on a shared checkout, which the 14 October rule already allows.

## Fact check

- Territory work "coordinates coordinators ... executes nothing"; others write "only by adding a line" - confirmed, Work Process Levels table and The inbox is a queue.
- State of play "runs no delivery itself and routes all real work to Project work" - confirmed, coordination Territory work; the main State of play opener repeats it as "route real work to Project work", so `ki agent prompts` output changes too.
- Project work opened "only where there is active work to drive"; seeding solely for a first message - confirmed, coordination Coordinating work and Seeding; work-package Entry points repeats the exception.
- Steward entry point is "its coordinator, or for regular and ad hoc work the session working it"; other work and State of play "One line in `messages.md`" - confirmed, work-package Entry points table. The same table's steward row also says "Never: Another work's folder, except one line in its `messages.md`", which the cascade must amend as well as the definition (row 6 below).
- `parent` and `covers` "required on a secondary State of play, else absent" - confirmed, work-package Work file. The closed field set also holds `worker` and `supervisor`, which bears on CASCADE-STEWARD.
- "Links point upward" - confirmed, but corrected in scope: both texts say the work file names its Project and "the Project note never links down", that is, a canonical `Streams/` note never points into a work folder. A secondary's `covers` links one work folder to others inside the working area; it is not a breach of that rule as written, so retiring `covers` is a design choice, not a correction.
- `state.md` `beat`, and nothing naming the acting thread - confirmed, work-package State file.
- Binding machine-local, never committed, none written until `ki thread` ships - confirmed, Work identity and native sessions.
- "no host" in Prohibited payloads against the `(<host>)` label suffix - confirmed, work-package Prohibited payloads and Work file; coordination Work naming adds "The id, slug and title never carry a host".
- "Neither file names a host"; a hold "never says which host the work comes back up on" - confirmed, coordination Picking work up and Putting work on hold.
- Record `project` optional, "optionally territory-qualified" - confirmed, work item format.
- Sender "commits that path alone and pushes at once"; steward commits "at every send, every owner receive, every mark and hold"; own-commits-only push - corrected: Committing the work folder says the coordinator "commits and pushes its work folder" at those points, so the standard already requires a push at each, in tension with Pushing beneath other sessions; the brief drops "and pushes", which is the half of the clash problem five turns on.
- Runs "pull `--ff-only` before committing"; coordinators and short work-package runs "stay on primary `main`" - confirmed, background-run Coordination. Keeping primary checkouts current adds that a coordinator pulls "only with `--ff-only` into a clean checkout" and skips a dirty one "rather than stashed, rebased or reset"; the brief omits it and the model contradicts it.
- The 25 October unresolved merge of `+/_WORK/ki/messages.md` - not verifiable from the sources; taken as observation.
- COMMIT-CADENCE wording - not checked, `decisions.md` being outside this review.

## Conflicts table

| # | Check |
| --- | --- |
| 1-2 | Confirmed. |
| 3 | Corrected: "thread" is not missing. The coordination Glossary defines thread as "the thread model's word for a session's line of work; read as the work it carries", and session as one that "works at most one piece of coordinating work". The change is to redefine thread and amend session, not to add a word. "Steward" also exists already, as the work-package entry point and as method stewardship in Work Process and coordination; a third sense needs care (see CASCADE-STEWARD). |
| 4-6 | Confirmed; row 6 must also amend the steward row's "Never" column. |
| 7 | Confirmed as a gap; the simpler alternative is below. |
| 8 | Confirmed as a choice, not a contradiction (see Links point upward). Also missed: the main "records secondary and coverage in its `work.md` description, so routing reads one register", and "changing a coverage is a main decision, made in both `work.md` files in one commit". Deriving coverage from `parent` turns a coverage change into a write to every moved Project's `work.md`, which needs its own entry-point allowance for the main. |
| 9-11 | Confirmed. Missed: coordination `sources.md` Deferred host-move questions already asks whether agents "that must run on a specific host ... are held in the checkpoint with a host constraint"; HOST-TARGET answers half of that for lines and briefs, and the brief should either fold it or say it stays deferred. |
| 12 | Confirmed; see PACKAGE-PUSH for its limit. |
| 13 | Confirmed. |
| 14-16 | Confirmed. |
| - | Missed: Work Process Git is the logbook and work-package Update lifecycle, "Only sends and the supervisor's receives commit". Point 14 replaces both. |
| - | Missed: coordination Glossary, session "works at most one piece of coordinating work". |
| - | Missed: coordination Turn budget, reads "limited to the work package, `ki agent status`, one report and one short file". A State of play acting in several packages per turn needs either a per-package budget or a rule that a turn acts in one package. |
| - | Missed: coordination Keeping primary checkouts current and background-run Commits, both fast-forward only; the model's "pull with rebase" conflicts with both. |
| - | Missed: Committing the work folder's "commits and pushes", which conflicts with Pushing beneath other sessions today, before any change. |

## Points

| Point | Mark | Reason and evidence |
| --- | --- | --- |
| 1 | Agree | It is Kris's distinction verbatim and needs the Glossary's thread and session entries rewritten to carry it. |
| 2 | Agree | The full steward entry point is the only form under which a State of play can keep a Project package sorted, which Kris asked for; it needs the turn-budget and one-coordinating-work changes above. |
| 3 | Differ | Record it, but in `work.md`'s existing `worker` field, `worker: work/va` when the State of play works it and `agent` when its own coordinator does, rather than a new `state.md` `steward` field. Stewardship changes only when Kris opens or closes a Project thread, which is definition-rate change and suits `work.md`; `worker` already names the party on the worker side of the package's handoffs; and `self` is not a value in the holder vocabulary (`owner`, `agent`, `run/<name>`, `work/<id>`, `person/<handle>`, `repo/<name>`). If a `state.md` field is kept, its values should be `work/<id>` in both cases, never `self`. |
| 4 | Agree | Consistent with the binding rules. |
| 5 | Agree | Needs the `ki agent launch` target change the brief names. |
| 6 | Agree | Matches today's rule that queries live in the package and are rendered into the report; logging the answer in the Project's `decisions.md` keeps re-bootstrap of that package whole. |
| 7 | Agree | The cap limits Kris's attention; counting packages is the honest measure. |
| 8 | Agree, with a correction | Selection under `ki-next` is run by whatever session runs it; the link into `state.md` next steps is written by the package's steward at its next wake, by a line, not by `ki-next` directly, or the entry points break. |
| 9 | Agree, with a limit | Only for a registered Project, and only within the cap, since a package created `with-worker` is active at once. |
| 10 | Differ in part | `parent` on every package below the main: agree, it answers Kris's "what it's related to" for a package read alone. Retiring `covers`: not needed for the upward-link rule (see fact check), and it moves the main's one-commit coverage change into many Project files. Keep `covers` as the main's register of record and have `ki work status` check `parent` against it, which the brief offers as its fallback. |
| 11 | Agree | Until `ki thread` ships a thread's relationship is its opener and label; say so, so nobody reads point 11 as needing the binding first. |
| 12 | Agree | It resolves a real self-contradiction in the work-package standard by narrowing, not deleting, the rule. |
| 13 | Agree, with an addition | Take the host name from the territory's machine inventory, as point 12's Categories bullet says, mapped from the local machine, rather than from raw `hostname -s`, whose result on a Mac depends on network and sharing settings. A line tagged for a host or category no live thread holds needs an age flag in the banner, or it waits unseen. |
| 14 | Differ | Commit at the write: agree. Pull before the write: corrected order. On a shared primary checkout other sessions' uncommitted changes are normal; `git pull --rebase` refuses a dirty tree, and autostash would stash another session's changes, which Keeping primary checkouts current forbids. The workable sequence is pull `--ff-only` before committing, as the background-run standard already says, commit by explicit path, push at once; only if the push is rejected, rebase when the tree is clean, else report one line. COMMIT-CADENCE's "pulls with rebase at every wake" needs the same correction. |
| 15 | Agree, with a limit | Sound for a stack wholly of `+/_WORK/` commits, after fetch, fast-forward, hooks, never force. It does nothing when any product commit lies beneath, since a stack pushes as a whole; pair it with every session pushing its own product commits at once, which the 14 October words already allow. It amends an owner rule, so it is Kris's decision. |
| 16 | Agree in substance, Differ on timing | True only once writers commit and push at the write; with that in place the conflict window is a few seconds. Adopt the built-in `merge=union` attribute only if the pilot shows recurring conflicts, with a rubric check for a resurrected line; one file per message is out, as it changes the closed list. |
| 17 | Agree, with an addition | Valle Armonia fits the cascade, but has no host-bound lines; pilot the host requirement in `ki.chezmoi`, whose `terra:` and `sol:` lines are the case it is meant for. |
| - | Add | **Handover of runs in flight.** When Kris opens a Project's own thread, the State of play may have runs launched for that package whose reports the launcher homes there. The new thread's bootstrap writes the worker change and takes those runs as its own supervisor; the State of play stops launching for the package once it reads the change, which commit-at-the-write and fast-forward-before-the-write make prompt. Closing the thread reverses it. |
| - | Add | **Stale-thread rule is redundant.** Point 3's "no move or beat for a day" would flag a Project thread legitimately waiting on Kris, which has no beat by design. The existing stuck view, a worker-held item unmoved and unbeaten for 10 minutes, already covers a dead thread holding the work; nothing new is needed. |
| - | Add | **Ad hoc `parent`.** An ad hoc id `<territory>.regular.<slug>` already nests under regular work, while point 10 has it name a State of play. Say which `parent` means: the coordinating State of play, not the id's parent. |
| - | Add | **One turn, one package.** The simplest fix for the turn budget is that a State of play turn acts in one package at a time, rereading that package as its one read, and its Summary rolls up the rest from `ki work status`. |

## Open questions

- **CASCADE-STEWARD.** My view: record stewardship as `worker: work/<sop id>` in `work.md`, `agent` when the Project has its own thread; the brief's `state.md` `steward` field, with `work/<id>` values only, is the fallback. Confidence medium: both work, and the choice rests on keeping the closed field set and the word "steward" unchanged against making the marker visible beside the state.
- **CASCADE-REPORT.** Agree as written. Confidence high: it follows today's rule that queries and decisions live in the package.
- **PARENT-UP.** `parent` on every package below the main, `covers` kept as the main's register and checked against `parent`. Confidence medium: the brief's fuller derivation is also coherent, at the cost of a many-file coverage change.
- **HOST-TARGET.** Agree: an optional `@<host or category>` after the date (after `IMPORTANT` where present), names from the machine inventory, unmatched lines held and counted with an age flag. Confidence medium: the slot is sound, but the inventory's names and the deferred host-move questions should be settled together.
- **PACKAGE-PUSH.** Agree, narrowed to stacks wholly of `+/_WORK/` commits, paired with prompt pushing of each session's own product commits. Confidence medium: it amends Kris's 14 October rule and its benefit depends on how often product commits sit beneath.
- **MESSAGES-MERGE.** Defer: no merge mechanism until the pilot measures conflicts under commit-and-push at the write; then `merge=union` with a resurrection check. Confidence medium: the cause Kris described is uncommitted, unpushed work, which the cadence change addresses first.
