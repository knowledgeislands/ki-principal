# ki.prj.ways-of-working queries

## Open

### WORKER-WAIT-MEANING - With worker means the worker role holds the work, not that a process is live

since 2026-10-29 · from run/sol-state-machine-readiness, split from WORKER-WAIT on 30 October at Kris's request; refines the parked STATE-MACHINE-DECISIONS · high now, no further work needed

**Context:** Kris's words under ROLES-ORCHESTRATOR name three roles: "the worker is a subagent, and then the thread agent is effectively the orchestrator of the state machine". The sentence "With worker means a run holds the work" is the read-back's, not Kris's, and the [state machine](design/work-state-machine.md) States table narrows it further to "a run of the work is in flight". ROLES-EITHER then lets a human hold any role, and a human worker never has a run in flight, so the narrow reading cannot describe a case Kris has already allowed. The banner makes its last glyph whose move it is, and its list already names a holder per item, `run/<name>` for `[running]` and `[queued]` alike. This part settles only the test; WORKER-WAIT-QUEUED, WORKER-WAIT-MIDTURN and WORKER-WAIT-GATED apply it to the disputed cases.

**Query:** Is With worker defined by assignment, the worker role holding the next move on at least one named unit, or by liveness, a run process being in flight?

**Options:**

a) (recommended, confidence high - the only reading that fits Kris's own role words, ROLES-EITHER's human worker and the banner's existing holder items, and it can be checked against `ki agent status` and the run queue) Assignment: the work is With worker while at least one authorised unit is assigned to a named worker holder, running or queued, so its next move is the worker side's; a run in flight is the common case, not the definition. The States table and the read-back's narrower sentence are restated to match.

b) Liveness: With worker only while a run process is in flight; every other moment of Working must sit in another inner state.

### WORKER-WAIT-QUEUED - Briefed work waiting only for a slot stays With worker

since 2026-10-29 · from run/sol-state-machine-readiness, split from WORKER-WAIT on 30 October at Kris's request · high now; the earlier blind review, which preferred an actual holder, also held that "a holder can own queued work without a live run"

**Context:** About three agents run per thread and the rest wait in the run queue, each with its brief, agent name and launch options; the dispatcher launches the next as a slot frees and honours each `DONE` gate, with no further decision from anyone. The banner already lists such a unit as `[queued]` with holder `run/<name>`. Current coordination says "Authorised work waiting for worker capacity stays with the worker; send to supervisor only for an actual decision or review", and the agreed `inform` arc needs a decision or review due, all dispatched work finished or a stuck worker, none of which a full queue is. This part covers only a unit that is briefed and queued; authorised work that cannot yet be queued is WORKER-WAIT-GATED.

**Query:** Is the work With worker when its remaining authorised units are briefed and in the run queue, waiting for a slot or for a `DONE` gate on another run of this work?

**Options:**

a) (recommended, confidence high - each unit has a named holder and will start without anyone's further move, so sending it to Kris would ask Kris for nothing) Yes: With worker, each unit shown `[queued] · run/<name>` and never counted as running or with you; the `pick up` and `receive by worker` arcs complete only when every authorised unit they restart is running, queued or recorded as gated.

b) No: entry to With worker waits for a launch, so after a direction the work stays in Handoff to worker until a slot frees, and a bootstrap that finds only queued work refines to With supervisor.

### WORKER-WAIT-MIDTURN - An orchestrator turn moves nothing

since 2026-10-29 · from run/sol-state-machine-readiness, split from WORKER-WAIT on 30 October at Kris's request · high now; the earlier blind review made the same point, that an orchestrator mid-turn "does not by itself establish that assignment"

**Context:** Current coordination, States and moves, says territory and Project work are With worker "while any items lies with a run or the coordinator is mid-turn". The clause dates from when the thread agent was the worker to Kris, which ROLES-ORCHESTRATOR reframed. The agreed machine says a steer, a heartbeat, a run launched or received and a mark happen inside a state and move nothing; only an arc moves the work, and the orchestrator makes the arcs. A coordinator answering Kris in With supervisor, or receiving a report before it informs, is orchestrating, not working. The coordinator style already forbids the orchestrator substantive work, so no coordinating case needs it as the worker.

**Query:** Does an orchestrator turn by itself put or keep the work With worker?

**Options:**

a) (recommended, confidence high - follows the agreed rule that only arcs move the work, and the clause is a remnant of the role ROLES-ORCHESTRATOR reframed) No: during an orchestrator turn the work stays in its last committed state and moves only by an arc; drop "or the coordinator is mid-turn" from the state rule. If ROLES-EITHER ever puts the orchestrating actor in the worker role, it is named as a unit's holder like any other, under WORKER-WAIT-MEANING.

