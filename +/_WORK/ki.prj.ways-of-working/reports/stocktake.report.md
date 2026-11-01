# [Model](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › stocktake

**🤖 → 👤 Handoff to supervisor · Run report at 01:04 GMT · last mark 13:55 GMT (31 October)**

---

## Done

- Classified every report, design note and brief in [ki.prj.ways-of-working](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/work.md), read-only, as of 00:59 GMT on 1 November. No commit; nothing changed, moved or deleted.
- **Reports (77):** 56 can be deleted now. 9 can be deleted once their open queries are copied into `queries.md`. 12 stay.
- **Design (95 files in 11 folders):** 21 graduated and cited nowhere else. 5 graduated but cited from outside the package, so their links must be repointed before deletion. 26 superseded. 38 live. 5 old proposals were never disposed of and are in doubt.
- **Briefs (19):** 15 are spent and 4 are open (`finished-tidy`, `hook-nostash`, `rename-paperclip` and this one).
- **Queries never logged:** 24 are still open but appear only in reports, the morning summaries or a design note. They are copied in full under Findings, ready to paste into `queries.md`. Ten more were settled in practice and need only one line each in `decisions.md`.
- **Links:** `work.md`, `state.md`, `queries.md` and `messages.md` have no broken local links. Live and cited design notes have 39 broken links, each with its correct target or "unrecoverable" below. `decisions.md` has 5, which belong to BROKEN-LINKS-HISTORY.
- **Checks:** the link check passed for the four package files and found the 39 links above. Every pinned revision below was confirmed to hold its file (`git cat-file`). `fb84c0b5` is on `origin/main`, judged from the local ref with no fetch.
- **Material finding:** all 40 top-level reports, plus the two Z files in `reports/`, are untracked and have never been committed, so Git keeps no copy. Deleting them cannot be undone, unlike every other tidy. The move-only sweep already authorised under SWEEP-SCOPE ("All 17", 1 November) skipped this folder because this work's runs were live. Running it here first would commit the reports into `reports/`, so Git keeps them, before the mark deletes the homed ones. The two Z files should stay out of that commit until PUBLIC-REPORT-AUDIENCE and PUBLIC-REPORT-RECOVERY are settled.

## In Progress

- Nothing is running in this run. The package changed while it read: HOOK-STASH and RENAME-NAME were answered, the `start-name` report landed, and the `finished-tidy` and `rename-paperclip` briefs appeared. The tables are as of 00:59 GMT.

Outstanding - no action requested now:

- **Copy in the 24 unlogged queries** under UNLOGGED-QUERIES a. Two caveats. First, the nine empty-board choices predate IDEAS-IN-GRAPH (31 October) and IDEAS-ROADMAP-HOME a (1 November), and none has had a blind review. Second, several medium ones need one before they reach Kris.
- **Log ten settled-in-practice items** in `decisions.md`, one line each:
  - HARNESS-RECEIVER: the AMEND-RACE line went to State of play's queue, [ki.sop.main decisions](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.sop.main/decisions.md).
  - CLOSE-OUT-ROUTE: delivered in this work's harness lane, as the morning summary records.
  - FOOTER-MODE-SPACING: the blank line between mode lines is now in the style.
  - VEGA-SYNC: the plan went to sol and terra only, under HOST-SYNC-SEND and SYNC-LEAD-SHARED.
  - PUSH-DIVERGED: `fb84c0b5` is on `origin/main`.
  - QUERY-CARD: superseded by CARD-PATTERN.
  - REVIEW-BRIEF: settled by the `blind-review-7b` relaunch.
  - MASK-CONTEXT and ORCH-NAME-MASK: superseded by blind reviews 4 and 5 and REVIEW-CHALLENGE.
  - WORK-WRITES: merged into AGENT-HOME, answered a) on 30 October with a follow-up due 2 November.
- **Receive the unreceived reports.** Receipts are not logged for `capture-settled`, `discussions-plan`, `reports-folder`, `resolve-4`, `principal-resolve-2` and `-3`, the five sweeps and `start-name`.
- **Four older reports are unproved.** Their queries were never logged and I could not trace them: `burn-tools-ki` (seven untagged queries), `wow-burn-plan` (HELD-FOLD), `wow-review-deps` (DEPS-CLEAR) and `wow-review-tending-source` (TENDING-SOURCE). All date from 25 to 27 October and were probably overtaken. A short message to each owner, then deletion, is the likely course. That is the steward's call.

## Findings

### REPORTS - Report verdicts

**Goal:** say, for each report, whether its outcome has a home and where each of its queries went.

**Scope:** the 40 top-level `*.report.md` files and the 37 files in `reports/`, as of 00:59 GMT on 1 November.

**As of:** 1 November 2026, 00:59 GMT. Key: T means tracked in Git, U means untracked and never committed.

Top-level reports, all U:

| Report | Verdict | Where the outcome and each query went |
| --- | --- | --- |
| `a-3` | delete after copy | Outcome is in the window record. PILOT-CONTRACT-LINE is open and appears only in the morning summaries: copy it in. |
| `accept-by-criteria` | delete | Outcome is in [accepted](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/window-31-oct/accepted.md) and decisions (31 Oct 01:51). HARNESS-RECEIVER and CLOSE-OUT-ROUTE were settled in practice: log one line each. |
| `b-U5` | delete after copy | Outcome is in the tools-burndown U5-LANDED receipt (tools-mgit `f67e255`). SYNC-UNPUSHED-EXIT is open, belongs to tools-mgit and was never logged. |
| `blind-broken-links` | delete | Received 31 Oct 23:35. BROKEN-LINKS was split: -LIVE answered a), -HISTORY open in `queries.md`. |
| `blind-layout` | delete | Received 1 Nov 00:42. LAYOUT-SHAPE is open in `queries.md`, now reframed by LAYOUT-TOPIC. |
| `blind-rename-name` | delete | START-NAME became RENAME-NAME: answered a) and delivered (harness `3a86954a`). |
| `blind-review-7` | delete | REVIEW-BRIEF settled by the `blind-review-7b` relaunch (decisions, 31 Oct 12:31). |
| `blind-top-level` | delete | REPORT-LOCATION and REPORT-CLEARANCE became TOP-LEVEL-NOW and TOP-LEVEL-SWEEP-*, all answered 1 Nov. |
| `capture-settled` | keep | Not received yet. Its outcome is commit `a0ed819d`. CHECKSUMS-SETTLED is open: copy it in. |
| `discussions-plan` | keep | The DISCUSSIONS rollout plan exists only in this report's Findings. Not received. SWEEP-GATE is open: copy it in. |
| `footer-layout` | delete | Delivered, and the layout is in the style. FOOTER-MODE-SPACING settled by delivery: log one line. |
| `host-reconcile-plan` | delete | Outcome is [host-reconcile/plan](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/host-reconcile/plan.md), sent under HOST-SYNC-SEND. VEGA-SYNC settled in practice: log one line. |
| `ideas-board` | delete after copy | Outcome is [empty-board design](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/empty-board/design.md) and the ideas list. Its nine choices are open and never reached `queries.md`. |
| `landscape-review-claude` | delete | The review is kept as `design/landscape-review-claude.md`. WAKE-PLACE became WAKE-HOST (open). WORK-WRITES became AGENT-HOME, answered a) on 30 Oct. |
| `landscape-rollout` | delete after copy | AGENT-HOME-IDEA and ORCA-REACH-VEGA are open: no line reached ki.sop.main or ki.prj.agent-host. |
| `listen-and-awake` | delete after copy | Outcome is in the harness and was received. OBS-FEEDBACK-LINE is open: no line reached the Observatory. |
| `mask-queries-4`, `mask-queries-5` | delete | Superseded: blind reviews 4 and 5 ran, and REVIEW-CHALLENGE's neutral-Context rule was adopted. |
| `move-procedure-add` | delete | Received 31 Oct 23:38. Outcome is `884e5cc5`. No queries. |
| `principal-resolve-2`, `principal-resolve-3`, `resolve-4` | delete | Merges are on origin (`557cf18f`, `1fb3f96f`, `0b25eb04`, `37a872d2`, personal-principal `ba5aeb7a`). No queries. |
| `query-turns` | delete | QUERY-TURNS delivered. PUSH-DIVERGED is moot because `fb84c0b5` is on origin. |
| `question-prompt` | delete | Kept as `design/question-prompt/design.md`. QUERY-CARD superseded by CARD-PATTERN (31 Oct 13:33). |
| `quiet-listen` | delete after copy | QUIET-LISTEN delivered. WP-HEARTBEAT is open: the [Work Process](</Users/krisbrown/kis/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Processes/Work Process/Work Process.md>) note's heartbeat paragraph (line 105) still says "at least every 5 minutes". |
| `reports-folder` | delete | Outcome is harness `c273a1fb` and `58e1d128`. No queries. |
| `restart-review` | delete after copy | RESTART-POLICY and RESTART-EVIDENCE are open and appear only in the morning summaries. |
| `start-name` | delete | Outcome is harness `3a86954a`. No queries. Receipt not logged. |
| `sweep-hnr-principal`, `sweep-ki-principal`, `sweep-legal-principal`, `sweep-personal-principal`, `sweep-va-principal` | delete | Each outcome is commits in its repository plus REPORTS-MOVED lines. No queries. The ki-principal sweep skipped this package. |
| `top-level-cause` | delete | Kept as `design/package-layout/top-level-cause.md`. TOP-LEVEL-NOW and TOP-LEVEL-SWEEP-* answered. |
| `w-U13` | delete | Routed to ki.prj.chezmoi as ORCA-PREFS-DESIGN with ORCA-PREFS-READ and -BUILD (its `messages.md` line 20). |
| `w-U22` | delete | STOA-THEME is carried by STOA-HOME in [ki.sop.main queries](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.sop.main/queries.md). |
| `w-U3` | delete | WHATSAPP-HOST-FIELD is carried by WHATSAPP-MCP-SCOPE in [ki.prj.chezmoi decisions](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.chezmoi/decisions.md). |
| `w-U4` | delete | RELEASE-GO is open in [ki.reg.main queries](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.reg.main/queries.md). |
| `worker-wait-split` | delete after copy | WORKER-WAIT-* answered (31 Oct and 1 Nov 00:23). SPLIT-COMMIT is open and was never logged. |
| `wow-tidy` | delete after copy | CLOSE-BLOCKED is open and appears only in the morning summaries. It may since have been overtaken by later closes; not checked. |

