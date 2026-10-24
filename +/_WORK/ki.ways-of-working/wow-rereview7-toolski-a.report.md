VERDICT: REFUSE · confidence high - legacy replay and checkpoint recovery remain unsafe, and the required offline audit is red.

# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-rereview7-toolski-a

**🤖 → 👤 Handoff to supervisor · blocked · Run report at 13:53 BST · last mark 08:24 BST**

---

## Done

### Blocking findings

#### P1 — Repeated legacy worker wording prevents recovery of a completed run

Location: [events.ts:596](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/src/core/agent/events.ts:596), with the rejection condition at line 601.

The progress identity combines attempt, kind and text but omits the source status identity. The earlier matching event consumes the current matching status evidence; the final repeated event is then refused as ambiguous. Supplying a valid report and completion status does not clear the refusal.

Reproduction uses the existing [CLI fixture](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/src/tests/cli/agent-control.test.ts:829) with managed control disabled and the [real baseline loader](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/src/tests/cli/agent-control.test.ts:4724), which builds commit `51725e8b` from Git:

1. Launch a worker through the baseline CLI and keep it alive.
2. Have the baseline CLI observe the worker’s failed progress twice, at 12:00 and 12:01, using the missing-report launcher wording both times.
3. Upgrade to `3a3407e0` and request status: it exits 1 for ambiguous legacy failure at sequence 3 despite the matching current status and snapshot.
4. Write the report, retain the second progress line followed by `DONE`, and confirm the worker has ended. Status still exits 1, preventing completion recovery.

This also reproduces with blocked progress using gate-failure wording, and with the snapshot removed. All four combinations fail. These are ordinary baseline-produced journals, without fabricated event rows. Classification must preserve distinct progress occurrences and permit completion recovery from the retained evidence.

#### P1 — Initial checkpoint adoption can erase a newer committed append intent

Location: [events.ts:369](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/src/core/agent/events.ts:369); a control caller reaches this through [controls.ts:93](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/src/core/agent/controls.ts:93).

The first checkpoint is written without the event lease and without re-reading concurrent publication evidence. A control operation can therefore publish its stale checkpoint after an observer has committed a newer recovery intent.

Reproduction uses the same public CLI fixture and real baseline loader:

1. Launch through `51725e8b`, leaving its genuine journal and no checkpoint. Supply the worker’s report and completion status, with the process ended.
2. Start the upgraded stop command and suspend its first checkpoint temporary-file write before it writes anything.
3. Concurrently request status. Let it commit the checkpoint containing completion at sequence 2, then inject a short journal append that writes half the completion event. Status refuses, leaving a recoverable full append intent.
4. Resume the stop command. Its initializer replaces the sequence-2 checkpoint with its stale sequence-1 checkpoint.
5. Request status again: it exits 1 because journal and checkpoint differ. The committed completion suffix needed for exact recovery has been overwritten.

The probe verified the checkpoint regression from sequence 2 to 1 and the subsequent refusal. Initial adoption must share publication’s event lock and re-read the checkpoint before writing.

#### P1 — The required audit rejects the candidate while the migration is held

Location: [package.json:56](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/package.json:56).

Reproduction: run the compiled `3a3407e0` CLI’s repository audit with `KI_REPO_OFFLINE=1`, isolated registered state, and a local copy of the installed Harness at `03d415638894`. `DESIGN-2` fails because that Harness requires the prepare script to provision `tooling/depcruise`, while this candidate provisions `tooling/boundaries`.

The migration is in the explicitly held-back `d4849813`. The requested admission set therefore does not meet the audit gate under the current Harness contract. Resolve the intended compatible audit contract or review the held migration separately; this review does not authorise including it.

### Non-blocking findings and review limits

Workflow history is correct at the admission tip: the CI audit job and release package jobs have full checkout history, at [ci.yml:20](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/.github/workflows/ci.yml:20) and [release.yml:78](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/.github/workflows/release.yml:78). The baseline is an ancestor of the admission tip.

