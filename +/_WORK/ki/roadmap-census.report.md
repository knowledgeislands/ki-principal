# [Knowledge Islands](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/Themes.md) › State of play › roadmap-census

**🤖 → 👤 Handoff to supervisor · Run report at 23:17 BST · last mark 18:58 BST**

---

## Done

Read-only census, flow and diagnosis for ROADMAP-GROWTH, taken at 23:14 BST on 19 October from `ki repo -t knowledge-islands roadmap summary` and `list --format json` (both worked), with Git history over 21 September to 19 October read locally. No commits, no record touched; checks: none to run.

### Census

Knowledge Islands territory, 21 repositories: **125 open records** (plus one done awaiting prune). Later is `soon` and `future`. Awaiting review sits inside Now. Added and closed count record files created and deleted over the four weeks, with same-name renames and cross-repository moves removed.

| Repository | Open | Now (of which Awaiting review) | Next | Later | Hold | Triage | Added / closed, 4 weeks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ki-design | 24 | 21 (14) | 2 | 0 | 1 | 0 | +25 / -1 |
| apps-observatory.local | 21 | 1 (0) | 1 | 0 | 1 | 18 | +101 / -89 |
| ki-agentic-harness | 20 | 2 (1) | 2 | 2 | 1 | 13 | +153 / -146 |
| tools-ki | 18 | 5 (3) | 2 | 0 | 1 | 10 | +77 / -60 |
| tools-rig | 15 | 2 (2) | 0 | 1 | 3 | 9 | +76 / -64 |
| mcp-m365 | 10 | 0 | 0 | 10 | 0 | 0 | +14 / -14 |
| ki-principal | 4 | 1 (0) | 0 | 0 | 1 | 2 | +48 / -70 |
| tools-mgit | 4 | 0 | 1 | 0 | 0 | 3 | +22 / -19 |
| ki-techne-harness | 2 | 0 | 0 | 0 | 2 | 0 | +21 / -24 |
| mcp-gsuite | 2 | 0 | 0 | 2 | 0 | 0 | +4 / -12 |
| tools-techne | 2 | 0 | 1 | 0 | 1 | 0 | +6 / -7 |
| apps-knowledgeislands.info | 1 | 1 (0) | 0 | 0 | 0 | 0 | +30 / -32 |
| ki-specifications | 1 | 0 | 0 | 0 | 0 | 1 | +2 / -5 |
| mcp-git-audit | 1 | 0 | 0 | 0 | 0 | 1 | +2 / -7 |
| Seven others, now empty † | 0 | 0 | 0 | 0 | 0 | 0 | +13 / -41 |
| **Territory** | **125** | **33 (20)** | **9** | **15** | **11** | **57** | **+594 / -591** |
| chezmoi ‡ | 20 | 2 (1) | 9 | 3 | 4 | 2 | +62 / -50 |

† homebrew-tap, mcp-acquire-whatsapp, mcp-housekeeping-chatgpt, mcp-housekeeping-claude, mcp-ki-kb-fs, mcp-ki-kb-notion-mirror, tools-git-almanac. ‡ Personal territory, worked by ki.chezmoi; shown for its lane, not in the total. It also holds one cancelled record awaiting prune.

Territory flow by week (Monday start): 21 Sep +126 / -101; 28 Sep +112 / -166; 5 Oct +123 / -199; 12 Oct +182 / -99; 19 Oct (one day) +51 / -26.

Open record files at the end of each day: 27 Sep 148; 4 Oct 94; 11 Oct 21; **12 Oct 16**; 13 Oct 34; 14 Oct 31; 15 Oct 40; 16 Oct 54; 17 Oct 68; 18 Oct 101; now 126.

### Diagnosis

