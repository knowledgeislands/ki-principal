# ki.prj.ways-of-working queries

## Open

### WORKER-WAIT - Who holds authorised work before a worker does

since 2026-10-29 · from run/sol-state-machine-readiness; refines the parked STATE-MACHINE-DECISIONS, of which it is the sole unresolved semantic choice.

**Context:** The agreed role model distinguishes the orchestrator from a worker. The current coordination contract includes an orchestrator mid-turn and authorised work waiting for worker capacity in With worker; the newer source says a worker run holds that state. No worker is in flight in either case. The agreed diagram does not settle that distinction. This choice blocks only those two cases, not the agreed shape, portable stop, report layout or compatible-reader planning. The run settled REST-PORTABLE, FINISH-FROM, REST-NAMES and ROLE-WORDS and found WAIT-RESUME and WORK-REENTRY to be factual compatibility work, in the [state-machine rollout plan](design/state-machine-rollout-plan.md).

**Query:** Should With worker include these cases as worker-side ownership with an explicit queued/orchestrating description, or require an actual worker role holder before entering it?

**Blind review (30 October, Codex, high effort):** differs, prefers b) at medium confidence: an explicit holder keeps ownership truthful, and an orchestrator mid-turn does not by itself establish assignment.

**Options:**

a) (recommended, confidence medium - preserves the current capacity rule and agreed diagram while keeping run status truthful) Include both cases as worker-side ownership; say explicitly that this need not mean a run is in flight and show queued/orchestrating work accurately. Align the narrower source sentence and holder projections with that reading.

b) Require an actual worker role holder; qualify the dispatch/entry procedure and who holds authorised work before dispatch before enabling these cases, without inventing a state or redrawing the agreed machine in this rollout.

### HOST-REVIEW - Supply the missing common-brief review packet

since 2026-10-29 · from run/sol-host-sync-design; refines the parked HOST-SYNC by naming the gate its design qualification is blocked on.

**Context:** The saved execution task claims an existing brief and independent reviews. The actual pair reviews Observatory executor ownership. The HOST-SYNC received note has no numbered reflection, and neither review assesses this report's complete mapping, sequence, secondary publication and read-back proposal. The design-loop standard requires at least two independent reviews of the brief. This run was explicitly forbidden to start agents. The preparation is in the [HOST-SYNC preparation report](design/host-sync-report.md).

**Query:** Will the supervising coordinator arrange the missing HOST-SYNC brief and two independent reviews before treating this recommendation as qualified?

**Options:**

a) (recommended, confidence high - satisfies the actual gate while retaining all useful preparation) Have the supervising coordinator commission the common brief and two independent read-only reviews, on different models or runtimes, then reconcile this report before adoption. Ask each to mark Agree, Differ or Add against every numbered claim, verify owner wording and examine sequence, publication, absence and state-machine boundaries.

b) Keep this preparation report parked; do not adopt or roll out HOST-SYNC until that review packet is available.

### HOST-CADENCE - Choose the proposed offsets for later planning

since 2026-10-29 · from run/sol-host-sync-design; refines the parked HOST-SYNC on its offset question.

**Context:** The owner requested regular equivalent work with offsets and gave an hour/five-minute example. No actual cadence, host offset or zone is adopted. Independent reviews establish that offsets cannot prevent overlap or certify completion. Rig and chezmoi would own any later realisation.

**Query:** Which cadence should the receiving owners prepare, without activating it?

**Blind review (30 October, Codex, high effort):** differs, prefers b) at medium confidence: measured phase duration and exclusion behaviour should come before a fixed interval.

**Options:**

a) (recommended, confidence medium - follows the hourly/five-minute example and gives the hosts distinct phase offsets) Prepare hourly GMT/UTC phases: Terra primary :00 and secondary consumption :05; Sol primary :02 and secondary consumption :07, subject to explicit exclusion and pilot evidence.

b) Keep cadence unchosen and prepare attended passes only until the pilot establishes phase duration and a suitable interval.

### HOST-COVERAGE - Prepare an explicit responsibility map

since 2026-10-29 · from run/sol-host-sync-design; refines the parked HOST-SYNC on which host is primary for what.

**Context:** Seats encode coordination landing and existing active-active roles, not sync-primary ownership. There is no evidenced per-territory sync mapping or per-repository publication eligibility set to adopt. Neither host's physical checkout inventory grants it writes. Rig and chezmoi own preparation of the requested dotfiles declaration.

**Query:** Should the two Rig owners prepare the explicit mapping for a separate bounded review, or will Kris provide its entries directly?

**Options:**

a) (recommended, confidence high - preserves owner control without inventing mappings from seats) Ask Rig and chezmoi to propose the per-territory primary/secondary map, enumerate repository and phase eligibility plus exclusions, and return it for approval before configuration or operations. Start with one jointly nominated non-HNR non-deploying pilot repository.

b) Kris supplies the mapping and pilot repository directly; the receiving owners then verify eligibility and prepare its bounded plan.

### HOST-SECONDARY-PUBLISH - Bound secondary-origin publication

since 2026-10-29 · from run/sol-host-sync-design; refines the parked HOST-SYNC on its publication sequence.

**Context:** The source wants the primary to read secondary updates but does not choose how those updates reach Git. Pulling primary work on a secondary cannot publish secondary-origin commits. Scheduling read-back alone therefore cannot fulfil that requirement. Existing per-repository grants still apply.

**Query:** Should secondary-origin changes continue to be published only through separately authorised attended work, or should Rig prepare a recurring secondary-publication phase for later review?

**Blind review (30 October, Codex, high effort):** differs, prefers b) at medium confidence: a separately reviewed opt-in publication phase closes the round trip; activation stays a separate decision.

**Options:**

a) (recommended, confidence medium - supplies a valid return path without adding unattended publication authority) Keep secondary consumption pull-only in the recurring proposal; secondary-origin changes reach Git through separately authorised attended work. Read-back consumes only what is actually published and reports outstanding unpublished work as outside its coverage.

b) Ask Rig and the Git-tool owner to prepare a distinct opt-in secondary-publication phase with repository eligibility and authority-at-effect checks; do not activate it or assume a grant from HOST-SYNC.

### HOST-READBACK - Choose when primaries check published return work

since 2026-10-29 · from run/sol-host-sync-design; refines the parked HOST-SYNC on how primary hosts consume secondary updates.

