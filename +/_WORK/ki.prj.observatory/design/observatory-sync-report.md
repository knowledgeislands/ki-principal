# Scheduled cross-machine Git sync ownership: merged report

**Brief:** [Original brief](<observatory-sync-brief.md>) · **Reviews:** [Authority, Claude Opus 5.5](<observatory-sync-review-authority.md>), [reliability, GPT-6/Codex](<observatory-sync-review-reliability.md>) · **Date:** 2026-10-29

**Owning work:** [ki.prj.observatory](<../work.md>) · **Stage:** merged report, awaiting owner decisions · **Authority:** AWAY-2026-10-29 and the bounded merge instruction, preparation only until 09:00 GMT/UTC or explicit return sooner.

## Summary

### SYNC-MERGE - Recommendation and limits

**Goal:** Answer Kris's question, recorded on 28 October: "given the fact that the observatory is running, why doesn't the observatory just do it?"

**Scope:** Merge the independent reviews against local sources and isolated fixtures; compare execution homes without selecting one, granting publication or tidy, or operating any runtime.

**As of:** 29 October 2026, local source verification during this merge; no installed binding, loaded service, remote ref or other-host state was checked.

Recommend a deterministic Git recipe with observation independent of execution. Compare E, a direct per-host Rig resource, against A, attended passes under fresh grants, before adding dispatcher or Bridge machinery. B remains viable if dispatcher enrolment earns its extra scope; D needs an attended request use case; C needs an explicit product-authority review. Confidence is high in the separation and safeguards, moderate in E's relative simplicity, and low in any claim about current deployed coverage. These are recommendations for Kris, not an execution-owner decision.

The current local `mgit sync` can push ahead-only branches by default despite the adopted no-push-default request. Current Jobs cannot prove complete host/occurrence/repository coverage and can keep a stale hourly-calendar result healthy indefinitely. Those defects are independent of the ownership design: neither their repair nor any sync rollout is authorised here.

## Corrections to the brief

