# ki.prj.ways-of-working queries

## Open

### WORKER-WAIT-MEANING - With worker means the worker role holds the work, not that a process is live

since 2026-10-29 · from run/sol-state-machine-readiness, split from WORKER-WAIT on 30 October at Kris's request; refines the parked STATE-MACHINE-DECISIONS · high now, no further work needed

**Context:** Kris's words under ROLES-ORCHESTRATOR name three roles: "the worker is a subagent, and then the thread agent is effectively the orchestrator of the state machine". The sentence "With worker means a run holds the work" is the read-back's, not Kris's, and the [state machine](design/work-state-machine.md) States table narrows it further to "a run of the work is in flight". ROLES-EITHER then lets a human hold any role, and a human worker never has a run in flight, so the narrow reading cannot describe a case Kris has already allowed. The banner makes its last glyph whose move it is, and its list already names a holder per item, `run/<name>` for `[running]` and `[queued]` alike. This part settles only the test; WORKER-WAIT-QUEUED, WORKER-WAIT-MIDTURN and WORKER-WAIT-GATED apply it to the disputed cases. Not taken under ACCEPT-BY-CRITERIA on 31 October: its option also settles the queued case, where the earlier blind review of WORKER-WAIT preferred another option, so test 2 is not met.

**Query:** Is With worker defined by assignment, the worker role holding the next move on at least one named unit, or by liveness, a run process being in flight?

**Options:**

a) (recommended, confidence high - the only reading that fits Kris's own role words, ROLES-EITHER's human worker and the banner's existing holder items, and it can be checked against `ki agent status` and the run queue) Assignment: the work is With worker while at least one authorised unit is assigned to a named worker holder, running or queued, so its next move is the worker side's; a run in flight is the common case, not the definition. The States table and the read-back's narrower sentence are restated to match.

b) Liveness: With worker only while a run process is in flight; every other moment of Working must sit in another inner state.

### WORKER-WAIT-QUEUED - Briefed work waiting only for a slot stays With worker

since 2026-10-29 · from run/sol-state-machine-readiness, split from WORKER-WAIT on 30 October at Kris's request · high now; the earlier blind review, which preferred an actual holder, also held that "a holder can own queued work without a live run"

**Context:** About three agents run per thread and the rest wait in the run queue, each with its brief, agent name and launch options; the dispatcher launches the next as a slot frees and honours each `DONE` gate, with no further decision from anyone. The banner already lists such a unit as `[queued]` with holder `run/<name>`. Current coordination says "Authorised work waiting for worker capacity stays with the worker; send to supervisor only for an actual decision or review", and the agreed `inform` arc needs a decision or review due, all dispatched work finished or a stuck worker, none of which a full queue is. This part covers only a unit that is briefed and queued; authorised work that cannot yet be queued is WORKER-WAIT-GATED. Not taken under ACCEPT-BY-CRITERIA on 31 October: the earlier blind review of WORKER-WAIT preferred another option, an actual holder, and its agreement with this part is not shown, so test 2 is not met.

**Query:** Is the work With worker when its remaining authorised units are briefed and in the run queue, waiting for a slot or for a `DONE` gate on another run of this work?

**Options:**

a) (recommended, confidence high - each unit has a named holder and will start without anyone's further move, so sending it to Kris would ask Kris for nothing) Yes: With worker, each unit shown `[queued] · run/<name>` and never counted as running or with you; the `pick up` and `receive by worker` arcs complete only when every authorised unit they restart is running, queued or recorded as gated.

b) No: entry to With worker waits for a launch, so after a direction the work stays in Handoff to worker until a slot frees, and a bootstrap that finds only queued work refines to With supervisor.

### WORKER-WAIT-GATED - Authorised work that nothing will start by itself

since 2026-10-29 · from run/sol-state-machine-readiness, split from WORKER-WAIT on 30 October at Kris's request · high after the blind review of 30 October; still to check before enforcement: REST-PORTABLE's settled rule that a short external wait may stay within Working "only when its actual holder/state is represented honestly"; a ruling on whether dated follow-ups, such as ORCA-REACH's due 6 November, are gates or ordinary next steps; and evidence of what the dispatcher does when a usage limit or provider outage stops a launch, which no run has verified

**Context:** Some authorised units cannot be briefed or queued yet because they wait on something outside this work's runs: another work's reply, a person, a date, a host, or model capacity lost to a usage limit or outage. Nothing will start them until someone acts on an event. While other units run or are queued the work is With worker anyway; the question arises only when gated units are all that remain. The current capacity rule would keep such work with the worker indefinitely, which can show a With worker with nothing running and no heartbeat for days. REST-PORTABLE makes At rest · waiting the honest state for a real wait, but at the cost of the full stop: drain, the portability checks, parked queries and a struck mark, even for a short reply. A live coordinator wakes at least every five minutes and reads `messages.md` at each wake, so it notices a reply line; once the session ends nothing does, unless a granted headless pass names the work. Not taken under ACCEPT-BY-CRITERIA on 31 October: three checks behind its confidence are still open (REST-PORTABLE's honesty rule, whether dated follow-ups are gates, and what the dispatcher does on a usage limit), so it is not a clean high and test 1 is not met.

**Query:** When gated units are all the authorised work that remains, does the work stay With worker or stop to At rest · waiting?

**Blind review (30 October, Codex, high effort):** agrees with a) at high confidence: responsibility can stay with an active coordinator that will observe and act on the gate, while a concluded session needs an explicit waiting handoff; it adds that an open session alone is not enough without an actual wake-and-check. Confidence lifted to high.

**Options:**

a) (recommended, confidence high - reviewed; honest about the holder while a live session that wakes and checks can act on the gate, and avoids an idle With worker once it cannot) Stay With worker, each gate shown as an item naming it, `[handoff]` where it is other work or a person, only while the orchestrator session that will act on it is open and waking; conclude and stop to At rest · waiting, the gate as release, before that session ends or when the gate is a date or outlasts it.

b) Stop to At rest · waiting as soon as nothing of this work is running or queued, however short the gate.