b) Yes: keep the clause, so any orchestrator turn reads as With worker whatever was last committed.

### WORKER-WAIT-GATED - Authorised work that nothing will start by itself

since 2026-10-29 · from run/sol-state-machine-readiness, split from WORKER-WAIT on 30 October at Kris's request · high after the blind review of 30 October; still to check before enforcement: REST-PORTABLE's settled rule that a short external wait may stay within Working "only when its actual holder/state is represented honestly"; a ruling on whether dated follow-ups, such as ORCA-REACH's due 6 November, are gates or ordinary next steps; and evidence of what the dispatcher does when a usage limit or provider outage stops a launch, which no run has verified

**Context:** Some authorised units cannot be briefed or queued yet because they wait on something outside this work's runs: another work's reply, a person, a date, a host, or model capacity lost to a usage limit or outage. Nothing will start them until someone acts on an event. While other units run or are queued the work is With worker anyway; the question arises only when gated units are all that remain. The current capacity rule would keep such work with the worker indefinitely, which can show a With worker with nothing running and no heartbeat for days. REST-PORTABLE makes At rest · waiting the honest state for a real wait, but at the cost of the full stop: drain, the portability checks, parked queries and a struck mark, even for a short reply. A live coordinator wakes at least every five minutes and reads `messages.md` at each wake, so it notices a reply line; once the session ends nothing does, unless a granted headless pass names the work.

**Query:** When gated units are all the authorised work that remains, does the work stay With worker or stop to At rest · waiting?

**Blind review (30 October, Codex, high effort):** agrees with a) at high confidence: responsibility can stay with an active coordinator that will observe and act on the gate, while a concluded session needs an explicit waiting handoff; it adds that an open session alone is not enough without an actual wake-and-check. Confidence lifted to high.

**Options:**

a) (recommended, confidence high - reviewed; honest about the holder while a live session that wakes and checks can act on the gate, and avoids an idle With worker once it cannot) Stay With worker, each gate shown as an item naming it, `[handoff]` where it is other work or a person, only while the orchestrator session that will act on it is open and waking; conclude and stop to At rest · waiting, the gate as release, before that session ends or when the gate is a date or outlasts it.

b) Stop to At rest · waiting as soon as nothing of this work is running or queued, however short the gate.

c) Stay With worker while any authorised gated unit remains, however long the gate, each shown as an item naming it.

### WORKER-WAIT-DELIVERY - Carry the high parts into the rollout now

since 2026-10-29 · from run/sol-state-machine-readiness, split from WORKER-WAIT on 30 October at Kris's request · high now, once the three high parts above are taken

**Context:** The [state-machine rollout plan](design/state-machine-rollout-plan.md) excludes WORKER-WAIT's two cases from U1's Harness contract fixtures and from the pilot pending an answer, and says WORKER-WAIT blocks only their enforcement. WORKER-WAIT-MEANING, WORKER-WAIT-QUEUED and WORKER-WAIT-MIDTURN change wording, fixtures and holder projections only: no state value, arc or diagram. WORKER-WAIT-GATED may change when a stop falls due, which touches the stop arc's trigger.

**Query:** Once the three high parts are taken, should U1 and U2 carry them now, with WORKER-WAIT-GATED left isolated until it is decided?

**Options:**

a) (recommended, confidence high - the three are consistency corrections inside the agreed shape, and holding them back leaves the mid-turn clause live in the standard) Yes: U1 restates States and moves, the States table and the role words to the adopted reading and adds running, queued and orchestrator-turn fixtures; U2's readers show queued apart from running wherever they project holders; WORKER-WAIT-GATED stays out of enforcement and the pilot until decided.

b) Hold every part of WORKER-WAIT out of U1 and U2 until WORKER-WAIT-GATED is decided too.

### HOST-CADENCE - Which cadence Rig prepares, without activating it

since 2026-10-29 · from run/sol-host-sync-design; rewritten 30 October from the [merged host-sync report](design/host-sync/report.md#host-cadence---which-cadence-rig-prepares).

**Context:** Kris's shape is hourly, publishing primaries "on the hour" and secondaries "five minutes later". Each territory has one primary host, so at any slot the two hosts touch disjoint territories, and the brief's extra two-minute host stagger protects nothing measured. No phase duration, sleep or wake behaviour has been measured, and offsets confer no exclusion or completion proof. The reviewers disagree: Claude recommends Kris's `:00` primary and `:05` secondary on both hosts at medium confidence, because the sets are disjoint and the attended run measures duration before activation; Codex recommends measuring attended passes first and keeping the hourly pattern only as a candidate, at medium confidence, because durations and wake behaviour are unverified. Both accept one attended run per host before any recurrence. An earlier blind review preferred measuring first. Nothing is activated either way.

**Query:** Should Rig prepare Kris's hourly `:00`/`:05` cadence now, confirmed by each host's attended run, or leave the cadence unchosen until measured?

**Blind review (30 October, Codex, high effort):** agrees with a) at medium confidence: a provisional plan keeps Kris's stated shape while each host's attended measurement stays a hard gate on recurrence; if measurements fail, the cadence is revised before activation, and offsets give no locking or completion guarantee. Confidence lifted to high.

