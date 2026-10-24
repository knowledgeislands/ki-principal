# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › mark-at-start

**🤖 → 👤 Handoff to supervisor · Run report at 20:09 BST · last mark 18:56 BST**

---

## Done

- Rule added after the Bootstrap steps in [standards-coordination.md](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md#bootstrap), which openers and the send line both run: "Work opened, bootstrapped or restarted in a new session with no mark strikes one at its start, writing `mark` in `state.md`, so every work always carries a mark. Re-anchoring in the same session still moves none."
- `mark: null` or a missing `mark` passes the `ki-work-package` schema check, and `ki work status` only reads the field. No mechanical check exists, so none was changed. The judgement item COORD-6 already asks "does the work file hold one mark", with "restore the mark" as an outcome.
- Checks: the generated surfaces and the rubric are in sync and needed no regeneration; `bun run test` passed (1286 tests); `bunx tsc --noEmit` passed; the `ki-coordination` audit had no failures and one existing fleet warning (COORD-3, one folder in `+/_WORK_REVIEW/`); the `ki-authoring` audit passed; the pre-commit hook passed.
- Commit `5a3616e4` `feat(ki-coordination): strike a mark when work starts in a new session without one` was pulled with rebase and pushed fast-forward to `origin/main`. It was the only commit stacked. The hook line and the output style were not touched.

## In Progress

Nothing is running.

## Queries

No outstanding queries
