# [Knowledge Islands model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Initiatives/knowledge-islands-model/knowledge-islands-model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working/ways-of-working.md) › thread-states

**Run report at 23:19 BST · last mark 22:34 BST**

---

## Done

- This is the revision `thread-states-rev` made in place. It rebuilds the design on Kris's THREAD-STATES-HANDOFF refinement of 17 October 23:07 BST: two holders, one handoff between them that carries a target, and the verbs send and receive. It also takes in two later entries in the [decisions log](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/ways-of-working/decisions.md). COUNSEL (23:09 BST) asks for advice, not transcription, so section 1 says where I think the model should bend. THREAD-STATES-IDEATION (23:17 BST) says states describe the conversation, not the turn, that every state should show its age, and that nothing goes into standards while ideating.
- The first version's groundwork stands. It covered the ki-pmo standard as `restart-standard` left it in harness `0e4cdebd`, section 1.4 of the [restart report](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/ways-of-working/restart.report.md), the [thread-lifecycle report](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/ways-of-working/thread-lifecycle.report.md), `ki-checkpoint`, ki-delegation, the [coordinator hook](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/hooks/coordinator-reminder.sh), the banner tests and tools-ki. The design still sits on top of the restart standard without replacing any of it, and still supersedes thread-lifecycle sections 1 to 4.
- What changed from the first version: the four states become two holders plus one handoff with a target, and the old "pick up" becomes a receive. Sections 1 to 4 are redrawn. A new section 5 covers what the target buys later, and the migration becomes section 6, held until ideation ends. ACK-TAKE becomes RECEIVE-WORDS, and HANDOFF-SHAPE is new. STATES-WRITE is withdrawn, because THREAD-STATES-IDEATION holds the write-in.
- Collisions checked again: the new words `with`, `sent`, `send`, `receive` and `finished` collide with no roadmap horizon, Project lifecycle value, work-record status or messages-block signal. `received` is not used as a status anywhere in tools-ki or the harness.
- No standard, skill, hook, style, record or checkpoint was changed. Only this report and the run report are committed.

### 1. The state machine

Every state is about the conversation on a topic and who holds it, as THREAD-STATES-IDEATION puts it. It is not about whose turn it is in the chat. Runs that the thread launches are detail inside "With agent". There are three kinds of state:

- **Holder states:** With agent and With you. One party holds the work, whether working on it or simply holding it. Nobody multi-processes, so a holder that does nothing is still the holder.
- **The handoff:** one state, Sent, which always carries a **target** and the sender it came from. There are two targets today: agent to you, and you to agent.
- **Finished:** terminal, and entered only from With you.

Both verbs belong to parties. The holder **sends** the work into the handoff, and only the target **receives** it out. There is no edge from one holder straight to the other, and none from the handoff back to itself.

```text
      HOLDER              HANDOFF, one state with a target       HOLDER

  ┌────────────┐                                            ┌────────────┐
  │            │──send──▶  SENT · agent → you  ──receive──▶ │            │
  │ WITH AGENT │                                            │  WITH YOU  │
  │            │◀─receive─ SENT · you → agent  ◀───send──── │            │
  └────────────┘                    ▲                       └────────────┘
     ▲      │                       │                             │
     └──────┘             opener or send line                     │ finish
  launch, finish,         in a fresh session                      ▼
  steer: no change                                          ┌────────────┐
                                                            │  FINISHED  │
                                                            └────────────┘
```

Where I think the model should bend, in line with COUNSEL:

