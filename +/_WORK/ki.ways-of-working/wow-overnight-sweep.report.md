# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-overnight-sweep

**🤖 → 👤 Handoff to supervisor · Run report at 00:24 BST · last mark 23:16 BST**

---

## Done

- Swept all 44 open records across tools-\*, mcp-\* and apps-\* and the two held queues. This was read-only: nothing changed, nothing committed, no remote call.
- 8 of the 15 repositories in scope have no open records: tools-mgit, tools-git-almanac, mcp-acquire-whatsapp, mcp-git-audit, mcp-housekeeping-chatgpt, mcp-housekeeping-claude, mcp-ki-kb-fs and mcp-ki-kb-notion-mirror.
- Only 5 records can be worked tonight under the grants as they stand. 25 are valid holds or wait on other work. 12 need Kris, either a decision or being present. 2 should be cancelled or reshaped.
- Other sessions have one commit each stacked in tools-git-almanac, tools-ki and tools-techne. Nothing is uncommitted anywhere. apps-observatory.local is level with origin, so the eight commits OBS-ACCEPT2-FOLLOWUPS reported are now pushed.
- The ki.ways-of-working `queries.md` is out of date. It still lists as open the queries answered at 23:16: FOOTER-PROVISIONALS, SPEC-SKETCH, RIG-053-SHAPE, PLAN067-READY, DESIGN-DISPOSITIONS, TOOLS-KI-SHAPES, GOV225-CLOSE, OPS009-SPLIT, CALENDAR-LIBRARY and LAYER-PATHS. It also lists ENACTMENT-ADMIN, taken at 23:30. The coordinator should move them out under SMALL-FIXES.
- The KI-TOOL-RIG-CORE pre-commit hook still runs the full Bats suite, so RIG-PRECOMMIT-BATS has not landed. That hook is the one thing that unblocks KI-TOOL-RIG-CORE-053, -056, -047 and -062.
- Under EMAIL-OWNER, the email-routing records number 11, not 12: KI-MCP-M365-TOOL-020 does not exist.

### Counts by repository

Categories: 1 workable tonight · 2 needs a Kris decision · 3 needs Kris present · 4 waiting on other work · 5 cancel or reshape.

| Repository | Open | 1 | 2 | 3 | 4 | 5 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| apps-knowledgeislands.info | 1 | 0 | 0 | 1 | 0 | 0 |
| apps-observatory.local | 14 | 0 | 1 | 3 | 10 | 0 |
| mcp-gsuite | 2 | 0 | 0 | 0 | 2 | 0 |
| mcp-m365 | 9 | 0 | 0 | 0 | 9 | 0 |
| tools-ki | 8 | 2 | 1 | 0 | 4 | 1 |
| tools-rig | 9 | 3 | 1 | 4 | 0 | 1 |
| tools-techne | 1 | 0 | 1 | 0 | 0 | 0 |
| **Total** | **44** | **5** | **4** | **8** | **25** | **2** |

### Per record

**apps-knowledgeislands.info**

- [KI-WEBSITE-SITE-044](/Users/krisbrown/workspaces/knowledge-islands/apps-knowledgeislands.info/docs/roadmap/KI-WEBSITE-SITE-044-design-v1.md) (awaiting review): category 3. It needs public access to ki-design and Kris's checks at 1,440 and 390 px in both colour schemes. That is already asked under SITE-SOURCE, which is open. HEADLESS-LOOK would cover the functional half.

**apps-observatory.local**

- [KI-OBSERVA-APP-044](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md) (draft, now): category 2. It is a `decide` record and can only run once step 3 has shipped.
  - Step 3 is [KI-OBSERVA-VIS-030](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-030-known-lands-chart.md) and [KI-OBSERVA-BRG-005](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-005-act-board-missing-parts.md). [KI-OBSERVA-VIS-044 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/e23d85acb3404c2a9cc8ce52bf7bad8b72093a61/docs/roadmap/KI-OBSERVA-VIS-044-commit-authors-in-tables.md) has landed.
  - How it decides is ki.observatory's parked RESTRUCTURE.
  - Its Current state still calls BRG-005 a draft at `now`. That is stale, a one-line fix.
