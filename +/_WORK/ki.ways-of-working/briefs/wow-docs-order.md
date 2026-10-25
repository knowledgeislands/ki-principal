# wow-docs-order - delivery order for the website documentation units

The ten units deliver the [merged plan](../design/website-docs.md) in the website repository `apps-knowledgeislands.info`. Each is finished and verified by one run, commits by explicit path and pushes `main` fast-forward only, which publishes it. Units that change a generator or shared layout come before the pages that use them; units that add a site-owned diagram all write `docs/diagrams/diagrams.toml`, so they never run together.

| # | Unit | Brief | Depends on | Changes shared files | May run alongside |
| --- | --- | --- | --- | --- | --- |
| 1 | Structure | [wow-docs-structure](wow-docs-structure.md) | nothing | `docsSections.json5`, `site.ts`, `docs/index.njk`, `redirects.njk`, `page.njk`, `package.json`, `featureAreas.json5`, new gates | nothing |
| 2 | Diagram pipeline | [wow-docs-diagrams](wow-docs-diagrams.md) | 1 | `eleventy.config.ts`, `.ki.toml`, `package.json`, `diagrams.toml`, CSS, `docs/ki/command-groups.md` figure | nothing |
| 3 | Skills | [wow-docs-skills](wow-docs-skills.md) | 1, 2 | `skillCatalogue.json5`, `featureAreas.json5` pages | 4 |
| 4 | ki CLI | [wow-docs-ki](wow-docs-ki.md) | 2 | `cliCommands.json5`, `featureAreas.json5` commands | 3 |
| 5 | Harness | [wow-docs-harness](wow-docs-harness.md) | 3, 4 | `diagrams.toml`, `featureAreas.json5` | nothing |
| 6 | Ways of working 1-5 | [wow-docs-work-a](wow-docs-work-a.md) | 5 | `diagrams.toml`, `featureAreas.json5` | nothing |
| 7 | Ways of working 6-8 | [wow-docs-work-b](wow-docs-work-b.md) | 6 | `diagrams.toml`, `featureAreas.json5` | nothing |
| 8 | Findings and tending | [wow-docs-work-c](wow-docs-work-c.md) | 7 | `diagrams.toml`, `featureAreas.json5` | nothing |
| 9 | Knowledge | [wow-docs-knowledge](wow-docs-knowledge.md) | 8 | `diagrams.toml`, `featureAreas.json5` | nothing |
| 10 | Standards and sweep | [wow-docs-standards](wow-docs-standards.md) | 9 | `diagrams.toml`, `featureAreas.json5`, `by-outcome.md`, landing | nothing |

Units 3 and 4 both edit `featureAreas.json5`, in different keys of different areas; each pulls fast-forward before pushing and stops on divergence, so if both finish at once the second reruns its pull. Everything else is a chain. Units 6 to 10 could run together only if the manifest were split per unit, which the `ki-diagrams` standard does not allow; the chain is the cost of one manifest.

After each unit's report is received, update the pending markers in [the review pack](../design/review-pack.md) for the pages it published and push, so the chat model reading it from GitHub sees the current state. Kris steers from the review pack; a change of plan it produces becomes a new unit here, not an edit to a finished one.
