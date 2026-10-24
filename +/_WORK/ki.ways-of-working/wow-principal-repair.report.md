# [Model](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md>) › [Ways of working](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md>) › wow-principal-repair

**🤖 → 👤 Handoff to supervisor · blocked · Run report at 09:16 BST · last mark 08:24 BST**

---

## Done

- PASS - Captured clean primary `main` as P = `573faa531a0e078e58c079c58515a494c1cc9122` in the unused `review-primary-snapshot` ref; preserved `integration-original`, `integration-upstream` and the starting candidate.
- PASS - Repair commit `71a8851c4ffb166a821ff45bec38c6dc42e19b44` removes every locally consumed queue entry: CLI-156-POLICY, AUDIT-OUTSIDE-LANE and DEPCRUISE-PATH; examining all 127 original commits found no other consumed entry.
- PASS - The two origin-only arrivals present at the starting upstream, SCHED-DEBRIEF and COORD-HANDOFF-ASKS, retain their complete source lines.
- PASS - Chez-moi state selects the newer starting snapshot, `since: 2026-10-22T06:42:00Z`, committed at 08:21 BST, replaces obsolete reconciliation-running and cutover instructions, and distinguishes completed evidence from pending owner actions.
- PASS - Chez-moi's decisions retain all 91 distinct source sections from both histories, in timestamp order, including the earlier reconciliation decision and its fetch-authority entry under the correct heading.
- PASS - Appended one PRINCIPAL-STATE-RESOLUTION line to Chez-moi's messages, naming the resolution and requesting confirmation of its state and pending actions.
- PASS - Ancestry-preserving merge commit `833dd21fc47d0657a45eea241120b7f96121b2bc` has the repair and P as its two parents; the primary's later decisions and complete Work Process change are retained.
- PASS - All 127 original commit identities and all 127 replay counterparts are ancestors of the retained candidate; every original/replay message, trailer and author record still matches.
- PASS - Both new commits ran the ki-principal pre-commit and commit-message hooks, use Conventional Commits and a GPT-6 co-author trailer, and contain only the verified explicit-path changes; neither bypassed hooks.
- PASS - Before KB audits: starting origin has zero failures and five warnings; starting candidate has zero failures and four warnings, with no added finding against that origin.
- PASS - Fetched live origin in the clone: `868c67213623b1d91e842f188b7ddf13c7dbd0c1`; its 14 new commits form a continuous extension of the starting upstream and affect five work-package Markdown paths.
- PASS - Inspected the actual paths of all 259 unpublished ancestors; all are Markdown under the permitted knowledge and work areas, with no code or runtime-configuration change.
- PASS - After KB audits: live origin has zero failures and six warnings; retained candidate has zero failures and five warnings, with zero added findings against live origin. Both staged commit audits also passed.
- PASS - Final path-collision check: the retained candidate adds one path relative to P and collides with none of the primary's 456 current untracked paths, including file/directory and case-insensitive checks.
- PASS - The integration clone is clean; all repository mutations were confined to that clone. The primary was read only; no work record was accepted or pruned, and no publication was attempted.
- FAIL - Primary stability gate: `main` still equals P, but `+/_WORK/ki.ways-of-working/decisions.md` became dirty after capture and remains dirty. Four initially untracked files also disappeared outside this run's writes; the remaining captured untracked files have unchanged contents.
- FAIL - Live-origin merge and renewed queue/state reconciliation were not attempted after that stability failure; the newer origin includes additional incoming messages and a later Chez-moi state.
- FAIL - Final candidate qualification: retained provisional F = `833dd21fc47d0657a45eea241120b7f96121b2bc` contains P and all original history, but live origin is not its ancestor. F is not a completed or approved final candidate.

## In Progress

Nothing is running. The verified local repair and primary-history merge remain in ki-principal on sol, branch `repair-wow-principal`, for the supervisor's handoff. Evidence is retained in [.git/repair-evidence](</Users/krisbrown/.local/state/ki/worktrees/ki-principal-integrate/.git/repair-evidence>), including pinned refs, conflict stages, explicit commit paths, the unpublished-ancestor ledger, audits and [final checks](</Users/krisbrown/.local/state/ki/worktrees/ki-principal-integrate/.git/repair-evidence/final-checks.json>).

Outstanding - no action requested now: Chez-moi's confirmation request remains queued. Final independent review belongs after the live-origin merge and renewed verification.

## Queries

### PRIMARY-STABILITY

**Context**: The safe sequence requires the primary to remain clean at P. Its decisions log changed during this run, while live origin advanced by 14 commits. This run has no authority to alter or settle the primary's working files and stopped under the brief's stop-on-blocker rule.

**Query**: Should the supervisor settle the primary's tracked change and commission completion against a fresh stable snapshot?

**Options**:

a) (recommended, confidence high - preserves the primary owner's work and re-establishes the sequence's required clean snapshot) Settle the primary in its owning session, then resume in this integration clone: recapture its tip if changed, merge live origin, preserve newly arrived messages, select the latest coherent Chez-moi state, and repeat the final checks and independent review.

b) Retain the two verified local commits and defer the remaining integration until the primary has a stable write window.

### 🤖 → 👤 Handoff to supervisor · blocked · since 09:16 BST

🤖 0 running · 👤 1 with you · ⛔ 1 blocked

- [blocked] Re-establish primary stability and complete live-origin integration · supervisor · since 09:16 BST

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
