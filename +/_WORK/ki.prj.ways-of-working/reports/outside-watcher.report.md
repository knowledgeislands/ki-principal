# [Model](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › outside-watcher

**🤖 → 👤 Handoff to supervisor · Run report at 12:42 GMT · last mark 01:41 GMT**

---

## Done

- Designed the watcher that sits outside the threads (LISTEN-SYNC-OUTSIDE-THREADS, SYNC-CONTEXT-COST, SYNC-CONTEXT-COST-2): five units, their boundaries and hand-offs, where it runs, how it wakes Claude Code and Orca threads, how it relates to `ki work watch`, the Observatory and the Rig sync passes, interim rules for now and three phases. The design is under Findings as WATCHER-DESIGN; nothing written to any repository, no commit, no remote call. The coordinator may home it as `design/outside-watcher/design.md`.
- Found the main cause of the 880k-token day: sol's Rig loop (`host-loop.sh`) wakes the thread whenever a pass pulls or pushes anything, not only when judgement is needed. On 1 November, 4 of the last 8 passes moved something and so woke the model, on top of a forced re-arm wake every 110 minutes and every message check. Fixing that one rule removes most wakes without new tooling (JUDGEMENT-ONLY-WAKE).
- Found that Claude Code 2.1.309 takes `--autocompact <auto|tokens>` (100k to 1M) as a launch flag, so the compaction window can be set per session, not only per user or repository (AUTOCOMPACT-WINDOW).
- Found a conflict between two of Kris's words: SYNC-DIRECTION on 31 October ("observatory watching, it's not doing the syncing") and OBSERVATORY-WATCHER on 1 November (the Observatory runs the sync, the GitHub pull and the queue watch) (OBSERVATORY-SYNCS).
- Sources read: the decisions entry "eight messages received" in full, `design/inbox-wake/design.md`, the `ki-coordination` standard (Coordinator responsiveness, Thread capabilities, Messages between work, Headless passes) at harness `321742fe`, the Techne Programme Focus, the ki.prj.observatory package and its queue, the WATCH-VERB line in ki.prj.tools-burndown, sol's Rig scripts and pass log, the Observatory's launchd agent, the ki.prj.orca-evaluation wake decisions, and local `claude --help`.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Seven queries below. JUDGEMENT-ONLY-WAKE is high confidence; the other six are medium and, under the query-review rule, go to one blind review before they reach Kris.
- Once Kris agrees, Kris's ask still stands: send the agreed way of working to personal.reg.rig-terra, personal.reg.rig-sol and this work as an acknowledgement. Draft lines are in WATCHER-DESIGN, section 8.
- Proofs not run here (read-only brief): whether a Claude Code channel can carry a wake into an open thread, including one Orca hosts; whether auto-compaction fires while a background command is armed; whether Orca passes launch flags such as `--autocompact` through to its Claude Code threads.

## Findings

### WATCHER-DESIGN - A watcher outside the threads

**Goal:** keep long-lived threads open with small context by moving mechanical work (sync, GitHub pull, message-queue watch) out of the chat, waking a thread only when judgement is needed.

**Scope:** units and hand-offs, host and Techne Programme Focus position, wake paths for Claude Code and Orca threads, relation to `ki work watch`, the Observatory and Rig sync, interim rules, phases, draft rollout lines. Design only; nothing changed.

**As of:** 1 November 2026, 12:42 GMT, on sol; harness `321742fe`; Claude Code 2.1.309; Orca 1.4.245.

#### 1. Why threads grow today

| Source of wakes | How often | Evidence |
| --- | --- | --- |
| Rig pass that pulled or pushed anything | Most 15-minute slots: the loop exits on any `PULL` or `PUSH` line, so routine catch-up wakes the model | `host-loop.sh`; `passes.log` shows 4 of 8 passes on 1 November ran two rounds, meaning something moved |
| Forced re-arm under the two-hour limit on background commands | Every 110 minutes, about 13 a day per thread | `host-loop.sh` (`REARM` after 6600 s) |
| New message lines | As they land | Wanted: these need judgement |
| Each wake re-reads the work package and replies | Every wake | Coordinator rules |

