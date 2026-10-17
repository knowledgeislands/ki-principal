# [Knowledge Islands model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Initiatives/knowledge-islands-model/knowledge-islands-model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working/ways-of-working.md) › thread-states

**Run report at 23:12 BST · last mark 22:34 BST**

---

## Done

- I read the THREAD-STATES decision of 17 October 23:01 BST and the [thread-lifecycle report](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/ways-of-working/thread-lifecycle.report.md) in full. I also read the ki-pmo standard as `restart-standard` left it in harness `0e4cdebd` (Glossary, Thread types, Coordinator responsiveness, Banner, Surfaces, Bootstrap, Messages between threads, Committing and Tidying the thread folder, Draining, Picking up, Project close) and section 1.4 of the [restart report](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/ways-of-working/restart.report.md).
- I also read the `ki-checkpoint` `state` and `role` rules, the ki-delegation run packet, prompt shape and monitoring, the [coordinator hook](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/hooks/coordinator-reminder.sh), the banner tests and generator under `skills/change-management/ki-pmo/scripts/`, and how tools-ki handles `thread.status`. tools-ki does not parse it yet, so no tool breaks when the words change.
- This design fits on top of the restart standard; it replaces none of it. It renames the triggers "resting point" and "hold" that section 1.4 uses for commits and parking, narrows when BUSY applies, and folds the two resume lines into one. It replaces sections 1 to 4 of the thread-lifecycle design: the SEEN frame, acknowledgement as an extra detail on REST and HOLD, and the 64-column frame. None of those was ever applied.
- Collisions checked: `hold` is already a roadmap horizon in tools-ki and `paused` a Project lifecycle value in ki-work. `done` and `ready` are work-record statuses, and `READY` is the restart signal in the messages block. The recommended names avoid all five.
- No standard, skill, hook, style, record or checkpoint was changed. Only this report is committed.

### 1. The state machine

Who holds the work defines the states. **Draining** is something the thread does on the way into the owner's hands, not a state. **Re-syncing** is something it does on the way back. Every transition writes everything the thread knows somewhere durable, or reads it back.

I keep the agent-to-owner handoff as a state and make the owner-to-agent handoff a transition. The handoff to the owner lasts until Kris reads it, which may be hours, and telling "handed over, unread" from "with me, acknowledged" is the Cmd-K problem itself. The handoff back to the agent lasts a single turn: the thread re-syncs and either launches work or hands straight back. So no banner ever shows that handoff, and its proper home is the pick-up block, which already describes it.

```text
          AGENT HOLDS THE WORK          ┊          OWNER HOLDS THE WORK
                                        ┊
   ┌──────────────────┐   hand over     ┊        ┌──────────────────┐
   │                  │─────────────────┊───────▶│                  │
   │    WITH AGENT    │                 ┊        │   OVER TO YOU    │
   │                  │◀────────────────┊────────│                  │
   └──────────────────┘    pick up      ┊        └──────────────────┘
     │   ▲      ▲                       ┊                  │
     │   │      │                       ┊                  │ take
     │   │      │                       ┊                  ▼
     │   │      │                       ┊        ┌──────────────────┐
     │   │      │                       ┊        │                  │
     │   │      └─────── pick up ───────┊────────│     WITH YOU     │
     │   │                              ┊        │                  │
     └───┼───────────── hold ───────────┊───────▶│                  │
         │                              ┊        └──────────────────┘
      opener or                         ┊                  │
      pick-up line                      ┊                  │ finish
                                        ┊                  ▼
                                        ┊        ┌──────────────────┐
                                        ┊        │     FINISHED     │
                                        ┊        └──────────────────┘
```

The names here are option a) of STATE-NAMES. The **sync** steps referred to below are:

