# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-day-rig-ci-fix

**🤖 → 👤 Handoff to supervisor · blocked · Run report at 15:20 BST · last mark 14:11 BST**

---

## Done

Green technical v0.8.0 dossier at `a2bc10939462e387b18dcdaedb54e886ac00386a`; tagging remains blocked on RIG-RELEASE-REVIEW-BOUNDARY. No tag, release, live apply, product-code change or work-record change was made.

Commit `a2bc10939462e387b18dcdaedb54e886ac00386a`, `fix(ci): pin the compatible governance harness`, changes only `.github/workflows/ci.yml`; hooks passed without bypass and the post-hook path inspection confirms that boundary. The co-author trailer names the runtime model, gpt-6.1-sol. [Committed-path evidence](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-ci-fix.work/evidence/committed-paths.txt).

RIG-RELEASE-CI-DIAGNOSIS resolved: read-only retrieval of the exact failed job attributed the failure to KI v0.12.0's bundled harness `f4d6c521ef4859dc8965579bc39a5575004e3ac5`, whose shell-hook rubric requires Bats in the commit hook. CI now seeds the reconciled harness `7dc5bb8aa8d8a0e0fce3a34084a90260033ba643` before bootstrap, matching the required offline audit and Rig's canonical hook contract. [Failed-job evidence](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-ci-fix.work/evidence/failed-audit-job.txt) and [Old rubric snapshot](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-ci-fix.work/evidence/old-rubric.ts) retain the attribution; no credential was printed, copied or changed.

Release range reconciled: all 69 commits from `v0.7.0` to the final candidate are covered by the predecessor's exact 66-commit review, separate review of the nine-path release preparation and KI pin, and this one-path repair. Every one of the nine new done transitions was independently matched to its acceptance commit and exact record snapshot. [Full fetched range](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-ci-fix.work/evidence/range-commits.txt), [Independent reconciliation](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-ci-fix.work/evidence/range-confirmation.json) and [Inherited full review](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/range-review.md) retain the evidence.

[KI-TOOL-RIG-DIST-012](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/KI-TOOL-RIG-DIST-012-green-main-ci.md): done snapshot and acceptance `ef5b0d4e3fa8349f94069ae52cacbcf49ef2a47d` independently matched to this release ancestry.

[KI-TOOL-RIG-CORE-042](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/KI-TOOL-RIG-CORE-042-profile-filtered-dock-items.md): done snapshot and acceptance `9478d6211b62d358dbc1909889b5d74ea7aa8e83` independently matched to this release ancestry.

[KI-TOOL-RIG-CORE-063](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/KI-TOOL-RIG-CORE-063-fatal-bats-assertions.md): done snapshot and acceptance `f8cb24f027f1b575dcd90ded4ee9b171f775b701` independently matched to this release ancestry.

[KI-TOOL-RIG-CLI-027](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/KI-TOOL-RIG-CLI-027-command-line-convention-departures.md): done snapshot and acceptance `4ca939fa230b3e9eb02d9a170491a544a51b3651` independently matched to this release ancestry.

[KI-TOOL-RIG-CORE-065](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/KI-TOOL-RIG-CORE-065-resource-subject-links.md): done snapshot and acceptance `4ca939fa230b3e9eb02d9a170491a544a51b3651` independently matched to this release ancestry.

[KI-TOOL-RIG-CORE-066](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/KI-TOOL-RIG-CORE-066-plan-managers-and-uv-prerequisite.md): done snapshot and acceptance `4ca939fa230b3e9eb02d9a170491a544a51b3651` independently matched to this release ancestry.

[KI-TOOL-RIG-CORE-048](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/KI-TOOL-RIG-CORE-048-signed-release-install-kind.md): done snapshot and acceptance `47845d714b652e118216056f5b3a740778988f56` independently matched to this release ancestry.

[KI-TOOL-RIG-CORE-067](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/KI-TOOL-RIG-CORE-067-package-managers-as-catalogue-tools.md): done snapshot and acceptance `3cc18f657a4a56d265b2ef1e6f756551a6172a01` independently matched to this release ancestry.

