# Decisions

Struck at the mark of 2026-10-19T22:45:48Z. Git history holds every struck entry; [historical-decisions.md](design/historical-decisions.md) keeps the 11 to 14 October log as evidence.

## Standing push and branch-delete authorities (16 October)

Kris, 16 October 01:05 BST: "stop to ask me before any ki or mgit release", and from Master: state-of-play: "Remote branch deletes and any ki or mgit release ask me first."

Kris, 16 October 21:40 BST, UNPUSHED-COMMITS: "Push ki-principal's 16 commits fast-forward now and at each resting point, other sessions' included". Standing: push ki-principal fast-forward at each resting point.

## One tools-ki writer (16 October)

OWNER-LANE a), taken under BURN-OVERNIGHT on 16 October: "tools-burndown runs the only tools-ki writer for all in-scope records; tell the ways-of-working and knowledge-acquisition threads through Messages from Master, and they keep priority and acceptance input."

## RIG-TARGET-SPEED-LOAD (18 October)

Kris, 18 October 19:09 BST, "agreed with all the recommendations": Rig's configuration-load cost is left as it is, and no record is captured.

## KI-TOOL-KI-CLI-139 "Decision 55" deferral (18 October)

Kris, 18 October 03:55 BST: "we're in the process of moving some of the decisions around so that might be confusing to you." Read back as DECISION-55-CITATIONS: leave -139's citations while the decisions move; revisit after (source: hnr-principal 5g-emerge-phase3 decisions, SRC-TOOLING, 16 October).

## DIGESTS-SCAFFOLD (17 October)

Kris, 17 October: "Keep -/_DIGESTS/ as the declared scaffold."

## Pointers

- HOST-WRITES (14 October): the replacement-policy investigation stays parked with Techne: agent-host; held in [ki.estate-factorisation](../ki.estate-factorisation/work.md).
- HOST-GUARDS (14 October): [KI-TOOL-TECHNE-CLI-006](/Users/krisbrown/workspaces/knowledge-islands/tools-techne/docs/roadmap/KI-TOOL-TECHNE-CLI-006-guarded-host-commands.md) stays on Hold, review on 12 November; the record carries it.
- FOOTER-GRANTS (16 October): separate `--allow fetch` and `--allow machine` grants; [KI-TOOL-KI-CLI-134](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-134-launch-footer-follows-brief.md) carries it.
- SIZE-PRIORITY (19 October): Kris, "work should have a size and a priority, even if its horizon isn't now or next"; handed to Ways of working through its Messages section, and Kris confirmed the handoff done on 19 October; [ki.ways-of-working](../ki.ways-of-working/work.md) carries it.
- RIG-SITE-001-POINTER a) (19 October): at Kris's acceptance of KB-MIDNIGHT-RIG-SITE-001, drop the bootstrap-guide pointer as overtaken by `c416154`.
- HIGH-CONFIDENCE (19 October), Kris: "do all high confidence items and then give me a summar about the reset. Take a mark". Still live: SITE-CONFIG-PREMISE a), tell the rig.midnight.ninja side the host columns would match today, shape provisional ([rig-site-reply](design/rig-site-reply.md)); ASK-B a), Ask B parked until the site side asks. KI-TOOL-KI-CLI-153 accepted and KI-TOOL-KI-CLI-156 captured carry the rest.
- CONSUMER-MIGRATE (17 October), Kris: "Wait for the mgit release, then migrate the chezmoi dot_mgit.toml source and the live manifest together." mgit v0.18.0 shipped on 19 October and [ki.chezmoi](../ki.chezmoi/work.md) carries it.
- RIG-SITE-CONFIG and RIG-OUTPUT-SCHEMA (19 October): carried by [KI-TOOL-RIG-CORE-065](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-065-resource-subject-links.md), [KI-TOOL-RIG-CORE-066](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-066-plan-managers-and-uv-prerequisite.md), [KI-TOOL-RIG-CORE-067](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-067-package-managers-as-catalogue-tools.md) and [KB-DOTFILES-UE-099](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-099-resource-subject-links-and-service-paths.md).
- MGIT-LEARN-UNATTENDED a) (19 October, "All recommended"): unattended learning stays impossible; a flag record only if a need comes up.
- GFM-CONVERTER (19 October): routed from ki.ways-of-working, Kris approved at 22:00 BST that tools-ki builds the GitHub-flavoured Markdown converter (GFM-ORDER a, GFM-LINK-FORM a) to the converter requirements in [gfm-migration](../ki.ways-of-working/design/gfm-migration.md); it blocks KI-PRINCIPAL-OPS-014. gfmconv builds it, local commits only; the release is ask-first, and ki.ways-of-working is told when it is out.

