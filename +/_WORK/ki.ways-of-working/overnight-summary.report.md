# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md)

**🤖 → 🧑 Handoff to supervisor · Summary at 05:35 BST · last mark 22:34 BST**

---

**Where to read this in the Observatory:** the Observatory now has a Work view that shows this summary as the newest report of Ways of working. I checked this at 05:36 BST on a second copy, started from today's code on port 1676 and stopped afterwards, which rendered the whole summary. The service you normally open, `http://127.0.0.1:1675/`, still runs code from before tonight, so it has no Work view yet. To see it there, run `launchctl kickstart -k "gui/$(id -u)/uk.me.kris.rig.observatory"` and open the Work view. Until then the file is `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/overnight-summary.report.md`.

## Done

- **The Knowledge Islands territory now runs on the work model.** Every step Kris set in the migration order, from the harness to the skills audit, has run. Only the check-pass walk-through with Kris and the other territories remain.
- **Harness, phase 1** ([migrate-phase1](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/migrate-phase1.report.md)): the work model is written into the ki-agentic-harness skills, standards and checkers, and pushed, under [KI-HARNESS-GOV-210](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-210-work-model-write-in.md). The record is still Awaiting review because of one broken link (HARN-ANCHOR).
- **Migration plan** ([migrate-plan](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/migrate-plan.report.md)): dry-run scripts were written for the Capital, the harness and tools-rig. Kris answered all five of its queries at 03:31.
- **tools-ki, phase 2, and the release** ([migrate-phase2b](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/migrate-phase2b.report.md)): Kris cleared the stuck rebase at 03:50. tools-ki now reads `Streams/Themes` and `+/_WORK`, and ships `ki work status`. `ki agent` homes runs in work folders. Released as **v0.11.0** and installed through Homebrew on this Mac; all checks passed. The release number is provisional (RELEASE-NUMBER).
- **The move into work folders, phase 3** ([migrate-apply](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/migrate-apply.report.md)): checkpoints and threads in ki-principal are now nine work folders in `+/_WORK/`, with five more in `+/_WORK_REVIEW/` for you to review. Initiatives are now four themes in `Streams/Themes/`. The Mac Studio files are merged and ki-principal is pinned to v0.11.0. The harness and tools-rig follow suit. Everything is pushed. Five judgement calls are provisional (MIGRATE-CALLS).
- **This run's home**: the `ways-of-working` run now records `+/_WORK/ki.ways-of-working/` as its home. I checked this at 05:28.
- **Acceptance** ([accept-review](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/accept-review.report.md)): [KI-TOOL-KI-CLI-127](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-127-agent-status-live-threads.md) passed independent review and is accepted. [KI-HARNESS-GOV-210](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-210-work-model-write-in.md) was left for you because of one failed audit. Correction: one of another session's tools-ki commits was pushed beyond ROUTINE's reach (TOOLS-PUSH).
- **Rest of the territory** ([territory-rest](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/territory-rest.report.md)): the website's command list is regenerated for v0.11.0, which needed a small parser fix (SITE-PARSER), and CI passed. ki-specifications, ki-techne-harness and the other tools needed nothing.
- **Observatory** ([observatory-bringup](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/observatory-bringup.report.md)): three records are Awaiting review, all pushed. They are the Work view, which shows each work's newest report and so shows this summary, the Review queue over work folders, and the Beacon raising stuck work. A fourth record is Ready. The service still needs a restart before it serves them.
- **Skills audit** ([skills-audit](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/skills-audit.report.md)), read-only: no skill should retire. It recommends renames for ki-pmo, ki-checkpoint and ki-pmo-design, one owner for each rule now written twice, and keeping the name `ki agent`. These are seven queries for you.
- **Check pass** ([check-pass](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/check-pass.report.md)): audits ran across all 20 Knowledge Islands repositories. 15 have no failures. The failures in the other five come from older causes, not from the migration. All theme and Project references resolve, and no live note links an old area. 13 links in open records were repointed (provisional, RECORD-LINKS).
- **Decisions log**: none of tonight's approvals was taken "provisional, on Fable's opinion". No run stopped in a way that needed one.

## In Progress

