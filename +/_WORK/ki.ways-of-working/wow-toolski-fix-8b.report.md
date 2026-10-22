# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-toolski-fix-8b

**🤖 → 👤 Handoff to supervisor · Run report at 16:13 BST · last mark 08:24 BST**

---

## Done

Fixed every blocking recovery finding in reviews a, b and c. The settled audit boundary was applied separately to the admission and migration trees. No admission, live remote operation, tag or release was performed; primary `main` remains `6c4d2a1a`. A comparison-harness mistake temporarily created fourteen untracked receiver-report copies outside the allowed worktree; those copies were identified and quarantined to restore their prior absence, as detailed below.

Ordered range `51725e8b..f4ce77b8` on `wow-toolski-integrate`:

1. `805e4d36` — original terminal/control identity fix, retained unchanged.
2. `b2d8e795` — original interrupted-control evidence fix, retained unchanged.
3. `4cd0ab87` — original preparation/append recovery fix, retained unchanged.
4. `b3fec501` — original renamed-folder history regression, retained unchanged.
5. `a7c80cd8` — original legacy failure classification fix, retained unchanged.
6. `22e0ea9c` — earlier worker-progress fix, retained unchanged.
7. `3a3407e0` — baseline-history CI fix, retained unchanged.
8. `0fd85a08` — seventh-round recovery fix; **new admission tip**.
9. `f4ce77b8` — **held migration, last**, rebased from `d4849813`; its stable patch ID is unchanged.

**A: repeated legacy worker wording.** Uncorroborated old failures remain provisional instead of refusing the run. Repeated wording is classified independently of how many times a retained line has been matched; only the latest matching progress event receives that source identity. A following genuine launcher failure keeps its own terminal identity. [Ten baseline-upgrade variants](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/src/tests/cli/agent-control.test.ts:4758) cover launcher-like failed/blocked wording, successful completion, one report home and snapshot reconstruction. The existing duplicate-text terminal regression also checks both identities.

**A: concurrent initial checkpoint replacement.** Unlocked initialization now validates without writing a checkpoint. Only a publisher that has read under `events.lock` adopts it. The [concurrent initializer regression](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/src/tests/cli/agent-control-recovery.test.ts:143) pauses the initializer after observing no checkpoint, commits sequence 2 with a short completion append, resumes initialization, verifies the committed checkpoint is byte-identical, and recovers exactly one completion and report home.

**Cross-attempt corroboration:** the [additional baseline regression](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/src/tests/cli/agent-control.test.ts:4822) reproduced a later attempt’s completed snapshot incorrectly corroborating an earlier worker-progress failure. Crash corroboration now requires the snapshot’s attempt to match. This additional regression fails on the intermediate candidate and passes after the guard; it is included in the 16-case original-baseline discrimination and final full reruns.

**B1/C1: ordinary crashed legacy runs.** Retained crash status can corroborate an old terminal failure; missing terminal metadata alone cannot fence the run. Otherwise a fresh observation publishes the actual outcome. [Real-baseline crash regressions](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/src/tests/cli/agent-control.test.ts:4792) exercise status, relaunch, successor completion and close with and without the old snapshot.

**B3/C4: pre-event snapshots.** Legacy snapshots can remember completion, status and queries that predate event publication. They are retained unless worker failure progress identifies the known poisoned-end case. [Pre-event snapshot regressions](/Users/krisbrown/.local/state/ki/worktrees/tools-ki/wow-toolski-integrate-f579054bcd51/src/tests/cli/agent-control.test.ts:4845) cover ordinary and protocol status plus an earlier query absent from the journal; they also append milestone, failed and blocked progress and observe again. Only failure rows whose original journal lacked terminal metadata can trigger the old poisoning repair; newly typed progress cannot reopen an ended pre-event attempt. Only an explicit modern launch/hold identity establishes complete modern history, so later progress cannot erase a pre-event ended state. The added observations fail on the intermediate candidate and pass with this provenance rule. Modern typed history still rejects lost or changed terminal/status/query evidence; existing digest, sequence, cursor, immutable-attempt and confirmed-receipt contradiction regressions remain in force.

