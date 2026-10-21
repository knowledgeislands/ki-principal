---
note_type: streams/design
status: draft
---

# Agent control and launch-defaults contract

This is the proposed build contract for CONTROL-CONTRACT and DEFAULTS-CONTRACT, for Kris's acceptance before implementation. Kris agreed the drafting step on 21 October 2026, in [owner answers](../decisions.md#2026-10-21-1410-bst---owner-answers), extended by [the afternoon grant](../decisions.md#2026-10-21-1411-bst---mark-afternoon-unattended-run). The queries at local Git revision `6ed6a194`, headings CONTROL-CONTRACT and DEFAULTS-CONTRACT in `+/_WORK/ki.ways-of-working/queries.md`, ask for these observable contracts, process ownership, continuation binding and a complete role mapping. Acceptance of this draft must be recorded in that decisions log; draft status grants no command, runtime or publication authority.

## Scope and ownership

[tools-ki](../../../../../tools-ki/README.md) owns command parsing, runtime adapters, process control, queue transactions, receipts and tests. The [KI Agentic Harness](../../../../../ki-agentic-harness/README.md) owns the portable behaviour in `ki-delegation`, the wake and steering rules in `ki-coordination`, authority-footer wording and generated prompt/report surfaces. This island holds this proposal and Kris's acceptance. No new roadmap record, scheduling service, hosted notifier or estate rollout is part of this build.

The build order is: accept this contract and its model bindings; one tools-ki run implements and verifies the commands in isolation; the Harness then aligns its skill text and generated surfaces against that verified interface; finally the coordinator reviews the combined evidence before enabling any wake window. The tools-ki run must report a Harness handoff for the coordinator to send as one message to the receiving work. It has no authority to edit the Harness. Release, installation and live activation remain separately authorised work.

## Shared identity, states and receipts

A command resolves the run's recorded work home, independently of the target working directory. It refuses an ambiguous home, a foreign machine's runtime packet or a mismatched work identity. It never searches process names, guesses a repository from a basename or treats a PID alone as ownership evidence.

A launched attempt has an immutable identity: run, agent, attempt number, random launch token, runtime, physical working directory, process birth identity, session/process-group identity and the launcher that owns it. A queue entry has its own immutable entry ID, reserved attempt and launch token before dispatch. Receipts name these identities and UTC timestamps, with readable local times in text output. Existing attempts without adequate ownership evidence remain observable but cannot be signalled automatically; they need a new explicitly authorised launch, not retroactive trust in their PID.

Every new control supports `--json`. A versioned receipt (`ki/agent-control/v1`) includes operation ID, operation, run, target identity, previous state, resulting state, outcome, reason, timestamp and associated event sequence where applicable. The durable machine-local journal is written before an external effect; a later receipt records the observed outcome. Retries reuse an operation ID through `--request <id>` and return the recorded outcome, unless the same ID is presented with different arguments, which is refused. Exit 0 means a confirmed result, including an explicit idempotent no-op; exit 1 means refusal, conflict or unconfirmed outcome; exit 2 means invalid usage. An acknowledged request alone is never a successful stop or wake.

Queue state is `queued -> claimed -> started`, or `queued/claimed -> cancelled` before spawn. Attempt execution is `held/running -> stop-requested -> stopped`, or `stop-requested -> stop-timeout` while still live. Natural `done` and `failed` remain distinct. These are runtime states, not new states for the work package. No control changes a roadmap record or writes a work-package state, acceptance, report or `DONE` on the worker's behalf.

Extend the append-only run-event vocabulary with `stop-requested`, `stopped` and `dequeued`. A timeout or lost ownership produces a `blocked` event with the operation ID. `wait --next` returns each unseen `stopped` or `dequeued` event as well as today's terminal/query events; `watch` and status render them. A stopped or dequeued predecessor closes its dependants' gates as blocked; it never satisfies a `DONE` gate. `ALL FINISHED` requires an empty queue and no held, running, claimed or unconfirmed live attempt. An armed watcher alone does not keep a run busy. Receipt retries and event derivation cannot emit duplicate terminal events.

## Stop

Proposed surface: `ki agent stop <run> <name> --attempt <n> --reason <text> [--grace <seconds>] [--request <id>] [--json]`. The attempt is required so a delayed instruction cannot stop a later relaunch. Grace defaults to 30 seconds and accepts 1-120 seconds. The command applies to one launched or held attempt. A queued entry is refused with its dequeue command; it is not silently removed.

