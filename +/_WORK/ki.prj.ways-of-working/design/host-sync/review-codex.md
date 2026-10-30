# Host synchronisation: independent review (Codex)

**Reviewer:** GPT-6.1 Sol (Codex) · **Date:** 30 October 2026 · **Status:** independent design review, not adoption

The proposal has sound safety boundaries but does not yet meet the whole requirement. It automates outward primary publication while leaving secondary-origin publication to attended work, and postpones read-back until the next hour despite the request for a resync in short order. Prepare a separately authorised secondary-publication capability and a prompt, bounded read-back; establish the actual offsets through a small attended pilot.

## Findings

### HOST-FACTS - Source verification and limits

**Goal:** Verify each established fact and quotation in the [common brief](<brief.md>), as Kris requested through HOST-REVIEW on 30 October 2026.

**Scope:** The brief, its preserved received input and historical source, relevant decisions, seat declaration, Rig package identities, state diagram and cited Observatory brief/reviews. No queries file, preparation or merged report, other HOST-SYNC review, HNR source, scheduler, installed binding, remote host or service was read.

**As of:** 30 October 2026, 06:21 GMT; local source verification only, before publication checks.

- **Owner's proposal, all six quoted passages:** Confirmed by exact substring comparison against [the received input](<../host-sync-and-reply-trades.md#full-received-source>). Every quoted passage there concerning HOST-SYNC also occurs in the historical messages file at Principal `3b512680dd0f756227ae37b5d8408401b6555841`; that complete historical file's SHA-256 matches the input's recorded checksum. This verifies transmitted wording, not an independently recovered recording of Kris's speech.
- **Decisions, all four quoted passages:** HOST-SYNC-DESIGN, RECOMMENDED-ALL, HOST-REVIEW and REVIEW-INDEPENDENCE match the [decisions log](<../../decisions.md>) exactly. LANDSCAPE is correctly labelled the log's summary, not verbatim speech; the log records the priority and cross-host levelling request. The log's read-back supports proceeding with design, not choosing the four still-open options.
- **Stopped HNR sync:** Confirmed only as dated sender evidence in the [received input](<../host-sync-and-reply-trades.md#full-received-source>): stopped at 13:52 GMT on 28 October. Its present state and whether anything replaced it remain unknown; no HNR inspection was performed.
- **Seats and host binding:** Confirmed against [ADR-KI-PRINCIPAL-007](<../../../../../Admin/Governance/Decisions/ADR-KI-PRINCIPAL-007-territory-seats-on-hosts.md>) and a parsed [seats declaration](</Users/krisbrown/.local/share/chezmoi/.chezmoidata/seats.yaml>). Terra/home has humans-not-robots, knowledge-islands, personal and legal; Sol/hub has valle-armonia, sacred-inquiry, techmedix, equal-remedy, knowledge-islands, personal and legal; the tip is hub. The current declaration is byte-identical to chezmoi `38be5a1`, has no sync-primary/secondary field, and describes coordination liveness. No sync takeover follows from standby fallback.
- **Rig destinations:** Confirmed by the existing [personal.reg.rig-terra work file](</Users/krisbrown/workspaces/personal/personal-principal/+/_WORK/personal.reg.rig-terra/work.md>), [personal.reg.rig-sol work file](</Users/krisbrown/workspaces/personal/personal-principal/+/_WORK/personal.reg.rig-sol/work.md>) and their sibling incoming queue paths. The older spelling in HOST-SYNC-REPLY is preserved sender text, not the current destination.
- **Observatory comparison:** The [cited brief](<../../../ki.prj.observatory/design/observatory-sync-brief.md>) defines alternatives A-D; the [authority review](<../../../ki.prj.observatory/design/observatory-sync-review-authority.md>) adds E as a direct per-host Rig resource. Thus the HOST-SYNC brief's E-for-thread/A-for-direct labels are not established by those permitted sources; a later merged report may relabel them, but was excluded from this independent review. Use descriptive option names and identify the version supplying any letters. The [HOST-RESPONSIBILITY queue line](<../../../ki.prj.observatory/messages.md>) confirms Observatory's observation remit and dotfile placement, without choosing execution ownership.
- **State machine and roles:** Confirmed by the [diagram](<../work-state-machine.mmd>) and ROLES-ORCHESTRATOR, ROLES-EITHER and WORKING-EXIT in the [decisions log](<../../decisions.md>). The diagram represents End (work) as Working's final pseudo-state; the explicit name is in WORKING-EXIT. Working, its four internal states, Bootstrap, stop/resume/finish, At rest reasons and actor-neutral roles agree. This is agreed design, not proof of deployed encoding.
- **Other inputs and baseline:** The [request/reply section](<../host-sync-and-reply-trades.md#requestreply-trades>) confirms the distinct request/reply problem and holds PACKAGE-FORWARDING separately. Principal `8dd0f118` resolves and precedes the committed common brief; that establishes an available preparation baseline, not runtime parity or evidence that no external inspection occurred during its preparation.

These checks raise HOST-CADENCE, HOST-COVERAGE, HOST-SECONDARY-PUBLISH and HOST-READBACK below. The Observatory letter ambiguity needs an editorial correction, not a new owner decision.

### HOST-CLAIMS - Verdict on claims 1 to 23

**Goal:** Agree, differ from or extend every numbered proposal claim in the [common brief](<brief.md#reflection>).

**Scope:** Design correctness and proportionality against the verified owner requirement; earlier approvals are evidence, not a reason to agree. The existing executor is not certified by this review.

**As of:** 30 October 2026, 06:21 GMT.

1. **Agree.** A dotfiles-owned declaration matches the explicit setup preference in [HOST-RESPONSIBILITY](<../../../ki.prj.observatory/messages.md>); Rig and chezmoi are appropriate preparation owners.
2. **Agree.** Seats govern coordination, and neither their fallback nor this sync map creates an exclusive Git writer; [ADR-KI-PRINCIPAL-007](<../../../../../Admin/Governance/Decisions/ADR-KI-PRINCIPAL-007-territory-seats-on-hosts.md>) supports that distinction.
3. **Add.** Enumerate repository, branch/upstream, host, phase and exclusions, but reference the existing grant and veto sources rather than creating a second publication-authority register in dotfiles.
4. **Agree.** Existing host inventories and seats cannot supply approval; a jointly proposed, owner-approved non-HNR, non-deploying pilot keeps the first decision small.
5. **Add.** Primary publication then secondary consumption is a useful skeleton, but it needs an explicit return-publication branch for opted-in repositories if the recurring process is to circulate secondary-origin work.
6. **Add.** Revalidate branch, upstream, reviewed commit range and authority inside exclusion covering every participating manual/scheduled writer, and publish only the reviewed tip. A preflight outside that boundary can approve one range and push a later unreviewed range; the [Observatory reliability review](<../../../ki.prj.observatory/design/observatory-sync-review-reliability.md>) identifies this race.
7. **Agree.** Fetching, changing local branch state and publishing are separate actual effects; eligibility for one does not grant the others.
8. **Agree.** Keep executor selection open in this design, using descriptive names rather than ambiguous E/A labels; neither an AI thread nor a deterministic resource inherits the other's grants.
9. **Agree.** Offsets reduce likely overlap but prove nothing about exclusion or completion; bounded reobservation and an explicit stale/missing result are appropriate.
10. **Differ.** The sources establish hourly/five-minute intent, not measured durations or the additional two-minute host offset; the [reliability review](<../../../ki.prj.observatory/design/observatory-sync-review-reliability.md>) specifically warns about slow runs and simultaneous wake-up. Replace the fixed preparation choice with attended measurement first, retaining the hourly pattern as a candidate rather than a settled cadence.
11. **Agree.** A fetch or fast-forward on the secondary transfers nothing back to the remote; unpublished secondary commits remain invisible to the primary regardless of read-back frequency.
12. **Differ.** Attended-only secondary publication is a safe temporary restriction but leaves part of the [owner's regular two-host requirement](<../host-sync-and-reply-trades.md#full-received-source>) outside the recurring solution. Replace it with preparation of a distinct, default-off secondary-publication capability requiring explicit repository eligibility, ancestor review and authority at the effect; until authorised, retain pull-only operation and label its coverage partial.
13. **Agree.** Return-publication authority, read-back timing and package-message forwarding are distinct decisions; none should implicitly settle another.
14. **Differ.** Next-hour read-back is not supported as the preferred answer to the [request for resync in short order](<../host-sync-and-reply-trades.md#full-received-source>). Replace it with a bounded pull-only read-back after the return-publication opportunity, provisionally :10/:12 if the pilot supports that cadence, plus next-occurrence reobservation of late or missing work.
15. **Agree.** No automatic takeover is the smallest safe absence policy; withholding an absent host's work is preferable to inventing distributed election or failover.
16. **Differ.** The requirement for fresh authority on every return is unnecessarily stronger than checking an existing valid standing grant; the [Git authority standard](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/.agents/skills/ki-git/references/standards-git.md#commit-publication-and-integration-authority>) permits standing publication authority where explicitly granted. Replace that phrase with revalidation of still-effective authority and current sources; keep uncertain-effect reconciliation and a default of no retrospective replay until recovery policy is approved.
17. **Add.** Expected membership must come from the approved map, independently of observed report files, with host, repository, branch, phase, occurrence and map/grant revision. Ask Observatory to expose coverage without making its own liveness a condition of sync execution.
18. **Agree.** Synchronised Git files do not retire executors, home host-bound evidence or receive a handoff; the [diagram's portability condition](<../work-state-machine.mmd>) is stronger than a successful Git pass.
19. **Agree.** Git may transport queue-file contents but that supplies no receipt, ownership transfer or release of a wait; preserve the existing package semantics.
20. **Agree.** Designing a replacement neither changes the stopped HNR job nor grants any scheduler or repository operation.
21. **Agree.** After decisions, send one planning message to each actual Rig queue; receiving owners retain planning and rollout ownership, and this review sends neither message.
22. **Add.** Use a bounded, dated pilot grant with explicit stop/restore conditions, and test publication acknowledgement loss as well as interruption. Keep grant expiry for the pilot distinct from a demand that every future standing permission expire, and require restore machinery proportionate to the actual effect rather than a new host-wide service for read-only prediction.
23. **Differ.** Claims 11-12 leave unpublished secondary commits uncovered, while claim 14 can delay return visibility until the next hour; [the owner's requirement](<../host-sync-and-reply-trades.md#full-received-source>) asks for regular two-host sync and prompt resync. Replace the sufficiency claim with: this is a safe partial proposal pending return-publication, promptness and failure-recovery decisions, to be judged against a small end-to-end pilot.

The Differ verdicts raise HOST-CADENCE, HOST-SECONDARY-PUBLISH and HOST-READBACK; the authority wording correction in claim 16 can be made without another permission request.

### HOST-MISSING - Conditions needed to make the proposal testable

**Goal:** Identify necessary claims absent from the [common brief](<brief.md>), numbering from 24 as requested.

**Scope:** Minimal correctness and acceptance criteria; no transport, schema, global lock service, executor installation or new authority is selected.

**As of:** 30 October 2026, 06:21 GMT.

24. **Define convergence and delay.** Name the pilot repository and tracked branch, expected authorised commits and an agreed visibility target. Demonstrate a primary-origin commit reaching the secondary and an eligible secondary-origin commit reaching the primary, with the observation time and published tip recorded; report uncovered work explicitly.
25. **Define the concurrent-commit boundary.** If both hosts commit independently from the same base, fast-forward-only integration cannot combine their different histories, even when edits touch different files. Stop that repository and return it to its named owner for separately authorised reconciliation; show the divergence honestly rather than promise that cadence or another pull will resolve it. This requires no new merge authority.
26. **Protect the actual publication.** Cover linked worktrees through their common Git directory, checkout/index writes through their checkout, and all participating manual entry points. Bind publication to the reviewed commit and remote destination, with a bounded exclusion policy; for independent authorised writers, ordinary remote non-fast-forward rejection is sufficient safety against overwriting and does not itself require a distributed lease.
27. **Define skipped-occurrence recovery before recurrence.** Adopt a finite duration bound, overlap refusal, acceptable lateness and a rule for sleep/wake and missed slots; the simplest starting policy is no backlog replay and one fresh bounded pass. Reobserve an uncertain prior push before considering another publication, without automatically retrying it.
28. **Separate intent, implementation and deployment proof.** Before a pilot, the Tools owner must identify a recipe/version that actually supports phase-specific pull-only and opt-in publication, Rig must identify the invocation, and both hosts must validate the same approved map revision. The [local mgit implementation](</Users/krisbrown/workspaces/knowledge-islands/tools-mgit/bin/mgit:3022>) still includes an ordinary push branch in generic sync; a design declaration cannot turn that command into a certified pull-only executor.
29. **Bound the decision and rollout paperwork.** Keep the shared method, approved map and existing repository grants as the sources of truth; do not introduce per-occurrence roadmap records, duplicated grants or a new forwarding system. Advance one pilot repository through the staged checks, then return evidence and the minimum remaining choices before widening coverage.

These additions qualify the four choices below; no additional infrastructure decision is required merely to record the conditions.

## Queries

### HOST-CADENCE - Measure before fixing the offsets

**Context:** The owner proposed an hourly primary phase and a secondary phase five minutes later. No verified source establishes normal duration, two-minute cross-host spacing or what happens after sleep.

**Query:** Which cadence should Rig prepare, without activation?

**Options:**

a) (recommended, confidence medium - the hourly intent is clear, but duration and wake behaviour are unmeasured) Choose the brief's option b: prepare attended passes and measure them first; retain :00/:02/:05/:07, with possible :10/:12 read-back, as the candidate to validate, then return a bounded recurring plan promptly.

b) Choose the brief's option a now: prepare those exact hourly phases, keeping activation conditional on pilot evidence and exclusion.

### HOST-COVERAGE - Let the receiving owners propose the map

**Context:** The seats declaration contains coordination placement, not sync responsibility. Both Rig packages own keeping their hosts level, and chezmoi owns the shared setup source.

**Query:** Who should prepare the map and pilot nomination?

**Options:**

a) (recommended, confidence high - the owners can inspect actual applicability while Kris retains approval) Choose the brief's option a: Rig and chezmoi propose the map, explicit repository/branch/phase eligibility and exclusions, grant references and one jointly nominated non-HNR, non-deploying pilot; return it before configuration or operation.

b) Choose the brief's option b: Kris supplies the map and pilot directly, and the receiving owners verify them.

### HOST-SECONDARY-PUBLISH - Prepare the return path explicitly

**Context:** Pull-only secondary consumption cannot return unpublished secondary commits. Leaving all return publication to attended work is safe as an interim boundary but cannot demonstrate the complete recurring requirement.

**Query:** Should the design prepare a separately opted-in secondary-publication capability?

**Options:**

a) (recommended, confidence high - this closes a demonstrated coverage gap without granting any effect) Choose the brief's option b: Rig and the Git-tool owner prepare that distinct capability, default off, with repository grants/vetoes, reviewed ancestors and authority revalidated at publication; retain pull-only operation until separately authorised.

b) Choose the brief's option a: rely on separately authorised attended publication and explicitly accept that recurring coverage excludes unpublished secondary-origin commits.

### HOST-READBACK - Prefer a prompt bounded read-back

**Context:** Under next-hour read-back, work published at :05 can wait about 55 minutes to be consumed on Terra; Sol's :07-to-next-:02 interval is also about 55 minutes. That is eventual visibility, without evidence that it meets the requested prompt resync.

**Query:** Should Rig prepare a short pull-only read-back after the return-publication opportunity?

**Options:**

a) (recommended, confidence medium - prompt read-back fits the words, but exact slots depend on pilot duration and publication availability) Choose the brief's option b in principle: prepare bounded read-back, provisionally Terra :10 and Sol :12 if the hourly candidate proves suitable; retain next-occurrence recovery, record missed/late phases and promise neither acknowledgement nor immediate convergence.

b) Choose the brief's option a: accept next-hour read-back, explicitly accepting the approximate 55-minute nominal delay after an on-time secondary publication.
