# [Model](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › granola-screenshots

**🤖 → 👤 Handoff to supervisor · Run report at 17:28 GMT · last mark 01:41 GMT · blocked**

---

## Done

- Found the fault. The screenshot check in `src/core/acquire/granola/projection.ts` threw an error on any difference between a meeting's listed screenshot count and the attachments named in its detail: a repeated attachment, an invalid identity, an attachment that is not a screenshot, or a different count. One such meeting therefore aborted the whole day.
- Fixed it (tools-ki `eca35dbe`, on `main`):
  - The importer now matches attachments to the count. It sets aside an attachment typed as something other than a screenshot and counts a repeated identity once, then requests only the screenshots that remain.
  - A meeting that still doesn't match is withheld, not captured. The run reports it on a `Withheld:` line with both counts and every repeated, invalid or non-screenshot attachment, then carries on with the rest of the day.
  - Marking still refuses a meeting that doesn't match.
- ACQUIRE-HELD-2: the importer did not write to `_held/granola/`. It wrote to `captured/_review/granola/`. Fixed in the same commit: a meeting that no single territory owns now goes to the repository's top-level `_held/granola/`, and later runs find packages there. Updated the user guide and changelog to match.
- Tests: one test is shaped like the failing meeting (25 screenshots plus one repeated and one non-screenshot attachment, alongside a mismatched meeting and a plain one on the same day). Another covers each kind of difference. The earlier abort tests now check for withholding. The two `_review` tests now check `_held/granola/`.
- Full suite: 2,181 of 2,181 tests pass. Type check: pass. Formatting and the commit gate: pass. Coverage gate: fails at 99.97% against the required 100%. The shortfall is entirely in two files this change doesn't touch, `src/core/agent/thread.ts` and `src/core/work/identity.ts`, both changed in earlier commits.
- Nothing released or installed.

## In Progress

- The dry run against the assistant repository could not run on sol, for 28 or 30 October. Before the importer starts, the Granola connection fails with `Granola MCP schema inspection failed … MCP operation failed (CLIENT_HTTP_NOT_IMPLEMENTED)`. The installed `ki` and a direct `mcporter call granola.get_account_info` fail the same way, so the cause is the Granola connection on this machine, not the fix. No capture was written.
- So the real cause for meeting 4ffa813b-68a8-4bf0-b798-4793546c4d3a is still unconfirmed. If it is one of the differences above, the meeting will now import. Otherwise it will be withheld with a line naming exactly which attachments differ, and the rest of the day will still import.

## Queries

### GRANOLA-DRYRUN-HOST - Where to run the confirming dry run

**Context**

The Granola connection fails on sol with `CLIENT_HTTP_NOT_IMPLEMENTED`, so I couldn't run the confirming dry run here. Granola probably needs signing in again on sol, or the connection works only on terra, where the fault was first seen. I made no change to the connection or its sign-in, because the run's rules don't allow it.

**Query**

How should the dry run for 28 and 30 October be run to confirm the fix?

**Options**

a) (recommended, confidence high - the fix is on `main`, and terra already has a working Granola connection) Ask assistant-terra to run the same dry run on terra from a checkout of tools-ki `main`, and report the `Withheld:` lines, if any.

b) Kris restores the Granola connection on sol (for example by signing in to Granola through mcporter again), then a short follow-up run repeats the dry run here.

c) Wait for the next tools-ki release and install, then run the dry run with the installed `ki`.

### COVERAGE-GATE - Coverage below 100% in untouched agent files

**Context**

The full suite passes, but coverage is 99.97% against the required 100%. The missing lines are in `src/core/agent/thread.ts` (lines 139, 470 and 516, from the recent report-homing commits) and `src/core/work/identity.ts` (line 20, from 28 October). This change touches neither file.

**Query**

Who should bring coverage back to 100%?

**Options**

a) (recommended, confidence medium - the gaps sit in the agent report-homing work, which owns those files) Send it to the run that owns the launcher-reports work as a follow-up.

b) Leave it for the next tools-ki release-readiness check to catch.
