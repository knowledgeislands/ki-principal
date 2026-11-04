# Stock-take findings - Knowledge Islands work packages

Run `stock-take` for [ki.sop.main](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.sop.main/work.md), under Kris's MOVE-FORWARD words of about 01:55 GMT on 4 November 2026: "go and get lots of information and try to start moving forwards things overall on the Knowledge Islands of work packages". Read-only; this file is the only change.

## STOCK-TAKE - Every package, its queue and its records

**Goal:** One picture of every Knowledge Islands work package and its repositories, so State of play can launch the next authorised units.

**Scope:** The 16 packages ki.sop.main's `work.md` `covers` lists (ki.prj.agora in one line), their `messages.md`, `discussions.md` and `state.md`, the roadmap records in the KI repositories and chezmoi, and each repository's level against GitHub after a fresh `git fetch`.

**As of:** 03:56 GMT on 4 November 2026 (2026-11-04T03:56Z). Every repository checked was level with `origin/main` (0 behind, 0 ahead): ki-principal, ki-agentic-harness, tools-ki, tools-mgit, tools-rig, tools-techne, ki-techne-harness, apps-observatory.local, apps-knowledgeislands.info, apps-agora.local, packages-stoa, ki-specifications, ki-design, tools-git-almanac, homebrew-tap, the six `mcp-*` repositories and chezmoi. Message counts exclude REFRESH lines, which the next coordinator of each package takes first.

Running now under `ki-sop-main` (all relaunched 03:52 GMT): tools-ki chain run-close, then audit-hang, sub-package, granola-follow and territory-names; harness chain summary-model, then emerging-only.

### ki.sop.main - KI > SoP

| Field | Value |
| --- | --- |
| State | With worker since 3 November 03:20 GMT; mark 4 November 01:44 GMT; listening |
| Queue | 10 lines: five Stoa asks from hnr.sop.sites and hnr.sop.5ge (STOA-NO-CONSUMERS and addendum, PRINT-LAYOUT, STOA-CANCELLED, STOA-ICAL-MAPPING), four from hnr.sop.main (STOA-HANDOVER, STOA-HEADER, STOA-THEME-MENU-CONTRAST, STOA-DIAGRAM-OVERLAY, STOA-TOOLING), all waiting on STOA-HOME; plus a broken fragment (see Stale) |
| Open queries | 27: ACCEPT-KI-TOOL-RIG-CORE-070, ACCEPT-PERSONAL-DOTFILES-UE-106, ACCEPT-KI-TOOL-MGIT-CLI-032, CHAIN-QUIET, CHAIN-START-ENTER, CHAIN-START-FIRST, MAIL-ASKS, STOA-HOME, ACCESS-ADMINS-ROUTE, OBSOLETE-DROP, OLD-ORPHANS, ADOBE-SCRIPT-HOME, GITCONFIG-AUTOSTASH, CHEZMOI-FOLD, UNTRACKED-REPORTS, BOARD-CAPTURE, VALUES-HOME, STATUS-DETAIL, WHAT-I-HEARD, GOAL-SETTING, URGENT-CRITERIA, LIVENESS, MESSAGE-WORDS, BROADCAST-POINTER, FOOTER-SYNC-WORDING, RENAME-FENCE, EDA-HOME |
| Parked | 22, including ACCEPT-CHEZMOI, ACCEPT-OBSERVATORY, ESTATE-CLOSE, KA-CLOSE, AGENT-HOST, CLI006-CONFIRM, CLI006-READY |
| Records | Owns acceptance only: [KI-TOOL-MGIT-CLI-032](/Users/krisbrown/kis/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-032-chain-command.md) and [KI-TOOL-MGIT-CLI-033](/Users/krisbrown/kis/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-033-sync-push-guard.md) awaiting review (Now); [KI-TOOL-RIG-CORE-070](/Users/krisbrown/kis/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-070-handler-read-back-after-confirmation.md) awaiting review (Now) |
| Repositories | ki-principal level; 12 uncommitted entries (eight SoP briefs and `decisions.md` staged by another session, plus untracked reports) |

### ki.prj.agora - KI > Techne > Agora

| Field | Value |
| --- | --- |
| State | With worker since 4 November 01:44 GMT; its own thread is live (not swept). Two queue lines (AGORA-CALL, LISTEN-HOW); seven open queries; run mark-all-scope under `ki-prj-agora`. Records in apps-agora.local: [KI-AGORA-TRY-001](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/KI-AGORA-TRY-001-menu-bar-identity.md) awaiting review, three triage; remote branch `origin/design/agora-identity` one commit ahead of `main` (3 November) |

