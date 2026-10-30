# Host synchronisation: merged report

**Brief:** [brief.md](brief.md) · **Reviews:** [review-claude.md](review-claude.md) (Claude Opus 5.5), [review-codex.md](review-codex.md) (GPT-6.1 Sol, Codex) · **Date:** 2026-10-30

**Owning work:** `ki.prj.ways-of-working` · **Authority:** HOST-REVIEW a), 30 October 2026: "proceed with the recommendation, then refine additional HOST-* based on that review". This report adopts nothing; the four decisions below are Kris's.

## Summary

Both reviewers accept the brief's safety boundaries and both find it does not meet Kris's requirement: a pull-only secondary never levels commits made on the secondary, and next-hour read-back is not the "resync as well in short order" Kris asked for. The merged model keeps Kris's shape: a chezmoi-carried per-territory map naming each territory's primary and secondary host; on each host an hourly pass that publishes its primary territories, then a secondary phase five minutes later that fast-forwards the other host's work and, once Kris grants it, publishes its own fast-forward work in those territories; then a short pull-only read-back on each primary. One deterministic recipe runs every phase: refuse dirty, live or diverged repositories, fast-forward only, never force. A named resolver, the host's Rig thread, takes what the pass leaves. Offsets are cadence only. Nothing exclusive is held, so an absent host blocks nothing and there is nothing to take over. One attended run per host measures the pass before any recurrence. Rig and chezmoi own the rollout; nothing here grants scheduler or publication authority.

## Corrections to the brief