Files in `reports/`, T unless marked:

| Report | Verdict | Where the outcome and each query went |
| --- | --- | --- |
| `burn-ki-design` | delete | MAP-002 and the size queries passed through `queries.md` (pickaxe), and the record has since left the ki-design roadmap. |
| `burn-tools-ki` | keep, unproved | Seven untagged queries, such as "parity table" and the packet fix, were never found in the package history. |
| `burn-tools-techne` | delete | No queries. A 27 October burn-down outcome. |
| `burn-website` | delete | Its citation query passed through `queries.md`. Superseded by the website's later delivery. |
| `drain-form` | keep | Tied to TERRA-LOCAL-REPORTS (open). DRAIN-STATE and DRAIN-HOST were settled by DRAIN-MEANS and the hold form. |
| `fields-personal-principal` | delete after routing | PRINCIPAL-READOPT, PRINCIPAL-KIND-SIZE and STREAMS-CHECKER-GAP were never logged. They concern Personal's records and the harness checker, so they belong with personal.sop.main and the harness owner. |
| `harness-followups` | delete | KI-HARNESS-GOV-214 has been pruned from the harness roadmap. |
| `hold-request-20261030-z.md` (U) | keep | Never committed. Z retirement context, tied to PUBLIC-REPORT-RECOVERY. Do not commit it in a sweep. |
| `ki-toml-switch` | delete | KITOML-GATE settled: `.ki.toml` declares `ki-work-package`. |
| `rig-fixes` | delete | KI-TOOL-RIG-CORE-062 has been pruned, and the Linux risk is noted as a non-goal in [KI-TOOL-RIG-CORE-047](/Users/krisbrown/kis/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md), as recommended. |
| `spec-areas-design` | delete | Routed: [ki.prj.portable-specifications spec-areas](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.portable-specifications/design/spec-areas.md) carries the design. |
| `threads-fix` | delete | THREADS-RELEASE was overtaken by `ki` v0.12 and v0.14. DESK-KIT-HOME is stale. |
| `work-folder-design`, `work-folder-rename` | delete | Superseded by `ki-work-package` (the skill rename and `.ki.toml`). |
| `work-package-review-fable` | delete | All ten queries graduated into the five-file package: `state.md`, `queries.md` with Parked, `messages.md`, `method_read`, route receipt, and STEWARD-HOME in `work.md`. |
| `work-package-standard` | delete | ALIAS-LIMIT was done by the declaration switch. HARNESS-PUSH is long past. |
| `wow-accept-prune` | delete | Q1 is a stale link repin. Q2 (close the Website Project) was overtaken: the [Website Project](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/website.md) is `lifecycle: paused`. |
| `wow-burn-plan` | keep, unproved | VIS030-NARROW settled: VIS-030 pruned. OBS-FOLD passed through `queries.md`. HELD-FOLD was never found. |
| `wow-ci-pins`, `wow-ki-pin-release`, `wow-release-runs` | delete | Overtaken by v0.14.0 and green main (decisions, 25 Oct 13:23), then by the 26 October no-release steer and the parked REL-X64-TIMEOUT. |
| `wow-close-done-2`, `wow-close-done-3b` | delete | KI-HARNESS-GOV-189 and -209 have been pruned from the harness roadmap. |
| `wow-extra-writes` | delete | EXTRA-WRITES-BRIEF was a placeholder brief, since overtaken. |
| `wow-perm-prompts` | delete | WORKTREE-REMOVE graduated: the coordinator style now bars `git worktree remove` and routes deletion to `ki agent close`. |
| `wow-rereview6-toolski-a` | delete | LEGACY-REPLAY and RELEASE-HISTORY were overtaken when tools-ki was admitted (23 Oct 04:24). |
| `wow-rev-principal-integrate` | keep | INTEGRATION-REPAIR was never logged. The report bears on the held retention evidence in `state.md`. |
| `wow-review-deps` | keep, unproved | DEPS-CLEAR was never logged. |
| `wow-review-docs-red` | delete | DOCS-ROUTE went through CI-RED-DOCS in decisions. |
| `wow-review-spec-orphan` | delete | Received 26 Oct 21:50, and SPEC-ORPHAN-OWNER passed through `queries.md`. |
| `wow-review-sweep` | delete | Its records were disposed of under the 27 October bulk reading. FIREWALL-SOL continues as RIG-ATTENDED (parked). |
| `wow-review-tending-source` | keep, unproved | TENDING-SOURCE was never logged. |
| `wow-rig-attended-steps` | keep | The step list behind RIG-ATTENDED (parked). |
| `wow-sm-polish`, `wow-sm-refine` | delete | END-RECORD, ARC-HOVER and the old PUSH-DIVERGED were overtaken by DIAGRAM-AGREED and WORK-CYCLE-ENDS (29 Oct). |
| `wow-sync-2` | delete | OUTPUT-READABILITY concerned a finished sync. |
| `z-session-retirement-20261030.md` (U) | keep | As for `hold-request-20261030-z.md`. |

### DESIGN - Design-note verdicts

**Goal:** mark each design note as graduated, superseded or live, with the evidence.

**Scope:** all 95 files under `design/`.

**As of:** 1 November 2026, 00:59 GMT. "Cited" means another file outside this package links to it by local path, so deleting it breaks that link.

