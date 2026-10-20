---
id: ki.tools-burndown
state: on-hold
reason: take stock on ways of working
release: Kris says resume
since: 2026-10-20T01:05:07Z
received: 2026-10-19T18:00:08Z
beat: null
method_read: 9c17df3c
---

# ki.tools-burndown state

## Now

Mark at 23:45 BST, 19 October.

- 02:05 BST: On hold for Kris (take stock on ways of working). recordki, yorkmsg, kidesign and hooktests stopped before starting; briefs kept, relaunch on resume. estpush2 draining after its current repository. Queries parked. On resume: relaunch those four, answer HOOK-TESTS to ki.ways-of-working when the harness is green.
- 01:59 BST: received prunegit2 (KI-MCP-GIT-FND-006 pruned, pushed). HOOK-TESTS from ki.ways-of-working: hooktests queued after estpush2 in ki-agentic-harness; reply when main is green.
- 01:57 BST: Kris to bed again; no timed updates; overnight autonomy. Received acceptki2 (154, 161, 164, 166 Done; 152, 167 In progress, CAPTURE-FOLLOWUPS), acceptmgit (four Done, pushed), qreview10 (eight applied; SRC-PLACEMENT, WORKTREE-GATE parked for Kris) and PIN-LINKS. Launched prunegit2, then after estpush2: recordki, yorkmsg, kidesign.
- 01:50 BST: Kris back; 10-minute updates; Summary given. Running: acceptki2, acceptmgit, qreview10 (11 queries), estpush2.
- 01:45 BST: received prunegit: KI-MCP-GIT-FND-006 stays Done, unpruned, because KB-DOTFILES-UE-098 links it; PIN-LINKS sent to ki.chezmoi through State of play. Prune it once that comes back.
- 01:44 BST: received release3 (v0.12.0 out), knipfix (KI-TOOL-KI-CLI-167), acceptki, burnki (161, 154, 164, 152 at Awaiting review; 165 adopted), burnmgit (026, 027, 029, 030 at Awaiting review), cimcp (CI-1 in three MCPs, pushed), estfix (six repositories, three pushed) and estmig-ki (18 KI repositories converted; ki-design refused on GitHub settings). Launched acceptki2, acceptmgit, qreview10 and estpush2.
- 01:42 BST: received acceptgit2: KI-MCP-GIT-FND-006 accepted as Done and pushed, with mcp-git-audit and tools-git-almanac level. PIN-LINKS resolved by removing this work's received report copies; prunegit makes the prune commit.
- 00:29 BST: received burnmcp1: mcp-acquire-whatsapp has no records; the 12 email-routing records in mcp-m365 and mcp-gsuite stay on hold under EMAIL-OWNER (hnr.email-routing, paused until Kris resumes Humans not Robots work), hold re-validated, dangling links fixed, OWN-1 fixed, all pushed. cimcp launched for CI-1 in those three.
- 00:27 BST: Kris gone to bed; OVERNIGHT in force (decisions.md). Sweep every 10 minutes once no run is live; re-review unresolved queries on later sweeps.
- 00:27 BST: received burnmcp2: mcp-housekeeping-claude, mcp-ki-kb-fs and mcp-ki-kb-notion-mirror have no records; CI-1 and OWN-1 audit fixes committed and pushed in all three. Outstanding: CLAUDEBIND-1 warning (Claude Desktop configuration on this machine) left - machine configuration.
- 00:25 BST: acceptgit stopped on ACCEPT-AUTHORITY (footer conflict); relaunched as acceptgit2 with --rules prune. burnmgit: KI-TOOL-MGIT-CLI-026 at Awaiting review.
- 00:24 BST: received burnrig: KI-MCP-GIT-FND-006 delivered to Awaiting review, CI pin fix in mcp-git-audit and tools-git-almanac, tools-git-almanac has no records. acceptgit (Codex high) accepts FND-006 and pushes both. estpush received: 13 pushed, 7 left under other sessions' commits.
- 00:21 BST: received qreview9; YORK-YARN, PKG-NO-HUSKY and NO-GATE applied, estfix launched; NO-GATE gate declaration sent to ki.ways-of-working through State of play. estpush finished, to receive.
- 00:20 BST: Kris set TO-DONE and is away four hours. SYNC-CATEGORIES c), SYNC-STREAMS b), GRANOLA-CHECKPOINT a) applied. burnmcp1 and burnmcp2 launched for the six other MCP repositories; burnmgit, burnrig and burnki extended to triage, unhold and keep going. Next: as each burn run finishes, launch a Codex high accept run on its repositories, then continuation burns until nothing can move. roadmap-census-2 acted on; tools-rig and tools-techne passed to State of play.
- 00:18 BST: received acceptrig (KI-TOOL-RIG-CORE-063 accepted and pruned; CANCEL-MERGE routed to ki.mac-studio-setup through State of play under LANE-FIX; its tools-rig commits added to estpush) and ideas (MGIT-ESCAPE and MGIT-OUTPUT on the Project note, MARK-FOLLOWUP sent).
- 00:17 BST: received estmig-org: 20 of 26 other-organisation repositories converted, local commits; estpush pushes them. YORK-YARN, PKG-NO-HUSKY and NO-GATE at qreview9. Conform's .rumdl.toml rewrite and rumdl --fix reflow reverted 20 times - outstanding.
- 00:16 BST: received release2, granola, qreview7. TRIAGE-NEXT and HOOK-ADOPT applied (sent to burnki). FOREIGN-COMMITS closed: the commits were granola's; release3 ships v0.12.0 after knipfix. GRANOLA-CHECKPOINT (medium) at qreview8. Still to receive: estmig-org, acceptrig (CANCEL-MERGE to ki.mac-studio-setup), ideas.
- 00:14 BST 20 October: messages acted on. LANE-FIX: tools-rig is ki.mac-studio-setup's; burnrig told to touch only mcp-git-audit and tools-git-almanac, and acceptrig's tools-rig CANCEL-MERGE goes to ki.mac-studio-setup at receive. TERRITORY-TECHMEDIX folded into KI-TOOL-KI-CLI-154 and CHECKER-GAPS taken as a small fix, both sent to burnki under HIGH-APPLY. release2, granola, estmig-org, acceptrig, qreview7 and ideas finished, to receive.
- 00:10 BST 20 October: Kris set HIGH-APPLY and asked for full speed. Seven SYNC-* answers applied. Burn runs: burnmgit running, burnrig held on acceptrig, burnki held on acceptki; each plans and implements its lane's records to Awaiting review. HIGH-APPLY sent to every live run. SYNC-CATEGORIES and SYNC-STREAMS (review disagreed) with Kris; TRIAGE-NEXT and HOOK-ADOPT applied automatically if qreview7 lifts them to high.
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
