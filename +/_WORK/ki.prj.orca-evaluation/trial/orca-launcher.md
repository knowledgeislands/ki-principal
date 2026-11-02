---
note_type: streams/design
status: draft - 1 November 2026
work: ki.prj.orca-evaluation
author: Written with Claude
---

# Orca launcher proposal: `ki-delegation-orca`

**Owning work:** `ki.prj.orca-evaluation` · **Authority:** ORCA-SKILL (30 October 2026) and ORCA-SKILL-NOW a) (1 November 2026): draft the proposal here, then hand it to `ki.prj.ways-of-working` to adopt. The adapter's name is ORCH-NAME-DISPATCH a) in Ways of working. This note adopts nothing. · **Evidence:** the [trial log](orca-trial.md); Orca 1.4.245 help on sol, read 1 November.

Each statement is marked **[proved]** with its trial-log source, **[elsewhere]** with its owner, or **[proposed]**.

## Scope and boundary

`ki-delegation-orca` is an adapter of the portable `ki-delegation` contract, as `ki-delegation-paperclip` is. It owns only how a coordinator starts, waits on, steers, stops and closes Orca supervised workers. The run contract (brief, authority footer, report shape, owner report) stays in `ki-delegation`; turn budget, receive, mark, hold and Finished stay in `ki-coordination`. **[elsewhere: ORCH-NAME-DISPATCH, Ways of working]**

## When Orca launches, and when `ki agent` stays

- Orca only on attended Macs, for a package that opts in by a logged decision; `ki agent` stays the only launcher on `vega`. **[elsewhere: ORCA-REACH, follow-up due 6 November 2026]**
- One launcher per package per host, recorded in its decisions log, as ORCA-OPTIN b) does for this Project. **[proposed, from orca-fit claim 2]**
- `ki agent` stays: on any host without Orca, for a package without an opt-in, and for a run that must outlive the coordinator until worker survival is proved (open points). **[proposed]**

## Start

1. **Run.** `orca orchestration run-create --objective "<work id> - <purpose>" --json`, once per package per coordinator session; the objective starting with the work id is how a later session finds it. **[proved: 1 November new Run; gotcha "Finding a Run"]**
2. **Worker.** `orca orchestration worker-start --spec <rendered prompt> --task-title <run name> --worktree current --agent <claude|codex> [--model <id> --effort <level>] --json`. Claude and Codex workers ran from a chat coordinator without permission prompts and nest under the coordinator's row. **[proved: TRIAL-SHAPE; four workers on 1 November]**
3. **Ids.** Read the Task and Dispatch ids from `worker-list --run <id> --json`, not from the start receipt, which nests them. **[proved: gotcha "worker-start's receipt nests the ids"]**
4. **Worktree.** `current` by default, commits by pathspec, and workers that touch the same files chained, never parallel. **[proved: ORCA-DISPATCH-LEARNINGS (2)]** Writing runs move to `new-child` when the `ki-delegation` worktree baseline takes effect. **[elsewhere: worktree baseline, `ki-delegation`]**
5. **Agent choice.** The brief's runtime, passed as `--agent`; Orca's own launch, switching to `terminal create` plus `worker-start --terminal` only if a worker meets prompts or blocked writes. **[elsewhere: ORCA-PLACEMENT a), Ways of working]**
6. **Prompt.** The full rendered brief with its authority footer and report rule, passed as the spec. A render-only `ki` step does not yet exist; until it does, the coordinator passes the brief text. **[proposed, from orca-fit OF-PROMPT a)]**

## Wait

- The adapter's `wait` is one detached `orca orchestration check --wait --timeout-ms 300000 --json`, one at a time, re-armed after each wake. It re-invokes a Claude Code chat when a delivery arrives. **[proved: TRIAL-SHAPE]** The contract is **[elsewhere: WAKE-SESSION a), `ki-delegation` Wait verb]**.
- `check` returns the Run's oldest unacknowledged batch whole; `--types` sets only what wakes it, so heartbeats arrive with or ahead of `worker_done`. **[proved: gotcha "Heartbeats", and `check --help`]**
- The waiter acknowledges heartbeats itself: when a woken batch holds only heartbeats, it runs `check --ack <deliveryId>` and waits again inside the same bound, so Kris is not prompted and the coordinator is not woken for liveness. Any batch holding `worker_done`, `escalation` or `question` is left unacknowledged for the coordinator, which processes every message and then acknowledges. **[proposed]**
- Codex as coordinator: unproved. **[elsewhere: CODEX-WAKE, Ways of working]** The durable wake is the headless pass; no Orca automation is a wake. **[elsewhere: WAKE-DURABLE a)]**