### ki.prj.tools-burndown - KI > Foundations > Tools burndown

| Field | Value |
| --- | --- |
| State | Handoff to worker since 3 November 03:25 GMT; released by State of play on Kris's words of 31 October 13:37 GMT, "Release it, one fix at a time"; nothing running in its own name |
| Queue | 72 lines, 11 IMPORTANT (8 REFRESH); IMPORTANT non-REFRESH: REPORTS-FOLDER, RUNHOME-FOLLOWS-REGISTRY, GRANOLA-IMPORT-FAIL, REPORTS-HOMING, DOWNLOADS-RETIRED, SUMMARY-NOW. Live tools-ki and tools-mgit asks run from TAKE-STOCK (20 October) to LOOP-PUSH-BUSY (3 November) |
| Open queries | HELD-ROADMAP-KNIP, ASK-B |
| Method | `method_read` `dacdcc33`, behind the queued REFRESH lines |
| Records | tools-ki: [KI-TOOL-KI-CLI-172](/Users/krisbrown/kis/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-172-group-vscode-workspaces-by-territory.md) triage; KI-TOOL-KI-CLI-173, 174 and 175 done, not pruned. tools-mgit: CLI-032 and CLI-033 awaiting review |
| Repositories | tools-ki level; local branches `launcher-paths` (+1, held under AUDIT-GATE's disposition), `run-close` (+3, running), stray `wow-close-done-2` (+2, 21 October) and `wow-day-impl-fix-5` (+3, 22 October), merged `wow-rel-0141`; 7 extra worktrees. tools-mgit level and clean |

### ki.prj.chezmoi - KI > Rig > chezmoi

| Field | Value |
| --- | --- |
| State | Handoff to supervisor since 24 October 20:43 GMT; nothing running |
| Queue | 48 lines, 9 IMPORTANT (7 REFRESH); IMPORTANT non-REFRESH: INTERACTIVE-QUERIES and HANDOVER-HOUSEHOLD (Kris's 1 November fold into household works, unacted), DOWNLOADS-RETIRED, SUMMARY-NOW. The rest are the scheduled-runner cluster (WAKE-SUBSTRATE, DISPATCHER, TRIAGE-HOURS, MGIT-SYNC-JOB), the 31 October repository-move lines, Orca preference lines and HNR token asks |
| Open queries | ACCEPT-UE106, UTM-SOURCE, WARP-CONTAINER, WARP-HANDLER (all with Kris since 24 October); nothing parked |
| Records | chezmoi: [PERSONAL-DOTFILES-UE-076](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/PERSONAL-DOTFILES-UE-076-always-run-latest-source.md) and [PERSONAL-DOTFILES-UE-106](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/PERSONAL-DOTFILES-UE-106-apply-tower-assistant-at-applications.md) awaiting review; UE-086 and UE-112 in progress; Now drafts UE-105, UE-107, UE-118; 21 drafts, 3 triage, 6 done not pruned. tools-rig: [KI-TOOL-RIG-CORE-047](/Users/krisbrown/kis/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md) in progress since FW-ADR (15 October) |
| Repositories | chezmoi level; branch `tower-nudge-retire` (+1, 3 November) with a worktree in `/private/tmp/ki-chezmoi-retire` |

### ki.prj.mac-studio-setup - KI > Rig > Mac Studio setup

| Field | Value |
| --- | --- |
| State | On hold since 3 November 03:10 GMT; release "when Kris opens this Project work, or ki.sop.main closes it out; coordination runs through ki.sop.main from 3 November" |
| Queue | 14 lines, 3 IMPORTANT (2 REFRESH): RIG-APP-FOOTPRINT; the retained Rig capability lines (RIG-COMMENT-KIND, RIG-NOTIFICATIONS twice, RIG-MACHINE-MANAGEMENT, RIG-CLI-CONSISTENCY, RIG-TUI, RIG-SSH-CHECK), HANDOVER-RECEIVED, HANDOVER-MAC-STUDIO, RADAR-SCHEMA, DOCTOR-NODE-PIN |
| Parked | 8: TOOLS-RIG-LANE, MGIT-PRESEED, RIG-069-PROBE, RIG-ASKS, RIG-INTAKE, UE-089-SHAPE, OLD-ORPHANS, SOL-WHATSAPP |
| Records | tools-rig: CORE-047 in progress; [KI-TOOL-RIG-CORE-068](/Users/krisbrown/kis/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-068-replaced-pf-root-ruleset-bypass.md) and [KI-TOOL-RIG-CORE-069](/Users/krisbrown/kis/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-069-dynamic-type-handler-fallback.md) draft (Now); CORE-070 awaiting review; CORE-075 and CORE-076 triage |
| Repositories | tools-rig level; stray `run/wow-accept-rig-056` (+1) and `run/wow-rework-rig-056` (+2), both 20 October; merged `run/wow-night-rig-048-f` and `run/wow-night-rig-056-e`; 4 extra worktrees. Untracked `handover.report.md` in the package |

### ki.prj.observatory - KI > Model > Observatory

| Field | Value |
| --- | --- |
| State | On hold since 3 November 03:11 GMT; release "when Kris opens this Project work, or resume; coordination runs through ki.sop.main from 3 November" |
| Queue | 31 lines, 8 IMPORTANT (5 REFRESH): OBS-LANDED-VIS030, SERVE-WATCH, PROTECTED-PUBLICATION, ACQUIRE-INTAKE-VIEW (high priority from personal.reg.acquire-intake), then 22 ordinary asks from WORK-OPENER to STRAY-REPORTS-SOL |
| Parked | 10 in priority order: PUBLICATION-ONE, ACQUIRE-VIEW, STATUS-FIRST, NEXT-TOOL, HOST-VIEW, SCHEDULED-FINDINGS, SYNC-CLOSE, DESIGN-PASS, TIDY-RUN, ESTATE-ROUTE |
| Method | `method_read` `df3f5503`, behind |
| Records | apps-observatory.local: [KI-OBSERVA-APP-044](/Users/krisbrown/kis/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md) draft (Now); VIS-032, VIS-034, VIS-045 draft (held); BRG-004 done, not pruned |
| Repositories | apps-observatory.local level; branch `z-retirement/observatory-20261030` (+3, on origin too). Untracked `blind-review-stocktake.report.md` in the package |

### ki.prj.ways-of-working - KI > Model > Ways of working

| Field | Value |
| --- | --- |
| State | On hold since 3 November 03:11 GMT (DRAIN-TO-SOP); release "when Kris opens this Project work again; coordination now runs through ki.sop.main" |
| Queue | 2 REFRESH lines only |
| Parked | 38, among them the quick wins QUICK-FIXES, QUICK-FIXES-LIFECYCLE, QUICK-FIXES-FOLDER, DONE-PRUNE and DONE-PRUNE-TOOLS-KI, and the policy set WIP-PACKAGE, WIP-TERRITORY, HOLD-CLOSE, HOLD-ROUTE, GATES |
| Records | ki-agentic-harness: KI-HARNESS-GOV-232, 233 and 234 done, not pruned; ki-principal: [KI-PRINCIPAL-MOD-011](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-MOD-011-amend-work-model-assigned-package-cascade.md) draft (Now) |
| Repositories | ki-agentic-harness level; unmerged drafts `ki-e2e` (+2, 2 November) and `orca-adapter` (+2, 1 November) in worktrees of closed runs; merged `finished-tidy`, `quiet-listen`, `rename-paperclip` still with worktrees. ki-principal: `run/wow-mod011-approved-candidate-mpg8sgz6` and `origin/wip/z-retired-mod011-20261030` (both the same two MOD-011 commits of 28 October). Untracked reports in `aside/`, `reports/` and the top level |

### ki.prj.orca-evaluation - KI > Techne > Orca evaluation

| Field | Value |
| --- | --- |
| State | On hold since 2 November 15:25 GMT; release "close-out by State of play (ki.sop.main) ... once personal.reg.assistant-terra acknowledges the handover" |
| Queue | 2 REFRESH lines |
| Parked | 5: SCOPE-SPLIT, ORCA-UPSTREAM, THREADS-TRY, THREADS-SWEEP, THREADS-FR (carried by the assistant) |
| Records | None open; no acknowledgement from assistant-terra is recorded in the package's decisions (last change `a70531f9`, 3 November) |

### ki.prj.agent-host - KI > Techne > Agent host

| Field | Value |
| --- | --- |
| State | On hold since 29 October, "more expected"; release "when Kris brings this work package back up" |
| Queue | 3 live lines (VEGA-XDG, VEGA-RIG-LINK, TS-OAUTH-PARAM), 7 REFRESH |
| Parked | 5: CLI006-PLAN, DEV-MODE, RIG-LINK, Firewall, HARNESS-INSTRUCTIONS |
| Records | ki-techne-harness: [KI-TECHNE-OPS-018](/Users/krisbrown/kis/knowledge-islands/ki-techne-harness/docs/roadmap/KI-TECHNE-OPS-018-converge-tools-through-rig.md) draft, held to 12 November; [KI-TECHNE-OPS-024](/Users/krisbrown/kis/knowledge-islands/ki-techne-harness/docs/ideas/KI-TECHNE-OPS-024-weekly-pin-bump.md) an idea, held to 12 November |
| Repositories | ki-techne-harness and tools-techne level and clean |

### ki.prj.baseline-rollout - KI > Foundations > Baseline rollout

| Field | Value |
| --- | --- |
| State | On hold since 20 October 01:05 GMT, paused; release "Kris says resume" |
| Queue | 10 live lines (HARNESS-DEFECTS, WEBSITE-SKILL, PRODUCT-RECORDS, REPO-METADATA, REPO-CODE-CAP, HARNESS-FEEDBACK, HARNESS-FEEDBACK-2, SITE-STD-GAPS, SPA-FALLBACK-SCOPE, TYPED-ID-ROLLOUT), 7 REFRESH |
| Parked | 15 rollout queries with review verdicts folded in (TMX-AREA-TITLES to ICO-DATE) |
| Records | None in KI repositories; its records sit in the other territories' repositories |

### ki.prj.portable-specifications - KI > Model > Portable specifications

| Field | Value |
| --- | --- |
| State | On hold since 20 October 01:05 GMT, paused; release "Kris says resume" |
| Queue | 7 REFRESH lines only |
| Parked | SPEC-TEXT a) and HOMING-EDITS a), both high after six blind reviews |
| Records | ki-agentic-harness ideas: [KI-HARNESS-GOV-228](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/docs/ideas/KI-HARNESS-GOV-228-home-work-spec.md), [KI-HARNESS-GOV-229](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/docs/ideas/KI-HARNESS-GOV-229-home-acquire-spec.md), [KI-HARNESS-GOV-230](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/docs/ideas/KI-HARNESS-GOV-230-knowledge-package-skill.md) |