Source labels S1-S13 below refer to the [original source inventory](<observatory-sync-brief.md#sources>). All 25 recorded source hashes still match. The committed brief and both reviews remain unchanged; corrections live here.

- **Owner words:** The [Observatory queue][obs-queue] records the question quoted above and "I think this is in ki.prj.observatory". The [Terra log][terra-log] independently retains both. They place a design question here; they do not choose C. Quotations are verified against those records, not a recovered transcript.
- **Expired execution is historical:** Terra's log records SYNC-EVENING ended at midnight. S4 records its half-hourly HNR job stopped on 28 October. A stop-gap prompt was supplied, but running coverage is unknown. Recast A as attended sync under fresh bounded grants, not an evidenced existing scheduled service. Absence of local evidence does not prove no job exists anywhere.
- **Dispatcher decisions have later routed evidence:** S6's report left choices open at publication, but [DISPATCHER][chezmoi-queue] subsequently says Kris took its recommendations: chezmoi stages 4 and 5, ordinary enrolled Activities, one HNR job on terra, child Jobs coverage before retirement and a Triage-only comparison/dry-run with Drift off. Preserve that bounded routed acceptance; the originating verbatim owner entry was not located. It does not authorise two-host Git sync. Do not reopen that HNR scope or present its routed wording as Kris's quotation.
- **Publication default is already an owner boundary:** [MGIT-PUSH-GUARD][tools-queue] records opt-in `--push` and a hard `mgit.syncPush false` veto. Neither guard is in the inspected script. The incident of unreviewed commits being published and four sites redeploying is historical reported evidence, not a deployment reproduced here. Delivery of the guard is a prerequisite, not a new choice about the default.
- **Fetch is a mutation:** S8 fetches before checking dirtiness. A dirty skip preserves working files but can update local refs/objects. Do not use `mgit sync` as a read-only shadow. S8 skips divergence, predicts mergeability and does not perform the proposed ordinary merge; its sync interface has no `--json` contract. Chain delivery does not deliver the sync recipe.
- **Tidy's existing bounds are narrower:** S10 permits formatting and an explicit-path commit of sufficiently idle packages, forbidding deletion, movement and renaming. Its judgement, exclusions and permission to publish peers' commits belong to that expired pass, not to a future daemon. Package stewardship and generic Git mechanics remain different responsibilities.
- **Headless rules do not assign every ordinary job:** S12 assigns headless job design/install to Rig, chezmoi and tools-ki and governs one-package passes. Ordinary cross-territory sync is not automatically headless coordination. S7 separately establishes Rig's machine-resource boundary and chezmoi's source-install role; tools-mgit retains Git semantics.
- **Owner map and limits:** Add State of play, chezmoi, both host Rig works and every affected territory/repository owner. Ordinary push can deploy; avoiding a public release is insufficient. [PUSH-KRIS][obs-decisions] remains narrower than general standing publication authority for ki-principal and apps-observatory.local.

## Model

### Settled boundaries

Observation is read-only by default; Bridge operations require declared capability, visible inputs, proportionate confirmation and a receipt under [PDR-KI-OBSERVA-001][bridge-pdr] (S2). An already-running service supplies no standing unattended permission. C therefore requires explicit review of the PDR and package scope, with a superseding decision if their contract changes. D can potentially fit an attended Bridge operation; the mere existence of a request interface does not itself require replacing the PDR.

No schedule, package location, territory inventory or primary/secondary label grants cross-repository writes. PUSH-KRIS still reserves publication of ki-principal and apps-observatory.local to Kris. This affects any executor, not only C/D. A C/D design that never publishes those repositories need not retire that rule; one that would publish them needs Kris's explicit change. Confidential material never becomes public without his go. No force, hook bypass, implicit stash/reset, discretionary merge, acceptance or package deletion follows from a sync schedule.

The unattended criticality test still excludes changes that could disconnect Kris or take a site down. Deploying repositories require a repository-specific assessment; the historical four-site redeployment does not prove every deployment necessarily causes an outage. Any later connection-critical rollout needs a tested restore path in its task, and dotfiles rollout needs the independent judgement of its diff. This preparation grant permits none of those operations (S3, S13).

### Proposed responsibility contract

Keep four responsibilities explicit regardless of placement: adopted intent, due/exclusion checks, deterministic Git effects and truthful observation. Expectation must be discoverable independently of observed run files. Dotfiles remain the owner-indicated home for personal host setup, not an inferred extension of `seats.yaml` or a new authority registry in a territory.

A future binding needs stable host identity, repository/territory coverage, primary/secondary meaning, schedule and zone, read-back, absence policy and revision. The executor needs approved eligibility for each repository and phase. Publish only after verifying grants, every unpublished ancestor and its actual paths, confidential/deployment restrictions and live work, inside an effective exclusion boundary that prevents an unchecked ancestor entering the published range. Keep merge and tidy outside the basic fetch/fast-forward/publish recipe until separately approved and delivered.

Use distinct safeguards for occurrence overlap, checkout/index writes, common-Git-directory refs across worktrees and cross-host behaviour. All participating manual and scheduled entry points need the same applicable guards. Offsets reduce collisions but do not prevent them. Do not hold the shared index window across a whole network pass; preserve eligibility through the actual effect boundary. Reporter locks and short native Git ref locks are not that contract.

If hosts publish independently, ordinary non-force remote rejection can be legitimate contention, followed by later authorised reobservation. A global claim is not automatically necessary. If responsibility is exclusive, lease expiry or a dead PID is insufficient to retire an old executor: a suspended process may resume. Require an enforced fence or equivalent proof preventing its next prohibited effect; withhold failover during uncertainty. A report token or asynchronously replicated file is not a distributed atomic claim.

Durable receipts must distinguish expected, attempted, withheld, skipped, not-reached, failed and unknown members and phases, with host/run/occurrence identity and input/grant provenance. Record partial fetch, fast-forward and push effects; a transport failure is not proof a push failed remotely. Reconcile surviving descendants and uncertain effects before replay. Keep these semantic obligations open for later design, rather than selecting a schema, lock service or retry policy here (S4-S8, S10-S13).

### Alternatives

| Option | Execution placement | Main benefit | Remaining cost |
| --- | --- | --- | --- |
| A, recast | Fresh attended Rig passes | Smallest comparison baseline | Temporary grants and human judgement |
| B | Rig/chezmoi dispatcher child | Shared due/exclusion machinery | HNR scope expansion and child coverage |
| C | Observatory schedules and executes | One command surface | Product authority and coupled failure |
| D | Bridge requests external runner | Runner survives observer restart | Request authority and lost acknowledgements |
| E, authority addition | Direct per-host Rig resource | HOST-SYNC fit without dispatcher | Per-host binding and guards |

All five remain viable subject to their prerequisites. A has no claim of automatic continuity. B needs reconciliation with the bounded HNR dispatcher decision and host-versus-territory topology. C must operate without browser visits and recover when scheduling and observation die together. D must retain a durable request identity, reconcile lost acknowledgements and revalidate authority at execution; retrying a request is distinct from retrying uncertain Git effects. E avoids the dispatcher's scope change but still needs exclusion, recovery and an expectation feed. No option imports SYNC-EVENING's publication or tidy grant.

### Verified reliability findings

Using byte-identical copies of `automation.ts`, `beacon.ts` and `envelope.ts` from S11, isolated Bun fixtures reproduced:

- **Rolling hourly grace:** With an enabled `calendar:minute=0`, an `ok` result finished on 1 October and observation on 29 October at 12:59 UTC, the row is `ok`, not overdue, expected by 14:00. Seventy-two observations across that day (minutes 00, 30 and 59 each hour) remain healthy. The source explains why: each latest hourly instant restarts a two-hour allowance. The same stale result under `interval:3600` is overdue. Existing interval/daily tests do not establish hourly-calendar detection.
- **Occurrence ambiguity:** A previous occurrence finishing at 13:00:10 satisfies the 13:00 expectation. Timestamp comparison cannot prove which occurrence ran.
- **Projection limits:** A terminal fixture carrying a run ID, host, start and failed repository retains only status, summary and finish through `parseRun`. A start-only `running` fixture is unreadable. An enabled declared job with no observed row yields no row through composition; adapter source separately confirms discovery is driven by latest JSON filenames, with schedules enriching discovered rows.

These are confirmed source/fixture findings, not observations of failed production sync. The [contract][automation-contract] deliberately excludes `detail` for privacy; preserve that boundary and design separately governed mechanical coverage evidence. A parent `ok` or process exit zero cannot certify repository coverage. In S8 interactive refusal is counted as skipped without making the pass fail; ordinary skips normally do make it non-zero.

The rolling-grace defect and missing-coverage limitation block any rollout claim that the present Jobs view reliably detects missing hourly sync. They do not block completion of this design merge or authorise a repair. The supervisor should route these concrete findings to the appropriate owners separately; no new record, message or implementation was made here.

## Agreement and difference

A is the authority review; R is the reliability review. Marks describe their views on the brief, not votes. S labels resolve through the source inventory; details above settle additions.

| Point | A / R | Settlement and evidence |
| --- | --- | --- |
| 1, service and authority | Agree / Agree | Placement supplies no grant; S1-S3. |
| 2, mechanical core | Agree / Add | Keep judgement outside; fetch mutates before dirty refusal; S8-S10. |
| 3, offsets | Agree / Add | Neither exclusion nor convergence/read-back policy; S4-S6. |
| 4, locks | Agree / Add | Manual guards, checkout/common-dir protection and effective fencing; S6-S8, S13. |
| 5, publication | Agree / Agree | Adopted default guard is undelivered; check authority at effect; S3, S8-S9, S13. |
| 6, tidy | Agree / Agree | Current formatting grant forbids deletion; steward authority stays separate; S10, S12. |
| 7, reporting | Agree / Add | Expected membership and occurrence evidence missing; S6-S7, S11 and fixtures. |
| 8, recovery | Agree / Add | Retire executor and reconcile uncertain effects before takeover/replay; S6-S8, S13. |
| 9, ownership and criticality | Differ / Agree | Expand owner map; ordinary push may deploy; S3-S4, S9, S13. |
| 10, pilot | Agree / Add | Failure injection and independent recovery precede replacement; S6, S11-S13. |

A's claim that A has "nothing to keep" is valid as a correction to evidenced continuity, not proof no schedule exists. R's preservation baseline is retained as A recast. A's E supplies the missing direct-resource comparison. R's preference for D is conditional on a real request need; no such need is established by the later question alone. A's proposed superseding PDR is required only if the resulting contract changes, and PUSH-KRIS constrains publication, not mere placement. These distinctions settle overstatements without inventing a winner.

## Rollout plan

No capture, pilot or operation is authorised by this plan. After Kris's decisions, the receiving owners choose their own records and priorities; cross-repository needs travel as messages, not records written into another owner's queue.

1. **Resolve boundaries first:** Kris with [Ways of working][ways-work] settles HOST-SYNC and Activity home/realisation; [State of play][sop-work] and [chezmoi][chezmoi-work] reconcile the host-runner proposal with the routed HNR dispatcher remit. [Terra][terra-work] and [Sol][sol-work] own later host installation under their own authority. No host-scoped Activity home outside the principals is inferred.
2. **Deliver prerequisites through their owners:** [Tools burndown][tools-work] and tools-mgit own the safe recipe, adopted push guard, veto, explicit skip/refusal outcomes and machine-verifiable phase results. Observatory owns the expectation/coverage reader and honest overdue behaviour. Every territory and repository retains source access, publication and acceptance authority, including S10's personal chezmoi source and exclusions. Merge/tidy remain separate.
3. **Prepare one bounded pilot:** Pure due predictions first, without calling sync/fetch. Then separately approve one host/territory and fetch/fast-forward scope with explicit expected membership and exclusions. Push is a later, repository-opted-in phase after grant and deployment review; merge last, if ever approved. No new publication grant is proposed here. Record expiry, restoration and what stops the pilot.
4. **Prove failure behaviour:** Overlap beyond five minutes; manual/shared-index contention; dirty/live/missing repositories; divergence and rejected push; expired grants; host partition and suspended executor; sleep/wake, skipped/repeated civil times and clock rollback; complete parent/child bounds; termination with surviving descendants; interruption after each Git phase; lost acknowledgement and report-sink failure; observer and runner restarted independently. Preserve unknown and not-reached members through later success.
5. **Cut over only after proof:** Compare adopted intent, native reconciliation and receipts separately on each host. Retire the old binding only once coverage, exclusion and restore evidence pass. Pilot lessons go into each later wave before it starts under its own approved records and grant. S6's 28 October Terra deployment observations remain historical and cannot certify this cutover.

## Decisions

No decision below is adopted. Publication default, confidentiality, PUSH-KRIS, territorial ownership and tidy stewardship are settled constraints, not questions to reopen. Recovery details and rollout grants wait on the direction chosen; there is no new publication/tidy grant in these choices.

### SYNC-DIRECTION - Choose the candidate for design preparation

since 2026-10-29 · independent blind query review received

**Context:** The [merged sync paper](observatory-sync-report.md) compares A, attended passes under fresh grants; B, a Rig/chezmoi dispatcher child; C, Bridge scheduling/execution; D, Bridge requesting an external runner; and E, a direct per-host Rig scheduled activity invoking a deterministic Tools recipe. The merge preferred preparing E against A; [the blind query review](../away-sync-query-review.report.md) independently recommends that same course. A running Bridge supplies no periodic execution mandate. Existing publication, repository, confidentiality and deployment gates apply whichever candidate is chosen. HOST-SYNC responsibility semantics remain with Ways of working, with any seat/failover change separately owned; this choice does not settle them.

**Query:** Which candidate should its owners develop into a reviewable plan?

**Options:**

a) (recommended, confidence high - reviewed, independent source review agrees that direct per-host activity is the simplest candidate to develop) Prepare E against A as the baseline, retaining Observatory as observer and leaving executor selection, authority and rollout for the later reviewed plan.

