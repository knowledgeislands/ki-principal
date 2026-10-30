# Host synchronisation: review by Claude Opus 5.5

**Reviewer:** Default Claude runtime, Claude Opus 5.5. **Date:** 2026-10-30. **Read-only:** yes, apart from this file.

**Provenance:** Detached run `ki-prj-ways-of-working/host-sync-review-claude` on Sol, against Principal `e36fef0e` and chezmoi `38be5a1`. Read: the [brief](brief.md), the [received design input](<../host-sync-and-reply-trades.md>), the [decisions log](<../../decisions.md>) entries the brief quotes, [ADR-KI-PRINCIPAL-007](<../../../../../Admin/Governance/Decisions/ADR-KI-PRINCIPAL-007-territory-seats-on-hosts.md>), chezmoi `.chezmoidata/seats.yaml` at `38be5a1`, the [work state machine source](<../work-state-machine.mmd>), the [Observatory merged sync report](<../../../ki.prj.observatory/design/observatory-sync-report.md>), the two Rig host packages in personal-principal and the `tools-mgit` README. Not read: `queries.md`, the preparation report `host-sync-report.md`, any run report or the other reviewer's file. No HNR repository, scheduler, provider or host service was read or changed; the Rig host packages were read only where they record the owner's sync instructions.

## Own view

The proposal is careful and almost every safeguard in it is sound, but it answers a harder problem than the one Kris set, and in two places it contradicts what Kris said and has already had run.

1. **Kris's model has the secondary publish.** The words are "on the hour, it should resync and publish ... the ones which it has primary responsibility for. And then five minutes later ... the secondary ones", and then "the primary then needs to be able to read the secondary updates". There is nothing for the primary to read unless the secondary has published. Claims 5 and 12 make the secondary pull-only, which removes the one property Kris asked for: commits made on either host reach GitHub.
2. **The recipe already exists and both hosts have run it on Kris's instruction.** `mgit sync` fetches, fast-forwards branches that are only behind, pushes branches that are only ahead and leaves diverged, dirty, detached and untracked branches untouched, with a tally ([tools-mgit README](</Users/krisbrown/workspaces/knowledge-islands/tools-mgit/README.md>), "mgit sync" paragraph). Kris asked Terra at 17:40 GMT on 28 October for a 15-minute pass that makes "sure that everything is pushed" ([Terra sync brief](</Users/krisbrown/workspaces/personal/personal-principal/+/_WORK/personal.reg.rig-terra/briefs/sync.md>)), and asked Sol at 20:58 GMT the same day for "a regular 15 minute git sync" that ran at `:07`, `:22`, `:37` and `:52` until 16:20 GMT on 29 October ([Sol decisions](</Users/krisbrown/workspaces/personal/personal-principal/+/_WORK/personal.reg.rig-sol/decisions.md>), [Sol state](</Users/krisbrown/workspaces/personal/personal-principal/+/_WORK/personal.reg.rig-sol/state.md>)). The design treats unattended publication as new authority; the owner has already granted and exercised it, attended by a thread.
3. **With fast-forward-only, no-force publication on both hosts, the race Kris feared is harmless.** Two hosts pushing the same branch at once cost one rejected push that the next pass retries. The real failure is divergence from concurrent sessions: Sol's last tick left `hnr-principal` unsynced because another session had committed two minutes earlier. Offsets cannot fix divergence; only a named resolver can. The proposal names who refuses on divergence but not who resolves it.
4. **The per-territory pairing Kris half-remembers is the seat and standby.** [ADR-KI-PRINCIPAL-007](<../../../../../Admin/Governance/Decisions/ADR-KI-PRINCIPAL-007-territory-seats-on-hosts.md>) says "Each territory has one seat and one standby", and the sender's line itself names `seats.yaml` as the nearest entry. Keeping the semantics separate is right; refusing to use the seats even as the default proposal for Kris to confirm is not.
5. **Weight.** Kris called it urgent and wanted it "soon"; the route here runs review, owner choices, two rollout lines, a Rig-prepared map per repository and revision, Kris's approval, then a staged pilot with publication added "later". Meanwhile both hosts' syncs are stopped, so there is no sync at all. A lighter design keeps every guard that matters: one deterministic recipe, ff-only, no force, explicit exclusions, a stop word and a named resolver for divergence.

