# Brief: guild-transfers

From ki.sop.main (Knowledge Islands State of play), run `guild-transfers`. Work in `~/kis/knowledge-islands/ki-principal` and `~/kis/knowledge-islands/ki-agentic-harness`.

## Authority

Two lines from ki.reg.guilds (7 November 2026), carrying Kris's decisions, logged in `+/_WORK/ki.sop.main/decisions.md`:

- MSG-da83a96f SOP-BUNDLES, Kris (TRANSFER-SOP-QUERIES a): send HOLD-STATES (with HOLD-TIDY) and METHOD-BATCH, with their two design notes, to ki.reg.guilds as message lines; the guild asks them and lands the harness run.
- MSG-8125375d ORCA-HOME, Kris (ORCA-HOME a): the guild takes the sixteen Orca adapter queries (ORCA-SKILL-KIND and the ORCA-LAUNCHER set), ki.prj.orca-evaluation's SCOPE-SPLIT four method questions and the harness orca-adapter branch; Orca usage evidence and feedback to the Orca team go to the Inbox under ORCA-CLOSE-HOME. Route the adapter items to the guild.

## Task

1. SOP-BUNDLES: in `+/_WORK/ki.sop.main/discussions.md`, find HOLD-STATES, HOLD-TIDY (it may be folded into HOLD-STATES) and METHOD-BATCH, and their two design notes (search `+/_WORK/ki.sop.main/` focus folders). Add one line per query at the top of `## Inbound` in `~/kis/knowledge-islands/ki-agentic-harness/+/_WORK/ki.reg.guilds/messages.md`, format `- 2026-11-07 · <TAG> · from ki.sop.main · <HH:MM GMT> · <the query's Context, Query and options, condensed but complete, with its recommendation> · design note: <path>`. Move each design note into the guild's package (`+/_WORK/ki.reg.guilds/` in the harness, a focus folder matching how the guild keeps notes) with `git mv` across repos not possible, so copy into the harness and `git rm` from ki-principal. Then remove those query sections from ki.sop.main's discussions.md.
2. ORCA-HOME: find the sixteen Orca adapter queries (ORCA-SKILL-KIND and ORCA-LAUNCHER set) and SCOPE-SPLIT's four method questions: look in `+/_WORK/ki.prj.orca-evaluation/` (discussions.md, messages.md, state.md, focus folders), ki.sop.main's discussions and messages, and anywhere `grep -rl ORCA-LAUNCHER ~/kis/knowledge-islands/*/+/_WORK` finds them. Route each to the guild the same way, one line per query, and note the harness branch `orca-adapter` (check `git -C ~/kis/knowledge-islands/ki-agentic-harness branch -a | grep orca`) as now the guild's in one line. Remove routed queries from where they sat only if that package is ki.sop.main or has no active session (ki.prj.orca-evaluation: record the disposition in its decisions.md and remove the queries from its discussions.md; change nothing else there). Leave Orca usage evidence and Orca-team feedback where they are; list them in your report for ORCA-CLOSE-HOME.
3. ACK both lines at the top of the guild's `## Inbound`: `- 2026-11-07 · ACK MSG-da83a96f · from ki.sop.main · <time> · <n> queries and two design notes sent` and the same for MSG-8125375d.

## Commit

In each repository: pull with `git -c pull.autostash=false -c rebase.autoStash=false pull --ff-only`; `rumdl fmt` then `rumdl check` on touched Markdown; commit by explicit path (git add new files first), lower-case Conventional Commit subjects such as `docs(work): ki.sop.main send SOP-BUNDLES and ORCA-HOME queries to ki.reg.guilds`, trailer `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`; push fast-forward only. Never stash, rebase, reset, force or `--no-verify` in any primary checkout; on divergence stop and report. A refused commit is a failure to report. Touch no other session's uncommitted files.

## Report

Write your report where the launcher's footer says: Done, In Progress, Queries; list every query routed with its source, every design note moved, and each commit.