- **Only the holder can send.** A message Kris sends while the agent holds the work is a **steer**. It changes nothing: the thread logs it, folds it into the running work and answers in one line. Without this rule, a mid-run question would read as Kris handing work back that he does not hold.
- **"Read and hand straight back" passes through With you.** When the work is Sent to you, any message other than a bare receive word is a receive followed by a send in one move. That keeps the rule that there is no handoff-to-handoff edge, and it means the thread can always say when Kris last had the work.
- **Sent to agent is real but short-lived.** In a live chat the thread receives Kris's reply as soon as its turn starts, so the banner almost never shows it. It lasts when the thread is not running to receive it: a closed session, a crash, a compaction mid-turn, or a send line waiting in a fresh session. That is when it is worth seeing, because an old Sent to agent means a stuck send. Keep it as a state, and show it in `thread.status` and `ki agent status` rather than in reports.
- **Hold is a send and a receive in one move.** Today's "hold" is Kris asking the agent to drain and send to him. Because he asked, his hold word is also his receive. The work passes through Sent to you and lands With you. There is still no direct edge between the holders.
- **Finish runs its own close-out.** Close is Kris's verb from With you. The close-out tidy is the sync that finish performs, done by the thread in that one move. If the tidy turns up real work, the finish stops and is read as a send: the work goes back to the agent, which sends it back when done, and Kris closes again.
- **Every state shows how long it has held.** Each state records its `since` time. A report states it (`since 23:40 BST`), because a written age goes stale and a start time does not. The status tools turn it into an age. As THREAD-STATES-IDEATION says, only With agent is chased by heartbeat, because agents get stuck. An age With you is reported when Kris asks, never nagged.

The **sync** steps referred to below are unchanged from the first version:

- **status:** rewrite `thread.status`.
- **pick-up:** rewrite the pick-up block and `Current state`.
- **commit:** commit the checkpoint and thread folder by explicit path, pull with rebase and push fast-forward.
- **tidy:** delete answered and homed reports.
- **drain:** finish or stop agents at a safe point, park open queries, sweep leftovers, and copy what resuming needs out of the state folder.
- **mark:** strike the mark and classify the log entries since the last one.
- **re-sync:** pull fast-forward, re-read the standard if it changed, re-read the checkpoint and its messages block (`FIRST-STEP` first), run `ki agent status`, read the inbox and take stock.

| Move | From, to | Trigger | Sync it performs | What the thread says |
| --- | --- | --- | --- | --- |
| open | none, Sent to agent, With agent | opener, or the send line pasted into a fresh session (Kris's send) | receive: re-sync, status | the re-bootstrap report; if nothing launches, it sends back at once |
| steer | With agent, With agent | any owner message while the agent holds the work | owner words logged first, status | a timed line starting with the state glyph |
| launch or finish | With agent, With agent | a run launched or queued, or one finished while others run | status | a timed update |
| send to you | With agent, Sent to you | the last run finishes with nothing queued, or the turn needed no run, or it is waiting only on another thread | drain: pick-up, commit, tidy, status | the Summary ending with the state line and the send line |
| you receive | Sent to you, With you | a receive word as the whole message | status, pick-up with the receive time, commit, mark | one line ending with the state line |
| hold | With agent, Sent to you, With you | `hold` while the agent holds the work | full drain (agents finish within about 15 minutes or stop at a safe point), the send, then the receive with its mark | the hold report, then the state line and the send line |
| you send | With you, Sent to agent | any other message: a reply block, a bare letter, an instruction, a question or `back to you` | owner words logged first, status | nothing yet, because the receive follows in the same turn |
| pass through | Sent to you, With you, Sent to agent | any message other than a bare receive word while Sent to you | the receive's status and receive time (no mark), then the send's | as for you send |
| agent receives | Sent to agent, With agent | the thread's turn starts on the message, or a fresh session reads the send line | re-sync, parked queries put back, status | a timed update as it launches; if nothing launches, a short Summary and a send back |
| finish | With you, Finished | `close`; from Sent to you this counts as a receive first | the four close-out steps, pick-up written last as `finished`, checkpoint retired, run closed | the closing full summary with the Finished state line and no send line |

Two rules carry over from the first version unchanged. A thread whose own runs have all finished, and which is only waiting on another thread, sends to you and lists `- [waiting] <thread> - <what>`; today it shows BUSY. Compaction, a red x and re-anchoring are not moves: the thread re-syncs and the state stands. A third rule changes: a blocking query raised while runs continue is a line inside With agent, not a send, because the agent still holds the rest of the work.

What the thread says, and how often:

| State | Says | How often |
| --- | --- | --- |
| With agent | Timed updates on each launch and finish, a heartbeat naming each run's step and its age, and a blocking query in one line | At once on events; heartbeat under HEARTBEAT-PACE. The only state with a heartbeat |
| Sent to you | The Summary that sent it, then nothing | Never unprompted; asked, it gives the age (`sent to you 2 h ago, unread`) |
| With you | The one-line receive or the hold report, then nothing | Never; asked, it gives the age (`with you since Tuesday 18:10`) |
| Sent to agent | Nothing: the next thing said is the receive's update | Shown only by `thread.status` and `ki agent status`, flagged when old |
| Finished | The closing full summary | Once |

Every message the thread sends starts with its state glyph (section 4), so the last thing visible after Cmd-K, or in Zed's panel that cannot be cleared, always shows who holds the work.

### 2. Names

Each set names the two holders, the handoff, the two verbs, and the words Kris types to receive and to send. A banner word is in title case. The status word, used in the pick-up block and `thread.status`, is `<state>:<party>`, where the party is `owner` or `agent` today and `thread/<label>`, `run/<name>` or `person/<handle>` later (section 5).

| | a) Sent and with (recommended) | b) Tray | c) Kris's literal words |
| --- | --- | --- | --- |
| Agent holds | With agent, `with:agent` | Working, `working:agent` | Agent, `agent` |
| Handoff, agent to you | Sent to you, `sent:owner` | In your tray, `tray:owner` | Handoff → human, `handoff:owner` |
| You hold | With you, `with:owner` | On your desk, `desk:owner` | Human, `human` |
| Handoff, you to agent | Sent to agent, `sent:agent` | In agent's tray, `tray:agent` | Handoff → agent, `handoff:agent` |
| Terminal | Finished, `finished` | Finished, `finished` | Finished, `finished` |
| Verbs | send, receive | post, collect | send, receive |
| Kris receives | `with me` (canonical, safe for speech-to-text), `ack`, `got it`, `seen`, `hold` | `collected`, `got it`, `hold` | `received`, `ack`, `hold` |
| Kris sends | any other message; bare `back to you` sends without new instruction | any other message; bare `posted` | any other message; bare `send` |
| Line that brings it back | the send line, `Back to you on <label> ...` | `Collect <label> ...` | `Resume <label> ...` |
| For | The banner word is the result of the last verb: send gives "Sent to", receive gives "With". It says Kris's own phrases ("it's with me"), extends to any target, and avoids the agentic jargon THREAD-STATES-IDEATION wants gone | "In your tray" says unread, and which way, very vividly | Exactly the words Kris used |
| Against | "you" means the owner, so the standard has to say so | Two metaphors (tray and desk) for one model; "desk" means little for an agent | "Human" is cold in a banner addressed to Kris; the two handoffs differ only by an arrow; agentic jargon |