## 1. Fact check

| Item | Verdict | Evidence and correction |
| --- | --- | --- |
| Terra's half-hourly HNR `mgit sync` stopped on 28 October | Confirmed, incomplete | The sender's line says "stopped at 13:52 GMT until this lands" ([design input](<../host-sync-and-reply-trades.md#full-received-source>)). Omitted: Terra ran a 15-minute all-territory pass from 17:40 GMT on 28 October (SYNC-EVENING), Sol ran a 15-minute Git and dotfile sync from 20:58 GMT on 28 October to 16:20 GMT on 29 October (SOL-SYNC), and Kris asked on 29 October at 16:40 GMT to "`mgit sync` everything under `~/workspaces`" on both hosts (SYNC-NOW, [Terra decisions](</Users/krisbrown/workspaces/personal/personal-principal/+/_WORK/personal.reg.rig-terra/decisions.md>)). Sol's script is kept at `~/.local/state/ki/agents/chezmoi/git-sync/`, and [Sol's queries](</Users/krisbrown/workspaces/personal/personal-principal/+/_WORK/personal.reg.rig-sol/queries.md>) hold an open HOST-SYNC query recommending a restart until this rollout lands. |
| Kris's HOST-SYNC words (13:50 GMT) and the three-part shape | Confirmed | Verbatim against the full received source. Note that "soon" and "urgent" are the sender's summary, not Kris's quoted words; claim 23 presents "soon" as Kris's. |
| HOST-SYNC-REPLY and `personal.regular.rig-sol` | Confirmed | Verbatim; the older spelling is as stated. |
| HOST-SYNC-DESIGN, RECOMMENDED-ALL, HOST-REVIEW, REVIEW-INDEPENDENCE quotations | Confirmed | Each matches [the decisions log](<../../decisions.md>) verbatim. LANDSCAPE is correctly flagged as a summary. |
| Seats bind Terra home and Sol hub, active-active tipped to hub, no primary or secondary field | Confirmed | `seats.yaml` at chezmoi `38be5a1` matches, quotation included. Add: the ADR itself defines "one seat and one standby" per territory, which is a per-territory pairing. |
| Queues `personal.reg.rig-terra` and `personal.reg.rig-sol` exist | Confirmed | Both are in personal-principal `+/_WORK/`. A third, `personal.reg.rig`, is the public catalogue and not a receiver. The two host packages name the chezmoi-approach owner differently: Sol says `ki.prj.chezmoi`, Terra says `ki.chezmoi`. |
| Observatory "compares realising the pass as a fresh thread pass (E) or a direct scheduled resource (A)" | **Corrected** | The [merged report](<../../../ki.prj.observatory/design/observatory-sync-report.md>) has it the other way: "Compare E, a direct per-host Rig resource, against A, attended passes under fresh grants". It leans to E ("moderate in E's relative simplicity") without selecting it. It also records that "the current local `mgit sync` can push ahead-only branches by default despite the adopted no-push-default request", which bears directly on claims 6, 7 and 12. |
| State machine and roles | Confirmed | Matches the diagram source and the ROLES-ORCHESTRATOR and ROLES-EITHER entries. |
| Request/reply trades out of scope | Confirmed | As held in the design input. |

## 2. Per-claim verdicts

| # | Verdict | Reason |
| --- | --- | --- |
| 1 | Add | Agree on a chezmoi-carried declaration. Name the owners exactly: the chezmoi source repository through `personal.reg.rig-terra` and `personal.reg.rig-sol`, with whichever of `ki.prj.chezmoi` or `ki.chezmoi` is current for method; "Rig and chezmoi" is ambiguous today. |
| 2 | Agree | Seat fallback is coordination routing, not a Git lease. Colocate the sync field with the seats in the same data file so the two are reviewed together, without coupling their meaning. |
| 3 | Differ | Kris asked for a per-territory entry, and `mgit --territory HANDLE sync` already selects at that grain. Replace per-host repository enumeration with a revision with: territory-level primary and secondary, plus an explicit exclusion list (for example the `apps-io.5g-emerge*` repositories Terra's brief never fetches) and the chezmoi source as a named extra member. |
| 4 | Differ | Replace "not inferred from seats" with: Rig proposes the seat host as primary and the standby as secondary, active-active territories primary on the hub per `tippedTo`, and Kris confirms or amends in one answer. A single non-HNR pilot repository is reasonable for the first attended run, but HNR was the stopped sync that prompted this, so the plan should say when HNR joins rather than leave it open. |
| 5 | Differ | Both phases run the same recipe on different sets: each host at its primary slot syncs its primary territories, then at its secondary slot fast-forwards and publishes ahead-only work in the other territories. That is Kris's "publish ... then five minutes later ... the secondary ones" and the sender's "adjusts". |
| 6 | Add | Agree with the safeguards. The recipe exists: `mgit sync` (product owner `tools-mgit`) already refuses dirty, diverged and detached branches and never merges, rebases or forces. Its gaps are live-work refusal (the Terra brief's tests: a held `ki agent` write lock, or another session's unpushed commits under 60 minutes old), durable outcome evidence, and the no-push-default question below. Replace "inspect every unpublished ancestor", which an unattended pass cannot do meaningfully, with those objective tests. |
| 7 | Differ | Agree that pulling grants nothing. "Each actual effect needs its own grant" makes any recurrence impossible. Replace it with: Kris's approval of the map, naming which territories each host publishes, is the standing publication grant for ff-only, no-force pushes of committed work in those territories, revocable by a stop word. This matches PACKAGE-PUSH, which already authorises pushing everything stacked fast-forward only, and the SYNC-EVENING and SOL-SYNC grants. |
| 8 | Differ | Kris said "the sync process should always be run from this equivalent thread". Record that as the ownership: the host's Rig thread owns the pass, reads its tally and resolves what it leaves. Execution can still be a deterministic scheduled recipe (Observatory's E), which survives session limits that thread-launched passes do not. Also correct the E and A labels as above. |
| 9 | Agree | Offsets are cadence only; each phase rechecks and never infers success from elapsed time. |
| 10 | Add | Hourly is Kris's own cadence. Because each territory has exactly one primary, the two hosts' primary sets are disjoint and need no stagger between hosts: Kris's `:00` primary and `:05` secondary on both hosts suffices. The extra two minutes are harmless but buy nothing. |
| 11 | Agree | Correct as logic; it is the argument for publishing in the secondary phase, not against it. |
| 12 | Differ | Contradicts Kris's words and both precedents, and leaves every Sol commit in a Terra-primary territory unpublished until someone attends. Replace with: the secondary phase publishes ahead-only work under the same recipe; diverged repositories are left and reported to the host thread, which resolves them attended. |
| 13 | Agree | The three are separable choices. |
| 14 | Differ | Kris also said "we probably want to do a resync as well in short order after it". With claim 12 replaced, a pull-only resync on the primary shortly after the secondary phase is cheap and is what Kris described; waiting up to 55 minutes is the weaker reading. Sessions also fetch before working, so neither choice is critical. |
| 15 | Agree | Add: with every host publishing only its own fast-forwards, nothing is exclusive, so an absent host blocks nothing and there is nothing to take over. |
| 16 | Differ | The fencing and replay concerns follow from treating publication as exclusive. The recipe is idempotent, so the next occurrence is the catch-up; a returning host needs only to run it, refusing on dirty or live work as always. Replace with: no catch-up beyond the next occurrence; interrupted publication is a rejected or partial push that the next pass sees as ahead or diverged. |
| 17 | Agree | Add: the observation design should not gate rollout. A tally written where the host thread reads it is sufficient to start; Observatory improves coverage evidence later. |
| 18 | Agree | Sync moves commits; it changes no work state. |
| 19 | Agree | No forwarding, acknowledgement or wait release. |
| 20 | Differ | Agree that HOST-SYNC itself is not scheduler authority. Leaving both stopped syncs "neither restarted, retired nor replaced" leaves no sync at all while Sol's open HOST-SYNC query recommends a restart. Replace with: the rollout line states that the designed pass supersedes Terra's HNR sync, SYNC-EVENING and SOL-SYNC, closes Sol's HOST-SYNC query, and retires the kept script once the replacement runs. |
| 21 | Agree | One line per Rig host queue, requesting the plan. Add that each line names the confirmed map and the stop word. |
| 22 | Differ | Over-staged for a recipe both hosts have already run for most of a day on Kris's instruction. Replace with: one attended run per host of the exact scheduled command over the confirmed map, checked against its tally; then activation with a stop word, the restore path being to unload the job, and the exclusion list. Overlap, divergence, absence and return are observed in operation, not staged first. This is not a connection-critical change. |
| 23 | Differ | It is heavier than the requirement warrants and does not meet it, because a pull-only secondary never levels commits made on the secondary. "Soon" is the sender's word, not Kris's quoted one. |

## 3. Missing claims

24. **Divergence resolver.** The design names who refuses on divergence, not who resolves. The host's Rig thread receives each diverged repository from the tally and resolves it attended through a bounded resolve run, under the existing standard, escalating to Kris only when still diverged after two hours with no new local commits (the threshold Terra's brief already uses).
25. **Interim.** Until the rollout runs, an attended `mgit sync` on request (SYNC-NOW) stays available, so "soon" does not wait for the pilot.
26. **Laptop sleep is routine absence.** Terra sleeps; a calendar job missed during sleep fires once on wake or not at all, depending on the scheduler. The design states that a missed or late occurrence is simply skipped, and the next one runs.
27. **Branch scope.** `mgit sync` acts on every tracking branch. Say whether the pass is limited to the default branch.
28. **The no-push-default conflict.** Observatory records an adopted request that `mgit sync` stop pushing by default. The pass must call an explicit publish mode, and `tools-mgit` should know that this design depends on it.
29. **The chezmoi source and dotfile drift.** Sol's sync also handled dotfile drift at Kris's request, and Terra's brief syncs the chezmoi source. State whether the chezmoi source repository is in the map, and keep `chezmoi apply` out of the unattended pass.
30. **Work-package tidy stays out.** Terra's evening pass also tidied idle work packages. Keep tidy out of the recurring pass; the claims imply this only through claim 6's exclusion list.

## 4. Recommendations

### HOST-CADENCE

**a)**, simplified to Kris's own `:00` primary and `:05` secondary on both hosts, since the primary sets are disjoint. Confidence **medium**: Kris set hourly with a five-minute offset; the only reason to wait is phase duration, which the attended run measures before activation.

### HOST-COVERAGE

**A better option c):** Rig proposes the default map from the seats (seat host primary, standby secondary, active-active territories primary on the hub), with territory-level exclusions, and Kris confirms or amends it in one answer before configuration. Confidence **medium**: the ADR already pairs seat and standby per territory and the sender points there, but Kris may want a different split for the active-active territories.

### HOST-SECONDARY-PUBLISH

**A better option c):** the secondary phase runs the same recipe as the primary phase and publishes ahead-only work fast-forward, without force, leaving diverged and dirty repositories to the host thread; Kris's map approval is its grant. Option b's separately prepared opt-in phase is the fallback if Kris wants publication delayed. Confidence **medium**: Kris's words and both owner-run precedents support it, but unattended publication should be Kris's explicit choice, and the no-push-default request has to be reconciled.

### HOST-READBACK

**b)**, as one pull-only resync on each primary at `:10`, with next-occurrence recovery. Confidence **medium**: it is what Kris described as a resync "in short order", costs one fetch, and grants nothing; next-hour read-back is acceptable because sessions fetch before working.
