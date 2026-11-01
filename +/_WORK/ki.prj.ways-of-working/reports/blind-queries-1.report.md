# [Model](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › blind-queries-1

**🤖 → 👤 Handoff to supervisor · Run report at 01:27 GMT · last mark 01:10 GMT**

---

## Done

- Independently reviewed all 12 requested queries, using their Context, Query and option courses without using their recommendation annotations or blind-review paragraphs.
- Checked current standards, selected design notes, local implementation, local Git objects and declaration inventory; no repository changes or commits were made.
- Verified that the proposed historical roadmap-sweep link resolves to an object in local Git; no network verification was attempted.
- Verified both Z files exist and are untracked without reading their contents; preserved them unchanged.
- Used no remote calls, background agents, credentials, environment changes or repository writes; the required report and status are the only surviving run outputs.

## In Progress

Nothing is running.

Outstanding - no action requested now: the coordinator owns the disposition of these findings. This review neither settles owner queries nor authorises implementation, cancellation or deletion. Cross-host cleanliness, actual running sync loops and complete delivery of accepted contracts were not verified. Where the permitted evidence establishes only a partial settlement, the finding says so; the excluded decisions log and run reports were not used to infer more.

## Findings

### LAYOUT-SHAPE - Use a flat folder per matter for the pilot

**Goal:** Independently choose the package layout for the pilot, as requested in blind-queries-1 on 1 November 2026.

**Scope:** The three supplied choices, the permitted layout design, current package standard, actual ignore rules and launcher implementation; no prior run reports.

**As of:** 1 November 2026, 01:27 GMT.

**Pick:** a), C: one folder per matter with briefs and reports side by side.

**Confidence:** medium - it gives a matter one readable home without another directory layer, but its routing and reader behaviour remain unpiloted.

**Verified:** The standard already requires reports in `reports/` as an interim arrangement and explicitly leaves LAYOUT-SHAPE open. The blanket claim that reports folders are invisible is stale: package-level exceptions now exist. An exact local ignore check nevertheless confirms that a report beneath `<group>/reports/` is still ignored, while `<group>/<run>.report.md` is not. The current launcher still derives a top-level report path, so changing the standard has not established implementation support. See the [package standard](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/skills/governance/ki-work-package/references/standards-work-package.md:84), [ignore rules](/Users/krisbrown/kis/knowledge-islands/ki-principal/.gitignore:6) and [launcher path](/Users/krisbrown/kis/knowledge-islands/tools-ki/src/core/agent/thread.ts:91).

**Missed risk:** A manual move can hide evidence from consumers even when the folder passes its audit. Re-inventory each reader and the launcher at pilot time; ensure temporary report homes are handled explicitly, and preserve incoming links. Folder grouping is useful independently of whether whole-folder deletion is approved.

**Still live or settled:** Live. The interim report-folder location is settled; the final grouping shape is not.

### LAYOUT-GROUP-TIDY - Allow a named closed group only after checking its contents

**Goal:** Independently assess whether a closed group may be deleted as one unit.

**Scope:** The proposed closure conditions and current package and design-note deletion rules.

**As of:** 1 November 2026, 01:27 GMT.

**Pick:** a), conditional on an explicit, freshly checked list of the group's contents and the existing evidence and link guards.

**Confidence:** medium - one named group can be a bounded unit, but grouping does not prove every file is disposable.

**Verified:** The current rule expressly requires named-file deletion and forbids folder-wide deletion. The separate design-note guard requires every outcome, owner wording and grant to be homed and every incoming link rewritten first. See [tidying](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/skills/governance/ki-work-package/references/standards-work-package.md:136) and [design-note guards](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md:1120).

**Missed risk:** A running launcher or another session can add a report after the steward judges the group closed. Untracked or ignored files have no Git recovery merely because their neighbours do. Verify no producer remains active, check tracked and untracked contents immediately before deletion, and retain single-file tidy for mixed groups. This amendment must not become permission to prune work records or delete other work's folders.

