---
note_type: streams/design
updated: 2026-10-20T01:40:00Z
author: Written with Claude
---

# Checkout isolation

**Owner:** Kris Brown · **Owning repository:** knowledgeislands/ki-principal · **Owning work:** `ki.ways-of-working` · **Date:** 2026-10-20

Design note for CHECKOUT-ISOLATION. Kris asked on 20 October, "CHECKOUT-ISOLATION - can we look at this more?", after [take-stock](take-stock-2026-10-20.md) recommended a) a `ki` commit helper with a per-session index, worktrees for code build runs, serial record-editing runs in a knowledge base and audits reading committed state, and the blind review recommended b) a worktree for every coordinator session and writing run in every repository, with serial verified merging. This note maps each collision in the retros to its Git mechanism, measures b) on scratch worktrees of ki-principal and ki-agentic-harness, tests a per-session index against the real hooks, and recommends a staged course. It applies nothing. It graduates when Kris has answered CHECKOUT-ISOLATION and each accepted change has a record or a decision; it is then deleted in the same change.

## Contents

- [Findings in brief](#findings-in-brief)
- [Incident map](#incident-map)
- [Measurements](#measurements)
- [Per-session index and commit-landed check](#per-session-index-and-commit-landed-check)
- [Merge model for b)](#merge-model-for-b)
- [Recommended course](#recommended-course)
- [What it needs](#what-it-needs)

## Findings in brief

1. The retros report twelve collision incidents besides the unpushed stack. The shared index caused four, `index.lock` six and the live working tree read by audits three; one was a work-ownership overlap, and several had more than one cause. Five more were the unpushed stack. None was a ref lock on `HEAD`.
2. b) prevents nine of the twelve and narrows two; a) as take-stock framed it prevents four and narrows seven, leaving the lock waits in knowledge bases only narrowed.
3. A private index through `GIT_INDEX_FILE` is unsafe in a shared checkout as proposed. In the scratch worktree it caused two silent reverts that every hook passed: the next ordinary commit from the shared index reverted the private commit, and a private index seeded before another session committed reverted that session's change.
4. The safe form of a) is a pathspec commit, `git add -- <paths>` then `git commit -- <paths>`. Git builds a temporary index from `HEAD` plus the named paths, so it sweeps nothing and leaves the shared index consistent. It still holds the shared `index.lock` for the whole hook run.
5. Worktrees are cheap: each takes under a quarter of a second, a checkout of 38 MB for ki-principal and 21 MB for the harness, and `node_modules` cloned in about 1.5 seconds at almost no disk cost. Gates in a worktree give the same verdict as in the primary checkout once two machine-local gaps are closed: the project skill links and the registry entry.
6. Neither a) nor b) clears the unpushed stack. b) still lands every commit on the one `main`, so the stack is a push-policy matter.

## Incident map

Mechanisms: **index** is the shared Git index; **lock** is `.git/index.lock`; **live** is the live working tree read by audits or hooks; **stack** is the unpushed stack; **claim** is a work-ownership overlap with no Git cause. "Partly" means the change narrows the incident but does not remove it.

