# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-reader

**🤖 → 👤 Handoff to supervisor · Run report at 19:13 BST · last mark 19:02 BST**

---

## Done

- I folded the scope into [KI-OBSERVA-VIS-025 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/02cb729bf7a8c2fc9305ef4c597a19acd8e968e4/docs/roadmap/KI-OBSERVA-VIS-025-work-instrument.md) (Work Instrument), delivered it, and left it Awaiting review. Commits `a9fb2ed` (scope fold) and `53a40b0` (delivery), both local in apps-observatory.local and not pushed.
- The Work Instrument now reads both folder shapes. Single-file folders still go through `ki work status`. Five-file packages, which have a `state.md`, are read by the new `packages/evidence/src/work-package.ts`. It reads only the front matter of `work.md` and `state.md`, applies the same checks `ki` makes, and adds the runs homed in each folder. The `ki work status` hand-off point is clear: wherever `ki` reports a folder, its entry is used. Once `ki` reads packages, the new module adds nothing and can be deleted.
- `ki work status` can't take over yet: the installed `ki` 0.11.4 rejects every migrated folder in ki-principal and reports no work there. Until this delivery, the Work Instrument showed nothing for ki-principal.
- `review.ts` now dates review-held folders by `state.md` where one exists, falling back to `work.md`.
- **Item 4 holds.** A fixture of each shape gives the same Work Instrument report before and after migration. I also checked the 11 real migrated ki-principal folders: `ki`'s reading of each old `work.md` and the new reader's reading of each migrated `work.md` and `state.md` gave the same entries in all 11. Run against the live territory, the reader lists all 12 works with their runs.
- Checks: `bun run test` passed; `bun run self:typecheck` passed; `bun run build` passed; `bunx knip` passed; `bunx rumdl check .` passed; `bunx biome check` found nothing in the touched files; `ki repo audit` has no failures.

## In Progress

- The Observatory service needs a restart to serve this delivery. I didn't restart it, as the brief said.
- The ki-principal migration ran before the installed `ki work status` could read the new shape, which the migration gate (point 42) required. `ki work status` is still blind to packages until ki.tools-burndown changes the tools-ki reader.

## Queries

### OBS-PACKAGE-FOLLOWUPS - Two Observatory readers still use the old shape

**Context:** Feedback send writes only into the `## Messages` section of `work.md`, so it refuses to send to any migrated work. Feedback send is switched off for now. The Review queue takes open queries from run reports, not from `queries.md`. Once reports are pruned after their queries are copied into `queries.md`, those queries will drop out of the Review queue.

**Query:** Should these two be captured as Observatory records now?

**Options:** a) (recommended, confidence high - both break as the migrated works tidy up) capture two triage records under `ki-next`: feedback writing to `messages.md`, and the Review queue reading `## Open` in `queries.md`. b) Capture only the Review queue one, since feedback send is still switched off. c) Leave both until the migration pass has finished.