b) Retain A alone for now, using fresh bounded attended grants; defer scheduled design.

c) Prepare B instead, first showing the shared dispatcher value and resolving its narrower HNR remit.

d) Prepare C instead, explicitly reviewing the Observatory product and authority change.

e) Prepare D instead, first establishing an attended request need and separate request, authorisation and receipt contracts.

### HOST-MEANING - Receiver-owned responsibility semantics

**Context:** The original HOST-SYNC instruction is in [Ways of working's queue](../../ki.prj.ways-of-working/messages.md); its [work definition](../../ki.prj.ways-of-working/work.md) and the owner's words establish that route. The blind query review independently agrees with independent per-host responsibility, offsets as cadence only and no automatic takeover. Seats govern coordination landing, not Git leases. Any change to seats or exclusive failover requires its own Host network/operational ownership; no Host network package was found and none is created. Primary read-back timing remains a separate plan question, not a meaning silently selected by this recommendation.

**Query:** Which responsibility meaning should Ways of working develop under HOST-SYNC?

**Options:**

a) (recommended, confidence high - reviewed, independent review agrees that offsets and seats establish no exclusivity or failover grant) Prepare independent per-host responsibility with explicit non-force contention handling and no automatic takeover; return read-back timing and offline recovery as separate plan choices.