At about 70 to 90 wakes a day, 880k tokens is roughly 10k to 12k per wake, which fits. A running background command also stopped Kris compacting the thread in Orca until it was stopped.

#### 2. Units

| Unit | What it is | Owner | Boundary |
| --- | --- | --- | --- |
| **Watcher** | A shell program per Mac, no model. Runs the host's sync pass at its slot, fetches and watches the `messages.md` of each watched work, and notes finished runs from `ki agent status` | Interim: Rig and dotfiles (a Rig-declared launchd agent, like the existing `uk.me.kris.rig.observatory`). Lasting: the Observatory | Never writes inside a repository except fast-forward pulls of clean checkouts and, if allowed (WATCHER-PUSH), pushes of commits already made. Never merges, rebases, resets, stashes, forces or uses `--no-verify`. Never reads or passes on message content. Watches only checkouts in the host's `mgit` registry, which are Kris's own |
| **Doorbell** | One small file per watched work in a local state folder, for example `~/.local/state/ki/watch/<work-id>.ring`, holding only reason codes and times: `message`, `run-finished`, `sync-judgement`, with counts | Contract: Ways of working, in `ki-coordination`. Verbs: tools-ki | The hand-off between watcher and thread. It persists, so a nudge for a closed or sleeping thread waits until the thread opens. It never carries instructions; the thread reads its own queue from Git |
| **Wake adapter** | How a ring reaches an open thread, one per runtime (section 4) | Ways of working sets the rule; each runtime binding supplies it | The only part that differs by platform |
| **Thread rules** | What a listening or syncing thread does on a ring: read the reason, act on the new lines or the judgement item, clear the ring, re-arm silently | Ways of working (`ki-coordination` Inbox watch, Thread capabilities) | The thread no longer runs passes or fetch loops itself; it acts only on judgement |
| **Watch list** | Which works the watcher watches, taken from each work's capability fields (`listening_enabled` and `listening_status`, `syncing_enabled` and `syncing_status`, FOOTER-CAPABILITY-STATUS-2) | The work package; written by its own thread | Switching listening off in a thread stops its rings; syncing off stops the watcher pushing for that host (WATCHER-PUSH) |

Hand-offs, in order: watcher detects, watcher rings the doorbell, the wake adapter tells the open thread "look at your queue", the thread reads its own `messages.md` or the pass log, acts, clears the ring.

#### 3. Where it runs, and the Techne Programme Focus

- **Hosts:** sol and terra, each running the same watcher for its own checkouts, keeping the 15-minute sync slots with terra seven minutes after sol (HOST-SYNC-SEND). Not on `vega` (VEGA-SYNC).
- **Not an agent, carefully put:** the watcher runs no model, takes no prompt, makes no judgement and starts no session. It only rings a doorbell that a session Kris opened is waiting on, so the agent turn that follows happens inside a session the binding owner opened, which is what the focus allows on sol. It is a scheduled job in the same sense as the existing Observatory and Rig launchd agents, not a scheduled agent.
- **Where the line is:** it stays outside the focus's bar only while it never starts a model turn itself. Using `claude -p`, `claude --bg --resume <id>`, an Orca automation or a headless pass to wake a closed thread would be a scheduled agent, barred on sol and `vega` by the focus and not chosen under WAKE-HOST c). The design keeps that door shut: a nudge for a closed thread waits for Kris to open the thread.
- **Two cautions:** first, it acts while no session is open, so it needs its own decision rather than borrowing the Rig thread's; second, a push it makes publishes commits agents made, so whether it pushes is WATCHER-PUSH. Terra is outside the focus's two hosts, but the same bounds apply there so one agreement covers both, as LISTEN-SYNC-OUTSIDE-THREADS asks.

#### 4. Waking a thread