### ki.prj.timelines - KI > Foundations > Timelines

| Field | Value |
| --- | --- |
| State | On hold since 20 October 01:04 GMT, paused; release "Kris says resume" |
| Queue | HARNESS-TRIAGE (the pruned KI-HARNESS-GOV-222 hand-off), 7 REFRESH |
| Parked | OVERNIGHT-CONFIRM a) and CAPTURE-ADOPTION a), both high |
| Records | None open; KI-HARNESS-GOV-222 is pruned |

### ki.prj.estate-factorisation - KI > Foundations > Estate factorisation

| Field | Value |
| --- | --- |
| State | On hold since 19 October 22:47 GMT; release "Kris's review of the Project close-out"; retirement prepared in [estate-factorisation-retirement.md](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.sop.main/_emerging/estate-factorisation-retirement.md) |
| Queue | 7 REFRESH lines only |
| Parked | 13 (DEPS-HOLD to PROJECT-CLOSE); several cite records since pruned (see Stale) |
| Records | [KI-TOOL-KI-CLI-125](/Users/krisbrown/kis/knowledge-islands/tools-ki/docs/ideas/KI-TOOL-KI-CLI-125-ki-release-contract.md) an idea, review 16 November |

### ki.prj.paperclip-capture-and-rebuild - KI > Techne > Paperclip capture and rebuild