Stop is signal-driven graceful termination, not a promise that the worker has completed a cooperative checkpoint. Under the per-run control transaction, record the stop request and fence that attempt against a gate opening or a delayed spawn. Verify the launch token, process birth identity and exclusive session/group ownership immediately before sending SIGTERM to that owned group. The group must exclude the coordinator, dispatcher, watcher and other attempts. The runtime adapter must establish and test this ownership on the supported host; if it cannot, refuse the signal.

A held gate process and any runtime it could start share the stop fence and ownership record. Their transition to runtime launch is serialised with stop. Stop cannot acknowledge success while a gate process can still launch the worker. Observe the owned group until it is absent or grace expires, rechecking ownership throughout. Record `stopped` only after no owned process remains. If the attempt completed naturally first, return `already-terminal` with that natural outcome. A dead process without a prior stop or successful report remains `failed`, not successful completion. A repeated confirmed stop returns `already-stopped`.

At grace expiry return `stop-timeout`, exit 1, leave the attempt visibly live and emit `blocked`. No automatic SIGKILL or escalation option is included in this first build. A changed or unavailable ownership identity gives `ownership-unverified`, sends no signal and requires the coordinator's attention. If SIGTERM was sent but observation becomes uncertain, retain an unconfirmed stop and never describe it as stopped.

The coordinator uses stop only on an explicit owner instruction naming the work, or a stop condition explicitly preauthorised in that attempt's brief. A new owner message is steering, not such an instruction. Stop never discards edits, rolls back a transaction, deletes a worktree or lock, commits files, accepts work or marks the run done. The worker may leave a partial effect; the receipt points the coordinator to the preserved log, status and working directory for review.

Today's gap: `AgentProcesses` exposes launch, liveness and sleep only; attempts record a PID and launch options, not a verifiable process-ownership contract. There is no stop command, stop fence or stopped event. Build the process-port operations and attempt identity first, including safe refusal for old packets.

## Dequeue

Proposed surface: `ki agent dequeue <run> <name> --entry <id> --reason <text> [--request <id>] [--json]`. Queue and status expose the entry ID. Dequeue means prevent this queue entry from starting; it does not mean stop a worker or pause the dispatcher.

Queue append, dispatcher claim, dequeue, held-to-runtime transition and final spawn authorisation use one per-run transaction protocol with atomic persistence and a recoverable claim journal. A dispatcher records a claim before taking an entry out of the pending view. It must revalidate that claim and its cancellation fence inside the spawn-authorisation transaction. Holding the transaction through spawn and recording the returned process identity makes the winner observable; a crash in that interval leaves an unconfirmed claim that blocks replacement launches until reconciled. Never infer that an entry disappeared because it launched successfully.

If cancellation wins while queued or claimed but not spawned, write a persistent tombstone and a `dequeued` event; return `cancelled-before-start`. Preserve the brief and launch options as evidence. If spawn won, return `already-started`, exit 1, with its attempt identity and the exact stop command. If a prior cancellation won, return `already-dequeued`. A completed attempt returns `already-terminal` without pretending it was dequeued; an unknown entry is refused. A relaunch or deliberate requeue uses a fresh entry and attempt identity and cannot inherit or erase an earlier cancellation.

After restart the dispatcher honours tombstones and reconciles unconfirmed claims before taking more work. It cannot clear a cancellation by rewriting an older queue snapshot. Dequeue never signals a process, deletes a prompt or packet, reprioritises other entries, cancels dependants silently or broadens the concurrency limit.

Today's gap: dispatch reads `queue.jsonl`, removes a selected entry and then calls launch. There is no claim acknowledgement, cancellation tombstone or transaction joining dequeue to dispatch. Reusing only the events-file lock is insufficient unless all these queue and launch transitions participate in the same protocol.

## Bounded wake

Proposed surfaces:

- `ki agent wake arm <run> --runtime <claude|codex> --session <native-id> --until <UTC-time> --authority <local-path#heading> [--request <id>] [--json]`.
- `ki agent wake status <run> [--json]`.
- `ki agent wake disarm <run> --binding <id> --reason <text> [--request <id>] [--json]`.