**Options:**

a) (recommended, confidence high - reviewed; Kris's own hourly and five-minute shape with disjoint per-slot sets, prepared provisionally with each host's attended run as a hard gate before any recurrence) Prepare hourly phases on both hosts: primary `:00`, secondary `:05`, a pull-only read-back shortly after, each host's first attended run confirming phase duration fits before activation.

b) Keep cadence unchosen; prepare attended passes only, and return a recurring plan once they have measured phase duration and wake behaviour.

c) Prepare the brief's staggered phases: Terra primary `:00` and secondary `:05`, Sol primary `:02` and secondary `:07`.

### HOST-COVERAGE - Who prepares the responsibility map, and from what start

since 2026-10-29 · from run/sol-host-sync-design; rewritten 30 October from the [merged host-sync report](design/host-sync/report.md#host-coverage---who-prepares-the-map-from-what-start).

**Context:** Kris asked for a dotfiles entry naming "per territory" the primary and secondary host. Both reviewers have Rig and chezmoi propose the map and Kris approve it before any configuration or operation, at territory grain with explicit exclusions, the chezmoi source as a named member and the resolved per-repository membership recorded per occurrence. [ADR-KI-PRINCIPAL-007](../../../Admin/Governance/Decisions/ADR-KI-PRINCIPAL-007-territory-seats-on-hosts.md) says "Each territory has one seat and one standby", and the sender's line named `seats.yaml` as the nearest entry, but seats mean coordination landing, not sync primacy. The reviewers disagree: Claude recommends starting the proposal from seat host as primary and standby as secondary, active-active territories primary on the hub, for Kris to confirm in one answer, and saying when HNR joins, at medium confidence; Codex recommends not inferring from seats, enumerating repository, branch and phase eligibility, and piloting one jointly nominated non-HNR, non-deploying repository, at high confidence.

**Query:** Should Rig and chezmoi start their proposed map from the seats, for Kris to confirm or amend, or build it without that starting point?

**Blind review (30 October, Codex, high effort):** agrees with a) at medium confidence: existing coordination placement is a useful seed for the proposal when Kris explicitly approves the sync roles and the receiving owners verify repository, branch and phase eligibility before configuration. Confidence lifted to high.

**Options:**

a) (recommended, confidence high - reviewed; Kris's per-territory words, the ADR's seat and standby pairing and the sender's pointer give a seed, while Kris's approval and the owners' eligibility check keep seats from being read as sync authority) Rig and chezmoi propose a territory-grain map starting from seat host as primary and standby as secondary, active-active territories primary on the hub, with exclusions, resolved membership and the point at which HNR joins; Kris approves or amends it before configuration; the first attended run uses one non-HNR, non-deploying repository.

b) Rig and chezmoi propose the map without the seats starting point, enumerating repository, branch and phase eligibility, and return it for approval before configuration, starting from one jointly nominated non-HNR, non-deploying pilot repository.

c) Kris supplies the map and pilot repository directly; the receiving owners verify eligibility and prepare its bounded plan.

### HOST-SECONDARY-PUBLISH - How secondary-origin changes reach Git

since 2026-10-29 · from run/sol-host-sync-design; rewritten 30 October from the [merged host-sync report](design/host-sync/report.md#host-secondary-publish---how-secondary-origin-work-reaches-git).

**Context:** Kris said "then five minutes later ... the secondary ones" and "the primary then needs to be able to read the secondary updates"; there is nothing to read unless the secondary publishes. Both reviewers reject the brief's pull-only secondary as failing that requirement. Both precedent syncs Kris ran on 28 and 29 October pushed unattended (SOL-SYNC also rebased), and the [Git authority standard](../../../.agents/skills/ki-git/references/standards-git.md#commit-publication-and-integration-authority) permits explicit standing publication authority. `mgit sync` pushes ahead-only branches by default, contrary to an adopted no-push-default request, so the recipe needs an explicit publish mode either way. The reviewers disagree on when publication may run: Claude recommends publishing ahead-only work fast-forward in the secondary phase with Kris's map approval as its grant, at medium confidence; Codex recommends preparing a distinct default-off capability, pull-only until separately authorised, at high confidence. Preparing it grants nothing.

**Query:** Should Rig and the Git-tool owner prepare secondary publication as a default-off step that runs only under Kris's explicit standing grant?

**Options:**

a) (recommended, confidence high - both reviews independently reject pull-only as failing the requirement, and preparing a default-off step grants nothing) Prepare secondary publication in the same recipe: ahead-only, fast-forward, never forced, leaving diverged and dirty repositories to the host's Rig thread; off until Kris gives an explicit standing grant naming the territories, revocable by a stop word, which Kris may give in the same answer as the map approval.