**Still live or settled:** Live and dependent on the selected group layout. Current authority remains file by file until the owner changes it.

### HOOK-PATCH - Protect leftover patches explicitly

**Goal:** Independently assess the proposed protection for lint-staged recovery patches.

**Scope:** The installed dependency's implementation, the repository hook and the standards' current wording; no reproduction of the reported kill experiment.

**As of:** 1 November 2026, 01:27 GMT.

**Pick:** a), add the protection and regenerate the coordinator style from its source standard.

**Confidence:** high - the hook uses the relevant mode and the dependency source directly confirms a patch can be created independently of the backup stash.

**Verified:** The hook runs lint-staged with `--no-stash`. Its source builds a per-run hidden directory and writes `unstaged.patch` before the conditional stash creation. The delegation and coordination standards mention leftover backup stashes but contain no equivalent patch protection. See the [hook](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/.githooks/pre-commit:18), [patch creation](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/node_modules/lint-staged/lib/gitWorkflow.js:229), [delegation rule](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/skills/governance/ki-delegation/references/standards-background-runs.md:246) and [coordination rule](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md:822). The claimed exact restoration experiment was not independently reproduced.

**Missed risk:** The directory may belong to an active hook, and worktrees need the actual Git metadata location rather than an assumed `.git` directory. Report the location without printing patch contents. Do not edit only the generated style or apply a patch merely because it looks abandoned.

**Still live or settled:** Live; the protection is absent from the checked standards.

### SWEEP-GATE - Require fresh evidence for each repository

**Goal:** Independently choose the safety gate for the rename sweep.

**Scope:** The two supplied gates, current host-thread state and the recorded repository move; no remote or second-host inspection.

**As of:** 1 November 2026, 01:27 GMT.

**Pick:** a), a fresh per-repository check and an agreed handover between writers.

**Confidence:** medium - this checks the actual collision condition; an operating schedule alone cannot prove both checkouts are level.

**Verified:** Both host threads now record the move into `~/kis` as complete; terra records its recurring loop and sol records the loop running on the new paths. Older paragraphs in sol's same state still say it is stopped or waiting, so these files cannot prove present process health. The `~/world` move premise is stale. See [sol move completion](/Users/krisbrown/kis/personal/personal-principal/+/_WORK/personal.reg.rig-sol/state.md:28) and [terra current state](/Users/krisbrown/kis/personal/personal-principal/+/_WORK/personal.reg.rig-terra/state.md:15).

**Missed risk:** Clean and level is a momentary observation. Name the branch and commit on both machines, stop competing package writes during the bounded rename, and verify the receiving Mac has pulled the result before it resumes. A scheduled loop is not a lock; its seven-minute offset does not prevent overlapping long passes. No sweep should start from this review's historical state-file evidence.

**Still live or settled:** The move prerequisite is recorded as satisfied; the fresh per-repository execution gate remains live. Neither option requires waiting for a move to a path no longer being used.

### HOST-SYNC-CLOSE - Separate settled design from evidence deletion

**Goal:** Independently assess whether the parked HOST-SYNC question is superseded and its six notes may leave.

**Scope:** The permitted host-reconcile design and current host-thread states; no contents of the six proposed deletion targets or Observatory run report.

**As of:** 1 November 2026, 01:27 GMT.

**Pick:** a), close the obsolete primary/secondary and offset choice; delete notes only after the normal outcome and incoming-link checks.

**Confidence:** medium - the replacement design and receiving host's state explicitly establish supersession, but the six-file deletion is not independently proven safe.

**Verified:** The host-reconcile plan specifies quarter-hour sol passes and terra seven minutes later, and describes primary and secondary responsibilities. Sol's state explicitly calls HOST-SYNC superseded. See [host-reconcile plan](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/host-reconcile/plan.md:17) and [sol's receipt in state](/Users/krisbrown/kis/personal/personal-principal/+/_WORK/personal.reg.rig-sol/state.md:17).

