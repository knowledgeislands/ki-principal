VERDICT: UNSAFE · confidence high - Decision text is missing, pending queue records remain altered, hold metadata is invalid, and the primary changed during review.

# [Model](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md>) › [Ways of working](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md>) › wow-rev-principal-final-3

**🤖 → 👤 Handoff to supervisor · blocked · Run report at 10:32 BST · last mark 08:24 BST**

---

## Done

Reviewed F `13e94479db9675115e79ff62e343c8a1ec5d7ab1`, primary P `f2778b861f56d4ae17e0de0e6ff71d1ec0c9a40d`, and freshly fetched origin main `868c67213623b1d91e842f188b7ddf13c7dbd0c1`; created no commits and made no working-tree or index changes in either checkout.

PASS 1 - P and live origin main are ancestors of F; the proposed publication is a fast-forward, and a second read-only fetch found origin unchanged.

FAIL 2 - All 2,980 original commits rehash correctly, with their authors, timestamps, complete messages and trailers intact, and no original reachable object is lost; original decision text nevertheless disappears from F's current tree, as check 5 details.

FAIL 3 - Pending source queue records remain reformatted, including four exact-line failures: APP044-STALE and BRG004-NEAR in [Observatory messages](</Users/krisbrown/.local/state/ki/worktrees/ki-principal-integrate/+/_WORK/ki.observatory/messages.md:8>) and the explicit-outcomes and complete-project/no-op OPS009-SPLIT records in [Tools burndown messages](</Users/krisbrown/.local/state/ki/worktrees/ki-principal-integrate/+/_WORK/ki.tools-burndown/messages.md:12>); exact surviving records and restored originals retain source order, and handled source instructions remain absent.

FAIL 4 - All four touched state files parse as strict YAML with unique keys and coherent timestamps; [ki.chezmoi state](</Users/krisbrown/.local/state/ki/worktrees/ki-principal-integrate/+/_WORK/ki.chezmoi/state.md:4>) matches latest owning commit `b7c34fab` byte-for-byte, but its top-level reason/release fields violate the closed state schema and leave the required hold mapping absent.

