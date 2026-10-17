# [Knowledge Islands model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Initiatives/knowledge-islands-model/knowledge-islands-model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working/ways-of-working.md) › thread-lifecycle

**Run report at 23:00 BST · last mark 22:34 BST**

---

## Done

- Read the ki-pmo standard (thread states, cadence and heartbeat, Banner, Draining a thread, Picking up a thread, Project close), the ki-delegation status-line and monitoring rules, the `ki-checkpoint` `state` and `role` fields, the [ki-coordinator output style](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/output-styles/ki-coordinator.md) and the [coordinator hook](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/hooks/coordinator-reminder.sh) as they stand at 22:55 BST.
- Designed against the text as it will stand once both harness runs have landed: `quiet-style`, finished by 23:00 BST, cuts the hook line to a pointer plus five hard rules, one of which is "timed updates with a 5-minute check while work runs", so a pace change edits that rule; `restart-standard`, still running, writes the restart state model of the [restart report](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/ways-of-working/restart.report.md) into ki-pmo, ki-delegation and ki-checkpoint, so the pick-up block's Status stays the one home of the thread state and the checkpoint gains `role`.
- Measured the output width from the Bash tool and drew every banner candidate with a script that asserts each framed line is exactly 52 or 64 code points.
- Changed no standard, skill, hook, style, record or checkpoint. Only this report is committed.

### 1. States and lifecycle

Four states stay; acknowledgement is added as an attribute of REST and HOLD, not a fifth state. Draining stays an activity that the thread performs while BUSY.

```text
                      opener from the state-of-play thread
                                    │
                                    ▼
   ┌────────┐  owner: ack     ┌──────────┐  thread launches or queues   ┌──────────┐
   │  seen  │◀────────────────│          │─────────────────────────────▶│          │
   │ (REST, │                 │   REST   │                              │   BUSY   │
   │ acked) │────────────────▶│          │◀─────────────────────────────│          │
   └────────┘  any new report └──────────┘  last agent finishes and     └──────────┘
               or owner work     │  │       nothing is queued              │
                                 │  │                                      │
                  owner: hold    │  │ owner closes the        owner: hold  │
                  (nothing to    │  │ Project after the       (thread      │
                  drain)         │  │ close-out tidy          drains)      │
                                 ▼  ▼                                      ▼
                     ┌──────────┐  ┌──────────┐            ┌──────────────────────┐
                     │   HOLD   │  │   DONE   │            │ HOLD, once every run │
                     │          │  │ terminal │            │ finished or stopped  │
                     └──────────┘  └──────────┘            └──────────────────────┘
                          │                                          │
                          └──────────── resume line ─────────────────┘
                              pasted by the owner, or handed on by
                              the state-of-play thread: re-bootstrap,
                              then REST, or BUSY if authorised work
                              restarts. ack on a hold shows SEEN with
                              the caption "thread on hold".
```

| Transition | Triggered by | What the thread does |
| --- | --- | --- |
| open → REST or BUSY | the state-of-play thread's opener, then the owner | bootstraps; BUSY as soon as it launches work |
| REST → BUSY | the thread, on launching or queueing a run the owner authorised | timed one-line update |
| BUSY → REST | an agent finishing, when it was the last and nothing is queued | full Summary, REST frame, resume line |
| REST → seen | the owner, `ack` | one-line reply and the SEEN frame |
| seen → REST | the thread, on any new owner-facing output, or the owner, on new work | the new report carries the plain REST or BUSY frame |
| REST or BUSY → HOLD | the owner, "hold", or a territory hold through the state-of-play thread | drains, then the hold report |
| HOLD → REST or BUSY | the owner pasting the hold resume line, or the state-of-play thread naming it for restart | re-bootstrap, parked queries back, banner |
| REST → DONE | the owner closing the Project, after the four close-out steps | the DONE frame once, then the checkpoint is removed |

How the thread state relates to the Project and the checkpoint:

| Thread state | Banner word | Pick-up block Status | Checkpoint frontmatter `state` | Project note `lifecycle` |
| --- | --- | --- | --- | --- |
| REST | REST | `rest` | `active` | `active` |
| REST, acknowledged | SEEN | `rest`, with a `Seen:` time | `active` | `active` |
| BUSY, draining included | BUSY | `busy` | `active` | `active` |
| HOLD | HOLD, or SEEN captioned "thread on hold" | `hold` | `active` | `active`; a long hold may be paused by the owner through ki-repo-kb-streams, never by the thread |
| DONE | DONE | `done`, written last | removed by `ki-checkpoint` REMOVE | set to its closed value at Project close |

