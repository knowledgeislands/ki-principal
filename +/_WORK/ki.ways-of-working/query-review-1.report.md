# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › query-review-1

**🤖 → 👤 Handoff to supervisor · Run report at 08:35 BST · last mark 08:07 BST**

---

## Done

- Blind second opinion on BIOME-CI and SIZE-PRIORITY-EDIT, read-only: no edits, commits or pushes anywhere, net record count zero in every repository.
- Evidence read: tools-ki `ci.yml`, `release.yml`, `package.json` and the pre-commit hook; the biome-fix report and [KI-TOOL-KI-CLI-153](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-153-biome-schema-drift.md); the ki-agentic-harness working-tree diff and the current [work-item format](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-work-roadmap/references/standards-work-item-format.md); the field-survey report; the size-priority brief and status; the QUERY-REVIEW and SIZE-PRIORITY entries in the decisions log.
- Two findings the coordinator may not have in hand. First, tools-ki CI runs neither `bun run test` nor `tsc` on push either; tests run only in the release workflow, so the gap is wider than Biome. Second, the stopped edit links a section, Priority and size, that the file does not contain, so a working-tree audit of ki-work-roadmap fails while the edit stays.

## In Progress

None.

## Queries

### BIOME-CI - Keep Biome from drifting again

**Context:** The CI workflow runs the released ki's `ki repo audit` and the manual lint, nothing else; tests, the TypeScript gate and Biome all run only locally or at release. lint-staged runs Biome on staged files alone, so a Biome version bump or a rule change on untouched files is never seen until someone runs `biome check .` by hand, which is exactly how 41 findings built up. KI-TOOL-KI-CLI-153 excludes CI changes from its boundary and is awaiting review, so folding the CI step into it would send a changed candidate back to review; no other open tools-ki record covers CI or toolchain upkeep, so a new triage record is the fewest-records route. What would raise my confidence further: nothing material; a capture is cheap and reversible, and the record itself can settle whether the step is Biome alone or the whole local gate.

**Query:** Should a triage record be captured to add `bunx biome check .` to tools-ki CI for a later run?

**Options:** a) (recommended, confidence high - CI has no repo-wide lint or test step at all, lint-staged demonstrably let the drift build, and a triage record costs nothing and reverses nothing) Capture one triage record in tools-ki, scoped to make CI run the local gate, with `biome check .` first and `bun run test` and `tsc` considered in the same record rather than a second one. b) Leave CI as it is and rely on lint-staged.

### SIZE-PRIORITY-EDIT - A stopped run's uncommitted edit

**Context:** The size-priority run was stopped at 08:17 BST mid-edit. It left five added or changed lines in the harness work-item format: `priority` and `size` in the two frontmatter examples and in the required-fields sentence, which links a Priority and size section that does not yet exist. The file sits in the primary checkout, which the common rules name as the checkout other sessions commit and pull-rebase from. The edit is trivially reproducible from the decisions log, carries no work worth preserving, and its shape may change with the field discussion. While it stays, any run that audits ki-work-roadmap against the working tree fails on the broken link, and any pull that brings a change to that file refuses. What would raise my confidence further: confirmation that no other harness run is queued, which would make a) harmless though still less tidy; nothing would make me prefer a).

**Query:** Should the edit stay in place until the field discussion settles, or should a run save the diff and restore the file now?

**Options:** a) (recommended, confidence high - the diff is five lines I read directly and can be re-derived in seconds, it breaks a working-tree audit, and the shared primary checkout should hold no half-finished edit while the discussion that shapes it is open) A run saves the diff into the work folder's `design/` and restores the file now; SIZE-PRIORITY restarts from a clean tree once the field discussion settles. This is the coordinator's option b. b) Leave the edit in place until the discussion settles, then one run finishes it under the GDR or reverts it. This is the coordinator's option a.
