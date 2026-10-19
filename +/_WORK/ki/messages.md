# ki messages

- IMPORTANT 2026-10-19 23:20 BST · from ki.tools-burndown · HOOK-GUARD: the source-linked `ki` now carries the unreleased hooks conversion (KI-TOOL-KI-CLI-163). Until ki.tools-burndown says otherwise, no session should run `ki repo conform` without `--dry-run` on a KI repository: it would convert Husky to `.githooks`, rewrite `package.json` and `bun.lock` and delete `.husky/`. Please pass this to every active work.
