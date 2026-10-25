# ki.ways-of-working queries

## Open

### STEWARD-FIELD - where a package records who looks after it

**Context:** The assignment needs a committed home that names a work, never a host or session. The brief proposed a new `state.md` field, `steward: self` or `steward: work/<sop id>`. Both reviews reject `self`, which is not a holder value, and both reject reading the assignment as the holder. The Claude review would reuse `work.md`'s existing `worker` field: `worker: work/va` when the State of play looks after the package, and `agent` when the Project's own thread does. That adds no field and leaves the closed field set unchanged. Stewardship changes only when Kris opens or closes a thread, the slow rate `work.md` suits, and the holder stays derived from `state` and `worker` as today. The Codex review wants a dedicated assignment with its own vocabulary, distinct from holder and session, and leaves the exact field to the design. A separate field keeps the assignment visible beside the state, and it avoids a third sense of "steward" only if it is named with care.

**Query:** Should the assignment be recorded in a new dedicated field rather than `work.md`'s existing `worker` field?

**Options:**

a) (recommended, confidence medium - reviews disagree; the Codex review and a masked blind review on Codex want a dedicated field, as lasting responsibility should not share a field with the holder that pick-up reads, while the Claude review prefers reusing `worker` as it adds no field) A new dedicated field, taking `work/<id>` values only, never `self`, changed or removed as part of the acknowledged handover.

b) Reuse `work.md`'s `worker`: `worker: work/<sop id>` while the State of play looks after the package, `agent` while its own thread does.

### LEGACY-PREFIX - how a `repo_code` rename passes the streams and roadmap audits

**Context:** the `ki-repo-kb-streams` streams audit and `ki-work-roadmap`'s checks fail every record not prefixed with the current `repo_code`. A rename therefore has to happen in one sweep, or the repository fails its audit until every record has moved. Personal is renaming KB to PERSONAL that way now. An allowance, an optional list of former codes that existing records may keep while new records take the new code, would allow a gradual path. It would need both checkers and the tools-ki readers to change.

**Query:** Should a `repo_code` rename stay a one-sweep change, written into `ki-work-roadmap`, rather than gaining a legacy-prefix allowance?

**Options:**

a) (recommended, confidence medium - reviews disagree; a masked blind review on Codex would add the former-code list, since issued identifiers are cited outside the repository and a sweep breaks those links, while renames are rare and Personal's runs as one sweep, so documenting the sweep costs one paragraph where the allowance costs two checkers and tools-ki) Write the rename into `ki-work-roadmap` as one sweep: every record and in-repository reference in one commit, pruned links keeping their pinned revisions.

b) Add an optional legacy-prefix list accepted by both audits for existing records only, with new records required to use the current code.

### PARTIAL-REPOS - how a repository with only Pillars and Resources fits the model

**Context:** HNR keeps hnr-shared, which holds only Pillars and Resources, beside hnr-principal. ZONE-1 requires all five zones, and the registry binds one source store per declared repository, so hnr-shared cannot be declared. Its store is written up only in tracked notes, so `ki repo store` and the source audits do not see it. Kris asked Knowledge Islands to decide where partial repositories fit, and whether a person keeps a personal "work" knowledge base beside a person-agnostic company Capital, adding: "there's [a] kind [of] weird thing here we maybe need to come back to." The question reaches the Structure note, `ki-repo-kb` and tools-ki, beyond this work's method scope.

**Query:** Should PARTIAL-REPOS wait as an idea until Kris opens it, rather than starting a design now?

**Options:**

a) (recommended, confidence medium - reviews disagree; a masked blind review on Codex would start the design now, as your explicit question and the store-audit gap justify a bounded look, while your own words defer it, and nothing is broken beyond HNR's tracked-notes workaround) Record it as an idea on the Ways of working Project note with the HNR evidence linked, and start a `ki-work-design` brief when Kris opens it.

b) Start a `ki-work-design` brief now covering partial repositories, the personal "work" knowledge base and the store-binding gap.

### UNATTENDED-FIELD - recording unattended eligibility on records

**Context:** Personal's prototype assessed 76 records against eight ordered criteria, 9 eligible, 21 near-miss and 46 attended, and proposed a record field. The brief proposes an optional `unattended` mapping in `ki-work-roadmap` with `verdict` (`eligible`, `near-miss`, `attended`), `criterion`, `question` and `assessed`, an absent mapping read as attended, and the criteria owned by `ki-delegation`.

**Query:** Should records carry this optional `unattended` mapping, with the eight criteria in `ki-delegation`?

**Options:**

a) (recommended, confidence medium - reviews disagree; a masked blind review on Codex would keep the assessment in a per-window note with no record field, as eligibility depends on the grant and can go stale, and review the eight criteria before standardising them, while Personal's assessment shows the criteria sort real records, and a field spares rereading every record at each window) Adopt the mapping and the criteria, refreshed at each status or horizon change.

b) Keep the assessment in a per-window note, with no record field.