b) Keep the secondary pull-only; secondary-origin changes reach Git only through separately authorised attended work, and read-back reports unpublished work as outside its coverage.

### HOST-READBACK - When primaries consume published return work

since 2026-10-29 · from run/sol-host-sync-design; rewritten 30 October from the [merged host-sync report](design/host-sync/report.md#host-readback---when-primaries-consume-returned-work).

**Context:** Kris said "we probably want to do a resync as well in short order after it". Next-hour read-back leaves secondary-origin work about 55 minutes before the primary consumes it. Both reviewers now prefer a prompt pull-only read-back, keeping next-occurrence recovery: Claude at `:10` on each primary, at medium confidence, because it is what Kris described and costs one fetch; Codex at `:10`/`:12` if the hourly candidate holds, at medium confidence, because exact slots depend on measured duration. An earlier blind query review agreed with next-hour read-back at high confidence; it predates both design reviews. Read-back matters only for published work, so it depends on HOST-SECONDARY-PUBLISH, and its slot follows HOST-CADENCE. It adds no publication authority or acknowledgement.

**Query:** Should each primary run a short pull-only read-back after the secondary phase, or wait for its next hourly occurrence?

**Blind review (30 October, Codex, high effort):** agrees with a) at high confidence: a prompt pull-only attempt cuts avoidable delay for already-published work without needing more publication authority, and must not gain conflict-resolution, reset or publication powers. Confidence lifted to high.

**Options:**

a) (recommended, confidence high - reviewed; both design reviews and this blind review prefer it on Kris's "in short order", superseding the earlier blind query review that backed b), with its slot following cadence) Prepare a pull-only read-back on each primary shortly after the secondary phase, its slot following HOST-CADENCE, keeping next-occurrence recovery for late or missing work and promising no immediate convergence.

b) Read published secondary-origin updates at the start of the primary's next hourly occurrence, stating the roughly 55-minute delay.

### PUBLIC-REPORT-AUDIENCE - Choose the response scope

since 2026-10-29 · from run/sol-private-report-assessment; the parked TERRA-LOCAL-REPORTS and PROTECTED-PUBLICATION refer to this audience question.

**Context:** Exact selected historical content remains reachable in locally verified published history, and one protected version remains current. Readership and indexing are unknown. Assessment approval did not authorise a remedy. The run's private evidence and response options are at `/Users/krisbrown/.local/state/ki/agents/ways-sol-resume-20261029/sol-private-report-assessment.private/`, which stays private and outside the repository. An independent review on 30 October (private report `/Users/krisbrown/.local/state/ki/agents/ki-prj-ways-of-working/public-report-review.report.md`, quoting no protected payload) reproduced the exact local selection, byte, reachability, current-path, recovery and evidence-integrity claims on a fresh pinned snapshot. It could not establish actual public serving, readership, indexing, the original audience instruction, credentials or harm, and found no evidence supporting an emergency intervention. It recommends the private exact-version response design at high confidence, narrowed so that current and historical publication stay unchanged during the task without that implying audience clearance or a presupposed removal outcome, using the existing inventory rather than wider discovery and keeping protected detail out of the repository; its alternative was deferral with a named owner and return point.

**Query:** Should a separately bounded private response design follow, or should the owner explicitly retain the present publication posture?

**Options:**

a) (recommended, confidence high - resolves intended audience before selecting a remedy) Commission a private exact-version response design using the evidence locator above. Specify permitted audience and desired current/historical disposition; return a separate execution proposal with residual exposure stated. This authorises planning only, with no sanitisation, access change, history action, credential action or external contact.

b) Explicitly accept leaving current and historical publication unchanged, retaining the private evidence and unknown-readership qualification. This does not clear further public reuse.

c) Defer the response decision, naming its owner and return point; preserve evidence unchanged.

### PUBLIC-REPORT-RECOVERY - Decide private evidence durability

since 2026-10-29 · from run/sol-private-report-assessment; related to the parked TERRA-RECOVERY.