c) Stay With worker while any authorised gated unit remains, however long the gate, each shown as an item naming it.

### WORKER-WAIT-DELIVERY - Carry the high parts into the rollout now

since 2026-10-29 · from run/sol-state-machine-readiness, split from WORKER-WAIT on 30 October at Kris's request · high now, once the three high parts above are taken

**Context:** The [state-machine rollout plan](design/state-machine-rollout-plan.md) excludes WORKER-WAIT's two cases from U1's Harness contract fixtures and from the pilot pending an answer, and says WORKER-WAIT blocks only their enforcement. WORKER-WAIT-MEANING, WORKER-WAIT-QUEUED and WORKER-WAIT-MIDTURN change wording, fixtures and holder projections only: no state value, arc or diagram. WORKER-WAIT-GATED may change when a stop falls due, which touches the stop arc's trigger. Not taken under ACCEPT-BY-CRITERIA on 31 October: its confidence holds only once the three high parts are taken, and WORKER-WAIT-MEANING and WORKER-WAIT-QUEUED stay open, so test 1 is not met.

**Query:** Once the three high parts are taken, should U1 and U2 carry them now, with WORKER-WAIT-GATED left isolated until it is decided?

**Options:**

a) (recommended, confidence high - the three are consistency corrections inside the agreed shape, and holding them back leaves the mid-turn clause live in the standard) Yes: U1 restates States and moves, the States table and the role words to the adopted reading and adds running, queued and orchestrator-turn fixtures; U2's readers show queued apart from running wherever they project holders; WORKER-WAIT-GATED stays out of enforcement and the pilot until decided.

b) Hold every part of WORKER-WAIT out of U1 and U2 until WORKER-WAIT-GATED is decided too.

### HOST-CADENCE - Which cadence Rig prepares, without activating it

since 2026-10-29 · from run/sol-host-sync-design; rewritten 30 October from the [merged host-sync report](design/host-sync/report.md#host-cadence---which-cadence-rig-prepares).

**Context:** Kris's shape is hourly, publishing primaries "on the hour" and secondaries "five minutes later". Each territory has one primary host, so at any slot the two hosts touch disjoint territories, and the brief's extra two-minute host stagger protects nothing measured. No phase duration, sleep or wake behaviour has been measured, and offsets confer no exclusion or completion proof. The reviewers disagree: Claude recommends Kris's `:00` primary and `:05` secondary on both hosts at medium confidence, because the sets are disjoint and the attended run measures duration before activation; Codex recommends measuring attended passes first and keeping the hourly pattern only as a candidate, at medium confidence, because durations and wake behaviour are unverified. Both accept one attended run per host before any recurrence. An earlier blind review preferred measuring first. Nothing is activated either way. Not taken under ACCEPT-BY-CRITERIA on 31 October: the Codex design review and an earlier blind review preferred measuring first, option b), so test 2 is not met.

**Query:** Should Rig prepare Kris's hourly `:00`/`:05` cadence now, confirmed by each host's attended run, or leave the cadence unchosen until measured?

**Blind review (30 October, Codex, high effort):** agrees with a) at medium confidence: a provisional plan keeps Kris's stated shape while each host's attended measurement stays a hard gate on recurrence; if measurements fail, the cadence is revised before activation, and offsets give no locking or completion guarantee. Confidence lifted to high.

**Options:**

a) (recommended, confidence high - reviewed; Kris's own hourly and five-minute shape with disjoint per-slot sets, prepared provisionally with each host's attended run as a hard gate before any recurrence) Prepare hourly phases on both hosts: primary `:00`, secondary `:05`, a pull-only read-back shortly after, each host's first attended run confirming phase duration fits before activation.

b) Keep cadence unchosen; prepare attended passes only, and return a recurring plan once they have measured phase duration and wake behaviour.

c) Prepare the brief's staggered phases: Terra primary `:00` and secondary `:05`, Sol primary `:02` and secondary `:07`.

### HOST-COVERAGE - Who prepares the responsibility map, and from what start

since 2026-10-29 · from run/sol-host-sync-design; rewritten 30 October from the [merged host-sync report](design/host-sync/report.md#host-coverage---who-prepares-the-map-from-what-start).

**Context:** Kris asked for a dotfiles entry naming "per territory" the primary and secondary host. Both reviewers have Rig and chezmoi propose the map and Kris approve it before any configuration or operation, at territory grain with explicit exclusions, the chezmoi source as a named member and the resolved per-repository membership recorded per occurrence. [ADR-KI-PRINCIPAL-007](../../../Admin/Governance/Decisions/ADR-KI-PRINCIPAL-007-territory-seats-on-hosts.md) says "Each territory has one seat and one standby", and the sender's line named `seats.yaml` as the nearest entry, but seats mean coordination landing, not sync primacy. The reviewers disagree: Claude recommends starting the proposal from seat host as primary and standby as secondary, active-active territories primary on the hub, for Kris to confirm in one answer, and saying when HNR joins, at medium confidence; Codex recommends not inferring from seats, enumerating repository, branch and phase eligibility, and piloting one jointly nominated non-HNR, non-deploying repository, at high confidence. Not taken under ACCEPT-BY-CRITERIA on 31 October: the Codex design review preferred building the map without the seats, option b), so test 2 is not met.

**Query:** Should Rig and chezmoi start their proposed map from the seats, for Kris to confirm or amend, or build it without that starting point?

**Blind review (30 October, Codex, high effort):** agrees with a) at medium confidence: existing coordination placement is a useful seed for the proposal when Kris explicitly approves the sync roles and the receiving owners verify repository, branch and phase eligibility before configuration. Confidence lifted to high.

**Options:**

a) (recommended, confidence high - reviewed; Kris's per-territory words, the ADR's seat and standby pairing and the sender's pointer give a seed, while Kris's approval and the owners' eligibility check keep seats from being read as sync authority) Rig and chezmoi propose a territory-grain map starting from seat host as primary and standby as secondary, active-active territories primary on the hub, with exclusions, resolved membership and the point at which HNR joins; Kris approves or amends it before configuration; the first attended run uses one non-HNR, non-deploying repository.

b) Rig and chezmoi propose the map without the seats starting point, enumerating repository, branch and phase eligibility, and return it for approval before configuration, starting from one jointly nominated non-HNR, non-deploying pilot repository.

