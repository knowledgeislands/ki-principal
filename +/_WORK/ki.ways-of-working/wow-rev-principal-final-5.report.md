# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-rev-principal-final-5

VERDICT: SAFE · confidence high - F retains the source histories and pending instructions, adds no fault, and the guarded update refuses the primary's current overlap.

**🤖 → 👤 Handoff to supervisor · Run report at 11:35 BST · last mark 08:24 BST**

---

## Done

Reviewed candidate F `32f3efb2f34aad97055f913aae71bec54ca8a014` independently from Git objects and fresh read-only fetches; earlier run reports were not used as evidence. Both real checkouts stayed read-only. No real publication, commit, acceptance or pruning was performed.

PASS 1 - Ancestry: P `f2778b861f56d4ae17e0de0e6ff71d1ec0c9a40d` and freshly fetched origin main `868c67213623b1d91e842f188b7ddf13c7dbd0c1` are ancestors of F; the final fetch confirmed origin unchanged at 11:33 BST.

PASS 2 - Retention: neither P nor origin has any reachable commit absent from F; original commit objects, including authors, author/committer timestamps, messages and trailers, remain intact rather than being replaced by their replays.

PASS 3 - Queues: all 14 touched queues retain pending source instructions in source order; restored full instructions were checked against source blobs, 16 consumed origin instructions were traced to actual receive/disposition commits without resurrection, and both newly authored reconciliation lines satisfy the envelope schema.

PASS 4 - State: the four touched state files are valid or unchanged from their owner's latest snapshot; Chez-moi is byte-identical to `b7c34fab` and the other three introduce no state-schema failure.

PASS 5 - Decisions: all text from P survives in the four touched logs; origin omissions match actual owner mark/receive diffs, including `b7af7215`, `3577bbe1`, `ec5db3c0` and the held-package receipt; dated blocks are ordered, retaining the owner's imprecise `09:2x` timestamp.

PASS 6 - Hygiene: all 65 paths touched anywhere in origin..F are ordinary, non-executable Markdown; there is no incoming binary, symlink, code or configuration change and no conflict marker in the changed final paths.

PASS 7 - Audit: fresh `KI_REPO_OFFLINE=1` KB audits give F zero failures and five warnings versus origin's zero failures and six warnings; no finding is added. An additional package audit also adds no failure signature over origin.

PASS 8 - Primary overlap: at 11:33 BST, ten tracked modifications were present, with only `+/_WORK/ki.ways-of-working/decisions.md` overlapping P..F; none of the 16,761 untracked/ignored file paths collides, including case, Unicode-normalisation and ancestor/descendant collisions.

PASS 9 - Update procedure: the exact Python command below was exercised against byte-for-byte scratch copies of the current primary and a local scratch origin under `/private/tmp`; both refusal cases preserved all files and staged entries, and the disjoint success control published and advanced to F with protected bytes, modes and staged entries preserved.

### Pre-existing faults

- Chez-moi's on-hold state has top-level `reason` and `release` instead of the required `hold` mapping; both schema failures and its history/size warnings are byte-identical to owner commit `b7c34fab`. F queues a correction request without rewriting that state.
- Twenty-four older queue lines have malformed envelopes: Observatory seven, regular work one, tools burn-down six, Ways of working one and State of play nine. Every such line is byte-identical in a latest source-side snapshot; inherited priority-order faults, including Mac Studio's, are also present in origin. The two newly authored reconciliation lines are valid.
- The additional package audit reports 45 inherited failures versus origin's 54: the existing message-envelope/priority faults, closed-schema/hold/timestamp faults in State of play, agent host, baseline rollout, Chez-moi, Mac Studio, portable specifications and timelines, and closed-list faults in baseline rollout and Mac Studio. None is a new F failure signature; other untouched package size/history warnings also remain.
- The five remaining KB warnings are four Project close-out assessments (Mac Studio, Paperclip capture and rebuild, secrets hygiene and timelines) and the existing unresolved-link finding, including template targets and stale cross-repository pointers.

### Primary modifications at the final snapshot

