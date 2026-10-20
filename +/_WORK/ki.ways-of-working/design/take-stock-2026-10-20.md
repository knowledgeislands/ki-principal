# Take stock: ways of working, 20 October 2026

**Owner:** Kris Brown · **Owning repository:** knowledgeislands/ki-principal · **Owning work:** `ki.ways-of-working` · **Date:** 2026-10-20

Design note for TAKE-STOCK: Kris asked at the hold on 20 October to "take stock on what's working well and what's not working well so we can improve our ways of working". Ten works wrote a retro; this note merges them into themes, ranks what is not working by how many works raised it and what it cost, and groups the proposed changes by owner. It applies nothing. Each incident is cited as its retro reports it and was not re-verified. The note graduates when Kris has answered its queries and each accepted change has a record or a decision; it is then deleted in the same change.

## Contents

- [Sources](#sources)
- [Working well](#working-well)
- [Not working](#not-working)
- [Would change](#would-change)

## Sources

1. [ki](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/design/retro-2026-10-20.md) - State of play, on hold for take-stock.
2. [ki.baseline-rollout](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.baseline-rollout/design/retro-2026-10-20.md) - on hold for take-stock.
3. [ki.chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.chezmoi/design/retro-2026-10-20.md) - on hold for take-stock.
4. [ki.mac-studio-setup](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.mac-studio-setup/design/retro-2026-10-20.md) - on hold for take-stock.
5. [ki.observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.observatory/design/retro-2026-10-20.md) - on hold for take-stock.
6. [ki.portable-specifications](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/retro-2026-10-20.md) - on hold for take-stock.
7. [ki.timelines](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.timelines/design/retro-2026-10-20.md) - on hold for take-stock.
8. [ki.tools-burndown](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown/design/retro-2026-10-20.md) - on hold for take-stock.
9. [ki.ways-of-working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/retro-2026-10-20.md) - this work, with worker.
10. [kb.regular.acquire-intake](/Users/krisbrown/workspaces/personal/acquire/+/_WORK/kb.regular.acquire-intake/design/retro-2026-10-20.md) - Acquire, on hold for take-stock.

Live works with no retro: [ki.agent-host](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.agent-host/state.md) (with worker since 19 October 23:34 UTC) and [kb.personal-tower](/Users/krisbrown/workspaces/personal/personal-principal/+/_WORK/kb.personal-tower/state.md) (handoff to supervisor since 19 October 18:28 UTC). Every other work folder in the Capitals was already on hold before take-stock and wrote none.

## Working well

1. **Blind independent review changes outcomes, not just confidence** - 8 works (ki, baseline-rollout, chezmoi, mac-studio-setup, observatory, portable-specifications, timelines, tools-burndown). obs-review-5 found the Observatory's Git view chose unpushed commits by ahead count, wrong after a merge, fixed in `86f2a13` with a regression test; on CLI006-CONFIRM a review found a stale `CONFIRM_DESTROY_AGENT_HOST` export could destroy a clean host, so the query was parked.
2. **Overnight autonomy at high confidence moves real work** - 7 works (ki, baseline-rollout, mac-studio-setup, observatory, portable-specifications, timelines, tools-burndown). HIGH-APPLY settled 8 of 11 tools-burndown queries without Kris; observatory moved seven records to Awaiting review; the threshold held where it should, with SPEC-TEXT kept for Kris.
3. **Short owner answers to recommended options turn into work fast** - 3 works (baseline-rollout, mac-studio-setup, acquire-intake). "Anything high confidence can be done." moved eight queries, and within about 20 minutes five raise runs had captured triage records in ten repositories.
4. **Chaining same-repository runs with `--wait-for`** - 3 works (mac-studio-setup, observatory, portable-specifications). Drafts 0.4 to 0.8 and five reviews ran between 00:07 and 00:59 with no idle gap and no clashing edits.
5. **Single-hop routing through State of play** - 3 works (ki, tools-burndown, acquire-intake). ki.chezmoi repointed the KB-DOTFILES-UE-098 link within about ten minutes, which unblocked a prune in tools-burndown.
6. **Read-only surveys before building** - 3 works (chezmoi, observatory, timelines). next-scan turned an apparently empty overnight queue into nine safe runs and found three delivered records still marked draft.
7. **The work package and detached runs survive the coordinator** - 3 works (ways-of-working, timelines, acquire-intake). lane-triage and checker-gaps finished and reported while the coordinator was gone; Kris's words logged before launch made every resume straightforward.
8. **Runs stay in scope and lead with evidence** - 2 works (observatory, acquire-intake). The before-and-after smoke run showed the red browser check predated KI-OBSERVA-VIS-041, so the fix changed only the check.

## Not working

Ranked by works raising it, then by cost. Root-cause tags: tooling, standard, coordinator behaviour, shared checkout, owner interface.

1. **Sessions collide in shared checkouts** - 9 works (all but baseline-rollout). Cost: blocked and swept commits, false failures that caused wrong work, a dropped run and pushes stranded across about ten repositories. Incidents: ki's staged files were swept into ki.timelines' `e0489e42` and gov035-deliver's renames into ki.baseline-rollout's `0836bcae`, with a four-try lock retry loop; chezmoi's roadmap-gaps reported a failure on KB-DOTFILES-UE-076 from another run's half-saved edit, costing a decision and a fix run (fix-076-steps) that found nothing; observatory dropped obs-build-brg005 under OBS-CLAIM-FOUR; ki-principal's unpushed stack reached 62 commits, 11 of them portable-specifications'; Acquire's six commits were stranded under another session's `33b4244`. Root cause: shared checkout, with tooling (no per-session index or worktree) behind it.
2. **Nothing outside the session wakes the coordinator** - 5 works (ki, baseline-rollout, timelines, tools-burndown, ways-of-working). Cost: about four hours of overnight autonomy lost across three works. Incidents: baseline-rollout's three reviews finished at 00:35 and were read at 02:04, and wave1-review sat unread from 19:43 to 23:27; tools-burndown's waiter overslept 00:33 to 01:43; OVERNIGHT-AUTONOMY lapsed after 00:27 in ways-of-working; ki's disowned waiter could never wake it; timelines ran two watchers after compaction. Root cause: tooling, with coordinator behaviour in how waiters are armed.
3. **Building outruns Kris's acceptance and answers** - 5 works (ki, baseline-rollout, chezmoi, mac-studio-setup, observatory). Cost: sixteen observatory records and six mac-studio records await acceptance; chezmoi has 20 open queries and baseline-rollout 15, against the audit's warning at 8; at-screen steps for sol and terra keep growing. Incidents: chezmoi's ten RAT queries have waited since 19 October; PROJECT-CLOSE reached high confidence but stays Kris's choice. Root cause: owner interface, with coordinator behaviour (no work-in-progress cap).
4. **`ki agent` launch and control friction** - 6 works (mac-studio-setup, observatory, timelines, tools-burndown, ways-of-working, acquire-intake). Cost: relaunches and spent turns most nights. Incidents: `ki agent queue` printed help and queued nothing; `--repo` naming the target repository failed until it named the work's own; prepared prompts failed with "has already run"; the Astra review started on the wrong model; acceptgit and acceptki stopped because the default footer forbids accepting and pruning; `ki agent send` failed with "invalid run"; stopping spec-sched meant killing its launcher by hand. Root cause: tooling.
5. **Claims and premises not checked before acting** - 5 works (observatory, portable-specifications, timelines, ways-of-working, acquire-intake). Cost: wrong work. Incidents: KB-ACQUIRE-005 and 006 were cancelled on a wrong premise and 005 restored under DROP-SCOPE; observatory briefs told runs to restart the service against its AGENTS.md, and two did; "add something about it to the SoP" was run as METHOD-READ when Kris meant GFM; two Summaries carried a wrong path and a wrong ownership claim; Kris's "skill extension" framing was in no work file when cited. Root cause: coordinator behaviour.
6. **Bookkeeping fails only at commit time** - 5 works (ki, mac-studio-setup, portable-specifications, timelines, tools-burndown). Cost: commits that silently did not land, redone commits and chains held up. Incidents: `git commit -- <paths>` with untracked files failed behind an error filter, so mark commits did not land until 23:52; a free-text line in `messages.md` failed the audit; briefs failed the pre-commit Markdown check; a combined receive subject broke the commitlint header limit; tools-rig's pre-commit runs the full Bats suite and held plan068 several minutes. Root cause: tooling, with coordinator shell slips.
7. **Times written without reading the clock** - 4 works (ki, chezmoi, portable-specifications, tools-burndown). Cost: low, but records and heartbeats were wrong, up to 13 minutes ahead. Root cause: coordinator behaviour.
8. **Package state drifts** - 3 works (ki, mac-studio-setup, baseline-rollout). Cost: audit warnings and stale Now lines. Incidents: Now said query-review-8 waited after it was received; an overgrown Now raised LIFECYCLE-3; `method_read` holds a time, not a revision (METHOD-READ); untracked `*.report.md` mirrors appeared in a work folder from an unknown writer. Root cause: standard and tooling.
9. **Fixes target the instance, not the class** - 2 works (chezmoi, portable-specifications). Cost: four fix-and-review cycles on KB-DOTFILES-UE-090 and three drafts on one validator claim. Root cause: standard (brief shape).
10. **The harness's own `main` goes red** - 2 works (tools-burndown, ways-of-working). Cost: estate-wide; a harness edit in the main checkout broke every island's pre-commit for two minutes, and the estate hook migration shipped while harness hook tests failed (HOOK-TESTS). Root cause: standard and shared checkout.
11. **Reviews are not actually blind** - 1 work (baseline-rollout), but it qualifies Working well 1 everywhere. Cost: every confidence lift may be anchored. Incident: each reviewer read `queries.md`, which shows the recommendation and its confidence, and all three recorded it. Root cause: standard.
12. **The owner interface is heavy and shifting** - 2 works (acquire-intake, ways-of-working). Cost: Kris's confusion ("I honestly don't know anymore") and fleet-wide refresh lines. Incidents: jargon-heavy record summaries; one link repoint took a decision, brief, run and report; banner and push rules changed three times in one evening; Acquire's push rule conflicts with the hold standard. Root cause: owner interface and standard.
13. **CAPTURE-GATE collides with acceptance** - 1 work (tools-burndown). Cost: KI-TOOL-KI-CLI-152 and 167 returned because the work they owe has no record. Root cause: standard.

## Would change

Deduplicated; the bracket names the Not working theme each fixes.

### Harness standard

- H1. Isolate writers: a worktree per writing session or build run in code repositories, one owning session per checkout per night otherwise, and audits that read committed state only [1].
- H2. Re-anchoring lists armed watchers and keeps exactly one per work package [2].
- H3. A work-in-progress cap: no new build or planning run while more than about eight records await acceptance or eight queries are open [3].
- H4. Wording-only queries on triage records take the recommended option at medium unless Kris objects, since adoption is the real checkpoint [3].
- H5. Reviewer briefs carry a masked copy of each query, Context and Query only, and keep `queries.md` off the reading list [11].
- H6. Fix and revise briefs sweep for the whole class of a finding across all files; a review loop stops when no must-fix remains and carries should-fix items to the owner [9].
- H7. Harness `main` green is a gate on every run; a red baseline stops the line; harness hook tests pass before any estate-wide hook rollout; harness edits are not made in the shared main checkout [10].
- H8. Rewrite `state.md`'s Now at each receive, not only at a mark [8].
- H9. An accept run may capture the follow-up records it needs under CAPTURE-GATE [13].
- H10. Briefs carry each target repository's standing rules by default, such as "never restart the Observatory service; say a restart is due" [5].

### `ki` CLI

- C1. An out-of-session coordinator wake for autonomy windows: a detached `ki agent` watcher that survives the session and resumes the coordinator when a run finishes [2].
- C2. A commit helper: per-session index (`GIT_INDEX_FILE`) or one add-and-commit step, adds untracked paths, then checks `git log -1` and status [1, 6].
- C3. `ki agent launch` per-role defaults for runtime, model and effort (a review lands on Codex at the strongest model), footer chosen from purpose (an accept run gets `--rules prune`) or a refused mismatch, and `--repo` resolving the work's own repository [4].
- C4. Working `ki agent queue`, `send`, `stop` and `dequeue`, and reusable prepared prompts [4].
- C5. `ki agent new` scaffolds briefs that pass the Markdown check, and `messages.md` lines are validated on write [6].
- C6. `method_read` records the harness revision, and run reports are not mirrored into work folders, or the closed list admits them [8].

### Rig

- R1. If C1 needs a scheduler, host the coordinator wake as a launchd job on the agent host [2].
- R2. tools-rig's pre-commit runs a fast subset; the full Bats suite runs before push [6].

### Coordinator style

- K1. Take every time from `date`, including decision timestamps [7].
- K2. Check every path, ownership claim and instruction premise against the records before it goes into a Summary or a brief; read back an ambiguous direction in one line before launching; log Kris's framing when stated [5].
- K3. Arm waiters only with `run_in_background`; one receive per commit subject; quote shell variables [2, 6].
- K4. Keep a tested launch line in each work package [4].
- K5. Batch one-line mechanical fixes into one run per turn rather than one run each [12].

### Kris's interface

- O1. Batched decision sittings by decision type, and one at-screen checklist per machine (sol, terra) carrying its acceptances [3].
- O2. Explain each decision in plain words: what it does for Kris and what happens if it is left [12].
- O3. Change method rules at a mark, in one batch, not several times an evening [12].
- O4. A standing push rule for repositories that need explicit authority, such as Acquire: a hold pushes the session's own commits [1, 12].
