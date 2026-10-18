# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › roadmap-next

**🤖 → 🧑 Handoff to supervisor · Run report at 08:08 BST · last mark 22:34 BST**

---

## Done

- ki-principal `b567fb0`: finished the ways-of-working merge. Swept the leftover thread and checkpoint wording out of live guidance, fixed the stale links and the Known World entry, and removed the empty `+/_THREADS/` folder. The work is recorded as [KI-PRINCIPAL-MOD-010](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-MOD-010-work-model-terminology-sweep.md), now Awaiting review. The repository gate passed. `+/_THREADS/chezmoi/` and the other old folders are gone, and no other session's folder was touched.
- ki-agentic-harness `0ae39eac`: built Phase 1 of [KI-HARNESS-GOV-199](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-199-thread-identity-role-native-sessions.md).
  - It adds the "Work identity and native sessions" section to the `ki-checkpoint` standard, a `binding` glossary row and a bootstrap `level` check in `ki-pmo`, and level-gated wording in the hook line and output style, which were regenerated.
  - `bun run test` passed 1246, `tsc` passed, and the `ki-pmo`, `ki-checkpoint`, `ki-delegation` and `ki-authoring` audits passed. `ki-skills` passed with three LONG-3 warnings that were already there.
  - The record stays In progress, because Phase 3 waits on other records (see In Progress).
- ki-agentic-harness `fa9d8e57`: repointed the broken `#project-close` anchor in [KI-HARNESS-GOV-189](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-189-move-thread-between-hosts.md) to `#finishing-project-work`. This was an existing fault, and the `ki-authoring` MD-mech check now passes.
- ki-agentic-harness `0f166c31`: landed requirements 1 to 10 of [KI-HARNESS-GOV-175](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-175-delegation-run-events.md), following the run-event mechanics that [KI-TOOL-KI-CLI-123](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-123-agent-run-events.md) delivered.
  - Added a "Run events" subsection, the `wait --next`, `watch` and `send` idioms, and a unique-name rule.
  - The coordinator hook now relies on the run marker alone, with the terminal check dropped.
  - Added a new rubric item, PMO-12, at WARN, which checks that a run report opens with its `#` heading.
  - `bun run test` passed 1247 and `tsc` passed. `ki dev skill rubric ki-pmo` verified.
  - The audits passed as before, again with the three existing LONG-3 warnings.
  - The record stays In progress, because the mark rule is still open (see MARK-RULE-SPLIT).
- No other session's commits were pushed: each pull with rebase brought nothing in beneath mine. I accepted nothing.
- I re-surveyed every Next and Ready record in ki-principal, tools-ki, tools-rig, tools-mgit and ki-agentic-harness. None of the rest can be built locally without an owner decision, network access or another record landing first:
  - ki-agentic-harness:
    - [KI-HARNESS-GOV-170](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-170-keep-resolution-targets-local.md) is scheduled for later.
    - [KI-HARNESS-GOV-209](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-209-acquired-inbound-area.md) waits on work in the personal territory.
    - [KI-HARNESS-OPS-009](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-OPS-009-complete-ai-session-acquisition.md) needs network access and is large.
  - tools-ki:
    - [KI-TOOL-KI-CLI-125](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-125-ki-release-contract.md) is on hold.
    - [KI-TOOL-KI-CLI-136](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-136-errors-suggest-fixes.md) is blocked by [KI-TOOL-KI-CLI-131](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-131-host-absent-store-state.md).
    - [KI-TOOL-KI-CLI-139](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-139-ebu-sources-sync.md) reaches into other territories and browser cookies.
    - [KI-TOOL-KI-CLI-140](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-140-git-hygiene-estate-audit.md) waits on [KI-HARNESS-GOV-203](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-203-git-clean-down-criteria.md) and [KI-TOOL-MGIT-CLI-021](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-021-estate-overview.md).
  - [KI-PRINCIPAL-ECO-013](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-ECO-013-pmo-extraction-pilot.md) is a Codex pilot.
  - tools-rig and tools-mgit have nothing at Next or Ready.

