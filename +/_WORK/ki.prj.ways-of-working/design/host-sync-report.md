# Host synchronisation: merged preparation report

**Brief:** [Saved task](<../briefs/wow-host-sync-design.md>) and [received design input](<host-sync-and-reply-trades.md>) · **Reviews:** [Observatory merge](<../../ki.prj.observatory/design/observatory-sync-report.md>) and its underlying reviews · **Date:** 2026-10-29

**Owning work:** [Ways of working](<../work.md>) · **Stage:** source-grounded preparation; HOST-SYNC brief and two-review gate incomplete · **Prepared on:** Sol, run `ways-sol-resume-20261029/sol-host-sync-design`, model `gpt-6.1-sol`.

## Summary

Keep equivalent Rig work on Terra and Sol independently responsible for its own approved repository set. Each publishes eligible primary work before consuming the other host's primary updates. Offsets reduce collisions; they confer no lease, exclusion or automatic takeover. Primary read-back and publication of secondary-origin changes need separate choices. A host being absent leaves its work outstanding; the other host retains only its own authority.

This report merges the available source evidence and adjacent reviewed findings, using the design-loop report template. It is not a completed two-review HOST-SYNC merge. No HOST-SYNC design brief with numbered reflection points, or two independent reviews of that brief, was found in the owning design folder or its path history. The saved task is an execution brief, and the received note is an unadopted input. Neither satisfies that stage contract. The concrete missing review packet is specified under HOST-REVIEW. No agents were launched.

The owner authorised taking up this design, not any particular timing, mapping, executor or publication grant. The recommendations and two draft queue lines below remain conditional. Nothing has been sent, scheduled, synchronised, moved or adopted.

## Corrections to the brief

