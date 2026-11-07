# [Foundations](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Themes/foundations.md) › [Stoa](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/stoa.md) › stoa-names

**🤖 → 👤 Handoff to supervisor · Run report at 05:07 GMT · last mark 05:07 GMT**

---

## Done

- Under the decision "STOA-AUDIT-REST b) - everything is Stoa, house conventions throughout", `packages-stoa` no longer mentions the portal-framework or Portal Commons names anywhere except one place: the new changelog line (see In Progress). The old element, event, property, shortcode and lock names in the records, the audit note and the changelog's past release notes now use their current `stoa` names. Where "the framework" meant Stoa, it now says Stoa.
- Commit `4610eb2` brings the decision records into the `STOA` scope. All 58 records keep their numbers, so the ADR series now runs unbroken from `ADR-STOA-001` to `055`. Each file is named after its title. Every record has the standard frontmatter, Context and Consequences sections, and links only to other records. Records 022 to 048 had no Context section, so each now has one, written from the record's own text. Records 032 to 037 also had no Consequences section and now have one. `ADR-STOA-027`, `ADR-STOA-052` and `GDR-STOA-001` were rewritten to describe the decision as it stands now. The index is now an ordered list in reading order. No alias for any old id remains.
- Commit `cfd8518` (`refactor(tooling)!`) removes the `PORTAL_FRAMEWORK_CHECKOUT` fallback and the legacy lock and package-folder migration from the vendoring tools and their test. It also adds the **Breaking** line under `## Unreleased` in `CHANGELOG.md` and puts the changelog header and past notes in Stoa terms.
- Commit `2ef9af3` makes the same name changes in the READMEs, the custom-elements audit note, code comments, tests and the `tsconfig.json` display name.
- Checks: `git grep -i -E "portal.?framework|portal.?commons"` finds nothing. The decision-records audit passes, where it had 293 failures before. `bun run test` passes (252 + 3). `bun run typecheck` passes. `bun run lint` passes with the same 8 warnings as before. `git status` is clean.
- `ki repo audit --repo .` shows nothing new failing. Engineering still has its 18 failures, which belong to the `stoa-toolchain` run. The repository audit now reads live GitHub settings and fails on 8 of them: description, merge policy, feature toggles and Dependabot. Those belong to the `stoa-github` run.

## In Progress

- One use of an old name remains, on purpose: the Unreleased **Breaking** line names `portal-lock.json`, because a site has to know which file to rename. The brief's check pattern does not match it. The old checkout variable appears there only as `…_FRAMEWORK_CHECKOUT`, so the zero-match check holds. Git commit messages still contain the old names; history is not rewritten.
- A candidate for a roadmap record, not created: the decision records and the 0.1.0 to 0.21.0 changelog notes still say "gallery" for what is now the workbench. Those sentences describe what the gallery showed, and I could not confirm that the workbench shows the same things, so I left them.
- Other repositories cite the old ids. The table below is for them. I made no change outside `packages-stoa`.

## Findings

### STOA-NAMES - Old to new decision-record ids

**Goal:** Let other repositories update their citations of the old decision-record ids.

**Scope:** Every record in `packages-stoa/docs/decisions/`, as of commit `4610eb2`.

**As of:** 7 November 2026, 05:07 GMT.