**Context:** Kris explicitly left primary read-back to be decided and suggested a resync in short order. This is independent of secondary publication, message forwarding and request/reply trades. No timing guarantee can cover unpublished work or an absent host.

**Query:** Should primary read-back wait for its next hourly occurrence, or should the receiving owners prepare an additional short-delay phase?

**Blind review (30 October, Codex, high effort):** agrees with a); confidence lifted to high, its hourly interval conditional on HOST-CADENCE.

**Options:**

a) (recommended, confidence high - reviewed; simplest bounded start while coverage and duration are unproven) Read published secondary-origin updates at the start of the primary's next authorised hourly occurrence, before evaluating eligible primary publication. State the resulting delay explicitly; make no immediate-convergence promise.

b) Prepare an extra pull-only read-back at Terra :10 and Sol :12, separately bounded and guarded; retain next-occurrence recovery if a prior phase is late or absent. This adds promptness, not publication authority or an acknowledgement guarantee.

### PUBLIC-REPORT-AUDIENCE - Choose the response scope

since 2026-10-29 · from run/sol-private-report-assessment; the parked TERRA-LOCAL-REPORTS and PROTECTED-PUBLICATION refer to this audience question.

**Context:** Exact selected historical content remains reachable in locally verified published history, and one protected version remains current. Readership and indexing are unknown. Assessment approval did not authorise a remedy. The run's private evidence and response options are at `/Users/krisbrown/.local/state/ki/agents/ways-sol-resume-20261029/sol-private-report-assessment.private/`, which stays private and outside the repository.

**Query:** Should a separately bounded private response design follow, or should the owner explicitly retain the present publication posture?

**Options:**

a) (recommended, confidence high - resolves intended audience before selecting a remedy) Commission a private exact-version response design using the evidence locator above. Specify permitted audience and desired current/historical disposition; return a separate execution proposal with residual exposure stated. This authorises planning only, with no sanitisation, access change, history action, credential action or external contact.

b) Explicitly accept leaving current and historical publication unchanged, retaining the private evidence and unknown-readership qualification. This does not clear further public reuse.

c) Defer the response decision, naming its owner and return point; preserve evidence unchanged.

### PUBLIC-REPORT-RECOVERY - Decide private evidence durability

since 2026-10-29 · from run/sol-private-report-assessment; related to the parked TERRA-RECOVERY.

**Context:** Local recovery has been verified, but private off-machine recovery has not. The private evidence directory must remain outside the launcher's repository report home; no relevant source-store declaration was established for this operation.

**Query:** Should a later bounded task preserve the existing private recovery/provenance and this assessment at an explicitly approved private destination?

**Options:**

a) (recommended, confidence high - addresses the proved local-only gap without inventing a binding) Identify an approved private destination, or explicitly approve one, then separately authorise exact-manifest backup and restore verification with originals preserved. No transfer is authorised now.

b) Retain only the existing local copies and explicitly acknowledge the private recovery limitation; preserve this runtime evidence and its referenced archives.

### AMEND-RACE - Guard amends in a shared checkout

since 2026-10-30 · from a message line received by the coordinator.

**Context:** In the shared hnr-principal checkout a run amended `HEAD` after another package's explicit-path commit had landed, so `a1d61be4` became `21f4f02b` under the amending run's subject and trailer. The tree is identical and no content was lost, but the other package's commit subject and attribution were replaced. The `ki-git` standard already says to record and re-check `HEAD` before staging, to serialise the write window that advances shared `HEAD`, to rebuild only a commit "this session has not pushed" when it captured unrelated work, and to "never rewrite another actor's commit or a published commit"; it has no explicit check that `HEAD` is still the session's own commit before an amend. Its isolated-index procedure already uses that pattern: record the parent before committing and stop if `HEAD` has moved. The proposed rule would change `ki-git` in the KI Agentic Harness, which owns the change; no skill was changed here.

**Query:** Should `ki-git` allow an amend in a shared checkout only after confirming `HEAD` is the session's own unpublished commit, or forbid amending there altogether?

**Blind review (30 October, Codex, high effort):** agrees with a) at high confidence; confidence lifted to high.

**Options:**

a) (recommended, confidence high - reviewed; makes the existing never-rewrite-another's-commit rule mechanical with the parent-check pattern the standard already uses, and keeps its own-unpushed-commit repair path; a check outside the serialised window would still race) Amend in a shared checkout only inside the serialised write window and only after confirming `HEAD` equals the commit this session itself recorded and has not pushed; otherwise make a new commit. Send it to the KI Agentic Harness as a message line for `ki-git`.

b) Never amend in a shared checkout: correct with a follow-up commit, and rewrite the standard's own-unpushed-commit repair path to match. Send it to the KI Agentic Harness as a message line for `ki-git`.

c) Change no rule: the existing standard already forbids rewriting another actor's commit, so log the incident as a lapse in Mistakes and Lessons only.

### ORCH-NAME - What to call the coordination skill, the dispatch skills and the command

since 2026-10-30 · from run/landscape · merged in [landscape-report](design/landscape-report.md)

**Context:** The brief proposed `ki-coordination` for working the package with Kris and `ki-orchestration` for the portable half of `ki-delegation`, with Orca and Paperclip adapters and `ki agent` possibly renamed `ki orchestrate`. On 29 October Kris named the thread agent "the orchestrator of the state machine", the role `ki-coordination` governs; Orca, Oz and Paperclip all use "orchestration" for driving agents. KI-AGENTS-NAME, 17 October, says: "Keep "agents" ... nothing is renamed." `ki-delegation` already calls itself runtime-neutral. Both design reviews recommend keeping the names, at medium confidence, as a choice of words. They correct the design's reason: ROLES-ORCHESTRATOR assigns a role and does not reserve the word, and the Claude review notes that the role word, if anything, favours renaming `ki-coordination` itself, option c); the reason to keep it is the cost of renaming the output style, a 217 KB standard and every live package mid-rollout. Moving `decide`, `reconcile`, `home` and `prompts` under `ki work` is no longer part of this query; the four are not one kind, and their separation is a design step under AGENT-HOME. The remaining drift, a `ki-coordinator` style for a role now called orchestrator, is settled by one line in the Work Process note.

**Query:** Which names should the coordination skill, the dispatch contract, its adapters and the command take?

