VERDICT: ACCEPT · confidence high - every legacy, evidence, workflow, regression, gate, real-state and containment check passed; the one refusal found (an older writer extending a checkpointed journal) already exists in the primary's main, is recoverable without loss, and is contained by restarting the dispatcher as part of admission.

# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-rereview9-toolski-c

**🤖 → 👤 Handoff to supervisor · Run report at 01:10 BST · last mark 01:09 BST · blocked**

---

## Done

Blind read-only review of `51725e8b..0fd85a08` (candidate `0fd85a08`, held `f4ce77b8` out of scope). No commits made. Checks: legacy compatibility PASS, evidence preservation PASS, release workflow history PASS, regressions FAIL-then-PASS as required, tsc PASS, Biome PASS, build PASS, coverage PASS, offline audit PASS, real-state comparison PASS, containment PASS, admission plan written below. Observed at 01:08, outside the range: the primary checkout is mid-rebase with a conflict and `ki` on PATH fails to start (query below).

### Blocking findings

None.

### Non-blocking findings

1. **Journal extended by a checkpoint-unaware writer after a candidate checkpoint refuses every later read until a manual step.** `src/core/agent/events.ts` (0fd85a08) prefix check at the `journal differs from committed history` throw: once the candidate has written a v2 `events.history`, an older reader or writer (51725e8b, or the live dispatcher's in-memory code) appending one line to `events.jsonl` makes the disk journal longer than the checkpoint journal, and `status`, `wait`, `close` and `launch --relaunch` all exit 1 with `events-evidence-unverified: … journal differs from committed history` and the `#recover-event-evidence` route. Reproduction (sandbox fixture, candidate launch → old `ki agent status r` after a milestone → candidate `ki agent status r`): exit 1 on every subsequent read; the old reader still homes the report and marks the snapshot ended. Recovery: renaming `events.history` aside restores reads at once, the later `DONE` is published and the report homed, no completion lost; the candidate then re-appends a duplicate progress event for the old line (cosmetic). Judgement: not blocking. The primary's current `main` (6c4d2a1a) carries the identical check, so admission neither introduces nor widens it; the guide names the refusal and "preserve both copies" but not the concrete rename step; the only live checkpoint-unaware writer is the dispatcher below, which writes only when it dispatches, and the queue is empty.
2. **The live dispatcher runs code from before the control journal.** PID 86188 started 01:56 BST 21 Oct from `main` at `a2e3460d`, which predates `control-store.ts`, `locking.ts` and the checkpoint. It polls `queue.jsonl` only and appends events only when it dispatches a queued request, so it is inert while the queue is empty, but the first queued request would launch without control evidence and extend the `ways-of-working` journal past the committed checkpoint (finding 1) under today's `main` as much as under the candidate. Restart it as part of admission (plan below).
3. **Two earlier audit attempts were invalid through my own setup, not the range.** The first skipped CI's `ki repo repair` step and reported eight `RUNTIMES-2` activation failures (git-ignored skill links absent); the second had the repair but skipped CI's `bun install --frozen-lockfile --cwd tooling/boundaries` and failed `DESIGN-2` and `TEST-5` only on the missing `depcruise` binary, with every other criterion passing. A third run with that toolchain symlinked from another worktree failed only `DESIGN-2` ("boundary evidence escapes the repository"), with `TEST-5` and every other criterion passing. The gate reported below is the fourth run, with the toolchain copied inside the checkout as CI installs it. The offline audit also warns on `TERR-3`, `ROUTE-1` and `ITEM-2` (territory policy unavailable offline) and on `HOLD-1` (the trades hold in `.ki.toml` passed its review date 2026-10-21); `.ki.toml` is unchanged in the range, so these are standing repository findings, not admission findings.
4. **Biome reports one pre-existing style info** at `src/tests/cli/skill/generate.test.ts:68` (string concatenation); exit code 0, unchanged by the range.
5. **Admission is not a fast-forward.** The primary's `main` (6c4d2a1a) is not an ancestor of 0fd85a08 (merge-base 7eb0f017). Its two local commits 6c498f3a and 6c4d2a1a are re-authored in the range as 805e4d36 and b2d8e795; `git range-diff` shows only trailer and resolution-note differences plus the candidate keeping the `homeReports && !seen.ended` guard. Admission delta from 6c4d2a1a: 20 files, +1871/−172.

6. **The primary checkout is mid-rebase with a conflict, and `ki` on PATH cannot start.** Not caused by the range and not done by this run. At 23:54 someone began `git rebase` of `main` (orig-head 6c4d2a1a) onto `51725e8b` in `/Users/krisbrown/workspaces/knowledge-islands/tools-ki`: the first pick (6c498f3a) was re-created as `60948441`, the second (6c4d2a1a) stopped on a conflict in `src/core/agent/events.ts` (status `UU`, conflict markers at line 668), fifteen other files are staged, HEAD is detached and `refs/heads/main` still points at 6c4d2a1a. Because `ki` on PATH executes the primary's `src/main.ts`, `ki --version` and `ki agent status ways-of-working` now fail at start-up with `error: Unexpected <<` at `events.ts:668`. The dispatcher (PID 86188) is unaffected while it keeps its loaded code, but it could not relaunch, and nothing else on this machine can run `ki` until the rebase is finished or aborted. Left untouched.

### Point-by-point

1. Legacy compatibility: the candidate reads every run `51725e8b` reads (17 of 17 live runs, identical output, see 6). Sandbox reproductions against the real 51725e8b CLI: worker exited without DONE then relaunched and completed (reads 0, relaunch 0, successor done, predecessor stays failed); legacy `could not launch:` outcome then relaunch and completion (0, 0, done); repeated `failed:`/`blocked:` wording incl. launcher-like text with and without snapshot, crashed baseline run relaunch and close, pre-event seeded snapshots with later milestone/failed/blocked annotations, later-attempt snapshot not corroborating an earlier failure: all covered by the candidate's own sixteen `seventh-review` tests, which pass. Refusals occur only for the journal/checkpoint contradiction in finding 1, which has a working recovery route.
2. Evidence preservation: `finishOperation` now persists the observation in the first atomic projection and degrades receipt/journal failures to warnings for stop/dequeue/recover-resolve; `saveControl` verifies the projection after rename; `withRunLock` retains a confirmed result on unverifiable release; `read` distinguishes ENOENT from other I/O; `lostControlOperations`/`ownershipLoss` surface `blocked` without taking over locks; concurrent checkpoint adoption during a short completion append preserves the publisher's suffix (test passes, fails on 3a3407e0). Provenance across milestone, failed and blocked progress is bound by `statusLine` to the latest matching event and survives snapshot loss via the checkpoint `failures` list.
3. Release workflow: `ci.yml` `build` and `release.yml` `package` both check out with `fetch-depth: 0`; `agent-upgrade-workflows.test.ts` enforces it for every job matching `bun run test|ki repo audit`; `baselineCli` needs that history.
4. Regressions: the 16 tests added in 0fd85a08 (`agent-control.test.ts`, `agent-control-recovery.test.ts`) fail on 3a3407e0 (16 failed) and pass on 0fd85a08 (16 passed).
5. Gates on 0fd85a08: listed below.
6. Real-state compatibility: on an APFS-cloned copy of `~/.local/state/ki/agents` (8.4 GB, 17 open runs plus one archived) with every `thread.json` home (15 files) and every registry `path`/`sources` entry rewritten to temporary mirrors under `$TMPDIR`, `ki agent status <run>` exits 0 for all 17 runs with both 51725e8b and 0fd85a08, with byte-identical output; a second candidate pass is identical except for consumed inbox lines, which the baseline consumes the same way. The candidate created a v2 checkpoint for each run on first read. Nothing outside `$TMPDIR` changed: no file under `~/.local/state/ki` other than this run's own status, and the three repositories' working trees unchanged (`.git` index refresh from my own `git status` only).
7. Containment: `ki-principal` has no uncommitted tracked changes and only `+/_WORK/ki.ways-of-working/briefs/wow-rereview9-toolski.md` untracked (this run's brief, not an agent-report copy); `acquire` and `hnr-principal` clean.
8. Admission plan (owner action, not performed):
   - Preconditions: `git -C <primary> rev-parse main` = `6c4d2a1a` (true), `git -C <primary> status --porcelain` empty and HEAD on `main` (NOT true at 01:08: see the query), lockfile identical (no `bun install` needed), queue empty, no dispatch in flight.
   - Keep a restore handle: `git -C <primary> branch keep/main-6c4d2a1a 6c4d2a1a`.
   - Guarded swap: `git -C <primary> update-ref -m "admit 0fd85a08" refs/heads/main 0fd85a08 6c4d2a1a` (fails if main moved), then `git -C <primary> reset -q --hard main`. Restore path: `git -C <primary> update-ref refs/heads/main 6c4d2a1a 0fd85a08 && git -C <primary> reset -q --hard main`.
   - Timing: `ki` on PATH execs the primary's `src/main.ts` per invocation, so every new `ki` process runs 0fd85a08 immediately after the reset; in-flight processes keep their loaded code. Do the swap while no `ki agent` command of yours is mid-flight (the three review runs use temporary builds). The dispatcher (PID 86188) keeps `a2e3460d` in memory regardless; stop it right after the swap and before anything is queued, confirm `dispatch.pid` is stale, then start it again with the new code (`ki agent dispatch ways-of-working --max 3 --interval 30`). Verify with `ki --version` (0.13.0) and `ki agent status ways-of-working` exit 0.
   - `f4ce77b8` stays held.

### Gates run on 0fd85a08

- PASS tsc (`bun x tsc --noEmit`, exit 0)
- PASS Biome (`bun x biome check .`, exit 0, 1 pre-existing info)
- PASS build (`bun run build`, exit 0)
- PASS coverage (`bun run test:coverage`, exit 0, 96 files / 2143 tests, statements, branches, functions and lines 100%)
- PASS offline audit (`KI_REPO_OFFLINE=1 ki repo audit --repo .` with KI v0.12.0 and Harness f4d6c521 after `registry add`, `repo repair` and both CI install steps: exit 0, PASS=17 WARN=5 FAIL=0; warnings are standing repository findings listed under non-blocking finding 3, plus CLAUDEBIND-1, PKG-6 and CI-1 style notes unchanged by the range)
- PASS regressions (16 fail on 3a3407e0, 16 pass on 0fd85a08)
- PASS real-state read (17/17 runs on both builds, identical output, no change outside `$TMPDIR`)
- PASS containment (ki-principal, acquire, hnr-principal)

## In Progress

Nothing.

## Queries

Context: admission by compare-and-swap needs the primary on `main` with a clean tree, and the primary is instead stopped in someone's rebase of `main` onto 51725e8b with an unresolved conflict in `events.ts`; while it stays so, no new `ki` process on this machine starts. Both commits the rebase is replaying are already represented in 0fd85a08 (as 805e4d36 and b2d8e795), so the rebase adds nothing the candidate lacks.
Query: how should the primary be returned to a usable state before admission?
Options:
a) (recommended, confidence high - restores exactly the reviewed precondition and loses nothing, since the candidate already carries both commits) Whoever owns the rebase runs `git -C <primary> rebase --abort`, which puts HEAD back on `main` at 6c4d2a1a with a clean tree; then run the swap in the admission plan, which also restores `ki` on PATH.
b) Finish the rebase first, resolving `events.ts`, which moves `main` to a new, unreviewed commit; the swap's old-value guard (6c4d2a1a) would then refuse and the plan would need re-basing on the new `main`.
c) If the rebase belongs to a session still working, pause admission until that session reports.

Context: the live dispatcher predates the control journal and will corrupt the `ways-of-working` evidence the first time it dispatches, under today's `main` as much as under the candidate.
Query: should the dispatcher restart be part of the admission step?
Options:
a) (recommended, confidence high - removes the only live path to finding 1 and gives the restarted dispatcher the admitted code) Stop PID 86188 immediately after the swap, before anything is queued, and start it again with the new code.
b) Leave it running and restart only when something must be queued; nothing is lost while the queue stays empty.