- **The burn-down worked, then capture outran it.** The roadmap went from 148 to 16 in a fortnight, then back to 126 in seven days. Since the 14 October burn-down focus, 209 records were added and 117 closed. 116 of today's 125 open records were created on or after 14 October; the median age is one day. The problem is not old records going stale. Capture outpaces closure.
- **Capturing a record is the default response.** `ki-next` captures `triage` without approval, and run briefs and reports turn each out-of-scope finding into a record. Unadopted triage is now 57 records (46%). Going by the record text (a rough heuristic), open records came from audit and conformance findings 38, trades and transfers 27, hand-offs 24, run follow-ups 10, explicit owner requests 4, and other sources 23.
- **One record per decision.** The Observatory hand-off to ki-design became 15 records in one commit on 19 October. 14 of them went straight to Awaiting review, each recording a decision already settled ("app wins"). A meeting of one design system with one app produced more records than the whole of tools-rig holds.
- **New repositories and designs arrive with full roadmaps and no owning work.** ki-design brought 24 records over 18 and 19 October under `project: ki-design`, which has no Project note and no work package. The email-routing engine design put 12 drafts into mcp-m365 and mcp-gsuite on 17 and 18 October with no Project and no work. That is 36 records (29%) that no live work owns. 62 open records carry no `project` at all.
- **Awaiting review is the acceptance queue: 20 records waiting on Kris.** Most were created today, so this is a queue, not neglect. Without a regular acceptance pass it grows by the day.
- **Holds come back, but in a cluster.** All 11 holds carry a review date, so none are forgotten. 7 of them wait on the same unblocker: the agent host, vega's rebuild or an ARM host, across tools-ki, tools-rig, tools-techne and ki-techne-harness.
- **Fan-out and near-duplicates.** One standard ([KI-HARNESS-GOV-218](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-218-cli-conventions.md)) spawned a departures record in each of three tools. One Bats warning became two records. Diagrams are spread over five records in three repositories. Several records written in thread vocabulary predate the work model.

### Closable candidates (evidence only, nothing acted on)

**ki-design**

- [KI-DESIGN-OBS-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-OBS-001-row-and-type-scale.md), [KI-DESIGN-OBS-002](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-OBS-002-frame-gutter.md), [KI-DESIGN-OBS-003](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-OBS-003-tab-glyph-size.md), [KI-DESIGN-OBS-004](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-OBS-004-one-glyph-per-tab.md), [KI-DESIGN-OBS-005](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-OBS-005-subject-glyphs.md), [KI-DESIGN-OBS-006](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-OBS-006-work-banner-emoji.md), [KI-DESIGN-OBS-007](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-OBS-007-decision-record-number.md), [KI-DESIGN-OBS-008](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-OBS-008-role-colours-match.md), [KI-DESIGN-OBS-009](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-OBS-009-git-tracker-draft-overtaken.md), [KI-DESIGN-OBS-010](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-OBS-010-tailnet-draft-overtaken.md), [KI-DESIGN-OBS-011](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-OBS-011-switchboard-draft-overtaken.md), [KI-DESIGN-OBS-012](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-OBS-012-act-follows-authority.md), [KI-DESIGN-OBS-013](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-OBS-013-tab-count.md), [KI-DESIGN-OBS-014](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-OBS-014-sessions-stays-runs-view.md): Awaiting review. All were captured in one commit, each carries a Review section and each reads "Decided by: app wins". [KI-DESIGN-OBS-009](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-OBS-009-git-tracker-draft-overtaken.md), [KI-DESIGN-OBS-010](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-OBS-010-tailnet-draft-overtaken.md) and [KI-DESIGN-OBS-011](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-OBS-011-switchboard-draft-overtaken.md) only mark ki-design drafts as overtaken. One `ki-accept` pass closes all 14.
- [KI-DESIGN-OBS-015](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-OBS-015-banner-glyphs-question.md): held, "Needs Kit. ki-design does not decide this." This is a question for the owner, not work. It already sits in `docs/decisions/OPEN.md`, so the record can be cancelled.
- Seven drafts at Now, [KI-DESIGN-TOK-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-TOK-001-tokens-v0.md), [KI-DESIGN-ELE-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md), [KI-DESIGN-ICO-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ICO-001-icon-seed-set.md), [KI-DESIGN-SYM-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-SYM-001-symbol-library-data.md), [KI-DESIGN-TIL-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-TIL-001-tile-set-contract.md), [KI-DESIGN-MAP-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-MAP-001-hexmap-v0.md) and [KI-DESIGN-ART-002](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ART-002-art-licensing.md), have no owning work. They are not closures, but they should leave Now until a work owns them.

**apps-observatory.local**

- [KI-OBSERVA-VIS-031](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-031-who-is-working.md): accepted at 23:09 BST today and ready to prune.
- [KI-OBSERVA-VIS-032](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-032-library-instrument.md), [KI-OBSERVA-VIS-033](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-033-waiting-for-you.md), [KI-OBSERVA-VIS-034](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-034-streams-instrument.md), [KI-OBSERVA-VIS-038](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-038-machine-instrument.md): four triage "instrument" ideas sitting beside [KI-OBSERVA-APP-044](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md), "Instrument restructure decision". They read as Idea bullets in the Observatory Project note until [KI-OBSERVA-APP-044](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md) is decided.
- [KI-OBSERVA-VIS-029](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-029-sessions-from-every-host.md), "Sessions from every host" (triage), cuts across [KI-OBSERVA-VIS-028](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-028-retire-sessions-readers.md), "Retire Sessions readers" (held). One of them should go.
- [KI-OBSERVA-BRG-004](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-004-turn-feedback-sending-on.md), [KI-OBSERVA-BRG-006](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-006-feedback-to-messages-file.md) and [KI-HARNESS-GOV-219](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-219-feedback-work-folder-kind.md): three feedback-path records across two repositories. They are merge candidates (medium).

