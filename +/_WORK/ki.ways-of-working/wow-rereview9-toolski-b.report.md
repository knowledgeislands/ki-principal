VERDICT: ACCEPT · confidence medium - 0fd85a08 reads every run 51725e8b reads, keeps every completion and passes every gate; one mixed-version refusal remains, the same one the current primary has, and the admission plan below contains it

# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-rereview9-toolski-b

**🤖 → 👤 Handoff to supervisor · Run report at 00:21 BST · last mark 23:06 BST**

---

## Done

Blind review of tools-ki `51725e8b..0fd85a08`; the held depcruise commit `f4ce77b8` was read only as context. No commits, no record changes, no network.

### Urgent, outside the candidate

**The tools-ki primary is stuck halfway through a rebase.** At 23:54:49 BST, another session ran `git pull --rebase` in `/Users/krisbrown/workspaces/knowledge-islands/tools-ki`, replaying `6c498f3a` and `6c4d2a1a` onto `origin/main` `51725e8b`. This review did not start it.
- The rebase stopped in a conflict. HEAD is detached at `60948441`, and `main` is still `6c4d2a1a`.
- 16 paths are staged or conflicted. `src/core/agent/events.ts` contains conflict markers.
- `~/.local/bin/ki` is the local runner over the primary's source. So any fresh `ki` process that loads the agent event code will probably fail until the rebase is resolved. Dispatcher 86188 is unaffected only because it loaded its code on 21 October.
- I left it untouched. Query PRIMARY-REBASE asks who resolves it.

### Blocking findings

None.

### Non-blocking findings

1. **An append by an older reader after a checkpoint is refused until someone recovers it by hand.** At `src/core/agent/events.ts:296-303`, a journal that is longer than `events.history` is refused with "journal differs from committed history". That applies even when the extra bytes are a valid suffix written by a checkpoint-unaware reader (51725e8b, the live dispatcher's code, or Homebrew `ki` 0.13.0).
   - **Reproduction:** in a sandbox, the candidate runs `ki agent launch`, which writes a v2 checkpoint. The 51725e8b CLI then runs `ki agent status r`, which appends an event. After that, candidate `status`, `wait --next` and `close` all exit 1 with `events-evidence-unverified`, for both the milestone and the done worker.
   - **Recovery:** moving `events.history` aside restores reading. The older reader's `done` is kept and `wait` returns done. So nothing is lost and the refusal is recoverable.
   - **Gap:** `docs/guides/user/background-agents.md:80` only says to "preserve both copies for an explicit coordinator recovery decision" and gives no procedure.
   - **Why it does not block:** the current primary `6c4d2a1a` refuses the same case more strictly (it needs an exact match), and the live ways-of-working state already carries a v2 checkpoint. Admission therefore adds no exposure. Query TOOLS-MIXED-WRITER below covers it.
2. **The candidate journals what was only implied before, and drops one duplicated query.** In the real-state copy, 0fd85a08 appended terminal `failed: no report` events for seven runs whose old journals already held an untagged `failed no report`:
   - `seat-change`, `diagram-fix`, `away-housekeeping`, `threads-stock` and `pilot-seed` in state-of-play;
   - `migrate-phase2b` and `migrate-apply` in ways-of-working.

   It also did not re-raise `RIG-MANAGERS` for `mac-studio-setup/triage-review`. 51725e8b re-raised that query with altered link text, although it is already at seq 49. Rendered status was byte-identical between the two versions for every team, and no completion changed.
3. **ki-principal has one untracked file:** `+/_WORK/ki.ways-of-working/briefs/wow-rereview9-toolski.md`, written at 23:09. It is the brief for this review, not an agent-report copy. My read-only `git status` calls updated the `.git` directory mtime in ki-principal and acquire. No working file changed.

### Gates

- Legacy compatibility (gate 1): PASS. 17/17 runs and `--all` were read by both versions on both passes. Every old completion was kept. The only refusal is the mixed-version case in finding 1, which has a recovery route.
- Evidence preservation (gate 2): PASS. The concurrent checkpoint adoption, snapshot loss and later-attempt snapshot tests pass, and provenance holds across milestone, failed and blocked progress.
- Release workflow history (gate 3): PASS. `release.yml`'s validate and package jobs, and ci.yml's build job, use `fetch-depth: 0`. Package runs the suite and build runs the audit. Publish and verify-release-install run neither.
- Regressions (gate 4): PASS. 28 of 0fd85a08's new or changed tests fail on 3a3407e0, and the same filter passes on 0fd85a08 (103 tests).
- Full suite with coverage (gate 5): PASS, 2143 tests in 96 files.
- TypeScript (gate 5): PASS.
- Biome (gate 5): PASS.
- Build (gate 5): PASS.
- `KI_REPO_OFFLINE=1 ki repo audit`, KI v0.12.0 with Harness f4d6c521, from a local checkout (gate 5): PASS, FAIL=0. The 8 warnings come only from the isolated registry: no ki-principal or territory registration exists there. Repair also passed in the isolated homes.
- Real-state compatibility (gate 6): PASS. Report homes and the registry were mirrored under $TMPDIR, and writes outside $T were denied by sandbox. Both versions read the same run count. No file outside $TMPDIR changed beyond the `.git` mtimes noted above.
- Containment (gate 7): PASS. acquire is clean. ki-principal holds only the brief file in finding 3, and neither repository has an untracked report copy.
- Primary fixes represented (gate 8): PASS.
  - `6c498f3a` has the same patch-id as `805e4d36`.
  - `6c4d2a1a`'s change is contained in `b2d8e795`.
  - The swap is not a fast-forward (merge-base `7eb0f017`).

## In Progress

Nothing. Removed my temporary worktrees, including their registrations in the tools-ki primary and the Harness checkout. Scratch files remain under $TMPDIR.

## Queries

**PRIMARY-REBASE**

**Context:** The tools-ki primary has been mid-rebase since 23:54:49 BST, with conflict markers in `src/core/agent/events.ts`. `main` still points at `6c4d2a1a`, so nothing committed is lost. A rebase onto `origin/main` here was already aborted once, on 22 October at 02:00. Both local fixes are represented in `0fd85a08`.

**Query:** Who clears the half-finished rebase, and how?

**Options:**
a) (recommended, confidence high - returns the live runner to committed code with nothing lost) The session that started it, or the coordinator with your approval, runs `git -C /Users/krisbrown/workspaces/knowledge-islands/tools-ki rebase --abort`. Then confirm the primary is on `main` at `6c4d2a1a` with a clean tree before TOOLS-ADMIT-9.
b) Resolve the conflicts by hand and finish the rebase. Not advised: that work duplicates what `0fd85a08` already contains.
c) Leave it until admission, with `ki` broken in the meantime.

