# [Model](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › coverage-fix

**🤖 → 👤 Handoff to supervisor · Run report at 19:15 GMT · last mark 19:15 GMT**

---

## Done

- The tools-ki coverage gate is back at 100%. Commit `2fb09fed` adds tests only and changes no source code. The threshold is unchanged and there are no ignore comments.
- What the new tests prove:
  - A member checkout never takes a Capital regular work as its home, whether the work is named or picked automatically.
  - A file that is not a report, or a focus folder that cannot be read, gives no report to `ki agent decide`.
  - A three-part work id with no recognised type keeps only its own name and is not mistaken for another work's alias.
  - A registered checkout that no longer exists does not break the home check in `ki agent close`.
- The last item covers a gap the brief did not list: a function-coverage miss from the same report-homing commit `2a2eab2a` (`src/core/agent/thread.ts` line 357).
- Checks: full suite passed (97 files, 2182 tests); coverage gate passed; type check passed; commit hook passed.

## In Progress

Nothing.

## Queries

None.
