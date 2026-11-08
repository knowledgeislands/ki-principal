# KI > Techne > Agora › mark-all-scope

**🤖 → 👤 Handoff to supervisor · Run report at 01:47 GMT · last mark 01:46 GMT**

---

## Done

Scoped a `mark` broadcast: one action from Kris that has every listening thread, on every rig, strike its mark and reply with its Summary and Status table. It is a fourth kind beside `away` and `ping` and travels the same way they do. No code, record or repository file was changed. The check run (`bun run self:check`) was not needed, because nothing changed.

### What Kris does

The tray gets one new submenu, **Mark all**, under **Ping threads**:

- **Mark and summarise**: every thread strikes its mark and replies with its Summary.
- **Mark only**: every thread strikes its mark and gives no summary.
- **No art**: a tick-box. While it is ticked, both items above ask for the summary footer without the art.

There is no command-line route in this slice (MARK-SEND below).

### What travels

This is the same broadcast line as today, with kind `mark` and two optional flags. The words are fixed, like a ping's, and carry the id and how to acknowledge:

```json
{"id":"sol-20261104T014500Z-3c9d","kind":"mark","from":"Kris","rig":"sol","at":"2026-11-04T01:45:00.000Z","text":"Mark sol-20261104T014500Z-3c9d from Kris: strike your mark now and reply with your Summary since the previous mark, with its Status table, under ki-coordination; then acknowledge with: mkdir -p ~/.local/state/ki/agora/ack/<work-id> && date -u +%FT%TZ > ~/.local/state/ki/agora/ack/<work-id>/sol-20261104T014500Z-3c9d","only":false,"noArt":false}
```

With `only` set, the words say "strike your mark now; give no summary". With `noArt` set, they add "leave the art out of the footer". The flags let the tray, the Observatory and any later tooling read the request without parsing the words. The words let a thread act without knowing the flags. Kris's own words are left out of this slice (MARK-WORDS).

### Delivery and queuing

Everything is reused unchanged. The mark is appended to each watched package's `broadcast/<work-id>.jsonl` on this rig, the package's doorbell rings, and the mark is sent to every peer, which delivers it to its own packages. A peer that is absent has the mark queued in `outbox.json` until it is present again, even across a restart.

The Orca wake line keeps its fixed form and gains one reason word, `mark`, as in `Agora: news for <package> (mark); read your messages.md and <broadcast file>`. Kris's words still never reach a terminal.

Acknowledgements use the ping's path. The Broadcasts menu shows each mark as `mark: 5 marked, 2 silent`, listing who answered and who did not, so Kris can type "mark" into a silent thread himself.

### What a listening thread does

A listening thread reads the line and acts on it as Kris saying "mark" (or "mark only", with "no art" where set):

1. Strike the mark under the standard's Striking rule.
2. Reply in the same turn with the Summary and its `## Status` section, as the standard sets at the time.
3. Write the acknowledgement.

Agora carries only the instruction. The shape of the Summary stays with `ki-coordination`, so the household-terra summary model (one Summary form, two-column table, footer art) can land without touching Agora.

A thread that is open but not coordinating has no mark. It acknowledges only, and says so in one line.

### Late pickup

A thread that was not listening, or an Orca chat that Agora cannot wake, picks up the mark later:

- **When it reads the file.** The broadcast file keeps the mark. The thread reads the file at its next turn, when it is opened or bootstrapped, or when it re-anchors after compaction, and acts on each line newer than the last broadcast it recorded.
- **When it acts.** It strikes the mark when it actually acts, and records the broadcast's id and sending time beside the mark. It skips the broadcast if its own mark is already later.
- **Several unread marks.** If several marks are waiting, it acts on the newest only and acknowledges each.

Meanwhile the tray lists the thread as silent, and an Orca chat as a chat with its wake queued. Both are shown today.

### Files to change

- `src/broadcast.ts` (pure):
  - Add `'mark'` to `BroadcastKind` and `KINDS`.
  - Add optional `only` and `noArt` to `Broadcast`, `composeBroadcast` and `parseBroadcast`. Refuse a value that is not true or false.
  - Add `markText(person, id, options)` beside `pingText`, reusing `ackCommand`.
  - Add an `answerable(kind)` helper, true for `ping` and `mark`, so that `recordAnswer` and `silent` cover both.
- `src/wake.ts` (pure): add `'mark'` to `WakeReason` and `REASONS`, so that `wakeLine` and `addRing` carry it.
- `src/agora.ts`:
  - Add `mark(options)` beside `ping()`.
  - `deliverHere` wakes with `mark` for a mark.
  - `answerRound` reads acknowledgements for every answerable kind, not only `ping`.
- `src/main.ts`:
  - Add the **Mark all** submenu in `broadcastItems`.
  - `sentItem` shows answers and silent threads for every answerable kind.
