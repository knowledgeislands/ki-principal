# Decisions

## 2026-10-09 - Project closures deferred

- Kris deferred Project closures until acquire-ChatGPT knowledge items are checked against them.

## 2026-10-09 - Website records held

- Kris: Keep KI-WEB-SITE-001 and KI-WEB-SITE-039 on hold.

## 2026-10-09 - Projects and roadmap count

- Kris wants everything captured in Projects/threads, ideally as ideas or roadmap items, and the roadmap count brought down.

## 2026-10-09 - PRFLOW

- PRFLOW: Kris chose (a) - background agents keep pushing directly to harness main through the admin bypass, after tests and audit.
- 2026-10-10: PRFLOW reconfirmed: push directly to ki-agentic-harness main.

## 2026-10-09 - PIN

- PIN: Kris chose (a) - tools-ki CI builds ki from its own source instead of taking a pin; KI-HARNESS-GOV-168 excludes tools-ki.

## 2026-10-09 - STATE retention rule

- STATE: Kris approved (1) a run-folder retention rule in ki-delegation, parked with the ways-of-working Project

## 2026-10-11 - macOS defaults split parked

- Kris (2026-10-11): Parked: splitting macOS defaults out of Rig (not now).

## 2026-10-12 - DESIGN-SYSTEM

- Kris, 2026-10-12 05:40 BST: DESIGN-SYSTEM approved - roll ki-design-system out to every apps-* repository (website and app repos). Read-only assessment now; changes land after the step 9 renames so no agent works in a folder that is moving.
- Kris, 2026-10-12 05:58 BST: DESIGN-SYSTEM - Techmedix sites wait until adopted; kris.me.uk gets full conformance; midnight.ninja holds three sites (apex, rig, tower) and Kris is minded to split it.

## 2026-10-12 - SPEC-REVIEW and KI-RELEASE order

- Kris, 2026-10-12 06:45 BST: SPEC-REVIEW starts only once the known Knowledge Islands roadmap records are near zero. KI-RELEASE (ki and mgit) yes, after their roadmaps reach zero. Drive the Knowledge Islands roadmaps towards zero first.

## 2026-10-12 - Other territories parked

- Kris, 2026-10-12 ~19:50 BST: only Personal and Valle Armonia masters running among other territories; keep others parked until Knowledge Islands is bottomed out, then Paperclip helps.

## 2026-10-14 - Roadmap burn-down focus

- Kris 2026-10-14: roadmap has grown ~50% since last measured. Standing focus: burn the roadmap down; no new feature records. Capture only blockers, defects or Kris-requested items; prefer closing, merging or rejecting. Applies to every Knowledge Islands thread and every agent brief. Also: stay available and delegate everything.

## 2026-10-14 - RIG-REL-PATCH and capture landing

- Kris 2026-10-14 morning: RIG-REL-PATCH accepted; follow-up releases stop and ask first from now on.
- Kris 2026-10-14 morning: Kris wants: always land the information even if imperfect (uncertain territory goes to a triage territory), record the agentic system's session or thread ID in front matter

## 2026-10-14 - ROADMAP-SIZING

- Kris 2026-10-14: ROADMAP-SIZING agreed: one design record to ways-of-working; daily count snapshots first, sizing and ID allocation after.

## 2026-10-14 - ROUTE-LOCAL

- ROUTE-LOCAL (Kris, 14 Oct, pasted from acquire-intake): act on the prepared Master message. Coordinate receiving ownership of KB-ACQUIRE-002 and KB-ACQUIRE-003 with knowledge-acquisition, and return the proposed MCP home, hosting and concrete first-probe scope for review before implementation. Review only: no records, repositories, code, migration, credentials, live tests, deployment or push.

## 2026-10-14 - GRANOLA-SUPPORT, BINARY-HOME and ACQ-FOCUS

