# Scheduled cross-machine Git sync ownership: reliability review

**Reviewer:** GPT-6 (Codex runtime) · **Date:** 2026-10-29 · **Read-only:** yes, except this commissioned review and its local commit

**Baseline:** Original [brief](observatory-sync-brief.md), committed at `6fd427e47200f5e0bf548d280c506a833bcb58b0`. Review B under AWAY-2026-10-29; preparation only, ending 09:00 GMT/UTC or explicit return sooner.

## Own view

Formed independently before reading any other review. I have not read the authority review, its report or a merged sync recommendation/decisions file. The earlier territory-dispatcher merged report is required source S6, not this design's other review.

The strongest boundary is a deterministic executor that remains accountable when the Observatory is absent. A running service makes C feasible, but provides no evidence that C is safer or cheaper than A, B or D. The hard problems are the inventory of expected work, shared-checkout exclusion, authority at the actual mutation boundary and reconciliation of uncertain effects. Moving the timer leaves those problems intact.

Compare A as the preservation baseline and D as the candidate where an attended Bridge request has an established need. B becomes useful if several adopted Activities justify dispatcher infrastructure. C needs evidence that combining scheduling, execution and observation outweighs the coupled restart and failure boundary. These are review preferences, not selection of an owner or authority to implement.

## Fact check

All 25 source entries in the original brief, including the two Automation tests and method templates, matched their recorded SHA-256 values at review. The working brief was byte-identical to its original committed version. Current queues and the AWAY entry were read directly. This establishes local source freshness only: no installed binding, loaded service, other-host state or remote ref was inspected. S6's 28 October Terra observations retain their historical scope.

- **S1-S3:** Observation/Bridge separation and mechanical-first operation are explicit. The current AWAY entry preserves five unanswered choices and narrower product/runtime gates. The new review instruction grants only this artefact and commit; it does not inherit earlier execution grants.
- **S4-S5:** HOST-SYNC proposes offsets and a still-unresolved primary read-back. Seats bind coordination roles, not primary/secondary sync responsibility. Neither proves installation or failover authority.
- **S6-S7:** The dispatcher report explicitly identifies manual bypass, surviving descendants, whole-child timeout gaps, partial effects and missing Jobs coverage. Reporting locks protect records; one launchd label does not protect separate manual paths or another host. Source-native schedule mismatch is already demonstrated historically, so declarative intent cannot certify actual timing.
- **S8-S9:** The current `sync_command` fetches before checking dirtiness, then serially checks and fast-forwards or pushes; it skips divergence. Fetch deduplication applies within one invocation to a common Git directory and remote, not across processes. `sync --json` is rejected; chain JSON is a different contract. A skipped repository normally makes sync non-zero; an interactive refusal is counted as skipped without failure. Thus exit zero alone still does not establish complete coverage. The chain record remains awaiting review and excludes sync redesign. [Git paths](</Users/krisbrown/workspaces/knowledge-islands/tools-mgit/bin/mgit:2980>).
- **S10:** The hand-run pass includes live-run checks, exclusions and bounded conflict/tidy judgement. Its tidy is formatting and an explicit-path commit, with deletion, movement and renaming forbidden. The brief's warning about deletion/acceptance is a future boundary, not something this pass presently does. A dirty checkout can still have fetched refs/objects before the skip, so “untouched” must not be read as zero local Git effects.
- **S11:** Latest JSON filenames create rows; Rig schedules only enrich those rows. A scheduled job with no JSON is absent. `parseRun` retains status, summary and finish time, losing run/host/occurrence identity and any repository results. Starts become unreadable, not confirmed running, and unreadable rows are never overdue. History is limited in the projection and cannot replace a durable occurrence ledger. [Discovery](</Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/evidence/src/automation.ts:215>), [parser](</Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/contracts/src/automation.ts:138>).
- **S12-S13:** Headless coordination has its own trigger, grant, exclusion, bound and no-within-firing-retry rules. That contract does not automatically govern every ordinary Git Activity. The proposed sync recovery policy needs its own approval; it is not already delivered by borrowing the headless name. Publication and criticality gates remain unchanged.

### Observation counterexamples