- **status:** rewrite `thread.status`.
- **pick-up:** rewrite the checkpoint's pick-up block (status, pick-up line, next steps) and `Current state`.
- **commit:** commit the checkpoint and thread folder by explicit path, pull with rebase and push fast-forward.
- **tidy:** delete answered and homed reports.
- **drain:** finish agents or stop them at a safe point, park every open query in the checkpoint with its tag, one line of context and option a), sweep leftovers (unpushed commits, stale branches, stray files, spent runtime files, `tmp/`), and copy what resuming needs out of the state folder.
- **mark:** strike the mark and classify the log entries since the last one.
- **re-sync:** pull fast-forward, re-read the standard if it changed, re-read the checkpoint and its messages block (`FIRST-STEP` first), run `ki agent status`, read the inbox and take stock.

| Transition | From, to | Trigger | Sync it performs | What the thread says |
| --- | --- | --- | --- | --- |
| open | none, With agent | opener, or the pick-up line in a fresh session | re-sync, status | the re-bootstrap report; if nothing launches, it hands over at once |
| launch or finish | With agent, With agent | the thread launches or queues a run, or an agent finishes while others still run | status; decisions log if the owner spoke | a timed one-to-two-line update |
| hand over | With agent, Over to you | agent finishing: its last running agent finishes and nothing is queued, or the turn needed no agent | pick-up, commit, tidy, status | the Summary under the report heading, ending with the state line and the pick-up line |
| take | Over to you, With you | owner acknowledgement: `ack`, `seen`, `noted`, `with me` or `hold` as the whole message | drain (light, as nothing runs), mark, pick-up, commit, tidy, status | one line, the state line with its list, then the pick-up line |
| hold | With agent, With you | owner hold: `hold`, or a territory hold through the state-of-play thread | drain (full: agents finish within about 15 minutes or stop at a safe point; every repository touched committed and pushed), mark, pick-up, commit, tidy, status | the hold report (`## Done` per repository, `## Parked`, `## Left over`), then the state line and the pick-up line; if it cannot drain it stays With agent and says what blocks it |
| pick up | Over to you or With you, With agent | owner reply: any other message, including a reply block, a bare letter, an instruction or the pick-up line | owner words logged first, then re-sync, parked queries put back, pick-up, status | a timed one-line update as it launches; if nothing launches, it hands over again at once with a short Summary |
| finish | With you, Finished | owner close; a close sent from Over to you counts as a take first | the four close-out steps, pick-up block written last as `finished`, checkpoint removed, run closed | the closing full summary ending with the Finished state line and no pick-up line |

Three rules make this tighter than today's:

- **With agent means the thread's own agents are running or queued, and nothing else.** A thread that is blocked, or waiting on another thread, with nothing of its own running, hands the work over and lists `- [waiting] <thread> - <what>`. Only the owner or a messages-block line moves it on, and its heartbeat would only repeat itself. Today such a thread shows BUSY.
- **Compaction, a red x and re-anchoring are not transitions.** The thread re-syncs and the state stays as it was.
- **A reply ending `then hold`** asks the thread to take instead of handing over at its next hand-over, for an owner who is stepping away.

What the thread says, and how often:

| State | Says | How often |
| --- | --- | --- |
| With agent | Timed one-to-two-line updates on each launch and finish. A heartbeat naming each running agent's step, with its age. A blocking query in one line the moment it arises | At once on launch, finish or query. Heartbeat under HEARTBEAT-PACE: poll every 5 minutes; speak at 5 only if a step changed, always by 10, and flag any status older than 10 minutes. The only state with a heartbeat |
| Over to you | The hand-over Summary, then nothing | Never unprompted; no check is armed |
| With you | The one-line take, or the hold report, then nothing | Never; the thread does not wake |
| Finished | The closing full summary | Once |

Every message a coordinating thread sends shows its state, so the bottom of the panel always answers "whose is it?". A report ends with the state line. Any other reply, whether a timed update, a heartbeat or a one-line answer, starts with the state's emoji, for example `⏳ 23:10 BST - quiet-style step 3 of 5, regenerating the skill`. Kris clears his shells with Cmd-K, and Zed's panel cannot be cleared. Showing the state on every message is the substitute: the last thing visible always says who holds the work.