- Modified [raise-tmx.report.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.baseline-rollout/raise-tmx.report.md) - disjoint from F.
- Modified [review-naming.report.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.baseline-rollout/review-naming.report.md) - disjoint from F.
- Modified [review-plans-sizes.report.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.baseline-rollout/review-plans-sizes.report.md) - disjoint from F.
- Modified [review-themes.report.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.baseline-rollout/review-themes.report.md) - disjoint from F.
- Modified [sizekind-1.report.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.baseline-rollout/sizekind-1.report.md) - disjoint from F.
- Modified [va-plan.report.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.baseline-rollout/va-plan.report.md) - disjoint from F.
- Modified [wave1-audit.report.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.baseline-rollout/wave1-audit.report.md) - disjoint from F.
- Modified [wave1-review.report.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.baseline-rollout/wave1-review.report.md) - disjoint from F.
- Modified [wave1-sweep.report.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.baseline-rollout/wave1-sweep.report.md) - disjoint from F.
- Modified [decisions.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/decisions.md) - overlaps F.

Nothing was staged. The primary continued to change during review, as expected; the procedure takes a new baseline when run and does not rely on this list staying current.

### Exact guarded update command and dry-run result

Run this only inside the shared checkout's serialised Git-write window, with its filesystem writers paused until the command returns. This short operational prerequisite is necessary for an absolute byte-preservation guarantee: a writer can otherwise race any final check. It is not a requirement to freeze the checkout during review. If that window cannot be obtained, leave both branches unchanged.

The command discovers the current primary HEAD, staged and unstaged edits, all untracked files including ignored files, and live origin at run time. It refuses overlapping paths before publishing, preserves the index's staged entries, uses a normal fast-forward push and merge, and disables automatic stashing explicitly. If a later guard detects a change after publication, it stops with the primary untouched and origin already at F. It never stashes, cleans, resets or force-updates either checkout. A post-merge hook requires separate review and causes refusal.