FAIL 5 - [Ways of working decisions](</Users/krisbrown/.local/state/ki/worktrees/ki-principal-integrate/+/_WORK/ki.ways-of-working/decisions.md:1>) retains all 80 P blocks but omits text from 17 [origin decision blocks](https://github.com/knowledgeislands/ki-principal/blob/868c67213623b1d91e842f188b7ddf13c7dbd0c1/+/_WORK/ki.ways-of-working/decisions.md): 15 headings are absent and two existing headings lack origin's body version; the other three logs retain both sides, and all F dated blocks are in chronological order.

PASS 6 - Across all 264 incoming commits, every touched path is Markdown: 73 paths, 350 distinct text blobs, ordinary non-executable file modes only, and no conflict marker in F's changed paths; no binary, symlink, code or configuration change was found.

PASS 7 - Offline KB audits with KI_REPO_OFFLINE=1 found no new finding: origin has zero failures and six warnings, F zero failures and five warnings; the complete internal-link sets also match, including all 18 unresolved links hidden by the report's abbreviated display.

FAIL 8 - Primary HEAD remains P and both indexes are unchanged, but the primary acquired an additional tracked [queries edit](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/queries.md:1>) during review; its decisions change remains append-only and grew from 6,588 to 7,902 suffix bytes; all 16,372 untracked/ignored paths are collision-free under exact, file/directory, NFC, NFD and case-insensitive comparisons, with no merge, rebase or index lock in progress.

FAIL 9 - The guarded rehearsal of the later primary snapshot stopped before fetch/push because of that extra tracked edit; an end-to-end trial reconstructed from the recorded earlier P snapshot succeeded against a local scratch origin, preserving its 6,588-byte suffix and all 16,372 untracked/ignored files byte-for-byte, including symlink targets and modes; the live update is therefore not ready to execute.

### Exact update commands and dry-run result

These are the exact guarded commands for F. They are withheld from live execution because F failed this review. Run only after a successful review of the chosen candidate and with both checkouts held by one writer; a successor needs its newly reviewed commit identifiers substituted. The current primary fails the guard before publication.

The script captures the suffix from P's committed prefix, saves recovery copies under /private/tmp, fetches immediately before a non-force push, fetches the published commit into the primary, temporarily restores only its decisions log, fast-forwards main, and appends the captured bytes to F's committed log. Its finally block restores the suffix against whichever approved HEAD the merge reached. It verifies every untracked/ignored leaf before and after the update and keeps the recovery backup for owner review.

```sh
python3 - <<'PY'
import hashlib, json, os, stat, subprocess, tempfile, unicodedata
from pathlib import Path

integration = Path(os.environ.get("WOW_INTEGRATION", "/Users/krisbrown/.local/state/ki/worktrees/ki-principal-integrate"))
primary = Path(os.environ.get("WOW_PRIMARY", "/Users/krisbrown/workspaces/knowledge-islands/ki-principal"))
candidate = "13e94479db9675115e79ff62e343c8a1ec5d7ab1"
pinned = "f2778b861f56d4ae17e0de0e6ff71d1ec0c9a40d"
log = "+/_WORK/ki.ways-of-working/decisions.md"
env = dict(os.environ, GIT_OPTIONAL_LOCKS="0", KI_REPO_OFFLINE="1")
def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args], env=env)
def require(condition, message):
    if not condition: raise RuntimeError(message)
def inventory():
    result = {}
    for raw in git(primary, "ls-files", "--others", "-z").split(b"\0"):
        if not raw: continue
        path = os.fsdecode(raw); item = primary / path; mode = item.lstat().st_mode
        value = os.readlink(item) if stat.S_ISLNK(mode) else hashlib.sha256(item.read_bytes()).hexdigest()
        result[path] = [mode, value]
    return result

def preflight(original=None):
    require(git(primary, "symbolic-ref", "--short", "HEAD").strip() == b"main", "primary branch changed")
    require(git(primary, "rev-parse", "HEAD").decode().strip() == pinned, "primary HEAD changed")
    require(git(primary, "status", "--porcelain=v1", "-z", "--untracked-files=no") == b" M " + log.encode() + b"\0", "primary tracked changes changed")
    gitdir = Path(git(primary, "rev-parse", "--absolute-git-dir").decode().strip())
    common = Path(git(primary, "rev-parse", "--git-common-dir").decode().strip())
    if not common.is_absolute(): common = primary / common
    for directory in {gitdir, common}:
        for name in ["MERGE_HEAD", "REBASE_HEAD", "rebase-apply", "rebase-merge", "index.lock", "sequencer", "CHERRY_PICK_HEAD", "REVERT_HEAD"]:
            require(not (directory / name).exists(), "Git operation or index lock exists")
    if original is not None: require((primary / log).read_bytes() == original, "decisions log changed; rerun review")

preflight()
base = git(primary, "show", pinned + ":" + log)
original = (primary / log).read_bytes()
require(original.startswith(base), "primary decisions change is not append-only")
suffix = original[len(base):]
untracked = inventory()
tracked = [os.fsdecode(x) for x in git(integration, "ls-tree", "-rz", "--name-only", candidate).split(b"\0") if x]
for form in ["NFC", "NFD"]:
    normal = lambda p: unicodedata.normalize(form, p).casefold()
    files = {normal(p) for p in tracked}
    directories = {normal(str(q)) for p in tracked for q in Path(p).parents if str(q) != "."}
    for p in untracked:
        require(normal(p) not in files | directories and not any(normal(str(q)) in files for q in Path(p).parents if str(q) != "."), "untracked path collides with candidate")
backup = Path(tempfile.mkdtemp(prefix="ki-principal-update.", dir="/private/tmp"))
(backup / "original.bin").write_bytes(original)
(backup / "suffix.bin").write_bytes(suffix)
(backup / "untracked.json").write_text(json.dumps(untracked))
print("Recovery backup:", backup, flush=True)
git(integration, "-c", "maintenance.auto=false", "-c", "gc.auto=0", "fetch", "-q", "--no-tags", "--no-write-fetch-head", "origin", "refs/heads/main:refs/remotes/origin/main")
git(integration, "merge-base", "--is-ancestor", "refs/remotes/origin/main", candidate)
git(integration, "merge-base", "--is-ancestor", pinned, candidate)
preflight(original)
require(inventory() == untracked, "untracked files changed; rerun review")
git(integration, "push", "-q", "origin", candidate + ":refs/heads/main")
git(primary, "-c", "maintenance.auto=false", "-c", "gc.auto=0", "fetch", "-q", "--no-tags", "--no-write-fetch-head", "origin", "refs/heads/main:refs/remotes/origin/main")
require(git(primary, "rev-parse", "refs/remotes/origin/main").decode().strip() == candidate, "origin advanced again; stop before updating primary")
preflight(original)
require(inventory() == untracked, "untracked files changed; stop before updating primary")
try:
    git(primary, "restore", "--source=" + pinned, "--worktree", "--", log)
    git(primary, "merge", "-q", "--ff-only", candidate)
finally:
    # Even an interrupted or failed merge gets its current committed version plus the saved suffix.
    head = git(primary, "rev-parse", "HEAD").decode().strip()
    require(head in [pinned, candidate], "unexpected primary HEAD; recover from backup")
    (primary / log).write_bytes(git(primary, "show", head + ":" + log) + suffix)
require(git(primary, "rev-parse", "HEAD").decode().strip() == candidate, "primary did not reach candidate")
require((primary / log).read_bytes() == git(primary, "show", candidate + ":" + log) + suffix, "suffix verification failed")
require(inventory() == untracked, "untracked-file verification failed")
require(git(primary, "status", "--porcelain=v1", "-z", "--untracked-files=no") == b" M " + log.encode() + b"\0", "unexpected tracked change after update")
print("Verified: origin and primary at candidate; suffix and all untracked files preserved.")
print("Keep the recovery backup until the owner has reviewed the result.")
PY
```

The scratch rehearsal used identical script contents with only WOW_INTEGRATION and WOW_PRIMARY redirected to copied checkouts, both origins redirected to a bare repository under /private/tmp, and that bare main initialised to the fetched origin commit. For the successful trial, only the scratch tracked state was reconstructed to the earlier observed P plus its saved decisions suffix; no live edit was restored or reverted. Local origin main and copied primary main reached F, the copied log equalled F's committed bytes plus the exact saved suffix, and the full untracked inventory matched. The saved suffix SHA-256 was `090adb949c6f487677d06030ee0db21c4e0c16b53100809d72e643f2b002d0cf`. The later-snapshot refusal and reconstructed-snapshot success are distinct results; no network push was attempted.

All review snapshots, scratch repositories and rehearsal recovery copies were removed; the run temporary directory is empty.

## In Progress

Nothing is running. This read-only review cannot repair the candidate or settle the primary writer's changes.

## Queries

### [PRINCIPAL-F-SAFETY - repair the rejected candidate](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/work.md>)

**Context:** F preserves the original Git history but fails the required current-content checks. Fifteen origin decision blocks need reinserting and two body variants need merging into their existing headings, keeping all text and chronological order. Two queues still contain altered pending source records. The latest ki.chezmoi hold state also needs its owning work to correct the hold mapping without changing its meaning or timestamps. Meanwhile the primary writer changed queries and appended more decisions during review, so its original publication precondition no longer holds. This run's explicit read-only bounds forbid applying any of these repairs.

**Query:** Authorise a bounded successor repair and another independent publication review after the primary writers are serialised?

**Options:**

a) (recommended, confidence high - the defects are directly reproduced and the repair is additive and reversible) Keep F unpublished; restore the missing decision text and all remaining altered pending instructions verbatim without reviving consumed portions, obtain the owning ki.chezmoi state correction, and preserve the primary writer's edits while agreeing a new pinned snapshot; then review the successor and repeat the scratch update trial.

b) Keep F unpublished and defer the integration.

### 🤖 → 👤 Handoff to supervisor · blocked · since 10:32 BST

🤖 0 running · 👤 1 with you · ⛔ 1 blocked

- [blocked] Candidate retention/state repair and a settled primary snapshot · supervisor · since 10:32 BST

🧵 Coordination thread · KI > Model Ways working (ki.ways-of-working)
