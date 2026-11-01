# [Model](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › sweep-va-principal

**🤖 → 👤 Handoff to supervisor · Run report at 00:29 GMT · last mark 00:28 GMT**

---

## Done

- `.gitignore` in va-principal now re-includes `!/+/_WORK/*/reports/` and `!/+/_WORK_REVIEW/*/reports/` straight after the `reports/` rule (`880682c`); pre-commit gate passed.
- `va.prj.community-website`: 1 report moved into `reports/` (`community-presence-handover.report.md`, tracked, `git mv`); no clash; 3 links repointed: 2 absolute links in its `messages.md` and the wikilink in [VA-PRINCIPAL-KNW-002](/Users/krisbrown/kis/valle-armonia/va-principal/Streams/Roadmap/VA-PRINCIPAL-KNW-002-bring-community-identity-into-principal.md); REPORTS-MOVED line added to its `messages.md`; all in `b503d4f`. Pre-commit gate passed.
- `va.prj.knowledge-intake`, `va.prj.markhowarth-launch`, `va.sop.main`: no top-level reports, nothing moved, no commit.
- Skipped folders: none; no live run held any va-principal work.
- Nothing deleted. Full `ki repo audit --repo .`: FAIL, with findings not caused by this sweep: the pre-commit gate check (GATE-1), IMPORTANT-ordering in three `messages.md` files (RECORD-2), the repository not registered locally (REPO-REG-1), and COORD-7 on the moved report's own content (record links outside this checkout), which the move did not change.
- One mention of the report's bare filename in `messages.md` (a code span in the TIDY-REPORT line, not a link) was left as written.

## In Progress

Nothing is running.

Outstanding - no action requested now: the moved handover report stays held under HANDOVER-HELD until the steward prunes it at their next mark.

## Queries

No outstanding queries.