### BOOT-HOME - Who owns the bootstrap from a fresh machine to a working coordinator

**Context:** `ki-bootstrap` covers the harness and skill activation and then stops; `ki-coordination` starts at the opener. Between them, chezmoi's hook and style binding, the Capital's declarations, `ki skill add ki-work-design`, the readiness checks and `ki agent prompts` with `claude --name` are written nowhere as one path, so a fresh machine can fail silently at the hook or the style. Kris's goal is that "when we do a bootstrap ... it works really well".

**Query:** Which skill holds the one bootstrap checklist?

**Options:**

a) (recommended, confidence high - reviewed; a masked blind review on Codex agreed, as it follows the existing ownership boundary and gives silent activation failures one accountable home) `ki-bootstrap` owns the one machine-readiness checklist, ending with a "Ready to coordinate" result and observable checks that the hook and output style actually work; `ki-coordination`'s Bootstrap gains a "Before the opener" step that cites it and keeps the session half; a `ki doctor` check in `tools-ki` backs it later, and readiness never depends on it before it exists.

b) `ki-coordination` owns the whole path, machine half included, and `ki-bootstrap` links to it

c) a guide in ki-principal under `Pillars/` owns the narrative, and both skills link to it

### TRADES-FATE - What becomes of ki-trades now its hold is overdue

**Context:** `ki-trades` is on hold with a review due by 21 October 2026, now four days past, and its `HOLD-1` audit item warns. Existing trades keep full support. HANDOFF-AS-MESSAGE moved handoffs and rollouts to `messages.md`, so it now governs only the trade routes `.ki.toml` declares. The planned Trades revamp Project's outcome, a succinct trade policy granting the same as now, is that narrower job.

**Query:** Should `ki-trades` be narrowed now or kept on hold?

**Options:**

a) (recommended, confidence high - reviewed; a masked blind review on Codex agreed that a bounded clarification aligns the skill with the message contract without granting new authority) Narrow `ki-trades` now to the routes the Capital's declared trade policy grants, with a pointer to `messages.md` for handoffs and rollouts; keep full support for existing trades and the ban on new submissions; make opening the Trades revamp the next review trigger, with a finite calendar backstop kept on HOLD-1.

b) keep it on hold with a new review date, untouched until the Trades revamp opens

### RECAP-NAME - What ki-recap's checkpoint argument is called

**Context:** `ki-recap` offers `checkpoint <thread>`, which composes `ki-work-package` UPDATE. "Thread" now means a session acting on work, and the argument is really a work id. The three recap forms (one session, one work since its mark, the unattended window's return) otherwise have clean scopes.

**Query:** Should the argument become `checkpoint <work id>`?

**Options:**

a) (recommended, confidence high - the model made work the unit and the argument already resolves an id) rename it to `checkpoint <work id>`, accepting the old word through the tolerance window

b) keep `checkpoint <thread>` and define it in the Glossary as the work the thread carries

### CLI-PREVIEW - How public commands that change state offer a preview

**Context:** You settled that `mgit repair` writes by default, and on 24 October left the wider convention open. Today the two harness standards for tools ([tool repositories](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-tools/references/standards-tool-repositories.md) and [CLI conventions](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-tools/references/standards-cli-conventions.md)) still require a preview step before a repair writes, contradicting that decision. `mgit repair`, `ki repo repair` and `ki repo conform` already act by default; `ki repair` and Almanac repair keep preview gates. Some writes must keep their safeguards: Rig remove (deletes data), Rig repair (a reviewed proposal file), firewall and service changes, and remote host removal. The command inventory is retained in [wow-dryrun-survey.report.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/wow-dryrun-survey.report.md).

**Query:** Should public commands that change owned state write by default and offer `--dry-run`/`-n` as the preview, with both standards reconciled now and each tool changed later through its own work?

**Options:**

a) (recommended, confidence medium - reviewed; a masked blind review on Codex recommended it, keeping medium because your decision settled `mgit` only, not every shipped command) Write by default; `--dry-run` and `-n` show the same changes without applying them, and must prevent local and provider changes, not just the final write; `--check` is a read-only verification that fails on findings; `--apply`, `--write` and `--fix` are not routine write gates, and `--yes` only confirms. Keep named, documented exceptions for data deletion, publication, reviewed proposals and connection-critical changes. Reconcile both standards first, then change each tool through its owning work, with no fleet-wide flag migration.

b) Keep the current convention with `mgit repair` as the one exception, and hold the survey for a later decision.

### INTERIM-REPAIR - small repairs that fall under an adopted record

**Context:** Tending proposes fixing small authorised defects within the pass, but its pilot leaves open what happens when the same repair implements an already adopted record. That record may have a plan, hold or owner the tending pass must preserve. No such record was changed here.