| Runtime | Wake today | Lasting wake | Status |
| --- | --- | --- | --- |
| Claude Code (terminal or Orca-hosted) | The thread arms one small background waiter that only watches its doorbell file (no fetch, no pass) and exits on a ring. A ring is rare, so wakes drop to judgement only plus the two-hour re-arm, which is silent | A Claude Code channel: a local channel server loaded by the thread forwards "look at your queue" when the doorbell rings, with nothing armed in the background, so compaction is never blocked and there is no two-hour re-arm | Waiter: proven pattern (the background-command exit, and Orca's own wait command in a Claude Code chat under TRIAL-SHAPE). Channel: vendor docs only; local `claude --help` for 2.1.309 lists no channel flag; unproven (CHANNEL-PROOF) |
| Orca native chat | The same as Claude Code, since Orca chats run Claude Code underneath | `orchestration send` reaches only a Run-bound coordinator and is "best-effort attention" by Orca's own words; `terminal send` types into Kris's conversation and stays rejected | No push wake into a chat is proven |
| Codex | Checks its queue when Kris writes or a run event arrives (CODEX-WAKE) | `codex queue --resume` from the watcher, after the attended trial | Unproven; trial already agreed |

A waiter still running in the background still blocks a manual `/compact` in Orca. Until a channel is proven, compacting is: "stop the wake", `/compact`, then the thread re-arms under the existing re-anchoring rule.

#### 5. Relation to other work

- **`ki work watch` (WATCH-VERB, sent to ki.prj.tools-burndown):** still wanted, but its home moves. It becomes the watcher's message check, plus three small doorbell verbs (`ring`, `wait`, `clear`) so the thread-side waiter is one command, not a hand-written loop. A revised WATCH-VERB line would go to tools-burndown once Kris agrees WATCHER-SHAPE.
- **The Observatory (OBSERVATORY-WATCHER, ki.prj.observatory):** the lasting home. It already runs as a Rig launchd service on sol (`uk.me.kris.rig.observatory`, loopback web server). It can later host the watcher in the planned menu-bar app, show each host's doorbells and pass log, and let Kris clear or ring one by hand. The doorbell contract stays the same, so threads do not change when the watcher moves from Rig into the Observatory. Whether the Observatory itself syncs is OBSERVATORY-SYNCS.
- **Rig sync passes (personal.reg.rig-sol, personal.reg.rig-terra):** `pass.sh` becomes the watcher's sync step, then `mgit sync --push` once the push guard has landed. The Rig thread keeps its role and judgement but stops running `host-loop.sh`. Rig and dotfiles own the interim launchd job.
- **Headless passes:** unchanged. The watcher's trigger is like a headless pass's trigger, but it never starts the pass. WAKE-HOST c) stands.

#### 6. Interim rules for now, inside today's tactical model

1. **Wake only on judgement:** host-sync loops exit only on a `WAKE` line (divergence, dirty checkout blocking a pull, lock, failure) or a new message line. Routine pulls and pushes go to `passes.log` silently, and the thread reads the log only when Kris asks (JUDGEMENT-ONLY-WAKE).
2. **Quiet re-arm:** at the two-hour limit the thread re-arms with one tool call, no chat line and no package read.
3. **Small wake turns:** on a message wake, read only the new lines the loop printed and act; on a sync wake, read only the `WAKE` lines. The package tidy stays at most one small item.
4. **Smaller compaction window:** long-lived listening and sync threads set `/autocompact` once at opening, or `--autocompact` at launch where the launch line can be set (AUTOCOMPACT-WINDOW).
5. **Compacting by hand:** "stop the wake", `/compact`, then re-anchor and re-arm.
6. **One loop per thread**, as the standard already requires; non-sync listening threads keep their silent fetch and fast-forward of their own repository and wake only on news.

#### 7. Phases

| Phase | What | Owner | Waits on |
| --- | --- | --- | --- |
| 0, now | Interim rules 1 to 6 | Ways of working (rules); Rig threads (their loop) | Kris's answers to JUDGEMENT-ONLY-WAKE and AUTOCOMPACT-WINDOW |
| 1 | Rig launchd watcher on sol and terra; threads arm only a doorbell waiter | Rig and dotfiles; Ways of working for the contract | WATCHER-SHAPE, WATCHER-PUSH |
| 2 | `ki work watch` and doorbell verbs; `mgit sync --push` replaces `pass.sh` | tools-ki (ki.prj.tools-burndown) | Revised WATCH-VERB; the push guard |
| 3 | The Observatory hosts the watcher; channel wake if proven | ki.prj.observatory; Ways of working for the channel rule | OBSERVATORY-SYNCS, CHANNEL-PROOF, the Observatory's own plan |

