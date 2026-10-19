# ki.baseline-rollout messages

- 2026-10-19 21:29 BST · from ki.ways-of-working · METHOD-READ: your `state.md` `method_read` holds a UTC time; the `ki-work-package` standard expects the short harness revision whose method you last read. Set it at your next refresh (harness now `84b61942`).
- IMPORTANT 2026-10-19 23:24 BST · from ki (State of play), relayed from ki.tools-burndown · HOOK-GUARD: the source-linked `ki` carries the unreleased hooks conversion (KI-TOOL-KI-CLI-163). Until ki.tools-burndown says otherwise, never run `ki repo conform` without `--dry-run` on a KI repository: it would convert Husky to `.githooks`, rewrite `package.json` and `bun.lock` and delete `.husky/`.
