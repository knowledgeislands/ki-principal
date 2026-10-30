# Host synchronisation: brief

**Owning work:** `ki.prj.ways-of-working`

**Owner:** Kris Brown · **Owning repository:** knowledgeislands/ki-principal · **Date:** 2026-10-30

## Problem

Equivalent coordinating work runs on two hosts, Terra and Sol, and both commit to the same GitHub repositories. Without an agreed synchronisation sequence the two hosts race each other, leave commits stranded on one machine and fall out of level. Terra's half-hourly HNR `mgit sync` was stopped on 28 October 2026 until this design lands, according to the sender's line; that is sender evidence, not a fresh status check.

A preparation report, [Host synchronisation: merged preparation report](<../host-sync-report.md>), proposes a model, but it was prepared without a common brief or independent reviews of its own proposal; the reviews it draws on are Observatory's, on the adjacent question of executor ownership. Kris approved HOST-REVIEW a) on 30 October 2026, so this brief supplies the missing gate: the requirement, the proposal restated as numbered claims, and what each reviewer must answer. The numbered claims below restate the preparation report in full; a reviewer needs no other copy of the proposal.

Nothing here adopts a mapping, cadence, executor, schedule or publication grant. No message has been sent to either Rig queue.

## Owner's proposal

Kris, 28 October 2026, 13:50 GMT, received through `personal.reg.rig-terra` as the HOST-SYNC line, preserved in full in [the received design input](<../host-sync-and-reply-trades.md#full-received-source>):

> "the sync process should always be run from this equivalent thread on both Terra and Sol … each of them gets an offset … we're going to get into race conditions if both are trying to do the sync at the same time and we probably want to do a resync as well in short order after it."

The shape Kris proposed in the same line, with his words quoted inside the sender's summary:

1. The dotfiles carry an entry naming, per territory, which host is primarily and which secondarily responsible ("I can't remember where it's gone").
2. A regular activity registered per host: "on the hour, it should resync and publish effectively into the GitHub repos the ones which it has primary responsibility for. And then five minutes later … the secondary ones", so each primary publishes first and each secondary then pulls in the other host's primaries and adjusts.
3. "the primary then needs to be able to read the secondary updates … It shouldn't be an onerous process", which still needs deciding.

Kris: "push that into the ways of working … I'll deal with the ins and outs."

HOST-SYNC-REPLY, the same day: "when the design is settled, send its rollout as one line each to personal.reg.rig-terra and personal.regular.rig-sol, which carry it into the chezmoi sources and Rig on their hosts."

From [the owner decisions log](<../../decisions.md>):

- HOST-SYNC-DESIGN, 29 October 2026: "Take up HOST-SYNC as the next design under ki-work-design. Its inputs are the HOST-SYNC line in messages.md and Observatory's HOST-SYNC-REVIEW, with its design report. Put any questions for me as tagged decisions with recommendations. When it's decided, send the rollout as one line each to personal.reg.rig-terra and personal.reg.rig-sol."
- RECOMMENDED-ALL, 29 October 2026, covering HOST-SYNC option a among others: "The queries, I agree with the most recommended one for, so you can get on with those, please." HOST-SYNC option a was to discuss and settle the existing design choices, then send one bounded rollout line to each Rig queue, with Rig and chezmoi owning execution.
- LANDSCAPE, 30 October 2026: Kris asked to pick up HOST-SYNC early, keeping commits level across Sol and Terra (the log's summary, not verbatim).
- HOST-REVIEW, 30 October 2026: "proceed with the recommendation, then refine additional HOST-* based on that review".
- REVIEW-INDEPENDENCE, 30 October 2026: "blind reviews ... must not really be concerned with previous decisions too much, and they must be able to challenge those, so we can make sure that we haven't gone down a particular avenue incorrectly".

## Established facts

- Seats are coordination routing, not sync primacy. [ADR-KI-PRINCIPAL-007](<../../../../../Admin/Governance/Decisions/ADR-KI-PRINCIPAL-007-territory-seats-on-hosts.md>) and chezmoi `.chezmoidata/seats.yaml` (checked at chezmoi `38be5a1`) bind Terra as home (humans-not-robots, knowledge-islands, personal, legal) and Sol as hub (valle-armonia, sacred-inquiry, techmedix, equal-remedy, knowledge-islands, personal, legal), with active-active territories tipped to the hub. The file says "a seat says only where a coordination service treats the territory as live"; it carries no primary or secondary sync field.
- The two receiving queues exist as `personal.reg.rig-terra` and `personal.reg.rig-sol` in personal-principal `+/_WORK/`. HOST-SYNC-REPLY's `personal.regular.rig-sol` is an older spelling of the latter.
- Observatory holds an adjacent design on executor ownership: [brief](<../../../ki.prj.observatory/design/observatory-sync-brief.md>), [authority review](<../../../ki.prj.observatory/design/observatory-sync-review-authority.md>), [reliability review](<../../../ki.prj.observatory/design/observatory-sync-review-reliability.md>) and [merged report](<../../../ki.prj.observatory/design/observatory-sync-report.md>). It compares realising the pass as a fresh thread pass (E) or a direct scheduled resource (A) and selects no winner. Observatory owns the separately routed HOST-RESPONSIBILITY observation input.
- The agreed work state machine, from the [diagram source](<../work-state-machine.mmd>) and the ROLES-ORCHESTRATOR and ROLES-EITHER entries in the decisions log: Working contains With worker, Handoff to supervisor, With supervisor and Handoff to worker; Bootstrap enters Working; Working concludes through End (work) and `stop` reaches At rest, with reasons holding, waiting or moving; `resume` returns through Bootstrap and `finish` leaves At rest for Finished. Supervisor, worker and orchestrator are roles that an AI or a human may fill. These are agreed meanings, not a claim about deployed encoding.
- Request/reply trades (TRADES-REPLY, WAITS-AS-TRADES) and PACKAGE-FORWARDING are separate inputs held in [the received design input](<../host-sync-and-reply-trades.md#requestreply-trades>); they are out of scope here.
- This brief was written at Principal `8dd0f118`. No HNR repository, scheduler, provider or host service was read or changed in preparing it.

## Reflection

The claims restate the preparation report's proposal. Each is one claim to agree with, differ from or extend.

### Mapping

1. A declaration in the dotfiles (chezmoi sources) names, per territory, the primary and secondary host for synchronisation; Rig and chezmoi own its preparation.
2. The declaration is separate from seats. ADR-KI-PRINCIPAL-007 and `seats.yaml` govern coordination landing only; seat fallback is not a sync takeover, a Git lease or publication eligibility, and the seats topology is not reopened.
3. A territory label grants no repository access or publication. The map must enumerate, per host, the repositories it publishes, the phases it may perform, exclusions and a revision.
4. The map is not inferred from seats or checkout inventories: Rig and chezmoi propose it, Kris approves it before any configuration or operation, starting from one jointly nominated non-HNR, non-deploying pilot repository.

### Sequence

5. Each host's pass has two phases: a primary phase that inspects and publishes only eligible repositories in its approved primary set, then a later secondary phase that consumes the other host's published primary work under each repository's rules.
6. The Git operation is one bounded, reviewed recipe from its product owner: refuse on dirty or live work, fetch and fast-forward only, publish without force, inspect every unpublished ancestor, and record outcome evidence. It includes no discretionary merge, stash, reset, acceptance or package tidy. A rejected push is contention to reobserve, never permission to overwrite.
7. The ability to pull confers no authority to publish; each repository and each actual effect needs its own grant.
8. How the recurring pass is realised, a fresh pass of the equivalent thread or a direct scheduled resource, is left unchosen here; Observatory's E-versus-A comparison stays a separate proposal.

### Cadence

9. Offsets are cadence only. They confer no lease, exclusion, acknowledgement or proof that the preceding phase completed. Each phase rechecks eligibility and local exclusion, may see only the preceding published revision and reports that limitation, never waits indefinitely and never infers success from elapsed time.
10. The proposed cadence is hourly in GMT/UTC: Terra primary `:00`, Sol primary `:02`, Terra secondary `:05`, Sol secondary `:07`, prepared for later planning and not activated, subject to explicit exclusion and pilot evidence.

### Secondary publication

11. Pulling primary work on the secondary cannot publish secondary-origin commits, so scheduling read-back alone cannot meet Kris's requirement that the primary reads secondary updates.
12. The recurring secondary phase stays pull-only. Secondary-origin changes reach Git only through separately authorised attended work; read-back consumes only what is actually published and reports unpublished work as outside its coverage.

### Read-back

13. Read-back timing is a separate choice from secondary publication authority, and both are separate from message forwarding and request/reply trades; neither implies the other.
14. The primary reads published secondary-origin updates at the start of its next authorised hourly occurrence, before evaluating its own eligible publication. The resulting delay is stated explicitly, and no immediate convergence is promised.

### Absence

15. No host adopts an absent host's responsibilities; there is no automatic takeover, and the present host keeps only its own authority.
16. A returning host needs fresh authority and source checks before its own work. No catch-up, retry, missed-occurrence or replay policy is chosen; interrupted or uncertain publication is reconciled before any replay. Exclusive failover, if ever wanted, needs fencing and executor retirement under a separate owner design.
17. Unknown stays unknown: observation must distinguish expected host, repository and phase membership from attempted, skipped, failed and unknown effects, and a green parent result cannot stand in for coverage or authority evidence. Observatory owns that observation design.

### State-machine boundaries

18. Synchronisation is not a work-state transition: it does not receive a handoff, release a waiting package, prove At rest portability, resume a worker or finish a package. At rest (moving) still meets its own portability checks; synchronised files alone are insufficient.
19. Synchronisation adds no forwarding service, second queue, automatic acknowledgement, polling field, delivery-triggered completion or automatic release of a sender's wait. One authoritative incoming queue per package and an explicit request for a reply remain the semantics.

### Authority and rollout

20. HOST-SYNC confers no scheduler authority. Terra's stopped sync is neither restarted, retired nor replaced by this design, and existing narrower task and repository push rules govern every operation.
21. After review and Kris's choices, one rollout line goes to each of `personal.reg.rig-terra` and `personal.reg.rig-sol`, requesting planning, not installation; Rig owns the host rollout and chezmoi the source changes, and neither receives a record created in its queue by this work.
22. Rollout runs one attended pilot before any recurrence: compare expected membership and offset predictions first without fetching; prove one-host fetch and fast-forward before adding the second host; opt into publication later with ancestor and path review; test dirty-work refusal, overlap beyond offsets, divergence, absence and return, interrupted phases and uncertain publication; and require a restore path, expiry and stop conditions before any host operation is approved.
23. Taken together, the proposal meets Kris's stated requirement, regular equivalent sync on both hosts "soon", with offsets and a read-back that "shouldn't be an onerous process", without being heavier than that requirement warrants.

## What each reviewer must answer

Independence: you may and should challenge earlier owner decisions and prior reasoning where the evidence warrants; an earlier decision is evidence, not a constraint, and agreement with it earns no confidence by itself.

Work read-only against the sources this brief cites, and form your own view before reading any other review. Then give:

1. **Fact check.** Confirm or correct each established fact and each quotation of Kris's words against its source.
2. **Per-claim verdict.** For every numbered claim, 1 to 23, mark **Agree**, **Differ** or **Add**, with one or two sentences; every Differ cites its evidence and says what should replace the claim.
3. **Missing claims.** Anything the design needs that no claim covers, numbered on from 24.
4. **Recommendations.** For each of the four open choices below, recommend one option, or a better one of your own, with a confidence of high, medium or low and a one-line reason.

### HOST-CADENCE - Which cadence the Rig owners prepare, without activating it

a) Prepare hourly GMT/UTC phases: Terra primary `:00` and secondary `:05`; Sol primary `:02` and secondary `:07`, subject to explicit exclusion and pilot evidence.

b) Keep cadence unchosen and prepare attended passes only until the pilot establishes phase duration and a suitable interval.

### HOST-COVERAGE - Who prepares the responsibility map

a) Rig and chezmoi propose the per-territory primary and secondary map, enumerate repository and phase eligibility plus exclusions, and return it for approval before configuration or operations, starting with one jointly nominated non-HNR, non-deploying pilot repository.

b) Kris supplies the mapping and pilot repository directly; the receiving owners then verify eligibility and prepare its bounded plan.

### HOST-SECONDARY-PUBLISH - How secondary-origin changes reach Git

a) Keep secondary consumption pull-only in the recurring proposal; secondary-origin changes reach Git through separately authorised attended work, and read-back reports unpublished work as outside its coverage.

b) Rig and the Git-tool owner prepare a distinct opt-in secondary-publication phase with repository eligibility and authority-at-effect checks, neither activated nor granted by HOST-SYNC.

### HOST-READBACK - When primaries check published return work

a) Read published secondary-origin updates at the start of the primary's next authorised hourly occurrence, before evaluating its own publication, stating the delay and promising no immediate convergence.

b) Add a separately bounded pull-only read-back at Terra `:10` and Sol `:12`, keeping next-occurrence recovery when a prior phase is late or absent; this adds promptness, not publication authority or an acknowledgement guarantee.
