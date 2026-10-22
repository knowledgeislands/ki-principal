# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › state-note-fix

**🤖 → 👤 Handoff to supervisor · Run report at 14:53 BST**

---

## Done

- `024b069b` fix(ki-repo-kb): NOTE-1c now exempts all five package files (`work.md`, `state.md`, `queries.md`, `messages.md`, `decisions.md`) directly under `+/_WORK/<id>/` and `+/_WORK_REVIEW/<id>/`. It is written the same way as the existing `work.md` exemption, and the frontmatter standard's footnote now says so. The test covers all five files, and a new test shows that other files in a work folder are still checked.
- `db30d0ca` fix(ki-work-package): RECORD-2 now accepts `None.` as an empty `messages.md`. This was the second failure caused only by the five-file shape: migrate-pass wrote `None.` in `ki.ways-of-working/messages.md`, and every other package section already accepts it. The new test failed before the fix and passes with it.
- ki-principal full `ki repo audit`: ki-repo-kb fails before (NOTE-1c), passes after. Overall result: 5 failing skills down to 4, and 20 findings down to 18.
- Harness checks: `bun run test` passes (1286 tests), `bunx tsc --noEmit` passes, the focused ki-work-package audit passes, and the pre-commit hook passed for both commits. `ki dev skill generate` does not apply: neither skill has generated surfaces. `ki dev skill rubric` matches for both. A focused ki-repo-kb audit cannot run in the harness because the harness does not declare that skill.
- Net record count: 0 in each repository.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- ki-principal still fails four skills. These are problems with what the files say, not with the five-file shape, so I left them alone:
  - ki-authoring: Markdown problems in another session's uncommitted `+/_WORK/ki.chezmoi/` files.
  - ki-decision-records: 4 findings on GDR records.
  - ki-work-package: in `ki.specifications`, `state.md` gives `since` without seconds (`2026-10-19T13:33Z`), and a `messages.md` line puts the time and "from" in the wrong order.
  - ki-coordination: 11 COORD-7 findings for unlinked identifiers in work-folder reports.
- Not pushed, as the brief says. ki-agentic-harness `main` is 8 commits ahead of origin: my 2 sit on top of 6 from other sessions.

## Queries

No outstanding queries