**Query:** Should repairs that implement an adopted record stay with that record's delivery owner and plan?

**Options:**

a) (recommended, confidence high - preserves the existing record's authority, holds and acceptance without inventing an overlapping grant) Keep them with the record's owner and plan; a tending pass may deliver one only when explicitly authorised within those bounds and must leave the evidence with the record, without inferring acceptance.

b) Permit any otherwise authorised small tending repair immediately, then have the record's owner reconcile its plan afterwards.

### INTERIM-FINDING-WRITER - who writes a package finding file

**Context:** The interim note proposes a run writing a finding file when its brief names it. The standard now permits the finding kind, but its Entry points table gives writing and settlement to the own steward; a run writes its report in state and the launcher homes it. The steward can copy the finding at receive, so no new permission is needed for the existing route.

**Query:** Should direct finding-file writing remain with the steward?

**Options:**

a) (recommended, confidence high - matches the inspected entry-point contract and the working report-to-steward handoff) Keep the standard's steward-only package writer; treat the interim note's extra direct-run permission as declined, and carry the finding through the run report when needed.

b) Adopt a bounded run writer entry point for the exact finding file named in its brief, with authority and settlement ownership stated explicitly.

### INTERIM-FINDING-AGE - whether findings need an age warning

**Context:** The interim note proposes warning on an old open finding when its work is not On hold, but supplies no threshold. The current package rubric permits findings and checks their lifecycle without this warning. Choosing an arbitrary age now would create policy unsupported by the pilots.

**Query:** Should an age warning remain deferred until the pilots show what age is useful?

**Options:**

a) (recommended, confidence high - preserves current behaviour and avoids an invented threshold) Defer the age warning in the findings idea; land freshness and settlement rules first and revisit the warning with territory evidence.

b) Require an age warning as part of graduation, with a threshold selected by Kris before implementation.

### INTERIM-HOMEPAGE-OMISSION - what an absent homepage means

**Context:** The settled metadata direction makes configuration the master. Its homepage caution proposes that an absent key means no homepage, so a leftover root-package or GitHub value is stale, but explicitly asks the standard to confirm this before a checker lands. An audit can report drift without clearing a live URL, and a conform proposal can require approval for clearing it.

**Query:** Should omission mean no repository homepage, with stale mirrors reported and clearing separately approved?

**Options:**

a) (recommended, confidence high - follows the settled configuration-master direction while preserving explicit approval before deletion of a mirror) Confirm absence means no repository homepage; audit reports stale root-package and GitHub values, and conform proposes clearing them for explicit approval. Workspace-package homepages remain outside this rule.

b) Treat omission as unmanaged and leave existing mirror values unassessed until a homepage is declared.

### INTERIM-TAG-SCOPE - optional or shape-scoped territory tag types

**Context:** The metadata proposal currently requires exactly one value for every declared territory type on every member. Personal found that a domain type would fit only its sites, so it declares no types. The note explicitly waits for a second territory to need optional or shape-scoped types; neither schema nor checker supports them yet.

**Query:** Should optional or shape-scoped types stay deferred until a second territory demonstrates the need?

**Options:**

a) (recommended, confidence high - follows the note's explicit pilot boundary and keeps the first schema bounded) Keep the every-member rule for initial graduation and retain optional/shape-scoped types as an extension awaiting a second territory's evidence.

b) Include optional or shape-scoped types in the first standardisation design and review their membership and validation semantics before implementation.

### TIDY-GAPS - an orphan package and a missing source report

**Context:** `+/_WORK/ki.specifications/` in ki-principal holds only old reports, with no `work.md` or `messages.md`, so it has no identity or steward. Separately, harness record KI-HARNESS-REV-012 (Thoughtworks Radar input) links to `radar-confirm-2.report.md`, and no tracked copy exists anywhere. Creating package metadata or substituting another source would invent identity or provenance.

**Query:** Should the coordinator find the intended owner of the orphan package and the source report's durable home from their stewards before any repair?

**Options:**

a) (recommended, confidence high - preserves evidence and avoids inventing identity or provenance) Obtain both authoritative homes, then commission bounded repairs.

b) Keep both findings unresolved for Kris's next review.

### AREA-COLUMN - how the skill catalogue shows functional areas

**Context:** The website's skill catalogue (`/docs/skills/catalogue/`) now groups the 64 skills by their 8 source concerns and adds a finder table (skill, source concern, functional area), rendered as inline HTML because the site's Markdown gate does not accept a generated row loop as a table. The 10 functional areas exist only inside the harness's generator code, which calls them a diagram reading aid rather than published metadata; the website's sync parses that code directly, so a harness refactor could break the sync without any change in membership. The inline finder is live now, taken provisionally. A masked blind review on Codex disagreed with the worker: the worker recommended keeping the inline finder (medium confidence) as it needs no upstream change; the reviewer recommended the harness publish the area table in its generated `skills/README.md` block (high confidence) as a stable boundary, at the cost of a coordinated harness, sync and page change and a new pin.