- `src/view.ts` has no change beyond the types it already imports.
- `docs/api/view-v1.md`: `answers` now applies to a ping or a mark, and `queued` may hold `mark`.
- `README.md`: a new **Mark** section after **Ping**, and `mark` added to the list of kinds under **Broadcast**.

The new logic sits only in `broadcast.ts` and `wake.ts`, which `.dependency-cruiser.ts` already treats as pure core. Files and the network stay in `files.ts` and `agora.ts`, so `src/boundaries.test.ts` needs no change.

### Tests to add

- `src/broadcast.test.ts`:
  - Building and reading a mark with each flag.
  - Refusing a flag that is not true or false, and refusing an unknown kind.
  - The words of `markText` with and without `only` and `noArt`.
  - `recordAnswer` and `silent` for a mark.
- `src/wake.test.ts`: `wakeLine` puts `mark` in its fixed order.
- `src/agora.test.ts`:
  - A mark is delivered here with its flags, rings the doorbell and queues a `mark` wake.
  - An absent peer has it queued, and gets it once present.
  - An acknowledgement to a mark from this rig is recorded, and one to a peer's mark is passed on to that peer.
- `src/view.test.ts`: a sent mark shows its answers.

### Candidate record

`KI-AGORA-TRY-002-mark-broadcast`, sitting in the tray area beside `KI-AGORA-TRY-001-menu-bar-identity`. This run did not create it.

### Change for ki.sop.main (text only)

Under **Recap since the mark**, in **Striking**, add after "by saying "mark"":

> or through a `mark` broadcast from Agora, which is the owner's own instruction to strike, with `only` and `noArt` read as "mark only" and "no art"; a thread reads it at its next turn when it was not listening, strikes when it acts, records the broadcast's id beside the mark, skips it when its own mark is later, and acknowledges it as a ping; a thread on hold acknowledges without striking.

## In Progress

Nothing is running. The record, the code and the standard line all wait on Kris's answers below.

## Queries

### MARK-SEND - How Kris sends a mark

**Context**

Agora has no command line today. Its only local endpoint is read-only and refuses anything but reading. A command-line send would need a new local way to write, which is a security surface of its own.

**Query**

Should the first slice offer a tray item only, or a command-line route as well?

**Options**

a) (recommended, confidence high - the tray is one click everywhere Agora runs and adds no new way in) Tray only, under **Mark all**; a command line waits for a later slice.

b) Tray and command line now, with a loopback-only local endpoint that accepts writes.

### MARK-WORDS - Whether a mark carries Kris's own words

**Context**

The `away` and `ping` broadcasts use fixed wording, while **Broadcast…** carries free text. Free text inside a mark could blur what the instruction is.

**Query**

Should a mark carry Kris's own words, beside `only` and `noArt`?

**Options**

a) (recommended, confidence medium - fixed words keep the instruction plain, and Kris can send words with **Broadcast…** next) Fixed words and the two flags only.

b) An optional note typed in a small window, added after the fixed words.

### MARK-ACK - Seeing which threads marked

**Context**

A ping already shows who answered and who is silent, through small acknowledgement files that Agora reads every five seconds.

**Query**

Should a mark use the same acknowledgement, so the tray shows `mark: 5 marked, 2 silent`?

**Options**

a) (recommended, confidence high - Kris wants every thread to act, and the silent list is how a missed one shows) Yes, reusing the ping's path in this slice.

b) No acknowledgement; Kris reads each thread's reply.

### MARK-ROLLOUT - Older Agoras on other rigs

**Context**

A rig still running the current Agora refuses a broadcast of an unknown kind. Agora sends queued broadcasts in order and stops at the first one refused, so one mark would hold back every later broadcast to that rig until it is upgraded.

**Query**

How should the new kind reach the rigs?

**Options**

a) (recommended, confidence high - Rig installs Agora on each host anyway, and it keeps the protocol plain) Install the new Agora on every rig before the first mark is sent.

b) Send a mark to older rigs as a plain message with the same words, so they deliver it as text.

### MARK-LATE - A thread that reads the mark late

**Context**

A thread that is not listening, or an Orca chat Agora cannot wake, sees the mark only at its next turn, which may be hours later. By then Kris may have marked it directly.

**Query**

When a thread acts on a late mark, what time is its mark?

**Options**

a) (recommended, confidence medium - a mark bounds what the next Summary covers, so it should be the moment the thread actually took stock) The time it acts; it records the broadcast's id and time beside the mark, skips the broadcast if its own mark is later, and acts on the newest only.

b) The broadcast's sending time, so every thread's mark lines up.

### MARK-HOLD - A thread on hold

**Context**

A hold strikes its own mark and has its own hold report. A mark broadcast reaches every watched package, held ones included.

**Query**

What does a thread on hold do with a mark?

**Options**

a) (recommended, confidence medium - a hold is the owner's choice to pause, and a broadcast should not reopen it) Acknowledge it without striking, and say "on hold" in one line.

b) Strike and give its hold report.

🧵 ki.prj.agora