The checkpoint's frontmatter `state` never tracks the thread, because `ki-checkpoint` RESUME validates `active`; the pick-up block's Status is the thread state, and acknowledgement never changes it.

### 2. Update cadence by state

| State | What the thread says | How often |
| --- | --- | --- |
| BUSY | a timed one-to-two-line update on each launch and each finish; a heartbeat naming each running agent's current step; a blocking query in one line the moment it arises; the full Summary when the last run finishes | launch, finish and query at once; heartbeat as HEARTBEAT-PACE settles |
| REST | the Summary that brought it to rest, then nothing | never unprompted; no check is armed |
| REST, acknowledged | the one-line acknowledgement and the SEEN frame, then nothing | never unprompted |
| HOLD | the hold report, then nothing | never; the thread does not wake |
| DONE | the closing full summary with the DONE frame | never again |

**Five or ten minutes.** The detached check costs nothing while it waits, but each wake is a model turn and an entry in a Zed panel that cannot be cleared. Background agents in this run typically take 10 to 40 minutes and rewrite their status every two minutes, but many 5-minute heartbeats repeat the step the last one named. A fixed 10 minutes halves the noise but breaks the personal default of an update "at least every few minutes" and lets a stuck agent go unnoticed longer. The better rule is change-driven. The check still wakes at once when any agent finishes, and polls every 5 minutes. The thread speaks at a 5-minute wake only if some running agent's step has changed. Otherwise it waits on, and speaks at 10 minutes regardless, naming the unchanged steps and flagging any agent whose status is older than 10 minutes as possibly stuck. The waiter does the comparison, so a wake with nothing new never reaches the thread.

**What the agents' status steps must do.** The thread can only report what the status line holds, so the status line must carry progress rather than activity alone:

- **Form:** `HH:MM <zone> - step <n> of <m> - <plain words>`, where the step numbers are the brief's numbered steps, which the ki-delegation prompt shape already requires.
- **Rewrite:** at each change of step, and at least every two minutes with a fresh time even when the step is unchanged, so its age shows whether the agent is alive.
- **Content:** plain words about the work, never a command or tool output; a wait names what it waits on.
- **Last line:** `DONE` on its own, unchanged.

A heartbeat then reads, for example, `23:10 BST - quiet-style step 3 of 5, regenerating the skill; thread-lifecycle step 4 of 6, drafting the report.`

### 3. Owner acknowledgement

**The words.** `ack` is canonical: short, speakable and unlike anything else the thread hears. The thread also takes `seen`, `noted` and `with me` as the whole message, case and trailing punctuation ignored, because speech-to-text may render `ack` as "act" or "back". A message that says anything more is an ordinary steering message.

**What the thread does.** It makes no launch and changes no state:

1. It writes `HH:MM <zone> - seen - <state word>, <n> queries with owner` to its `thread.status`, so `ki agent status` and the state-of-play thread can tell read threads from unread ones.
2. It replies with one line, `Seen at 23:12 BST - at rest, 3 queries with you.`, then the SEEN frame, then the same list the last banner carried with `- [seen] <local time>` added beneath the state item, then, at rest, the resume line, or after a hold the hold resume line.
3. It records `Seen: <UTC>` in the checkpoint's `Current state` the next time it writes the checkpoint for another reason, and never makes a commit for an acknowledgement alone.

The reply becomes the last thing in the panel, so the panel itself shows that the latest state has been read. Any later output from the thread replaces it, so it can never claim that something new has been seen.

**Attribute, not state.** Acknowledgement applies only where nothing moves: REST and HOLD. At BUSY, `ack` gets the one-line reply alone, such as `Seen at 23:12 BST - still busy: quiet-style, restart-standard.`, with no frame, because the next heartbeat will move the panel on anyway and a SEEN frame must never stand over running work. Open queries stay visible in every case: the SEEN list repeats each `[waiting]` item, and the third caption says the queries are with the owner. The pick-up block's Status is unchanged, so resume behaves exactly as for REST or HOLD.

**The banner.** A new block word, with the form word `seen` on the top border and the second caption naming the underlying state, rather than a caption change on REST: a REST frame with altered captions looks identical at a glance, which defeats the purpose. The candidates, in the existing glyphs, each line 52 code points:

SEEN, recommended: it says exactly what happened, uses only glyphs the font already has, and reads unlike REST, BUSY, HOLD and DONE at a glance.

