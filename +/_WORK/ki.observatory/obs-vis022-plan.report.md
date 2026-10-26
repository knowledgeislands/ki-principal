# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-vis022-plan

**🤖 → 👤 Handoff to supervisor · Run report at 01:44 BST**

---

## Done

- [KI-OBSERVA-VIS-022 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/c1f008346dc085a0c25026ea5c9a08b383ef1d5b/docs/roadmap/KI-OBSERVA-VIS-022-judge-overdue-against-each-job-schedule.md) planned and set Ready in commit 3b3c785 (local, not pushed): Current state checked against the code at 0d58592, Planning decisions, Steps, Files touched, Verify, size m kept.
- The sweep's premise was wrong: Rig 0.7.0's `rig show --format json` does carry each scheduled job's `schedule` (for example `calendar:hour=8,minute=0`) under the specified RIG-STATE-033 contract, and its job ids match the reporter's job names exactly. So the schedule comes from Rig's stable machine contract and the launchd property lists are not read at all. That meets AGENTS.md's consume-stable-contracts rule, which is why the record went to Ready rather than staying in planning.
- The other two choices are settled in the record: a 2-hour grace after the most recent scheduled run, which keeps daily jobs as they are now (24 + 2 = 26 hours); and an unparseable schedule falls back to the 26-hour rule with its reason shown, because Rig already checks the calendar grammar. A job Rig declares disabled is not judged overdue.
- Roadmap audit: FAIL=0 (three existing size warnings, all on other records). Markdown lint: clean. No code changed and the service was not restarted.

## In Progress

Nothing. A side finding, not acted on: the Bridge's `RIG_UNAVAILABLE` text in `packages/evidence/src/machine.ts` still says Rig has no JSON output, which stopped being true with Rig 0.7.0. It may be worth capturing as a separate record.

## Queries

**Context:** The `schedule` value in `rig show --format json` is covered by RIG-STATE-033's promise of complete declaration values, and its calendar records follow the grammar in Rig's `configuration.md`. Its own format, the `calendar:` and `interval:` prefixes with records joined by `;`, is observed in Rig's code but not written down in Rig's specification.

**Query:** Should tools-rig be asked to specify that format before or alongside the build?

**Options:**

a) (recommended, confidence medium-high - the build is not blocked and an unknown format already falls back safely) Build [KI-OBSERVA-VIS-022 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/c1f008346dc085a0c25026ea5c9a08b383ef1d5b/docs/roadmap/KI-OBSERVA-VIS-022-judge-overdue-against-each-job-schedule.md) as planned and send tools-rig a handoff to specify the `schedule` format, or to add a structured field next to it.

b) Hold the build until tools-rig adds a structured, specified schedule field.

c) Read the rendered launchd property lists instead. This is not recommended: it duplicates Rig's rendering and works only on macOS.
