---
id: ki.ways-of-working
level: project
title: 'KI > Model > Ways of working'
project: ways-of-working
theme: model
worker: agent
supervisor: owner
state: with-worker
since: 2026-10-18T03:30:38Z
received: null
beat: null
mark: 2026-10-17T21:34:13Z
created_at: 2026-10-09T20:58:00Z
---

# ki.ways-of-working

## Next steps

**Pick-up - mark 2026-10-17T21:34:13Z (22:34 BST)**

- **Status:** busy. migrate-phase1 is running phase 1 of the work migration in ki-agentic-harness, after Kris answered MIGRATION-REVIEW (confident items to `+/_WORK/`, the rest to `+/_WORK_REVIEW/`), SKILL-NAMES (keep the names for now; revisit in the skills audit), TITLE-THEME, WORK-THEME-SLUGS, TARGET-GLYPH (👤 for every target) and MIGRATION-LAUNCH on 18 October, with most territories put on hold for the run. Open: RUN-SHAPE, which takes in PHASE2-OWNER: whether this thread organises everyone's move while tools are down, including tools-ki, its release and other projects' checkouts. The work model is settled in [GDR-KI-PRINCIPAL-009](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/GDR-KI-PRINCIPAL-009-the-work-model.md) and the [Work Process](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Processes/Work Process/Work Process.md>) note. A skills audit follows once the work model is finished (Kris, 18 October).
- **Resume:** `Resume KI > Model > ways working under current ki-pmo and ki-delegation since 2026-10-17T21:34:13Z: re-bootstrap, mark, fresh summary with carried-forward open points, take stock, restart authorised work, then banner.`
- **Next steps, in order:** see migrate-phase1 through; on RUN-SHAPE, run phase 2 with the KI-TOOL-KI-CLI-127 work-status handoff (in `settle-model.report.md`) to the tools burndown thread; Parked: WORKER-CLI, Kris's idea of 18 October to rename `ki agent` to `ki worker`, offered to the tools burndown thread with phase 2; Personal > SoP handoff (ACT-WORK); HARNESS-ACCEPT sitting (KI-HARNESS-GOV-195, -198, -203, KI-HARNESS-OPS-005); SYNC-GUARD's KI-HARNESS-GOV-189 amendment; QUIET-HOOK; AREAS-DISPATCH.

**Messages** - the receiving thread acts on each line, then removes it.