- **Observatory labels are reversed.** The [Observatory merged report](<../../../ki.prj.observatory/design/observatory-sync-report.md>) says "Compare E, a direct per-host Rig resource, against A, attended passes under fresh grants", leaning to E without selecting it. Both reviewers caught this; the merged model uses descriptive names.
- **The stopped HNR sync is not the whole history.** Kris asked Terra at 17:40 GMT on 28 October (SYNC-EVENING) to "check every 15 minutes ... make sure that everything is pushed" ([Terra sync brief](</Users/krisbrown/workspaces/personal/personal-principal/+/_WORK/personal.reg.rig-terra/briefs/sync.md>)); asked Sol at 20:58 GMT the same day (SOL-SYNC) for "a regular 15 minute git sync", which ran at `:07`, `:22`, `:37` and `:52` until 16:20 GMT on 29 October ([Sol decisions](</Users/krisbrown/workspaces/personal/personal-principal/+/_WORK/personal.reg.rig-sol/decisions.md>)); and on 29 October at 16:40 GMT asked for `mgit sync` of everything on both hosts (SYNC-NOW, not run before the host-move stop, [Terra decisions](</Users/krisbrown/workspaces/personal/personal-principal/+/_WORK/personal.reg.rig-terra/decisions.md>)). [Sol's queries](</Users/krisbrown/workspaces/personal/personal-principal/+/_WORK/personal.reg.rig-sol/queries.md>) hold an open HOST-SYNC query recommending a restart until this rollout lands. Checked by the merge: SOL-SYNC was "fast-forward or rebase only", so the precedent is not identical to the ff-only recipe below.
- **The recipe already exists and pushes by default.** `mgit sync` fast-forwards behind-only branches and pushes ahead-only ones, leaving diverged, dirty and detached checkouts ([tools-mgit `bin/mgit`](</Users/krisbrown/workspaces/knowledge-islands/tools-mgit/bin/mgit>), the push at line 3177). Observatory records this as contrary to an adopted no-push-default request, so a pull-only phase cannot simply call it.
- **A per-territory pairing exists.** [ADR-KI-PRINCIPAL-007](<../../../../../Admin/Governance/Decisions/ADR-KI-PRINCIPAL-007-territory-seats-on-hosts.md>) says "Each territory has one seat and one standby", and the sender's line names `seats.yaml` as "the nearest today". It is a coordination pairing, not sync primacy.
- **"Soon" and "urgent" are the sender's words**, not Kris's quoted ones; claim 23 attributed "soon" to Kris.
- **Owner naming.** The Rig host packages name the chezmoi-method owner differently (`ki.prj.chezmoi` on Sol, `ki.chezmoi` on Terra); the rollout lines should name the current one.

All quotations of Kris and of the decisions log were confirmed verbatim by both reviewers; Codex also matched the received input against the historical messages file's recorded checksum.

## Model

**Map.** A chezmoi-carried declaration, beside `seats.yaml` but with its own meaning, names per territory the primary and secondary host, plus explicit exclusions and named extras such as the chezmoi source repository. Each occurrence resolves it to the expected repository membership it records, so observation reads membership from the map rather than from report files. It references existing grants and vetoes; it is not a second authority register.

**Pass.** Each host runs the same recipe in three phases, offsets being cadence only:

1. _Primary_: fetch, fast-forward and publish ahead-only work in its primary territories.
2. _Secondary_, five minutes later: fetch and fast-forward the other host's published work in its secondary territories; publish its own ahead-only work there only once Kris has granted secondary publication.
3. _Read-back_, shortly after: a pull-only fetch and fast-forward on the primary, so secondary-origin work is consumed promptly; the next occurrence also catches anything late.

**Recipe.** One version of `mgit sync`, or its successor, certified by `tools-mgit` with an explicit publish mode and a pull-only mode. It refuses dirty, detached, diverged and live checkouts, live meaning a held `ki agent` write lock or another session's unpushed commits under 60 minutes old, as Terra's brief already tests. It pushes exactly the tip it checked, fast-forward only, never forced; a rejected push is contention to reobserve, never permission to overwrite. It covers linked worktrees through their common Git directory and acts on the default tracking branch only unless the map says otherwise. It does no merge, rebase, stash, reset, `chezmoi apply`, acceptance or package tidy. It writes a tally of in-sync, pulled, pushed, skipped and failed repositories where the host thread reads it.

**Divergence.** Fast-forward-only integration cannot combine two hosts' independent commits. The host's Rig thread takes each diverged repository from the tally and resolves it through a bounded resolve run under the existing standard, escalating to Kris when it is still diverged after two hours with no new local commits.

**Ownership and executor.** Kris's "run from this equivalent thread" sets ownership: each host's Rig thread owns its pass, reads its tally and resolves what it leaves. Whether the pass executes as a fresh thread pass or a direct per-host scheduled resource stays with Observatory's comparison; neither inherits the other's grants.

**Authority.** Pulling grants nothing. Publication needs an explicit grant, which may be standing where Kris gives it, as the Git authority standard and PACKAGE-PUSH allow, naming the territories and revocable by a stop word. A returning host revalidates still-effective authority and current sources; it does not need a fresh grant.

**Absence and missed occurrences.** No host takes over another's work. A missed or late occurrence, including laptop sleep, is skipped; the next occurrence is one fresh bounded pass, with no backlog replay. An uncertain earlier push is reobserved, appearing as ahead or diverged, never blindly retried. Each phase has a finite duration bound and refuses to overlap its own previous run.

**Observation.** Unknown stays unknown: the tally distinguishes expected from attempted, skipped, failed and unknown. Observatory improves coverage evidence later; its liveness never gates sync execution.

**Boundaries.** Synchronisation is not a work-state transition and adds no forwarding, queue, acknowledgement or wait release.

## Agreement and difference

C is the Claude review, X the Codex review. A Differ is settled on cited evidence where it can be, otherwise named as open and carried to a decision.

| Claim | C | X | Merged position and evidence |
| --- | --- | --- | --- |
| 1 | Add | Agree | Agreed. Name the receiving owners exactly: the chezmoi source through `personal.reg.rig-terra` and `personal.reg.rig-sol`, with the current chezmoi-method package. |
| 2 | Agree | Agree | Agreed. Store the field beside the seats so they are reviewed together, without coupling their meaning. |
| 3 | Differ | Add | **Settled.** Territory grain, as Kris asked ("per territory") and `mgit --territory` already supports, with explicit exclusions and extras; each occurrence records the resolved per-repository membership (X's concern), and the map references existing grants rather than duplicating them (X). |
| 4 | Differ | Agree | **Open: HOST-COVERAGE.** Both have Rig and chezmoi propose and Kris approve before any operation. They differ on starting from seat and standby (C, on the ADR's per-territory pairing and the sender's pointer) or not inferring from seats (X), and on when HNR joins. |
| 5 | Differ | Add | **Partly settled.** Both reject a skeleton with no return publication; the model adds a secondary publication step. Whether it runs on map approval (C) or after a separate default-off grant (X) is **open: HOST-SECONDARY-PUBLISH**. |
| 6 | Add | Add | **Settled.** `mgit sync` is the candidate recipe (C); it pushes by default (line 3177), so `tools-mgit` certifies a version with explicit publish and pull-only modes (C28, X28). Replace unattended "inspect every unpublished ancestor" with objective live-work tests (C) and push exactly the checked tip (X's range race). |
| 7 | Differ | Agree | **Settled in wording.** Pulling grants nothing, and fetch, branch update and publication are separate effects (X). "Each actual effect needs its own grant" read as per occurrence would forbid recurrence; the [Git authority standard](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/.agents/skills/ki-git/references/standards-git.md#commit-publication-and-integration-authority>), cited by X itself under claim 16, permits explicit standing authority (C). When that grant is given stays with HOST-SECONDARY-PUBLISH. |
| 8 | Differ | Agree | **Settled.** Ownership is the host's Rig thread, from Kris's words (C); the executor mechanism stays open (both), with descriptive names (both). |
| 9 | Agree | Agree | Agreed. |
| 10 | Add | Differ | **Open: HOST-CADENCE.** C: Kris's `:00`/`:05` on both hosts, since each territory has one primary and the slots touch disjoint sets. X: measure duration and wake behaviour before fixing any interval. Both accept an attended run before activation. |
| 11 | Agree | Agree | Agreed; it argues for a return publication step. |
| 12 | Differ | Differ | **Open: HOST-SECONDARY-PUBLISH.** Both reject attended-only return publication as failing the two-host requirement; C would publish under the map approval, X would prepare a default-off capability under a separate grant. |
| 13 | Agree | Agree | Agreed. |
| 14 | Differ | Differ | **Direction settled, slot open: HOST-READBACK.** Both prefer a prompt pull-only read-back over next-hour, on Kris's "resync as well in short order"; the slot follows HOST-CADENCE (C `:10` on each primary, X `:10`/`:12`). |
| 15 | Agree | Agree | Agreed. Nothing is exclusive, so there is nothing to take over (C). |
| 16 | Differ | Differ | **Settled.** Compatible replacements: revalidate still-effective standing authority rather than demand fresh authority (X, Git authority standard); the next occurrence is the catch-up, with no backlog replay (both); reobserve an uncertain push before any publication (X). |
| 17 | Agree | Add | **Settled.** Expected membership comes from the map with host, repository, branch, phase, occurrence and map revision (X); a tally the host thread reads is enough to start, and observation never gates execution (both). |
| 18 | Agree | Agree | Agreed. |
| 19 | Agree | Agree | Agreed. |
| 20 | Differ | Agree | **Settled.** HOST-SYNC grants no scheduler authority (both). The rollout lines name the syncs the design is meant to supersede (Terra's HNR sync, SYNC-EVENING, SOL-SYNC) so each Rig owner can propose their retirement once the replacement runs (C); any interim restart stays with Sol's own HOST-SYNC query, which Rig owns. |
| 21 | Agree | Agree | Agreed. Each line also names the approved map and the stop word (C). |
| 22 | Differ | Add | **Settled, weight reduced.** Both want an attended run before recurrence. On the evidence of SOL-SYNC's 19 hours and SYNC-EVENING under Kris's instruction (C), use one attended run per host of the exact command over the approved map, with staged tests only for dirty refusal and divergence, which are cheap. Other cases are observed in operation. A dated pilot grant carries a stop word and a proportionate restore path, unloading the job (X). This is not a connection-critical change. |
| 23 | Differ | Differ | **Settled.** The brief's proposal does not meet the requirement (both). The merged model does if HOST-SECONDARY-PUBLISH supplies a return path, and it is lighter than the brief. |

**Missing claims, merged.**

| New | From | Merged position |
| --- | --- | --- |
| 24 Divergence | C24, X25 | The host's Rig thread resolves diverged repositories through a bounded resolve run; escalation after two hours with no new local commits. No new merge authority. |
| 25 Interim | C25 | Until the rollout runs, an attended `mgit sync` on request (SYNC-NOW) stays available. |
| 26 Missed occurrences | C26, X27 | A missed or late slot, including sleep, is skipped; finite duration bound, overlap refusal, no backlog replay. |
| 27 Branch scope | C27, X3 | Default tracking branch only unless the map names more. |
| 28 Recipe certification | C28, X28 | `tools-mgit` identifies a version with explicit publish and pull-only modes, Rig the invocation; both hosts validate the same map revision. `tools-mgit` hears that this design depends on it. |
| 29 Chezmoi source | C29 | The chezmoi source repository is a named map member; `chezmoi apply` stays out of the unattended pass. |
| 30 Tidy | C30 | Work-package tidy stays out of the recurring pass. |
| 31 Convergence | X24 | The attended run shows a primary-origin commit reaching the secondary and, once granted, a secondary-origin commit reaching the primary, with times and tips recorded. |
| 32 Publication guard | X26 | Linked worktrees covered through their common Git directory; remote non-fast-forward rejection is sufficient against overwriting, with no distributed lease. |
| 33 Paperwork bound | X29 | No per-occurrence records, duplicated grants or forwarding system; evidence returns before coverage widens. |

## Rollout plan

1. Kris answers the four decisions below.
2. One line each to `personal.reg.rig-terra` and `personal.reg.rig-sol`, as HOST-SYNC-DESIGN set, requesting a plan, not installation: the merged model, Kris's answers, the stop word, the syncs to be superseded, and the dependency on `tools-mgit` (claim 28). No record is created in their queues.
3. Rig and chezmoi return the proposed map and invocation for Kris's approval; `tools-mgit` certifies the recipe version.
4. One attended run per host of the exact command over the approved map, with the dirty-refusal and divergence tests, measuring phase duration.
5. Activation under a dated pilot grant with a stop word; HNR joins at the point the approved plan names; Observatory adds coverage observation independently.

## Decisions

### HOST-CADENCE - Which cadence Rig prepares

**Options:** a) hourly `:00` primary, `:05` secondary, read-back shortly after, on both hosts, confirmed by each host's attended run before activation; b) leave cadence unchosen until attended passes measure it; c) the brief's staggered `:00`/`:02`/`:05`/`:07`. **Recommendation:** a), medium: Kris's own shape and the disjoint per-slot sets support it, but durations are unmeasured and the reviewers split.

### HOST-COVERAGE - Who prepares the map, from what start

**Options:** a) Rig and chezmoi propose a territory-grain map starting from seat host as primary and standby as secondary, active-active territories primary on the hub, with exclusions, resolved membership and the point HNR joins, for Kris's approval; first attended run on one non-HNR, non-deploying repository; b) the same, but without the seats starting point and enumerated per repository and phase; c) Kris supplies the map directly. **Recommendation:** a), medium: Kris's per-territory words, the ADR's seat and standby pairing and the sender's pointer support it, but seats carry a different meaning and the reviewers differ.

### HOST-SECONDARY-PUBLISH - How secondary-origin work reaches Git

**Options:** a) prepare secondary publication in the same recipe, default off, switched on only by Kris's explicit standing grant naming territories, which Kris may give in the same answer as the map approval; b) keep the secondary pull-only and leave return publication to attended work. **Recommendation:** a), high: both reviews independently reject pull-only as failing Kris's requirement, and preparing a default-off step grants nothing.

### HOST-READBACK - When primaries consume returned work

**Options:** a) a pull-only read-back on each primary shortly after the secondary phase, its slot following HOST-CADENCE, keeping next-occurrence recovery; b) next-hour read-back only. **Recommendation:** a), medium: both design reviews prefer it on Kris's "in short order", but an earlier blind query review backed b) and the slot depends on cadence.

## Changes after review

- Observatory E/A labels corrected; descriptive executor names used (both).
- Fact base widened with SYNC-EVENING, SOL-SYNC, SYNC-NOW and Sol's open HOST-SYNC query (C).
- `mgit sync` named as the candidate recipe, with its default push and a certification step (C, X).
- Map moved to territory grain with exclusions and recorded membership (C, X).
- Secondary publication added as a default-off step (both, from claims 5, 11, 12 and 23).
- Read-back moved from next hour to a prompt pull-only phase (both, claim 14).
- Standing publication authority allowed in place of per-effect grants (C, X).
- Named divergence resolver added (C24, X25).
- Absence simplified to skip-and-next-occurrence with revalidation (both, claim 16).
- Pilot reduced to one attended run per host with targeted tests and a dated grant (C, X).
- Supersession of the earlier syncs named in the rollout lines (C).
- Missing claims 24 to 33 added.
