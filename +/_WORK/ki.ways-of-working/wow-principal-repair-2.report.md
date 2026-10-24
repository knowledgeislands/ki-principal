# [Model](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md>) › [Ways of working](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md>) › wow-principal-repair-2

**🤖 → 👤 Handoff to supervisor · blocked · Run report at 09:23 BST · last mark 08:24 BST**

---

## Done

- PASS - Captured fresh primary P = `f2778b861f56d4ae17e0de0e6ff71d1ec0c9a40d` on `main`, initially with no tracked changes; captured 462 untracked paths and fetched P into `review-primary-snapshot-2` in the integration clone.
- PASS - Primary resolution: merged P with `--no-ff`; local commit `bce02d0e1942d5ff05d993fd34f01a869c4e9afd` preserves its new Ways of working decision entry without conflict. Retained provisional F = `bce02d0e1942d5ff05d993fd34f01a869c4e9afd`; this is not a qualified final candidate.
- PASS - Commit checks: Conventional Commit, GPT-6 co-author trailer, normal pre-commit and commit-message hooks, no bypass; explicit-path inspection confirms the only changed path is `+/_WORK/ki.ways-of-working/decisions.md`.
- PASS - Fetched live origin O = `868c67213623b1d91e842f188b7ddf13c7dbd0c1`, meeting the required `868c6721` baseline.
- FAIL - Primary stability: P stayed unchanged and the tracked decisions edit remained append-only, but two new untracked reports appeared outside the permitted briefs area: `+/_WORK/ki.ways-of-working/wow-replan6-ele001.report.md` and `+/_WORK/ki.ways-of-working/wow-rereview5-c.report.md`. Brief creation/deletion was permitted and did not cause the stop.
- FAIL - Live-origin resolution: its uncommitted merge conflicted in `+/_WORK/ki.agent-host/messages.md` and `+/_WORK/ki.chezmoi/state.md`; the stability gate stopped reconciliation before any manual resolution or staging. Saved the incoming merge evidence and aborted only this run's unfinished merge.
- FAIL - Queue resolution: retaining the incoming agent-host DRAIN line beside the local AUDIT-OUTSIDE-LANE line, and retaining all four new Ways of working messages, remains pending; none was committed or consumed by this run.
- FAIL - Decisions-log resolution against live origin: its later Chez-moi entries remain pending integration; no union or chronological rewrite was committed. The completed primary merge preserves P's decision history.
- FAIL - Chez-moi state resolution: live origin has the later whole `b7c34fab` snapshot, `state: on-hold`, `since` and `mark` both `2026-10-22T07:51:00Z`, with nothing running and six parked queries. Selection and the PRINCIPAL-STATE-RESOLUTION update were not applied after the stop; F retains the earlier repaired snapshot and notice.
- PASS - Retained-F ancestry: all 127 original commits and all 127 replay counterparts are ancestors; author records and full messages/trailers match each mapped pair.
- PASS - P is an ancestor of retained F, and P's Work Process content is preserved byte-for-byte.
- FAIL - Live origin O is not an ancestor of retained F; final-candidate qualification therefore fails.
- PASS - Consumed-message removal: CLI-156-POLICY, AUDIT-OUTSIDE-LANE and DEPCRUISE-PATH remain absent from the Ways of working queue.
- PASS - Conflict-marker check: all paths changed against origin are clear; repository-wide matches are unchanged vendor examples in `.obsidian/plugins/obsidian-git/main.js`, with an identical blob in P, origin and F.
- FAIL - Fresh KB audits and the no-added-finding comparison against live origin were not run after the stability stop. The earlier run's audit is not claimed as renewed verification.
- PASS - Final collision check for retained F: its one added path collides with none of the primary's 462 current untracked paths, including file/directory, Unicode-normalised and case-insensitive comparisons.
- PASS - Integration clone is clean at retained F with no active merge. Primary was read only; no work record was accepted, pruned or deleted, and nothing was pushed. The task-specific no-publication bound governed the conflicting generic push footer.

## In Progress

Nothing running. Completion is blocked on the primary stability boundary. The primary merge is preserved locally on `repair-wow-principal`; live-origin reconciliation, fresh KB audits and final qualification remain unfinished.

Outstanding - no action requested now: repair evidence, conflict stages, hook log, blocker fingerprints and retained-candidate checks are preserved in [repair-2-evidence](</Users/krisbrown/.local/state/ki/worktrees/ki-principal-integrate/.git/repair-2-evidence>). The task temporary directory is empty. Repository `ki-principal`, machine running this integration clone, branch `repair-wow-principal` retains this run's local merge commit for the next authorised integration session.

## Queries

### PRIMARY-STABILITY

**Context**: the brief permits append-only changes to the primary's Ways of working decisions log and creation/deletion under its briefs folder. Two coordinator report creations fell outside that allowance. P did not move, and this run neither wrote to nor altered those primary files.

**Query**: Should completion resume with coordinator-created report files explicitly included in the stability allowance, or wait for a window without such writes?

**Options**:

a) (recommended, confidence high - preserves active coordination while keeping the primary read only and retaining collision checks) Authorise creation of coordinator-owned `+/_WORK/ki.ways-of-working/*.report.md` files alongside the existing allowance, then resume from retained F with a fresh primary capture, live-origin reconciliation and every required check.

b) Keep the existing allowance and resume only during a primary window without report creation or other excluded changes.

### 🤖 → 👤 Handoff to supervisor · blocked · since 09:23 BST

🤖 0 running · 👤 1 with you · ⛔ 1 blocked

- [blocked] Complete live-origin integration and qualify final F under an agreed stability window · supervisor · since 09:23 BST

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