| Note | Verdict | Evidence |
| --- | --- | --- |
| `change-management-brief`, `-decisions`, `-report`, `-review-astra`, `-review-fable`, `change-management-skills.architecture.json`, `.svg`, `design.md` (8) | graduated | The 13 October model now lives in `ki-coordination`, `ki-delegation`, `ki-work-design` and `ki-work-package` (`ki-pmo` was renamed). Kris's verbatim 13 October words stay in Git. |
| `checkout-isolation` | graduated | `ki-git` explicit staging and worktrees, the `ki-delegation` worktree rule, and the website page "Worktrees for writing runs". |
| `coord-any-package-brief`, `-report`, `-review-claude`, `-review-codex` (4) | graduated | `ki-coordination`: coordination opens on any valid territory, project or regular package. |
| `model-shape`, `model-shape-review-claude`, `model-shape-review-codex` (3) | graduated | `ki-coordination`'s State of play coordinating several packages. |
| `naming-rollout-manifest` | graduated | The rollout finished on 28 October and typed ids are in use. |
| `op-cache-rule` | graduated | The `op_cache` rule is in [standards-background-runs](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/skills/governance/ki-delegation/references/standards-background-runs.md). |
| `question-prompt/design` | graduated | CARD-PATTERN (31 Oct 13:33) is in `ki-coordination` and the style. |
| `discussions/design` | graduated | DISCUSSIONS b) (1 Nov 00:18) is in decisions. The rollout plan is in `discussions-plan.report.md`. |
| `website-docs` | graduated | The course is live (website `e8f986b`, WEBSITE-LIVE). |
| `coordination-lessons`, `method-feedback` | graduated, cited | Cited as sources by the `ki-coordination`, `ki-delegation` and `ki-work-package` `references/sources.md` files. |
| `gfm-migration` | graduated, cited | GFM is in `ki-authoring` standards-markdown. Cited by [ki.prj.tools-burndown decisions](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.tools-burndown/decisions.md). |
| `unattended-work` | graduated, cited | The unattended-window rules are in `ki-coordination`. Cited by personal.sop.main decisions. |
| `work-id-shape-plan` | graduated, cited | Typed ids are in use. Cited by the ki.prj.baseline-rollout and ki.prj.observatory `messages.md`. |
| `host-sync-report` (29 Oct) | superseded | By `host-sync/report.md`, then by the 31 October pass rule (HOST-ALL closed 1 Nov 00:29). |
| `host-sync/brief`, `report`, `review-claude`, `review-codex` (4) | superseded | HOST-ALL closed as superseded on 1 Nov: "it's a step back from where we are now". |
| `host-reconcile/findings` | superseded | By `host-reconcile/plan.md`. |
| `finish-first` | superseded | By EMPTY-BOARD and WIP-LIMIT (31 Oct) and `empty-board/design.md`. |
| `query-sweep`, `roadmap-sweep` | superseded | Settled by the 27 October bulk reading. |
| `retro-2026-10-20`, `take-stock-2026-10-20`, `unparked-queries` | superseded | Spent: their actions were taken or overtaken, CHECKOUT-ISOLATION among them. |
| `review-pack`, `overview`, `skill-set`, `window-plan` | superseded | By the later owner reports and morning summaries. The skill-set model was overtaken by the landscape study and ORCH-NAME. |
| `method-lines` | superseded | METHOD-LINES was disposed of on 25 October (wow-lines received). |
| `stop-for-host-move` | superseded | The move finished on 31 October. ki.prj.chezmoi owns the procedure (MOVE-PROCEDURE-STEPS). |
| `window-31-oct/accepted`, `morning-summary`, `-final`, `-last` (4) | superseded | By the return report and decisions. The morning summaries are the only record of several unlogged queries, so copy those first. |
| `window-31-oct/sync` | superseded | The AWAY-31-OCT decisions entry links it as the window's revision record. Repoint that link to a pinned revision before deleting. |
| `work-model.svg`, `work-model.architecture.json` | superseded | By the `work-state-machine.*` diagrams (DIAGRAM-AGREED, 29 Oct). Medium confidence. |
| `context-efficiency` | superseded | It recommended no change, so there is nothing to home. Medium confidence. |
| `capture-model/brief` | live | CAPTURE-MODEL is in its design loop. HOLDING-SCOPE-CARDS and IDEAS-ROADMAP-PRINCIPLE are open. |
| `empty-board/design`, `empty-board/ideas` | live | Kris's review is pending (`state.md` step 1). |
| `finished-tidy-kick` | live | FINISHED-TIDY-KICK is being applied (brief `finished-tidy`). |
| `package-layout/design`, `package-layout/top-level-cause` | live | LAYOUT-SHAPE and LAYOUT-GROUP-TIDY are open under LAYOUT-TOPIC. |
| `package-definition-freshness-brief`, `-report`, `-review-freshness`, `-review-portability` (4) | live | HOMES, EXECUTION, HOST, DISPLAY, THEME, ROUTING, SIGNAL and RESTART are open in `queries.md`. |
| `landscape`, `landscape-report`, `-explainer`, `-review-claude`, `-review-codex`, `-skills-inventory`, `-vendors` (7) | live | ORCH-NAME-DISPATCH and WAKE-HOST are open. `landscape-report` is cited by the orca-evaluation trial plan and tools-burndown messages. |
| `orca-fit`, `orca-fit-explainer` | live | `orca-fit` is cited by the [orca-evaluation trial plan](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.orca-evaluation/design/orca-trial-plan.md). |
| `orca-subagents/design` | live | Part B and the pilot are pending. Cited by tools-burndown messages. |
| `inbox-wake/design` | live | INBOX-ALL a) (1 Nov) is logged, but the CODEX-WAKE trial is still to be arranged. Cited by tools-burndown messages. |
| `mgit-cache` | live | Parked MGIT-CACHE-SCOPE and MGIT-CACHE-FAILED depend on it. |
| `work-state-machine.md`, `.mmd`, `.svg`, `.html`, `state-machine-rollout-plan` (5) | live | Units U1 and U2 are not delivered: the Work Process note has no "At rest". WORKER-WAIT-DELIVERY rides on them. The `.html` is cited by Observatory messages. |
| `mod011-wording`, `model-shape-report` | live | Both are cited by [KI-PRINCIPAL-MOD-011](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-MOD-011-amend-work-model-assigned-package-cascade.md) (draft, horizon now). |
| `tending`, `findings`, `repository-metadata`, `interim-cover` (4) | live | Areas still being worked out. Cited by the [Ways of working Project](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) note, the website diagrams (54 links to `tending`), ki.sop.main and Personal. |
| `roadmap-sizing-and-burn-down` | live, cited | Cited by ki.sop.main decisions and `va-consolidation`. Whether it has graduated is unproved. |
| `window-31-oct/plan` | live | Holds the briefs for units in the four packages still on hold. Cited by chezmoi's `orca-prefs`. |
| `host-reconcile/plan` | live | An unreceived IMPORTANT line in personal.reg.rig-sol `messages.md` links it on GitHub `main`. |
| `host-sync-and-reply-trades` | live until HOST-SYNC closes | The parked HOST-SYNC query points to it. See HOST-SYNC-CLOSE. |
| `finish-line-plan` | live | Adopted as the Project's closing plan under FINISH-LINE a) (RECOMMENDED-ALL, 29 Oct). |
| `agent-control-contract` | in doubt | The build contract was accepted on 21 Oct. I could not prove its delivery in tools-ki docs. |
| `gov-227-storage-schema`, `tags-model`, `overload-process`, `observatory-review` | in doubt | Proposals never disposed of. GOV-227 has a harness idea record, and the Observatory review view is already in the Observatory's `_IDEAS.md`. See OLD-PROPOSALS. |

### LINKS - Broken links and their correct targets

**Goal:** give the correct target for every broken link in the package files and in live or cited design notes, never inventing one.

**Scope:** `work.md`, `state.md`, `queries.md`, `messages.md` and every design note marked live, cited or in doubt above.

**As of:** 1 November 2026, 00:59 GMT. Package files: none broken. Pinned revisions were confirmed to hold each file.

