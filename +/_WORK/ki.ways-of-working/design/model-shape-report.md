---
note_type: streams/design
updated: 2026-10-25T00:58:00Z
author: Written with Claude
---

# Model shape: one State of play, many packages: merged report

**Brief:** [model-shape.md](model-shape.md) · **Reviews:** [model-shape-review-codex.md](model-shape-review-codex.md) (GPT-6, Codex), [model-shape-review-claude.md](model-shape-review-claude.md) (Claude Opus 5.5, Claude Code) · **Date:** 2026-10-25

**Status:** merged report under `ki-work-design`, awaiting Kris's decisions. Nothing here is a standard; no standard, Pillars note or package file has changed.

## Summary

Both reviews accept the spine Kris drew: a package is where work lives, a thread is who acts on it, and every write goes to the package the work belongs to, whichever thread makes it. Both accept that one State of play thread may look after the Project packages of its territory, that queries and decisions stay in each Project's own package, that the active-work cap counts packages, and that the no-host rule protects a thread's seat while a host requirement is a fact about the work.

They tighten the brief in four places. Stewardship is an explicit assignment, changed only by an acknowledged handover, not something inferred from whether a thread is open; a record's `project` field finds its package but authorises nothing; `covers` stays as the main State of play's register beside a new upward `parent`; and a host requirement constrains device-dependent execution, not every action on a line. The brief also missed five current rules that assume one session per piece of work, one package per turn, or commits only at sends and receives.

The model below is the brief's, corrected by the reviews. Six questions go to Kris; the commit and push questions are not repeated here, since COMMIT-CADENCE and PACKAGE-PUSH already carry them, but both reviews bear on them (see [Bearing on COMMIT-CADENCE and PACKAGE-PUSH](#bearing-on-commit-cadence-and-package-push)).

## Corrections to the brief

- **"Thread" is not a missing word** (conflict 3) - the coordination Glossary already defines thread as "the thread model's word for a session's line of work; read as the work it carries" and session as a runtime instance on "a piece of work". The change is to rewrite thread and amend session so that a thread may act in several packages, not to add a word. Both reviews; checked against `standards-coordination.md` Glossary.
- **One session, one piece of work** - `ki-work-package` Work identity and native sessions says a native session "belongs to at most one piece of work". The cascade must amend this as well as the bootstrap level check (conflict 15). Both reviews; checked.
- **Turn budget** - the coordinator turn reads are "limited to the work package", singular; a State of play acting across packages needs a rule for it. Claude review; checked in the coordination Turn budget.
- **Commits only at sends and receives** - the Work Process note, Git is the logbook, says "Only sends and the supervisor's receives commit"; shared-writing point 1 and COMMIT-CADENCE overturn it, so the Work Process record must carry it. Both reviews; checked.
- **Pull order** - the coordination standard's Keeping primary checkouts current says a coordinator "pulls only with `--ff-only` into a clean checkout" and skips a dirty one; the brief's "pull with rebase" contradicts it, and `git pull --rebase` refuses a dirty shared tree. Claude review; checked.
- **"commits and pushes"** - Committing the work folder already says the coordinator "commits and pushes its work folder" at sends, receives, marks and holds; the brief dropped "and pushes", which is the half of the clash Kris's fifth problem turns on. Claude review; checked.
- **Report homing** - the background-run standard has the launcher copy a report "into the owning work folder", the launching work's; launching a run for another package is a `ki-delegation` change as well as a `ki agent launch` one. Codex review; checked.
- **"Links point upward" is not breached by `covers`** (conflict 8) - the rule says the Project note never links down into a work folder; `covers` links one work folder to others inside the working area. Retiring it is a design choice, not a correction. Claude review.
- **`self` is not a holder** - the holder vocabulary is `owner`, `agent`, `run/<name>`, `work/<id>`, `person/<handle>` and `repo/<name>`, and the current holder is derived, never stored. Both reviews; checked.
- **A Project-less record is not an ownerless one** (conflict 16) - record classification deliberately allows upkeep without a Project and regular work; the diagnosis is invalid. Codex review.
- **The one-day stale-steward flag** would fire on a Project waiting on Kris, which has no beat by design; the existing stuck view already covers a dead thread holding the work. Both reviews.
- **One steward does not confine conflicts to `messages.md`** - the launcher appends on the steward's instruction, design writers can collide on a note, a tidy can delete a report while the launcher homes it, and two clones can both act as the same steward. Codex review.
- **Deferred host questions** - coordination `sources.md` already asks whether host-bound agents "are held in the checkpoint with a host constraint"; HOST-TARGET answers part of it and should fold it or leave the rest deferred. Claude review.

