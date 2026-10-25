# wow-ask-timeout - a question in an unattended window waits two minutes, then nothing happens

## Goal

Kris on 2026-10-25: "If you ask me for input as well in ... an unattended period, you should only really ask it for a couple of minutes. And if I don't respond, then you should not take any action from it. That's also something they should learn about." Write it into `ki-delegation`'s unattended-window rules in the KI Agentic Harness: a question to Kris during a window waits a couple of minutes at most; with no answer, nothing is done on it, it is parked as a query for the return report, and other authorised work carries on. Silence is never consent. Carry it into the coordinator output-style source and the generated surfaces where window behaviour is stated, so every coordinator learns it.

## Do

- Work in `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness` after wow-external-limits has pushed, building on its and wow-unattended-limits' wording. Pull first; use a clean temporary clone or the primary checkout if clean. Update rubric, examples and generated surfaces (`ki dev skill generate ... --write`) and run tests and audits until they pass.
- Commit by explicit path as Conventional Commits ending with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`, pull with rebase, push fast-forward only.
- Append one REFRESH line naming the revision and the rule to `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/messages.md`; commit and push it by explicit path.

## Do not

Change any other standard or setting, release, force-push, use `--no-verify`, or touch another session's uncommitted files.

## Report

The owner report: Done, In Progress, Queries with Context, Query and Options, recommended first with confidence and reason.