**ki-agentic-harness**

- [KI-HARNESS-GOV-218](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-218-cli-conventions.md): Awaiting review since 18 October and ready for acceptance. Its three fan-out records, [KI-TOOL-KI-CLI-151](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-151-cli-conventions-departures.md), [KI-TOOL-MGIT-CLI-029](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-029-cli-convention-departures.md) and [KI-TOOL-RIG-CLI-027](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CLI-027-command-line-convention-departures.md), could wait as one line in it until it is accepted.
- [KI-HARNESS-GOV-200](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-200-thread-folder-closed-list.md): its own Discussion says the standards wording was built on 18 October and only the rubric checks remain. Its temporary-home footer is overtaken, because runs now use system temp outside the repository (this run's packet does). Re-scope it or cancel it as superseded (medium).
- [KI-HARNESS-GOV-189](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-189-move-thread-between-hosts.md), "Move coordinating thread to another host" (triage), is idea-grade and predates the work model (medium).
- [KI-HARNESS-GOV-222](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-222-timeline-and-calendar-skill.md), "Timeline and calendar skill" (triage), belongs as an idea with ki.timelines.
- [KI-HARNESS-GOV-223](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-223-island-maturity-declaration.md) with [KI-TOOL-KI-CLI-159](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-159-island-maturity-and-health.md), "Island maturity", are a harness and CLI pair of triage ideas. They should become one Idea bullet.
- [KI-HARNESS-GOV-205](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-205-static-light-diagram-export.md), [KI-HARNESS-GOV-221](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-221-ki-diagrams-mermaid-fence-warning.md), [KI-HARNESS-GOV-224](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-224-diagram-viewer-receipts.md), [KI-SPEC-RGV-004](/Users/krisbrown/workspaces/knowledge-islands/ki-specifications/docs/roadmap/KI-SPEC-RGV-004-archify-status-flow-diagrams.md) and [KI-OBSERVA-VIS-042](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-042-diagram-overlay-everywhere.md): five diagram records across three repositories. They are merge candidates (low; scopes differ in detail).

**tools-ki**

- [KI-TOOL-KI-CLI-155](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-155-priority-and-size-fields.md), [KI-TOOL-KI-CLI-158](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-158-work-status-reads-packages.md), [KI-TOOL-KI-CLI-162](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-162-gfm-converter.md): Awaiting review and ready for acceptance. Accepting [KI-TOOL-KI-CLI-155](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-155-priority-and-size-fields.md) releases the CLI-FIELDS hold on 18 records.
- [KI-TOOL-KI-CLI-160](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-160-work-status-routing-view.md), "Work status routing view", overlaps [KI-TOOL-KI-CLI-158](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-158-work-status-reads-packages.md), which adds the same description and pending-message fields, and [KI-TOOL-KI-CLI-149](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-149-work-status-views-contract.md)'s views contract. It is a merge candidate (medium).
- [KI-TOOL-KI-CLI-145](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-145-thread-session-bindings-role.md), "Thread session bindings", is the tools-ki half of the in-progress [KI-HARNESS-GOV-199](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-199-thread-identity-role-native-sessions.md). Keep it, but restate it in work-model terms.

**tools-rig, tools-mgit, tools-techne, ki-techne-harness**

- [KI-TOOL-RIG-CORE-042](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-042-profile-filtered-dock-items.md), [KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md): Awaiting review. [KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md) is accepted on a pass under FW-ADR (15 October), but still needs the terra steps.
- [KI-TOOL-RIG-CORE-063](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-063-fatal-bats-assertions.md) and [KI-TOOL-MGIT-CLI-027](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-027-fatal-bats-assertions.md), "Fatal Bats assertions": the same mechanical `|| false` fix in two repositories. Each is a small direct fix that needs no record.
- The agent-host hold cluster: [KI-TOOL-KI-CLI-125](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-125-ki-release-contract.md), [KI-TOOL-RIG-CORE-048](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-048-signed-release-install-kind.md), [KI-TOOL-RIG-DIST-011](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-DIST-011-stale-terra-rig-link.md), [KI-TOOL-RIG-CLI-026](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CLI-026-per-tool-development-mode-switch.md), [KI-TOOL-TECHNE-CLI-006](/Users/krisbrown/workspaces/knowledge-islands/tools-techne/docs/roadmap/KI-TOOL-TECHNE-CLI-006-guarded-host-commands.md), [KI-TECHNE-OPS-018](/Users/krisbrown/workspaces/knowledge-islands/ki-techne-harness/docs/roadmap/KI-TECHNE-OPS-018-converge-tools-through-rig.md) and [KI-TECHNE-OPS-024](/Users/krisbrown/workspaces/knowledge-islands/ki-techne-harness/docs/roadmap/KI-TECHNE-OPS-024-weekly-pin-bump.md). These are 7 holds reviewed between 12 and 16 November on one unblocker. One owner should review them together.

**ki-principal**

- [KI-PRINCIPAL-MOD-008](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-MOD-008-whole-philosophy-coherence-review.md): held "until most of Arcadia's roadmap is cleared", review 23 October. ki-principal has 4 open records, so the condition is met. Release it or make it an idea.
- [KI-PRINCIPAL-ECO-013](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-ECO-013-pmo-extraction-pilot.md), "PMO extraction pilot", has been in progress since 14 October with 6 of 15 steps open. The PMO has since become `ki-coordination` and the work model, so check whether it is superseded (low).

**mcp-m365, mcp-gsuite**

- [KI-MCP-M365-TOOL-011](/Users/krisbrown/workspaces/knowledge-islands/mcp-m365/docs/roadmap/KI-MCP-M365-TOOL-011-judgment-verdict-hook.md) to [KI-MCP-M365-TOOL-020](/Users/krisbrown/workspaces/knowledge-islands/mcp-m365/docs/roadmap/KI-MCP-M365-TOOL-020-distribute-the-routing-core.md) (10) and [KI-MCP-GSUITE-TOOL-008](/Users/krisbrown/workspaces/knowledge-islands/mcp-gsuite/docs/roadmap/KI-MCP-GSUITE-TOOL-008-consume-the-routing-core.md), [KI-MCP-GSUITE-TOOL-009](/Users/krisbrown/workspaces/knowledge-islands/mcp-gsuite/docs/roadmap/KI-MCP-GSUITE-TOOL-009-add-gmail-routing-report-mode.md): the email-routing engine design, at Later, with no Project or work. They are not closures. They need one hold or one owner.

**chezmoi**

- [KB-DOTFILES-UE-095](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-095-guide-continuity-check.md): cancelled and ready to prune. [KB-DOTFILES-UE-091](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-091-shared-dock-tool-links.md): Awaiting review.

First wave if approved: 22 acceptances or prunes (14 ki-design, 3 tools-ki, 2 tools-rig, 1 harness, [KI-OBSERVA-VIS-031](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-031-who-is-working.md), [KB-DOTFILES-UE-095](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-095-guide-continuity-check.md)) plus about 12 cancellations, merges and conversions to ideas. That takes the territory from 125 to about 90. De-queuing ki-design and the email-routing cluster then leaves about 30 in active horizons.

### Proposed burn-down plan

1. **Intake rule.** A background run never captures. It lists follow-ups in its report, and the coordinator of the owning work decides. A new record needs a blocker, a defect seen failing, or a Kris request (the 14 October rule), and must name its owning work. One record per change, never one per decision. Ideas go to the Project note's Idea bullets or `_IDEAS.md`. Audit warnings on small fixes are fixed directly, without a record.
2. **Caps.** Territory open count of 60 or fewer by 2 November and 40 or fewer by 16 November. Per lane: Now 5 or fewer, Awaiting review 5 or fewer, triage 10 or fewer. A lane at its cap closes before it captures.
3. **Lane owners.** ki.tools-burndown takes tools-ki, tools-mgit, tools-rig, tools-techne and mcp-git-audit (40). ki.observatory takes apps-observatory.local and ki-design (45), plus the website's design adoption. ki.ways-of-working takes ki-agentic-harness, ki-principal and ki-specifications (25). ki.chezmoi takes chezmoi (20). ki.mac-studio-setup reviews the agent-host hold cluster (7) and ki-techne-harness. The email-routing cluster (12) holds as one until a Project opens for it.
4. **First wave.** Each lane runs one `ki-accept` pass on its Awaiting review records and brings its cancel, merge and idea list above to Kris for a single approval per lane.
5. **Measure.** Each Monday, State of play reports per lane: open count, records added and closed over the week, Awaiting review and triage against the caps, from `ki repo -t knowledge-islands roadmap summary` and the Git add and delete count used here. The target is a net decrease every week. This extends the daily count snapshots agreed under ROADMAP-SIZING (14 October).

## In Progress

Nothing is running. Every figure above is a snapshot at 23:14 BST; ki.observatory accepted [KI-OBSERVA-VIS-031](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-031-who-is-working.md) and pruned [KI-OBSERVA-APP-042 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/22ea8dcbf7fba0806f1370899cd506a6705c3741/docs/roadmap/KI-OBSERVA-APP-042-design-tokens-and-glyphs.md) during this run.

Outstanding - no action requested now:

- Limitation: the origin classification and the duplicate pairs come from titles and record text, not full reads. Each lane should confirm its candidates before cancelling.
- Before 14 October, a few weeks of add and close counts include ID migrations that Git could not pair as renames, which inflates both sides equally.

## Queries

### CAPTURE-GATE - stop runs creating records

**Context:** 209 records were added in the six days after the 14 October "no new feature records" focus. 57 open records (46%) are unadopted triage, mostly findings and follow-ups captured automatically by runs. The 14 October rule names what may be captured but never says who captures. `ki-next` permits triage capture without approval.

**Query:** Should only the coordinator of the owning work create records, with runs listing follow-ups in their reports?

**Options:**
a) (recommended, confidence high - the inflow data is direct and the rule only narrows who captures) Runs never capture. The owning work's coordinator captures only a blocker, a defect seen failing or a Kris request, naming the work. Ideas go to Project notes. Small audit fixes are done without a record. State of play adds this to every brief and routes a method change to ki.ways-of-working for `ki-next` and `ki-delegation`.
b) Keep automatic triage capture but cap triage at 10 per repository.

