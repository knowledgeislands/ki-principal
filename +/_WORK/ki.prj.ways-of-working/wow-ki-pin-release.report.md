# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-ki-pin-release

**🤖 → 👤 Handoff to supervisor · blocked · Run report at 13:17 GMT · last mark 01:07 GMT**

---

## Done

All work was done in clean clones of `origin/main` under the run's scratch folder; the primary checkouts were not touched.

- tools-ki `1d65a32e` `fix(bootstrap): pin the v0.14.0 Harness archive`: canonical harness pin moved from `52779419` to harness main `fdf9a604` (newest green main commit, after `5cb52973`), digest recomputed from the downloaded archive, bootstrap test fixtures updated.
- tools-ki `143df112` `test(agent): normalise the resolved fixture root in launch snapshots`: test-only fix for the failure that had kept tools-ki main red since 2026-10-21 (TEST-5): the agent-compatibility snapshot carried the macOS `/private` prefix. Beyond the brief's letter but required for a green main before the release; no runtime code changed.
- tools-ki `09316eb5` `chore(release): prepare v0.14.0`: package version and CHANGELOG baseline line.
- Local verification in the clone: full suite passed (97 files, 2150 tests, 100% coverage thresholds); Biome clean apart from two pre-existing infos; `ki repo audit` TEST-5 pass. Two local audit failures are not caused by this work: DESIGN-2 (tools-ki itself still has `tooling/boundaries`, see query Q3) and RUNTIMES-2 (clean clone lacks the gitignored materialised skill folders; the primary checkout passes).
- Pushed fast-forward to tools-ki `main`; CI run 40190921009 success: https://github.com/knowledgeislands/tools-ki/actions/runs/40190921009 (first green main since 2026-10-21).
- Tag `v0.14.0` created at `09316eb5` and pushed; `Release` workflow dispatched from main with `version=v0.14.0`.
- Release run 40192625875 failed: https://github.com/knowledgeislands/tools-ki/actions/runs/40192625875. Validate: success. linux-x64 package: success (20 min). darwin-x64 and darwin-arm64 package: failure, both in the `bun run test` step: the vitest fork worker for `src/tests/cli/agent-control.test.ts` died with `FATAL ERROR: Reached heap limit Allocation failed - JavaScript heap out of memory` (Node 24.22.1 via mise); 96 of 97 files and 2111 of 2150 tests had passed; the jobs ran 38 and 50 min against about 2 min for the v0.13.0 release. Sign and publish, verify install and notify tap: skipped. No GitHub release or draft exists for v0.14.0; the tag exists on origin.
- Release fan-out (tap formula PR, tap CI, notify job): not started, because nothing was published.
- Website: `KI_VERSION: v0.14.0` edited in the clone's `.github/workflows/ci.yml` but not committed or pushed, because no v0.14.0 release exists to install. Local website checks: `bun run test` fails on a fresh clone because `verify-diagrams.test.ts` reads `apps/site/dist`; after `bun run ki:site:build` all tests pass (116 + 15). See query Q2.
- Prerequisites checked, nothing changed: immutable releases on, release bot variable present, `gh` authenticated as krisb.

## In Progress

Nothing is running. The scratch folder holds the tools-ki and website clones, the downloaded harness archive and the logs (`release-failed.log` has the failing job output); nothing in it needs to survive `ki agent close` except as evidence.

## Queries

### Q1 - ki v0.14.0 cannot publish: macOS package jobs run out of memory in the agent-control test file

**Context** The release workflow checks out the tag commit and runs `bun run test` on each packaging runner before packaging. On both macOS runners the vitest worker running `src/tests/cli/agent-control.test.ts` (5284 lines, 544 tests, last changed 2026-10-22, after v0.13.0) exhausted the Node heap; Linux passed and the same file passes locally on macOS in 153 s. The 20 to 50 min job times suggest heavy swapping on the 7 GB macOS runners. The brief says to stop if the release process needs a setting change. Published tags must never be moved, and `v0.14.0` is already on origin, so any fix in the tested commit means a new version. The website stays red on DESIGN-2 until a release ships.

**Query** How should the release proceed?

**Options**
a) (recommended, confidence medium - the only path that keeps the release process honest and gives the test a stable footprint on every runner) Fix the test footprint in tools-ki main: split `agent-control.test.ts` into smaller files or free its fixtures between groups, and give the package job's test step a `NODE_OPTIONS=--max-old-space-size` ceiling matched to the runner; prepare and tag `v0.14.1`, dispatch Release, then continue steps 2 and 3 of the brief against v0.14.1. Leave the `v0.14.0` tag in place unpublished.
b) Only raise the heap ceiling in `release.yml` for the package test step, prepare and tag `v0.14.1`, and re-dispatch. Smallest change, but it may merely slow the failure if the test file keeps growing.
c) Change the release workflow to run the test suite on Linux only and let the macOS jobs package without testing, then tag `v0.14.1`. Cuts release time but weakens the release gate.
d) Leave the release unpublished and keep the website on v0.13.0 with DESIGN-2 red until a later window.

### Q2 - website CI runs tests before the site build, so it would fail again after the pin fix

**Context** The website CI order is audit, then `bun run test`, then `bun run ki:site:build`. The test "passthrough viewers and SVGs remain byte-identical after the site build" in `apps/site/scripts/verify-diagrams.test.ts` reads `apps/site/dist`, which only exists after the build, so on a clean runner the test step fails whatever `KI_VERSION` says. On a fresh clone the suite failed before the build and passed after it. This is a failure "for a reason other than this drift", so the brief says to query rather than fix.

**Query** May the website run move `bun run ki:site:build` before `bun run test` in `.github/workflows/ci.yml` (one line), in the same commit as the `KI_VERSION` bump, once a release exists?

**Options**
a) (recommended, confidence high - the test is a post-build check by design and the fix is one line in a file the run already edits) Yes, reorder build before test in the same commit as the pin bump and watch CI.
b) Keep the KI_VERSION bump on its own and raise the ordering as a website work record for a later run.
c) Skip or remove the dist-dependent test instead.

### Q3 - tools-ki's own CI will hit the same DESIGN-2 drift when its KI_VERSION moves

**Context** tools-ki's CI installs released ki `v0.13.0` and audits itself. Its checker root is still `tooling/boundaries` and `ci.yml` installs it at that path. The clone's local audit with current ki already fails DESIGN-2 for that reason. Nothing fails today, because v0.13.0 still expects the old name; it will fail the moment tools-ki bumps its own `KI_VERSION` to a release carrying the new pin.

**Query** Should the rename to `tooling/depcruise` and the `KI_VERSION` bump in tools-ki be folded into the v0.14.1 work in Q1, or left as a separate work record?

**Options**
a) (recommended, confidence medium - it is the same drift the brief exists to clear and it is small, but it widens the run's scope) Fold the rename and the tools-ki `KI_VERSION` bump into the v0.14.1 run so tools-ki's own CI stays green after the release.
b) Capture it as a tools-ki work record and leave tools-ki on v0.13.0 for now.
