# KI > Techne > Agora › guilds-table

**🤖 → 👤 Handoff to supervisor · Run report at 03:55 GMT · last mark 00:04 GMT**

---

## New and noteworthy

Guilds is now filter-led: the illustrator’s shields sit above a two-level skill table, and skill documents open in the right tray. Home’s logo navigation and every sidebar section’s fold were corrected.

## Done

- Commit `5ecf465` contains only the sixteen owned paths; the inherited work was completed and unrelated edits were left untouched.
- The horizontal shield bar preserves guild order. All guilds stays fixed while the remaining shields scroll; each shield filters the table.
- Guild rows expand and collapse with skill counts. Skill rows show name, short description, kind, applicability, dependencies, argument hint, supported runtimes and runtime binding.
- Kind and applicability tallies filter the table, with removable chips, find and Group; territory context still selects whose harness is shown.
- The right tray shows all front matter and the body, with document and directory tabs, individual files and Open file. Guilds no longer opens the bottom pane. File opening checks that the target remains inside the skill.
- Home is absent from the sidebar and reachable from the Atlas logo, which marks Home when selected. Every sidebar section, including System and the active section, folds; navigating to a place opens its section.
- Pure fixture tests cover front matter and tree building, including block lists, absent fields, false runtime binding, counts, grouping and combined filters. File-path tests cover escaping links.
- `bun run self:check`: passed.
- `bun run test`: passed, 560 tests across 56 files.
- Throwaway capture checks passed against 65 real skills in eight guilds, including filtering, tree folds, sidebar folds, logo navigation, file browsing, Open file, Escape and the frozen All guilds shield; no renderer errors.
- Inspected [light tray](/Users/krisbrown/.local/state/ki/agents/ki-prj-agora/guilds-table-r.evidence/guilds-tray-light.png), [dark documents](/Users/krisbrown/.local/state/ki/agents/ki-prj-agora/guilds-table-r.evidence/guilds-files-dark.png) and [narrow scrolling bar](/Users/krisbrown/.local/state/ki/agents/ki-prj-agora/guilds-table-r.evidence/guilds-narrow-dark.png) captures. Evidence and check logs are retained in [the evidence folder](/Users/krisbrown/.local/state/ki/agents/ki-prj-agora/guilds-table-r.evidence); the temporary capture workspace was emptied.

## In Progress

Nothing is running. The installed apps were left unchanged; delivery awaits supervisor review.

## Queries

No outstanding queries.

🧵 ki.prj.agora
