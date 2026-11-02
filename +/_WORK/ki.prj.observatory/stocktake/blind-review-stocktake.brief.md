# Brief: blind review of six Observatory decisions

You are an independent reviewer. Form your own view from the facts below and from the repositories (read-only); do not read any `queries.md`, `decisions.md` or `*.report.md` in `+/_WORK/`. The options are listed in no particular order and no option is preferred. Do not edit, commit, push or send anything.

Repositories: `/Users/krisbrown/kis/knowledge-islands/ki-principal` (the Capital, public on GitHub), `/Users/krisbrown/kis/knowledge-islands/apps-observatory.local` (the Observatory, a local read-only operations site listening on 127.0.0.1), `/Users/krisbrown/kis/knowledge-islands/tools-ki`, `/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness`.

For each question give: your choice, confidence (high, medium or low) with a one-line reason, anything in the facts you found wrong, and any better option.

## 1. Where the published report history is decided

Facts: two Observatory reports from a 29 October away run name Humans Not Robots jobs and work. They are in the Capital's public Git history; one is still in the current files (moved into `+/_WORK/ki.prj.observatory/reports/` on 1 November, which committed it again). The Observatory work has three open questions on it (who the audience is, how to respond to exposure, and whether to make the whole `knowledgeislands/ki-principal` repository private) and a message from Ways of working asking it to decide before any push; that push has since happened through ordinary syncing. Ways of working (`ki.prj.ways-of-working`) holds a parallel question on the same history; on 30 October Kris asked for an independent review before answering it, and that review exists. Question: should the Observatory's three questions and the hold be decided as one decision with Ways of working's? Options: (x) fold them into Ways of working's question, the Observatory retiring its three once that work acknowledges, changing nothing meanwhile; (y) move the whole matter to KI State of play (`ki.sop.main`), since making the repository private affects every work in the Capital; (z) keep the Observatory's three here and answer them separately now.

## 2. Which new tool next (after an Acquire area)

Facts: diagram notes - Kris (29 October) wants to pin comments on design diagrams (Archify HTML in a work's `design/`) and have them reach the worker as feedback; the Observatory already sends feedback into a work's `messages.md`. Opener button - a work explorer that serves a work's opening line by state with a copyable launch command (21 October); `ki agent prompts` already prints openers. Options: (x) diagram notes first, opener after; (y) opener first as smaller, notes after; (z) plan both together as one slice.

## 3. Plan for the Observatory's Host area

Facts: a Rig status JSON reader exists but the Observatory's Bridge does not use it; an earlier independent review advised keeping that parked while a Machine view is only an idea. Kris decided on 31 October each Mac syncs every 15 minutes, sol leading Knowledge Islands, Personal and Legal, and that the Observatory watches rather than syncs. Scheduled jobs should show when a run found problems. Later asks: live agent state from Claude Code/Codex hooks; Claude account scores (log not yet built). Options: (x) one bounded plan now covering Rig state, expected host sync from the seats map and scheduled-run problems, with hooks and account scores as later slices, nothing built until Kris approves; (y) wait until host sync has run supervised for a week, then plan; (z) plan only scheduled-run problems now.

## 4. How failed scheduled runs become visible

Facts: HNR email routing asked (28 October) whether the Observatory should read the Failures section of each Route Triage run summary, or the job wrapper should report a `findings` result (a chezmoi change via ki.prj.chezmoi). Its route-triage runs record `ok` even when the summary lists failures (6 of 15 reviewed). The Observatory's automation spec (`apps-observatory.local/docs/specs/automation.md`) already accepts and ranks `findings` and never reads a run's free text. Specimens stay on terra and hold mail details. Options: (x) wrapper reports `findings`; Observatory only shows it; (y) Observatory parses the Failures section itself, with tests over specimens read in place.

## 5. One design pass

Facts: open design items are: preparing remaining convergence choices against the delivered five-area layout; whether to drop or trim a ten-commit Git list that overlaps newer lists (a review found it holds otherwise missing history); a non-blocking Mermaid-label hardening investigation with no shown bypass; the Known Lands chart's look reserved for Kris; and how island maturity/health from the CLI should show. Nothing changed since 29 October; nothing else waits on them. Kris's standing instructions: lose nothing until he approves a consolidation; converge on the design step by step with his go. Options: (x) one pass with Kris covering convergence choices, the commit list and the Known Lands look/condition, Mermaid follow-up parked; (y) leave all parked until the design thread asks.

## 6. 5G Emerge checkout identities

Facts: strict estate reads fail on four 5G Emerge checkouts (under `/Users/krisbrown/kis/humans-not-robots/`) that declare other identities; the Observatory reads around them and names them. Fixing checkouts is not Observatory work. HNR has a main State of play `hnr.sop.main` and a 5G Emerge one `hnr.sop.5ge`. Whether the identities are wrong or intended is unverified. Options: (x) one line to hnr.sop.5ge, then drop it here; (y) one line to hnr.sop.main; (z) keep it here until someone checks whether the identities are intended.

## Report

Write to `/Users/krisbrown/.local/state/ki/agents/ki-prj-observatory/blind-review-stocktake.report.md`, one section per question, plain British English. End with DONE.
