# KI > Techne > Agora › skill-table-style

**🤖 → 👤 Handoff to supervisor · Run report at 04:18 GMT · last mark 00:04 GMT**

---

## New and noteworthy

- The Guilds skill table now reads from the top of each row. Descriptions and argument hints wrap between words, and short values such as "governance" and "declaration-only" stay whole.
- At the Atlas's usual 1440 × 900 window, all eight columns fit with no clipping. Long headers break at their hyphens, for example "ki-supported- / runtimes".
- Below about 1300 points wide, the table scrolls sideways inside its own bordered panel and the Name column stays in place.

## Done

- `590efe0` fix(atlas): tidy the Guilds skill table's layout. It is pushed to `origin/main`.
  - The two sets of duplicate `.skill-table` rules, and the scattered `.guild-row` rules, are merged into one block in `src/app/renderer/app.css`. That block also fixes the cause of the mid-row alignment: the shared records-table rule was overriding the skill table's rules.
  - Skill names are left-aligned with a consistent 28-point indent, so they line up under the group heading's shield. The full group label now shows; before, it was cut off at 100 points.
  - The table now matches the Roadmap and Jobs tables. It uses their bordered panel, padding, header style and horizontal lines, and highlights the selected row the same way. Identifiers are in monospace: skill names, depends-on and argument hints.
  - In `src/app/renderer/index.ts`, the table now sits in a `tablepanel` and gains a `flat` class when grouping is None, so names are not indented when there are no groups.
- Checks: `self:check` passed and `test` passed (57 files, 567 tests), both in a clean worktree of the commit, which has since been removed.
- I looked at the result in the development build with real harness data, with the Repository structure guild chosen. Screenshots are in [the evidence folder](/Users/krisbrown/.local/state/ki/agents/ki-prj-agora/skill-table-style.evidence/):
  - [before, light](/Users/krisbrown/.local/state/ki/agents/ki-prj-agora/skill-table-style.evidence/before-light.png)
  - [light](/Users/krisbrown/.local/state/ki/agents/ki-prj-agora/skill-table-style.evidence/guilds-repository-light.png)
  - [dark](/Users/krisbrown/.local/state/ki/agents/ki-prj-agora/skill-table-style.evidence/guilds-repository-dark.png)
  - [narrow window scrolled sideways, dark](/Users/krisbrown/.local/state/ki/agents/ki-prj-agora/skill-table-style.evidence/guilds-narrow-scrolled-dark.png)
- No unit test was added. The change is styling and markup only, the renderer has no DOM tests, and the pure logic in `src/app/skill-table.ts` is unchanged. The screenshots are the check on the layout.
- Nothing was installed or relaunched. The uncommitted change to `ios/AgoraBeacon.xcodeproj/project.pbxproj` belongs to another session and was left untouched.

## In Progress

- Nothing. The installed Atlas will show the change once the coordinator installs it.

## Queries

None.

🧵 ki.prj.agora