```text
╭─ seen · 2026-10-17T22:30:00Z ────────────────────╮
│                                                  │
│  █▀▀▀ █▀▀▀ █▀▀▀ █▄ █   · owner has read this     │
│  ▀▀▀█ █▀▀  █▀▀  █ ██   · thread at rest          │
│  ▄▄▄█ █▄▄▄ █▄▄▄ █  █   · queries with owner      │
│                                                  │
╰──────────────────────────────────────────────────╯
```

SEEN after a hold, the only caption that varies:

```text
╭─ seen · 2026-10-17T22:30:00Z ────────────────────╮
│                                                  │
│  █▀▀▀ █▀▀▀ █▀▀▀ █▄ █   · owner has read this     │
│  ▀▀▀█ █▀▀  █▀▀  █ ██   · thread on hold          │
│  ▄▄▄█ █▄▄▄ █▄▄▄ █  █   · queries parked          │
│                                                  │
╰──────────────────────────────────────────────────╯
```

USER: says where the ball is, but "user" reads as a role, not an event, and the thread cannot know the owner has acted on anything.

```text
╭─ seen · 2026-10-17T22:30:00Z ────────────────────╮
│                                                  │
│  █  █ █▀▀▀ █▀▀▀ █▀▀▄   · owner has read this     │
│  █  █ ▀▀▀█ █▀▀  █▀▀▄   · thread at rest          │
│  █▄▄█ ▄▄▄█ █▄▄▄ █  █   · queries with owner      │
│                                                  │
╰──────────────────────────────────────────────────╯
```

ACKD: needs new A, C and K glyphs and reads as jargon.

```text
╭─ seen · 2026-10-17T22:30:00Z ────────────────────╮
│                                                  │
│  ▄▀▀▄ █▀▀▀ █ ▄▀ █▀▀▄   · owner has read this     │
│  █▀▀█ █    █▀▄  █  █   · thread at rest          │
│  █  █ █▄▄▄ █  █ █▄▄▀   · queries with owner      │
│                                                  │
╰──────────────────────────────────────────────────╯
```

MINE: the M needs five columns and the I three, so the word still fills 19; whose "mine" it is depends on who reads it.

```text
╭─ seen · 2026-10-17T22:30:00Z ────────────────────╮
│                                                  │
│  █▄ ▄█ ▀█▀ █▄ █ █▀▀▀   · owner has read this     │
│  █ ▀ █  █  █ ██ █▀▀    · thread at rest          │
│  █   █ ▄█▄ █  █ █▄▄▄   · queries with owner      │
│                                                  │
╰──────────────────────────────────────────────────╯
```

OWNR: the W needs five columns, so the word takes 20 and pushes its captions one column right of every other frame; the abbreviation also reads poorly.

```text
╭─ seen · 2026-10-17T22:30:00Z ────────────────────╮
│                                                  │
│  ▄▀▀▄ █   █ █▄ █ █▀▀▄   · owner has read this    │
│  █  █ █ █ █ █ ██ █▀▀▄   · thread at rest         │
│  ▀▄▄▀ ▀▄▀▄▀ █  █ █  █   · queries with owner     │
│                                                  │
╰──────────────────────────────────────────────────╯
```

### 4. Banner width

**Detection does not work.** The Bash tool runs commands with no terminal attached. There, `tput cols` fails with "No value for $TERM" because `TERM` is unset; with `TERM` set, it falls back to the terminfo default of 80. `$COLUMNS` is `0`, `stty size` fails with "stdin isn't a terminal", and `tty` reports "not a tty". `ZED_ENVIRONMENT` and `CLAUDECODE` are set but carry no geometry. Even a real measurement would be the wrong number. Zed's agent panel is a graphical pane that renders Markdown. How many columns a code block shows depends on the pane's width, the buffer font, its size and zoom, and any split, and all of these can change after the reply is written. The same report is also read in a terminal, in a file preview and on GitHub. The width has to come from the owner, once.

**The ruler.** Kris views the block below once in the Zed agent panel at the usual layout and replies with the last digit fully visible on the second line before it wraps or is cut off. The result is a single fixed number. Because the frame is checked byte for byte by the ki-pmo banner tests and found in archives by its block word, the width belongs in the ki-pmo standard as one fixed value for every thread, not in a per-machine preference that would let frames differ. A personal note in the managed chezmoi configuration records only the measurement and the layout it was taken at.