| Note:line | Broken target | Correct target |
| --- | --- | --- |
| `capture-model/brief.md:33` | Acquire capture `.../intake/2026-10-30-intent-based-onedrive-acquisition/original.txt` | Unrecoverable here: the capture folder now sits under `captures/_review/` and holds only `README.md`. |
| `capture-model/brief.md:34` | same folder `/README.md` | `/Users/krisbrown/kis/personal/acquire/captures/_review/knowledge-islands/intake/2026-10-30-intent-based-onedrive-acquisition/README.md` (same capture folder, moved under `_review/`) |
| `capture-model/brief.md:75` | `attachments/01-3.jpg` | Unrecoverable: no attachments in the capture folder. |
| `landscape.md:18`, `landscape-review-claude.md:15`, `landscape-review-codex.md:9` | `../briefs/landscape.md` (pruned) | `https://github.com/knowledgeislands/ki-principal/blob/ef452184d1f102b84203203283b0a417d6c9f359/+/_WORK/ki.prj.ways-of-working/briefs/landscape.md` |
| `landscape-review-codex.md:39` | `.../tools-ki/src/core/agent/worktrees.ts:42` | `/Users/krisbrown/kis/knowledge-islands/tools-ki/src/core/agent/worktrees.ts`. The file exists; the `:42` suffix breaks the link, so give "line 42" in the text instead. |
| `landscape-skills-inventory.md:289, 305, 328` | relative harness paths truncated by the generator (`../../../governance/ki-delegation/references/sta`) | Unrecoverable as written. The full file names were cut off. |
| `landscape.md:62`, `orca-fit.md:15`, `orca-fit.md:214` | `../../ki.prj.mac-studio-setup/design/orca-trial.md` | `../../ki.prj.orca-evaluation/design/orca-trial.md`. Proven move: `d38088a3`, "hand Orca trial evidence to ki.prj.orca-evaluation". |
| `orca-fit.md:15` | `../../ki.prj.mac-studio-setup/plan069.report.md` (deleted in `a95f0ddc`) | `https://github.com/knowledgeislands/ki-principal/blob/d38088a3a47407a4d37ff79050f9e94a52cbdb72/+/_WORK/ki.prj.mac-studio-setup/plan069.report.md` |
| `tending.md:11`, `findings.md:11`, `repository-metadata.md:11` | `va-principal/+/_WORK/va/work.md` and `/va/decisions.md` | `/Users/krisbrown/kis/valle-armonia/va-principal/+/_WORK/va.sop.main/work.md` and `.../va.sop.main/decisions.md` (folder renamed in the 28 October naming rollout) |
| `findings.md:145` | `.../ki-principal/+/_WORK/ki.ways-of-working/messages.md` | `/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/messages.md` |
| `repository-metadata.md:19, 84` | `~/.local/state/ki/agents/va/repo-align.report.md`, `tag-proposal.report.md` | Unrecoverable: runtime reports, never in Git, now absent. |
| `repository-metadata.md:229` | `personal-principal/+/_WORK/personal/findings/REPO-META.md` | `/Users/krisbrown/kis/personal/personal-principal/+/_WORK/personal.sop.main/findings/REPO-META.md` |
| `interim-cover.md:13` | `.../va/decisions.md` and `.../personal/decisions.md` | `.../va.sop.main/decisions.md` and `/Users/krisbrown/kis/personal/personal-principal/+/_WORK/personal.sop.main/decisions.md` |
| `interim-cover.md:49` | `../../ki/queries.md#baseline---one-baseline-for-every-capital` | Path: `../../ki.sop.main/queries.md`. Anchor unrecoverable: the BASELINE query is no longer there, and my search found no revision holding that heading. |
| `coordination-lessons.md:21-23` | `hnr-principal/+/_WORK/hnr/design/scheduling-debrief.md`, `coordination-model-notes.md`, `hnr/decisions.md` | `/Users/krisbrown/kis/humans-not-robots/hnr-principal/+/_WORK/hnr.sop.main/design/scheduling-debrief.md`, `.../hnr.sop.main/design/coordination-model-notes.md`, `.../hnr.sop.main/decisions.md` (link only; no HNR source was read) |
| `coordination-lessons.md:28` | `acquire/+/_WORK/personal.regular.acquire-intake/work.md` | `/Users/krisbrown/kis/personal/acquire/+/_WORK/personal.reg.acquire-intake/work.md` |
| `mod011-wording.md:36` | `../../../../../Admin/Governance/Decisions/GDR-KI-PRINCIPAL-009-the-work-model.md` (one level too deep) | `../../../../Admin/Governance/Decisions/GDR-KI-PRINCIPAL-009-the-work-model.md` |
| `finish-line-plan.md:8` | `../briefs/wow-finish-line.md` (pruned) | `https://github.com/knowledgeislands/ki-principal/blob/ef452184d1f102b84203203283b0a417d6c9f359/+/_WORK/ki.prj.ways-of-working/briefs/wow-finish-line.md` |
| `gfm-migration.md:23` | `../Folder/Note.md` | Not a link: an example inside inline code. No change. |
| `unattended-work.md:44, 46, 57` | `.../ki.ways-of-working/decisions.md`, `messages.md`, `queries.md` | The same files under `.../ki.prj.ways-of-working/` |
| `unattended-work.md:56` | `personal-principal/+/_WORK/personal/design/unattended-criteria.md` | `/Users/krisbrown/kis/personal/personal-principal/+/_WORK/personal.sop.main/design/unattended-criteria.md` |

### BRIEFS - Brief verdicts

**Goal:** mark each brief as spent or open.

**Scope:** the 19 files in `briefs/`.

**As of:** 1 November 2026, 00:59 GMT.

| Brief | Verdict |
| --- | --- |
| `b-U5`, `blind-broken-links`, `blind-layout`, `capture-settled`, `discussions-plan`, `principal-resolve-3`, `reports-folder`, `resolve-4`, `start-name`, `sweep-hnr-principal`, `sweep-ki-principal`, `sweep-legal-principal`, `sweep-personal-principal`, `sweep-va-principal` | spent: each report has landed |
| `orca-fit` | spent: its output is `design/orca-fit.md`, received on 30 October |
| `finished-tidy`, `hook-nostash`, `rename-paperclip`, `stocktake` | open: runs launched or in flight |

### TOPICS - Proposed topic folders for what survives

**Goal:** group the surviving briefs, design notes and reports by topic, under LAYOUT-TOPIC.

**Scope:** only what the verdicts above keep. Whether each topic holds `briefs/` and `reports/` subfolders or flat `<run>.brief.md` and `<run>.report.md` files stays with LAYOUT-SHAPE.

**As of:** 1 November 2026, 00:59 GMT. Moving a cited note breaks its outside links just as deleting it would, so a cited note moves only once its citations are repointed.

| Topic | Design notes | Reports and briefs | Queries it would carry |
| --- | --- | --- | --- |
| `work-model/` | `work-state-machine.{md,mmd,svg,html}`, `state-machine-rollout-plan`, `mod011-wording`, `model-shape-report` | `quiet-listen` (until copied) | WP-HEARTBEAT, the WORKER-WAIT delivery |
| `package-layout/` | `package-layout/design`, `top-level-cause`, `finished-tidy-kick` | brief `finished-tidy` | LAYOUT-SHAPE, LAYOUT-GROUP-TIDY, FINISHED-TIDY-KICK |
| `package-definition/` | `package-definition-freshness-*` (4) | `restart-review` (until copied) | HOMES, EXECUTION, HOST, DISPLAY, THEME, ROUTING, SIGNAL, RESTART, RESTART-POLICY, RESTART-EVIDENCE |
| `discussions/` | none left once `design.md` is deleted | `discussions-plan` | SWEEP-GATE |
| `capture-model/` | `capture-model/brief` | `capture-settled` | HOLDING-SCOPE-CARDS, IDEAS-ROADMAP-PRINCIPLE, CHECKSUMS-SETTLED |
| `empty-board/` | `empty-board/design`, `ideas` | `ideas-board` (until copied) | the nine empty-board choices |
| `landscape/` | `landscape*` (7) | `landscape-rollout` (until copied), brief `rename-paperclip` | ORCH-NAME-DISPATCH, WAKE-HOST, AGENT-HOME-IDEA, AGENT-HOME follow-up |
| `orca/` | `orca-subagents/design`, `orca-fit`, `orca-fit-explainer` | `a-3` (until copied) | PILOT-CONTRACT-LINE, ORCA-REACH-VEGA |
| `listening/` | `inbox-wake/design` | `listen-and-awake` (until copied) | OBS-FEEDBACK-LINE, the CODEX-WAKE trial |
| `host-sync/` | `host-reconcile/plan`, plus `host-sync-and-reply-trades` unless HOST-SYNC-CLOSE | none | HOST-SYNC (parked) |
| `nascent-areas/` | `tending`, `findings`, `repository-metadata`, `interim-cover` | `wow-review-tending-source` (unproved) | none; these need a lasting home by the Project's close |
| `publication-recovery/` | none | `drain-form`, `wow-rev-principal-integrate`, the two Z files (untracked, private) | PUBLIC-REPORT-AUDIENCE, PUBLIC-REPORT-RECOVERY, TERRA-LOCAL-REPORTS, TERRA-PR-CHECK, TERRA-RECOVERY |
| `window-31-oct/` | `plan` (held units) | none | HOLD-SCOPE remainder |