## In Progress

Nothing is running.

- [KI-HARNESS-GOV-199](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-199-thread-identity-role-native-sessions.md) Phase 3 and its pilots are waiting on three things:
  - the `ki thread` tooling in [KI-TOOL-KI-CLI-145](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-145-thread-session-bindings-role.md);
  - the hook registration in [KB-DOTFILES-UE-096](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-096-thread-identity-hook-registration.md);
  - the pilot label, PILOT-LABEL, already open with you.
- The mark rule in [KI-HARNESS-GOV-175](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-175-delegation-run-events.md) is waiting on you (MARK-RULE-SPLIT).
- [KI-HARNESS-GOV-194](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-194-review-verification-effects.md) is waiting on you (GOV194-REFRESH).
- [KI-TOOL-KI-CLI-134](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-134-launch-footer-follows-brief.md) is waiting on you (CLI134-GRANTS).

Outstanding - no action requested now

- PMO-7 flags record identifiers left unlinked in older reports in the `ki.chezmoi`, `ki.tools-burndown`, `ki`, `ki.mac-studio-setup`, `ki.observatory`, `ki.knowledge-acquisition` and `ki.ways-of-working` work folders. The coordinators can fix these at their next marks.
- PMO-9 lists prune candidates in the same work folders. Pruning is the coordinators' job at their marks.
- The new PMO-12 warns on 14 older reports in `ki.chezmoi`, `ki.tools-burndown` and `ki` that open with a lint directive or a frame, not the heading. They will clear as those folders are pruned.
- ki-engineering SCR-11 wants the ki-principal `.husky/pre-commit` to start with lint-staged and then run `bunx syncpack format --check`. I did not touch the gate during an overnight run.
- The `ki.ways-of-working` work file still carries the MIGRATED line in its Messages section. That line is the coordinator's to act on.
- Two chezmoi records share the identifier KB-DOTFILES-UE-096:
  - [the thread-identity hook registration](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-096-thread-identity-hook-registration.md)
  - [Gmail routing paths](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-096-configure-gmail-routing-paths.md)

  The chezmoi work should renumber one of them. Chezmoi is outside this run's scope, so I left it.
- The pruned record [KI-HARNESS-GOV-184 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/731580841ce5be89687784284a432e84a187646f/docs/roadmap/KI-HARNESS-GOV-184-working-area-marks.md) now lives on inside KI-HARNESS-GOV-175, so nothing is needed from it.

## Queries

### MARK-RULE-SPLIT - Split the working-area mark rule out of the run-events record

**Context:** [KI-HARNESS-GOV-175](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-175-delegation-run-events.md) now has requirements 1 to 10 landed and checked. The only part still open is the working-area mark rule, merged in from [KI-HARNESS-GOV-184 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/731580841ce5be89687784284a432e84a187646f/docs/roadmap/KI-HARNESS-GOV-184-working-area-marks.md) on 14 October. That rule still needs its sidecar and front-matter field names settled, and those are your call. While the rule stays in the record, the finished run-events work cannot go to review.

**Query:** Should the mark rule move back into its own record, so that KI-HARNESS-GOV-175 can go to Awaiting review now?

**Options:** a) (recommended, confidence medium - the landed part is complete and checked, and the mark rule is a separate design decision) Split the mark rule into a new harness record and move KI-HARNESS-GOV-175 to Awaiting review. b) Keep the rule in KI-HARNESS-GOV-175 and settle the field names now, so a later run can build it in the same record.

### PMO12-LEVEL - Severity of the report-heading check

**Context:** The new PMO-12 check confirms that a run report's first non-blank line is its `#` heading, after any front matter. It runs at WARN and currently warns on 14 older reports, which open with a markdownlint directive or a frame. A lint directive before the heading counts as a failure today.

**Query:** Should PMO-12 stay at WARN, and should a leading lint-directive comment count as a failure?

