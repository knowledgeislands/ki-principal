VERDICT: UNSAFE · confidence high - F introduces malformed Chez-moi queue entries; retention and update-mechanics checks pass.

# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-rev-principal-final-4

**🤖 → 👤 Handoff to supervisor · blocked · Run report at 11:08 BST · last mark 08:24 BST**

---

## Done

Reviewed F `7200dd9baf86784f74e64331d131174b15611d75`, P `f2778b861f56d4ae17e0de0e6ff71d1ec0c9a40d` and fetched origin/main `868c67213623b1d91e842f188b7ddf13c7dbd0c1` independently. Earlier review and repair reports supplied no evidence.

- PASS 1 - Ancestry: P and live origin/main are ancestors of F; a second read-only fetch confirmed origin remained at the reviewed commit.
- PASS 2 - Retention: all 2,980 commits reachable from the source heads remain reachable as their original objects, preserving authors, both timestamps, messages and trailers; all 2,914 P commit objects also match the primary byte-for-byte, and no non-package content has an unexplained merge choice.
- FAIL 3 - Queues: pending instructions remain verbatim and in both source heads' order, with no owner-consumed instruction resurrected, but the two newly added [Chez-moi entries](/Users/krisbrown/.local/state/ki/worktrees/ki-principal-integrate/+/_WORK/ki.chezmoi/messages.md:3), lines 3 and 4, fail RECORD-2's message-envelope schema.
- PASS 4 - State: the Observatory and tools burn-down states pass the state checks; ways-of-working is byte-identical to its owner's `e0d9c58d` snapshot, and Chez-moi is byte-identical to its owner's latest `b7c34fab` snapshot, including its pre-existing faults.
- PASS 5 - Decisions: all P blocks and all other surviving origin text remain; each of the 17 origin ways-of-working blocks absent or rewritten in F was verified against its actual owning-work mark commit: `b7af7215` (9), `3577bbe1` (4), `ec5db3c0` (4); all four touched logs have their explicitly dated blocks in time order.
- PASS 6 - Hygiene: all 265 incoming commits touch only 73 regular, non-executable Markdown paths; no binary, symlink, code or configuration transition, and no conflict marker in the changed final paths.
- PASS 7 - Offline KB audit: `KI_REPO_OFFLINE=1` audit of F and origin, including declared KB prerequisites, finds zero failures and no added finding; warnings fall from six to five.
- PASS 8 - Primary: at 11:05 BST, HEAD remains P, the only tracked edit is the original 11,083-byte decisions suffix, all initially observed untracked files are unchanged, and all 16,491 current untracked files, including ignored files, have no tracked-path collision; neither checkout has an active merge, rebase or index lock.
- PASS 9 - Update rehearsal: the exact procedure below completed against isolated copies and a local bare origin under `/private/tmp`, leaving both heads at F, the suffix appended byte-for-byte, and all 16,491 untracked files and symlinks intact with their modes; changed-suffix, collision and index-lock cases stopped before publication; all scratch copies were removed before DONE.

**Publication blocker**

The queue entry at line 3 was introduced by `71a8851c`; line 4 was introduced by F itself. Both use an invalid envelope. They are absent from the Chez-moi owner's latest queue at `b7c34fab`, so the pre-existing-fault exemption does not apply. A separate offline work-package audit identifies this as the sole new finding over the union of P and origin. A scratch-only two-line envelope correction, preserving instruction bodies, senders and timestamps, removes that finding. The real candidate was not edited.

**Pre-existing faults**

- [Chez-moi state](/Users/krisbrown/.local/state/ki/worktrees/ki-principal-integrate/+/_WORK/ki.chezmoi/state.md:1): legacy top-level hold fields and missing structured `hold` fail the closed schema; its Now length, body length and history also warn. The complete file is byte-identical to the owner's latest `b7c34fab` commit.
- [Ways-of-working state](/Users/krisbrown/.local/state/ki/worktrees/ki-principal-integrate/+/_WORK/ki.ways-of-working/state.md:1): the history warning already exists in the byte-identical owner snapshot `e0d9c58d`; its decisions-length warning already exists at owner head P, with the same blocks and line count before F's ordering-only change.
- KB warnings: existing close-out assessments remain missing for [mac-studio-setup](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/mac-studio-setup.md), [paperclip-capture-and-rebuild](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/paperclip-capture-and-rebuild.md), [secrets-hygiene](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/secrets-hygiene.md), [timelines](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/timelines.md); the existing unresolved-link finding also remains. No new KB finding is introduced.
- The other 56 work-package findings in F reproduce at P or origin; they are not new candidate findings.