FINISHED stays the terminal word in every set.

How each maps from today:

| Today, banner | Today, pick-up Status | a) | b) | c) |
| --- | --- | --- | --- | --- |
| BUSY | `busy` | With agent, `with:agent` | Working | Agent |
| REST | `rest` | Sent to you, `sent:owner` | In your tray | Handoff → human |
| HOLD | `hold` | With you, `with:owner` | On your desk | Human |
| DRAINED (retired) | `drained` | With you, `with:owner` | On your desk | Human |
| SEEN (proposed, never adopted) | none | With you, `with:owner` | On your desk | Human |
| resume (a move today, not a state) | none | Sent to agent, `sent:agent` | In agent's tray | Handoff → agent |
| DONE | `done` | Finished, `finished` | Finished | Finished |

The checkpoint front-matter `state` stays `active`, because `ki-checkpoint` RESUME validates it. The pick-up block's Status remains the one home of the thread state, and it adds `since`.

### 3. Receiving and sending

- **Receive words (set a):** `with me` is canonical, because Kris mostly speaks his messages and speech-to-text can turn "ack" into "act" or "back". `ack`, `got it`, `seen` and `hold` are also accepted as the whole message, ignoring case and trailing punctuation. `act` and `back` are refused, because each could mean "go ahead".
- **Send:** every other message is a send, or a receive and a send when the work was Sent to you. `back to you` as the whole message sends with no new instruction: the agent re-syncs and continues authorised work, and approves nothing new.
- **Mark:** a receive strikes the mark only when the work comes to rest with Kris, which means a bare receive word or `hold`. A pass-through records the receive time but does not mark. Otherwise every reply would strike a mark and classify the log, which is too heavy and empties "recap since the mark" of meaning. The mark then means "where I last stopped and caught up".
- **Receive words at other states:** at With agent, a receive word gets one line, `🤖 Noted at 23:12 BST - still with agent: quiet-style, harness-records.`, and changes nothing, because nothing was sent. Only `hold` drains. At With you, it gets `🧑 Already with you since 23:12 BST.`
- **Partial answers:** the thread acts on the answered tags. The unanswered ones stay `[waiting]`, and the next send's reply block carries a full entry for each. If the answers launch nothing, it sends back at once with a short Summary.
- **A question that needs only an answer** is a send. The agent receives it, answers in one turn and sends back, starting with the state glyph. It launches nothing and leaves no Summary behind.