| Field | Value |
| --- | --- |
| State | On hold since 20 October, paused under the Techne Programme Focus; release "the island owner taking up remote Paperclip through the Enactment Process ... or resume" |
| Queue | PAPERCLIP-OUT (Kris retired Paperclip from the personal dotfiles, 31 October), 7 REFRESH |
| Parked | None; PAPERCLIP-RETIRE stays with Kris (SoP decisions, 3 November) |

### ki.prj.website - KI > Model > Website

| Field | Value |
| --- | --- |
| State | On hold since 25 October, seeded and never opened; release "when Kris opens this Project work" |
| Queue | 5 live lines (WEBSITE-DRIFT, SITE-DEPS, STOA-PUBLIC, SITE-RENAME, ACCESS-ADMINS), 7 REFRESH |
| Records | apps-knowledgeislands.info: none open. Merged branch `ways-of-working-learn` still on origin |

### ki.reg.main - KI > Regular

| Field | Value |
| --- | --- |
| State | On hold since 18 October, more expected; release "new regular work arriving" |
| Queue | STOA-ICONS (30 October, for packages-stoa), 7 REFRESH |
| Open queries | RELEASE-GO - release Stoa with the import-cycle fix and the new icons |
| Records | packages-stoa has no roadmap; level and clean |

### ki.prj.knowledge-acquisition - KI > Model > Knowledge acquisition

