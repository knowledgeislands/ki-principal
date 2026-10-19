# [Knowledge Islands](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Charter.md) › State of play › sop-restock

**🤖 → 👤 Handoff to supervisor · Run report at 11:10 BST · last mark 16:14 BST on 15 October**

---

## Done

- Work file restocked in `4b65f1e` (local, unpushed): every Messages line acted on and removed. PRUNED-LINKS and PIN-DONE-LINKS are settled by deleting `threads-stock.report.md`. Both OVERDUE-TITLE lines and THREADS-REGRESSION are removed as resolved. MIGRATED is done: the file is now next steps, `Messages: None` and five parked tags. THREADS-ORPHANS is dropped because `+/_THREADS/` no longer exists and Rig: chezmoi's work file holds nothing for it. The 15 October settled items, the live-threads list and the closed parked items are dropped; each already has a home or is in Git history.
- Work folder pruned in the same commit. Five reports were deleted by explicit path:
  - `away-housekeeping`: OVERTAKEN-REPORTS was overtaken. `8d1d2e6` is on `origin/main` and eco-prune-4 pruned [KI-PRINCIPAL-ECO-014 (pruned)](https://github.com/knowledgeislands/ki-principal/blob/5c1f2279cfe0627d25becae76a6ce81ed8cf397d/Streams/Roadmap/KI-PRINCIPAL-ECO-014-decision-citation-and-run-folder-sweep.md).
  - `diagram-fix`: DIAGRAMS-PUSH was overtaken. All four commits are on `origin/main`.
  - `seat-change`: SEAT-PUSH was overtaken. `8d1d2e6` and `c2237da` are on `origin/main`, and the outcome is in [ADR-KI-PRINCIPAL-007](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/ADR-KI-PRINCIPAL-007-territory-seats-on-hosts.md).
  - `tools-project`: LABEL-FORM was overtaken because the work file's title is `KI > Foundations > Tools burndown`. PROJECT-OVERLAP was overtaken by OWNER-LANE in the [Tools burndown](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/tools-burndown.md) Project note.
  - `threads-stock`: BUGCENSUS-CLOSE was logged as overtaken at 22:45 BST on 17 October. ACQUIRE-LOOP-REPORT's outcome is in [KB-ACQUIRE-005](/Users/krisbrown/workspaces/personal/acquire/docs/roadmap/KB-ACQUIRE-005-seed-and-return-loop.md).
- Kept: `work.md`, `decisions.md`, `design/`, and `pilot-seed.report.md`, which is held for a terra session.
- Checks: `ki repo audit`, scoped to my paths, passes. The repository-wide audit fails RECORD-2 on this work file because of the front matter's `hold: null` line. That line was already there and the brief leaves the front matter to the coordinator. The audit's other failures belong to other work.
- `decisions.md` has uncommitted changes that are not mine. I left them alone.

Survey of the territory's work (last commit to each folder; dirty means other sessions' uncommitted files):

| Work | State | Whose move | Last commit |
| --- | --- | --- | --- |
| KI > Foundations > Baseline rollout | Handoff to supervisor | Kris | 19 Oct 11:04 |
| KI > Rig > chezmoi | Handoff to supervisor, blocked (COVERAGE-SCOPE) | Kris | 19 Oct 09:04, dirty |
| KI > Model > Knowledge acquisition | On hold, more expected | nobody until restart | 18 Oct 20:49 |
| KI > Rig > Mac Studio setup | With worker (`footer-record` running) | agent | 19 Oct 11:07, dirty |
| KI > Model > Observatory | With worker (`obs-overlay` running) | agent | 19 Oct 11:00, dirty |
| KI > Foundations > Timelines | With worker | agent | 19 Oct 11:07, dirty |
| KI > Foundations > Tools burndown | Handoff to supervisor | Kris | 19 Oct 11:05 |
| KI > Model > Ways of working | Handoff to supervisor | Kris | 19 Oct 08:48 |
| KI > Regular | On hold | nobody | 18 Oct 04:30 |
| KI > Regular > Registry removal | On hold | nobody | 18 Oct 04:39 |

