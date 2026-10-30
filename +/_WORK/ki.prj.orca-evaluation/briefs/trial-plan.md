# Brief: trial-plan (ki.prj.orca-evaluation)

You are a background agent for the Knowledge Islands Project work ki.prj.orca-evaluation ("KI > Techne > Orca evaluation"), in ki-principal. Read the work package first: /Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.orca-evaluation/work.md, state.md and decisions.md, then the trial log /Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.orca-evaluation/design/orca-trial.md and the landscape report /Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/landscape-report.md.

Goal: draft the plan for the rest of the Orca trial, as a design note at /Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.orca-evaluation/design/orca-trial-plan.md.

The plan must:

- fit ORCA-REACH (Orca only on attended Macs, this package opting in by a logged decision, never on vega), WAKE-SESSION (prove `orca orchestration check --wait` as the native `wait`: one detached waiter at a time, bounded at five minutes, re-armed after each wake, no seen event lost, in both Claude Code and Codex) and WAKE-DURABLE (no Orca automations in the wake design);
- propose two or three concrete trial units, each with its repository, host, runtime, what it proves, its evidence and its pass criteria; the WAKE-SESSION proof is one of them; prefer units that are real, bounded work rather than synthetic ones, and say where each comes from;
- carry the plan069 lessons from the trial log (heartbeats, asynchronous ask, the ask timing out at ten minutes, worker_done reported failed when publication was blocked by the no-stash rule against lint-staged's backup stash) into each unit's risks;
- say what the ORCA-SKILL proposal (an Orca launcher under ki-delegation and ki-coordination) will need from the units' evidence;
- note what is still missing (the ORCA-FIT notes from ki.prj.ways-of-working have not arrived).

Do not dispatch anything through Orca, launch other agents or change anything outside this design note. British English, ASCII hyphens only. Commit only +/_WORK/ki.prj.orca-evaluation/design/orca-trial-plan.md by explicit path under ki-git, pull fast-forward only and push; never force or use --no-verify; stop on divergence.

Report: put the decisions Kris must make, starting with whether this package opts in to Orca dispatch for the trial, as queries in the owner-report shape: a `### <TAG> - <title>` heading, then Context, Query and Options with a recommended option first carrying its confidence and reason.
