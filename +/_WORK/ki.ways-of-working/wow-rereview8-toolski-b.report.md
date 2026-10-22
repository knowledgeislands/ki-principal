# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-rereview8-toolski-b

VERDICT: ACCEPT · confidence medium - every gate passes, upgraded real state reads 17/17 runs, and the remaining refusal needs a mixed-version downgrade that already exists live

**🤖 → 👤 Handoff to supervisor · Run report at 17:15 BST · last mark 17:15 BST**

---

## Done

Blind review of tools-ki range `51725e8b..0fd85a08` (`805e4d36`, `b2d8e795`, `4cd0ab87`, `b3fec501`, `a7c80cd8`, `22e0ea9c`, `3a3407e0`, `0fd85a08`). The held depcruise rename `f4ce77b8` was read for context only. All work ran in temporary detached worktrees and copies under `$TMPDIR`, which have been removed.

**Blocking findings.** None.

**Non-blocking findings.**

N1, mixed-version refusal, `src/core/agent/events.ts:302`. If a checkpoint-unaware reader appends to a journal that already has a v2 `events.history`, the candidate refuses with "journal differs from committed history". The journal is then a strict, valid extension of the checkpoint, so this is not a genuine contradiction. Reproduction on my copy of live agent state: read `ways-of-working` with `6c4d2a1a`-written state, then with `51725e8b` (which appended seq 2357–2371 without touching the checkpoint), then with `0fd85a08`; the last step refuses. Setting `events.history` aside makes the run readable again with exit 0. The same refusal already exists in the live primary `6c4d2a1a`. The Homebrew `ki` 0.13.0 on `PATH` is checkpoint-unaware and could trigger it. The error message and `docs/guides/user/background-agents.md#recover-event-evidence` give only "preserve both copies for an explicit coordinator recovery decision" and do not name the set-aside route.

N2, provisional legacy classification is frozen, `src/core/agent/events.ts:609` and `:635`. An uncorroborated legacy `failed` or `blocked` event is classified `terminal: false`. At the next verified append that classification is written into the checkpoint, so it is provisional only until the first publish. Later reads re-derive an outcome only for the current attempt. Old runs never lose a completion, but an older attempt's outcome can stay non-terminal.

N3, reconstructed launches read as legacy, `src/core/agent/events.ts:166` with the receipt reconstruction at `:937`/`:960`. A launch rebuilt from a control receipt can carry no `terminal` field, so `legacyAttempt` treats that attempt as legacy and `verifyLegacyHistory` (`:197`) skips it. This is cosmetic in practice; no real-state run was affected.

N4, containment observation, receivers. No receiver write in `ki-principal` or `acquire` is later than 12:00 BST today, apart from the coordinator's own brief and `decisions.md` (16:16 and 16:17). An earlier burst at 11:09–11:10 BST did write to receivers. It overwrote nine tracked `ki-principal` `+/_WORK/ki.baseline-rollout/*.report.md` files with their live agent-state copies (byte-identical to `~/.local/state/ki/agents/baseline-rollout/`), and it added untracked report copies across threads, including three in `acquire` `+/_WORK/kb.regular.acquire-intake/`. That burst falls between `a7c80cd8` and `22e0ea9c`. It coincides with `wow-rev-principal-final-4` ending and `wow-principal-repair-7` launching. I could not attribute it to this range's verification without reading earlier reports, which the brief forbids.

N5, admission topology. Primary `main` `6c4d2a1a` is not an ancestor of `0fd85a08`; both fork from `7eb0f017`. The admission is therefore a guarded branch move, not a fast-forward. Branch `wow-day-impl-fix-5` (`eb0e8b2e`, the pre-rebase twin of `4cd0ab87`) sits on `6c4d2a1a` and will be left off `main`.

**Item outcomes.**

