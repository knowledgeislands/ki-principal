---
id: ki.tools-burndown
state: with-worker
since: 2026-10-19T22:45:48Z
received: 2026-10-19T18:00:08Z
beat: null
method_read: 9c17df3c
---

# ki.tools-burndown state

## Now

Mark at 23:45 BST, 19 October.

- tritools finished 23:49 BST: KI-TOOL-KI-CLI-164, -165 and KI-HARNESS-GOV-225 captured in triage; all 10 tools-ki triage records adopted at Soon (tools-ki e0bb5bcc, local); hooks design note updated (ki-principal 92241e5c). TRIAGE-NEXT and HOOK-ADOPT at blind review qreview7. SIZE-GAP a) taken by the coordinator as a small audit fix under CAPTURE-GATE, folded into acceptki. Message MARK-FOLLOWUP (23:50): MGIT-ESCAPE and MGIT-OUTPUT taken as ideas, written to the tools-burndown Project note by run ideas.
- mgitplan finished 23:48 BST: KI-TOOL-MGIT-CLI-030 at Next as a draft (tools-mgit 5b2a4cd local), nine SYNC-* design queries copied in and at blind review qreview6.
- messages 23:47 BST: BURN-WAVE-1 and LANE-OWNERS taken. acceptrig (tools-rig, tools-git-almanac, mcp-git-audit) running; acceptki (tools-ki, tools-mgit) held on knipfix. CAPTURE-GATE sent to every live run; the records tritools, granola and knipfix create are coordinator-briefed for Kris requests (HOOK-CAPTURE a), GRANOLA-TRUST, KNIP-HUSKY a)).
- Hooks: pilot done and proven (tools-ki d88d494b, ki-principal 2646d94b pushed, va-principal 7f61803 local). Kris ordered the whole `.ki.toml` estate off Husky tonight: estmig-org converting other organisations on the source-linked ki; estmig-ki queued after tritools, ending with HOOK-3 to HOOK-5 at FAIL. Estate runs add Knip ignores by hand, restore the stray `.rumdl.toml` rewrite and test refusal with only git on PATH. Commits stay local; pushing is housekeeping, not a query (PUSH-NOT-WITH-YOU).
- Release: KI-TOOL-KI-CLI-163 done (aa37f512), KI-TOOL-KI-CLI-157 blocker fixed (e5224f33), KI-TOOL-KI-CLI-162 accepted and pruned by another session. release2, queued after tritools, bumps the harness pin (HARNESS-PIN-FETCH a), cuts v0.12.0, pushes tools-ki and upgrades Homebrew `ki` (installed 0.11.5).
- tools-ki chain, one writer at a time: tritools (HOOK-CAPTURE records, hooks design note, tools-ki triage of 11 records) -> release2 -> granola (GRANOLA-TRUST, Acquired folder alone) -> knipfix (KNIP-HUSKY a), Knip reads `.githooks`, harness guidance).
- tools-mgit: triage done (977bec6 local); mgitplan promoting KI-TOOL-MGIT-CLI-030 to Next and returning its nine design choices as queries. MGIT-026-SIZE a) applies when KI-TOOL-MGIT-CLI-026 is planned. tools-git-almanac has no records.
- Outstanding: ki-authoring `.rumdl.toml` drift (conform drops MD005 and MD075 disables); va-principal `commit-msg` waits on KI-TOOL-KI-CLI-161; estate Knip cleanup after the next release; KI-TOOL-KI-CLI-159 OWNER-LANE flag; rig-site-reply still to pass on.

## Next steps

1. Receive hooksv2: copy its wave-plan query to `queries.md`, blind-review any medium or low one, and bring the first wave grant to Kris.
2. Receive gfmconv: bring the converter release to Kris (ask-first), then tell ki.ways-of-working.
3. Not this work's: KI-TOOL-KI-CLI-154; LGL-PRINCIPAL-OPS-018 (legal-principal).

## Held

- RIG-SITE-001-POINTER: drop the bootstrap-guide pointer, until Kris accepts KB-MIDNIGHT-RIG-SITE-001.
- KI-TOOL-KI-CLI-139's "Decision 55" citations, until the decisions move settles (DECISION-55-CITATIONS).