c) Kris supplies the map and pilot repository directly; the receiving owners verify eligibility and prepare its bounded plan.

### HOST-SECONDARY-PUBLISH - How secondary-origin changes reach Git

since 2026-10-29 · from run/sol-host-sync-design; rewritten 30 October from the [merged host-sync report](design/host-sync/report.md#host-secondary-publish---how-secondary-origin-work-reaches-git).

**Context:** Kris said "then five minutes later ... the secondary ones" and "the primary then needs to be able to read the secondary updates"; there is nothing to read unless the secondary publishes. Both reviewers reject the brief's pull-only secondary as failing that requirement. Both precedent syncs Kris ran on 28 and 29 October pushed unattended (SOL-SYNC also rebased), and the [Git authority standard](../../../.agents/skills/ki-git/references/standards-git.md#commit-publication-and-integration-authority) permits explicit standing publication authority. `mgit sync` pushes ahead-only branches by default, contrary to an adopted no-push-default request, so the recipe needs an explicit publish mode either way. The reviewers disagree on when publication may run: Claude recommends publishing ahead-only work fast-forward in the secondary phase with Kris's map approval as its grant, at medium confidence; Codex recommends preparing a distinct default-off capability, pull-only until separately authorised, at high confidence. Preparing it grants nothing. Not taken under ACCEPT-BY-CRITERIA on 31 October: the two design reviews disagreed on when publication may run and no blind review is recorded, so test 2 is not met; it also bears on unattended pushing, a security matter.

**Query:** Should Rig and the Git-tool owner prepare secondary publication as a default-off step that runs only under Kris's explicit standing grant?

**Options:**

a) (recommended, confidence high - both reviews independently reject pull-only as failing the requirement, and preparing a default-off step grants nothing) Prepare secondary publication in the same recipe: ahead-only, fast-forward, never forced, leaving diverged and dirty repositories to the host's Rig thread; off until Kris gives an explicit standing grant naming the territories, revocable by a stop word, which Kris may give in the same answer as the map approval.

b) Keep the secondary pull-only; secondary-origin changes reach Git only through separately authorised attended work, and read-back reports unpublished work as outside its coverage.

### HOST-READBACK - When primaries consume published return work

since 2026-10-29 · from run/sol-host-sync-design; rewritten 30 October from the [merged host-sync report](design/host-sync/report.md#host-readback---when-primaries-consume-returned-work).

**Context:** Kris said "we probably want to do a resync as well in short order after it". Next-hour read-back leaves secondary-origin work about 55 minutes before the primary consumes it. Both reviewers now prefer a prompt pull-only read-back, keeping next-occurrence recovery: Claude at `:10` on each primary, at medium confidence, because it is what Kris described and costs one fetch; Codex at `:10`/`:12` if the hourly candidate holds, at medium confidence, because exact slots depend on measured duration. An earlier blind query review agreed with next-hour read-back at high confidence; it predates both design reviews. Read-back matters only for published work, so it depends on HOST-SECONDARY-PUBLISH, and its slot follows HOST-CADENCE. It adds no publication authority or acknowledgement. Not taken under ACCEPT-BY-CRITERIA on 31 October: an earlier blind query review preferred next-hour read-back, option b), so test 2 is not met; it also rests on HOST-SECONDARY-PUBLISH and HOST-CADENCE, which stay open.

**Query:** Should each primary run a short pull-only read-back after the secondary phase, or wait for its next hourly occurrence?

**Blind review (30 October, Codex, high effort):** agrees with a) at high confidence: a prompt pull-only attempt cuts avoidable delay for already-published work without needing more publication authority, and must not gain conflict-resolution, reset or publication powers. Confidence lifted to high.

**Options:**

a) (recommended, confidence high - reviewed; both design reviews and this blind review prefer it on Kris's "in short order", superseding the earlier blind query review that backed b), with its slot following cadence) Prepare a pull-only read-back on each primary shortly after the secondary phase, its slot following HOST-CADENCE, keeping next-occurrence recovery for late or missing work and promising no immediate convergence.

b) Read published secondary-origin updates at the start of the primary's next hourly occurrence, stating the roughly 55-minute delay.

### PUBLIC-REPORT-AUDIENCE - Choose the response scope

since 2026-10-29 · from run/sol-private-report-assessment; the parked TERRA-LOCAL-REPORTS and PROTECTED-PUBLICATION refer to this audience question.

**Context:** Exact selected historical content remains reachable in locally verified published history, and one protected version remains current. Readership and indexing are unknown. Assessment approval did not authorise a remedy. The run's private evidence and response options are at `/Users/krisbrown/.local/state/ki/agents/ways-sol-resume-20261029/sol-private-report-assessment.private/`, which stays private and outside the repository. An independent review on 30 October (private report `/Users/krisbrown/.local/state/ki/agents/ki-prj-ways-of-working/public-report-review.report.md`, quoting no protected payload) reproduced the exact local selection, byte, reachability, current-path, recovery and evidence-integrity claims on a fresh pinned snapshot. It could not establish actual public serving, readership, indexing, the original audience instruction, credentials or harm, and found no evidence supporting an emergency intervention. It recommends the private exact-version response design at high confidence, narrowed so that current and historical publication stay unchanged during the task without that implying audience clearance or a presupposed removal outcome, using the existing inventory rather than wider discovery and keeping protected detail out of the repository; its alternative was deferral with a named owner and return point. Not taken under ACCEPT-BY-CRITERIA on 31 October: it concerns protected material and needs Kris to state the intended audience, which no one else can decide, so test 3 is not met.

**Query:** Should a separately bounded private response design follow, or should the owner explicitly retain the present publication posture?

**Options:**