**Blind review (30 October, Codex, high effort; applies to the earlier wording of a), which also moved the four commands under `ki work`):** agrees with a); confidence lifted to high.

**Options:**

a) (recommended, confidence high - reviewed, and both design reviews choose the same names; the keep rests on rollout cost, and the words are Kris's to hear) Keep `ki-coordination`. Keep `ki-delegation`, slimmed, as the portable contract, with adapters `ki-delegation-orca` and `ki-delegation-paperclip`, the second renamed from `ki-agent-coordination-paperclip`, and no adapter for `ki agent`. Keep the name `ki agent`. Say in the Work Process note that the orchestrator role is exercised under `ki-coordination`.

b) The brief's family: `ki-orchestration`, `ki-orchestration-orca` and `ki-orchestration-paperclip` for dispatch, with `ki-coordination` unchanged.

c) Rename `ki-coordination` to `ki-orchestration` to match the role word, and use the `ki-delegation` family from a) for dispatch.

### ORCA-REACH - Where Orca may run

since 2026-10-30 · from run/landscape · merged in [landscape-report](design/landscape-report.md)

**Context:** On sol, Orca 1.4.244's local help shows it can run without a window (`orca serve --supervise`), place workers on paired servers with `worker-start --on`, and run Codex. The vendor's documentation marks server mode as beta, for LAN or tailnet use only; neither design review could verify that locally, no server is paired and no remote run has been tested. The Techne Programme Focus allows agents on sol and `vega` only "in sessions the binding owner opens, with no unattended or scheduled agents", and keeps "the execution fabric" as an idea. Both design reviews recommend a) at high confidence, but differ from the design on `vega`: the focus names no sole launcher and does not bar Orca used inside owner-opened sessions there, so keeping `ki agent` alone on `vega` is a deployment choice rather than a policy bar. An always-on supervised Orca server accepting remote workers is closer to the execution fabric and would go through the Enactment Process.

**Query:** Where should Orca be used as a launcher?

**Options:**

a) (recommended, confidence high - both design reviews choose it; it is reversible and rests on local evidence) Use Orca only on attended Macs, for packages that opt in by a logged decision. Keep `ki agent` as the only launcher on `vega`, by choice. Any Orca use on `vega` comes back as its own decision with remote-delivery proof, and an always-on Orca server there goes through the Enactment Process.

b) Pair `vega` as an Orca environment now and place remote workers on it from sol, inside owner-opened sessions and agreed remote-delivery bounds; no operational proof exists yet.

### AGENT-HOME - Where `ki agent` lives and how its work-model commands separate

since 2026-10-30 · from run/landscape · merged in [landscape-report](design/landscape-report.md)

**Context:** `ki agent` combines dispatch (launch, queue, wait, status, stop and so on) with four commands that touch the work model. Both design reviews show the four are not one kind: `decide` and `reconcile` write the decisions log, `home` binds a run to its work home and belongs with the run, and `prompts` prints the openers. `ki work` describes itself as "read the work model", so moving write commands under it changes its contract. The Techne focus keeps "the execution fabric" as an idea until Kris takes it up through the Enactment Process, and Orca is not proposed for `vega` (ORCA-REACH). The Claude review recommends a) at medium confidence because of the split's destination; the Codex review recommends a) at high, with the split designed command by command first and no blanket freeze, so that contract correctness, isolation and recovery work continue.

**Query:** Should `ki agent` stay in tools-ki or move to a Techné agent, and how should its work-model commands be separated?

**Options:**

a) (recommended, confidence high - both design reviews choose it, and designing the split first answers the one reviewer's doubt about its destination) Keep it in tools-ki as the floor launcher, maintained, with no new features that duplicate Orca while contract correctness, isolation and recovery work continue. Design the separation of `decide`, `reconcile`, `home` and `prompts` command by command, as a tools-ki record, before moving any; `home` stays with the run. Record a Techné dispatch agent as an `Idea:` line on the Techne theme page.

b) Move dispatch to tools-techne behind a thin `ki` shim, once an Enactment decision takes up Techné dispatch and sets its bounds; not on this design's authority.

c) Retire `ki agent` and use Orca everywhere, once another launcher meets the contract on every required host; that evidence is absent.

### WAKE-SESSION - How a live coordinator session hears that a run has finished or is blocked

since 2026-10-30 · from run/landscape, split from WAKE · merged in [landscape-report](design/landscape-report.md)

**Context:** While a coordinator session is open, `ki agent wait --next` and `orca orchestration check --wait` both block until the next finish, failure, block or question; Orca's nudge to an idle session is "best-effort attention only", and Paperclip has no outbound webhook. Both design reviews agree with one bounded `wait`, one armed at a time, and add proof requirements. `ki agent wait` has no timeout option, so the five-minute bound must come from the detached waiter around it. `--next` marks an event seen, so a waiter that dies after marking can lose it. Claude Code re-invokes the session when a background task exits, but a Codex coordinator has no such re-invocation, so its wait is only as good as its next turn. The standard already calls session wakes best effort.

**Query:** How should every launcher wake a live coordinator session?

**Options:**

a) (recommended, confidence high - both design reviews agree, and the additions rest on local help) Add one contract verb, `wait`, implemented natively by each launcher, with exactly one detached waiter armed at a time, bounded at five minutes by the waiter and re-armed after each wake. Prove wake and acknowledgement per runtime and launcher before relying on it, including that no seen event is lost. Session wakes stay best effort.

b) Adopt the verb as the design worded it, without the per-runtime proof step.

### WAKE-DURABLE - What wakes the work when no coordinator session is open

since 2026-10-30 · from run/landscape, split from WAKE · merged in [landscape-report](design/landscape-report.md)

**Context:** The landscape design said a durable wake "stays deferred under WAKE-SUBSTRATE". Both design reviews show that is stale. On 26 October Kris took WAKE-SUBSTRATE a), read back as "lift the deferral in order: write the headless coordinator-pass contract ... into `ki-coordination`, then send the launchd shell-check job as a line to ki.chezmoi and ki.mac-studio-setup". The contract is written in `ki-coordination`'s Headless passes section, and only doorbells and extra liveness fields stay deferred. Neither the standard nor the merge establishes that the job is installed. The design's alternative, Orca automations with a shell pre-check, would be a second durable mechanism beside the chosen one; the Codex review would consider it only after an explicit new choice reconciles it with the headless pass and the host bounds. Where the pass may run is WAKE-HOST.