#### 8. Draft rollout lines, to send only after Kris agrees

- To personal.reg.rig-sol and personal.reg.rig-terra: `- IMPORTANT · <date> · LISTEN-SYNC-AGREED · Ways of working (ki.prj.ways-of-working): Kris agreed <answers>. Now: your loop wakes the thread only on a WAKE line or a new message line; routine pulls and pushes go to passes.log silently; re-arm at the two-hour limit silently; set /autocompact <value> once at opening. Next: <phase 1 if agreed>. Design: ki-principal +/_WORK/ki.prj.ways-of-working/design/outside-watcher/design.md.`
- To this work: the acknowledgement Kris asked for, recorded as the decisions entry that takes the answers.

## Queries

### JUDGEMENT-ONLY-WAKE - Stop routine syncing from waking the Rig threads

**Context:** Each Mac's Rig thread runs a background loop that does a sync pass every 15 minutes and checks its messages every two minutes. Today the loop wakes the thread whenever a pass pulls or pushes anything, even when nothing needs a decision, and that, with a forced re-arm every 110 minutes, is most of the 880k-token day. Kris has said to keep in-thread syncing for now. This changes only when the loop wakes the thread, not what it does.

**Query:** Should the Rig loops on sol and terra wake their thread only when a pass needs judgement or a new message line arrives, logging routine pulls and pushes silently?

**Options:**

a) (recommended, confidence high - it removes most wakes with a few lines changed in a Rig-owned script, nothing else changes, and it is easily undone) Yes, now: send one line each to personal.reg.rig-sol and personal.reg.rig-terra to change their loop, re-arm silently at the two-hour limit, and read the pass log only when Kris asks.

b) Leave the loops as they are until the outside watcher exists.

### AUTOCOMPACT-WINDOW - A smaller compaction window for long-lived threads

**Context:** Kris prefers long-lived threads that clean themselves up. Claude Code compacts a conversation automatically when it reaches a set size, the "auto-compact window". Kris noted it can be set per user or per repository; the installed Claude Code (2.1.309) also accepts it for one session, at launch (`--autocompact 200k`) or inside the thread (`/autocompact`). A per-repository setting would also shrink every other thread in that repository. A coordinator re-reads its whole work package after a compaction, which here is about 3,000 lines across the five files, so too small a window compacts again soon.

**Query:** Should long-lived listening and sync threads set a smaller window for themselves, and at what size?

**Options:**

a) (recommended, confidence medium - the per-session setting fits Kris's per-thread aim, but the best size is a judgement and whether Orca passes launch flags through is untested) Set 200k per thread, with `/autocompact 200k` once at opening, or the launch flag where the launch line can be set; review after a week.

b) The same per thread, but 400k: fewer compactions, larger context between them.

c) Set it per repository for the repositories whose threads are long-lived (chezmoi, ki-principal), accepting that their other threads shrink too.

### WATCHER-SHAPE - Adopt the outside watcher and its phases

**Context:** Kris asked for a watcher outside the threads that does sync, GitHub pull and message-queue watching, and wakes a thread only for judgement; the Observatory is to be its lasting home and Rig and dotfiles own any interim job. The design (WATCHER-DESIGN above) uses a shell program per Mac, with no model, that leaves a small "doorbell" file per work; the open thread waits only on its doorbell, and the doorbell carries reason codes, never instructions. Kris also said to keep today's in-thread way as the tactical solution. The Observatory work has not started on this; its package is with Kris with nine open queries.

**Query:** Should the doorbell design become the way of working, with a Rig launchd job on sol and terra as its first form before the Observatory takes it over?

**Options:**

a) (recommended, confidence medium - it takes polling out of threads soon with a small Rig job and lets the Observatory adopt the same contract later, but no part has been prototyped) Adopt it: Ways of working writes the doorbell contract into `ki-coordination`; Rig and dotfiles build the interim launchd job on both Macs; a revised WATCH-VERB asks tools-ki for the watch and doorbell verbs; the Observatory takes the job over in its own time.

b) Adopt the contract only, keep in-thread loops with the interim rules, and wait for the Observatory to host the watcher.

c) Skip the Rig step and ask the Observatory work to build the watcher first.

