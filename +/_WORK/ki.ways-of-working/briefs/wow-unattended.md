# wow-unattended

## Goal

Draft a `ki-work-design` brief for unattended working, at `+/_WORK/ki.ways-of-working/design/unattended-work.md`, that Kris can point at while it is drafted. Brief only: reviews and the merged report come later.

## Kris's words (25 October, before sleep)

"I want you to think about this in terms of how we deal with unattended work for a fixed period of time, such as effectively going through the queries and planning ahead of time so that you can do that unattended. In particular, I think this ties into also the general point I made before in the ways of working ... about unattended working and flags like that being put on roadmap items and such." "for unattended periods of time, there's no mark. So, basically, as you're going into an unattended period, it should be a mark that's taken so that when I come back after that unattended period, we can effectively walk through all the changes that have landed." "if there's any packed questions or queries before I go, it's important that they're unpacked and questioned, and ... continuously look at the roadmap and progress things as much as you can ... progress as much of the roadmap as possible related to your area." "in the unattended working mode, we need to make sure that the git repos are resynced ... every change that's finished ... or every 15 minutes ... if we do get [collisions], that they get resolved as part of the unattended work."

## Read

This work's `messages.md` (UNATTENDED-AND-DUE-DATES, AWAY-GRANT, WAKE-SUBSTRATE, UNWRITTEN-RULES), `decisions.md` (the away grant entries), `queries.md` (COMMIT-CADENCE, PACKAGE-PUSH, COORD-COMMANDS, DRAIN-END), and in ki-agentic-harness the `ki-coordination` standard (unattended windows, Pushing beneath other sessions, Keeping primary checkouts current), `ki-delegation` (authority footers) and `ki-work-roadmap` (record fields).

## Cover

The window's life cycle: entry (grant recorded, mark struck, interactive pass, packed queries split, a plan of what will run), during (commit cadence, sync after each finished change and every 15 minutes, conflict resolution by a run, picking roadmap records eligible for unattended work, wakes and their failure modes), and return (a walk-through of everything landed since the mark, across repositories, failures and stops reported). Propose roadmap record flags for unattended eligibility and due dates. Name the decisions Kris must make as queries, recommended option first with confidence and reason.

## Rules

Write only that note; commit it alone by explicit path, Conventional Commits subject under 100 characters; pull only `--ff-only`; do not push. Leave every other dirty file alone. No standard changes. Report in the owner-report shape with the queries and the banner.
