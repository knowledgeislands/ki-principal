# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-tidy

**🤖 → 👤 Handoff to supervisor · blocked · Run report at 01:47 GMT · last mark 01:31 GMT**

---

## Done

- Tidied the package in `23a97820` (`docs(work): ki.prj.ways-of-working tidy at window start`). It removed 45 tracked reports under `reports/` and 42 briefs with `git rm` by explicit path, plus 42 untracked report copies with `rm` on literal paths. The commit hook and the scoped repository audit passed. The commit is published fast-forward.
- To count as deletable, a report had to meet three tests. First, its run is named in the package's decisions, state or queries history, or a receive run says it received it. Second, every query tag in its Queries section is in `queries.md` or `decisions.md`, either now or in the package's Git history. Third, every query carries a tag. Reports that failed any test were kept. A brief was deleted only when its run had finished and its report had been received.
- The three protected files are untouched: `public-report-review.report.md`, `sol-private-report-assessment.report.md` and `reports/z-session-retirement-20261030.md`. Design notes are untouched, and nothing was moved into a new layout.
- Closing `ways-of-working-reg` and `ways-sol-resume-20261029` failed. See CLOSE-BLOCKED.

Deletions and homes:

| Deleted | Home |
| --- | --- |
| `blind-review-1` to `-6` reports, briefs and `.packet.md` files | Blind-review lines in `queries.md` (WORKER-WAIT\*, HOST-\*, ORCH-NAME, WAKE-HOST, LAYOUT-\*, ORCA-\*); no review pending |
| `fold-review-4` to `-6` reports and briefs | Folds committed into `queries.md` (e.g. `7c794992`) |
| `host-sync-review`, `-review-claude`, `-review-codex`, `-merge` reports and briefs | `design/host-sync/` brief, both reviews and the merged report (`e36f…`, `76beec53`, `10fac552`) |
| `landscape`, `landscape-merge`, `landscape-revise` reports; those three plus `landscape-review-codex` briefs | `design/landscape*.md`; queries copied by `receive-landscape` (`55017cc1`) |
| `mask-queries`, `-2`, `-3`, `-6` reports and briefs | The packets they wrote, now folded (e.g. `c3003803`) |
| `op-cache-apply`, `op-cache-rule` reports and briefs | The cached-reader rule in the ki-delegation standard; decisions log entry of 30 October, 16:18 GMT |
| `orca-cleanup`, `orca-subagents` reports and briefs | `design/orca-subagents/design.md`; ORCA-\* queries (`b359d5c2`) |
| `orch-name-fresh`, `orch-name-update` reports and briefs | ORCH-NAME in `queries.md` (`94e25ae1`) |
| `package-layout` report and brief | `design/package-layout/design.md`; LAYOUT-\* queries (`aafba011`) |
| `receive-landscape`, `-layout`, `-more`, `-orca`, `-sol` reports (root and `reports/` copies) and briefs | Their receive commits `55017cc1`, `aafba011`, `2129e5f9`, `b359d5c2`, `41c5a0b9` |
| `send-env-leak` report and brief | ORCA-ENV-LEAK line in `ki.prj.tools-burndown` `messages.md` |
| `sol-estate-origin-preflight`, `sol-reconcile-hnr`, `sol-reconcile-legal`, `wow-freshness-reminder-blind-20261029`, `wow-mark-followthrough` reports | Homes verified by `receive-more`: the decisions log entry of 2026-10-29T23:43:09Z, the HNR and Legal repair commits, `design/package-definition-freshness-report.md` and `25f5926b` |
| `sol-finish-line-plan`, `sol-host-sync-design`, `sol-state-machine-readiness` reports; `wow-finish-line`, `wow-host-sync-design` briefs | `design/finish-line-plan.md`, `design/host-sync-report.md`, `design/state-machine-rollout-plan.md` and their queries (`41c5a0b9`) |
| 44 tracked `reports/` files: `accept-prune`, `agentspecs-scan`, `banner-on-state`, `burn-observatory`, `checkout-iso`, `ci-review`, `cli-conventions`, `delete-review`, `design-triage`, `gfm-convert`, `gfm-scope`, `green-main`, `harness-link-fix`, `harness-moves`, `ki-release`, `lane-triage`, `mgit-learn`, `no-alias-sweep`, `principal-audit`, `query-review`, `query-review-4`, `reinstall-check`, `report-sweep`, `restart-consolidate`, `spec-drafts`, `stash-review`, `take-stock`, `territory-rename`, `work-package-design`, `worktree-flow`, `wow-drain-tidy`, `wow-dryrun-survey`, `wow-fleet-green`, `wow-hnr-tidy`, `wow-mod011-approved-candidate`, `wow-model-shape`, `wow-night-audit-home-registries`, `wow-principal-records`, `wow-sol-clone-2`, `wow-sort-roadmap`, `wow-state-machine`, `wow-sync-terra`, `wow-take-stock`, `wow-tidy-night` | Each run is named in the package's decisions, state or queries history. Each queries is in `queries.md` or `decisions.md` now or in the package's Git history, back to `+/_THREADS/ways-of-working/` and `+/_CHECKPOINTS/` |