Fits no topic:

- `finish-line-plan`, the Project's closing plan, could stay at the top of `design/`.
- `mgit-cache`, behind a parked feature.
- `roadmap-sizing-and-burn-down`, which is cited.
- The cited graduated notes, until their citations are repointed.
- The OLD-PROPOSALS five.
- `wow-rig-attended-steps`, which goes with RIG-ATTENDED.
- `fields-personal-principal`, to be routed to Personal.
- The unproved `burn-tools-ki`, `wow-burn-plan` and `wow-review-deps`.
- `b-U5`, `worker-wait-split` and `wow-tidy`, until their single queries are copied in.

### UNLOGGED - Open queries not yet in `queries.md`, for copying in

**Goal:** carry, in full, every query still open that never reached `queries.md`.

**Scope:** 24 queries copied word for word from their reports, with `~/workspaces/` links repointed to `~/kis/` after the move. Each carries its source run.

**As of:** 1 November 2026, 00:59 GMT. Two caveats:

- The nine empty-board choices predate IDEAS-IN-GRAPH and IDEAS-ROADMAP-HOME a), and none has had a blind review.
- CLOSE-BLOCKED and STREAMS-CHECKER-GAP may have been overtaken. Check them before copying.

#### PILOT-CONTRACT-LINE - Tell the Orca evaluation about the extra pilot checks

since 2026-10-31 · from run/a-3 · not yet in `queries.md`

**Context:** Row 2 already sent the ORCA-SUBAGENT-PILOT line to [ki.prj.orca-evaluation's messages](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.orca-evaluation/messages.md), using the wording drafted before the review. That line asks four things: whether the worker nests in the list, whether it runs without prompts, whether it survives the chat ending, and what it leaves in the inbox. The blind review on ORCA-PLACEMENT added three checks that the pilot must also cover: the run's directories, running without anyone at the keyboard, and authority limits, so that too much access fails as well. These are now in the design note, and the line links to that note, but the line itself does not mention them. The pilot could run without them, and then Part B's route could not be confirmed. This run sent nothing, because the row only asked for the design note.

**Query:** Should the coordinator send ki.prj.orca-evaluation a short follow-up line adding the three checks to the pilot?

**Options:**

a) (recommended, confidence medium - the line is cheap and easy to withdraw, and without it the pilot may miss what the route decision depends on; but it goes beyond the row, so this is the coordinator's call) Send one follow-up line to ki.prj.orca-evaluation's `messages.md` naming the three checks and pointing to section 3 of the design.

b) Send nothing, and rely on the pilot reading the linked design note.

#### SYNC-UNPUSHED-EXIT - Should leaving a branch unpushed make sync report failure?

since 2026-10-31 · from run/b-U5 · not yet in `queries.md`

**Context:** By default sync now leaves branches that are only ahead unpushed. I counted these as "skipped" but let the run finish successfully (exit status 0), the same way sync already treats a pull or push the user declines under `-i`. Other skips, such as local changes or divergence, still make sync exit with status 1. A script that relied on sync's exit status to spot unpublished commits would now have to read the summary at the end. The decision's words say nothing about exit status, so this was my call. It is recorded in [KI-TOOL-MGIT-CLI-033](/Users/krisbrown/kis/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-033-sync-push-guard.md) for review.

**Query:** Should an unpushed branch leave sync's exit status successful, as delivered?

**Options:**

a) (recommended, confidence medium - not pushing is now the intended default, so failing every routine run on a repository with local commits would make the exit status meaningless) Keep it as delivered: unpushed branches are reported and counted as skipped but do not fail the run.

b) Make an unpushed branch fail the run (exit status 1), like the other skips, so scripts notice unpublished commits.

#### CHECKSUMS-SETTLED - CAPTURE-LEAN also answers the checksum choice

since 2026-11-01 · from run/capture-settled · not yet in `queries.md`

**Context:** CAPTURE-LEAN was read back in Acquire as "there is no `original.txt` and no checksum file". That covers the brief's CHECKSUMS choice, whose recommended option is to stop writing `SHA256SUMS` for intake captures. This run's brief said to settle only LEAN-CAPTURE and to leave the other choices open with their wording unchanged, so CHECKSUMS is still shown as open.

**Query:** Should the brief also mark CHECKSUMS as settled by CAPTURE-LEAN before the blind reviews?

**Options:**

a) (recommended, confidence high - the read-back says it in so many words, and reviewers would otherwise test something already decided) Yes: a one-line follow-up marks CHECKSUMS as settled for intake captures, quoting CAPTURE-LEAN, and leaves each other route guide to keep or drop the file on its own terms.

b) No: leave CHECKSUMS open for the reviews.

#### SWEEP-GATE - What "both Macs level" means before each repository is swept

since 2026-11-01 · from run/discussions-plan · not yet in `queries.md`

**Context:** On 31 October Kris asked that the rename sweep wait until "host sync has both Macs level", to avoid clashes between the two Macs, sol and terra. Host sync is not yet running routinely. Sol's sync loop stopped at its session restart on 31 October and has not resumed, and no host-sync executor or schedule has been chosen. A wholesale move of every repository to `~/world/<territory>/<repo>` is also being prepared. The sweep renames a file in 60 work packages across 9 repositories. If either Mac holds unpushed changes to those packages, or the move happens mid-sweep, the two copies drift apart and someone has to merge them by hand.

**Query:** Should each repository's sweep wait for a one-off check that that repository is clean and level on both Macs, or wait until host sync runs routinely and the repository move is finished?

**Options:**

a) (recommended, confidence medium - it meets the aim of Kris's words without waiting on host sync, which has no date; but it reads "host sync" as a check rather than the running service) Just before each repository's run, each Mac's Rig thread or Kris makes a fresh one-off check that the repository is committed, pushed and level on both Macs. The run then renames and pushes at once, and the other Mac pulls before any coordinator there writes. No sweep runs while the `~/world` move is under way.

b) Hold the whole sweep until host sync runs routinely on both Macs and the `~/world` move has finished. The readers and writers (U1 to U5) go ahead meanwhile, and the old and new names live side by side until then.

#### OBS-FEEDBACK-LINE - Should the Observatory also send feedback as a message line?

since 2026-10-31 · from run/listen-and-awake · not yet in `queries.md`

**Context:** Under FEEDBACK-AS-MESSAGE on 31 October 2026, Kris said "we can probably drop the feedback idea. We just send a message with it instead." I replaced the hand-written and steward-written feedback files. The Observatory's own feedback-sending feature still writes a separate feedback file plus a message line linking it. It is shipped under its own decision, PDR-KI-OBSERVA-007, and owned by the Observatory work, so I left it alone and kept those files readable for now. Until the Observatory changes, the method has two routes for owner feedback.

**Query:** Should this work send the Observatory work a message asking it to send feedback as a message line only, so that the separate feedback file can be retired?

**Options:**

a) (recommended, confidence medium - it matches Kris's words and removes the second route, but the Observatory may need the separate file for comments anchored to passages, which I have not checked) Send one line to the Observatory work's `messages.md`, asking it to move `feedback-send` to message lines and then retire the `feedback/` kind.

b) Keep the Observatory's feedback file as the one exception, and retire nothing.

#### WP-HEARTBEAT - Bring the Work Process note into line with the quiet watcher

since 2026-10-31 · from run/quiet-listen · not yet in `queries.md`

**Context:** The harness standard no longer has a timed heartbeat. A run finishing, or a new message, is now the only thing that wakes the thread. The [Work Process note](</Users/krisbrown/kis/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Processes/Work Process/Work Process.md>) in Knowledge Islands Principal still says, under "Stuck and the heartbeat", that a heartbeat gives "an update on change, at least every 5 minutes and always by 10". That note is canonical content, so changing it goes through the Enactment Process, and this run had no authority in that repository.