- **Tools burndown roadmap** (run `ways-of-working/tools-burndown`, running since 05:27 BST): it is working through [KI-TOOL-KI-CLI-144](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-144-older-runs-start-seen.md), whose code and tests are done and whose coverage gate is running. [KI-TOOL-KI-CLI-142](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-142-preserve-harness-release-settings.md) is next. So far it has done this:
  - captured [KI-TOOL-KI-CLI-146](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-146-ki-quiet-setting.md), the KI_QUIET setting, in tools-ki;
  - recorded the independent review of [KI-TOOL-RIG-CORE-060](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-060-single-target-operation-speed.md), and delivered two tools-rig features: Dock layouts filtered by profile, and clearer doctor causes;
  - captured the mgit plan records [KI-TOOL-MGIT-CLI-020](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-020-safe-parallel-sync.md) to [KI-TOOL-MGIT-CLI-022](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-022-external-member-review-findings.md).
  - tools-rig and tools-mgit are level with origin. tools-ki is one commit ahead, with its work in flight.
- **This summary** (run `ways-of-working/morning-summary`): it finishes when this report is committed and checked in the Observatory.

Outstanding - no action requested now:

- The Observatory service runs the code from before tonight's deliveries. Restarting it is step 1 of its restart prompt below, and it asks you first.
- The other Mac still has ki 0.10.5. Its next session should run `brew update && brew upgrade knowledgeislands/tap/ki`.
- `ki.ways-of-working` shows as stuck in `ki work status` until its coordinator writes its next beat.
- 28 report-link findings (PMO-7) sit in other work folders. Each is fixed at that work's first mark: ki 6, ki.chezmoi 8, ki.tools-burndown 11, and 1 each in ki.observatory, ki.mac-studio-setup and ki.knowledge-acquisition.
- Older audit failures belong to their own owners: SCR-11, the pre-commit shape, in ki-principal and the harness; CAP-2 and MD051 in the harness; and missing toolchain installs for apps-knowledgeislands.info and ki-techne-harness. On [KI-TECHNE-OPS-027](/Users/krisbrown/workspaces/knowledge-islands/ki-techne-harness/docs/roadmap/KI-TECHNE-OPS-027-agent-host-tailscale-key-minting.md), ITEM-3 waits for the Techne Programme Hold to lift.
- The website's `command-groups.md` still cites the v0.10.1 manual. Bringing it up to date needs a prose review in the website's own work.
- tools-rig had five source files dirty from another session overnight, and they were left alone.

## Queries

### GOV-206-CLOSE - close the activity-homes record

**Context:** [KI-HARNESS-GOV-210](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-210-work-model-write-in.md) delivered what [KI-HARNESS-GOV-206](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-206-activity-homes-and-coordination.md) asked for: Activities homed in regular work or their Project, and coordination folded into the work model.

**Query:** Should [KI-HARNESS-GOV-206](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-206-activity-homes-and-coordination.md) close as delivered by [KI-HARNESS-GOV-210](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-210-work-model-write-in.md)?

**Options:**

a) (recommended, confidence high - the delivery is the same change, and it closes in one step) Close it as delivered once [KI-HARNESS-GOV-210](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-210-work-model-write-in.md) is accepted. b) Keep it open and review it separately.

### HARN-ANCHOR - one broken link holds back the harness write-in

**Context:** [KI-HARNESS-GOV-189](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-189-move-thread-between-hosts.md) links to a `project-close` heading, which phase 1 renamed to "Finishing Project work". Its sentence still uses thread-model words. The governing audit therefore fails, and acceptance allows no waiver, so [KI-HARNESS-GOV-210](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-210-work-model-write-in.md) stays Awaiting review. Every other check passed.

**Query:** Shall a short run fix that sentence and its link, so that a fresh review can accept [KI-HARNESS-GOV-210](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-210-work-model-write-in.md)?

**Options:**

a) (recommended, confidence high - a one-sentence documentation fix with a mechanical check) Launch the fix run, then a fresh review that accepts under ACCEPT-NIGHT's terms if the audit passes. b) Leave it Awaiting review for you to review by hand.

### REPO-OWNERSHIP - ki-repo still names the old working areas

**Context:** The `ki-repo` standards and its COVERAGE check still name `+/_CHECKPOINTS/` and `+/_THREADS/` as working areas, not `+/_WORK/` and `+/_WORK_REVIEW/`. No record covers the change yet. Unless it lands first, the other territories would migrate onto a contract that does not know the new areas.

**Query:** Should one harness record move ki-repo's ownership and COVERAGE to `+/_WORK/` and `+/_WORK_REVIEW/` before the other territories migrate?