Kept, failing a test:

- **Not yet received:** `embargo`, `embargo-correct`, `survey`, `website-learn`, `lessons-apply` and `sync-all` reports, with their briefs.
- **Queries never copied:** `landscape-review-claude`, `landscape-rollout`, `mask-queries-4`, `mask-queries-5` and `worker-wait-split`, with their briefs.
- **Queries never copied, untagged queries, or no receipt evidence:** 54 tracked `reports/` files and the untracked `reports/hold-request-20261030-z.md`, the same set earlier tidies kept, plus `landscape-review-codex`.
- **Brief with an unclear run:** `briefs/orca-fit.md`. No run record was found; the landscape study succeeded it.
- **Briefs still in use:** `briefs/public-report-review.md` (its report is protected) and `briefs/wow-tidy.md` (this run).

## In Progress

Nothing is running from this run. Close side effect: `ki agent close ways-sol-resume-20261029` moved `sol-finish-line-plan`, `sol-host-sync-design` and `sol-state-machine-readiness` reports from that run's state folder back into the package root, after I had deleted the package copies. Those files are now the only copies. They were never tracked, so I left them in place rather than lose them; see CLOSE-BLOCKED.

## Queries

### CLOSE-BLOCKED - The two stale runs cannot close

**Context:** `ki agent close` refuses both runs for two reasons. First, the package folder has untracked files, which are the reports kept above and newly finished run reports. Second, decisions in `decisions.md` have no recorded home: 13 named for `ways-of-working-reg` (DIAGRAM-AGREED, MOVE-PROMPT-SHAPE, STOP-FOR-MOVE-WOW, ORCA-FIT, LANDSCAPE, ORCA-SUBAGENTS, AWAY-31-OCT and the dated receive entries) and 72 for `ways-sol-resume-20261029`. Homing each decision through `ki agent reconcile` is a judgement on live decisions, outside a tidy. `--reconciled` would waive the check, but nothing authorises a waiver. A side effect remains: three sol reports now sit untracked in the package root as their only copies.

**Query:** How should the two stale runs be closed?

**Options:**

a) (recommended, confidence medium - the decision homes need the steward's judgement, and committing the three sol reports keeps them safe in Git) Have the coordinator receive the new reports and commit the three returned sol reports into `reports/`. Then run one bounded reconcile pass that records each decision's home or class with `ki agent reconcile`, and retry both closes.

b) Close both with `--reconciled` under an explicit owner waiver. The close note records the waiver, and the decision-home check is left to the next mark.

### 🤖 → 👤 Handoff to supervisor · blocked · since 01:47 GMT

👤 1 with you · ⛔ 1 blocked

- [blocked] close ways-of-working-reg and ways-sol-resume-20261029 · owner · since 01:46

🧵 ki.prj.ways-of-working