| Old id | New id | New file |
| --- | --- | --- |
| `ADR-PORTAL-FRAMEWORK-001` | `ADR-STOA-001` | `ADR-STOA-001-vendored-web-components-from-one-canonical-source.md` |
| `ADR-PORTAL-FRAMEWORK-002` | `ADR-STOA-002` | `ADR-STOA-002-theme-semantics-and-site-owned-adapters.md` |
| `ADR-PORTAL-FRAMEWORK-003` | `ADR-STOA-003` | `ADR-STOA-003-shared-theme-state-pre-paint-and-events.md` |
| `ADR-PORTAL-FRAMEWORK-004` | `ADR-STOA-004` | `ADR-STOA-004-page-foot-and-site-footer-with-site-owned-source-adapters.md` |
| `ADR-PORTAL-FRAMEWORK-005` | `ADR-STOA-005` | `ADR-STOA-005-header-frame-with-site-owned-navigation-and-slots.md` |
| `ADR-PORTAL-FRAMEWORK-006` | `ADR-STOA-006` | `ADR-STOA-006-shortcut-help-placement-outside-the-default-header-frame.md` |
| `ADR-PORTAL-FRAMEWORK-007` | `ADR-STOA-007` | `ADR-STOA-007-progressive-image-and-svg-diagram-viewer.md` |
| `ADR-PORTAL-FRAMEWORK-008` | `ADR-STOA-008` | `ADR-STOA-008-static-issues-list-contract-and-rendering.md` |
| `ADR-PORTAL-FRAMEWORK-009` | `ADR-STOA-009` | `ADR-STOA-009-explicit-trusted-markup-for-diagram-viewer-captions.md` |
| `ADR-PORTAL-FRAMEWORK-010` | `ADR-STOA-010` | `ADR-STOA-010-site-owned-issue-vocabulary-and-owners.md` |
| `ADR-PORTAL-FRAMEWORK-011` | `ADR-STOA-011` | `ADR-STOA-011-site-owned-issue-row-attributes.md` |
| `ADR-PORTAL-FRAMEWORK-012` | `ADR-STOA-012` | `ADR-STOA-012-opt-in-strict-issue-validation.md` |
| `ADR-PORTAL-FRAMEWORK-013` | `ADR-STOA-013` | `ADR-STOA-013-named-next-call-issue-links.md` |
| `ADR-PORTAL-FRAMEWORK-014` | `ADR-STOA-014` | `ADR-STOA-014-optional-issues-list-heading.md` |
| `ADR-PORTAL-FRAMEWORK-015` | `ADR-STOA-015` | `ADR-STOA-015-preserve-diagram-interaction-across-resize.md` |
| `ADR-PORTAL-FRAMEWORK-016` | `ADR-STOA-016` | `ADR-STOA-016-composite-typescript-plugin-inputs.md` |
| `ADR-PORTAL-FRAMEWORK-017` | `ADR-STOA-017` | `ADR-STOA-017-explicit-sync-commit-attribution.md` |
| `ADR-PORTAL-FRAMEWORK-018` | `ADR-STOA-018` | `ADR-STOA-018-calendar-timeline.md` |
| `ADR-PORTAL-FRAMEWORK-019` | `ADR-STOA-019` | `ADR-STOA-019-build-commit-provenance.md` |
| `ADR-PORTAL-FRAMEWORK-020` | `ADR-STOA-020` | `ADR-STOA-020-calendar-today-board.md` |
| `ADR-PORTAL-FRAMEWORK-021` | `ADR-STOA-021` | `ADR-STOA-021-exact-field-filters.md` |
| `ADR-PORTAL-FRAMEWORK-022` | `ADR-STOA-022` | `ADR-STOA-022-calendar-feed-capability.md` |
| `ADR-PORTAL-FRAMEWORK-023` | `ADR-STOA-023` | `ADR-STOA-023-recurrence-exception-dates.md` |
| `ADR-PORTAL-FRAMEWORK-024` | `ADR-STOA-024` | `ADR-STOA-024-calendar-view-selection.md` |
| `ADR-PORTAL-FRAMEWORK-025` | `ADR-STOA-025` | `ADR-STOA-025-page-foot-style-scope.md` |
| `ADR-PORTAL-FRAMEWORK-026` | `ADR-STOA-026` | `ADR-STOA-026-self-contained-search-trigger-icon.md` |
| `ADR-PORTAL-FRAMEWORK-027` | `ADR-STOA-027` | `ADR-STOA-027-page-foot-data-keys.md` |
| `ADR-PORTAL-FRAMEWORK-028` | `ADR-STOA-028` | `ADR-STOA-028-issues-list-labels.md` |
| `ADR-PORTAL-FRAMEWORK-029` | `ADR-STOA-029` | `ADR-STOA-029-issues-list-row-fragments.md` |
| `ADR-PORTAL-FRAMEWORK-030` | `ADR-STOA-030` | `ADR-STOA-030-issues-list-source-row-access.md` |
| `ADR-PORTAL-FRAMEWORK-031` | `ADR-STOA-031` | `ADR-STOA-031-rich-issue-registers.md` |
| `ADR-PORTAL-FRAMEWORK-032` | `ADR-STOA-032` | `ADR-STOA-032-validate-build-revisions.md` |
| `ADR-PORTAL-FRAMEWORK-033` | `ADR-STOA-033` | `ADR-STOA-033-opt-in-build-day-dating.md` |
| `ADR-PORTAL-FRAMEWORK-034` | `ADR-STOA-034` | `ADR-STOA-034-short-build-identifiers-retain-dirty-state.md` |
| `ADR-PORTAL-FRAMEWORK-035` | `ADR-STOA-035` | `ADR-STOA-035-package-owned-test-fixtures.md` |
| `ADR-PORTAL-FRAMEWORK-036` | `ADR-STOA-036` | `ADR-STOA-036-all-day-weekly-recurrence.md` |
| `ADR-PORTAL-FRAMEWORK-037` | `ADR-STOA-037` | `ADR-STOA-037-optional-today-board-links.md` |
| `ADR-PORTAL-FRAMEWORK-038` | `ADR-STOA-038` | `ADR-STOA-038-preserve-page-foot-fallback-renderer-inputs.md` |
| `ADR-PORTAL-FRAMEWORK-039` | `ADR-STOA-039` | `ADR-STOA-039-ordered-dated-issue-histories.md` |
| `ADR-PORTAL-FRAMEWORK-040` | `ADR-STOA-040` | `ADR-STOA-040-optional-issue-resolution-dates.md` |
| `ADR-PORTAL-FRAMEWORK-041` | `ADR-STOA-041` | `ADR-STOA-041-multiple-issue-areas-and-site-owned-splitting.md` |
| `ADR-PORTAL-FRAMEWORK-042` | `ADR-STOA-042` | `ADR-STOA-042-self-contained-command-bar-dialog-search-icon.md` |
| `ADR-PORTAL-FRAMEWORK-043` | `ADR-STOA-043` | `ADR-STOA-043-opt-in-to-page-ids-for-page-foot.md` |
| `ADR-PORTAL-FRAMEWORK-044` | `ADR-STOA-044` | `ADR-STOA-044-full-revision-in-build-metadata.md` |
| `ADR-PORTAL-FRAMEWORK-045` | `ADR-STOA-045` | `ADR-STOA-045-explicit-timezone-for-build-day-dating.md` |
| `ADR-PORTAL-FRAMEWORK-046` | `ADR-STOA-046` | `ADR-STOA-046-record-adoption-at-existing-unit-boundaries.md` |
| `ADR-PORTAL-FRAMEWORK-047` | `ADR-STOA-047` | `ADR-STOA-047-optional-issues-list-ownership-and-call-columns.md` |
| `ADR-PORTAL-FRAMEWORK-048` | `ADR-STOA-048` | `ADR-STOA-048-sectioned-registers-stay-site-owned-markdown.md` |
| `ADR-PORTAL-FRAMEWORK-049` | `ADR-STOA-049` | `ADR-STOA-049-time-of-day-colour-mode.md` |
| `ADR-PORTAL-FRAMEWORK-050` | `ADR-STOA-050` | `ADR-STOA-050-holding-time-of-day-at-a-chosen-moment.md` |
| `ADR-PORTAL-FRAMEWORK-051` | `ADR-STOA-051` | `ADR-STOA-051-mode-selection-and-solar-phases.md` |
| `ADR-STOA-052` | `ADR-STOA-052` | `ADR-STOA-052-named-stoa-the-theme-engine-names-its-keys-from-a-prefix.md` |
| `ADR-STOA-053` | `ADR-STOA-053` | `ADR-STOA-053-preview-overrides-and-an-isolated-workbench-stage.md` |
| `ADR-STOA-054` | `ADR-STOA-054` | `ADR-STOA-054-compact-mode-icons-and-the-solar-dial.md` |
| `ADR-STOA-055` | `ADR-STOA-055` | `ADR-STOA-055-the-command-k-palette-jumps-to-sister-sites.md` |
| `GDR-PORTAL-FRAMEWORK-001` | `GDR-STOA-001` | `GDR-STOA-001-adopting-decision-records.md` |
| `PDR-PORTAL-FRAMEWORK-001` | `PDR-STOA-001` | `PDR-STOA-001-the-v0-1-first-cut.md` |
| `PDR-PORTAL-FRAMEWORK-002` | `PDR-STOA-002` | `PDR-STOA-002-forward-extraction-releases-and-pilot-order.md` |

## Queries

None.