- The saved task's claim that the brief and independent reviews exist overstates HOST-SYNC provenance. Observatory has a committed [executor-ownership brief](<../../ki.prj.observatory/design/observatory-sync-brief.md>), [authority review](<../../ki.prj.observatory/design/observatory-sync-review-authority.md>) and [reliability review](<../../ki.prj.observatory/design/observatory-sync-review-reliability.md>). Those reviews establish independent views on that adjacent subject, not two reviews of this report's sequence and read-back proposals.
- Observatory's [blind query review](<../../ki.prj.observatory/away-sync-query-review.report.md>) independently supports per-host responsibility, cadence-only offsets and no automatic takeover. The routed HOST-SYNC-REVIEW line, preserved in local Git at `c66d73e9:+/_WORK/ki.prj.ways-of-working/messages.md`, explicitly selects no option, executor, schedule or rollout. It was subsequently received; its absence from today's queue is not absence of the source.
- The HOST-SYNC-DESIGN and RECOMMENDED-ALL entries in the [owner decisions](<../decisions.md#host-sync-design---2026-10-29>) approve proceeding through design and later replies. The [HOST-SYNC option a](<../queries.md#host-sync---settle-the-two-host-synchronisation-design>) approved discussion and settlement, not this report's new recommendations. FINISH-LINE does not waive review or answer unchosen semantics.
- Apply the saved task on Sol in the current valid run group. Its old Terra coordinator and remote Git instructions are superseded by this run's explicit local-only, one-artefact authority. The saved task remains unchanged.
- [ADR-KI-PRINCIPAL-007](<../../../../Admin/Governance/Decisions/ADR-KI-PRINCIPAL-007-territory-seats-on-hosts.md>) and the selected chezmoi `.chezmoidata/seats.yaml` describe coordination seats: Terra is home, Sol is hub, with active-active territories tipped to the hub. They contain no sync-primary/secondary contract. Coordination fallback is not permission for a Git executor to take over. Neither topology nor those roles is reopened.

## Model

### Source authority and review provenance

The received HOST-SYNC and HOST-SYNC-REPLY lines were compared with local Git at `3b512680dd0f756227ae37b5d8408401b6555841:+/_WORK/ki.prj.ways-of-working/messages.md`. The [received note](<host-sync-and-reply-trades.md#full-received-source>) preserves the full wording. Kris asked for equivalent work on both hosts, an offset, primary publication before secondary consumption, and an inexpensive way for the primary to read secondary updates. His example was publication on the hour and secondary consumption five minutes later. The reported stopped Terra sync is historical sender evidence, not a current service check or restart grant. No HNR source was accessed.

Observatory's brief was committed at `6fd427e4`; its authority review at `9a8fc33f` names Claude Opus 5.5 in Claude Code, and its reliability review at `20c08b7f` names GPT-6 in Codex. Both explicitly say they formed their own view before reading the other review; the reliability review names the original brief revision. Their source/point coverage and distinct model/runtime attribution support independence for Observatory's design. The later blind query review explicitly excluded prior recommendations. This is documentary provenance, not a fresh replay of their tests or a claim that their inspected implementation remains current.

### Units, boundaries and hand-offs

1. **Owner-approved responsibility declaration:** dotfiles are the requested home for host setup. Rig and chezmoi must prepare an explicit per-territory mapping and its repository coverage, independent of seat routing. Record who publishes which repositories, which phases each host may perform, exclusions and revision. No schema or field is selected here, and a territory label grants no repository access or publication authority.
2. **Terra and Sol Rig work:** each independently plans and owns its host's pass. A primary phase inspects and publishes only eligible repositories in that host's approved primary set. A later secondary phase consumes the other host's published primary work under each repository's rules. This report does not choose whether the recurring realisation is a fresh thread pass or a direct scheduled resource. Observatory's E-versus-A comparison remains a separate proposal.
3. **Git recipe:** its product owner must supply a bounded, reviewed operation with dirty/live-work refusal, authorised fetch and fast-forward, non-force publication, full unpublished-ancestor inspection and outcome evidence. No discretionary merge, stash, reset, acceptance or package tidy is included. A secondary's ability to pull does not grant it authority to publish. Rejected publication is contention requiring reobservation, not permission to overwrite.
4. **Read-back:** the primary can consume secondary-origin work only once that work has been published through a separately authorised path. A read-only pull phase cannot expose an unpublished secondary commit to the primary. HOST-SECONDARY-PUBLISH decides that publication boundary; HOST-READBACK decides when the primary checks again. Neither implies the other.
5. **Observation:** Observatory owns its separate HOST-RESPONSIBILITY route and observation design. Expected host/repository/phase membership must be distinguishable from attempted, skipped, failed and unknown effects. Its report identifies historical coverage and hourly-overdue defects; current readiness is unverified. A green parent result cannot substitute for coverage or authority evidence.
6. **Replies:** after owner decisions and review completion, one line goes to each actual receiving queue, `personal.reg.rig-terra/messages.md` and `personal.reg.rig-sol/messages.md`. Rig owns receiving priority and host work; chezmoi owns source changes. Cross-repository needs are messages, never records created by this report in another owner's queue. The two lines below are drafts only.

### Sequence and absence

For discussion, HOST-CADENCE proposes an hourly sequence in GMT/UTC: Terra primary at `:00`, Sol primary at `:02`, Terra secondary consumption at `:05`, Sol secondary consumption at `:07`. These are offsets only. Each phase must recheck eligibility and applicable local exclusion; a slow, sleeping or partitioned host invalidates any assumption that the preceding phase completed. A consumer may see the preceding published revision and must report that limitation. It must not wait indefinitely or infer a successful phase from elapsed time.

No host adopts the absent host's responsibilities. A returning host needs fresh authority and source checks before doing its own work; this report chooses no catch-up, retry, missed-occurrence or failure-replay policy. Interrupted or uncertain publication must be reconciled before replay. If exclusive failover is ever wanted, fencing and executor retirement require separate owner design; they are outside this recommendation.

### Agreed state-machine context

The [current diagram source](<work-state-machine.mmd>) and later [owner words](<../decisions.md#roles-orchestrator---2026-10-29>) provide context: Kris is the supervisor, a background subagent is the worker, and the thread agent orchestrates the package state machine. Working contains With worker, Handoff to supervisor, With supervisor and Handoff to worker. Bootstrap enters Working; Working concludes through End (work) before stop reaches At rest, whose reasons include holding, waiting and moving. Resume returns through Bootstrap; finish leaves At rest for Finished. Drain is work on stop, not a state. Failed postconditions leave the source state blocked.

These are roles, not actor types: the [later clarification](<../decisions.md#roles-either---2026-10-29>) permits an AI or human in any role while retaining that preferred assignment. These are agreed design meanings, not a claim that the deployed encoding or transition checks implement them. Sync does not receive an owner handoff, release a waiting package, prove portability, resume a worker or finish a package. At rest portability must still meet its own checks. Synchronising files alone is insufficient.

### Separate unchosen semantics

PACKAGE-FORWARDING, request/reply trades and read-back timing remain distinct. One authoritative incoming queue and an explicit request for a reply remain the source semantics. This report introduces no forwarding service, second queue, automatic acknowledgement, polling field, delivery-triggered completion or automatic release of a sender's wait. The trade inputs stay preserved in the [received design note](<host-sync-and-reply-trades.md#requestreply-trades>) for their own design and acknowledged stewardship. Their disposition is not silently bundled into a cadence choice.

## Agreement and difference

Here A and R are Observatory's authority and reliability reviews; Q is its later blind query review. They are adjacent evidence, not HOST-SYNC reviewers.

| Point | Available review evidence | Settlement and evidence |
| --- | --- | --- |
| Responsibility | Q agrees; Observatory merge routes it here | Independent per-host responsibility; no takeover. |
| Offsets | A agrees; R adds limits; Q agrees | Cadence only; exclusion and convergence remain separate. |
| Executor placement | A adds E; R qualifies alternatives | No winner adopted; preserve Observatory's E/A preparation. |
| Seats | Q and merge distinguish routing | ADR-007 governs coordination, not Git leases or sync mapping. |
| Publication | A/R agree on authority limits | Each repository and actual effect need their own grant. |
| Read-back | R adds convergence limits; Q leaves timing open | Separate timing from secondary publication authority. |
| Missing host | R adds recovery/fencing concerns | No automatic takeover or replay; unknown stays unknown. |
| HOST-SYNC review gate | No common HOST-SYNC brief/review pair | Missing gate; HOST-REVIEW precedes adoption. |

The evidence resolves the apparent conflict between seat fallback and no sync takeover by their different purposes. It also resolves the suggestion that offsetting alone prevents races: elapsed time is neither exclusion nor acknowledgement. Observatory's executor disagreement cannot be settled by counting votes or treating its recommendation as an owner choice. Its reported implementation defects are prerequisites for later readiness assessment, not changes authorised here.

## Rollout plan

This is a bounded proposal after owner choices, not execution authority or a Ready plan under `ki-plan`.

1. **Complete the missing design gate:** the supervisor commissions a numbered HOST-SYNC brief and two independent, read-only reviews on different models/runtimes. Both review the same source-grounded proposal before reading each other. Merge their point-by-point findings and return only new unresolved choices. Preserve settled roles and topology.
2. **Record owner choices:** obtain explicit answers to the independent questions below; consolidate accepted meanings into their owning policy only through separately authorised work. Record secondary-publication and read-back choices separately. Defer forwarding/trades unchanged.
3. **Send the two approved routes:** only after review and choices, the authorised coordinator sends the conditional draft lines below, updated to quote the actual answers. Each Rig owner acknowledges receipt and identifies the chezmoi and Git-recipe dependencies. No message is sent by this run.
4. **Prepare one pilot:** receiving owners nominate one non-HNR, non-deploying repository with clean, uncontested working copies on both hosts and explicit source/phase authority. First compare expected membership and offset predictions without invoking sync or fetch. No scheduler is needed for this preparation. The actual mapping, operation bound, restore path, expiry and stop conditions must be reviewable before any host operation is approved.
5. **Separately authorise attended effects:** prove one-host fetch/fast-forward before adding the second host; publication is a later explicit opt-in with ancestor/path review. Test dirty/live-work refusal, overlap exceeding offsets, divergence, host absence/return, interrupted phases and uncertain publication. Require independent evidence of exclusions and per-phase results. Stop on unknown effects, contested work or unexpected code/deployment scope.
6. **Qualify later recurrence:** Rig and chezmoi decide readiness under their own authorised records, with observation evidence and a tested restoration path. Pilot lessons precede any broader wave. No current timer is restarted, retired or replaced by this report, and no acceptance, package move or work-record creation is included.

### Conditional draft queue lines

These are exactly two unsent lines, conditional on completion of HOST-REVIEW and explicit approval of the recommended options below. They request planning, not installation or recurring execution.

- 2026-10-29 · HOST-SYNC · KI > Model > Ways of working (ki.prj.ways-of-working): After the HOST-SYNC review gate and Kris's explicit choices, prepare Terra's bounded half of the approved design: independent per-host responsibility, no automatic takeover, proposed hourly UTC primary :00 and secondary consumption :05 as cadence only; prepare the explicit responsibility/repository map with Sol and chezmoi, keep secondary-origin publication under separately granted attended work and primary read-back at its next hourly occurrence, and nominate one non-HNR non-deploying attended pilot with source, exclusion and restore checks. Reply here with receipt and prerequisites; no scheduler, sync execution, seat change or package move is authorised by this line.
- 2026-10-29 · HOST-SYNC · KI > Model > Ways of working (ki.prj.ways-of-working): After the HOST-SYNC review gate and Kris's explicit choices, prepare Sol's bounded half of the approved design: independent per-host responsibility, no automatic takeover, proposed hourly UTC primary :02 and secondary consumption :07 as cadence only; prepare the explicit responsibility/repository map with Terra and chezmoi, keep secondary-origin publication under separately granted attended work and primary read-back at its next hourly occurrence, and nominate the same non-HNR non-deploying attended pilot with source, exclusion and restore checks. Reply here with receipt and prerequisites; no scheduler, sync execution, seat change or package move is authorised by this line.

## Decisions

All options below are proposals. Each can be answered separately. HOST-REVIEW blocks design qualification; the other questions are prepared for the owner and do not waive that gate.

### HOST-REVIEW - Supply the missing common-brief review packet

**Context:** The saved execution task claims an existing brief and independent reviews. The actual pair reviews Observatory executor ownership. The HOST-SYNC received note has no numbered reflection, and neither review assesses this report's complete mapping, sequence, secondary publication and read-back proposal. The design-loop standard requires at least two independent reviews of the brief. This run was explicitly forbidden to start agents.

**Query:** Will the supervising coordinator arrange the missing HOST-SYNC brief and two independent reviews before treating this recommendation as qualified?

**Options:**

a) (recommended, confidence high - satisfies the actual gate while retaining all useful preparation) Have the supervising coordinator commission the common brief and two independent read-only reviews, on different models or runtimes, then reconcile this report before adoption. Ask each to mark Agree, Differ or Add against every numbered claim, verify owner wording and examine sequence, publication, absence and state-machine boundaries.

b) Keep this preparation report parked; do not adopt or roll out HOST-SYNC until that review packet is available.

### HOST-CADENCE - Choose the proposed offsets for later planning

**Context:** The owner requested regular equivalent work with offsets and gave an hour/five-minute example. No actual cadence, host offset or zone is adopted. Independent reviews establish that offsets cannot prevent overlap or certify completion. Rig and chezmoi would own any later realisation.

**Query:** Which cadence should the receiving owners prepare, without activating it?

**Options:**

a) (recommended, confidence medium - follows the hourly/five-minute example and gives the hosts distinct phase offsets) Prepare hourly GMT/UTC phases: Terra primary :00 and secondary consumption :05; Sol primary :02 and secondary consumption :07, subject to explicit exclusion and pilot evidence.

b) Keep cadence unchosen and prepare attended passes only until the pilot establishes phase duration and a suitable interval.

