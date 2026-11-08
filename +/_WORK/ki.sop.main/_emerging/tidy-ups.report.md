# [KI > SoP](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.sop.main/work.md) › tidy-ups

**🤖 → 👤 Handoff to supervisor · Run report at 04:08 GMT · last mark 00:03 GMT**

---

## Done

- OBSOLETE-DROP: dropped seven queries that commits prove obsolete, each with a decisions-log line citing its commit, checked fresh (ki-principal `04da59f3`): HOST-GUARDS, STORE-REPAIR, TRIAGE-OWNERS and DOCK in [ki.prj.estate-factorisation](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.estate-factorisation/decisions.md), CLI006-PLAN in [ki.prj.agent-host](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.agent-host/decisions.md), WARP-HANDLER in [ki.prj.chezmoi](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.chezmoi/decisions.md) and VA-AREA-TITLES in [ki.prj.baseline-rollout](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.baseline-rollout/decisions.md). The other eight of the 15 were ki.sop.main's own and were already gone. The five that rest only on sol evidence are under Queries; nothing was done to them. `rumdl` clean.
- BRANCH-SWEEP: on sol, only `ways-of-working-learn` in apps-knowledgeislands.info was left; it is merged into `main`, so it was deleted locally with `git branch -d`. The six other named branches (three in ki-agentic-harness, one in tools-ki, two in tools-rig) and their worktrees no longer exist on sol or on GitHub. The copy of `ways-of-working-learn` on GitHub is merged too, but deleting it means pushing a deletion to GitHub, which this run's push rule does not cover, so it is left (query REMOTE-LEARN).
- UNMERGED-STRAYS: read-only comparison done; list below. Nothing deleted.
- UNTRACKED-REPORTS: read-only check done. All 11 reports were committed to ki-principal in `7109c998` ("chore: baseline", 4 November), so the question has gone. The only uncommitted reports in those works now are two recent Ways of working naming reports from a live session. Nothing deleted.
- KA-CLOSE: stopped and nothing changed. `ki agent close knowledge-acquisition` refused because two runs, `gov209-link` and `title-fix`, stopped without finishing (both were re-run, and the re-runs finished). Every other check passed. Under the close-out rule, KA-CLOSE-GATE is now a query in ki.sop.main's discussions (below).
- ORCA-CLOSE-HOME: sent MSG-a4f3326e to personal.reg.inbox-sol (inbox `e1489ee7`). It asks the Inbox to take the four open Orca questions (ORCA-UPSTREAM, THREADS-TRY, THREADS-SWEEP, THREADS-FR), the trial log and the handover note. SCOPE-SPLIT's questions and the `orca-adapter` branch are with ki.reg.guilds under ORCA-HOME, and the launcher proposal stays with Ways of working. The Orca folder stays on hold until the Inbox acknowledges the message.
- ESTATE-CLOSE: steps 1 and 2 of [the retirement note](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.sop.main/_emerging/estate-factorisation-retirement.md) sent as seven lines: HOST-WRITES to agent-host, RIG-REFS to mac-studio-setup and to chezmoi, OBS-ACTIVATION to observatory, DEPS-HOLD to ways-of-working, KI-RELEASE to tools-burndown and RECEIVER-ROLLOUT to baseline-rollout. ALIAS-OWNERS and GOVERNANCE are parked in ki.sop.main's discussions. Each line is recorded under Outbound as awaiting ACK (ki-principal `826ea06b`). Step 3, the close itself, still waits for your acceptance. The chezmoi copy of RIG-REFS is not yet in Git (see In Progress).
- PRE-REBASE-REF: left as is. This run ran on sol, and the branch exists only on terra.
- TIDY-UPS section removed from ki.sop.main's discussions. OLD-ORPHANS is back as its own short query, with KA-CLOSE-GATE beside it. The outcomes are logged in decisions (`826ea06b`). `rumdl` clean, commit hooks passed, all three commits are on GitHub.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- The RIG-REFS line to ki.prj.chezmoi (MSG-dc59c0e6) is written in chezmoi's `messages.md`, but the `chezmoi-fold` run was editing that file at the same time, so this run left it out of its own commit. The coordinator should check that `chezmoi-fold` routes or commits it. Its Outbound record in ki.sop.main is committed.
- PRE-REBASE-REF waits for a run on terra. That run checks whether old harness commit `57226cdea` holds anything `main` does not, then deletes `fold-harness/pre-rebase-main`.
- The Orca folder closes once personal.reg.inbox-sol acknowledges MSG-a4f3326e. The Estate factorisation close waits for the seven acknowledgements and for your acceptance.

Unmerged branches (read-only):

