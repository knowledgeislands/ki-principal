---
note_type: streams/design
status: draft - October 2026
work: ki.prj.orca-evaluation
run: ki-prj-orca-evaluation
agent: trial-plan
written_at: 2026-10-30T11:20:00Z
author: Written with Claude
---

# Orca trial plan - the remaining units

**Owning work:** `ki.prj.orca-evaluation` · **Inputs:** [the trial log](orca-trial.md), [the landscape report](../../ki.prj.ways-of-working/design/landscape-report.md), [decisions](../decisions.md) · **Status:** draft for Kris's decisions; nothing here has been dispatched, and this package still launches through `ki agent` until it opts in.

## Contents

- [Bounds](#bounds)
- [Shape of the trial](#shape-of-the-trial)
- [Unit 1 - WAKE: the session wake, proved in Claude Code and Codex](#unit-1---wake-the-session-wake-proved-in-claude-code-and-codex)
- [Unit 2 - LIVE: Orca's live-layer recovery map](#unit-2---live-orcas-live-layer-recovery-map)
- [Unit 3 - SKILL: the Orca launcher proposal, drafted under Orca](#unit-3---skill-the-orca-launcher-proposal-drafted-under-orca)
- [Working practice for every unit](#working-practice-for-every-unit)
- [What the ORCA-SKILL proposal needs from the units](#what-the-orca-skill-proposal-needs-from-the-units)
- [Still missing](#still-missing)
- [Decisions this plan needs](#decisions-this-plan-needs)

## Bounds

The plan fits three decisions Kris took on 30 October:

- **ORCA-REACH** (follow-up due 6 November 2026): Orca runs only on attended Macs, for packages that opt in by a logged decision; `ki agent` stays the only launcher on `vega`. Every unit below runs on sol, in a session Kris has opened and is attending, and only after this package's opt-in is logged. No unit uses `worker-start --on`, a paired environment or a remote server, and none touches `vega`.
- **WAKE-SESSION**: one contract verb, `wait`, implemented natively by each launcher; one detached waiter at a time, bounded at five minutes and re-armed after each wake; wake and acknowledgement proved per runtime and launcher; no seen event lost; session wakes best effort. Unit 1 is the proof of the Orca half, in Claude Code and in Codex.
- **WAKE-DURABLE**: the headless coordinator pass stays the durable wake. No unit creates, edits or relies on an Orca automation, and none runs `orca serve`.

The Techne Programme Focus's Sessions bound holds throughout: agents run on sol only in sessions the binding owner opens, with no unattended or scheduled agents. The units are therefore attended runs, not an away window.

## Shape of the trial

One Orca Run for this Project, created on sol with `orca orchestration run-create` by the coordinating session once the opt-in is logged, as ORCA-HOST set one Run per Project. The Mac Studio setup Run `run_0de85069bc1d` stays with that history and is not reused.

| Unit | Repository | Host | Coordinator | Worker | Worktree | Proves | Size |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 WAKE, leg A | ki-principal (read-only work) | sol, attended | Claude Code | Codex | `current` | `check --wait` as the native `wait` in Claude Code | small |
| 1 WAKE, leg B | ki-principal (read-only work) | sol, attended | Codex | Claude | `current` | the same in Codex | small |
| 2 LIVE | ki-principal, `design/` | sol, attended | Claude Code | Codex | `current` | a writing worker in a hooked repository; ask and write window; recovery verbs | medium |
| 3 SKILL (optional) | ki-principal, `design/` | sol, attended | Claude Code | Claude | `current` | the launcher proposal drafted by the launcher it proposes | medium |

Order: 1A, then 1B, then 2, then 3. Each unit waits on the receipt of the one before, so that its brief can carry what the last one taught. Units 1 and 2 should land before the ORCA-REACH follow-up on 6 November, so that the follow-up has evidence.

Every unit uses `--worktree current`. A new or child worktree would meet the open worktree prerequisites the landscape report lists (registry resolution of a linked worktree, an integrate command, a worktree base taken from committed `main`), and the report's short-package pilot rule stands until integrate ships. The shared checkout's cost, Git write windows granted by ask, is known from plan069 and is kept on purpose.

Each unit is real, bounded work this package owns, not a synthetic exercise:

- Unit 1's work is homing row 15 of the landscape report, "Orca repository setup links skills and dependencies", which the report gives to this package as an Orca evaluation trial step.
- Unit 2's work is the contract gaps the landscape report names (correction 6: no `queue`, no `recover`, no event identity or acknowledgement, no rule for report availability; claim 22: a shell-callable status verb), answered for Orca, which the Orca adapter of homing row 6 must carry.
- Unit 3's work is the ORCA-SKILL proposal itself, which Kris asked for on 30 October after two or three units.

## Unit 1 - WAKE: the session wake, proved in Claude Code and Codex

**Repository and host.** ki-principal on sol, attended. The worker's task is read-only; it writes nothing into any repository.

**Runtime.** Leg A: Claude Code coordinator, Codex worker (`--agent codex`). Leg B: Codex coordinator, Claude worker (`--agent claude`), in a Codex session Kris opens on this package, which binds the Project's Run with `run-use` once leg A's session has disarmed its waiter. Whether `run-use` hands a Run from one coordinator terminal to another cleanly is itself checked at the start of leg B; if it does not, leg B creates its own Run and the log says why.

**The work.** Each worker inventories what an Orca worker started in the current ki-principal worktree actually sees: which skills are discoverable to it (KI skills, `orca-cli` and `orchestration`), whether `ki` and the repository's dependencies resolve, which hooks would fire on a commit, and whether Orca's repository setup linked any of them. It reports the inventory outside every repository through `worker_done --report-path`. Two legs give the inventory for both worker runtimes.

**What it proves.** `orca orchestration check --wait` as the native `wait` under WAKE-SESSION:

1. The coordinator arms exactly one detached waiter: `orca orchestration check --ack <previous deliveryId> --wait --timeout-ms 300000 --json`, the `--ack` acknowledging the batch already processed before waiting again. In Claude Code it runs as a background command that re-invokes the session when it exits; in Codex, the leg establishes what the native detached form is.
2. The worker's events (heartbeats, any ask it raises, `worker_done`) each wake the coordinator; the coordinator processes the whole batch, gives its timed update, and re-arms with that batch's `deliveryId` as the next `--ack`.
3. With no event for five minutes, the waiter times out, the coordinator gives a timed update naming the worker's step from `worker-show` or `worker-read`, and re-arms.
4. **The loss test.** Once in each leg, after a delivery arrives and before it is acknowledged, the coordinator's waiter process is ended (or, in Claude Code, the session is interrupted). On re-arm without `--ack`, Orca's help says the bound Run replays the same delivery until it is acknowledged; the leg shows that it does, so a seen event is not lost. This is the property `ki agent wait --next` lacks, by the landscape report's evidence.
5. At no time are two waiters armed for the coordinator: checked by process listing at each wake. Orca allows several waiters on one inbox ("waiting reserves nothing, listeners woken together get same Delivery"), so the one-waiter rule is the coordinator's discipline, not Orca's.

**Evidence.** The Run, Task, Dispatch, message and delivery ids; a timestamped waiter log per leg (each arm, wake, timeout, ack and the replayed delivery), kept in the run's temporary folder and summarised into the trial log at receive; the process listings; the inventory report; Kris's note of whether the coordinator stayed responsive to their messages while a waiter was armed.

**Pass criteria.**

- Every event the worker sent appears in the coordinator's log exactly once as processed, matched against `orca orchestration inbox` for the Run.
- The replayed delivery in the loss test carries the same `deliveryId` and is processed once.
- No waiter outlived five minutes plus one keepalive interval (Orca emits a keepalive line on stderr every 15 seconds; the waiter filters them).
- One waiter at a time throughout.
- Each leg reports a pass, or a precise failure: in particular, if Codex has no detached form that re-invokes its session, leg B records the nearest native form (for example a foreground bounded wait between turns), its cost to responsiveness, and passes the no-loss criteria on that form, and the gap goes to Kris as a finding against WAKE-SESSION rather than being papered over.

**Risks, from plan069.**

- _Heartbeats are turn by turn._ A worker's long step is silent; a five-minute timeout with no heartbeat is not a stall. The coordinator reads `worker-show` before treating silence as failure.
- _Asks are asynchronous and time out at ten minutes by default._ Any ask the worker raises uses `--timeout-ms 1800000` (Orca's maximum, 30 minutes), and on a timeout resumes the same message with `--resume <message_id>` rather than asking again; the plan069 recovery of an interrupted ask by its message id is repeated if it arises.
- _worker_done can say `failed` for a succeeded unit._ Not expected here, since the worker writes nothing; if it happens, the report is read before anything is redispatched.
- _A dying waiter between process and ack._ Exactly what the loss test exercises; the coordinator acknowledges only after it has recorded the batch.

## Unit 2 - LIVE: Orca's live-layer recovery map

**Repository and host.** ki-principal on sol, attended; the worker writes one design note, `+/_WORK/ki.prj.orca-evaluation/design/orca-live-layer.md`, and commits it by explicit path.

**Runtime.** Claude Code coordinator, Codex worker, waking under unit 1's leg A recipe.

**The work.** For each verb the landscape report finds missing or underspecified in the contract, the worker records what Orca 1.4.244 offers and how far it was verified: `queue` (Task dependencies and `--deps`), `recover` after an uncertain outcome (`request-show`, `--retry-request`, `run-use` after a restart, `worker-abandon`), event identity and acknowledgement (`deliveryId`, `--ack`, replay), shell-callable status (`worker-list`, `worker-show`, `run-show`, `task-list`), stop (`worker-stop`, `worker-release`) and report availability (`--report-path`, on one host only under ORCA-REACH). It adds what Orca stores and where, from the trial log. Each claim is marked as read from local help, exercised in this trial, or unverified. The worker exercises nothing destructive: no `reset`, no stopping or abandoning another dispatch.

**What it proves.** A writing Orca worker in a repository whose pre-commit hook runs lint-staged: the Git write window granted by ask, publication of its own commit under the hook, a report outside the repository, and `worker_done` matching the unit's real outcome. It also exercises unit 1's wake over a longer, multi-step run.

**Evidence.** The ids as in unit 1; the ask and reply message ids for the write window; the commit on `main`, made by explicit path with hooks run and no `--no-verify`; the waiter log; the report; the coordinator's `state.md` Now line for the dispatch, added at dispatch and removed at receive.

**Pass criteria.**

- The note is committed by the worker inside its granted write window, hooks run, and the coordinator pushes it fast-forward only at receive.
- `worker_done` reports `succeeded`, and the report agrees.
- No ask timed out unanswered; every event processed once, as in unit 1.
- Every claim in the note carries its verification mark.

**Risks, from plan069.**

- _The no-stash rule against lint-staged's backup stash._ This is the failure that turned plan069's `worker_done` to `failed`. The brief must carry the publication rule Kris chooses under TRIAL-PUBLISH up front, not as a mid-run exception: either the bounded exception (the worker never runs `git stash` itself, but its explicit-path commit may let the repository's own pre-commit hook create and drop lint-staged's backup stash), or no worker commit at all, the coordinator committing the note at receive. In a shared checkout with other sessions' changes, the hook's backup stash touches more than the worker's own files, which is why the exception has to be Kris's and bounded.
- _Asks time out at ten minutes._ The write-window ask uses `--timeout-ms 1800000`; the coordinator answers it within the window or the worker resumes it by message id. A question only Kris can answer follows TRIAL-ASK.
- _Heartbeats are turn by turn._ The note's drafting is the long silent step; the coordinator's timed updates read `worker-read`.
- _worker_done reflects the last step._ A `failed` is read against the report and the Git log before any redispatch; a succeeded draft with a blocked publication is published as a follow-up, as plan069's was.

## Unit 3 - SKILL: the Orca launcher proposal, drafted under Orca

**Repository and host.** ki-principal on sol, attended; the worker writes the ORCA-SKILL proposal as a design note in this package's `design/` and commits it by explicit path. Optional: the proposal can equally be drafted by a `ki agent` run, and two units satisfy ORCA-SKILL's "two or three".

**Runtime.** Claude Code coordinator, Claude worker (`--agent claude` with an explicit `--model` and `--effort`), so that the trial has a Claude worker doing writing work as well as Codex.

**The work.** Crystallise units 1 and 2 and the plan069 log into the proposal for an Orca launcher under `ki-delegation` and `ki-coordination`, per [What the ORCA-SKILL proposal needs](#what-the-orca-skill-proposal-needs-from-the-units). The proposal is a draft for Kris; it changes no skill, standard or harness file.

**What it proves.** A Claude worker under Orca carrying a medium-length writing unit with the publication rule settled in unit 2, and whether the launcher is fit to carry its own design work. It also tests how the full rendered prompt passes as an Orca Task specification for a long brief.

**Evidence and pass criteria.** As unit 2: ids, waiter log, the commit, `worker_done` matching the report, every event processed once; and the proposal answering each item in the list below with a cited piece of trial evidence or an explicit "not evidenced".

**Risks, from plan069.** As unit 2, with one more: a long specification may be truncated or reshaped by the agent's first terminal; the worker's first heartbeat quotes the brief's last line so the coordinator can tell.

## Working practice for every unit

Until the ORCA-FIT notes arrive, the units run on the practice below, provisional and for the trial only, which is the ORCA-FIT draft's recommended course where it has one. TRIAL-PRACTICE asks Kris to confirm it.

- **Ids** (as ORCA-FIT's OF-IDS a): one `state.md` Now line per running unit naming the run, host, Orca Run, Task and Dispatch, removed at receive.
- **Specification** (OF-PROMPT a): the full rendered prompt, brief plus authority footer and report rule, passed as the Task specification.
- **Liveness** (OF-LIVENESS a): Orca heartbeats only; the coordinator's timed updates read `worker-show` and `worker-read`.
- **Report** (OF-REPORT a): outside every repository, named in `worker_done --report-path`; the coordinator copies it into the work folder at receive and commits it with the move.
- **The brief** still lives at `briefs/<run>.md` in the package, as plan069 found it must for the record.
- **Decisions and queries** stay in the package; the run report copies each ask's question, options, answer and message ids, so no decision depends on Orca's state alone, as checked at plan069's `worker_done`.

## What the ORCA-SKILL proposal needs from the units

Kris's go of 30 October asks for an Orca launcher under `ki-delegation` and `ki-coordination`. The landscape report names it `ki-delegation-orca`, an adapter beside `ki agent`, homed in ki-agentic-harness through a line to the harness's owning work (homing row 6). From the units it needs:

1. **`wait`, per runtime.** The exact Claude Code and Codex recipes for one bounded detached `check --wait`, its re-arm with `--ack`, the keepalive filter, and the loss test's result (unit 1). If Codex has no detached form, the proposal states the Codex form and its limit.
2. **`start`.** The `worker-start` line the adapter uses (worktree, agent, model, effort, setup policy), with what the setup inventory showed a worker sees (unit 1).
3. **`status`.** Which Orca verb gives a shell-callable status the timed updates and the headless pass can read (unit 2), without making Orca a dependency of the headless pass under WAKE-DURABLE.
4. **Queries.** The ask rule: timeout setting, resume by message id, and how a question only Kris can answer travels (units 1 and 2, TRIAL-ASK).
5. **Report and publication.** The report path, the hooked-repository commit rule, and the reading of `worker_done` against the report (unit 2).
6. **`recover`, `queue` and `stop`.** Orca's answer to each, with its verification mark (unit 2).
7. **Ids and storage.** Where ids are recorded and what is lost if Orca's state goes (units 1 to 3, the trial log).
8. **Scope.** Attended Macs only; nothing remote, so remote report availability is left out explicitly rather than assumed; no automations; skill loading only where a package has chosen Orca (landscape claims 8 and 21).
9. **What stays with KI.** The work package, decisions, queries, acceptance and the push; and the `ki agent` features Orca makes redundant, as evidence for OF-KI-AGENT and AGENT-HOME, not a decision.

## Still missing

- **The ORCA-FIT notes.** The draft [How Orca fits the Knowledge Islands work model](../../ki.prj.ways-of-working/design/orca-fit.md) is still in `ki.prj.ways-of-working`'s design folder, with eight open choices; no `messages.md` line has handed it to this package. Two of its choices are overtaken: OF-LAUNCHER by ORCA-REACH and OF-WAKE by WAKE-SESSION and WAKE-DURABLE. The units generate evidence for OF-REPORT, OF-OWNER-ASK, OF-LIVENESS, OF-IDS, OF-PROMPT and OF-KI-AGENT, but this plan decides none of them; it runs their recommended options as provisional practice if Kris agrees.
- **The second brief's line.** Homing row 28 of the landscape report says `ki.prj.ways-of-working` sends this package the second brief's inputs and prerequisites, split into attended-pilot and unattended prerequisites, as a `messages.md` line. It has not arrived. The report says an attended first pilot waits on the opt-in, "the adapter design note" and the worktree gaps; Kris's later ORCA-SKILL go puts the proposal after the units, and `--worktree current` avoids the worktree gaps, so this plan follows ORCA-SKILL and flags the difference for when the line arrives.
- **The Codex wake mechanism.** The landscape report records that a Codex coordinator has no background-task re-invocation. Whether a native detached waiter exists for Codex is unknown until leg B.
- **Run hand-over between runtimes.** Whether `run-use` moves a Run cleanly from a Claude Code coordinator terminal to a Codex one is untested.

## Decisions this plan needs

Kris's decisions, as queries in the run report: ORCA-OPTIN (this package opts in to Orca dispatch for the trial), TRIAL-UNITS (the units and their order), TRIAL-PUBLISH (how a worker publishes in a hooked repository), TRIAL-ASK (how a question only Kris can answer travels) and TRIAL-PRACTICE (the provisional working practice).