### WATCHER-PUSH - May the outside job push without a session open

**Context:** Today each Rig thread's pass pushes commits that exist only on that Mac, under Kris's decisions to publish from the secondary Mac and to push everything stacked. That happens while Kris's Rig thread is open. A job outside the threads would also push when no session is open, for example overnight, publishing commits agents made. It is a fixed script, not an agent, and pushes only fast-forward, never forced and never bypassing hooks. Pulling clean checkouts is not in question.

**Query:** May the outside job push, and when?

**Options:**

a) (recommended, confidence medium - it keeps pushing tied to a switch Kris already controls, but it is a new kind of unattended action) Push only while that Mac's Rig thread has syncing switched on; otherwise the job only fetches and fast-forwards, and leaves pushes for the next session.

b) Never push from the job; it pulls and rings, and pushes stay with the threads.

c) Always push, whether or not a session is open.

### OBSERVATORY-SYNCS - Does the Observatory sync, or only watch

**Context:** On 31 October, under HOST-RECONCILE, Kris said "observatory watching, it's not doing the syncing", with ad hoc sync from it a later idea; the Observatory's own SYNC-DIRECTION query is waiting to close on those words. On 1 November, OBSERVATORY-WATCHER said the Observatory as a real app is the lasting home for listening and syncing, running sync, GitHub pull and the queue watch. The two differ on whether the Observatory runs the sync.

**Query:** Does the 1 November word replace the 31 October one, so that the Observatory eventually runs the sync passes too?

**Options:**

a) (recommended, confidence medium - the later, more specific word reads as a deliberate change, but Kris did not say it replaces the earlier one) Yes: the Observatory eventually hosts the whole watcher, sync included; SYNC-DIRECTION closes as superseded and the Observatory work is told so.

b) No: the Observatory watches and rings doorbells, and the sync pass stays a Rig job permanently.

### CHANNEL-PROOF - Test a push wake into Claude Code threads

**Context:** Without a push into the session, a thread can only be woken by a background command it started ending, and a running background command stops Kris compacting the thread in Orca and needs a re-arm every two hours. Claude Code "channels" let a local connector push a message into a running session, as the Telegram plugin does; that would let the doorbell say "look at your queue" with nothing running in the background. The installed version's help does not list the feature, it may depend on how Orca launches Claude Code, and nothing has been tried here.

**Query:** Should a short attended trial test a local channel as the wake, inside an Orca-hosted thread as well as a terminal one?

**Options:**

a) (recommended, confidence medium - it is the only path seen that removes background loops entirely, but it rests on vendor documentation and may not work under Orca) Yes: one bounded trial on a scratch thread with Kris watching, carrying only "look at your queue"; until it passes, threads use the doorbell waiter.

b) No: rely on the doorbell waiter and revisit when the Observatory app is built.

### UNCLAIMED-NUDGE - What happens when no thread is listening

**Context:** When a doorbell rings for a work whose thread is closed or asleep, the design holds the ring and the thread catches up from its queue when Kris opens it, as Kris's message proposed. Nothing tells Kris that something needs judgement in the meantime. The watcher must not start an agent to deal with it, under the Techne Programme Focus and WAKE-HOST c).

**Query:** Should the watcher tell Kris when a judgement ring sits unclaimed?

**Options:**

a) (recommended, confidence medium - a desktop notice is cheap and starts no agent, but it adds an interruption Kris has not asked for) After 30 minutes unclaimed, one macOS notification naming the work and the reason, at most once per ring.

b) Hold silently; Kris sees it on next opening the thread or the Observatory.

### 🤖 → 👤 Handoff to supervisor · since 12:42 GMT

👤 7 with you

- [with you] JUDGEMENT-ONLY-WAKE · owner · since 12:42
- [with you] AUTOCOMPACT-WINDOW · owner · since 12:42
- [with you] WATCHER-SHAPE · owner · since 12:42
- [with you] WATCHER-PUSH · owner · since 12:42
- [with you] OBSERVATORY-SYNCS · owner · since 12:42
- [with you] CHANNEL-PROOF · owner · since 12:42
- [with you] UNCLAIMED-NUDGE · owner · since 12:42

🧵 ki.prj.ways-of-working
