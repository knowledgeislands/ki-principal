# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of Working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wf-review

**🤖 → 👤 Handoff to supervisor · Run report at 04:06 BST · last mark unavailable to blind review**

---

## Done

Blind review completed: WORKTREE-INTEGRATE - Yes, confidence medium; WORKTREE-START - start now in code repositories, confidence medium, subject to the conditions below.

Standards check: integration requires its own authority and a serialised primary-checkout write window; independent review remains required by the selected local-integration workflow ([ki-git](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-git/references/standards-git.md:69)).

Tooling inspection: current run status summarises process state, queue and inbox, rather than worktree delivery state ([runs.ts](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:556)); KB authority includes exact registered-path matching ([authority.ts](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/kb/authority.ts:16)). This supports the need for F3 and F5; it is source inspection, not a reproduced audit failure.

CLI help check: completed locally; no launch-time worktree allocation option is exposed by the inspected agent command interface.

Blindness and authority check: the prohibited work folder and all decisions logs remained unread; no repository changes, records, commits or remote calls were made. Only the requested runtime status and report files were written.

## In Progress

Nothing is running within this review.

Outstanding - no action requested now: trial execution, tooling delivery and repository-specific grants remain with the coordinator. No live integration, concurrency or audit tests were run. The coordinating work's last mark was not supplied and was not inferred from its unread package.

## Queries

### WORKTREE-INTEGRATE - authority to integrate a run's delivery

**Context:** Requiring a separate merge launch creates a second queue after implementation has finished. Fast-forward integration can remove that queue, but it still changes a busy primary checkout; a passing branch alone does not establish that the current combined result is safe. Neither option fixes a red baseline.

**Query:** Should worktree runs receive standing authority to fast-forward their verified delivery into local primary main before reporting?

**Options:**

a) (recommended, confidence medium - bounded self-integration removes the extra launch without needing to relax the integration checks) Yes, for explicitly enrolled repositories and eligible runs. The repository grant must name the local destination, scope, required review and gates, and fast-forward-only method. Rebase only the run's own unpublished delivery onto current main; independently review the exact candidate where repository policy requires it, then pass all required gates on the combined result. Acquire an exclusive Git write window respected by every primary-checkout writer, recheck source and destination commits and checkout/index state, and revalidate if the destination moved. Do not integrate over contested staging, an active Git operation or changes that would be overwritten. Self-integration grants no self-approval, push, acceptance or baseline bypass. If any condition fails, retain the branch and worktree and report them stranded with their exact location and reason. Remove them only after proving delivery reached the intended destination and nothing remains to preserve.

b) Keep integration with a separately authorised coordinator merge run, launched promptly on delivery completion; F3 and F4 expose waiting branches. Prefer this fallback wherever a shared write window or the required independent review cannot be established.

### WORKTREE-START - when to begin the trial

**Context:** Isolation addresses collisions immediately. F2 and F3 improve reliable allocation and visibility, while F5 fixes a known obstacle to meaningful ki-principal worktree audits. A small code-repository pilot can supply those operational safeguards manually while tooling is built.

**Query:** Start now under F1 and F4 in code repositories, or wait for F2, F3 and F5 before starting everywhere?

**Options:**

a) (recommended, confidence medium - a bounded code-repository pilot can test the workflow before registry-dependent knowledge-base runs join) Start now in code repositories under F1 and F4; add ki-principal only after F5 makes its required gates valid. Until F2 and F3 land, the coordinator must allocate collision-safe worktree paths and branch names, give each concurrent writer a separate worktree, and maintain a manual inventory of owner, location, local-main ahead/behind counts, uncommitted files and age. Inspect stranded deliveries on completion or failure as well as at each mark; marks alone leave an unbounded waiting interval. Start only from a green baseline, preserve required gates and review, and enforce F6 for tools-ki edits from the first pilot. Pause new launches if allocation, inspection or serialised integration cannot be maintained. This is a limited pilot, not permission to expand concurrency before one complete delivery and retirement succeeds.

b) Wait for F2, F3 and F5, then start everywhere. Choose this if the coordinator cannot reliably provide the temporary manual safeguards; landing those features still does not replace integration authority, independent review or serialised Git writes.

---

### 🤖 → 👤 Handoff to supervisor · since 04:06 BST

🤖 0 running · 👤 2 recommendations with you · ⛔ 0 blocked

- [with you] WORKTREE-INTEGRATE recommendation · supervisor · since 04:06 BST
- [with you] WORKTREE-START recommendation · supervisor · since 04:06 BST
