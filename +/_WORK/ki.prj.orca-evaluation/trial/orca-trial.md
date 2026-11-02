---
note_type: streams/design
status: current - 1 November 2026
work: ki.prj.orca-evaluation
author: Written with Claude
---

# Orca trial log

**Owning work:** `ki.prj.orca-evaluation` · **Purpose:** the single, current record of what is known about running Knowledge Islands work through Orca orchestration, on which the Orca launcher proposal rests. · **Host:** sol, Orca 1.4.244 to 1.4.245, local runtime.

## Contents

- [Bounds](#bounds)
- [What was tried](#what-was-tried)
- [What is proved](#what-is-proved)
- [What is still open](#what-is-still-open)
- [Known gotchas](#known-gotchas)
- [What Orca stores](#what-orca-stores)
- [Upstream reports](#upstream-reports)

## Bounds

- **ORCA-REACH** (30 October, follow-up due 6 November 2026): Orca only on attended Macs, for packages that opt in by logged decision; `ki agent` stays the only launcher on `vega`.
- **WAKE-SESSION** (30 October): one `wait` verb per launcher, one detached waiter at a time, bounded and re-armed, no seen event lost; session wakes best effort.
- **WAKE-DURABLE** (30 October): the headless coordinator pass stays the durable wake; no Orca automation is a wake.
- **ORCA-OPTIN** b) (30 October): this Project dispatches all its runs through Orca on attended Macs until Kris revokes it.
- **TRIAL-SHAPE** and **ORCA-SKILL-NOW** (1 November): no separate pilot unit; this log is unit 1, the launcher proposal unit 2.

## What was tried

| When | Who | What | Source |
| --- | --- | --- | --- |
| 29-30 October | ki.prj.mac-studio-setup, under ORCA-HOST | plan069: one Codex worker, `worker-start --worktree current --agent codex`, waited on with `check --wait`; it planned KI-TOOL-RIG-CORE-069 (tools-rig `9297c9c`). The Project then returned to `ki agent` (KI-AGENT-DISPATCH) | previous trial log, ORCA-HANDOVER |
| 30 October | hnr.reg.email-routing | First live supervised use in place of `ki agent launch`: one Run per thread, six Codex workers, `worker-start --spec ... --worktree current`, `check --wait`, `reply`, `send --to dispatch:<id>`, `worker-release` | ORCA-DISPATCH-LEARNINGS |
| 30 October | this Project, `ki agent` runs | Read-only studies of Orca's code and stores: thread nesting, sidebar restore, agent row labels | reports thread-nesting, sidebar-restore, orca-labels |
| 31 October | personal.reg.rig-terra | Repository move on terra (apps-markhowarth.com pilot) with Orca projects registered | ORCA-MOVE-LESSON |
| 1 November | this Project, Orca chat coordinator in Claude Code | New Run, four workers (Claude and Codex) dispatched from the chat: stock-take, review-upstream, file-card-bug, and this evidence homing | this thread's use, decisions STOCK-TAKE and ORCA-CARD-BUG |

## What is proved

| Claim | Date | Source |
| --- | --- | --- |
| Workers started by `orca orchestration worker-start` nest under the coordinator's row in the Agents list | 1 November | Kris's observation (TRIAL-SHAPE); mechanism read from Orca's code (thread-nesting) |
| `orca orchestration check --wait` works as the coordinator's wake in a Claude Code chat: a background check re-invokes the session when a delivery arrives | 1 November | Kris's observation (TRIAL-SHAPE); this thread's use |
| A chat coordinator can release a finished worker; `worker-release --dispatch <id>` closes the worker's terminal and captures its transcript | 1 November | Kris's observation (TRIAL-SHAPE); this thread's use |
| Claude and Codex workers run from an Orca chat coordinator without permission prompts | 1 November | this thread's use, four workers |
| `worker_done` arrives as an inbox delivery the coordinator acknowledges with `check --ack <deliveryId>` | 1 November | this thread's use |
| The ask path works: a worker asks a bounded question, blocks, and continues on the reply; an interrupted ask is resumed by its message id without a duplicate | 29-30 October | plan069; ORCA-DISPATCH-LEARNINGS (4) |
| Workers can be steered mid-run with `reply` and `send --to dispatch:<id>`, enough to serialise two workers editing the same notes | 30 October | ORCA-DISPATCH-LEARNINGS (3) |
| A pathspec commit, `git commit -- <paths>`, lets a `--worktree current` worker commit its own files without touching other sessions' staged files | 30 October | ORCA-DISPATCH-LEARNINGS (2) |
| No decision depends on Orca's state alone when the run report copies each ask's question, options, answer and message ids and the decisions log records the outcome | 30 October | plan069, checked at its `worker_done` |
| A detached `ki agent` run cannot nest under its coordinator: only Orca's own orchestration records carry the parent link, and no variable, name or directory supplies it | 30 October | thread-nesting, read from Orca's code and stores |
| A Claude chat row reads "Monitoring background tas..." instead of its name while it holds a background task such as an armed waiter; this is deliberate Orca behaviour and no setting changes it | 30 October | orca-labels, read from Orca's code |
| Hidden sidebar items are restored under Settings > Appearance > Sidebar; the Mobile page's "Configure in Settings > Mobile" hint points to the wrong page | 30 October | sidebar-restore, read from the app bundle |

## What is still open

- **Worker survival.** Whether a worker survives when its coordinator chat ends is untested; Kris left it as a technical detail for first live use (TRIAL-SHAPE).
- **Codex as coordinator.** Whether `check --wait` has a detached form that re-invokes a Codex session is unproved; the Codex half of WAKE-SESSION is with ki.prj.ways-of-working (CODEX-WAKE), subject to SCOPE-SPLIT.
- **Delivery replay.** Orca's help says an unacknowledged delivery replays on the next `check`; the loss test (end the waiter before `--ack`, re-arm, see the same `deliveryId`) has not been run.
- **Run hand-over.** Whether `run-use` moves a Run from one coordinator session to another is untested beyond the failure below; on 1 November a new Run was made instead.
- **Hooked-repository publication.** How a worker commits where the pre-commit hook makes lint-staged's backup stash (TRIAL-PUBLISH); Kris chose HOOK-STASH a), lint-staged with `--no-stash`, on 1 November, which may settle it.
- **Remote view.** Whether terra can show sol's threads (ORCA-REMOTE-VIEW) needs its own read-only investigation under ORCA-HOST.
- **Identity leak.** `ki agent` runs no longer inherit the Orca session variables (tools-ki `2970714c`); the pane, tab, worktree and hook variables remain (ORCA-IDENTITY-LEAK).

## Known gotchas

- **A Run is bound to the session that made it.** A new chat session could not use the Run made by the previous session ("caller not bound"), so a new Run was made on 1 November and the old one retired.
- **Finding a Run.** Run ids cannot live in package files (ORCA-ROUTING); find a Run by its objective, which starts with the work id.
- **worker-start's receipt nests the ids.** The task and dispatch ids sit deeper than `result.task`; read them from `worker-list`.
- **Heartbeats are owner-visible noise.** Each heartbeat arrives as an inbox delivery that Orca prompts Kris about ("You have 1 orchestration message"), so the waiter acknowledges each one; `check --wait --types worker_done,escalation,question` still returned on heartbeats. Heartbeats are sent turn by turn, so a long step is silent and silence is not a stall.
- **Asks time out.** An unanswered ask escalates after ten minutes by default; a longer `--timeout-ms` (up to 30 minutes) and resume by message id avoid a duplicate.
- **worker_done reflects the last step.** plan069 reported `failed` although its planning succeeded, because its report commit was blocked; read the report and the Git log before any redispatch.
- **Shared index under `--worktree current`.** Workers share the checkout's Git index with other sessions: commit by pathspec, and chain workers that edit the same files rather than running them in parallel.
- **Never hand-edit Orca's state.** Editing Orca's SQLite state by hand stopped Orca starting on terra; it was recovered with `orca profile state rollback --backup <id>` from Orca's own hourly backups (`orca profile state exports`).
- **Repository moves.** A project removed and re-added at a new path gets a new identity and its chats stay with the old one; for a move, leave a link at the old path and keep the Orca project registered there.
- **The waiter changes the row label.** An armed waiter makes the coordinator's row lead with "Monitoring background tasks"; only an Orca change fixes it.
- **The question card drops line breaks.** Multi-line text in an `AskUserQuestion` card renders as one paragraph; put context in chat text above the card.

## What Orca stores

- `~/Library/Application Support/orca/`: `orchestration.db` (Runs, Tasks, Dispatches, messages and deliveries), `agent-session-journal.db`, `profiles/local-default/profile-state.db` (settings), runtime, device, pairing and key files.
- `~/.orca/`: small, including `agent-hooks/`.
- Nothing from Orca is in a checkout. Losing Orca's state loses Run, Task and Dispatch history and raw ask threads, but no decision, provided reports copy each ask and the decisions log records outcomes.
- Orca has no supported settings export; reading settings means reading the profile database (ORCA-SETTINGS-READ).

## Upstream reports

| Item | State | Source |
| --- | --- | --- |
| Question card drops line breaks | Filed 1 November as [stablyai/orca#36830](https://github.com/stablyai/orca/issues/36830) | ORCA-CARD-BUG, file-card-bug |
| Row label leads with "Monitoring background tasks" | Awaiting Kris (ORCA-UPSTREAM) | orca-labels |
| Sidebar restore hard to find; Mobile hint names the wrong page | Awaiting Kris (ORCA-UPSTREAM) | sidebar-restore |
| Supported read-only settings export | Awaiting Kris (ORCA-UPSTREAM) | ORCA-SETTINGS-READ |
| An outside session declaring its parent or name | Awaiting Kris (ORCA-UPSTREAM) | thread-nesting |
