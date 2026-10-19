# wow-triage

Act as the worker of `+/_WORK/ki.ways-of-working/`. Kris's 20 October instruction is the direction its hold waits for: "Can you go through any items which are triaged in knowledge islands and get them progressed?" Taken as WOW-RESUME a).

1. Read the package's five files. Set `state.md` to with-worker, recording the release in its `decisions.md` in Kris's words. Act on each `messages.md` line, important lines first, then remove it. NO-GATE and the roadmap-census-2 line are there.
2. Triage every unadopted triage record that ki.ways-of-working owns, under `ki-work-roadmap`: 14 in ki-agentic-harness, 2 in ki-principal and 1 in ki-specifications. Do KI-HARNESS-GOV-219 and KI-HARNESS-GOV-224 first, because KI-OBSERVA-BRG-004 and KI-OBSERVA-VIS-042 are held on them. Adopt each record to the horizon you recommend at high confidence, cancel or merge only after a blind review agrees, and query the rest in the package.
3. Deliver what is high confidence and bounded, GOV-219 and GOV-224 first, under `ki-plan` and `ki-implement`, stopping each at Awaiting review.
4. Run an estate-wide COORD-12 check with the `ki-coordination` rubric. If it is clean, release KI-HARNESS-GOV-215 to `next`.
5. GFM-HOSTING-RULES: GitHub's main-branch ruleset on ki-agentic-harness requires a PR and a `build` check, and Kris's pushes bypass it. Check whether CI defines a job named `build`, and write the reconciliation as a query in the package. Change no GitHub settings.
6. Leave the package With worker and record its next steps in `state.md`.

## Rules

- OVERNIGHT authority (Kris, 20 October, 00:30 BST): "You can do anything on a high confidence level that you recommend." Act on your own high-confidence recommendations. For anything below high, write the query with Context, Query and Options into the owning package's `queries.md` and continue with the next item. Nothing destructive without a blind review that agrees.
- Do not push, and make no remote, GitHub-settings or host changes. Kris has not asked for a push.
- CAPTURE-GATE (Kris, 19 October): create no roadmap record except one this brief names. List follow-ups in your report.
- HOOKS-MIGRATION: never run `ki repo conform` without `--dry-run`. Do not touch `package.json`, `bun.lock`, `.husky/` or `.githooks/`.
- Other sessions are active. Leave alone any file another session has uncommitted changes in, and name it. Never stage ahead of your commit: put explicit paths on the commit command itself.
- Commit only your own changes, using Conventional Commits and ending with "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>".
- British English, ASCII hyphens only.
- Report to the path your run packet names, as an owner report: Done, In Progress, Queries. Each query gives Context, Query and Options, with a) recommended and its confidence.