## Hooks (19 October)

HOOKS-STANDARD, Kris via ki.ways-of-working: "add an urgent message to it to standardise". This work owns the convention, the harness standard and rubric change, and the rollout through `ki repo`.

Kris, 21:34 BST: "NON-KI - 100% not included in this, only ki repos." Only repositories with `.ki.toml`.

Kris, 22:02 BST: "ok - I'm good with the recommendations, but one final thing on githooks, is there a recognised way of dealing with this in general?" GIT-HOOKS a): every KI repository keeps all hook content in a committed `.githooks`, bound by `core.hooksPath`; `prepare` sets the binding; Husky and `.husky` leave. HOOKS-CONVENTION and KB-AUDIT fall away.

Kris, 22:11 BST: "I agree with the recommendations. You may think though that perhaps given the usefulness of githooks that we should add some mechanical checks for this in the audit. I think that's actually a massive area that we need to go back and look at anyway, but that's probably something to pass up to the state of play." COMMIT-MSG a): `ki git check-message` for `.githooks/commit-msg`, pre-commit only until it ships. ROLLOUT-AUTHORITY a): one owner grant per wave, runs commit by explicit path locally, Kris pushes. HOOK-AUDIT: mechanical hooks checks join this work's rubric change. The estate-wide conformance audit went to State of play as AUDIT-CONFORMANCE.

- Kris, 19 October 23:21 BST: "Go ahead with the recommendations. Although the hook release, I'm not sure we need to wait for a repo confirmed because we'll never get there. So can we just get on with it? Happy for you to do it now, straight off the back of this." Taken: SCR5-CONFORM a), VA-HOOKS a), HOOK-CAPTURE a), and HOOK-RELEASE b): release now, granting this work the ki release, tag and tools-ki push. HOOK-GUARD reached Kris after this answer and stays open.
- Kris, 19 October 23:21 BST: "There are 23 tickets across triage for the tool projects, can we get those triaged immediately?" Taken: triage every triage record in tools-ki, tools-mgit and tools-git-almanac now, commits local.
- Kris, 19 October 23:24 BST: "No, let's just migrate everything to the new form of hooks right now. Let's just get rid of the husky stuff across the entire estate. Let's just make it happen, if that's the plan, let's do it." Taken: HOOK-GUARD b), no opt-in switch; waves 2 to 5 collapse into one estate-wide migration of every `.ki.toml` repository on the released ki, commits local; then HOOK-3 to HOOK-5 move from WARN to FAIL, as HOOK-AUDIT set.
- HARNESS-PIN-FETCH (19 October, 23:41 BST): taken by the coordinator as a) under the HOOK-RELEASE b) grant - one public codeload download to compute the pin digest, as the tools-ki release guide requires; release2 finishes v0.12.0 after tritools.
- Kris, 19 October 23:42 BST: "Go ahead with the recommendations." Taken: KNIP-HUSKY a) (tools-ki follow-up configures Knip to read the committed hooks in conversion and scaffolding, cleans up converted repositories, harness Knip guidance names it), MGIT-030-NEXT a) (promote KI-TOOL-MGIT-CLI-030 to Next as a draft now, settle the nine choices with Kris at planning), MGIT-026-SIZE a) (size m when KI-TOOL-MGIT-CLI-026 is planned).
- Kris, 19 October, via State of play 23:45 BST (BURN-WAVE-1 and LANE-OWNERS): "I agree with all the recommendations in here, apart from the roadmap cap, I don't think we need one, I just think we need to focus on what we're doing now, which is to get through it." Taken: this lane is tools-ki, tools-rig, tools-mgit, tools-git-almanac and mcp-git-audit; one ki-accept pass in each, with cancel, merge and idea candidates brought to Kris as one query (CANCEL-MERGE); CAPTURE-GATE - runs create no records, the coordinator briefs one only for a blocker, a defect seen failing or a Kris request; no roadmap cap.
- SIZE-GAP (19 October, 23:50 BST): taken by the coordinator as a), a small audit fix under CAPTURE-GATE - size KI-TOOL-KI-CLI-125, -134, -139 and -140 in the acceptki pass.
- MARK-FOLLOWUP (19 October, 23:50 BST, from State of play): MGIT-ESCAPE and MGIT-OUTPUT taken as ideas in the tools-burndown Project note, no records.

## Speed (20 October)

