# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-design-batch

**🤖 → 👤 Handoff to supervisor · Run report at 00:17 BST · last mark 00:17 BST**

---

## Done

- [KI-DESIGN-TOK-001 (pruned)](https://github.com/knowledgeislands/ki-design/blob/e1d20b6b96770c35ac1c1c3186c672fb710aa969/docs/roadmap/KI-DESIGN-TOK-001-tokens-v0.md) is at Awaiting review in `f1ca1cc`. A new test holds every token role to its contrast floor. Read-only checks confirmed that the site and the Observatory both take the token build unchanged.
- [KI-DESIGN-MAP-001 (pruned)](https://github.com/knowledgeislands/ki-design/blob/e1d20b6b96770c35ac1c1c3186c672fb710aa969/docs/roadmap/KI-DESIGN-MAP-001-hexmap-v0.md) is at Awaiting review in `317edd6`. A new preview test confirms the Known Lands chart is drawn by the hex map package. The test showing Arcadia's map renders already existed.
- [KI-DESIGN-ICO-001 (pruned)](https://github.com/knowledgeislands/ki-design/blob/85a42bf13ddd7396ae28b83bc645c0767d06454d/docs/roadmap/KI-DESIGN-ICO-001-icon-seed-set.md) (`c3b4a7c`), [KI-DESIGN-SYM-001 (pruned)](https://github.com/knowledgeislands/ki-design/blob/e1d20b6b96770c35ac1c1c3186c672fb710aa969/docs/roadmap/KI-DESIGN-SYM-001-symbol-library-data.md) (`36d563d`) and [KI-DESIGN-TIL-001 (pruned)](https://github.com/knowledgeislands/ki-design/blob/e1d20b6b96770c35ac1c1c3186c672fb710aa969/docs/roadmap/KI-DESIGN-TIL-001-tile-set-contract.md) (`2c86325`) are planned to Ready. Each stops there for an owner decision (see Queries).
- Checks: all package tests pass except `elements`. The preview and generator tests pass (87), and so do typecheck, Biome, rumdl and the boards check. The roadmap and authoring audits report FAIL=0.
- Not run: `knip` fails, as it did before this run. `elements` tests and typecheck could not run. The cause of both is under In Progress.

## In Progress

- Nothing was running when this run stopped.
- Dependencies were installed from the local cache with the network blocked. Eight packages were not in the cache: `lit` and its parts, `happy-dom` and `rumdl`. So the `elements` tests and typecheck did not run, and `knip` reports `rumdl` unused. None of these five records touches `elements`. One online `bun install` would let them run.

## Queries

**Context:** [KI-DESIGN-ICO-001 (pruned)](https://github.com/knowledgeislands/ki-design/blob/85a42bf13ddd7396ae28b83bc645c0767d06454d/docs/roadmap/KI-DESIGN-ICO-001-icon-seed-set.md) and [KI-DESIGN-SYM-001 (pruned)](https://github.com/knowledgeislands/ki-design/blob/e1d20b6b96770c35ac1c1c3186c672fb710aa969/docs/roadmap/KI-DESIGN-SYM-001-symbol-library-data.md) share one test: every Official or Agreed symbol must have a glyph. Six symbols have none: `territory`, `realm`, `pillars`, `thriving`, `quiet` and `weathered`. The four conditions (those three plus `ruined`) are also drawn as building states on tiles, and `ruined` already uses the `ruins` glyph. SYM-001 asked for a glyph on every symbol, but Proposed symbols such as `storm` are left out, as in ICO-001.

**Query:** Should the condition symbols get line glyphs, or be left out of the glyph test?

**Options:** a) (recommended, confidence medium - it meets ICO-001's goal as written and gives the app a glyph for each condition) Draw `realm`, `pillars`, `thriving`, `quiet` and `weathered`, and give `territory` the existing `archipelago` glyph. b) Leave the conditions out of the test as building states, and draw only `realm` and `pillars`. c) Hold both records until the condition glyphs are designed with the tile states.

**Context:** [KI-DESIGN-TIL-001 (pruned)](https://github.com/knowledgeislands/ki-design/blob/e1d20b6b96770c35ac1c1c3186c672fb710aa969/docs/roadmap/KI-DESIGN-TIL-001-tile-set-contract.md)'s second check says every tile id must render in the preview's Known Lands chart. That chart is flat and never draws tile art. It can draw the 12 terrains and the 16 structures (`cottage` as the plain fallback marker), but not the 4 decals or 4 connectors. Only the isometric renderer, [KI-DESIGN-MAP-002](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-MAP-002-isometric-renderer.md), draws tile art, and MAP-002 is waiting on TIL-001, so the check as written can never pass. The tile validator already passes for the Modern set, though every tile is still marked draft.

**Query:** What should TIL-001's chart check cover?

**Options:** a) (recommended, confidence high - it is the only version that can pass before MAP-002, and MAP-002 waits on this record) Test that every terrain and structure renders in the flat chart, and leave decals and connectors to MAP-002. b) Move the chart check into MAP-002 and close TIL-001 on the validator check alone. c) Keep the check as written and remove TIL-001's block on MAP-002.
