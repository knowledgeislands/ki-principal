# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-review-pack-4

**🤖 → 👤 Handoff to supervisor · Run report at 06:38 GMT · last mark 06:06 GMT**

---

## Done

- Re-checked all 80 addresses the pack lists against the live site with `curl -sIL`: every one answers 200, each `.html` diagram address redirecting to its suffix-less form as expected, and roadmap-lifecycle shows the rewrite. No address still fails.
- Replaced the "Not answering" note in `+/_WORK/ki.ways-of-working/design/review-pack.md` with a "Live site checked" note giving the check time and result, and reworded the chat prompt's two sentences that referred to the old note. The deploy fix `904176e` changed only the build's receipt check, nothing a reader sees, so no review line was added for it.
- Rewrote the pack's open-queries section as a verbatim copy of the Open section of `queries.md`: 33 queries (the brief said 32; CI-PIN was queued after the brief was written and is included so the pack matches `queries.md` exactly), each block confirmed byte-for-byte against its source. Grouped under nine one-line lead-ins: The website (AREA-COLUMN, REPO-STANDARDS-SET, DEPS-1, CI-PIN); The model of work and its packages (STEWARD-FIELD, SOP-PROJECT-CARE, SINGLE-THREAD, WORK-LABEL, SIZE-LABEL, RECAP-NAME); Unattended windows and wakes (UNATTENDED-AND-DUE-DATES, UNATTENDED-FIELD, WAKE-SUBSTRATE); Standing rules for agents (the four UNWRITTEN-RULES); Permission prompts (the three PERM-PROMPTS); Tending and findings (INTERIM-REPAIR, INTERIM-FINDING-WRITER, INTERIM-FINDING-AGE, TIDY-GAPS); Repository standards, metadata and tools (INTERIM-HOMEPAGE-OMISSION, INTERIM-TAG-SCOPE, LEGACY-PREFIX, PARTIAL-REPOS, DIAGRAM-PRIVATE-CITATIONS, CLI-PREVIEW); Skills and bootstrap (BOOT-HOME, TRADES-FATE); Acceptance (ACCEPT). Both views kept wherever a review disagreed, as the source has them. Walkthrough instructions and digest shape unchanged apart from the two prompt sentences above.
- Committed as `da88dc00` by explicit path (pre-commit audit passed); fetched, fast-forward pull clean, pushed to `origin/main` fast-forward.

## In Progress

Nothing is running.

## Queries

No outstanding queries.
