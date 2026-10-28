# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-coord-standard

**🤖 → 👤 Handoff to supervisor · Run report at 01:42 BST · last mark 02:10 BST 23 October**

---

## Done

- REBOOT-SHAPE a) is in place. The re-bootstrap report is now a full owner report: `## Done` gives the role and where the work stands, `## In Progress` what is running, `## Queries` every open query in full, then the banner. The "three lines" wording is gone from Bootstrap step 7, Report forms and the three openers. Hook rule 4 now names the full summary and the re-bootstrap report, and says both restate every open query in full. The skill's notes say the same.
- GAP-SUMMARY a) is in place. The first reply after 30 minutes or more without an owner message, while queries are with the owner, answers the message and then gives the Summary with every open query in full. It is a new Gap Summary rule under Coordinator responsiveness, and the Summary row, the Self-contained exception, the skill's Summary mode and the output style all carry the same trigger.
- The hook line and the `ki-coordinator` output style were regenerated with `ki dev skill generate ki-coordination --write`. The two tests that pin the hook's wording were updated to match, and the source review in `references/sources.md` has a new 2026-10-25 entry.
- Committed as `8cc42754` in ki-agentic-harness, by explicit path, and pushed to `main` fast-forward. Only my own commit was stacked.
- Checks: the banner test passes; `bun run test` passes (1446 tests); `bunx tsc --noEmit` is clean; the `ki-coordination` audit passes; the pre-commit audit passes. The `ki-skills` audit has three LONG-3 warnings about ki-skills' own overdue source reviews. Those are fleet findings that were already there, not caused by this change.
- One small departure from the repository's convention: I edited in the primary checkout, which was clean, rather than in a linked worktree.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- tools-ki needs a follow-on change, which this run was not allowed to make. In `src/core/work/prompts.ts`, line 26, `FIRST_STEP` still reads `First step: follow the Bootstrap in ki-coordination, then report in three lines.` It needs to read `First step: follow the Bootstrap in ki-coordination, then give the full re-bootstrap report.` so that `ki agent prompts` prints the same openers as the standard.

## Queries

### COMMIT-CADENCE - commit and push the work folder at every package write and wake, and push work-folder-only commits stacked beneath

**Context:** You said on 25 October that work sits uncommitted in the work folder for a long time, which makes it hard to keep repositories in sync with the remote and with the other sessions that write into work packages. There are two gaps in the standard today. First, Committing the work folder only requires a commit and push at a send, an owner receive, a mark, a hold and finish. Writes in between are not covered: message dispositions, queries, decisions, briefs and state changes, and nothing is committed at a heartbeat wake. Second, Pushing beneath other sessions forbids pushing any other session's commits that sit under your own. In a Capital, those are usually other sessions' `messages.md` lines or their own work-folder commits, so the coordinator's push stalls until you push by hand. Your 14 October words allow a session to push stacked commits it is confident in, and to flag only the ones it is not: "if there's a need or it has little confidence in the other commits that are stacked up with it, that's flagged to me". The smallest change fixes both gaps. In Committing the work folder, replace the sentence beginning "So a coordinator commits and pushes its work folder at every send" with: "So a coordinator commits its work folder by explicit path at every write to it, a decision, a query, a message disposition, a brief or a state change, and at every send, receive, mark, hold and wake and before the work finishes, never with another session's uncommitted changes, each commit's subject carrying the move; each time it pulls with rebase first and then pushes fast-forward, so that no write stays uncommitted past the turn that made it; a line it writes into other work's `messages.md` is committed and pushed at once." In Pushing beneath other sessions, add a bullet after Push: "**Work-folder traffic:** another session's commit stacked beneath its own that touches only paths under `+/_WORK/`, such as a `messages.md` line it routed or its own package, is coordination traffic, not stacked work: the coordinator pushes it with its own, fast-forward only, never force. A stacked commit that touches anything else is left to the owner as above." The output style's commit sentence and hook rule 5 would then say "at every package write and wake" in place of "at every send". This has not had the blind query review the standard requires for a medium-confidence query; the coordinator should run one before this reaches you.
**Query:** Should the standard adopt this commit cadence, and allow work-folder-only commits stacked beneath to be pushed?
**Options:**
a) (recommended, confidence medium - it fixes both causes you described, but it widens push authority over other sessions' commits, which you limited on 14 and 19 October) adopt both changes as worded above, and regenerate the hook line and output style
b) adopt only the commit cadence, and keep the rule that every stacked commit from another session is left for you to push
c) leave the standard as it is

### 🤖 → 👤 Handoff to supervisor · since 01:42 BST

👤 1 with you

- [with you] COMMIT-CADENCE · owner · since 01:42
- [committed] ki-agentic-harness

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