### 4. Banner format

This also answers Kris's question of 17 October 23:17 BST about a richer Markdown format. Each candidate below is rendered, not fenced, so opening this report in Zed's Markdown preview shows it as a reply would. Footers are meant to be `##`, level with Done, In Progress and Queries. They are drawn at `###` here to keep this report's heading levels. In every candidate the header puts the state, with its age, in front of the form line.

**A. Party glyphs with an arrow (recommended).** Each party has a glyph: 🤖 agent, 🧑 you, and later 👤 another person, with a thread's label beside 🤖. A holder shows one glyph, and the handoff shows sender, arrow and target, so direction and target read at a glance. 🏁 is the end. Header form line:

**🤖 → 🧑 Sent to you since 23:40 BST · Summary at 23:40 BST · last mark 22:34 BST**

Footer, one per state:

### 🤖 With agent · since 23:41 BST · 2 running · 1 queued · 3 queries

- [running] harness-records - capture the agreed harness records
- [queued] states-write - after harness-records
- [waiting] STATE-NAMES

### 🤖 → 🧑 Sent to you · since 23:40 BST · 3 queries

- [waiting] STATE-NAMES
- [waiting] BANNER-FORM
- [committed] checkpoint and thread folder, pushed

### 🧑 With you · since 23:52 BST · 3 queries parked

- [parked] 3 queries in the checkpoint
- [committed] checkpoint and thread folder, pushed

### 🧑 → 🤖 Sent to agent · since 23:55 BST

- [waiting] receive: the thread has not yet picked this up

### 🏁 Finished · Ways of working closed

- [closed] decisions promoted, checkpoint retired, thread folder deleted, run archived

Later targets, in the same grammar:

### 🤖 → 🤖 Sent to State of play · since 09:10 BST · 1 item

### 🤖 → 👤 Sent to &lt;person&gt; · since 09:10 BST · 2 queries

