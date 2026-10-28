# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-rel-0141

**🤖 → 👤 Handoff to supervisor · Run report at 00:03 GMT · last mark 00:03 GMT · blocked**

---

## Done

- tools-ki, memory fix: `f68d643b` makes `src/tests/cli/agent-control.test.ts` archive, bundle and import the pre-terminal-identity baseline CLI once per file instead of once per test. ES modules never unload, so the per-test bundles were retained until the worker hit V8's 2 GB default on the 7 GB macOS runners; the file's peak fell from 2290 MB to 157 MB under a 1 GB ceiling, so the file was not split. `a3b8a7ad` gives the package job's test step `NODE_OPTIONS=--max-old-space-size=4096`; all three targets still run the full suite. The fix is confirmed: both darwin-x64 release attempts ran the whole suite (97 files, 2150 tests) with no out-of-memory crash.
- tools-ki, rename: `d8911ab1` renames `tooling/boundaries` to `tooling/depcruise` in `ci.yml`, `release.yml`, `package.json`, `src/core/agent/worktrees.ts`, the worktree contract test, the boundary tests, the hooks test fixtures and two developer guides. `825680cb` prepares v0.14.1 (package.json, CHANGELOG).
- tools-ki, verification: full suite with coverage passed in the worktree; typecheck, Biome and actionlint clean; `ki repo audit` in the primary checkout passed with warnings only (CI-1 inline pin, CLEAN-4, CLEAN-6, MATURITY-1, all pre-existing or expected) once another session's coverage run released the report lock.
- tools-ki, push: `main` reached `origin/main` at `825680cb` at 21:59 GMT by a push from this machine outside this run (its reflog shows the push; this run's transcript has none), fast-forward with exactly the four commits above. Main CI run [40408946800](https://github.com/knowledgeislands/tools-ki/actions/runs/40408946800) is red on DESIGN-2 alone: the released v0.13.0 still expects `tooling/boundaries`, the same red the fleet shows, which clears at step 4 once v0.14.1 installs.
- tools-ki, release: `v0.14.1` tagged at `825680cb` and pushed; Release run [40412437409](https://github.com/knowledgeislands/tools-ki/actions/runs/40412437409): validate passed, linux-x64 and darwin-arm64 packaged (full suite green), darwin-x64 failed twice (first run and a re-run of the failed job) on the same three tests, so publish, verify-release-install and the tap notification were skipped. No GitHub release exists for v0.14.1; `v0.14.0` stays unpublished and untouched.
- Fleet, prepared only: all eleven DESIGN-2-only checkouts and `apps-knowledgeislands.info` are clean and level with `origin/main` and still pin v0.13.0; commit messages are drafted in the scratch directory. `mcp-ki-kb-notion-mirror` has no checkout on this machine and is not visible under the GitHub account here, so it would need a clone or a different host when the pins bump.

## In Progress

Nothing. Steps 4 and 5 (tools-ki pin, fleet and website pins with the build-before-test reorder) all wait on a published v0.14.1 and are untouched. tools-ki main, the twelve fleet repositories and the website stay red on DESIGN-2 alone until a release installs.

## Queries

### REL-X64-TIMEOUT - darwin-x64 packaging fails on three five-second test timeouts, not memory

**Context** On the macos-latest (Intel) runner, `agent-control.test.ts` now runs to the end, but three tests hit vitest's 5000 ms default: `rereview-2: busy event publication after dispatch preserves a started worker`, and `third-review controls retain receipt with pending stop event` and `pending blocked event`. Each holds an events lock while the CLI runs its bounded retry loop (100 retries at 20 ms, about 2 s real time per busy transaction); the three make two such passes and take 4.3 s locally on Apple silicon, so they land at 5.02 to 5.05 s on the slower Intel runner. Both attempts failed identically, so this is a margin, not noise. The timeouts pre-date this release; they were hidden because the file used to crash earlier. A fix needs a new commit on `main`, and `v0.14.1` is a pushed tag that this run may not move, so the next release would be v0.14.2 and v0.14.1 would stay unpublished like v0.14.0. The brief says to raise rather than widen scope.

**Query** How should the darwin-x64 package job get past the three timeouts so ki can publish?

**Options**
a) (recommended, confidence high - both failures are identical and deterministic, the suite is otherwise green on all three targets, and the change is test-only) A bounded run gives those three lock-wait tests an explicit timeout (for example 30 s, or the file's lock tests generally), prepares v0.14.2, tags it and runs the Release workflow; the fleet pins then take v0.14.2 instead of v0.14.1.
b) (confidence medium - trims the real wait the tests sit in, but touches `src/core/agent/locking.ts` retry defaults or injects a budget through `KiContext`, a product change under `ki-self`) Make the busy-retry budget injectable so tests wait less, then release v0.14.2.
c) (confidence low - the brief requires every target to run the full suite) Package darwin-x64 without the test step.
d) (confidence low - needs a paid or unavailable runner label and does not remove the margin) Move the darwin-x64 package job to a larger macOS runner.

### 🤖 → 👤 Handoff to supervisor · since 00:03 GMT

🤖 0 running · 👤 1 with you · ⛔ 1 blocked · 📥 0 to accept

- [blocked] REL-X64-TIMEOUT darwin-x64 packaging timeouts; release, tools-ki pin, fleet and website pins wait on it · Kris · since 00:03 GMT

🧵 Coordination thread · Ways of working (ki.ways-of-working)