Kris, 20 October 00:10 BST: "Okay, let's try this. Let's try it that if you get a high confidence on a recommendation that you just apply it and I want it to go as fast as you can now on the tools, like super fast. Like let's just get it done. I want this back down to something sensible." Taken as HIGH-APPLY: any recommendation at high confidence, including one lifted to high by a blind review, is applied without asking Kris; runs apply their own high-confidence choices and report them; medium and low still go to blind review, and only disagreements or unlifted ones reach Kris. Runs plan, implement and leave records Awaiting review in parallel per repository. Releases stay ask-first under the 16 October standing rule.

- Applied under HIGH-APPLY at 00:10 BST: SYNC-TALLY, SYNC-SKIPDETAIL, SYNC-HELD, SYNC-EXIT, SYNC-JSON, SYNC-VERBOSE and SYNC-CLEANFETCH a) (reviewed high), each with the reviewer's added points folded into planning.
- Applied under HIGH-APPLY at 00:16 BST: TRIAGE-NEXT a) (reviewed, lifted to high; plan KI-TOOL-KI-CLI-161 before KI-TOOL-KI-CLI-152, splitting the close-gate repair out if separable) and HOOK-ADOPT a) (reviewed high: KI-TOOL-KI-CLI-164 at Next, KI-TOOL-KI-CLI-165 and KI-HARNESS-GOV-225 at Soon), both sent to burnki.
- FOREIGN-COMMITS closed at 00:16 BST without Kris: release2 took `af7c2d83` and `91c2531d` for another session's, but they are this work's granola run (KI-TOOL-KI-CLI-166), so pushing them is pushing this work's own commits. The v0.12.0 release goes ahead under HOOK-RELEASE b) as release3, after knipfix, carrying KI-TOOL-KI-CLI-166 and the Knip fix.

## All tools and MCPs to Done (20 October)

Kris, 20 October 00:20 BST: "Okay, I want you to take all the roadmap items for all of the MCPs and all the tools through to done. What I want you to do is make sure that anything which is on hold that can be unheld is on held. Everything that's triage is done. And where you need to use a higher model to get a second opinion about everything if you're not sure." Then: "I'm going to be away for the next four hours, so I'm usually done." and "I need you to get it done". Taken as TO-DONE: every open record in tools-ki, tools-mgit, tools-git-almanac and every mcp-* repository goes through triage, planning and delivery to Done, with an independent Codex accept pass taking Awaiting review to Done; every hold is re-validated and lifted where its condition no longer holds. Where a choice is medium or low, a blind Codex high review is the second opinion: agreement applies it, and on disagreement the reviewer's view is taken when its confidence is at least the run's, otherwise the run's. Releases other than v0.12.0 and remote branch deletes stay ask-first. tools-rig stays with ki.mac-studio-setup under LANE-FIX (sent the instruction through State of play); tools-techne stays under the Techne Programme Focus.

- Applied under TO-DONE at 00:20 BST: SYNC-CATEGORIES c) (reviewer, high: five outcomes, a failed fetch counts as failed, a dirty checkout whose fetch failed keeps both reasons) and SYNC-STREAMS b) (reviewer, tie at medium, taken as it finishes the convention here: skip, warning, progress and prompt lines to standard error, tally and results on standard output). GRANOLA-CHECKPOINT a) (reviewed high): keep the checkpoint check, concern recorded in KI-TOOL-KI-CLI-166.
- Applied under TO-DONE at 00:21 BST after qreview9: YORK-YARN a) (reviewed high: remove Husky through Yarn with registry access, then conform, keeping lint-staged and Commitlint); PKG-NO-HUSKY a) with the reviewer's correction (reviewed high: Knowledge Base pre-commit in hnr-principal and legal-principal, `prepare` binding in both manifests, HOOK-3 stays a warning until KI-TOOL-KI-CLI-161 ships); NO-GATE a) (reviewed, lifted to medium, applied on agreement: staged check-only `ki repo audit --skill ki-repo` pre-commit in apps-dafacts.org, apps-kris.me.uk and acquire; declaring it as the ki-repo-project gate is ki.ways-of-working's, sent through State of play).
- ACCEPT-AUTHORITY at 00:25 BST: acceptgit stopped because its default footer forbade accepting and pruning; its a) (high) applied: relaunched as acceptgit2 with the prune tier. Accept runs under TO-DONE launch with `--rules prune` from now on.

## Overnight autonomy (20 October)

