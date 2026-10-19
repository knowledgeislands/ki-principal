---
id: ki.observatory
state: with-worker
since: 2026-10-19T18:02:00Z
received: 2026-10-19T18:02:00Z
beat: null
mark: 2026-10-19T18:02:00Z
method_read: 2026-10-19T18:02:00Z
---

# ki.observatory state

## Now

- Sent back to the worker and marked at 19:02 BST on 19 October; the work package was re-read and its migrated description, Goals and Scope confirmed.
- obs-reader is running in apps-observatory.local: the Observatory reads both work-folder shapes (WORK-PACKAGE-READER from ki.ways-of-working).
- The Observatory service serves KI-OBSERVA-BRG-003, Awaiting review.
- Run reports sit in `~/.local/state/ki/agents/observatory/`.

## Next steps

1. When obs-reader reports, receive it and return the Work Instrument confirmation to ki.ways-of-working's `messages.md`, which is blocked on it.
2. KI-OBSERVA-BRG-003 is Awaiting review (BRG-003-REVIEW); KI-OBSERVA-VIS-030 is ready to promote to Next.
3. In triage: KI-OBSERVA-APP-045, KI-OBSERVA-VIS-042, KI-OBSERVA-OPS-003, and KI-TOOL-KI-CLI-154 in tools-ki.
4. Each design convergence step needs Kris's go (DESIGN-APPLY). The design thread's answers come back through ki-design's `-/observatory-handoff/`; the Observatory's handoff is apps-observatory.local `-/design-handoff/INSTRUCTION.md`.
5. Diagram conversion: originals stay collapsed beneath each Archify replacement until Kris signs off; the conversion records in the six other repositories are theirs to deliver. legal-principal's gantt stays as Mermaid until ki.timelines lands (DIAGRAM-GANTT).
6. ki-principal holds this work's commits unpushed among other sessions' (PUSH-STACKED); pushing stays with Kris.
7. `ki repo roadmap promote` refuses on an unrelated size field in KI-OBSERVA-APP-045, so set horizons by hand until fixed; `ki agent note` does not exist in this `ki`.

## Held

- KI-OBSERVA-VIS-029 and KI-OBSERVA-OPS-004, until the Host network Project's unit 4 opens.
