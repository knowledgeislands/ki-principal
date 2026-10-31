# ki.reg.main queries

## Open

### RELEASE-GO - Release Stoa with the import-cycle fix and the new icons

**Context:** The unattended window's unit U4 put both STOA-ICONS changes on `packages-stoa` `main` at `b4bf2d4`, on top of 0.31.0: the Theme Engine import cycle is gone and all 46 requested icon names render, six of them with an approximate Phosphor glyph (the two right-panel names share the left panel's `sidebar-simple`, `list-x` uses `list-dashes`, `message-circle-question-mark` uses `chat-circle-dots`, and the two distribute-centre names use `columns` and `rows`). Tests, typecheck and lint pass. Nothing is versioned, tagged or published, so the 5G Emerge apex, Infoschematics, demos and Phase 2 Phosphor moves stay blocked until a release ships and hnr.sop.5ge hears its version. Kris agreed "one release fixing both" on 29 October; the release itself was left out of the window.

**Query:** Shall Stoa be released now from `main` with both changes?

**Options:**

a) (recommended, confidence high - both changes are the release Kris already agreed, and every check passes) Release it as 0.32.0, a new-feature minor release, after a look at the icons in the workbench, then send each consumer its re-vendor line and reply with the version to hnr.sop.5ge.

b) Review the six approximate icon choices first and change any before releasing.

## Parked

None.