**Query:** Should the headless coordinator pass remain the durable wake, as decided under WAKE-SUBSTRATE?

**Options:**

a) (recommended, confidence high - follows Kris's 26 October decision and the written contract, and both design reviews agree) Keep the headless pass as the durable wake, acting only within a grant or decision that names it, and correct the landscape design and explainer to say so. Doorbells and extra liveness fields stay deferred, and Orca automations are not adopted as a durable wake.

b) Adopt Orca automations with a shell pre-check as the durable wake instead, under an away grant, after an explicit choice reconciling them with the headless pass and the host bounds.

### WAKE-HOST - Where the headless coordinator pass may run

since 2026-10-30 · from run/landscape, split from WAKE · merged in [landscape-report](design/landscape-report.md)

**Context:** The Techne Programme Focus, set on 20 October, names two hosts, `vega` and sol, and allows agents on them only "in sessions the binding owner opens, with no unattended or scheduled agents". A launchd headless pass is a scheduled agent. WAKE-SUBSTRATE, a later decision in this work, does not amend a governance policy, so the pass may not run on sol or `vega` until the focus is changed through the Enactment Process. Terra, Kris's other Mac, is outside the focus. The job itself was sent to `ki.prj.chezmoi` and `ki.prj.mac-studio-setup`. The Claude review recommends terra first at medium confidence, noting that a pass sees only its own host's runs, because `ki agent status` is host-local, while sol is where most coordination and the Orca trial now run. The Codex review treats host permission as a separate decision and names no host. The design treated scheduled runs as out of scope, which both reviews call stale.

**Query:** On which host may the headless coordinator pass run?

**Blind review (30 October, Codex, high effort):** differs, prefers b) at medium confidence: the pass should observe the work it serves, so propose the bounded Enactment amendment for sol, with no pass there before approval; a terra pass sees only terra's runs, and terra's absence from the focus is not itself permission.

**Options:**

a) (recommended, confidence medium - needs no policy change and is reversible, but a terra pass sees only terra's runs and the reviewers did not agree on a host) Terra first, for works whose own decision names the pass; no pass on sol or `vega` unless the focus is later changed through the Enactment Process.

b) Propose an Enactment change to the Techne Programme Focus admitting the headless pass on sol, bounded as the standard sets it (shell-only trigger, named works only, `push` tier at most), so that the pass runs where coordination and Orca run.

c) No host for now: session wakes only, until a work needs a durable wake and names its host in its own decision.

### WORKTREE-OPTOUT - Which runs may skip their own worktree, and from when

since 2026-10-30 · from run/landscape · merged in [landscape-report](design/landscape-report.md)

**Context:** Kris wants every writing run, under every launcher, in its own worktree, merged back to `main` fast-forward and verified. Coordinators stay on primary `main`. The collisions recorded in checkout-isolation came from the shared index and lock, not from the size of the change; a worktree costs about 0.2 seconds, plus about 1.5 seconds to clone dependencies. Both design reviews agree that only read-only runs should opt out, and add two points. Writes into the package folder, such as design notes and reports, count as writes and reach the coordinator only once integrated, so integrate precedes receive. And the baseline cannot be installed policy yet: no integrate command exists, so every trivial run would need a hand merge; `--worktree` bases the worktree on the supplied checkout's `HEAD`, not committed `main`; registry resolution and the pathspec commit helper are still open; and the installed guidance still carries the short-package pilot rule and a roadmap-ledger exception. The Claude review puts the no-trivial-exception rule at medium until integrate ships; the Codex review puts it at high, provided those exceptions are reconciled at rollout.

**Query:** Which runs may skip the worktree, and from when does the baseline apply?

**Blind review (30 October, Codex, high effort; applies to the earlier wording of a), which had no rollout condition):** agrees with a) at high confidence: whether a run writes into a repository, not its size, sets the shared-write risk.

**Options:**

a) (recommended, confidence high - reviewed, and both design reviews agree on the boundary; the timing follows the missing integrate command) Only runs that write nothing inside any repository may opt out; trivial writing runs get no exception, and package-folder writes count as writes. The baseline takes effect when the `ki` integrate command and the open worktree prerequisites land. Until then checkout-isolation's pilot rule stands, short package runs on primary `main` with pathspec commits and the landed check, and the existing exceptions are reconciled explicitly at rollout.

b) Let trivial single-file runs in a knowledge base write in the primary checkout as well, under an explicit serial write window, as a standing exception.

c) Apply the baseline now, before the integrate command exists, merging every writing run back by hand.

## Parked

