# Review pack - Knowledge Islands documentation on knowledgeislands.info

This pack is for a Claude or ChatGPT chat. Kris points the chat at this file's address on GitHub and the chat talks him through the published documentation. The pack opens with the prompt for the chat, then the review list of the pages and diagrams now live with one line each on what is worth his judgement, then every open query of the Ways of working work copied in full, and ends with the exact shape of the feedback digest the chat writes for Kris to paste back.

The merged plan the pages follow is [website-docs.md](website-docs.md). Delivery runs publish the pages one unit at a time in the order [wow-docs-order.md](../briefs/wow-docs-order.md) gives. As of 05:10 GMT on 25 October 2026 the first five units are live: the section structure, the diagram pipeline, Skills, the ki CLI and the harness section. The Ways of working pages beyond the roadmap lifecycle, Knowledge and Standards are still being written; a section marked **pending** is not yet published, carries no address here and the chat skips it.

## Prompt for the chat

Paste from here to the end of this section into a new chat, or point the chat at this file and ask it to follow the prompt.

> You are reviewing the documentation of Knowledge Islands, a way of keeping knowledge and running work in Git repositories with AI agents, published at <https://knowledgeislands.info>. Your reader is Kris, the owner, who delegated the documentation's design to an automated merge of two proposals and now steers by looking at the published pages. Your job is to walk Kris through the site conversationally, one page or one question at a time, and at the end write a feedback digest in the exact shape given at the end of this pack.
>
> Work from this pack. It has three parts: a review list of the live pages and diagrams with one line each on what to judge, the open queries of the underlying work, and the digest shape. Treat a section marked pending as not yet published: say so and move on. Never comment on code or on how the site is built; comment on whether a reader who uses Knowledge Islands would understand what each thing is, how it works, how they use it and what it provides.
>
> Method: open each page from the review list in order unless Kris chooses another, read it, give Kris a two-sentence impression, then ask him the page's question, offering the recommended answer where the list gives one and letting his answer shape the next question. Open each diagram's interactive view when you reach it and ask its question the same way. Where you see something the list does not ask about and a user would trip over, raise it as a note. Keep each turn short; Kris may answer in a word. When the review list is done, take the open queries in the same way: present each query's Context, Query and Options in full, with the recommended option first, and record Kris's answer by its tag and letter, or his words if he gives neither. Kris may say "skip", "later" or "digest now" at any time; "digest now" ends the walk and you write the digest with what you have.
>
> Rules: do not invent pages, addresses or facts about the site; if a page fails to load, record that in the digest under Notes. Do not propose redesigns; record Kris's steer. Do not write anything back to GitHub or anywhere else; the digest is a message in the chat for Kris to copy. Use British English and no em-dashes.

## Website review list

Pages and diagrams are grouped as the site groups them. Each live entry gives its address and one line on what Kris should judge there: design and use, never code. Where the merge took a choice it most wanted his view on, the line is marked **steer** and gives the recommended answer. A diagram's address opens its interactive view in the browser; the same diagram sits inline on the page named beside it.

### Docs landing and navigation

- <https://knowledgeislands.info/docs/> - **steer**: Atlas now shows Field Guide and Docs, the Projects catalogue sits in a block at the foot of this page instead of in the navigation, and the section grid shows eight sections for now because Knowledge and Standards appear only once their first page lands; is the catalogue easy enough to find, and does the grid read as a reading order? Recommended: keep the merge, because the catalogue answers "what is this" and the sections answer "how do I".
- <https://knowledgeislands.info/projects/> - unchanged, reached from the Docs landing block; does it still need its own place in the navigation now that it sits on the Docs landing?

### Skills, `/docs/skills/`

- <https://knowledgeislands.info/docs/skills/what-a-skill-is/> - does a reader who has never installed a skill understand what one is and what it will and will not do for them?
- <https://knowledgeislands.info/docs/skills/how-the-skills-fit-together/> - **steer**: eleven diagrams on one page, the skill map and ten area maps; is that the right page for them, or should each area have its own page? Recommended: one page, because the areas are a way of reading the map and not ten separate subjects.
- <https://knowledgeislands.info/docs/skills/catalogue/> - **steer**: sixty-four skills with one description each, grouped by where each is kept, with a finder table giving each skill's functional area, and no page per skill; is that enough, or do you want a page for every skill? Recommended: no per-skill pages, because the catalogue carries each description without drift and the explanatory sections carry the depth. The AREA-COLUMN query below asks where the finder's areas should come from.
- <https://knowledgeislands.info/docs/skills/by-outcome/> - are the outcomes the ones you would actually look for, and does naming the Ways of working, Knowledge and Standards pages as plain text until they exist read as a promise or a gap?

