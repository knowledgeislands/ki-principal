VERDICT: REFUSE · confidence high - 22e0ea9c turns the commonest legacy outcome, a worker that exited without DONE, into a permanent refusal that blocks a copy of the live ways-of-working run, and the offline audit fails on 3a3407e0 without the held-back d4849813

# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/work.md) › wow-rereview7-toolski-b

**🤖 → 👤 Handoff to supervisor · Run report at 14:26 BST · last mark 14:26 BST · blocked**

---

## Done

Reviewed `51725e8b..3a3407e0` blind. I made no commits and changed nothing in the supplied worktree, the tools-ki primary or any remote. All runs used detached worktrees and copied state under `$TMPDIR`.

### Blocking findings

**B1. Legacy `exited without DONE` outcomes are refused permanently (regression introduced in 22e0ea9c).** In `src/core/agent/events.ts:601-627`, `classifyLegacyFailures` counts a legacy launcher-wording event as terminal only when one of three things corroborates it: a `failed` or `done` attempt in control history, a `no report` with `DONE` and no report file, or a matching queue cancellation. The baseline launcher wrote `failed: exited without DONE (<status line>)` with no `terminal` field whenever a worker died without `DONE`. Such an attempt has no later events, its status file holds an ordinary line such as `12:16 UTC - launched` (the very line embedded in the event), and the baseline left no history state. The classifier therefore throws `ambiguous legacy failure`. That error refuses `status`, `wait --next`, `launch --relaunch`, `stop` and `close` across the whole run. The recovery section of `docs/guides/user/background-agents.md` says to recover the original status or receipt evidence, but none exists for a crash, so there is no recovery route. a7c80cd8 accepted the same state.

