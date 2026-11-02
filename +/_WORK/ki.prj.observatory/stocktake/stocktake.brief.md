# Brief: stocktake - consolidate and prioritise the Observatory queue and queries

Work: ki.prj.observatory (KI > Model > Observatory). Authority: Kris, 1 November 2026, logged as STOCKTAKE in `+/_WORK/ki.prj.observatory/decisions.md`: "take stock of all the messages you received and then look through everything that you've got from a query perspective ... consolidate some of these items together so that we can get on with them. It's probably important to also prioritize some parts of these."

## Goal

Give Kris one consolidated, prioritised picture of everything waiting on the Observatory, so the many separate items become a few groups he can decide and move forward.

## Inputs (read, do not edit)

- `+/_WORK/ki.prj.observatory/messages.md`: 37 lines, 7 IMPORTANT.
- `+/_WORK/ki.prj.observatory/discussions.md`: 10 open queries (QUEUE, RESTRUCTURE, TEN-COMMITS, MERMAID-HANDLER, BRIDGE-STALE, STATUS-REPAIR, SYNC-DIRECTION, PUBLIC-AUDIENCE, PUBLIC-EXPOSURE, ACCESS-DISPOSITION). QUEUE is answered by this run.
- `+/_WORK/ki.prj.observatory/state.md` (holds), `work.md` (scope), `decisions.md` (standing owner decisions such as PUSH-ALL, DESIGN-APPLY, DIAGRAM-REPLACE).
- `/Users/krisbrown/kis/knowledge-islands/apps-observatory.local`: its `docs/roadmap/`, `docs/ideas/`, decisions and Git log, to check whether each message is already settled.
- Other repositories only to verify a specific claim a message makes (read-only).

## Do

1. For every message line: say whether it is settled (with the evidence: commit, record or file), still live, or belongs to another work (name the receiving package). Do not remove any line.
2. For every open query: say whether anything since 29 October changed it.
3. Group live messages and queries into a small number of consolidated items (aim for 5 to 8), e.g. publication/protection, status correctness, host and sync observation, new areas and views (Acquire graph, account scores, diagram annotation, opener button, agent hooks, scheduled results), design convergence, housekeeping. Each group: what it contains, the one decision Kris needs to make to move it, and what would follow.
4. Propose a priority order across the groups with a one-line reason each, noting blockers (the PROTECTED-PUBLICATION hold blocks Principal pushes) and dependencies on other work.
5. Draft each group's decision as a query in the owner-report query shape (Context, Query, lettered Options with a recommended option first carrying confidence and reason), in plain British English, ASCII hyphens only. Mark which drafts are medium or low confidence so the coordinator can send them to blind review.
6. List message lines proposed for removal as settled, with evidence, for the coordinator to dispose of.

## Do not

Change any product, roadmap or idea record; adopt, promote, accept or prune anything; edit the work package's five files; send messages to other packages; push anything; change visibility, history, services or configuration. Read only, apart from writing your report.

## Report

Write your report to `/Users/krisbrown/.local/state/ki/agents/ki-prj-observatory/stocktake.report.md`; the launcher homes it in the work folder. Open with a short plain-English summary, then sections: Settled lines, Live lines by group, Query changes, Groups and priority, Draft queries, Proposed removals. Do not commit or push. End with DONE.
