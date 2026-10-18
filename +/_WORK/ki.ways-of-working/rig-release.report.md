# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › rig-release

**🤖 → 👤 Handoff to supervisor · Run report at 19:38 BST · last mark 19:05 BST**

---

## Done

- Main CI is green again under the new fix record [KI-TOOL-RIG-DIST-012](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-DIST-012-green-main-ci.md), now awaiting review. No existing record fitted. Two causes were fixed. Three `A && B || continue` guards in `src/rig/10-configuration.bash` broke the runner's ShellCheck (SC2015), so they are now written as an `if` and a `case`. The CI `KI_VERSION` pin moved from v0.8.4 to v0.11.2, because the v0.8.4 harness failed `ITEM-2` on `theme` in all 14 records. Commits: `c7d87c6` reserved the number, `8d2d253` holds the fix and record, and `64b846e` adds the CI evidence.
- The flaky `assert_no_global_firewall` match is recorded unfixed in [KI-TOOL-RIG-CORE-063](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-063-fatal-bats-assertions.md), under Discussion, with a suggested anchored pattern (`b8f3813`).
- Rig v0.7.0 is released at `b8f3813`. The tag is annotated, and the GitHub release "Rig v0.7.0" is published and immutable. The return to `0.7.0+dev` with released labels is in `03609a9`.
- Homebrew tap: the notify workflow ran, and formula PR knowledgeislands/homebrew-tap#45 auto-merged as `11c4029`. `Formula/rig.rb` now points at the v0.7.0 tarball, and its sha256 matches the downloaded archive.
- Check: before each push, the full local gate passed, including the audit, ShellCheck, `bash -n`, the assembly check, benchmark, smoke test, mandoc and `git diff --check`. Bats ran 582 tests with 582 passing.
- Check: main CI for `b8f3813` (run 39153236499) and for `03609a9` (run 39154474136) passed every job.
- Check: tag CI for v0.7.0 (run 39153802624) passed, including "Release tag matches executable".
- Check: tap main CI on `11c4029` passed.
- Check: the immutable installer, run into disposable directories, reports `rig 0.7.0` and installs the manual page.
- Net records: tools-rig gains one record, DIST-012, and CORE-063 was amended. ki-principal gains no records, only this report.
- No live `rig apply` or upgrade was run on any machine, and nothing was published beyond the Rig release and its tap formula.

## In Progress

Nothing.

## Queries

### RIG-TAG-SIGN - v0.7.0 tag is annotated, not signed

**Context:** The brief asked for a signed tag. No Git signing key is configured here, and v0.6.3 and the other KI tool tags are annotated but unsigned, so I tagged v0.7.0 the same way. The tag cannot be re-signed without replacing it, and the release is immutable.

**Query:** Do you accept the annotated tag as matching the v0.6.3 practice?

**Options:** a) Accept it, and leave tag signing to a separate decision covering the whole estate. b) Set up a signing key and sign tags from v0.7.1 onward. c) Something else.

### RIG-DIST-012-ACCEPT - accept the green-main-CI record

**Context:** [KI-TOOL-RIG-DIST-012](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-DIST-012-green-main-ci.md) is delivered with green CI evidence and is awaiting review. RIG-CI-RED a) proposed reclassifying the 14 records' `theme`. Moving the pin made that unnecessary, so the records are unchanged.

**Query:** Will you accept KI-TOOL-RIG-DIST-012 as delivered?

**Options:** a) Accept it as it stands. b) Also reclassify the 14 records' `theme`. c) Something else.

### KI-PIN-ESTATE - other repositories still pin ki v0.8.4

**Context:** At least nine other KI repositories pin `KI_VERSION: v0.8.4` in CI. Any whose records carry `theme` will fail `ITEM-2` the way tools-rig did. That is outside this brief.

**Query:** Should a run move those pins to the current ki release?

**Options:** a) Brief one run to move every pin and confirm each repository's CI. b) Fix each repository when its CI goes red. c) Something else.

### RIG-UPGRADE-MACHINES - upgrade Terra and Sol to v0.7.0

**Context:** The tap now serves v0.7.0. No machine was upgraded. An installed Rig older than v0.7.0 takes no removal lock. Live acceptance for [KI-TOOL-RIG-CORE-042](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-042-profile-filtered-dock-items.md) and [KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md) waits on the upgrade.

**Query:** Will you run `brew upgrade rig` on Terra and Sol yourself, then the CORE-042 and CORE-047 live acceptance?

**Options:** a) You upgrade both machines, then brief a run for the live acceptance. b) Hold the upgrade. c) Something else.