- **Reproduction 1 (CLI, through the suite's own `baselineCli` and `fixture`).** Launch with the 51725e8b CLI. Make the worker exit (`f.set({ empty: true })`) without writing `DONE`. Run the old `ki agent status r`; it journals `[1,failed,"exited without DONE (… - launched)"]`. Then run the new `ki agent status r`. Result: exit 1 with `ambiguous legacy failure at sequence 2`, managed and unmanaged, with or without the snapshot. `wait`, `launch --relaunch`, `stop` and `close` all exit 1 with the same error. On a7c80cd8 the same probe exits 0 (`EXITED WITHOUT DONE`), and wait, relaunch and stop succeed.
- **Reproduction 2 (real state, read-only copy).** I copied `~/.local/state/ki/agents/ways-of-working`, the live coordinating run, into `$TMPDIR` and called 3a3407e0's `readEvents` on it. It refuses at sequence 421: `gov194-refresh`, `exited without DONE (10:52 BST - DONE)`. Sequences 765, 778 and 1453 have the same shape. a7c80cd8 replays all 2351 events. Its `events.history` is already v2 with no `failures` entries, so nothing earlier classified these events. Installing 3a3407e0 would therefore brick the coordinating run.
- The new test `sixth-review ambiguous baseline failed exited without DONE (no status)` asserts refusal only after the status file is removed. Nothing tests the genuine crash, where the status file is still present.

**B2. Offline audit fails on the admission tip.** `KI_REPO_OFFLINE=1 ki repo audit` on 3a3407e0 fails DESIGN-2 (`.dependency-cruiser.ts`): the root `prepare` script must install `tooling/depcruise`, and 3a3407e0 still installs `tooling/boundaries`. The held-back d4849813 makes exactly that rename. Admitting 3a3407e0 without it fails the brief's own audit gate, and CI's `ki repo audit` step would presumably fail too. The same offline audit on d4849813 passes: PASS=17, WARN=5, FAIL=0.

**B3. Pre-event snapshots refuse permanently (introduced in the range by b2d8e795, already on primary `main` as 6c4d2a1a).** At `src/core/agent/events.ts:189-196`, `verifyLegacyHistory` throws `journal has lost an observed terminal outcome` when a v1 snapshot marks an attempt `ended` but its journal holds only non-terminal events. The baseline seeded `ended: true` for agents that had finished before events existed, so such runs are ordinary. Reproduction: a read-only copy of the live `~/.local/state/ki/agents/mac-studio-setup` refuses on both a7c80cd8 and 3a3407e0. There, agent `rig-lane` has a snapshot with `ended: true` and only a `needs-owner` event in the journal. This is not a regression against the primary's present `main`, but it breaches criterion 1, and admission would carry it towards `origin/main`, which (51725e8b) lacks it.

### Non-blocking findings

- **N1. Duplicate notification after snapshot loss.** When a legacy journal loses its snapshot, the unchanged status line is published again. Legacy `progress` events carry no `statusLine`, so `readSnapshot` cannot restore `seen.line`. Probe: a baseline `no report` run, snapshot removed, then the new `status` appends a second `[1,progress,"working"]`. a7c80cd8 behaves the same. This contradicts the guide's "without repeating notifications".
- **N2. Narrow workflow guard.** `src/tests/cli/agent-upgrade-workflows.test.ts` detects suite jobs only by the literal text `bun run test` or `ki repo audit`. A step such as `bunx vitest` or `mise run test` would escape the check.
- **N3. Upgrade tests depend on Git history.** `baselineCli` rebuilds the 51725e8b CLI for every case, and it needs 51725e8b in local history; a shallow clone fails with a `git archive` error instead of a clear skip.
- **N4. Admission plan is a non-fast-forward.** 6c4d2a1a is not an ancestor of 3a3407e0; the two diverge at 7eb0f017, so the guarded swap is a non-fast-forward rewrite of the primary's `main`. Both local fixes are represented. 6c498f3a ≡ 805e4d36 (identical stable patch-id). For 6c4d2a1a ≈ b2d8e795, the range-diff shows only the trailer and the documented `homeReport` conflict resolution, and the tree delta between them equals 51725e8b's own change. The plan is sound once B1 to B3 are settled.

### Criteria

1. Legacy replay: FAIL (B1, B3). The probes of failed-then-relaunched workers, `no report`, worker `failed:` progress and later status all passed.
2. Evidence preservation: the fault matrices pass. N1 is the only gap found.
3. Release workflow: PASS. `validate` and every `package` job check out with `fetch-depth: 0`, `publish` runs no suite, and the CI `build` job (suite via audit) has `fetch-depth: 0`.
4. Regressions: PASS. Grafting 3a3407e0's tests onto a7c80cd8 gives 32 failures among the new legacy and upgrade tests plus the workflow test, all of which pass on 3a3407e0.
5. Gates: one-line results are below.
6. Admission plan: representation confirmed (N4), but the admission should not proceed.

### Gates on 3a3407e0

- PASS — full suite: 96 files, 2127 tests.
- PASS — TypeScript (`tsc --noEmit`).
- PASS — Biome (`biome check .`).
- PASS — build (`bun run build`).
- FAIL — `KI_REPO_OFFLINE=1 ki repo audit`: PASS=17, WARN=4, FAIL=1; the failure is DESIGN-2 (B2). The same audit on d4849813 passes.

## In Progress

Nothing. Temporary worktrees and copies have been removed. While I was reviewing, another session left uncommitted edits in the supplied worktree (`events.ts`, `background-agents.md`, `agent-control-recovery.test.ts`). They are not mine and I left them alone; this verdict covers only the committed `3a3407e0`.

## Queries

### ADMIT-7 - How should the tools-ki admission proceed?

**Context** B1 is a regression introduced in this range that bricks a copy of the live coordinating run. B2 means the admission tip fails the audit unless d4849813 is included. B3 is already on the primary's `main`.

**Query** Should the candidate go back for a fix, or be admitted in some other form?

**Options**
a) (recommended, confidence high - B1 would block the live ways-of-working run on install) Return to the fixer. Corroborate legacy `exited without DONE (<line>)` against the retained status line or liveness, and seed pre-event `ended` snapshots as terminal rather than refusing them. Add regressions built from a copied real-state fixture covering B1 and B3. Admit with d4849813 included.
b) Admit 3a3407e0 plus d4849813 now and fix B1 and B3 before the next install. This risks any session running primary `main` refusing the coordinating run.
c) Admit a7c80cd8 plus d4849813 instead. That avoids B1 but reintroduces the completion losses that 22e0ea9c fixes.
