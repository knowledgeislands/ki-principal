# [KI > SoP](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.sop.main/work.md) › granola-property

**🤖 → 👤 Handoff to supervisor · Run report at 22:51 GMT**

---

## Done

- `ki-acquire-granola` now lists `capture_moves` among its repository properties, so `ki acquire` will accept a repository that declares it (ki-agentic-harness `b8083b2d`, published).
- The [Granola acquisition standard](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/skills/acquire/ki-acquire-granola/references/standards-granola-acquisition.md#triaged-to-captured-moves) has a new section, Triaged-to-Captured moves, that keeps every rule from tools-ki `e4fbd81c` and `d85feb4a`:
  - the table's shape, keyed by folder ID because a renamed folder keeps its ID;
  - it needs `capture_root` and `folder_territories`;
  - each pair's folders are both selected, in the same territory, and each folder appears only once;
  - every Captured folder is private to Kris, and this is checked at import, at marking and before each move;
  - a repository declares either `capture_moves` or `acquired_folder_id`, never both;
  - membership of a Captured folder counts as done, so import skips the meeting, `--refresh-acquired` re-reads it, and marking reports it as already captured;
  - a meeting moves only from exactly one Triaged folder, and every other case stays an exception;
  - both Granola folder tools must be available before anything is changed;
  - the move adds the meeting to Captured and checks it, then removes it from Triaged and checks again; if either step fails, the meeting stays in Triaged or in both folders, never in neither;
  - captures are not rewritten, and the move gives no authority to delete anything.
- The rest of the skill matches: its description and EDUCATE mode, the Repeat runs and Acquired marker sections, a new review criterion ACQUIRE-5, a 2026-11-03 entry in `sources.md`, and the regenerated rubric, capability catalogue and Acquire area diagram (SVG, viewer and receipt).
- Checks:
  - `bun run test`: passed (1542 tests). Adding ACQUIRE-5 meant raising the expected criteria count in the `ki-skills` inventory test.
  - `bunx tsc --noEmit`: passed.
  - Focused audits for `ki-acquire-granola`, `ki-acquire`, `ki-authoring` and `ki-repo-harness`: passed.
  - `ki-skills` audit: passed, with three existing warnings about other skills' review dates.
  - Full `ki repo audit`, run in the isolated worktree home: only three RUNTIMES-2 failures, because that test home has no Codex runtime set up. The worktree recipe expects these, and none comes from this change.
- Sent the GRANOLA-MOVE reply to [personal.reg.assistant-terra](/Users/krisbrown/kis/personal/assistant/+/_WORK/personal.reg.assistant-terra/messages.md) (assistant `a214fa91`, published), so its held commit can now land.

## In Progress

Nothing is running.

## Queries

No outstanding queries.