**TOOLS-ADMIT-9**

**Context:** 0fd85a08 passes every gate. The primary `main` sits at `6c4d2a1a`, and both of its local fixes are represented in the range. The swap is not a fast-forward. Dispatcher pid 86188 has run the primary's source since 21 October at 01:56 with older, checkpoint-unaware code loaded in memory. It is idle and its queue is empty.

**Query:** How should the primary move to `0fd85a08`?

**Options:**
a) (recommended, confidence medium - the guard and quiet point remove both the race and the mixed-writer exposure) Once PRIMARY-REBASE is cleared, wait for a quiet point with no queued or launching run. Stop dispatcher 86188. Confirm the primary is on `main` with a clean tree, then run `git -C <tools-ki primary> update-ref refs/heads/main 0fd85a08 6c4d2a1aeabdac5ce5ca2e4bd711908d043afcf3`, which refuses if `main` has moved. Then run `git -C <tools-ki primary> read-tree -q -m -u 6c4d2a1a 0fd85a08`, which brings the tree up to the new commit and refuses rather than overwrite a local change. Restart the dispatcher from the primary, and confirm `ki agent status` reads ways-of-working.
b) Swap at once and leave the dispatcher running; its next launch writes with old code until it is restarted.
c) Hold admission until finding 1 is fixed.

**TOOLS-MIXED-WRITER**

**Context:** A checkpoint-aware CLI (`6c4d2a1a` today, `0fd85a08` after admission) refuses a run once any checkpoint-unaware `ki` appends to it. That covers 51725e8b-era code, the running dispatcher and Homebrew `/opt/homebrew/bin/ki` 0.13.0. Moving `events.history` aside recovers the run with nothing lost, but no guide says so.

**Query:** How should mixed writers be handled after admission?

**Options:**
a) (recommended, confidence medium - it closes the gap without weakening digest checks) Record follow-up work in tools-ki to accept a well-formed legacy suffix that contains no checkpoint marker, and to document the move-aside recovery in the background-agents guide. Until then, run only the primary's `ki` on live state.
b) Only document the recovery step.
c) Accept the refusal as designed.

### 🤖 → 👤 Handoff to supervisor · since 00:21 BST

👤 3 with you

- [with you] PRIMARY-REBASE · owner · since 00:21 BST
- [with you] TOOLS-ADMIT-9 · owner · since 00:21 BST
- [with you] TOOLS-MIXED-WRITER · owner · since 00:21 BST

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