### 2. Names

Each set names the four states and the five transitions. The banner word is title case and the status word, used in the pick-up block and `thread.status`, is lower-case kebab.

| | a) Who holds the work (recommended) | b) Radio relay | c) Plain |
| --- | --- | --- | --- |
| Agent working | With agent, `with-agent` | Working, `working` | Busy, `busy` |
| Handed to owner, unread | Over to you, `over-to-you` | Over, `over` | Review, `review` |
| Owner has it | With you, `with-you` | Roger, `roger` | Paused, `paused` |
| Terminal | Finished, `finished` | Finished, `finished` (radio "out" set aside for Kris's word) | Finished, `finished` |
| Transitions | hand over, take, hold, pick up, finish | over, roger, break, go ahead, out | report, pause, hold, resume, finish |
| Line that brings it back | `Pick up <label> ...` | `Go ahead <label> ...` | `Resume <label> ...` |
| For | Says exactly Kris's model ("with the agent", "it's with me"), reads correctly from the panel, and collides with nothing | Short and memorable, and "roger" is a natural acknowledgement to say aloud | Familiar words |
| Against | Two words per state; "you" is the owner, so the standard has to say so | "Roger" and "over" are jargon, and "over" alone reads as "ended" | `review` echoes the work-record status `awaiting-review`; `paused` collides with the Project lifecycle value; it does not say who holds the work |

FINISHED stays the terminal word in every set. It is Kris's choice, it is rare, and it avoids the work-record status `done`.

How each name maps from today:

| Today, banner | Today, pick-up Status | a) | b) | c) |
| --- | --- | --- | --- | --- |
| BUSY | `busy` | With agent, `with-agent` | Working | Busy |
| REST | `rest` | Over to you, `over-to-you` | Over | Review |
| HOLD | `hold` | With you, `with-you` | Roger | Paused |
| DRAINED (retired) | `drained` | With you, `with-you` | Roger | Paused |
| SEEN (proposed, never adopted) | none | With you, `with-you` | Roger | Paused |
| DONE | `done` | Finished, `finished` | Finished | Finished |

The checkpoint front-matter `state` stays `active` throughout, because `ki-checkpoint` RESUME validates it. The pick-up block's Status is the one home of the thread state.

### 3. Acknowledgement and replies

- **Take words:** `ack` is canonical. `seen`, `noted`, `with me` and `hold` are also accepted when sent as the whole message, ignoring case and trailing punctuation. `act` and `back` are refused even though speech-to-text produces them for "ack", because each could mean "go ahead".
- **Mark:** a take strikes the mark, because Kris defined a hold on 15 October as "a Mark + stopping all work". The mark then means "where I last caught up", which is what Cmd-K meant in a shell. A recap later reaches back exactly that far. Outstanding items still carry forward across marks, so nothing open is lost.
- **Take at each state:** at With agent, an ack word gets one line, `⏳ Noted at 23:12 BST - still with agent: quiet-style, harness-records.`, and nothing changes, because the work is not his yet. Only `hold` drains running work. At With you, an ack word gets `✋ Already with you since 23:12 BST.` and nothing else.
- **Any other message is a pick-up.** The thread logs the words first, re-syncs, and moves the work to the agent.
- **Answering only some queries:** the thread acts on the answered tags and launches what they authorise. The unanswered tags stay open as `[waiting]` items, and the next hand-over's reply block carries a full entry for each. If the answers launch nothing, the thread hands back at once with a short Summary, so the work returns to Kris showing Over to you with the remaining queries.
- **A question that needs only an answer:** the thread answers in one turn, starting with the state emoji, and the work returns to the side it came from. It launches nothing and leaves no Summary behind.

### 4. Banner format

Each candidate is rendered below, not fenced, so it shows here as it would in a reply. Candidate A's footer is meant to be `##`, a closing section that stands level with Done, In Progress and Queries. It is drawn at `###` here so that this report keeps the ki-pmo heading levels. The header for every candidate except today's is the form line with the state put in front of it.