| Field | Value |
| --- | --- |
| State | Finished since 20 October on Kris's KA-FINISH; its own next step: "mark closes work, delete folder in one commit"; folder still present 15 days on |

## Next units State of play may launch now

Ranked. "Chains with" names units that touch the same files and so must run one after another.

1. **Keep the two running chains going; launch nothing into tools-ki or the harness beside them.** Repository: tools-ki (run-close, audit-hang, sub-package, granola-follow, territory-names) and ki-agentic-harness (summary-model, emerging-only). Authority: SOLE-THREAD (Kris, 3 November 03:14 GMT, "if you need to get anything done, you can call them all") and KI-TOOLING-GO (3 November, about 03:35 GMT, logged as "the tooling backlog is driven by detached runs, one bounded unit per repository at a time"). Size: in flight. Waits on: nothing. Chains with: every tools-ki and harness unit below.
2. **launcher-push - publish the held launcher fix.** Repository: tools-ki, branch `launcher-paths` (`8384a731`). Authority: the review-audit-gate disposition logged on 4 November: "the fix stays unpushed on its branch, and run audit-hang fixes AUDIT-HANG ... so the audit can complete; then a run pushes it." Size: S (rebase onto `main` after run-close, rerun the gate, push). Waits on: audit-hang finishing with a completing audit. Chains with: run-close and audit-hang (same `src/agent` close and launch paths); queue it straight after audit-hang, before sub-package.
3. **burndown-sweep - work the tools-burndown queue down.** Repository: ki-principal, only `+/_WORK/ki.prj.tools-burndown/`. Authority: Kris, 31 October 13:37 GMT, "Release it, one fix at a time"; BASELINE-CLEAN (28 October), "So you need to work through them bit by bit"; SOLE-THREAD. Work: refresh `method_read`; dispose of lines already delivered or overtaken (U2-LANDED and U5-LANDED receipts; GRANOLA-IMPORT-FAIL, delivered by assistant-terra in tools-ki `8ba2574c`..`ebcc903d`; RUN-CLOSE, AUDIT-HANG, LAUNCHER-FAULTS, KI-AGENT-MOVED-HOME and PATHS-FROM-CONFIG, carried by State of play's running chain); home lines over about 60 words; leave an ordered one-fix-at-a-time list of the live ones in `state.md` for State of play to feed the tools-ki chain after territory-names. Size: M. Waits on: nothing. Chains with: nothing (package files only), but must read the running chain's briefs so it does not queue the same fix twice.
4. **orca-close - close out Orca evaluation.** Repository: ki-principal, `+/_WORK/ki.prj.orca-evaluation/`. Authority: its hold release, "close-out by State of play (ki.sop.main) ... once personal.reg.assistant-terra acknowledges the handover". Work: look for the acknowledgement in assistant-terra's package; if present, run the `ki-work-package` close-out; if absent, send one line asking for it and stop. Size: S. Waits on: the acknowledgement. Chains with: nothing.
5. **mac-studio-close-plan - prepare the Mac Studio close-out.** Repository: ki-principal, `+/_WORK/ki.prj.mac-studio-setup/`. Authority: its hold release, "or ki.sop.main closes it out", and SOLE-THREAD. Work: a retirement plan in the shape of the Estate one, mapping each of the 14 lines and 8 parked queries to a receiver (household-sol, household-terra, the tools-rig lane), with TOOLS-RIG-LANE and RIG-INTAKE raised as the gating queries; no routing until they are answered. Size: M. Waits on: nothing for the plan; TOOLS-RIG-LANE for the close itself. Chains with: nothing.
6. **observatory-sweep - classify the Observatory queue, delivering nothing.** Repository: ki-principal, `+/_WORK/ki.prj.observatory/`. Authority: HAND-TO-SOP (Kris, 3 November about 03:10 GMT, "move all of the work to be coordinated through the SOP main") and the package's own next step 1, "ki.sop.main acknowledges in package's decisions and takes up queue and discussions"; OBSERVATORY-THREAD (28 October) keeps opening with Kris: "State of play does not open or release it for him". Work: refresh `method_read`, mark lines done or overtaken with evidence, leave the rest for opening. Size: M. Waits on: nothing. Chains with: unit 7 (same package files).
7. **path-repoint - finish the `~/kis` repoint.** Repository: ki-principal. Authority: the handover-intake run's repoint of 121 files to `~/kis` (3 November), under SOLE-THREAD; a mechanical follow-up. Work: nine package files still cite `/Users/krisbrown/workspaces/`: ki.sop.main `discussions.md`; ki.prj.website, ki.prj.observatory, ki.prj.chezmoi, ki.prj.baseline-rollout and ki.reg.main `messages.md`; ki.prj.observatory `discussions.md`; ki.prj.chezmoi `state.md`; ki.prj.knowledge-acquisition `decisions.md`. Leave pinned GitHub links and quoted history alone. Size: S. Waits on: units 3 and 6. Chains with: units 3, 6 and 8, and the coordinator's own edits to ki.sop.main.
8. **ka-close - close the finished Knowledge acquisition folder.** Repository: ki-principal. Authority: KA-FINISH (Kris, 20 October) and the coordinator style's rule that territory work closes "a finished work's folder, which it closes itself under the `ki-work-package` close-out". The parked KA-CLOSE query says the opposite ("State of play may not remove another work's folder on its own"), so the coordinator should confirm the style rule governs before launching, and drop KA-CLOSE as settled when it does. Size: S. Waits on: that confirmation. Chains with: unit 7.
9. **Coordinator's own one-line fix: the orphaned fragment in ki.sop.main's `messages.md`** (see Stale). Not a run.

Units State of play may not launch now: anything in ki.prj.chezmoi (with Kris, CHEZMOI-FOLD open); delivery in apps-observatory.local, ki-techne-harness, tools-techne, apps-knowledgeislands.info or packages-stoa (their packages are held for Kris to open, or the Stoa Project does not exist yet); the paused baseline-rollout, portable-specifications and timelines work ("Kris says resume"); agent-host (held to 12 November); every acceptance, prune and cancellation.

## Queries for Kris

The 27 open State of play queries listed above stand. The quickest to move work forward: the ACCEPT bundle (ACCEPT-KI-TOOL-MGIT-CLI-032 with CHAIN-QUIET, CHAIN-START-ENTER and CHAIN-START-FIRST, then ACCEPT-KI-TOOL-RIG-CORE-070 and ACCEPT-PERSONAL-DOTFILES-UE-106); STOA-HOME, which unblocks ten queued Stoa lines and RELEASE-GO; CHEZMOI-FOLD, which unblocks 48 lines; and OBSOLETE-DROP. New queries from this stock-take:

### ACCEPT-KI-TOOL-MGIT-CLI-033 - Accept the sync push guard

**Context:** [KI-TOOL-MGIT-CLI-033](/Users/krisbrown/kis/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-033-sync-push-guard.md) (`mgit sync` pushes only with `--push`, which Kris adopted after a blind review on 25 October) was delivered on 31 October (tools-mgit `f67e255`) and is awaiting review. Its only acceptance question sits among Ways of working's parked queries, and State of play has no ACCEPT query for it, though ACCEPT-BUNDLE (Kris, 20 October) has State of play bring every record awaiting acceptance "as the first point of call".

**Query:** Should State of play add this record to the `mgit` acceptance with KI-TOOL-MGIT-CLI-032?

**Options:**

a) (recommended, confidence high - the same repository and reviewer as CLI-032, and ACCEPT-BUNDLE asks for exactly this) Add ACCEPT-KI-TOOL-MGIT-CLI-033 beside ACCEPT-KI-TOOL-MGIT-CLI-032, oldest first, with a fresh review-prep run before you accept through `ki-accept`.