**Query:** Should the area finder stay as the website's own inline table, or should the harness publish the area table for the website to consume?

**Options:**

a) (recommended, confidence medium - reviewed, views differ: a stable published boundary outlasts parsing generator code, and the live finder serves until it lands) Keep the live finder now and send the harness a message to publish the area table in its README block, then switch the sync to it at the next pin.

b) Keep the inline finder as the lasting form and accept the coupling to the generator's code.

### ACCEPT - KI-PRINCIPAL-MOD-009 awaits your review

**Context:** [KI-PRINCIPAL-MOD-009](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-MOD-009-amend-adr-001-staging-wording.md) amends the staging wording of ADR-001 and is delivered and awaiting acceptance. [KI-PRINCIPAL-OPS-014](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-OPS-014-gfm-conversion.md) (GFM conversion) is not yet ready: it still needs its four-client render checks.

**Query:** Do you accept KI-PRINCIPAL-MOD-009 as done?

**Options:**

a) (recommended, confidence high - delivered, its checks pass and nothing depends on it remaining open) Accept it after reading the amended wording.

b) Return it with the change you want.

### REPO-STANDARDS-SET - which skills the Repository standards area lists

**Context:** The website's new feature-area map gives each reader-facing area a docs page and a "Provided by" box naming the harness skills behind it. Repository standards lists the twelve general `ki-repo-*` skills (website, MCP, harness and similar). The four knowledge-base skills, `ki-repo-kb` and its overlays for streams, activities, principal governance and live artifacts, are listed under Knowledge bases and, for some, Recurring work, but not under Repository standards. That is live now, taken provisionally. A masked blind review on Codex disagreed with the worker: the worker preferred leaving them out (medium confidence), so that one skill does not appear in three boxes; the reviewer preferred including them (high confidence), because a knowledge base is a governed kind of repository and the shared membership links the two concerns, at the cost of a longer box that might suggest every repository needs knowledge-base conventions.

**Query:** Should the knowledge-base skills also appear under Repository standards?

**Options:**

a) (recommended, confidence medium - reviewed, views differ: the reviewer's point that a knowledge base is a governed repository kind is sound, and a short line can say these apply only to knowledge bases) Include all sixteen, with the knowledge-base skills marked as applying only to knowledge bases.

b) Keep the live twelve and leave the knowledge-base skills to their own areas.

### UNATTENDED-AND-DUE-DATES - adopt the eight criteria as the unattended assessment

**Context:** Kris, 24 October, through Personal's State of play: "we need to push that into the ways of working thread as something that we need to do an assessment of", and roadmap records should carry an explicit due date or key milestone date "of what they're working towards". The due-date half is done: DUE-FIELD was decided at 01:43 GMT today and harness `1af72f2e` added the optional `target` mapping (`date`, `kind` of `due` or `milestone`, `what`) to the `ki-work-roadmap` format standard, with the nearer date ordering work within one horizon and priority. The assessment half is not. Personal's prototype tests each record against eight ordered criteria, `no-owner-judgement`, `no-outward-act`, `one-repo-authority`, `reversible`, `self-verifiable`, `unblocked`, `scoped` and `agent-step`, the first failure deciding `unattended`, `near-miss` with one question, or `attended`; across 76 open Personal records it found 9, 21 and 46. Each criterion cites an existing rule rather than restating one, and eligibility is not authority. The open query UNATTENDED-FIELD asks only where a verdict is recorded (a record mapping or a per-window note) and bundles the criteria into that choice; the Codex blind review that kept it at medium asked for the criteria to be reviewed before they are standardised. Today `ki-delegation`'s unattended deny list says what a window never does and `ki-coordination`'s unattended windows section says what a coordinator may progress, but neither says how a record is judged eligible, and the format standard states "No unattended-eligibility field is adopted".

**Query:** Should the eight criteria, in their order with the three outcomes, become the eligibility assessment in `ki-delegation`, leaving UNATTENDED-FIELD to decide only where the verdict is recorded?

**Options:**

a) (recommended, confidence medium - the criteria sorted 76 real records cleanly and rest on rules already in the standards, but they have run on one territory and one review asked for scrutiny before standardising; reviewed, views differ: a masked Codex review prefers b), piloting on a second territory first, since one territory cannot show whether near-misses really need only one owner answer or whether reviewers classify alike) Adopt them into `ki-delegation` beside the unattended deny list as the assessment every window plan uses, with a harness run writing them and the field question staying with UNATTENDED-FIELD.

b) Pilot them on one more territory's roadmap in a design note first, then adopt with the lessons.

c) Keep them as Personal's local prototype and let each territory judge eligibility in its window plan.

### DIAGRAM-PRIVATE-CITATIONS - a code citation form for private repositories