```sh
python3 - /Users/krisbrown/.local/state/ki/worktrees/ki-principal-integrate /Users/krisbrown/workspaces/knowledge-islands/ki-principal <<'PY_UPDATE'
import hashlib, os, stat, subprocess as s, sys, tempfile, unicodedata
from pathlib import Path
F = '32f3efb2f34aad97055f913aae71bec54ca8a014'
publisher, primary = map(Path, sys.argv[1:3])
env = {**os.environ, 'GIT_OPTIONAL_LOCKS': '0'}
def git(repo, *args):
    return s.check_output(['git', '-C', str(repo), *args], env=env)
def run(repo, *args):
    s.run(['git', '-C', str(repo), *args], env=env, check=True)
def require(ok, reason):
    if not ok:
        raise RuntimeError(reason)
def names(repo, *args):
    return set(os.fsdecode(x) for x in git(repo, *args).split(b'\0') if x)
def key(p):
    return unicodedata.normalize('NFD', p).casefold()
def collide(a, b):
    a, b = key(a), key(b)
    return a == b or a.startswith(b + '/') or b.startswith(a + '/')
def snapshot():
    dirty = names(primary, 'diff', '--no-ext-diff', '--no-renames', '--name-only', '-z')
    dirty |= names(primary, 'diff', '--cached', '--no-ext-diff', '--no-renames', '--name-only', '-z', 'HEAD')
    untracked = names(primary, 'ls-files', '--others', '-z')  # Includes ignored files.
    files = {}
    for name in sorted(dirty | untracked):
        p = primary / name
        try:
            mode = p.lstat().st_mode
        except FileNotFoundError:
            files[name] = None
            continue
        if stat.S_ISLNK(mode):
            data = os.fsencode(os.readlink(p))
        else:
            require(stat.S_ISREG(mode), 'special file requires manual preservation: ' + name)
            data = p.read_bytes()
        files[name] = (mode, hashlib.sha256(data).hexdigest())
    entries = tuple(x for x in git(primary, 'ls-files', '--stage', '-z').split(b'\0')
                    if x and os.fsdecode(x.split(b'\t', 1)[1]) in dirty)
    return dirty, untracked, files, entries
try:
    require(git(publisher, 'rev-parse', 'refs/heads/repair-wow-principal').decode().strip() == F,
            'candidate branch changed; review again')
    remote = git(publisher, 'remote', 'get-url', 'origin').decode().strip()
    require(git(primary, 'remote', 'get-url', 'origin').decode().strip() == remote,
            'primary and publisher origins differ')
    require(git(primary, 'symbolic-ref', '--short', 'HEAD').decode().strip() == 'main',
            'primary is not on main')
    base = git(primary, 'rev-parse', 'HEAD').decode().strip()
    require(not git(primary, 'ls-files', '--unmerged'), 'unmerged index')
    flags = git(primary, 'ls-files', '-v', '-z').split(b'\0')
    require(all(not x or (not chr(x[0]).islower() and x[:1] != b'S') for x in flags),
            'assume-unchanged or skip-worktree entries require review')
    for name in ['index.lock', 'MERGE_HEAD', 'CHERRY_PICK_HEAD', 'REVERT_HEAD', 'rebase-merge', 'rebase-apply']:
        p = Path(git(primary, 'rev-parse', '--git-path', name).decode().strip())
        if not p.is_absolute():
            p = primary / p
        require(not p.exists(), 'another Git operation is active: ' + name)
    hook = Path(git(primary, 'rev-parse', '--git-path', 'hooks/post-merge').decode().strip())
    if not hook.is_absolute():
        hook = primary / hook
    require(not (hook.exists() and os.access(hook, os.X_OK)), 'post-merge hook needs separate review')
    before = snapshot()
    with tempfile.TemporaryDirectory(prefix='ki-publish-guard-', dir='/private/tmp') as directory:
        probe = Path(directory)
        run(probe, 'init', '-q')
        run(probe, 'fetch', '-q', '--no-tags', str(publisher), F + ':refs/review/candidate')
        run(probe, 'fetch', '-q', '--no-tags', str(primary), base + ':refs/review/primary')
        run(probe, 'fetch', '-q', '--no-tags', remote, 'refs/heads/main:refs/review/live-main')
        run(probe, 'merge-base', '--is-ancestor', 'refs/review/live-main', F)
        run(probe, 'merge-base', '--is-ancestor', base, F)
        changed = names(probe, 'diff', '--no-renames', '--name-only', '-z', base, F)
        protected = before[0] | before[1]
        overlaps = sorted(p for p in protected if any(collide(p, c) for c in changed))
        require(not overlaps, 'overlap; leave owner edits in place: ' + ', '.join(overlaps))
        require(git(primary, 'rev-parse', 'HEAD').decode().strip() == base and snapshot() == before,
                'primary changed during preflight; rerun from its new baseline')
        # This normal push rejects any remote advancement incompatible with F.
        run(publisher, 'push', '-q', 'origin', F + ':refs/heads/main')
        require(git(primary, 'rev-parse', 'HEAD').decode().strip() == base and snapshot() == before,
                'primary changed after publication; stop with primary untouched')
        run(primary, 'fetch', '-q', '--no-tags', '--no-write-fetch-head', str(publisher), F)
        require(git(primary, 'rev-parse', 'HEAD').decode().strip() == base and snapshot() == before,
                'primary changed before update; stop with primary untouched')
        run(primary, 'merge', '-q', '--ff-only', '--no-autostash', '--no-edit', F)
        require(git(primary, 'rev-parse', 'HEAD').decode().strip() == F, 'unexpected primary HEAD')
        require(snapshot() == before, 'post-update preservation check failed; retain all files and investigate')
    print('PASS: published fast-forward; primary at F; protected bytes, modes and staged entries preserved')
except (RuntimeError, s.CalledProcessError) as error:
    print('STOP:', error, file=sys.stderr)
    sys.exit(1)
PY_UPDATE
```

The tested Python payload has SHA-256 `cf74f7a4906e540777b07e5a134275d09fd9bc267b5d7c5323c35e44fda2353b`.

The exact current-primary copy refused before push because of the live Ways of working decisions edit, with its filesystem, staged entries, HEAD and local scratch origin unchanged. A second copy, with that overlapping edit removed only in scratch and an untracked file placed at F's new Chez-moi design-note path, also refused before push without altering either side. The success control removed only that overlapping edit in scratch, retained every other captured live edit and untracked/ignored file, and added disjoint staged-deletion, ignored-binary and untracked-symlink probes; publication and the primary fast-forward both reached F, and all protected content and staged entries matched afterwards. The real primary's HEAD and index remained at their source values; unrelated sessions changed its working files during the rehearsal.

## In Progress

Nothing running. All review scratch copies and temporary files have been removed; only this report and the required status file remain. Publication and the primary update have not been performed. The current overlapping edit must remain with its owner; any new primary commit outside F requires another candidate or review before the guard can proceed.

## Queries

None. The current overlap is a safe refusal condition, not a fault in F and not an instruction to discard or relocate the edit.

### 🤖 → 👤 Handoff to supervisor · since 11:35 BST

👤 1 with you · 🤖 0 running · ⛔ 0 blocked

- [with you] Candidate F publication-safety review · work/ki.ways-of-working · since 11:35 BST

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
