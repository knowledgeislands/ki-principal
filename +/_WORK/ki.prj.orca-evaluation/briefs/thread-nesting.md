# Brief: thread-nesting (ki.prj.orca-evaluation)

You are a background agent for the Knowledge Islands Project work ki.prj.orca-evaluation ("KI > Techne > Orca evaluation"), in ki-principal. Read /Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.orca-evaluation/work.md and the trial log /Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.orca-evaluation/design/orca-trial.md first.

Kris's observation, 30 October 2026: "I noticed that when Orca is running subagents, it spins up them in the list of agents in the project view. I wonder if there's a way to show any subagent threads effectively under the parent one." Kris's screenshot (if still present): /private/tmp/claude-501/-Users-krisbrown-workspaces-knowledge-islands-ki-principal/4494702a-2c84-4952-9f6e-22e768c3ecb6/images/2.png. It shows the hnr-principal project view in Orca on terra: coordinator threads (Claude Code, Opus) and the background runs they launched (Codex, gpt-6.1-sol, and Claude runs) listed flat, side by side, under the main worktree, with no parent-child grouping.

Goal: find out whether, and how, Orca can show a coordinator's background runs nested under, or visibly grouped with, the coordinator thread that launched them.

Investigate, read-only:

- what Orca itself offers: the `orca` CLI help (`orca --help` and its subcommands, `orca orchestration --help`), the orca-cli and orchestration skills installed for Claude Code, Orca's docs and changelog, and its local state under ~/Library/Application Support/orca/ (read only; never edit it). Look for parent/child or task-DAG relations, worker-start and dispatch metadata, worktree or folder contexts, session naming, tags, pinning, grouping, collapsing or filtering in the project view;
- how runs reach the list today: `ki agent launch` starts a detached claude or codex session, which Orca discovers as a separate agent. Say whether it is the Orca hooks or session discovery that lists them, and whether anything a launcher can pass (an environment variable, a session name, a parent id, a working directory or worktree) would let Orca group them;
- whether dispatching through `orca orchestration worker-start` (as plan069 did) already gives the nesting.

Do not change Orca, ki agent, chezmoi or any configuration, and do not launch agents. Do not commit anything.

Report: what is possible now, what would need a launcher change (ki agent, under ki.prj.ways-of-working, or the Orca launcher proposal under ORCA-SKILL here), and what would need a feature request to Orca, each with evidence. Put any decisions Kris must make as queries in the owner-report shape: a `### <TAG> - <title>` heading, then Context, Query and Options with a recommended option first carrying its confidence and reason. British English, ASCII hyphens only.