**Context:** Kris, 24 October: settle a private-safe diagram citation form, "provided, of course, it's not causing a current failure somewhere"; no audit fails today. The `ki-diagrams` standard already says "Sources cite repository-relative paths. A repository URL in a source's metadata is the repository's own public remote or is omitted", its `traced` field takes repository-relative paths or pathspec globs, and its privacy rule bars a private repository's name, note content or commit subject from any committed source, SVG or HTML. What it lacks is a form for citing the revision and lines a diagram was traced from, because Archify's own citation object accepts a citation only with a repository URL. PERSONAL-TOWER-SITE-019 waits on the answer and PERSONAL-PRINCIPAL-045 shipped without line citations.

**Query:** Should `ki-diagrams` define a URL-free citation for private repositories, carried in the source's own metadata rather than Archify's citation object?

**Options:**

a) (recommended, confidence high - it extends the rule the standard already states, needs no new privacy exception, and the audit can check it mechanically) Yes: for a private repository, each `traced` entry may carry the short revision and a line range, `path:revision:lines`, with no URL; Archify's URL citation is used only where the remote is public; the audit accepts either form. A harness run writes it and Personal's two records follow.

b) Paths only: private repositories cite `traced` paths and nothing finer, as PERSONAL-PRINCIPAL-045 shipped, and the line-level ask is dropped.

c) Allow Archify's citation with the public mirror's URL where one exists and paths only where none does.

### SOP-PROJECT-CARE - whether the model-shape decisions answer it

**Context:** Kris, 24 October: "when you've got a state of play which is running, it also looks after any of the project work packages that are part of that and keeps those sorted out, unless, of course, I've got their own coordination thread, which it should know about somehow ... we need to add to the metadata of the threads, what it's related to ... it should probably be able to sort of keep a good eye on what it is anyway." Since the line was routed, the model-shape loop has answered most of it: at 01:38 GMT Kris accepted CASCADE-STEWARD (a State of play looks after a Project package by explicit committed assignment, changed only by an acknowledged handover when a Project thread opens or closes, with no timeout takeover), CASCADE-REPORT (one Summary across packages, queries tagged `(work id, tag)`), RELATIONS (every package below the main carries `parent`, the main's `covers` is the register) and the host pair, and harness `1af72f2e` carries them. One point differs from Kris's words: the standard does not detect a live thread, because nothing committed can show that a session is alive; it uses the assignment instead. The field that records the assignment is still open as STEWARD-FIELD in `queries.md`. For a package assigned elsewhere, territory work today sends messages, rolls up the five views through `ki work status` and flags rubric-caught folders at its mark, which is the "good eye" the standard offers.

**Query:** Is the line answered by CASCADE-STEWARD, CASCADE-REPORT and RELATIONS plus the open STEWARD-FIELD, with the watch on packages assigned elsewhere kept to messages, views and rubric flags?

**Options:**

a) (recommended, confidence high - Kris accepted the model at 01:38 GMT and it meets each of the three asks, with explicit assignment standing in for thread detection) Yes: dispose of the line as carried, with STEWARD-FIELD the one decision still due.

b) Add a watch: at its mark the State of play also reports each non-stewarded Project package's state, age since its last move and unread message count, so a quiet Project thread shows.

c) Reopen the "know about the thread somehow" ask: design a machine-local liveness signal a coordinator may read before acting on a package.

### SINGLE-THREAD - start the one-thread rollout

**Context:** Kris, 24 October: "I think the basic idea is that for something like Valley Armonia, we really only need to direct it through one single thread, which is focus at the state of play level, and it can then cascade down and deal with all of the work across the work packages that are within all of that ... there's a difference between work packages and threads, which are things working on the work packages ... I know it probably is something that we need to get mapped out ... and there's a lot of documentation to do really." The model-shape report, `design/model-shape-report.md`, maps exactly this: one State of play, many packages, a thread being a session acting on a package, work flowing from a record through its `project` into that Project's package. Its rollout plan has six steps: Kris's decisions (done at 01:38 GMT), one Knowledge Islands Principal record amending the Work Process note and GDR-KI-PRINCIPAL-009 (not started), the harness changes (landed, `1af72f2e`), the tools-ki readers (sent as a WORK-MODEL line to ki.tools-burndown), a pilot of one named Valle Armonia Project package stewarded by `va` for one wave with named exit conditions, and lessons before any other territory adopts it. The stewardship rule says to record the assignment in the owning work's decisions log until STEWARD-FIELD is decided, so the pilot does not wait on the field.

**Query:** Should the rollout continue now with the Work Process note record and the Valle Armonia pilot?

**Options:**

a) (recommended, confidence high - the model is decided and in the harness, the pilot is the plan's own next step and Valle Armonia is the territory Kris named) Yes, both: capture the Principal record for the Work Process note and GDR-KI-PRINCIPAL-009 through the Enactment Process, and open the pilot on one named VA Project package for one wave, the assignment logged in `va`'s decisions until STEWARD-FIELD lands.

b) Document first: the record and the website pages, then the pilot once the note is current.