```text
         1         2         3         4         5         6         7         8         9        10
1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
```

**52 and 64 side by side.** The current REST frame at 52:

```text
╭─ summary · 2026-10-17T22:30:00Z ─────────────────╮
│                                                  │
│  █▀▀▄ █▀▀▀ █▀▀▀ ▀▀█▀   · thread at rest          │
│  █▀▀▄ █▀▀  ▀▀▀█   █    · nothing running         │
│  █  █ █▄▄▄ ▄▄▄█   █    · nothing queued          │
│                                                  │
╰──────────────────────────────────────────────────╯
```

The same frame at 64, with the word column widened to take five letters and captions of up to 31 characters:

```text
╭─ summary · 2026-10-17T22:30:00Z ─────────────────────────────╮
│                                                              │
│  █▀▀▄ █▀▀▀ █▀▀▀ ▀▀█▀        · thread at rest                 │
│  █▀▀▄ █▀▀  ▀▀▀█   █         · nothing running or queued      │
│  █  █ █▄▄▄ ▄▄▄█   █         · open queries listed below      │
│                                                              │
╰──────────────────────────────────────────────────────────────╯
```

A five-letter acknowledgement at 64, NOTED, which is also a natural spoken acknowledgement:

```text
╭─ seen · 2026-10-17T22:30:00Z ────────────────────────────────╮
│                                                              │
│  █▄ █ ▄▀▀▄ ▀▀█▀ █▀▀▀ █▀▀▄   · owner has read this report     │
│  █ ██ █  █   █  █▀▀  █  █   · thread at rest                 │
│  █  █ ▀▄▄▀   █  █▄▄▄ █▄▄▀   · open queries with the owner    │
│                                                              │
╰──────────────────────────────────────────────────────────────╯
```

A wider frame buys five-letter words (NOTED, READY, PAUSE) and captions that can say what the list says, such as "open queries listed below". It costs re-drawing all five frames, re-baselining the banner tests and the output style, and a frame that wraps in any narrower view. It is worth doing only if the ruler shows at least 66 columns, which leaves two columns of margin.

### 5. Forward work

Nothing here is applied; each line waits on the queries below.

- ki-agentic-harness, ki-pmo: add acknowledgement (the words, the SEEN frame and its hold caption, the `[seen]` list item, the `Seen:` checkpoint line, the BUSY one-liner) to Banner and Picking up a thread, with a `seen-footer` block in the banner tests.
- ki-agentic-harness, ki-pmo: replace the fixed 5-minute heartbeat with the change-driven 5/10 rule in Coordinator responsiveness, the shortened hook line and the [ki-coordinator output style](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/output-styles/ki-coordinator.md).
- ki-agentic-harness, ki-delegation: set the status-line form `HH:MM <zone> - step <n> of <m> - <plain words>` in the run packet and the Rules footer.
- tools-ki, ki-delegation monitoring: give the run waiter a change-aware mode, waking at 5 minutes only on a changed step and always at 10, and show each status line's age in `ki agent status`, flagging one older than 10 minutes.
- tools-ki, ki-pmo Surfaces: accept the `seen` state word in `thread.status` and list threads awaiting the owner's reading beside runs.
- ki-agentic-harness, ki-pmo: only if BANNER-WIDTH lands at 64, re-draw every frame at the new width, re-baseline the banner tests and the output style, with chezmoi redeploying the style.

## In Progress

Nothing is running.

### Outstanding - no action requested now

- `restart-standard` is still writing the restart design into ki-pmo, ki-delegation and ki-checkpoint, and `quiet-style` has just finished changing the hook line and ki-pmo; whoever writes this design in must rebase on their landed text.

## Queries

### ACK-WORD - how you mark a thread as read

**Context:** In Zed's agent panel you cannot clear a thread you have dealt with, so you cannot tell whether you have already read its latest state. The design above adds `ack` (also `seen`, `noted`, `with me`), which makes the thread reply with one line and a SEEN banner. That reply becomes the last thing in the panel until the thread says anything new. It is an attribute of REST and HOLD only; at BUSY you get the one line alone. Open queries stay listed and the resume line still follows.

**Query:** Do you want acknowledgement as designed, with SEEN as its block word?

**Options:**

a) (recommended) Adopt `ack` with the synonyms `seen`, `noted` and `with me`, and the SEEN frame as an attribute of REST and HOLD, with a one-line reply only at BUSY.

b) Adopt the same mechanism with USER as the block word.

