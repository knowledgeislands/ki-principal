# wow-tidy-night - clean the work packages and the roadmaps

Kris, 25 October 2026 (DOCS-PUBLISH in `+/_WORK/ki.ways-of-working/decisions.md`): "make sure the work packages are cleaned up, make sure the roadmap's all cleaned up". Follow `ki-work-package` Tidying the work folder and `ki-work-roadmap`. Do not touch `+/_WORK/ki.ways-of-working/decisions.md`, `queries.md`, `messages.md`, `state.md`, `briefs/` or `design/` (the coordinator and live runs write them), and do not touch the website repository.

1. This package, `+/_WORK/ki.ways-of-working/`: it holds dozens of old `*.report.md` copies. For each, delete it by explicit path when its outcome has a durable home (a commit, record, decision entry or package file) and its queries are already in `queries.md` or answered in `decisions.md`; keep any in doubt and list them. Also check the ten kept in doubt by the earlier orphan sweep (named in decisions.md under wow-orphan-sweep).
2. Every other package under `+/_WORK/` in ki-principal: run the `ki-work-package` audit; do not edit another package's files. For each package the rubric flags, append one line to that package's `messages.md` naming the finding and the fix its steward should make, as the territory mark does.
3. Roadmaps: run the roadmap and Streams audits in ki-principal (`Streams/Roadmap/`) and ki-agentic-harness (`docs/roadmap/`). Fix only mechanical defects (broken links, index entries, front-matter shape, stale dependency references) by explicit path. Never change a record's state, accept, cancel, prune or adopt; list records that look ready for those moves for Kris.

Commit each repository's changes by explicit path, sync fast-forward only, stop on divergence, never `--no-verify`. Report in under 30 lines with counts and the list for Kris.