- Restarts: Rig: chezmoi and Rig: mac studio setup have restarted. Knowledge acquisition has not restarted and is on hold until Kris restarts it explicitly. Host network has no work file.
- Timelines is the new [Timelines](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/timelines.md) Project, opened on 19 October. It extracts a timeline and calendar skill from the 5G Emerge phase 3 calendar component.
- Baseline rollout is the [Baseline rollout](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/baseline-rollout.md) Project. Its aim is a green `ki repo audit --estate` and the released `ki` on every island. It was bootstrapped at 11:04 BST and has nothing running.
- `ki agent status`: three runs are active (`footer-record`, `obs-overlay` and this one).

Parked queries closed, with evidence:

- FW-DECLARE-NOW was overtaken by RIG-LIVE (19 October, [Rig: chezmoi work file](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.chezmoi/work.md)). Kris holds [KI-TOOL-RIG-CORE-042](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-042-profile-filtered-dock-items.md) and [KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md) until chezmoi delivers [KB-DOTFILES-UE-091](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-091-shared-dock-tool-links.md) with a firewall declaration covering both Macs. The laptop-only file is still absent. "Waiting on Rig" is closed the same way.
- SSH-SPARE-KEY: Kris answered on 16 October that no spare key is needed and the console is the restore path. The macOS workstation guide's Restore step (`docs/guides/user/macos-workstation.md`) covers the console.
- FW-SSH-KEYONLY: answered on 15 October. The plan is in the same guide's key-only section.
- FW-TERRA-OFF: answered no on 15 October.
- ESTATE-MAP-OBSERVATORY: delivered. It is the "Estate Map as Observatory view" idea in the [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) Project's Notes.
- HOLD-MODEL, HOLD-VERBS and HOLD-BANNER: delivered by ways of working's model. The [Work Process](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Processes/Work Process/Work Process.md>) has the On hold state, "drain" as the activity and never the state, `resume` as the move off hold, and the hold report with its resume line.
- RESTART-SET: overtaken by the Work Process levels and picking-up rules, and the restart has happened.
- SOL-FIRST-CHURN: CHURN-REMEDIES was approved a) on 16 October and went to ways of working, which delivered it as the work folder's closed list, tidy rules and temporary-output rule.
- SOL-MOVE: done. The work resumed on sol on 19 October.
- HOST-ROLES: recorded in the [Host network](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/host-network.md) Notes, including the 17 October amendment. ADR-KI-PRINCIPAL-007 states it by role, and SEAT-BIND went to Rig: chezmoi.
- SYNC-GUARD: delivered as [KI-HARNESS-GOV-189](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-189-move-thread-between-hosts.md)'s "Level check, decided 2026-10-18".
- CHANNEL-TELEMETRY: homed in the Project notes.
- CLI127-LINKS: overtaken, because [KI-TOOL-KI-CLI-127 (pruned)](https://github.com/knowledgeislands/tools-ki/blob/a22214ee581b73a1f395da88f9a118ad89814bb9/docs/roadmap/KI-TOOL-KI-CLI-127-agent-status-live-threads.md) is pruned.
- GATE-REMAIN: lies with its owners. Mac Studio setup still has RECORD-2 and BOUNDARY-1. The BOUNDARY-1 failure now shows on knowledge acquisition's work file.
- Dated queue: KI-PRINCIPAL-MOD-008 is no longer overdue. [The record](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-MOD-008-whole-philosophy-coherence-review.md) now carries a 2026-10-23 review. The pruned records were dropped from the queue.
- STASH-DROP and PILOT-SEED are already authorised, so they are next steps for a terra session, not queries.

## In Progress

Nothing is running from this run.

Outstanding - no action requested now:

- `4b65f1e` is local and unpushed. It sits on a `main` that carries other sessions' commits.
- RECORD-2 on this work file's `hold: null` is the coordinator's to fix: drop the line at the next front-matter rewrite.
- The retired `kit-mcp-gmail` entry is still in the chezmoi `.chezmoiignore`. It is carried as a follow-up for Rig: chezmoi.

## Queries

### PILOT-SEED-HOME - where the copied seed section goes

**Context:** On 18 October Kris said to copy section 4 of `foundations-coherence.report.md` into `+/_THREADS/state-of-play/pilot-seed.md` at a terra session. That folder is retired. A copied report section is also not a kind the work folder's closed list allows, so it cannot go into `+/_WORK/ki/` either. Knowledge acquisition's SEED-HOME (17 October) stages seed packs in `-`.

**Query:** Where should the terra session put the section 4 copy?

**Options:** a) (recommended, confidence medium - it follows SEED-HOME and the closed list, but the seed pack's exact path is knowledge acquisition's to name) Stage it as a seed pack in `-` under SEED-HOME, with a provenance line, and tell knowledge acquisition through one Messages line. b) Hand the copy to knowledge acquisition to home in its own Project's material.

