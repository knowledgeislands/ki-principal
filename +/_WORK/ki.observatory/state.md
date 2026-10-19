---
id: ki.observatory
state: with-worker
since: 2026-10-19T18:21:00Z
received: 2026-10-19T18:21:00Z
beat: null
mark: 2026-10-19T18:02:00Z
method_read: 2026-10-19T18:02:00Z
---

# ki.observatory state

## Now

- Sent back to the worker and marked at 19:02 BST on 19 October; the work package was re-read and its migrated description, Goals and Scope confirmed.
- Received obs-reader at 19:13 BST: KI-OBSERVA-VIS-025 now reads both work-folder shapes and is Awaiting review, committed locally; the Work Instrument confirmation was returned to ki.ways-of-working.
- Received obs-burndown at 19:20 BST: KI-OBSERVA-APP-043 pruned (35 to 34 records); four done records kept for peer links; one commit, 837ee05, unpushed in apps-observatory.local. Its queries BURNDOWN-ACCEPT and BURNDOWN-TRIAGE are in blind review (obs-query-review, Codex) before they go to Kris; the report is at `~/.local/state/ki/agents/observatory/obs-burndown.report.md`.
- The Observatory service serves KI-OBSERVA-BRG-003, Awaiting review.
- Run reports sit in `~/.local/state/ki/agents/observatory/`.

## Next steps

1. When obs-query-review reports, apply agreement or disagreement to BURNDOWN-ACCEPT and BURNDOWN-TRIAGE, copy them into `queries.md` and bring them to Kris.
2. When obs-reader reports, receive it and return the Work Instrument confirmation to ki.ways-of-working's `messages.md`, which is blocked on it.
3. KI-OBSERVA-BRG-003 is Awaiting review (BRG-003-REVIEW); KI-OBSERVA-VIS-030 is ready to promote to Next.
4. In triage: KI-OBSERVA-APP-045, KI-OBSERVA-VIS-042, KI-OBSERVA-OPS-003, and KI-TOOL-KI-CLI-154 in tools-ki.
5. Each design convergence step needs Kris's go (DESIGN-APPLY). The design thread's answers come back through ki-design's `-/observatory-handoff/`; the Observatory's handoff is apps-observatory.local `-/design-handoff/INSTRUCTION.md`.
6. Diagram conversion: originals stay collapsed beneath each Archify replacement until Kris signs off; the conversion records in the six other repositories are theirs to deliver. legal-principal's gantt stays as Mermaid until ki.timelines lands (DIAGRAM-GANTT).
7. ki-principal holds this work's commits unpushed among other sessions' (PUSH-STACKED); pushing stays with Kris.
8. `ki repo roadmap promote` refuses on an unrelated size field in KI-OBSERVA-APP-045, so set horizons by hand until fixed; `ki agent note` does not exist in this `ki`.

## Held

- KI-OBSERVA-VIS-029 and KI-OBSERVA-OPS-004, until the Host network Project's unit 4 opens.
