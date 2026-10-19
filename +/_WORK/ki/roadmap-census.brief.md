# Brief: roadmap-census

You are a detached background agent for KI > SoP, the territory's State of play coordinator (work package `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/`). Kris, 19 October: "the roadmap keep growing, I need to get this sorted, help me get there". Your job is the evidence and a plan, not the clean-up. Read-only: write nothing but your report and commit nothing.

Read first: `ki-work`, `ki-work-roadmap`, `ki-next` and `ki-coordination`; the territory inventory in `Admin/Governance/Known Lands.md`; and the package's `state.md` and `decisions.md` (the burn-down focus of 14 October, GO-AHEAD).

## Task

1. Census. For every repository in the territory with a roadmap (`docs/roadmap/` or `Streams/Roadmap/`), count open records by status and horizon (Now, Next, Later, held, triage or unadopted, Awaiting review). Use `ki work status` or `ki` roadmap commands where they work; fall back to reading front matter.
2. Flow. From Git history over the last four weeks, count records added and records closed or pruned per week per repository, and name the biggest sources of inflow: which works, sessions or habits create records (for example run reports capturing follow-ups, handoffs, intake, audits).
3. Diagnosis. Say why it grows: inflow exceeding closure, records parked in Awaiting review, holds that never come back, duplicates across repositories, records no live work owns, records that should be ideas or queries rather than work.
4. Candidates. List concrete records that look closable now: duplicates, superseded, already delivered, Awaiting review ready for acceptance, stale ideas. Give evidence for each; do not act.
5. Plan. Propose a short burn-down plan Kris can approve in a few decisions: an intake rule to slow inflow, a cap or WIP limit, an owner for each lane (existing works such as ki.tools-burndown, ki.observatory, ki.chezmoi, ki.mac-studio-setup), a first wave of closures, and how progress is measured each week.

## Report

Report to the path your run packet names, as an owner report. Under Done: the census table (repository, open, by horizon, added and closed in four weeks), the diagnosis in a few lines and the candidate list grouped by repository. Raise each decision Kris must take as a query with Context, Query and lettered Options, a) recommended with its confidence. Keep queries to the few that unlock the burn-down.
