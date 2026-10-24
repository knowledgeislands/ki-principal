# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › worktree-flow

**🤖 → 👤 Handoff to supervisor · Run report at 03:52 BST · last mark 03:08 BST**

---

## Done

- Wrote [design/worktree-flow.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/worktree-flow.md), committed in ki-principal as `92496234` by explicit path, not pushed. The landed check passed: only that path is in the commit and nothing is left unstaged.
- Count at 03:49 BST, read-only, across 57 repositories with no fetch:
  - 1 linked worktree, wow-rules2 in the harness. It is live and clean, 0 ahead and 0 behind.
  - No unmerged or stale branches.
  - 1 merged branch left behind: `feat/design-v1` in apps-knowledgeislands.info, already A-PRUNE in ki.chezmoi.
  - 2 stashes in ki-principal, already STASH-DROP here.
  - Mains ahead of origin: 2 at 03:49 BST, ki-principal by 1 and legal-principal by 2. At 03:47 BST it was 11 mains holding 81 commits, and nine of them were pushed in the two minutes between.
- Why work gets stuck, from today's examples: finishing a run and integrating its work are separate steps with separate owners, and nothing shows the gap between them.
  - lane-triage's branch waited 1 h 39 min to be merged.
  - checker-gaps' worktree waited 2 h 4 min behind a red baseline.
  - The check loop died for about an hour, and with it the only view of what was waiting.
  - Gaps in the worktree setup caused false audit failures, and the WORKTREE-GATE gap blocks commits from a worktree altogether.
- Three new findings:
  - `ki agent close` checks for worktrees in the run folder, but runs actually put them under `~/.local/state/ki/worktrees/`. A run can therefore close with its worktree still in place, and wow-rules2's is there now.
  - `ki agent status` crashed at 03:48 BST. Another session was part-way through editing `tools-ki`, and `ki` runs from that working copy.
  - The Observatory never reads worktrees.
- Six fixes, each with its owner and check:
  - F1: a run integrates, removes its worktree, then reports.
  - F2: one path and branch name per run, `agents/<run>/worktrees/<agent>.<repo>` on `run/<run>/<agent>`.
  - F3: `ki agent status` and the Observatory show each worktree with its ahead and behind counts, uncommitted files and age, and flag stranded ones.
  - F4: State of play sweeps at each mark and only reports what it finds.
  - F5: the registry recognises a linked worktree.
  - F6: `tools-ki` is edited only off its primary checkout, as GREEN-MAIN already requires for the harness.
- No code was changed, no records were made, and nothing was removed. The temporary folder is empty.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- The fixes go to their owners as `messages.md` lines, under HANDOFF-AS-MESSAGE, once Kris answers: the harness, `tools-ki` and apps-observatory.local.
- Both queries are medium confidence, so they go to blind review before reaching Kris.

## Queries

### WORKTREE-INTEGRATE - Let a run land its own work on local main

**Context:** Today's stuck work sat on branches because each run stopped at its branch and the merge waited for a separate launch. Under `ki-git`, merging into `main` is a separate decision that a run does not make unless it has been given the authority. F1 gives that authority, within limits: fast-forward only, into the local primary checkout, only after the gates pass on the rebased range, inside the short Git write window, and never a push.

**Query:** Should every worktree run have standing authority to fast-forward its own branch into local `main` before it reports?

**Options:**
a) (recommended, confidence medium - it removes the cause of every stuck case today, but its effect on ki-principal's busy write window is untested) Yes, under F1's conditions. A run that cannot fast-forward cleanly keeps its worktree and reports it as stranded.
b) No. Runs stop at their branch, the coordinator launches a merge run, and F3 and F4 make waiting branches visible.

### WORKTREE-START - Start the trial before the tooling lands

**Context:** F1 and F4 work by rule alone. F2, F3, F5 and F6 need `tools-ki` and harness changes, which take a few runs. Until F3 lands, worktrees show only in State of play's sweep and in run reports. Until F5 lands, an audit in a ki-principal worktree reports false failures. The trial would therefore start in the code repositories, where harness runs already work this way.

**Query:** Should the worktree trial start now on F1 and F4, with the tooling delivered during it, or wait until F2, F3 and F5 have landed?

**Options:**
a) (recommended, confidence medium - code-repository runs already use worktrees safely, but visibility stays thin for the first days) Start now in the code repositories under F1 and F4, and add ki-principal's long runs once F5 lands.
b) Wait until F2, F3 and F5 have landed, then start everywhere the checkout-isolation course names.
