# wow-shape-blind

## Goal

Masked blind review of two questions before Kris sees them. Give your own recommendation for each, with a confidence (high, medium or low) and a one-line reason. Do not read any `queries.md`, `decisions.md`, run report or `design/` file in any work package.

## Read

Only: in ki-agentic-harness, the ki-work-package standard (Work file fields; host rules) and the ki-coordination standard (Messages between work; Bootstrap; Picking work up).

## Context and questions (options unranked)

STEWARD-FIELD. Kris wants one State of play thread to look after every Project package in its territory unless the Project has its own coordination thread, by an explicit committed assignment changed only by an acknowledged handover. The assignment needs a committed home naming a work, never a host or session. Question: should it be recorded in `work.md`'s existing `worker` field (`worker: work/<sop id>` while the State of play looks after the package, `agent` while its own thread does), which adds no field and suits a value that changes only when Kris opens or closes a thread; or in a new dedicated field taking only `work/<id>` values, which keeps the assignment distinct from the holder vocabulary and visible beside the state?

HOST-TARGET. Message lines, briefs and records may carry an optional `@<host or category>` requirement after the date, names taken from the territory's machine inventory. Coordinators on one machine will meet lines meant for another. Question: should a thread act only on lines untagged or tagged for its own host or category, leaving the rest queued and counted in its banner (with an age flag so none waits unseen); or should the requirement restrict only device-dependent execution, leaving any coordinator free to acknowledge, plan, ask Kris about or dispatch the line to an eligible host in queue order, which keeps queue order and IMPORTANT lines intact but means a coordinator handles lines it cannot finish?

## Rules

Read only; write nothing in any repository; no network calls; launch no agents. Report in the owner-report shape with one query per question, your recommendation as a), and the banner.