a) (recommended, confidence high - resolves intended audience before selecting a remedy) Commission a private exact-version response design using the evidence locator above. Specify permitted audience and desired current/historical disposition; return a separate execution proposal with residual exposure stated. This authorises planning only, with no sanitisation, access change, history action, credential action or external contact.

b) Explicitly accept leaving current and historical publication unchanged, retaining the private evidence and unknown-readership qualification. This does not clear further public reuse.

c) Defer the response decision, naming its owner and return point; preserve evidence unchanged.

### PUBLIC-REPORT-RECOVERY - Decide private evidence durability

since 2026-10-29 · from run/sol-private-report-assessment; related to the parked TERRA-RECOVERY.

**Context:** Local recovery has been verified, but private off-machine recovery has not. The private evidence directory must remain outside the launcher's repository report home; no relevant source-store declaration was established for this operation. The 30 October independent review (same private report) confirmed local recovery: the bundle verifies, the recovery repository returns every selected version and all evidence hashes match, but every verified copy shares Sol's failure domain and no off-machine copy was inspected. It recommends option a) at high confidence: Kris identifies or approves a private destination independent of Sol, without guessing a source-store binding, then a separate task preserves a frozen manifest of the complete evidence chain and history bundle, verifies the destination copy and restores from it into an isolated location, reproducing the expected tip and every selected version hash, with originals kept and the runtime evidence kept out of cleanup until it succeeds. The retired Z session's private archive awaits the same preservation. Not taken under ACCEPT-BY-CRITERIA on 31 October: it needs Kris to name a private destination, and copying protected evidence off the machine cannot be undone, so tests 3 and 4 are not met.

**Query:** Should a later bounded task preserve the existing private recovery/provenance and this assessment at an explicitly approved private destination?

**Options:**

a) (recommended, confidence high - addresses the proved local-only gap without inventing a binding) Identify an approved private destination, or explicitly approve one, then separately authorise exact-manifest backup and restore verification with originals preserved. No transfer is authorised now.

b) Retain only the existing local copies and explicitly acknowledge the private recovery limitation; preserve this runtime evidence and its referenced archives.

### ORCH-NAME-DISPATCH - What to call the dispatch contract, its adapters and the command, without rename cost

since 2026-10-30 · from run/landscape · merged in [landscape-report](design/landscape-report.md) · rewritten after run/orch-name-fresh · split from ORCH-NAME after blind review 5, with ORCH-NAME-THREAD taking the thread skill and style

**Context:** On 30 October Kris asked: "If you put aside the rename cost, what is the feedback on naming then?" An independent naming review judged each unit with rename cost excluded. Portable run contract: `ki-delegation`, high - an orchestrator delegates a bounded job and a worker returns evidence or a question; `ki-dispatch` understates the brief, authority and return, and `ki-orchestration` would put the thread's name on one of its contracts. Adapters: `ki-delegation-orca` and `ki-delegation-paperclip`, high, provided the Paperclip skill's wider remit (company boundaries, readiness, memory, delivery policy) is described honestly rather than relabelled; `ki-agent-coordination-paperclip` has no natural Orca sibling. Launcher: `ki agent`, medium, on its own merits - `ki orchestrate` implies the executable owns the package, `ki delegate` names one action of a group that also observes, steers and closes, and `ki run` is too broad; this is the least certain unit. Both leading sets for the thread skill, in ORCH-NAME-THREAD, carry this same family. Moving `decide`, `reconcile`, `home` and `prompts` under `ki work` stays out of this query, under AGENT-HOME. Not taken under ACCEPT-BY-CRITERIA on 31 October: it renames a skill used across the estate, `ki-agent-coordination-paperclip` to `ki-delegation-paperclip`, so test 4 is not met.

**Query:** Setting rename cost aside, which names should the dispatch contract, its adapters and the command take?

**Blind review (30 October, Codex, high effort):** agrees with a), the family in both its pick and its runner-up for the whole naming query, which it rated medium overall because of the thread-skill split: delegation names the bounded worker contract, the Paperclip skill demonstrably governs company and repository boundaries, memory, readiness and delivery, so its wider scope must be stated explicitly and not narrowed for family symmetry, and Orca's installed `orchestration` skill already denotes Orca worker orchestration. It noted that the packet exposed an earlier review's preferences, so this review is not fully blind, and that the command's behaviour beyond its documented launcher role was not verified. Confidence lifted to high.

**Options:**

a) (recommended, confidence high - reviewed; the naming review and blind review 5 both choose this family on its merits, the reviewer verified the Paperclip skill's wider scope and Orca's separate `orchestration` skill, and the least certain unit is the launcher name, which both keep) Keep `ki-delegation`, slimmed, as the portable contract, with adapters `ki-delegation-orca` and `ki-delegation-paperclip`, the second renamed from `ki-agent-coordination-paperclip` with its wider remit stated; keep `ki agent`.

b) Keep the current names because of rename cost, as the earlier recommendation did: keep `ki-delegation`, `ki-agent-coordination-paperclip` and `ki agent`.

### LAYOUT-SHAPE - Which package layout to adopt

since 2026-10-30 · from run/package-layout · [design](design/package-layout/design.md)

**Context:** Kris set on 30 October that a work package keeps only its five files at the top level, with everything else grouped, possibly group first with briefs, design and reports beneath. Three shapes fit. A, kind-first: `reports/`, `briefs/` and `design/` folders, the cheapest change, but a matter stays spread across three folders and the tidy stays file by file. B, group-first with kind subfolders, as sketched: one folder per matter with `briefs/` and `reports/` inside, which needs an estate-wide ignore exception because `reports/` is ignored at any depth. C, group-first and flat: one folder per matter, with `<run>.brief.md` and `<run>.report.md` side by side and design files under plain names, needing no ignore change. The evidence suggests the sprawl comes mainly from retention, so the group earns its cost only as the unit of tidy. No shape has been piloted. Not taken under ACCEPT-BY-CRITERIA on 31 October: it picks a shape other than the group-first layout with briefs and reports beneath that Kris sketched on 30 October, so it is Kris's call and test 3 is not met.

**Query:** Which layout should the pilot use?