Diagrams on the fit-together page, vendored from the harness:

- <https://knowledgeislands.info/diagrams/vendored/ki-agentic-harness/skill-map.html> - skill map on how-the-skills-fit-together; can you find a skill you know and tell its shape and area at a glance, and does the interactive view earn its new tab, or should it open in an overlay on the page? Recommended: new tab for now, overlay as later work.
- <https://knowledgeislands.info/diagrams/vendored/ki-agentic-harness/skill-area-fundamentals.html> - Fundamentals area map; does the caption's "look for" reading make the diagram useful to someone who is not a harness developer?
- <https://knowledgeislands.info/diagrams/vendored/ki-agentic-harness/skill-area-records-and-code.html> - Records and code area map; do edges arriving from outside the area read as reliance rather than clutter?
- <https://knowledgeislands.info/diagrams/vendored/ki-agentic-harness/skill-area-coordination.html> - Coordination area map, the busiest of the ten; is it still legible inline, or only in the interactive view?
- <https://knowledgeislands.info/diagrams/vendored/ki-agentic-harness/skill-area-work-and-delivery.html> - Work and delivery area map; does it show the lifecycle skills as a set you would reach for together?
- <https://knowledgeislands.info/diagrams/vendored/ki-agentic-harness/skill-area-repository-types.html> - Repository types area map; does one shape per repository kind help a reader choose the right skill?
- <https://knowledgeislands.info/diagrams/vendored/ki-agentic-harness/skill-area-agentic-systems.html> - Agentic systems area map; is the Paperclip skill standing apart confusing or honest?
- <https://knowledgeislands.info/diagrams/vendored/ki-agentic-harness/skill-area-environment.html> - Environment area map; do the two portable roots and their adapters read as one idea?
- <https://knowledgeislands.info/diagrams/vendored/ki-agentic-harness/skill-area-acquire.html> - Acquire area map, three nodes; is a diagram this small worth the space on the page?
- <https://knowledgeislands.info/diagrams/vendored/ki-agentic-harness/skill-area-signals.html> - Signals area map, three nodes and no edges; same question, is it worth the space?
- <https://knowledgeislands.info/diagrams/vendored/ki-agentic-harness/skill-area-design.html> - Design area map, two nodes; same question, and should the smallest areas share one figure?

### Ways of working, `/docs/ways-of-working/`

- <https://knowledgeislands.info/docs/ways-of-working/roadmap-lifecycle/> - the former planning-and-delivery page at its new address, moved but not yet rewritten, so it still speaks from the harness's view; judge only whether it sits naturally under Ways of working and leave the content until the rewrite lands.
- The work model, work packages, coordination, background runs, work design, trades, recurring work, findings and tending - **pending**; being written now.

### Knowledge, `/docs/knowledge/`

- Knowledge bases, query-save-update, acquiring knowledge and recap-and-handover - **pending**; the section is declared and will appear on the Docs landing when its first page lands.

### Standards, `/docs/standards/`

- Repository standards, decision records, engineering and Git, writing and diagrams - **pending**; the section is declared and will appear on the Docs landing when its first page lands.

### The ki CLI, `/docs/ki/`