**Query:** Should the Work Process note's heartbeat paragraph be changed to match QUIET-LISTEN?

**Options:**

a) (recommended, confidence high - QUIET-LISTEN explicitly replaces the timed heartbeat updates, and the note is the model the standard cites) Yes. Launch a bounded run in Knowledge Islands Principal that rewrites the paragraph so the heartbeat wakes only when a run finishes, citing QUIET-LISTEN as the owner instruction for the Enactment Process.

b) Leave the note as it is for now, and accept that it disagrees with the standard until a wider model refresh.

#### RESTART-POLICY - How should the two restart policies coexist?

since 2026-10-31 · from run/restart-review · not yet in `queries.md`

**Context:** The landed restart rule responds to Kris's immediate enactment instruction through identity changes, repeated compaction and method changes. It excludes age or length alone and can repeat until declined. The parked RESTART design instead proposes four hours or 100 evidenced messages, a single reminder at a safe boundary and no repetition; it remains explicitly design-only. Neither the delivery nor this review answers that query.

**Query:** Should the landed categorical policy remain the current rule while the numerical design stays separately parked?

**Options:**

a) (recommended, confidence medium - preserves the explicit immediate delivery without treating an unanswered design proposal as adopted) Retain the categorical policy for now, record that it does not settle RESTART, and reconcile triggers, safe timing and repetition explicitly before any future numerical adoption.

b) Commission one combined design revision now, covering categorical and numerical triggers, evidence, safe boundaries and repetition, for Kris's review before any further implementation.

c) Request a scoped revision replacing the categorical policy with the numerical proposal; first decide its values, evidence requirements and implementation authority explicitly.

#### RESTART-EVIDENCE - Qualify the trigger rationale as a workflow convention?

since 2026-10-31 · from run/restart-review · not yet in `queries.md`

**Context:** The standard makes categorical necessity claims about a second compaction, changed identity and changed method. The reviewed evidence and passing source tests establish a coherent written rule, but do not validate improved session quality or prove that in-session correction cannot suffice. The parked numerical design already acknowledges this distinction.

**Query:** Should a later authorised wording revision qualify these triggers as provisional workflow heuristics rather than proven necessities?

**Options:**

a) (recommended, confidence high - brings the rationale into line with the evidence without selecting a new threshold or silently changing behaviour) Commission a bounded wording revision describing the triggers as reversible workflow conventions, remove universal claims about fidelity and impossibility of in-session correction, and retain owner discretion; review behavioural changes separately under RESTART-POLICY.

b) Keep the present wording pending specific evidence that validates the claimed necessity and the second-compaction cutoff.

#### SPLIT-COMMIT - The split was published inside another session's commit

since 2026-10-31 · from run/worker-wait-split · not yet in `queries.md`

**Context:** The brief asked for `queries.md` to be committed alone under "docs(work): ki.prj.ways-of-working split WORKER-WAIT". Before this run committed, another session's host-sync review commit `76beec53` swept the uncommitted `queries.md` into its own commit and pushed it. The content on origin is exactly this run's split; only the commit subject is misleading for that file.

**Query:** Is the split accepted as published under that commit, or should a marker be added?

**Options:**

a) (recommended, confidence high - the content is identical and on origin, and the only correction possible without rewriting history is a note) Accept it as published; the coordinator records in the decisions log, at its next receive, that `76beec53` carries the WORKER-WAIT split.

b) Add an empty commit with the brief's subject that names `76beec53` as carrying the split.

#### CLOSE-BLOCKED - The two stale runs cannot close

since 2026-10-31 · from run/wow-tidy · not yet in `queries.md`

**Context:** `ki agent close` refuses both runs for two reasons. First, the package folder has untracked files, which are the reports kept above and newly finished run reports. Second, decisions in `decisions.md` have no recorded home: 13 named for `ways-of-working-reg` (DIAGRAM-AGREED, MOVE-PROMPT-SHAPE, STOP-FOR-MOVE-WOW, ORCA-FIT, LANDSCAPE, ORCA-SUBAGENTS, AWAY-31-OCT and the dated receive entries) and 72 for `ways-sol-resume-20261029`. Homing each decision through `ki agent reconcile` is a judgement on live decisions, outside a tidy. `--reconciled` would waive the check, but nothing authorises a waiver. A side effect remains: three sol reports now sit untracked in the package root as their only copies.

**Query:** How should the two stale runs be closed?

**Options:**

a) (recommended, confidence medium - the decision homes need the steward's judgement, and committing the three sol reports keeps them safe in Git) Have the coordinator receive the new reports and commit the three returned sol reports into `reports/`. Then run one bounded reconcile pass that records each decision's home or class with `ki agent reconcile`, and retry both closes.

b) Close both with `--reconciled` under an explicit owner waiver. The close note records the waiver, and the decision-home check is left to the next mark.

#### AGENT-HOME-IDEA - Who writes the Techné dispatch `Idea:` line

since 2026-10-31 · from run/landscape-rollout · not yet in `queries.md`

**Context:** AGENT-HOME a) also says "Record Techné dispatch agent an `Idea:` line on Techne theme page". The Techne theme page lives in `Streams/Themes/techne.md`, and no work package's routing description claims it. Root `AGENTS.md` sends work that no package owns to State of play's `messages.md`.

**Query:** Should the `Idea:` line go to ki.sop.main as a message, or should this package write it itself?

**Options:**

a) (recommended, confidence medium - AGENTS.md routes unowned work to State of play, but this package may already own theme-page edits for its decisions) Send one line to ki.sop.main's `messages.md`.

b) This package's coordinator adds the line itself in a bounded run.

#### ORCA-REACH-VEGA - Tell ki.prj.agent-host about the `vega` launcher choice

since 2026-10-31 · from run/landscape-rollout · not yet in `queries.md`

**Context:** ORCA-REACH a) keeps `ki agent` as the only launcher on `vega`, by choice. ki.prj.agent-host builds and runs `vega`. The line went only to ki.prj.orca-evaluation, which owns Orca use.

**Query:** Should ki.prj.agent-host also get a line about ORCA-REACH?

**Options:**

a) (recommended, confidence medium - the decision constrains vega's launcher, but the brief named only the Orca owner) Send one ORCA-REACH line to ki.prj.agent-host's `messages.md`.

b) Leave it with ki.prj.orca-evaluation only.

#### IDEAS-HOME - Where should ideas live?

since 2026-10-31 · from run/ideas-board · not yet in `queries.md`

**Context:** Ideas live today in four sanctioned places (Project pages, theme pages, idea-stage Projects and repository `_IDEAS.md` ledgers) plus Emerging Concepts, parked queries and held packages. You asked for them to be consolidated in a single place. One territory list is easiest to review and to keep empty, but it moves ideas away from the Project pages that give them context, and it needs the roadmap standard changing.

**Query:** Where should every idea in the Knowledge Islands territory live?

**Options:**

a) (recommended, confidence medium - it gives you one place to review and age ideas, but it reverses the 17 October rule that ideas start on their Project page) One territory ideas list in Knowledge Islands Principal, each idea one line naming its Project or theme and linking to fuller text where it exists; Project and theme pages keep their context but no longer hold ideas.

b) Leave ideas where they are and generate the consolidated list from them on demand, like [ideas](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/empty-board/ideas.md), so there is one place to look but several places to write.

c) One ideas list per repository, with Project pages pointing to them.

#### WIP-PACKAGE - How many units may a package have in flight?

since 2026-10-31 · from run/ideas-board · not yet in `queries.md`

**Context:** Overnight this package ran up to three units at once, as the current "keep about three agents running" rule allows. You asked for one at a time where possible, finished quickly. A unit's independent review is a separate run, but it works on the same change.

**Query:** How many units may one work package have in flight at a time?

**Options:**

a) (recommended, confidence high - it is your WIP-LIMIT answer written down, and allowing the review keeps reviews independent without a second piece of work) One unit at a time, plus at most one independent review of that same unit.

b) One unit at a time with nothing alongside it, reviews included.

c) Up to two units at a time where they touch different repositories.

#### WIP-TERRITORY - How many packages may be active across the territory?

