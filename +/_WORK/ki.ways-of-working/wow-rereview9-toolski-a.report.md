VERDICT: REFUSE · confidence high - A valid older-reader append after checkpointing makes 0fd85a08 refuse the run.

# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-rereview9-toolski

**🤖 → 👤 Handoff to supervisor · Run report at 23:53 BST · last mark 23:06 BST**

---

## Done

Independently reviewed `51725e8b..0fd85a08` from code, tests and history. Earlier review and fix reports were not consulted. Every candidate gate used an exact detached `0fd85a08` copy; `f4ce77b8` remained held and excluded. No repository commits, admission, tags, work-record changes or remote operations were made.

### Blocking finding — B1: valid legacy journal extensions are treated as contradictions

[events.ts:295](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/src/core/agent/events.ts:295) accepts the journal only when it is a byte prefix of the saved checkpoint. A checkpoint-unaware `51725e8b` observer can append valid, sequential events after that checkpoint. The candidate rejects this ordinary forward extension before it can deliver the completion, even though the checkpoint prefix remains unchanged. Retrying produces the same refusal.

Reproduction uses the existing sandbox and legacy process adapter, `fixture(false)`, and the archived baseline CLI helper at [agent-control.test.ts:4724](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/src/tests/cli/agent-control.test.ts:4724):

1. Launch a worker using `51725e8b`.
2. Observe it once using `0fd85a08`, producing a checkpoint at sequence 1.
3. Write normal milestone progress and observe it using `51725e8b`; the old reader successfully appends sequence 2.
4. Write a report and `DONE`, mark the injected worker process exited, and observe and wait using `51725e8b`. The journal now contains sequence 3 and exactly one completion; the baseline reads it successfully.
5. Observe or wait using `0fd85a08`. It exits 1 with the event-evidence refusal. A second wait also exits 1. A separate progress-only reproduction fails in the same way.

This blocks admission under the explicit compatibility requirement. It is a consistent append, not contradictory evidence. The recovery guidance at [background-agents.md:80](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/docs/guides/user/background-agents.md:80) preserves mismatches for an explicit recovery decision; it supplies no normal adoption route for this valid extension. Fix forward-extension validation and adoption under the event lease while retaining the protection against checkpoint replacement and interrupted append loss. Preserve both copies; do not truncate the journal or discard checkpoint evidence.

### Non-blocking findings and limits

N1 — A legacy milestone can repeat after checkpoint adoption followed by snapshot loss. Its old journal lacks the full source status identity, and [events.ts:654](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/src/core/agent/events.ts:654) cannot reconstruct that identity. Independent milestone, failed and blocked cases retained all original journal bytes and exactly one completion; milestone progress appeared twice, while failed and blocked progress appeared once. The same milestone replay occurs on `51725e8b`. Modern source identities survived snapshot loss once each for all three forms.

N2 — The requested clean-state assertion is false for ki-principal: its sole untracked item is [the current review brief](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/briefs/wow-rereview9-toolski.md). Acquire is clean. Neither checkout has an untracked agent-report copy. These were read-only checks; nothing was cleaned or committed.

N3 — Review setup failures were corrected. The initial audit copy had an incorrect local Git identity, missing isolated dependencies and a conflicting coverage directory. The standalone suite later completed with 2 boundary failures out of 2,143 tests because that copy lacked the isolated boundary toolchain. Both boundary tests passed after installing it. The final, separately provisioned audit executed the complete coverage suite successfully. Neither tested checkout had tracked edits.

All 98 `thread.json` files in the full copied snapshot were redirected before reader execution, and all 59 absolute registry paths in each runnable copy were verified inside the temporary mirror. The comparison covered all 17 top-level runs. A fresh before/after comparison spanning both reader commands found no content changes in 13,614 original report-home files, and the write guard recorded zero outside-write attempts. Live decisions and an ignored cache had changed during earlier preparation, so this is not a claim that the entire live machine stayed static throughout the review.

### Admission plan assessment