| Branch | Ahead / behind `main` | Is its change on `main`? | Owner | Suggested disposition |
| --- | --- | --- | --- | --- |
| ki-agentic-harness `ki-e2e` (local only) | 2 / 244 | No: draft `ki-e2e` skill (801 lines) | ki.prj.ways-of-working, whose E2E queries are open | Keep until those queries are answered |
| ki-agentic-harness `orca-adapter` (local only) | 2 / 249 | No: draft `ki-delegation-orca` adapter | ki.reg.guilds, under ORCA-HOME (7 November) | Keep for the guild |
| apps-observatory.local `z-retirement/observatory-20261030` (local and GitHub) | 3 / 4 | No: Z retirement evidence under `docs/evidence/` | ki.prj.observatory | Keep as evidence, or merge if Observatory wants it on `main` |
| ki-principal `run/wow-mod011-approved-candidate-mpg8sgz6` (local and GitHub) = GitHub `wip/z-retired-mod011-20261030`, same commit `996bcf64` | 2 / 1761 | No: [KI-PRINCIPAL-MOD-011](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-MOD-011-amend-work-model-assigned-package-cascade.md) is still `draft` | ki.prj.ways-of-working | Keep one of the two names; the candidate is 1761 commits behind and would need redoing |
| tools-ki `wow-close-done-2` and `wow-day-impl-fix-5`; tools-rig `run/wow-accept-rig-056` and `run/wow-rework-rig-056`; chezmoi `tower-nudge-retire` | n/a | Not on sol or GitHub | Unknown | Check on terra |

## Queries

### OBSOLETE-SOL - Drop the five Mac Studio queries that rest on sol evidence

**Context:** Under OBSOLETE-DROP, five queries in [ki.prj.mac-studio-setup](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.mac-studio-setup/handover.report.md) look settled, but the only evidence is what that work's handover report says about sol, with no commit behind it. RIG-TRIAGE: every record done, cancelled or moved to ideas. FW-LIVE: the firewall is live. SOL-SOURCES: all source folders are on sol. SOL-HNR-HARNESS: the HNR harness is installed. SOL-KI-CONFIG-DRIFT: the drift is cleared. What a machine reports can change later, so you kept these for your word.

**Query:** Should ki.prj.mac-studio-setup drop these five as settled, logging each against its handover report?

**Options:**

a) (recommended, confidence medium - the handover report states each was settled, but nobody has checked sol again since) Drop all five with one decisions-log line each, citing the handover report.

b) First have a run on sol check each one again, then drop only those that still hold.

### KA-CLOSE-GATE - Let the Knowledge acquisition close pass two superseded runs

**Context:** [ki.prj.knowledge-acquisition](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.knowledge-acquisition/work.md) passes every close-out check: it is finished, its decisions are homed, no query is open, it has no worktree and nothing queued, and the only line in its `messages.md` asks for this close-out. But the tool that archives its runs, `ki agent close`, refused: two runs, `gov209-link` and `title-fix`, stopped without finishing on 17-18 October. Both were re-run as `gov209-link-2` and `title-fix-2`, and those finished. Nothing was deleted. This query has not been blind reviewed.

**Query:** May a State of play run close it, telling `ki agent close` to accept those two stopped runs as superseded?

**Options:**

a) (recommended, confidence medium - each stopped run has a re-run that finished, and Git keeps the folder) Yes: close with `--accept-exited` for the two runs (never `--reconciled`), then delete the folder in one commit.

b) Leave the folder until you open that work's thread.

### REMOTE-LEARN - Delete the merged branch on GitHub

**Context:** apps-knowledgeislands.info's `ways-of-working-learn` is fully merged into `main`. Its local copy is gone, but the copy on GitHub is still there. Deleting it needs a push that removes the branch, which this run's push rule (fast-forward pushes of `main` only) does not cover.

**Query:** Should the GitHub copy of `ways-of-working-learn` be deleted?

**Options:**

a) (recommended, confidence high - the branch is merged, so deleting it loses nothing) Yes: a run deletes it with `git push origin --delete ways-of-working-learn`.

b) Leave it on GitHub.

### OLD-ORPHANS - Where the old orphaned repositories live

**Context:** You kept this open when you agreed TIDY-UPS. The old orphaned repositories that were to be kept through the Mac Studio move have no checkout under `~/workspaces` and no bundle in OneDrive. If they lived only on a retired disk or Mac, the last copies may be gone. Nothing is dropped while this is unknown.

**Query:** Where do the old orphaned repositories live now, or are they gone?

**Options:**

a) (recommended, confidence high - reviewed: only you can say whether another copy exists) You name the location or confirm they are gone, and ki.prj.mac-studio-setup records the answer before closing its query.

b) Treat them as lost and close the query.