A local, pure call to the current `composeAutomation`, with an enabled `calendar:minute=0`, an `ok` result from 1 October and observation at 29 October 12:59 UTC, returns `standing: ok`, `overdue: false`, expected by 14:00. At each hour the latest scheduled instant advances, and its two-hour grace starts afresh. During a continuous hourly calendar the row never becomes overdue, however old its readable result. This differs from `interval:3600`, whose deadline is anchored to the last finish. Existing tests cover daily/weekday calendars and hourly intervals, not this rolling hourly-calendar failure. [Judgement](</Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/contracts/src/automation.ts:381>), [tests](</Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/contracts/src/automation.test.ts:178>).

A previous occurrence finishing at 13:00:10 can also satisfy the 13:00 expectation without establishing that occurrence ran. A synthetic terminal payload with an old run ID, host, start and failed repository entry loses all four through `parseRun`. These are directly reproduced projection limits, not claims about actual jobs. A parent `ok` carrying failures only in `detail` cannot provide repository health because `detail` is intentionally excluded. Preserve that privacy boundary and supply separately governed mechanical evidence.

## Points

| Point | Mark | Reason and evidence |
| --- | --- | --- |
| 1 | Agree | Service liveness supplies no execution grant; S1-S3, S10. |
| 2 | Add | Mechanical core is right; fetch has local effects before dirty refusal; S8-S10. |
| 3 | Add | Offsets do not settle convergence or partition policy; S4-S6. |
| 4 | Add | Require common manual guards and effect-boundary fencing; S6-S7, S13. |
| 5 | Agree | Eligibility must survive until the actual push; S8-S10, S13. |
| 6 | Agree | Keep tidy separately authorised; present pass forbids deletion; S3, S10, S12-S13. |
| 7 | Add | Existing Jobs cannot prove host/occurrence/repository coverage; S6-S7, S11. |
| 8 | Add | Distinguish expired claims from retired executors and unknown effects; S6-S7, S10, S12-S13. |
| 9 | Agree | Product placement changes no criticality or source-owner gate; S3, S6, S12-S13. |
| 10 | Add | Pilot needs repeatable failure injection and restart-independent receipts; S6, S11-S13. |

The additions below expand claims rather than reject their direction. There is no Differ mark: the material corrections qualify established-fact wording and expose missing proof, rather than contradict the ten provisional requirements.

**Point 2:** Do not execute `mgit sync` as a read-only shadow. Due predictions and eligibility checks must exclude its fetch phase as well as fast-forward/push. A future executor needs per-step evidence; an interrupted sequence may have fetched or fast-forwarded before a later failure.

**Point 3:** Primary publication at 12:00 followed by secondary publication at 12:05 leaves primary missing the latter until an agreed read-back. A five-minute offset promises neither a five-minute completion bound nor convergence by the next tick. If hosts may publish their own independent commits concurrently, remote non-force update rejection is normal contention to report; a global territory claim may be unnecessary. If only one host may execute, that exclusive responsibility and loss-of-contact policy must be explicit. Neither policy follows from seats.

**Point 4:** The Git common directory, including linked worktrees, is the local coordination boundary for shared refs; working-tree/index changes need the checkout boundary too. A clean/live-work check outside exclusion is a race. Revalidate branch, upstream, HEAD, intended commit range, grant and owned paths inside the relevant write window. All scheduled and manual entry points must participate. Git's own short ref/index locks are not a transaction around eligibility, hooks and push. Avoid holding the shared index window across the entire network pass, but prove no new unchecked ancestor can enter the pushed range between validation and publication.

**Point 7:** Derive the expected set independently of observed files. Missing repositories must remain in that set as missing/blocked, not disappear during discovery or be silently replaced by another checkout. A top-level result needs coverage and phase evidence, with skipped/not-reached/unknown outcomes preserved. Failure priority and timestamps cannot stand in for occurrence correlation. The rolling-grace counterexample is a pilot blocker for any promise that the current Jobs view reliably detects missing hourly sync.

**Point 8:** Lease expiry, a dead PID and an old lock pathname are different observations. A suspended old executor can resume after a replacement claims ownership. Prevent its next effect through a validated generation/fence or an equivalent enforced boundary; a token written only to a report does not fence Git. A local file or Git commit replicated later cannot establish a distributed atomic claim. During uncertainty withhold exclusive failover unless the chosen mechanism can prove retirement. PID reuse, boot identity and surviving descendants must be considered before disposition; never unlink an OS-held lock pathname to “free” a running lock.

