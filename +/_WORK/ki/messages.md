# ki messages

- IMPORTANT 2026-10-19 23:24 BST · from ki.tools-burndown · HOOKS-MIGRATION: by Kris's order the estate moves from Husky to committed `.githooks` tonight, once the new ki release is out. Runs convert every `.ki.toml` repository, skipping any with uncommitted changes in `package.json`, `bun.lock`, `.husky/` or `.githooks/`. Commit those paths soon so they are not skipped. This replaces the earlier HOOK-GUARD warning.