**B. One emoji per state, direction in words** (the first version's form, renamed). Footer:

### 📨 Sent to you · since 23:40 BST · 3 queries

With agent ⏳, With you ✋ and Finished 🏁. Both handoffs share 📨, so their direction is in the words only.

**C. Words and an arrow, no emoji.** Footer:

### Agent → you · sent since 23:40 BST · 3 queries

**D. Hybrid:** A plus a one-line shaded code band. Footer:

### 🤖 → 🧑 Sent to you · since 23:40 BST · 2 queries

```text
▶▶  AGENT → YOU  ◀◀
```

**E. Today:** the 52-column block-letter frame, as at the foot of this report. Block letters cannot carry a target that varies, so a handoff frame would need its target in a caption.

GitHub alerts stay rejected. In Zed and the terminal they show as a quote with a literal `[!WARNING]` in it.

| Form | Zed panel | Terminal | Obsidian, GitHub | Narrow panel | Direction and target at a glance | Distinct when scrolling back | What the tests would check |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A. Party glyphs | Heading† | Bold heading line† | Renders | Wraps; no width | Strong: sender, arrow and target are the first thing shown | Strong: one glyph for a holder, two with an arrow for a handoff, so the shape differs as well as the word | The last `##` matches `^## (🤖\|🧑\|👤)( → (🤖\|🧑\|👤))? (With\|Sent to) .+ · since \d{2}:\d{2} [A-Z]+( · .+)?$` or the Finished line; the form line opens with the same prefix |
| B. Emoji per state | Heading† | Bold line† | Renders | Wraps | Weak: in words only | Strong for the states; the two handoffs look alike | Fixed emoji per state word |
| C. Words and arrow | Heading | Bold line | Renders | Wraps | Medium: the arrow carries it | Weak: no glyph | Text pattern only |
| D. Hybrid | Heading and band† | Renders | Renders | Band is 19 columns | Strong | Strongest: adds the shaded block | A, plus the band's text |
| E. Block letters | Only if the panel is 52 or more columns† | Renders | Renders | Wraps or cuts below 52 | Caption only | Strong, but every frame has the same silhouette | Today's 52-code-point frame tests |

† Expected from each renderer's Markdown support; not seen by eye in this run, which has no display. Opening this report in Zed's preview settles it.

**Recommendation:** A at both ends. The state glyph also opens every other message (`🤖 23:44 BST - quiet-style step 3 of 5`). The facts after the state are fixed:

- With agent: `since <time>`, then `<n> running · <n> queued · <n> queries`, leaving out any zero.
- Sent to you: `since <time> · <n> queries` or `no queries`.
- With you: `since <time> · <n> queries parked` or `nothing parked`.
- Sent to agent: `since <time>`.
- Finished: `<Project> closed`.

The `[at rest]` and `[hold]` list items go, because the heading now says it. The width problem goes with the frame. Block letters survive nowhere in ki-pmo; past reports keep their frames, and anything that reads them accepts both forms. D is the fallback if Kris misses the weight of the shaded block.

### 5. What the target buys later

The target turns the state machine from a rule about Kris and one thread into a grammar for any handoff between parties. None of this is proposed for now; it is what the shape leaves room for.

- **Agent-to-agent handoff.** A run's life already fits the shape. Launching or queueing a run is a send to `run/<name>`, and today's `queued` is Sent to that run. The run starting and reading its brief is its receive and re-sync, and `running` is With that run. Writing its report is a send back to `thread/<label>`, and the thread reading the report is the thread's receive. Threads and runs could then share one vocabulary in `ki agent status`. My advice is to keep the thread's own state about the conversation, as THREAD-STATES-IDEATION asks, and to treat runs as items inside With agent until a reason appears to show them in the same words.
- **Between threads, and to the state-of-play thread.** A messages-block line or inbox entry is a send whose target is `thread/<label>`. The target receives it when it next bootstraps or acts on its Messages block. A unit handed over whole, for example a cross-territory matter given by a coordination thread to State of play, is Sent to that thread until it receives. The sender's own state changes only if that unit was all it held. State of play could then read every thread's state and age and tell Kris "three topics with you, the oldest since Tuesday; one sent to you, unread". That is the awareness of other threads THREAD-STATES-IDEATION describes.
- **Another person.** `person/<handle>` behaves like `owner`: no heartbeat, its age reported only when asked. A thread can send to a colleague and show 🤖 → 👤 until they receive.
- **`thread.status`.** The line today is `HH:MM <zone> - <state word> - <what>`. It would become `HH:MM <zone> - <state>:<party> since <HH:MM zone> - <what>`, for example `23:40 BST - sent:owner since 23:40 BST - 3 queries`. Old words are read as their set a) mapping, so nothing breaks while threads convert.
- **`ki agent status`.** Threads would be listed beside runs, with columns for topic, state, target, age and what, inside [KI-TOOL-KI-CLI-127](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-127-agent-status-live-threads.md). It would flag only what can get stuck: With agent with a step older than 10 minutes, Sent to agent older than a few minutes (nobody is receiving), and Sent to a thread older than a day (an unread message). A human holder's age is shown, never flagged.
- **Per-item state.** With a target, the machine could apply to each unit of work rather than to the topic as a whole. I would not do that now. The topic-level state is what Kris reads, and per-item state belongs with the work records.

### 6. Migration, held while ideating

THREAD-STATES-IDEATION ("let's not go ahead and steamroll into making updates whilst we're ideating") holds all of this until Kris says the model is settled. The edits, one line each, once it is:

