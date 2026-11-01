# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › listen-and-awake

**🤖 → 👤 Handoff to supervisor · Run report at 13:16 GMT · last mark 13:05 GMT**

---

## Done

- I waited for `drain-target` to push first, then worked in my own worktrees.
- **FEEDBACK-AS-MESSAGE** (harness `d3d6d507`, `ki-work-package`):
  - Owner feedback on a document now arrives as a line in the work's `messages.md`. The owner can add it by hand, or the work's own steward can write it word for word from Kris's words, naming Kris as the speaker and saying where the words came from.
  - The hand-written and steward-written feedback files that `16f550f7` allowed are withdrawn.
  - The Observatory's `feedback-send` still writes `feedback/` files, so those stay readable for the tolerance window. No other route writes one.
  - Updated: the entry-points table, the closed list, the skill summary and the source review.
- **LISTEN-STATUS** (harness `ee38d1a6`, `ki-coordination`):
  - The rule: an open coordinating thread keeps one inbox watcher armed, whoever holds the work. The watcher is the cheap shell loop from the inbox-wake design. It looks about every two minutes and wakes the thread when `messages.md` changes. Otherwise it wakes after 5 minutes while runs are going, or 15 minutes when they are not.
  - The watcher stops while draining, On hold, at Finished and on "stop the wake". While runs are going, the watcher and the heartbeat check are the same loop.
  - Every banner now has one short line just before its thread line, such as `👂 listening · not the sync thread for terra`. The other states read `🔇 draining, so not listening` and `🔇 not listening`.
  - A thread counts as "sync thread for <host>" only where an owner decision or an agreed host map names it. Otherwise the line says "not the sync thread".
  - A run report's banner has no listening line.
  - The rule that a runtime with no proven way to wake the thread counts as not listening follows WAKE-SESSION. The cadence figures are the ones INBOX-WATCH gave, and the standard says the inbox-wake questions are still open. None of them is settled.
- **UNATTENDED-AWAKE** (same commit):
  - An unattended window is described as a mode on top of normal coordination.
  - A new **Awake** step keeps the leading session alive and its machine awake for the window, with `caffeinate -dims -w <session pid>` on macOS and the platform's equivalent elsewhere. The keep-awake is released when the window ends.
  - The entry report says how this is done.
- Also changed:
  - Updated in the same commit: the hard-rule text, the hold steps (the watcher is cancelled), the inbox check, the rubric item COORD-4 and the skill summary. The output style was regenerated.
  - The [Work Process note](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Processes/Work Process/Work Process.md>) got two sentences (ki-principal `656262d4`, merged with the new `main`). Without them, its "thread line follows the list" wording would contradict the standard. `drain-target` did the same for its change.
- Checks:
  - Banner test: passed, 20 tests, 2 of them new.
  - Full harness tests: passed, 1,498.
  - Type check: passed.
  - Isolated-home `ki repo audit`: no failures.
  - Generated surfaces and both rubric catalogues: in sync in the worktree and in the primary checkout.
  - Commit hooks: passed in both repositories.
- My worktrees and temporary files are removed.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- The inbox-wake queries are still open and untouched: INBOX-ARMED, INBOX-CADENCE, INBOX-VERB, CODEX-WAKE, SENDER-NUDGE and WAKE-HOST. If Kris answers them differently, the watcher's figures and per-runtime wording in the standard need a follow-up.

## Queries

### OBS-FEEDBACK-LINE - Should the Observatory also send feedback as a message line?

**Context:** Under FEEDBACK-AS-MESSAGE on 31 October 2026, Kris said "we can probably drop the feedback idea. We just send a message with it instead." I replaced the hand-written and steward-written feedback files. The Observatory's own feedback-sending feature still writes a separate feedback file plus a message line linking it. It is shipped under its own decision, PDR-KI-OBSERVA-007, and owned by the Observatory work, so I left it alone and kept those files readable for now. Until the Observatory changes, the method has two routes for owner feedback.

**Query:** Should this work send the Observatory work a message asking it to send feedback as a message line only, so that the separate feedback file can be retired?

**Options:**

a) (recommended, confidence medium - it matches Kris's words and removes the second route, but the Observatory may need the separate file for comments anchored to passages, which I have not checked) Send one line to the Observatory work's `messages.md`, asking it to move `feedback-send` to message lines and then retire the `feedback/` kind.

b) Keep the Observatory's feedback file as the one exception, and retire nothing.

### 🤖 → 👤 Handoff to supervisor · since 13:16 GMT

👤 1 with you

- [with you] OBS-FEEDBACK-LINE · owner · since 13:16

🧵 ki.prj.ways-of-working