- HOMES - Existing packages default to the territory Capital, with approved regular/ad hoc exceptions. Local keys and canonical repository identities differ. Explicit metadata must not create a new home or permission. Recommended: a) (confidence high - portable identity and existing authority remain distinct) Use the HOMES model above: optional matching `territory`, omitted `canonical_home` derives Capital, explicit null stays unresolved, supplied identities must resolve uniquely and exceptions retain their approval requirements.
- EXECUTION - The owner means where work is meant to be running and illustrates the chezmoi repository footprint. Both earlier reviews prefer plural execution hints; neither establishes support in current readers. One declared default can supply a verified launch working directory without replacing canonical package home, explicit unit targets or authority. Recommended: a) (confidence medium - meets the owner's execution intent with lean semantics; launch compatibility remains unproved) Keep singular `execution_home`, unspecified when absent/null, as one default repository/context that can supply a verified launch working directory after explicit work selection, host requirements and unit authority checks. Preserve explicit unit targets and overrides; resolving the directory grants no write authority. Current readers need separately authorised compatibility work; no binding or directory change happens here.
- HOST - Device constraints already resolve through inventory, while live placement stays out of packages. Most constraints belong to units. The current naming ban needs clarification for the owner's illustrative machine-related subject id. Recommended: a) (confidence high - explicit constraints do not imply placement or authority) Adopt the optional typed `host_requirement` design, normally using unit constraints instead; unresolved required identities block device-dependent execution. Permit owner-chosen machine-related subjects such as illustrative `rig-sol`, with no inferred binding and no live-seat encoding.
- DISPLAY - Readers currently require title, but ordinary names are derivable and the owner wants a smaller definition. Custom labels and report headings must keep their meaning. Recommended: a) (confidence medium - feasible from naming rules, but compatibility needs fixture proof) Remove mandatory stored `title` after dual-reading readers can derive names, preserve custom display in optional `label`, expose compatible display projections and fall back visibly to id when metadata is unresolved.
- THEME - Regular is a work level; theme is optional thematic grouping. Requiring `theme: regular` would replace meaningful grouping or require an invented theme. Recommended: a) (confidence high - preserves both meanings without extra metadata) Keep optional/null `theme`, validate supplied theme slugs, and derive regular grouping from `level`; impose no regular-theme invariant.
- ROUTING - Description already includes exclusions at register depth. A separate `not_for` could improve authoring clarity but has no demonstrated routing gain and risks hidden or conflicting boundaries. Recommended: a) (confidence high - simplest design matching the actual reveal boundary) Retain purpose, Takes and Not for in `description`, the combined soft 500-character budget and Scope collision handling; add no anti field in this design.
- SIGNAL - No reviewed source proves universal telemetry. Package timestamps cannot supply session age. Useful partial evidence can coexist with explicitly unknown signals. Recommended: a) (confidence high - useful without fabricating counters or adding package state) Append evidenced elapsed wall-clock age and user/assistant message volume after `🧵 <id>` on the same final thread line, with coverage, provenance and observation time; preserve stable identity, epoch/reset rules, unknown/stale labels and no new persistent telemetry store. Keep the current footer unchanged until adoption and compatible reader migration.
- RESTART - The owner requested threshold-triggered advice. The masked review independently supports the same reversible four-hour/100-message convention with medium confidence in workflow fit and low confidence in the particular values. No evidence validates degradation prediction or numerical superiority. Existing pick-up defines safe continuation. Recommended: a) (confidence medium - reviewed workflow fit; numerical values unvalidated; fulfils the requested reminder through an explicitly unvalidated, reversible convention) Use four elapsed hours or 100 evidenced user/assistant messages, with a qualifying usable observation making one reminder pending per current session for the next existing safe resumable boundary. Unknown/stale evidence cannot establish a crossing; label partial coverage. The owner may continue and may request safe continuation earlier. No automatic restart, repeat or escalation; no implementation, pilot or study authority follows.
- STATE-MACHINE-DECISIONS - Open choices remain in [work-state-machine.md](design/work-state-machine.md). Recommended: settle them with the rollout.
- FOLDER-MIGRATE - This package has been tidied and its root reports moved losslessly into reports/; the wider migration remains open. Recommended: a) tidy, then git mv per package.

Terra portability questions below are deferred pending the owner's forthcoming movement/handover update. No option is selected and no Terra drain completion is claimed.

### TERRA-LOCAL-REPORTS - Dispose of the two run-only reports safely

**Context:** Terra retains drain-form.report.md and wow-sync-terra.report.md without exact blobs on origin/main. The sync outcome is logged in the package; the older report's complete outcome/query home is unproved here. PUBLIC-REPORT-AUDIENCE still applies.

**Query:** What private review and exact disposition should these copies receive before terra is called drained?

**Options:**

a) (recommended, confidence high - proves complete homes before disposal) Review both privately, record each outcome/query home, then select its disposition; retain both meanwhile.

b) Retain both on terra and leave the drain incomplete.

### TERRA-PR-CHECK - Supply the provider's open PR inventory

**Context:** Pruned origin refs and the absence of local work branches cannot establish open PR state. This run's provider-call ban prevented that check.

**Query:** Who will supply the current Ways of working open PR inventory?

**Options:**

a) (recommended, confidence high - obtains the missing fact within separate authority) Have an authorised attended session supply the inventory and resolve any named PR leftovers under its own grant.

b) Keep PR state unknown and leave the drain incomplete.

### TERRA-RECOVERY - Confirm the private recovery location

**Context:** The publication retention ref/archive and private-proof runtime named in decisions.md are absent on terra. No other machine or repository was inspected; nothing was deleted or published from those locations.

**Query:** Where is each retained item now held, with what size and private recovery home?

**Options:**

a) (recommended, confidence high - preserves retention without disclosure) Have the holding session confirm exact locations, sizes and private recovery arrangements, leaving every item intact and unpublished.

b) Leave recovery location/durability unknown and the drain incomplete.

