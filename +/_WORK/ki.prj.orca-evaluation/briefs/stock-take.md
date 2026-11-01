# Brief: stock-take of ki.prj.orca-evaluation

Work: ki.prj.orca-evaluation (KI > Techne > Orca evaluation), ki-principal at /Users/krisbrown/kis/knowledge-islands/ki-principal. Run name: stock-take. Agent: Orca worker under the Project's Run.

## Why

Kris, 1 November 2026: "I've been using Orca a little while now, and I'm really comfortable with the fact that I think it is the way forwards. So maybe we can get through this pretty quickly. I'm wondering if it's actually anything to tweak, and if some of these things that we are tweaking are part of ways of working really. ... let's take stock and really look to see where there are some things that are consolidated now."

## Goal

Propose a consolidated work package: fewer, sharper queries; a trial plan reshaped for Orca already being Kris's chosen way forward; and a clean split between what this Project owns (how Orca is used, Orca evidence, Orca feedback upstream) and what belongs to ki.prj.ways-of-working (the work method itself: launcher contract, ask/escalation rule, worker publish rule, ids and report practice).

## Read

- This package: `+/_WORK/ki.prj.orca-evaluation/` (work.md, state.md, queries.md, decisions.md, design/orca-trial-plan.md, design/orca-trial.md).
- Evidence reports: `~/.local/state/ki/agents/ki-prj-orca-evaluation/*.report.md`.
- ki.prj.ways-of-working package `+/_WORK/ki.prj.ways-of-working/` (work.md, state.md, queries.md, decisions.md, and design/orca-subagents/, design/question-prompt/), to see what it already owns or has decided about Orca (ORCA-FIT, launcher, wake, asks).
- The current method at ki-agentic-harness main: skills/change-management/ki-coordination/references/standards-coordination.md and the ki-delegation background-runs standard, for what is already settled.
- The Project note Streams/Projects/orca-evaluation.md.

## Produce

One report at `~/.local/state/ki/agents/ki-prj-orca-evaluation/stock-take.report.md` with:

1. For each of the ten open queries (ORCA-RUN-REBIND, TRIAL-UNITS, TRIAL-PUBLISH, TRIAL-ASK, TRIAL-PRACTICE, NEST-TRIAL, NEST-FR, ORCA-IDENTITY-LEAK, ORCA-SIDEBAR-FR, LABEL-FIRST): a verdict - keep, merge (with which), overtaken (by what, with evidence), or transfer to ki.prj.ways-of-working (why it is method) - one line of reasoning each.
2. The proposed remaining queries, each fully written in owner-report form (tag, Context, Query, lettered Options with a) recommended and a confidence with reason), in plain English.
3. A reshaped plan: what the trial still needs to prove now Orca is the way forward, as the fewest units, in order; and whether the ORCA-SKILL proposal (an Orca launcher under ki-delegation and ki-coordination) should come forward now.
4. Draft message lines (not sent) for ki.prj.ways-of-working's messages.md for each transfer.
5. A draft of one bundled Orca upstream request covering: question card line breaks (authorised by Kris 31 Oct), a supported read-only settings export, sidebar hidden-item discoverability, name-first rows while monitoring, and a parent/display-name declaration for outside sessions - marking which are authorised and which await Kris.
6. Proposed edits to work.md scope and state.md next steps, as text.
7. Decisions in decisions.md that a durable home now wholly carries (candidates to strike).

## Authority

Read-only. Do not edit, commit, stash or push in any repository; do not send messages or contact Orca upstream; do not call `orca orchestration` verbs other than heartbeats and worker_done for your own task. Write only the report file above. If a question only Kris can answer arises, put it in the report as a query rather than asking.

## Report

End with an owner report shape: Done, In Progress, Queries. Then call worker_done with the report path.