**Blind review (30 October, Codex, high effort):** agrees with a) at medium confidence: a flat matter folder tests the proposed organisational benefit with fewer structural dependencies; it adds that the pilot should use one small, explicitly bounded matter, and notes that the Context's claims about the sprawl's cause, the migration costs and the ignore behaviour were not verifiable from the packet. Confidence lifted to high.

**Options:**

a) (recommended, confidence high - reviewed; a flat matter folder tests the group as the unit of tidy with the fewest structural dependencies and avoids the ignore collision, and since nothing has been piloted the pilot takes one small, bounded matter) C, group-first and flat.

b) B, group-first with `briefs/` and `reports/` subfolders, plus the `ki-repo` ignore exception.

c) A, kind-first, with a stricter tidy cadence instead of groups.

### LAYOUT-GROUP-TIDY - Whether closing a group deletes it whole

since 2026-10-30 · from run/package-layout · [design](design/package-layout/design.md)

**Context:** Today's tidy deletes file by file, by explicit path, never folder-wide, and the steward judges each file's durable home. Under a group-first layout, a matter's files usually become homed together. The proposal is that once the steward judges a whole group closed, with outcomes homed, queries copied and design notes graduated or superseded, it deletes the group with one `git rm -r` naming that folder, in one commit, with Git keeping the history. Single-file deletion remains available. Not taken under ACCEPT-BY-CRITERIA on 31 October: it widens a deletion rule to whole folders and rests on LAYOUT-SHAPE, which stays open, so test 4 is not met.

**Query:** Should the tidy rule allow deleting one named, closed group folder whole?

**Blind review (30 October, Codex, high effort):** agrees with a) at medium confidence: one explicit group deletion is reviewable once every contained file has an evidenced disposition; it adds that before the one commit the steward enumerates the group's tracked contents and checks each file's durable home, copied queries and design-note disposition, preserving separately owned or unresolved material, because Git keeps committed versions but proves neither that knowledge was homed nor anything never committed. It recommends the policy only, not the deletion of any existing folder. Confidence lifted to high.

**Options:**

a) (recommended, confidence high - reviewed; one named group deletion stays reviewable when every file in it has an evidenced disposition checked before the commit, and Git keeps history; it widens a deletion rule, deletes no existing folder by itself, and is untested) Yes: a steward may delete one named, closed group in one commit.

b) No: keep file-by-file deletion inside groups.

### INBOX-ARMED - Keep the inbox watcher armed whenever a coordinating thread is open

since 2026-10-31 · from run/inbox-wake-design · [design](design/inbox-wake/design.md)

**Context:** Today the standard arms a background check only while runs are going; with Kris, nothing wakes the thread, so `messages.md` lines wait. Kris asked on 31 October for a watcher that stays armed while the work is with Kris, and this thread already runs one by hand. The watcher is a shell loop inside the open session, so it costs no model time until something changes and is not a scheduled agent.

**Query:** Should the inbox watcher stay armed whenever a coordinating thread is open?

**Options:**

a) (recommended, confidence high - it is what Kris asked for, every platform can at least run the shell part, and it is undone by deleting one rule) Arm it whenever the thread is open: amend `ki-coordination` with the Inbox watch rule in Proposal 1 of the design; stopped by "stop the wake", a hold, Finished or the session ending.

b) Only while runs are going: keep today's rule and leave this thread's watcher as a one-off.

c) Only on request: arm it in a thread only when Kris asks, as for this thread.

### INBOX-CADENCE - How often the watcher looks and when it wakes the thread

since 2026-10-31 · from run/inbox-wake-design · [design](design/inbox-wake/design.md)

**Context:** Kris's figures for this thread: look every two minutes, wake on a change, otherwise wake after fifteen minutes. The fifteen minutes matches the rule to sync at least every fifteen minutes, so one wake serves both. While runs are going, the existing five-minute heartbeat stays as it is.

**Query:** How often should the watcher look, and when should it wake the thread?

**Options:**

a) (recommended, confidence high - Kris's own numbers, aligned with the sync rule, and the model speaks only when something happened) Two-minute look, wake on change, else fifteen minutes (five while runs go), silent re-arm when nothing changed, as in Proposal 1 of the design.

b) Same, but a longer quiet bound of 30 or 60 minutes: fewer empty wakes, but the fifteen-minute sync then needs its own trigger.

c) Same, but say a one-line "nothing new" at each quiet wake: more visible, at the cost of noise in Kris's thread.

### INBOX-VERB - Put the watcher in one shared shell command in tools-ki

since 2026-10-31 · from run/inbox-wake-design · [design](design/inbox-wake/design.md)

**Context:** Every platform needs the same watching; only how its exit reaches the session differs. Nothing in `ki agent` or `ki work` watches `messages.md` today; until something does, each coordinator writes the loop by hand. The verb would belong to tools-ki, so this work could only ask for it by a `messages.md` line; the owning work decides how and when.

**Query:** Should the watcher become one shared shell command in tools-ki?

**Options:**

a) (recommended, confidence medium - the shape is clear, but the name and home inside `ki` are a tools-ki choice and nothing was prototyped) Ask for a read-only `ki work watch` verb: send one `messages.md` line to the work that owns tools-ki describing Proposal 2's verb; the `ki-coordination` surfaces carry the hand-written loop until it ships.

b) Keep the loop as a documented snippet only: no tooling change; each runtime binding carries the loop.

c) Extend `ki agent wait` instead: add `--timeout` and `--inbox <work id>` to the existing waiter.

### CODEX-WAKE - Prove Codex's queue as its wake before relying on it

since 2026-10-31 · from run/inbox-wake-design · [design](design/inbox-wake/design.md)

**Context:** Codex has no documented way for a background command to wake an open session. Codex 0.166.0 has `codex queue --thread <id> --message <text> --resume`, which may let an outside watcher wake a thread; nothing was run to prove it. WAKE-SESSION already says each runtime's wake must be proved before anyone relies on it.

**Query:** How should a Codex coordinating thread get its inbox wake?

**Options:**