## Status, steering, stop, release and close-out

- **Status:** `worker-show --dispatch <id>`, `worker-list --run <id>` and `worker-read --dispatch <id>`; `unverifiable` is never dead. Heartbeats are sent turn by turn, so silence is not a stall. **[proved: gotcha "Heartbeats"; mapping elsewhere: orca-subagents design section 3]**
- **Steering:** `orca orchestration send --to dispatch:<id>`. **[proved: ORCA-DISPATCH-LEARNINGS (3)]**
- **Stop:** `worker-stop --dispatch <id>` only when Kris names the run and says stop. **[proposed]**
- **Release and close-out:** `worker-release --dispatch <id>` after an accepted settlement; reclaimable list empty before mark, hold and Finished. **[proved for release from a chat: TRIAL-SHAPE; rule elsewhere: `ki-coordination` Closing out Orca workers]** Its open point on chat release is now settled and can be struck. **[proposed]**
- **Read before redispatch:** `worker_done` reflects the last step; read the report and the Git log first. **[proved: plan069]**

## Recovery after a coordinator session changes

A Run is bound to the session that made it; a new session could not use it ("caller not bound"). **[proved: gotcha]** So a new coordinator session makes a new Run, finds the old one by objective, settles or names any worker still owing a decision, and records the old Run as retired in its decisions log. `run-use --takeover-legacy` works only from a live coordinator terminal and is not a chat route. **[proposed; `run-use --help`]**

## Queueing

Orca never starts a worker when its dependencies finish. Within one session the coordinator starts the next worker at the wake that settles the last, keeping about three running. A queue that must outlive the session stays with `ki agent`'s dispatcher, Orca first while the parent chat is live. **[proposed; dispatcher rule elsewhere: ORCA-QUEUE a), Ways of working]**

## Ids, brief and report paths

- No Run, Task or Dispatch id in a package file; a machine-local routing record keyed by `<repository>/<work id>`; `messages.md` stays the durable channel and an Orca `send` is only a wake. **[elsewhere: ORCA-ROUTING]** Until the record exists, this Project's `state.md` Run line is a logged exception. **[elsewhere: STOCK-TAKE decision]**
- Brief at `+/_WORK/<id>/briefs/<run>.md` while open **[elsewhere: `ki-delegation`]**; report outside every repository at `~/.local/state/ki/agents/<run-dir>/<name>.report.md`, named by `worker_done --report-path`, copied in by the coordinator at receive. **[proved: this Project's four workers; rule proposed in orca-fit OF-REPORT a)]**

## Questions only Kris can answer

Operational questions go by `ask`, resumed by message id, never duplicated. **[proved: plan069; ORCA-DISPATCH-LEARNINGS (4)]** How a question only Kris can answer travels is undecided. **[elsewhere: OF-OWNER-ASK, Ways of working]**

## Commits

Workers commit by explicit pathspec in the product's repository. **[proved: ORCA-DISPATCH-LEARNINGS (2)]** Commits in hooked repositories follow the never-stash rule. **[elsewhere: HOOK-STASH a), Ways of working]**

## What stays in Knowledge Islands

The work package is the record: definition, state, queries, messages and decisions in Git. Orca's Runs, Tasks, Dispatches and messages are host-local and may be lost; no decision rests on them when reports copy each ask and the decisions log records outcomes. **[proved: plan069; "What Orca stores"]** Orca's state is never hand-edited. **[proved: gotcha]**

## Open points

- **Worker survival** when the coordinator chat ends: untested, left for first live use. **[proved open: TRIAL-SHAPE]**
- **Delivery replay:** the loss test is not run. **[open]**
- **Run hand-over** by `run-use` between chat sessions. **[open]**
- **Codex coordinator wake.** **[open: CODEX-WAKE]**
