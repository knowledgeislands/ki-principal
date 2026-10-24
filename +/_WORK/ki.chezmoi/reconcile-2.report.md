# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › reconcile-2

**🤖 → 👤 Handoff to supervisor · Run report at 14:21 BST · last mark 01:42 BST**

---

## Done

Reconciled sol on 21 October 2026 under the supplied reconciliation authority. All 18 authorised origin fetches succeeded; no checkout qualified for a fast-forward, and this run changed no repository HEAD or managed target. The final checkout snapshot below was taken at 14:20:15 BST.

### Checkouts

All checkouts are on `main`, tracking `origin/main`. Ahead/behind uses the locally recorded upstream after fetching. `FF: no` means no merge was needed or permitted. No locks were present before or after the Git operations.

Paths: `chezmoi` is `/Users/krisbrown/.local/share/chezmoi`; the tools, KI and MCP repositories are under `/Users/krisbrown/workspaces/knowledge-islands`; the site is `/Users/krisbrown/workspaces/personal/apps-rig.midnight.ninja`.

| Repository | Fetched | FF | Ahead/behind | Dirty | Locks | HEAD |
| --- | --- | --- | --- | --- | --- | --- |
| chezmoi | yes | no | 0/0 | clean | 0 | `a341460e` |
| tools-ki | yes | no | 0/0 | clean | 0 | `0f8b15de` |
| tools-techne | yes | no | 0/0 | clean | 0 | `3e686b66` |
| tools-git-almanac | yes | no | 0/0 | clean | 0 | `8851d4dc` |
| tools-mgit | yes | no | 0/0 | clean | 0 | `78a1b376` |
| tools-rig | yes | no | 0/0 | clean | 0 | `eccef96d` |
| ki-principal | yes | no | 72/0 | 19 untracked† | 0 | `21ad8b4e` |
| ki-agentic-harness | yes | no | 0/0 | clean | 0 | `d60b7b93` |
| ki-design | yes | no | 0/0 | clean | 0 | `38965f00` |
| mcp-acquire-whatsapp | yes | no | 0/0 | clean | 0 | `f7f0bbef` |
| mcp-git-audit | yes | no | 0/0 | clean | 0 | `1b873046` |
| mcp-gsuite | yes | no | 0/0 | clean | 0 | `88decf56` |
| mcp-housekeeping-chatgpt | yes | no | 0/0 | clean | 0 | `dd8e24fd` |
| mcp-housekeeping-claude | yes | no | 0/0 | clean | 0 | `c0076708` |
| mcp-ki-kb-fs | yes | no | 0/0 | clean | 0 | `4caff6be` |
| mcp-ki-kb-notion-mirror | yes | no | 0/0 | clean | 0 | `698af10f` |
| mcp-m365 | yes | no | 0/0 | clean | 0 | `f3bd8903` |
| apps-rig.midnight.ninja | yes | no | 0/0 | clean | 0 | `680a95f4` |

† The untracked files belong by location to `ki.ways-of-working`; no content was edited, staged, stashed or removed. Its local unpublished history and files remain with that session. Initial observation: 71 ahead and 18 untracked; final observation: 72 ahead and 19 untracked. These are concurrent changes, not this run's work.

- `+/_WORK/ki.ways-of-working/briefs/wow-day-gov-209.md`
- `+/_WORK/ki.ways-of-working/briefs/wow-day-ico-001-accept.md`
- `+/_WORK/ki.ways-of-working/briefs/wow-day-mark-tidy-b.md`
- `+/_WORK/ki.ways-of-working/briefs/wow-day-mark-tidy-c.md`
- `+/_WORK/ki.ways-of-working/briefs/wow-day-mark-tidy.md`
- `+/_WORK/ki.ways-of-working/briefs/wow-day-rig-release.md`
- `+/_WORK/ki.ways-of-working/briefs/wow-day-toolski-release.md`
- `+/_WORK/ki.ways-of-working/briefs/wow-night-order.md`
- `+/_WORK/ki.ways-of-working/briefs/wow-night-rig-056-accept-c.md`
- `+/_WORK/ki.ways-of-working/briefs/wow-night-rig-056-accept-d.md`
- `+/_WORK/ki.ways-of-working/briefs/wow-night-rig-056-accept-e.md`
- `+/_WORK/ki.ways-of-working/briefs/wow-night-rig-056-c.md`
- `+/_WORK/ki.ways-of-working/briefs/wow-night-tools-rig-release-candidate-c.md`
- `+/_WORK/ki.ways-of-working/briefs/wow-night2-obs-vis-042-accept-d.md`
- `+/_WORK/ki.ways-of-working/briefs/wow-night2-obs-vis-042-accept-e.md`
- `+/_WORK/ki.ways-of-working/briefs/wow-night2-obs-vis-042-accept-f.md`
- `+/_WORK/ki.ways-of-working/briefs/wow-night2-order.md`
- `+/_WORK/ki.ways-of-working/briefs/wow-night2-techne-006-accept.md`
- `+/_WORK/ki.ways-of-working/briefs/wow-night2-techne-006.md`