- [KI-OBSERVA-BRG-004](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-004-turn-feedback-sending-on.md) (hold): category 4. It waits only on [KI-OBSERVA-BRG-006](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-006-feedback-to-messages-file.md) being accepted, since its harness dependency is already accepted. It releases when BRG-006 does.
- [KI-OBSERVA-BRG-005](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-005-act-board-missing-parts.md) (awaiting review): category 3.
  - The only check left is the owner's: plan a fetch and a `rig apply`, then confirm the scope and inputs rows read well at 1,440 and 760 px.
  - This is open as OBS-ACT-VISUAL. It is a functional check, so HEADLESS-LOOK would cover it.
- [KI-OBSERVA-BRG-006](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-006-feedback-to-messages-file.md) (awaiting review): category 3. This is open as OBS-BRG-006-VISUAL.
  - Every acceptance point has a test with sending forced on.
  - Sending ships switched off, so nothing on screen changes.
  - The outstanding service restart no longer matters, because the service runs `bun --watch`.
  - HEADLESS-LOOK would cover it, or an independent review could simply accept it.
- [KI-OBSERVA-INT-003](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-INT-003-extensions-switchboard.md) (hold): category 4. The Git view, [KI-OBSERVA-VIS-041 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/e23d85acb3404c2a9cc8ce52bf7bad8b72093a61/docs/roadmap/KI-OBSERVA-VIS-041-git-view-replaces-repositories.md), has landed. The inbound phase still waits on the rest of step 3 (VIS-030 and BRG-005). Each later phase needs Kris's approval.
- [KI-OBSERVA-OPS-004](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-OPS-004-tailnet-read-only-appearance.md) (hold): category 4. It waits on Host network's tailnet service-name decision, which ROADMAP-CENSUS-2 re-validated on 20 October.
- [KI-OBSERVA-VIS-028](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-028-retire-sessions-readers.md) (hold): category 4. It waits on phase 5 of the work migration.
- [KI-OBSERVA-VIS-029](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-029-sessions-from-every-host.md) (hold): category 4. Same hold as OPS-004.
- [KI-OBSERVA-VIS-030](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-030-known-lands-chart.md) (in progress): category 3. Its look and positions stay with Kris's designs.
  - The browser smoke and the audit can be done tonight. Its check by eye cannot.
  - This record is also what holds up the end of step 3.
- [KI-OBSERVA-VIS-032](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-032-library-instrument.md), [KI-OBSERVA-VIS-034](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-034-streams-instrument.md) and [KI-OBSERVA-VIS-045](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-045-workers-instrument.md) (hold): category 4. Each waits on APP-044's decision and then on Kris approving its consolidation.
- [KI-OBSERVA-VIS-038](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-038-machine-instrument.md) (hold): category 4.
  - Its consolidation phase waits on APP-044.
  - Its storage phase waits on [KI-HARNESS-GOV-227](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-227-repository-storage-declarations.md), which waits on GOV227-SCHEMA (open).
- [KI-OBSERVA-VIS-042](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-042-diagram-overlay-everywhere.md) (hold): category 4. It waits on [KI-HARNESS-GOV-224](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-224-diagram-viewer-receipts.md), which failed review. The rework that would restore staged-snapshot enforcement sits as GOV-224-REWORK in the held ki.observatory queue.

**mcp-gsuite and mcp-m365**

