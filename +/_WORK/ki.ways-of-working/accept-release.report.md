# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › accept-release

**🤖 → 👤 Handoff to supervisor · Run report at 08:32 BST · last mark 08:07 BST**

---

## Done

- [KI-TOOL-KI-CLI-150](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-150-work-folder-entry-points.md) is accepted as done under CLI-150-ACCEPT a), in tools-ki `fa31efee`. Its `## Done` section cites the decision and the review-cli150 review, and lists the review's three minor points as known limits: subfolders of a work folder only draw a warning, a refused queued copy is left behind, and the retired-home refusal message is unclear. Before accepting, I re-ran the checks at `c2a9a062`: coverage passed (1,350 tests), and tsc, Biome on the whole tree, knip, mandoc, rumdl and `ki repo audit` (FAIL=0) were all clean.
- cli150-deliver's temporary before-copies are removed. They were the six state files in `$TMPDIR/ki-agents/ways-of-working/cli150-deliver/before/`, outside tools-ki, and acceptance released them. That run's gate logs are still in the folder, so `ki agent close` will flag it until it is emptied.
- I reran CLI-150 Verify 6 before releasing, and it passed. I searched 24 `_common-*.md` and `*.queued.md` briefs under `~/.local/state/ki/agents/`, and none sends its own report into a work folder. The only work-folder report path is in `roadmap-next.queued.md`, which cites the ki-review run's report, and that is allowed.
- The tools-ki tree was clean of other sessions' changes before the release.
- ki v0.11.4 is released under tools-ki's release guide.
  - Harness pin moved to `00f284c3` in `330ce95b`, with the archive digest checked twice.
  - Release prepared in `116de313`.
  - Release gates all passed: coverage (1,350 tests), tsc, Biome, knip, mandoc, the command inventory, `ki repo audit` (FAIL=0), the build at 0.11.4, help, completion, diag, and a `--link` install into scratch folders.
  - Pushed to main, and CI passed. Tag `v0.11.4` pushed, and the Release workflow passed every job, including signing, the clean Linux install check and the tap notification.
  - The release is immutable. A fresh install from the published `install.sh` reports 0.11.4 and installs the manual.
- Homebrew tap: [PR 47](https://github.com/knowledgeislands/homebrew-tap/pull/47) "Advance ki to v0.11.4" passed its checks and merged automatically at 08:31 BST.
- ki-principal CI pin moved to v0.11.4 in `f772bbd`, committing `.github/ki-version` only, and pushed fast-forward. No one else's commits were stacked beneath it.
  - `git pull --rebase` refused because of other sessions' dirty files. A fresh fetch showed origin had not moved, so the push was still a clean fast-forward.
  - I left those dirty files alone: `+/_WORK/ki.chezmoi/decisions.md`, `apply-owned-drift.report.md` and `briefs/apply-owned-drift.md`; four `+/_WORK/ki.observatory/obs-*.report.md` files; and three files under `Pillars/Philosophy/Model/Processes/Acquisition Process/`.
- ki-principal CI is still red on `f772bbd`. It shows the same 10 failures as the previous commit `8123092`, so the pin did not cause them. They are BODY-11 and DEPENDS-4 in GDR records, BOUNDARY-1 in `ki.knowledge-acquisition/work.md`, and COORD-7 in ki.chezmoi reports, which CI-RED-REST already leaves with their owners.
- tools-ki CI failed once on biome-fix's `c2a9a062`, in the roadmap prune test (`ENOTEMPTY` while removing its temporary `.git/info`). It passed on the next push and locally, so it looks like a flaky cleanup race.
- Net records: 0 in tools-ki, 0 in ki-principal. My temporary folder is empty.

## In Progress

- Nothing.

## Queries

- None.