## Model

### Units

The brief's five units stand: State of play, Project package, thread, run and record. Two words change meaning. **Thread** becomes a session acting on work, seated in one package and able to act in others it stewards. **Steward** keeps its entry-point sense, the work that may write a package's own files, and is named distinctly from method stewardship wherever both appear.

### The cascade, corrected

1. **Assigned steward.** Each Project package has one assigned coordinating work: the State of play that covers it, or the Project's own coordination thread. The assignment is committed, names a work and never a host or session, and is not the holder: the State of play may be assigned while the work lies with Kris or is On hold, and assignment neither receives the work nor releases its hold. Field home: STEWARD-FIELD.
2. **Handover, never inference.** Opening a Project's own thread asks for a handover: the old steward reconciles runs in flight, queued launches and pending writes, stops launching for the package, and the assignment change is committed in one write; the new thread acknowledges it before acting and takes the in-flight runs as their supervisor. Closing the thread hands back the same way. A closed session, quiet thread, missing binding or old beat transfers nothing; uncertain ownership is reported, not reassigned.
3. **Full entry point.** An assigned State of play is the package's coordinator for every entry-point purpose, including tidying on the owning work's behalf; a package with another steward still gets one line in `messages.md`.
4. **Delegating down.** A stewarding State of play may brief runs straight into the package; the brief names both the reporting package and the product repository, and the launcher homes the report into the reporting package whoever launched it.
5. **Reporting.** One territory Summary; each item names its package; a query is identified as `(work id, tag)`, since two packages may share a tag; it lives in that package's `queries.md` and Kris's answer is logged in that package's `decisions.md`. Each package keeps its own state, `since`, mark and beat: a territory mark does not move Project marks, and an acknowledgement of the Summary moves only the work it clearly names. A decision spanning Projects is kept once at the territory home, never copied as several grants.
6. **Turn budget.** A State of play turn acts in one package, that package's read being its one package read; the Summary rolls the rest up from `ki work status`.
7. **Cap, hold and commits** as the brief: the cap counts packages neither On hold nor Finished; a territory hold drains Project packages first, asking a package with its own steward to drain rather than writing it; a commit subject names the package whose state changed and the acting work where useful, and a multi-file move stays one coherent commit.
8. **Creation.** A State of play may create a package it will steward only for a registered Project, within the cap, in the state its actual move supports; it never seeds `with-worker` merely because the package is missing. The On hold first-message exception stays for dormant Projects.

### Records

A record's `project` resolves, through the registry, to a Project, its territory and its package. It authorises nothing: selection into `now` under `ki-next` neither opens the work nor grants execution, and the link into the package's next steps is written by its steward, from a line, at its next wake. The record stays in its owning repository with its holds, readiness and acceptance. A record with no `project` first goes to its existing owner, such as regular or ad hoc work; only an unresolved unit reaches State of play's routing queue, and Tending flags it. A classification change never moves a running record without reconciling its runs and reports.

### Relationships

Every package below the main names the State of play that coordinates it as `parent`, which for ad hoc work means the coordinating State of play, not the id's regular-work parent. The main keeps `covers` as its register of record, because coverage of a registered Project must survive before its package exists and after it is pruned; `ki work status` checks `parent` against it, with same-territory, uniqueness and cycle checks. A thread carries no committed metadata; until `ki thread` ships its relationship is its opener and label.

### Hosts

A thread's **seat**, the host it runs on, is never committed: no package, hold or report says where work comes back up. A **requirement**, a host or category the work needs, is a fact about the work and may sit on the smallest unit it constrains: a message line, a brief, a record, or the whole package's existing `label` suffix. A coordinator establishes its host at bootstrap and re-anchoring by mapping the local machine to the territory's machine inventory, which Rig owns for Knowledge Islands, rather than trusting raw `hostname -s`. What a requirement restricts is HOST-TARGET.

### Shared writing

Shared writing is wholly COMMIT-CADENCE and PACKAGE-PUSH. Two parts settle here without a query: the launcher commits each report it homes, by explicit path, as one verified unit; and the `messages.md` merge stays as it is, with ordinary conflict detection and explicit reconciliation, until the pilot shows recurring conflicts under the new cadence. Both reviews reject a union merge driver now, since it can resurrect a consumed line or disturb IMPORTANT order while looking clean, and both reject one file per message as a closed-list change, not a conflict fix.

## Agreement and difference

