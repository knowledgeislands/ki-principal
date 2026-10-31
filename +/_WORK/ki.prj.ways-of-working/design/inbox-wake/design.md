---
note_type: streams/design
status: draft - October 2026
work: ki.prj.ways-of-working
run: ki-prj-ways-of-working
agent: inbox-wake-design
written_at: 2026-10-31
author: Written with Claude
---

# Inbox wake: how an idle coordinating thread hears new messages and new work

**Owning work:** `ki.prj.ways-of-working` · **Authority:** INBOX-WATCH, Kris in this thread, 31 October 2026, 12:18 GMT: "an active coordination thread may well have a scheduled kind of wake up to see if there's any new work for it? I don't know if Orca supports that natively, or if that's something that we need to put into our skills ... could be different by each orchestration platform." Design only: nothing here changes a standard, skill, tool, schedule or automation, and no watcher, worker or automation was started to write it.

**Settled inputs:** WAKE-SESSION a) and WAKE-DURABLE a), both taken on 30 October 2026 ([decisions](../../decisions.md#owner-answers-30-october-2026-0615-gmt)); WAKE-SUBSTRATE a), 26 October 2026, which put the durable wake in the `ki-coordination` Headless passes section; ORCA-ROUTING, relayed on 31 October 2026, under which `messages.md` stays the durable channel and an Orca send to a Run is only a wake ([Orca sub-agents design](../orca-subagents/design.md)). WAKE-HOST is still open ([queries](../../queries.md)).

**Evidence base, read only on this host on 31 October 2026:** Orca 1.4.245 (`orca --help`, `orca orchestration --help`, `send --help`, `check --help`, `terminal send --help`, `automations create --help`, the bundled `orchestration` guide and the `orca-cli` guide's `automations` reference); Claude Code's own tool contract as loaded in this session (background Bash, `Monitor`, `CronCreate`, `ScheduleWakeup`, `RemoteTrigger`, and the `/loop` and `/schedule` skills); Codex CLI 0.166.0 (`codex --help`, `codex queue --help`, `codex exec --help`, `codex features list`, and the names of the hooks in `~/.codex/config.toml`); Paperclip's documentation in the local clone at `831c3301e` (25 October 2026: `docs/agents-runtime.md`, `docs/guides/agent-developer/how-agents-work.md`, `docs/specs/external-task-protocol.md`); `ki agent --help`, `ki agent wait --help` and `ki work status --help`; the `ki-coordination` and `ki-delegation` standards at harness `29d635e1` or later.

## Contents

- [The question in plain words](#the-question-in-plain-words)
- [What the method says today](#what-the-method-says-today)
- [What each platform offers](#what-each-platform-offers)
- [Proposal 1: the portable rule](#proposal-1-the-portable-rule)
- [Proposal 2: what each adapter supplies](#proposal-2-what-each-adapter-supplies)
- [Proposal 3: should a sender also nudge?](#proposal-3-should-a-sender-also-nudge)
- [Challenges to earlier decisions](#challenges-to-earlier-decisions)
- [Queries](#queries)

## The question in plain words

Other work sends this work new things by adding a line to its `messages.md` and pushing. A coordinating thread only reads that file when something wakes it: Kris writing, or its own background check while runs are going. When the work is with Kris and nothing is running, nothing wakes it, so a line can sit unread for hours while Kris and the coordinator are both in the thread. Kris wants the open thread to notice such lines by itself and act on them.

Three kinds of thing can need the coordinator's attention:

1. **A new message:** a line in this work's `messages.md`, which is also how new work arrives from other work and from State of play.
2. **A run event:** one of this work's runs finishing, failing, blocking or asking.
3. **A date:** a dated next step or follow-up in the package, such as AGENT-HOME's on 2 November 2026.

The question is about the first, with the other two folded in where that is cheap.

## What the method says today

- **Heartbeat:** while work lies with a worker, one background check wakes the coordinator at least every five minutes; "With the supervisor, in handoff or On hold, no check is armed and there is no heartbeat" (`ki-coordination`, Coordinator responsiveness).
- **Inbox check:** the five-minute check also compares `messages.md`'s last commit, but "Nothing adds a wake where none is armed" (`ki-coordination`, Messages between work).
- **WAKE-SESSION a):** one contract verb, `wait`, which each launcher implements; exactly one detached waiter at a time, bounded at five minutes and re-armed after each wake; proved per runtime before anyone relies on it; session wakes stay best effort.
- **WAKE-DURABLE a):** when no session is open, the durable wake is the headless pass, a shell-only scheduled check that starts one bounded model turn only when something changed. Orca automations are not adopted as the durable wake.
- **WAKE-HOST, open:** where a headless pass may run, given that the Techne Programme Focus allows no unattended or scheduled agents on sol or `vega`.

INBOX-WATCH changes the first two: Kris asked for a watcher that stays armed while the work is with Kris. This thread already runs one by hand under part 1 of that decision.

## What each platform offers

Labels: **observed** means seen working in this territory's own use; **local help** means the installed version's own help or bundled guide says so, but nothing was run here to prove it; **vendor docs** means only the vendor's documentation says so.

### Claude Code

| Mechanism | What it does | Fit for an inbox watch | Evidence |
| --- | --- | --- | --- |
| Background shell command (`Bash` with `run_in_background`) | Runs a shell command detached; when it exits, the session is re-invoked with a notification. Up to two hours per command | **Best fit.** A shell loop does the polling at no model cost, and the model wakes only when the loop exits with a reason | Observed: it is how this thread's five-minute heartbeat and its INBOX-WATCH watcher run. Local help gives the two-hour limit |
| `Monitor` | Streams each output line of a script as a notification; expires after at most ten minutes and must be re-armed | Works, but the ten-minute cap forces a re-arm turn every ten minutes even when nothing happened | Local help (tool contract) |
| `CronCreate` | Enqueues a prompt on a cron schedule; session-only, fires only while the session is idle, runs up to half its period late, and expires after seven days. "durable" has no effect | Poor: every firing costs a model turn whether or not anything changed | Local help (tool contract) |
| `/loop` and `ScheduleWakeup` | Re-runs a prompt on an interval or a self-chosen delay of one minute to an hour; `ScheduleWakeup` works only inside `/loop` | Poor for the same reason, and it turns the thread into a loop rather than a conversation | Local help (skill and tool contract) |
| `RemoteTrigger` and `/schedule` (cloud routines) | Runs a routine in Anthropic's cloud on a schedule or a GitHub event; a routine can post into an existing claude.ai session | Not a fit: it runs off this machine, cannot see local runs or unpushed state, is an external service, and is a scheduled agent under the Techne Programme Focus | Local help (tool contract); the posting into a session is not proven for a local CLI session |
| Hooks (`UserPromptSubmit`, `SessionStart`) | Run a script when Kris writes or a session starts | Useful as a backstop: the coordinator-reminder hook could say "messages.md changed since you last read it" on Kris's next message. Never a wake on its own | Observed (the coordinator-reminder hook is bound) |

### Codex

| Mechanism | What it does | Fit | Evidence |
| --- | --- | --- | --- |
| Background shell inside a session | No documented re-invocation of an idle interactive session when a background command exits | No session-side wake | Local help shows none; the landscape reviews said the same |
| `codex queue --thread <id> --message <text> [--resume]` | Queues a message for an existing session; with `--resume`, "try to resume the thread on the local daemon", and a failed resume only warns | **Possible wake from outside**: a detached shell watcher, not the session, could queue "messages.md changed" into the coordinator's thread | Local help, Codex 0.166.0; not run. Whether a queued message starts a turn in a thread held open in the terminal is unproven |
| `wake_on_agent_messages` feature | Name suggests waking a session on agent messages | Not usable: "under development", off | Local help (`codex features list`) |
| `in_app_local_automation` feature | Local automations in the Codex desktop app | Would be a scheduled agent, the same class as a headless pass; out of scope for a session wake | Local help (feature name only) |
| Hooks (`session_start`, `user_prompt_submit`, `pre_tool_use` and others, feature "stable") | Scripts at session events | Same backstop role as Claude Code's hooks | Local config shows them registered |

### Orca 1.4.245

| Mechanism | What it does | Fit | Evidence |
| --- | --- | --- | --- |
| Mailbox: `orchestration send --to run:<id>` | Durably enqueues a message for a Run's inbox. "A successful `orchestration send` proves durable enqueue; its wake or nudge is best-effort attention only and does not prove the recipient read or accepted it" | A **doorbell** at best. It reaches only a coordinator that has bound an Orca Run, on a host that can reach that Orca runtime | Local help and bundled guide; no send made |
| `orchestration check --wait --types ... --timeout-ms` | Blocks until a message arrives for the bound Run, or times out; `--peek` reads without marking read | Can be one more trigger inside the shell watcher where the work has a verified ORCA-ROUTING record | Local help; observed in the Orca trial runs reported to this work |
| Does a message to a chat session wake it? | Orca's own guide promises only "best-effort attention". The mailbox is Run-scoped: a chat that has bound no Run has no mailbox to wake | **Not established.** ORCA-SUBAGENT-PILOT is the place to test it | Vendor guide only |
| `terminal send --terminal <h> --text ... --enter` | Types a prompt into a live agent terminal, with submission observed | Would wake an idle agent, but it types into Kris's own conversation as if Kris had written, possibly mid-turn. **Rejected** for wakes | Local help |
| Automations (`automations create --trigger ... --precheck <cmd>`) | A scheduled prompt run by a chosen agent in a new or existing workspace. A shell precheck runs first; a non-zero exit skips the run and records `skipped_precheck`. `--reuse-session` reuses the automation's own previous session, not the coordinator's | Not a session wake: each firing is a new or automation-owned session, so it is a scheduled agent, the headless pass's class. It does match the headless pass's trigger contract closely (shell-only check, model only on change) | Local help; nothing created |

### Paperclip

| Mechanism | What it does | Fit | Evidence |
| --- | --- | --- | --- |
| Heartbeats | Agents "run in heartbeats: short execution windows triggered by a wakeup". Wake sources: `timer` (`intervalSec`), `assignment`, `on_demand`, `automation`, and comment mentions (`issue_comment_mentioned`). Wakeups for a running agent are coalesced, and the next heartbeat reuses the saved session | Paperclip's whole model is the durable wake. It cannot wake a live CLI session that Kris has open; it wakes Paperclip's own agents. A timer heartbeat is a scheduled agent under the Techne Programme Focus | Vendor docs (local clone, 25 October 2026); no server run |
| Comment or mention wake | A comment mentioning an agent, or an imported comment where `wakeOnExternalComment` is set, wakes the assignee | The Paperclip-native equivalent of a `messages.md` line, but the line would then live in Paperclip, not the repository, which KI's authority rules do not allow as the channel of record | Vendor docs |

### `ki agent` today

- `ki agent wait --next` blocks until the next unseen run event and marks it seen; it has an interval but no timeout, so the bound comes from the waiter around it (as WAKE-SESSION found).
- `ki agent watch` prints events and one status line per interval; `ki agent send` appends to a live run's inbox.
- Nothing in `ki agent` or `ki work` watches a work's `messages.md`. `ki work status` reads packages once, read-only.

### What this adds up to

No platform offers a native "wake this open conversation when a file in Git changes". Claude Code comes closest, because any shell command that exits wakes the session, so the watching can be a plain shell loop. Codex may be able to do the same from outside through `codex queue`, unproven. Orca's mailbox is a doorbell for Run-bound coordinators, best effort by its own words. Orca automations and Paperclip heartbeats are durable, scheduled agents, which is the headless pass's territory, not the open thread's.

So the portable part is the watching, a shell loop that costs no model time, and the per-platform part is only how its exit reaches the session.

## Proposal 1: the portable rule

Proposed wording for `ki-coordination`, replacing "no check is armed" with the supervisor and "Nothing adds a wake where none is armed":

> **Inbox watch.** While a coordinating thread is open and its work is not On hold or Finished, the coordinator keeps one watcher armed, whoever holds the work. The watcher is a detached shell loop that spends no model time. Every two minutes it checks for: a change to this work's `messages.md` in the local `main` or on `origin/main` (for territory work, also each assigned package's `messages.md`); and, while runs are going, an unseen run event. It exits on the first change, naming it, or at its bound: five minutes while work lies with a worker, which is the heartbeat, and fifteen minutes otherwise, which is the sync cadence. On a change, the coordinator pulls fast-forward, acts on the new lines in queue order under Messages between work, commits and re-arms, telling Kris in one timed line only what changed and what it did. On a bare timeout with the work with Kris, it syncs and re-arms without a word. Kris's own messages need no watcher. The watcher stops with "stop the wake", at a hold, at Finished, and when the session ends; it is session-only, so it promises nothing once the thread closes, when the headless pass, if one is named, is the only wake. There is never more than one watcher per session; after a compaction or a red-x recovery the coordinator checks whether one is armed before arming another.

Details behind the wording:

- **What it reads.** Only blob identifiers, never content: `git rev-parse HEAD:<path>` and, after a quiet `git fetch origin main`, `origin/main:<path>`. The local check catches a sender on this host that shares the checkout and has committed but not yet pushed; the remote check catches every other sender. A `git ls-remote` first can skip the fetch when `main` has not moved. Run events come from the launcher's own `wait` (Proposal 2).
- **Why two minutes.** It is Kris's own figure for this thread, and one `ls-remote` or fetch every two minutes is cheap; a sender on the same checkout is seen within two minutes, and a cross-host sender within two minutes of its push.
- **Why fifteen minutes when nothing is running.** It matches COMMIT-CADENCE's "at least every 15 minutes" sync, so the one wake serves both rules and the model wakes at most four times an hour with nothing to say. It is also Kris's figure.
- **Speaking.** The heartbeat's timed updates stay as they are while work lies with a worker. With Kris, a quiet wake says nothing, under "between owner messages it has nothing else to say"; a line acted on gets one timed line. A line that needs Kris becomes a query, raised in one line at once if it blocks.
- **Dates.** A dated next step is checked at every wake rather than being a trigger of its own, so the latest it is noticed is fifteen minutes late.
- **What it is not.** It is not a scheduled agent: it lives inside a session Kris opened and dies with it, so the Techne Programme Focus's bar on "unattended or scheduled agents" does not reach it. It is a refinement of WAKE-SESSION's one waiter, not a second mechanism beside it.

## Proposal 2: what each adapter supplies

The rule above is portable; each adapter supplies three things: **the watcher body** (one shared shell verb), **the re-invocation** (how the watcher's exit reaches the session) and **the run-event source**.

| Adapter | Watcher body | Re-invocation | Run events | Status |
| --- | --- | --- | --- | --- |
| `ki agent` (tools-ki), the floor | A new read-only verb, proposed `ki work watch <work id> [--run <run>] --interval 120 --timeout <m>`, printing one reason line (`message`, `run-event`, `timeout`) and exiting. Shell only, no model, no writes beyond `git fetch` | None of its own: the runtime supplies it | `ki agent wait --next`, folded in when `--run` is given | To build; sent as one `messages.md` line to the work that owns tools-ki once Kris agrees |
| Claude Code (runtime binding in `ki-coordination`'s generated surfaces) | Runs `ki work watch` as a background shell command; until it ships, the shell loop sketched below | Native: the background command's exit re-invokes the session | `ki agent wait --next` inside the same loop | Ready now; this thread already does it by hand |
| Codex (runtime binding) | The same verb, launched detached with `nohup` so it outlives the turn | `codex queue --thread <coordinator thread> --message "inbox: <reason>" --resume`, run by the watcher when it exits | Same | **Unproven.** Until a proof shows a queued message starts a turn in an open thread, a Codex coordinator checks the inbox at each owner message and at each run event only, and says so in its first report |
| `ki-delegation-orca` (to be written, homing row 6 of the landscape report) | The same verb; where the work has a verified ORCA-ROUTING record, the loop also runs `orca orchestration check --peek` on its Run | Whatever runtime the coordinator itself is (Claude Code or Codex inside Orca). Orca adds no re-invocation of its own that this design relies on | `orca orchestration check --wait` for Orca workers, `ki agent wait` for detached runs | Write with the adapter; the chat-wake question goes to ORCA-SUBAGENT-PILOT |
| `ki-delegation-paperclip` (today `ki-agent-coordination-paperclip`) | None for an open thread: Paperclip cannot wake a live CLI session | None | Paperclip's own task status | Says only that a Paperclip agent's heartbeat (timer, assignment, mention) is a durable scheduled wake, governed by the Headless passes section and WAKE-HOST, and that `messages.md` stays the channel; a Paperclip comment is never the message of record |

Illustrative shell loop for Claude Code until `ki work watch` exists (not to be run by this design):

```sh
r=/path/to/repo; p='+/_WORK/<id>/messages.md'; bound=900   # 300 while runs go
l0=$(git -C "$r" rev-parse "HEAD:$p"); o0=$(git -C "$r" rev-parse "origin/main:$p")
end=$(( $(date +%s) + bound ))
while [ "$(date +%s)" -lt "$end" ]; do
  git -C "$r" fetch -q origin main 2>/dev/null || true
  [ "$(git -C "$r" rev-parse "HEAD:$p")" != "$l0" ] && { echo "message: local"; exit 0; }
  [ "$(git -C "$r" rev-parse "origin/main:$p")" != "$o0" ] && { echo "message: origin"; exit 0; }
  sleep 120
done
echo timeout
```

The `sleep` runs inside a background command, so it does not trip the foreground-`sleep` permission check the coordinator style warns about.

## Proposal 3: should a sender also nudge?

Recommendation: **not now.** The sender's job stays one line in `messages.md`, committed by path and pushed at once. Reasons:

- The receiver's watcher already sees the line within about two minutes of the push, on any host and any platform. A nudge would save at most those two minutes.
- Orca's nudge reaches only a receiver bound to an Orca Run on a reachable Orca runtime, and Orca itself calls it "best-effort attention only". A sender would have to look up the receiver's ORCA-ROUTING record, which is machine-local, so a sender on another host cannot nudge at all.
- A nudge that sometimes works invites senders to rely on it, and a second channel invites the content to drift into it. ORCA-ROUTING already settled that an Orca send is "only a wake"; this keeps it that way by not adding one yet.
- `orca terminal send` and `codex queue` aimed by a sender at someone else's open conversation would type into Kris's thread; that is the receiver's choice, made by its own watcher, never the sender's.

Revisit when ORCA-SUBAGENT-PILOT shows whether a Run-bound coordinator in an Orca chat is actually woken by its mailbox. If it is, a same-host sender may add `orca orchestration send --to run:<id> --type status --subject "messages.md: new line"` after its push, carrying a pointer only, never the content.

## Challenges to earlier decisions

1. **The standard's "no check with the supervisor".** INBOX-WATCH, in Kris's words, overrides it for the inbox. The proposal keeps the heartbeat's speaking rules and changes only whether a watcher is armed. This is an amendment the work that owns `ki-coordination` (this work) makes once Kris agrees INBOX-ARMED.
2. **WAKE-SESSION's "bounded at five minutes".** That bound was set for run events while work lies with a worker. With the supervisor the proposal uses fifteen minutes. It is still one waiter, so the decision's shape holds; only the bound differs by state.
3. **"A Codex coordinator has no background-task re-invocation, so its wait is only good as its next turn"** (landscape report, row 20). Partly stale: Codex 0.166.0 has `codex queue --resume`, which may let an outside watcher wake a Codex thread. It is unproven, so the per-runtime proof WAKE-SESSION already requires now has something concrete to test.
4. **WAKE-DURABLE a), "Orca automations are not adopted as the durable wake".** The evidence does not argue for reversing it, but it does show Orca automations with `--precheck` implement almost exactly the headless pass's trigger contract (shell check, model only on change, skipped firings recorded). That makes an Orca automation a candidate way to _install_ the headless pass on a host where Orca runs, rather than a rival wake. It changes nothing while WAKE-HOST is open, since either way it is a scheduled agent.
5. **Bearing on WAKE-HOST.** With a watcher armed whenever a thread is open, the durable wake matters only when no thread is open. That strengthens WAKE-HOST's option c), "no host for now: session wakes only, until a work needs a durable wake and names its host in its own decision". This is evidence for Kris's open question, not a new query.

## Queries

Query 1 of 5

## INBOX-ARMED: Keep the inbox watcher armed whenever a coordinating thread is open

**Where things stand**

- Today the standard arms a background check only while runs are going; with Kris, nothing wakes the thread, so `messages.md` lines wait.
- Kris asked on 31 October for a watcher that stays armed while the work is with Kris, and this thread already runs one by hand.
- The watcher is a shell loop inside the open session, so it costs no model time until something changes and is not a scheduled agent.

**The options**

1. **Arm it whenever the thread is open** _(recommended, high confidence)_: amend `ki-coordination` with the Inbox watch rule in Proposal 1; stopped by "stop the wake", a hold, Finished or the session ending. _Why:_ it is what Kris asked for, every platform can at least run the shell part, and it is undone by deleting one rule.
2. **Only while runs are going**: keep today's rule and leave this thread's watcher as a one-off.
3. **Only on request**: arm it in a thread only when Kris asks, as for this thread.

Reply with 1, 2 or 3, or your own words.

Query 2 of 5

## INBOX-CADENCE: How often the watcher looks and when it wakes the thread

**Where things stand**

- Kris's figures for this thread: look every two minutes, wake on a change, otherwise wake after fifteen minutes.
- The fifteen minutes matches the rule to sync at least every fifteen minutes, so one wake serves both.
- While runs are going, the existing five-minute heartbeat stays as it is.

**The options**

1. **Two-minute look, wake on change, else fifteen minutes (five while runs go), silent re-arm when nothing changed** _(recommended, high confidence)_: as in Proposal 1. _Why:_ Kris's own numbers, aligned with the sync rule, and the model speaks only when something happened.
2. **Same, but a longer quiet bound of 30 or 60 minutes**: fewer empty wakes, but the fifteen-minute sync then needs its own trigger.
3. **Same, but say a one-line "nothing new" at each quiet wake**: more visible, at the cost of noise in Kris's thread.

Reply with 1, 2 or 3, or your own words.

Query 3 of 5

## INBOX-VERB: Put the watcher in one shared shell command in tools-ki

**Where things stand**

- Every platform needs the same watching; only how its exit reaches the session differs.
- Nothing in `ki agent` or `ki work` watches `messages.md` today; until something does, each coordinator writes the loop by hand.
- The verb would belong to tools-ki, so this work could only ask for it by a `messages.md` line; the owning work decides how and when.

**The options**

1. **Ask for a read-only `ki work watch` verb** _(recommended, medium confidence - the shape is clear, but the name and home inside `ki` are a tools-ki choice and nothing was prototyped)_: send one `messages.md` line to the work that owns tools-ki describing Proposal 2's verb; the `ki-coordination` surfaces carry the hand-written loop until it ships.
2. **Keep the loop as a documented snippet only**: no tooling change; each runtime binding carries the loop.
3. **Extend `ki agent wait` instead**: add `--timeout` and `--inbox <work id>` to the existing waiter.

Reply with 1, 2 or 3, or your own words.

Query 4 of 5

## CODEX-WAKE: Prove Codex's queue as its wake before relying on it

**Where things stand**

- Codex has no documented way for a background command to wake an open session.
- Codex 0.166.0 has `codex queue --thread <id> --message <text> --resume`, which may let an outside watcher wake a thread; nothing was run to prove it.
- WAKE-SESSION already says each runtime's wake must be proved before anyone relies on it.

**The options**

1. **Prove it in one attended trial, and until then say plainly that a Codex coordinator checks the inbox only when Kris writes or a run event arrives** _(recommended, medium confidence - the command is documented locally but its effect on an open terminal thread is unknown)_: a bounded run tests it with Kris watching, on a scratch thread.
2. **Treat Codex as having no inbox wake** and coordinate waiting threads from Claude Code only.
3. **Adopt `codex queue --resume` now** as Codex's wake, proving it in use.

Reply with 1, 2 or 3, or your own words.

Query 5 of 5

## SENDER-NUDGE: Should a sender also nudge the receiving thread?

**Where things stand**

- The receiver's watcher sees a new line within about two minutes of the push, on any host.
- Orca's mailbox nudge is "best-effort attention only" by Orca's own words, reaches only a coordinator bound to an Orca Run, and needs the receiver's machine-local routing record, so a sender on another host cannot use it.
- ORCA-ROUTING already settled that an Orca send is only a wake, never the message.

**The options**

1. **No nudge now; revisit after ORCA-SUBAGENT-PILOT shows whether the mailbox wakes an Orca chat** _(recommended, medium confidence - the gain is two minutes at most, but whether the Orca wake works is untested)_: senders write and push their line, nothing more.
2. **Optional same-host Orca nudge now**: where the receiver has a verified routing record on this host, the sender adds a pointer-only `orchestration send` after its push.
3. **Required nudge wherever the platform allows**: every sender nudges when it can.

Reply with 1, 2 or 3, or your own words.
