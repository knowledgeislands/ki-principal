---
id: ki.agent-host
level: project
title: 'KI > Techne > Agent host'
project: agent-host
theme: techne
worker: agent
supervisor: owner
state: on-hold
hold:
  reason: paused
  release: the Techne Programme Hold lifting
since: 2026-10-18T03:30:38Z
received: null
beat: null
mark: 2026-10-15T14:59:23Z
created_at: 2026-10-07T09:05:00Z
---

# ki.agent-host

## Next steps

2026-10-15: the state-of-play territory hold set this checkpoint's frontmatter to drained, matching the thread's own drain recorded under Current state; the next steps are those already in this checkpoint.

**Messages from Master: state-of-play** - the receiving thread acts on each line, then removes it.

- 2026-10-16 · CI-RED-PRINCIPAL · Fnd: tools-burndown, on Kris's decision of 16 October: `ki repo audit` fails these reports in `+/_WORK_REVIEW/ki.agent-host/`, for this thread to fix in its own folder: cli133-plan (PMO-7). PMO-7 wants every full record identifier in prose linked to its local file, or as `<ID> (pruned)` to the GitHub file at its last revision; NOTE-1a reads a report's opening `---` rules as unterminated frontmatter, which tools-burndown cleared by putting a `<!-- markdownlint-disable-file MD041 -->` line above the unchanged rules.
- 2026-10-16 · THREADS-CLEAR · KI Model: ways-of-working, on Kris's decision of 15 October: "Each owning thread clears its own folder at its next mark, moving scratch to tmp/, homing or removing tracked work products and moving briefs to the state folder, told through its inbox by this thread." Apply it to `+/_WORK_REVIEW/ki.agent-host/` against the closed list now in [ki-pmo's Tidying the thread folder](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-pmo/references/standards-pmo.md) and the ki-delegation [Run packet](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-delegation/references/standards-background-runs.md) (ki-agentic-harness `065bbd5b`, on `origin/main`), in Kris's words: "A thread folder holds a closed list, decisions.md and <name>.report.md only; briefs live in the state folder, work products in their owning home, temporary output in the temporary location." · detail: [ways-of-working decisions log](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/decisions.md)
- 2026-10-17 · PMO-7-BACKLOG · Master: state-of-play, on Kris's decision of 15 October: "Each thread relinks or deletes its own reports at its next mark under the thread-tidy rule, and the state-of-play thread tells each one so." Apply it to this thread's own folder, [`+/_WORK_REVIEW/ki.agent-host/`](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK_REVIEW/ki.agent-host/) · detail: [ways-of-working decisions log](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/decisions.md)

On sol: re-bootstrap from this checkpoint, then wait on Kris for CLI-133-DELIVER. Until KI-TOOL-KI-CLI-133 is fixed, remove re-copied retired reports by explicit path after any `ki agent decide`. Once KI-TOOL-TECHNE-CLI-009 is delivered, ki-techne-harness adds the matching optional recipe parameter. Resume line: `Resume Techne: agent-host on sol from its checkpoint under current ki-pmo and ki-delegation since 2026-10-15T14:59Z: re-bootstrap, read the parked queries, take stock, restart authorised work, then banner.`

## Messages

- MIGRATED - this file was `+/_CHECKPOINTS/techne.agent-host.md` until the work migration of 2026-10-18. At your next mark, cut it to next steps, Messages and the tags of parked queries, each linked to its report; move anything else to its durable home, then remove this line.

## Parked

For Kris:

- **CLI-133-DELIVER:** [KI-TOOL-KI-CLI-133](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-133-retired-reports-come-back.md) is Ready (reproduced against the installed `ki`; fix: adopt a state file only if Git has never held that path in the thread folder). Recommended: deliver on Sonnet through ki-implement, stop at Awaiting review, commit and push, no release. Report: `+/_WORK_REVIEW/ki.agent-host/cli133-plan.report.md`. [KI-TOOL-TECHNE-CLI-009](/Users/krisbrown/workspaces/knowledge-islands/tools-techne/docs/roadmap/KI-TOOL-TECHNE-CLI-009-tailscale-oauth-binding-field.md) is adopted as deliver at horizon next (Decision 64).

Handoffs:

**STORE-REPAIR (with tools-burndown):** Kris approved planning for [KI-TOOL-KI-CLI-126](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-126-unavailable-store-breaks-repair.md). The record is already Ready / Now in ways-of-working under CI-STORE. Please confirm the current ways-of-working tools-ki writer, or name the agreed writer and slot. Tools-burndown will preserve the current record and remain read-only until agreement; no rollback, duplicate planner, implementation or host operation is requested.

- **DEV-MODE** (with state-of-play): Kris chose that Rig owns `rig dev local|release <tool>`; handed to state-of-play on 2026-10-14, which holds it with RIG-LINK for Kris's decision under the burn-down rule.
- **RIG-LINK** (with state-of-play): `~/.local/bin/rig` links to the retired `~/workspaces/kit/knowledgeislands/tools-rig` path and is broken; it belongs to the Rig thread.
- **Firewall** (with `mac-studio-bootstrap`): KI-TOOL-RIG-CORE-047 (macOS) and KI-TOOL-RIG-CORE-051 (Linux nftables) are delivered and awaiting review there; nothing is planned or implemented here. The Mac Studio owned-host exemption is KI-ARCADIA-GOV-033 in that thread.

Held:

- [KI-TECHNE-OPS-018](/Users/krisbrown/workspaces/knowledge-islands/ki-techne-harness/docs/roadmap/KI-TECHNE-OPS-018-converge-tools-through-rig.md) (converge host tools through Rig): on hold per its record until Kris releases it.
- The vega host name in `status.sh`: held until Kris releases it.

Parked:

- Parked 2026-10-09: personal harness instructions - Kris wants the Claude and Codex instructions to become skills from a personal harness, leaving thin `CLAUDE.md` and `AGENTS.md`; raise in state-of-play when picked up.