**Exact guarded update commands and dry-run result**

Mechanical rehearsal: PASS, including the three refusal cases above. These commands exhibit the tested F update; they are not authority to execute this UNSAFE candidate. Keep publication blocked. A repaired candidate needs a new F pin and another review. Before an approved update, pause writers in both checkouts for the entire procedure. It rechecks heads, origin identity, tracked edits, suffix bytes, untracked collisions and operation locks, and preserves a recovery copy through the primary fast-forward. It uses ordinary hooks and non-force Git operations.

```sh
python3 - \
  '/Users/krisbrown/.local/state/ki/worktrees/ki-principal-integrate' \
  '/Users/krisbrown/workspaces/knowledge-islands/ki-principal' \
  '9bb66be4177b78976cab56288695ca67d631b92bf4bd149e3c92997e1dcad510' <<'PY'
import hashlib, json, os, shutil, stat, subprocess, sys, tempfile
from pathlib import Path

publisher, primary = map(Path, sys.argv[1:3])
expected_url_hash = sys.argv[3]
F = '7200dd9baf86784f74e64331d131174b15611d75'
P = 'f2778b861f56d4ae17e0de0e6ff71d1ec0c9a40d'
O = '868c67213623b1d91e842f188b7ddf13c7dbd0c1'
rel = '+/_WORK/ki.ways-of-working/decisions.md'
env = dict(os.environ, GIT_OPTIONAL_LOCKS='0', KI_REPO_OFFLINE='1')

def git(repo, *args):
    return subprocess.check_output(
        ['git', '--no-optional-locks', '-C', str(repo), *args], env=env)

def require(value, message):
    if not value:
        raise RuntimeError(message)

def no_operation(repo):
    for name in ('MERGE_HEAD', 'REBASE_HEAD', 'CHERRY_PICK_HEAD',
                 'rebase-merge', 'rebase-apply', 'index.lock'):
        path = Path(git(repo, 'rev-parse', '--git-path', name).decode().strip())
        require(not (path if path.is_absolute() else repo / path).exists(),
                f'{repo}: outstanding {name}')

def untracked(repo):
    result = {}
    for raw in git(repo, 'ls-files', '--others', '-z').split(b'\0')[:-1]:
        name = os.fsdecode(raw)
        path = repo / name
        mode = path.lstat().st_mode
        require(stat.S_ISREG(mode) or stat.S_ISLNK(mode),
                f'Unsupported untracked file: {name}')
        data = os.fsencode(os.readlink(path)) if path.is_symlink() else path.read_bytes()
        result[name] = [stat.S_IMODE(mode), stat.S_ISLNK(mode),
                        hashlib.sha256(data).hexdigest()]
    return result

for repo in (publisher, primary):
    no_operation(repo)
    url = git(repo, 'remote', 'get-url', 'origin').strip()
    require(hashlib.sha256(url).hexdigest() == expected_url_hash,
            f'{repo}: unexpected origin')
require(git(publisher, 'rev-parse', 'HEAD').decode().strip() == F, 'Publisher moved')
require(git(publisher, 'symbolic-ref', '--short', 'HEAD').strip() == b'repair-wow-principal',
        'Unexpected publisher branch')
require(not git(publisher, 'status', '--porcelain=v1', '-z', '-uall'), 'Publisher is dirty')
require(git(primary, 'rev-parse', 'HEAD').decode().strip() == P, 'Primary moved')
require(git(primary, 'symbolic-ref', '--short', 'HEAD').strip() == b'main',
        'Primary is not on main')
require(git(primary, 'status', '--porcelain=v1', '-z', '--untracked-files=no')
        == b' M ' + rel.encode() + b'\0', 'Unexpected tracked change')
base = git(primary, 'show', P + ':' + rel)
original = (primary / rel).read_bytes()
require(original.startswith(base), 'Primary edit is not an appended suffix')
suffix = original[len(base):]
require(len(suffix) == 11083 and hashlib.sha256(suffix).hexdigest()
        == '67d9bee52555f3a6951997d3f661636952b44a159ea66af555dcb373e07c253b',
        'Primary suffix changed since review')
before = untracked(primary)
tracked = [os.fsdecode(x) for x in git(publisher, 'ls-tree', '-r', '--name-only', '-z', F)
           .split(b'\0')[:-1]]
require(not any(u == t or u.startswith(t + '/') or t.startswith(u + '/')
                for u in before for t in tracked), 'Untracked path collides with F')
git(publisher, 'fetch', '-q', '--no-tags', 'origin', 'refs/heads/main:refs/remotes/origin/main')
require(git(publisher, 'rev-parse', 'origin/main').decode().strip() == O, 'Origin moved')
git(publisher, 'merge-base', '--is-ancestor', P, F)
git(publisher, 'merge-base', '--is-ancestor', O, F)
require((primary / rel).read_bytes() == original and untracked(primary) == before,
        'Primary changed during preflight')
for repo in (publisher, primary):
    no_operation(repo)
git(publisher, 'push', '-q', 'origin', F + ':refs/heads/main')
git(primary, 'fetch', '-q', '--no-tags', 'origin', 'refs/heads/main:refs/remotes/origin/main')
require(git(primary, 'rev-parse', 'origin/main').decode().strip() == F, 'Origin advanced again')
require(git(primary, 'rev-parse', 'HEAD').decode().strip() == P, 'Primary moved after push')
require(git(primary, 'status', '--porcelain=v1', '-z', '--untracked-files=no')
        == b' M ' + rel.encode() + b'\0', 'Tracked changes changed after push')
require((primary / rel).read_bytes() == original and untracked(primary) == before,
        'Primary changed after push')
no_operation(primary)
backup = Path(tempfile.mkdtemp(prefix='ki-principal-ff-', dir='/private/tmp'))
(backup / 'original.bin').write_bytes(original)
(backup / 'suffix.bin').write_bytes(suffix)
(backup / 'untracked.json').write_text(json.dumps(before, sort_keys=True))
try:
    git(primary, 'restore', '--source=' + P, '--worktree', '--', rel)
    git(primary, 'merge', '-q', '--ff-only', F)
    require(git(primary, 'rev-parse', 'HEAD').decode().strip() == F, 'Fast-forward failed')
    expected = git(primary, 'show', F + ':' + rel) + suffix
    (primary / rel).write_bytes(expected)
    require((primary / rel).read_bytes() == expected, 'Suffix verification failed')
    require(untracked(primary) == before, 'Untracked preservation failed')
    require(git(primary, 'status', '--porcelain=v1', '-z', '--untracked-files=no')
            == b' M ' + rel.encode() + b'\0', 'Unexpected final tracked change')
    for repo in (publisher, primary):
        no_operation(repo)
except BaseException:
    head = git(primary, 'rev-parse', 'HEAD').decode().strip()
    if head in (P, F):
        (primary / rel).write_bytes(original if head == P
                                   else git(primary, 'show', F + ':' + rel) + suffix)
    print('STOP: preserve recovery files at', backup, file=sys.stderr)
    raise
else:
    shutil.rmtree(backup)
    print('PASS: origin/main and primary main are F; suffix and every untracked file preserved')
PY
```