**Missed risk:** One note can contain unresolved material beyond the superseded scheduling question. Supersession of a query does not demonstrate graduation of every note. Also, the receiving host already records the host-reconcile plan, so retaining it solely until receipt should use an acknowledgement predicate rather than waiting for a particular message to remain in a queue. The Observatory report's claimed incoming link was not inspected under this review's exclusions.

**Still live or settled:** Substantive supersession is already established by permitted evidence. Recording the query's disposition and proving each note eligible for removal remain live housekeeping.

### CITED-NOTES - Repair live links, but prove graduation separately

**Goal:** Independently assess deletion of the five cited design notes.

**Scope:** Current harness source lists, permitted package references and the design-note guard; no claim that all five notes have been fully delivered.

**As of:** 1 November 2026, 01:27 GMT.

**Pick:** a), conditional on actual graduation and completed incoming-link repairs; omit repairs that are already done.

**Confidence:** medium - historical links can preserve provenance, but a rewritten link does not establish that a live design has finished its job.

**Verified:** The three harness source lists already cite the method-feedback and coordination-lessons proposals through pinned historical GitHub links. The query's assertion that these are still local-path repairs is stale. A live baseline-rollout message still links to the current work-id-shape plan. The source lists also explicitly retain deferred material, so their existence does not prove wholesale graduation. See [coordination sources](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/sources.md:34), [delegation sources](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/skills/governance/ki-delegation/references/sources.md:24), [package sources](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/skills/governance/ki-work-package/references/sources.md:19) and [baseline handoff](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.baseline-rollout/messages.md:13).

**Missed risk:** Merely sending a replacement link does not repair the receiver's reference. Wait for the actual repair or verified disposition, distinguish historical provenance from a current operative plan, and preserve any unhomed grant or deferred clause. The [existing guard](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md:1120) already requires this before deletion.

**Still live or settled:** The three source-list repairs are already settled. Remaining incoming references and graduation checks are live; retaining every note until Project close is unnecessarily broad.

### OLD-PROPOSALS - Do not demote an accepted contract to an idea

**Goal:** Independently choose the treatment of the five purportedly undecided proposals.

**Scope:** The accepted agent-control contract, current CLI control implementation and the proposed interim ideas destination; not a full delivery audit of all five notes.

**As of:** 1 November 2026, 01:27 GMT.

**Pick:** b), retain the notes for now; separate their dispositions rather than approve option a) as one batch.

**Confidence:** medium - direct evidence contradicts the shared premise, and the proposed destination is a snapshot rather than an established durable home.

**Verified:** The agent-control note identifies itself as accepted on 21 October and specifies staged delivery, wake and model-evidence gates. Tools-ki now contains stop, dequeue and recovery commands, but that proves only part of the contract and does not prove all gates or wake delivery. The empty-board ideas file expressly calls itself a snapshot that leaves ownership where each idea sits. See the [accepted contract](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/agent-control-contract.md:3), [staged delivery](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/agent-control-contract.md:21), [current commands](/Users/krisbrown/kis/knowledge-islands/tools-ki/src/commands/agent/control.ts:23) and [ideas-list purpose](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/empty-board/ideas.md:11).

**Missed risk:** A one-line idea can erase an accepted obligation, its safety gates or an unresolved grant while appearing to preserve the topic. Conversely, waiting indefinitely for IDEAS-HOME should not block separately proven graduation of a particular note. Reclassify the accepted contract apart from speculative proposals and keep existing receiver-owned ideas at their owners.

**Still live or settled:** The batch-disposal choice remains live. The assertion that all five were never accepted is already disproved. No complete contract-delivery conclusion is justified by this review.

### TOPIC-SET - Prefer topics that can finish independently

**Goal:** Independently choose the topic granularity for the package pilot.