**A. State heading (recommended).** Header form line:

**🔔 Over to you · Summary at 23:20 BST · last mark 22:34 BST**

Footer, one per state:

### ⏳ With agent · 2 running · 1 queued · 3 queries

- [running] harness-records - capture the agreed harness records
- [running] tools-status - thread state words in ki agent status
- [queued] states-write - after harness-records
- [waiting] STATE-NAMES

### 🔔 Over to you · 3 queries

- [waiting] STATE-NAMES
- [waiting] BANNER-FORM
- [waiting] STATES-WRITE
- [committed] checkpoint and thread folder, pushed

### ✋ With you · 3 queries parked

- [parked] 3 queries in the checkpoint
- [committed] checkpoint and thread folder, pushed

### 🏁 Finished · Ways of working closed

- [closed] decisions promoted, checkpoint retired, thread folder deleted, run archived

**B. Bold status line.** Footer:

🔔 **Over to you** · 3 queries · committed and pushed

**C. Blockquote.** Footer:

> 🔔 **Over to you** · 3 queries
>
> - [waiting] STATE-NAMES
> - [committed] checkpoint and thread folder, pushed

**D. One-row table.** Footer:

| 🔔 Over to you | 3 queries | committed and pushed |
| --- | --- | --- |

**E. GitHub alert,** one alert type per state (NOTE for With agent, WARNING for Over to you, TIP for With you). Footer:

> [!WARNING]
> 🔔 **Over to you** · 3 queries · committed and pushed

**F. Hybrid,** the state heading plus a one-line shaded code band, which keeps the visual weight of a code block at any width. Footer:

### 🔔 Over to you · 2 queries

```text
▶▶  OVER TO YOU  ◀◀
```

**G. Today.** The 52-column block-letter frame in a fenced block, as at the foot of this report.

| Form | Zed agent panel | Terminal (Claude Code) | Obsidian | GitHub | Light and dark | Narrow panel | At a glance, scrolling back | Hook line and banner tests would check |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A. State heading | Renders as a heading | Bold heading line† | Renders | Renders | Theme text colour; the emoji keeps its own colour | Wraps; no width | Strong: the largest text near the end of the message, with a distinct emoji shape and colour per state | The last `##` matches `^## (⏳ With agent\|🔔 Over to you\|✋ With you\|🏁 Finished)( · .+)?$`, then a blank line and the list; the form line opens with the same emoji and word; the hook's rule 4 says "closing with the state line" |
| B. Bold line | Renders | Renders† | Renders | Renders | As A | Wraps | Medium: body-size text, easily lost among other bold lines | The last paragraph matches the state pattern |
| C. Blockquote | Renders with a bar | Renders, bar or indent† | Renders | Renders | Bar takes the theme | Wraps | Medium: reports already quote Kris in blockquotes | First quote line matches; every list item quoted |
| D. One-row table | Renders† | Box table† | Renders | Renders | Theme | Squeezes or scrolls sideways | Weak: looks like any other table | Exact header and delimiter rows |
| E. GitHub alert | Not as an alert: a quote with literal `[!WARNING]`† | Literal tag | Callout | Coloured callout | Strong colour where it renders | Wraps | Strong on GitHub and Obsidian; noise in Zed and the terminal, where Kris reads | Alert type per state and its first line |
| F. Hybrid | Renders | Renders | Renders | Renders | Shaded band in both | Band is 19 columns | Strong: heading plus shaded band | A, plus the band's exact text per state |
| G. Block letters today | Renders if the panel is 52 or more columns wide | Renders | Renders | Renders | Theme | Wraps or cuts below 52; width unknowable, as thread-lifecycle found | Strong, but all four frames share one silhouette and differ only in the letters | Today's 52-code-point frame tests |

† Expected from each renderer's Markdown support; not seen by eye in this run, which has no display. The thread can check in one step: paste section 4 into the panel once.

