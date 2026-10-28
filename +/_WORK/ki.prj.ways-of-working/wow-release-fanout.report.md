# [Model](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md>) › [Ways of working](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md>) › wow-release-fanout

**🤖 → 👤 Handoff to supervisor · blocked · Run report at 07:26 GMT · last mark 01:07 GMT**

---

## Done

- Established the current fan-out: signed GitHub release → bot-managed Homebrew formula → website catalogue; the tap's sole enrolled consumer is the website. Evidence: [Release workflow](</Users/krisbrown/workspaces/knowledge-islands/tools-ki/.github/workflows/release.yml:214>), [Tap intake](</Users/krisbrown/workspaces/knowledge-islands/homebrew-tap/.github/workflows/propose-tool-releases.yml:50>), [Consumer registry](</Users/krisbrown/workspaces/knowledge-islands/homebrew-tap/.github/tool-release-consumers.json:2>), [Website receiver](</Users/krisbrown/workspaces/knowledge-islands/apps-knowledgeislands.info/.github/workflows/update-tool-release.yml:32>).
- Confirmed recent tap updates were automatic: bot commits `45393a2` (v0.11.5), `a0aec08` (v0.12.0) and `f31b194` (v0.13.0). Evidence: local `homebrew-tap` history for `Formula/ki.rb`; [KI formula](</Users/krisbrown/workspaces/knowledge-islands/homebrew-tap/Formula/ki.rb:8>).
- Explained the website lag: its last pre-investigation CI change was `41a683c`, setting v0.8.4 on 7 October; catalogue automation cannot edit CI. Evidence: local file history, [Website CI](</Users/krisbrown/workspaces/knowledge-islands/apps-knowledgeislands.info/.github/workflows/ci.yml:12>), [Website receiver](</Users/krisbrown/workspaces/knowledge-islands/apps-knowledgeislands.info/.github/workflows/update-tool-release.yml:32>).
- Found a working exception to manual CI pins: the Harness receiver has bot pin-bump history, including `fcc0f383` for v0.13.0; this receiver was not rolled out to the website. Evidence: [Harness pin receiver](</Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/.github/workflows/update-ki-pin.yml:9>), [Harness pin](</Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/.github/ki-version:1>).
- Reconciled the parallel run: website CI now has a committed v0.13.0 pin (`7132ba1`); this investigation made no edits there. Evidence: [Website CI](</Users/krisbrown/workspaces/knowledge-islands/apps-knowledgeislands.info/.github/workflows/ci.yml:12>) and its local history.
- Local source and history checks completed; live GitHub release/run checks were not executed because the brief forbids all remote calls. No repository changes, commits, pushes, workflow triggers or settings changes were made.

## In Progress

Nothing is running in this investigation. The recent release-job failure/skip check awaits the narrow network decision below.

## Findings

### RELEASE-PATH - The App fans out distribution and website information

**Goal:** Answer Kris's 2026-10-25 question: “what does a tools-ki release update?”

**Scope:** Local release workflow, packaging script, package scripts, tap workflows/scripts and website receiver; live configuration excluded.

**As of:** 2026-10-25, 07:26 GMT; local checkouts and locally available Git history, without fetching.

The manually dispatched Release workflow validates an existing version tag, builds Linux x64 and macOS arm64/x64 archives, and publishes an immutable GitHub release containing the executable/manual archives, checksum manifest and signature. It also runs a clean Linux installation/bootstrap proof. Publication uses the workflow's GitHub token and the `release` environment's `KI_RELEASE_SIGNING_KEY` reference. Package scripts contain build/test tasks, with no registry-publication or repository-wide pin updater. Evidence: [Packaging](</Users/krisbrown/workspaces/knowledge-islands/tools-ki/release/package.sh:29>); `tools-ki/.github/workflows/release.yml:93`; `tools-ki/package.json:51`.

The separate tap-notification job uses `ki-tools-release-bot`, through `KI_TOOLS_RELEASE_BOT_APP_ID` and `KI_TOOLS_RELEASE_BOT_PRIVATE_KEY`, to mint a tap-scoped installation token. It runs after publication, independently of the clean-install job, and is skipped when the App ID variable is empty. The tap also polls daily at 06:17 UTC, so a missing dispatch need not prevent delivery. Its intake scans every formula, prepares newer immutable releases, opens formula PRs and requests squash auto-merge after required checks. Evidence: [Release workflow](</Users/krisbrown/workspaces/knowledge-islands/tools-ki/.github/workflows/release.yml:214>), [Tap intake](</Users/krisbrown/workspaces/knowledge-islands/homebrew-tap/.github/workflows/propose-tool-releases.yml:50>).

