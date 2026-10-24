# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-night-cli-156-d

**🤖 → 👤 Handoff to supervisor · Run report at 04:57 BST · last mark 01:40 BST**

---

## Done

[KI-TOOL-KI-CLI-156](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-156-ci-runs-local-gate.md) is awaiting review. Implementation `fcbaf5105eee4b6804a6e251781e454f2ff868d9` and review packet `a859371c6701f9c58b2930ceefdbb524019dd20e` were committed by explicit path, integrated fast-forward and pushed to tools-ki origin/main on sol.local. Post-hook inspection confirmed only the authorised workflow, shape guard and existing record; the second commit contains only the record.

The apparent missed gate was reproduced: the historical green source has 26 Biome warnings and 15 infos, and both local and native-audit commands exit zero. The actual current CI failure was the obsolete v0.11.3/Harness pin. The coordinator selected the compatible released-pin repair at 04:36 BST, leaving diagnostic policy unchanged. CI now uses v0.12.0, with one native audit and no repeated checks under CI-2.

The original [exact-head run](https://github.com/knowledgeislands/tools-ki/actions/runs/39538420966) and [build job](https://github.com/knowledgeislands/tools-ki/actions/runs/39538420966/job/119020343906) failed at baseline `d6e8f369fac456de387298cae060058471970705`. The five latest pre-repair runs all failed; their exact heads, workflows, jobs, logs and actual runtime evidence are saved in [the investigation evidence](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-night-cli-156-d.work/ci-evidence.json) and [preceding-job evidence](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-night-cli-156-d.work/recent-ci-evidence.json). Inspected original jobs used v0.11.3 and Harness `fdbb73d883db75a9f42a7aaa77a5b609dc3d38a9`.

The [implementation-head CI run](https://github.com/knowledgeislands/tools-ki/actions/runs/39540586660) and [build job](https://github.com/knowledgeislands/tools-ki/actions/runs/39540586660/job/119027163432) pass at `fcbaf5105eee4b6804a6e251781e454f2ff868d9`.

The [final-head CI run](https://github.com/knowledgeislands/tools-ki/actions/runs/39540918234) and [build job](https://github.com/knowledgeislands/tools-ki/actions/runs/39540918234/job/119028204835) pass at `a859371c6701f9c58b2930ceefdbb524019dd20e`. Installation, Audit and manual lint all succeed. Logs prove v0.12.0 and Harness `f4d6c521ef4859dc8965579bc39a5575004e3ac5`, archive digest `004d7fa408e63036558879ef101207b7f71b6567b3a35383da4a570d0e6e07f9`. This is final-head evidence; no candidate CI is pending. [Release-candidate evidence](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-night-cli-156-d.work/final-head-ci-proof.json).

Published-release and clean-Linux-install proof: PASS for the selected v0.12.0 release; no release or archive download was performed by this run.

Historical warning/info reproduction: PASS; the existing gate behaves as specified.

Intentional native failures: PASS; the disposable combined fixture fails BIO-1, TSC-1 and TEST-5 for the respective Biome, type and test defects. Its unused probe exports also fail Knip. [Proof](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-night-cli-156-d.work/negative-native-proof.json).

Tests: PASS using installed dependencies.

TypeScript: PASS.

Biome: PASS with one existing informational finding.

Coverage: PASS through the full native governance audit.

Manual lint: PASS; public grammar and manual source are unchanged.

Full repository audit: PASS, no failures; the chosen released-Harness baseline retains PKG-6, CI-1 and HOOK-4 warnings. Package and hook files are unchanged; CI-1 still describes the existing inline-pin location, with only the release value changed under the approved repair. Linux CI also retains TERR-3, ROUTE-1 and two ITEM-2 warnings from unavailable Capital/Project checkouts; their declarations and Project references are unchanged. The newer offline baseline Harness separately had existing CI-1 and MATURITY-1 warnings. No warning was suppressed and no duplicate-check exception invented.

Work adapter, roadmap, authoring and diff checks: PASS on the complete review packet.

Setup correction: initial local failures were this run's missing borrowed boundary dependencies, blocked loopback fixtures and copied-home memory/dependency-containment settings; all were corrected in disposable state before the passing gates. External IP traffic remained denied. No dependency install or real registry/runtime configuration change occurred.

Retirement: PASS; the own merged worktree and branch were removed, temporary fixtures were cleared, and tools-ki main is clean. [Retirement proof](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-night-cli-156-d.work/retirement.json). Source changes remain within the authorised three paths; no record was accepted, pruned or created.

Pending handoff: `ki-principal`, `sol.local`, `main`, `04c36675cc3045faf34244657072f61b7ec38328` - `docs(work): route CLI-156 diagnostic policy boundary`. This was the single authorised local Messages commit; the coordinator consumed the line and selected option b. This run made no Principal remote call, and the commit is not reachable from the locally observed origin/main.

## In Progress

Nothing running. Independent review and acceptance are for the coordinator's next designated run; this run has not accepted the work.

Outstanding - no action requested now: inherited audit warnings and the existing informational Biome finding remain recorded above. No diagnostic policy change, release, live apply, provider mutation or follow-up capture was made. All surviving proof is [beside this report](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-night-cli-156-d.work).

## Queries

No outstanding queries. CLI-156-POLICY was answered by the coordinator's 04:36 BST decision; the selected option b was delivered and verified.

### 🤖 → 👤 Handoff to supervisor · since 04:55 BST

👤 1 with you · 🅿️ 0 parked

- [awaiting review] [KI-TOOL-KI-CLI-156](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-156-ci-runs-local-gate.md) · ki.ways-of-working coordinator / independent reviewer · since 04:55 BST
- [committed] tools-ki main, pushed and exact-head CI passed · wow-night-cli-156-d · since 04:55 BST
- [unpushed] authorised local-only Messages commit · ki-principal/main on sol.local · since 04:32 BST