Arming requires an explicit owner-authorised autonomy window recorded at the supplied decision reference. `--until` is an absolute RFC 3339 UTC expiry, later than now and no later than the cited grant. An omitted expiry or decision is an error. The tool checks that the local reference exists and records its digest; the coordinator is responsible for the grant's meaning. No command invents, extends or renews authority. Disarm is local and idempotent and never stops workers or the coordinator.

The immutable binding contains the work ID and physical work home, exact native runtime/session ID, owner-decision reference and digest, expiry, registration event cursor and one continuation lease. The adapter verifies that the native session belongs to that work and can be resumed locally without opening a new conversation. Reject a missing, ambiguous, busy or unsupported session; never choose the most recent session, an unrelated terminal or a GUI tab. A change in work-home identity or decision digest suspends the binding. A session being quiet is not evidence that it is idle: interactive turns and resumed turns must participate in the same exclusive continuation lease. An adapter unable to prove that exclusion refuses arming.

Arming starts one detached watcher, with a receipt including binding and watcher identities. It survives the launching terminal and watches events without consuming `wait --next`'s cursor. The default cursor is the current tail: old events do not cause surprise continuations. Within the window, a new `done`, `failed`, `blocked`, `needs-owner`, `stopped` or `dequeued` event is eligible; plain status lines, milestones and five-minute heartbeat ticks are not. Coalesce eligible unseen events into one pending continuation, with their sequence range. Wake uses the current work send line as its message and adds only the event identities and the instruction to re-read the package, not a new brief or a new authority grant.

Binding states are `armed`, `pending`, `resuming`, then `armed` after acknowledged delivery; `expired`, `disarmed`, `suspended` or `error` end automatic delivery. Check expiry, grant digest, work state and session lease immediately before every resume. On hold, Finished or a handoff to the supervisor suspends automatic continuation, leaving the events visible. A busy session keeps one pending batch until idle or expiry, with no parallel resume. Expiry ends the watcher and pending automatic delivery, leaving workers and unread coordinator events intact.

Use a persistent delivery key comprising binding ID and event sequence range. Record the pending delivery before invoking the adapter. The adapter must return a native acknowledgement tying the same session to that key. Commit the delivered cursor only on that acknowledgement. A crash after invocation but before acknowledgement gives `delivery-unconfirmed`: do not retry blindly or claim exactly-once native delivery. Surface it as an error requiring manual reconciliation; restart may retry only a delivery proven not invoked. Confirmed delivery, repeated arming requests and watcher restarts must not resume the same batch twice. A second binding is refused while one is armed or a continuation remains in flight. Disarm or expiry cannot interrupt an already acknowledged continuation; the resumed coordinator must itself obey the grant's expiry before launching more work.

Wake never creates a new session as a fallback, sends email or chat, changes a scheduler, resumes without a matching grant, launches workers directly or accepts work. It never changes work-package state itself. Native continuation is a required local adapter capability; if either runtime cannot establish ownership, busy-state exclusion and acknowledgement, that adapter remains explicitly unsupported and its wake build is returned as a query rather than simulated with a fresh `exec` call.

Today's gap: `wait --next` prints an event and advances its read cursor; `watch` prints events/status and exits at completion. Neither binds or resumes a coordinator session, records an autonomy window or implements a continuation lease and delivery journal. The Harness describes OOS-WAKE as agreed but explicitly leaves out-of-session runs waiting for the owner's send line until tooling ships.

## Launch defaults

Add `--role <mechanical|plan|build|review|accept|prune|release>` and `--authority <local-path#heading>` to both launch and queue. Add `--dry-run --json` to resolve and display the effective request, sources of each value, required authority and any refusal before writing a packet, creating a worktree or spawning. A queued request freezes that resolved result and its profile revision; dispatch validates it again but never silently re-resolves it against changed defaults.

### Proposed mapping

The following is a complete proposed role mapping, not evidence of a validated fleet default. Profile names are tool-owned, versioned defaults, not provider aliases. The native model IDs below are candidates for Kris to confirm. Local run metadata proves use of `claude-opus-5-5`, but does not prove either Codex candidate or their relative capability. Confirm the native IDs and local suitability before enabling these defaults; do not translate a family name into a guessed ID. The dated `ki-tokenomics-chatgpt` evidence explicitly requires evaluation before a durable fleet recommendation.

