# finish-first

Work: ki.ways-of-working. Authorised by Kris at 02:38 BST on 20 October: "how do we make it so that we get work finished before we start creating more work in the roadmap items? You know we need to see roadmaps going down, not going up like they are."

## Task

1. Measure: for every repository under `/Users/krisbrown/workspaces` with `docs/roadmap/` or `Streams/Roadmap/`, count records by status now and at daily points over the last 14 days from Git history (created, done, pruned, cancelled per day). Show which repositories grow and where new records come from (run captures, triage of retros, handoffs between repositories, owner requests), citing commits.
2. Read the current rules that govern record creation and closure: CAPTURE-GATE and BURN-WAVE-1 in `+/_WORK/ki/decisions.md`, `ki-next`, `ki-accept`, `ki-work-roadmap`, and OWNER-QUEUE in `+/_WORK/ki.ways-of-working/decisions.md`.
3. Write `+/_WORK/ki.ways-of-working/design/finish-first.md`: the measurements, the causes of growth, and a small rule set that makes counts fall, for example a per-work cap on Now plus awaiting-review before new adoption, a net-down target per repository per week shown by State of play, closure and prune cadence, and where ideas go instead of records. Say for each rule which standard or tool owns it and how it would be checked.
4. Put the choices that need Kris as queries, each with a recommendation and confidence.

## Rules

- Read-only except the one design file, committed by explicit path in ki-principal; do not push if other sessions' commits are stacked. No network.
- Check every path and claim before stating it (CLAIM-CHECK). HOOK-GUARD: never run `ki repo conform` without `--dry-run`. CAPTURE-GATE: no new records. British English, ASCII hyphens.

## Report

Owner-report shape: Done, In Progress, Queries.
