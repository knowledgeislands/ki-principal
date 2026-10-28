# [Model](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md>) › [Ways of working](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md>) › wow-rev-principal-integrate

**🤖 → 👤 Handoff to supervisor · blocked · Run report at 08:54 BST · last mark 08:24 BST**

---

## Done

VERDICT: UNSAFE · confidence high · The 127 commits have complete replay counterparts, but union resolutions restore consumed messages and obsolete live-state instructions; the candidate also excludes the primary checkout's later commit and cannot fast-forward that checkout.

- Scope passed: independent, local, read-only review of the diagnosis, integration report, Git objects and saved resolution evidence; only this report and its status file were written, with no remote call, repository mutation or commit.
- History passed with a qualification: all 127 original commits between `80860d92` and `84550579` map in order and one-to-one to 127 replays above `07df4b3`, ending at `e0d9c58d`; all author records and complete messages/trailers are byte-identical, and none became empty. Original hashes remain under `integration-original`, rather than in the ancestry of `2d010c86`.
- Patch check passed for 114 stable patch identities; the remaining 13 comprise the 12 conflict-bearing commits and `c78c6714` → `0e68b357`, whose added/removed content is unchanged but whose surrounding heading context differs.
- Whole-tree conservation passed: comparing both sides with `80860d92` gives 63 local-only changed paths, two upstream-only changed paths and six shared changed paths; every exclusive path has its source side's exact blob and mode, and no path outside those sets changed.
- Resolution provenance passed: all 15 saved conflict events on the six shared paths have stage 1, stage 2, stage 3 and resolved bytes matching the actual original parent, replay parent, original commit and replay commit respectively.
- Parent-content check passed for all five non-state shared paths, including Chez-moi decisions: every non-blank content-line occurrence from both source tips survives after ordered-list numbering is normalised. This proves textual retention, not preservation of queue disposition.
- Chez-moi metadata qualification: final state front matter is byte-identical to `07df4b3`; the old local state value, timestamp and duplicate Next steps heading are deliberately absent. Every other non-blank content-line occurrence from both tips survives. Literal losslessness against both parents is therefore too strong a claim, even though the newer metadata selection is sensible.
- Formatting check passed: `2d010c86` changes only the four declared logs; their normalised non-blank content multisets match `e0d9c58d`, and all six conflict paths are free of conflict markers. The integration clone is clean; this review did not rerun the reported KB audit or formatter gate.
- Cached publication ancestry passed: `07df4b3` is an ancestor of `2d010c86`; live origin state remains unverified because this review forbids fetching. An ancestry pass alone does not clear the semantic findings below.
- Primary reconciliation failed: primary `main` is `4a54e6912a80a65eeaa180700027a9ad7302e765`, one commit beyond `84550579`; its Work Process change is absent from `2d010c86`. Primary also has an unstaged change to the Ways of working decisions log and hundreds of untracked paths; no exact untracked-file/target-file collision was found against the current candidate.

### Blocking findings

1. The message union restores work deliberately consumed locally. Original commits `02a212e3`, `7430c63e` and `5267c8e5` remove message entries; their replay counterparts `a64aaacc`, `26ef7bd3` and `5343fe05` make no change to that queue. The restored entries are CLI-156-POLICY at [messages.md:7](</Users/krisbrown/.local/state/ki/worktrees/ki-principal-integrate/+/_WORK/ki.ways-of-working/messages.md:7>), AUDIT-OUTSIDE-LANE at [messages.md:4](</Users/krisbrown/.local/state/ki/worktrees/ki-principal-integrate/+/_WORK/ki.ways-of-working/messages.md:4>) and DEPCRUISE-PATH at [messages.md:3](</Users/krisbrown/.local/state/ki/worktrees/ki-principal-integrate/+/_WORK/ki.ways-of-working/messages.md:3>). The retained [disposition at decisions.md:334](</Users/krisbrown/.local/state/ki/worktrees/ki-principal-integrate/+/_WORK/ki.ways-of-working/decisions.md:334>) records DEPCRUISE-PATH dispatched and its queue line removed. Republishing it as an important incoming message can dispatch it again. Preserve its evidence and disposition together, and reconcile all retained queue entries against their owning decisions before publication.

2. Chez-moi's live state combines successive snapshots as simultaneous instructions. The old cutover instruction at [state.md:39](</Users/krisbrown/.local/state/ki/worktrees/ki-principal-integrate/+/_WORK/ki.chezmoi/state.md:39>) and the two old running-reconciliation claims at [state.md:43](</Users/krisbrown/.local/state/ki/worktrees/ki-principal-integrate/+/_WORK/ki.chezmoi/state.md:43>) are restored alongside later completion evidence and newer next steps. The owning work must reconcile these into one current state. Keeping every historical line in an executable Next steps section does not satisfy the work-package requirement that state is current rather than history. The decisions log itself passes the content-retention check.

