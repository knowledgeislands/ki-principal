# Review pack - Knowledge Islands documentation on knowledgeislands.info

This pack is for a Claude or ChatGPT chat. Kris points the chat at this file's address on GitHub and the chat talks him through the published documentation. The pack opens with the prompt for the chat, then the checklist of pages with the questions worth his steer, then every open query of the Ways of working work copied in full, and ends with the exact shape of the feedback digest the chat writes for Kris to paste back.

The merged plan the pages follow is [website-docs.md](website-docs.md). Delivery runs publish the pages one unit at a time in the order [wow-docs-order.md](../briefs/wow-docs-order.md) gives; a page marked **pending** is not yet published and the chat skips it.

## Prompt for the chat

Paste from here to the end of this section into a new chat, or point the chat at this file and ask it to follow the prompt.

> You are reviewing the documentation of Knowledge Islands, a way of keeping knowledge and running work in Git repositories with AI agents, published at <https://knowledgeislands.info>. Your reader is Kris, the owner, who delegated the documentation's design to an automated merge of two proposals and now steers by looking at the published pages. Your job is to walk Kris through the site conversationally, one page or one question at a time, and at the end write a feedback digest in the exact shape given at the end of this pack.
>
> Work from this pack. It has three parts: a checklist of pages with design and use questions, the open queries of the underlying work, and the digest shape. Treat a page marked pending as not yet published: say so and move on. Never comment on code or on how the site is built; comment on whether a reader who uses Knowledge Islands would understand what each thing is, how it works, how they use it and what it provides.
>
> Method: open each page from the checklist in order unless Kris chooses another, read it, give Kris a two-sentence impression, then ask him the page's questions one at a time, offering the recommended answer where the checklist gives one and letting his answer shape the next question. Where you see something the checklist does not ask about and a user would trip over, raise it as a note. Keep each turn short; Kris may answer in a word. When the checklist is done, take the open queries in the same way: present each query's Context, Query and Options in full, with the recommended option first, and record Kris's answer by its tag and letter, or his words if he gives neither. Kris may say "skip", "later" or "digest now" at any time; "digest now" ends the walk and you write the digest with what you have.
>
> Rules: do not invent pages, addresses or facts about the site; if a page fails to load, record that in the digest under Notes. Do not propose redesigns; record Kris's steer. Do not write anything back to GitHub or anywhere else; the digest is a message in the chat for Kris to copy. Use British English and no em-dashes.

## Checklist of pages

Pages are grouped as the site groups them. Each entry gives the address, its status and the questions worth Kris's steer, the recommended answer first where the plan took one. Questions marked **steer** are the ones the merge most wanted his view on.

### Docs landing and navigation

- `https://knowledgeislands.info/docs/` - **pending** until unit 1 publishes. Steer: Atlas now shows Field Guide and Docs, with the Projects catalogue reached from a block at the foot of the Docs landing rather than from the navigation; is the catalogue easy enough to find? Recommended: yes, keep the merge, because the catalogue answers "what is this" and the sections answer "how do I". Does the ten-section grid read as a reading order or as a pile? Do the section names Ways of working, Knowledge and Standards say what is in them?
- `https://knowledgeislands.info/projects/` - published today, unchanged. Does it still need its own place in the navigation once it sits on the Docs landing?

### Skills, `/docs/skills/`

- `https://knowledgeislands.info/docs/skills/what-a-skill-is/` - **pending** until unit 3. Does a reader who has never installed a skill understand what one is and what it will and will not do for them?
- `https://knowledgeislands.info/docs/skills/how-the-skills-fit-together/` - **pending** until unit 3. Steer: eleven diagrams on one page, the skill map and ten area maps; is that the right page for them, or should each area have its own page? Recommended: one page, because the areas are a way of reading the map and not ten separate subjects. Does clicking Interactive and getting a new tab feel right, or should the diagram open in an overlay on the page?
- `https://knowledgeislands.info/docs/skills/catalogue/` - **pending** until unit 3. Steer: the catalogue lists sixty-four skills with one description each and there is no page per skill; is that enough, or do you want a page for every skill? Recommended: no per-skill pages, because the catalogue carries each description without drift and the Ways of working, Knowledge and Standards pages carry the depth.
- `https://knowledgeislands.info/docs/skills/by-outcome/` - **pending** until unit 3. Are the outcomes the ones you would actually look for?

### Ways of working, `/docs/ways-of-working/`