c) Keep the REST word and change only its captions to say the owner has read it.

### HEARTBEAT-PACE - how often a busy thread speaks

**Context:** Today a busy thread wakes and speaks every 5 minutes, often repeating the step it last named, in a panel you cannot clear. Under the change-driven rule, the check still polls every 5 minutes and wakes at once when an agent finishes. The thread speaks at 5 minutes only if a step has changed, and always by 10, flagging an agent whose status is older than 10 minutes. Agents write `step n of m` so there is progress to report.

**Query:** Which heartbeat should busy threads keep?

**Options:**

a) (recommended) The change-driven rule: speak at 5 minutes on a changed step, at 10 regardless, with agents writing `step n of m` status lines.

b) Keep the fixed 5-minute heartbeat and add only the `step n of m` status lines.

c) A fixed 10-minute heartbeat with the `step n of m` status lines.

### BANNER-WIDTH - whether the footer frame grows to 64

**Context:** No thread can detect the Zed panel's width: the Bash tool has no terminal, so `tput cols` fails or guesses 80 and `$COLUMNS` is 0, and the panel's width depends on the pane, font and zoom anyway. The ruler in section 4 lets you measure it once. A 64-column frame would allow five-letter words and longer captions but needs every frame and test redrawn. That is worth doing only if the panel shows at least 66 columns.

**Query:** Will you read the ruler once so the width can be decided on the measurement?

**Options:**

a) (recommended) Read the ruler in the Zed agent panel at your usual layout and reply with the last digit you see whole; at 66 or more, the standard moves every frame to 64, otherwise it stays at 52.

b) Keep 52 without measuring, and use only four-letter block words.

### LIFECYCLE-WRITE - who writes this into the standards

**Context:** Once ACK-WORD and HEARTBEAT-PACE are answered, they need the edits listed in section 5 across ki-pmo, ki-delegation, the hook line, the output style, the banner tests and tools-ki. `restart-standard` is editing the same harness files now, and `quiet-style` has just changed the hook line. Writing it in means one harness run chained after `restart-standard`, then a tools-ki run.

**Query:** Should the thread dispatch the write-in once `restart-standard` lands?

**Options:**

a) (recommended) Chain one ki-agentic-harness run after `restart-standard` to write the answered parts into ki-pmo, ki-delegation, the hook line, the output style and the banner tests, then a tools-ki run for the waiter, status age and `seen` state word.

b) Hold the write-in until RESTART-AGREE has fully landed and you have reviewed a combined lifecycle note.

```text
ACK-WORD

Adopt `ack` with the synonyms `seen`, `noted` and `with me` as the owner acknowledgement, with the SEEN frame as an attribute of REST and HOLD (second caption "thread at rest" or "thread on hold"), a one-line reply only at BUSY, the `[seen]` list item and a `Seen:` checkpoint line, as designed in /Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/ways-of-working/thread-lifecycle.report.md section 3.

---

HEARTBEAT-PACE

Use the change-driven heartbeat: poll every 5 minutes and wake at once when an agent finishes, speak at 5 minutes only on a changed step and always by 10 minutes, flag a status older than 10 minutes, and have agents write `HH:MM <zone> - step <n> of <m> - <plain words>` status lines, as in section 2 of thread-lifecycle.report.md.

---

BANNER-WIDTH

Width: <last digit you see whole on the ruler in section 4 of thread-lifecycle.report.md>. At 66 or more, move every ki-pmo frame to 64; otherwise keep 52.

---

LIFECYCLE-WRITE

Chain one ki-agentic-harness run after restart-standard lands to write the answered parts of thread-lifecycle.report.md into ki-pmo, ki-delegation, the hook line, the ki-coordinator output style and the banner tests, then a tools-ki run for the change-aware waiter, status age and the `seen` state word.
```

```text
╭─ run report · 2026-10-17T22:00:00Z ──────────────╮
│                                                  │
│  █▀▀▄ █  █ █▀▀▀ █  █   · thread busy             │
│  █▀▀▄ █  █ ▀▀▀█  ▀█▀   · running or queued work  │
│  █▄▄▀ █▄▄█ ▄▄▄█   █    · lines below say which   │
│                                                  │
╰──────────────────────────────────────────────────╯

- [running] restart-standard - restart design into the standards
- [waiting] ACK-WORD
- [waiting] HEARTBEAT-PACE
- [waiting] BANNER-WIDTH
- [waiting] LIFECYCLE-WRITE
- [committed] thread-lifecycle report
```
