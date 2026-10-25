---
note_type: streams/design
author: Written with Codex
---

# Model shape: review by Codex

**Reviewer:** GPT-6 (Codex) · **Date:** 2026-10-25 · **Read-only:** yes, apart from this review

## Own view

Support the package-thread distinction and a State of play session coordinating work in several Project packages. The [Work Process][process] already makes work independent of a conversation. The change is principally to the assignment of coordination duties, the permitted writers and the operation of one session across several packages. It does not require merging the packages or moving their records.

The [brief][brief] needs revision before its proposed model becomes a rollout contract. Its most consequential claims overreach: a committed steward assignment cannot establish that one particular session is alive or exclude another writer; putting a record in `now` cannot open work or authorise execution; a missing `project` does not imply missing ownership; and a path beneath `+/_WORK/` cannot establish permission to publish its contents. Only having one assigned steward does not confine conflicts to the message queue.

Prefer an explicit assignment of package stewardship, changed through an acknowledged handover, over an automatic fallback based on whether a thread exists. Keep the existing work-state machine and per-package decision homes. Establish a safe shared-writing procedure separately from publication authority. Pilot one named Project package under Valle Armonia, then test a handover and a return from hold before widening adoption.

This view was formed without reading another review, any queries or decisions file, or a run report. The owner's proposal is taken from the brief; its original conversation and the reported Valle Armonia incidents were not independently available within the permitted source set. Recommendations below are proposals for the merged report, not decisions or implementation authority.

## Fact check

- **The conceptual split already exists.** Work Process, Overview and Homes, treats the session as a channel and the work item record as its own home. The [coordination glossary][glossary] already distinguishes sessions, threads and bindings. The missing part is permission for a single coordinating session to serve several packages, not the discovery that packages and sessions differ.
- **The current entry-point boundary is real.** Work Process, The inbox is a queue, and [package entry points][entries] limit another work and State of play to their message lines. [Tidying][tidy] separately reserves deletion to the owning work. Cascade must explicitly amend both boundaries, including acting on behalf of the owning work when tidying.
- **A second restriction is omitted from the conflict list.** [Native sessions][sessions] assigns a native session to at most one piece of work; the coordination glossary similarly limits a session to one piece of coordinating work. Permitting multiple packages requires defining a stable session identity and a changing acting package, not merely relaxing the bootstrap level check.
- **A steward assignment is not a holder or a liveness observation.** The [state schema][state] derives the holder from work state and roles. `self` is not in its holder vocabulary. A local binding records identity; neither that file nor a committed assignment proves continued activity. Existing heartbeat and stuck rules apply to work with a worker, not all packages indiscriminately.
- **The host wording does clash.** The [work-file schema][definition] permits a machine-limited label while [prohibited payloads][prohibited] broadly excludes hosts. However, discovering the current host does not itself conflict with prohibiting a host in committed state. Requirement and runtime seat are useful separate concepts; the blanket filter proposed for incoming lines is an additional policy choice.
- **Project classification is optional for a reason.** [Record classification][classification] explicitly includes upkeep without a Project, permits regular work, and preserves the owning repository's priority, planning and acceptance. A qualified Project reference needs resolution through that registry contract; it is not authority to write another Capital's package.
- **The ordinary commit cadence is narrower than the proposed cadence.** Work Process, Git is the logbook, and [package updates][updates] specify send and supervisor-receive commits; [coordination committing][committing] also names marks and holds. The brief describes a local cadence decision, but I have not read that decision under this review's independence boundary. Treat it as a reported local override, not an already verified universal rule.
- **Existing Git rules contradict unconditional pull and push proposals.** [Background-run coordination][runs] specifies fast-forward pulls, explicit-path commits and the model trailer. [Safe Git hygiene][git-safe] requires uncontested complete files and a serialised index/HEAD write window. [Pushing beneath other sessions][pushing] ordinarily excludes other writers' commits. Repository-specific grants can alter publication scope; this needs an explicit applicable grant, not an inference from paths.
- **Report homing and design writes are established entry points.** The launcher owns report homing; a named design run may write `design/`. [Design artefacts][design-home] are already committed when produced. Those facts support prompt commits of verified units, but do not make every intermediate file write a complete unit.

## Points

These marks cover every numbered Reflection claim. The subsequent sections also test the numbered cascade, shared-writing and rollout proposals.