b) Leave it with Ways of working until that work opens again.

### STALE-ACCEPTS - Drop four acceptance queries whose records are already accepted

**Context:** Four parked State of play queries ask Kris to accept records that were accepted and pruned on 27 October: [KI-WEBSITE-SITE-044 (pruned)](https://github.com/knowledgeislands/apps-knowledgeislands.info/blob/ae886e2b/docs/roadmap/KI-WEBSITE-SITE-044-design-v1.md) in apps-knowledgeislands.info `fdc1ac2`, [KI-PRINCIPAL-OPS-014 (pruned)](https://github.com/knowledgeislands/ki-principal/blob/1fba2fb7/Streams/Roadmap/KI-PRINCIPAL-OPS-014-gfm-conversion.md) and [KI-PRINCIPAL-MOD-009 (pruned)](https://github.com/knowledgeislands/ki-principal/blob/1fba2fb7/Streams/Roadmap/KI-PRINCIPAL-MOD-009-amend-adr-001-staging-wording.md) in ki-principal `a88b2f92`, and [KI-TOOL-RIG-CORE-062 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/14715c30/docs/roadmap/KI-TOOL-RIG-CORE-062-own-address-firewall-destination.md) in tools-rig `033d952`, each "chore(roadmap): prune ... done work records". I checked each deletion commit directly. OBSOLETE-DROP, still open, asks the general version of this question.

**Query:** May State of play drop ACCEPT-KI-WEBSITE-SITE-044, ACCEPT-KI-PRINCIPAL-OPS-014, ACCEPT-KI-PRINCIPAL-MOD-009 and ACCEPT-KI-TOOL-RIG-CORE-062, logging each prune commit?

**Options:**

a) (recommended, confidence high - the prune commits show each record done and gone, and dropping a query changes no record) Drop the four, one decisions-log line each citing its commit, and treat this as part of OBSOLETE-DROP a).