**Scope:** The fine-grained versus eight-folder alternatives as described in the permitted query, and the existing group definition; not the excluded stock-take Findings table.

**As of:** 1 November 2026, 01:27 GMT.

**Pick:** a), the finer-grained pilot, subject to checking and naming its actual 13-topic manifest before moving anything.

**Confidence:** low - independent completion is a sound grouping criterion, but the precise 13-topic inventory is not available in the permitted query text and was not independently verified.

**Verified:** The permitted layout design defines a group by the matter producing the files and keeps it open while any artefact remains live. The eight-folder alternative combines distinct matters such as package layout, package freshness and discussions. See the [group definition and closure proposal](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/package-layout/design.md:100). No current count of 13 has been verified.

**Missed risk:** The comparison frames fewer folders as less searching without measuring retrieval or closure. Broad folders can hold unrelated open work that prevents complete tidy; very narrow folders can fragment one decision. Prefer one decision lifecycle per folder, allow later merging, and verify every retained file has one unambiguous home. This finding supports the pilot principle, not an unseen exact move list.

**Still live or settled:** Live. Neither exact topic set is established by the checked standard. The coordinator must supply the current manifest before implementation.

### Z-FILES - Preserve the untracked originals pending a private disposition

**Goal:** Independently assess whether the two Z retirement files should remain uncommitted.

**Scope:** File existence and tracking metadata only, the current ignore rules and the brief's confidentiality boundary; their contents were not read.

**As of:** 1 November 2026, 01:27 GMT.

**Pick:** a), keep them uncommitted pending the permitted audience and private destination.

**Confidence:** high - withholding publication preserves the owner's choice, and both originals are directly verified as existing and untracked.

**Verified:** Both named files exist and neither is in the Git index. The current report-folder exception means their location no longer guarantees they are hidden from Git. The review cannot establish from metadata whether other private copies exist or whether publication would reveal particular information. See the [report-folder exception](/Users/krisbrown/kis/knowledge-islands/ki-principal/.gitignore:7). The brief expressly forbids confidential publication without Kris's go.

**Missed risk:** Remaining uncommitted is not a preservation plan. An authorised private backup is needed if these are the only copies, and broad staging or a future sweep can accidentally include them now. Do not move, back up or dispose of them without the bounded private-destination instruction; flag their exception to any report-commit sweep without reproducing their contents.

**Still live or settled:** The immediate safe handling is clear; the audience and storage disposition remain unverified and live. Prior approval of an option is not evidence that the missing private destination has been supplied.

### SWEEP-NOTE-LINKS - Notify the owners of the historical reference

**Goal:** Independently assess whether the two owning works should receive the corrected roadmap-sweep link.

**Scope:** The two roadmap records' current link text and the pinned object in local Git; no deleted-note contents or remote calls.

**As of:** 1 November 2026, 01:27 GMT.

**Pick:** a), notify each receiving owner once with the pinned reference and let it repair or otherwise dispose of its own reference.

**Confidence:** high - both broken links and the replacement Git object are directly verified, and the proposed correction is bounded.

**Verified:** The [Observatory record](/Users/krisbrown/kis/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-004-turn-feedback-sending-on.md:89) and [Rig record](/Users/krisbrown/kis/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-070-handler-read-back-after-confirmation.md:90) contain the old checkout and package path. The object exists locally at the [proposed pinned revision](https://github.com/knowledgeislands/ki-principal/blob/f8c70a3000cdd7a531811ffe363884489eda0e50/+/_WORK/ki.prj.ways-of-working/design/roadmap-sweep.md). Its availability on GitHub was not tested.

**Missed risk:** A record may be pruned before the message is processed; the receiver can retain the historical reference with its own disposition rather than recreate the record. Identify the real Rig-owning work before sending. No cross-repository edit or pruning authority follows from this review.

**Still live or settled:** Live: both old links remain in the locally checked records. Their having been broken earlier does not remove the provenance value of a correction.

### ORCA-ADAPTER-WHEN - Write the adapter from the trial evidence

**Goal:** Independently assess when to commission the Orca delegation adapter.

**Scope:** Current evaluation state and canonical harness skill inventory; no remote experiment or prior evaluation report.

**As of:** 1 November 2026, 01:27 GMT.

**Pick:** a), commission the adapter once the relevant shared boundary and attended evaluation evidence are available.

