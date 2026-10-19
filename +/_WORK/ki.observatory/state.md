---
id: ki.observatory
state: handoff-to-supervisor
since: 2026-10-19T19:05:00Z
received: 2026-10-19T19:04:00Z
beat: null
mark: 2026-10-19T18:02:00Z
method_read: 2026-10-19T18:02:00Z
---

# ki.observatory state

## Now

- With Kris since 20:05 BST on 19 October; marked at 19:02 BST.
- Nothing is running; the open queries are in `queries.md`, all blind-reviewed.
- Received obs-pies-tables at 19:51 BST: KB-PRINCIPAL-046 in personal-principal and HNR-PRINCIPAL-KM-018 in hnr-principal carry PIES-TABLE-BARS, both in triage and committed locally, unpushed.
- Received obs-condition at 19:52 BST: KI-HARNESS-GOV-223 (maturity scale and `.ki.toml` key) and KI-TOOL-KI-CLI-159 (`ki` exposes maturity and health), both triage, committed locally in ki-agentic-harness and tools-ki, unpushed. Its MATURITY-SCALE query is reviewed (review prefers three levels) and in `queries.md`.
- Received obs-accept-answers at 20:03 BST: four records accepted, seven merged, three triage records captured (KI-OBSERVA-BRG-005, KI-OBSERVA-BRG-006, KI-OBSERVA-VIS-043), answers folded in, ten pruned; 34 to 27 records; five local commits in apps-observatory.local.
- Kris pushes ki-principal and apps-observatory.local himself (PUSH-KRIS).
- Run reports sit in `~/.local/state/ki/agents/observatory/`.

## Next steps

1. On Kris's answers: MATURITY-SCALE to KI-HARNESS-GOV-223; OVERLAY-COMMITTED a) to a harness record and KI-OBSERVA-VIS-042; LARGE-SCREEN-EXISTING to KI-OBSERVA-APP-044.
2. Four triage records await a later merge decision: KI-OBSERVA-VIS-029, KI-OBSERVA-VIS-032, KI-OBSERVA-VIS-033, KI-OBSERVA-VIS-034.
3. Four done records (KI-OBSERVA-APP-042, KI-OBSERVA-VIS-023, KI-OBSERVA-VIS-024, KI-OBSERVA-BRG-002) stay until their peer links and BRG-002's frozen figure are re-pointed.
4. `ki work status` (installed `ki` 0.11.4) is blind to five-file packages until ki.tools-burndown changes the tools-ki reader.
5. Each design convergence step needs Kris's go (DESIGN-APPLY); the design thread's answers come back through ki-design's `-/observatory-handoff/`.
6. Diagram conversion records in six other repositories are theirs to deliver; legal-principal's gantt stays as Mermaid until ki.timelines lands (DIAGRAM-GANTT).
7. `ki repo roadmap promote` refuses on an unrelated size field in KI-OBSERVA-APP-045; set horizons by hand until fixed.

## Held

- KI-OBSERVA-VIS-029 and KI-OBSERVA-OPS-004, until the Host network Project's unit 4 opens.
