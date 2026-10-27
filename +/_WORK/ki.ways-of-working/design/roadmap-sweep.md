---
note_type: streams/design
updated: 2026-10-27T00:10:00Z
author: Written with Claude
---

# Roadmap sweep

**Owner:** Kris Brown · **Owning repository:** knowledgeislands/ki-principal · **Owning work:** `ki.ways-of-working` · **Date:** 2026-10-27 · **Status:** decision pack, awaiting Kris's bulk decisions. Replaces the 20 October sweep, which Git keeps at `23d81aba`.

Kris, 26 October 2026, 23:40 GMT: "get the Knowledge Island stuff roadmap down to next to nothing ... the observatory is a bit of a mess ... It needs to be finished in the next few hours ... we need to be less concerned with doing releases ... everything should be linked locally ... If it's down to the CI builds, I'd rather it disabled them for now."

Read-only survey of every open work record in the Knowledge Islands territory as of 00:05 GMT on 27 October, under the [Techne Programme Focus](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Policies/Techne%20Programme%20Focus.md). Nine KI repositories hold no records at all (ki-specifications, homebrew-tap, tools-techne, tools-git-almanac, mcp-acquire-whatsapp, mcp-git-audit, mcp-housekeeping-chatgpt, mcp-housekeeping-claude, mcp-ki-kb-fs).

## Totals

| Bucket | Records | Bulk decision |
| --- | --- | --- |
| A. Already done: accept and prune | 9 | "accept bucket A as listed" |
| B. Obsolete, superseded or idea only: cancel | 10 | "cancel bucket B as listed" |
| C. Small, agent-doable tonight | 8 | "run bucket C as listed" |
| D. One decision each from Kris | 7 | answer the seven lines in bucket D |
| E. Waits on a release or CI | 3 | "drop the release dependencies in bucket E" |
| F. Larger: defer to Later | 28 | "defer bucket F to Later" |
| **Total** | **65** | After A to C and E: 35 open, of which 28 are Later |

| Repository | Open | A | B | C | D | E | F |
| --- | --- | --- | --- | --- | --- | --- | --- |
| apps-observatory.local | 12 | 2 | 0 | 1 | 4 | 0 | 5 |
| tools-rig | 11 | 2 | 1 | 5 | 1 | 0 | 2 |
| ki-agentic-harness | 10 | 2 | 5 | 1 | 0 | 0 | 2 |
| tools-ki | 10 | 0 | 4 | 1 | 0 | 1 | 4 |
| mcp-m365 | 9 | 0 | 0 | 0 | 0 | 0 | 9 |
| ki-design | 4 | 0 | 0 | 0 | 1 | 0 | 3 |
| ki-principal | 3 | 2 | 0 | 0 | 1 | 0 | 0 |
| ki-techne-harness | 2 | 0 | 0 | 0 | 0 | 2 | 0 |
| mcp-gsuite | 2 | 0 | 0 | 0 | 0 | 0 | 2 |
| apps-knowledgeislands.info | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| tools-mgit | 1 | 0 | 0 | 0 | 0 | 0 | 1 |
| **Total** | **65** | **9** | **10** | **8** | **7** | **3** | **28** |

## A. Already done: accept and prune

Four are `done` and only await the prune; five are `awaiting-review` with their review packets in place, six of them already parked as `ACCEPT-*` queries in the State of play package.