b) Keep them parked until you answer OBSOLETE-DROP.

### BRANCH-SWEEP - Clear merged branches and the worktrees of finished runs

**Context:** Every repository is level with GitHub, but finished runs left branches and working copies behind. Merged into `main` and safe to remove by Git's own check: ki-agentic-harness `finished-tidy`, `quiet-listen` and `rename-paperclip`; tools-ki `wow-rel-0141`; tools-rig `run/wow-night-rig-048-f` and `run/wow-night-rig-056-e`; the remote `ways-of-working-learn` in apps-knowledgeislands.info. Most still have a worktree (a second working copy of the repository) under `~/.local/state/ki/agents/` or `$TMPDIR`, from Ways of working runs that `ki agent status` no longer lists. I did not check those worktrees for uncommitted files.

**Query:** Should one housekeeping run remove the merged branches and their worktrees?

**Options:**

a) (recommended, confidence medium - the branches are proven merged, but the worktrees' contents are unchecked; not yet blind-reviewed) One bounded run checks each worktree is clean, removes clean ones with `git worktree remove` and their merged branches with `git branch -d`, and lists any dirty one for you without touching it.

b) Leave them until each owning Project closes.

### UNMERGED-STRAYS - Decide the unmerged branches finished runs left

**Context:** Eight branches hold commits not on `main`, from runs that have finished: tools-ki `wow-close-done-2` and `wow-day-impl-fix-5` (21 and 22 October, `ki agent` recovery fixes); ki-agentic-harness `ki-e2e` and `orca-adapter` (1 and 2 November, draft skills); tools-rig `run/wow-accept-rig-056` and `run/wow-rework-rig-056` (20 October, KI-TOOL-RIG-CORE-056 evidence); apps-observatory.local `z-retirement/observatory-20261030` (30 October retirement evidence, also on GitHub); ki-principal `run/wow-mod011-approved-candidate-mpg8sgz6`, the same two commits as GitHub's `wip/z-retired-mod011-20261030` (28 October, KI-PRINCIPAL-MOD-011 candidate); chezmoi `tower-nudge-retire` (3 November). Some may be superseded by later work on `main`; none has been compared.

**Query:** Should a read-only run compare each branch with `main` and bring you a keep, merge or drop list?

**Options:**

a) (recommended, confidence high - read-only, and nothing is lost while you decide) One read-only run reports, per branch, whether `main` already carries its change, which work owns it and a recommended disposition; nothing is deleted.

b) Leave them for each owning Project.

### RESUME-SPECS - Resume Portable specifications

