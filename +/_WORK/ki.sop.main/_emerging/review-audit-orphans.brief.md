# review-audit-orphans (blind review)

Independent review: you have not seen anyone's recommendation; give your own. Do not read any `discussions.md`, `decisions.md` or `*.report.md` in a `+/_WORK/` folder. You may read tools-ki and ki-agentic-harness (the ki-engineering skill's evidence code) read-only.

## AUDIT-ORPHANS - A stopped audit leaves its test run going

**Context:** When an audit is stopped part-way, for instance by an agent's command time limit, the full test run it started keeps going in the background and holds the coverage report folder. The next audit of the same checkout then fails at once with "already in use by another Vitest process", or both runs slow each other down. I saw this happen today. The test run is started by the ki-engineering skill's evidence code in the harness, not by tools-ki's audit code, so it was outside this run's scope. The minute-by-minute line now makes stopping less likely, but doesn't prevent it.

**Query:** Should a stopped audit also stop the test run it started?

**Options (unranked):**

- Leave it, and rely on agents running the audit in the background with a long enough time limit.

- Record it as a work item for the harness's ki-engineering evidence code: stop its child processes when the audit is interrupted.

Give your choice, confidence and a two-line reason. Read-only; no commits. Write it as your run report.