**Recommendation:** A, applied at both ends. The state goes at the front of the form line, so a report opened from the top shows it first. The closing `## <emoji> <State> · <facts>` heading, with its bracketed list beneath, ends every report. Every other message starts with the emoji. The facts after the state are fixed:

- With agent: `<n> running · <n> queued · <n> queries`, leaving out any zero.
- Over to you: `<n> queries` or `no queries`.
- With you: `<n> queries parked` or `nothing parked`.
- Finished: `<Project> closed`.

The `[at rest]` and `[hold]` items go, because the heading now carries that. The width problem and BANNER-WIDTH go with the frame. Block letters survive nowhere in ki-pmo: the four frames, the hold frame and the DONE frame are retired. Past reports keep their frames, and anything that reads them accepts both forms. `ki-recap`'s own single-session frame belongs to that skill and is untouched. F is the fallback if Kris misses the weight of the shaded block.

### 5. Migration

Each line gives the repository and the skill.

- **ki-agentic-harness, ki-pmo Glossary and Thread types:** the four states and five transitions replace the hold, drain and resume rows; drain stays an activity, done on take and hold; the Banner row and the Coordination threads Close bullet use the new names.
- **ki-agentic-harness, ki-pmo Coordinator responsiveness:** the cadence table, the change-driven heartbeat at With agent only, and the state emoji on every message.
- **ki-agentic-harness, ki-pmo Coordinating-thread practices and Banner:** the state at the front of the form line; the state heading and its list replace the REST, BUSY, HOLD and DONE frames; `[at rest]` and `[hold]` items removed; the `rest-footer`, `busy-footer` and `hold-footer` blocks become four state-line blocks; one pick-up line replaces the REST and HOLD resume lines, and With agent keeps a recovery line in the pick-up block only.
- **ki-agentic-harness, ki-pmo Draining, Picking up and Project close:** drain runs on take (light) and hold (full); Status values `with-agent`, `over-to-you`, `with-you` and `finished`, with `busy`, `rest`, `hold`, `drained` and `done` read as those until each checkpoint's next update; Finished at close.
- **ki-agentic-harness, ki-pmo Committing the thread folder and Surfaces:** "every resting point, mark and hold" becomes "every hand-over, take, hold and finish", which keeps restart 1.4's cadence; `thread.status` carries the status word.
- **ki-agentic-harness, ki-pmo generator and banner tests:** the block names in `scripts/generate/index.ts`, and `scripts/banner.test.ts` moved from 52-code-point frame assertions to the state-line pattern, form-line prefix, list vocabulary and no frame in the standard.
- **ki-agentic-harness, `ki-coordinator` output style and the hook line:** regenerated with `ki dev skill generate ki-pmo --write`; rule 3 becomes "while the work is with the agent, change-driven updates", and rule 4 becomes "closing with the state line exactly as the standard prints it".
- **ki-agentic-harness, ki-delegation:** the `<name>.status` form becomes `HH:MM <TZ> - step <n> of <m> - <plain words>`; the monitor or waiter becomes change-aware; a run report ends with the Over to you state heading through the generated footer-report rule, and the `rules-*.md` footers are regenerated.
- **ki-agentic-harness, ki-checkpoint:** no rule change. `state: active` and `role` stand, and ki-pmo owns the pick-up block.
- **tools-ki, `ki agent status`:** list coordinating threads beside runs with their `thread.status` word and its age, accepting the old words, inside [KI-TOOL-KI-CLI-127](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-127-agent-status-live-threads.md); the waiter gains the 5-and-10-minute change-aware mode.
- **chezmoi:** redeploy the regenerated style and hook through Rig chezmoi.
- **Existing checkpoints:** each thread rewrites its own pick-up block at its next update, mapping the Status word and swapping in the pick-up line. Until then the old words are read as the new ones, so no migration pass and no messages-block line are needed.
- **Ordering:** `restart-standard` has landed (harness `0e4cdebd`) and this design is built on its text. `harness-records` has finished in ki-agentic-harness, so nothing there blocks the write-in run. The tools-ki run can go in parallel, since nothing else is editing tools-ki. SHAPE-AGREE's naming migration is independent and neither waits on the other.

