---
id: ki.observatory
state: with-supervisor
since: 2026-10-19T19:40:00Z
received: 2026-10-19T19:13:00Z
beat: null
mark: 2026-10-19T18:02:00Z
method_read: 2026-10-19T18:02:00Z
---

# ki.observatory state

## Now

- With Kris since 20:40 BST on 19 October; NARROW-DECLARE answered a) at 20:40 BST, needing no change; no authorised work remains; marked at 19:02 BST. Nothing is running.
- Received obs-declare-review at 20:13 BST: the review agrees with keeping the declaration, so NARROW-DECLARE goes to Kris at high confidence.
- Received obs-answers-2 at 20:12 BST: KI-OBSERVA-APP-044, KI-OBSERVA-BCN-008, KI-OBSERVA-VIS-030 and KI-OBSERVA-VIS-031 reworded to large screens first, not only, with the narrow rule and test kept; KI-OBSERVA-VIS-042 carries OVERLAY-SYNC, depending on KI-HARNESS-GOV-224; commit 9f56976, local.
- Received obs-viewer-sync at 20:11 BST: KI-HARNESS-GOV-224 (diagram viewer receipts, triage) captured and KI-HARNESS-GOV-223 set to `founding`, `growing`, `settled`, `thriving`; three local commits in ki-agentic-harness, unpushed.
- Received obs-pies-tables at 19:51 BST: KB-PRINCIPAL-046 in personal-principal and HNR-PRINCIPAL-KM-018 in hnr-principal carry PIES-TABLE-BARS, both in triage and committed locally, unpushed.
- Received obs-condition at 19:52 BST: KI-HARNESS-GOV-223 (maturity scale and `.ki.toml` key) and KI-TOOL-KI-CLI-159 (`ki` exposes maturity and health), both triage, committed locally in ki-agentic-harness and tools-ki, unpushed. Its MATURITY-SCALE query is reviewed (review prefers three levels) and in `queries.md`.
- Received obs-accept-answers at 20:03 BST: four records accepted, seven merged, three triage records captured (KI-OBSERVA-BRG-005, KI-OBSERVA-BRG-006, KI-OBSERVA-VIS-043), answers folded in, ten pruned; 34 to 27 records; five local commits in apps-observatory.local.
- Kris pushes ki-principal and apps-observatory.local (PUSH-KRIS).
- Run reports sit in `~/.local/state/ki/agents/observatory/`.

## Next steps

1. Awaiting Kris's next steer; the items below wait on their own decisions or other threads.
2. Four triage records await a later merge decision: KI-OBSERVA-VIS-029, KI-OBSERVA-VIS-032, KI-OBSERVA-VIS-033, KI-OBSERVA-VIS-034.
3. Four done records (KI-OBSERVA-APP-042, KI-OBSERVA-VIS-023, KI-OBSERVA-VIS-024, KI-OBSERVA-BRG-002) stay until their peer links and BRG-002's frozen figure are re-pointed.
4. `ki work status` (installed `ki` 0.11.4) is blind to five-file packages until ki.tools-burndown changes the tools-ki reader.
5. Each design convergence step needs Kris's go (DESIGN-APPLY); the design thread's answers come back through ki-design's `-/observatory-handoff/`.
6. Diagram conversion records in six other repositories are theirs to deliver; legal-principal's gantt stays as Mermaid until ki.timelines lands (DIAGRAM-GANTT).
7. `ki repo roadmap promote` refuses on an unrelated size field in KI-OBSERVA-APP-045; set horizons by hand until fixed.

## Held

- KI-OBSERVA-VIS-029 and KI-OBSERVA-OPS-004, until the Host network Project's unit 4 opens.