**Options:**

a) (recommended, confidence high - a small change, and a prerequisite for the other territories) Capture one ki-agentic-harness record that adds the two new areas and still accepts the old ones with a warning, and land it before the other territories. b) Fold it into the HARN-ANCHOR fix run.

### REPORT-SHAPE - run reports in the work-model shape

**Context:** Phase 1 wrote its report in the old thread-model shape, because its brief asked for that. Every later brief tonight asked for the work-model run report, and every later report used it.

**Query:** Do you confirm that briefs ask for the work-model run report from now on?

**Options:**

a) (recommended, confidence high - the live standard sets it, and tonight's runs already follow it) Confirm it. b) Keep the thread-model shape until phase 5.

### RELEASE-NUMBER - the one approved release shipped as v0.11.0

**Context:** You approved one tools-ki release, expected to be 0.10.6. It shipped as v0.11.0 because it adds the `ki work status` command. It is still the one release. The pre-approved fix release would now be 0.11.1, and none was needed.

**Query:** Do you confirm v0.11.0 as tonight's one release?

**Options:**

a) (recommended, confidence high - a new command is a minor bump under semantic versioning, and the release is already out through Homebrew) Confirm it. b) Name a different numbering for the next release. v0.11.0 itself stands, because re-tagging would rewrite a published release.

### MIGRATE-CALLS - five judgement calls in the move

**Context:** migrate-apply made five calls inside the pre-approvals, each on the recommended course:

1. took chezmoi off the defer list, because its log was committed and no chezmoi agent was running;
2. dropped Foundations' upkeep paragraph from its theme page;
3. removed links from Project notes into work folders, except the Paperclip design link;
4. treated the tracked Mac Studio decisions log as canonical;
5. left the history line in [KI-HARNESS-GOV-198](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-198-reply-forms.md) that names the old path.

**Query:** Do you confirm all five calls?

**Options:**

a) (recommended, confidence high - each follows a pre-approved option, and Git holds every earlier text) Confirm all five. b) Name any to reverse, and a follow-up run reverses it.

### TOOLS-PUSH - another session's tools-ki commit went out

**Context:** `1d72fa94` was pushed beneath the acceptance of [KI-TOOL-KI-CLI-127](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-127-agent-status-live-threads.md). It is another session's documentation-only change to [KI-TOOL-KI-CLI-140](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-140-git-hygiene-estate-audit.md). ROUTINE covers other sessions' commits only in ki-agentic-harness and ki-principal.

**Query:** Do you accept that push as it stands?

**Options:**

a) (recommended, confidence medium - small, documentation-only and fast-forward, but its content has not been reviewed) Accept it. Its author keeps responsibility for its content. b) Have its session review it, and revert it with a new commit if it is wrong.

### SITE-PARSER - the website generator fix

**Context:** The website's command-list generator refuses any roff macro it does not know, and v0.11.0's manual uses a bare `.IP`. territory-rest taught the generator to treat `.IP` like `.PP`, with a test, and regenerated the command list. That gives 119 commands in 18 groups, and CI passed.

**Query:** Do you confirm `4f70461` and `05af1ad` as pushed?

**Options:**

a) (recommended, confidence high - a one-line change with its own test, and CI passed) Confirm both. b) Revert both and ask tools-ki to drop the `.IP` from its manual instead.

### OBS-SESSIONS-RETIRE - when the Sessions readers retire

**Context:** The Beacon record was shaped to retire the Sessions instrument's checkpoint and thread readers. Legacy folders still exist in other territories, though, and runs homed outside a work folder show only through those readers. The retirement was therefore held back until the tolerance window closes. This is provisional.

**Query:** Should the Sessions readers retire at phase 5 under a record of their own?

**Options:**

a) (recommended, confidence medium - nothing is lost while legacy folders remain) File a record for the retirement, blocked on phase 5, and take [KI-OBSERVA-VIS-027](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-027-themes-in-streams-read.md) alongside it. b) Fold the retirement into [KI-OBSERVA-VIS-027](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-027-themes-in-streams-read.md) as its last step. c) Retire them now, so legacy-homed runs drop out of the Observatory.

### OBS-STREAMS-VIEW - what the Sessions instrument becomes

**Context:** Once threads and runs leave it, the Sessions instrument shows only themes and Projects.