- **ki-agentic-harness, ki-pmo Glossary, Thread types and Coordinator responsiveness:** the holder, handoff and finished states, the send and receive verbs, steer, pass-through, the cadence table, and the heartbeat at With agent only.
- **ki-agentic-harness, ki-pmo Banner, Draining, Picking up and Project close:** the party-glyph state line at both ends replaces the REST, BUSY, HOLD and DONE frames; Status values become `<state>:<party>` with `since`; the send line replaces both resume lines; drain runs on send to you and on hold; Finished at close.
- **ki-agentic-harness, ki-pmo Committing the thread folder and Surfaces:** "every resting point, mark and hold" becomes "every send to you, receive, hold and finish", keeping restart 1.4's cadence; the new `thread.status` form.
- **ki-agentic-harness, ki-pmo generator, banner tests, `ki-coordinator` style and the hook line:** state-line blocks and pattern tests replace the frame tests; the style and hook line are regenerated.
- **ki-agentic-harness, ki-delegation:** `step <n> of <m>` status lines; a change-aware waiter; a run report ends with the Sent state line through the generated footer rule.
- **ki-agentic-harness, ki-checkpoint:** no rule change; `state: active` and `role` stand. A rename of "checkpoint", which THREAD-STATES-IDEATION raises, would be its own design.
- **tools-ki:** the `thread.status` parser, the state, target and age columns, and the flags, inside [KI-TOOL-KI-CLI-127](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-127-agent-status-live-threads.md).
- **chezmoi:** redeploy the regenerated style and hook through Rig chezmoi.
- **Existing checkpoints:** each thread rewrites its own pick-up block at its next update, and old words are read as new until then.
- **Ordering:** `restart-standard` and `harness-records` have landed, so nothing blocks the write-in once it is released. SHAPE-AGREE's naming migration, and any renaming of threads, topics or checkpoints from THREAD-STATES-IDEATION, could share one pass with it.

## In Progress

- Nothing of this run is running. `work-cascade` is queued in run `ways-of-working`.

### Outstanding - no action requested now

- STATES-WRITE is withdrawn. THREAD-STATES-IDEATION of 17 October 23:17 BST holds any write-in, and it returns as a query once Kris says the model is settled.
- THREAD-STATES-IDEATION also raises names for threads, checkpoints and topics ("checkpoint" being "a bad name now"). That is outside this revision. The state names here contain no "thread", "session", "agentic" or "checkpoint", so they survive whichever names are chosen.
- Another session has `+/_THREADS/chezmoi/decisions.md` dirty in ki-principal. I left it untouched.

## Queries

### HANDOFF-SHAPE - one handoff with a target, or two handoffs

**Context:** Kris weighed one handoff state that carries a target against two separate handoff states. Two states are simpler while only two parties exist, but they multiply with every new party. One state with a target, recorded as `sent:<party>` with its sender, covers agent-to-agent, thread-to-thread and person handoffs without new states. It still shows as two visibly different variants today (🤖 → 🧑 and 🧑 → 🤖). Section 1 also proposes that only the holder sends, that a mid-run message is a steer, that a direct reply from Sent to you passes through With you, and that `hold` is a send and a receive in one move.

**Query:** Should the handoff be one state carrying a target, with the section 1 rules, as the model to keep developing?

**Options:**

a) (recommended) Agree in principle: one Sent state carrying its target and sender, the holder alone sends, a mid-run message is a steer, a direct reply passes through With you, `hold` is a send and receive in one move, and every state shows its `since` time; nothing is written into standards yet.

b) Two handoff states, one per direction, with the same rules.

### STATE-NAMES - what the states, verbs and words are called

**Context:** Section 2 gives three sets. Set a) makes each banner word the result of the last verb: a send gives "Sent to you", a receive gives "With you". It uses Kris's phrase "it's with me", extends to any target, and avoids the agentic jargon Kris wants gone. `with me` is the canonical receive word because it survives speech-to-text, and `back to you` is the bare send. Set b) is a tray metaphor and set c) is Kris's literal words.

**Query:** Which name set should the model carry forward?

**Options:**

a) (recommended) Set a): With agent, Sent to you, With you, Sent to agent and Finished, with status words `<state>:<party>`, the verbs send and receive, the receive words `with me`, `ack`, `got it`, `seen` and `hold`, the bare send `back to you`, and the send line starting `Back to you on <label>`.

b) Set b): Working, In your tray, On your desk, In agent's tray and Finished, with post and collect.

c) Set c): Agent, Handoff, Human and Finished, with send and receive.

### RECEIVE-WORDS - how receiving moves the mark and what replies do

**Context:** Under section 3, a bare receive word or `hold` lands the work With you and strikes the mark. A reply sent while the work is Sent to you passes through With you, recording when it was received but not striking the mark, so that "recap since the mark" keeps its meaning. Partial answers carry the rest forward. At With agent, a receive word is noted in one line, and only `hold` drains. This replaces ACK-TAKE.

**Query:** Should receiving and sending work as section 3 sets out?

**Options:**