| # | Incident, as its retro reports it | Mechanism | a) | b) |
| - | --------------------------------- | --------- | -- | -- |
| 1 | ki's staged files swept into ki.timelines' `e0489e42` | index: ki staged with `git add`, then a pathspec-less commit took everything staged | prevents | prevents |
| 2 | gov035-deliver's renames swept into ki.baseline-rollout's `0836bcae` | index: a `git mv` stages both sides; a commit naming only some paths leaves the rest for the next plain commit | prevents, if the helper commits both sides of a rename | prevents |
| 3 | ki's four-try lock retry loop | lock | partly: a bounded retry inside the helper, contention remains | prevents: each worktree has its own index and lock |
| 4 | ki.chezmoi's roadmap-gaps reported PERSONAL-DOTFILES-UE-076 failing from a half-saved edit, costing a decision and fix-076-steps; theme-renames did the same on PERSONAL-DOTFILES-UE-084 | live | prevents, through serial record-editing runs and audits on committed state | prevents |
| 5 | ki.mac-studio-setup: another session's `index.lock` in ki-principal blocked `git rm` | lock | partly | prevents |
| 6 | ki.observatory: `index.lock` failures in apps-observatory.local | lock | partly; prevents if build runs there use worktrees, as a) proposes for code | prevents |
| 7 | ki.observatory: the Claude chat's KI-OBSERVA-BRG-005 and VIS-027 landed with roadmap-audit failures in the middle of obs-build-vis022 | live: the run's audit judged other sessions' files | partly: committed-state audits still see committed failures | prevents until the run rebases, then shows them at integration |
| 8 | ki.observatory dropped obs-build-brg005 under OBS-CLAIM-FOUR | claim: Kris gave those records to the chat | neither | neither |
| 9 | ki.portable-specifications: lock waits at 00:40, staged moves swept, and `git commit -- <paths>` with untracked files failing silently so mark commits did not land until 23:52 | lock, index and a commit that did not land | prevents the sweep and the silent failure, partly the lock | prevents the sweep and the lock; the silent failure needs the landed check either way |
| 10 | ki.timelines: a lint-staged backup failed while another session was committing | lock, or lint-staged's backup stash, whose `refs/stash` every worktree shares (not verified) | partly | prevents the lock cause; not the shared stash ref |
| 11 | A harness edit in the harness main checkout broke every island's pre-commit for two minutes (ki.ways-of-working, ki.tools-burndown) | live: every island reads the harness through a development link to its main checkout | prevents, since a) puts code-repository runs in worktrees | prevents |
| 12 | ki.ways-of-working: a stale `index.lock` and other sessions' staged files in ki-principal | lock and index | partly: prevents the sweep, narrows the lock | prevents |
| 13 | ki-principal's unpushed stack of 62 commits, 11 of them ki.portable-specifications'; ki.tools-burndown's ten repositories unpushed; ki.timelines' hold commit among others'; Acquire's six commits under `33b4244`; ki.ways-of-working's stacked commits | stack | neither | neither: integrated commits still stack on `main` |

Tally across rows 1 to 12: index 4 (1, 2, 9, 12), lock 6 (3, 5, 6, 9, 10, 12), live 3 (4, 7, 11), claim 1 (8); row 13 groups the five stack incidents. a) prevents 4 rows (1, 2, 4, 11), narrows 7 (3, 5, 6, 7, 9, 10, 12) and leaves 1 (8); b) prevents 9 (1 to 7, 11, 12), narrows 2 (9, 10) and leaves 1 (8). The ref lock on `HEAD` appears in none: in one checkout, concurrent commits meet `index.lock` first, and Git's ref update checks the old value, so a lost race fails loudly rather than silently.

## Measurements

Scratch worktrees were created detached at the current `main` of each repository, under the run's temporary directory, and removed afterwards. Neither main checkout was touched; both were clean and level with their state at the start.

| Measure | ki-principal | ki-agentic-harness |
| ------- | ------------ | ------------------ |
| `git worktree add` | 0.17 s | 0.22 s |
| Checkout size | 38 MB, 538 tracked files | 21 MB, 1,326 tracked files |
| Administrative files in `.git/worktrees/` | 88 KB | 204 KB |
| `node_modules` | absent; the pre-commit refuses ("the commit gate cannot run") | absent; the same |
| `node_modules` by APFS clone (`cp -cR`) | 1.49 s, 157 MB apparent, blocks shared | 1.62 s, the same |
| Pre-commit with one staged change | passes in 1.38 s | passes in 2.40 s, staged-skill audit included |
| Focused `ki-repo-kb` audit | same verdict as the primary checkout | not applicable |
| Full `ki repo audit` | 8 more failures than the primary checkout: RUNTIMES-2 seven times and REPO-REG-1 once | not run |
| Test suite | not applicable | 20 s; 1,302 pass and the 4 hook tests that fail on `main` fail, the same result |
| `git worktree remove --force` | 0.61 s | 0.66 s |

The data volume holding the worktree root is 94% full with 54 GiB free, so worktrees are affordable but stale ones should be swept.

What assumes the primary checkout path:

