# [Model](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md>) › [Ways of working](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md>) › wow-principal-repair-6
**🤖 → 👤 Handoff to supervisor · Run report at 10:49 BST · last mark 08:24 BST**
---

## Done

PASS - New F `7200dd9baf86784f74e64331d131174b15611d75`, committed locally on `repair-wow-principal` on `sol.local`; only the three authorised `messages.md` files changed.

PASS 1 - P `f2778b861f56d4ae17e0de0e6ff71d1ec0c9a40d` and origin `868c67213623b1d91e842f188b7ddf13c7dbd0c1` are ancestors of F; both read-only fetches found origin unchanged.

PASS 2 - All 2,980 original reachable commits rehash exactly, all original reachable objects remain reachable, and all 127 original/replay pairs retain author headers and complete message/trailer bytes.

PASS 3 - The four rejected pending queue records are restored verbatim, once each, in source order; every touched queue matches its expected bytes line-for-line, including the single appended Chez-moi owner message.

PASS 3a - APP044-STALE and BRG004-NEAR use origin source lines 10 and 11, last queue revision `e666ab051b2c2263da4642acfe3cd1377571d43f`; both also match the pinned origin snapshot exactly.

PASS 3b - OPS009-SPLIT explicit-outcomes and complete-project/no-op use origin source lines 22 and 24, last queue revision `ee440eef1a1e37f646aa5ed1dbed70caf3723e52`; both match the pinned origin snapshot exactly.

PASS 3c - All 14 affected queues retain pending instructions and source order; 193 source-history commits were checked, with no genuinely consumed instruction resurrected.

PASS 3d - All 17 earlier exact-line repairs remain once each; the four new repairs bring the original-for-summary substitutions to 21, all traced to `06f3d893`, rather than owner consumption.

PASS 3e - All 29 territory-queue occurrences, including its pre-existing duplicate, remain; agent-host retains DRAIN and AUDIT-OUTSIDE-LANE; consumed Ways working CLI-156-POLICY, AUDIT-OUTSIDE-LANE and DEPCRUISE-PATH remain absent.

PASS 4a - All 14 state files parse as YAML with unique keys and coherent UTC timestamps; the four reviewed state files remain byte-identical to the starting candidate. Portable-specifications retains its pre-existing minute-precision timestamps.

FAIL 4b - The reviewed Chez-moi state still violates the closed schema: top-level `reason` and `release` are outside it and the required `hold` mapping is absent. The same fault exists in owner commit `b7c34fab`; retaining that state byte-for-byte was an explicit requirement.

PASS 4c - Chez-moi state is byte-identical to `b7c34fab`; one CHEZMOI-HOLD-SCHEMA line was appended to its queue, naming the fault and asking its owner to fix it without changing the intended hold or timestamps.

FAIL 4d - A wider scan also finds pre-existing closed-schema faults in ki, ki.agent-host, ki.baseline-rollout, ki.mac-studio-setup, ki.portable-specifications and ki.timelines; all six state files are byte-identical to the starting candidate and were left outside this repair.

PASS 5 - All 17 origin decision differences are deliberate owner-work mark outcomes: 15 strikes and two pointer rewrites. No block was lost only through the merge, so no struck material was restored.

PASS 5a - All 80 primary decision blocks remain; both source sides' added decision lines remain verbatim; Work Process remains byte-identical to P.

PASS 5b - All four decision logs remain byte-identical to the starting candidate, preserving repair-5's three moves and all block bytes; time-order checks pass for Chez-moi (91 blocks), Observatory (25), Portable specifications (9) and Ways working (80), including partial-time and date-only headings.

PASS 6 - Every actual parent change in all 265 unpublished ancestors was inspected: 621 path/mode changes across 73 paths, ordinary non-executable Markdown only; no code, configuration, binary or symlink change.

PASS 6a - Changed paths and tracked Markdown have no conflict markers; the sole repository-wide marker example remains the unchanged vendored Obsidian Git file, identical in P, origin and F.

PASS 7 - Offline KB audit with `KI_REPO_OFFLINE=1` ran Activities, Live Artifacts and Streams prerequisites; origin has FAIL=0/WARN=6 and F has FAIL=0/WARN=5, with no added structured finding.

PASS 7a - The complete unresolved-link lists were independently recomputed, including the eight hidden by abbreviated audit output: all 18 match exactly, with zero ambiguous links.

PASS 8 - Primary main remains P, its index remains unchanged, and its only tracked working change is appended Ways working decisions text; the integration index is empty and its working tree is clean.

PASS 8a - Neither checkout has a merge, rebase, cherry-pick, revert or index lock in progress; all 16,372 primary untracked and ignored paths are collision-free under exact, file/directory, NFC, NFD and case-insensitive comparisons.

