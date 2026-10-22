# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-day-rig-release

**🤖 → 👤 Handoff to supervisor · blocked · Run report at 14:39 BST · last mark 14:11 BST**

---

## Done

Incomplete release dossier: the v0.8.0 preparation is committed and pushed, with all local gates passing, but required branch CI failed on an unchanged baseline prerequisite. There is no commit ready for Kris to tag yet.

Preparation commit: `d7b4250884be9ec3591b2f9a35719863cfb6fa04`, `chore(release): prepare v0.8.0 candidate`, on local and origin `main` in tools-rig on `sol.local`. Only this run's one commit was pushed, fast-forward; the owner's earlier pruning commit was already on origin. Hooks remained enabled, the model trailer names gpt-6.1-sol, and the post-hook [committed-path inspection](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/committed-paths.txt) confirms only the nine intended paths.

The [complete range review](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/range-review.md) covers all 66 existing commits from v0.7.0 through baseline `eccef96d8d51d2f9f922c759e43355523da17607`, including every changed path; the nine-path preparation was then reviewed separately. [Compatibility conclusions](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/review-conclusions.md) distinguish added capabilities, script compatibility changes, migration and outstanding acceptance boundaries.

All nine acceptance transitions in that range were checked against the committed terminal records; the links below retain their acceptance snapshots because the records were subsequently pruned:

- [KI-TOOL-RIG-DIST-012](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/KI-TOOL-RIG-DIST-012-green-main-ci.md): terminal acceptance confirmed at `ef5b0d4e3fa8349f94069ae52cacbcf49ef2a47d`.
- [KI-TOOL-RIG-CORE-042](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/KI-TOOL-RIG-CORE-042-profile-filtered-dock-items.md): terminal acceptance confirmed at `9478d6211b62d358dbc1909889b5d74ea7aa8e83`.
- [KI-TOOL-RIG-CORE-063](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/KI-TOOL-RIG-CORE-063-fatal-bats-assertions.md): terminal acceptance confirmed at `f8cb24f027f1b575dcd90ded4ee9b171f775b701`.
- [KI-TOOL-RIG-CLI-027](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/KI-TOOL-RIG-CLI-027-command-line-convention-departures.md): terminal acceptance confirmed at `4ca939fa230b3e9eb02d9a170491a544a51b3651`.
- [KI-TOOL-RIG-CORE-065](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/KI-TOOL-RIG-CORE-065-resource-subject-links.md): terminal acceptance confirmed at `4ca939fa230b3e9eb02d9a170491a544a51b3651`.
- [KI-TOOL-RIG-CORE-066](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/KI-TOOL-RIG-CORE-066-plan-managers-and-uv-prerequisite.md): terminal acceptance confirmed at `4ca939fa230b3e9eb02d9a170491a544a51b3651`.
- [KI-TOOL-RIG-CORE-048](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/KI-TOOL-RIG-CORE-048-signed-release-install-kind.md): terminal acceptance confirmed at `47845d714b652e118216056f5b3a740778988f56`.
- [KI-TOOL-RIG-CORE-067](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/KI-TOOL-RIG-CORE-067-package-managers-as-catalogue-tools.md): terminal acceptance confirmed at `3cc18f657a4a56d265b2ef1e6f756551a6172a01`.
- [KI-TOOL-RIG-CORE-056](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/KI-TOOL-RIG-CORE-056-menu-bar-order-persistence.md): terminal acceptance confirmed at `63d1ac92d4a19fc0b8b7bd980b0dc831858e5efb`.

[KI-TOOL-RIG-CORE-052](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/KI-TOOL-RIG-CORE-052-doctor-service-launch-prerequisites.md), [KI-TOOL-RIG-CORE-054](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/KI-TOOL-RIG-CORE-054-command-line-tools-check.md) and [KI-TOOL-RIG-CORE-055](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/KI-TOOL-RIG-CORE-055-interpreter-port-owner-matching.md) were already done at v0.7.0; their terminal states were separately confirmed before their pruning commits. Acceptance evidence does not grant live host convergence.