**Query:** Should it become a Streams view once its thread and run readers retire?

**Options:**

a) (recommended, confidence medium - the name then says what it shows, and the Work view owns runs) Rename it Streams in the retirement record, and keep the `sessions` addresses redirecting. b) Keep the name Sessions. c) Fold themes and Projects into the Work view and retire the instrument.

### OBS-WITH-YOU-SIGNAL - one Beacon note per work with you

**Context:** The Beacon raises one note for each work or item that is with you, each on its own line, rather than one note with a count. This is provisional.

**Query:** Do you confirm one note per line?

**Options:**

a) (recommended, confidence medium - each note lands on its own row and shows as new when it arrives) Confirm it. b) Raise one note carrying the count.

### OBS-KI-CONTRACT-GAPS - views and review count derived in the Observatory

**Context:** `ki/work-status/v1` carries entries, not the five views, and gives the review count only in its text form. So the Observatory works both out itself, which is provisional.

**Query:** Should tools-ki publish the views and the review count in a later schema?

**Options:**

a) (recommended, confidence medium - one derivation, not two that can drift apart) Ask tools-ki for both in `ki/work-status/v2`, and keep the Observatory's own derivation until then. b) Keep deriving them in the Observatory.

### OBS-RECORD-FIELDS - Project field and short titles

**Context:** The four Observatory records carry `project: ways-of-working`, and their titles are cut to four words or fewer to pass the ITEM-1 audit. This is provisional.

**Query:** Do you confirm the Project field and the shortened titles?

**Options:**

a) (recommended, confidence high - they pass the audit and keep the rollout under one Project, as you set in ONE-PROJECT) Confirm both. b) Move the records to the observatory Project when the rollout ends.

### PMO-NAME - rename ki-pmo

**Context:** "PMO" is not a word in the work model. The skill's standard already calls itself the "Coordinating-work standard". A rename touches 9 repositories' declarations and 9 tools-ki source files, and needs a tools-ki release beyond tonight's ceiling. It is cheapest before the other territories migrate.

**Query:** Should ki-pmo be renamed before the other territories migrate?

**Options:**

a) (recommended, confidence medium - the name matches its standard and pairs with ki-delegation) Rename it `ki-coordination`, with `ki-pmo` accepted as an alias through the tolerance window. b) Rename it `ki-coordinator`, to match the output style and hook. c) Keep `ki-pmo`.

### CHECKPOINT-FATE - what ki-checkpoint becomes

**Context:** ki-checkpoint now owns the work file, `+/_WORK/<id>/work.md`, which `ki work status` and the Observatory read. The job is real, but "checkpoint" now names only a move, and ownership of the work folder is split across three skills.

**Query:** Should ki-checkpoint become the one owner of `+/_WORK/` under a new name?

**Options:**

a) (recommended, confidence medium - one owner for the work folder, and a name that says what it holds) Rename it `ki-work-file`, and move the work-folder and review-area rules into it from ki-pmo and ki-delegation. b) Merge it into ki-pmo. c) Keep `ki-checkpoint` as it is.

### WORK-FOLDER-DEDUP - one home for each rule written twice

**Context:** The rules for capturing decisions, pruning the work folder and closing finished work are written out in both ki-delegation and ki-pmo. They agree today, but every change has to be made twice.

**Query:** Should each rule have one owner, with the other skill linking to it?

**Options:**

a) (recommended, confidence medium - it ends the double maintenance) Put the decisions log and its life cycle in ki-pmo, and pruning and close-out with the work-folder owner. ki-delegation keeps only the run side, with links. b) Keep both copies, and add a test that they stay identical.

### DESIGN-NAME - rename ki-pmo-design

**Context:** ki-pmo-design shapes new work before any record exists, and does not depend on ki-pmo. The `ki-design-*` names already belong to website and interface design.

**Query:** Should ki-pmo-design be renamed along with ki-pmo?

**Options:**

a) (recommended, confidence low - it names what the skill shapes, but no name is an obvious fit) Rename it `ki-work-design`. b) Rename it `ki-coordination-design`, to follow PMO-NAME.

### STREAMS-SLIM - slim ki-repo-kb-streams

**Context:** ki-repo-kb-streams owns the Streams container and the Enactment gate. Its PROPOSE, READY, ROLLOUT and ITERATE modes only point to ki-next, ki-plan and ki-implement, and its status table repeats ki-work-roadmap's.

