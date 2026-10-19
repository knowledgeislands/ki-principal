# obs-burndown - Roadmap burndown push for apps-observatory.local

Run `obs-burndown` for KI > Model > Observatory (`ki.observatory`), working in apps-observatory.local. Routed from KI > Model > Ways of working as BURNDOWN-PUSH: Kris agreed a roadmap burndown push for apps-observatory.local. It starts after obs-reader, which also edits a record there.

1. Count the records in `docs/roadmap/` by status and horizon before you change anything.
2. Prune every record that is done, under `ki-work-roadmap` and `ki-accept`'s prune rules, so that its outcome is homed and the commit boundary is respected. Commit by explicit path under `ki-git`.
3. List every record Awaiting review as one acceptance batch for Kris: each record with its ID, a one-line outcome, what Kris should look at, and any known gaps. Accept nothing.
4. Go through the triage records and propose cancelling or merging at least half of them, with a one-line reason each, and name the merge target for each merge. Cancel and merge nothing: Kris confirms first.
5. Count again, and give the net count before and after, both now (after pruning) and projected (if Kris confirms the cancellations and merges).

Do not push, touch another repository, or restart the Observatory service.

Report in owner-report shape, kept short. Done gives the pruned records and the counts. Queries holds two queries: BURNDOWN-ACCEPT, the acceptance batch, and BURNDOWN-TRIAGE, the cancel and merge list. Give lettered options for each, with the recommended option first and its confidence.
