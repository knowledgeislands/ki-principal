# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › accept-by-criteria

**🤖 → 👤 Handoff to supervisor · Run report at 01:53 GMT · last mark 01:29 GMT**

---

## Done

- I tested all 25 open queries in [queries](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/queries.md) against the four ACCEPT-BY-CRITERIA tests, strictly, failing any query where there was doubt. Commit `afdb29b4` is pushed; the commit hook's scoped audit passed.
- **Nine passed and are taken as a)**, each with one line in [decisions](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/decisions.md#owner-answers-during-away-31-oct-0136-gmt-31-october-2026) and a pointer under Answered: WORKER-WAIT-MIDTURN, AMEND-RACE, LAYOUT-PILOT-ORDER, REVIEW-CHALLENGE, REVIEW-LIFT, READ-FEEDBACK-NOW, ORCA-CLOSE-OUT, ORCA-SUBAGENT-PILOT and ORCA-PLACEMENT.
- **Fourteen failed and stay open.** Each has one plain-English line in its Context naming the test it failed:
  - A reviewer preferred another option (test 2): WORKER-WAIT-MEANING, WORKER-WAIT-QUEUED, HOST-CADENCE, HOST-COVERAGE, HOST-SECONDARY-PUBLISH and HOST-READBACK.
  - The confidence is not a clean high (test 1): WORKER-WAIT-GATED, which still has three open checks, and WORKER-WAIT-DELIVERY, which rests on parts still open.
  - Contentious or only Kris can decide (test 3): PUBLIC-REPORT-AUDIENCE and LAYOUT-SHAPE, which departs from Kris's own sketch.
  - Not easily undone (test 4): ORCH-NAME-DISPATCH, a skill rename; LAYOUT-GROUP-TIDY, a wider deletion rule; and PUBLIC-REPORT-RECOVERY, which also fails test 3.
  - Fails tests 1 and 2: WAKE-HOST, which Kris kept for the morning.
- ORCH-NAME-THREAD b) and ORCA-QUEUE a), which Kris answered directly, are moved to Answered as pointers.
- [accepted.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/window-31-oct/accepted.md) lists the nine accepted queries in execution order, one at a time after the 01:49 window queue:
  - three small message and design units in ki-principal;
  - five harness units behind U1 and U9;
  - LAYOUT-PILOT-ORDER, parked until LAYOUT-SHAPE is answered.
- None of the accepted options has been acted on.

## In Progress

Nothing is running.

Outstanding - no action requested now: two of the fourteen failures, WORKER-WAIT-QUEUED and WORKER-WAIT-MEANING, failed only because the earlier WORKER-WAIT blind review's full verdict is not in the package. If Kris looks at them, they may be quick to settle.

## Queries

### HARNESS-RECEIVER - Which package receives the AMEND-RACE line

**Context:** AMEND-RACE a) says to send the amend guard "to the KI Agentic Harness as a message line for `ki-git`". No work package in `+/_WORK/` is named for the harness. ki.prj.baseline-rollout already carries other harness-owner proposals, but it is held, although queued message lines into held packages are allowed. This run did not guess.

**Query:** Where should the AMEND-RACE line go?

**Options:**

a) (recommended, confidence medium - it is where harness-owner proposals already wait, and a queued line respects its hold) Send it as one line to ki.prj.baseline-rollout's `messages.md`.

b) Send it to ki.sop.main's `messages.md` for State of play to route.

### CLOSE-OUT-ROUTE - How ORCA-CLOSE-OUT reaches `ki-coordination`

**Context:** ORCA-CLOSE-OUT a) says to send the worker close-out rule "to the harness now as a message". This work's own scope includes `ki-coordination`, and U1 already edits that standard directly through this work's harness lane, with a review run before the push. The accepted option's words point to a message; the scope points to doing it here.

**Query:** Should this work write the close-out rule into `ki-coordination` itself, or send it as a message line?

**Options:**

a) (recommended, confidence medium - this work owns `ki-coordination`, so sending it a message would only route the change back to itself, as happened with OP-CACHE on 30 October) Deliver it in this work's harness lane as unit 8 of accepted.md, after the read-only check of Orca's close-out steps.

b) Send it as a message line, keeping to the option's literal words.

### 🤖 → 👤 Handoff to supervisor · since 01:53 GMT

👤 2 with you

- [with you] HARNESS-RECEIVER · coordinator · since 01:53
- [with you] CLOSE-OUT-ROUTE · coordinator · since 01:53

🧵 ki.prj.ways-of-working