[KI-TOOL-RIG-CORE-056](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/KI-TOOL-RIG-CORE-056-menu-bar-order-persistence.md): done snapshot and acceptance `63d1ac92d4a19fc0b8b7bd980b0dc831858e5efb` independently matched to this release ancestry.

Version, [consolidated Pre-1.0 changelog](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/CHANGELOG.md), [v0.7.0-to-v0.8.0 migration guidance](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/guides/user/migrating-command-surface.md) and [public release notes](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-ci-fix.work/v0.8.0-notes.md) remain exactly as prepared at `d7b4250884be9ec3591b2f9a35719863cfb6fa04`; authored and assembled versions are `0.8.0`. No command is removed and no mandatory configuration or persisted-state rewrite is introduced. Compatibility notes cover duplicate status options, additive query fields, optional manager declarations and changed macOS firewall drift.

Offline full audit: PASS=17 WARN=3 FAIL=0, with four findings identical to the unchanged baseline. Accepted existing warnings are `.rumdl.toml` template drift, absent maturity, and missing size on [KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md) and [KI-TOOL-RIG-CORE-064](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-064-unmanaged-configuration-scan.md); those files are unchanged. Fresh copied home, both local Capital registrations and network denial followed the audit-home README. [Audit evidence](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-ci-fix.work/evidence/candidate-audit.log) and [Baseline comparison](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-ci-fix.work/evidence/warning-comparison.json).

ShellCheck: pass. [ShellCheck evidence](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-ci-fix.work/evidence/candidate-shellcheck.log).

Bash syntax: pass. [Syntax evidence](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-ci-fix.work/evidence/candidate-syntax.log).

Assembly drift: pass. [Assembly evidence](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-ci-fix.work/evidence/candidate-assembly.log).

Benchmark: pass. [Benchmark evidence](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-ci-fix.work/evidence/candidate-benchmark.log).

Bounded native-provider smoke: pass. [Smoke evidence](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-ci-fix.work/evidence/candidate-smoke.log).

Full Bats fixture suite: 645 passed, none skipped; its own fixture isolation followed RIG-056-GATE. [Bats evidence](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-ci-fix.work/evidence/candidate-bats.log).

Mandoc lint: pass. [Manual evidence](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-ci-fix.work/evidence/candidate-manual.log).

Diff check: pass. [Diff evidence](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-ci-fix.work/evidence/candidate-diff.log).

Workflow validation: actionlint and extracted governance-step Bash syntax pass offline. Disposable linked executable/manual installation, rendered manual inspection, Bash/Zsh completion syntax and private-data-free public export pass. The complete Bats suite includes the release-installer and staged-prerequisite fixtures. [Candidate proof](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-ci-fix.work/evidence/candidate-proof.log).

