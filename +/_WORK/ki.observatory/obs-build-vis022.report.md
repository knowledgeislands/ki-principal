# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-build-vis022

**🤖 → 👤 Handoff to supervisor · Run report at 02:00 BST · last mark not stated in the brief**

---

## Done

- [KI-OBSERVA-VIS-022 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/c1f008346dc085a0c25026ea5c9a08b383ef1d5b/docs/roadmap/KI-OBSERVA-VIS-022-judge-overdue-against-each-job-schedule.md) is built as planned and is now Awaiting review, with its Review section. Automation now judges each job against its own Rig schedule from `rig show --format json`, matched by exact `id`. The reader of the `calendar:` and `interval:` forms is strict. A report is due 2 hours after the most recent scheduled run. A job Rig declares disabled is never judged overdue. Anything unmatched or unreadable keeps the 26-hour rule and shows why on its row, and the state line says once if Rig itself could not be read. Calendar times follow the host's wall clock across both clock changes.
- The record is corrected: Rig's declaration values are specified (RIG-STATE-033, RIG-CONF-016), but the encoding of the schedule string is only implementation evidence, which the strict reader and the visible fallback bound. The record notes that a specification handoff to tools-rig has been requested.
- The stale `RIG_UNAVAILABLE` text in `packages/evidence/src/machine.ts` no longer says Rig has no JSON output.
- Commits on local `main`, not pushed: `fd92124` (the Bridge Rig text), `e3e7dc9` (schedule-aware overdue), `b98d47c` (record to Awaiting review). Baseline is `3b3c785`. Another session committed `788f9ea` to `fcf6196` in the same checkout during this run. I left them alone and checked that my diffs held only my changes.
- Tests: pass. Typecheck: pass. Build: pass. Knip: pass. rumdl: pass. Biome: no finding in a touched line; the findings it does report are in lines I did not touch. Contract-shape snapshot: updated and passing. Browser smoke check: passed. Check against this machine: the four Rig jobs read on their schedules with no local path in the answer, and with `rig` off `PATH` every job falls back with its reason.
- Roadmap audit: FAIL=0 for this record. The whole tree reports FAIL=3. All three are Review or body-order failures in [KI-OBSERVA-BRG-005 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/0966ac3e/docs/roadmap/KI-OBSERVA-BRG-005-act-board-missing-parts.md) and [KI-OBSERVA-VIS-027 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/ab08287869ce6d5b187be7e5266e7194146f48b5/docs/roadmap/KI-OBSERVA-VIS-027-themes-in-streams-read.md), which the other session changed during this run.

## In Progress

- The local Observatory service has not been restarted, because a background run does not restart it. A restart is due for Kris so the live service serves this delivery.

## Queries

**Context:** The roadmap audit fails on [KI-OBSERVA-BRG-005 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/0966ac3e/docs/roadmap/KI-OBSERVA-BRG-005-act-board-missing-parts.md) and [KI-OBSERVA-VIS-027 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/ab08287869ce6d5b187be7e5266e7194146f48b5/docs/roadmap/KI-OBSERVA-VIS-027-themes-in-streams-read.md). The other session committed those records during this run with Review sections out of the required order. I did not touch them.

**Query:** Who should fix those two records?

**Options:** a) (recommended, confidence high - they are that session's own records, so its owner can fix them without guessing) route it to the session that delivered [KI-OBSERVA-BRG-005 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/0966ac3e/docs/roadmap/KI-OBSERVA-BRG-005-act-board-missing-parts.md) and [KI-OBSERVA-VIS-027 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/ab08287869ce6d5b187be7e5266e7194146f48b5/docs/roadmap/KI-OBSERVA-VIS-027-themes-in-streams-read.md); b) brief a small separate run to fix only their structure; c) leave them until acceptance review.

**Context:** Comments in `packages/contracts/src/bridge.ts` and `packages/contracts/src/beacon.ts`, and the Bridge test fixtures, still say Rig has no machine-readable projection. The brief named only `machine.ts`, and these change no behaviour.

**Query:** Should the remaining stale statements be captured as follow-up work?

**Options:** a) (recommended, confidence medium - one small corrective record keeps the claim consistent without widening this delivery) capture a triage record for the Bridge to read `rig show --format json` and correct these comments with it; b) correct the comments only, in a small separate run; c) leave them as they are.