- PACKAGE-FORWARDING - PKG-POINTER original request preserved at bcb3c1a3:+/_WORK/ki.ways-of-working/messages.md and the Principal enactment report. Owner approved one authoritative package and a Capital discovery reference; principal-only message forwarding remains separate design before any relay or second queue is built.
- PERM-PROMPTS-SETTINGS - whether to change the chezmoi-managed permission settings; Kris, 25 October: "can we come back to it later?". Recommended: not now, revisit if Kris leaves bypass mode.
- STEWARD-FIELD - where a package records who looks after it; reviews disagree, the harness carries the model with a marked placeholder and the Valle Armonia pilot runs on `worker` as it is. Recommended: a new dedicated field taking `work/<id>` values only. Parked under the 27 October bulk reading; comes back if the pilot needs it.
- LEGACY-PREFIX - whether a `repo_code` rename stays a one-sweep change; renames are rare and Personal's runs as one sweep, while an allowance costs two checkers and tools-ki. Recommended: write the one-sweep rename into `ki-work-roadmap`. Parked under the 27 October bulk reading; comes back at the next rename.
- PARTIAL-REPOS - how a repository with only Pillars and Resources fits the model; Kris's own words defer it and HNR's tracked-notes workaround holds. Recommended: record the idea on the Ways of working Project note and open a `ki-work-design` brief when Kris takes it up. Parked under the 27 October bulk reading; comes back when Kris opens it.
- UNATTENDED-FIELD - recording unattended eligibility on records; a new record field with reviews disagreeing while the roadmap is cut to next to nothing. Recommended: adopt the optional `unattended` mapping and criteria. Parked under the 27 October bulk reading; comes back if a window plan needs it.
- UNATTENDED-AND-DUE-DATES - adopting the eight criteria as the unattended assessment; the due-date half is done and the criteria stay Personal's prototype. Recommended: adopt the criteria in `ki-delegation`, leaving UNATTENDED-FIELD to decide where the verdict is recorded. Parked under the 27 October bulk reading; comes back with UNATTENDED-FIELD.
- CLI-PREVIEW - whether public state-changing commands write by default and preview with `--dry-run`; a fleet-wide tool convention while tools are not ready and releases are deprioritised. Recommended: write by default, `--dry-run` and `-n` preview, both standards reconciled first and each tool changed through its own work. Parked under the 27 October bulk reading; comes back when a repair command is next touched.
- MGIT-CACHE-SCOPE - what to build first for the mgit cache; Kris asked for the concept in plain language first, and the design note keeps the six routes. Recommended: `--repos-from` with `--to-cache` and `--from-cache` in one record, `sync --push-only` and `--pull-only` in a second. Parked under the 27 October bulk reading; comes back when Kris wants the cache built.
- MGIT-CACHE-FAILED - whether a checkout the sweep failed on goes into the cached set; same feature as MGIT-CACHE-SCOPE. Recommended: exclude them, keep their names and count as diagnostics, and warn on every `--from-cache` that the selection is incomplete. Parked under the 27 October bulk reading; comes back with MGIT-CACHE-SCOPE.
- RECORD-2 - work-package schema failures in thirteen folders; forty judgement fixes across live packages with reviews disagreeing on who makes them, and the full audit now runs only in CI. Recommended: one run per territory sweep, read-back of every changed field. Parked under the 27 October bulk reading; comes back when the work-package standard settles or a package is next tidied.
- FOLDER-1 - extras in two work folders; a rename of nine old reports and a script's home, with the review finding the counts wrong. Recommended: rename the nine to `<name>.report.md`, move `adobe-remove.sh` beside its design note and `spec-sched.brief.md` to `briefs/`. Parked under the 27 October bulk reading; comes back when those packages are next tidied.
- COORD-7-REST - fifty-one identifiers in reports with no local target; a known floor in old run reports that marks will prune, and fixing it needs a fetch and a rewrite run. Recommended: authorise the fetch of the two personal checkouts, write pruned links and rewrite the 25 tag-like identifiers. Parked under the 27 October bulk reading; comes back if the reports survive pruning.
- LINT-WHERE - where generated Markdown gets linted; the check-only staged hook of 26 October stops a bad report at commit with CI the backstop, and a generator check is extra machinery. Recommended: check-only in the generator, after FORM-VS-RUMDL. Parked under the 27 October bulk reading; comes back if bad reports still reach `+/_WORK`.
- MISSING-TOOLS - installing the missing hook tools in three package repositories; the recommendation is itself to wait, and installing would add new software. Recommended: leave them until the second convergence and bring any needed tool to Kris as its own decision. Parked under the 27 October bulk reading; comes back at that convergence.
- REL-X64-TIMEOUT - local timeout-only repair delivered and verified; release and pin work stays deferred until Kris explicitly reopens releases, under the current local-tools/no-release instruction.
- MIRROR-TOKEN - the Notion integration token and 1Password item behind the retired mirror; taken under the 27 October bulk reading, but the action is Kris's own and needs Notion and a credential change, both outside the window's limits. Recommended: revoke the integration in Notion and delete the 1Password item after `chezmoi apply` removes the last reference, finishing any HNR Notion page removal first. Parked for Kris to do at the machine.

### RIG-ATTENDED - Existing Rig attended prerequisites

since 2026-10-27 · from run/wow-rig-remainder; parked until Kris is available for the existing attended checks.

**Context:** These are existing prerequisites, not a request for another item-by-item approval. No live evidence was obtained in this run.

**Query:** Coordinator to route the existing attended checks and CORE-068 planning questions when Kris is available; keep both records in draft meanwhile.

**Options:**

a) (recommended, confidence high - preserves the plans' explicit gates) Arrange the existing attended checks and record the existing owner answers before another bounded delivery run.

b) Leave both drafts parked until those prerequisites are available.

### ANSWER-VECTOR - whether the first slice writes the answer line itself or waits for a `ki work answer` command

**Parked:** Parked with ki.observatory, which owns the feature and redesign. Release when its steward or the owner returns a route decision; neither option is selected here.

**Context:** The proposal's first slice has the Observatory compose the `messages.md` line and commit it through its own declared file effect, the path `feedback-send` already implements and tests, so the slice needs no tools-ki change. The Observatory's contract prefers consuming stable `ki` commands over duplicating work semantics, and a `ki work answer <id> <TAG> --option a --note "..."` command would make the line's shape one tool's and give the Observatory an argument vector instead. Waiting for it adds a tools-ki unit and a pin before anything can be answered in the Observatory; building the file effect first means a later swap to the command.

The review also found that the `ki-work-package` entry points let the owner, through the Observatory, commit a feedback package with its linking message, but grant no standalone answer-line write, so either option needs that authority written into the standard; sending stays off (`FEEDBACK_SENDING` false, KI-OBSERVA-BRG-004 delivered and Awaiting review pending its audit).

**Query:** Should the first slice write the line through the Observatory's own file effect, with the `ki work answer` command as a later record, rather than wait for the command?

**Options:**

a) (recommended, confidence medium - the file effect and its gate exist and are tested, and the swap later is one operation's vector, but the Observatory's own contract leans the other way) Build the first slice on the existing file effect; capture `ki work answer` and `ki work queries` for tools-ki as a later message and the Observatory's KI-OBSERVA-INT-005.

b) (blind review's pick, confidence medium - putting answer validation, the line's shape and the repository effect in one tools-ki command avoids a temporary second implementation; the feedback effect proves the mechanism, not an answer contract) Wait for tools-ki to provide `ki work answer`, and have the Observatory's first slice declare it as its vector from the start.

### AREA-COLUMN - publish the existing area reading aid?

**Irreducible hold:** `standards-compatible-harness.md` under `skills/repo-structure/ki-repo-harness/references/` explicitly calls areas a diagram reading aid rather than a published skill fact. Its marker-bounded README catalogue derives from frontmatter; `capability-publication.ts` has no area projection. The original blind review recommended extending this boundary, but that recommendation was never accepted. Existing area values avoid a new taxonomy/schema design; publishing them as a stable consumer contract still needs the choice below. A release is not the blocker.

**Delivered partial:** The immutable-ref local catalogue adapter is committed in website `2c15168`; Primary baseline received and final facts (27 October 07:03 GMT) records its integration, focused replacement evidence and the closed factual catalogue correction. The earlier dispatch and verification instructions are complete. They do not authorise the README publication extension below.

**Parked:** README publication remains outside the two independently qualified local website units; release when Kris decides the consumer contract.