a) (recommended, confidence medium - the command is documented locally but its effect on an open terminal thread is unknown) Prove it in one attended trial, and until then say plainly that a Codex coordinator checks the inbox only when Kris writes or a run event arrives: a bounded run tests it with Kris watching, on a scratch thread.

b) Treat Codex as having no inbox wake and coordinate waiting threads from Claude Code only.

c) Adopt `codex queue --resume` now as Codex's wake, proving it in use.

### SENDER-NUDGE - Should a sender also nudge the receiving thread?

since 2026-10-31 · from run/inbox-wake-design · [design](design/inbox-wake/design.md)

**Context:** The receiver's watcher sees a new line within about two minutes of the push, on any host. Orca's mailbox nudge is "best-effort attention only" by Orca's own words, reaches only a coordinator bound to an Orca Run, and needs the receiver's machine-local routing record, so a sender on another host cannot use it. ORCA-ROUTING already settled that an Orca send is only a wake, never the message.

**Query:** Should a sender also nudge the receiving thread after writing its `messages.md` line?

**Options:**

a) (recommended, confidence medium - the gain is two minutes at most, but whether the Orca wake works is untested) No nudge now; revisit after ORCA-SUBAGENT-PILOT shows whether the mailbox wakes an Orca chat: senders write and push their line, nothing more.

b) Optional same-host Orca nudge now: where the receiver has a verified routing record on this host, the sender adds a pointer-only `orchestration send` after its push.

c) Required nudge wherever the platform allows: every sender nudges when it can.

### ACQ-TEXT-RECHECK - Recheck the skill once Acquire publishes its decisions

since 2026-10-31 · from run/capture-skill

**Context:** The brief makes Acquire's own text the authority (ACQ020-OWNER). However, the decisions and the run that aligns Acquire's README, AGENTS and CAPTURE (`acq020-entry`) have not yet reached Acquire's remote. So the skill was aligned to the relayed wording rather than to Acquire's own text. Small differences are possible, for example in exactly when a README note "will do" instead of `original.txt`.

**Query:** Should the skill be checked against Acquire's own text once it is published?

**Options:**

a) (recommended, confidence high - it closes the only gap between the authority and the source I could read, at the cost of one short run) Once Acquire publishes its decisions and its entry-point changes, a short run compares them with the `ki-acquire` standard and corrects any wording that differs.

b) Treat the relayed wording as final and do no recheck.

### HOLDING-SCOPE - Does "nothing migrates out" cover the knowledge cards too?

since 2026-10-31 · from run/capture-skill

**Context:** GOAL-HOLDING-AREA makes Acquire a holding area for now: "nothing migrates out". The new wording says that neither captures nor cards leave Acquire, and that dispatch is on hold. The relayed decisions don't say outright whether the curated cards in `knowledge/` must also stay, or whether they may be reconciled into a Capital's graph.

**Query:** Does the holding rule keep the curated cards in Acquire as well as the captures?

**Options:**

a) (recommended, confidence medium - "nothing migrates out" reads as covering everything, but the decision text itself could not be read) Yes: cards and captures both stay in Acquire until Kris lifts the holding area. This is how the skill reads now.

b) No: only captures are held. Cards may be reconciled into their owning Capital's graph whenever they are ready, and the skill should say so.

### IDEAS-ROADMAP-STANDARD - Change where the roadmap standard sends ideas

since 2026-10-31 · from run/capture-skill

**Context:** IDEAS-IN-GRAPH says future ideas live in the knowledge graph as future concepts, not on the roadmap. The `ki-work-roadmap` standard ([Ideas and graduation](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-work-roadmap/references/standards-repository-roadmaps.md#ideas-and-graduation)) already keeps ideas out of the record queue. It sends concepts to a Capital's Emerging Concepts note. Other ideas go to `Idea:` bullets in Project or theme notes, or to `_IDEAS.md` beside the roadmap. Where every idea finally lives is IDEAS-HOME, which is still open in the [empty-board design](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/empty-board/design.md). I changed only the capture skill.

**Query:** Should the roadmap standard's ideas section change now, or wait for IDEAS-HOME?

**Options:**

a) (recommended, confidence medium - changing it now would settle IDEAS-HOME early, and the current text already keeps ideas off the record queue) Leave the roadmap standard as it is. Carry IDEAS-IN-GRAPH into IDEAS-HOME and change the standard once Kris settles that.

b) Change it now so that every future idea is a future concept in the graph, and retire `Idea:` bullets and `_IDEAS.md`.

### ACQUISITION-PROCESS-NOTE - Bring the Acquisition Process note into line

since 2026-10-31 · from run/capture-skill

**Context:** The skill's sources name the [Acquisition Process](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Processes/Acquisition Process/Acquisition Process.md>) note in Knowledge Islands Principal as the owner of the long-term lifecycle. That note still describes dispatch to each principal followed by Acquire removing its copy. It has no staging graph, no holding area and no item-by-item curation. It is canonical content, so changing it goes through the Enactment Process, and it was outside this run's scope.

**Query:** Should the Acquisition Process note be revised to match the 31 October decisions?

**Options:**

a) (recommended, confidence medium - the note now contradicts the skill, but Acquire's text should be settled first so the note isn't revised twice) After ACQ-TEXT-RECHECK, a bounded run drafts the revision under Ways of working for Kris's approval through the Enactment Process.

b) Leave the note until the holding area is lifted, and add one line saying that dispatch is currently on hold.

### CAPTURE-MODEL-SETTLED - Mark the choices the decisions have already settled

since 2026-10-31 · from run/capture-skill

**Context:** The capture-model brief that U12 wrote, [brief](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/capture-model/brief.md), puts seven choices to Kris. The 30 October decision on lean captures largely answers LEAN-CAPTURE. IDEAS-IN-GRAPH bears on IDEA-ROUTE. GOAL-HOLDING-AREA changes OPEN-ITEMS, whose recommended option has a closed item dispatch "as today". The brief has not yet had its blind reviews.

**Query:** Should the capture-model brief be updated to reflect these decisions before its reviews?

**Options:**