After formula validation and merge, tap CI sends release evidence to explicitly enrolled consumers. The registry contains only `knowledgeislands/apps-knowledgeislands.info`. Its receiver verifies release/tap evidence and changes only `apps/site/src/_data/projects.json5`: the advertised version and three versioned links. It requests CI-gated auto-merge. It does not bump consumer CI. Evidence: [Tap consumer notification](</Users/krisbrown/workspaces/knowledge-islands/homebrew-tap/.github/workflows/ci.yml:144>), [Consumer registry](</Users/krisbrown/workspaces/knowledge-islands/homebrew-tap/.github/tool-release-consumers.json:2>), [Website receiver](</Users/krisbrown/workspaces/knowledge-islands/apps-knowledgeislands.info/.github/workflows/update-tool-release.yml:32>), [Website auto-merge decision](</Users/krisbrown/workspaces/knowledge-islands/apps-knowledgeislands.info/docs/decisions/ODR-KI-WEBSITE-001-tool-release-updates-auto-merge.md:26>).

The App is documented with Contents write, Pull requests write and Metadata read; installation targets are the tap, website and Harness. Tool repositories hold the credential references to mint tap-scoped tokens, rather than being installation targets themselves. Only reference names and tracked documentation were inspected; no credential values were read. Evidence: [GitHub Apps convention](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Conventions/Admin Conventions/GitHub Apps.md:20>).

Queries raised: RELEASE-RUN-CHECK.

### DELIVERY-HISTORY - Recent releases reached the tap and website catalogue

**Goal:** Check whether the release automation Kris remembers actually delivered recent versions, requested on 2026-10-25.

**Scope:** Local tap formula history and website catalogue history; actual dispatch/run logs excluded.

**As of:** 2026-10-25, 07:26 GMT.

The tap's formula was advanced by `ki-tools-release-bot[bot]` to v0.11.5 on 19 October (`45393a2`, PR #49), v0.12.0 later that day (`a0aec08`, PR #50), and v0.13.0 on 22 October (`f31b194`, PR #51). The current formula has v0.13.0 URLs and checksums for all three platforms. The website bot's `5f964d1`, also on 22 October, advertised ki v0.13.0 and changed only the catalogue. Evidence: local history for [KI formula](</Users/krisbrown/workspaces/knowledge-islands/homebrew-tap/Formula/ki.rb:8>) and [Website catalogue](</Users/krisbrown/workspaces/knowledge-islands/apps-knowledgeislands.info/apps/site/src/_data/projects.json5>).

This proves downstream updates landed through automation in the available history. It cannot distinguish an immediate release dispatch from the tap's daily recovery poll, or establish whether an individual release job failed or was skipped.

Queries raised: RELEASE-RUN-CHECK.

### CI-PIN-GAP - Website CI was outside the pin-update rollout

**Goal:** Explain why the website still used ki v0.8.4, requested by Kris on 2026-10-25.

**Scope:** Committed website CI history, its receiver and the Harness pin receiver; concurrent pin edits observed without modification.

**As of:** 2026-10-25, 07:26 GMT.

Before the parallel run, `jobs.build.env.KI_VERSION` in `.github/workflows/ci.yml:12` was v0.8.4. Commit `41a683c` on 7 October advanced it from v0.8.3; the installer URL, installation and version assertion all use that variable. The 24 locally available CI-file commits inspected before the parallel update were authored as Kris Brown, with no release-bot pin bump. Some were agent-assisted; author names alone do not prove changes were typed manually. There was no website `update-ki-pin.yml` receiver. Evidence: [Website CI](</Users/krisbrown/workspaces/knowledge-islands/apps-knowledgeislands.info/.github/workflows/ci.yml:12>), local `git log` and `git show 41a683c` for that file.

The catalogue receiver explicitly rejects any changed path outside its registry. Therefore successful Homebrew/catalogue fan-out could coexist indefinitely with an unchanged CI pin. The approved receiver design moves the pin outside `.github/workflows/` into `.github/ki-version`, avoiding a grant of Workflows permission to the App. The Harness already has that receiver and bot commits `81eb109d`, `2f85c068` and `fcc0f383` updating its pin. It is absent from the tap's consumer registry, so its scheduled/manual path can update it independently. Evidence: [Website receiver](</Users/krisbrown/workspaces/knowledge-islands/apps-knowledgeislands.info/.github/workflows/update-tool-release.yml:32>), [CI receiver contract](</Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-engineering/references/standards-engineering.md:158>), [Harness pin receiver](</Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/.github/workflows/update-ki-pin.yml:9>), [Consumer registry](</Users/krisbrown/workspaces/knowledge-islands/homebrew-tap/.github/tool-release-consumers.json:2>), and local Harness pin-file history.

The website lag is explained by incomplete receiver rollout, not by evidence of a broken all-repository fan-out step. The concurrent wow-ci-pins run has now committed v0.13.0; that repairs the immediate pin but does not itself install an updater. Evidence: [Website CI](</Users/krisbrown/workspaces/knowledge-islands/apps-knowledgeislands.info/.github/workflows/ci.yml:12>); [Release Cascade](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Operations/Processes/Release Cascade.md:79>) describes the separate rollout.