| Point | Reviews | Settlement and evidence |
| --- | --- | --- |
| 1 package and thread | Codex Agree, Claude Agree | Adopted; the Glossary's thread and session entries are rewritten. |
| 2 default steward | Codex Differ, Claude Agree | Settled as explicit assignment with acknowledged handover (CASCADE-STEWARD): the holder vocabulary and the binding rules give no liveness signal to infer from. |
| 3 `steward` in `state.md` | Codex Differ, Claude Differ | Both reject `self` and a holder reading; they differ on the home (STEWARD-FIELD). |
| 4 binding as evidence | Codex Differ, Claude Agree | A binding records identity, not liveness; it is evidence of nothing beyond its host. |
| 5 runs into the package | Codex Agree, Claude Agree | Adopted, with the `ki-delegation` report-home change. |
| 6 queries and answers in the Project | Codex Agree, Claude Agree | Adopted, with `(work id, tag)` identity (CASCADE-REPORT). |
| 7 cap counts packages | Codex Agree, Claude Agree | Adopted. |
| 8 `project` selects the package | Codex Differ, Claude Agree with correction | Resolution only, no authority; the steward writes the link (RELATIONS). |
| 9 create in any state | Codex Differ, Claude Agree with limit | Registered Project, within the cap, state from the actual move (CASCADE-STEWARD). |
| 10 `parent` up, `covers` derived | Codex Differ, Claude Differ in part | `parent` adopted; `covers` kept and checked (RELATIONS). |
| 11 threads carry no committed metadata | Codex Agree, Claude Agree | Adopted; opener and label until `ki thread` ships. |
| 12 seat and requirement | Codex Agree, Claude Agree | Adopted (HOST-SEAT). |
| 13 act only on own-host lines | Codex Differ, Claude Agree with addition | Reviews disagree on scope (HOST-TARGET); both want inventory names. |
| 14 commit at the write, pull before | Codex Differ, Claude Differ | Both correct the pull order and Codex the unit; carried to COMMIT-CADENCE. |
| 15 push work-folder stacks | Codex Differ, Claude Agree with limit | Reviews disagree; carried to PACKAGE-PUSH. |
| 16 only `messages.md` conflicts | Codex Differ, Claude Agree in substance, Differ on timing | Not a guarantee; no merge change before pilot evidence. |
| 17 Valle Armonia pilot | Codex Agree, Claude Agree with addition | Adopted for the cascade; host requirement piloted in `ki.chezmoi`. |
| Add: handover of runs in flight | Codex Add, Claude Add | Adopted into the handover rule. |
| Add: one turn, one package | Codex Add (aggregate budget), Claude Add | Adopted. |
| Add: per-package moves and marks | Codex Add | Adopted into reporting. |
| Add: ad hoc `parent` meaning | Claude Add | Adopted: the coordinating State of play. |
| Add: observable pilot exit conditions | Codex Add | Adopted into the rollout plan. |

## Bearing on COMMIT-CADENCE and PACKAGE-PUSH

These two queries are already open in this work and are not repeated as decisions here. The shape reviews bear on them, and the coordinator should reconcile both before they reach Kris again:

- **COMMIT-CADENCE's pull.** Kris's read-back says the coordinator "pulls with rebase at every wake". The coordination standard says a coordinator pulls "only with `--ff-only` into a clean checkout" and skips a dirty one; a rebase refuses a dirty shared tree, and autostash would touch another session's changes. Both shape reviews correct it to fast-forward before the commit, and Codex adds that the unit committed is the smallest complete, verified one, not each file write.
- **PACKAGE-PUSH.** The cadence blind review on Codex agreed with it; the shape review on Codex, at high confidence, rejects a push permitted by path alone and asks for a bounded grant naming publisher, repositories, refs and ancestor inspection, since briefs and decisions under `+/_WORK/` can carry unreviewed material. The Claude shape review agrees with the narrow exception but notes it does nothing while any product commit lies beneath, and pairs it with each session pushing its own product commits at once, which the 14 October words already allow. PACKAGE-PUSH's recommendation should now say the reviews disagree.

## Rollout plan

1. Kris's decisions on the six queries below, with COMMIT-CADENCE and PACKAGE-PUSH, recorded in `model-shape-decisions.md`.
2. One Knowledge Islands Principal record for the Work Process note (Levels, the inbox, Words, Git is the logbook) and [GDR-KI-PRINCIPAL-009](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/GDR-KI-PRINCIPAL-009-the-work-model.md), amended in place.
3. A line to ki-agentic-harness for one record covering `ki-coordination`, `ki-work-package` and `ki-delegation`'s run packet and report home, the receiving repository capturing it.
4. A line to `ki.tools-burndown` naming the schema readers (`steward` or `worker`, `parent`, `covers` checks), run and package identity in `ki agent launch`, report homing, `ki agent prompts`, the Observatory's readers and the rubrics; the pilot waits until readers accept the new fields.
5. Pilot: one named Valle Armonia Project package stewarded by `va` for one wave. Exit conditions: the record stays in its owning repository; brief, report, query and answer reach the Project package; two packages hold the same tag without ambiguity; a handover to a dedicated thread stops the old writer; a Project hold survives a thread's closure; a fresh checkout resumes from committed state alone. The host requirement is piloted separately in `ki.chezmoi`, whose `terra:` and `sol:` lines are its case, once handover is shown.
6. Lessons written into the wave brief before any other territory adopts the model.

