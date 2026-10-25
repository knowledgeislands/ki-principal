# wow-docs-standards - the Standards section and the closing sweep

Unit 10 of the website documentation plan, the last. It follows wow-docs-knowledge. It touches `apps/site/src/docs/standards/`, `diagrams.toml`, `docs/diagrams/`, `featureAreas.json5`, the Docs landing copy and `skills/by-outcome.md`, so it runs alone.

## Task

1. Write five pages at the plan's addresses and orders, each following the skeleton, and draw their diagrams with `archify`, each with a manifest entry, finalised with `diagrams:build` and embedded.

| Order | Page | Sources to read | Diagrams |
| --- | --- | --- | --- |
| 1 | `repository-standards.md` | `ki-repo` and the `ki-repo-*` shapes, `ki-bootstrap`; `ki-principal` `+/_WORK/ki.ways-of-working/design/repository-metadata.md` for an `Interim` section describing repository metadata as it works now, recorded at the SHA you read | `repository-shapes` (architecture: universal contract, shapes, overlays), `audit-conform` (workflow: educate, audit, conform, re-audit) |
| 2 | `decision-records.md` | `ki-decision-records` | `decision-to-record` (workflow: logged decision, record type, review, durable rationale) |
| 3 | `engineering-and-git.md` | `ki-engineering`, `ki-git` | `standards-layers` (architecture: universal, shape, repository) |
| 4 | `writing.md` | `ki-authoring`, `ki-guides`, `ki-specs` | none |
| 5 | `diagrams.md` | `ki-diagrams` standard and rubric | `diagram-regeneration` (workflow: source, build, export, receipt, freshness) |

2. Closing sweep: set every remaining `page` in `featureAreas.json5` so no area is without one and `verify:features` passes with the full crosswalk; turn every plain section name left by earlier units in `skills/by-outcome.md`, the CLI pages and the harness pages into a link; check the Docs landing hero and the section descriptions read correctly for ten sections; confirm `verify:reachable` reaches every page from the home page.

## Commit and report

Make two commits by explicit path: `docs(site): publish the Standards section` and `docs(site): complete the feature-area crosswalk and section links`. Report the five URLs, the five interactive diagram URLs and the full page count of the Docs landing.

## Common rules for every wow-docs unit

- Work in the website repository `/Users/krisbrown/workspaces/knowledge-islands/apps-knowledgeislands.info` on `main`. Read its `AGENTS.md`, `docs/guides/developer/docs-sections.md`, `page-provenance.md`, `what-to-publish.md` and `prose-styling.md` first, then the merged plan `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/website-docs.md`, which settles every design question; do not reopen one. Do not edit `ki-principal`, the harness or `tools-ki`.
- The reader is a user of Knowledge Islands, not a developer. Each new Markdown page follows the plan's skeleton: an opening claim of at least 120 characters, at most two figures, `## What it is`, `## How it works`, `## How you use it`, `## What it provides`, `## Boundaries`, the generated `Provided by` box and the provenance footer. No hand-off link text. British English, ASCII hyphens only, no em-dashes or en-dashes. Worked examples use a fictional island and fictional people; never name a private repository or a person.
- The website shows only the settled current state. Never mention an open owner query, a proposal or future work. An interim practice carries one `Interim` callout under the opening claim and is described as it works now.
- Pin sources: harness pages `repository: knowledgeislands/ki-agentic-harness`, `ref: 8897008f` (use the full 40-character SHA from `git -C /Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness rev-parse 8897008f`); `tools-ki` pages `ref: v0.13.0`; `ki-principal` pages the full SHA of the commit you read. Quote `governs` and `reviewed`; `reviewed` is today's date.
- Every `ki-...` skill name you write must exist in the vendored catalogue at `apps/site/src/_data/skillCatalogue.json5`. Read the skill's `SKILL.md` and `references/` in the harness checkout at the pinned ref (`git -C <harness> show 8897008f:skills/<concern>/<skill>/SKILL.md`), not the working tree.
- Diagrams follow the `ki-diagrams` standard (`skills/governance/ki-diagrams/` in the harness) and are drawn with the `archify` skill: one of the five manifest types, JSON source, `svg_form = "ki"` SVG, `commit_html = true` with HTML and receipt, a `diagrams.toml` entry with `question`, `audience`, `traced`, `stale_when`, `regenerate` and `last_checked`. Embed with the `figure` shortcode the diagram pipeline unit added. Finalise with `bun run --cwd apps/site diagrams:build -- --svg <slug>` as that unit documents.
- Checks, all of which must pass before you commit: `bun run ki:site:build` from the repository root (it runs every `verify:*` gate), `bun run --cwd apps/site test`, `bun run --cwd apps/site typecheck`, then `ki repo audit --skill ki-repo-website-content --repo .`, `ki repo audit --skill ki-engineering --repo .`, `ki repo audit --skill ki-authoring --repo .` and, once `.ki.toml` declares it, `ki repo audit --skill ki-diagrams --repo .`. If `node_modules` is missing, stop and report rather than installing. After removing or moving a route run `bun run ki:site:clean` and build again.
- Commits: Conventional Commits with scope `site`, local, staged by explicit path only, ending with the co-author trailer naming your model. Never `--no-verify`, never a force-push, never touch another session's uncommitted files.
- Publishing: after the checks pass, `git fetch -q`, `git pull -q --ff-only`, then `git push -q origin main` fast-forward only. Pushing `main` deploys the site. Stop on divergence and report it; do not rebase, reset or stash.
- No other network call: no GitHub API, no package installs, no `verify:provenance -- --network`.
- Report in under 30 lines in owner-report form: Done with the commit identifiers and one line per check, In Progress, Queries. Name every published URL as `https://knowledgeislands.info<path>`, noting that the deploy completes after the push. Put a design choice you had to make that the plan did not settle in Queries with a recommended option; do not block on it.

## Gate baseline note (04:47 GMT)

Follow the plan's Gate baseline section in `design/website-docs.md`: the engineering audit's DEPS-1 dependency-age failure and CI-1 warning are the pre-existing baseline. Once the site build with every gate, the tests, the typecheck and the website-content, authoring and diagrams audits pass, commit only your own paths by explicit path and push fast-forward, naming DEPS-1 in your report. Never install or update dependencies. Other units may be working in the same checkout: never stage, revert or touch their files. Also follow the plan's Linking back from Skills by outcome section.