**Point 10:** Verify preserved behaviour with a bounded, separately authorised pilot, including loss of the observer while execution continues and loss of the runner while observation continues. A service restart must reconcile durable attempts and process ownership before claiming another occurrence, not replay an in-memory timer backlog.

## A-D reliability comparison

| Alternative | Main reliability benefit | Additional proof required |
| --- | --- | --- |
| A | Smallest preservation baseline | Current jobs still need common guards and expected coverage. |
| B | Shared due checks and child discipline | Parent/child bounds, fairness, claims and schedule feed. |
| C | One local command surface | Browser-independent timing, durable recovery and restart isolation. |
| D | Executor survives observer restart | Durable request receipt, duplicate suppression and authority revalidation. |

A retains per-label exclusion only for invocations of that label; manual calls remain a separate risk. B must bound both each child and the complete tick, report withheld children and avoid starvation. C may run headlessly, but process death can remove scheduling and observation together; durable receipts must survive it. D has an acknowledgement gap: an accepted request followed by a lost response must reconcile the same request, not issue a second mutation. Retrying requests and retrying uncertain Git effects are distinct policies. Under all four, an unavailable host produces unknown/missing evidence rather than a newly elected executor.

## Stress tests and proof obligations

- **Offsets, manual starts and local writes:** Hold a run longer than five minutes, start a manual pass and edit/stage another file during its preflight. One participating local writer must win; the other records withheld contention, preserves the peer index and revalidates before continuing. A stopped parent with a surviving child must not release effective exclusion prematurely.
- **Two hosts and fencing:** Partition hosts after a claim, suspend the holder past its lease and resume it after attempted takeover. Demonstrate the old holder cannot perform a newly prohibited effect, or withhold takeover. For independent-host publication, demonstrate ordinary remote rejection and later reobservation without force, implicit merge or concealed failure.
- **Sleep/wake and clock changes:** Recompute due work from agreed instants and the adopted timezone; bound lateness, coalescing and catch-up. Both hosts may wake together despite offsets. Test repeated/skipped civil times, clock rollback and a time change during a run. Duration and ownership checks must not depend solely on adjustable wall clocks. Existing London DST tests prove observer calculations, not native scheduling parity.
- **Partial effects and reporting:** Interrupt after fetch, after fast-forward, after remote acceptance but before acknowledgement, and after completion but before durable reporting. Retain uncertain phase outcomes. Reobserve local and remote facts under later authority before retry; a push transport failure is not proof the remote rejected it. Failure of the report sink is separate from failure of Git.
- **Missing and failed repositories:** Omit an expected checkout, break one upstream, withhold one grant, reject one push, lose one terminal record and fail discovery. Every expected member must remain accountable. Continued independent work is permissible only where dependencies allow; no healthy aggregate can erase blocked, failed or unconfirmed members.
- **Stale claims and restart independence:** Kill the parent, leave a descendant, reboot, and restart observer/runner separately. Identify owner, boot and generation; reconcile surviving activity before retry. Keep history and previously uncertain effects visible after a newer run succeeds. Bound preparation, subprocess tree, shutdown and reporting as well as the central Git command.

Proof of host responsibility requires an owner-approved, dotfiles-owned binding naming stable host identity, territory/repository coverage, primary/secondary meaning, schedule/zone, read-back, absence/failover policy and revision. Compare adopted intent with separately observed native reconciliation and per-host evidence age. Proof of honest outcomes requires expected versus attempted membership, distinct host/run/occurrence identity, input and grant provenance, per-repository phase/result/reason, start and terminal evidence, and explicit uncertainty. These are semantic requirements, not a selected schema, lock service or execution owner.

## Review boundary

No runtime, scheduler, service, provider or remote operation was performed. No product code, package state, queue, grant, decision or work record was changed. This review proposes neither automatic repair of the observation gaps nor rollout under the AWAY grant. The merge stage should carry the findings into its comparison and leave topology, failover, lateness, replay and cutover choices to Kris and the responsible owners.