- **`ki` registry.** `~/.local/state/ki/registry.toml` holds one `path` per repository, the primary checkout. A worktree fails REPO-REG-1, and the registry does not know it as the same repository.
- **Project skill activation.** `.agents/skills/` and `.claude/skills/` are ignored symlinks written into the primary checkout; a worktree has none, so RUNTIMES-2 fails seven times and an agent there sees only the 13 user-level skills, without `ki-repo-kb` and the rest.
- **The harness development link.** `~/.local/share/ki/harnesses/knowledgeislands/ki-agentic-harness` and `locals.toml` point at the harness main checkout, so every island's hooks and audits read its live working tree. That caused row 11. A harness edit in a worktree is invisible to the islands until integrated, which is the protection wanted; `ki`'s development write interlock refuses a development write from a different worktree from the linked one.
- **Obsidian.** The vault is the primary checkout; `.obsidian/workspace.json` is ignored. Edits in a worktree are invisible to Obsidian until integrated. A fast-forward into the primary checkout refuses only if Kris has uncommitted edits to the same files.
- **OneDrive source stores.** The registry binds `sources` to an absolute OneDrive path per repository, so every worktree shares the one store. Nothing collides through Git, but nothing is isolated either, and a worktree reaches the store only once the registry knows it.
- **Pre-commit gates.** The island and harness hooks resolve `node_modules` from `git rev-parse --show-toplevel`, so they need `node_modules` in each worktree; `core.hooksPath` is shared and works unchanged. The harness hook already audits a snapshot from `git checkout-index`, which is the committed-state pattern a) wants.
- **`ki agent launch`.** `workdir` may be a worktree. `--repo` defaults to the working directory's repository, which is then the worktree, so the work folder, prompts and adopted state files would land on the run's branch rather than in the coordinator's package; a coordinator must pass `--repo` with the primary checkout. Runs already record `workdir` in their launch packet, and `ki agent close` already refuses while `worktrees/` holds anything. There is no `--worktree` option and no integrate command.
- **Existing practice.** Harness runs already use worktrees under `~/.local/state/ki/worktrees/`: checker-gaps and green-main hold two now, and banner-on-state pushed `6baab0b0` from one. `ki-git` already names `worktrees-with-local-integration` among its four working approaches.

## Per-session index and commit-landed check

Each test ran in the scratch ki-principal worktree, on its detached `HEAD`, with the real hooks.

| Test | Result |
| ---- | ------ |
| Commit with `GIT_INDEX_FILE` seeded by `git read-tree HEAD`, while another session's file is staged in the shared index | Hooks honour the private index; the commit took only its own path. |
| The next ordinary `git commit` from the shared index | Silently reverted the private commit's change: the shared index still held the old content, so it showed as staged. Every hook passed. |
| A private index seeded before another session's commit, committed after it | Silently reverted the other session's change: the tree came from the stale private index. Every hook passed. |
| `git commit -- <paths>` naming an untracked file | Fails: "pathspec did not match any file(s) known to git". This is the portable-specifications silent failure without its error filter. |
| `git add -- <paths>` then `git commit -- <paths>` | Took only the named paths, left the other session's staged file staged, and left the shared index consistent with `HEAD`; 1 s. |
| The same with a rumdl-fixable file | lint-staged's fix landed in the commit and the shared index stayed clean. |
| A `git mv` committed by its new path only | The deletion stayed staged in the shared index for the next plain commit to sweep, as in row 2. |
| Locks held during a pathspec commit | `index.lock` and `next-index-<pid>.lock` were held for the whole hook run, about a second here and several minutes under tools-rig's full Bats hook. |

So a private index is practical only if it is seeded from `HEAD` under the index lock immediately before committing and the shared index is refreshed afterwards, which is what `git commit -- <paths>` already does. The helper should use the pathspec form, not `GIT_INDEX_FILE`.

A commit-landed check is practical with the current hooks and costs three read-only commands after the commit: `HEAD` moved from its recorded value; `git diff-tree --no-commit-id --name-only -r HEAD` equals the intended paths, both sides of each rename included; and `git status --porcelain -- <paths>` is empty, which also proves no lint-staged fix was left unstaged. It catches every failed or partial commit in the tests above except the two silent reverts, which only removing pathspec-less commits from shared checkouts prevents.

## Merge model for b)

