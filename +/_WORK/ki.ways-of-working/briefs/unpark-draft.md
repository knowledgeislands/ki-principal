# unpark-draft - draft five unparked queries in full

Work: ki.ways-of-working, package `+/_WORK/ki.ways-of-working/` in ki-principal. Kris unparked five queries at 02:55 BST: NO-GATE, PKGLESS-GATE, GFM-HOSTING-RULES, HARNESS-TRIAGE, PRINCIPAL-TRIAGE. Their one-line forms are in `queries.md`; their sources are in `decisions.md` and the run reports in `/Users/krisbrown/.local/state/ki/agents/ways-of-working/` (lane-triage, wow-triage, gfm-review, gfm-harness and others; grep the tags). PKGLESS-GATE came from tools-ki via ki.tools-burndown and is taken with NO-GATE.

## Task

1. Check each against current state (records may have moved since; harness main now includes lane-triage and ci-green). Drop any that is overtaken and say so.
2. Write `design/unparked-queries.md`: each live query in ki-coordination owner-report shape (`### <TAG> - <title>`, **Context:** enough for Kris to decide cold, **Query:** one sentence, **Options:** `a) (recommended, confidence <level> - <reason>) ...`, `b) ...`). Every record cited by full identifier linked to its absolute local path. HARNESS-TRIAGE lists each record's disposition. Say which were already blind-reviewed (NO-GATE was).
3. Write `briefs/unpark-review.md`: a masked blind review brief for the queries not already reviewed, giving only Context, Query and unranked options, no recommendation or confidence, forbidding reads of any `+/_WORK/` file, decisions log or run report, no edits, commits, launches or network calls; asking per query for a pick, confidence, one-line reason and conditions; report as owner report.
4. Commit both files by explicit path with `docs(work): ki.ways-of-working draft unparked queries`.

## Limits

Edit only those two files. CAPTURE-GATE: no new records. HOOK-GUARD: no `ki repo conform` without `--dry-run`. Never `--no-verify`, never push. British English, ASCII hyphens, they/them.

## Report

Owner report: Done, In Progress, Queries.