c) Pilot first and document from what the pilot shows.

### WAKE-SUBSTRATE - whether the outage evidence lifts the launchd deferral

**Context:** Moved from hnr's parked queries on 24 October by Kris's "Move all three to Ways of Working". On 23 October at 02:37 BST, under Kris's grant to act where confidence is high, the coordinator took WAKE-SUBSTRATE a) as reviewed to high: pursue the completion watcher first, label session wakes best effort, defer launchd, doorbells and liveness fields. The watcher has since shipped as `ki agent wait --next` in tools-ki and the standard's Monitoring section. HNR's debrief reports the two 22 October outages: between 03:21 and 05:00 BST every wake hit the plan's session usage limit, and between 06:25 and 07:30 BST the coordinator sat inside one turn waiting on two `rm -rf` permission prompts; it names idle-only firing the main hazard, since a blocked turn silences every wake and notification, and recommends one Rig launchd job on `StartCalendarInterval` running a shell-only check (has `messages.md` changed, has a run finished, has a deadline passed) that spends model time only when something is new, built by Rig and chezmoi once Kris chooses it, with Ways of working writing the contract for a headless coordinator pass. HNR has stopped its own wakes and deploys sites only on request until a durable wake exists. Claude Code's schedules remain session-only and fire only when the session is idle.

**Query:** Should the launchd shell-check wake now become the next unit after the completion watcher, or stay deferred?

**Options:**

a) (recommended, confidence high - reviewed: a masked Codex review agrees, with the contract settling authority, model budget, overlapping passes and unavailable capacity before any job is installed; neither outage is cured by launchd, one being a usage limit and the other a blocked turn, yet it is the only wake that survives a quit and HNR's deploys wait on it) Lift the deferral in order: Ways of working writes the headless-pass contract (what a pass may do, its budget, its report) into `ki-coordination`, then sends the launchd job as a line to ki.chezmoi and ki.mac-studio-setup.

b) Keep the 23 October order: session-only wakes with stop words, revisit after the usage-limit and blocked-turn causes are addressed.

c) Build the launchd job first and write the contract from what it needs.

### CI-RED-DOCS - document-rule failures keep two repositories' CI red

**Context:** After the pin move, `ki-design` CI fails on BIO-1, BODY-11, DEPENDS-4, FILENAME-0, FILENAME-1, FM-6 and ROUTE-1, red since 22 October. `ki-principal` CI fails on BODY-11, COORD-7, COORD-12, DEPENDS-4, FOLDER-1, MD-mech, PRINCIPAL-5, RECORD-2 and STRUCTURE-1, red all day. The dependency findings in both are going to wow-fleet-green. The rest are content and structure rules, some possibly from this work's own folder, and changes to `ki-principal`'s canonical content go through the Enactment Process.

**Query:** May one run fix both repositories' document-rule failures, under one bounded owner approval recorded in the decisions log?

**Options:**

a) (recommended, confidence high - reviewed: a masked Codex review agreed; 230 of 357 findings are mechanical (COORD-7 alone 187), the Enactment Process allows one bounded batch approval, and fixing only this work's folder would leave 273 findings) One run with an enumerated finding and path scope fixes them: each mechanical fix verified before it is applied, and RECORD-2, FOLDER-1, STRUCTURE-1 and any work-package case returned as queries. BIO-1's configuration migration is bounded separately. b) Fix only this work's own folder findings now, and leave the rest to each repository's own work.

### SUMMARY-VISIBLE - the release dispatch line is visible only in the browser

**Context:** When the tap tells consumers about a release, its Notify job writes "Dispatched <tool> <version> to <consumer>" only to the job summary, which GitHub shows on the web page but not through `gh` or the API. The overnight replay check proved delivery from the harness's own run instead.

**Query:** Should the Notify job also print that line to its log, so a future check can be confirmed from the command line alone?

**Options:** a) (recommended, confidence high - a one-line tap workflow change with no behaviour change) Print the line to the log as well, and point the release guide's step 6 at it. b) Leave it, and reword the guide to treat the receiver's run as the proof. c) Do nothing.

### MGIT-CACHE-SCOPE - what to build first

**Context:** Six routes were weighed. The Codex review and the note agree that `--repos-from` (an explicit path-list selector, route F) is the right primitive and that teaching `push` to skip locally (route C) is wrong. They differ on timing for your two-flag cache (route D): the reviewer would ship F and the `sync` direction switches first and defer D until isolation is specified; the note says the selection key, membership check, stop-on-expiry and an optional set name specify it, and that F alone gives you nothing at the prompt without `jq`.

**Query:** Which shape goes to `tools-mgit` as the first record?

