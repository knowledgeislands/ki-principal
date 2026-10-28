# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-docs-skills

**🤖 → 👤 Handoff to supervisor · Run report at 04:37 GMT · last mark 04:37 GMT**

---

## Done

- Website `57864b1` on `main`, pushed; deploy completes after push. The Skills section's four pages at harness `8897008f`, catalogue count 64 skills (53 governance, 11 process):
  - https://knowledgeislands.info/docs/skills/what-a-skill-is/ (rewritten: kinds, modes and HELP, applicability, dependencies, source shelves, how Claude Code and Codex load a skill)
  - https://knowledgeislands.info/docs/skills/how-the-skills-fit-together/ (new: ten areas, skill map plus ten area figures with what-to-look-for captions)
  - https://knowledgeislands.info/docs/skills/catalogue/ (vendored loops untouched; skeleton framing and runtime-finding prose added)
  - https://knowledgeislands.info/docs/skills/by-outcome/ (rewritten against the 64; links only the roadmap lifecycle page)
- Task 3: no crosswalk change needed; `roadmap-lifecycle` is the only Ways of working, Knowledge or Standards page that exists and it already carries its `page`. `featureAreas.json5` is dirty from another session and was left alone.
- Checks: `ki:site:build` pass (all nine gates, verify:skill-names 43 pages against 64, verify:diagrams pass); `test` 113 pass; `typecheck` pass; audit ki-repo-website-content PASS; audit ki-authoring WARN (pre-existing `.rumdl.toml` drift); audit ki-diagrams WARN (another session's uncommitted `command-groups.md` change); audit ki-engineering FAIL on DEPS-1 (pre-existing: @types/node, rumdl and bun past the 14-day window; package installs were out of authority) plus a pre-existing CI-1 warn.
- Retired names absent; no em or en dashes; every `ki-` token outside fences is a catalogue skill or allowed name.

## In Progress

- Nothing. Status file ends with DONE.

## Queries

- **Q1 Unlinked explaining pages.** by-outcome names these as sections without links: Ways of working (the work model, work packages, coordination, background runs, work design, trades, recurring work), Knowledge (knowledge bases, acquiring knowledge, recap and handover), Standards (repository standards, decision records, engineering and git, writing, diagrams), Harness (agent environment); the two Design rows point at the catalogue entry. Options: (a) recommended, high confidence: the unit that lands each page adds the link in by-outcome in the same commit; (b) leave by-outcome until all sections exist.
- **Q2 Figure count.** The plan's skeleton allows two figures per page but assigns eleven to how-the-skills-fit-together; I followed the assignment. Options: (a) recommended, high confidence: accept as the plan's explicit exception; (b) split the ten area figures onto a second page.
- **Q3 ki-engineering DEPS-1.** Options: (a) recommended, medium confidence: a separate small unit runs `ki:deps:update` and bumps bun; (b) record an adoption deferral.

```text
Reply: Q1 a · Q2 a · Q3 a
```
