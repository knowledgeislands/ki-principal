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

### CLI-PREVIEW - How public commands that change state offer a preview

**Context:** You settled that `mgit repair` writes by default, and on 24 October left the wider convention open. Today the two harness standards for tools ([tool repositories](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-tools/references/standards-tool-repositories.md) and [CLI conventions](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-tools/references/standards-cli-conventions.md)) still require a preview step before a repair writes, contradicting that decision. `mgit repair`, `ki repo repair` and `ki repo conform` already act by default; `ki repair` and Almanac repair keep preview gates. Some writes must keep their safeguards: Rig remove (deletes data), Rig repair (a reviewed proposal file), firewall and service changes, and remote host removal. The command inventory is retained in [wow-dryrun-survey.report.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/wow-dryrun-survey.report.md).

**Query:** Should public commands that change owned state write by default and offer `--dry-run`/`-n` as the preview, with both standards reconciled now and each tool changed later through its own work?

**Options:**

a) (recommended, confidence medium - reviewed; a masked blind review on Codex recommended it, keeping medium because your decision settled `mgit` only, not every shipped command) Write by default; `--dry-run` and `-n` show the same changes without applying them, and must prevent local and provider changes, not just the final write; `--check` is a read-only verification that fails on findings; `--apply`, `--write` and `--fix` are not routine write gates, and `--yes` only confirms. Keep named, documented exceptions for data deletion, publication, reviewed proposals and connection-critical changes. Reconcile both standards first, then change each tool through its owning work, with no fleet-wide flag migration.

b) Keep the current convention with `mgit repair` as the one exception, and hold the survey for a later decision.

### AREA-COLUMN - how the skill catalogue shows functional areas

**Context:** The website's skill catalogue (`/docs/skills/catalogue/`) now groups the 64 skills by their 8 source concerns and adds a finder table (skill, source concern, functional area), rendered as inline HTML because the site's Markdown gate does not accept a generated row loop as a table. The 10 functional areas exist only inside the harness's generator code, which calls them a diagram reading aid rather than published metadata; the website's sync parses that code directly, so a harness refactor could break the sync without any change in membership. The inline finder is live now, taken provisionally. A masked blind review on Codex disagreed with the worker: the worker recommended keeping the inline finder (medium confidence) as it needs no upstream change; the reviewer recommended the harness publish the area table in its generated `skills/README.md` block (high confidence) as a stable boundary, at the cost of a coordinated harness, sync and page change and a new pin.

**Query:** Should the area finder stay as the website's own inline table, or should the harness publish the area table for the website to consume?

**Options:**

a) (recommended, confidence medium - reviewed, views differ: a stable published boundary outlasts parsing generator code, and the live finder serves until it lands) Keep the live finder now and send the harness a message to publish the area table in its README block, then switch the sync to it at the next pin.

b) Keep the inline finder as the lasting form and accept the coupling to the generator's code.

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

### MGIT-CACHE-SCOPE - what to build first

**Context:** Six routes were weighed. The Codex review and the note agree that `--repos-from` (an explicit path-list selector, route F) is the right primitive and that teaching `push` to skip locally (route C) is wrong. They differ on timing for your two-flag cache (route D): the reviewer would ship F and the `sync` direction switches first and defer D until isolation is specified; the note says the selection key, membership check, stop-on-expiry and an optional set name specify it, and that F alone gives you nothing at the prompt without `jq`.

**Query:** Which shape goes to `tools-mgit` as the first record?

**Options:** a) (recommended, confidence medium - reviewed blind on Codex, which disagrees on timing, agreeing on everything the first cut would contain) `--repos-from` and `--to-cache [NAME]`/`--from-cache [NAME]` together, one record; `sync --push-only` and `--pull-only` as a second record. b) `--repos-from` and the `sync` switches first; the cache flags as a later record once the primitive has been used. c) The cache flags alone as you proposed, one default slot, no `--repos-from` and no name.

### MGIT-CACHE-FAILED - whether a checkout the sweep failed on goes into the cached set

**Context:** In the mgit cache design, `mgit --to-cache st` records the checkouts needing attention for five minutes, and `mgit --from-cache push` acts on just those. A sweep can fail in a checkout, for example on an `index.lock`, a missing upstream or a broken worktree. The sweep's exit status of 1 already stops an `&&` chain, so `--from-cache` is reached after a failure only by `;` or a separate command, and the follow-up may be destructive. The design note recommends including failed checkouts (medium confidence). A masked blind review on Codex disagreed at high confidence: a failed sweep is an unknown result, not a confirmed target for a possibly destructive command. Both views are shown.

**Query:** Are checkouts the sweep failed on included in the cached set?

**Options:** a) (recommended, confidence medium - reviewed blind on Codex, which disagreed: the design favours a superset needing attention, the reviewer holds that an unknown result should not be a target) Exclude them, but keep their names and count in the set as diagnostics, and warn on every `--from-cache` that the selection is incomplete. This is the reviewer's added option. b) Include them, and show the count of failed candidates in the age line, as the design note recommends. c) Exclude them silently, so the set holds only checkouts that ran and printed something. d) Make `--from-cache` refuse to run while the set records any failed checkout, until the sweep is repeated clean.

### SPEC-ORPHAN-OWNER - the orphan `+/_WORK/ki.specifications/` folder belongs to ki.portable-specifications