- 2026-10-18 · FIRST-STEP · Master: state-of-play, carrying RUN-HYGIENE from ways of working's READY of 17 October: "each thread fixes its checkpoint form and adds role on its FIRST-STEP line at restart". Before launching work, bring this checkpoint to the current ki-checkpoint and ki-pmo form; its `role` is already set. Then, for HARNESS-ACCEPT, present KI-HARNESS-GOV-195, KI-HARNESS-GOV-198, KI-HARNESS-GOV-203 and KI-HARNESS-OPS-005 to Kris in one ki-accept sitting after the restart, with the KI-HARNESS-GOV-203 30-day stale threshold put to Kris there · [restart report](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/ways-of-working/restart.report.md)
- 2026-10-14 · AREAS-DISPATCH · Two ideas for evaluation are added to the [Ways of working Project note](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) Notes: agent-advertisement fields in the run-events contract (with a `--json` live-threads listing asked of tools-ki), and acting on token economics (usage and a `limit` stop reason on run events, a fallback ladder per model purpose in ki-tokenomics from Kris's "change them to claude-opus-5-5 at their same effort, at least until the next reset", and a concurrency gate read from account windows); placement rests on Kris's open OBS-MERGE and NEW-AREAS · detail: [areas-tokens report (deleted)](https://github.com/knowledgeislands/ki-principal/blob/70fa1e63b4afc56129c4d9a1c5ab41c244502793/+/_THREADS/state-of-play/areas-tokens.report.md)
- 2026-10-14 · SYNC-GUARD · Kris: fold "level before resume and at every mark" into [KI-HARNESS-GOV-189](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-189-move-thread-between-hosts.md) (mgit fetch, then mcp-git-audit ahead/behind, at session start, every mark and before leaving a host, with [behind] and [unpushed] footer items); a tools-ki `ki repo level` record only if that proves too slow · detail: [sync-telemetry report](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/sync-telemetry.report.md)

Handover for a fresh agent taking this thread:

- Re-bootstrap: read this checkpoint and ki-pmo, run `/Users/krisbrown/workspaces/knowledge-islands/tools-ki/bin/ki agent status ways-of-working`, read the tail of the [decisions log](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/decisions.md), then give the Re-bootstrap report. On another host, first fetch and level ki-principal, ki-agentic-harness and tools-ki, since the state folder and run history do not travel. The restart prompt is the pick-up block's resume line, verbatim.
- Launch pattern: `/Users/krisbrown/workspaces/knowledge-islands/tools-ki/bin/ki agent launch --rules push ways-of-working <name> <workdir> <prompt> --runtime claude --model claude-opus-5-5 --effort medium`, the prompt built from a task body followed by this `Rules:` block, copied verbatim from the old host's `svg-extract.md` because the state folder does not travel (set the trailer to the model actually launched):

  ```text
  Rules:

  - Never `--no-verify` or force-push.
  - Do not edit any checkpoint, `Admin`, `Pillars` or `Resources`.
  - Do not read or print secrets.
  - No package installs.
  - If a file you need is dirty from another session, leave it and name it.

  Commit per repository as a Conventional Commit, explicit-path staging, trailer `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>`; then `git pull --rebase` and push only if fast-forward, otherwise report.

  **Durability:** where you cite an owner decision, quote its words inline. A local decision number is not enough.

  **Report** in the owner-report format set in `ki-delegation`'s Reporting section, linking every record by its full identifier via verified absolute paths.

  Do not use background subagents. Never end your session while waiting.
  ```

- Push only this thread's own commits: those touching `+/_WORK/ki.ways-of-working/` or this checkpoint, or made by its agents. If other sessions' commits sit beneath, hold and ask Kris. Never autostash, reset shared `main` or force-push.
- Kris's layout session owns `docs/diagrams/` in ki-agentic-harness and the dirty harness files; leave them alone.

Then:

1. Give the rest summary in full, with every open question above and the reply block.
2. Act on Kris's answers; AREAS-REFRESH is unblocked now the harness is pushed, and AREAS-OVERTAKE settles IDEA-STAGE and IDEA-CAP together.
3. Tell state-of-play when IDEA-STAGE, IDEA-CAP and REGISTRY-RECORD are answered, and raise SOP-DROPPED with it.
4. Remove the acted-on Master messages at the top of this checkpoint.
5. Prepare the [KI-TOOL-KI-CLI-130](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-130-skill-generated-surfaces.md) review packet; offer [KI-PRINCIPAL-ECO-014 (pruned)](https://github.com/knowledgeislands/ki-principal/blob/5c1f2279cfe0627d25becae76a6ce81ed8cf397d/Streams/Roadmap/KI-PRINCIPAL-ECO-014-decision-citation-and-run-folder-sweep.md) for pruning.
6. Pilot [KI-PRINCIPAL-ECO-013](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-ECO-013-pmo-extraction-pilot.md): run test 1 on Codex, score tests 2 and 3, hand to `ki-accept`; then [KI-TOOL-KI-CLI-123](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-123-agent-run-events.md) and [KI-HARNESS-GOV-175](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-175-delegation-run-events.md).
7. Hold the report-shape review around 21 October, logging any tweak for it and building none before; take rumdl 0.2.79 around 23 October; consider Archify 3.1.0.

## Messages

- MIGRATED - this file was `+/_WORK/ki.ways-of-working/work.md` until the work migration of 2026-10-18. At your next mark, cut it to next steps, Messages and the tags of parked queries, each linked to its report; move anything else to its durable home, then remove this line.

## Parked

- None open. Kris answered the 16 October queries, regrouped in the [restart design report](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/ways-of-working/restart.report.md) as RESTART-AGREE, RUN-HYGIENE, TOOLS-PUSH, HARNESS-ACCEPT, CHEZMOI-APPLY, SHAPE-AGREE, DIAGRAMS-EXPORT and IDEAS-ROOTING, with option a) at 22:50 BST on 17 October, with QUIET-GATE, QUIET-STYLE, QUIET-HOOK, ACT-HOME, ACT-THREAD, ACT-NAMES and ACT-WORK (decisions log); STATE-AGREE, IDENTITY-NEXT and NAMING folded into them. Their follow-ons are the pick-up block's next steps. The thread-states design will bring new queries.
- Answered on 15 October and held in the decisions log, their reports deleted: DEPS-HOLD, PMO-7-BACKLOG, AREAS-REFRESH, RECORD-NAME, THREADS-CONTENT, THREADS-TMP-HOME, THREADS-TELL, THREADS-CLEAR, IDEA-STAGE, IDEA-CAP, REGISTRY-RECORD, PAUSE-CONDITION, PRIORITY-FIELD, STREAMS-INDEX, SOP-DROPPED, HEADING-LASTING and AREAS-OVERTAKE. Overtaken: PUSH-OTHERS, PUSH-CARRY, PUSH-LINKS, CHECKPOINT-PUSH, CHECKPOINT-LINKS and ECO014-BRIEF.
- Held: PAPERCLIP-REQ, until Wave F. Waves A to D and F, re-anchoring, the thread status line, the inbox channel and messaging follow the pilot's lessons.
- Parked 2026-10-09: a gradual move from Obsidian-style to GitHub-flavoured Markdown, starting with a front-matter field declaring a note's flavour.