- All 11 email-routing records are category 4: [KI-MCP-GSUITE-TOOL-008](/Users/krisbrown/workspaces/knowledge-islands/mcp-gsuite/docs/roadmap/KI-MCP-GSUITE-TOOL-008-consume-the-routing-core.md), [KI-MCP-GSUITE-TOOL-009](/Users/krisbrown/workspaces/knowledge-islands/mcp-gsuite/docs/roadmap/KI-MCP-GSUITE-TOOL-009-add-gmail-routing-report-mode.md), [KI-MCP-M365-TOOL-011](/Users/krisbrown/workspaces/knowledge-islands/mcp-m365/docs/roadmap/KI-MCP-M365-TOOL-011-judgment-verdict-hook.md), [KI-MCP-M365-TOOL-012](/Users/krisbrown/workspaces/knowledge-islands/mcp-m365/docs/roadmap/KI-MCP-M365-TOOL-012-judged-mail-recheck.md), [KI-MCP-M365-TOOL-013](/Users/krisbrown/workspaces/knowledge-islands/mcp-m365/docs/roadmap/KI-MCP-M365-TOOL-013-per-rule-hit-counts.md), [KI-MCP-M365-TOOL-014](/Users/krisbrown/workspaces/knowledge-islands/mcp-m365/docs/roadmap/KI-MCP-M365-TOOL-014-routing-run-ledger.md), [KI-MCP-M365-TOOL-015](/Users/krisbrown/workspaces/knowledge-islands/mcp-m365/docs/roadmap/KI-MCP-M365-TOOL-015-deduplicate-saved-attachments.md), [KI-MCP-M365-TOOL-016](/Users/krisbrown/workspaces/knowledge-islands/mcp-m365/docs/roadmap/KI-MCP-M365-TOOL-016-thread-follow-skips-disposal-folders.md), [KI-MCP-M365-TOOL-017](/Users/krisbrown/workspaces/knowledge-islands/mcp-m365/docs/roadmap/KI-MCP-M365-TOOL-017-size-the-hold-window.md), [KI-MCP-M365-TOOL-018](/Users/krisbrown/workspaces/knowledge-islands/mcp-m365/docs/roadmap/KI-MCP-M365-TOOL-018-extract-the-routing-core.md) and [KI-MCP-M365-TOOL-019](/Users/krisbrown/workspaces/knowledge-islands/mcp-m365/docs/roadmap/KI-MCP-M365-TOOL-019-move-the-rule-specification.md).
  - Each is on a valid hold under EMAIL-OWNER, held by hnr.email-routing until Kris resumes Humans not Robots work.
  - They only count as cleared if a valid hold does (HOLDS-COUNT).

**tools-ki**

- [KI-TOOL-KI-CLI-125](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-125-ki-release-contract.md) (hold): category 4. It is a valid hold until an ARM host is needed, with a review due on 16 November.
- [KI-TOOL-KI-CLI-139](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-139-ebu-sources-sync.md): category 2.
  - Where its command group sits is the parked SRC-PLACEMENT.
  - It is Humans not Robots work, and the first live sync needs Kris's Chrome session.
- [KI-TOOL-KI-CLI-140](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-140-git-hygiene-estate-audit.md): category 1.
  - TOOLS-KI-SHAPES a) is answered, and harness b91fa71d makes CLEAN-2 to CLEAN-7 mechanical over `mgit overview --json`.
  - Steps: plan it to Ready around that output, deliver it in a worktree, get a blind review, then accept and prune.
- [KI-TOOL-KI-CLI-145](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-145-thread-session-bindings-role.md): category 5.
  - Work packages have replaced its thread and checkpoint keys.
  - The other half is still needed: launches should not get the coordinator output style. This run received it.
  - Reshape it to that half and probe `--settings` locally (STALE-RESHAPE).
- [KI-TOOL-KI-CLI-149](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-149-work-status-views-contract.md) and [KI-TOOL-KI-CLI-160](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-160-work-status-routing-view.md): category 4. Both wait on State of play confirming the form work status takes. Kris could settle it directly (WORK-STATUS-FORM).
- [KI-TOOL-KI-CLI-156](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-156-ci-runs-local-gate.md): category 1. Steps: read the latest CI runs, then either fix the audit gate or add the missing steps, as BIOME-CI-STANDARD a) directs. Then review and accept.
  - Reading CI with `gh` is a remote read, which the run's brief must allow.