3. The primary's newer commit is outside the reviewed candidate. `4a54e691` adds the closing thread identity rule to [Work Process](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Processes/Work Process/Work Process.md:243>); that addition is absent in the candidate. Neither `84550579` nor its descendant primary tip can fast-forward to the rebased candidate. Updating the primary requires a separately reviewed reconciliation that includes its actual current tip and preserves its uncommitted material.

### Exact safe sequence

This is the sequence for a separately authorised repair/integration run. No step below was executed by this review. Use an ancestry-preserving merge so the eventual result can fast-forward both origin and the primary, while retaining the original 127 commit identities as well as their replay counterparts.

1. Obtain the exclusive Git write window for both checkouts. Have the owner of the primary's dirty decisions log finish or otherwise resolve that change without another session staging, stashing or resetting it. Leave unrelated untracked material in place. Require primary `main`, no staged or unstaged tracked changes, and no active Git operation; capture its now-current full tip as `P`. If it changes again, restart the snapshot and review.

2. In the clean integration clone, retain `integration-original` and `integration-upstream`, create a new repair branch from `2d010c86`, and capture primary `main` into a new, unused local snapshot ref with `git fetch -q --no-tags /Users/krisbrown/workspaces/knowledge-islands/ki-principal refs/heads/main:refs/heads/review-primary-snapshot`. Require that snapshot ref to equal `P` and primary still to equal `P`. Reconcile findings 1 and 2 with the owning works, retaining the history in Git and recording each current disposition. Commit only the explicitly enumerated repair paths through normal hooks and the actual committing model's co-author trailer; accept or prune no work record.

3. On the repair branch, run `git merge --no-ff --no-commit review-primary-snapshot`. Review and resolve any conflicts against both current parents, including the six shared paths, and explicitly stage only the agreed resolutions before the hook-backed merge commit. Verify the actual committed paths afterwards. This merge retains the original 127 ancestors and `4a54e691` or any subsequently captured primary commits; it makes `P` an ancestor of the eventual candidate.

4. Fetch live origin in that clone with `git fetch -q origin refs/heads/main:refs/remotes/origin/main`. Inspect every unpublished ancestor and its actual paths, including the original history brought into the merge. If origin has advanced beyond the captured upstream, merge that tip into the repair branch and repeat semantic resolution and verification. Stop for unexpected code, high-risk changes, history discontinuity or an ownership dispute. An origin change is new review scope, not permission to reuse this verdict unchanged.

5. Run the repository's required checks and an independent review of the complete final candidate. Capture its full tip as `F`. Require both `git merge-base --is-ancestor origin/main "$F"` and `git merge-base --is-ancestor "$P" "$F"` to succeed; verify the primary's later Work Process change, all original and replay commit mappings, current message dispositions, coherent Chez-moi state, and final-path collision safety for the primary's untracked material. Recheck that the primary is still clean at `P` and the candidate is still `F`.

6. With publication authority and that final review, publish the pinned candidate with `git push -q origin "$F:refs/heads/main"`. A rejection means stop, fetch and review the changed remote ancestry; never force the update.

7. In the primary, recheck the exclusive window, clean tracked state, branch `main`, unchanged tip `P` and absence of target path collisions. Run `git fetch -q origin refs/heads/main:refs/remotes/origin/main`, require the fetched `origin/main` to equal reviewed `F`, then `git merge -q --ff-only "$F"`. Verify primary `HEAD` and its tracked files match `F`, with unrelated untracked material preserved. A changed primary or remote restarts the corresponding review rather than permitting a reset or rebase of another session's work.

## In Progress

Nothing running. Review is complete; candidate repair, live-origin verification, publication and primary integration remain blocked by the findings above and were not attempted.

## Queries

### INTEGRATION-REPAIR

**Context**: The candidate conserves the original commits' replay records and almost all source text, but it changes live queue/state meaning and excludes the primary's later work. The primary is also dirty.

**Query**: Should the supervisor commission a bounded corrective integration and independent rereview using the ancestry-preserving sequence above?

**Options**:

a) (recommended, confidence high - preserves both histories and provides a genuine fast-forward destination for both checkouts) Resolve the owning works' current queue/state, merge the settled primary tip into the repaired candidate, then rereview before publication.

b) Keep `2d010c86` as review evidence and defer publication and primary integration until the owning sessions can settle the outstanding material.

### 🤖 → 👤 Handoff to supervisor · since 08:54 BST

🤖 0 running · 👤 1 with you · ⛔ 1 blocked

- [blocked] Correct integration and obtain a new final review · supervisor · since 08:54 BST

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