### ROADMAP-CAP - caps and weekly measure

**Context:** The roadmap went from 148 to 16 in two weeks when focused, then back to 126 in seven days. There is no cap, so nothing forces a lane to close before it captures. The 14 October ROADMAP-SIZING decision already agreed daily count snapshots.

**Query:** Should the territory run to caps of 60 by 2 November and 40 by 16 November, with per-lane limits and a Monday measure?

**Options:**
a) (recommended, confidence medium - the targets are judgement, though the first wave alone reaches about 90) Territory 60 or fewer by 2 November and 40 or fewer by 16 November. Per lane: Now 5 or fewer, Awaiting review 5 or fewer, triage 10 or fewer. A lane at its cap closes before it captures. State of play reports per lane each Monday.
b) No hard caps; a weekly measure only.

### LANE-OWNERS - who owns each roadmap

**Context:** 36 open records have no live work: ki-design's 24, whose `project: ki-design` has no Project note, and the 12 email-routing drafts in mcp-m365 and mcp-gsuite. The other repositories map onto existing works. Seven holds share the agent-host unblocker.

**Query:** Do you agree the lane owners as proposed, with ki-design under ki.observatory and the email-routing cluster held as one?

**Options:**
a) (recommended, confidence medium - the ki-design hand-off is Observatory-driven, but ki-design may deserve its own work) ki.tools-burndown takes the tools repositories and mcp-git-audit. ki.observatory takes apps-observatory.local, ki-design and the website's design adoption. ki.ways-of-working takes ki-agentic-harness, ki-principal and ki-specifications. ki.chezmoi takes chezmoi. ki.mac-studio-setup takes the agent-host hold cluster and ki-techne-harness. The 12 email-routing records move to one hold until a Project opens.
b) Open a separate ki.design work for ki-design, and give the email-routing records to ki.knowledge-acquisition.

### BURN-WAVE-1 - authorise the first wave

**Context:** 22 records can close by acceptance or prune: 14 ki-design hand-off decisions, 3 tools-ki, 2 tools-rig, 1 harness, plus [KI-OBSERVA-VIS-031](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-031-who-is-working.md) and [KB-DOTFILES-UE-095](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-095-guide-continuity-check.md). About 12 more are cancellation, merge or idea candidates, listed under Done by repository. Together they take the territory from 125 to about 90.

**Query:** Should each lane run its acceptance pass now and bring its cancel and merge list to you for one approval per lane?

**Options:**
a) (recommended, confidence high - acceptance stays with you per lane, and nothing is cancelled without your approval) Each lane owner runs one `ki-accept` pass on its Awaiting review records and presents its cancel, merge and idea list as a single query. The 14 ki-design records go as one batch.
b) Present every record to you individually.

### 🤖 → 👤 Handoff to supervisor · since 23:17 BST

👤 4 with you

- [with you] CAPTURE-GATE · owner · since 23:17
- [with you] ROADMAP-CAP · owner · since 23:17
- [with you] LANE-OWNERS · owner · since 23:17
- [with you] BURN-WAVE-1 · owner · since 23:17