Other-session HEAD movement observed during the run:

- `ki-principal`: `97da8ef0` → `21ad8b4e`; docs(work): ki.ways-of-working relaunch the mark tidy. Preserved without integration by this run.
- `ki-design`: `bfb6a45a` → `38965f00`; docs(roadmap): return icon seed set after independent review. Preserved without integration by this run.

Pending cross-machine handoff: `ki-principal` on sol, branch `main`, was 72 commits ahead of `origin/main` at the snapshot. The next machine must fetch and reconcile before working there. Publication remains outside this run's authority.

### Drift inventory

`chezmoi status` succeeded before and after the checks with the same nine targets. Status columns were verified against local command help: column one compares the last written state with the live target; column two compares the live target with the desired state. No full diff, secret-bearing target diff or apply was run.

#### Source changed upstream: seven targets

These changes were already present when this run started. Reflog records the workspace inventory update arriving on sol at 01:47:03 BST and the scheduled-job changes arriving in a prior pull at 14:11:40 BST. Nothing arrived through a merge performed by this run.

- `~/.config/rig/conf.d/50-services.toml` (` M`): upstream scheduling declarations add three disabled jobs and move HNR route drift to weekdays at 08:30. Handling: review the source declaration and its companions as one proposed change; retain the disabled state and apply gate.

- `~/bin/scheduled/rig-hnr-email-route-drift` (` A`): new upstream executable for the disabled HNR route-drift job. Handling: review and eventually deploy with its shared library and service declaration, only after approval.

- `~/bin/scheduled/rig-hnr-email-route-triage` (` M`): the non-secret scoped diff confirms extraction of common runner behaviour into `scheduled_agent.bash`. Handling: review and deploy together with that library; do not apply this wrapper alone.

- `~/bin/scheduled/rig-legal-briefing-cause-list-watch` (` A`): new upstream executable for the disabled cause-list watch. Handling: review with the shared library and disabled declaration; do not start or enable the job during reconciliation.

- `~/bin/scheduled/rig-legal-briefing-daily` (` A`): new upstream executable for the disabled daily briefing. Handling: review with the shared library and disabled declaration; retain its existing approval gate.

- `~/bin/scheduled/scheduled_agent.bash` (` A`): new upstream shared runner library. Handling: include it in the same reviewed application as the refactored triage wrapper and new job wrappers.

- `~/workspaces/humans-not-robots/.mgit.toml` (` M`): the non-secret scoped diff adds six repository members: `5g-emerge-p2ms3`, `apps-eit.humansnotrobots.be`, `apps-home.humansnotrobots.be`, `apps-packages-portal-framework`, `apps-product.humansnotrobots.be` and `apps-sales.humansnotrobots.be`. Handling: let the HNR workspace owner review the membership additions before any targeted apply; no clones or other remote operations were performed.

#### Target edited by an app or by hand: one target

- `~/Library/Application Support/Claude/claude_desktop_config.json` (`MM`): both live edits since chezmoi last wrote the file and a desired managed-fragment mismatch are present. The fragment wrapper preserves app-owned state while replacing declared MCP servers and merging trust grants. Handling: preserve those live edits and review a redacted, fragment-specific comparison in the morning; do not adopt the whole live file or restart Desktop. No private file contents were inspected, so app versus manual authorship and the exact mismatching fragment remain unproven.