**Options:** a) (recommended, confidence medium - reviewed blind on Codex, which disagrees on timing, agreeing on everything the first cut would contain) `--repos-from` and `--to-cache [NAME]`/`--from-cache [NAME]` together, one record; `sync --push-only` and `--pull-only` as a second record. b) `--repos-from` and the `sync` switches first; the cache flags as a later record once the primitive has been used. c) The cache flags alone as you proposed, one default slot, no `--repos-from` and no name.

### MGIT-CACHE-EXPIRY - what `--from-cache` does when the set is missing or older than five minutes

**Context:** Your words were that after expiry "you can still do mgit st and it works as standard", which is true of the plain command either way. The open point is the flagged command. mgit's habit is to stop on selector conflicts and KI zero matches rather than widen; a `--from-cache reset --hard` that silently ran everywhere would be the worst outcome of the feature. The reviewer agrees that missing or expired state must stop.

**Query:** When the set is missing or expired, does `--from-cache <command>` stop with an error, or run the full set with a warning?

**Options:** a) (recommended, confidence high - reviewed; stopping is the only safe behaviour for a destructive follow-up and costs one re-run) Stop with a one-line error naming the set's age and the fix, exit 2, nothing dispatched; a fresh empty set runs nothing and exits 0. b) Warn and run the full selection, as plain `mgit <command>` would.

### MGIT-CACHE-TTL - whether five minutes is fixed

**Context:** You set "not more than 5 minutes". The note fixes 300 seconds from the sweep's start, with no option, so the behaviour is the same on every machine and in every script. A configurable limit would need a setting home mgit does not yet have beyond templates.

**Query:** Is the five-minute limit fixed, or configurable?

**Options:** a) (recommended, confidence high - one constant, no new configuration surface, and your words set the bound) Fixed at five minutes from the sweep's start. b) Configurable, with five minutes as the default, by an environment variable or a future `mgit` setting.

### MGIT-PUSH-ALIAS - adopting the no-cache push guard today

**Context:** Route B is a one-line `mgit -R sh -c '...'` guard that pushes only checkouts ahead of their upstream, costs no network for level ones, keeps push failures visible, and needs no change to mgit. Tested read-only on this machine. It would live in chezmoi as an alias such as `mpush`, handed to the ki.chezmoi work as a message.

**Query:** Do you want the alias now, independent of what `tools-mgit` builds?

**Options:** a) (recommended, confidence high - zero cost, available today, and it remains useful after the cache ships) Yes: hand the alias to ki.chezmoi as a `messages.md` line, and learn `push` over a level set so a plain `mgit push` is quiet. b) No: wait for the `tools-mgit` record.

### MGIT-CACHE-FAILED - whether a checkout the sweep failed on goes into the cached set

**Context:** In the mgit cache design, `mgit --to-cache st` records the checkouts needing attention for five minutes, and `mgit --from-cache push` acts on just those. A sweep can fail in a checkout, for example on an `index.lock`, a missing upstream or a broken worktree. The sweep's exit status of 1 already stops an `&&` chain, so `--from-cache` is reached after a failure only by `;` or a separate command, and the follow-up may be destructive. The design note recommends including failed checkouts (medium confidence). A masked blind review on Codex disagreed at high confidence: a failed sweep is an unknown result, not a confirmed target for a possibly destructive command. Both views are shown.

**Query:** Are checkouts the sweep failed on included in the cached set?

**Options:** a) (recommended, confidence medium - reviewed blind on Codex, which disagreed: the design favours a superset needing attention, the reviewer holds that an unknown result should not be a target) Exclude them, but keep their names and count in the set as diagnostics, and warn on every `--from-cache` that the selection is incomplete. This is the reviewer's added option. b) Include them, and show the count of failed candidates in the age line, as the design note recommends. c) Exclude them silently, so the set holds only checkouts that ran and printed something. d) Make `--from-cache` refuse to run while the set records any failed checkout, until the sweep is repeated clean.

### HNR-LEVEL - bring the Humans Not Robots local copy level by dropping a redundant local commit

**Context:** Overnight a run wrote one line in the Humans Not Robots State of play queue asking HNR to list its confidential sites, but the local copy at `/Users/krisbrown/workspaces/humans-not-robots/hnr-principal` was behind, so it published the line from a separate worktree as `bb404954`. The local copy still holds the original commit `6043f001`, one ahead of and 89 behind `origin/main`. Its single added line is byte-identical on `origin/main`, the tree is clean and there is no stash; git does not match the two commits only because the lines around it moved. The run briefed to level it stopped, as briefed, rather than drop the commit.

**Query:** May the local copy be moved to `origin/main`, dropping the redundant local commit?