## In Progress

- `restart-convert` is running, converting the ways-of-working checkpoint under the restart standard.
- `thread-states-rev` is queued behind this run, presumably to review this report.

### Outstanding - no action requested now

- Another session has `+/_THREADS/chezmoi/decisions.md` dirty in ki-principal. I left it untouched.
- The thread-lifecycle queries ACK-WORD, HEARTBEAT-PACE, BANNER-WIDTH and LIFECYCLE-WRITE are superseded by the THREAD-STATES decision. ACK-WORD becomes ACK-TAKE below, HEARTBEAT-PACE is carried over unchanged, BANNER-WIDTH is replaced by BANNER-FORM and LIFECYCLE-WRITE by STATES-WRITE.

## Queries

### STATE-NAMES - what the thread states are called

**Context:** Section 1 gives four states, based on who holds the work: the agent working, handed to you and unread, with you, and finished. Five transitions connect them: hand over, take, hold, pick up and finish. Draining happens on take and hold, and re-syncing on pick up. Section 2 offers three name sets. Set a) uses your own words ("with the agent", "it's with me"), and none of its names collides with the existing words `hold`, `paused`, `done`, `ready` or `review`.

**Query:** Which name set should the thread states take?

**Options:**

a) (recommended) With agent, Over to you, With you and Finished, with the transitions hand over, take, hold, pick up and finish, and the pick-up line starting `Pick up <label>`.

b) The radio set: Working, Over, Roger and Finished.

c) The plain set: Busy, Review, Paused and Finished.

### ACK-TAKE - how you take the work and how replies return it

**Context:** In Zed you cannot clear what you have dealt with. Under section 3, a whole-message `ack` (or `seen`, `noted`, `with me`, `hold`) sent while the work is Over to you moves it to With you. The thread then drains, strikes the mark, commits and pushes, and replies with one line and the state line. Any other message picks the work up. A partial answer leaves the unanswered queries open and carried forward. At With agent, `ack` is noted in one line and only `hold` drains. This replaces ACK-WORD.

**Query:** Should taking the work work as section 3 sets out, including striking the mark?

**Options:**

a) (recommended) Adopt section 3 as written: the five take words, the take drains and strikes the mark, every other message is a pick-up, partial answers carry forward, and a reply ending `then hold` takes at the next hand-over.

b) The same, but a take does not move the mark; only `mark` or `hold` does.

### BANNER-FORM - the Markdown-native state line

**Context:** Section 4 compares six Markdown forms with today's 52-column block-letter frame, which cannot adapt to the panel's width. The recommended form puts the state's emoji and name at the front of the form line, and ends every report with a `## <emoji> <State> · <facts>` heading over the bracketed list. Every other message starts with the emoji: ⏳ With agent, 🔔 Over to you, ✋ With you, 🏁 Finished. It wraps at any width and renders in Zed, the terminal, Obsidian and GitHub, and each state differs in shape and colour. GitHub alerts are expected not to render as alerts in Zed. This replaces BANNER-WIDTH.

**Query:** Which banner form should replace the block-letter frames?

**Options:**

a) (recommended) Form A: the state at the front of the form line, a closing `##` state heading with its list, and the emoji on every other message; the block-letter frames retire from ki-pmo, and past reports keep theirs.

b) Form F: form A plus a one-line shaded code band beneath the state heading.

c) Keep the block-letter frames at 52 columns with the new state words.

### HEARTBEAT-PACE - how often the thread speaks while the agent holds the work

**Context:** This is carried over from thread-lifecycle. A heartbeat runs only at With agent. Under the change-driven rule, the check polls every 5 minutes and wakes at once when an agent finishes. The thread speaks at 5 minutes only if a step has changed, and always by 10, flagging any status older than 10 minutes. Agents write `HH:MM <zone> - step <n> of <m> - <plain words>` so there is progress to report.