| Point | Mark | Reason and evidence |
| --- | --- | --- |
| 1 | Agree | Preserve package homes and record authority; see [identity](#identity-and-stewardship). |
| 2 | Differ | Use assigned stewardship, not inferred thread absence; see [handover](#identity-and-stewardship). |
| 3 | Differ | Assignment is neither holder nor proof of an exclusive writer; see [handover](#identity-and-stewardship). |
| 4 | Differ | A binding records identity, not observed liveness; see [native sessions][sessions]. |
| 5 | Agree | Keep runs scoped to their acting package and its authority; see [operations](#operating-the-cascade). |
| 6 | Agree | Preserve Project homes and qualify tags when aggregating; see [operations](#operating-the-cascade). |
| 7 | Agree | The existing cap counts active work, including work with its supervisor; see [territory work][territory]. |
| 8 | Differ | Classification assists resolution; selection grants no execution authority; see [routing](#records-and-relationships). |
| 9 | Differ | Create only in the state supported by an authorised move; see [routing](#records-and-relationships). |
| 10 | Differ | Deriving coverage from existing packages loses absent Projects; see [relationships](#records-and-relationships). |
| 11 | Agree | Commit work relationships, keep native session identity local; see [identity](#identity-and-stewardship). |
| 12 | Agree | Distinguish execution requirements from session location; see [hosts](#host-requirements). |
| 13 | Differ | Host restrictions should constrain execution, not all coordination; see [hosts](#host-requirements). |
| 14 | Differ | Commit verified units; reconcile safely before editing shared files; see [Git](#shared-writing-and-publication). |
| 15 | Differ | A work-folder path is insufficient publication evidence; see [Git](#shared-writing-and-publication). |
| 16 | Differ | Ownership metadata does not eliminate file or semantic conflicts; see [Git](#shared-writing-and-publication). |
| 17 | Agree | One package and one wave is a sensible pilot boundary; see [pilot](#pilot-and-rollout). |
| - | Add | Define per-package moves, aggregate budgets, handover and failure recovery before rollout. |

## Identity and stewardship

Cascade claims 1-3 need a distinction between **assignment**, **work holder** and **current session**. State of play can be assigned coordination of a Project package while that Project's work is with Kris or On hold. It must not thereby receive the work, release its hold or become its holder. Use a dedicated stewardship assignment with a defined vocabulary rather than describing `self` as a holder. Its exact field and home should follow the agreed lifetime of the assignment.

Absence of a native binding, a quiet session or an old heartbeat is not permission to take over. A valid assignment can persist across session closure. Conversely, the same work id can be opened in two sessions on different hosts. A Git field travels eventually between clones; it supplies neither an exclusive lock nor immediate agreement between them. The proposed one-day warning is also inappropriate for work awaiting its supervisor or deliberately held. Use the existing state-sensitive heartbeat rules for observations, with uncertain ownership reported rather than reassigned.

Opening a dedicated Project thread should request a handover: reconcile in-flight runs, queued launches and pending writes, stop the previous steward starting more work for that package, commit the assignment change under one write window, and have the receiving steward acknowledge it before acting. The old session must revalidate the assignment on its next wake. A session closing unexpectedly leaves recovery work; it does not silently transfer authority. A hold retains its release condition and is independent of who will steward the next authorised move.

The simpler alternative is to record which work is assigned coordination, defaulting to the covering State of play only where the owner has approved that default, without trying to record whether a thread exists. Before tooling ships, an explicit handover and opener can operate this assignment. Do not invent bindings or liveness promises during the pilot.

## Operating the cascade

Cascade claims 4-5 are sound if each launch names both the reporting package and the product repository, carries the same scoped authority and immutable delivery evidence as before, and has an unambiguous run identity. Its launcher must home the report into the reporting package regardless of the launcher's session identity. The [run-packet contract][packet] currently ties the report home to the launching work, so this is also a `ki-delegation` change and a tooling dependency.

Keep queries and decisions in their owning package. In the rolled-up Summary, identify a query by `(work id, tag)` because different packages can use the same tag. Define how Kris's answer in the State of play thread is assigned to a package, how cross-Project decisions are kept once at their territory home, and how ambiguous answers are clarified. Never duplicate grants into several packages as if each were a separate approval.

Reporting is not merely presentation. Specify which packages are sent to supervisor, received, marked or left with workers when one Summary includes them. An acknowledgement of the overall Summary must not automatically receive every underlying package. Each package retains its own `since`, mark, heartbeat, open queries and held work. A territory mark must not move all Project marks. Acceptance remains a named bundle per work and still needs its normal grant.

Cascade claim 6 preserves the current cap, but the coordinator also needs a total launch and reading budget. Applying roughly three runs per package to four packages can multiply concurrency and context while leaving only one responsive session. Retain the turn budget across the whole session; read changed packages as needed and queue work when that budget is exhausted. Define which packages a wake checks without rereading every decision log on every turn.

Cascade claim 7 preserves Project-first territory draining. Add a branch for packages with dedicated stewards: State of play requests and confirms their drain rather than overwriting them. Losing a dedicated thread during a hold cannot release held work by fallback. Cascade claim 8's commit attribution is helpful, but multi-file moves should remain coherent units; the subject must identify the package whose state changed, with the acting work recorded where useful.

## Records and relationships

Use `project` to resolve an existing registry Project, its territory and Capital, then its package. A record remains in its owning repository and is linked from the coordinating package. Preserve repository authority, holds, dependencies, planning readiness and acceptance. A classification change must not move a running record between packages without reconciling its pending run and reports.

A `now` record can still be a draft awaiting planning. Package creation needs an approved Project opening within the cap; state follows the actual move. Do not seed `with-worker` because a package is missing, nor allow creation in literally any state. If the Project is unknown, its registry is unavailable, or its package is held or Finished, resolve that condition instead of fabricating an active package. The existing first-message exception remains useful for dormant registered Projects.

A record without `project` may already belong to regular or ad hoc work. Try its existing ownership and routing description first; only an unresolved unit belongs in State of play's routing queue. State of play can clarify or route it without becoming its delivery coordinator. Do not turn the main package into a substitute roadmap or an execution home for all upkeep.

Upward `parent` links simplify navigation, but coverage and stewardship are separate relationships. A secondary can cover a registered Project before its live package exists and after a finished package is pruned. Deriving all coverage from live folders loses that assignment. Preserve declared secondary coverage during the pilot, or choose a durable registry home for it before removing `covers`. Also specify same-territory validation, permitted parent levels, uniqueness, cycle rejection and what happens when a secondary is held or retired. Keep regular and ad hoc work self-coordinating unless a separate approved assignment changes that rule.

## Host requirements

Discovering the current host at bootstrap and re-anchoring is reasonable. A device requirement belongs with the smallest executable unit it constrains, with inventory names resolved explicitly. A tag must distinguish a concrete host from a category and define unknown names, renamed devices and unavailable inventory; a collision between a host and category must not silently widen eligibility.

Do not restrict every action on a targeted message to that host. A coordinator elsewhere can acknowledge it, ask Kris a question, plan it, or dispatch an authorised run to an eligible host. Only device-dependent execution needs the device. Conversely, a line without a tag cannot override a restriction in its linked record or brief. Conflicting requirements need resolution, and unavailable eligibility means no device-dependent execution.

Specify how host targeting interacts with IMPORTANT, FIRST-STEP and REFRESH order. An ineligible first line must neither disappear nor be silently overtaken contrary to the queue contract. It can remain with its disposition or query recorded, while independent eligible work proceeds under an explicit ordering rule. Count held requirements as held work without inventing a new state. Keep the current session's host out of portable work state and resume promises.

## Shared writing and publication

Shared-writing claim 1 should mean committing the smallest complete, verified unit promptly. Updating state, moving a query and recording its answer can require several file writes in one coherent commit. Committing every individual write can expose an invalid intermediate package and does not solve another writer editing the same complete file. Design artefacts already have a commit-as-produced rule; report homing needs an explicit verified commit boundary.

Claim 2 conflates reconciling before editing with pulling immediately before committing. Fetch and reconcile before taking an uncontested editing turn where authorised; recheck HEAD, index, changed paths and ownership under the serialised commit window. On a shared dirty checkout, do not rebase, autostash or repair another actor's work. A clean tree also does not make rewriting another writer's unpublished commits authorised. Fast-forward when safe; otherwise stop and coordinate the conflicting writer. An isolated delivery branch may rebase its own work under its existing contract. Neither procedure guarantees a clone is at most one write behind a remote that other writers can advance at any time.

Claim 3 needs a publication grant that defines eligible repositories, refs, content and checks, not just a directory test. Inspect every unpublished ancestor and its actual changes, including deletions, renames and mixed commits, and apply the repository's deployment and privacy constraints. Briefs and decisions can carry sensitive or unreviewed instructions even under a work-folder path. Prefer using an existing applicable grant, or a narrowly defined shared publisher, to giving every session blanket publication authority. Do not manufacture routine owner queries about stacked commits where the standard prohibits them.

Claim 4 is false as a guarantee. The launcher can append decisions on the steward's instruction; design writers can collide on a note; a tidy can delete a report while the launcher homes it; two clones can both act for the same assigned steward; and simultaneous message edits in one checkout can be committed together unintentionally. The [entry-point table][entries] is a permission model, not mutual exclusion. Apply complete-file ownership and serialised Git writes, and reserve deletion/homing overlap explicitly.

For claim 5, retain ordinary conflict detection and explicit reconciliation for the pilot. A union merge can restore a consumed instruction, duplicate it or disturb IMPORTANT ordering while appearing clean. A message identity and disposition check could later prevent replay, but need not become a new queue system before the pilot. One file per message also introduces priority, acknowledgement, deletion and closed-list changes; it is not a small conflict fix.

## Named conflicts

Each row tests the corresponding numbered conflict in the brief against the current source, rather than treating the proposed resolution as established.

| Conflict | Assessment | Required correction or boundary |
| --- | --- | --- |
| 1 | Real change | [Territory duties][territory] expand; execution still belongs to runs and record owners. |
| 2 | Real change | Amend [entry points][entries] and [tidying][tidy] for acting on behalf of the owning work. |
| 3 | Overstated gap | [Words][process] and [glossary][glossary] already separate work and sessions; define the assignment. |
| 4 | Real change | Amend [territory duties][territory] and [run report homes][packet], preserving delivery authority. |
| 5 | Real change | Amend [seeding][territory] only for approved opening; reject arbitrary initial states. |
| 6 | Real change | Extend [steward permissions][entries] with an acknowledged handover, not inferred absence. |
| 7 | Real schema change | [State][state] is closed; distinguish assignment from derived holder and liveness. |
| 8 | Real schema change | [Parent and covers][definition] are restricted today; preserve coverage without live packages. |
| 9 | Literal inconsistency | Narrow [host prohibition][prohibited] against [label exception][definition]; model requirements. |
| 10 | Mixed claim | [Pick-up][pickup] bans persisted host data, not discovering a host; queue filtering is new. |
| 11 | Real shape change | [Message syntax][messages] needs requirement and priority semantics together. |
| 12 | Real authority change | [Push policy][pushing] needs an applicable bounded grant; paths alone are insufficient. |
| 13 | Missing explicit step | Add verified report-homing commits to [launcher duties][packet] under [Git safety][git-safe]. |
| 14 | Real reporting change | Extend [reports][reports] with per-package moves, qualified tags and retained query homes. |
| 15 | Incomplete conflict | Amend [session cardinality][sessions] and [glossary][glossary], beyond the bootstrap check. |
| 16 | Invalid diagnosis | Optional [Project classification][classification] is deliberate; preserve regular-work routing. |

## Views on the open questions

### CASCADE-STEWARD

**Recommendation:** Explicitly assign coordination to the covering State of play or dedicated Project work, independently of holder and native session. Require an acknowledged transfer; closing a thread or holding work does not automatically transfer it. Do not use a one-day timeout as a takeover mechanism.

**Confidence:** high - the present state and session contracts directly establish the distinctions; exact field placement can remain a design choice.

### CASCADE-REPORT

**Recommendation:** Keep one territory Summary, package-qualified items and query tags, and queries and decisions at their existing homes. Define per-package send, receive, heartbeat and mark behaviour before the pilot; a single owner acknowledgement moves only the work it clearly identifies.

**Confidence:** high - this preserves the existing report and state contracts while allowing a shared channel.

### PARENT-UP

**Recommendation:** Permit a validated upward coordination relationship where useful, while retaining declared secondary coverage for the pilot. Do not retire `covers` until registered Projects without live packages still have a durable coverage assignment and migration checks preserve it.

**Confidence:** high - package creation and pruning make the missing-coverage case a direct consequence of the proposed derivation.

### HOST-TARGET

**Recommendation:** Represent an execution requirement on the relevant unit and resolve its host or category through the inventory. Let other hosts coordinate that unit; restrict device-dependent execution. Define unknown-target and IMPORTANT-order behaviour before adopting syntax.

**Confidence:** medium - the separation is supported, but the permitted sources do not establish inventory resolution or remote execution behaviour.

### PACKAGE-PUSH

**Recommendation:** Reject blanket permission based only on work-folder paths. Use a verified existing publication grant where applicable, or obtain a bounded grant naming publisher, repositories, refs, eligible content and ancestor inspection. Keep commit cadence independent of publication authority.

**Confidence:** high - the current Git and push contracts explicitly separate these permissions and require complete-file safety.

### MESSAGES-MERGE

**Recommendation:** Keep the single queue and ordinary conflict detection during the pilot. Reconcile consumption, replacement and priority explicitly. Consider message identity and replay protection only if observed conflicts justify more machinery; do not enable a union driver now.

**Confidence:** high - the brief itself identifies resurrection, and the source queue contract makes replay and priority material.

### COMMIT-CADENCE

**Recommendation:** Commit each completed, verified package unit promptly, including homed reports, under complete-file ownership and one serialised Git write window. Reconcile before editing when authorised; never mandate rebase of a shared dirty checkout or rewriting other writers' commits. This recommendation addresses the question named by the brief without reading the separate cadence review or decision material.

**Confidence:** high - the design commit rule and shared-tree Git rules support this boundary directly.

## Pilot and rollout

Rollout step 1 follows the [design stage contract][design-stages]: retain independent reviews, settle differences against evidence, then obtain Kris's decisions. This review does not substitute for the second review or merged report.

Step 2 has the right repository ownership, but the harness scope must also include `ki-delegation`, its run-packet/report-home contract and the Git/publication cross-references. The receiving harness owns capture and execution; this design does not create records in its roadmap. Step 3's message to `ki.tools-burndown` should name schema readers, run/package identity, report homing, Observatory consumers and ordering prerequisites. The pilot must wait for required readers and writers to accept the same schema; do not use new fields while existing consumers reject them.

For step 4, retain one named Valle Armonia Project and one wave. The reported current practice is a candidate setting, not verified pilot evidence. Agree observable exit conditions: a record remains in its owning repository; its brief, report, query and answer reach its Project package; two packages may hold the same query tag without ambiguity; a dedicated-steward handover stops the old writer; a Project hold survives thread closure; a host requirement can be coordinated elsewhere; and overlapping message consumption and addition preserve disposition and order. Verify a fresh permitted checkout can resume from committed work without a transcript. Exercise publication only under its explicit grant.

Keep the first pilot focused on stewardship and reporting. Test cross-host writing and publication as a separate controlled part once safe writer handover is demonstrated. Existing packages and states provide a rollback: reassign the pilot package explicitly to dedicated coordination and retain its normal files and history. Write the observed lessons into later wave briefs before any parallel rollout, as the design standard requires.

[brief]: <model-shape.md>
[process]: <../../../../Pillars/Philosophy/Model/Processes/Work Process/Work Process.md>
[glossary]: <../../../../../ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md#glossary>
[entries]: <../../../../../ki-agentic-harness/skills/governance/ki-work-package/references/standards-work-package.md#entry-points>
[tidy]: <../../../../../ki-agentic-harness/skills/governance/ki-work-package/references/standards-work-package.md#tidying-the-work-folder>
[sessions]: <../../../../../ki-agentic-harness/skills/governance/ki-work-package/references/standards-work-package.md#work-identity-and-native-sessions>
[state]: <../../../../../ki-agentic-harness/skills/governance/ki-work-package/references/standards-work-package.md#state-file>
[definition]: <../../../../../ki-agentic-harness/skills/governance/ki-work-package/references/standards-work-package.md#work-file>
[prohibited]: <../../../../../ki-agentic-harness/skills/governance/ki-work-package/references/standards-work-package.md#prohibited-payloads-and-claims>
[classification]: <../../../../../ki-agentic-harness/skills/change-management/ki-work-roadmap/references/standards-work-item-format.md#classification>
[updates]: <../../../../../ki-agentic-harness/skills/governance/ki-work-package/references/standards-work-package.md#update-lifecycle>
[committing]: <../../../../../ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md#committing-the-work-folder>
[runs]: <../../../../../ki-agentic-harness/skills/governance/ki-delegation/references/standards-background-runs.md#coordination>
[git-safe]: <../../../../../ki-agentic-harness/skills/governance/ki-git/references/standards-git.md#safe-git-hygiene>
[pushing]: <../../../../../ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md#pushing-beneath-other-sessions>
[design-home]: <../../../../../ki-agentic-harness/skills/change-management/ki-work-design/references/standards-work-design.md#artefact-home>
[territory]: <../../../../../ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md#territory-work>
[packet]: <../../../../../ki-agentic-harness/skills/governance/ki-delegation/references/standards-background-runs.md#run-packet>
[messages]: <../../../../../ki-agentic-harness/skills/governance/ki-work-package/references/standards-work-package.md#messages-lines>
[pickup]: <../../../../../ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md#picking-work-up>
[reports]: <../../../../../ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md#owner-report>
[design-stages]: <../../../../../ki-agentic-harness/skills/change-management/ki-work-design/references/standards-work-design.md#stage-contracts>
