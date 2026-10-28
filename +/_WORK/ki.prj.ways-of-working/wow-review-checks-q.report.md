# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-review-checks-q

**🤖 → 👤 Handoff to supervisor · Run report at 22:19 GMT · last mark 01:07 GMT**

---

## Done

Independent read-only review completed on 26 October 2026. No repository changes or commits; no hooks, audits, conform, repair, fix or remote operations run. No queries.md, decisions.md or existing report files read. Synthetic Markdown was checked through stdin without caching or fixing.

### COMMIT-VS-CI

**Pick:** Third option, with one correction: move audits to CI and make staged lints check-only, but preserve necessary isolated runtime setup rather than deleting `ki repo repair` solely because its name suggests content repair.

**Confidence:** High.

**Reason:** Commit checks should give fast feedback without rewriting work; CI should audit committed source, with runtime provisioning clearly separated from source conformance.

**Verified:** All 16 canonical pre-commit assets have an early empty-index exit and a focused staged audit, without an explicit ki-authoring audit or conform command. Package hooks invoke lint-staged and syncpack; the installed principal package configuration rewrites Markdown and code. The standard itself already says hooks are check-only while also requiring the focused audit, so the change must reconcile policy, assets and lint-staged configuration. See [hook composition](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/keystone/ki-repo/references/standards-repository.md:139), [canonical asset](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-kb/assets/githooks/package/pre-commit:1), and [installed lint-staged configuration](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/package.json).

**Verified:** The tools-ki conform host obtains canonical bytes from the resolved ki-repo provider and applies hook conversion. The staged audit still gathers and evaluates whole-tree evidence before filtering the verdict; staged scope therefore does not guarantee staged-only cost. See [hook writer](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/repository/operations/conform.ts:95), [provider boundary](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/repository/canonical-hooks.ts:9), and [audit evaluation](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/repository/operations/audit.ts:65).

**Refuted or qualified:** The inference that CI repairs governed source before auditing is unsupported by current repair source. It registers the checkout and reconciles managed skill projections; it does not run conform or fix Markdown. Removing it without replacing required activation can break CI. The installed principal workflow runs repair during isolated setup, then an unfiltered audit. Source conformance should be checked without source rewrites, but a passing audit also remains limited to its mechanical criteria. See [repair implementation](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/commands/repo/repair.ts:35) and [CI setup and audit](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/.github/workflows/ci.yml:45).

**Not reproduced:** The current local scan found 74 Git roots, 66 with .ki.toml, and 22 of those with ci.yml; all 22 include repair. The stated 23/51 needs its inventory boundary or earlier snapshot. I found no separate tracked ci.yml asset in the harness, only its installed workflow, so the proposed asset destination needs identifying. The timing figures were not rerun. Canonical hooks exit before tools on an empty index; any observed slow empty-index path needs attribution to a legacy hook or direct audit. “Never checked locally” is too broad: full local authoring audits remain available, although the canonical automatic hook omits that audit.

### LINT-WHERE

**Pick:** Third option: generator check-only validation with receiving-repository configuration, backed by check-only staged hooks and whole-tree CI.

**Confidence:** High.

**Reason:** Validate generated output before it enters the receiving work package, while retaining checks for coordinator-authored files and later edits.

**Verified:** The current normal report-copy operation reads the state report and writes the work-folder copy without a lint check. It lives in events.ts, reached through run event derivation, rather than directly in the runs.ts copy step named in the proposal. Legacy adoption also copies reports without linting. See [normal report homing](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:698), [run integration](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:849), and [legacy adoption](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/thread.ts:166).

**Verified:** A synthetic query with adjacent lettered options fails MD013 under each of the three receiving configurations. Check-only diagnostics propose joining the options into one paragraph; no fix was executed. Resolve that form/configuration conflict before enforcing generator rejection. See [principal configuration](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/.rumdl.toml:44), [HNR configuration](/Users/krisbrown/workspaces/humans-not-robots/hnr-principal/.rumdl.toml:43), and [legal configuration](/Users/krisbrown/workspaces/legal/legal-principal/.rumdl.toml:38).

**Refuted or qualified:** Not every installed hook fixes staged Markdown: HNR principal and legal principal currently invoke their shape audit without rumdl or lint-staged. MD-mech can also run locally, not only in CI. The generator proposal covers copied reports, not every package file the coordinator writes. See [HNR hook](/Users/krisbrown/workspaces/humans-not-robots/hnr-principal/.githooks/pre-commit:20), [legal hook](/Users/krisbrown/workspaces/legal/legal-principal/.githooks/pre-commit:20), and [MD-mech](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-authoring/scripts/rubric/items/markdown.ts:29).

**Unverified:** The 85/94 and 15/57 failure attribution, and the universal assertion about every well-formed report, cannot be established without reading excluded reports. The synthetic check establishes the adjacent-option conflict, not those fleet counts.

### BASELINE-COMMITS

**Pick:** Second option: explicit-path staging applies to baselines too; investigate commit provenance separately without delaying enforcement of the existing rule.

**Confidence:** High.

**Reason:** A baseline label cannot authorise collecting another thread's work, and a lint pass cannot establish ownership or completeness.

**Verified:** Principal has 15 matching baseline commits in the stated date window. The current broader HEAD-history scan finds matching commits in 44 other repositories; this does not establish which belonged to the named rollout. On 24 October, principal's e78fff6 added 414 report paths, 5c2f74b added 30, and 54e3010 added seven. These are filename/history checks only, not a review of report contents or their lint results.

**Refuted or qualified:** The present immutable-baseline step records the existing full HEAD identifier; it does not instruct the agent to create a baseline commit. ki-git already requires fully enumerated touched paths and forbids whole-tree staging in shared checkouts, without a baseline exception. Clarification may help, but the ownership rule does not depend on first identifying the producer. See [baseline step](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-implement/references/standards-implementation.md:20) and [explicit staging rule](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-git/references/standards-git.md:114).

**Unverified:** Neither the 81 failing-report subset nor the command that produced those commits was established. Git history alone does not prove the staging command, hook execution, or attribution to ki-implement, ki-batch or a person. No session logs or excluded report bodies were inspected.

## In Progress

Nothing.

## Queries

None.

### 🤖 → 👤 Handoff to supervisor · since 22:19 GMT

✅ 3 queries reviewed · ❓ 0 outstanding

- [reviewed] Three recommendations and their evidence limits · supervisor · since 22:19 GMT

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
