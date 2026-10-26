# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › rig-lock-review

**🤖 → 🧑 Handoff to supervisor · Run report at 18:44 BST · last mark 18:43 BST**

---

## Done

- I reviewed [KI-TOOL-RIG-CORE-061 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/6ac358fb607629ca9f9ff32d1694afdec112737d/docs/roadmap/KI-TOOL-RIG-CORE-061-removal-lock-diagnostics.md) (commit `cacce0c`) independently and found it clean. Every acceptance criterion is met by the committed code. A held active, stale or unknown lock refuses `remove --apply` with exit 2, makes no provider call and leaves the lock in place. A confirmed removal holds the lock as `command=remove` and releases it on every outcome. Preview and `--dry-run` take no lock. A refused upgrade names `owner=remove`. Every doctor case behaves as the record specifies, and the new assertions are fatal. I have two notes, neither of which blocks: doctor does not check for a symlinked `operation/` or `reconciliation/` parent, which is harmless because doctor only reads; and an interrupted removal relies on the shared signal traps, with no test written for removal.
- I re-ran the local gate at `3a33d51` and it passed: `ki repo audit` (warnings only, HOOK-1 and SHELL-FATAL), ShellCheck, `bash -n`, the assemble check, the benchmark, the native-provider smoke, the mandoc lint and `git diff --check`. Bats ran 582 tests and all passed.
- Accepted under ACCEPT-AND-PRUNE in `6ac358f`, pushed: [KI-TOOL-RIG-CORE-052 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/7ba751395a9c5492ed7664fb60cccf56ef52e5d3/docs/roadmap/KI-TOOL-RIG-CORE-052-doctor-service-launch-prerequisites.md), 054, 055, 058 and 061. Each record's verification evidence was already recorded, and each provisional choice stands as RIG-LOCK-FOLLOWUP a) and RIG-LOCK-CHOICES a) say.
- Pruned in `24c28e9`, pushed: [KI-TOOL-RIG-CORE-058 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/6ac358fb607629ca9f9ff32d1694afdec112737d/docs/roadmap/KI-TOOL-RIG-CORE-058-apply-lock-handler-history.md) and [KI-TOOL-RIG-CORE-061 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/6ac358fb607629ca9f9ff32d1694afdec112737d/docs/roadmap/KI-TOOL-RIG-CORE-061-removal-lock-diagnostics.md).
- [KI-TOOL-RIG-CORE-052 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/7ba751395a9c5492ed7664fb60cccf56ef52e5d3/docs/roadmap/KI-TOOL-RIG-CORE-052-doctor-service-launch-prerequisites.md), [KI-TOOL-RIG-CORE-054 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/7ba751395a9c5492ed7664fb60cccf56ef52e5d3/docs/roadmap/KI-TOOL-RIG-CORE-054-command-line-tools-check.md) and [KI-TOOL-RIG-CORE-055 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/7ba751395a9c5492ed7664fb60cccf56ef52e5d3/docs/roadmap/KI-TOOL-RIG-CORE-055-interpreter-port-owner-matching.md) are kept as Done and not pruned. The chezmoi repository, which belongs to another work, still refers to them:
  - [setup-mac-rig.md](/Users/krisbrown/.local/share/chezmoi/docs/guides/user/setup-mac-rig.md) lines 177-179;
  - [KB-DOTFILES-UE-089 (pruned)](https://github.com/krisb/dotfiles/blob/2584fffb3a60f41fbe82e19be0ec5b27362ed410/docs/roadmap/KB-DOTFILES-UE-089-ki-tool-release-channels.md) lines 61 and 124.
- I committed and pushed the v0.7.0 release candidate in `f6160db`. It sets `RIG_VERSION=0.7.0`, reassembles `bin/rig`, and labels the README, getting-started guide, manual page and release guide as an unpublished candidate, with v0.6.3 still the latest release. Candidate checks:
  - Audit, ShellCheck, syntax, benchmark, smoke, mandoc and diff-check passed.
  - A disposable `install.sh --link` passed, as did an offline export.
  - Bats passed 580 of 582. The two failures, in `tests/rig-firewall.bats`, are a flaky regex: `pfctl (-d|.*-X)` matched a random temporary directory named `bats-run-X9wm9S`. They passed on re-run.
- The release was not cut: there is no tag, no GitHub release and no tap change. The branch CI for `f6160db` failed, so the release guide's first gate is not met; see RIG-CI-RED below.
- The Homebrew tap formula `rig.rb` is still at v0.6.3, as it should be, and nothing triggered it.
- I made no live Rig apply or upgrade on any machine, and I emptied the temporary directory.

Net record count in tools-rig: of the 7 records that were awaiting review, 2 remain. 5 are Done, 2 of which were pruned. The roadmap now holds 14 record files, down from 16.

## In Progress

- **Release v0.7.0 (RIG-LOCK-RELEASE a):** waiting for a green main CI. `main` carries the candidate commit, and its docs say the installer URLs are not available before publication.
- **[KI-TOOL-RIG-CORE-042 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/abb734b12bca7e5836254741564c3ac093192524/docs/roadmap/KI-TOOL-RIG-CORE-042-profile-filtered-dock-items.md) and [KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md):** left at awaiting review because live acceptance is still owed. 042 needs Sol; 047 needs Terra and Sol, including tailnet SSH and VNC, refusal on the LAN, behaviour across a restart, and NordVPN on Sol. Both can be checked with Kris once v0.7.0 is released and installed.
- **Installed Rig:** Terra and Sol both still run the old code, with no removal lock and no lock findings in doctor, until Kris upgrades them.
- **Messages to relay**, which I could not write because `+/_WORK/ki.chezmoi/work.md` has uncommitted changes from another session:
  - to ki.chezmoi: the 052, 054 and 055 references listed above;
  - to ki.mac-studio-setup: [work.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.mac-studio-setup/work.md) line 40 still lists 052, 054, 055 and 058 as future steps.
- **Observations:**
  - `3a33d51`, a capture commit from another session, also deleted [KI-TOOL-RIG-CORE-060 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/9752f6821938b67bc4177fa88b1c5bc529700dba/docs/roadmap/KI-TOOL-RIG-CORE-060-single-target-operation-speed.md), which breaks the rule that a prune commits on its own. It is already on origin, so I left it.
  - The queued accept-prune run also names the Rig lock follow-up, which is now done here.
- **Other sessions' uncommitted files in ki-principal, left alone:**
  - `+/_WORK/ki.chezmoi/decisions.md` and `+/_WORK/ki.chezmoi/work.md`;
  - `ki.knowledge-acquisition/stock-take.report.md`;
  - `ki.mac-studio-setup/rig-lane.report.md`;
  - `ki.observatory/work.md`;
  - `ki.tools-burndown/work.md`;
  - deleted `ki.ways-of-working/*.report.md` files.

## Queries

### RIG-CI-RED - Main CI has been red since 15 October

**Context:** The last green main run was `efd4eae` on 15 October; every main run since then has failed, including the one for `cacce0c`, so 061 did not cause this. Two jobs fail, and both pass locally:

- **Shell lint:** the runner's newer ShellCheck reports SC2015 (`A && B || C`) at `src/rig/10-configuration.bash` lines 999, 1000 and 2578, and at the matching lines in `bin/rig`. Locally, ShellCheck 0.11.0 is silent on these lines.
- **KI governance:** `ki-work-roadmap` ITEM-2 rejects `theme: rig` as retired in 14 records and asks for `project`, `initiative` or `component` instead. CI pins `KI_VERSION: v0.8.4`, while the local `ki` is 0.11.2.

**Query:** Should a fix record restore a green CI so that v0.7.0 can be tagged on top of it?

**Options:** a) (recommended, confidence high - both fixes are small but outside this brief, and reclassifying the records needs a choice of field) capture one tools-rig debt record that rewrites the three SC2015 lines as `if` statements, reclassifies the 14 records from `theme: rig` to the field you choose, and checks whether the `KI_VERSION` pin should move to the current release; build it, then rerun this release sequence from step 2. b) Waive the CI gate and tag v0.7.0 now, because Bats on Linux and macOS and mandoc pass. c) Revert the candidate commit and defer the release.

