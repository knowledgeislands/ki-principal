# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › ki-fixes

**🤖 → 🧑 Handoff to supervisor · Run report at 08:16 BST · last mark 08:16 BST**

---

## Done

I fixed both minor findings from the `ki-review` report, each one inside its own record. Both records stay at Awaiting review. roadmap-next had fixed neither. There was no release.

- STORE-FIX, under [KI-TOOL-KI-CLI-131](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-131-host-absent-store-state.md): for a bound store, the suggested fix now unbinds the role before marking it absent (`store unbind <role> --write then store absent <role> --write`). Every place that shows the fix passes in whether the role is bound. A test now runs the suggested commands and checks that they work. Commit `427342ac`.
- HOME-HELD, under [KI-TOOL-KI-CLI-147](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-147-agent-state-folder-tooling.md): if `events.state.json` is lost, the thread folder no longer gets back a report it retired. Commit `6afdd477`. The new test fails when the check is switched off.
- Each record has a `### Correction, 18 October 2026` note, and the guides and changelog are updated.
- Gate: `bun run test:coverage` passed all 1327 tests in 78 files at 100%; tsc, biome, knip, `mandoc -T lint` and rumdl were clean; `ki repo audit --repo .` gave FAIL=0, with the existing warnings CI-1 and HOOK-1.
- Pushed fast-forward to tools-ki `origin/main`. Only my own two commits went up.

## In Progress

Nothing.

## Queries

### HOME-MATCH - The retired-report check compares contents, not just the path

**Context:** The review suggested giving `homeReport` the same path-only `held` check that `adoptStateFiles` uses. But a path-only check would also block the new report of an agent restarted with `--relaunch` ([KI-TOOL-KI-CLI-135](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-135-reused-agent-name-overwrites.md)) once the thread had retired its earlier report. So the new `heldAs` skips a report only when Git holds that path with the same contents.

**Query:** Should KI-TOOL-KI-CLI-147 keep the contents-based check when it is accepted?

**Options:** a) (recommended, confidence high - it closes the lost-snapshot case and still delivers a relaunched agent's report) keep it as delivered. b) Switch to the path-only `held` check and accept that a relaunched agent's report is not delivered after a retirement. c) Also move `adoptStateFiles` onto the contents-based check, in a new record.