## Decisions

### CASCADE-STEWARD - a State of play looks after a Project package by explicit assignment and handover

**Context:** You want one State of play thread to keep every Project package in its territory sorted unless the Project has its own coordination thread. The brief made the State of play the steward automatically whenever no thread is open, with a one-day flag on a quiet thread. The Codex review differs: nothing committed or local can show that a thread is alive, so inferring stewardship from an absent thread risks two writers or none; it wants an explicit assignment that changes only by an acknowledged handover, which stops the old steward, passes its runs in flight to the new one and is committed in one write. The Claude review agrees the State of play should steward by default and independently adds the same handover of runs in flight; both drop the one-day flag, which would fire on a Project simply waiting on you. Both limit package creation to a registered Project within the cap, created in the state its actual move supports rather than `with-worker` by default.

**Query:** Should a State of play steward a Project package by an explicit committed assignment, set when it creates or adopts the package and changed only by an acknowledged handover when you open or close the Project's own thread?

**Options:**

a) (recommended, confidence high - reviews disagree on inferring stewardship from an absent thread; the state and session contracts give no liveness signal, and explicit assignment keeps the default you asked for) Yes: explicit assignment, acknowledged handover with runs in flight, no timeout takeover, creation only for a registered Project within the cap.

b) Infer it, as the brief proposed: the State of play steps in whenever no Project thread is open, with a flag on a quiet thread.

### STEWARD-FIELD - where a package records who looks after it

**Context:** The assignment needs a committed home that names a work, never a host or session. The brief proposed a new `state.md` field, `steward: self` or `steward: work/<sop id>`. Both reviews reject `self`, which is not a holder value, and both reject reading the assignment as the holder. The Claude review would reuse `work.md`'s existing `worker` field, `worker: work/va` when the State of play looks after it and `agent` when the Project's own thread does: no new field, the closed field set unchanged, and stewardship changes only when you open or close a thread, which is the slow rate `work.md` suits; the holder stays derived from `state` and `worker` as today. The Codex review wants a dedicated assignment with its own vocabulary, distinct from holder and session, and leaves its exact field to the design; a separate field keeps the assignment visible beside the state and avoids a third sense of "steward" only if it is named with care.

**Query:** Should the assignment be recorded in `work.md`'s existing `worker` field rather than a new field?

**Options:**

a) (recommended, confidence medium - reviews disagree; reusing `worker` adds no field and fits the slow rate of change, but a dedicated field is clearer beside the state) Yes: `worker: work/<sop id>` while the State of play looks after the package, `agent` while its own thread does.

b) A new dedicated field, taking `work/<id>` values only, never `self`.

### CASCADE-REPORT - one Summary for several packages

**Context:** When the State of play thread works several Project packages, you still get one Summary from it. Both reviews agree with the brief that each item names its package, each query lives in its Project's `queries.md` and your answer is logged in that Project's `decisions.md`, so any package can be picked up alone. Codex adds that two packages may use the same tag, so a query is named by work and tag; that each package keeps its own state, mark and beat, so a territory mark or your acknowledgement of the Summary moves only the work it clearly names; and that a decision spanning Projects is kept once at the territory, not copied as several grants. Claude adds that the five-call turn budget reads "the work package", singular, so a State of play turn should act in one package at a time and roll the rest up from `ki work status`.

**Query:** Should the State of play's Summary report each package as its own work, with work-qualified query tags, per-package marks and one package acted on per turn?

**Options:**

a) (recommended, confidence high - both reviews agree, and it keeps today's rule that queries and decisions live in the package) Yes, with all four additions.

b) One Summary as the brief proposed, without per-package marks or the one-package turn.

### RELATIONS - what a package and a record say they relate to

