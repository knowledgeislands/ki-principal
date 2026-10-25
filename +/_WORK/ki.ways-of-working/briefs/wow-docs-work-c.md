# wow-docs-work-c - Ways of working, findings and tending, the interim pair

Unit 8 of the website documentation plan. It follows wow-docs-work-b. It touches `apps/site/src/docs/ways-of-working/`, `diagrams.toml`, `docs/diagrams/` and `featureAreas.json5`, so it runs alone.

Both pages describe an interim practice. Each carries one `Interim` callout under the opening claim saying the practice is in use and its standard home is not yet chosen, and nothing else about its future. Neither page mentions an open query, a proposal, a review or a decision still to be made.

## Task

Read, in `ki-principal` at its HEAD when you start: `+/_WORK/ki.ways-of-working/design/findings.md`, `design/tending.md` and `design/interim-cover.md`, together with the Findings section of the `ki-coordination` standard at harness `8897008f`. Record the `ki-principal` SHA you read as each page's source ref. Write two pages and draw three diagrams with `archify`, each with a manifest entry traced to those notes, finalised with `diagrams:build` and embedded.

| Order | Page | What it covers | Diagrams |
| --- | --- | --- | --- |
| 9 | `findings.md` | What a finding is, the finding file and its table, Goal, Scope and As of, how a finding is carried in reports, the dispositions that settle it and where a settled finding is homed, all as practised now | `finding-life` (lifecycle: opened, carried, settled, homed or dropped) |
| 10 | `tending.md`, in depth | The two tracks, structural and PMO; the four structural and five PMO levels and what each looks at; how each level picks up the captures of the one below; the focus rule; the write boundaries, what a pass may change and what it may only report; the lightweight report; the running pass as practised, described with a fictional island and no private repository or person named | `tending-tracks` (architecture: the two tracks, their levels, upward capture), `tending-pass` (workflow: focus, pass, captures, report) |

Set the two areas' `page` in `featureAreas.json5` with `interim: true`, which the `Provided by` box renders as an interim label.

## Commit and report

Commit as `docs(site): publish findings and tending as interim practices` by explicit path. Report the two URLs and the three interactive diagram URLs.

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