| Role | Runtime | Model profile | Effort | Footer |
| --- | --- | --- | --- | --- |
| mechanical | codex | codex-standard | medium | none |
| plan | codex | codex-strongest | high | none |
| build | claude | claude-worker | high | none |
| review | codex | codex-strongest | high | none |
| accept | codex | codex-strongest | high | prune |
| prune | claude | claude-worker | high | prune |
| release | claude | claude-worker | high | release |

Proposed profile pins: `codex-standard = gpt-6.1-sol`, `codex-strongest = gpt-6-astra`, `claude-worker = claude-opus-5-5`. Review always resolves to the accepted strongest Codex pin, never the runtime's unnamed default. High effort is the explicit judgement default, not a claim of maximal supported effort; an explicit supported higher effort may override it. The build must refuse unresolved, unavailable or unsupported model/effort combinations without falling back or starting an agent. Offline fixtures can prove that refusal, but cannot prove live availability or model suitability. Acceptance of pins must therefore cite prior local evidence or separately authorised evaluation; this draft launches none.

These roles describe background runs. Interactive coordinator defaults are unchanged. A review must still be independent of the delivery it reviews; selecting Codex does not prove independence on its own.

### Precedence and safety

Resolve each field in this order: explicit option, accepted role profile, legacy default only when no role was supplied. Do not infer a role from an agent's name, prompt text, folder or file suffix. Unknown roles fail. A role-free invocation retains today's Claude runtime, omitted model/effort and `none` footer for compatibility, and its receipt labels that path `legacy`. Role-based launches must pin model and effort.

Explicit options win only within the role's constraints. Changing runtime requires an explicit model valid for that runtime; it cannot inherit a model from the other runtime's profile. The review role refuses a runtime/model below its accepted strongest Codex binding. An acceptance run refuses a non-prune footer; prune and release roles similarly require their matching footer. An explicit footer above `none` for any other role requires cited owner authority and cannot make a review into an implementation run. Invalid combinations fail before any launch side effect. Explicit extra directories, gates, worktree and repository options retain their existing meanings and do not acquire wider defaults.

A role supplies no owner authority. `push`, `prune` and `release` require an explicit existing `--authority` reference to the bounded decision, recorded in the launch receipt and brief. Acceptance additionally requires the brief to state the exact records, independent review prerequisite and explicit owner override of the footer's acceptance ban. The CLI records and displays that declaration for review; it does not infer approval from the presence of a path or claim to interpret the owner's prose. A missing acceptance declaration is a preflight refusal. Harness wording must make clear that the cited task-specific acceptance grant takes precedence and applies only to its named records. Do not remove the blanket ban globally or let `--role accept` supply the grant. `--allow fetch` and `--allow machine` remain explicit and never follow a role automatically.

The proposed accept-to-prune mapping follows C3's recommendation, but prune also carries push and deletion authority. The cited decision must cover those capabilities or explicitly narrow them in the task; otherwise refuse the profile and return the authority gap. Accepting and pruning remain separate lifecycle actions with the required terminal-state commit before any deletion. A footer is a constraint and an authority description, not proof that any named record was accepted.

Extend `.launch.json` with schema version, role, effective runtime/model/effort/footer/grants, per-field source, profile revision, authority reference/digest, entry/attempt identity and work home. Preserve the effective values through queueing, gates and relaunch; a deliberate new request may choose new values, but never rewrites an older attempt's receipt. Print the effective selection in launch and queue receipts so the coordinator can see a wrong model before it runs.

Today's gap: launch and queue default to Claude and `--rules none`, omit model and effort unless supplied and have no role option. Runtime adapters pass explicit model/effort through. `.launch.json` records runtime, optional model/effort and workdir/worktree, not role, footer, grants, provenance or authority. The prune footer explicitly says never accept work; it cannot become acceptance authority merely by being selected.

## Acceptance tests for the build

Use injected process, clock, filesystem and continuation ports. These tests run offline with no live worker, native session, credential, signal to an unrelated process or external service. Keep command-help and JSON-schema assertions alongside behaviour tests. The build report distinguishes passed fixture tests from native adapter capabilities still unproved.