**A audit/C2/B2: settled boundary.** Admission `0fd85a08` was audited with locally compiled KI `v0.12.0` and a local Harness `f4d6c521ef4859dc8965579bc39a5575004e3ac5` snapshot. Migration `f4ce77b8` was audited with the candidate CLI and local current Harness `03d4156388944d374fd9a8b1fa69c8fe56fa7e79`, later than `db5e3cff`. Both used isolated homes/registries, `KI_REPO_OFFLINE=1`, and OS denial of external network with fixture loopback allowed. The current-Harness pre-migration `tooling/depcruise` mismatch remains expected and outside the settled admission gate.

The first full audit attempts passed their test/coverage gates but failed boundary containment because my temporary copies linked their isolated dependency directories outside the clone. Replacing those links with physical contained copies corrected the audit setup; that correction needed no source change. The final full reruns include the later attempt-scope guard and passed. Nonblocking audit warnings remain, including isolated-registry/clone context and existing toolchain/CI guidance.

Execution exception: early focused test invocations used the sandbox's default OS temporary root before I explicitly routed those fixtures through the designated run root. Their automatic teardowns removed the fixtures. The copied agent state, full audit environments and final focused test fixtures used the designated run root. Live agent state was not written; the separate receiver-home spill below affected two other repositories and was reversed.

**Comparator containment exception, restored:** copied `thread.json` records still pointed at real report homes in the early comparison harness. That created fourteen untracked report copies in `ki-principal` and `acquire`. I established ownership from creation times matching copied completion events, exact hashes against unchanged original agent reports, zero corresponding live completion events, and absence from the Git index. The injected Git response made both readers skip any already-existing report target. I moved only those unchanged new copies into quarantine and restored the receiver paths to absence; I did not revert an existing or tracked receiver file. An expanded check across both original snapshots found no other newly created matching receiver reports. Final comparisons redirect every report home to a frozen temporary mirror and run under an OS sandbox denying writes outside the designated run root and denying network access. The quarantined duplicates are discarded only after verifying that the original reports remain unchanged.

Restored receiver paths and verified hashes:

- `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.mac-studio-setup/fix027.report.md` — SHA-256 `076449e7465afa9bb30b77974c010d273ff38586332826dd244958092ca1c10f`.
- `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/wow-rereview6-toolski-b.report.md` — SHA-256 `3903dafd2cfa1b9aaa389919cedde6b2b01a95028e5d4a11f50ef1e95d5efd0f`.
- `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/wow-rereview7-toolski-a.report.md` — SHA-256 `3a857d9d49a2d4bc283b1f6d37670221132850da84aff372e94c4ee7d163ea27`.
- `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/wow-rereview7-toolski-b.report.md` — SHA-256 `eb4ecca1c4e1232c06adf6005932a7c3d6e03d37df0c0d2ca5cc4c07837c36b4`.
- `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/wow-rereview7-toolski-c.report.md` — SHA-256 `5bae968fe5411cec70746e2f95544eb0df2d75981daea4f84f0c4d406090c245`.
- `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/wow-toolski-fix-7.report.md` — SHA-256 `611909c9690f354353419fd26d8cad21ca22d4f750d9d742a6f0ed060acc95b3`.
- `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/wow-toolski-fix-8.report.md` — SHA-256 `1f9aa4384359d5205886ca8f5fbe84126f8bbb20edac032755f7d459e31518a2`.
- `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/review-hold.report.md` — SHA-256 `a12ed5886cd8a39d2901fa32ad985ce7e3963123cd941c0205f2b086afd91bf6`.
- `/Users/krisbrown/workspaces/personal/acquire/+/_WORK/kb.regular.acquire-intake/ledger-removal.report.md` — SHA-256 `8afd54b2f9188c4f5d959e167ae35b6756f6343999510339aee55b1bf5c9421b`.
- `/Users/krisbrown/workspaces/personal/acquire/+/_WORK/kb.regular.acquire-intake/query-review-7.report.md` — SHA-256 `27df2c8128c34e66a8d575751642f835297dd0495cf315b40181b70e241d0466`.
- `/Users/krisbrown/workspaces/personal/acquire/+/_WORK/kb.regular.acquire-intake/roadmap-clear.report.md` — SHA-256 `70cabf28a502b6e7987dccc8c8fbfa65088bb57972298c53e271246e4c38c001`.
- `/Users/krisbrown/workspaces/personal/acquire/+/_WORK/kb.regular.acquire-intake/simplify-apply.report.md` — SHA-256 `d8ea6a2333917293d92d109c6425e67dd8b3df5ee16cac6746128697fa4dea87`.
- `/Users/krisbrown/workspaces/personal/acquire/+/_WORK/kb.regular.acquire-intake/simplify.report.md` — SHA-256 `d851d72ebd145a7810c6f34cdb82ecc184446986c92b3d23a4f610077dbd0acc`.
- `/Users/krisbrown/workspaces/personal/acquire/+/_WORK/kb.regular.acquire-intake/skills-cut.report.md` — SHA-256 `2e2b159e6d61a57813ff4691b35e0bf9be518bc35744af1c08af278d05a9d8cc`.

