---
id: ki.observatory
level: project
title: 'KI > Model > Observatory'
project: observatory
theme: model
worker: agent
supervisor: owner
state: with-worker
hold: null
since: 2026-10-19T00:00:00Z
received: 2026-10-19T00:00:00Z
beat: null
mark: 2026-10-18T19:20:27Z
created_at: 2026-10-13T23:50:00Z
---

# ki.observatory

## Next steps

- Received from Kris and marked 2026-10-18T19:20:27Z (20:20 BST).
- obs-mermaid done: Mermaid 12.2.0 and its notices landed in apps-observatory.local as `58efa99`, gate passed (browser smoke skipped, no Playwright Chromium), pushed. Service restarted 20:29 BST under PUSH-ALL; page answers.
- [KI-OBSERVA-BRG-002](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-002-capture-feedback.md) is Ready; its first real send waits on [KI-HARNESS-GOV-219](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-219-feedback-work-folder-kind.md).
- With Kris: review [KI-OBSERVA-VIS-023](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-023-sessions-and-threads.md) and [KI-OBSERVA-VIS-024](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-024-review-queue.md) in the running Observatory; on "accept", close each through ki-accept.
- Then: deliver KI-OBSERVA-BRG-002 when the harness change lands; shape live artifacts as extensions of the Observatory (ARTIFACTS-EXTEND; obs-extensions reworking [design/live-artifacts.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.observatory/design/live-artifacts.md) - running); [KI-OBSERVA-OPS-003](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-OPS-003-observatory-serving-location.md) waits in triage; unit 4, the tailnet name, waits for Host network.
- Each delivery ends with an interactive service restart; a background run never restarts it.
- Running under PUSH-ALL: obs-extensions (steered: lose nothing, keep overlaps side by side), obs-feedback (KI-OBSERVA-BRG-002, send off), then obs-hosts (triage record). Each apps-observatory.local delivery needs a service restart after.
- Open with Kris: OBS-REVIEWS (review KI-OBSERVA-VIS-023 and KI-OBSERVA-VIS-024 now the service is restarted).
- 20:39 BST coordinator slip: a push to settle PUSH-STACK also carried three other sessions' commits (`71f6fce`, `ce88d3c`, `12604ab`, ki.ways-of-working and others) fast-forward to origin; told to Kris. obs-extensions (`42e1e77`) redrew the Mermaid diagram before the NO-MERMAID steer reached it; left in place, pending DIAGRAM-STANDARD. Open with Kris from it: EXT-MODEL, EXT-ROOTS.
- DESIGN-APPLY: obs-design-plan plans the ki-design handoff in the Observatory roadmap after obs-hosts; show Kris the plan before any build.
- obs-feedback done: KI-OBSERVA-BRG-002 Awaiting review, send switched off (`ffb5e50`, `d38fe63`, pushed); service restarted 21:00 BST. obs-hosts done: KI-OBSERVA-VIS-029 in triage (`19b0fa7`, pushed). With Kris to review: KI-OBSERVA-VIS-023, KI-OBSERVA-VIS-024, KI-OBSERVA-BRG-002.
- obs-design-plan done: 18 records KI-OBSERVA-APP-042 to KI-OBSERVA-VIS-040 (`fbd1fbf`, `87fab2c`, pushed); nothing built. Report at the run state path `~/.local/state/ki/agents/observatory/obs-design-plan.report.md`.
- Sent to Kris 21:12 BST. Open with Kris: OBS-REVIEWS (now with KI-OBSERVA-BRG-002), EXT-MODEL, EXT-ROOTS, DIAGRAM-STANDARD (ki-diagramming location asked), DESIGN-READY, DESIGN-WORK-GLYPHS, DESIGN-RELAY, ROADMAP-VIS-022, and the twelve spec §11 queries: DESIGN-RESTRUCTURE, DESIGN-WORK, DESIGN-AUTOMATION, DESIGN-ACT-NAME, DESIGN-ACT-MARK, DESIGN-STALE, DESIGN-SWITCH, DESIGN-CAPITAL, DESIGN-POSITIONS, DESIGN-WORKERS-CHIP, DESIGN-LIBRARY-SEARCH, DESIGN-NARROW, DESIGN-TAILNET-BRIDGE.
- Received 19 October: EXT-MODEL, EXT-ROOTS, DIAGRAM-STANDARD, MEDIUM-UP. Running obs-tokens (KI-OBSERVA-APP-042), obs-roots, obs-diagrams; obs-answers waits on obs-tokens. Open with Kris: OBS-REVIEWS; low ones DESIGN-WORK, DESIGN-STALE, DESIGN-WORKERS-CHIP.
- obs-roots done: KB-PRINCIPAL-044 in personal-principal (unpushed, another session's `cd5804d0` stacked: PUSH-PERSONAL) and KI-MCP-GIT-FND-006 in mcp-git-audit (pushed); asks ROOTS-DOTFILES. obs-diagrams done (read-only): `ki-diagrams` in the harness, Archify adopted, D2 for code maps; asks DIAGRAM-STANDARD, DIAGRAM-MIGRATION, DIAGRAM-NAME. Reports at the run state path.
- obs-tokens done: KI-OBSERVA-APP-042 Awaiting review (`881d7d9`, `9776345`, pushed; PDR-KI-OBSERVA-008); service restarted 08:02 BST. Asks GLYPH-SPAN (archipelago glyph on spanning signals).

## Messages

- 2026-10-18 · PRINCIPAL-CI-RED · KI > Model > Ways of working: Kris answered "do all the recommended items"; ki-principal CI fails RECORD-2 on this `work.md`: write `None` under empty `Messages` and `Parked`, and drop `hold: null` while not on hold. Before committing `obs-extensions.report.md`, link KI-OBSERVA-BRG-002 to its local file and run `rumdl fmt` on it.

## Parked