b) Prepare exclusive responsibility only with separately reviewed fencing, retirement and failover ownership.

c) Keep the semantics undecided and retain attended passes while the requirement is narrowed.

This is a routed receiver-owned question. Observatory asks Kris here only for SYNC-DIRECTION; the route transfers no authority and settles no option.

## Changes after review

- Authority review: recast A after expiry evidence; add E; restore MGIT-PUSH-GUARD, territorial publication and PUSH-KRIS limits; expand affected owners; distinguish routed HNR acceptance from its earlier open report.
- Reliability review: qualify fetch/dirty behaviour; require expected membership, shared manual guards, phase uncertainty, effective fencing and restart-independent receipts; independently reproduce hourly-calendar and projection limits.
- Merge settlement: avoid claiming absent schedules from absent evidence; distinguish ordinary Activity from headless coordination; qualify blanket PDR/PUSH-KRIS objections to C/D; distinguish deployment risk from inevitable outage; prefer E/A comparison without appointing an executor.
- Scope control: preserve the original brief and reviews unchanged, retain two actionable future choices, and separate newly confirmed defects from design rollout. No owner decision, new grant, record, pilot, schema, configuration or runtime action follows from this report.

### Final independent query review and freshness receipt

The [blind query review](../away-sync-query-review.report.md) independently agrees with E-versus-A preparation and independent per-host responsibility. Under the query-review rule only those matching courses rise from medium/moderate to high, with reviewed reasons. This agreement selects neither course. The original authority/reliability disagreement remains in Agreement and difference; it is not a unanimous executor recommendation.