The authored and assembled versions are 0.8.0. The [consolidated Pre-1.0 changelog](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/CHANGELOG.md) was updated without adding a dated 0.x entry; [migration notes](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/guides/user/migrating-command-surface.md) cover the full range. [Reviewed public release notes](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/v0.8.0-notes.md) are prepared for eventual publication. README, getting-started, manual and release guide identify v0.8.0 as unpublished, retain v0.7.0 as the latest published release, and pin candidate installer examples exactly.

The [local gate exit ledger](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/candidate-results.txt) records the complete gate outcomes.

- Whole-repository audit: passed offline in this run's fresh copied audit home after target and both Capital registrations; four unchanged baseline warnings, no failures ([baseline](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/baseline-audit.log); [candidate](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/candidate-audit.log)).
- Baseline warnings: authoring template drift and missing maturity, plus missing size on [KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md) and [KI-TOOL-RIG-CORE-064](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-064-unmanaged-configuration-scan.md); all four affected files remain unchanged.
- ShellCheck: passed ([evidence](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/candidate-shellcheck.log)).
- Bash 3.2 syntax: passed for the complete documented script list ([evidence](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/candidate-syntax.log)).
- Deterministic assembly drift: passed ([evidence](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/candidate-assembly.log)).
- Benchmark: passed the repository's normal portability budget ([evidence](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/candidate-benchmark.log)).
- Native-provider smoke: all six bounded version probes passed offline ([evidence](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/candidate-smoke.log)).
- Complete Bats suite: all 645 fixtures passed, without skips, in Rig's fixture isolation ([evidence](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/candidate-bats.log)); this includes staged prerequisites, installer fixtures, command inventory and public-export boundaries.
- Mandoc lint: passed ([evidence](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/candidate-manual.log)); the [rendered installation section](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/candidate-manual-rendered.txt) was inspected.
- Diff whitespace gate: passed ([evidence](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/candidate-diff.log)).
- Disposable linked executable and manual, manual resolution, Bash/Zsh completion syntax and an offline public export excluding a private sentinel: passed ([evidence](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/candidate-proof.log)).
- Existing release-surface fixtures: passed after the version and unpublished-candidate assertions were updated ([evidence](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/candidate-release-focus.log)).
- Baseline isolation correction: an extra network sandbox denied the process inspection needed by 17 attended-operation fixtures; all 33 affected fixtures then passed in the required isolation, followed by the successful complete candidate run ([corrected baseline proof](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/baseline-fixture-isolation.log)).