| Record | Title | Repository | Disposition | Reason |
| --- | --- | --- | --- | --- |
| [KI-PRINCIPAL-MOD-009 (pruned)](https://github.com/knowledgeislands/ki-principal/blob/da027e6d/Streams/Roadmap/KI-PRINCIPAL-MOD-009-amend-adr-001-staging-wording.md) | Amend ADR-KI-PRINCIPAL-001 staging wording | ki-principal | prune | `done` since 26 Oct 22:11 GMT |
| [KI-PRINCIPAL-OPS-014 (pruned)](https://github.com/knowledgeislands/ki-principal/blob/da027e6d/Streams/Roadmap/KI-PRINCIPAL-OPS-014-gfm-conversion.md) | Convert ki-principal to GitHub-flavoured Markdown | ki-principal | accept | awaiting review since 20 Oct; all batches applied; parked as ACCEPT-KI-PRINCIPAL-OPS-014 |
| [KI-HARNESS-GOV-189 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/bedbb4d9/docs/roadmap/KI-HARNESS-GOV-189-move-thread-between-hosts.md) | Repository level check | ki-agentic-harness | prune | `done` 22 Oct; the `[behind]` banner item is live in ki-coordination |
| [KI-HARNESS-GOV-209 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/bedbb4d9/docs/roadmap/KI-HARNESS-GOV-209-acquired-inbound-area.md) | `+/_ACQUIRED/` inbound area | ki-agentic-harness | prune | `done` 22 Oct, reviewed with no defect |
| [KI-OBSERVA-BRG-005 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/0966ac3e/docs/roadmap/KI-OBSERVA-BRG-005-act-board-missing-parts.md) | Act board missing parts | apps-observatory.local | accept | awaiting review since 22 Oct; parked as ACCEPT-OBSERVATORY |
| [KI-OBSERVA-VIS-030 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/0966ac3e/docs/roadmap/KI-OBSERVA-VIS-030-known-lands-chart.md) | Known Lands chart | apps-observatory.local | accept | awaiting review since 22 Oct; parked as ACCEPT-OBSERVATORY |
| [KI-WEBSITE-SITE-044 (pruned)](https://github.com/knowledgeislands/apps-knowledgeislands.info/blob/ae886e2b/docs/roadmap/KI-WEBSITE-SITE-044-design-v1.md) | Adopt ki-design v1 | apps-knowledgeislands.info | accept | awaiting review since 20 Oct; site live on the design; parked as ACCEPT-KI-WEBSITE-SITE-044 |
| [KI-TOOL-RIG-CORE-053](https://github.com/knowledgeislands/tools-rig/blob/223ba459/docs/roadmap/KI-TOOL-RIG-CORE-053-macos-menu-bar-declarations.md) | macOS menu bar declarations | tools-rig | prune | `done` 23 Oct under Kris's acceptance decisions of 02:10 and 02:12 BST |
| [KI-TOOL-RIG-CORE-062](https://github.com/knowledgeislands/tools-rig/blob/223ba459/docs/roadmap/KI-TOOL-RIG-CORE-062-own-address-firewall-destination.md) | Own-address firewall destination | tools-rig | accept | resubmitted 22 Oct with the audit refusal cleared; 602 Bats pass; parked as ACCEPT-KI-TOOL-RIG-CORE-062 |

**Bulk decision:** "accept bucket A as listed".

## B. Obsolete, superseded, duplicate or idea only: cancel

Each is unadopted triage, or adopted and held on something that never came. Cancelling keeps the record in Git history; where a line says "idea", one `Idea:` line goes on the named Project note or theme page.

| Record | Title | Repository | Disposition | Reason |
| --- | --- | --- | --- | --- |
| [KI-HARNESS-GOV-204](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/ideas/KI-HARNESS-GOV-204-pretooluse-quietening-hook.md) | PreToolUse quietening hook | ki-agentic-harness | cancel, idea on ways-of-working | held since 20 Oct for evidence Kris never supplied; the quiet-tools rule now covers the noise |
| [KI-HARNESS-GOV-228](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/ideas/KI-HARNESS-GOV-228-home-work-spec.md) | Home the work spec | ki-agentic-harness | cancel, idea on portable-specifications | unadopted triage; the Project is on hold; HOMING-REVIEW decision survives in the record's history |
| [KI-HARNESS-GOV-229](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/ideas/KI-HARNESS-GOV-229-home-acquire-spec.md) | Home the acquire spec | ki-agentic-harness | cancel, idea on portable-specifications | as GOV-228 |
| [KI-HARNESS-GOV-230](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/ideas/KI-HARNESS-GOV-230-knowledge-package-skill.md) | Knowledge package skill | ki-agentic-harness | cancel, idea on portable-specifications | unadopted triage, size l, Project on hold |
| [KI-HARNESS-REV-012](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/ideas/KI-HARNESS-REV-012-thoughtworks-radar-input.md) | Review ThoughtWorks Radar | ki-agentic-harness | cancel | the record itself says the weekly model-radar review HK-003 can carry a per-volume check; add it there, no record needed |
| [KI-TOOL-KI-CLI-149](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/ideas/KI-TOOL-KI-CLI-149-work-status-views-contract.md) | Work status views contract | tools-ki | cancel, idea on observatory | low priority; the text views of `ki work status` serve the Observatory today; a JSON schema is premature |
| [KI-TOOL-KI-CLI-168](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/ideas/KI-TOOL-KI-CLI-168-readable-chatgpt-project-acquisition.md) | Readable ChatGPT project acquisition | tools-ki | cancel, idea on knowledge-acquisition | unadopted triage, size l; the acquisition Project is finished |
| [KI-TOOL-KI-CLI-170](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/ideas/KI-TOOL-KI-CLI-170-guarded-source-retirement-design.md) | Guarded source retirement design | tools-ki | cancel, idea on knowledge-acquisition | nothing deletes sources today, so the guard has nothing to guard |
| [KI-TOOL-KI-CLI-171](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/ideas/KI-TOOL-KI-CLI-171-complete-acquisition-move-proof.md) | Complete acquisition move proof | tools-ki | cancel, idea on knowledge-acquisition | a prerequisite only for CLI-170's deletion, which is not wanted |
| [KI-TOOL-RIG-CORE-064](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/ideas/KI-TOOL-RIG-CORE-064-unmanaged-configuration-scan.md) | Rig manages app configuration | tools-rig | cancel, fold into CORE-072 | narrowed on 20 Oct to a recurring scan; CORE-072 now owns configuration touch points and can carry the scan as a line |

**Bulk decision:** "cancel bucket B as listed".

## C. Small and agent-doable tonight

No decision needed; each is `s`, or `m` with its Steps already written. Four suggested runs, one per repository.

| Record | Title | Repository | Disposition | Reason |
| --- | --- | --- | --- | --- |
| [KI-HARNESS-GOV-202](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-202-skill-area-stable-stats-badge.md) | Skill-area stable stats badge | ki-agentic-harness | run `harness-c` | size s, adopted 22 Oct; the badge and the viewer need one reconciling pass, then the generator change |
| [KI-OBSERVA-BRG-004](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-004-turn-feedback-sending-on.md) | Turn feedback sending on | apps-observatory.local | run `observatory-c` | size s; its hold waited on KI-HARNESS-GOV-219, which landed and is pruned; Kris already said "go ahead" on 19 Oct |
| [KI-TOOL-KI-CLI-160](https://github.com/knowledgeislands/tools-ki/blob/cf186ecf39791689145530f3be73341a4717a8dc/docs/roadmap/KI-TOOL-KI-CLI-160-work-status-routing-view.md) | Work status routing view | tools-ki | run `tools-ki-c` | size s; its shape was agreed under TOOLS-KI-SHAPES on 20 Oct and its predecessor CLI-158 landed |
| [KI-TOOL-RIG-CORE-068](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-068-replaced-pf-root-ruleset-bypass.md) | pf root ruleset bypass | tools-rig | run `rig-c`, first | priority high; Steps written; doctor reports `unknown` when NordVPN replaces root's ruleset; may run past an hour |
| [KI-TOOL-RIG-CORE-071](https://github.com/knowledgeislands/tools-rig/blob/4f006e3505c4e14c247b8f4a8b129ed8551547a4/docs/roadmap/KI-TOOL-RIG-CORE-071-firewall-exposure-wording.md) | Firewall exposure wording | tools-rig | run `rig-c`, with 068 | size s; the record asks to be merged into 068's doctor wording change |
| [KI-TOOL-RIG-CORE-069](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-069-dynamic-type-handler-fallback.md) | Dynamic-type handler fallback | tools-rig | run `rig-c` | size s, adopted under OVERNIGHT; terra evidence of 23 Oct gives the route |
| [KI-TOOL-RIG-CORE-070](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-070-handler-read-back-after-confirmation.md) | Handler read-back after confirmation | tools-rig | run `rig-c`, with 069 | size s; same resource and same fixtures as 069 |
| [KI-TOOL-RIG-CORE-073](https://github.com/knowledgeislands/tools-rig/blob/4f006e3505c4e14c247b8f4a8b129ed8551547a4/docs/roadmap/KI-TOOL-RIG-CORE-073-native-tool-absolute-path-fallback.md) | Native tool absolute-path fallback | tools-rig | run `rig-c` | size s; one lookup path change with a test stub |

Suggested runs: `rig-c` (068 + 071, then 069 + 070, then 073; one worktree, sequential commits), `harness-c` (202), `observatory-c` (BRG-004), `tools-ki-c` (160). Each delivers to awaiting review and leaves acceptance to Kris, under the standing local-only, explicit-path, no-prune rules. Adoption of the four triage records (070, 071, 073 and the `next` horizon of 202) is folded into "run bucket C".

**Bulk decision:** "run bucket C as listed".

## D. One decision from Kris

| Record | Title | Repository | Question | Recommended answer |
| --- | --- | --- | --- | --- |
| [KI-OBSERVA-APP-044](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md) | Instrument restructure decision | apps-observatory.local | Converge the fifteen tabs on the ten instruments under four jobs, with one redirect table for every old `?view=` address? | **Yes, converge** (high: Kris's "far too many sections" tonight and DESIGN-RESTRUCTURE a) on 19 Oct both say so). Council first as a pure rename, then Streams, then Workers; keep the lens until three consolidations have landed |
| [KI-OBSERVA-VIS-034](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-034-streams-instrument.md) | Streams instrument | apps-observatory.local | Same decision as APP-044: once converging, Streams is the first real consolidation (roadmap + work in flight) | **Release from hold and run** after APP-044's redirect table (high: Kris's DESIGN-WORK answer keeps Work beside it, so the shape is settled) |
| [KI-OBSERVA-VIS-045](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-045-workers-instrument.md) | Workers instrument | apps-observatory.local | Same decision: Workers folds Sessions and Automation into one view | **Release from hold and run** second (medium: VIS-028 and VIS-029 change how runs are read, so Workers reads what exists today and takes the cross-host view later) |
| [KI-OBSERVA-VIS-032](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-032-library-instrument.md) | Library instrument | apps-observatory.local | Same decision: Library folds knowledge bases and documents | **Release from hold, run third** (medium: no open design question, but less pressing than Streams and Workers; say "Later" if three runs tonight is too many) |
| [KI-PRINCIPAL-MOD-011](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-MOD-011-amend-work-model-assigned-package-cascade.md) | Amend work model cascade | ki-principal | Adopt into Now draft and plan the Enactment wording, or wait for the Valle Armonia pilot? (open query MOD-011-ADOPT) | **Adopt into Now draft, size m** (high: the harness already carries the decided model, so the canonical Work Process note and GDR-KI-PRINCIPAL-009 are behind today) |
| [KI-DESIGN-ART-002](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ART-002-art-licensing.md) | Art-licensing decision | ki-design | Record ownership, generator terms and style-reference risk for AI-generated brand art now, or defer with the tile set? | **Defer with KI-DESIGN-TIL-002 to Later** (medium: it only blocks TIL-002, which is xl and in bucket F; nothing produces brand art tonight). If Kris wants it closed, it is a one-run decision record |
| [KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md) | Tailnet-only listener firewall | tools-rig | terra is done (24 Oct); sol still needs its attended `rig apply --sudo`. Close on terra's evidence and treat sol's apply as a Rig operation, or keep in progress until sol is applied? | **Close on terra's evidence; sol's apply is an operation, not roadmap work** (medium: the code, tests and ADR are delivered; what remains is Kris at the machine, which a record cannot speed up). One pasteable command goes in the mac-studio-setup package when Kris is at sol |

**Bulk decision:** "take the recommended answer on every line of bucket D", or name the lines to change.

## E. Waits on a release or CI

| Record | Title | Repository | Disposition | Reason and local alternative |
| --- | --- | --- | --- | --- |
| [KI-TOOL-KI-CLI-125](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/ideas/KI-TOOL-KI-CLI-125-ki-release-contract.md) | KI release contract | tools-ki | cancel, idea on tools-ki | per-platform archives, checksums and signing serve only released installs; with every machine running `ki` from the linked checkout there is nothing to contract. Held to 16 Nov anyway |
| [KI-TECHNE-OPS-018](/Users/krisbrown/workspaces/knowledge-islands/ki-techne-harness/docs/roadmap/KI-TECHNE-OPS-018-converge-tools-through-rig.md) | Converge tools through Rig | ki-techne-harness | drop the release dependency, defer Later | inside the Focus (vega's workspace setup) but waits on "a Rig release containing CORE-051"; locally, vega's `converge.sh` can clone tools-rig at a pinned commit instead of installing a release. Not blocking anything |
| [KI-TECHNE-OPS-024](/Users/krisbrown/workspaces/knowledge-islands/ki-techne-harness/docs/ideas/KI-TECHNE-OPS-024-weekly-pin-bump.md) | Weekly pin bump | ki-techne-harness | cancel, idea on agent-host | a weekly job that chases newer releases of every tool pinned for the agent host; the Focus forbids unattended agents on the hosts and Kris has deprioritised releases. Bump pins by hand when vega is rebuilt |

**Bulk decision:** "drop the release dependencies in bucket E as listed".

## F. Genuinely larger: defer to Later

| Record | Title | Repository | Disposition | Reason |
| --- | --- | --- | --- | --- |
| [KI-HARNESS-GOV-227](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/ideas/KI-HARNESS-GOV-227-repository-storage-declarations.md) | Repository storage declarations | ki-agentic-harness | Later | a `.ki.toml` schema for MCP and XDG storage across `ki-repo` and `ki-engineering`; feeds only the Machine instrument, itself Later |
| [KI-HARNESS-OPS-009](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/ideas/KI-HARNESS-OPS-009-complete-ai-session-acquisition.md) | Incremental ChatGPT acquisition path | ki-agentic-harness | Later | an evaluation of the local-cache route; the acquisition Project is finished and nothing waits on it |
| [KI-OBSERVA-INT-003](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/ideas/KI-OBSERVA-INT-003-extensions-switchboard.md) | Two-way live-artifact adapter | apps-observatory.local | Later | size l; outbound transport and where the pair lives are both still open |
| [KI-OBSERVA-OPS-004](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/ideas/KI-OBSERVA-OPS-004-tailnet-read-only-appearance.md) | Tailnet read-only appearance | apps-observatory.local | Later | waits on the host network thread; Kris said "let's come back" on 19 Oct |
| [KI-OBSERVA-VIS-028](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/ideas/KI-OBSERVA-VIS-028-retire-sessions-readers.md) | Retire Sessions readers | apps-observatory.local | Later | retires the run-packet reader once Workers exists; sequence it after VIS-045 |
| [KI-OBSERVA-VIS-029](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/ideas/KI-OBSERVA-VIS-029-sessions-from-every-host.md) | Sessions from every host | apps-observatory.local | Later | size l; waits on a stable tailnet address per host |
| [KI-OBSERVA-VIS-038](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/ideas/KI-OBSERVA-VIS-038-machine-instrument.md) | Machine instrument | apps-observatory.local | Later | size l; its tool-storage phase waits on GOV-227 |
| [KI-DESIGN-ELE-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/ideas/KI-DESIGN-ELE-001-lit-ssr-spike.md) | Lit SSR spike | ki-design | Later | size l investigation with a cross-repository dependency question; the site ships without it |
| [KI-DESIGN-MAP-002](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/ideas/KI-DESIGN-MAP-002-isometric-renderer.md) | Isometric renderer | ki-design | Later | size l; needs the tile set |
| [KI-DESIGN-TIL-002](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/ideas/KI-DESIGN-TIL-002-ancient-tile-set.md) | Ancient tile set | ki-design | Later | size xl; blocked by ART-002 |
| [KI-MCP-M365-TOOL-011](/Users/krisbrown/workspaces/knowledge-islands/mcp-m365/docs/ideas/KI-MCP-M365-TOOL-011-judgment-verdict-hook.md) | Judgment verdict hook | mcp-m365 | Later, with hnr.email-routing | the nine mcp-m365 and two mcp-gsuite records are the email-routing rollout phases 2 to 4, held and owned by the HNR email-routing thread ("Email-routing records stay with hnr.email-routing") |
| [KI-MCP-M365-TOOL-012](/Users/krisbrown/workspaces/knowledge-islands/mcp-m365/docs/ideas/KI-MCP-M365-TOOL-012-judged-mail-recheck.md) | Judged mail re-check | mcp-m365 | Later, with hnr.email-routing | blocked by TOOL-011 |
| [KI-MCP-M365-TOOL-013](/Users/krisbrown/workspaces/knowledge-islands/mcp-m365/docs/ideas/KI-MCP-M365-TOOL-013-per-rule-hit-counts.md) | Per-rule hit counts | mcp-m365 | Later, with hnr.email-routing | phase 4 |
| [KI-MCP-M365-TOOL-014](/Users/krisbrown/workspaces/knowledge-islands/mcp-m365/docs/ideas/KI-MCP-M365-TOOL-014-routing-run-ledger.md) | Routing run ledger | mcp-m365 | Later, with hnr.email-routing | phase 4 |
| [KI-MCP-M365-TOOL-015](/Users/krisbrown/workspaces/knowledge-islands/mcp-m365/docs/ideas/KI-MCP-M365-TOOL-015-deduplicate-saved-attachments.md) | Deduplicate saved attachments | mcp-m365 | Later, with hnr.email-routing | small fix, but belongs to the same owner |
| [KI-MCP-M365-TOOL-016](/Users/krisbrown/workspaces/knowledge-islands/mcp-m365/docs/ideas/KI-MCP-M365-TOOL-016-thread-follow-skips-disposal-folders.md) | Thread-follow skips disposal folders | mcp-m365 | Later, with hnr.email-routing | Kris: "Keep, fix later" |
| [KI-MCP-M365-TOOL-017](/Users/krisbrown/workspaces/knowledge-islands/mcp-m365/docs/ideas/KI-MCP-M365-TOOL-017-size-the-hold-window.md) | Size the hold window | mcp-m365 | Later, with hnr.email-routing | Kris: "Accept, size later" |
| [KI-MCP-M365-TOOL-018](/Users/krisbrown/workspaces/knowledge-islands/mcp-m365/docs/ideas/KI-MCP-M365-TOOL-018-extract-the-routing-core.md) | Extract and distribute core | mcp-m365 | Later, with hnr.email-routing | ENGINE-HOME a) decided; the work is the HNR thread's |
| [KI-MCP-M365-TOOL-019](/Users/krisbrown/workspaces/knowledge-islands/mcp-m365/docs/ideas/KI-MCP-M365-TOOL-019-move-the-rule-specification.md) | Move the rule specification | mcp-m365 | Later, with hnr.email-routing | follows TOOL-018 |
| [KI-MCP-GSUITE-TOOL-008](/Users/krisbrown/workspaces/knowledge-islands/mcp-gsuite/docs/ideas/KI-MCP-GSUITE-TOOL-008-consume-the-routing-core.md) | Consume the routing core | mcp-gsuite | Later, with hnr.email-routing | needs TOOL-018 first |
| [KI-MCP-GSUITE-TOOL-009](/Users/krisbrown/workspaces/knowledge-islands/mcp-gsuite/docs/ideas/KI-MCP-GSUITE-TOOL-009-add-gmail-routing-report-mode.md) | Add Gmail routing report-mode | mcp-gsuite | Later, with hnr.email-routing | blocked by TOOL-008 |
| [KI-TOOL-KI-CLI-139](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/ideas/KI-TOOL-KI-CLI-139-ebu-sources-sync.md) | EBU sources sync | tools-ki | Later | size l; an HNR 5G-EMERGE need, not KI's |
| [KI-TOOL-KI-CLI-145](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/ideas/KI-TOOL-KI-CLI-145-thread-session-bindings-role.md) | Thread session bindings | tools-ki | Later | waits on GOV-199 phase 1 and a launch-style probe |
| [KI-TOOL-KI-CLI-157](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/ideas/KI-TOOL-KI-CLI-157-validator-parity.md) | Validator parity | tools-ki | Later | a shared fixture set between the harness checker and `ki work`; real drift risk, but the tools-burndown Project is on hold |
| [KI-TOOL-KI-CLI-169](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/ideas/KI-TOOL-KI-CLI-169-explicit-acquisition-failures.md) | Explicit acquisition failure outcomes | tools-ki | Later | the one acquisition record worth keeping: silent drops are a correctness fault |
| [KI-TOOL-RIG-CORE-072](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/ideas/KI-TOOL-RIG-CORE-072-application-configuration-touch-points.md) | Application configuration touch points | tools-rig | Later | adopted 24 Oct at Soon; size m with shaping still open; carries CORE-064's scan |
| [KI-TOOL-RIG-CORE-074](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/ideas/KI-TOOL-RIG-CORE-074-host-specific-software-retirement.md) | Host-specific software retirement | tools-rig | Later | triage; needs host/profile identity settled with fixtures first |
| [KI-TOOL-MGIT-CLI-031](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/ideas/KI-TOOL-MGIT-CLI-031-learn-command-shapes.md) | Learn command shapes | tools-mgit | Later | already at the `future` horizon with six open design questions |

**Bulk decision:** "defer bucket F to Later". If Kris wants F smaller still, the eleven email-routing records can be cancelled in KI and recaptured by the HNR thread when it resumes.

## Open queries in KI work packages

| Package | Open | Parked | Blocks a roadmap record |
| --- | --- | --- | --- |
| [ki.ways-of-working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/queries.md) | 34 | 0 | MOD-011-ADOPT blocks KI-PRINCIPAL-MOD-011 (answered by bucket D). MGIT-CACHE-SCOPE and MGIT-CACHE-FAILED block only the `mgit-cache.md` design note, no record |
| [ki.agent-host](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.agent-host/queries.md) | 1 | 2 | CLI006-PLAN names KI-TOOL-TECHNE-CLI-006, which tools-techne no longer holds (its roadmap is empty); the query is stale and can be parked or struck |
| [ki](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/queries.md) (State of play) | 0 | 22 | six parked ACCEPT-* queries are bucket A; MAIL-MCP-HOME is bucket F's email-routing line |
| [ki.mac-studio-setup](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.mac-studio-setup/queries.md) | 0 | 9 | FW-LIVE is CORE-047's sol apply (bucket D); RIG-TRIAGE is answered by this pack |
| [ki.tools-burndown](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown/queries.md) | 0 | 1 | none |
| ten other packages | 0 | 0 | none |

No other KI repository holds a `+/_WORK/*/queries.md`.

## Releases and CI

**Where things stand at 00:05 GMT.**

- Every KI repository's `ci.yml` installs the _released_ `ki` and runs `ki repo audit --repo .`; twenty repositories pin `v0.13.0` (ten in `.github/ki-version`, ten inline). The local `ki` is 0.14.1 from the linked tools-ki checkout.
- Thirteen repositories are red with DESIGN-2 only: released 0.13.0 looks for `tooling/boundaries`, the repositories moved to `tooling/depcruise`. Harness and tools-ki mains are green.
- The v0.14.0 release failed on the two darwin builds. v0.14.1 is tagged and its Release run is in flight now under `wow-rel-0141` (linux-x64 and darwin-arm64 green, darwin-x64 re-running); `wow-tap-log` is queued behind it. If it publishes, `repository_dispatch` fires the daily pin-bump receivers in ten repositories and the tap's release proposer, which then open bot pull requests.
- Harness `d174adbc` tonight made the commit hook check-only and moved the full `ki repo audit` to CI. Pushes to `main` already bypass the branch rules, so CI blocks nothing today; the tap, pin and website release receivers are the only automation that acts on it.
- Records waiting on a release or CI: the three in bucket E. No record waits on a red check.

**Options, recommended first.**

a) **Disable the release and CI workflows for now** (recommended, confidence high: Kris's own words tonight, and nothing is blocked by CI that the local audit does not catch). Switch `ci.yml` in the thirteen red repositories to `workflow_dispatch` only, and the same for `update-ki-pin.yml` in ten repositories, `propose-tool-releases.yml` and `update-tool-release.yml`, by one commit per repository; let `wow-rel-0141` finish or stop it, and do not bump the twenty pins. Lost: the fleet-wide catch of cross-machine link breaks (as KI-LINK-2 did on 26 Oct) and toolchain drift, the daily pin proposals, and the home that `d174adbc` just gave the full audit. Replace it with one line in every brief: run `ki repo audit --repo .` with the linked `ki` before the final commit.

b) **Keep CI, make it run the linked tools** (confidence medium: one template change, but it re-couples every repository's CI to tools-ki main). Replace "Install released KI" with a checkout of tools-ki `main` and `bun link`; the DESIGN-2 red clears without a release, and the pin files, tap and release receivers go dormant. Costs one fan-out run of twenty repositories tonight.

c) **Finish v0.14.1 and bump the pins** (confidence low: it is the release treadmill Kris wants off). The release is minutes from done; the receivers then open ten pull requests to merge, and the fleet goes green on 0.14.1 until the next drift.

**Decision line:** "disable the workflows as in option a", "run the linked tools in CI as in option b", or "finish the release as in option c".