- [KI-TOOL-KI-CLI-157](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-157-validator-parity.md): category 4. Under VALIDATOR-HOME a), the rule table and fixtures go into the harness first, then tools-ki vendors them.

**tools-rig**

- [KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md) and [KI-TOOL-RIG-CORE-062](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-062-own-address-firewall-destination.md) (in progress, failed acceptance): category 3.
  - They change the firewall, so they are connection-critical.
  - They need the hook fix, a re-review, then Kris's live apply on terra and then sol. This is under RIG-ATTENDED (open).
- [KI-TOOL-RIG-CORE-048](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-048-signed-release-install-kind.md) (soon): category 1. It serves vega under the Techne Programme Focus.
  - Steps: plan its design choices through a blind review, then deliver against a fixture signed release, review and accept.
- [KI-TOOL-RIG-CORE-053](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-053-macos-menu-bar-declarations.md) (awaiting review): category 2. RIG-053-SHAPE a) is taken. Accepting it tonight with order drift caveated needs RIG-053-ORDER. It also needs the hook fix first.
- [KI-TOOL-RIG-CORE-056](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-056-menu-bar-order-persistence.md) (awaiting review): category 1 once the hook is fixed.
  - Steps: integrate the rework on branch `run/wow-rework-rig-056` (3160dcc7) after the failed review on `run/wow-accept-rig-056` (4efcee6b), then a fresh blind review, then accept.
- [KI-TOOL-RIG-CORE-064](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-064-unmanaged-configuration-scan.md) (triage): category 5. It is outside the vega and sol focus, so it should become an Idea line (STALE-RESHAPE).
- [KI-TOOL-RIG-CORE-067](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-067-package-managers-as-catalogue-tools.md) (Ready): category 1. Steps: deliver its nine fixture-only steps, then review and accept.
- [KI-TOOL-RIG-CORE-068](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-068-replaced-pf-root-ruleset-bypass.md) and [KI-TOOL-RIG-CORE-069](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-069-dynamic-type-handler-fallback.md): category 3, under RIG-ATTENDED (open).
- Something tonight's runs can do first: line the tools-rig pre-commit hook up with the canonical hook (RIG-PRECOMMIT-BATS). It is a small audit fix that needs no record. The line asking for it sits in the held ki.tools-burndown queue (QUEUES-OVERNIGHT).

**tools-techne**

- [KI-TOOL-TECHNE-CLI-006](/Users/krisbrown/workspaces/knowledge-islands/tools-techne/docs/roadmap/KI-TOOL-TECHNE-CLI-006-guarded-host-commands.md): category 2, under TECHNE-006-REVIEW (open).

## In Progress

Nothing is running.

Outstanding - no action requested now

- These queries are already open and are not asked again here: GRANT-INTERIM, OBS-ACT-VISUAL, OBS-BRG-006-VISUAL, SITE-SOURCE, RIG-ATTENDED, TECHNE-006-REVIEW and GOV227-SCHEMA. RELEASE-OVERNIGHT a) would also answer GRANT-INTERIM, and HEADLESS-LOOK a) would answer OBS-ACT-VISUAL and OBS-BRG-006-VISUAL.
- Some ki.tools-burndown parked queries have been overtaken and need no answer.
  - CAPTURE-FOLLOWUPS: [KI-TOOL-KI-CLI-152 (pruned)](https://github.com/knowledgeislands/tools-ki/blob/fde00e97/docs/roadmap/KI-TOOL-KI-CLI-152-work-folder-housekeeping-commands.md) and [KI-TOOL-KI-CLI-167 (pruned)](https://github.com/knowledgeislands/tools-ki/blob/fde00e97/docs/roadmap/KI-TOOL-KI-CLI-167-knip-reads-committed-hooks.md) are pruned, and their follow-ups are already message lines.
  - WORKTREE-GATE: settled as F5 under WORKTREE-START a).
  - Most of ki.observatory's parked ACCEPT bundle is already pruned. All of these are struck under STALE-RESHAPE.
- The coordinator's medium- and low-confidence queries below still need a blind review before they reach Kris.