### HOST-COVERAGE - Prepare an explicit responsibility map

**Context:** Seats encode coordination landing and existing active-active roles, not sync-primary ownership. There is no evidenced per-territory sync mapping or per-repository publication eligibility set to adopt. Neither host's physical checkout inventory grants it writes. Rig and chezmoi own preparation of the requested dotfiles declaration.

**Query:** Should the two Rig owners prepare the explicit mapping for a separate bounded review, or will Kris provide its entries directly?

**Options:**

a) (recommended, confidence high - preserves owner control without inventing mappings from seats) Ask Rig and chezmoi to propose the per-territory primary/secondary map, enumerate repository and phase eligibility plus exclusions, and return it for approval before configuration or operations. Start with one jointly nominated non-HNR non-deploying pilot repository.

b) Kris supplies the mapping and pilot repository directly; the receiving owners then verify eligibility and prepare its bounded plan.

### HOST-SECONDARY-PUBLISH - Bound secondary-origin publication

**Context:** The source wants the primary to read secondary updates but does not choose how those updates reach Git. Pulling primary work on a secondary cannot publish secondary-origin commits. Scheduling read-back alone therefore cannot fulfil that requirement. Existing per-repository grants still apply.

**Query:** Should secondary-origin changes continue to be published only through separately authorised attended work, or should Rig prepare a recurring secondary-publication phase for later review?