**Query:** Should ki-repo-kb-streams keep only its own jobs?

**Options:**

a) (recommended, confidence medium - it removes a copy of the lifecycle table that can drift) Keep the skill and its name, retire the four routing modes, and link to ki-work-roadmap's status table. b) Merge it into ki-repo-kb's Streams section. c) Keep it as it is.

### WORKER-CLI - keep `ki agent`

**Context:** In the work model, worker is a role and an agent is a party. A coordinator is a worker that `ki agent` never launches, and `ki worker` would sit one letter away from `ki work`. Separately, the help text of `ki agent decide` and `ki agent home` still uses thread-model words.

**Query:** Should `ki agent` keep its name?

**Options:**

a) (recommended, confidence medium - the command acts on agents and runs, and it avoids a near-clash with `ki work`) Keep `ki agent`, close the rename idea, and send the help-text corrections to tools-ki as a trade. b) Rename it `ki worker`, keeping `ki agent` as an alias. c) Rename it `ki run`.

### UPDATE-SHAPE - three-line updates for every coordinator

**Context:** On 18 October you asked that every update says what's done, what's left on the plan and what's outstanding. This thread does that now, but ki-pmo still asks for one or two lines.

**Query:** Should ki-pmo require the three lines in every coordinator's timed updates?

**Options:**

a) (recommended, confidence medium - you asked for it in plain terms, and nothing in it is specific to this Project) Adopt it in ki-pmo at the report-shape review around 21 October, and regenerate the hook line and output style. b) Keep it a rule for this thread only.

### COV-1 - ki-checkpoint's coverage check looks at the old area

**Context:** ki-checkpoint's coverage marker still looks for `+/_CHECKPOINTS/`. Every migrated repository will therefore warn until this changes.

**Query:** Should the harness move the coverage marker to `+/_WORK/` before the other territories migrate?

**Options:**

a) (recommended, confidence high - it is one fixed path in one skill) Capture a harness record that moves it to `+/_WORK/`, still accepting `+/_CHECKPOINTS/` through the tolerance window, and land it before the next territory. b) Accept one COV-1 warning per migrated repository until the window closes.

### RECORD-LINKS - links in open records count as live

**Context:** check-pass repointed 13 links in six open records, in `e434304c` (harness) and `09f5f3b3` (tools-ki), and left done records as history. Eight more KI records link into other territories' `+/_THREADS/`.

**Query:** Should territory migrations rewrite old-area links in open records across the estate?

**Options:**

a) (recommended, confidence medium - open records are still acted on, and the rewrite is mechanical) Confirm tonight's repointing, and add that step to each territory run, pinning pruned targets to their last revision. b) Treat records as history everywhere, and revert the two commits.

### PMO-CODE - PMO-7 checks identifiers inside code spans

**Context:** The PMO-7 report-link check flags record identifiers inside inline code, such as a quoted commit subject, which cannot hold a link.

**Query:** Should PMO-7 skip inline code spans as it skips fenced blocks?

**Options:**

a) (recommended, confidence medium - a code span quotes literal text) Capture a harness record so that PMO-7 skips inline code spans. b) Keep the rule, and rewrite such quotes without backticks.

### 🤖 → 🧑 Handoff to supervisor · since 05:35 BST

🤖 1 running · 🧑 25 with you

- [running] tools burndown roadmap, [KI-TOOL-KI-CLI-144](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-144-older-runs-start-seen.md) · run/ways-of-working · since 04:27
- [with you] GOV-206-CLOSE · owner · since 03:24
- [with you] HARN-ANCHOR · owner · since 04:54
- [with you] REPO-OWNERSHIP · owner · since 03:24
- [with you] REPORT-SHAPE · owner · since 03:24
- [with you] RELEASE-NUMBER · owner · since 04:33
- [with you] MIGRATE-CALLS · owner · since 04:47
- [with you] TOOLS-PUSH · owner · since 04:54
- [with you] SITE-PARSER · owner · since 05:00
- [with you] OBS-SESSIONS-RETIRE, OBS-STREAMS-VIEW, OBS-WITH-YOU-SIGNAL, OBS-KI-CONTRACT-GAPS, OBS-RECORD-FIELDS · owner · since 05:25
- [with you] PMO-NAME, CHECKPOINT-FATE, WORK-FOLDER-DEDUP, DESIGN-NAME, STREAMS-SLIM, WORKER-CLI, UPDATE-SHAPE · owner · since 05:04
- [with you] COV-1, RECORD-LINKS, PMO-CODE · owner · since 05:16
- [committed] ki-principal, ki-agentic-harness, tools-ki, tools-rig, tools-mgit, apps-observatory.local and apps-knowledgeislands.info, pushed; tools-ki one burndown commit ahead, in flight

