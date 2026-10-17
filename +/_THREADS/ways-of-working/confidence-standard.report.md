# [Knowledge Islands model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Initiatives/knowledge-islands-model/knowledge-islands-model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working/ways-of-working.md) › confidence-standard

**Run report at 00:37 BST · last mark 22:34 BST**

---

## Done

- The change was already made and pushed when I got to it. Another session committed `b7ab7eff` at 00:34 BST, a minute after this run was launched. It delivers [KI-HARNESS-GOV-207](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-207-recommendation-confidence.md) to Awaiting review on origin/main. The commit's trailer reads `Claude Opus 5.5 (1M context)`, so it is not this run's.
- What it covers: option a) now reads `a) (recommended, confidence <level> - <reason>) <course>`, with the level `high`, `medium` or `low`. A destructive course resting on claims nobody has verified directly is never `high`. The reply-block entry still carries only option a)'s instruction. The change runs through the ki-pmo standard, its examples and DEFAULTS query, the generated output style, the run-prompt and the four authority footers, and the PMO-6 and RUN-4 judgment rubrics and both source reviews.
- I checked it independently at the current main: tests pass (1210), TypeScript is clean, and the ki-pmo generated surfaces match their source.
- I made no edits, commits or pushes in ki-agentic-harness. Opening a second record or re-editing the same files would have duplicated work that is already under review.
- Not done: step 3 of the brief, an automatic check that flags a recommended option with no confidence level. GOV-207 changed only the judgment rubrics. I stopped rather than change a candidate that another session has already put to review (CONFIDENCE-CHECK below).

## In Progress

Nothing is running.

Outstanding - no action requested now:

- GOV-207's own record notes one follow-up: a chezmoi-managed copy of the coordinator output style, if one is bound, needs its own review of `chezmoi diff`.
- Two runs did the same work because the coordinating thread launched this run as GOV-207 was being delivered elsewhere. This is worth checking before the next launch.

## Queries

### [CONFIDENCE-CHECK](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-207-recommendation-confidence.md) - automatic check for a missing confidence level

**Context:** The ki-pmo rubric already scans every thread report under `+/_THREADS/<run>/` for unlinked record identifiers (PMO-7, in `skills/change-management/ki-pmo/scripts/rubric/contexts/pmo.ts`). That makes a new mechanical PMO-11 cheap, at WARN level. It would flag any line in a report's Queries section that starts `<letter>) (recommended` without `, confidence high|medium|low - <reason>)`, skip fenced blocks, and give it a test in `pmo.test.ts`. To avoid flagging older reports, it would check only reports whose footer's top border shows an issued time on or after 2026-10-17T23:34Z. Conversational run reports have no such border, so they would go unchecked. GOV-207 is Awaiting review, so adding this now means changing a candidate already under review. **Query:** Should the automatic check be added to KI-HARNESS-GOV-207 before it is accepted, or left out? **Options:** a) (recommended, confidence medium - the scan is already in place and the check is small, but the date cut-off leaves conversational reports unchecked) add PMO-11 to KI-HARNESS-GOV-207 in a fresh harness run, then send GOV-207 back to Awaiting review b) accept KI-HARNESS-GOV-207 as it stands, with confidence checked only by judgment rubrics

```text
CONFIDENCE-CHECK

Launch a ki-agentic-harness run to add a mechanical WARN item PMO-11 to KI-HARNESS-GOV-207 (/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-207-recommendation-confidence.md). It flags any recommended option in a thread report's Queries section that lacks ", confidence high|medium|low - <reason>)", skipping fenced blocks and checking only reports whose footer was issued on or after 2026-10-17T23:34Z. Add a test in pmo.test.ts, regenerate the ki-pmo rubric, then return GOV-207 to Awaiting review.
```

```text
╭─ run report · 2026-10-17T23:37:30Z ──────────────╮
│                                                  │
│  █▀▀▄ █  █ █▀▀▀ █  █   · thread busy             │
│  █▀▀▄ █  █ ▀▀▀█  ▀█▀   · running or queued work  │
│  █▄▄▀ █▄▄█ ▄▄▄█   █    · lines below say which   │
│                                                  │
╰──────────────────────────────────────────────────╯
```

- [waiting] CONFIDENCE-CHECK
- [committed] this report in ki-principal, pushed
- [unknown] the run's other agents; the thread confirms its own state