since 2026-10-31 · from run/ideas-board · not yet in `queries.md`

**Context:** The current cap is "three or four" Project packages, not counting State of play; today five packages are neither on hold nor finished, one being worked and four waiting on you. A package waiting on you would count as active under this proposal, so that answering frees a slot.

**Query:** How many work packages may be active at once across the Knowledge Islands territory?

**Options:**

a) (recommended, confidence medium - it tightens the existing cap to its lower bound without stopping you working on more than one thing a day, though "minimal parallelisation" could mean one) At most three Project or regular packages, plus State of play, with packages waiting on you counting as active.

b) One package at a time, plus State of play: strictly serial.

c) Keep "three or four", with packages waiting on you not counted.

#### ROADMAP-UPCOMING - Should the roadmap hold only upcoming work?

since 2026-10-31 · from run/ideas-board · not yet in `queries.md`

**Context:** Records can sit on the roadmap with horizon `soon`, `future` or `hold`, and done records stay until pruned. Today 19 of 22 records are finished, held, in triage or tied to work that is not moving. Making the roadmap hold only `now` and `next` would turn the other horizons into ideas, which needs the roadmap standard and its checker changing in the harness and tools-ki.

**Query:** Should a roadmap hold only records that are coming up next, with everything else moved back to ideas?

**Options:**

a) (recommended, confidence medium - it is what EMPTY-BOARD asks for, but it changes a standard and a checker that other territories also use) Yes: only `now` and `next` stay, capped at three per repository and ten across the territory; `soon` and `future` records go back to ideas, and held records go back to ideas unless their release is in sight within a fortnight.

b) Keep the horizons as they are, but count only `now` and `next` as upcoming, and cap those.

#### GATES - Are the two gates right?

since 2026-10-31 · from run/ideas-board · not yet in `queries.md`

**Context:** Section 3 proposes Gate 1 (idea to upcoming: you say yes, it has a home, the next step is known, it is small, and there is room) and Gate 2 (upcoming to active: it is Ready, nothing it needs is missing, and the package and the territory have a free slot). Most of these already exist in `ki-next` and `ki-plan`; the new parts are the size rule and the room checks.

**Query:** Should the two gates in section 3 be adopted as written?

**Options:**

a) (recommended, confidence medium - most of each gate restates existing rules, and the new size and room checks are easily relaxed later) Adopt both gates as written.

b) Adopt them without the size rule, so larger work can be adopted and split later.

#### PARKED-TO-IDEAS - What happens to parked queries?

since 2026-10-31 · from run/ideas-board · not yet in `queries.md`

**Context:** 120 parked queries sit in nine packages with no age limit; several point at records that no longer exist, and eight here are duplicated. A parked query is a decision nobody is currently making, which is what an idea is. Moving one keeps its recommendation, so nothing is lost.

**Query:** Should parked queries move to the ideas list?

**Options:**

a) (recommended, confidence medium - it empties the Parked sections and stops stale decisions piling up, but some parked queries are close to answerable and might be better brought back) Yes: at each package's next mark, each parked query moves to the ideas list with its recommendation, and the Parked section goes.

b) Keep Parked sections, but offer any parked query older than 30 days for dropping at your next review.

#### HOLD-CLOSE - What happens to packages on hold?

since 2026-10-31 · from run/ideas-board · not yet in `queries.md`

**Context:** Nine packages are on hold, six of them since 18 to 20 October. While held they still receive messages they cannot act on, such as the ORCA-ENV-LEAK security fix waiting in tools-burndown. Closing a held package would home its decisions, move its messages and parked queries to the ideas list and remove its folder, leaving the Project `paused`; reopening means creating a fresh package.

**Query:** Should a package on hold for more than 14 days be closed out?

**Options:**

a) (recommended, confidence low - it clears the board fastest, but closing a package is hard to undo cleanly and several held packages, such as tools-burndown, hold live handoffs) Yes, after you have seen what each would close, one package at a time.

b) No: keep held packages, but route new messages for a held package to State of play instead, so nothing waits behind a hold.

c) Keep held packages as they are.

#### QUICK-FIXES - Fix the easily undone contradictions now?

since 2026-10-31 · from run/ideas-board · not yet in `queries.md`

**Context:** Three contradictions can be fixed in Knowledge Islands Principal alone, each easily undone: nine Project pages whose `lifecycle` disagrees with their package (seven `active` but on hold, two `active` with no package); the finished Knowledge acquisition folder, which the standard says should already be gone and whose history Git keeps; and the eight duplicated parked entries in this package.

**Query:** Should one small run make these three fixes now, as a bounded change you approve?

**Options:**

a) (recommended, confidence medium - each fix is small, within this island and recoverable from Git, though the lifecycle wording for held Projects needs a choice between `paused` and keeping `active`) Yes: set the seven held Projects to `paused` and the two packageless ones to `planned`, remove the Knowledge acquisition folder, and remove the duplicate entries.

b) Fold them into the wider rollout instead, after the standards change.

#### DONE-PRUNE - Prune the seven finished records?

since 2026-10-31 · from run/ideas-board · not yet in `queries.md`

**Context:** Seven records are done and accepted but still on their roadmaps: [KI-OBSERVA-BRG-004](/Users/krisbrown/kis/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-004-turn-feedback-sending-on.md), [KI-HARNESS-GOV-232](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-232-any-package-coordination.md), [KI-HARNESS-GOV-233](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-233-typed-work-naming-readers.md), [KI-HARNESS-GOV-234](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-234-footer-markdown-writers.md), [KI-TOOL-KI-CLI-173](/Users/krisbrown/kis/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-173-regular-coordination-readers.md), [KI-TOOL-KI-CLI-174](/Users/krisbrown/kis/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-174-typed-work-naming-readers.md) and [KI-TOOL-KI-CLI-175](/Users/krisbrown/kis/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-175-footer-markdown-writers.md). Pruning is yours to approve; it removes the file from the roadmap and Git keeps it.

**Query:** Should the seven done records be pruned now?

**Options:**

a) (recommended, confidence medium - they are closed and pruning is recoverable from Git, but this run has not rechecked each one's closure evidence) Yes, through `ki-accept`'s prune, each repository in turn, after a check that each closure is complete.

b) Leave them until each owning work's next mark.

#### PRINCIPAL-READOPT - Whether the 22 records that left adoption are re-adopted

since before 25 October 2026 · from run/fields-personal-principal · not yet in `queries.md`

**Context:** The rule turned `horizon: triage` into `status: triage` for 22 drafts. In this Capital, that draft-on-triage combination already meant captured intake, so the meaning holds, but leaving triage now needs your approval. Five are date-bound and now fall outside selection: the half-term break ([KB-PRINCIPAL-018 (pruned)](https://github.com/krisb/personal-principal/blob/acd6e5c73c58b88a486c7c23805949fdb2515e1b/Streams/Roadmap/KB-PRINCIPAL-018-plan-half-term-break-with-lauren.md)), Halloween ([KB-PRINCIPAL-019 (pruned)](https://github.com/krisb/personal-principal/blob/b10b24dff565565536dffaa9d6b6d3e343df7983/Streams/Roadmap/KB-PRINCIPAL-019-plan-halloween-activity.md)), Lauren's birthday ([KB-PRINCIPAL-024 (pruned)](https://github.com/krisb/personal-principal/blob/b10b24dff565565536dffaa9d6b6d3e343df7983/Streams/Roadmap/KB-PRINCIPAL-024-plan-laurens-birthday.md)), the railway tickets before expiry ([KB-PRINCIPAL-025 (pruned)](https://github.com/krisb/personal-principal/blob/acd6e5c73c58b88a486c7c23805949fdb2515e1b/Streams/Roadmap/KB-PRINCIPAL-025-use-north-york-moors-railway-tickets.md)) and your daughter's birthday on 27 October ([KB-PRINCIPAL-027 (pruned)](https://github.com/krisb/personal-principal/blob/acd6e5c73c58b88a486c7c23805949fdb2515e1b/Streams/Roadmap/KB-PRINCIPAL-027-mark-daughters-october-birthday.md)).

**Query:** Should the five date-bound records be adopted now while the other 17 stay in triage?

**Options:**

a) (recommended, confidence medium - the mechanical result matches the old meaning, but the dated items fall before their next likely review) Adopt the five date-bound records now through `ki-next`, as `draft` at Now or Next with the proposed kind and size, and leave the other 17 in triage for ordinary intake review.

b) Leave all 22 in triage until the next personal triage review.