a) (recommended, confidence high - reviewers would otherwise test options that Kris has already decided) Before the reviews, a short run marks LEAN-CAPTURE as settled. It also records IDEAS-IN-GRAPH and the holding area against IDEA-ROUTE and OPEN-ITEMS, and leaves the other choices open.

b) Leave the brief as it is and let the reviews and the merged report pick up the decisions.

### WAKE-HOST - Where the headless coordinator pass may run

since 2026-10-30 · from run/landscape, split from WAKE · merged in [landscape-report](design/landscape-report.md)

**Context:** The Techne Programme Focus, set on 20 October, names two hosts, `vega` and sol, and allows agents on them only "in sessions the binding owner opens, with no unattended or scheduled agents". A launchd headless pass is a scheduled agent. WAKE-SUBSTRATE, a later decision in this work, does not amend a governance policy, so the pass may not run on sol or `vega` until the focus is changed through the Enactment Process. Terra, Kris's other Mac, is outside the focus. The job itself was sent to `ki.prj.chezmoi` and `ki.prj.mac-studio-setup`. The Claude review recommends terra first at medium confidence, noting that a pass sees only its own host's runs, because `ki agent status` is host-local, while sol is where most coordination and the Orca trial now run. The Codex review treats host permission as a separate decision and names no host. The design treated scheduled runs as out of scope, which both reviews call stale. Not taken under ACCEPT-BY-CRITERIA on 31 October: it is medium confidence and the blind review preferred option b), so tests 1 and 2 are not met; Kris kept it for the morning.

**Query:** On which host may the headless coordinator pass run?

**Blind review (30 October, Codex, high effort):** differs, prefers b) at medium confidence: the pass should observe the work it serves, so propose the bounded Enactment amendment for sol, with no pass there before approval; a terra pass sees only terra's runs, and terra's absence from the focus is not itself permission.

**Options:**

a) (recommended, confidence medium - needs no policy change and is reversible, but a terra pass sees only terra's runs and the reviewers did not agree on a host) Terra first, for works whose own decision names the pass; no pass on sol or `vega` unless the focus is later changed through the Enactment Process.

b) Propose an Enactment change to the Techne Programme Focus admitting the headless pass on sol, bounded as the standard sets it (shell-only trigger, named works only, `push` tier at most), so that the pass runs where coordination and Orca run.

c) No host for now: session wakes only, until a work needs a durable wake and names its host in its own decision.

### HOOK-STASH - Does a commit hook's own backup stash break the "never stash" rule?

since 2026-10-30 · returned by ki.prj.mac-studio-setup through State of play as a cross-cutting delegation-rule question; shaped by run/w-U7 in window AWAY-31-OCT · high after the blind review of 31 October; no rule changed

**Context:** Sessions and background runs share one checkout of each repository, often several at once, each committing only its own files. To protect one another's uncommitted work, the delegation standard and the coordinator style say never rebase, reset or stash a shared checkout. Every canonical pre-commit hook, kept by eight `ki-repo-*` skills in the harness, runs `lint-staged --quiet`. By default lint-staged 17.6.0 first records a backup as a stash entry without touching the files, and drops it after a successful commit. If a formatter fails, it resets the whole checkout to the last commit and puts the backup back, so another session's edit made in the seconds between backup and restore is lost. A hook killed part-way leaves the stash entry behind for the Git hygiene audit to report. `lint-staged --no-stash` makes no backup and no reset: on failure the commit simply stops and formatter changes stay for the committer to look at. It still briefly hides the unstaged parts of a file that is only partly staged, which is a smaller version of the same risk. A run on 30 October could not publish a report-only commit because its brief forbade stashing; Kris allowed that one commit as "a bounded exception, not a general change to the no-stash rule".

**Query:** Should the "never stash" rule cover the backup stash that lint-staged makes inside our pre-commit hooks?

**Blind review (31 October, Codex, high effort):** agrees with a) at high confidence, from the installed lint-staged source: the failure path resets the whole checkout whoever started it, so exempting the hook would exempt exactly what the rule guards against. It adds that `--no-stash` does not make concurrent commits fully safe, because hiding partly staged files still rewrites working files, so commits should keep to isolated worktrees or a short exclusive window, failure and partial-staging behaviour should be tested before rollout, and losing automatic rollback should be stated. It also found ki-principal's installed hook differs from the harness asset, which is a separate conformance matter.

**Options:**

a) (recommended, confidence high - reviewed: the risk is the hook's reset of the whole checkout on failure, which only removing the backup takes away, and the reviewer reached the same course independently from the source) Keep the rule absolute, hooks included: change every canonical pre-commit asset to `lint-staged --quiet --no-stash` and roll it out through each repository's normal conformance route, after testing failure, interruption and partly staged files; a leftover `lint-staged automatic backup` entry is reported, never dropped.

b) Read the rule as covering only stashes a session runs itself, so the hook's backup is outside it, and say so in one sentence in the delegation standard and the coordinator style; hooks stay as they are.

c) Leave both the rule and the hooks as they are, and have background runs stop before committing in any repository whose hook stashes, leaving the commit to the coordinator.

### FINISHED-TIDY-KICK - Let State of play delete a Finished work's leftover folder itself?

since 2026-10-31 · relayed from personal.reg.acquire-intake at Kris's request on 30 October; shaped by run/w-U8 in window AWAY-31-OCT · high after the blind review of 31 October; no rule changed · [design note](design/finished-tidy-kick.md)

**Context:** You asked to "sort out the method so that the kick actually gets the folder deleted". When a piece of work finishes, its coordinator is meant to delete the work folder at the next mark, but once the thread ends nobody holds the work, so that mark never comes. Three things then fail together. The tidy check (FOLDER-4) only flags a Finished folder after a closing mark, so a folder left before that mark is never flagged. The only remedy State of play has is a line in that work's `messages.md`, which nobody reads, because nothing reopens Finished work. And the method forbids State of play from tidying another work's folder. [ki.prj.knowledge-acquisition](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.knowledge-acquisition/state.md) has been stuck like this since 20 October; whether to close that folder is the separate KA-CLOSE query in [ki.sop.main](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.sop.main/queries.md). A masked blind review on Codex chose option a) on its own at high confidence, but said it is not plainly within your words: you agreed a finished work deletes its own folder, and this makes a named exception to the rule that territory work never tidies another work's folder, so it needs your adoption. The wording is drafted and tested, and nothing has changed in the harness.