**Options:**

a) (recommended, confidence medium - supplies a valid return path without adding unattended publication authority) Keep secondary consumption pull-only in the recurring proposal; secondary-origin changes reach Git through separately authorised attended work. Read-back consumes only what is actually published and reports outstanding unpublished work as outside its coverage.

b) Ask Rig and the Git-tool owner to prepare a distinct opt-in secondary-publication phase with repository eligibility and authority-at-effect checks; do not activate it or assume a grant from HOST-SYNC.

### HOST-READBACK - Choose when primaries check published return work

**Context:** Kris explicitly left primary read-back to be decided and suggested a resync in short order. This is independent of secondary publication, message forwarding and request/reply trades. No timing guarantee can cover unpublished work or an absent host.

**Query:** Should primary read-back wait for its next hourly occurrence, or should the receiving owners prepare an additional short-delay phase?

**Options:**

a) (recommended, confidence medium - simplest bounded start while coverage and duration are unproven) Read published secondary-origin updates at the start of the primary's next authorised hourly occurrence, before evaluating eligible primary publication. State the resulting delay explicitly; make no immediate-convergence promise.

b) Prepare an extra pull-only read-back at Terra :10 and Sol :12, separately bounded and guarded; retain next-occurrence recovery if a prior phase is late or absent. This adds promptness, not publication authority or an acknowledgement guarantee.

## Changes after review

- No HOST-SYNC review completion is claimed. The report exposes the missing common brief and independent pair rather than relabelling adjacent reviews.
- Observatory's authority/reliability merge and later blind query review support cadence-only offsets, independent responsibility and the publication/exclusion boundaries. Their executor alternatives remain proposals.
- Current owner diagram and role agreements are integrated as context; older held/handoff vocabulary is not used to infer implementation or a new host move.
- New owner choices are split into cadence, coverage preparation, secondary publication and read-back. Forwarding/trades and execution placement remain separately unchosen. Two conditional Rig lines are drafted after those choices; none is sent.