**Query:** Which heartbeat should a thread keep while the agent holds the work?

**Options:**

a) (recommended) The change-driven rule: speak at 5 minutes on a changed step, always by 10, with `step n of m` status lines.

b) A fixed 5-minute heartbeat with `step n of m` status lines.

c) A fixed 10-minute heartbeat with `step n of m` status lines.

### STATES-WRITE - who writes this into the standards

**Context:** Once the four queries above are answered, section 5 lists the edits: ki-pmo, ki-delegation, the generator, the banner tests, the output style and hook line in ki-agentic-harness, then tools-ki and a chezmoi redeploy. `harness-records` has finished in ki-agentic-harness. As with the restart standard, this is an owner-directed, bounded standard edit, so it needs no new harness record, and the tools-ki part fits inside [KI-TOOL-KI-CLI-127](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-127-agent-status-live-threads.md). This replaces LIFECYCLE-WRITE.

**Query:** Should the thread dispatch the write-in now that `harness-records` has landed?

**Options:**

a) (recommended) Launch one ki-agentic-harness run, `states-write`, to write the answered parts of sections 1 to 5 into ki-pmo and ki-delegation, update the generator and banner tests, regenerate the style and hook line, run the audits and push. Run tools-ki in parallel for the status words, status age and change-aware waiter, then ask Rig chezmoi to redeploy. Each thread converts its own pick-up block at its next update.

b) Hold the write-in until SHAPE-AGREE's migration, so that names, ids and states change in one pass.

```text
STATE-NAMES

Name the thread states With agent, Over to you, With you and Finished, with the transitions hand over, take, hold, pick up and finish, and the pick-up line starting "Pick up <label>", as in section 2 of /Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/ways-of-working/thread-states.report.md.

---

ACK-TAKE

Adopt section 3 of thread-states.report.md: ack, seen, noted, with me or hold as the whole message takes the work from Over to you to With you, draining, striking the mark, committing and pushing; any other message is a pick-up; partial answers carry the rest forward; at With agent an ack is noted in one line and only hold drains; a reply ending "then hold" takes at the next hand-over.

---

BANNER-FORM

Adopt form A of section 4 of thread-states.report.md: the state's emoji and name at the front of the form line, a closing "## <emoji> <State> · <facts>" heading over the bracketed list, and the emoji leading every other message (⏳ With agent, 🔔 Over to you, ✋ With you, 🏁 Finished); retire the block-letter frames from ki-pmo, with past reports keeping theirs.

---

HEARTBEAT-PACE

Use the change-driven heartbeat at With agent only: poll every 5 minutes and wake at once when an agent finishes, speak at 5 minutes only on a changed step and always by 10, flag a status older than 10 minutes, and have agents write "HH:MM <zone> - step <n> of <m> - <plain words>" status lines.

---

STATES-WRITE

Launch one ki-agentic-harness run, states-write, to write the answered parts of thread-states.report.md sections 1 to 5 into ki-pmo and ki-delegation, update the generator and banner tests, regenerate the style and hook line, run the audits and push; run tools-ki in parallel for the status words, status age and change-aware waiter inside KI-TOOL-KI-CLI-127; then ask Rig chezmoi to redeploy; each thread converts its own pick-up block at its next update.
```

```text
╭─ run report · 2026-10-17T22:12:00Z ──────────────╮
│                                                  │
│  █▀▀▄ █  █ █▀▀▀ █  █   · thread busy             │
│  █▀▀▄ █  █ ▀▀▀█  ▀█▀   · running or queued work  │
│  █▄▄▀ █▄▄█ ▄▄▄█   █    · lines below say which   │
│                                                  │
╰──────────────────────────────────────────────────╯

- [running] restart-convert - convert the ways-of-working checkpoint
- [queued] thread-states-rev - after this run
- [waiting] STATE-NAMES
- [waiting] ACK-TAKE
- [waiting] BANNER-FORM
- [waiting] HEARTBEAT-PACE
- [waiting] STATES-WRITE
- [committed] thread-states report
```