c) Adopt all 22 again at once through `ki-next`, each with a horizon chosen afresh.

#### PRINCIPAL-KIND-SIZE - Confirming the proposed kind and size

since before 25 October 2026 · from run/fields-personal-principal · not yet in `queries.md`

**Context:** The table above proposes a kind for the 6 adopted records that lack one, a kind for each of the 26 triage records to set at adoption, and a size for 33 records. [GDR-KI-PRINCIPAL-016](/Users/krisbrown/kis/knowledge-islands/ki-principal/Admin/Governance/Decisions/GDR-KI-PRINCIPAL-016-priority-and-size-on-work-records.md) makes these the owner's judgement. Until the `ki` release that accepts the fields, a writer leaves out any field the installed `ki` rejects. The harness already accepts `size`, as [KB-PRINCIPAL-045 (pruned)](https://github.com/krisb/personal-principal/blob/8f33dbb7cb00afda9b4abd186de15721bf02c37a/Streams/Roadmap/KB-PRINCIPAL-045-redraw-mermaid-diagrams-in-archify.md) shows.

**Query:** Do you confirm the proposals, with any changes, so that a follow-up run can write them?

**Options:**

a) (recommended, confidence medium - the sizes are provisional judgements from each record's Goal and Boundary, and are revisited before Ready anyway) Confirm them as listed. A short follow-up run then writes the 33 sizes and the 6 adopted kinds now, and the triage kinds are set at adoption.

b) Confirm them with the changes you name, for example `xl` on [KB-PRINCIPAL-004 (pruned)](https://github.com/krisb/personal-principal/blob/b10b24dff565565536dffaa9d6b6d3e343df7983/Streams/Roadmap/KB-PRINCIPAL-004-develop-intentional-life-thesis.md).

c) Hold all kind and size writes until the `ki` release, and write them together with the other repositories.

#### STREAMS-CHECKER-GAP - The Streams checker cannot see the migrated fields

since before 25 October 2026 · from run/fields-personal-principal · not yet in `queries.md`

**Context:** The Streams checker, both installed and in the workspace at `88cce3e5`, does not warn on a retired horizon, on `initiative` or on a theme beside a Project. It lists `initiative` as a known field. The standard's migration window says the checkers warn on all three, and the window closes on "a complete scan of that inventory showing no gaps", so a scan of Streams Capitals would wrongly report no gaps. This matches VALIDATOR-PARITY, which ki.tools-burndown holds.

**Query:** Should the coordinator route this gap to the harness owner before the remaining Streams migrations?

**Options:**

a) (recommended, confidence high - verified directly: the before and after audits gave the same 34 warnings, and the workspace `streams.ts` has no rule for these shapes) Route it now as a Messages line to the harness work that owns the checkers, and have each remaining field run prove its result with a front-matter scan, as here.

b) Fold it into the next harness release run, and carry on with the front-matter scans meanwhile.

## Queries

### HOST-SYNC-CLOSE - Close the parked host-sync design too?

**Context:** On 1 November you closed the four HOST-* questions as superseded: "I think we've moved on from some of these points ... it's a step back from where we are now". Each Mac's Rig sync thread now runs every 15 minutes, with terra seven minutes after sol, and repeats until the Mac and GitHub are level. Sol leads Knowledge Islands, Personal and Legal. One older parked query, HOST-SYNC, still asks which primary or secondary order and offset hosts should publish in, which that rule has already answered. While it stays parked, six design notes stay with it: `host-sync-and-reply-trades`, `host-sync-report` and the four in `host-sync/`. Deleting them is undone easily from Git. One Observatory report links `host-sync-and-reply-trades` by local path.

**Query:** Should the parked HOST-SYNC query be closed as superseded by the same 1 November words, so that the host-sync design notes can go at the next mark?

**Options:**

a) (recommended, confidence high - your 1 November words and the 31 October answers already settle its order, offset and lead host, and Git keeps the notes) Close HOST-SYNC as superseded. Delete the six notes at the next mark, pointing the Observatory report's link to the notes' last revision. Keep `host-reconcile/plan.md` until the sol Rig thread has received the IMPORTANT line that links it.

b) Keep HOST-SYNC parked and the six notes with it until a later design discussion.

### CITED-NOTES - Delete graduated notes that other files still link to?

**Context:** Five design notes have done their job, because their decisions now live in the skills, but other files still link to them by local path. `coordination-lessons` and `method-feedback` are listed as sources by three harness skills that this work owns. `gfm-migration`, `unattended-work` and `work-id-shape-plan` are linked from the tools-burndown, Personal State of play, baseline-rollout and Observatory packages. Deleting a note breaks those links. The standard already handles a removed record the same way: it links the last version on GitHub. Moving a note to a topic folder breaks the links just as deleting it would.

**Query:** May these five notes be deleted once every link to them points to the note's last version on GitHub?

**Options:**

a) (recommended, confidence high - it is the same pinned-link rule the standard uses for pruned records, and nothing is lost from Git) Yes. A run repoints the three harness source lists itself and sends each other package one message line with its pinned link. The notes are deleted at the mark after those links land.

b) No. Keep the five notes until the Project closes.

### OLD-PROPOSALS - What to do with five proposals never decided

**Context:** Five design notes from 21 to 27 October were never adopted or dropped:

- `tags-model`, on subject tags.
- `gov-227-storage-schema`, a storage-schema draft for the [KI-HARNESS-GOV-227](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/docs/ideas/KI-HARNESS-GOV-227-repository-storage-declarations.md) idea.
- `overload-process`, on what to do when you are overloaded.
- `observatory-review`, a review view in the Observatory, already listed in the Observatory's own ideas file.
- `agent-control-contract`, accepted on 21 October as a tools-ki build contract, though I could not prove it was delivered.

Under IDEAS-IN-GRAPH, future ideas belong in the knowledge graph, not in a work package. Where ideas finally live (IDEAS-HOME) is still open.

**Query:** Should these five become one-line ideas, with the notes then deleted, or stay where they are?

**Options:**

a) (recommended, confidence medium - it empties the folder without losing the ideas, but IDEAS-HOME, which decides their final home, is still open) Record each as one line in the current ideas list, `design/empty-board/ideas.md`, linking the note's last version on GitHub. Leave GOV-227 and the Observatory review view where they already are. First check `agent-control-contract` against tools-ki, and delete only if it was delivered. Then delete the notes.

b) Keep all five in `design/` until IDEAS-HOME is settled.

### TOPIC-SET - Which topic folders to pilot

**Context:** On 1 November you said this work's folders "should really be aligned to the topic", each holding its briefs, design and reports. Once the deletions above are made, what is left falls into the 13 topics in the Findings table. Fine-grained topics close and can be deleted whole sooner, for example `discussions/` once its rollout lands. Coarser topics would mean fewer folders to look through: `work-package/` could take package layout, package definition and discussions, and `agents/` could take landscape, Orca and listening. Whether each topic has `briefs/` and `reports/` subfolders or keeps them side by side stays with LAYOUT-SHAPE.

**Query:** Should this package's pilot use the 13 proposed topics, or a coarser set?

**Options:**

a) (recommended, confidence medium - small topics match how the work closes and make each folder a natural unit to tidy, but you asked for simplicity and fewer folders also serve that) The 13 topics as proposed.

b) A coarser set of about eight: `work-model/`, `work-package/`, `capture-model/`, `empty-board/`, `agents/`, `host-sync/`, `nascent-areas/` and `publication-recovery/`, with `window-31-oct/` folded into `work-model/`.

### 🤖 → 👤 Handoff to supervisor · since 01:04 GMT

👤 4 with you

- [with you] HOST-SYNC-CLOSE · owner · since 01:04
- [with you] CITED-NOTES · owner · since 01:04
- [with you] OLD-PROPOSALS · owner · since 01:04
- [with you] TOPIC-SET · owner · since 01:04

🧵 ki.prj.ways-of-working
