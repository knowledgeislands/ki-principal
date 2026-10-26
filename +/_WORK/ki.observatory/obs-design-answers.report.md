# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-design-answers

**🤖 → 👤 Handoff to supervisor · Run report at 00:41 BST · last mark 00:29 BST**

---

## Done

- **Install and baseline:** the online `bun install` worked. Before any change, the `elements` tests (11 pass), typecheck and knip all passed, along with every other gate. The roadmap audit showed FAIL=0.
- **BANNER-GLYPHS a), [KI-DESIGN-OBS-015 (pruned)](https://github.com/knowledgeislands/ki-design/blob/e1d20b6b96770c35ac1c1c3186c672fb710aa969/docs/roadmap/KI-DESIGN-OBS-015-banner-glyphs-question.md), `f41cbc5`:** the answer is recorded as [GDR-KI-DESIGN-037](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/decisions/GDR-KI-DESIGN-037-the-banner-emoji-stay-the-written-notation-line-glyphs-may-be-a-rendered-form.md), and the question has left `OPEN.md`. The briefs, the Observatory design spec and the generated decisions board now point to the record. `ANSWER-2026-10-19.md` said the question was open, so it now gives the answer and fills in the option in its hand-off text. The glyphs stay proposed. The record is Awaiting review. Checks pass.
- **CONDITION-GLYPHS a), [KI-DESIGN-ICO-001 (pruned)](https://github.com/knowledgeislands/ki-design/blob/85a42bf13ddd7396ae28b83bc645c0767d06454d/docs/roadmap/KI-DESIGN-ICO-001-icon-seed-set.md), `a3034a3`:**
  - I drew five new glyphs: `realm` (a globe), `pillars` (three free-standing columns) and a house family for the conditions. `thriving` has chimney smoke, `quiet` is unlit, and `weathered` has a broken roof line and a cracked wall. All five pass `lintIcon`.
  - `territory` now uses `archipelago`.
  - A new shared test checks that every Official or Agreed symbol names a glyph.
  - The contact sheet, preview pages, boards and glyph counts (now 78) are rebuilt.
  - The record is Awaiting review. Checks pass.
- **[KI-DESIGN-SYM-001 (pruned)](https://github.com/knowledgeislands/ki-design/blob/e1d20b6b96770c35ac1c1c3186c672fb710aa969/docs/roadmap/KI-DESIGN-SYM-001-symbol-library-data.md), `09e001f`:** the shared test fails when a glyph is removed and passes once it is restored. The Field Guide rebuilds from the data with no diff. The record is Awaiting review. Checks pass.
- **TILE-CHECK a), [KI-DESIGN-TIL-001 (pruned)](https://github.com/knowledgeislands/ki-design/blob/e1d20b6b96770c35ac1c1c3186c672fb710aa969/docs/roadmap/KI-DESIGN-TIL-001-tile-set-contract.md), `d845e32`:** the validator still passes for the Modern set. A new preview test checks that the flat Known Lands chart draws every inventory terrain and structure; only `cottage` falls back to the neutral marker. The decal and connector check moves into [KI-DESIGN-MAP-002](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-MAP-002-isometric-renderer.md)'s Steps and Verify. The record is Awaiting review. Checks pass.
- **Final gates:** tests, typecheck, Biome, rumdl, knip and the board drift check all pass. The roadmap and authoring audits show FAIL=0. The tree is clean, and nothing is pushed.

## In Progress

- **New glyphs:** they need your eye on `packages/icons/contact-sheet.png`, which borders them in brass. At 16 px, `thriving` and `quiet` differ only by the chimney smoke.
- **Contact sheet:** Playwright isn't a ki-design dependency. I rendered the sheet with the Playwright already installed in the `apps-observatory.local` checkout. Nothing was installed and `package.json` is unchanged.
- **Board fix:** my first OBS-015 commit missed regenerating the decisions board. I amended that local commit before going on, so the check passes at every commit.

## Queries

None.
