VERDICT: REFUSE · confidence high - required receiver containment remains unverified despite passing code gates.

# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-rereview8-toolski-a

**🤖 → 👤 Handoff to supervisor · blocked · Run report at 17:19 BST · last mark 08:24 BST**

---

## Done

Reviewed 51725e8b..0fd85a08 independently from source, tests and history. Earlier review/fix prose was not consulted; report bytes were hashed solely for containment. f4ce77b8 stayed excluded. No changes to the supplied checkout, primary, receivers or work records were made; no live admission occurred.

### Blocking finding — receiver containment cannot be certified

There are 873 untracked Principal reports and three untracked Acquire reports, all byte-identical to their corresponding runtime reports. Examples: [Principal copy](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.chezmoi/accept-047.report.md:1) and [Acquire copy](/Users/krisbrown/workspaces/personal/acquire/+/_WORK/kb.regular.acquire-intake/granola-trust.report.md:1). The other Acquire copies are messaging-close.report.md and spec-link.report.md in the same folder.

Nine tracked reports under +/_WORK/ki.baseline-rollout/ differ from HEAD and match the runtime copies; [raise-tmx.report.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.baseline-rollout/raise-tmx.report.md:29) is one example. Their modification times cluster at 11:09:46 BST on 22 October.

Reproduction: enumerate Git's untracked report paths in each receiver, resolve their runs through runtime thread.json homes, and compare SHA-256 values with the corresponding runtime reports. For the tracked example, compare the working file with its HEAD blob and then with agents/baseline-rollout/raise-tmx.report.md: it differs from Git and equals runtime state.

These artifacts and deltas existed before this review and remain unchanged. Hashes and timestamps do not establish which earlier invocation created each artifact. Without provenance or a reviewed reconciliation, I cannot certify the brief's narrower requirement that verification copies are gone and tracked receivers were not changed by verification. I have not treated every pre-existing dirty file as proven fallout from this range.

### Non-blocking findings

The primary's fixes are represented: 6c498f3a by 805e4d36, and 6c4d2a1a by b2d8e795, with the integration retaining first-end-only report homing together with the control homeReports gate at [events.ts](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/src/core/agent/events.ts:863). The private admission rehearsal accepted the expected old ref, rejected a stale expected ref, and left its checkout and index clean at 0fd85a0895d4f0b68937f092dd30aa0bc98f8c18. A future admission must serialize writers, recheck the clean primary at the stipulated old commit, and update the checkout/index as well as the ref.

Initial verification attempts were invalidated by my copy setup: concurrent coverage writers shared an output directory, the clone lacked canonical origin metadata, and a macOS temporary-path alias mismatched four golden snapshots. I corrected these in temporary copies, verified the affected checks, and ran the final native CI audit alone. An initial real-state trial that rewrote journal text was also discarded; the reported comparison preserves journal/checkpoint bytes and redirects report homes and registry into the supplied temporary area.

### Gates

PASS — Legacy compatibility: the requested old-run cases remain readable and retain completion/relaunch behavior.

PASS — Evidence preservation: persistence faults, process interruption, checkpoint replacement and snapshot-loss/progress provenance checks pass.

PASS — Release history: both CI audit and release suite jobs check out full baseline history.

PASS — Red/green regressions: the same 16 cases fail on production code at 3a3407e0 and pass at 0fd85a08; see [legacy cases](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/src/tests/cli/agent-control.test.ts:4758) and [checkpoint race](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/src/tests/cli/agent-control-recovery.test.ts:143).

PASS — Full suite with coverage through the final native audit: all configured 100% coverage thresholds pass.

PASS — TypeScript.

PASS — Biome.

PASS — Build.

PASS — Offline repository audit: KI v0.12.0, local Harness checkout f4d6c521ef4859dc8965579bc39a5575004e3ac5, and KI_REPO_OFFLINE=1; no FAIL findings.

PASS — Real-state comparison: baseline 17/17 runs readable; candidate 17/17, on independent copies with mirrored report homes and a temporary registry.

FAIL — Receiver containment: the remaining copied reports and tracked report deltas prevent the required certification.

PASS — Admission-plan inputs and private guarded-swap rehearsal; live primary remains at 6c4d2a1aeabdac5ce5ca2e4bd711908d043afcf3.

PASS — Review isolation: supplied checkout, primary and both receiver HEADs/status/tracked diffs match their initial inventory; no remote calls, tags or work-record changes.

## In Progress

Nothing running.

Outstanding — no action requested now: the candidate remains held pending receiver provenance and a fresh containment check. The depcruise migration remains separately held.

## Queries

### CONTAINMENT — establish the receiver artifacts' disposition

**Context:** The required containment proof is missing for 876 untracked copies and nine tracked report deltas. Their presence and byte equality are verified, but attribution to a particular prior invocation is not. This review's read-only bounds exclude reconciling receiver files.

**Query:** Can the coordinator establish the exact verification side effects and their disposition before admission is reconsidered?

**Options:**

a) (recommended, confidence high - preserves the explicit admission gate and the read-only boundary) Keep admission held, establish provenance, arrange a narrowly scoped owner-authorized reconciliation of confirmed verification side effects, and repeat containment.

b) Supply a prior inventory proving these artifacts and deltas are unrelated to verification, then repeat the containment assessment without changing them.

### 🤖 → 👤 Handoff to supervisor · blocked · since 17:19 BST

👤 1 with you · ⛔ 1 blocked

- [with you] CONTAINMENT · owner · since 17:19 BST
- [blocked] tools-ki admission · work/ki.ways-of-working · since 17:19 BST

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
