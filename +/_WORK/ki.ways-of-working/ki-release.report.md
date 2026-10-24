# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › ki-release

**🤖 → 👤 Handoff to supervisor · Run report at 19:43 BST · last mark 19:08 BST**

---

## Done

- `ki` v0.11.3 is released, signed and immutable. The release workflow passed every job: the three builds, signing and publishing, the Homebrew notification and the clean Linux install check.
- The Homebrew tap opened "Advance ki to v0.11.3" (PR #46), and it merged automatically after its checks passed.
- This Mac's Homebrew `ki` is now 0.11.3 and reports itself as a release install. The `ki` first on the PATH is still the local link to the tools-ki checkout, which also reports 0.11.3.
- The release pins ki-agentic-harness main at `fdbb73d8`, with its archive digest checked twice (commit `9cc2f0b6`). That commit includes:
  - GLYPH-OWNER and RESUME-PWD, from commit `5f8d6165`
  - [KI-HARNESS-GOV-197](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-197-pmo-7-outside-checkout-links.md)
  - SCR-11
  - the ki-repo-tools command-line conventions
- I tagged and released v0.11.3 the same way as v0.11.2: a plain tag, then the release workflow dispatched by hand. The "signed" part is the Ed25519-signed checksum manifest, as the release guide describes.
- CLI-F-FILTER c) is shipped in v0.11.3 (commit `3cc88f4f`, `feat(cli)!`). The tests were written first.
  - `ki repo`, `ki registry` and the `ki territory` selectors now accept only `--filter`.
  - `-f` is now a usage error: it exits 2, names `--filter` and runs nothing.
  - Help, completions, the manual, the command list, the README, the territories spec, the user guide and the changelog are all updated.
- tools-ki CI on main had been red since the threads-fix commit. It is green again on the release commit.
  - Cause 1: the generated command list in `man/` was out of date. The regenerated copy is in `3cc88f4f`.
  - Cause 2: some threads-fix code paths had no tests, so 100% coverage failed. I added tests for them in `4f0bf1a8`.
- The launch part of [KI-TOOL-KI-CLI-150](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-150-work-folder-entry-points.md) is not small, so it waits for a later release.
  - The record is still in triage, and its planning questions are open.
  - Refusing a report path inside the work folder would reject the current common rules. Those rules, including the ones for this batch, still send reports to `$D/<name>.report.md`.
  - The record now says that v0.11.3 shipped the threads-fix part and the launch part still needs planning (`32b2f7a9`).
- ki-principal CI now installs v0.11.3 (`9d2830a`).
  - The CI result is a failure, the same as the three runs before it.
  - The harness pin works: CI installed v0.11.3 with harness `fdbb73d8`, and it shows none of the "missing" link findings the local audit still shows. GOV-197's shape check is doing its job.
  - Something else keeps it red. 17 work reports mention record identifiers without linking them (COORD-7). Also, `+/_WORK/ki.observatory/work.md` breaks the RECORD-2 hold schema. See the PRINCIPAL-CI-RED query.
- Checks:
  - tools-ki: 1348 of 1348 tests passed, with full coverage
  - `tsc`: passed
  - Biome on the changed files: passed
  - `ki repo audit`: passed, with 0 failures
  - mandoc lint and rumdl: clean
  - the built `ki` and the source launcher both report 0.11.3
- Pushes were all fast-forward, and no other session's commits were stacked under mine:
  - tools-ki: `4f0bf1a8`, `3cc88f4f`, `9cc2f0b6`, `4b2506f1` and `32b2f7a9`, plus the `v0.11.3` tag
  - ki-principal: `9d2830a`
- In ki-principal, `git pull --rebase` refused to run because of another session's modified file. Origin had not moved, so the push still went through as a fast-forward, and the checkout is level with origin.
- Nothing was published to npm.
- Net records: 0 in tools-ki and 0 in ki-principal.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Running `bunx biome check` on the whole of tools-ki reports problems that were already there:
  - a Biome config schema mismatch (2.5.12 against 2.5.15) left by the dependency update
  - style errors in files this run did not touch
  - CI and the pre-commit hook do not catch these, because they check only staged files.
- Other sessions' uncommitted files in ki-principal were left alone:
  - `+/_WORK/ki.ways-of-working/mgit-filter.report.md` (modified)
  - `+/_WORK/ki.chezmoi/mark-tidy-current.report.md` (untracked)
  - `+/_WORK/ki.ways-of-working/small-fixes.report.md` (untracked)
- This report is only at the run's state-folder path, as the progress protocol requires. `ki` copies it into the work folder, so I did not commit a copy in ki-principal.

## Queries

### PRINCIPAL-CI-RED - Clear the COORD-7 and RECORD-2 failures in ki-principal

**Context:** ki-principal CI installs v0.11.3, and its shape check for links outside the checkout passes. It still fails on two kinds of finding:

- 17 reports mention record identifiers without linking them. The reports are in the ki.chezmoi, ki.tools-burndown and ki.ways-of-working work folders, and they include gov197-hook, prune-held, rig-lock-review and mgit-filter.
- `+/_WORK/ki.observatory/work.md` breaks the RECORD-2 hold schema.

**Query:** How should ki-principal CI be made green?

**Options:**

a) (recommended, confidence high - each work keeps writing its own files, and it is the fastest route to green CI) One run adds the missing links to the ways-of-working reports. ki.chezmoi, ki.tools-burndown and ki.observatory each get a Messages line asking them to fix their own reports or work file.
b) Prune the affected reports at the next mark instead of linking them, and send ki.observatory a Messages line about its hold fields.
c) Leave CI red until each work's next tidy.

### CLI-150-LAUNCH - Plan the launch part of KI-TOOL-KI-CLI-150

**Context:** The rest of [KI-TOOL-KI-CLI-150](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-150-work-folder-entry-points.md) has not been released. That includes:

- the run outline using the state-folder report path
- `launch` and `queue` refusing a brief that sends its report into `+/_WORK/<id>/`
- the matching run-prompt wording in the harness

The record is still in triage. Today's common rules still send reports into the work folder.

**Query:** Should the launch part be planned to Ready now, so that it ships in the next `ki` release?

**Options:**

a) (recommended, confidence medium - the common rules have to change before the refusal, or every live brief breaks) One planning run makes the launch part Ready with the harness wording. The coordinators' common rules move to the state-folder path first, and then the refusal ships in the next release.
b) Plan the whole record, including the close-gate parsing, `decide`, `ki work message` and `ki work prune`, as one release.
c) Leave it in triage.