The two primary fixes are represented: `6c498f3a` is patch-equivalent to `805e4d36`; `6c4d2a1a` is represented by `b2d8e795`, with all changed lines retained and the baseline's first-end report-homing guard preserved. This is a replacement of local ancestry, requiring the proposed compare-and-swap rather than an ordinary fast-forward.

The primary remained clean at `6c4d2a1aeabdac5ce5ca2e4bd711908d043afcf3`. Any future integration must serialize Git writes, recheck that exact expected tip and clean index/tree, guard the ref replacement, and synchronize the primary's index and working files while writers remain quiescent. The long-lived dispatcher retains its loaded code and starts children through the primary's on-disk launcher, as [runs.ts:1489](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/src/core/agent/runs.ts:1489) shows. Drain or deliberately stop the old dispatcher and held launchers, let in-flight KI control/event operations finish, perform the guarded update and tree synchronization, verify the installed tree, then start a fresh dispatcher from the admitted source.

Do not execute the proposed swap to `0fd85a0895d4f0b68937f092dd30aa0bc98f8c18`: B1 rejects that target. A fix requires a new reviewed target and renewed guard checks. No dispatcher was stopped or restarted during this review.

### Gate outcomes

PASS — Listed ordinary legacy cases: crashed workers, failure progress and later status, relaunch, legacy launch refusals, launcher-like wording and pre-event seeded snapshots.

FAIL — Mixed-reader compatibility: valid progress and completion appended by `51725e8b` after candidate checkpointing are repeatedly refused by `0fd85a08` (B1).

PASS — Interrupted-operation evidence: all 26 persistence-fault and 26 SIGKILL scenario families completed successfully.

PASS — Concurrent checkpoint replacement regression and snapshot-loss checks; independent modern provenance cases 3/3 and legacy completion cases 3/3, with the inherited milestone replay noted in N1.

PASS — Release history: CI's audit job and every release matrix suite job use full checkout history; the workflow regression passes.

PASS — Differential regressions: the same 16 tests fail on `3a3407e0` and pass on `0fd85a08`, including the concurrent checkpoint case.

FAIL — Initial standalone full coverage run: 2 setup-related boundary failures, 2,141 passes; missing isolated toolchain corrected (N3).

PASS — Corrected boundary rerun: 2/2.

PASS — Final full suite with coverage, executed by the pinned audit's TEST-5 gate: 100% statements, branches, functions and lines; verified coverage counters 14,304/14,304 lines, 3,600/3,600 functions and 11,772/11,772 branches.

PASS — TypeScript, `tsc --noEmit`.

PASS — Biome, check-only.

PASS — Candidate build.

PASS — Final `KI_REPO_OFFLINE=1 ki repo audit`: local KI `v0.12.0`, local Harness checkout `f4d6c521ef4859dc8965579bc39a5575004e3ac5`; exit 0, zero failing findings, eight warnings. The held current-Harness depcruise migration was not used for this gate.

PASS — Real-state readability: `51725e8b` reads 17/17 runs; `0fd85a08` reads the same 17/17.

PASS — Copied-state containment: all homes and registry paths redirected before execution; no observed outside writes or original report-home content changes during either reader command.

FAIL — Requested clean-checkout containment: ki-principal has the untracked current review brief; acquire is clean, and both have zero untracked agent-report copies (N2).

PASS — Primary expected-tip and fix-representation checks; supplied worktree and primary remained clean and unchanged. All review-owned temporary copies were removed.

## In Progress

Nothing running. Admission remains with the supervisor; B1 needs a fix and another admission review. The held `f4ce77b8` migration remains outside this review.

## Queries

None. The refusal is established by the reproduced compatibility failure; no additional owner information is needed to route the fix.

### 🤖 → 👤 Handoff to supervisor · since 23:53 BST

🤖 0 with worker · 👤 1 with you · 🅿️ 0 parked

- [with you] B1 — retain the admission hold and route compatible legacy extension recovery · supervisor · since 23:53 BST

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
