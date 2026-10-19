# Decisions

Struck at the mark of 2026-10-19T17:58Z. Git history holds every struck entry; [historical-decisions.md](design/historical-decisions.md) keeps the 11 to 14 October log as evidence.

## Standing push and branch-delete authorities (16 October)

Kris, 16 October 01:05 BST: "stop to ask me before any ki or mgit release", and from Master: state-of-play: "Remote branch deletes and any ki or mgit release ask me first."

Kris, 16 October 21:40 BST, UNPUSHED-COMMITS: "Push ki-principal's 16 commits fast-forward now and at each resting point, other sessions' included". Standing: push ki-principal fast-forward at each resting point.

## One tools-ki writer (16 October)

OWNER-LANE a), taken under BURN-OVERNIGHT on 16 October: "tools-burndown runs the only tools-ki writer for all in-scope records; tell the ways-of-working and knowledge-acquisition threads through Messages from Master, and they keep priority and acceptance input."

## RIG-TARGET-SPEED-LOAD (18 October)

Kris, 18 October 19:09 BST, "agreed with all the recommendations": Rig's configuration-load cost is left as it is, and no record is captured.

## KI-TOOL-KI-CLI-139 "Decision 55" deferral (18 October)

Kris, 18 October 03:55 BST: "we're in the process of moving some of the decisions around so that might be confusing to you." Read back as DECISION-55-CITATIONS: leave -139's citations while the decisions move; revisit after (source: hnr-principal 5g-emerge-phase3 decisions, SRC-TOOLING, 16 October).

## CONSUMER-MIGRATE (17 October)

Kris, 17 October: "Wait for the mgit release, then migrate the chezmoi dot_mgit.toml source and the live manifest together."

## DIGESTS-SCAFFOLD (17 October)

Kris, 17 October: "Keep -/_DIGESTS/ as the declared scaffold."

## Pointers

- HOST-WRITES (14 October): the replacement-policy investigation stays parked with Techne: agent-host; held in [ki.estate-factorisation](../../_WORK_REVIEW/ki.estate-factorisation/work.md).
- HOST-GUARDS (14 October): [KI-TOOL-TECHNE-CLI-006](/Users/krisbrown/workspaces/knowledge-islands/tools-techne/docs/roadmap/KI-TOOL-TECHNE-CLI-006-guarded-host-commands.md) stays on Hold, review on 12 November; the record carries it.
- FOOTER-GRANTS (16 October): separate `--allow fetch` and `--allow machine` grants; [KI-TOOL-KI-CLI-134](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-134-launch-footer-follows-brief.md) carries it.
- SIZE-PRIORITY (19 October): Kris, "work should have a size and a priority, even if its horizon isn't now or next"; handed to Ways of working through its Messages section, and Kris confirmed the handoff done on 19 October; [ki.ways-of-working](../ki.ways-of-working/work.md) carries it.
- RIG-SITE-001-POINTER a) (19 October): at Kris's acceptance of KB-MIDNIGHT-RIG-SITE-001, drop the bootstrap-guide pointer as overtaken by `c416154`.
- MGIT-LEARN-MAJORITY (19 October), with its refinement: homed in [KI-TOOL-MGIT-CLI-028](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-028-learn-majority-output.md), delivered.
- RIG-SITE-CONFIG (19 October), Kris, passing on a handoff from the rig.midnight.ninja design project (per-host configuration flag, optional coarse acquisition kind): "Take it with a pinch of salt, we own the data structure, so can suggest better ways of making data available / structured. Also, rig depends on certain underlying package managers, e.g. brew. Is that covered in the management and output?" Read back: assess the handoff and propose Rig's own data shape before any capture; answer whether Rig manages and reports its package-manager prerequisites. Ask B (widening the public export) has no go-ahead yet.
- RIG-OUTPUT-SCHEMA (19 October), Kris: "what we should do is create a schema for the output and then that can be used so the designer know what data is where..." Read back: Rig publishes a schema for its JSON output (`rig show`, `rig export`) that consumers such as the rig.midnight.ninja designer use to know what data is where; fold into the RIG-SITE-CONFIG proposal.
- HIGH-CONFIDENCE (19 October), Kris: "do all high confidence items and then give me a summar about the reset. Take a mark". Still live: SITE-CONFIG-PREMISE a), tell the rig.midnight.ninja side the host columns would match today, shape provisional ([rig-site-reply](design/rig-site-reply.md)); ASK-B a), Ask B parked until the site side asks. KI-TOOL-KI-CLI-153 accepted and KI-TOOL-KI-CLI-156 captured carry the rest.
- HOOKS-STANDARD (19 October), Kris via [ki.ways-of-working](../ki.ways-of-working/decisions.md): "add an urgent message to it to standardise". Read back: one commit-gate hooks convention, Husky, across the estate; tools-burndown owns the convention, the harness standard and rubric change, and the rollout through `ki repo`; design first, rollout after Kris settles the convention.
- KI-PATCH-RELEASE (19 October), Kris via [ki.ways-of-working](../ki.ways-of-working/decisions.md), "CI-RED-MAIN and CLI-FIELDS": "can you sort that please". Read back: one `ki` patch release soon carrying KI-TOOL-KI-CLI-155 and a harness pin providing `ki-work-package`; the standing ask-first rule holds the tag until Kris answers KI-RELEASE-GO.
- BURNDOWN-PUSH (19 October), Kris via [ki.ways-of-working](../ki.ways-of-working/decisions.md), agreed a roadmap burndown push for tools-ki, tools-mgit and the MCP server repositories: prune every done record; bring every record awaiting review as one acceptance batch; cancel or merge triage records, aiming for at least half, each with a one-line reason, for Kris to confirm before anything is cancelled; report the net count before and after.
- MGIT-RELEASE (19 October), via [ki.ways-of-working](../ki.ways-of-working/decisions.md): Kris's hands-on check of KI-TOOL-MGIT-CLI-023 passed; under MGIT-RELEASE a), accept it under `ki-accept` with Kris, then cut one mgit release. The standing ask-first rule holds the tag until Kris answers MGIT-GO. CONSUMER-MIGRATE follows the release.

