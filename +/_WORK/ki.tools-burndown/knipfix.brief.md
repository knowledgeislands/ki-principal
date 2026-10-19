# knipfix - let Knip read the committed hooks directly

KNIP-HUSKY a). Once Husky goes, Knip stops seeing the hook tools. A blind review proved locally (Knip 6.42.0 in tools-ki) that configuring Knip's Husky plugin explicitly, pointed at `.githooks/pre-commit` and `.githooks/commit-msg`, finds `@commitlint/cli`, `lint-staged` and `syncpack` without any `ignoreDependencies` entries.

1. In tools-ki, under ki-work-roadmap, capture, plan and deliver a record: the conversion in `ki repo conform` (`src/core/repository/hooks.ts`) and new-repository scaffolding write that Knip configuration into `knip.json` or `knip.ts`, preserving unrelated settings, idempotent, with dry-run coverage, and remove hook-tool `ignoreDependencies` entries it makes redundant. Full gate green; leave it Awaiting review; no release.
2. In ki-agentic-harness, update the ki-engineering Knip guidance to name it, in its own commit.
3. Do not edit other repositories; the estate cleanup runs after the next release. List the repositories whose `ignoreDependencies` the cleanup will touch (tools-ki, ki-principal and those in ~/.local/state/ki/agents/tools-burndown/estmig-*.report.md).

Authority: Kris, 19 October 23:42 BST, quoted in /Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown/decisions.md. Commit by explicit path; never --no-verify or force-push; no push. Report under Done, In Progress and Queries in British English and ASCII hyphens; put anything needing Kris as a Query with a recommended option and confidence.
