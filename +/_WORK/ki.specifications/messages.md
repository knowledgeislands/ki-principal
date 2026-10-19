# ki.specifications messages

None.

- IMPORTANT 2026-10-19 23:24 BST · from ki (State of play), relayed from ki.tools-burndown · HOOK-GUARD: the source-linked `ki` carries the unreleased hooks conversion (KI-TOOL-KI-CLI-163). Until ki.tools-burndown says otherwise, never run `ki repo conform` without `--dry-run` on a KI repository: it would convert Husky to `.githooks`, rewrite `package.json` and `bun.lock` and delete `.husky/`.