## 19 October, 21:34 BST - Summary of 21:28 answered

Kris: "All recommended with the following changes or queries. NON-KI - 100% not included in this, only ki repos. GIT HOOKS (query to resolve before any of the questions you have). Do we need to use Husky? What advantage does that bring? Can we just put the git hooks inside the `.git` folder? Or is it better to have it outside of the `.git` folder?"

Taken as: KI-RELEASE-GO a), tag `v0.11.5` at tools-ki HEAD once a full re-run there passes, then push, publish and tell ki.ways-of-working, Kris answering before qreview3's disagreement reached them and the green re-run guarding it; MGIT-GO a) and BURNDOWN-ACCEPT a), accept KI-TOOL-MGIT-CLI-028 and KI-TOOL-MGIT-CLI-023 and publish mgit `v0.18.0` on `9a3564d`; TRIAGE-PROPOSAL a), keep all eight; BIOME-CI-STANDARD a); MGIT-LEARN-UNATTENDED a); SITE-CONFIG-SHAPE a); SITE-CONFIG-DATA a); MANAGERS-AS-TOOLS a); NON-KI a), outright, only KI repositories. HOOKS-CONVENTION, KB-AUDIT, COMMIT-MSG and ROLLOUT-AUTHORITY are held behind the new GIT-HOOKS query. ROUTING-VIEW was not yet before Kris.

## 19 October, 22:02 BST - Summary of 21:54 answered

Kris: "ok - I'm good with the recommendations, but one final thing on githooks, is there a recognised way of dealing with this in general?"

Taken as: GIT-HOOKS a), committed `.githooks` holding all hook content in every KI repository, bound by `core.hooksPath`, Husky and `.husky` removed, so HOOKS-CONVENTION is settled by it and KB-AUDIT falls away; ROUTING-VIEW a), capture the tools-ki routing-view record now, planned after KI-TOOL-KI-CLI-158. The general-practice question was answered in the reply. COMMIT-MSG and ROLLOUT-AUTHORITY return to Kris before any rollout.

## 19 October, 22:08 BST - SYNC-SUMMARY

Kris: "mgit sync could do with a better summary", with a run where ki-agentic-harness was skipped for local changes while 5 commits ahead, ki-principal pushed 1 commit and 55 were in sync. Taken as: capture a tools-mgit triage record for a clearer closing summary of `mgit sync`.

## 19 October, 22:11 BST - Summary of 22:04 answered

Kris: "I agree with the recommendations. You may think though that perhaps given the usefulness of githooks that we should add some mechanical checks for this in the audit. I think that's actually a massive area that we need to go back and look at anyway, but that's probably something to pass up to the state of play. We need to do that whole proper audit and checking of skills and everything. There's a massive conformance piece if we ever get to the point of getting this roadmap down to something sensible."

Taken as: COMMIT-MSG a), a `ki git check-message` command for `.githooks/commit-msg`, pre-commit only until it ships; ROLLOUT-AUTHORITY a), one owner grant per wave, runs commit by explicit path locally and Kris pushes; HOOK-AUDIT, mechanical hooks checks join this work's rubric change; AUDIT-CONFORMANCE, the estate-wide audit and conformance of skills passed to State of play's messages.md.
