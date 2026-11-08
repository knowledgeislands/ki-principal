# KI > Techne > Agora › search-words

**🤖 → 👤 Handoff to supervisor · Run report at 22:25 GMT · last mark 00:04 GMT**

---

## New and noteworthy

Atlas's search box now reads "Find an island or repo, work package or agent". Typing a repository name or part of a checkout path now finds its island.

## Done

- Changed the placeholder and its `aria-label` in `src/app/renderer/index.html`. The search results have no group labels or hints that used the old words, and the empty state ("Nothing on the map by that name.") names none of the three things, so it stays as it is. Each result's role line (council, work package, doer) names the agent's role, so it also stays.
- Search now matches an island's repository name, which is the last part of its checkout path, and its full checkout path, with a new test (`src/app/search.ts`, `src/app/search.test.ts`).
- Commit `cd7ca91` is pushed. `bun run self:check` passed with warnings only, and `bun run test` passed (503 tests).

## In Progress

Nothing.

## Queries

None.

🧵 ki.prj.agora