#### Other: one target

- `~/.codex/config.toml` (` M`): a managed-fragment mismatch, without a detected live edit since the last chezmoi write. Its wrapper predates `efcd49b`; there is no evidence that the four subsequent commits caused it. Handling: inspect only redacted managed preference, trust and MCP key differences before choosing source or target changes. The private target was not diffed or read for this run; the exact fragment and cause remain unclassified.

#### Script entries

None: there are no `R` entries. The five scheduled paths above are managed files, not pending chezmoi run-script entries.

### Rig doctor

`rig doctor` completed with exit 1 and an unhealthy verdict: 241 passing checks, four failures, no warnings and 17 skipped. Every finding matches the supplied known four; new findings: none. This checks the live declaration, which still predates the pending service-file changes.

| Finding | Observed state | Recommended handling |
| --- | --- | --- |
| UTM | `source-mismatch:unclassified`, via MAS | Keep for attended source/removal review. |
| TOML handler | Warp is current; Zed is declared | Review the desired handler at the machine. |
| Screen-sharing firewall | `anchor-changed` | Keep held; require a tested restore path before changes. |
| TOML apply history | Failure recorded 2026-10-20 03:41:50 UTC, exit 1 | Retain the evidence for the attended handler fix. |

No finding was repaired: this task explicitly authorises a read-only baseline. The existing non-zero verdict is a known unhealthy state, not a passing gate.

### ChezMoi history since efcd49b

Exactly four commits are reachable after `efcd49b` through the current source HEAD. All have author and committer Kris Brown (`kris@kris.me.uk`). Git does not record their originating host here; the sol reflog proves receipt times, not which machine authored them. The three scheduled-job commits credit Claude Opus 5.5 (1M context); the workspace inventory commit has no model co-author trailer.

| Commit | Subject |
| --- | --- |
| `2c987ded` | Update dot_mgit.toml |
| `18f58156` | refactor(scheduled): extract the shared scheduled-agent library |
| `cc6b0dce` | feat(scheduled): add three disabled headless prompt jobs |
| `a341460e` | fix(scheduled): move HNR route drift to weekdays 08:30 |

The inventory commit was received before the scheduled-job pull. The scheduled commits cover the runner extraction, three new disabled jobs and the subsequent 08:30 slot adjustment. No originating host has been guessed.

### Checks and boundaries

- All 18 `git fetch -q --prune origin` calls succeeded; no merge, rebase, reset, stash, commit or push was performed.

- Both status inventories succeeded and matched; the two non-secret scoped diffs succeeded and were summarised above.

- `rig doctor` completed with exactly the four known findings; it did not pass.

- Final checks found no Git locks; unrelated dirty files and concurrent commits were preserved.

- Git, KI, ChezMoi and Rig subprocesses used environments with inherited `GIT_*` removed. No `op`, apply, conform write, provider mutation, scheduler change or service restart was performed. Readdle Spark and Spark Desktop were not changed.

- No repository edit was made, so repository implementation gates and commits were not applicable.

- Report Markdown validation passed with explicit repository house rules; the initial default-rule check used incompatible line-length and emphasis rules.

- All run-owned scratch output was removed; no test process, job, hook or configuration scaffolding was created.

## In Progress

Nothing running.

Outstanding - no action requested now: the supervisor owns the morning review of the seven upstream file changes, two private managed-fragment mismatches and the four already held Rig findings. This baseline does not approve application or repair.

The final progress-protocol instruction makes this state-directory file the only report path. Accordingly, no copy was written to the requested design path and no record was changed or committed. The coordinator can home this baseline at `+/_WORK/ki.chezmoi/design/reconcile-baseline-2026-10-21.md` and commit it under its own authority.

## Queries

No outstanding queries. Missing originating-host metadata and the two intentionally uninspected private-fragment differences are explicit evidence limits, not guessed conclusions.

### 🤖 → 👤 Handoff to supervisor · since 14:21 BST

🤖 0 running · 👤 0 with you · ⛔ 0 blocked

- [completed] reconciliation and drift baseline · run/reconcile-2 · since 14:21 BST
- [unpushed] ki-principal on sol, main: 72 commits at the snapshot
- [uncommitted] baseline report; coordinator owns homing and commit
