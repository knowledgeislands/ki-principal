# obs-lane-sweep - triage and acceptance sweep, ki-design and website design adoption

Lane (BURN-WAVE-1): ki-design (find its checkout under /Users/krisbrown/workspaces/knowledge-islands) and the design-adoption records of apps-knowledgeislands.info (/Users/krisbrown/workspaces/knowledge-islands/apps-knowledgeislands.info). apps-observatory.local is already being triaged and built by other runs: read it only, for step 3.

Read TRIAGE-ALL, BURN-WAVE-1 and PUSH-ALL in ki-principal `+/_WORK/ki.observatory/decisions.md`.

1. List every triage record in the lane. Under `ki-next`, give each a disposition (now, next, later, hold with conditions, merge, cancel) with a confidence and a one-line reason. Shaping that needs no decision may be done.
2. Adopt each high-confidence now/next/later/hold disposition directly (status and horizon by hand if `ki repo roadmap promote` refuses). Never merge, cancel or delete: those, and every medium or low one, become one query for the lane, `LANE-TRIAGE`, each record with recommended option and confidence.
3. List every Awaiting review record in the lane and in apps-observatory.local. Do not accept anything; give one query, `LANE-ACCEPT`, recommending accept, return or cancel for each with confidence, plus any ideas that belong in a Project note rather than a record.
4. Do not create records (CAPTURE-GATE). Do not deliver anything; report the high-confidence records you moved to now, so the coordinator can launch deliveries.

Audit each repository you change (FAIL=0), commit by explicit path per repository, do not push. Never run `ki repo conform` without `--dry-run`; commit any `package.json`, `bun.lock`, `.husky/` or `.githooks/` change you make in the same unit.