**Options:** a) (recommended, confidence medium - the older reports clear as folders are pruned, and a FAIL now would block the coordinators' marks) Keep WARN, keep counting a lint directive as a failure, and promote to FAIL once those folders have been pruned. b) Promote to FAIL now. c) Keep WARN and let a lint-directive comment come before the heading.

### IDENTITY-TIMING - Keep the work identity section landed ahead of the tooling

**Context:** The [KI-HARNESS-GOV-199](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-199-thread-identity-role-native-sessions.md) Discussion left open whether the identity section should land before the `ki thread` tooling. I settled it provisionally by landing it now, with a sentence saying no binding is written until [KI-TOOL-KI-CLI-145](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-145-thread-session-bindings-role.md) and [KB-DOTFILES-UE-096](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-096-thread-identity-hook-registration.md) ship.

**Query:** Do you confirm that the identity section stays landed now, ahead of the tooling?

**Options:** a) (recommended, confidence high - the section is guarded by its no-binding sentence and the level gating is already in use) Confirm, and leave Phase 3 waiting on the two records. b) Revert the section and land it together with the tooling.

### GOV194-REFRESH - Long-skill refresh needs network access

**Context:** [KI-HARNESS-GOV-194](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-194-review-verification-effects.md) owns the three LONG-3 warnings that every `ki-skills` audit reports. Clearing them needs a fresh look at outside sources, which this run was not allowed to fetch.

**Query:** Should a run with network access do the LONG-3 refresh?

**Options:** a) (recommended, confidence medium - the warnings recur in every audit and the fix is bounded) Queue a run with network access for the KI-HARNESS-GOV-194 refresh. b) Leave the warnings until the record comes up in order.

### CLI134-GRANTS - Grant texts for the launch footer

**Context:** [KI-TOOL-KI-CLI-134](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-134-launch-footer-follows-brief.md) makes the launch footer follow the brief. It needs the harness-owned grant texts in `skills/governance/ki-delegation/assets/` agreed first (FOOTER-GRANTS, open since 16 October). The texts set how much authority a run gets, so I did not draft them.

**Query:** Should a harness run draft the grant texts for you to approve, so that KI-TOOL-KI-CLI-134 can go ahead?

**Options:** a) (recommended, confidence medium - drafting is low risk, while the wording of a grant is your call) Have a harness run draft `grant-fetch.md` and `grant-machine.md` for your review. b) Write or dictate the texts yourself.

### COMPOSE-REPLY-BLOCK - tools-ki launch prompt still asks for a reply block

**Context:** The `composePrompt` text in tools-ki still tells runs to put outstanding queries "with the reply block". That contradicts your 18 October REPLY-BLOCK decision, which removed the reply block. Every launched run sees that text. The fix is in tools-ki, so it needs a tools-ki record, which this run did not open.

**Query:** Should I add a tools-ki handoff record to remove the reply-block wording from `composePrompt`?

**Options:** a) (recommended, confidence high - it is a one-line wording fix that brings the launcher into line with a standing decision) Add the tools-ki record at Next, and a later run builds it. b) Fold the fix into [KI-TOOL-KI-CLI-134](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-134-launch-footer-follows-brief.md), which already edits the launch prompt.

### 🤖 → 🧑 Handoff to supervisor · since 08:08 BST

🧑 6 with you · ⏳ 1 waiting

- [with you] MARK-RULE-SPLIT · owner · since 08:08
- [with you] PMO12-LEVEL · owner · since 08:08
- [with you] IDENTITY-TIMING · owner · since 08:08
- [with you] GOV194-REFRESH · owner · since 08:08
- [with you] CLI134-GRANTS · owner · since 08:08
- [with you] COMPOSE-REPLY-BLOCK · owner · since 08:08
- [waiting] KI-HARNESS-GOV-199 Phase 3 · KI-TOOL-KI-CLI-145 and KB-DOTFILES-UE-096 · since 08:08
- [committed] ki-principal and ki-agentic-harness, pushed