At the pre-route final receipt, 20 of the original 25 source hashes still match; the later HOST-SYNC receipt also changes Ways of working messages. The five changed sources are Observatory messages/decisions, Tools messages and the coordination/delegation standards: receipts and method updates postdate the brief. Their current changes were reread; the original inventory remains historical evidence. No source, installed-service or other-host freshness is inferred from an old hash. The hourly-calendar reproduction remains 72 healthy stale observations versus an overdue interval control; no defect has been adopted or repaired. Existing HNR specimens/producer and Tools resolver/recipe routes remain with their owners.

[obs-queue]: ../messages.md
[obs-decisions]: ../decisions.md
[terra-log]: /Users/krisbrown/workspaces/personal/personal-principal/+/_WORK/personal.reg.rig-terra/decisions.md
[chezmoi-queue]: ../../ki.prj.chezmoi/messages.md
[tools-queue]: ../../ki.prj.tools-burndown/messages.md
[bridge-pdr]: /Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/decisions/PDR-KI-OBSERVA-001-observatory-beacon-and-bridge.md
[automation-contract]: /Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/contracts/src/automation.ts
[ways-work]: ../../ki.prj.ways-of-working/work.md
[sop-work]: ../../ki.sop.main/work.md
[chezmoi-work]: ../../ki.prj.chezmoi/work.md
[terra-work]: /Users/krisbrown/workspaces/personal/personal-principal/+/_WORK/personal.reg.rig-terra/work.md
[sol-work]: /Users/krisbrown/workspaces/personal/personal-principal/+/_WORK/personal.reg.rig-sol/work.md
[tools-work]: ../../ki.prj.tools-burndown/work.md
