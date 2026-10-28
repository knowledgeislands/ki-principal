# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-docs-design-fable

**🤖 → 👤 Handoff to supervisor · Run report at 03:04 GMT · last mark 03:04 GMT**

---

## Done

- Design note written and committed as `7700e558` at `+/_WORK/ki.ways-of-working/design/website-docs-fable.md` (251 lines): website survey, sources of truth, principles, section structure with page list and URLs, 18 diagrams (archify type, provenance), truth-keeping classes with two new gates (`verify:features`, `verify:skill-names`) and a `sync:diagrams`, feature-area list of 13, Docs and Projects merge, nine delivery units, review list for Kris, and 16 named decisions with confidence.
- Headline shape: Get Started · Skills (4 pages, new section) · Feature areas (13 pages, new section: work model, work packages, coordination, delegation and background runs, roadmap lifecycle, recap, trades, findings, decision records, tending, repository standards, knowledge bases, runtimes and context) · The ki CLI (10, adds work-and-agents) · Agentic Harness narrowed to 3 with redirects · Prompting, Optional Tools, Contribute unchanged · Projects joined to Docs in navigation, addresses kept.
- Website untouched. Commit hook and repo audit passed on the staged path (one commitlint warning about a footer blank line; commit accepted).
- Fetch ok. Push not done: `origin/main` has one commit this checkout lacks and local `main` is ahead by three (two from other sessions plus mine), so a fast-forward pull was refused and I stopped per the brief. The unit is committed locally and unpublished.

## In Progress

Nothing is running.

## Queries

### DOCS-IA-PUBLISH - divergence on ki-principal main

**Context:** Local `main` in ki-principal carries three unpushed commits, one of them this run's design note, and `origin/main` has one commit not here. The brief forbids rebase, reset and force-push, so the run stopped.
**Query:** How should the stacked commits reach the remote?
**Options:**
a) (recommended, confidence high - the brief names this path for a pull that cannot fast-forward) The coordinator hands the reconcile to a bounded resolve run in its own worktree, which merges or rebases the three local commits onto `origin/main` and pushes fast-forward.
b) Kris pulls with rebase in the primary checkout and pushes.

### DOCS-IA-MERGE - which design questions the merge brief should settle first

**Context:** The note's section 10 lists seven design questions for Kris: section names, the thirteen-page feature set (fold recap and runtimes to make eleven?), interim publication of tending and findings, diagram interaction (new-tab link first, overlay later), the catalogue's place, one dual-theme SVG per diagram or two exports, and depth of the ki narrative pages. The sibling Codex proposal may answer some differently.
**Query:** Should the merge brief resolve all seven, or carry the unresolved ones to Kris as queries?
**Options:**
a) (recommended, confidence medium - only Kris's reading of the site decides names and the interim banner) The merge settles the structural and tooling questions where both proposals agree and carries section names, the interim standing and the feature-set size to Kris.
b) The merge settles all seven and Kris reviews the result on the published pages.