**Context:** Local recovery has been verified, but private off-machine recovery has not. The private evidence directory must remain outside the launcher's repository report home; no relevant source-store declaration was established for this operation. The 30 October independent review (same private report) confirmed local recovery: the bundle verifies, the recovery repository returns every selected version and all evidence hashes match, but every verified copy shares Sol's failure domain and no off-machine copy was inspected. It recommends option a) at high confidence: Kris identifies or approves a private destination independent of Sol, without guessing a source-store binding, then a separate task preserves a frozen manifest of the complete evidence chain and history bundle, verifies the destination copy and restores from it into an isolated location, reproducing the expected tip and every selected version hash, with originals kept and the runtime evidence kept out of cleanup until it succeeds. The retired Z session's private archive awaits the same preservation.

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

### ORCH-NAME-THREAD - What to call the coordination skill and its style, without rename cost

since 2026-10-30 · from run/landscape · merged in [landscape-report](design/landscape-report.md) · rewritten after run/orch-name-fresh · split from ORCH-NAME after blind review 5, with ORCH-NAME-DISPATCH taking the contract, adapters and command

**Context:** On 30 October Kris asked: "If you put aside the rename cost, what is the feedback on naming then?" The earlier recommendation, to keep the current names, rested on the cost of renaming the output style, a 217 KB standard and every live package mid-rollout; both design reviews kept the names for that reason, and once it is removed the keep has no high-confidence footing. An independent naming review then judged each unit with rename cost excluded. Thread-governance skill: `ki-orchestration`, medium - `ki-coordination` is intelligible but broad, and a newcomer cannot tell whether it governs human collaboration, worker dispatch or project administration; orchestration names the agent that runs the package's state machine, the role Kris named "the orchestrator of the state machine" on 29 October. Output style: `ki-orchestrator`, medium - it names the role and drops "coordinator" as a fourth actor word beside orchestrator, worker and supervisor. Portable run contract: `ki-delegation`, high - an orchestrator delegates a bounded job and a worker returns evidence or a question; `ki-dispatch` understates the brief, authority and return, and `ki-orchestration` would put the thread's name on one of its contracts. Adapters: `ki-delegation-orca` and `ki-delegation-paperclip`, high, provided the Paperclip skill's wider remit (company boundaries, readiness, memory, delivery policy) is described honestly rather than relabelled; `ki-agent-coordination-paperclip` has no natural Orca sibling. Launcher: `ki agent`, medium, on its own merits - `ki orchestrate` implies the executable owns the package, `ki delegate` names one action of a group that also observes, steers and closes, and `ki run` is too broad; this is the least certain unit. Main risk: `ki-orchestration` overlaps Orca's installed `orchestration` skill in meaning, though not in identifier, so the descriptions must keep package governance and Orca mechanics apart. The review's strongest alternative keeps `ki-coordination` and `ki-coordinator`: coordination comfortably covers questions to Kris, decisions, handoffs and stewardship when no worker is running, and is less associated with an execution engine. It placed that second because it leaves "coordinator" as a synonym a newcomer must learn for the orchestrator. Overall confidence is medium: both leading sets are defensible and no newcomer has tested them. Moving `decide`, `reconcile`, `home` and `prompts` under `ki work` stays out of this query, under AGENT-HOME.

**Query:** Setting rename cost aside, should the thread skill and its output style be renamed `ki-orchestration` and `ki-orchestrator`, or keep `ki-coordination` and `ki-coordinator`?

**Blind review (30 October, Codex, high effort; applies to the earlier wording of this query, whose a) kept `ki-coordination` and also moved the four commands under `ki work`):** agreed with that a); confidence lifted to high.

**Blind review (30 October, Codex, high effort):** differs, prefers b) at medium confidence: coordination accurately covers the verified human and agent governance scope, including periods when no worker is running, and the supplied precedent does not establish that orchestration is clearer to newcomers; it judged the orchestration wording defensible. It also noted that the packet exposed an earlier review's preferences, rankings and confidence, so this review is not fully blind. Confidence stays at medium.

**Options:**

a) (recommended, confidence medium - the independent naming review's pick with rename cost excluded: the skill and style match the orchestrator role and drop "coordinator" as a fourth actor word; blind review 5 prefers b) instead, holding that coordination covers the whole human and agent governance scope, including periods with no worker running, and that orchestration is untested with newcomers, so the two reviews split) Rename the thread skill `ki-orchestration` and the output style `ki-orchestrator`.

b) The naming review's strongest alternative and blind review 5's pick: keep `ki-coordination` and `ki-coordinator` because coordination better conveys the whole human and agent governance practice.

c) Keep the current names because of rename cost, as the earlier recommendation did: keep `ki-coordination` and `ki-coordinator`, and say in the Work Process note that the orchestrator role is exercised under `ki-coordination`.