**Context:** The current contract deliberately keeps areas outside published skill facts. The parked recommendation would make the harness README a stable consumer boundary. Local sync alone does not authorise that change; the two direct units and local-input partial can proceed independently.

**Query:** May the harness publish the existing area membership as a generated README reading aid and have the website consume it, without changing applicability or dependency semantics?

**Options:**

a) (recommended, confidence high - reuses the existing model and removes generator-code coupling, with the contract change explicit) Approve that bounded publication extension, then qualify exact harness generator/contract/test paths and the website parser/provenance companion paths. Use local immutable commits and local sync; no release cycle.

b) Retain the diagram-only publication boundary and the current finder/parser coupling; deliver only the independently qualified units above.

### HOST-SYNC - Settle the two-host synchronisation design

since 2026-10-28; parked until owner design discussion, source HOST-SYNC and HOST-SYNC-REPLY.

**Context:** Full received owner words, stopped-sync context, unresolved primary/secondary publication sequence and both Rig reply destinations are in [the live unadopted design](design/host-sync-and-reply-trades.md). Existing seat policy does not select concurrency, timing or a scheduler.

**Query:** Which primary/secondary publication sequence and offset should the equivalent Rig work use, including how primary hosts consume secondary updates?

**Options:**

a) (recommended, confidence medium - preserves the full request without inventing concurrency or scheduling authority) Discuss and settle the existing design choices, then send one bounded rollout line to each Rig queue; Rig and chezmoi own execution.

b) Keep the design parked and leave existing host operations to their owners; no new scheduler or host action is authorised here.

### STREAM9-SHA - Define the bare SHA-256 boundary

since 2026-10-28; parked pending owner boundary, source STREAM9-SHA and the masked source review.

**Context:** A bare hexadecimal SHA-256 can collide with an otherwise valid work identifier. The source review did not establish a high-confidence grammar-wide exemption. Filename and source-linked work references must retain precedence. No classifier change was delivered and no HNR source was inspected.

**Query:** What context should distinguish a bare checksum from a work identifier without suppressing a genuine identifier?

**Options:**

a) (recommended, confidence high - retains the existing hard boundary until the ambiguous case is defined) Keep the classifier change held; qualify a context-specific rule and negative examples before implementation.

b) Bring the exact bare-identifier ambiguity to an owner design decision before qualifying a patch; no general hexadecimal exemption is selected.

### GATE-BASELINE-COMPARATOR - Define inherited-finding equivalence

since 2026-10-28; parked until a source-grounded comparison can be reviewed, source GATE-BASELINE-PREFLIGHT.

**Context:** The routed approval asks that inherited origin/main findings be distinguished from regressions. The current preflight hard stops still apply; an exact baseline comparator, its identity/provenance and refusal cases have not been settled. A prose clarification cannot silently waive all existing WARN/FAIL findings. The sibling-worktree half already belongs to Tools under GATE-BASELINE-SIBLING.

**Query:** What exact evidence establishes that a finding is unchanged from the declared baseline, while preserving hard stops for new, changed or uncomparable findings?

**Options:**

a) (recommended, confidence high - preserves the approved goal without weakening an undefined guard) Retain current hard stops until the narrow comparator and refusal evidence are qualified; keep this a held method need.

b) Revisit the approved approach with the owner before defining comparator semantics. No baseline-wide exemption is adopted.

### THREAD-DEFAULTS - Select a session and its default work home

since 2026-10-28; parked until session/default selection is decided, sources THREAD-HOME and HOOK-SHORTCUT.

**Context:** Typed readers and member-launched coordination support are delivered. The new unknown-session hook partial emits a short conditional pointer and avoids checkout-wide scans; it does not discover the selected session. Default selection for member-local status, a Capital package and multiple candidates remains undecided. No session marker, schema or automatic work opening is authorised.

**Query:** How should a session explicitly select its one work and determine the default status/home context without assuming the launch checkout is the package home?

**Options:**

a) (recommended, confidence high - keeps delivered launch support usable while retaining explicit selection) Preserve explicit work selection and the quiet-hook partial; design the remaining default/session boundary separately.

b) Have the owner choose the intended default-selection contract before qualifying another implementation unit.

### LINK-EXTERNAL - Decide the external linked-target boundary

since 2026-10-28; parked until owner boundary decision, source THREAD-HOME/LINK-CHECKER.

**Context:** Shared LINK-1 now follows contained linked directories and contained absolute filesystem paths, with outside-byte/refusal checks. Targets outside the selected root are still excluded. This does not clear the reported HNR sibling-tree findings; no HNR source was inspected or changed.

**Query:** Should a future resolver follow a separately declared external target, and under what explicit source-access and containment contract?

**Options:**

a) (recommended, confidence high - preserves the tested containment boundary and confidential-source guard) Keep external targets held and the contained partial unchanged until the access contract is decided.

b) Ask the owner to define a bounded external-target model before any source discovery, traversal or implementation.

### PUSH-RETRY - Decide whether any bounded retry is wanted

since 2026-10-28; parked pending method choice, source Personal Rig terra PUSH-RETRY.

**Context:** The sender proposes up to five retries for a queue append losing a push race. Current coordination/delegation/Git rules distinguish an uncontested remote append from actual divergence, peer-owned history, contested staging or content conflict. No blind replay or retry policy has been adopted. The existing private qualification preserves the two routes and their source sections.

**Query:** Should the method retain the current bounded conflict-run route or design a narrowly qualified retry for uncontested append races?

**Options:**

a) (recommended, confidence high - uses the existing supported route and preserves every ownership/refusal guard) Retain the current stop-and-bounded-conflict-run method; make no retry policy change now.

b) Qualify a bounded own-content-only retry for disjoint append races before adoption; the sender's five-attempt count remains a proposal and cannot override divergence, privacy or narrower push rules.

- PROTECTED-PUBLICATION - the current unpublished Principal stack has two protected report blob versions in the existing private safe-sync inventory. Owning Observatory has an IMPORTANT disposition request before any push; preserve peer work/history and infer no publication certification. This remains separate from the earlier remotely exposed report-history audience query.
- MD-STANDARD-REMAINDER - local writer/exclusion and staged-gate evidence is independently accepted Done in CLI-175; the HNR hook-bypass cause, global historical cleanliness and other-host/provider freshness are still unproved. HNR source/access remains excluded; no estate audit is commissioned. Revisit only under the owning source/access authority.
- ENACTMENT-ADMIN - the 20 October tiered/Admin-only gate-narrowing choice remains unmade; retain the current gate. Full original decision is retained in decisions.md.
- PROXY-SHAPER - Kris deferred this on 25 October; no proxy or chezmoi change. Full original owner words remain in decisions.md; revisit only when taken up.

