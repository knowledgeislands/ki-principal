---
note_type: streams/design
updated: 2026-10-20T02:50:00Z
author: Written with Claude
---

# Worktree flow

**Owner:** Kris Brown · **Owning repository:** knowledgeislands/ki-principal · **Owning work:** `ki.ways-of-working` · **Date:** 2026-10-20

Design note WORKTREE-FLOW. Kris answered CHECKOUT-ISOLATION on 20 October: "happy to do a trial, and I think probably work trees make sense. The problem is, it's hard to see any progress using the normal tooling. Is there an approach to making work trees work better? What I don't like is how stuff gets stuck on them." This note counts today's worktrees, branches and stacks across the estate, explains why worktree work gets stuck with today's examples, and proposes six fixes, each with its owner and check, so the trial [checkout isolation](checkout-isolation.md) recommends can start. It changes nothing. It graduates when Kris has answered its queries and the fixes have gone to their owners as `messages.md` lines under HANDOFF-AS-MESSAGE; it is then deleted in the same change.

## Contents

- [Findings in brief](#findings-in-brief)
- [Today's count](#todays-count)
- [Why work gets stuck](#why-work-gets-stuck)
- [The fixes](#the-fixes)
- [How the trial runs](#how-the-trial-runs)
- [Queries](#queries)

## Findings in brief

1. Worktree work gets stuck at the end, not in the middle. Every stuck case today was finished work on a branch that nobody integrated: no run integrates its own work, so the merge is a separate step someone must launch, and nothing shows the branch waiting.
2. Nothing in the normal tooling shows a worktree. `ki agent status` lists agents, not worktrees; the Observatory reads each primary checkout's branch and ahead and behind counts, never `git worktree list`. Kris's MAIN-NOT-WORKTREES on 18 October ("Are you just working on work trees? ... you should be able to just work on the main") was the same complaint: progress on a worktree is invisible until it lands.
3. The one safety net that exists looks in the wrong place. `ki agent close` refuses while `~/.local/state/ki/agents/<run>/worktrees/` holds anything, as `ki-delegation` places worktrees, but runs actually create them under `~/.local/state/ki/worktrees/<repo>/<agent>`, and [checkout isolation](checkout-isolation.md#merge-model-for-b) proposed a third form. A run can finish, report and close with its worktree still standing.
4. Two setup gaps make a worktree run stop short of a commit: a red baseline blocks its commit, and the registry does not know a linked worktree, so `ki repo audit` fails there (WORKTREE-GATE in ki.tools-burndown, WORKTREE-AUDIT here).
5. The tooling that would show progress runs from a live working tree. At 03:48 BST `ki agent status` failed with a `SyntaxError` because another session was part-way through editing Granola acquire code in the `tools-ki` primary checkout, which the `ki` command runs from. This is row 11 of the checkout-isolation incident map again, in `tools-ki` rather than the harness.
6. The estate is clean of stuck worktrees right now; unpushed mains are the larger stuck mass, and they clear only by pushing, which worktrees do not change.

## Today's count

A read-only census at 03:47 and 03:49 BST of the 57 repositories under `~/workspaces/*/` with `git worktree list --porcelain`, `for-each-ref`, `rev-list --left-right --count` against local `main`, `git cherry` and `git stash list`. No fetch was made; remote counts are as of each repository's last fetch, ki-principal's at 03:48 BST.

| Kind | Count at 03:49 BST | Items |
| ---- | ------------------ | ----- |
| Linked worktrees | 1, live | ki-agentic-harness `wow-rules2` under `~/.local/state/ki/worktrees/ki-agentic-harness/`, created 03:46 BST, 0 ahead and 0 behind, clean, its agent running |
| Unmerged branches | 0 | none with a commit not on its `main` |
| Merged branches left behind | 1 | apps-knowledgeislands.info `feat/design-v1`, 0 ahead and 30 behind, last commit 18 October, no worktree; A-PRUNE in ki.chezmoi |
| Stale branches (over 30 days, unmerged) | 0 | none |
| Stashes | 2 | ki-principal `stash@{0}` and `stash@{1}`; STASH-DROP here |
| Mains ahead of `origin/main` | 2 at 03:49 BST, 11 at 03:47 BST | 03:49: ki-principal 1, legal-principal 2. 03:47: 81 commits across 11 mains, ki-principal 44 and acquire 19 among them; nine were pushed in the two minutes between |

ki.chezmoi's wt-survey found no linked worktree at 03:19 BST either. The `dotfiles` repository lists `~/.local/share/chezmoi` as its worktree because its working tree lives there; that is its main worktree, not a linked one, and is not counted.

## Why work gets stuck

Today's examples, from this work's decisions log:

| # | What happened | Stuck for | Why |
| - | ------------- | --------- | --- |
| 1 | lane-triage delivered KI-HARNESS-GOV-219 and KI-HARNESS-GOV-224 to Awaiting review on harness branch `lane-triage` at 00:55 BST, "not yet integrated" | 1 h 39 min, until green-main fast-forwarded it at 02:34 BST | The run stopped at its branch; the merge was a separate queued launch, and the take-stock pause at 02:01 BST held it |
| 2 | checker-gaps finished its candidate in a retained worktree at 00:30 BST, "blocked before commit by four hook tests that fail on unchanged harness `main`" | 2 h 4 min, until green-main | A red baseline: the run's own work was fine, but the gate it must pass was broken on `main` |
| 3 | The coordinator's check loop stopped after 00:27 BST; "nothing was checked or launched between 00:55 and 01:57 BST" | about 1 h | Nothing outside the coordinator's own loop shows a waiting branch, so when the loop died, so did the visibility |
| 4 | ci-green's harness audit showed nine FAILs that were "worktree setup, not source" | one run's judgement | The registry, project skill links and `node_modules` assume the primary checkout, so a worktree audit lies until they are fixed |
| 5 | ki.tools-burndown parked WORKTREE-GATE: "`ki repo audit` blocks commits from linked worktrees on exact path registration" | parked since 01:57 BST | A run in a worktree in a repository with that gate cannot commit at all |
| 6 | The wow-rules2 run now live: its launch record names `workdir` as the ki-principal primary checkout, and its harness worktree sits under `~/.local/state/ki/worktrees/`, not the run folder | live | The launcher does not know the worktree exists, so neither `ki agent status` nor the close gate can see it |
| 7 | `ki agent status` failed at 03:48 BST while a session edited `tools-ki` | until that edit lands | `ki` runs from the `tools-ki` primary checkout's live tree |

The pattern: work gets stuck when finishing a run and integrating its work are two steps owned by different actors, and stays stuck because no view lists what is waiting between them.

## The fixes

Six fixes, each small, in the order they matter. Owners deliver them; this note captures no records, and each goes to its owner as a `messages.md` line once Kris answers.

| # | Fix | Owner | Check |
| - | --- | ----- | ----- |
| F1 | **Integrate, then remove, then report.** A worktree run's last step before `DONE` is the merge model's integrate, verify and dispose: rebase onto local `main` with no fetch, run the gates on the rebased range, `git merge --ff-only` into the primary checkout inside the short write window, check the commits are reachable from `main`, `git worktree remove`, `git branch -d`. A run that cannot (conflict, red gate, contested primary checkout) keeps its worktree and reports `stranded: <reason>` as a blocking query, never a quiet `DONE`. Pushing stays as it is. | KI Agentic Harness: `ki-delegation` Coordination isolation line and authority footer; `ki-git` names this as the default `worktrees-with-local-integration` grant for runs | `ki agent close` refuses while the run's worktree or any `run/<run>/*` branch exists; the coordinator checks the report's integrated commit with `git merge-base --is-ancestor <commit> main` |
| F2 | **One place and one name.** Every run worktree lives at `~/.local/state/ki/agents/<run>/worktrees/<agent>.<repo>` on branch `run/<run>/<agent>`, the place `ki-delegation` already names and the close gate already checks. `ki agent launch --worktree <repo>` creates it, clones `node_modules`, links the project skills and records it in the launch record. Checkout isolation's merge model and the current `~/.local/state/ki/worktrees/` practice both move to this form. | `tools-ki` (launch option, launch record); KI Agentic Harness (`ki-delegation` path line, checkout-isolation's merge model) | A `tools-ki` CLI test launches with `--worktree` and asserts the path, branch and launch record; `ki agent status` marks any linked worktree outside the form `orphan` |
| F3 | **Show every worktree.** `ki agent status` gives each run's worktrees beneath its agents as `- [worktree] <agent> · <repo> · run/<run>/<agent> · <ahead> ahead, <behind> behind · <dirty> uncommitted · last commit <age>`, and `[stranded]` in place of `[worktree]` when its agent is no longer running. `ki agent status --worktrees` lists every linked worktree and non-default branch across the estate, run-owned or not. The Observatory's repositories evidence adds `git worktree list --porcelain` and the same counts, so Kris sees them on the page Kris already reads. | `tools-ki` (status); apps-observatory.local (evidence package and repositories view) | A `tools-ki` test with a fixture worktree asserts the line and the stranded flag; an Observatory evidence test asserts worktrees appear with their counts |
| F4 | **State of play sweeps at each mark.** State of play runs `ki agent status --worktrees` and the clean-down reads at each mark and shows each finding in its banner as `[stranded]`, `[branch]`, `[stash]` or `[unpushed]` with its owning work, whatever its age. It removes nothing: integrating goes to the owning work, and any removal, a stash drop or a branch deletion, goes to Kris by name under the clean-down rule. This is a report of Git state, not the date-based draft sweep Kris declined in STALE-SWEEP. | KI Agentic Harness: `ki-coordination` State of play mark step | The `ki-coordination` rubric flags a State of play mark with no sweep line |
| F5 | **A worktree gives the same verdict as the primary checkout.** The registry resolves a linked worktree to its registered repository, so REPO-REG-1, RUNTIMES-2 and the commit gate pass there; this is WORKTREE-GATE's a) and WORKTREE-AUDIT's recipe made unnecessary. | `tools-ki` | A full `ki repo audit` in a fresh `--worktree` checkout gives the same verdict as the primary checkout, as a contract test |
| F6 | **Tools run from committed code.** `tools-ki`, whose code every session runs, joins the harness under GREEN-MAIN: edits only in a worktree, integrated by fast-forward once its tests pass, so a half-made edit never breaks `ki` for everyone. | KI Agentic Harness: `ki-git` working-copy rule, extending its harness sentence to `tools-ki`; `tools-ki` `AGENTS.md` | At each mark the `tools-ki` primary checkout has no uncommitted changes under `src/`; F4's sweep reports one that does |

F1 and F3 answer Kris's two complaints directly: F1 stops work getting stuck, F3 makes it visible while it runs. F2 is what lets the tools find a worktree at all. F4 catches whatever F1 misses. F5 and F6 remove today's two causes of a run stopping short.

Neither worktrees nor these fixes clear an unpushed `main`; the push policy under PUSH-NOT-WITH-YOU stands, and F3 and F4 only show the stack.

## How the trial runs

The trial is the checkout-isolation course: worktrees for every writing run in code repositories, and for long multi-file runs in ki-principal, coordinators and short work-package runs staying on primary `main` under MAIN-NOT-WORKTREES. F1 and F4 need no code: a brief rule and a State of play step can start with the trial, the census in this note serving as the sweep until F3 lands. F2, F3, F5 and F6 are `tools-ki` and harness changes delivered during the trial. The trial measures, over one week: worktrees stranded at a mark, minutes from a run's last commit to its work reaching `main`, and false audit findings in worktrees. It ends with a short note back to Kris.

## Queries

### WORKTREE-INTEGRATE - Let a run land its own work on local main

**Context:** Today's stuck work sat on branches because the run stopped at its branch and the merge waited for a separate launch. `ki-git` treats integrating into `main` as a separate decision that a run does not hold unless granted. F1 grants it: fast-forward only, into the local primary checkout, after the gates pass on the rebased range, inside the short write window, and never a push.

**Query:** Should every worktree run carry standing authority to fast-forward its own branch into local `main` before it reports?

**Options:** a) (recommended, confidence medium - it removes the cause of every stuck case today, but its effect on ki-principal's busy write window is untested) Yes, under F1's conditions; a run that cannot fast-forward cleanly keeps its worktree and reports it stranded. b) No; runs stop at their branch, the coordinator launches a merge run, and F3 and F4 make waiting branches visible.

### WORKTREE-START - Start the trial before the tooling lands

**Context:** F1 and F4 work by rule alone; F2, F3, F5 and F6 need `tools-ki` and harness changes that take a few runs. Until F3 lands, worktrees show only in State of play's sweep and in run reports, and until F5 lands an audit in a ki-principal worktree reports false failures, so the trial would start in code repositories, where the harness runs already work this way.

**Query:** Should the worktree trial start now on F1 and F4, with the tooling delivered during it, or wait until F2, F3 and F5 have landed?

**Options:** a) (recommended, confidence medium - code-repository runs already use worktrees safely, but visibility stays thin for the first days) Start now in code repositories under F1 and F4, adding ki-principal's long runs once F5 lands. b) Wait until F2, F3 and F5 have landed, then start everywhere the checkout-isolation course names.