PASS 9 - An offline guarded fast-forward rehearsal advanced a scratch primary to F and preserved all 16,372 untracked/ignored leaves, modes and symlink targets, plus the exact 10,365-byte primary decisions suffix; an injected extra tracked edit was correctly refused.

PASS 9a - The rehearsal used a compare-and-swap update of a local scratch origin ref and a local fetch; live origin and primary were not updated. The later live-primary snapshot remains within the permitted append-only bound.

PASS - Normal pre-commit and commit-message hooks completed with offline operation, without bypass; the ending co-author trailer names GPT-6, the runtime model identity available to this run.

PASS - Post-hook `git show --name-status HEAD` confirms only Chez-moi, Observatory and Tools burndown queues were committed; no state, decision log, work record, acceptance or pruning change was made.

### Classification of the 17 origin blocks

For every entry below, the exact origin block equals the parent-side block at the cited mark commit, and the committed mark result equals both P and F. The complete P and origin file histories were searched; none of these removals occurs on origin's history. Later receive and mark commits, including `84550579`, preserve these outcomes. The mark rule expressly permits a struck entry to leave no stub and a live decision to become a pointer.

Evidence A: `b7af7215af195c15d0e9efa948bbc810111f0ba3`, parent `ef0b1000`, “tidy decisions at the afternoon mark”.

Evidence B: `ec5db3c0db110b04b7303bdac3c8c05a54179115`, parent `0de498a9`, “ki.ways-of-working mark, prune and strike”; its message explicitly describes four completed strikes and one live pointer reduction.

Evidence C: `3577bbe19dc3e46863191d5857d5f3734984cd48`, parent `77fe5ab1`, “ki.ways-of-working mark, prune and strike”; its message explicitly describes completed strikes and live pointer reductions.

1. 14 October, thread-model owner words - deliberate strike, `b7af7215`; keep the mark result.
2. 19 October, CAPTURE-GATE - deliberate strike, `b7af7215`; keep the mark result.
3. 19 October 23:22, PUSH-NOT-WITH-YOU - deliberate strike, `b7af7215`; keep the mark result.
4. 20 October 03:34, HANDOFF-AS-MESSAGE / NET-DOWN / WIP-CAP - deliberate strike, `b7af7215`; keep the mark result.
5. 20 October, acceptance grant - deliberate strike, `3577bbe1`; keep the mark result.
6. 20 October 09:27, send to owner - deliberate strike, `b7af7215`; keep the mark result.
7. 20 October 22:03, self-serve burndown - deliberate rewrite to the surviving live-authority pointer, `ec5db3c0`; keep the mark result.
8. 20 October 23:05, send to owner - deliberate strike, `b7af7215`; keep the mark result.
9. 20 October 23:13, first query sign-offs - deliberate strike, `3577bbe1`; keep the mark result.
10. 20 October 23:16, first query-sign-off batch - deliberate strike, `3577bbe1`; keep the mark result.
11. 20 October 23:29, TOOLS-KI-SHAPES harness message - deliberate strike, `ec5db3c0`; keep the mark result.
12. 20 October 23:42, GOV-225 baseline evidence - deliberate strike, `ec5db3c0`; keep the mark result.
13. 21 October 00:00, GOV-225 third acceptance - deliberate strike, `ec5db3c0`; keep the mark result.
14. 21 October 00:05, Chez-moi harness hold - deliberate strike, `b7af7215`; keep the mark result.
15. 21 October 00:10, Chez-moi harness released - deliberate strike, `b7af7215`; keep the mark result.
16. 21 October 00:14, overnight tools/MCP/apps queries - deliberate strike, `b7af7215`; keep the mark result.
17. 21 October 01:40, overnight answers and mark - deliberate rewrite to the surviving live-authority pointer, `3577bbe1`; keep the mark result.

Durable verification evidence: [repair-6-evidence](</Users/krisbrown/.local/state/ki/worktrees/ki-principal-integrate/.git/repair-6-evidence>), including the 17 exact parent/result comparisons in [history.json](</Users/krisbrown/.local/state/ki/worktrees/ki-principal-integrate/.git/repair-6-evidence/history.json>), final checks, queue provenance, raw-history scope, full audit/link findings and rehearsal receipt.

## In Progress

Nothing running. Chez-moi's owner correction remains queued. The inherited schema faults remain outside the authorised state-preserving repair; the new candidate is ready for the supervisor's independent review.

## Queries

None. The explicit no-push integration bound governed this run; no publication approval is requested here.

### 🤖 → 👤 Handoff to supervisor · since 10:49 BST

🤖 0 running · 👤 1 you · ⛔ 0 blocked

- [with you] Independent review of candidate F and inherited owner-state faults · supervisor · since 10:49 BST

🧵 Coordination thread · KI > Model > Ways working (ki.ways-of-working)