a) (recommended) Adopt section 3 in principle: a bare receive word or `hold` receives and marks, a pass-through records the receive without marking, any other message is a send, partial answers carry forward, and at With agent a receive word is noted and only `hold` drains.

b) The same, but no receive strikes the mark; only `mark` or `hold` does.

### BANNER-FORM - the Markdown-native state line

**Context:** Section 4 renders five forms against today's 52-column block letters, which cannot show a target that varies or adapt to the panel's width. Form A gives each party a glyph (🤖 agent, 🧑 you, 👤 another person) and shows a handoff as sender, arrow and target, for example `## 🤖 → 🧑 Sent to you · since 23:40 BST · 3 queries`. A holder shows one glyph, so the shape differs as well as the word. The same prefix opens the form line and every other message. Zed rendering is expected but not seen by eye; opening this report in Zed's preview settles it.

**Query:** Which banner form should the model carry forward?

**Options:**

a) (recommended) Form A, party glyphs with an arrow, at both ends and on every message, with the fixed facts and `since` time of section 4; the block letters retire when the write-in comes, and past reports keep theirs.

b) Form D, form A plus a one-line shaded code band.

c) Form B, one emoji per state with direction in words.

### HEARTBEAT-PACE - how often the thread speaks while the agent holds the work

**Context:** This is carried over unchanged, and THREAD-STATES-IDEATION confirms that only the agent's hold needs periodic updates, "because I know that agents can get stuck". The check polls every 5 minutes and wakes at once when a run finishes. The thread speaks at 5 minutes only if a step has changed, and always by 10, flagging any status older than 10 minutes. Runs write `HH:MM <zone> - step <n> of <m> - <plain words>`.

**Query:** Which heartbeat should a thread keep while the agent holds the work?

**Options:**

a) (recommended) The change-driven rule: speak at 5 minutes on a changed step, always by 10, with `step n of m` status lines.

b) A fixed 5-minute heartbeat with `step n of m` status lines.

c) A fixed 10-minute heartbeat with `step n of m` status lines.

```text
HANDOFF-SHAPE

Agree in principle the model in section 1 of /Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/ways-of-working/thread-states.report.md: one Sent state carrying its target and sender, the holder alone sends, a mid-run message is a steer, a direct reply passes through With you, hold is a send and receive in one move, and every state shows its since time; nothing is written into standards yet.

---

STATE-NAMES

Carry forward set a) of section 2 of thread-states.report.md: With agent, Sent to you, With you, Sent to agent and Finished, status words <state>:<party>, the verbs send and receive, the receive words "with me", ack, "got it", seen and hold, the bare send "back to you", and the send line starting "Back to you on <label>".

---

RECEIVE-WORDS

Adopt section 3 of thread-states.report.md in principle: a bare receive word or hold receives and strikes the mark, a pass-through records the receive without marking, any other message is a send, partial answers carry forward, and at With agent a receive word is noted in one line and only hold drains.

---

BANNER-FORM

Carry forward form A of section 4 of thread-states.report.md: party glyphs with an arrow (🤖 agent, 🧑 you, 👤 another person, 🏁 finished) at the front of the form line, as the closing "## <glyphs> <State> · since <time> · <facts>" heading over the bracketed list, and leading every other message; the block letters retire at the write-in and past reports keep theirs.

---

HEARTBEAT-PACE

Use the change-driven heartbeat at With agent only: poll every 5 minutes and wake at once when a run finishes, speak at 5 minutes only on a changed step and always by 10, flag a status older than 10 minutes, and have runs write "HH:MM <zone> - step <n> of <m> - <plain words>" status lines.
```

```text
╭─ run report · 2026-10-17T22:19:40Z ──────────────╮
│                                                  │
│  █▀▀▄ █  █ █▀▀▀ █  █   · thread busy             │
│  █▀▀▄ █  █ ▀▀▀█  ▀█▀   · running or queued work  │
│  █▄▄▀ █▄▄█ ▄▄▄█   █    · lines below say which   │
│                                                  │
╰──────────────────────────────────────────────────╯

- [queued] work-cascade - queued in ways-of-working
- [waiting] HANDOFF-SHAPE
- [waiting] STATE-NAMES
- [waiting] RECEIVE-WORDS
- [waiting] BANNER-FORM
- [waiting] HEARTBEAT-PACE
- [committed] thread-states report, revised
```