Queries raised: none beyond the live verification limitation.

### HARNESS-COPIES - Release publication does not update installed machines

**Goal:** Identify whether a release updates Harness copies or any other installation, requested on 2026-10-25.

**Scope:** Release package, built-in Harness pin and documented bootstrap/update behaviour.

**As of:** 2026-10-25, 07:26 GMT.

Release archives contain only `ki` and `man/ki.1`; they do not contain or push Harness copies. Each CLI release instead embeds one Harness archive commit and digest. For example, v0.8.4 pins Harness commit `93b07fbd3fceb92b6c5b0a54f79d1d39cd16b68d`, while v0.13.0 pins `52779419f518f8e5ee53ca675c9c9ecc215da2d5`. A bootstrap/acquisition or refresh on the consuming machine is a separate operation; CI must first install the newer CLI to acquire its newer pin. Evidence: [Packaging](</Users/krisbrown/workspaces/knowledge-islands/tools-ki/release/package.sh:29>), [Built-in Harness pin](</Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/storage/registry.ts:23>), [Releasing guide](</Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/guides/developer/releasing.md:9>); the same registry file at the two local tags.

Publishing also does not pull repository checkouts, rebuild local executables, run `brew upgrade`, or update host provisioning pins. Those remain operator/consumer actions. Evidence: [Release Cascade](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Operations/Processes/Release Cascade.md:79>), sections “Kris's machines” and “Automatic, manual and approved”.

Queries raised: none.

### RELEASE-DESIGN - The intended wider automation is already written down

**Goal:** Find the written release fan-out design, requested on 2026-10-25.

**Scope:** tools-ki release guide, Harness standards/decision, principal process/convention and principal Decision Records.

**As of:** 2026-10-25, 07:26 GMT.

[Releasing guide](</Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/guides/developer/releasing.md:9>) describes the exact Harness pin and tap handoff. [Release-readiness policy](</Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-tools/references/standards-release-readiness.md:52>) gives standing authority for enrolled downstream updates, while requiring actual merge evidence rather than treating an event as delivery. [Release App operations](</Users/krisbrown/workspaces/knowledge-islands/homebrew-tap/docs/guides/maintainer/release-app-operations.md:7>) describes sender operation, replay and failure diagnosis. [Website auto-merge decision](</Users/krisbrown/workspaces/knowledge-islands/apps-knowledgeislands.info/docs/decisions/ODR-KI-WEBSITE-001-tool-release-updates-auto-merge.md:26>) records the website's catalogue-only acceptance boundary.

In ki-principal, [Release Cascade](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Operations/Processes/Release Cascade.md:79>) explicitly distinguishes the working tap/catalogue chain, the Harness receiver and manual inline CI pins elsewhere. It records approval on 9 October for receiver rollout across `knowledgeislands`, owned by the Harness, with settings changes reserved to Kris. [GitHub Apps convention](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Conventions/Admin Conventions/GitHub Apps.md:20>) documents the App and its scope. No dedicated principal Decision Record matching release cascade, fan-out, this App or this event was found; the principal design is in that process and convention, with the auto-merge exception in [Harness security decision](</Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/decisions/XDR-KI-HARNESS-001-dependabot-security-updates-without-auto-merge.md:25>).

A fresh all-repository automation decision is therefore not needed to establish intent. Implementation/enrolment and live delivery remain distinct from that approval.

Queries raised: RELEASE-RUN-CHECK.

## Queries

### RELEASE-RUN-CHECK - Permit the requested live release-job check?

**Context:** The brief asks for recent GitHub releases and runs, but its explicit rule says “No remote call of any kind”, including GitHub API calls. Consequently `gh release list`, `gh run list` and job inspection were not run. Local history proves downstream delivery, but cannot prove whether the last few release notifications failed, were skipped, or were recovered by polling. This restriction comes from the task brief, not a skill or approval rejection.

**Query:** May a follow-up make read-only GitHub calls to inspect the last few tools-ki releases and Release runs, plus their relevant tap/website delivery jobs?

**Options:**

a) (recommended, confidence high - completes the explicit live-verification request while preserving the read-only boundary) Allow only release/run metadata and job-log reads; no fetch, workflow trigger, setting, credential or repository mutation.

b) Keep the no-network rule and accept this local-evidence report, retaining recent release-job failures/skips as unverified.

### 🤖 → 👤 Handoff to supervisor · blocked · since 07:26 GMT

🤖 0 running · 👤 1 with you · ⛔ 1 blocked · 📥 0 to accept

- [blocked] Recent GitHub release-job verification awaits the network decision · Kris · since 07:26 GMT

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