### ORCH-NAME-DISPATCH - What to call the dispatch contract, its adapters and the command, without rename cost

since 2026-10-30 · from run/landscape · merged in [landscape-report](design/landscape-report.md) · rewritten after run/orch-name-fresh · split from ORCH-NAME after blind review 5, with ORCH-NAME-THREAD taking the thread skill and style

**Context:** On 30 October Kris asked: "If you put aside the rename cost, what is the feedback on naming then?" An independent naming review judged each unit with rename cost excluded. Portable run contract: `ki-delegation`, high - an orchestrator delegates a bounded job and a worker returns evidence or a question; `ki-dispatch` understates the brief, authority and return, and `ki-orchestration` would put the thread's name on one of its contracts. Adapters: `ki-delegation-orca` and `ki-delegation-paperclip`, high, provided the Paperclip skill's wider remit (company boundaries, readiness, memory, delivery policy) is described honestly rather than relabelled; `ki-agent-coordination-paperclip` has no natural Orca sibling. Launcher: `ki agent`, medium, on its own merits - `ki orchestrate` implies the executable owns the package, `ki delegate` names one action of a group that also observes, steers and closes, and `ki run` is too broad; this is the least certain unit. Both leading sets for the thread skill, in ORCH-NAME-THREAD, carry this same family. Moving `decide`, `reconcile`, `home` and `prompts` under `ki work` stays out of this query, under AGENT-HOME.

**Query:** Setting rename cost aside, which names should the dispatch contract, its adapters and the command take?

**Blind review (30 October, Codex, high effort):** agrees with a), the family in both its pick and its runner-up for the whole naming query, which it rated medium overall because of the thread-skill split: delegation names the bounded worker contract, the Paperclip skill demonstrably governs company and repository boundaries, memory, readiness and delivery, so its wider scope must be stated explicitly and not narrowed for family symmetry, and Orca's installed `orchestration` skill already denotes Orca worker orchestration. It noted that the packet exposed an earlier review's preferences, so this review is not fully blind, and that the command's behaviour beyond its documented launcher role was not verified. Confidence lifted to high.

**Options:**

a) (recommended, confidence high - reviewed; the naming review and blind review 5 both choose this family on its merits, the reviewer verified the Paperclip skill's wider scope and Orca's separate `orchestration` skill, and the least certain unit is the launcher name, which both keep) Keep `ki-delegation`, slimmed, as the portable contract, with adapters `ki-delegation-orca` and `ki-delegation-paperclip`, the second renamed from `ki-agent-coordination-paperclip` with its wider remit stated; keep `ki agent`.

b) Keep the current names because of rename cost, as the earlier recommendation did: keep `ki-delegation`, `ki-agent-coordination-paperclip` and `ki agent`.

### LAYOUT-SHAPE - Which package layout to adopt

since 2026-10-30 · from run/package-layout · [design](design/package-layout/design.md)

**Context:** Kris set on 30 October that a work package keeps only its five files at the top level, with everything else grouped, possibly group first with briefs, design and reports beneath. Three shapes fit. A, kind-first: `reports/`, `briefs/` and `design/` folders, the cheapest change, but a matter stays spread across three folders and the tidy stays file by file. B, group-first with kind subfolders, as sketched: one folder per matter with `briefs/` and `reports/` inside, which needs an estate-wide ignore exception because `reports/` is ignored at any depth. C, group-first and flat: one folder per matter, with `<run>.brief.md` and `<run>.report.md` side by side and design files under plain names, needing no ignore change. The evidence suggests the sprawl comes mainly from retention, so the group earns its cost only as the unit of tidy. No shape has been piloted.

**Query:** Which layout should the pilot use?

**Blind review (30 October, Codex, high effort):** agrees with a) at medium confidence: a flat matter folder tests the proposed organisational benefit with fewer structural dependencies; it adds that the pilot should use one small, explicitly bounded matter, and notes that the Context's claims about the sprawl's cause, the migration costs and the ignore behaviour were not verifiable from the packet. Confidence lifted to high.

**Options:**

a) (recommended, confidence high - reviewed; a flat matter folder tests the group as the unit of tidy with the fewest structural dependencies and avoids the ignore collision, and since nothing has been piloted the pilot takes one small, bounded matter) C, group-first and flat.

b) B, group-first with `briefs/` and `reports/` subfolders, plus the `ki-repo` ignore exception.

c) A, kind-first, with a stricter tidy cadence instead of groups.

### LAYOUT-GROUP-TIDY - Whether closing a group deletes it whole

since 2026-10-30 · from run/package-layout · [design](design/package-layout/design.md)

