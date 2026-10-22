# [Model](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md>) › [Ways of working](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md>) › ts-review

**🤖 → 👤 Handoff to supervisor · Run report at 02:17 BST · last mark 02:01 BST**

---

## Done

- CHECKOUT-ISOLATION: **b), confidence medium** - separate working trees and indexes address both commit contamination and in-flight audit failures; serial, verified integration must keep main usable. Checked: both cited mixed commits and the historical 62-commit stack with 11 portable-specifications commits are verified locally. Wrong or overstated: the available retros support checkout trouble in eight of nine works, not nine of ten; worktrees still need serial integration and do not themselves clear an unpublished stack or eliminate all shared-reference locks. Evidence: [retrospective](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/retro-2026-10-20.md:12>) and [existing parallel-run isolation rule](</Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-delegation/references/standards-background-runs.md:152>).
- OOS-WAKE: **a), confidence medium** - a work-scoped detached watcher fits the existing launcher and avoids making progress depend on a host scheduler. It needs an expiring autonomy window, one watcher per work, durable event receipts and an idle message-polling wake as well as completion wakes; coordinator resumption is new behaviour, not an existing launcher capability. Checked: five retros mention wake/watcher problems, and the three reported gaps total about 219 minutes across works, reasonably described as about four hours. No factual Context claim disproved; that is aggregate delay, not four distinct elapsed hours. Option b) also needs an explicit change to the [host sessions policy](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Policies/Techne Programme Focus.md:29>), which currently excludes unattended or scheduled agents on either host. Evidence: [baseline timing](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.baseline-rollout/design/retro-2026-10-20.md:10>), [waiter delay](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown/design/retro-2026-10-20.md:14>), [session loss](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/retro-2026-10-20.md:10>) and [current watcher implementation](</Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:672>).
- OWNER-QUEUE: **a), confidence high** - cap new queue-producing builds and planning, then batch owner decisions and attended checks; keep acceptance fixes and backlog-clearing work possible. Wrong: there are **21**, not 22, records awaiting review across the stated lanes: 16 Observatory-related and five Mac Studio; the sixth Mac Studio item was accepted and pruned before the retro. The 20 chezmoi and 15 baseline queries are unresolved but **parked**, with none open at review; the audit warns above eight under Open and sets no acceptance cap. Two retros independently propose an approximately eight-item cap; the exact threshold is a reversible policy choice, not an evidenced optimum. Evidence: [Observatory proposal](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.observatory/design/retro-2026-10-20.md:20>), [chezmoi proposal](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.chezmoi/design/retro-2026-10-20.md:23>), [parked chezmoi queries](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.chezmoi/queries.md>), [parked baseline queries](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.baseline-rollout/queries.md>) and [audit rule](</Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/scripts/rubric/items/threads.ts:125>).

## In Progress

Nothing is running. No repository edits, commits or network calls were made. The three excluded sources and all run reports were left unread; only the requested runtime status and this report were written.

Outstanding - no action requested now: the coordinator can fold these independent recommendations and corrections into the owner-facing queries. The support counts use the nine available retros; no tenth retrospective was present at review.

## Queries

No outstanding queries.

### 🤖 → 👤 Handoff to supervisor · since 02:17 BST

🤖 0 running · 👤 0 with you · ⛔ 0 blocked

- [handoff] Three-query blind review complete · ki.ways-of-working coordinator · since 02:17 BST