1. **Create.** The launcher makes a worktree under `~/.local/state/ki/worktrees/<run>-<date>/` on branch `run/<run>` from the primary checkout's `main`, clones `node_modules` with `cp -c`, links the project skills and registers it as a linked worktree of the registered repository.
2. **Work.** The run commits on its branch; its gates run in its worktree and judge only its own tree.
3. **Integrate.** One integrator per repository at a time, under a per-repository lock: in the worktree, `git rebase main` with no fetch; run the gates on the rebased range, because hooks do not run during a rebase (the island audit over the changed paths, the harness test suite for code); then in the primary checkout `git merge --ff-only run/<run>`.
4. **Verify.** The primary `HEAD` equals the branch tip, the primary checkout's status is as it was before the merge, and the commits named in the run's report are reachable from `main`.
5. **Dispose.** `git worktree remove`, then `git branch -d`, never `-D`; a conflict or a red gate stops the integration and is reported with the worktree kept.
6. **Push.** Unchanged: fast-forward only, own commits only, by the session with push authority.

Costs observed or implied:

- In ki-principal, 89% of the paths changed since 18 October lie in each work's own `+/_WORK/<id>/` folder, so rebases there rarely conflict. The shared hot files are index and Project notes: `Admin/Governance/Decisions/Decisions.md` was changed by 9 works, and `Streams/Projects/Projects.md` and three Project notes by 5 or 6 each.
- The peak was 131 commits in one hour on 19 October at 23:00. Serial integration at about 3 to 5 seconds each fits, but every one of them becomes a queued step instead of a commit.
- A coordinator in its own worktree breaks things that work today: the work package, `messages.md` routing through State of play and Obsidian all read the live primary checkout, so a routed line or a state rewrite would reach nobody until integrated. It also reverses MAIN-NOT-WORKTREES (Kris, 18 October: "you should be able to just work on the main").

## Recommended course

A staged mix, confidence medium: the mechanisms are measured directly, but knowledge-base integration cadence and the pilot's live collision rate are untested.

1. **Now: a safe commit path for every session in a shared checkout.** A `ki` commit helper that adds the named paths, both sides of each rename, commits by pathspec, retries `index.lock` a bounded number of times and runs the landed check; and a `ki-git` rule that no session in a shared checkout makes a pathspec-less commit or commits from a private `GIT_INDEX_FILE`. This removes rows 1 and 2, the sweeps and silent failure in rows 9 and 12, and the silent reverts measured above, and narrows the lock waits in rows 3, 5, 9, 10 and 12.
2. **Now: worktrees for every writing run in code repositories,** with the merge model above: the harness, `tools-ki`, `tools-rig`, `tools-techne` and the apps. This formalises what harness runs already do and removes rows 6 and 11. Harness edits are never made in the harness main checkout.
3. **Now: audits that judge a run read a committed snapshot,** as the harness hook already does with `git checkout-index`, and record-editing runs in one knowledge base stay chained with `--wait-for`. This removes row 4 and narrows row 7.
4. **Pilot, one week: worktrees for long, multi-file knowledge-base runs** (renames, migrations, bulk record edits) in ki-principal, while coordinators and short work-package runs stay on primary `main` under MAIN-NOT-WORKTREES. The lock waits in ki-principal (rows 3, 5 and 12) are the measure: if they persist, extend b) to every knowledge-base writing run; coordinators stay on main unless the work package moves out of Git.
5. **Separately: the unpushed stack** is a push-policy matter (O4 in take-stock), not checkout isolation.

## What it needs

From `ki` (`tools-ki`), as handoffs once Kris answers, with no records captured now under CAPTURE-GATE:

- A commit helper as in the recommended course, refining take-stock's C2: the pathspec form, not `GIT_INDEX_FILE`.
- `ki agent launch --worktree`, creating the worktree, cloning `node_modules` and linking the project skills, with `--repo` defaulting to the primary checkout of the worktree's repository; and an integrate step running the merge model under a per-repository lock.
- Registry resolution of a linked worktree to its registered repository, so REPO-REG-1 and RUNTIMES-2 pass there, and so source stores resolve.

From the harness:

- `ki-git`: the pathspec-commit rule, the landed check, both sides of a rename, no private index in a shared checkout, and `worktrees-with-local-integration` as the default for writing runs in code repositories.
- `ki-delegation` and `ki-coordination`: briefs for code-repository runs name a worktree; coordinators pass `--repo` with the primary checkout; audits that judge a run read committed state.

From Rig:

- A doctor finding for stale worktrees under `~/.local/state/ki/worktrees/` and for disk headroom, which is at 94% used.
- tools-rig's fast pre-commit subset (take-stock's R2), since the shared `index.lock` is held for the whole hook run and the full Bats hook holds it for minutes.