1 Legacy compatibility: PASS. Upgraded copies read every run that `51725e8b` reads, except the mixed-version case N1. 2 Evidence preservation: PASS. Interrupted control operations, concurrent checkpoint adoption under the event lease (`:375`), snapshot loss, and milestone, failed and blocked provenance are each covered and pass. 3 Release workflow history: PASS. The CI `build` job and the release `validate` and `package` jobs check out with `fetch-depth: 0`, and `agent-upgrade-workflows.test.ts` enforces it for every job that runs the suite or the audit. 4 Regressions: PASS. With the `0fd85a08` tests on `3a3407e0`, 24 targeted tests fail for genuine reasons, and all of them pass on `0fd85a08`. 6 Real-state compatibility: PASS. `51725e8b` reads 17/17 runs, and `0fd85a08` reads 17/17 on two passes. Base-then-new on the same copy reads 16/17, the exception being N1. 7 Containment: PASS for writes since 12:00 BST. The 11:09 BST burst is unattributed; see N4 and Q2. 8 Representation: PASS. `6c498f3a` has the same patch-id as `805e4d36`; `6c4d2a1a` matches `b2d8e795` apart from the documented conflict resolution.

**Gates on `0fd85a08`.**

Full suite with coverage: PASS. 96 files and 2143 tests; statements, branches, functions and lines all at 100%. TypeScript: PASS. Biome: PASS. Build: PASS. The compiled binary reports 0.13.0. Pinned audit (KI `v0.12.0`, Harness `f4d6c521`, `KI_REPO_OFFLINE=1`): PASS. FAIL=0 with 18 skills passing and 4 at WARN (8 advisory findings); the run used the `tooling/boundaries` layout, so the depcruise path caveat did not arise.

## In Progress

Nothing. Temporary worktrees and copies are removed, and the temp directory is empty.

## Queries

**Q1 Admit `0fd85a08` to the primary's `main`**

**Context.** No blocking finding and every gate passes. The primary at `/Users/krisbrown/workspaces/knowledge-islands/tools-ki` is on `main` at `6c4d2a1aeabdac5ce5ca2e4bd711908d043afcf3` with a clean tree. Both of its local fixes are represented in the range, and `origin/main` `51725e8b` is an ancestor of the candidate. Plan: check that `git symbolic-ref HEAD` is `refs/heads/main`, that `git rev-parse HEAD` equals the old id and that `git status --porcelain` is empty. Then run `git update-ref -m "admit wow-toolski-integrate" refs/heads/main 0fd85a0895d4f0b68937f092dd30aa0bc98f8c18 6c4d2a1aeabdac5ce5ca2e4bd711908d043afcf3`, which fails if `main` has moved, followed by `git read-tree -u -m 6c4d2a1a 0fd85a08` to bring the index and tree along. Confirm with `git status` and `ki --version`. Restore path: the same compare-and-swap in reverse.

**Query.** Approve the guarded move of the primary's `main` from `6c4d2a1a` to `0fd85a08`?

**Options.** a) (recommended, confidence medium - all gates pass and the only refusal is pre-existing and recoverable) Approve the compare-and-swap as planned, with `f4ce77b8` still held. b) Hold admission until N1 is fixed in the range. c) Refuse.

**Q2 The 11:09 BST receiver writes**

**Context.** Nine tracked `ki.baseline-rollout` reports in `ki-principal` were overwritten with their live agent-state copies, and untracked report copies appeared in `ki-principal` and `acquire`. I left everything untouched, as the brief requires.

**Query.** Should the owner of the 11:09 BST activity be identified, and the nine tracked files restored with `git restore`, before admission?

**Options.** a) (recommended, confidence medium - the writes predate the final range commits and do not affect the code verdict) Admit independently, and route attribution and restoration to the principal thread. b) Attribute and restore first, then admit.

**Q3 Follow-up for N1**

**Context.** Only `ways-of-working` has a v2 checkpoint today, and its journal currently equals that checkpoint. A checkpoint-unaware `ki`, such as Homebrew 0.13.0, would make the next candidate read refuse until `events.history` is set aside.

**Query.** How should the mixed-version extension case be handled?

**Options.** a) (recommended, confidence medium - a strict valid suffix is not a contradiction) Record follow-up work to adopt a valid suffix beyond the checkpoint, and meanwhile document the set-aside route in `#recover-event-evidence`. b) Document the set-aside route only. c) Leave it as is.
