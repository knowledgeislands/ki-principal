# fold-site: publish the apps-knowledgeislands.info merges

Repository: /Users/krisbrown/workspaces/knowledge-islands/apps-knowledgeislands.info. Local main is 6 commits ahead of origin: three merges of the release-bump branches (ki v0.13.0, mgit v0.18.0, rig v0.7.0) that change only version pins in apps/site/src/_data/projects.json5. Kris authorised folding all branch work into main and pushing (FOLD-TO-MAIN). The tests and type check failed only because dependencies were never installed.

1. Fetch. Registry access for this frozen install alone is authorised under FOLD-TO-MAIN, which needs the checks to pass before the push. Run `bun install --frozen-lockfile` and `bun install --frozen-lockfile --cwd tooling/depcruise`. Do not change lockfiles or dependency versions.
2. Re-run the tests, type check, site build and `ki repo audit`.
3. Push main fast-forward only if tests, type check and build pass and every remaining audit failure (e.g. DEPS-1, stale dependencies) is also present on origin/main before the merges; check that by running the audit on a clean origin/main worktree or by reasoning from the finding. Never force, never --no-verify. If origin moved, rebase onto it first.
4. Do not change `core.hooksPath` (it still points at Husky's retired `.husky/_`); report it.

Report only to /Users/krisbrown/.local/state/ki/agents/ki/fold-site.report.md: checks and results, pushed yes/no, any query with Context, Query and Options, recommended first with confidence. End with LEVEL or NOT LEVEL.