**Context:** [ki.prj.portable-specifications](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.portable-specifications/state.md) has been paused since 20 October, released only when Kris says resume. Its draft 0.8 specifications passed six blind reviews, the last finding nothing, and its two parked queries, SPEC-TEXT and HOMING-EDITS, are both recommended at high confidence. Resuming means planning KI-HARNESS-GOV-229 and KI-HARNESS-GOV-230 to Ready in the harness, which the summary-model and emerging-only chain also edits. Timelines and Baseline rollout are paused the same way, with two and fifteen parked queries.

**Query:** Should Portable specifications resume now, with the other two paused works left as they are?

**Options:**

a) (recommended, confidence medium - it is the readiest paused work, but whether to spend owner attention on it now is your call; not yet blind-reviewed) Resume Portable specifications only: put SPEC-TEXT and HOMING-EDITS to you, then plan its harness records after the harness chain finishes.

b) Keep all three paused until the open method queries are settled.

## Stale, overtaken or broken

- **Broken queue line.** [ki.sop.main messages](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.sop.main/messages.md) ends with an orphaned numbered list ("Full board, not a delta", "Removing done items", "The table's shape") and "Please write it into `ki-coordination` ... Kris will talk to you directly about it", with no head line. It is the body of a STATUS-FORM line the 4 November restart entry removed ("Their lines are removed"). A one-line mechanical fix for the coordinator.
- **Stale hold.** ki.sop.main `state.md` holds CLI-FIELDS "until ki.prj.tools-burndown releases KI-TOOL-KI-CLI-155"; that record was done and pruned on 19 October (tools-ki `4b1ac882`), and tools-burndown was released on 3 November.
- **Overtaken parked queries.** The four acceptance queries in STALE-ACCEPTS. In ki.prj.agent-host, RIG-LINK: `~/.local/bin/rig` now points at `/Users/krisbrown/kis/knowledge-islands/tools-rig/bin/rig`, so the broken link is fixed; CLI006-PLAN, already recommended "drop it at release as settled". In ki.prj.estate-factorisation, DOCK says KI-TOOL-RIG-CORE-042 "stays Ready / Now", but it was done and pruned on 19 October (tools-rig `be2ae7a`); STORE-REPAIR and HOST-GUARDS cite KI-TOOL-KI-CLI-126 and KI-TOOL-TECHNE-CLI-006, both pruned. ESTATE-CLOSE's retirement plan should be read against these.
- **Overtaken scope.** BASELINE-CLEAN (28 October) excluded ki.prj.ways-of-working and ki.prj.observatory; HAND-TO-SOP and SOLE-THREAD (3 November) brought both under State of play's coordination.
- **Unacted IMPORTANT line.** HANDOVER-HOUSEHOLD (1 November) in ki.prj.chezmoi: Kris's fold into the household works, now the open CHEZMOI-FOLD query. ki.prj.chezmoi has been with Kris since 24 October with four answerable queries.
- **Long-running record.** KI-TOOL-RIG-CORE-047 in progress since FW-ADR (15 October), "with ki.prj.chezmoi", which is itself with Kris.
- **Method behind.** ki.prj.tools-burndown at `dacdcc33` and ki.prj.observatory at `df3f5503`, against State of play's `f85ce21a`.
- **Finished folder not closed.** ki.prj.knowledge-acquisition, Finished since 20 October.
- **Done records not pruned.** tools-ki KI-TOOL-KI-CLI-173 to 175, ki-agentic-harness KI-HARNESS-GOV-232 to 234 (DONE-PRUNE and DONE-PRUNE-TOOLS-KI parked in Ways of working), apps-observatory.local KI-OBSERVA-BRG-004, and six chezmoi records.
- **Regular work held but live.** ki.reg.main is On hold "more expected", yet carries the open RELEASE-GO query and the STOA-ICONS line.
- **Uncommitted files in ki-principal.** Eight SoP briefs and `decisions.md` are staged by another session; untracked reports sit in ki.prj.mac-studio-setup, ki.prj.observatory, ki.prj.ways-of-working and ki.sop.main (`_emerging/eda-home.report.md`, `review-audit-gate.report.md`, `review-rename-eda.report.md`, `aside/`). This run touched none of them.
- **Stranded worktrees.** Four in ki-agentic-harness, five in tools-ki, four in tools-rig, from runs no longer listed by `ki agent status`; one chezmoi worktree in `/private/tmp`. See BRANCH-SWEEP and UNMERGED-STRAYS.