**Query:** Should State of play close a Finished work's leftover folder itself, under strict checks, instead of sending it a message nobody reads?

**Options:**

a) (recommended, confidence high - reviewed: the blind review reached the same course on its own; it is the only option that both finds every stranded folder and names who deletes it, and Git keeps the folder, so a delete is easily undone) The tidy check flags every Finished folder. At a mark you authorise, whose report names the folder, State of play checks that every decision and other durable fact is homed, `design/` is resolved, findings are settled, no query is open, no message is waiting and no run is live; it then archives the runs with `ki agent close`, never using your waiver, and deletes the folder in one commit. If any check fails, it deletes nothing and asks you instead. A run applies the drafted wording to the harness, with an independent review before it is pushed.

b) Keep today's rule that only the work itself deletes its folder. Fix only the tidy check so it flags every Finished folder, and have State of play bring each one to you as a query at its mark.

c) Have the finishing coordinator delete the folder in the same sitting as your `finish`. This stops new cases, but does nothing for folders already left behind, such as knowledge acquisition.

## Answered

- ORCA-REACH - answered a) on 30 October 2026, follow-up due 6 November 2026; see [Owner answers](decisions.md#owner-answers-30-october-2026-0615-gmt).
- AGENT-HOME - answered a) on 30 October 2026, follow-up due 2 November 2026; see [Owner answers](decisions.md#owner-answers-30-october-2026-0615-gmt).
- WAKE-SESSION - answered a) on 30 October 2026; see [Owner answers](decisions.md#owner-answers-30-october-2026-0615-gmt).
- WAKE-DURABLE - answered a) on 30 October 2026; see [Owner answers](decisions.md#owner-answers-30-october-2026-0615-gmt).
- WORKTREE-OPTOUT - answered a) on 30 October 2026; see [Owner answers](decisions.md#owner-answers-30-october-2026-0615-gmt).
- HOST-REVIEW - supply the missing common-brief review packet. Answered a) on 30 October 2026, "proceed with the recommendation, then refine additional HOST-* based on that review"; see [Owner answers, 30 October 2026, 06:15 GMT](decisions.md#owner-answers-30-october-2026-0615-gmt). Delivered as the [merged host-sync report](design/host-sync/report.md).
- ORCA-ENV-LEAK - acted on 30 October 2026 under Kris's ORCA-SUBAGENTS words: sent to ki.prj.tools-burndown; see [ORCA-SUBAGENTS](decisions.md#orca-subagents---ki-agent-runs-appear-as-orca-sub-agents-30-october-2026-1610-gmt).
- WORKER-WAIT-MIDTURN - An orchestrator turn moves nothing. Taken a) under ACCEPT-BY-CRITERIA on 31 October 2026; see [Owner answers during AWAY-31-OCT](decisions.md#owner-answers-during-away-31-oct-0136-gmt-31-october-2026).
- AMEND-RACE - Guard amends in a shared checkout. Taken a) under ACCEPT-BY-CRITERIA on 31 October 2026; see [Owner answers during AWAY-31-OCT](decisions.md#owner-answers-during-away-31-oct-0136-gmt-31-october-2026).
- ORCH-NAME-THREAD - answered b) by Kris on 31 October 2026, keep `ki-coordination` and `ki-coordinator`; see [Owner answers during AWAY-31-OCT](decisions.md#owner-answers-during-away-31-oct-0136-gmt-31-october-2026).
- LAYOUT-PILOT-ORDER - When the pilot moves files. Taken a) under ACCEPT-BY-CRITERIA on 31 October 2026; see [Owner answers during AWAY-31-OCT](decisions.md#owner-answers-during-away-31-oct-0136-gmt-31-october-2026).
- REVIEW-CHALLENGE - Let reviews challenge earlier decisions, visibly. Taken a) under ACCEPT-BY-CRITERIA on 31 October 2026; see [Owner answers during AWAY-31-OCT](decisions.md#owner-answers-during-away-31-oct-0136-gmt-31-october-2026).
- REVIEW-LIFT - Precedent earns no confidence. Taken a) under ACCEPT-BY-CRITERIA on 31 October 2026; see [Owner answers during AWAY-31-OCT](decisions.md#owner-answers-during-away-31-oct-0136-gmt-31-october-2026).
- READ-FEEDBACK-NOW - Feedback packages before the Observatory can write them. Taken a) under ACCEPT-BY-CRITERIA on 31 October 2026; see [Owner answers during AWAY-31-OCT](decisions.md#owner-answers-during-away-31-oct-0136-gmt-31-october-2026).
- ORCA-CLOSE-OUT - Make worker release part of KI coordinator close-out. Taken a) under ACCEPT-BY-CRITERIA on 31 October 2026; see [Owner answers during AWAY-31-OCT](decisions.md#owner-answers-during-away-31-oct-0136-gmt-31-october-2026).
- ORCA-SUBAGENT-PILOT - Prove the Orca worker path before changing tools-ki. Taken a) under ACCEPT-BY-CRITERIA on 31 October 2026; see [Owner answers during AWAY-31-OCT](decisions.md#owner-answers-during-away-31-oct-0136-gmt-31-october-2026).
- ORCA-PLACEMENT - Which Orca route Part B takes. Taken a) under ACCEPT-BY-CRITERIA on 31 October 2026; see [Owner answers during AWAY-31-OCT](decisions.md#owner-answers-during-away-31-oct-0136-gmt-31-october-2026).
- ORCA-QUEUE - answered a) by Kris on 31 October 2026, Orca first while the parent chat is live, detached otherwise; see [Owner answers during AWAY-31-OCT](decisions.md#owner-answers-during-away-31-oct-0136-gmt-31-october-2026).

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