### LIVE-MAN-SWITCH - home the reverse dead man's switch idea

**Context:** On 15 October Kris proposed that each host periodically pull a control repository and re-apply its declared state, so a host that loses inbound access heals itself. It was a design input for the firewall and key-only SSH rollouts. Its likely home, [KI-TOOL-RIG-CORE-046 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/06da52aec5de/docs/roadmap/KI-TOOL-RIG-CORE-046-remote-access-and-continuity.md), was cancelled and pruned, and no Project note mentions the idea.

**Query:** Where should the idea live?

**Options:** a) (recommended, confidence high - Host network owns host access and restore paths, and its thread opens with a restore-path decision paper) Capture it as an idea in the Host network Project's Notes, flagged as a design input for the firewall and SSH rollouts. b) Send it to Rig: mac studio setup as a tools-rig idea.

### THREADS-CHECKINS - close Kris's question on check-ins

**Context:** On 15 October Kris asked how threads are used and why there are so many check-ins. It went to ways of working on 16 October as part of THREAD-DURABILITY. Since then, threads have been retired into work folders. The Work Process sets the seven states and the moves, and the coordinator style limits updates to timed one-to-two-line lines with nothing said between owner messages. The question was never answered by its tag.

**Query:** Can THREADS-CHECKINS close as delivered by the work model?

**Options:** a) (recommended, confidence medium - the model addresses both halves, but Kris has not said whether the check-in load is now acceptable) Close it as delivered, and raise it again only if the check-ins still feel excessive. b) Keep it parked for a talk with Kris about check-in frequency.

### RIG-FULLSCREEN - home the Rig full-screen mode idea

**Context:** A Rig full-screen mode idea was parked on 12 October. Its old pointer, `thread-history.md` section 5, no longer exists. Rig's new two-line progress footer is a different feature. Rig: mac studio setup holds the tools-rig lane under RIG-OWNER.

**Query:** Should the idea go to Rig: mac studio setup?

**Options:** a) (recommended, confidence medium - the idea's original wording is only in Git history) Send it to Rig: mac studio setup as a tools-rig idea, through one Messages line. b) Drop it, since Git history keeps it.

### 🤖 → 👤 Handoff to supervisor · since 11:10 BST

👤 4 with you · 🅿️ 4 parked

- [with you] PILOT-SEED-HOME · owner · since 11:10
- [with you] LIVE-MAN-SWITCH · owner · since 11:10
- [with you] THREADS-CHECKINS · owner · since 11:10
- [with you] RIG-FULLSCREEN · owner · since 11:10
- [committed] work file and folder prune, unpushed
- [uncommitted] decisions.md, another session's
