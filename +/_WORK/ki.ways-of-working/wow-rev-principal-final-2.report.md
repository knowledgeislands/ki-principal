VERDICT: UNSAFE · confidence high · Three inherited decision-block inversions fail the required chronological-order gate; the other publication and checkout checks pass.

# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-rev-principal-final-2

**🤖 → 👤 Handoff to supervisor · blocked · Run report at 10:04 BST · last mark 08:24 BST**

---

## Done

The failed condition is timestamp order, not an integration deletion. All three inversions already exist in the source history; this verdict applies the brief's chronological-order requirement literally.

- CHRONOLOGY-1: In [portable-specifications decisions](/Users/krisbrown/.local/state/ki/worktrees/ki-principal-integrate/+/_WORK/ki.portable-specifications/decisions.md:19), move the complete 19 October 23:35 ENTRY-NAMES block before the 23:37 SPEC-HOME block at line 7, preserving both bodies verbatim; this file is identical at origin, P and F.
- CHRONOLOGY-2: In [ways-of-working decisions](/Users/krisbrown/.local/state/ki/worktrees/ki-principal-integrate/+/_WORK/ki.ways-of-working/decisions.md:293), move the complete 22 October 02:21 block before the 02:22 block at line 289, preserving both bodies verbatim; F inherits this ordering from P.
- CHRONOLOGY-3: In the same decisions log at line 316, move the complete 02:28 overnight burn-down block after all three 02:26 blocks and before the 02:41 block at line 338, preserving every body and the relative order of the three 02:26 entries; F inherits this ordering from P.

- Ancestry: F `3a6b7bf8bb445fcfe222e69f2c48bc34f8fbafee` contains fetched origin/main `868c67213623b1d91e842f188b7ddf13c7dbd0c1` and primary P `f2778b861f56d4ae17e0de0e6ff71d1ec0c9a40d`; both fast-forward ancestry predicates pass and neither history is discarded.
- Content: Non-queue, non-state and non-decision files obey the three-way source comparison without exceptions; the changes retain each side's content where that side changed it alone.
- Queues: All 14 message files retain pending source instructions verbatim and in source order; 17 shortened instructions match their original `20b5fce0` source lines exactly after restoration in F, and the 20 absent origin instructions have explicit source-history removals in `06f3d893` and `5267c8e5`.
- Queue addition: The new ki.chezmoi PRINCIPAL-STATE-RESOLUTION instruction records the selected latest owning-work snapshot and requests confirmation; it replaces no pending source instruction.
- States: All 14 state files parse with unique YAML keys, one front matter block and no duplicate headings; each is one complete source snapshot, including origin's later ki.chezmoi hold and P's coherent Observatory, tools-burndown and ways-of-working states.
- Decisions: Both source histories survive with deliberate source-commit pruning accounted for; the combined ki.chezmoi log retains both sides in chronological order, while the three inherited inversions above remain elsewhere.
- Conflict markers: No unresolved markers; the sole full-tree pattern match is the unchanged Obsidian Git plugin's literal conflict-resolution help example, byte-identical at origin, P and F.
- Offline KB audit: Identical temporary exports of origin and F audited with `KI_REPO_OFFLINE=1` have zero failures; warnings decrease from six to five, with no added finding.
- Unpublished range: All 263 commits were enumerated with their actual changed paths; all 72 paths are ordinary Markdown knowledge or work-package content, with no unexpected mode, executable, symlink, code or configuration change.
- Primary preservation: P remains current; its sole tracked modification is an append-only decisions suffix, currently 5,260 bytes, and F's committed copy of that file is byte-identical to P's; all 460 current untracked paths avoid F's tracked paths and directory collisions.
- Checkout rehearsal: Git's two-tree working-directory update dry run succeeds using a copied index outside the repositories and the clone as an alternate object source; there is no post-merge hook in the primary's configured hooks directory.
- Review bounds: Only the authorised origin/main fetch changed a repository; no push, merge, commit, staging, checkout or repository-content edit was performed, and no earlier integration review or run report was consulted.

### Exact primary update for the reviewed F

A normal fast-forward with autostash disabled preserves the dirty decisions file because that path is unchanged between P and F. No stash, reset, rebase or file overlay is needed.

This procedure is mechanically verified for F, but publication remains blocked by this verdict until the chronology condition is expressly waived or a repaired candidate is reviewed. After an authorised publication of F, stop concurrent primary writers, save the current decisions file byte-for-byte and record an untracked path/content-hash manifest outside every repository, verify primary HEAD is still P, recheck the append-only dirty path and the untracked collision predicate, then run:

```sh
git -C /Users/krisbrown/workspaces/knowledge-islands/ki-principal fetch -q --no-tags origin refs/heads/main:refs/remotes/origin/main
git -C /Users/krisbrown/workspaces/knowledge-islands/ki-principal merge -q --ff-only --no-autostash 3a6b7bf8bb445fcfe222e69f2c48bc34f8fbafee
```

Verify HEAD equals F, the saved decisions suffix is byte-identical, and every untracked path and its contents remain intact before releasing the writer window. The primary changed during this review through external activity: its untracked set moved from 462 to 460 and its appended suffix grew from 4,591 to 5,260 bytes. The final checks cover the later snapshot; recheck immediately before updating. If chronology repairs change the committed decisions file, this direct-update proof does not carry over to the replacement tip: separately preserve the local suffix and re-review that checkout procedure.

## In Progress

Nothing running. Publication and the primary update wait on the supervisor's disposition of the chronology condition.

## Queries

### CHRONOLOGY - Correct or expressly waive the inherited ordering failures

**Context:** F passes the ancestry, content-retention, queue, state, conflict-marker, offline-audit and checkout-preservation checks. Three timestamp inversions already present in its sources fail the brief's requirement that decisions logs remain in time order. No repository correction has been made under this read-only review.

**Query:** Should the three complete decision blocks be reordered and a replacement candidate reviewed, or is the inherited chronology explicitly exempt from this publication gate?

**Options:**

a) (recommended, confidence high - the inversions and exact block boundaries are directly verified, and reordering can preserve all text) Correct the three block positions, preserve the primary's live appended suffix separately when planning its update, and review the resulting pinned candidate before publication.

b) Explicitly waive these inherited chronology inversions for F; retain its existing text and use the exact fast-forward procedure above after refreshing the publication and primary-state checks.

### 🤖 → 👤 Handoff to supervisor · blocked · since 10:04 BST

⛔ 1 blocked · 🤖 0 running

- [blocked] CHRONOLOGY disposition · supervisor · since 10:04 BST

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