The primary suffix SHA-256 is `67d9bee52555f3a6951997d3f661636952b44a159ea66af555dcb373e07c253b`. The script verifies that exact suffix before publication and verifies F's decisions plus that suffix afterwards. Its untracked manifest covers file bytes, symlink targets and modes. A failure after the primary update starts retains recovery files outside the checkout and restores the suffix against whichever guarded head was reached.

## In Progress

Nothing running. No real checkout edit, commit, merge or publication was performed. The review is complete; correction and another publication-safety review belong to the supervisor's repair workflow.

## Queries

### PRINCIPAL-PUBLICATION - Correct the two new queue envelopes before publication

**Context:** Candidate F preserves the source content and rehearses safely, but its newly added [Chez-moi messages](/Users/krisbrown/.local/state/ki/worktrees/ki-principal-integrate/+/_WORK/ki.chezmoi/messages.md:3), lines 3 and 4, violate the required message format. This is a new fault, unlike the owner's unchanged state-schema fault. The smallest correction was verified in scratch and leaves both instruction bodies, sender identities and original times intact.

**Query:** Will you have the repair owner correct only these two envelopes and submit the resulting candidate for a fresh review before publication?

**Options:**

a) (recommended, confidence high - the scratch-only correction clears the sole new finding) Correct only those two envelopes to the [work-package message format](/Users/krisbrown/.local/share/ki/harnesses/knowledgeislands/ki-agentic-harness/skills/governance/ki-work-package/references/standards-work-package.md:114), preserving instruction bodies and sender metadata and putting colon-containing timestamps in the body; make one deliberate repair commit and request another blind review. Keep F unpublished.

b) Leave F unpublished and postpone the integration.

### 🤖 → 👤 Handoff to supervisor · blocked · since 11:08 BST

👤 1 with you · 🅿️ 0 parked

- [with you] PRINCIPAL-PUBLICATION - repair two envelopes and submit a new candidate · owner · since 11:08 BST

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
