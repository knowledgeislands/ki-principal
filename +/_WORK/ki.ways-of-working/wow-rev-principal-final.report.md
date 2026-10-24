VERDICT: UNSAFE · confidence high · Pending queue instructions were replaced with summaries instead of retaining their unconsumed source lines.

# [Model](/Users/krisbrown/.local/state/ki/worktrees/ki-principal-integrate/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/.local/state/ki/worktrees/ki-principal-integrate/Streams/Projects/ways-of-working.md) › wow-rev-principal-final

**🤖 → 👤 Handoff to supervisor · blocked · Run report at 09:42 BST · last mark 08:24 BST**

---

## Done

- Independently reviewed F `7eb989278ed63115ad69c39b0519580df1637682`; no earlier integration review or run report was opened.
- Ancestry passes: fetched origin/main `868c67213623b1d91e842f188b7ddf13c7dbd0c1` and P `f2778b861f56d4ae17e0de0e6ff71d1ec0c9a40d` are both ancestors of F; neither history is discarded.
- Publication scope passes: inspected all 262 unpublished commits and their 72 changed paths; every path is Markdown knowledge or work-package content, with ordinary file modes and no binary payload.
- Merge preservation passes outside the queue finding: every origin-only change survives verbatim; primary-only changes survive, with the additional chezmoi state-resolution message replacing its empty-queue placeholder.
- Decision reconciliation passes: both sides' added entries survive in chronological order; all 77 incoming chezmoi decision lines are retained, and the primary's decision-log contents survive.
- Current-state reconciliation passes: all 14 tracked state files have one state, unique frontmatter keys and unique current sections; chezmoi uses the latest owning-work hold at 07:51 UTC with matching mark.
- Conflict-marker check passes across tracked Markdown.
- Offline KB audit passes its comparison: `KI_REPO_OFFLINE=1`, four selected KB skills, zero failures on both snapshots, five candidate warnings against six on origin, and no added finding.
- Queue retention fails: 17 exact source lines still present on fetched origin are absent from the live queues and replaced by summaries with historical links; several summaries explicitly retain pending work.
- Primary preservation passes for the latest snapshot: 460 untracked files have no F path collision; its 3696-byte decisions append remains a strict append, and the tracked decisions blob is identical at P and F.
- Checkout dry run passes using an external index copy and read-only alternate objects; the real primary index is unchanged, and no post-merge hook is installed.
- Review made no repository edits, merge, commit or push; its only network operation was the permitted origin/main fetch, without FETCH_HEAD, tags, submodule fetches or automatic maintenance.

### QUEUE-LINES - Restore the pending original queue lines

The live [Observatory queue](/Users/krisbrown/.local/state/ki/worktrees/ki-principal-integrate/+/_WORK/ki.observatory/messages.md:3) and [Tools burndown queue](/Users/krisbrown/.local/state/ki/worktrees/ki-principal-integrate/+/_WORK/ki.tools-burndown/messages.md:3) substitute summaries for source instructions. The pending capture, reminder-check, bring-up, integration and importer requests make this a failure of the requested unconsumed-line preservation rule. Historical links retain access to the source, but do not retain those lines in the live queue.

Exact change needed: restore each wholly or partly unconsumed original line verbatim from `20b5fce0bb34c213b3bfcec9c7e437eef5e45e1e`, at the same queue path. Completion notes may accompany it. Delete an original only after recording a verified disposition consuming the whole instruction. These are all 17 replacements requiring that disposition; pairs below are F line → original line:

| Queue | F line → original line |
| --- | --- |
| ki.observatory | 3 → 4; 4 → 5; 5 → 6; 6 → 7; 7 → 9; 12 → 15 |
| ki.tools-burndown | 3 → 4; 4 → 7; 5 → 9; 6 → 11; 7 → 15; 8 → 18; 9 → 19; 10 → 20; 11 → 21; 13 → 23; 15 → 25 |

Then repeat this read-only comparison on the repaired candidate before publication. No Git history rewrite is needed.

## In Progress

Nothing running. Publication remains blocked by QUEUE-LINES.

The primary changed concurrently during review: its untracked inventory moved from 462 to 460 and its append grew. The preservation and checkout checks were repeated against the latest snapshot, which stayed stable during that recheck. Serialise the eventual update with its other writers and repeat the dirty-file and collision preflight immediately beforehand.

### Exact primary-checkout procedure

For the requested P-to-F operation, once the publication candidate is approved, import its objects from the local integration clone and perform a fast-forward-only merge with autostash disabled:

```sh
git -C /Users/krisbrown/workspaces/knowledge-islands/ki-principal fetch -q --no-tags /Users/krisbrown/.local/state/ki/worktrees/ki-principal-integrate refs/heads/repair-wow-principal
git -C /Users/krisbrown/workspaces/knowledge-islands/ki-principal -c merge.autoStash=false merge -q --ff-only 7eb989278ed63115ad69c39b0519580df1637682
```

The primary is on main at P and does not yet have F's object. No stash or temporary commit is needed: F does not modify `+/_WORK/ki.ways-of-working/decisions.md`, so the uncommitted append carries through directly, and the checked untracked paths remain untouched. Verify the append and untracked-file hashes after the update. These commands describe the preservation mechanism; F's queue finding must be resolved before execution, and a repaired candidate requires its own verified commit identifier.

## Queries

### QUEUE-LINES - Return the candidate for queue repair

**Context:** The graph, offline audit and dirty-primary update mechanism pass. The live pending queue instructions do not meet the explicit source-line retention requirement.

**Query:** Should the responsible writer restore the pending originals and return a repaired candidate for review?

**Options:**

a) (recommended, confidence high - exact source lines and their live replacements were independently compared) Repair the queues using the mapping above, then repeat the safety review before publication.

b) Keep publication blocked and leave F unchanged.

### 🤖 → 👤 Handoff to supervisor · blocked · since 09:42 BST

🤖 0 running · 👤 1 you · ⛔ 1 blocked

- [blocked] QUEUE-LINES: restore pending source instructions before publication · Ways of working coordinator · since 09:42 BST

🧵 Coordination thread · Ways of working (ki.ways-of-working)