**Confidence:** medium - the evaluation already sequences the launcher proposal after the trial, and an empty skill would add little tested guidance.

**Verified:** No `ki-delegation-orca` skill exists in the inspected canonical harness tree. The evaluation state puts the attended pilot first and the launcher proposal after receipt of unit 1, and separately lists remote-view investigation. It does not establish that a remote execution trial has happened. See [evaluation next steps](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.orca-evaluation/state.md:22).

**Missed risk:** Waiting for the whole portable contract to be perfect can become an indefinite dependency. Define the minimal interface the adapter needs, and commission when that boundary and trial evidence are adequate. Keep unknown remote execution outside the adapter's supported claims; do not confuse remote viewing with launching or recovering a remote worker. Existing `orca-cli` operational guidance can serve during the wait without creating a second portable contract.

**Still live or settled:** Live as an owner choice; the receiving evaluation's recorded sequence already supports evidence before adapter drafting. No skeleton or adapter has been verified as delivered.

### PAPERCLIP-RETIRE - Dormancy needs to cover operative authority too

**Goal:** Independently assess dormancy, removal or continued rollout of the Paperclip skill.

**Scope:** Canonical adapter and alias, alias audit implementation, local repository declarations and the harness's standing local-delivery policy; no Paperclip service or provider inspection.

**As of:** 1 November 2026, 01:27 GMT.

**Pick:** a), retain dormant compatibility, stop the rename rollout and let owners remove unused declarations during ordinary conformance, with a fresh design required before reuse.

**Confidence:** medium - this preserves recoverable knowledge and avoids a broad removal sweep, but a description change alone does not retire the operative policy.

**Verified:** Both the renamed adapter and deprecated alias exist. The alias explicitly warns and directs migration, and its audit implements that warning. A local parse found 54 repositories declaring the old alias and three declaring the renamed skill. The harness's root guidance still grants a named Convenor local integration authority and says the grant remains valid until changed or revoked. See the [adapter](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/skills/agentic-systems/ki-delegation-paperclip/SKILL.md:22), [alias](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/skills/agentic-systems/ki-agent-coordination-paperclip/SKILL.md:19), [warning implementation](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/skills/agentic-systems/ki-agent-coordination-paperclip/scripts/rubric/items/alias.ts:6) and [standing delivery policy](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/AGENTS.md:24).

**Missed risk:** Calling the skill dormant does not suspend standing delivery grants or participating repositories' operative instructions. The owner must explicitly resolve those when adopting dormancy; the three already-renamed declarations also need accounting. Make only the unused alias diagnostic quiet, not real active-use failures. A rollout message can be withdrawn, but any formal work cancellation still needs the exact human-approved resolution. Runtime/service retirement belongs to its separate owner and is not covered by this skill change.

**Still live or settled:** Live. Current sources still describe an available adapter, an active migration warning and operative delivery policy; no dormant implementation was found. The factual count of 54 old declarations is verified locally, without asserting that all 54 actively use Paperclip.

## Queries

No outstanding queries from this review. The coordinator should use the findings to correct premises and retain the genuinely live owner decisions; no query was answered on Kris's behalf.

### 🤖 → 👤 Handoff to supervisor · since 01:27 GMT

🤖 0 running · 👤 1 with you · ⛔ 0 blocked

- [with you] Independent review of 12 owner queries · supervisor · since 01:27 GMT

🧵 ki.prj.ways-of-working