- Kris, 2026-10-14 ~21:40 BST, replies to the re-bootstrap report. GRANOLA-SUPPORT: adopt KI-TOOL-KI-CLI-128 as the tools-ki half and create only the harness record; local delivery; migration separately gated.
- Kris, 2026-10-14 ~21:40 BST, replies to the re-bootstrap report. BINARY-HOME: iPhone check first, then the private mcp-acquire-chatgpt repo and local synthetic build; 'a candidate that should be handed off to the Knowledge Acquisition project/thread'.
- Kris, 2026-10-14 ~21:40 BST, replies to the re-bootstrap report. ACQ-FOCUS: adopt as delivery priority (mac-studio-bootstrap and agent-host first; hold unchanged; policy wording only when asked).

## 2026-10-15 - FW-ADR

- Kris, 2026-10-15, FW-ADR: "On a pass, the acceptance run accepts KI-TOOL-RIG-CORE-047 and marks both ADR-KI-TOOL-RIG-009 and ADR-KI-TOOL-RIG-010 accepted."

## 2026-10-17 - Kris's intake dump, items not yet homed

Kris: "I've now destroyed all my notes about it" - this log is the durable capture until each item reaches its owning thread.

- **MGIT-ESCAPE** (tools burndown, tools-mgit): "we could do with better output from mgit. A lot of the commands in mgit are effectively pass-throughs ... anything which I create at the mgit level overrides the pass-through ... There should be some kind of escape hatch". Proposed: `--bare` runs the git subcommand in each child bypassing mgit's own command; `--raw` (rather than `-B`) runs any command as a shell in each repository directory; mind clashes with the physical and follow-symlinks options. "Git has got work tree. We've got mgit work tree, so it'd be nice to have an escape hatch".
- **MGIT-OUTPUT** (tools-mgit): "I really want MGIT to have much better output ... if I do MGIT status over the entire estate, because there's like 50 projects, it scrolls off the screen ... I really, really want this kind of idea of it giving me a progress bar ... and then it gives me the results at the end ... anything which has got no changes, it doesn't tell me about it, it only tells me ... the ones that have changed ... sync could be the way to try that out first ... if it pulls and it gets a rebase or a merge warning, it should effectively automatically abort that and give me a warning instead ... some of this might be better off done as like we did with the Git Almanac, so we can put some code behind it". References: the Claude Code terminal UI ("a little windowing toolkit within a prompt"), Omarchy (DHH's Arch distro).
- **MGIT-ESCAPE** (part 1) restated: bare and raw modes let "commands that I wrap over the top of existing ones".
- **CAPTURE-ONLY**: "I don't want you to start spinning out loads of designs from this. The whole thing here is to capture everything ... and then we can go through a prioritization phase". "I don't want them to go into intake ... these can become part of this ideas of stuff".
- **DIAGRAMS-BLACK** (2026-10-17 14:10 BST): "the preview and markdown for the themes.md is largely speaking black diagrams. I can see some kind of faint things on it, but whatever you're doing to render those, it's not looking right." Screenshot: dark frames and boxes on a black canvas, no legible text.

## 2026-10-17 14:20 BST - replies to the 14:02 BST summary

- **AWAITING-REVIEW:** "Clear the backlog one repository group at a time through ki-accept: tools burndown presents KI-TOOL-KI-CLI-126, -130, -133, -141 and KI-TOOL-MGIT-CLI-017 after the tools-ki push; ways of working presents KI-HARNESS-GOV-195, -198, -203 and KI-HARNESS-OPS-005; knowledge acquisition presents KI-PRINCIPAL-MOD-006; the five personal records wait for the personal master thread; the owning threads prune KI-PRINCIPAL-ECO-014 and KI-TOOL-RIG-CORE-059."
- **KI-AGENTS-NAME:** "Keep "agents"; ways of working logs the decision in its decisions log and nothing is renamed."
- **GO-AHEAD** (2026-10-17 14:22 BST): "hopefully, all this gets captured back into Knowledge Island in the Knowledge Base, and then there's the observatory's built, we can start to look at and understand all these in a reader-only fashion. Not everything that we do needs to be in the public set of information on the website. Although, of course, much of this would be. So, you've got permission to get on with anything."

## 2026-10-19 23:08 BST - ROADMAP-GROWTH

- **ROADMAP-GROWTH:** "the roadmap keep growing, I need to get this sorted, help me get there". Taken as: measure the territory's roadmaps and their inflow and closure, diagnose the growth, and bring Kris a burn-down plan with a few decisions. Dispatched `roadmap-census`, read-only; no record is changed until Kris decides.

## 2026-10-19 23:09 BST - PILOT-SEED-HOME

- PILOT-SEED-HOME (Kris, 19 October, under HIGH-CONFIDENCE): stage section 4 as a seed pack in `-`; carried in [state.md](state.md)'s next steps for the terra session.

## 2026-10-19 23:45 BST - ANSWERS

- **ANSWERS:** "I agree with all the recommendations in here, apart from the roadmap cap, I don't think we need one, I just think we need to focus on what we're doing now, which is to get through it." Read back as taken, option a) on eight queries and no cap on the ninth:
  - REVIEW-HOLD a): ki.agent-host, ki.estate-factorisation and ki.paperclip-capture-and-rebuild return to `+/_WORK/` on hold; CHECKLIST and the `update-ki-pin.yml` payload mismatch are copied into the live ki.baseline-rollout's parked queries; then the old ki.baseline-rollout, ki.regular.command-centre and ki.regular.skill-reviews are deleted. Dispatched `review-hold-apply`.
  - HOMELESS-STANDING a): one `homeless:` line per rule in state.md; PRFLOW, PIN, RIG-REL-PATCH and the burn-down focus routed to ki.ways-of-working for a home in a standard or `AGENTS.md`.
  - MODEL-FALLBACK a): strike it at the next mark, and treat later expired time-limited entries the same way.
  - THREADS-CHECKINS a): closed as delivered by the work model; raise again only if check-ins still feel excessive.
  - TECHNE-FOCUS a): revise the Techne Programme Hold through the Enactment Process to a focus rule, Mac Studio and agent host only, other Techné work kept as ideas, carrying forward the hold's operating bounds; Kris approves the exact wording before GDR-KI-PRINCIPAL-004 is superseded. Dispatched `techne-focus` to draft it.
  - CAPTURE-GATE a): runs never create records; the owning work's coordinator captures only a blocker, a defect seen failing or a Kris request; ideas go to Project notes; small audit fixes need no record. Added to every brief from now; method change routed to ki.ways-of-working.
  - ROADMAP-CAP: no cap and no weekly cap measure; the focus is getting through the burn-down.
  - LANE-OWNERS a): ki.tools-burndown the tools repositories and mcp-git-audit; ki.observatory apps-observatory.local, ki-design and the website's design adoption; ki.ways-of-working ki-agentic-harness, ki-principal and ki-specifications; ki.chezmoi chezmoi; ki.mac-studio-setup the agent-host hold cluster and ki-techne-harness; the 12 email-routing drafts to one hold until a Project opens (dispatched `email-routing-hold`). Route lines sent to each lane.
  - BURN-WAVE-1 a): each lane runs one `ki-accept` pass on remaining Awaiting review records and brings Kris its cancel, merge and idea list as a single query; carried in each lane's route line.