### RIG-VERSION - Version number for the release

**Context:** There are five `feat` commits since v0.6.3: the built-in `mas` provider, profile-filtered Dock items, the shared operation lock, doctor's new findings, and lock diagnostics for removal. Between 0.5.0 and 0.6.0, a change of that size moved the minor version.

**Query:** Is v0.7.0 the right number for this release?

**Options:** a) (recommended, confidence medium - this follows the earlier minor bump made for new features) keep v0.7.0. b) Use v0.6.4.

### RIG-FLAKY-FIREWALL - Flaky firewall assertion

**Context:** In `tests/rig-firewall.bats`, `assert_no_global_firewall` matches `pfctl (-d|.*-X)` against log lines that include a random temporary path, so about one run in a few hundred fails because a directory name contains `-X`.

**Query:** Should the fix be folded into [KI-TOOL-RIG-CORE-063 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/735a8e8560f951afeaa0194df52c5dffa26a3797/docs/roadmap/KI-TOOL-RIG-CORE-063-fatal-bats-assertions.md), the record for fatal Bats assertions?

**Options:** a) (recommended, confidence high - it is the same kind of test-hygiene debt and needs no new record) fold it into [KI-TOOL-RIG-CORE-063 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/735a8e8560f951afeaa0194df52c5dffa26a3797/docs/roadmap/KI-TOOL-RIG-CORE-063-fatal-bats-assertions.md). b) Add it to the RIG-CI-RED fix record.
