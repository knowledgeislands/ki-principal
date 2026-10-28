# Independent release review › wow-review-rel

**Run report at 13:26 GMT**

---

## Done

Reviewed local HEAD and v0.14.0 at `09316eb5`; no repository changes or commits made.

Release workflow, Vitest configuration, fixture teardown and v0.13.0 comparison checked; recommendations below.

Dependency-checker references checked across CI, packaging, tests and agent worktree preparation; runtime coupling found.

No remote calls or test execution; Actions failures, timings, publication status and downstream impact are supplied context, not independently verified.

## In Progress

Nothing running.

## Findings

### RELEASE-RECOVERY - Repair the footprint and retain platform tests

**Goal:** Recommend how the failed release should proceed, as requested in this review.

**Scope:** Local release workflow, Vitest configuration, agent-control suite and sandbox helper; no Actions logs or memory profiling.

**As of:** 25 October 2026, 13:26 GMT.

**Choice:** Fix the test footprint and also set a bounded heap allowance on the package test step; release v0.14.1.

**Confidence:** High.

**Reason:** The newly added 5,284-line suite and reported heap failures justify splitting coherent test groups while preserving the existing tests on every packaging platform, rather than relying solely on more memory ([suite](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-control.test.ts:1), [configuration](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/vitest.config.ts:8), [release workflow](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/.github/workflows/release.yml:85)). Sandbox directories already have per-test teardown, so missing directory cleanup is not an established cause; investigate retained JavaScript state rather than assuming fixture cleanup is absent ([helper](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/_cli_helper.ts:274)). Select a heap budget appropriate to runner memory, verify that it reaches the failing worker, and require successful full-suite packaging runs on all three targets before publishing the new version.

Queries raised: none; this is an advisory recommendation.

### CHECKER-MIGRATION - Separate the migration from release recovery

**Goal:** Recommend whether the checker rename and self-audit version bump belong in the release repair.

**Scope:** Local checker installation references, boundary tests, worktree preparation and CI version pin; no work records read or created.

**As of:** 25 October 2026, 13:26 GMT.

**Choice:** Capture a separate tools-ki work record and leave tools-ki on v0.13.0 for now.

**Confidence:** Medium.

**Reason:** The rename reaches beyond CI: agent worktree preparation explicitly copies the old checker dependency root, and its contract test asserts that behavior ([runtime](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/worktrees.ts:47), [test](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/agent-worktrees.test.ts:61)). Both workflows, root preparation and boundary checks also require coordinated updates, while the inspected release workflow does not depend on changing tools-ki's self-audit version ([CI](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/.github/workflows/ci.yml:12), [preparation](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/package.json:56), [boundary tests](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/boundaries.test.ts:9)). Make this a prompt, complete follow-up with worktree verification, and bump the self-audit pin only after the chosen release is available to install.

Queries raised: none; this is an advisory recommendation.

## Queries

No outstanding queries.
