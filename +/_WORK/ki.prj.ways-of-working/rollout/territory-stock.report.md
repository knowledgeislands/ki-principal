# [Model](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › territory-stock

**🤖 → 👤 Handoff to supervisor · Run report at 01:58 GMT · last mark 01:41 GMT**

---

## Done

- Took stock of the Knowledge Islands territory, read-only, under AWAY-1-NOV: 16 work packages, 23 checkouts, every roadmap record and the territory audits. Nothing changed, nothing committed.
- Work-package audit on ki-principal: FAIL, 28 failures and 145 warnings; detail in Findings PKG.
- Repository audits on 21 KI repositories: 1 passes (ki-agentic-harness); 19 fail, mostly on three new commit-gate rules; packages-stoa has no `.ki.toml` and cannot be audited; the tools-ki audit hung, timing out at 400 s and then again at 900 s.
- Repositories: every local `main` equals `origin/main` as last fetched (01:30 to 01:42 GMT; no fetch made). Only ki-principal is dirty, with six untracked files from other runs or sessions, named below and not touched.
- Roadmap: 10 live records across the territory, none Ready, none plannable without Kris. No delivery wave is eligible (Findings WAVES).

## In Progress

Nothing is running. The second tools-ki audit was stopped at 01:58 GMT, unfinished; tools-ki was left clean.

Outstanding - no action requested now:

- ki-principal untracked files, from other runs or sessions, left as found: `+/_WORK/ki.prj.observatory/blind-review-stocktake.report.md`, `+/_WORK/ki.prj.ways-of-working/holding-wording.report.md`, `+/_WORK/ki.prj.ways-of-working/review-finished-tidy.report.md`, `+/_WORK/ki.prj.ways-of-working/wow-cleanup.report.md`, `+/_WORK/ki.prj.ways-of-working/reports/hold-request-20261030-z.md`, `+/_WORK/ki.prj.ways-of-working/reports/z-session-retirement-20261030.md`.
- 34 finished run state folders under `~/.local/state/ki/agents/ki-project-ways-of-working/` are not yet closed with `ki agent close`.

## Findings

### THREADS - Live work packages and the main threads

**Goal:** every package's id, state, holder, waiting messages, open queries, runs and breakage. **Scope:** `ki-principal/+/_WORK/`, `ki agent status`, `ki agent prompts` (run from ki-principal), `ki repo audit --skill ki-work-package`. **As of:** 01:44 to 01:56 GMT, 1 November 2026, ki-principal `d7309bc0`.

Main threads, the six packages not on hold (Kris spoke of five; read as ways-of-working plus these five or as these five beside it): [ki.sop.main](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.sop.main/work.md), [ki.prj.chezmoi](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.chezmoi/work.md), [ki.prj.mac-studio-setup](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.mac-studio-setup/work.md), [ki.prj.observatory](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.observatory/work.md), [ki.prj.orca-evaluation](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.orca-evaluation/work.md), and this one, [ki.prj.ways-of-working](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/work.md).