The primary’s two local fixes are represented: `6c498f3a` maps to `805e4d36` with identical changed-line patches; `6c4d2a1a` maps to `b2d8e795`, retaining the additional first-completion report guard. The primary remains clean at `6c4d2a1aeabdac5ce5ca2e4bd711908d043afcf3`. A future admission must re-check that expected old value, branch and clean index/tree under one writer, and synchronise the checked-out files with the ref. Use the exact reviewed target, rather than the integration branch’s later tip. Admission remains blocked by the findings above.

The audit also reports `TEST-5`: seven installer tests timed out under the blanket OS network denial. Their [fixture binds loopback](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/src/tests/install/_helper.ts:135), which that denial blocks; the ordinary full suite passed them. This is a limitation of the coverage run’s setup, not an independently established installer defect. Other audit warnings include isolated-registry/clone artifacts and pre-existing governance warnings; they were not changed.

Execution exception: the initial temporary bootstrap inadvertently fetched the pinned Harness archive, breaching the no-network bound. That setup was abandoned. The final audit used a local Harness copy, offline mode and an OS network denial. No remote was mutated. This deviation is retained explicitly for the supervisor’s assessment.

Reviewed code, tests and history for `51725e8b..d4849813`; all candidate gates used `3a3407e09dd0b2d39976840d95e8b4ee94b63de7`, excluding the migration. No earlier review or fix report was consulted, and no repository commit was created.

### Gate results

PASS — Full test suite: 96 files and 2,127 tests passed on the admission tip.

PASS — TypeScript: the no-emit compiler check passed.

PASS — Biome: the check-only repository pass succeeded.

PASS — Build: the candidate compiled successfully.

FAIL — `KI_REPO_OFFLINE=1 ki repo audit`: `DESIGN-2` contract mismatch and `TEST-5` installer timeouts under network denial; coverage is not verified clean by this run.

PASS — Prior-candidate discrimination: 31 agent cases and the workflow case fail on `a7c80cd8`; all 50 selected cases pass on `3a3407e0`, without missing-history or fixture-loading failures.

FAIL — Independent admission probes: four repeated-status cases and one concurrent checkpoint-adoption case fail the required behaviour on `3a3407e0`.

## In Progress

Nothing running. Temporary copies are removed before completion. The supplied checkout and primary remain unchanged; no admission was performed.

## Queries

### TOOLS-RECOVERY — Fix both recovery defects before admission

**Context:** Real legacy runs remain stuck after repeated launcher-like worker progress even when valid completion evidence is supplied. Concurrent first-checkpoint adoption can also overwrite a committed append-recovery intent. Both defects reproduce at the proposed admission tip despite the existing suite passing.

**Query:** Should a writing run fix both classes and return for a new blind admission review?

**Options:**

a) (recommended, confidence high - both defects are reproduced through the public CLI) Fix both classes, add the missing regression cases, rerun the gates and obtain a fresh blind review.

b) Keep the current primary and set this candidate aside.

### TOOLS-AUDIT — Resolve the audit contract while keeping the migration held

**Context:** The current Harness at `03d415638894` rejects the candidate’s old tooling path, while the migration that satisfies it is explicitly excluded from admission. The blanket network denial also blocks the installer fixtures’ loopback servers, preventing a clean coverage result in this audit setup.

**Query:** Which Harness revision and local-fixture network allowance should govern the next admission audit?

**Options:**

a) (recommended, confidence high - preserves the explicit admission boundary and makes the gate reproducible) Keep `d4849813` held, identify an approved compatible Harness revision, and explicitly allow only fixture loopback while denying external network for the audit.

b) Keep admission blocked while the tooling migration receives separate review and the audit setup is agreed.

### 🤖 → 👤 Handoff to supervisor · blocked · since 13:53 BST

👤 2 with you · ⛔ 3 blocked

- [with you] TOOLS-RECOVERY · supervisor · since 13:53 BST
- [with you] TOOLS-AUDIT · supervisor · since 13:53 BST
- [blocked] repeated legacy-status recovery · repo/tools-ki · since 13:18 BST
- [blocked] concurrent checkpoint recovery · repo/tools-ki · since 13:26 BST
- [blocked] admission audit contract · repo/tools-ki · since 13:49 BST

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