## 2026-10-19 23:48 BST - TRIAGE-ALL

- **TRIAGE-ALL:** "Okay, there's a lot of items in triage. I need them all triaging. So I want them all running out with the high order functions and anything which is High confidence recommended. Let's move it into now and get it done. Especially to focus on anything to do with the tools burn-downs first." Taken as: every lane triages all its triage records now, high-confidence adoptions go straight to Now and are delivered, the rest come to Kris; ki.tools-burndown first. IMPORTANT route lines sent to the five lanes. This was held in `state.md` while `sop-mark-2` rewrote the log.

## 2026-10-19 23:49 BST - RECEIPTS

- 23:49 BST: `email-routing-hold` received. All 12 are held (mcp-m365 `fdd6708`, mcp-gsuite `2fd5471`, not pushed), and EMAIL-OWNER is copied to queries.md for blind review. Follow-up with no record: drop the dangling `KI-MCP-M365-TOOL-010` from KI-MCP-M365-TOOL-012's `blocked_by`.
- Correction: State of play's commit `6faf8f0c` also took in `review-hold-apply`'s staged renames of the three live folders. They were content-free moves, so nothing was lost. From now on, commits carry explicit paths on the commit command itself.
- 23:49 BST: `sop-mark-2` received. The log is struck (`c3847f88`), and `design/` is unchanged. Follow-ups routed: `design/personal-acquire-handover.md` to ki.knowledge-acquisition, `design/observatory-goals/` to ki.observatory, and MGIT-ESCAPE and MGIT-OUTPUT to ki.tools-burndown as ideas.
- 23:51 BST: `review-hold-apply` received. The three live packages are back on hold in `+/_WORK/` (`e7ad9671`); CHECKLIST and PIN-PAYLOAD are parked in ki.baseline-rollout; the old ki.baseline-rollout and ki.regular.command-centre are deleted. Its SKILL-REVIEWS-DELETE query is settled under Kris's REVIEW-HOLD approval: the local `origin/main` ref, fetched at 23:22 BST, already shows the acceptance and prune, so `skill-reviews-delete` is dispatched to delete the folder and pin the KI-HARNESS-GOV-202 link.
- 23:51 BST: LANE-OWNERS return from ki.mac-studio-setup. tools-rig is that work's own scope and its `rig-triage` is already running, so tools-rig is taken off ki.tools-burndown's lane and both works have been told. ki-techne-harness is outside mac-studio's scope and under the Techne Programme Hold, so its triage waits with the on-hold ki.agent-host until the TECHNE-FOCUS wording is settled. Line removed.
- 23:53 BST: `techne-focus` received. It captured KI-PRINCIPAL-GOV-035 at State of play's request (`6143b6b0`) with the exact policy and GDR wording. Nothing canonical has changed. TECHNE-WORDING is copied to queries.md, and `query-review-4` (Codex, high) is dispatched for a blind review of it and EMAIL-OWNER. Its follow-ups (the harness and tools-techne citation sweep, and the Agent host and Techne note rewrites) wait for the approved wording.
- 23:53 BST: MARK-FOLLOWUP from ki.tools-burndown. MGIT-ESCAPE and MGIT-OUTPUT now live as ideas in its Project note; strike them at the next mark. Line removed.
- 23:54 BST: `skill-reviews-delete` received. The harness skill-reviews folder is deleted, and the KI-HARNESS-GOV-202 link is pinned to `8c5b5575` (ki-agentic-harness `aa888e33`, not pushed). REVIEW-HOLD is now fully delivered.
- 23:56 BST: `query-review-4` received, blind. It agrees on EMAIL-OWNER (raised to high: hnr.email-routing is itself paused until Kris resumes HNR work) and disagrees on TECHNE-WORDING (approve with named changes, keeping the two readiness gates). queries.md is updated, and the work goes to Kris.