## Left on the plan

The order you set at 02:49 and 02:50, with where each step stands:

1. Harness phase 1: done. [KI-HARNESS-GOV-210](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-210-work-model-write-in.md) waits on HARN-ANCHOR.
2. tools-ki reader and release: done, v0.11.0.
3. The Capital: done.
4. The rest of the Knowledge Islands territory: done.
5. The tools brought in line: the Observatory's work is Awaiting review, and its service needs a restart. Tools burndown is working its roadmap.
6. The check pass with you: the report is ready. **Next: walk through it with you** and take the queries above.
7. The skills audit: the report is ready. **Next: your answers.** Any rename then needs a harness change, a tools-ki release beyond 0.11.1 (reserved for you) and a declaration sweep.
8. The other territories: wait for steps 6 and 7. See Before the other territories below.
9. Then the tolerance window closes (phase 5). The Sessions readers retire, and the old-area readers in tools-ki come out.

Also left: review the five works in `+/_WORK_REVIEW/` in ki-principal and `ki.regular.skill-reviews` in the harness. Each work fixes its report links and prunes at its first mark. STREAM-10 close-out assessments are due for chezmoi, mac-studio-setup, paperclip-capture-and-rebuild and website.

## Provisional approvals for Kris to confirm

None of these was taken on Fable's opinion. Each followed the recommended option inside the night's pre-approvals.

- **REHOME** (thread call, 04:52): `ki agent home ways-of-working --work ki.ways-of-working`, done and checked.
- **RELEASE-NUMBER**: the one release shipped as v0.11.0, not 0.10.6.
- **MIGRATE-CALLS**: the five calls listed in its query.
- **CLI-127 live checks**: the live Codex launch and a real `ki agent send` were not run, one needing the network and the other writing into another session's run. They were accepted as covered by the record's sandbox checks.
- **TOOLS-PUSH**: another session's commit `1d72fa94` was pushed in tools-ki.
- **SITE-PARSER**: the website parser fix and the regenerated command list.
- **OBS-SESSIONS-RETIRE, OBS-WITH-YOU-SIGNAL, OBS-KI-CONTRACT-GAPS and OBS-RECORD-FIELDS**: the Observatory's four calls.
- **RECORD-LINKS**: 13 links repointed in six open records.

## Restart prompts

Paste each into an interactive session in the ki-principal checkout, `/Users/krisbrown/workspaces/knowledge-islands/ki-principal`. All of them are on hold since 04:30 BST.

**Tools burndown** (KI > Foundations > Tools burndown). The `ways-of-working/tools-burndown` run has been working its roadmap overnight, so take stock of that run first:

```text
Resume KI > Foundations > Tools burndown from its work file, /Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown/work.md, under current ki-pmo and ki-delegation since 2026-10-18T02:55:00Z: re-bootstrap, act on its Messages FIRST-STEP first, read the pick-up block, take stock (including `ki agent status ways-of-working`: the ways-of-working run tools-burndown worked KI-TOOL-KI-CLI-144 and onwards overnight, captured KI-TOOL-KI-CLI-146, reviewed KI-TOOL-RIG-CORE-060 and captured KI-TOOL-MGIT-CLI-020 to 022; let it finish before launching in tools-ki), put the parked queries back, restart authorised work (Rig first), then banner.
```

**Observatory** (KI > Model > Observatory):