**Context:** `+/_WORK/ki.specifications/` was opened on 19 October 2026 as the Project work package for KI Specifications (`cd388627`). That day the Project was renamed under its PROJECT-NAME decision: the rename run's own report (`rename.report.md`, in the orphan folder) records that the whole package became [`+/_WORK/ki.portable-specifications/`](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/work.md), Project [Portable specifications](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/portable-specifications.md) under theme Model; Git confirms every tracked file moved as a pure rename in `a90aea3b`, and the renamed package has been on hold since 20 October (`release: Kris says resume`). The 25 `*.report.md` files left in the old path were run reports that nobody had ever tracked, so the rename did not carry them; all 25 are byte-identical copies of the run reports still held in `/Users/krisbrown/.local/state/ki/agents/specifications/`, and they were swept into Git by the `chore: baseline` commit `e78fff63` on 24 October. The renamed package holds no reports and had already pruned its only tracked one (`create-project.report.md`, `5b8ac0f3`) as homed. The orphan folder therefore has no identity of its own and carries nothing that its run packets do not.

**Query:** Do you accept ki.portable-specifications as the owner, with the repair being a bounded run that removes `+/_WORK/ki.specifications/` by explicit path once that package confirms its reports are homed?

**Options:**

a) (recommended, confidence high - reviewed: a masked Codex review chose this course independently, verified all 25 files byte-identical by SHA-256, and added that duplication proves bytes, not homing) Owner ki.portable-specifications. Send one line to its `messages.md` naming the folder and its 25 reports; when its steward next tidies, it checks each report's outcome has a durable home, its queries are carried, and live references still work (its decisions log line 67 points at `query-review-6.report.md`, which exists only at the old path), then deletes only the eligible reports, each by explicit path; nothing is deleted before that check.

d) The reviewer's added course: authorise a bounded exception to that Project's hold so its own steward does the same per-report check and tidy now.

b) Owner ki.portable-specifications, but delete the folder now in a bounded run, relying on the run packets as the surviving copy, without the package's own homing check.

c) Keep the folder as it is until the Project resumes, with no message sent.

### RADAR-REPORT-HOME - `radar-confirm-2.report.md` came from ki.chezmoi and its evidence already lives in UE-108

**Context:** [KI-HARNESS-REV-012](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-REV-012-thoughtworks-radar-input.md) cites `/Users/krisbrown/.local/state/ki/agents/chezmoi/radar-confirm-2.report.md` as a "verified source check". That path is a run packet of the [ki.chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.chezmoi/work.md) work (Project [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md), theme Rig). Its decisions log shows the chain on 24 October 2026: radar-confirm launched at 12:28 BST (`b5c6c299`), relaunched as radar-confirm-2 at 12:31 BST with a read-only fetch grant for the public ThoughtWorks pages under Kris's 12:25 instruction (`230aadc8`), its finding that the fourth ring is Caution recorded at 12:35 BST (`1d9613dd`), and radar-confirm-3 then homing that finding at 12:41 BST in two places: the chezmoi record [PERSONAL-DOTFILES-UE-108](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/PERSONAL-DOTFILES-UE-108-decide-tool-radar.md), whose "Confirmed scope and ring vocabulary" section carries the source URLs, the check date and the verbatim FAQ ring excerpts, and the harness record REV-012 (`7a759440`, `c4285065` in the log). The report file itself was never copied into the ki.chezmoi package, never tracked in any repository, and no longer exists in the chezmoi run directory or the archive; both records cite a dead local path. UE-108 holds everything the citation stood for.

**Query:** Do you accept ki.chezmoi as the owner, with the durable home being UE-108's ring-vocabulary section rather than a recreated report, and the repair a repointing of both citations?

**Options:**

a) (recommended, confidence high - the report's content is carried verbatim in UE-108 and the file is gone, so no provenance is invented) Owner ki.chezmoi. A bounded run repoints REV-012's citation to the public ThoughtWorks Radar and FAQ pages plus UE-108's section, and replaces UE-108's self-citation of the dead path with the same public pages and the 24 October check date; two small `docs(roadmap)` commits, one per repository, with REV-012 kept at triage.

b) Owner ki.chezmoi, and ask it to recreate the source check as a tracked note under the harness `ki-model-radar` sources reference, then cite that from both records.

c) Leave both citations as they are, treating the dead path as historical.

### FALLBACK-DATE - the HOLD-1 fallback review date for the trades hold

**Context:** TRADES-FATE makes opening the Trades revamp Project the review trigger and keeps a fixed date on HOLD-1 as the fallback, but names no date. The notice in `ki-trades` SKILL.md is the only place the date is written and the HOLD-1 check warns once it passes. wow-harness-a set 2026-12-31, two months out, so a planned revamp that slips still gets a review before the year ends.

**Query:** Does 2026-12-31 stand as the HOLD-1 fallback date, or do you want another?

**Options:** a) (recommended, confidence high - the date is a fallback only, the revamp Project is planned, and a one-line change moves it) Keep 2026-12-31. b) Name another date and a run moves the notice in a one-line commit.

## Parked

- PERM-PROMPTS-SETTINGS - whether to change the chezmoi-managed permission settings; Kris, 25 October: "can we come back to it later?". Recommended: not now, revisit if Kris leaves bypass mode.