**Context:** Today's tidy deletes file by file, by explicit path, never folder-wide, and the steward judges each file's durable home. Under a group-first layout, a matter's files usually become homed together. The proposal is that once the steward judges a whole group closed, with outcomes homed, queries copied and design notes graduated or superseded, it deletes the group with one `git rm -r` naming that folder, in one commit, with Git keeping the history. Single-file deletion remains available.

**Query:** Should the tidy rule allow deleting one named, closed group folder whole?

**Blind review (30 October, Codex, high effort):** agrees with a) at medium confidence: one explicit group deletion is reviewable once every contained file has an evidenced disposition; it adds that before the one commit the steward enumerates the group's tracked contents and checks each file's durable home, copied queries and design-note disposition, preserving separately owned or unresolved material, because Git keeps committed versions but proves neither that knowledge was homed nor anything never committed. It recommends the policy only, not the deletion of any existing folder. Confidence lifted to high.

**Options:**

a) (recommended, confidence high - reviewed; one named group deletion stays reviewable when every file in it has an evidenced disposition checked before the commit, and Git keeps history; it widens a deletion rule, deletes no existing folder by itself, and is untested) Yes: a steward may delete one named, closed group in one commit.

b) No: keep file-by-file deletion inside groups.

### LAYOUT-PILOT-ORDER - When the pilot moves files

since 2026-10-30 · from run/package-layout · [design](design/package-layout/design.md)

**Context:** The rubric's FOLDER-1 fails any folder outside the closed list, the launcher homes reports only at the top level, and the Observatory reads only top-level reports and `design/`. Piloting this package before those change gives evidence sooner but shows rubric failures and hides moved reports from the Observatory and `ki agent decide`. Changing the standard and rubric first is a small harness change; the launcher and Observatory changes belong to other works and would take longer.

**Query:** In what order should the pilot run?

**Blind review (30 October, Codex, high effort):** agrees with a) at medium confidence: establishing a valid layout first and then gathering bounded manual evidence avoids waiting for the full tooling rollout; it adds that the pilot keeps an explicit inventory and reachable links for moved material, and waits for tooling support if those cannot keep receiving, discovery and tidy whole. Confidence lifted to high.

**Options:**

a) (recommended, confidence high - reviewed; a small harness change first keeps the rubric honest, and moving received reports by hand at receive, with an inventory of what moved, bridges the launcher gap) Change the closed list and FOLDER rubric first, then pilot this package by hand, receiving and tidying before moving, with launcher and Observatory changes following.

b) Pilot now, ahead of the rubric, and accept FOLDER-1 failures in this package until the harness catches up.

c) Wait until the launcher and Observatory changes have also landed.

### REVIEW-CHALLENGE - Let reviews challenge earlier decisions, visibly

since 2026-10-30 · from run/package-layout · [design](design/package-layout/design.md)

**Context:** Kris asked on 30 October that blind reviews be free to challenge earlier decisions. Today's masked query review hides the recommendation but not the precedent in the Context. The proposal: every review brief carries a fixed independence sentence, generated so that it cannot be left out; the masked Context states earlier decisions as dated facts, not as premises; a review that challenges a decision is shown at the end of the Context with an option to revisit it, never acted on without Kris; and `ki-work-design` reviews gain a Challenges section.

**Query:** Should `ki-coordination` and `ki-work-design` adopt these four amendments?

**Options:**

a) (recommended, confidence high - each part only adds text or display, is reversible, and implements Kris's own words) Adopt the independence sentence, neutral Context, challenge display and design-review Challenges section.

b) Adopt only the independence sentence in review briefs.

### REVIEW-LIFT - Precedent earns no confidence

since 2026-10-30 · from run/package-layout · [design](design/package-layout/design.md)

**Context:** Under the query-review rule, a blind review that agrees with a recommendation lifts its confidence one level. A review can agree simply because the Context framed the question inside an earlier decision. The proposal: agreement that rests only on an earlier decision or on the framing is marked `reviewed, precedent only` and lifts nothing, and an option whose only stated reason is an earlier decision is capped at medium. This changes how confidence is earned across every query, and it will send more queries to Kris at medium.

**Query:** Should precedent alone stop counting towards confidence?

**Blind review (30 October, Codex, high effort):** agrees with a) at high confidence: repeated reliance on one premise creates no independent evidence for that premise or for the recommended course; it would also give framing-only agreement no lift, as the proposal does, and judge confidence against the verified rationale rather than reviewer unanimity, and it notes that the forecast of more medium queries reaching Kris is unverified. Confidence lifted to high.

**Options:**