Exact-commit [CI run 39608543523](https://github.com/knowledgeislands/tools-rig/actions/runs/39608543523) finished with failure on `d7b4250884be9ec3591b2f9a35719863cfb6fa04`; observation continued until every job finished. Its outcomes:

- CI [Bats (macos-latest)](https://github.com/knowledgeislands/tools-rig/actions/runs/39608543523/job/119251025364): success.
- CI [mandoc](https://github.com/knowledgeislands/tools-rig/actions/runs/39608543523/job/119251025905): success.
- CI [Bats (ubuntu-latest)](https://github.com/knowledgeislands/tools-rig/actions/runs/39608543523/job/119251026007): success.
- CI [KI governance](https://github.com/knowledgeislands/tools-rig/actions/runs/39608543523/job/119251026040): failure.
- CI [Shell lint](https://github.com/knowledgeislands/tools-rig/actions/runs/39608543523/job/119251026306): success.
- CI [Release tag matches executable](https://github.com/knowledgeislands/tools-rig/actions/runs/39608543523/job/119255313145): skipped.

The governance failure is attributable to the unchanged KI v0.11.3 pin: its old contract requires the retired Bats hook check, rejects current size/priority fields and warns about assembly metadata. The hook, workflow, metadata and all failing record inputs are byte-identical to the baseline ([attribution](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/ci-attribution.json); [job log](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/ci-governance.log)). This preparation introduced none of those findings.

A [prepared one-line pin patch](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/proposed-ci-pin.patch) to KI v0.12.0 is prepared but unapplied. The local v0.12.0 tag, using matching already installed dependencies, passed the complete copied-home audit offline with the same four baseline warnings ([offline v0.12.0 audit](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/proposed-ki-v0.12.0-audit.log)). This proves local compatibility, not a green replacement CI run.

## In Progress

Nothing is running.

Outstanding - no action requested now: the selected tag is `v0.8.0`, but exact tag and publish commands are left undone under the failed-CI prerequisite. A pin repair creates a new commit, so naming this failed SHA in a tag command would be invalid. A replacement dossier must supply the new exact SHA and commands after green branch CI, under [Release Rig](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/guides/developer/releasing.md).

Outstanding - no action requested now: publication remains Kris's stage, including annotated tag CI, repository release immutability, public distribution checks, the exact notes file above, the immutable installer check, and downstream tap/website evidence. No distribution-setting or public-channel network check was authorised here. The post-publication +dev change and notice removal remain separate later work.

Outstanding - no action requested now: the clean, merged worktree and branch `run/wow-day-rig-release` are retained under the task's no-deletion rule at `/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/worktrees/tools-rig`. Evidence and copied audit/fixture material are retained beneath `/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work`; the run's temporary output directory is empty. There are no unpushed repository commits from this run.

## Queries

### RIG-RELEASE-CI-PIN - restore the required CI governance prerequisite

**Context**: all local gates pass, but the exact pushed candidate fails required governance CI because its pre-existing KI v0.11.3 pin understands older contracts. Every failing input is unchanged by this preparation. The dispatch's skip-and-continue rule leaves the failed green-CI prerequisite for a query; the concrete [prepared one-line pin patch](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/proposed-ci-pin.patch) and [offline v0.12.0 audit](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/proposed-ki-v0.12.0-audit.log) are ready for review.

**Query**: should a bounded follow-up apply the prepared KI v0.12.0 pin repair, verify and push its own commit, observe full CI and return a replacement exact-SHA release dossier?

**Options**

a) (recommended, confidence high - the one-line repair addresses the demonstrated version mismatch and the released-tag source passes the complete isolated audit) Apply the prepared patch in a separately designated writing run, complete its gates and exact-commit CI, then provide the new tag and publish commands. Keep product code and work records unchanged.

b) Hold v0.8.0 preparation at the pushed commit and leave the CI pin unchanged; keep tagging and publication blocked.

### RIG-RELEASE-REVIEW-BOUNDARY - settle the open implementation reviews before tagging

**Context**: the full range also contains [KI-TOOL-RIG-CORE-053](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-053-macos-menu-bar-declarations.md), still awaiting review, and [KI-TOOL-RIG-CORE-062](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-062-own-address-firewall-destination.md), still in progress after refused acceptance. The related [KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md) retains attended acceptance gaps. The accepted [KI-TOOL-RIG-CORE-056](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/KI-TOOL-RIG-CORE-056-menu-bar-order-persistence.md) is a written investigation only and explicitly does not accept the menu-bar implementation. The task forbids this run from accepting records or performing live checks; version selection does not settle their release eligibility.

**Query**: should tagging wait for the owning work to dispose of these open review gates, or may v0.8.0 proceed after green CI with those records and their documented limits retained?

**Options**

a) (recommended, confidence high - it preserves independent acceptance and keeps the release decision distinct from fixture verification) Hold tagging while the owning work settles the implementation review gates; keep attended host checks and rollout under separate authority, then confirm the release boundary explicitly.

b) Explicitly authorise v0.8.0 after green CI with the open records and documented limits retained; do not treat release approval as record acceptance or authority for live convergence.

### 🤖 → 👤 Handoff to supervisor · blocked · since 14:39 BST

🤖 0 running · 👤 2 with you · ⛔ 1 blocked · 📥 0 to accept

- [with you] RIG-RELEASE-CI-PIN · Ways of working coordinator · since 14:39 BST
- [with you] RIG-RELEASE-REVIEW-BOUNDARY · Ways of working coordinator · since 14:39 BST
- [blocked] A green exact-SHA v0.8.0 dossier · Ways of working coordinator · since 14:39 BST