Exact-commit [CI run 39614579471](https://github.com/knowledgeislands/tools-rig/actions/runs/39614579471) finished successfully: KI governance, Shell lint, Bats on Linux, Bats on macOS and mandoc all passed. The exact SHA and terminal status were verified through public read-only HTML, without another GitHub API call. [Final CI observation](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-ci-fix.work/evidence/ci-current.json) and [individual platform-job results](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-ci-fix.work/evidence/ci-platforms.json). The tag/version job is intentionally absent from this branch run and must pass after Kris tags.

Conditional tag and publication commands for Kris, also retained in [the command file](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-ci-fix.work/kris-release-commands.sh); none was executed. Run the lines in order and stop on any failed prerequisite. If the tag run has not appeared yet, repeat its read-only listing before proceeding.

```sh
#!/bin/bash
set -euo pipefail

# Run only after RIG-RELEASE-REVIEW-BOUNDARY is resolved by Kris.
cd /Users/krisbrown/workspaces/knowledge-islands/tools-rig
git fetch -q origin
test -z "$(git status --porcelain)"
test "$(git rev-parse HEAD)" = a2bc10939462e387b18dcdaedb54e886ac00386a
test "$(git rev-parse origin/main)" = a2bc10939462e387b18dcdaedb54e886ac00386a
test "$(gh api repos/knowledgeislands/tools-rig/immutable-releases --jq .enabled)" = true
git tag -a v0.8.0 a2bc10939462e387b18dcdaedb54e886ac00386a -m 'Rig v0.8.0'
git push -q origin refs/tags/v0.8.0

# Identify the new tag run, then require its full success, including tag/version.
gh run list --repo knowledgeislands/tools-rig --workflow CI --branch v0.8.0 --commit a2bc10939462e387b18dcdaedb54e886ac00386a --event push --limit 1
rig_tag_run=$(gh run list --repo knowledgeislands/tools-rig --workflow CI --branch v0.8.0 --commit a2bc10939462e387b18dcdaedb54e886ac00386a --event push --limit 1 --json databaseId --jq '.[0].databaseId')
test -n "$rig_tag_run" && test "$rig_tag_run" != null
gh run watch "$rig_tag_run" --repo knowledgeislands/tools-rig --exit-status

gh release create v0.8.0 --repo knowledgeislands/tools-rig --verify-tag --title 'Rig v0.8.0' --notes-file /Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-ci-fix.work/v0.8.0-notes.md
```

## In Progress

Nothing running. The green candidate is with Kris through the Ways of working coordinator, blocked solely on the release-review boundary below.

Outstanding - no action requested now: GitHub release immutability and public installation endpoints were not queried in this run. The commands require immutability before publication; after publishing, Kris must verify the release is immutable and follow [Release Rig](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/guides/developer/releasing.md) for disposable exact-tag executable/manual installation, tap-owned formula checks and downstream completion. A dispatched event alone proves no downstream result.

Outstanding - no action requested now: the unpublished-candidate notice removal and return to a development version remain post-publication work. Rig's signed-release consumer capability does not add a signing or packaging workflow for publishing Rig itself.

Outstanding - no action requested now: the owned clean worktree and branch are retained at `/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-ci-fix.work/worktrees/tools-rig`, branch `run/wow-day-rig-ci-fix`, under the no-deletion rule. Evidence and the copied audit home are retained under `/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-ci-fix.work`; no temporary-output artefact needs homing.

## Queries

### RIG-RELEASE-REVIEW-BOUNDARY - settle eligibility before tagging

**Context:** Branch CI is green on `a2bc10939462e387b18dcdaedb54e886ac00386a`, but [KI-TOOL-RIG-CORE-053](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-053-macos-menu-bar-declarations.md) remains awaiting review, and [KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md) and [KI-TOOL-RIG-CORE-062](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-062-own-address-firewall-destination.md) remain in progress. The second-Mac discovery check is still outstanding; [KI-TOOL-RIG-CORE-068](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-068-replaced-pf-root-ruleset-bypass.md) retains the attended NordVPN investigation boundary. Acceptance of [KI-TOOL-RIG-CORE-056](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-release.work/evidence/KI-TOOL-RIG-CORE-056-menu-bar-order-persistence.md) covers the written persistence investigation, not menu-bar enforcement or live firewall convergence. The coordinator's blind review disagreed with the earlier release assessment; that decision remains with Kris. This dossier supplies technical evidence and does not accept the open records or authorise live work.

**Query:** Must v0.8.0 tagging wait for the owning work to dispose of those review gates, or may Kris tag with the open records and documented limits retained?

**Options:**

a) (recommended, confidence high - preserves independent acceptance while leaving the verified candidate intact) Keep tagging blocked until the owning work resolves the review gates or Kris explicitly approves a release exception.

b) Kris explicitly permits this green v0.8.0 candidate to proceed to tagging with the open records and documented limits retained; no acceptance or live-apply authority follows.

### 🤖 → 👤 Handoff to supervisor · blocked · since 15:20 BST

🤖 0 running · 👤 1 with you · ⛔ 1 blocked · 📥 0 to accept

- [with you] RIG-RELEASE-REVIEW-BOUNDARY · Kris via Ways of working coordinator · since 14:39 BST
- [blocked] v0.8.0 tag eligibility · Ways of working coordinator · since 15:20 BST
