# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › b-U5

**🤖 → 👤 Handoff to supervisor · Run report at 14:23 GMT · last mark 14:23 GMT**

---

## Done

- Window unit U5 (MGIT-PUSH-GUARD) has landed in tools-mgit at `f67e255` on `main`. By default `mgit sync` now only fetches and fast-forwards. A branch that is only ahead of its upstream is reported as "ahead N, not pushed (pass --push)" and counted as skipped. `mgit sync --push` publishes, and `-i` offers a push only when `--push` is also given. `git config mgit.syncPush false` is a hard veto that neither `--push` nor `-i` overrides, and a value Git cannot read as true or false vetoes too. The usage text, both shell completions, the man page, README, user guide, spec MGIT-WS-018 and a changelog line announcing the new default are all updated. No tag, no release.
- tools-mgit's roadmap needs a record for this kind of change, so it is captured as [KI-TOOL-MGIT-CLI-033](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-033-sync-push-guard.md), in commits `c431492` (number reserved) and `f39ccd5` (record planned). It now awaits review; acceptance stays with Kris.
- Checks: the full test suite passed (153 of 153), including two new sync tests and five adjusted ones covering default no-push, explicit push, veto precedence, interactive mode and linked worktrees. Shellcheck, the syntax check, the man-page lint, the whitespace check and the Markdown lint all passed. The repository audit's only failure is the existing commit-hook finding, which this work did not touch.
- Receipt line added to [ki.prj.tools-burndown messages](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.tools-burndown/messages.md) in ki-principal `5f3f246e`. The original MGIT-PUSH-GUARD queue line is left for that work's coordinator to dispose, because this unit's brief did not ask for it.
- The worktree and branch are removed, and the temporary folder is empty.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- ki.prj.tools-burndown's SYNC-RECIPE line plans to rebuild `mgit sync` on `mgit chain`. That rebuild must keep this push rule, and the receipt line says so.
- A global `mgit.syncPush false` would also block every repository, because Git reads the setting through normal config lookup. The decision covers only the per-repository case, so this is recorded as a side effect in the record's review notes.

## Queries

### SYNC-UNPUSHED-EXIT - Should leaving a branch unpushed make sync report failure?

**Context:** By default sync now leaves branches that are only ahead unpushed. I counted these as "skipped" but let the run finish successfully (exit status 0), the same way sync already treats a pull or push the user declines under `-i`. Other skips, such as local changes or divergence, still make sync exit with status 1. A script that relied on sync's exit status to spot unpublished commits would now have to read the summary at the end. The decision's words say nothing about exit status, so this was my call. It is recorded in [KI-TOOL-MGIT-CLI-033](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-033-sync-push-guard.md) for review.

**Query:** Should an unpushed branch leave sync's exit status successful, as delivered?

**Options:**

a) (recommended, confidence medium - not pushing is now the intended default, so failing every routine run on a repository with local commits would make the exit status meaningless) Keep it as delivered: unpushed branches are reported and counted as skipped but do not fail the run.

b) Make an unpushed branch fail the run (exit status 1), like the other skips, so scripts notice unpublished commits.