### HOMES - Repository identity and defaults

**Context:** Existing packages default to the territory Capital, with approved regular/ad hoc exceptions. Local keys and canonical repository identities differ. Explicit metadata must not create a new home or permission.

**Query:** Use canonical repository identities, a derived Capital default and optional checked `territory`?

**Options:**

a) (recommended, confidence high - portable identity and existing authority remain distinct) Use the HOMES model above: optional matching `territory`, omitted `canonical_home` derives Capital, explicit null stays unresolved, supplied identities must resolve uniquely and exceptions retain their approval requirements.

b) Keep home declarations only in current Scope and omit both new fields; retain the current resolution contract.

### EXECUTION - One default execution context

**Context:** The owner means where work is meant to be running and illustrates the chezmoi repository footprint. Both earlier reviews prefer plural execution hints; neither establishes support in current readers. One declared default can supply a verified launch working directory without replacing canonical package home, explicit unit targets or authority.

**Query:** Use one optional execution repository/context as a checked launch default, with explicit unit targets and overrides?

**Options:**

a) (recommended, confidence medium - meets the owner's execution intent with lean semantics; launch compatibility remains unproved) Keep singular `execution_home`, unspecified when absent/null, as one default repository/context that can supply a verified launch working directory after explicit work selection, host requirements and unit authority checks. Preserve explicit unit targets and overrides; resolving the directory grants no write authority. Current readers need separately authorised compatibility work; no binding or directory change happens here.

b) Defer an execution field and retain explicit per-unit working-directory and target declarations under current readers, leaving the requested package-level launch default undelivered.

### HOST - Required machine versus session seat

**Context:** Device constraints already resolve through inventory, while live placement stays out of packages. Most constraints belong to units. The current naming ban needs clarification for the owner's illustrative machine-related subject id.

**Query:** Add an optional whole-package host/category requirement and distinguish subject naming from live placement?

**Options:**

a) (recommended, confidence high - explicit constraints do not imply placement or authority) Adopt the optional typed `host_requirement` design, normally using unit constraints instead; unresolved required identities block device-dependent execution. Permit owner-chosen machine-related subjects such as illustrative `rig-sol`, with no inferred binding and no live-seat encoding.

b) Retain all constraints in existing labels/Scope/unit prose and retain the current host-in-id prohibition; choose a different subject id before any adoption.

### DISPLAY - Remove mandatory stored title compatibly

**Context:** Readers currently require title, but ordinary names are derivable and the owner wants a smaller definition. Custom labels and report headings must keep their meaning.

**Query:** Approve title removal as the destination, after compatible readers and preserved display overrides?

**Options:**

a) (recommended, confidence medium - feasible from naming rules, but compatibility needs fixture proof) Remove mandatory stored `title` after dual-reading readers can derive names, preserve custom display in optional `label`, expose compatible display projections and fall back visibly to id when metadata is unresolved.

b) Retain required stored `title` as the permanent authoring contract, updating it from display metadata as today.

### THEME - Independent grouping

**Context:** Regular is a work level; theme is optional thematic grouping. Requiring `theme: regular` would replace meaningful grouping or require an invented theme.

**Query:** Keep theme independent and derive a Regular work display group from level?

**Options:**

a) (recommended, confidence high - preserves both meanings without extra metadata) Keep optional/null `theme`, validate supplied theme slugs, and derive regular grouping from `level`; impose no regular-theme invariant.

b) Make regular level imply `theme: regular`, deliberately replacing independent grouping for those packages and requiring a separately authorised real theme definition.

### ROUTING - One exclusion source

**Context:** Description already includes exclusions at register depth. A separate `not_for` could improve authoring clarity but has no demonstrated routing gain and risks hidden or conflicting boundaries.

**Query:** Keep the combined description as the proposed routing contract?

**Options:**

a) (recommended, confidence high - simplest design matching the actual reveal boundary) Retain purpose, Takes and Not for in `description`, the combined soft 500-character budget and Scope collision handling; add no anti field in this design.

b) Introduce optional text `not_for` as the sole exclusion source when present, with positive-only authored description, a combined legacy projection and the same total soft budget; migrate all register readers before conversion.

### SIGNAL - Truthful session indicator

**Context:** No reviewed source proves universal telemetry. Package timestamps cannot supply session age. Useful partial evidence can coexist with explicitly unknown signals.

**Query:** Display separately evidenced age and volume with volatile runtime observations and explicit unknowns?

**Options:**

a) (recommended, confidence high - useful without fabricating counters or adding package state) Append evidenced elapsed wall-clock age and user/assistant message volume after `🧵 <id>` on the same final thread line, with coverage, provenance and observation time; preserve stable identity, epoch/reset rules, unknown/stale labels and no new persistent telemetry store. Keep the current footer unchanged until adoption and compatible reader migration.

b) Show only a qualitative resumability reminder until one client can evidence both full-session age and volume; keep numerical freshness display deferred.

### RESTART - Advisory policy and safe continuation

**Context:** The owner requested threshold-triggered advice. The masked review independently supports the same reversible four-hour/100-message convention with medium confidence in workflow fit and low confidence in the particular values. No evidence validates degradation prediction or numerical superiority. Existing pick-up defines safe continuation.

**Query:** For the design only, use four elapsed hours or 100 evidenced user/assistant messages as the provisional reminder cutoff?

**Options:**

a) (recommended, confidence medium - reviewed workflow fit; numerical values unvalidated; fulfils the requested reminder through an explicitly unvalidated, reversible convention) Use four elapsed hours or 100 evidenced user/assistant messages, with a qualifying usable observation making one reminder pending per current session for the next existing safe resumable boundary. Unknown/stale evidence cannot establish a crossing; label partial coverage. The owner may continue and may request safe continuation earlier. No automatic restart, repeat or escalation; no implementation, pilot or study authority follows.

b) Retain truthful signals and user-requested safe continuation without numerical reminders, explicitly deferring the requested threshold-triggered element.

c) Choose different provisional numerical values as an owner workflow preference, with the same advisory and evidence constraints and no degradation claim.