- <https://knowledgeislands.info/docs/ki/command-groups/> - **steer**: rewritten around the eighteen manual groups, a paragraph each, with the command-groups diagram; is that the right depth for the CLI section, or should the three added pages carry more and this one less?
- <https://knowledgeislands.info/diagrams/site/command-groups.html> - command-groups diagram on that page; do the eighteen groups labelled by what each operates on help you pick a group faster than the page's prose?
- <https://knowledgeislands.info/docs/ki/work-and-agents/> - new; does grouping the work model, background agents and batch commands by what a user is doing beat one page per manual group?
- <https://knowledgeislands.info/docs/ki/repositories-and-territory/> - new; six manual groups on one page; can you tell registry, repository and territory commands apart as you read?
- <https://knowledgeislands.info/docs/ki/trades-and-acquisition/> - new; does putting trades, acquisition and knowledge-base search together make sense to a user, or is it a leftovers page?
- <https://knowledgeislands.info/docs/ki/getting-started/>, <https://knowledgeislands.info/docs/ki/commands/>, <https://knowledgeislands.info/docs/ki/local-commands/>, <https://knowledgeislands.info/docs/ki/naming-and-locations/>, <https://knowledgeislands.info/docs/ki/operator-guides/>, <https://knowledgeislands.info/docs/ki/capability-lifecycle/>, <https://knowledgeislands.info/docs/ki/update-upgrade/> and <https://knowledgeislands.info/docs/ki/chatgpt-local-capture/> - refreshed to v0.13.0. **Steer**: the site describes the last release only, not what is on main; is that what you expect a user to read? Recommended: yes, the last reviewed release.

### KI Agentic Harness, `/docs/ki-agentic-harness/`

- <https://knowledgeislands.info/docs/ki-agentic-harness/how-the-harness-works/>, <https://knowledgeislands.info/docs/ki-agentic-harness/installing-a-harness/>, <https://knowledgeislands.info/docs/ki-agentic-harness/onboarding/>, <https://knowledgeislands.info/docs/ki-agentic-harness/repositories/>, <https://knowledgeislands.info/docs/ki-agentic-harness/using-skills/> and <https://knowledgeislands.info/docs/ki-agentic-harness/tuning/> - refreshed; with the skills pages and planning-and-delivery moved out, does this section still read as a whole about running a harness?
- <https://knowledgeislands.info/docs/ki-agentic-harness/agent-environment/> - new; is bindings, budgets and housekeeping one subject to a reader, or three?
- <https://knowledgeislands.info/diagrams/site/agent-environment.html> - agent-environment diagram on that page; does inventory above and budgets below make the split between configuration and runtime health obvious?

### Served but not yet on a page

- <https://knowledgeislands.info/diagrams/vendored/ki-agentic-harness/thread-model.html> - the harness's thread-model diagram, vendored for the pending coordination page; look only if curious, and judge whether a coordinating thread, its runs and its returns read as one picture.

## Open queries of the Ways of working work

Every open query in [`queries.md`](../queries.md) as of this pack, copied in full with Context, Query and Options. The chat presents each as written, recommended option first, and records Kris's answer in the digest by tag and letter. Where a blind review disagreed with the worker, the recommendation says so and both views are kept.

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

### DEPS-1 - Bring the website's dependencies inside the age window

**Context:** The website's engineering audit fails its DEPS-1 dependency-age check: `@types/node` 26.6.5, `rumdl` 0.2.79 and Bun 1.4.3 are past the 14-day adoption window. Tonight every documentation unit committed under it as a pre-existing baseline, since no unit may install dependencies. The skills unit proposed a separate update, and a masked blind review on Codex agreed independently: the standard defaults to adoption and no concrete incompatibility has been found.

**Query:** Should a separate maintenance unit bring these dependencies current, after the away window?

**Options:** a) (recommended, confidence high - reviewed: the standard defaults to adoption and no incompatibility is known) A separate maintenance unit, after the window, runs `ki:deps:update`, bumps Bun, re-runs every gate and test and commits the update on its own. b) Record an adoption deferral for these three, with a reason and a review date, and leave the versions as they are.

## Feedback digest shape

When the walk ends, the chat writes exactly this, filling every section and keeping the headings, so Kris can paste it to the coordinating thread. One line per item; tags are the ones used above; a letter is one of the options offered; "none" where a section is empty.

```markdown
# Review digest - knowledgeislands.info documentation - <date> <local time with zone>

## Pages reviewed
- <address> - <one line of Kris's verdict>

## Pages skipped or pending
- <address or section> - pending | skipped | failed to load

## Steer on design choices
- <section or page> - <the question in a few words> - <Kris's answer in his words>

## Changes Kris wants
- <address or section> - <what to change, one line>

## Answers to open queries
- <TAG> - <letter> - <Kris's words if he added any, or none>

## Queries deferred
- <TAG> - <why, or none>

## Notes
- <anything Kris said that fits nowhere above, or none>
```