## Queries

### QUEUES-OVERNIGHT - Act on the two held queues tonight

**Context:** ki.tools-burndown and ki.observatory are both on hold until Kris says resume, but their `messages.md` queues hold most of the work that can be done tonight:

- Worktree fixes F2, F3, F5 and F6 (WORKTREE-START a)).
- The tools-rig hook fix (RIG-PRECOMMIT-BATS), which unblocks [KI-TOOL-RIG-CORE-053](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-053-macos-menu-bar-declarations.md), [KI-TOOL-RIG-CORE-056](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-056-menu-bar-order-persistence.md), [KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md) and [KI-TOOL-RIG-CORE-062](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-062-own-address-firewall-destination.md).
- In tools-ki, narrowing the `acquisitionActions` ledger and the parser change for local resolution.
- The four OPS009-SPLIT capture lines for tools-ki.
- The [KI-HARNESS-GOV-224](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-224-diagram-viewer-receipts.md) rework.
- Five briefs to tidy at the burndown folder root.
- The leftover bring-up lines.

**Query:** May ki.ways-of-working work through both held queues tonight under OVERNIGHT-BURNDOWN, without resuming those works, with its coordinator capturing the records that Kris-authorised lines ask for?

**Options:** a) (recommended, confidence high - every line is either already authorised by Kris or a small audit fix, and it keeps the burn-down order) Yes. Act on every authorised or mechanical line. Capture only what Kris has already authorised, such as OPS009-SPLIT. Leave lines that need a decision, such as RIG-REMINDER-DOCTOR and the AGENTS.md "confirm it answers" change, in place. b) Only the hook fix and the worktree fixes. Leave everything else held until each work is resumed. c) No. Wait for resume.

### HEADLESS-LOOK - A headless check instead of Kris's look, for function only

**Context:** These records wait only on Kris looking at them at the reserved widths, and those checks are functional rather than aesthetic:

- [KI-OBSERVA-BRG-005](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-005-act-board-missing-parts.md): do the scope and inputs rows appear at 1,440 and 760 px?
- [KI-OBSERVA-BRG-006](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-006-feedback-to-messages-file.md): nothing visible changes while sending is off.
- The functional half of [KI-WEBSITE-SITE-044](/Users/krisbrown/workspaces/knowledge-islands/apps-knowledgeislands.info/docs/roadmap/KI-WEBSITE-SITE-044-design-v1.md).

Accepting BRG-006 releases [KI-OBSERVA-BRG-004](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-004-turn-feedback-sending-on.md). Accepting BRG-005 moves step 3 towards releasing [KI-OBSERVA-APP-044](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md). The look of [KI-OBSERVA-VIS-030](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-030-known-lands-chart.md) and SITE-044's design judgement would stay with Kris.

**Query:** May a recorded headless-browser check at the reserved widths stand in for Kris's functional checks, so independent reviewers can accept on it?

**Options:** a) (recommended, confidence medium - it clears three records tonight, but leans on a headless render matching Kris's browser) Yes, for functional checks only, with screenshots kept in the review packet. This answers OBS-ACT-VISUAL and OBS-BRG-006-VISUAL. The look stays with Kris. b) Yes for BRG-006 only, where nothing visible changes. BRG-005 and SITE-044 wait for the morning. c) No. Every check named for the owner waits for Kris.

### HOLDS-COUNT - Whether valid holds count as cleared

**Context:** 25 of the 44 records wait validly on other work:

- The 11 email-routing records in mcp-m365 and mcp-gsuite, held by hnr.email-routing under EMAIL-OWNER.
- 10 Observatory holds behind step 3, APP-044, Host network, phase 5 of the work migration and the GOV-224 and GOV-227 harness records.
- [KI-TOOL-KI-CLI-125](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-125-ki-release-contract.md), waiting on ARM hardware.
- Three tools-ki records waiting on the harness or State of play.

No run can move any of them tonight.

**Query:** For "roadmaps cleared overnight", does a record on a re-validated hold count as cleared?

**Options:** a) (recommended, confidence medium - the holds are real and re-validated, and forcing them would mean work outside the focus) Yes. "Cleared" means nothing actionable is left. Holds stay where they are, with their conditions restated. b) Move the 11 email-routing records out of the KI repositories into Humans not Robots tracking, so the KI roadmaps show only KI work. c) Cancel the email-routing records, to be recaptured when Humans not Robots work resumes.

