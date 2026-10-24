# wow-restart-blind

Masked blind review of three design questions about how Kris (the owner) coordinates AI agents. Do not read `+/_WORK/ki.ways-of-working/queries.md`, `decisions.md`, any `*.report.md` or `design/` note. You may read the harness standard `skills/change-management/ki-coordination/references/standards-coordination.md` in `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness` and the Work Process note `Pillars/Philosophy/Model/Processes/Work Process/Work Process.md` in ki-principal. Read-only: change, commit and push nothing.

For each question, pick one option (or propose a better one), give a confidence (high, medium, low) and a two-line reason.

## Q1 - naming coordination threads

Context: Kris asked that a bootstrapped coordination thread get a good name, or failing that the report say how. Claude Code's `--name` flag names a session at launch; a running session cannot rename itself. Reports currently must not carry paste instructions or send/resume prompts. Some threads are opened by pasting an opener into an existing session. Question: how should threads be named?

- Launch openers with `claude --name "<label> (<id>)"` only; reports stay free of paste lines.
- Launch openers with `--name`, and bootstrap and re-bootstrap reports also carry one `Rename this thread: /rename <label> (<id>)` line as a named exception to the no-paste rule.

## Q2 - explicit coordinator commands

Context: Kris wants to say a move as a command, e.g. `/ki-coordination hold`. Today only summary, recap, full-summary and mark are commands. In the Work Process note, drain is an activity inside the move to On hold, not a state. A standalone drain would stop new launches, let runs finish, and leave the work With worker. Question: which commands should be added?

- `hold`, `resume`, `send` and `receive`, with drain only ever part of hold.
- All of those plus `drain` usable on its own, `hold` being drain plus On hold.

## Q3 - ending Initiatives

Context: Kris asked that the theme registry be used everywhere and "enforced mechanically now". Checkers only warn on `Streams/Initiatives/` and `initiative:` fields; the tolerance window has no end date. One territory (Personal) has migrated; Legal still has 7 Initiative files and no Themes folder; HNR has one `initiative:` field. Failing now breaks both audits. Today is 24 October 2026. Question: when should the checkers fail on Initiatives?

- Turn the warnings into failures at once and let Legal and HNR fix their audits.
- Message Legal's and HNR's coordinators to migrate now, and turn warnings into failures on a fixed date (proposed 7 November 2026), or earlier once a scan finds no residue.

## Output

Write `/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-restart-blind.answer.md` with Q1-Q3 answers, and report the same in your final message.
