---
id: ki.ways-of-working
level: project
title: 'KI > Model > Ways of working'
project: ways-of-working
theme: model
worker: agent
supervisor: owner
state: handoff-to-supervisor
since: 2026-10-19T06:59:31Z
received: 2026-10-18T19:20:01Z
beat: null
mark: 2026-10-18T19:20:01Z
created_at: 2026-10-09T20:58:00Z
---

# ki.ways-of-working

## Next steps

Sent to Kris at 07:59 BST on 19 October. Every run Kris authorised on 18 and 19 October has reported; reports sit in `~/.local/state/ki/agents/ways-of-working/`.

1. Nothing is running.
2. With Kris: CLI-150-REVIEW (KI-TOOL-KI-CLI-150 at Awaiting review), BIOME-DRIFT (cli150-deliver) and KI-RELEASE-NEXT.
3. Kris is on: Rig upgrade on Terra and Sol, then a live-acceptance run for KI-TOOL-RIG-CORE-042 and -047; the mgit hands-on check, then MGIT-RELEASE.
4. KI-TOOL-KI-CLI-150 step 2 is done: this work's common rules and queued briefs name the state-folder report path; reports no longer go into this folder. cli150-deliver's before-copies stay in its temporary folder as the restore path until acceptance, so `ki agent close` waits.
5. At the next mark: recheck ki-principal CI (CI-RED-REST, waiting on ki.chezmoi and ki.observatory) and ki-agentic-harness CI (KI-HARNESS-GOV-210 links); check whether desk-kit is already closed.
6. Outstanding, not this work's: DESK-CAM with Mac Studio setup; KI-HARNESS-GOV-219 in triage; pre-existing CI red in apps-observatory.local, mcp-m365, tools-mgit and ki-techne-harness; acquire-intake's ACQUIRE-DECISIONS-LINKS Messages line.

## Messages

- 2026-10-19 08:00 BST · SIZE-PRIORITY · KI > Foundations > Tools burndown: Kris, 19 October: "work should have a size and a priority, even if its horizon isn't now or next", and answered SIZE-PRIORITY a) to hand you the standard change. Findings: no standard defines `priority` or `size`; `horizon` has been the only ordering signal since your PRIORITY-FIELD answer of 15 October (ki-principal `b4a2306`, `c275d26`; ki-agentic-harness `45bbaea6`), and triage, done and cancelled records carry none; tools-ki `src/core/work/items.ts` warns on `priority` as unknown (`6aa676a0`); no size field has ever existed; none of the estate's 367 records carries either, the last five being legal-principal LGL-PRINCIPAL-EVD-001 to -004 and LGL-PRINCIPAL-OPS-018 (high, medium, medium, low, medium), which Tools burndown is restoring by revert; [GDR-KI-PRINCIPAL-009](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/GDR-KI-PRINCIPAL-009-the-work-model.md) is silent on both. Proposed, for you to settle: `priority` (high, medium, low) and `size` (s, m, l, xl) required on every record from capture whatever its horizon, defined for both adapters in the [work-item format](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-work-roadmap/references/standards-work-item-format.md) and the `ki-work` crosswalk, values set by the owning repository; a Governance Decision Record reversing PRIORITY-FIELD; a tools-ki follow-up to stop warning on `priority` and warn, then fail, on a missing field after a migration window.

## Parked

- Held: PAPERCLIP-REQ, until Wave F. Waves A to D and F, re-anchoring, the thread status line, the inbox channel and messaging follow the pilot's lessons.
- Parked 2026-10-09: a gradual move from Obsidian-style to GitHub-flavoured Markdown, starting with a front-matter field declaring a note's flavour.