**Context:** You asked that the metadata say what each piece of work is related to. Both reviews agree every package below the main should name the State of play that coordinates it as `parent`, so a package read alone shows its territory, Project, theme and coordinator; for ad hoc work `parent` means the coordinating State of play, not the regular-work parent its id nests under. The brief would then derive a secondary's `covers` list from those `parent` fields and retire it; both reviews reject that, because coverage of a registered Project must hold before its package exists and after it is pruned, and because a coverage change would become a write to every moved Project's file instead of one commit in the main's. On records, both agree a record's `project` field finds its package through the registry, but Codex notes it authorises nothing: selection into `now` neither opens work nor grants execution, the steward writes the link into its next steps, and a record with no `project` goes first to its existing owner, such as regular work, before State of play routes it.

**Query:** Should every package below the main carry `parent`, with `covers` kept as the main's register and checked against it, and a record's `project` used only to find its package?

**Options:**

a) (recommended, confidence high - both reviews agree; it answers your metadata ask without losing coverage of Projects that have no package) Yes.

b) As the brief proposed: `covers` derived from `parent` and retired after a tolerance window.

### HOST-SEAT - committed host requirements, never a committed seat

**Context:** You asked that coordinators know which machine they run on so that work aimed at particular machines can be handled. The work-package standard contradicts itself: it says a package names "no host" yet allows a `(<host>)` label suffix for machine-limited work. Both reviews agree with the brief's resolution: the prohibition protects a thread's seat, where it runs and will resume, which goes stale at every move and stays out of every package, hold and report; a requirement, a host or category the work needs, is a fact about the work and may sit on a message line, a brief, a record or a package's label. Both want host and category names taken from the territory's machine inventory, which Rig owns for Knowledge Islands; Claude adds that the coordinator should map the local machine to that inventory rather than trust raw `hostname -s`, which varies on a Mac with network settings.

**Query:** Should the no-host rule narrow to the seat, allowing a host or category requirement on a line, brief, record or label, with each coordinator establishing its host from the machine inventory at bootstrap and re-anchoring?

**Options:**

a) (recommended, confidence high - both reviews agree, and it resolves a contradiction in the standard by narrowing rather than deleting the rule) Yes.

b) Keep the blanket no-host rule and drop the label suffix.

### HOST-TARGET - what a host requirement restricts

**Context:** With requirements allowed, a coordinator on one machine will meet lines meant for another. The brief and the Claude review would have a thread act only on lines untagged or tagged for its own host or category, leave the rest queued and count them in its banner; Claude adds an age flag so a line no live thread can take does not wait unseen. The Codex review differs: only device-dependent execution needs the device, so a coordinator elsewhere may still acknowledge the line, plan it, ask you about it or dispatch a run to an eligible host; and a blanket skip breaks the queue's order when the first or an IMPORTANT line is for another host. It also wants concrete hosts told apart from categories, and rules for unknown or renamed names, before the syntax is adopted. Both agree the syntax is an optional `@<host or category>` after the date, and the pilot runs in `ki.chezmoi`.

**Query:** Should a host requirement restrict only device-dependent execution, leaving any coordinator free to acknowledge, plan, ask about or dispatch the line in queue order?

**Options:**

a) (recommended, confidence medium - reviews disagree; restricting execution only keeps the queue's order and IMPORTANT lines intact, but a coordinator then handles lines it cannot finish) Yes, with an age flag on lines no eligible host has taken and host-versus-category rules settled before adoption.

b) A thread acts only on lines for its own host or category and leaves the rest queued and counted, as the brief proposed.

## Changes after review

- Stewardship moved from inference to explicit assignment with acknowledged handover, and the one-day flag dropped - Codex, with Claude on handover and the flag.
- `self` and the holder reading removed from the steward marker; its home made a query - both reviews.
- Package creation limited to a registered Project within the cap in a state backed by a move - both reviews.
- Reporting gained work-qualified tags, per-package marks, single-package acknowledgement and one package per turn - Codex and Claude.
- `covers` kept as the register; `parent` added on every package, with its ad hoc meaning - both reviews.
- A record's `project` reduced to resolution without authority; the steward writes the link; Project-less records go to their existing owner first - Codex, with Claude on the link.
- Host names taken from the inventory, not raw `hostname -s`; what a requirement restricts made a query; the host pilot moved to `ki.chezmoi` - Claude and Codex.
- Five missed conflicts added: Glossary session and thread, one piece of work per session, turn budget, commits only at sends and receives, and fast-forward-only pulls - both reviews.
- The launcher commits each homed report; `ki-delegation` joins the harness record - Codex, with Claude.
- No `messages.md` merge change before pilot evidence - both reviews.
- Pull order and push scope handed to COMMIT-CADENCE and PACKAGE-PUSH, with the reviews' disagreement on the latter noted - both reviews.
- Pilot exit conditions made observable - Codex.