**Options:** a) (recommended, confidence high - reviewed blind on Codex, which verified the line byte-identical itself; the tree is clean, nothing unpublished is lost and the command refuses if a tracked file would be) A bounded run runs `git -C /Users/krisbrown/workspaces/humans-not-robots/hnr-principal reset -q --keep origin/main`. b) An offline `git rebase origin/main`, skipping the one commit when it conflicts; the same end state with an extra step. c) Leave it for the next session working in hnr-principal to level.

### REL-MACOS-OOM - ki v0.14.0 cannot publish because the macOS package jobs run out of memory in one test file

**Context:** The Release workflow runs `bun run test` on each packaging runner before packaging. On both macOS runners the vitest worker for `src/tests/cli/agent-control.test.ts` (5284 lines, 544 tests, changed after v0.13.0) ran out of JavaScript heap: 2111 of 2150 tests had passed, and the jobs took 38 and 50 minutes against about 2 for v0.13.0, which suggests heavy swapping on the 7 GB runners. Linux passed, and the same file passes locally on macOS in 153 seconds. Release run 40192625875: <https://github.com/knowledgeislands/tools-ki/actions/runs/40192625875>. Nothing was published and no GitHub release exists. The `v0.14.0` tag is already on origin at `09316eb5` and published tags are never moved, so any fix in the tested commit means a new version. Twelve repositories and the website stay red on DESIGN-2 until a release ships.

**Query:** How should the release proceed?

**Options:** a) (recommended, confidence high - reviewed: a blind Codex review chose the same course independently, adding that per-test sandbox teardown already exists so retained JavaScript state is the likelier cause, and that all three package jobs must pass the full suite before publishing) Fix the test footprint on tools-ki main by splitting `agent-control.test.ts` or freeing its fixtures between groups, give the package job's test step a `NODE_OPTIONS=--max-old-space-size` ceiling matched to the runner, then tag and release `v0.14.1` and continue the pin and website steps against it; leave `v0.14.0` unpublished in place. b) Only raise the heap ceiling in `release.yml` for the package test step, tag `v0.14.1` and re-dispatch. Smallest change, but it may only slow the failure as the file grows. c) Run the test suite on Linux only and let the macOS jobs package without testing, then tag `v0.14.1`. Faster, but it weakens the release gate. d) Leave the release unpublished and the fleet on v0.13.0, with DESIGN-2 red, until a later window.

### WEB-BUILD-ORDER - website CI runs its tests before the site build

**Context:** The website CI runs the audit, then `bun run test`, then `bun run ki:site:build`. The test "passthrough viewers and SVGs remain byte-identical after the site build" in `apps/site/scripts/verify-diagrams.test.ts` reads `apps/site/dist`, which exists only after the build, so on a clean runner the test step fails whatever `KI_VERSION` says. On a fresh clone the suite failed before the build and passed after it (116 + 15 tests). The release run's brief told it to query rather than fix a failure with another cause.

**Query:** Once a release exists, may the website run move `bun run ki:site:build` before `bun run test` in `.github/workflows/ci.yml`, in the same commit as the `KI_VERSION` bump?

**Options:** a) (recommended, confidence high - the test is a post-build check by design and the fix is one line in a file the run already edits) Yes: reorder build before test in the same commit as the pin bump, and watch CI. b) Bump `KI_VERSION` alone and capture the ordering as a website work record for later. c) Skip or remove the dist-dependent test instead.

### TOOLSKI-DEPCRUISE - tools-ki's own CI hits the same checker-root drift once its KI_VERSION moves

**Context:** tools-ki's CI installs released ki v0.13.0 and audits itself. Its checker root is still `tooling/boundaries`, and its `ci.yml` installs it at that path. Nothing fails today because v0.13.0 expects the old name, but the moment tools-ki bumps its own `KI_VERSION` to a release carrying the new harness pin, DESIGN-2 fails, as it already does in a local audit with current ki. A blind review found the rename reaches beyond CI: agent worktree preparation copies the old checker root (`src/core/agent/worktrees.ts:47`), a contract test asserts it (`src/tests/cli/agent-worktrees.test.ts:61`), and `package.json` and the boundary tests name it too. The release itself does not need tools-ki's own `KI_VERSION` to move.

**Query:** Should tools-ki's rename to `tooling/depcruise` and its own `KI_VERSION` bump be folded into the release work in REL-MACOS-OOM, or kept separate?

**Options:** a) (recommended, confidence medium - reviewed, views differ: the release run's view is that it is the same drift the release exists to clear, though it widens the run's scope) Fold the rename and the bump into the next release run, so tools-ki's own CI stays green after the release. b) (the blind review's view, confidence medium - the rename touches agent worktree preparation and its contract test, so it deserves its own verified change, with the pin bumped only once the release installs) Make it a separate, prompt tools-ki change after the release, and leave tools-ki on v0.13.0 until then.

## Parked

- PERM-PROMPTS-SETTINGS - whether to change the chezmoi-managed permission settings; Kris, 25 October: "can we come back to it later?". Recommended: not now, revisit if Kris leaves bypass mode.