**Regression discrimination:** all 16 new seventh-round cases fail against production source at `3a3407e0`, without missing-history, fixture-loading or timeout failures; all pass after the fix. The complete two-file agent recovery suite passes all 565 cases. Earlier ambiguity-refusal expectations now assert provisional replay and eventual completion, while modern contradiction checks remain strict. The recovery guide describes the new behavior.

**Real-state proof:** a temporary snapshot captured at 14:41 BST covered every one of the 17 live run folders enumerated by the CLI, including the four without journals. `_archive`, logs and unrelated temporary payloads were excluded; event, control, launch, PID, status, report and prior-attempt-name evidence was copied. Each CLI used an independent copy and identical injected offline process observations, with report homes redirected to frozen temporary mirrors. OS policy denied writes outside the temporary run root and all network access; external commands, fetching, launching and signalling were also disabled. `51725e8b` reads **17/17**; admission `0fd85a08` reads **17/17**; migration tip `f4ce77b8` reads **17/17**. No refusal or genuine contradiction remains in that snapshot. Live agent state was never mutated.

PASS — Full suite: unfiltered coverage-backed suites pass on both audit trees; the four 100% coverage thresholds and exclusions are unchanged.

PASS — TypeScript: full no-emit checks pass on the admission and migration trees.

PASS — Biome: full check-only passes on the admission and migration trees.

PASS — Build: canonical compiled builds pass on the admission and migration trees.

PASS — rumdl: full repository checks pass on the admission and migration trees; this report also passes.

PASS — Admission offline audit: `0fd85a08`, KI `v0.12.0`, pinned Harness `f4d6c521…`; zero failures, 9 nonblocking warnings.

PASS — Migration offline audit: `f4ce77b8`, candidate CLI, current Harness `03d41563…`; zero failures, 13 nonblocking warnings.

PASS — History and final-tree fidelity: normal hooks, explicit-path commits, post-hook path inspection, unchanged earlier ancestors, unchanged migration patch, clean supplied tree and byte-identical tracked audit trees. Execution-bound exceptions and restoration are disclosed above.

**Updated admission plan:** send `51725e8b..0fd85a08` for independent review, including the containment-restoration evidence and excluding `f4ce77b8`. After approval, recheck the primary checkout and expected `main=6c4d2a1a`; admission requires the previously reviewed guarded compare-and-swap, because the candidate is not a descendant of that primary tip. Preserve both primary fixes through their existing equivalents in the candidate and verify the worktree after the guarded update. Keep migration `f4ce77b8` held for its separate review and a compatible CI/Harness transition; its current-Harness audit does not authorize including it in the pre-migration admission. This run performs none of those admission steps.

## In Progress

Nothing running. Outstanding — no action requested now: independent review and any subsequent admission belong to the coordinator; the migration remains held. All temporary audit/source/state copies were removed after preserving this report.

## Queries

None.

### 🤖 → 👤 Handoff to supervisor · since 16:13 BST

👤 1 with you · ⛔ 0 blocked

- [with you] Seventh-round fixes and updated admission plan · supervisor · since 16:13 BST

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
