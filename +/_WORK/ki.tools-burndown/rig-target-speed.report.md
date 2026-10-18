# [Platform foundations](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Initiatives/platform-foundations.md) › [Tools burndown](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/tools-burndown.md) › rig-target-speed

**Run report at 22:48 BST · last mark none**

---

## Done

A single-target Rig preview is now about four times faster on `sol`, and output is unchanged. The work is delivered as [KI-TOOL-RIG-CORE-060](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-060-single-target-operation-speed.md), which is now Awaiting review.

The HNR mail-triage job is not declared on `sol`, so `scheduled-job:workstation-health` on the `laptop` profile stood in for it. Nothing ran a live apply, and the HNR job was not touched. Every measured run produced output byte-identical to the baseline binary's.

| Run (`apply --dry-run --profile laptop`, seconds) | Before | After | Main cost before → after |
|---|---|---|---|
| 50-tool fixture, one scheduled job | 1.3 | 1.1 | config load 0.6 → 0.6 |
| 50-tool fixture, whole profile | 2.1 | 2.2 | preflight of every item 1.0 → 1.2 |
| 200-tool fixture, one scheduled job | 14.3 | 3.2 | planner 9.8 → 0.1 |
| 200-tool fixture, whole profile | 17.6 | 7.3 | planner 9.6 → 0.1 |
| 500-tool fixture, one scheduled job | 171.3 | 10.1 | planner 149.9 → 0.4; config load 13.5 → 7.5 |
| 500-tool fixture, whole profile | 183.1 | 20.4 | planner 152.8 → 0.4 |
| `sol` `laptop` preview, one scheduled job | 23.6 | 5.4 | planner 13.2 → 0.7; profile 4.1 → 0.9 |
| `sol` `show scheduled-job:workstation-health` | 5.2 | 3.4 | config load only |

Fixture runs went through a timing wrapper; the `sol` rows are plain wall-clock time. On the fixtures, a targeted run probes native tools for its dependency closure only, and that was already true before this change.

What changed:

- The cause was algorithmic. Several steps rescanned the whole catalogue for every item, and the dependency planner was cubic.
- That work now takes one pass:
  - dependency planning
  - finding a tool's install bindings
  - resource ordering
  - native-target conflict checks
  - cycle checks
  - catalogue indexing
- Validation, profile and platform rules, dependency closure, repeated targets, scope limits and unrelated-resource safety all behave as before.
- Two new regression tests:
  - A targeted apply calls native tools for its dependency closure only.
  - The planner keeps its original order when an early tool waits on a later one.

The commits are local in tools-rig on `main` and not pushed: `4112c6c` reserves the record, `a6b368b` captures it, `a6fefba` is the implementation, and `fc01755` completes the record shape.

Checks:

- All 552 Bats tests pass.
- shellcheck, syntax check, assembly drift check, both benchmark budgets, native smoke probes, manual-page lint and whitespace check all pass.
- `ki repo audit` passes, with one warning that predates this work: no committed pre-commit hook (HOOK-1).

What still costs time: a targeted run on `sol` spends about 3.6 seconds loading and validating the whole configuration, 0.9 seconds resolving the profile and 0.7 planning. The configuration is still loaded in full on purpose, so a targeted run reports the same configuration errors as a full one.

## In Progress

Nothing is running. Before this run, tools-rig `main` had uncommitted edits to `bin/rig` and three `src/rig` modules. Those were this run's own earlier work, and they are now committed. No other session's files were touched.

## Queries

### RIG-TARGET-SPEED-ACCEPT - review KI-TOOL-RIG-CORE-060

**Context:** The record is Awaiting review. Its Review section has the change summary and the measurements, and its output matches the baseline. All four commits are local and unpushed.

**Query:** Should KI-TOOL-RIG-CORE-060 be accepted as delivered?

**Options:**

a) (recommended) Accept KI-TOOL-RIG-CORE-060 as done under ki-accept, commit the acceptance in tools-rig locally, and push tools-rig `main` from `sol`.

b) Accept it locally, but hold the push.

c) Hold acceptance and send it back for changes.

### RIG-TARGET-SPEED-LOAD - the remaining configuration-load cost

**Context:** Loading the whole configuration is now the main cost of a targeted run: about 3.6 of 5.4 seconds on `sol`. To go lower, Rig would have to cache the parsed configuration between runs, or speed up parsing and validation without validating any less.

**Query:** Should the load cost be taken further?

**Options:**

a) (recommended) Leave the load cost as it is. About 5 seconds is acceptable for a targeted preview, and there is no record to capture.

b) Capture a tools-rig triage record to speed up parsing and validation without caching.

c) Capture a tools-rig triage record for a parsed-configuration cache that is invalidated by configuration change.

```text
RIG-TARGET-SPEED-ACCEPT
Accept KI-TOOL-RIG-CORE-060 as done under ki-accept, commit the acceptance in tools-rig locally, and push tools-rig main from sol.
RIG-TARGET-SPEED-LOAD
Leave the load cost as it is. About 5 seconds is acceptable for a targeted preview, and there is no record to capture.
```
