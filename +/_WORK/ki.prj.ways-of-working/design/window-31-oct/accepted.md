# Queries accepted by criteria, in execution order

Written by run `accept-by-criteria` at 01:51 GMT on Saturday 31 October 2026, under Kris's ACCEPT-BY-CRITERIA answer in this package's [decisions](../../decisions.md#owner-answers-during-away-31-oct-0136-gmt-31-october-2026): an open query counts as answered with its recommended option only if it is high confidence, every reviewer agreed, it is not contentious and it is easily undone. Nine queries passed; nothing has been acted on. The fourteen that failed stay open in [queries](../../queries.md), each with the test it failed.

ORCH-NAME-THREAD b) and ORCA-QUEUE a) were answered by Kris directly and are not part of this list.

## How to run them

- One unit at a time, under WIP-LIMIT, after the window queue the coordinator set at 01:49 GMT (U1, U9, U3, U4, U22, U14, U7, U8, U12, U13).
- The three message and design units in ki-principal come first, because nothing blocks them.
- The harness units follow U1 and U9 in the same repository. Each one ends with a separate review run before its push, as the [window plan](plan.md) sets for harness work.
- A unit that waits on a held package or an open query is parked, not started.

## Units

| Order | Query | Owner work | Repository | What doing it means | Size | Waits on |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | AMEND-RACE | ki.prj.ways-of-working | ki-principal | Send one message line asking for the `ki-git` amend guard: amend in a shared checkout only inside the serialised write window, after confirming `HEAD` is the session's own unpushed commit; otherwise make a new commit. | S | The coordinator naming the receiving package; see the first point below. |
| 2 | ORCA-SUBAGENT-PILOT | ki.prj.ways-of-working | ki-principal | Send the drafted ORCA-SUBAGENT-PILOT line from the [Orca sub-agents design](../orca-subagents/design.md) to `ki.prj.orca-evaluation`'s `messages.md`. Nothing more. | S | Nothing for the line. The pilot itself starts an Orca worker, which this window excludes, and needs Kris watching. |
| 3 | ORCA-PLACEMENT | ki.prj.ways-of-working | ki-principal | Record in the [Orca sub-agents design](../orca-subagents/design.md) that Part B uses `worker-start --agent`, switching to the terminal route only if the pilot shows prompts or blocked writes. The pilot must also test the run's directories, non-interactive running and its authority limits, so that too much access fails as well. | S | Nothing for the design note. Part B itself, in tools-ki, waits on the pilot and on ki.prj.tools-burndown's hold. |
| 4 | WORKER-WAIT-MIDTURN | ki.prj.ways-of-working | ki-agentic-harness | Drop "or the coordinator is mid-turn" from `ki-coordination`'s States and moves, so that only an arc moves the work, and match the [state machine](../work-state-machine.md) note. | S | U1 and U9 in the same repository; a review run before the push. |
| 5 | REVIEW-LIFT | ki.prj.ways-of-working | ki-agentic-harness | In `ki-coordination`'s query-review rule, mark agreement resting only on precedent `reviewed, precedent only` with no lift, and cap a precedent-only reason at medium. | S | Unit 4; a review run before the push. |
| 6 | REVIEW-CHALLENGE | ki.prj.ways-of-working | ki-agentic-harness | Add the generated independence sentence to review briefs, state earlier decisions as dated facts in masked Contexts, show a challenge at the end of the Context with an option to revisit it, and add a Challenges section to `ki-work-design` reviews. With unit 5 this unblocks the REVIEW-INDEPENDENCE text the window plan excluded. | M | Unit 5; a review run before the push. |
| 7 | READ-FEEDBACK-NOW | ki.prj.ways-of-working | ki-agentic-harness | Widen the `feedback/` row of the `ki-work-package` closed list: the owner may write a feedback package by hand, or the steward verbatim from the owner's words, naming the owner as speaker and keeping any later reading of it apart. | S | Unit 6; a review run before the push. |
| 8 | ORCA-CLOSE-OUT | ki.prj.ways-of-working | ki-agentic-harness | First check, read only, Orca's five close-out steps and what release does. Then add the worker close-out rule for receive, mark, hold and Finished, with history deletion kept out. | M | Unit 7; the read-only check; the second point below. |
| 9 | LAYOUT-PILOT-ORDER | ki.prj.ways-of-working | ki-agentic-harness, then ki-principal | Change the package closed list and the FOLDER rubric for the chosen layout, then pilot this package by hand, with an inventory of what moved. The launcher and Observatory changes follow in their own works. | M | LAYOUT-SHAPE, still open with Kris. Parked until it is answered. |

## Points for the coordinator

1. **AMEND-RACE's receiving package.** The option says to send the guard "to the KI Agentic Harness as a message line for `ki-git`". No `+/_WORK/` package is named for the harness. ki.prj.baseline-rollout carries other harness-owner proposals, but it is held. Name the receiving package before sending; this run did not guess.
2. **ORCA-CLOSE-OUT's route.** The option says to send the rule to the harness "as a message". This work's scope already includes `ki-coordination`, so it may deliver the rule itself through its harness lane, as U1 does. The coordinator decides which route to take; this run did not choose.