- `https://knowledgeislands.info/docs/ways-of-working/the-work-model/` - **pending** until unit 6. Does the supervisor and worker framing, the seven states and send and receive read as one simple model? Do the two diagrams add to the prose or repeat it?
- `https://knowledgeislands.info/docs/ways-of-working/work-packages/` - **pending** until unit 6. Could you set up a work folder from this page alone?
- `https://knowledgeislands.info/docs/ways-of-working/coordination/` - **pending** until unit 6. Steer: is the owner report, the queries with options and the banner explained at the right depth for someone who receives them rather than writes them?
- `https://knowledgeislands.info/docs/ways-of-working/background-runs/` - **pending** until unit 6. Are grants, the deny list and unattended windows clear enough that you would trust the description?
- `https://knowledgeislands.info/docs/ways-of-working/roadmap-lifecycle/` - **pending** until unit 6. Does the record lifecycle diagram match how you think of a record's journey?
- `https://knowledgeislands.info/docs/ways-of-working/work-design/` - **pending** until unit 7. Is it clear when to shape a design this way rather than just capture work?
- `https://knowledgeislands.info/docs/ways-of-working/trades/` - **pending** until unit 7. The page describes trades as the skills define them today and says nothing about their standing; is that the right thing to publish?
- `https://knowledgeislands.info/docs/ways-of-working/recurring-work/` - **pending** until unit 7. Does it distinguish a recurrence from a scheduled wake clearly?
- `https://knowledgeislands.info/docs/ways-of-working/findings/` - **pending** until unit 8. Steer: an interim practice published with one Interim callout and no mention of what is undecided; is that label enough, or too quiet?
- `https://knowledgeislands.info/docs/ways-of-working/tending/` - **pending** until unit 8. Steer: this is the in-depth page, two tracks and nine levels across two diagrams; is the depth right for a user, or is it an operator's page? Is the fictional island example helpful or distracting?

### Knowledge, `/docs/knowledge/`

- `https://knowledgeislands.info/docs/knowledge/knowledge-bases/` - **pending** until unit 9. Does the zones diagram make the folder model obvious?
- `https://knowledgeislands.info/docs/knowledge/query-save-update/` - **pending** until unit 9. Would a new island owner know what to do in their first session?
- `https://knowledgeislands.info/docs/knowledge/acquiring-knowledge/` - **pending** until unit 9. Is exception-based capture explained so that a reader knows what will and will not be captured?
- `https://knowledgeislands.info/docs/knowledge/recap-and-handover/` - **pending** until unit 9. The page uses the skill's current argument names; does the page read naturally with them?

### Standards, `/docs/standards/`

- `https://knowledgeislands.info/docs/standards/repository-standards/` - **pending** until unit 10. Steer: repository metadata appears as an Interim section inside this page rather than as its own page; right place?
- `https://knowledgeislands.info/docs/standards/decision-records/` - **pending** until unit 10. Is the path from a logged decision to a record clear?
- `https://knowledgeislands.info/docs/standards/engineering-and-git/` - **pending** until unit 10. Is combining engineering and Git on one page a help or a muddle?
- `https://knowledgeislands.info/docs/standards/writing/` - **pending** until unit 10. The only new page without a diagram; does it miss one?
- `https://knowledgeislands.info/docs/standards/diagrams/` - **pending** until unit 10. Steer: the diagrams across the site use the ki day palette on a panel in both the day and night charts; would you rather they switched palette with the chart?

### The ki CLI, `/docs/ki/`

- `https://knowledgeislands.info/docs/ki/command-groups/` - published today; rewritten with the command-groups diagram **pending** until units 2 and 4. Steer: eighteen groups on one page, a paragraph each; is that the right depth for the CLI section, or should the three added pages carry more and this one less?
- `https://knowledgeislands.info/docs/ki/work-and-agents/`, `https://knowledgeislands.info/docs/ki/repositories-and-territory/`, `https://knowledgeislands.info/docs/ki/trades-and-acquisition/` - **pending** until unit 4. Is grouping by what a user is doing better than one page per manual group?
- The nine existing CLI pages - published today, refreshed to v0.13.0 by unit 4. Steer: the site describes the last release only, not what is on main; is that what you expect a user to read?

### KI Agentic Harness, `/docs/ki-agentic-harness/`

- `https://knowledgeislands.info/docs/ki-agentic-harness/how-the-harness-works/` and the five other retained pages - published today, refreshed by unit 5. With the skills pages moved out, does this section still read as a whole?
- `https://knowledgeislands.info/docs/ki-agentic-harness/agent-environment/` - **pending** until unit 5. Is bindings, budgets and housekeeping one subject to a reader, or three?

## Open queries of the Ways of working work

Every open query in [`queries.md`](../queries.md) as of this pack, copied in full with Context, Query and Options. The chat presents each as written, recommended option first, and records Kris's answer in the digest by tag and letter.

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

## Feedback digest shape

When the walk ends, the chat writes exactly this, filling every section and keeping the headings, so Kris can paste it to the coordinating thread. One line per item; tags are the ones used above; a letter is one of the options offered; "none" where a section is empty.

```markdown
# Review digest - knowledgeislands.info documentation - <date> <local time with zone>

## Pages reviewed
- <address> - <one line of Kris's verdict>

## Pages skipped or pending
- <address> - pending | skipped | failed to load

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
