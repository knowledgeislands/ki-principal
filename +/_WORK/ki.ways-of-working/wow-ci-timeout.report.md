# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-ci-timeout

**🤖 → 👤 Handoff to supervisor · Run report at 22:24 BST · last mark not supplied in the brief**

---

## Done

- Change: harness CI's `build` job now has `timeout-minutes: 30` and its Test step `timeout-minutes: 10`, in `.github/workflows/ci.yml`, commit 81b8c8c7 `fix(ci): bound the build job and its Test step with time limits`. Local `main` was fast-forwarded from 17166cf2 to 81b8c8c7, and the worktree and its branch are retired. Nothing was pushed: local `main` is 2 commits ahead of `origin/main`, the other being 17166cf2 from another session.
- Why these limits: I could not read the durations of recent green CI runs, because the brief forbids GitHub API calls and no earlier report recorded them. So I sized the limits from local timing instead. The full suite passed in 22-25 s in five local runs. A 10-minute Test limit is over 20 times that, which leaves room for a slower CI runner without letting a hang last. The 30-minute job limit also covers the install, KI bootstrap and audit steps, which make network calls. Either limit stops a hang at well under a tenth of the six hours it took before.
- Suspected cause: not found, and no hang reproduced in five local runs. The leading suspects are the 19 synchronous child-process calls in the tests that have no `timeout`. They start `bun` (`recap-grounding`, `remove-legacy-ki`, `content-only`, `build-html --check`, `export-svg`), `bash` (the plan and lock hooks) and `git commit` through the copied hooks (`git-hook-stub`, `pre-commit`). A blocked synchronous child also blocks Bun's event loop, so Bun's 5-second per-test timeout can never fire. That fits both the indefinite hang and the orphan `bun` processes. The two hung commits (185624b0, ba4055ef) changed nothing relevant, so the hang looks intermittent and environment-driven rather than caused by a commit. The Chrome-based diagram tests launch no real browser, so they are ruled out. I did not attempt a fix because the cause is not clear.
- Checks: `bun run test` passed 1374 of 1374, five times. `bunx tsc --noEmit` passed. The pre-commit hook's focused `ki-repo-harness` audit passed. The full `ki repo audit`, run in an isolated home, failed one check unrelated to this change: `ki-engineering` DEPS-1, knip 6.39.0 → 6.40.0, which passed the 14-day adoption window today. That failure is time-driven and fails the same on 17166cf2.
- Routed: two lines added to the [ki.ways-of-working messages](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/messages.md), HARNESS-DEPS-1 (adopt knip 6.40.0 or record a hold) and CI-HANG-CAUSE (read the next timed-out log for the last test file that started). The file is left uncommitted for the coordinator to take in.

## In Progress

Nothing is running.

Outstanding - no action requested now: the harness CI Audit step will turn red on the next push until knip is updated or held (routed as HARNESS-DEPS-1). The hang's cause stays open until a timed-out run's log names the file (routed as CI-HANG-CAUSE).

## Queries

No outstanding queries
