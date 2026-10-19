# estmig-org - estate hooks migration: other organisations

Kris ordered Husky removed across the estate now. Scope: every repository with `.ki.toml` under /Users/krisbrown/workspaces/{equal-remedy,humans-not-robots,personal,legal,techmedix,valle-armonia}, except tools-ki, ki-principal and va-principal (wave1 did those). Use the released `ki` (check `ki --version` is the new release first).

For each repository:

- Skip and report it if it has uncommitted changes in `package.json`, `bun.lock`, `.husky/` or `.githooks/`, an index lock, or a merge or rebase in progress. Never touch other sessions' uncommitted files.
- With a package and Husky: `ki repo conform --dry-run`, then `ki repo conform`, then `bun install` so `prepare` binds `core.hooksPath`.
- Without a package: follow wave1's va-principal pattern, a frame-first `.githooks/pre-commit` (mode 0755) running the gates the repository already declares, no `commit-msg` until KI-TOOL-KI-CLI-161 ships, bound by conform.
- Verify: `git config core.hooksPath` is `.githooks`, no `.husky/` remains, each hook refuses with `ki` off PATH, and a real staged commit passes. Then `ki repo audit` shows no HOOK failure.
- Commit the conversion as `build(hooks): standardise committed githooks and retire husky`.

Where conform refuses, record the reason and move on.

Authority: Kris, 19 October 23:24 BST, quoted in /Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown/decisions.md. Commit by explicit path in each repository; never --no-verify or force-push; no push. Report under Done, In Progress and Queries in British English and ASCII hyphens, with one line per repository; put anything needing Kris as a Query with a recommended option and confidence.