a) (recommended, confidence high - reviewed; it follows Kris's direction directly and agreement resting on one premise adds no independent evidence for it, though it shifts confidence on every query and has no trial evidence) Yes: no lift from precedent-only agreement, and a precedent-only reason caps at medium.

b) No: keep today's lift rule, relying on the independence sentence alone.

### READ-FEEDBACK-NOW - Feedback packages before the Observatory can write them

since 2026-10-30 · from run/package-layout · [design](design/package-layout/design.md)

**Context:** The closed list keeps owner feedback on documents as `feedback/<date>-<slug>.md` plus one `messages.md` line, and names only "the owner, through the Observatory" as its writer. Kris can read design notes in Obsidian today, but feedback longer than a spoken answer can be left only through the Observatory's `feedback-send`, which reads only top-level reports and `design/` notes and so loses sight of moved files until it is made group-aware. The proposal widens that row: the owner may write the package by hand, or the steward may write it verbatim from the owner's spoken words, committed with its message line in the same shape.

**Query:** Should feedback packages be writable now, outside the Observatory?

**Blind review (30 October, Codex, high effort):** agrees with a) at medium confidence: an equivalent manual route removes an interface dependency while keeping owner attribution and receipt; it adds that a steward transcription names the owner as speaker, keeps the words verbatim, never turns a comment into approval, and keeps transcription and any later interpretation distinguishable. Confidence lifted to high.

**Options:**

a) (recommended, confidence high - reviewed; it uses an existing kind and shape and removes the Observatory dependency, provided the steward's verbatim rule holds with the owner named as speaker) Yes, by the owner by hand or by the steward verbatim from the owner's words.

b) No: feedback stays spoken until the Observatory path is ready.

### WAKE-HOST - Where the headless coordinator pass may run

since 2026-10-30 · from run/landscape, split from WAKE · merged in [landscape-report](design/landscape-report.md)

**Context:** The Techne Programme Focus, set on 20 October, names two hosts, `vega` and sol, and allows agents on them only "in sessions the binding owner opens, with no unattended or scheduled agents". A launchd headless pass is a scheduled agent. WAKE-SUBSTRATE, a later decision in this work, does not amend a governance policy, so the pass may not run on sol or `vega` until the focus is changed through the Enactment Process. Terra, Kris's other Mac, is outside the focus. The job itself was sent to `ki.prj.chezmoi` and `ki.prj.mac-studio-setup`. The Claude review recommends terra first at medium confidence, noting that a pass sees only its own host's runs, because `ki agent status` is host-local, while sol is where most coordination and the Orca trial now run. The Codex review treats host permission as a separate decision and names no host. The design treated scheduled runs as out of scope, which both reviews call stale.

**Query:** On which host may the headless coordinator pass run?

**Blind review (30 October, Codex, high effort):** differs, prefers b) at medium confidence: the pass should observe the work it serves, so propose the bounded Enactment amendment for sol, with no pass there before approval; a terra pass sees only terra's runs, and terra's absence from the focus is not itself permission.

**Options:**

a) (recommended, confidence medium - needs no policy change and is reversible, but a terra pass sees only terra's runs and the reviewers did not agree on a host) Terra first, for works whose own decision names the pass; no pass on sol or `vega` unless the focus is later changed through the Enactment Process.

b) Propose an Enactment change to the Techne Programme Focus admitting the headless pass on sol, bounded as the standard sets it (shell-only trigger, named works only, `push` tier at most), so that the pass runs where coordination and Orca run.

c) No host for now: session wakes only, until a work needs a durable wake and names its host in its own decision.

## Answered

- ORCA-REACH - answered a) on 30 October 2026, follow-up due 6 November 2026; see [Owner answers](decisions.md#owner-answers-30-october-2026-0615-gmt).
- AGENT-HOME - answered a) on 30 October 2026, follow-up due 2 November 2026; see [Owner answers](decisions.md#owner-answers-30-october-2026-0615-gmt).
- WAKE-SESSION - answered a) on 30 October 2026; see [Owner answers](decisions.md#owner-answers-30-october-2026-0615-gmt).
- WAKE-DURABLE - answered a) on 30 October 2026; see [Owner answers](decisions.md#owner-answers-30-october-2026-0615-gmt).
- WORKTREE-OPTOUT - answered a) on 30 October 2026; see [Owner answers](decisions.md#owner-answers-30-october-2026-0615-gmt).
- HOST-REVIEW - supply the missing common-brief review packet. Answered a) on 30 October 2026, "proceed with the recommendation, then refine additional HOST-* based on that review"; see [Owner answers, 30 October 2026, 06:15 GMT](decisions.md#owner-answers-30-october-2026-0615-gmt). Delivered as the [merged host-sync report](design/host-sync/report.md).

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
