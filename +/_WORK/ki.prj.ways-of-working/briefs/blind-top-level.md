# Brief: blind review, two owner queries (read-only)

Review independently. Do not read `queries.md`, `decisions.md`, `design/package-layout/top-level-cause.md` or any report in `/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/`. You may read `design/package-layout/design.md` there, the `ki-work-package`, `ki-delegation`, `ki-coordination` and `ki-repo` skills in `/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/skills/`, `tools-ki` source (`/Users/krisbrown/kis/knowledge-islands/tools-ki`, e.g. `src/core/agent/thread.ts`, `events.ts`, `runs.ts`), and any `+/_WORK/` folder under `/Users/krisbrown/kis/*/*/`. Change nothing.

**Facts:** On 30 October 2026 Kris directed that a work package (`+/_WORK/<id>/`) keeps only its five files (`work.md`, `state.md`, `queries.md`, `messages.md`, `decisions.md`) at the top level, everything else grouped, "possibly group first with briefs, design and reports beneath". The layout choice (LAYOUT-SHAPE: A kind-first `reports/`, `briefs/`, `design/`; B group-first with `briefs/` and `reports/` inside each group; C group-first and flat) is still open and unpiloted. On 1 November Kris asked for the cause to be found and the fix put into the rules, skills and tools at priority. The `tools-ki` launcher writes every run report to `+/_WORK/<id>/<name>.report.md` by design; the standards and the audit allow it; 182 reports sit at the top level of 17 folders across five repositories. The shared `ki-repo` ignore block ignores `reports/` at any depth, so moving reports to `reports/` needs an exception `!/+/_WORK/*/reports/`. Each work folder has its own steward; the rules forbid deleting a whole folder at once and require each report's outcome to have a durable home before it is deleted.

**Query 1:** Should reports go into a `reports/` folder now, ahead of the layout decision? Options (unranked):

- Change the launcher, the rules and the ignore exception to use `reports/` now, keeping LAYOUT-SHAPE open (if the flat group layout C later wins, reports move a second time).
- Answer LAYOUT-SHAPE first and make one change to the chosen layout; reports keep arriving at the top level until then.
- Keep reports at the top level and tidy every package strictly at each mark.

**Query 2:** Once the change lands, who clears the existing top-level reports? Options (unranked):

- Each folder's steward tidies at its next mark, deleting homed reports and moving the rest into `reports/`, prompted by one message line per folder from State of play.
- One bounded sweep run per repository moves every top-level report into `reports/` with no deletions; stewards prune later.

For each query give your pick, a confidence (high, medium or low) with a one-line reason, any risk missed, and which claims you verified yourself.