```text
Resume KI > Model > Observatory, work id ki.observatory, from /Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.observatory/work.md under current ki-pmo and ki-delegation since 2026-10-18T03:30:38Z.

The ways-of-working run observatory-bringup did the four bring-up items in apps-observatory.local, all pushed to main: KI-OBSERVA-VIS-025 Work instrument, KI-OBSERVA-VIS-026 Review queue work folders and KI-OBSERVA-BCN-007 Beacon raises stuck work are Awaiting review; KI-OBSERVA-VIS-027 Themes in Streams read is Ready. Its report is /Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/observatory-bringup.report.md; its five OBS- queries are in /Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/overnight-summary.report.md.

First steps:
1. Ask Kris, then restart the service so it serves these deliveries: launchctl kickstart -k "gui/$(id -u)/uk.me.kris.rig.observatory", and confirm http://127.0.0.1:1675/ answers and the Work view shows the ways-of-working overnight summary.
2. Re-read the work file, its decisions and the Messages section, mark, and take stock (ki agent status; apps-observatory.local roadmap and git status).
3. Walk Kris through the three records awaiting review in the Work, Review queue and Beacon views, and take the OBS- queries.
4. Put back the parked queries OBS-SESSIONS-ACCEPT, OBS-REVIEW-ACCEPT, OBS-REVIEW-OPEN and OBS-OVERDUE-TITLE.
5. Then deliver KI-OBSERVA-VIS-027 as a run, and the carried work: the serving and live-reload triage record and unit 3, Capture feedback.
Then banner.
```

**State of play** (KI > SoP, work id `ki`):

```text
Resume KI > State of play, work id ki, from /Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/work.md under current ki-pmo and ki-delegation since 2026-10-18T03:30:38Z: re-bootstrap, act on its Messages first (the MIGRATED line: at this mark cut the carried State of play to next steps, Messages and parked tags, and fix its 6 report links), take stock, put the parked queries back, restart authorised work, then banner.
```

**Mac Studio setup** (KI > Rig > mac studio setup):

```text
Resume KI > Rig > Mac Studio setup, work id ki.mac-studio-setup, from /Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.mac-studio-setup/work.md under current ki-pmo and ki-delegation since 2026-10-18T03:30:38Z: re-bootstrap, act on its Messages first (MIGRATED; hosts.md now lives in Pillars/Engineering Practice/Architecture/Hosts, Roles and Layers.md and the decisions in force in Streams/Projects/mac-studio-setup.md), take stock, put the parked queries back, restart authorised work, then banner.
```

**Chezmoi** (Chezmoi > misc):

```text
Resume KI > Rig > Chezmoi, work id ki.chezmoi, from /Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.chezmoi/work.md under current ki-pmo and ki-delegation since 2026-10-18T03:30:38Z: re-bootstrap, act on its Messages first (MIGRATED; its 8 report links are fixed at this mark), take stock, put the parked queries back, restart authorised work, then banner.
```

The `ports` session in your sidebar has no work folder in ki-principal, so it has no prompt here. Restart it from its own record, or name its home and the next run will give it one.

## Before the other territories

These must be settled first, in this order:

1. **The check pass with you**: take COV-1, RECORD-LINKS and PMO-CODE.
2. **The skills audit answers**, so the other territories migrate once onto the final names: PMO-NAME, CHECKPOINT-FATE, WORK-FOLDER-DEDUP, DESIGN-NAME, STREAMS-SLIM, WORKER-CLI and UPDATE-SHAPE. A rename needs a harness change and a tools-ki release beyond 0.11.1, which is yours to approve.
3. **The harness contract**: REPO-OWNERSHIP and COV-1 land, and [KI-HARNESS-GOV-210](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-210-work-model-write-in.md) is accepted after HARN-ANCHOR.
4. **The other Mac** moves to ki v0.11.0 and is level with origin in every repository.
5. **What is waiting in the other territories** (old shape, read today through the tolerance window):
   - personal-principal: 5 checkpoints, 7 threads and 7 Initiatives;
   - hnr-principal: 11 checkpoints, 10 threads and 3 Initiatives;
   - legal-principal: 2 checkpoints, 1 thread and 7 Initiatives;
   - Acquire: 2 checkpoints and 1 thread;
   - va-principal 3, si-principal 2 and er-principal 2 checkpoints;
   - techmedix: none.
6. **Cross-territory links**: eight KI records in mcp-m365, mcp-gsuite and tools-ki link into hnr-principal's and Acquire's `+/_THREADS/`. They are rewritten in those territories' runs if RECORD-LINKS a) is confirmed. mcp-m365 and mcp-gsuite wait for the Humans Not Robots migration.
7. **Each territory is its own authority**: moving other territories is reserved for you, and needs your word for each one.

```text
Send KI > Model > Ways of working back to its worker under current ki-pmo and ki-delegation since 2026-10-17T21:34:13Z: re-read the work file and decisions, mark, fresh summary with carried-forward open points, take stock, restart authorised work, then banner.
```