## 2026-10-20 00:07 BST - ANSWERS

- **EMAIL-OWNER:** "Well, not now. I think the email owner stuff, if that's all to do with H and R, it can go to the H and R area. We don't need it in here." Taken as: no work now. The 12 email-routing records pass to Humans not Robots, owned by hnr.email-routing and held until Kris resumes HNR work. They leave the KI lanes, and a route line is sent to hnr.email-routing.
- **TECHNE-WORDING:** "Let's get on with the technique word in, yes." Taken as option a): approve both texts as drafted, retiring the two readiness gates and adding the `Idea:` storage rule. Dispatched `gov035-deliver` to take KI-PRINCIPAL-GOV-035 to Awaiting review.
- **PROGRESS-ALL:** "Can you go through any items which are triaged in knowledge islands and get them progressed? We need to move as much as we can forwards in the roadmap so it gets done." Taken as: TRIAGE-ALL stands. The ki.tools-burndown, ki.mac-studio-setup, ki.observatory and ki.chezmoi lanes are running; `roadmap-census-2` finds any repository whose triage pile has no live pass.
- **HOLD-REVALIDATE:** "And then things that are on hold, we need to re-validate everything, make sure it really is. On hold, why is anything on hold in the observatory, for example?" Taken as: re-validate every hold across the territory, answering Observatory first. Releases go to their owning works; cancellations come to Kris as one query. Dispatched as part of `roadmap-census-2`.
- 00:17 BST: `roadmap-census-2` received.
  - Triage: 28 records left, down from 58 at 23:00 BST on 19 October.
  - Holds: of the 25 KI roadmap holds, 3 are met, 2 are stale or deadlocked and 20 are valid. Every Observatory hold is real; KI-DESIGN-OBS-015 waits on an answer rather than a dependency.
  - Cancellations: none found, so HOLD-CANCEL does not go to Kris.
  - Routed under PROGRESS-ALL and HOLD-REVALIDATE: ki.observatory, ki.ways-of-working, ki.chezmoi, ki.tools-burndown, ki.regular.registry-removal and ki.paperclip-capture-and-rebuild.
  - WOW-RESUME a) is taken as covered by Kris's 20 October instruction. ki.ways-of-working needs a session to pick it up.
  - Held until KI-PRINCIPAL-GOV-035 is accepted: resume ki.agent-host, release KI-TOOL-RIG-DIST-011, KI-TECHNE-OPS-024 and KI-TOOL-TECHNE-CLI-006, and release KI-PRINCIPAL-MOD-008 to next, because its "roadmap mostly cleared" condition is met.
  - Finding: `0836bcae` (ki.baseline-rollout) swept in gov035-deliver's renames. Check at gov035-deliver's receipt.