| Work | State · since | Holder | Messages (IMPORTANT) | IMPORTANT waiting | Open / parked queries | Runs | Broken (audit) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ki.sop.main | with-supervisor · 30 Oct 01:51 | Kris | 8 (2) | REFRESH 31 Oct, PAPERCLIP-HOLD 1 Nov | 12 / 22 | none | `state.md` headings and empty Next steps; one message line with no tag (the ways-of-working line of 1 Nov on DESKTOP-RESET and BACKUPS-DELETE); 12 open queries over the cap of 8; 3 received reports due for pruning with unlinked record ids |
| ki.prj.chezmoi | handoff-to-supervisor · 24 Oct 20:43 | Kris | 35 (5) | REFRESH 28 Oct, REFRESH 31 Oct ×3, INTERACTIVE-QUERIES | 4 / 0 (ACCEPT-UE106, UTM-SOURCE, WARP-CONTAINER, WARP-HANDLER) | none | IMPORTANT lines below ordinary ones; 4 lines waiting more than 7 days; handed to Kris a week ago |
| ki.prj.mac-studio-setup | handoff-to-supervisor · 30 Oct 02:04 | Kris | 12 (2) | RIG-APP-FOOTPRINT 22 Oct, REFRESH 31 Oct | 3 / 11 | none | `hold: null` should be absent; `design/adobe-remove.sh` outside the closed list; 6 lines waiting more than 7 days; received reports due for pruning |
| ki.prj.observatory | with-supervisor · 1 Nov 00:58 | Kris | 23 (5) | OBS-LANDED-VIS030, SERVE-WATCH, PROTECTED-PUBLICATION, ACQUIRE-INTAKE-VIEW, REFRESH | 10 / 0 | none | `queries.md` headings; one malformed message line; two reports at top level; spent briefs `stocktake` and `blind-review-stocktake`; 10 open queries over the cap; 7 lines waiting more than 7 days |
| ki.prj.orca-evaluation | with-supervisor · 1 Nov 01:34 | Kris | 1 (1) | REFRESH 31 Oct | 2 / 0 | none | decisions log has 18 entry lines before its first `##` heading (close gate warning) |
| ki.prj.ways-of-working | with-worker · 1 Nov 01:41 | worker (this thread) | 6 (0) | none | 50 / 20 | territory-stock (this run) | three reports at top level; `.DS_Store` and two untracked `reports/*.md` not named `.report.md`; spent briefs; `queries.md` headings and an AGENDA entry not in query shape; decisions log 1,143 lines (soft limit 400); design notes without `note_type`; 50 open queries over the cap |
| ki.prj.agent-host | on-hold (more-expected) · 29 Oct | nobody | 7 (4) | REFRESH ×4 | 0 / 5 | none | IMPORTANT lines below ordinary ones |
| ki.prj.baseline-rollout | on-hold (paused) · 20 Oct | nobody | 14 (4) | REFRESH ×4 | 0 / 7 | none | IMPORTANT lines below ordinary ones |
| ki.prj.estate-factorisation | on-hold (paused) · 19 Oct | nobody | 4 (4) | REFRESH ×4 | 0 / 8 | none | none beyond long lines |
| ki.prj.knowledge-acquisition | finished · 20 Oct | nobody | 0 | none | 0 / 0 | none | finished folder still standing; State of play closes it at a mark |
| ki.prj.paperclip-capture-and-rebuild | on-hold (paused) · 20 Oct | nobody | 5 (4) | REFRESH ×4 | 0 / 0 | none | IMPORTANT lines below ordinary ones |
| ki.prj.portable-specifications | on-hold (paused) · 20 Oct | nobody | 4 (4) | REFRESH ×4 | 0 / 2 | none | none beyond long lines |
| ki.prj.timelines | on-hold (paused) · 20 Oct | nobody | 5 (4) | REFRESH ×4 | 0 / 2 | none | IMPORTANT lines below ordinary ones |
| ki.prj.tools-burndown | on-hold (paused) · 20 Oct | nobody | 55 (6) | RESUME 31 Oct, REFRESH ×4, REPORTS-FOLDER 1 Nov | 0 / 2 | none | IMPORTANT lines below ordinary ones |
| ki.prj.website | on-hold (paused) · 25 Oct | nobody | 9 (4) | REFRESH ×4 | 0 / 0 | none | IMPORTANT lines below ordinary ones |
| ki.reg.main | on-hold (more-expected) · 18 Oct | nobody | 5 (4) | REFRESH ×4 | 1 / 0 | none | IMPORTANT lines below ordinary ones |

Cross-package breakage:

- `ki agent prompts knowledge-islands`, as the brief gives it, fails: "territory knowledge-islands is not declared by a registered Capital" (also for `ki` and `knowledgeislands`). It works with no argument from inside ki-principal and with `ki.sop.main`. The territory handle (the `.ki.toml` `territory_prefix`) does not resolve: a tools-ki or registry defect.
- 116 files in `+/_WORK/` carry 804 absolute links to `/Users/krisbrown/kis/knowledge-islands/...`, which no longer exists since the move to `~/kis/`; the coordinator output style's own example heading uses it too.
- The REFRESH lines pile up in the on-hold packages (three or four each), appended below ordinary lines, so every on-hold package fails "IMPORTANT lines stand above every ordinary line". The sender, not the receiver, put them there.
- No other run group in the territory is live; `ki agent status` shows only this run here (personal tower runs are outside the territory).

### REPOS - Repositories: clean, level, checks

**Goal:** each repository's dirt, level with `origin/main` and failing checks. **Scope:** the 23 checkouts under `/Users/krisbrown/kis/knowledge-islands/`, local refs only (last fetch 01:30 to 01:42 GMT), `ki repo audit` on each. **As of:** 01:48 to 01:56 GMT, 1 November 2026.

| Repository | `main` | Level | Dirty | Audit (repository level) | Failing checks |
| --- | --- | --- | --- | --- | --- |
| apps-knowledgeislands.info | e8f986b | level | clean | FAIL 3 | FILES-6, SCR-11 |
| apps-observatory.local | 96f999a | level | clean | FAIL 2 | FILES-6, SCR-11 |
| homebrew-tap | d016ffa | level | clean | FAIL 2 | FILES-6, GATE-1 |
| ki-agentic-harness | fd3403b4 | level | clean | PASS (156 warnings) | none |
| ki-design | 6fe3557 | level | clean | FAIL 14 | FILES-6, SCR-11, PKG-6, ROUTE-1 (`docs/spec` retired root) |
| ki-principal | d7309bc0 | level | 6 untracked (others') | FAIL 67 | SCR-11, PKG-6, GATE-1, NOTE-1c, the package failures above, COORD-7 unlinked ids in received reports |
| ki-specifications | 03490bc | level | clean | FAIL 2 | FILES-6, GATE-1 |
| ki-techne-harness | e17563a | level | clean | FAIL 3 | FILES-6, SCR-11, PKG-6 |
| mcp-acquire-whatsapp | 643c5de | level | clean | FAIL 4 | FILES-6, SCR-11, PKG-6, TEST-5 (branch coverage 99.97% < 100%) |
| mcp-git-audit | 75d31e8 | level | clean | FAIL 3 | FILES-6, SCR-11, PKG-6 |
| mcp-gsuite | e410311 | level | clean | FAIL 4 | FILES-6, SCR-11, PKG-6, TEST-5 (1 failing test) |
| mcp-housekeeping-chatgpt | 6d89060 | level | clean | FAIL 3 | FILES-6, SCR-11, PKG-6 |
| mcp-housekeeping-claude | d1a3639 | level | clean | FAIL 4 | FILES-6, SCR-11, PKG-6, TEST-5 (audit-log rotation test, ENOENT) |
| mcp-ki-kb-fs | b989558 | level | clean | FAIL 3 | FILES-6, SCR-11, PKG-6 |
| mcp-m365 | 110a2be | level | clean | FAIL 3 | FILES-6, SCR-11, PKG-6 |
| packages-stoa | b4bf2d4 | level | clean | not run | no `.ki.toml` |
| tools-git-almanac | e00938b | level | clean | FAIL 3 | FILES-6, SCR-11, PKG-6 |
| tools-ki | 2970714c | level | clean | unknown | audit hung past 400 s and 900 s |
| tools-mgit | f67e255 | level | clean | FAIL 2 | FILES-6, SHELL-HOOK (same check-only gate as GATE-1) |
| tools-rig | e190ae3 | level | clean | FAIL 1 | FILES-6 |
| tools-techne | f860979 | level | clean | FAIL 3 | FILES-6, SCR-11, PKG-6 |

The three fleet-wide failures are new commit-gate rules, not regressions in code: FILES-6, `.gitignore` managed blocks not reconciled (17 repositories); SCR-11, the pre-commit hook must run `lint-staged` then `syncpack format --check` and nothing else (14); PKG-6, lint-staged must not `--write` or `--fix` at commit time (12). GATE-1 (ki-principal, homebrew-tap, ki-specifications) is the same check-only gate failing on a `quiet_audit` in the hook. Remote CI was not read (no network).

Leftover worktrees and branches, from earlier runs (no stash anywhere):

| Repository | Item | Unique commits | Landed? |
| --- | --- | --- | --- |
| ki-agentic-harness | sibling checkouts `ki-agentic-harness-finished-tidy`, `ki-agentic-harness-quiet-listen` in the territory folder | 0 | yes, both at `fd3403b4` |
| ki-agentic-harness | `rename-paperclip` worktree in this thread's temp folder | 0 (4 behind) | yes |
| apps-knowledgeislands.info | branch `ways-of-working-learn` | 0 | yes |
| tools-ki | worktree `wow-rel-0141`, detached worktrees `legacy` and `reproductions` | 0 | yes |
| tools-ki | `wow-close-done-2`, `wow-day-impl-fix-5` | 2 and 3 | partly: `6c498f3a` and `eb0e8b2e` are on main under other hashes; `6c4d2a1a` is not patch-equivalent to what landed |
| tools-rig | `run/wow-night-rig-048-f`, `run/wow-night-rig-056-e` | 0 | yes |
| tools-rig | `run/wow-accept-rig-056`, `run/wow-rework-rig-056` | 1 and 2 | superseded: KI-TOOL-RIG-CORE-056 was accepted and pruned on main |
| apps-observatory.local | `z-retirement/observatory-20261030` | 3 (Z retirement evidence) | no |
| ki-principal | `run/wow-mod011-approved-candidate-mpg8sgz6` | 2 ("ready MOD-011 isolated candidate plan", "prepare approved MOD-011 review candidate"), 701 behind | no |

### ROADMAP - Adopted Now or Next drafts, Ready and in-flight records

**Goal:** each live record's id, title, owning work, dependencies, size and any decision Kris has not made. **Scope:** `docs/roadmap/` in every repository and `ki-principal/Streams/Roadmap/`; `docs/ideas/` checked for stray live metadata. **As of:** 01:58 GMT, 1 November 2026.

No record in the territory is Ready.

| Record | Title | Status · horizon | Owning work | Size | Depends on | Needs a decision Kris has not made |
| --- | --- | --- | --- | --- | --- | --- |
| [KI-PRINCIPAL-MOD-011](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-MOD-011-amend-work-model-assigned-package-cascade.md) | Amend work model cascade | draft · now | ki.prj.ways-of-working | m | none recorded | yes: Kris's Enactment review of the exact wording and plan; STEWARD-FIELD stays open. An unlanded branch already holds a Ready plan and an "approved" candidate |
| [KI-OBSERVA-APP-044](/Users/krisbrown/kis/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md) | Instrument restructure decision | draft · now | ki.prj.observatory | m | none | yes: a `decide` record; convergence, Council-first or Waiting-first, each step on Kris's own go |
| [KI-DESIGN-ART-002](/Users/krisbrown/kis/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ART-002-art-licensing.md) | Art-licensing decision | draft · now | none named (ki-design) | s | none | yes: who owns the generated art and under what licence, for a public repository |
| [KI-TECHNE-OPS-018](/Users/krisbrown/kis/knowledge-islands/ki-techne-harness/docs/roadmap/KI-TECHNE-OPS-018-converge-tools-through-rig.md) | Converge tools through Rig | draft · now (partial awaiting review) | ki.prj.agent-host (on hold) | l | gated: Rig installs `ki`'s signed release; a clean `rig status` through one pin bump | release and install gates, outside the window |
| [KI-TOOL-RIG-CORE-068](/Users/krisbrown/kis/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-068-replaced-pf-root-ruleset-bypass.md) | pf root ruleset bypass | draft · now | Rig theme, ki.prj.mac-studio-setup | m | Kris's attended NordVPN check; follows KI-TOOL-RIG-CORE-047 | yes: attended check; firewall is connection-critical |
| [KI-TOOL-RIG-CORE-069](/Users/krisbrown/kis/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-069-dynamic-type-handler-fallback.md) | Dynamic-type handler fallback | draft · now | Rig theme, ki.prj.mac-studio-setup | s | RIG-069-PROBE, an attended probe on sol | yes: Kris must authorise and attend the probe |
| [KI-TOOL-RIG-CORE-047](/Users/krisbrown/kis/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md) | Tailnet-only listener firewall | in-progress · now | Rig theme | - | sol's attended re-apply | attended, connection-critical |
| [KI-TOOL-RIG-CORE-070](/Users/krisbrown/kis/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-070-handler-read-back-after-confirmation.md) | Handler read-back after confirmation | awaiting-review · now | Rig theme | s | none | acceptance |
| [KI-TOOL-MGIT-CLI-032](/Users/krisbrown/kis/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-032-chain-command.md) | Chain Git commands | awaiting-review · now | none named | m | none | acceptance |
| [KI-TOOL-MGIT-CLI-033](/Users/krisbrown/kis/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-033-sync-push-guard.md) | Guard sync pushes | awaiting-review · now | none named | m | none | acceptance |

Out of the queue: the 27 October roadmap sweep moved records to `docs/ideas/`, and four of them still say `now` or `next`: [KI-DESIGN-ELE-001](/Users/krisbrown/kis/knowledge-islands/ki-design/docs/ideas/KI-DESIGN-ELE-001-lit-ssr-spike.md), [KI-HARNESS-GOV-227](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/docs/ideas/KI-HARNESS-GOV-227-repository-storage-declarations.md), [KI-HARNESS-OPS-009](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/docs/ideas/KI-HARNESS-OPS-009-complete-ai-session-acquisition.md) and [KI-TOOL-KI-CLI-139](/Users/krisbrown/kis/knowledge-islands/tools-ki/docs/ideas/KI-TOOL-KI-CLI-139-ebu-sources-sync.md); [KI-TECHNE-OPS-024](/Users/krisbrown/kis/knowledge-islands/ki-techne-harness/docs/ideas/KI-TECHNE-OPS-024-weekly-pin-bump.md) is `ready` with horizon `hold`. None is adopted Now or Next work; bringing one back is Kris's adoption.

The roadmap is small: 10 live records. The territory's real backlog is in the message queues (about 190 lines, 55 in tools-burndown and 35 in chezmoi) and the open queries (about 80, 50 in ways-of-working).

### FIXES - Good working order, each with the package whose authority covers it

**Goal:** the fixes that put the territory in good working order without deciding anything. **Scope:** the findings above; authority read from AWAY-1-NOV and the coordination standard (a work's coordinator tidies its own package; other works get one `messages.md` line). **As of:** 01:58 GMT, 1 November 2026.

| # | Fix | Authority | Tier |
| --- | --- | --- | --- |
| 1 | Tidy this package: home the three top-level reports into `reports/` once received, remove `.DS_Store`, prune spent briefs and received reports, put AGENDA in query shape or move it to `state.md`, fix `queries.md` headings, add `note_type` to design notes, strike decisions a durable home now carries (log 1,143 lines) | ki.prj.ways-of-working | push |
| 2 | Decide what to do with the two untracked `reports/hold-request-20261030-z.md` and `reports/z-session-retirement-20261030.md` (Z retirement, another session's output): receive and home them, or leave for their owner | ki.prj.ways-of-working, after checking who wrote them | push |
| 3 | Close this thread's 34 finished runs with `ki agent close`, which also removes the `rename-paperclip` and `wow-rel-0141` worktrees; remove the two landed sibling checkouts `ki-agentic-harness-finished-tidy` and `-quiet-listen` and the landed branches in the table above through a bounded run | ki.prj.ways-of-working (its own runs) | push |
| 4 | Fix the one tag-less message line this thread wrote into ki.sop.main on 1 Nov, by replacing it with a well-formed line; and in each on-hold package move this thread's own IMPORTANT REFRESH lines above the ordinary lines | ki.prj.ways-of-working (sender of those lines) | push |
| 5 | Root cause of fix 4: the appender adds IMPORTANT lines at the bottom; send the fix to the harness method and to tools-ki | ki.prj.ways-of-working, message line to ki.prj.tools-burndown | push |
| 6 | Message lines naming the audit failures to ki.sop.main (state headings, Next steps, received reports), ki.prj.observatory (headings, malformed line, top-level reports, spent briefs), ki.prj.mac-studio-setup (`hold: null`, `adobe-remove.sh`, reports), ki.prj.orca-evaluation (decisions log shape) and ki.prj.chezmoi (queue order) | ki.prj.ways-of-working, one line each | push |
| 7 | `ki agent prompts knowledge-islands` fails to resolve the territory handle | message line to ki.prj.tools-burndown (tools-ki), held | push |
| 8 | 804 stale `/Users/krisbrown/workspaces/knowledge-islands` links in 116 package files and in the coordinator output style | each package for its own files; MOVE-LINKS is with ki.prj.chezmoi; the output style through ki.prj.ways-of-working's harness route | push |
| 9 | Fleet commit-gate conform (FILES-6, SCR-11, PKG-6, GATE-1) in 19 repositories, one bounded run per repository | ki.prj.ways-of-working under HOOK-STASH (1 Nov) and RED-MAIN, if the query CONFORM-SCOPE is answered yes | push |
| 10 | Red tests in mcp-acquire-whatsapp, mcp-gsuite and mcp-housekeeping-claude (TEST-5); retired `docs/spec` root in ki-design (ROUTE-1) | RED-MAIN ("Fix mains first") under ki.prj.ways-of-working | push |
| 11 | Find why the tools-ki audit hangs | ki.prj.ways-of-working, read-only investigation | read-only |
| 12 | Close the finished ki.prj.knowledge-acquisition folder | ki.sop.main at an owner-authorised mark; message line only | message |

### WAVES - Proposed `ki-batch` delivery waves

**Goal:** waves of one repository each, Ready records first, then drafts to plan, honouring dependencies and the owner-queue cap. **Scope:** the ROADMAP table; the owner-queue cap of eight open queries and eight records awaiting acceptance per work. **As of:** 01:58 GMT, 1 November 2026.

No delivery wave is eligible tonight. There is no Ready record, and every Now draft needs a decision Kris has not made or an attended step. Separately, ways-of-working (50 open queries), Observatory (10) and State of play (12) are over the eight-query cap, under which no new build or planning run starts in that work until Kris catches up; backlog-clearing work stays allowed.

Proposed order, as the window's work instead of waves:

1. Wave 0, ki-principal, ki.prj.ways-of-working: fixes 1 to 4 and 6 (package tidy, run close-out, message lines). Backlog-clearing, so allowed over the cap. Size s.
2. Wave 1, one repository per run, about three at once: fix 10 (red tests in the three mcp repositories), then fix 9 (commit-gate conform), ki-principal last because other sessions' untracked files sit there. Waits on CONFORM-SCOPE for fix 9. Size s each.
3. Wave 2, ki-agentic-harness: the decided discussions rollout harness step (readers accept both names) and fix 5. Waits on CAP-DECIDED.
4. Wave 3: message lines to tools-ki and the Observatory for the decided follow-ups, and fix 7.

### EXCLUDED - What stays out, and why

**Goal:** everything left untouched, with its reason. **Scope:** the ROADMAP and FIXES tables against AWAY-1-NOV's exclusions. **As of:** 01:58 GMT, 1 November 2026.

| Item | Reason |
| --- | --- |
| KI-PRINCIPAL-MOD-011 and its unlanded branch | Kris's Enactment review; STEWARD-FIELD is an open query; ways-of-working is over the query cap |
| KI-OBSERVA-APP-044 | Kris's convergence decision; Observatory is over the query cap |
| KI-DESIGN-ART-002 | Kris's licensing decision |
| KI-TECHNE-OPS-018 | release and install gates; agent-host is on hold |
| KI-TOOL-RIG-CORE-047, -068, -069 | attended steps on sol; firewall is connection-critical with no tested restore path |
| KI-TOOL-RIG-CORE-070, KI-TOOL-MGIT-CLI-032, -033 | awaiting Kris's acceptance |
| Records in `docs/ideas/` | not adopted; adoption is Kris's |
| Every open query and agenda item in all packages (about 80) | Kris's, not answered by a recommended option |
| apps-observatory.local branch `z-retirement/observatory-20261030` | unlanded evidence; the Observatory's own call |
| tools-ki branch commit `6c4d2a1a` | not proven landed; needs a reviewer before removal |
| ki.prj.paperclip-capture-and-rebuild and its messages | Paperclip rollout held |
| HNR lines (SITE-STD-GAPS, TRIAGE-HOURS, ROUTE-TRIAGE-SPECIMENS and others) | another territory; message lines only |
| Any `tools-ki` pin bump or release, installs, credentials | release, installation and credential operations are excluded |
| Machine steps routed in (DESKTOP-RESET, BACKUPS-DELETE) | each Mac's Rig thread, not this territory |

## Queries

### CONFORM-SCOPE - Does the window cover the fleet commit-gate conform?

**Context:** 19 of 21 audited repositories fail three new commit-gate rules: the pre-commit hook must only check, lint-staged must not rewrite files, and `.gitignore` managed blocks must be reconciled. Kris chose on 1 November (HOOK-STASH a)) that hooks run lint-staged without stashing, and RED-MAIN says "Fix mains first". AWAY-1-NOV permits push-tier commits and excludes releases. A conform is one bounded run per repository; it changes no product behaviour, but it touches every repository's hook and ignore file while Kris is away. Not blind-reviewed: this run may not use subagents.

**Query:** Should the window run the commit-gate conform across the 19 repositories?

**Options:**

a) (recommended, confidence medium - HOOK-STASH and RED-MAIN cover the hook change, but the `.gitignore` rule is newer and was not named) Run it, one repository per run, three at a time, ki-principal last, stopping at any repository whose conform touches more than the hook, lint-staged settings and `.gitignore`.

b) Leave it for Kris's return and report the failures only.

### CAP-DECIDED - Do the decided follow-ups proceed while ways-of-working is over the query cap?

**Context:** The coordination standard says that over eight open queries the coordinator launches no new build or planning run until Kris catches up, and allows backlog-clearing work. Ways-of-working has 50 open queries. AWAY-1-NOV, given by Kris at 01:41 GMT knowing the queue, says to "carry on every unit Kris has already decided (the discussions rollout, the report and launcher follow-ups, the delegation and Acquire follow-ups)". Not blind-reviewed: this run may not use subagents.

**Query:** Do the follow-ups Kris named in the grant go ahead despite the cap?

**Options:**

a) (recommended, confidence medium - Kris named these units in the same words that granted the window, which is a newer, more specific instruction than the cap) Yes, run the named decided units; start no other build or planning run in ways-of-working.

b) No; run only backlog-clearing work until Kris has worked the queries down.

### 🤖 → 👤 Handoff to supervisor · since 01:58 GMT

👤 2 with you

- [with you] CONFORM-SCOPE · supervisor · since 01:58
- [with you] CAP-DECIDED · supervisor · since 01:58

🧵 ki.prj.ways-of-working