Kris, 20 October 00:27 BST: "I'm going to bed now. I want you to keep looking every 10 minutes to see if there's any new work for yourself in some way. And if there is, I want you to progress it. You can do anything on a high confidence level that you recommend. If you can get a good recommendation, you can move on to the next one, and as you do more and work, it might be that when you come back to ones that you couldn't get a good recommendation for, it might be more accurate. We've got autonomy to make this happen, so I'm going to leave you with this in your safe hands." Taken as OVERNIGHT: while runs are live the coordinator still wakes at least every 5 minutes; when none is live it sweeps every 10 minutes - messages.md, then `ki work status` across tools-ki, tools-mgit, tools-git-almanac and the mcp-* repositories - and launches a run for anything that can move. High-confidence recommendations, own or reviewed, are applied; a query left medium or low is set aside and re-reviewed on a later sweep with the newer evidence, and only what still stays unresolved waits for Kris's return. Releases other than v0.12.0, remote branch deletes and other sessions' stacked commits stay out of bounds.

- 01:44 BST receive: ki v0.12.0 released (Release run green, Homebrew 0.12.0). acceptki verified KI-TOOL-KI-CLI-166, 167, KI-TOOL-MGIT-CLI-026 and 027 but could not accept (none tier); relaunched as acceptki2 and acceptmgit with the prune tier, covering everything at Awaiting review, plus SIZE-GAP a). HOLD-PUSH (estfix) answered by the push style: hnr-principal, legal-principal and acquire stay unpushed under other sessions' commits. Open queries from burnki, acceptki, estfix and estmig-ki go to qreview10 under TO-DONE.
- Kris, 20 October 01:50 BST: "I'm back, so let me know what the current situation is, and the latest summary is, so that I can answer some questions. You can start with 10-minute updates. I can concentrate on what's upstanding." Taken as: OVERNIGHT ends, Kris is present; timed updates every 10 minutes, with the waiter still waking on any run's finish; HIGH-APPLY and TO-DONE stand, and queries that stay medium or low after review now go to Kris.

## Bed again (20 October, about 01:58 BST)

Kris: "I don't think I really need a 10 minute update so I'm not here right. So what I really want you to do is get on with it. I'm going to bed now so I want to be able to set the right message to all of our threads so when I come back it's done and I'm not actually stuck waiting."

Taken as: no timed updates; overnight autonomy again, with HIGH-APPLY and TO-DONE standing; the waiter wakes every 10 minutes to receive runs and launch the next unit; a query that stays medium or low after blind review is parked for Kris's return and re-reviewed on later sweeps.

## Applied after qreview10 (20 October, 01:58 BST)

- CANCEL-MERGE-BURNKI and CANCEL-MERGE-ACCEPTKI: reviewer high, so KI-TOOL-KI-CLI-160, 140 and 125 stay as they stand; the message and prune capture waits on CAPTURE-FOLLOWUPS.
- HOOK-LOCAL a), reviewed high: a marked local block the host keeps verbatim, once KI-HARNESS-GOV-225 recognises it.
- CLI-OUTPUT: reviewer high, split: progress to standard error after a consumer inventory; `--json` replaces `--format` only with an agreed consumer migration, because the Observatory calls `--format`.
- VALIDATOR-HOME a), reviewed high. CI-EVIDENCE a), reviewed high. YORK-COMMITMSG a), reviewed high.
- KI-DESIGN-REFUSAL: reviewer high, local-only hook conversion, GitHub settings untouched.
- PKGLESS-GATE a), reviewed high: keep the homebrew-tap and ki-specifications gates; their shape ownership goes to ki.ways-of-working with NO-GATE.
- PIN-LINKS returned by ki.chezmoi at 01:52: prunegit2 prunes KI-MCP-GIT-FND-006.
- acceptki2: KI-TOOL-KI-CLI-154, 161, 164 and 166 Done and pruned; 152 and 167 back to In progress for want of follow-up identifiers. acceptmgit: KI-TOOL-MGIT-CLI-026, 027, 029 and 030 Done, pruned and pushed.
- HOOK-TESTS from ki.ways-of-working (01:57): the harness hook tests failing on `main` fall under this work's hooks migration; hooktests repairs them after estpush2, and this work tells ki.ways-of-working when `main` is green.

## Hold (20 October, 02:05 BST)

Kris: "pause - take stock. Go On hold under current ki-coordination: drain (let a run that will end within about 15 minutes finish, stop any other at a safe point and record where), launch nothing new, commit your own work by explicit path and push only as the standard allows, park every open query, and set state.md to on-hold with reason "take stock on ways of working" and release "Kris says resume". Before the hold report, write design/retro-2026-10-20.md in your work folder with three headings, Working well, Not working and Would change, in five to ten plain bullets that cite real incidents from this work, and commit it with the hold. Then give the hold report and its resume line."

Taken as: recordki, yorkmsg, kidesign and hooktests stopped before they started, with their briefs kept for resume; estpush2 told to stop after its current repository; CAPTURE-FOLLOWUPS, SRC-PLACEMENT and WORKTREE-GATE parked.