1. Identity and compatibility: legacy packets remain readable; old or forged PID-only ownership is refused without a signal. Relaunch allocates a new attempt/token. A delayed stop cannot target that attempt. Invalid arguments, foreign homes and duplicate operation IDs with changed payloads leave all state unchanged.
2. Stop: test running and held attempts, natural completion racing SIGTERM, already-stopped retries, dead-before-request failure, PID reuse, foreign process groups, permission errors and ownership loss after signalling. Test group disappearance and grace expiry with an injected clock. Exactly one stop receipt/event is derived, no SIGKILL is sent and no unrelated process is touched.
3. Stop against a held gate: exercise both orders of gate-open and stop, including a crash during transition. A confirmed stop leaves no possible later spawn; uncertain state blocks replacement work. A stopped predecessor blocks its dependants and never opens a `DONE` gate.
4. Dequeue: force both orders of dequeue and dispatcher claim/spawn, concurrent appends, repeated cancellation, restart from claim journal and crash around spawn acknowledgement. Cancellation that wins guarantees zero spawn; spawn that wins returns the stop identity without claiming cancellation. No queue entry is lost or resurrected and no evidence file is deleted.
5. Events: status, watch, `wait --next`, gate evaluation and completion detection agree on stopped/dequeued/timeout states. Two observers emit one terminal event. The new wake cursor does not consume the waiter's cursor, and a stopped attempt is not success.
6. Wake guards: missing/expired/unbounded authority, changed decision digest, wrong work/session, busy or unsupported session, On hold, Finished and supervisor handoff each prevent resume. A successful arm is detached and unique. Expiry or disarm leaves workers and events intact. No old event wakes on arming.
7. Wake delivery: multiple events coalesce; exactly one continuation lease can be held; an event arriving during continuation remains pending. Test two watchers, watcher restart, native rejection, acknowledgement loss and crash before/after invocation. Confirmed deliveries deduplicate; unconfirmed delivery suspends rather than duplicates. A continuation uses the exact bound session and current send line and cannot start after expiry. Unsupported native exclusion/acknowledgement cannot be reported as a passed adapter.
8. Defaults: test every role and profile, the role-free legacy path, every explicit-field precedence case, changed runtime/model combinations, strongest-review and footer mismatches, missing authority/acceptance declaration, unsupported effort/model and unavailable profile pins. Refusal creates no worktree, prompt or process. A role never adds a grant, acceptance, publication or deletion authority by implication.
9. Persistence: queue, dispatch, held launch and relaunch preserve frozen selections and authority evidence, including when defaults change while queued. Dry-run has no mutation. Receipts contain the effective values, provenance and immutable IDs, with stable schema and exit codes.
10. Repository gates: the tools-ki run passes its required lint, types, unit/integration and full audit gates in its own isolated offline home, compares warnings against its unchanged baseline and reports any native limitation as a query. The Harness follow-up verifies portable wording, authority footers, generated surfaces and relevant hook/prompt tests without claiming live wake support. No release or live apply is part of acceptance of this draft.

## For Kris

- STOP-POLICY: confirm SIGTERM to a verified owned attempt group, a 30-second grace and no automatic hard kill. Recommendation: accept; uncertainty remains visible and partial work is preserved.
- QUEUE-CANCEL: confirm a transactional cancellation fence and an explicit already-started refusal requiring stop. Recommendation: accept; dequeue must never pretend it stopped a running worker.
- WAKE-BOUNDARY: confirm exact native-session binding, an absolute owner-authorised expiry, terminal/query events only and no automatic retry after uncertain delivery. Recommendation: accept, with a runtime left unsupported until its adapter proves session exclusion and acknowledgement.
- ROLE-PINS: confirm the seven-role table, high judgement effort and proposed native model pins after local validation. Recommendation: accept the role/precedence policy now; enable pins only once the cited runtime IDs and suitability are evidenced, with no unnamed runtime fallback.
- ACCEPT-AUTHORITY: confirm accept uses prune only with explicit bounded owner authority and the task's acceptance override; the role itself grants nothing. Recommendation: accept this guard; if acceptance should exclude prune's push/deletion capabilities entirely, return that one mapping for revision before build.
- BUILD-ORDER: confirm one tools-ki implementation run followed by a separate Harness wording follow-up and combined review. Recommendation: accept; neither this draft nor the command build activates a watcher or authorises release.
