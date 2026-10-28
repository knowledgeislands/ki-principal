# [Model](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md>) › [Ways of working](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md>) › wow-tap-consumer

**🤖 → 👤 Handoff to supervisor · Run report at 08:33 GMT**

---

## Done

- Confirmed with read-only `gh` calls that the tap's notify credential reaches the harness: the `ki-tools-release-bot` App installation is on selected repositories with Contents write, the harness holds `KI_TOOLS_RELEASE_BOT_APP_ID` and `KI_TOOLS_RELEASE_BOT_PRIVATE_KEY`, and the harness's own daily `update-ki-pin` runs (latest 24 October) mint an App token scoped to `ki-agentic-harness` successfully, which proves the installation covers it.
- Confirmed the harness receiver's filter matches the tap payload: `update-ki-pin.yml` runs on `tool-release-published` when `client_payload.source_repository == 'knowledgeislands/tools-ki'`, and the tap's extractor sends exactly `source_repository: knowledgeislands/tools-ki` for `Formula/ki.rb`, plus `tool`, `version`, `formula_path` and `tap_commit`.
- Added `knowledgeislands/ki-agentic-harness` to `.github/tool-release-consumers.json` in a clean temporary clone of `origin/main`; the registry stays unique and sorted as the extractor requires. Commit `ef2ad37` `chore(release): enrol ki-agentic-harness as a tool release consumer`, trailer `Co-Authored-By: Claude Fable 5.1`, the model that made the commit per the commit-trailer rule, rather than the Opus 5.5 trailer the brief named.
- Checks before commit: release-event tests pass (13 runs, 53 assertions), proposal tests pass (7 runs, 21 assertions), both scripts syntax-check clean, the staged `ki-repo-homebrew-tap` audit passes in the pre-commit hook, and the commit-message gate passes. The full `ki repo audit` on the temporary clone reports only location findings (RUNTIMES-2 and REPO-REG-1, the unregistered temp path); the same tree audits clean in the primary checkout apart from the three pre-existing warnings already on `main`.
- Pushed fast-forward to `origin/main`, no other sessions' commits stacked. CI run <https://github.com/knowledgeislands/homebrew-tap/actions/runs/40176937846> green: Detect formula changes, KI governance and Notify release consumers succeeded; Homebrew formula gates skipped, as no formula changed. The notify job correctly sent nothing, because no formula changed in this push.
- Primary checkout at `/Users/krisbrown/workspaces/knowledge-islands/homebrew-tap` fast-forwarded to `ef2ad37`; the temporary clone was removed, leaving the run's temp directory empty.

## In Progress

Nothing.

## Queries

### REPLAY-SMOKE - run the onboarding replay smoke test

**Context** Step 6 of the tap's onboarding guide replays an already-current release so both the tap dispatch and the receiver's bounded outcome can be confirmed. That means a manual `workflow_dispatch` of the tap's CI with `formula=ki`, a remote write this run was not authorised to make. Until it runs, the harness's first real dispatch arrives with the next tools-ki release, and the daily poll remains the backstop.

**Query** Should the replay smoke test run now, and who runs it?

**Options**
a) Run it now from your machine (recommended, confidence high - one command, no code change, and the expected result is a green tap run with a "Dispatched ki v0.13.0 to knowledgeislands/ki-agentic-harness" summary line, then a harness `update-ki-pin` run that exits "pin v0.13.0 is current; nothing to propose"):
   `gh workflow run CI --repo knowledgeislands/homebrew-tap -f formula=ki`
b) Delegate a short follow-up run with explicit authority for that one `workflow_dispatch` and a read of both runs.
c) Skip the replay and let the next tools-ki release be the first live test, relying on the daily poll if the dispatch misses.
