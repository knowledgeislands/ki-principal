# Brief - orca-fit

Work: ki.prj.ways-of-working. Authority: ORCA-FIT design run, 2026-10-30, in decisions.md. Skill: ki-work-design (design stage only).

## Goal

Design how Orca fits the Knowledge Islands work model so each does what it does best, and explain the whole picture plainly to Kris, who said: "I don't quite get what's going on ... how we balance all these things up, how and where we're running, what work we're doing, how that works with the roadmaps, how that works with work packages."

## Read

- Work Process note: Pillars/Philosophy/Model/Processes/Work Process/Work Process.md
- ki-coordination, ki-delegation, ki-work-package, ki-work-roadmap skills; the orchestration and orca-cli skills; `orca orchestration --help` and subcommand help (read-only).
- Evidence of the first Orca trial: +/_WORK/ki.prj.mac-studio-setup/plan069.report.md (two questions answered through Orca; the third timed out because Orca cannot wake the coordinator; the brief's "never stash" collided with the lint-staged hook's backup stash; `check` shows titles only, bodies need `inbox --full`; no gates were used).
- Existing design notes here that touch launching, checkout isolation and coordination: design/checkout-isolation.md, design/agent-control-contract.md, design/coordination-lessons.md, design/work-model.svg.

## Starting proposal (test it, do not assume it)

Knowledge Islands is the durable layer: roadmaps say what work exists; the work package holds where one piece of work stands, its queries, messages and decisions, with Git as logbook; authority and acceptance stay with Kris. Orca is the live layer: launching workers, per-worker worktrees, task queue and dependencies, heartbeats and status, asks for operational questions, gates for owner decisions. Hand-offs: brief -> Orca task (ids recorded in state.md); worker_done -> receive into the package; owner-level asks -> queries.md plus an Orca gate; coordinator wake loop watches the Orca inbox. Workers never write the package; Orca chatter never goes into Git.

## Deliver, in design/

1. `orca-fit.md`: name each unit (roadmap record, work package, coordinator, run/worker, host, repository checkout, Orca run/task/dispatch/gate/message), its boundary, what it owns, and every hand-off; what changes in ki-agent vs Orca per host; what Orca should not be made to do; open choices with a recommended option each.
2. `orca-fit-explainer.md`: for Kris, no jargon first. One analogy, one layered picture (a Mermaid diagram plus a short worked example tracing KI-TOOL-RIG-CORE-069 from roadmap record to Orca worker to report to Kris's query), and a one-table "who owns what". Under two pages.

Use British English and ASCII hyphens only. Change nothing outside this package's design/ folder; no standard, skill, record, hook or Orca state changes. Commit only your two files by explicit path with `docs(work): ki.prj.ways-of-working orca-fit design`, pull --ff-only and push; normal hooks apply (the hook's own lint-staged backup stash is fine; never stash manually, never bypass). Report to +/_WORK/ki.prj.ways-of-working/reports/orca-fit.report.md with Done, In Progress and Queries in ki-coordination owner-report query form.
