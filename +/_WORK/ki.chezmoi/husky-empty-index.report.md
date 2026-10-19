# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › husky-empty-index

**🤖 → 👤 Handoff to supervisor · Run report at 17:59 BST · last mark 18:57 BST**

---

## Done

Source commit `484ab543c2594ee0e4547f7c3c6fae05124f0484` (`fix(husky): skip pre-commit checks when the index is empty`) changes only [dot_config/husky/init.sh](/Users/krisbrown/.local/share/chezmoi/dot_config/husky/init.sh:12); source is committed locally and verified, with live apply held.

Bookkeeping commit `964f8910ef4b8a40cedd3a6ba0109c31622fdf5b` (`docs(chezmoi): record reviewed Husky source handoff`) changes only the [current work file](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.chezmoi/work.md); mark, complete Messages and parked holds were compared exactly and preserved.

Installed Husky 9.1.7 wrapper inspection and execution confirm the init sees the named wrapper in `$0` before the original hook; apps-midnight.ninja and the canonical engineering prefix remain untouched.

The POSIX guard skips only pre-commit with an empty staged index, continues on Git status 1, and preserves unexpected Git status and diagnostics; GUI/mise PATH setup and Husky disabled/debug behaviour remain intact.

Actual-wrapper boundary verification: 17 cases passed, covering empty and changed indexes, unborn HEAD, untracked and unstaged files, alternate `GIT_INDEX_FILE` in both directions, staged deletion, check failure status 7, fatal Git-diff status 128, other hooks, disabled/debug modes and mise present/absent. [Verifier](/Users/krisbrown/.local/state/ki/agents/chezmoi/husky-empty-index.evidence/verify.py) and [result](/Users/krisbrown/.local/state/ki/agents/chezmoi/husky-empty-index.evidence/boundary.log).

POSIX syntax check: `/bin/sh -n dot_config/husky/init.sh` passed; source whitespace check passed.

Full source audit under umask 022: exit 0, 0 failures, 27 warnings read; retained findings are authoring-template drift, an ADR amendment heading, absent committed gate and 24 roadmap migration warnings, all outside this focused change. [Audit log](/Users/krisbrown/.local/state/ki/agents/chezmoi/husky-empty-index.evidence/audit.log).

Full Node gate under umask 022: exit 0, 270 tests, 268 passed, 2 skipped, 0 failed. [Test log](/Users/krisbrown/.local/state/ki/agents/chezmoi/husky-empty-index.evidence/tests.log).

Full Markdown gate: exit 0, 92 files clean; owned work-file formatting and validation also passed. [Markdown log](/Users/krisbrown/.local/state/ki/agents/chezmoi/husky-empty-index.evidence/markdown.log).

Bounded scripts-excluded chezmoi diff: one target only, [~/.config/husky/init.sh](/Users/krisbrown/.local/state/ki/agents/chezmoi/husky-empty-index.evidence/target.diff); matching [source diff](/Users/krisbrown/.local/state/ki/agents/chezmoi/husky-empty-index.evidence/source.diff). Live target remains byte-identical to the parent source. [Verification receipt](/Users/krisbrown/.local/state/ki/agents/chezmoi/husky-empty-index.evidence/verification.json).

Teardown: temporary fixture repositories, synthetic hooks/tools, indexes and logs are removed; runtime temporary directory is empty. Only protected, inactive review evidence and the reusable verification script remain in launcher state; no installations, live bypass flags, real baseline commits, jobs or persistent runtime configuration were created.

Commit path inspection: each commit contains only its intended path; both staging areas and Git lock inventories are empty. Other writers' arriving edits and the untracked brief remain untouched. No writes under `+/_WORK/ki/`, remote calls, pushes, live bootstrap/repair, source-selection changes, apply, acceptance, pruning or new mark occurred.

This fixes hook noise. Normal Git clean-tree and exit behaviour remains as Git defines.

## In Progress

Nothing is running. Live apply is HOLD for Kris's review and explicit approval, required by the repository's [apply rule](/Users/krisbrown/.local/share/chezmoi/AGENTS.md).

Outstanding - no action requested now: migration evidence and SOURCE-LOCALS holds remain in the work file. The [latest Sol gate report](/Users/krisbrown/.local/state/ki/agents/chezmoi/sol-locals-gate.report.md) was context only. Kris's source-removal commit `dea74ab` and test commit `006ce2d` belong to other work; this run neither replayed the migration nor claimed those commits.

Unpublished handoff, cached refs only with no fetch: chezmoi on Sol/main has one unpublished commit, this run's `484ab543c2594ee0e4547f7c3c6fae05124f0484`, above cached `origin/main` at `006ce2d`; working tree is clean.

Unpublished handoff, cached refs only with no fetch: ki-principal on Sol/main has two unpublished commits, other work's `fd50f58d` (`chore: baseline`) and this run's `964f8910ef4b8a40cedd3a6ba0109c31622fdf5b`, above cached `origin/main` at `3a9b70fe`. Other-writer edits remain unstaged in chezmoi decisions and ways-of-working decisions/queries/state, plus the untracked Husky brief. [Exact handoff](/Users/krisbrown/.local/state/ki/agents/chezmoi/husky-empty-index.evidence/git-handoff.json). Reconcile both Sol/main checkouts before starting elsewhere; no publishing is authorised by this run.

## Queries

### HUSKY-APPLY - Review and apply the single target

**Context:** The focused source is verified and locally committed. The [bounded target diff](/Users/krisbrown/.local/state/ki/agents/chezmoi/husky-empty-index.evidence/target.diff) has not been applied. Repository guidance explicitly requires Kris's diff review before apply.

**Query:** Approve the single-target apply and the isolated verification below, or keep it held?

**Options:** a) (recommended, confidence high - actual installed-wrapper fixtures cover the requested boundaries) Review the bounded diff, then approve this exact apply and verification. b) Keep live apply held and request a source revision. Neither option authorises pushing or wider rollout.

Proposed apply, not executed:

```sh
chezmoi apply --exclude scripts /Users/krisbrown/.config/husky/init.sh
```

Proposed isolated post-apply verification, not executed against the live target: byte-compare source/target, check POSIX syntax, then copy the applied init into disposable fixtures and repeat the same 17 actual-wrapper boundary cases. All hook execution stays inside those fixtures; the verifier removes them in its `finally` teardown, and the final command removes the empty temporary root.

```sh
(
  umask 022
  cmp /Users/krisbrown/.local/share/chezmoi/dot_config/husky/init.sh /Users/krisbrown/.config/husky/init.sh &&
  /bin/sh -n /Users/krisbrown/.config/husky/init.sh &&
  HUSKY_TEST_INIT=/Users/krisbrown/.config/husky/init.sh python3 /Users/krisbrown/.local/state/ki/agents/chezmoi/husky-empty-index.evidence/verify.py &&
  rmdir /var/folders/6b/b4c73j8s6w12g2k9_yl652_h0000gn/T/ki-agents/chezmoi/husky-empty-index
)
```

### 🤖 → 👤 Handoff to supervisor · since 17:59 BST

👤 1 with you · 🅿️ 0 parked in this run

- [with you] HUSKY-APPLY single-target review and apply · Kris · since 17:59 BST
- [unpushed] chezmoi Sol/main: one owned source commit; no push authorised
- [unpushed] ki-principal Sol/main: owned bookkeeping above another writer's baseline; no push authorised