- 00:20 BST: `gov035-deliver` received. [KI-PRINCIPAL-GOV-035](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-GOV-035-turn-the-techne-programme-hold-into-a-focus-rule.md) is at Awaiting review (`8895ff0f`, `d5522a38`). Its renames were also taken in by ki.baseline-rollout's `0836bcae`, with no loss. GOV035-ACCEPT (high) goes to Kris. TECHNE-FOLLOWUPS (medium) is sent to `query-review-5` (Codex, high) for blind review.
- 00:20 BST: CANCEL-MERGE from ki.tools-burndown, which is acceptrig's proposal to cancel KI-TOOL-RIG-DIST-011, merge KI-TOOL-RIG-CORE-056 into CORE-053, and reject CORE-057 and CORE-064. Routed to ki.mac-studio-setup, which owns tools-rig and runs its own blind review. Note the conflict: roadmap-census-2 found DIST-011 about to be met by GOV-035 rather than obsolete. Line removed.
- 00:23 BST: `query-review-5` received, blind, and agrees on TECHNE-FOLLOWUPS a), so its confidence is raised to high. Its finding: ki-principal was pushed at 00:21 BST, so the Techne repositories' links to the old policy are already broken.
- 00:23 BST: NO-GATE from ki.tools-burndown routed to ki.ways-of-working, which owns the hooks standard. That work picks it up when it resumes. Line removed.

## 2026-10-20 00:27 BST - OVERNIGHT

- **OVERNIGHT:** "I'm going to bed now. I want you to keep looking every 10 minutes to see if there's any new work for yourself in some way. And if there is, I want you to progress it. You can do anything on a high confidence level that you recommend. If you can get a good recommendation, you can move on to the next one, and as you do more and work, it might be that when you come back to ones that you couldn't get a good recommendation for, it might be more accurate. We've got autonomy to make this happen, so I'm going to leave you with this in your safe hands."
  - Taken as: until Kris returns, State of play acts on every high-confidence recommendation, its own and its runs'.
  - A medium or low query goes to a blind review. If the review agrees, it rises to high and is acted on; if not, it is parked for Kris and revisited later.
  - Destructive actions still need a review that agrees.
  - No push: Kris's standing "never push without a request" is not lifted.
  - Checks run every 10 minutes when idle, and every 5 minutes while runs are going.
- **GOV035-ACCEPT a)**, taken under OVERNIGHT: `gov035-accept` dispatched, which also releases KI-PRINCIPAL-MOD-008 to next.
- **TECHNE-FOLLOWUPS a)**, taken under OVERNIGHT: `agent-host-resume` is chained after gov035-accept.
- **WOW-RESUME a)**, taken under PROGRESS-ALL and OVERNIGHT: with no ways-of-working session open, `wow-triage` is dispatched as that package's worker.
- 00:31 BST: `gov035-accept` received. KI-PRINCIPAL-GOV-035 is accepted and done (`a54cd931`), and KI-PRINCIPAL-MOD-008 is released to next. Links are clean. `agent-host-resume` dispatched. Note: State of play's OVERNIGHT entry and briefs were taken into ki.timelines' commit `e0489e42` during a lock race. Nothing was lost.