### STALE-RESHAPE - Cancel or reshape stale records and parked queries

**Context:**

- [KI-TOOL-KI-CLI-145](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-145-thread-session-bindings-role.md): work packages have replaced its thread and checkpoint keys. Only its launch-style half is still needed.
- [KI-TOOL-RIG-CORE-064](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-064-unmanaged-configuration-scan.md): a triage idea outside the Techne Programme Focus.
- Parked queries that have been overtaken:
  - In ki.tools-burndown, CAPTURE-FOLLOWUPS and WORKTREE-GATE.
  - In ki.observatory, most of the ACCEPT bundle.
  - In ki.observatory's messages, the serve-stale-binary line and its correction.

**Query:** May the overnight runs reshape KI-TOOL-KI-CLI-145, turn KI-TOOL-RIG-CORE-064 into an Idea line, and strike the overtaken parked items?

**Options:** a) (recommended, confidence high - each item has been overtaken by a decision already taken or by the focus, and nothing is lost because Git keeps the history) Yes, all of it. CLI-145 is cut down to its launch-style half and planned. RIG-064 is cancelled and becomes an Idea line on the Rig Project note. b) Strike the overtaken queries, but leave CLI-145 and RIG-064 for the morning. c) Leave all of it.

### RELEASE-OVERNIGHT - Patch or minor releases after acceptance

**Context:** Once accepted, tonight's tools-ki work (worktree fixes, [KI-TOOL-KI-CLI-140](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-140-git-hygiene-estate-audit.md), [KI-TOOL-KI-CLI-156](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-156-ci-runs-local-gate.md)) and tools-rig work ([KI-TOOL-RIG-CORE-056](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-056-menu-bar-order-persistence.md), [KI-TOOL-RIG-CORE-067](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-067-package-managers-as-catalogue-tools.md)) only reaches the installed tools through a release. GRANT-INTERIM (open) already asks for a tools-ki release carrying `--allow`. A release is publication, which OVERNIGHT-BURNDOWN leaves for the morning.

**Query:** May overnight runs cut tools-ki and tools-rig patch or minor releases, through each repository's own release process, once every included record has been accepted?

**Options:** a) (recommended, confidence medium - releases come from accepted work through the repositories' own pipelines, but publication is the one step OVERNIGHT-BURNDOWN kept for Kris) Yes, patch and minor only, from accepted work, through each repository's release process. This also answers GRANT-INTERIM. b) Prepare the release notes and version bump, but leave the tag and publication to Kris in the morning. c) No releases overnight.

### RIG-053-ORDER - Accept the menu bar declarations with order drift caveated

**Context:** [KI-TOOL-RIG-CORE-053](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-053-macos-menu-bar-declarations.md) is awaiting review, and RIG-053-SHAPE a) is taken. Its order-drift report can only be confirmed by Kris doing a Command-drag on sol (RIG-053-LEGACY-ORDER). Everything else the record does is observe-only and covered by tests. Once the tools-rig hook is fixed, an independent review can rule on all of it except that check.

**Query:** May KI-TOOL-RIG-CORE-053 be accepted on its tests, with the order-drift check by Command-drag on sol recorded as a caveat to do after release?

**Options:** a) (recommended, confidence medium - apply never writes and never fails, so the caveat cannot harm sol, but order drift stays unconfirmed) Yes. Accept with the caveat, and leave the Command-drag check as a line for Kris's next session at sol. b) Hold acceptance until Kris has done the Command-drag check.

### SRC-PLACEMENT - Where the EBU SharePoint sync command sits

