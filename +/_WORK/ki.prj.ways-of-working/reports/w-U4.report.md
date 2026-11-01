# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › w-U4

**🤖 → 👤 Handoff to supervisor · Run report at 02:51 GMT · last mark 01:31 GMT**

---

## Done

- Stoa import cycle removed: `solarScrub` now lives in its own small module, `packages/stoa/src/theme-engine/solar-scrub.js`, so the Sun Dial no longer imports the Theme Engine element back. Both existing exports work exactly as before. A new test, `packages/stoa/test/import-graph.test.js`, walks every Stoa module's imports and fails on any cycle; I confirmed it fails when the old import is put back. Commit `bc06773` in `packages-stoa`.
- Stoa icons added: `packages/stoa/src/icons/mapping.js` now maps all 46 requested names to Phosphor Duotone (44 distinct names, because `maximize-2` and `grid-3x3` were each asked twice), and the icon data was regenerated from the locally cached Phosphor 2.1.1, with no download. A new test renders every requested name in both weights. `CHANGELOG.md` records both changes under Unreleased. Commit `b4bf2d4` in `packages-stoa`.
- Six icons are near matches, not exact, because Phosphor has no exact glyph: `panel-right-close` and `panel-right-open` use the same sidebar icon as the left-panel names, `list-x` uses `list-dashes`, `message-circle-question-mark` uses `chat-circle-dots`, and the two distribute-centre names use `columns` and `rows`.
- Checks in `packages-stoa`: tests pass (245 passed, 1 skipped, 0 failed), typecheck passes, lint passes. Both commits are on `main` and pushed. No version bump, tag, publish or visibility change. I did not do the visual check in the workbench; it needs a browser and belongs with the release.
- Release-ready note: [ki.reg.main decisions](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.reg.main/decisions.md) records the delivery. The query RELEASE-GO in [ki.reg.main queries](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.reg.main/queries.md) asks Kris for the release go when they return. I kept the STOA-ICONS line in [ki.reg.main messages](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.reg.main/messages.md), now pointing to that query, because the release and the version reply to hnr.sop.5ge are still outstanding. I left the package's state and hold alone. Commit `6b82777b` in ki-principal.
- My worktree and its branch have been removed, and the temporary folder is empty. Nothing from the private repository was copied anywhere else.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- The STOA-ICONS release, the re-vendor lines to Stoa's consumers and the version reply to hnr.sop.5ge all wait on RELEASE-GO. Unit U22 may move that release line into its new package.

## Queries

### RELEASE-GO - Release Stoa with the import-cycle fix and the new icons

**Context:** Both STOA-ICONS changes are now on `packages-stoa` `main` at `b4bf2d4`, on top of 0.31.0. The Theme Engine import cycle is gone, and all 46 requested icon names render, six of them with a near-match Phosphor icon (listed in Done). Tests, typecheck and lint pass. Nothing is versioned, tagged or published, so the 5G Emerge apex, Infoschematics, demos and Phase 2 Phosphor moves stay blocked until a release ships and hnr.sop.5ge hears its version. Kris agreed to "one release fixing both" on 29 October. The release itself was left out of the window.

**Query:** Should Stoa be released now from `main` with both changes?

**Options:**

a) (recommended, confidence high - this is the release Kris already agreed to, and every check passes) Release it as 0.32.0, a minor release for the new icons, after a look at the icons in the workbench. Then send each consumer its re-vendor line and reply to hnr.sop.5ge with the version.

b) Review the six near-match icons first and change any of them before releasing.