**Context:** [KI-TOOL-KI-CLI-139](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-139-ebu-sources-sync.md) mirrors EBU SharePoint sources for hnr-principal. Where its command sits is parked in ki.tools-burndown, where a reviewer favoured a separately specified source-maintenance command group in `ki`, with medium confidence. Its first live sync needs Kris's Chrome session, and it is Humans not Robots work, outside the Techné focus.

**Query:** Should KI-TOOL-KI-CLI-139 be planned tonight, or held with the rest of the Humans not Robots work?

**Options:** a) (recommended, confidence medium - it is Humans not Robots work and cannot be finished without Kris's Chrome session, so planning it now gains little) Hold it until Kris resumes Humans not Robots work, keeping SRC-PLACEMENT parked. b) Settle SRC-PLACEMENT with the reviewer's view and plan it to Ready tonight, leaving the live sync for Kris.

### OBS-FOLLOWUPS - Dispositions for the Observatory's parked queries

**Context:** ki.observatory has four parked queries of medium confidence.

- RESTRUCTURE: how [KI-OBSERVA-APP-044](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md) decides. A review agreed with the direction but would keep the Work tab as it is.
- TEN-COMMITS, MERMAID-HANDLER and BRIDGE-STALE (not yet reviewed).

Separately, the serve-watch and ops003-delivered lines ask whether AGENTS.md should say "confirm <http://127.0.0.1:1675/> answers" instead of "restart", since the service now runs `bun --watch`. APP-044 itself cannot run until [KI-OBSERVA-VIS-030](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-030-known-lands-chart.md) and [KI-OBSERVA-BRG-005](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-005-act-board-missing-parts.md) land.

**Query:** May the coordinator take each parked Observatory query's recommended option, after a blind review of BRIDGE-STALE, and make the AGENTS.md wording change?

**Options:** a) (recommended, confidence medium - all four already carry recommendations and none commits Kris to a design, but RESTRUCTURE shapes the instrument model) Take the recommendations for TEN-COMMITS, MERMAID-HANDLER and BRIDGE-STALE (once reviewed) and change the AGENTS.md wording. Keep RESTRUCTURE for Kris, since APP-044 cannot run tonight anyway. b) Take all four, RESTRUCTURE included, with the review's view of keeping the Work tab. c) Leave all of them for the morning.

### WORK-STATUS-FORM - Settle what work status looks like

**Context:** [KI-TOOL-KI-CLI-149](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-149-work-status-views-contract.md) (the contract for work-status views) and [KI-TOOL-KI-CLI-160](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-160-work-status-routing-view.md) (the routing view, `--view routing`) both wait on State of play confirming what form work status takes. State of play has not answered, and no run can.

**Query:** Should Kris settle the work-status form directly, so both records can be planned tonight?

**Options:** a) (recommended, confidence medium - it unblocks two records, but the form is State of play's to own) Yes. Kris confirms the form already described in KI-TOOL-KI-CLI-149, and a run plans and delivers both records with `--view routing` as written. b) Leave both waiting on State of play.

### 🤖 → 👤 Handoff to supervisor · since 00:24 BST

👤 9 with you · ⏸️ 25 waiting on other work

- [with you] QUEUES-OVERNIGHT · owner · since 00:24
- [with you] HEADLESS-LOOK · owner · since 00:24
- [with you] HOLDS-COUNT · owner · since 00:24
- [with you] STALE-RESHAPE · owner · since 00:24
- [with you] RELEASE-OVERNIGHT · owner · since 00:24
- [with you] RIG-053-ORDER · owner · since 00:24
- [with you] SRC-PLACEMENT · owner · since 00:24
- [with you] OBS-FOLLOWUPS · owner · since 00:24
- [with you] WORK-STATUS-FORM · owner · since 00:24
- [ready] 5 workable records: KI-TOOL-KI-CLI-140, KI-TOOL-KI-CLI-156, KI-TOOL-RIG-CORE-048, -056 and -067 · coordinator · since 00:24
- [unpushed] tools-git-almanac, tools-ki, tools-techne, one stacked commit each
