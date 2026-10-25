# Review pack - Knowledge Islands documentation on knowledgeislands.info

This pack is for a Claude or ChatGPT chat. Kris points the chat at this file's address on GitHub and the chat talks him through the published documentation. The pack opens with the prompt for the chat, then the review list of the pages and diagrams now published with one line each on what is worth his judgement, then every open query of the Ways of working work copied in full and grouped by subject, and ends with the exact shape of the feedback digest the chat writes for Kris to paste back.

The merged plan the pages follow is [website-docs.md](website-docs.md). Delivery runs published the pages one unit at a time in the order [wow-docs-order.md](../briefs/wow-docs-order.md) gives. As of 06:06 GMT on 25 October 2026 all ten units are on the website's `main`: the section structure, the diagram pipeline, Skills, the ki CLI, the harness section, the ten Ways of working pages, Knowledge and Standards, 64 pages across ten sections with 38 diagrams. Nothing is pending.

**Live site checked.** The deployment failed between 04:22 GMT and the fix at 06:22 GMT, so an earlier version of this pack listed addresses that answered 404. At 06:37 GMT every one of the 80 addresses this pack lists answered 200 to `curl -sIL`, each `.html` diagram address redirecting to its suffix-less form as Cloudflare does by design, and roadmap-lifecycle shows the rewrite. The fix changed only the build's receipt check, nothing a reader sees. The chat still opens each address; where one fails on the day, it records that in the digest under Pages skipped or pending as failed to load and moves on.

## Prompt for the chat

Paste from here to the end of this section into a new chat, or point the chat at this file and ask it to follow the prompt.

> You are reviewing the documentation of Knowledge Islands, a way of keeping knowledge and running work in Git repositories with AI agents, published at <https://knowledgeislands.info>. Your reader is Kris, the owner, who delegated the documentation's design to an automated merge of two proposals and now steers by looking at the published pages. Your job is to walk Kris through the site conversationally, one page or one question at a time, and at the end write a feedback digest in the exact shape given at the end of this pack.
>
> Work from the pack. It has three parts: the review list of pages and diagrams with one line each on what to judge, the open queries of the underlying work grouped by subject, and the digest shape. Every page is published and every address answered when the pack was written. Open each address; if one fails to load, say so, record it under Pages skipped or pending as failed to load, and move on. Never comment on code or on how the site is built; comment on whether a reader who uses Knowledge Islands would understand what each thing is, how it works, how to use it and what it provides.
>
> Method: open the page the review list gives in order unless Kris chooses another, read it, give Kris a two-sentence impression, then ask him the page's question, offering the recommended answer where the list gives one and letting his answer shape the next question. Open each diagram's interactive view when you reach it and ask its question the same way. Where you see something the list does not ask about and a user would trip over, raise it as a note. Keep each turn short; Kris may answer in a word. When the review list is done, take the open queries in the same way: present each query's Context, Query and Options in full, recommended option first, and record Kris's answer by tag and letter, or the words he gives if neither. Kris may say "skip", "later" or "digest now" at any time; "digest now" ends the walk and you write the digest from what you have.
>
> Rules: do not invent pages, addresses or facts about the site; if a page fails to load, record that in the digest. Do not propose redesigns; record Kris's steer. Do not write anything back to GitHub or anywhere else; the digest is a message in the chat for Kris to copy. Use British English and no em-dashes.

## Website review list

Pages and diagrams grouped as the site groups them. Each entry gives the address and one line on what Kris should judge there: design and use, never code. Where the merge took a choice he most wanted a view on, the line is marked **steer** and gives the recommended answer. A diagram's address opens its interactive view in the browser; the same diagram sits inline on the page named beside it.

### Docs landing and navigation

- <https://knowledgeislands.info/docs/> - **steer**: Atlas now shows Field Guide and Docs; the grid shows all ten sections in reading order, Skills first, then Ways of working, Knowledge and Standards before the CLI and the harness; the Projects catalogue sits in a block at the foot of the page instead of in the navigation. Is the catalogue easy enough to find, and does the grid read as a reading order? Recommended: keep the merge, because the catalogue answers "what is this" and the sections answer "how do I".
- <https://knowledgeislands.info/projects/> - unchanged, reached from the Docs landing block; does it still need its own place in the navigation now that it sits on the Docs landing?
- Every page in Skills, Ways of working, Knowledge and Standards ends with a "Provided by" box naming the skills and commands behind it, and a provenance footer naming the sources it restates. Judge once, on any page: does the box help a reader find the skill, or does it read as internal plumbing?

### Skills, `/docs/skills/`

- <https://knowledgeislands.info/docs/skills/what-a-skill-is/> - does a reader who has never installed a skill understand what one is and what it will and will not do for them?
- <https://knowledgeislands.info/docs/skills/how-the-skills-fit-together/> - **steer**: eleven diagrams on one page, the skill map and ten area maps; is one page right for them, or should each area have its own page? Recommended: one page, because the areas are a way of reading the map and not ten separate subjects.
- <https://knowledgeislands.info/docs/skills/catalogue/> - **steer**: sixty-four skills with one description each, grouped by where each is kept, with a finder table giving each skill's functional area, and no page per skill; is that enough, or do you want a page for every skill? Recommended: no per-skill pages, because the catalogue carries each description without drift and the explanatory sections carry the depth. The AREA-COLUMN query below asks where the finder's areas should come from.
- <https://knowledgeislands.info/docs/skills/by-outcome/> - every outcome now links the skill to reach for and the page that explains the practice; are the outcomes ones you would actually look for, and is skill plus page per row the right amount?

Diagrams on the fit-together page, vendored from the harness:

- <https://knowledgeislands.info/diagrams/vendored/ki-agentic-harness/skill-map.html> - the skill map on how-the-skills-fit-together; can you find a skill you know and tell its shape and area, and is opening the interactive view in a new tab acceptable for now, with an overlay as later work?
- <https://knowledgeislands.info/diagrams/vendored/ki-agentic-harness/skill-area-fundamentals.html> - the Fundamentals area map; does the caption's "look for" reading make the diagram useful to someone who is not a harness developer?
- <https://knowledgeislands.info/diagrams/vendored/ki-agentic-harness/skill-area-records-and-code.html> - the Records and code area map; do the edges arriving from outside the area read as reliance rather than clutter?
- <https://knowledgeislands.info/diagrams/vendored/ki-agentic-harness/skill-area-coordination.html> - the Coordination area map, the busiest of the ten; is it still legible inline, or only in the interactive view?
- <https://knowledgeislands.info/diagrams/vendored/ki-agentic-harness/skill-area-work-and-delivery.html> - the Work and delivery area map; does it show the lifecycle skills as a set you reach for together?
- <https://knowledgeislands.info/diagrams/vendored/ki-agentic-harness/skill-area-repository-types.html> - the Repository types area map; does one shape per repository kind help a reader choose the right skill?
- <https://knowledgeislands.info/diagrams/vendored/ki-agentic-harness/skill-area-agentic-systems.html> - the Agentic systems area map; is the Paperclip skill standing apart confusing or honest?
- <https://knowledgeislands.info/diagrams/vendored/ki-agentic-harness/skill-area-environment.html> - the Environment area map; do the two portable roots and their adapters read as one idea?
- <https://knowledgeislands.info/diagrams/vendored/ki-agentic-harness/skill-area-acquire.html> - the Acquire area map, three nodes; is a diagram this small worth the space on the page?
- <https://knowledgeislands.info/diagrams/vendored/ki-agentic-harness/skill-area-signals.html> - the Signals area map, three nodes and no edges; same question, is it worth the space?
- <https://knowledgeislands.info/diagrams/vendored/ki-agentic-harness/skill-area-design.html> - the Design area map, two nodes; same question, and should the smallest areas share one figure?

### Ways of working, `/docs/ways-of-working/`

- <https://knowledgeislands.info/docs/ways-of-working/the-work-model/> - the first page of the section; does "the unit is work, not the chat session" land for a reader who has only ever used a chat, and do the seven states read as something you could tell from the files alone?
- <https://knowledgeislands.info/diagrams/site/work-model.html> - the work-model diagram on that page; do supervisor, worker, the work and its package read as one picture, with the two moves between them?
- <https://knowledgeislands.info/diagrams/site/seven-states.html> - the seven-states diagram on the same page; can you tell from it which states are with someone, which are handed off, and which two are set rather than derived?
- <https://knowledgeislands.info/docs/ways-of-working/work-packages/> - the work folder and its five files, with design notes, briefs, reports and findings beside them; could you pick a piece of work up from this page and Git alone?
- <https://knowledgeislands.info/diagrams/site/work-folder.html> - the work-folder diagram on that page; is the line between the five files and what sits beside them for a while clear?
- <https://knowledgeislands.info/docs/ways-of-working/coordination/> - **steer**: the coordinating session, its turn budget, the owner report with Done, In Progress and Queries, the banner and the three reply forms; is the owner report explained so that a reader knows what to expect in a reply, or does it read as internal procedure? Recommended: keep the full shape, because the report is what the reader actually receives.
- <https://knowledgeislands.info/diagrams/vendored/ki-agentic-harness/thread-model.html> - the harness's thread-model diagram on the coordination page; do a State of play thread and a Project thread, each with its runs and returns, read as one picture?
- <https://knowledgeislands.info/diagrams/site/coordinating-turn.html> - the coordinating-turn diagram on the same page; does one turn, from the owner's message through launch, wake and receive to the report, read as a sequence you could follow in a real session?
- <https://knowledgeislands.info/docs/ways-of-working/background-runs/> - detached runs, the brief, the status and report files, authority tiers, grants and the deny list; can a reader tell what they may hand off unattended and what they may not?
- <https://knowledgeislands.info/diagrams/site/background-run.html> - the background-run diagram on that page; does the run's life from brief to pruned report show where the owner is and is not needed?
- <https://knowledgeislands.info/docs/ways-of-working/roadmap-lifecycle/> - rewritten around the seven statuses and the four lifecycle skills from the user's view, at the address the former planning-and-delivery page moved to; does it now sit naturally under Ways of working, and is one page enough for adapters, horizons, holds and batches?
- <https://knowledgeislands.info/diagrams/site/record-lifecycle.html> - the record-lifecycle diagram on that page; do hold and cancelled sitting beside the main path, and pruning as a last step, read correctly?
- <https://knowledgeislands.info/docs/ways-of-working/work-design/> - brief, independent reviews, merged report, owner decisions and a pilot; is it clear when to reach for this rather than a roadmap record?
- <https://knowledgeislands.info/diagrams/site/work-design-loop.html> - the work-design-loop diagram on that page; does it show that the owner decides between the report and the pilot, not before the reviews?
- <https://knowledgeislands.info/docs/ways-of-working/trades/> - a trade between two repositories with ownership never transferred; does keeping submission, receipt and the receiver's decision separate read as a safeguard or as ceremony?
- <https://knowledgeislands.info/diagrams/site/trade.html> - the trade diagram on that page; can you tell which side acts at each step and that the receiver decides locally?
- <https://knowledgeislands.info/docs/ways-of-working/recurring-work/> - one repository-owned definition, one ordinary record per run and reviewed evidence; does it convince you that recurring work needs no second backlog?
- <https://knowledgeislands.info/diagrams/site/recurring-occurrence.html> - the recurring-occurrence diagram on that page; does the loop from schedule through delivery and evidence to review read as one recurrence?
- <https://knowledgeislands.info/docs/ways-of-working/findings/> - **steer**: interim, labelled so in a callout under the opening claim; is the interim callout the right way to show a practice in use whose standard home is not yet chosen, or should interim practices stay off the site until settled? Recommended: keep the callout, so the site says what is in use without claiming it is settled.
- <https://knowledgeislands.info/diagrams/site/finding-life.html> - the finding-life diagram on that page; does a finding opened, carried in full, settled and homed or dropped read as a life a reader can follow?
- <https://knowledgeislands.info/docs/ways-of-working/tending/> - **steer**: interim, in depth: the two tracks, four structural and five PMO levels, the focus rule, write boundaries and the lightweight report, all on one page; is that depth right for an interim practice, or should it be shorter until it has a home? Recommended: keep the depth, because this page is the one place the whole practice is written for a reader.
- <https://knowledgeislands.info/diagrams/site/tending-tracks.html> - the tending-tracks diagram on that page; do the structural and PMO tracks, their levels and upward capture read as two ladders or as a wall of boxes?
- <https://knowledgeislands.info/diagrams/site/tending-pass.html> - the tending-pass diagram on the same page; does one pass from focus to report show who runs what, and where every item gets its disposition?

### Knowledge, `/docs/knowledge/`

- <https://knowledgeislands.info/docs/knowledge/knowledge-bases/> - the zones, index notes, the Capital and its principal overlay, live artifacts; does a reader new to islands see why five zones and two working areas rather than one folder of notes?
- <https://knowledgeislands.info/diagrams/site/kb-zones.html> - the kb-zones diagram on that page; do the five indexed zones, the directional areas beside them and the Capital's overlay read at a glance?
- <https://knowledgeislands.info/docs/knowledge/query-save-update/> - the working loop in a session: query, save, update, link, digest; is the confirmation and canonical-change approval step clear as a boundary a reader will meet?
- <https://knowledgeislands.info/diagrams/site/query-save-update.html> - the query-save-update diagram on that page; does the loop show where the island's approval sits, and that the session digest is what leaves?
- <https://knowledgeislands.info/docs/knowledge/acquiring-knowledge/> - selected capture from agent sessions, ChatGPT, Granola and pulses; does "exception-based", only chosen things captured and the island deciding what to keep, come across?
- <https://knowledgeislands.info/diagrams/site/acquisition-flow.html> - the acquisition-flow diagram on that page; do the sources, the capture packages and the island's adoption read as a flow with a gate, and does the pulse route read as separate on purpose?
- <https://knowledgeislands.info/docs/knowledge/recap-and-handover/> - recapping a live session and routing durable learning; is it clear what a recap produces and who reads it next?
- <https://knowledgeislands.info/diagrams/site/recap-handover.html> - the recap-handover diagram on that page; do the routes for changes, decisions and learning read as different destinations?

### Standards, `/docs/standards/`

- <https://knowledgeislands.info/docs/standards/repository-standards/> - **steer**: the universal contract, shapes, the audit and conform loop and the `+` and `-` areas, with an Interim section on repository metadata as it works now; is one page right for the repository standards, and does the interim metadata section belong here or on its own page? Recommended: one page with the interim section, because the metadata practice is part of what a repository declares. The REPO-STANDARDS-SET query below asks which skills this page's "Provided by" box lists.
- <https://knowledgeislands.info/diagrams/site/repository-shapes.html> - the repository-shapes diagram on that page; does one contract, one primary shape and supporting standards that add capabilities without changing identity read clearly?
- <https://knowledgeislands.info/diagrams/site/audit-conform.html> - the audit-conform diagram on the same page; do educate, audit, conform and re-audit read as a loop a reader would run, not a checklist?
- <https://knowledgeislands.info/docs/standards/decision-records/> - typed records and when a decision warrants one; can a reader tell a decision in a log from a decision record, and see how one becomes the other?
- <https://knowledgeislands.info/diagrams/site/decision-to-record.html> - the decision-to-record diagram on that page; does the path from a logged owner decision to a typed record show when a record is amended instead of created?
- <https://knowledgeislands.info/docs/standards/engineering-and-git/> - TypeScript and Bun engineering, Conventional Commits, explicit staging and shared-tree safety on one page; do code standards and commit standards belong together for a user?
- <https://knowledgeislands.info/diagrams/site/standards-layers.html> - the standards-layers diagram on that page; do the universal contract, the shape and capability standards and the repository's own choices read as layers that each own a distinct part?
- <https://knowledgeislands.info/docs/standards/writing/> - Markdown, TOML, READMEs, guides and specifications, with no diagram; does the page help a reader choose where a piece of writing belongs, not only how to format it?
- <https://knowledgeislands.info/docs/standards/diagrams/> - Archify, the five diagram types, committed forms, the manifest, embedding, privacy and regeneration; is this a standard a user needs, or a maintainer's page?
- <https://knowledgeislands.info/diagrams/site/diagram-regeneration.html> - the diagram-regeneration diagram on that page; does source, build, export, receipt and freshness check read as the one loop that keeps a diagram true?

### The ki CLI, `/docs/ki/`

- <https://knowledgeislands.info/docs/ki/command-groups/> - **steer**: rewritten around the eighteen manual groups, a paragraph each, with the command-groups diagram; is that the right depth for the CLI section, or should the three added pages carry more and this one less?
- <https://knowledgeislands.info/diagrams/site/command-groups.html> - the command-groups diagram on that page; do the eighteen groups labelled by what each operates on help you pick a group faster than the page's prose?
- <https://knowledgeislands.info/docs/ki/work-and-agents/> - new; does grouping the work model, background agents and batch commands by what a user is doing beat one page per manual group? It now links to the Ways of working pages for the practice behind each command.
- <https://knowledgeislands.info/docs/ki/repositories-and-territory/> - new; six manual groups on one page; can you tell registry, repository and territory commands apart as you read?
- <https://knowledgeislands.info/docs/ki/trades-and-acquisition/> - new; does putting trades, acquisition and knowledge-base search together make sense to a user, or is it a leftovers page?
- <https://knowledgeislands.info/docs/ki/getting-started/>, <https://knowledgeislands.info/docs/ki/commands/>, <https://knowledgeislands.info/docs/ki/local-commands/>, <https://knowledgeislands.info/docs/ki/naming-and-locations/>, <https://knowledgeislands.info/docs/ki/operator-guides/>, <https://knowledgeislands.info/docs/ki/capability-lifecycle/>, <https://knowledgeislands.info/docs/ki/update-upgrade/> and <https://knowledgeislands.info/docs/ki/chatgpt-local-capture/> - refreshed to v0.13.0. **Steer**: the site describes the last release only, not what is on main; is that what you expect a user to read? Recommended: yes, the last reviewed release.

### KI Agentic Harness, `/docs/ki-agentic-harness/`

- <https://knowledgeislands.info/docs/ki-agentic-harness/how-the-harness-works/>, <https://knowledgeislands.info/docs/ki-agentic-harness/installing-a-harness/>, <https://knowledgeislands.info/docs/ki-agentic-harness/onboarding/>, <https://knowledgeislands.info/docs/ki-agentic-harness/repositories/>, <https://knowledgeislands.info/docs/ki-agentic-harness/using-skills/> and <https://knowledgeislands.info/docs/ki-agentic-harness/tuning/> - refreshed; with the skills pages and planning-and-delivery moved out, does this section still read as a whole about running a harness? The repositories page now points to the Standards pages for what it no longer explains itself.
- <https://knowledgeislands.info/docs/ki-agentic-harness/agent-environment/> - new; is bindings, budgets and housekeeping one subject to a reader, or three?
- <https://knowledgeislands.info/diagrams/site/agent-environment.html> - the agent-environment diagram on that page; does inventory above and budgets below make the split between configuration and runtime health obvious?

## Open queries of the Ways of working work

Every open query in [`queries.md`](../queries.md) as of this pack, 33 in all, copied in full and verbatim with Context, Query and Options. They are grouped so that related queries are met together; within a group the chat takes them in the order given. The chat presents each as written, recommended option first, and records Kris's answer in the digest by tag and letter. Where a blind review disagreed with the worker, the recommendation says so and both views are kept.

**The website.** These four arise from the pages just reviewed, so they come first while the pages are fresh.

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

### DEPS-1 - Bring the website's dependencies inside the age window

**Context:** The website's engineering audit fails its DEPS-1 dependency-age check: `@types/node` 26.6.5, `rumdl` 0.2.79 and Bun 1.4.3 are past the 14-day adoption window. Tonight every documentation unit committed under it as a pre-existing baseline, since no unit may install dependencies. The skills unit proposed a separate update, and a masked blind review on Codex agreed independently: the standard defaults to adoption and no concrete incompatibility has been found.

**Query:** Should a separate maintenance unit bring these dependencies current, after the away window?

**Options:** a) (recommended, confidence high - reviewed: the standard defaults to adoption and no incompatibility is known) A separate maintenance unit, after the window, runs `ki:deps:update`, bumps Bun, re-runs every gate and test and commits the update on its own. b) Record an adoption deferral for these three, with a reason and a review date, and leave the versions as they are.

### CI-PIN - Bring the website's CI onto a ki that knows the diagrams skill

**Context:** The website's GitHub Actions CI has been red on every commit since the diagram pipeline landed at 04:22 GMT on 25 October, failing at its `ki repo repair` step: the workflow pins `ki` v0.8.4, whose harness lacks the `ki-diagrams` skill the repository's `.ki.toml` now declares. The live site is unaffected, since Cloudflare builds and deploys on its own and succeeds again since fix `904176e`. The website's AGENTS.md treats this as checker drift owed to a `tools-ki` pin bump. Moving the pin changes CI configuration, which the away window excluded.

**Query:** Should a bounded run move the website's CI `ki` pin to the current `tools-ki` release so CI goes green?

**Options:** a) (recommended, confidence high - the declared skill exists only in newer harnesses, the website's own guidance names a pin bump as the cure, and it is a one-line, reversible change) A bounded run moves the pin to the current `tools-ki` release, confirms CI passes on the next push and commits it on its own. b) Leave CI red until the next scheduled `tools-ki` pin review.

**The model of work and its packages.** How a State of play looks after Project packages, the one-thread rollout, how work is named and sized, and one argument name in ki-recap.

### STEWARD-FIELD - where a package records who looks after it

**Context:** The assignment needs a committed home that names a work, never a host or session. The brief proposed a new `state.md` field, `steward: self` or `steward: work/<sop id>`. Both reviews reject `self`, which is not a holder value, and both reject reading the assignment as the holder. The Claude review would reuse `work.md`'s existing `worker` field: `worker: work/va` when the State of play looks after the package, and `agent` when the Project's own thread does. That adds no field and leaves the closed field set unchanged. Stewardship changes only when Kris opens or closes a thread, the slow rate `work.md` suits, and the holder stays derived from `state` and `worker` as today. The Codex review wants a dedicated assignment with its own vocabulary, distinct from holder and session, and leaves the exact field to the design. A separate field keeps the assignment visible beside the state, and it avoids a third sense of "steward" only if it is named with care.

**Query:** Should the assignment be recorded in a new dedicated field rather than `work.md`'s existing `worker` field?

**Options:**

a) (recommended, confidence medium - reviews disagree; the Codex review and a masked blind review on Codex want a dedicated field, as lasting responsibility should not share a field with the holder that pick-up reads, while the Claude review prefers reusing `worker` as it adds no field) A new dedicated field, taking `work/<id>` values only, never `self`, changed or removed as part of the acknowledged handover.

b) Reuse `work.md`'s `worker`: `worker: work/<sop id>` while the State of play looks after the package, `agent` while its own thread does.

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

### WORK-LABEL - name every piece of work as label then id

**Context:** Decided in substance. Kris, 25 October, on "Personal > Tower (personal.regular.tower)": "I like this label, the way that you put the work package in brackets after it at the end. Can we adopt that as a standard?" Today `ki-coordination`'s Work naming gives each work an id, slug and title, the label being the title plus a host suffix only where the work is limited to one machine, and the `<label> (<id>)` form appears only in the coordinator's closing thread line; the message sender label is `<Territory> > SoP:` with no id; regular and ad hoc work carry no thread line, so a regular thread had no settled way to name itself. The change: `ki-coordination` names `<label> (<id>)` as the work name used wherever a session names a piece of work, in replies, reports, message sender labels, hand-offs and openers, and the `ki-work-package` message line form gains the id after the sender label.

**Query:** Should it land now, and in which run?

**Options:**

a) (recommended, confidence high - decided, two short edits in the harness, and SIZE-LABEL shares the run) Land it on return in the one harness run with SIZE-LABEL, with a REFRESH line to live works afterwards.

b) Land it on return as a run of its own.

c) Land only the `ki-coordination` naming rule now and leave the message line form as it is.

### SIZE-LABEL - land the T-shirt display convention now

**Context:** Decided in substance. Kris, 24 October 08:42 BST: "I wonder if there's a way of showing T-shirt S, M, etc. next to it. And probably put it in a capital letter, almost like it's a label on a t-shirt." Under VA-HIGH a) on 25 October he sent it here as a message, read back as "TENDING-FOLD, SIZE-LABEL and PRODUCT-RECORDS go to their owning works tonight as messages". Today `ki-work-roadmap`'s Priority and size section defines `size` as `s`, `m`, `l` or `xl`, with `xl` split before Ready and no `xs`, and says nothing about display; Valle Armonia already shows 👕 S, 👕 M, 👕 L and 👕 XL in reports and messages, and one record was labelled 👕 XS against the vocabulary. The change is one paragraph: a display convention of 👕 plus the capital letter in reports and messages, field values unchanged, no XS. The deny list keeps standard changes out of tonight's window.

**Query:** Should it land now, and in which run?

**Options:**

a) (recommended, confidence high - decided, one paragraph, and WORK-LABEL is the same kind of change in the same repository) Land it on return in one harness run together with WORK-LABEL, the run's tests covering both.

b) Land it on return as a run of its own.

c) Hold it for the next harness batch.

### RECAP-NAME - What ki-recap's checkpoint argument is called

**Context:** `ki-recap` offers `checkpoint <thread>`, which composes `ki-work-package` UPDATE. "Thread" now means a session acting on work, and the argument is really a work id. The three recap forms (one session, one work since its mark, the unattended window's return) otherwise have clean scopes.

**Query:** Should the argument become `checkpoint <work id>`?

**Options:**

a) (recommended, confidence high - the model made work the unit and the argument already resolves an id) rename it to `checkpoint <work id>`, accepting the old word through the tolerance window

b) keep `checkpoint <thread>` and define it in the Glossary as the work the thread carries

**Unattended windows and wakes.** What makes a record eligible for unattended work, where that verdict is recorded, and whether the launchd wake is next.

### UNATTENDED-AND-DUE-DATES - adopt the eight criteria as the unattended assessment

**Context:** Kris, 24 October, through Personal's State of play: "we need to push that into the ways of working thread as something that we need to do an assessment of", and roadmap records should carry an explicit due date or key milestone date "of what they're working towards". The due-date half is done: DUE-FIELD was decided at 01:43 GMT today and harness `1af72f2e` added the optional `target` mapping (`date`, `kind` of `due` or `milestone`, `what`) to the `ki-work-roadmap` format standard, with the nearer date ordering work within one horizon and priority. The assessment half is not. Personal's prototype tests each record against eight ordered criteria, `no-owner-judgement`, `no-outward-act`, `one-repo-authority`, `reversible`, `self-verifiable`, `unblocked`, `scoped` and `agent-step`, the first failure deciding `unattended`, `near-miss` with one question, or `attended`; across 76 open Personal records it found 9, 21 and 46. Each criterion cites an existing rule rather than restating one, and eligibility is not authority. The open query UNATTENDED-FIELD asks only where a verdict is recorded (a record mapping or a per-window note) and bundles the criteria into that choice; the Codex blind review that kept it at medium asked for the criteria to be reviewed before they are standardised. Today `ki-delegation`'s unattended deny list says what a window never does and `ki-coordination`'s unattended windows section says what a coordinator may progress, but neither says how a record is judged eligible, and the format standard states "No unattended-eligibility field is adopted".

**Query:** Should the eight criteria, in their order with the three outcomes, become the eligibility assessment in `ki-delegation`, leaving UNATTENDED-FIELD to decide only where the verdict is recorded?

**Options:**

a) (recommended, confidence medium - the criteria sorted 76 real records cleanly and rest on rules already in the standards, but they have run on one territory and one review asked for scrutiny before standardising; reviewed, views differ: a masked Codex review prefers b), piloting on a second territory first, since one territory cannot show whether near-misses really need only one owner answer or whether reviewers classify alike) Adopt them into `ki-delegation` beside the unattended deny list as the assessment every window plan uses, with a harness run writing them and the field question staying with UNATTENDED-FIELD.

b) Pilot them on one more territory's roadmap in a design note first, then adopt with the lessons.

c) Keep them as Personal's local prototype and let each territory judge eligibility in its window plan.

### UNATTENDED-FIELD - recording unattended eligibility on records

**Context:** Personal's prototype assessed 76 records against eight ordered criteria, 9 eligible, 21 near-miss and 46 attended, and proposed a record field. The brief proposes an optional `unattended` mapping in `ki-work-roadmap` with `verdict` (`eligible`, `near-miss`, `attended`), `criterion`, `question` and `assessed`, an absent mapping read as attended, and the criteria owned by `ki-delegation`.

**Query:** Should records carry this optional `unattended` mapping, with the eight criteria in `ki-delegation`?

**Options:**

a) (recommended, confidence medium - reviews disagree; a masked blind review on Codex would keep the assessment in a per-window note with no record field, as eligibility depends on the grant and can go stale, and review the eight criteria before standardising them, while Personal's assessment shows the criteria sort real records, and a field spares rereading every record at each window) Adopt the mapping and the criteria, refreshed at each status or horizon change.

b) Keep the assessment in a per-window note, with no record field.

### WAKE-SUBSTRATE - whether the outage evidence lifts the launchd deferral

**Context:** Moved from hnr's parked queries on 24 October by Kris's "Move all three to Ways of Working". On 23 October at 02:37 BST, under Kris's grant to act where confidence is high, the coordinator took WAKE-SUBSTRATE a) as reviewed to high: pursue the completion watcher first, label session wakes best effort, defer launchd, doorbells and liveness fields. The watcher has since shipped as `ki agent wait --next` in tools-ki and the standard's Monitoring section. HNR's debrief reports the two 22 October outages: between 03:21 and 05:00 BST every wake hit the plan's session usage limit, and between 06:25 and 07:30 BST the coordinator sat inside one turn waiting on two `rm -rf` permission prompts; it names idle-only firing the main hazard, since a blocked turn silences every wake and notification, and recommends one Rig launchd job on `StartCalendarInterval` running a shell-only check (has `messages.md` changed, has a run finished, has a deadline passed) that spends model time only when something is new, built by Rig and chezmoi once Kris chooses it, with Ways of working writing the contract for a headless coordinator pass. HNR has stopped its own wakes and deploys sites only on request until a durable wake exists. Claude Code's schedules remain session-only and fire only when the session is idle.

**Query:** Should the launchd shell-check wake now become the next unit after the completion watcher, or stay deferred?

**Options:**

a) (recommended, confidence high - reviewed: a masked Codex review agrees, with the contract settling authority, model budget, overlapping passes and unavailable capacity before any job is installed; neither outage is cured by launchd, one being a usage limit and the other a blocked turn, yet it is the only wake that survives a quit and HNR's deploys wait on it) Lift the deferral in order: Ways of working writes the headless-pass contract (what a pass may do, its budget, its report) into `ki-coordination`, then sends the launchd job as a line to ki.chezmoi and ki.mac-studio-setup.

b) Keep the 23 October order: session-only wakes with stop words, revisit after the usage-limit and blocked-turn causes are addressed.

c) Build the launchd job first and write the contract from what it needs.

**Standing rules for agents.** Four rules the HNR coordinator has applied unwritten, each to be confirmed one by one and given a home.

### UNWRITTEN-RULES-CLOUDFLARE - no DNS, Access, route, Builds or Zero Trust change without Kris's go

**Context:** The HNR coordinator has applied this rule unwritten, and on 24 October Kris asked for each of the four rules to be confirmed one by one and the confirmed wording written into its home. On 23 October the coordinator, acting under a grant, took the view that none of the four inferred rules becomes a standing instruction; HNR keeps applying them meanwhile. Today `ki-delegation`'s unattended deny list bars "DNS, Cloudflare, GitHub settings, machine, scheduler, credential or connection-critical changes" during an unattended window only, the connection-critical rule requires a tested restore path for any run touching such a service, and the Cloudflare half of RUN-SECRETS restricts credential reads; nothing states the rule for an attended coordinator turn.

**Query:** Should this be a standing rule at every time, not only in an unattended window?

**Options:**

a) (recommended, confidence high - it matches the deny list, the connection-critical rule and Kris's practice, and the change is one sentence) Confirm it as standing: no DNS, Cloudflare Access, route, Builds or Zero Trust change without Kris's go in the thread, written into `ki-delegation`'s authority tiers beside the connection-critical rule.

b) Keep it window-only as the deny list has it, trusting attended turns to ask.

c) Not a rule: the connection-critical restore path is enough.

### UNWRITTEN-RULES-CONFIG - no mcporter or chezmoi configuration change without approval

**Context:** The second HNR rule. Today `ki-delegation`'s machine grant lifts "only the ban on an environment or scheduler change: the local changes the task names, on this machine, each with its undo", the deny list bars machine and configuration changes in a window, and Kris's own user instructions require a `chezmoi diff` review and the repository's approval before a source-store binding is applied. Neither standard names mcporter or chezmoi.

**Query:** Should the rule be confirmed as standing, with mcporter and chezmoi named as the managed configuration it covers?

**Options:**

a) (recommended, confidence high - the machine grant already requires each change to be named with its undo, so this only names the two surfaces) Confirm it: no mcporter or chezmoi configuration change without Kris's approval, written into `ki-delegation`'s machine grant as the named example, with `ki-binding` pointing to it.

b) Confirm it for HNR only, in hnr-principal's AGENTS.md.

c) Not a rule: the machine grant covers it unnamed.

### UNWRITTEN-RULES-DRAFTS - drafts only in Linear, Notion and Slack

**Context:** The third HNR rule: an agent creates drafts in Linear, Notion and Slack and never sends, publishes or changes state others see. Today the deny list bars "messages to people or new publication" in an unattended window, and the authority tiers say no footer authorises "publication outside the cited task"; neither names these three platforms or covers an attended turn. The MCP tools for all three can write directly.

**Query:** Should the rule be confirmed as standing for every session, and where should it live?

**Options:**

a) (recommended, confidence medium - it generalises the deny list's publication ban to attended turns, but the three platforms and the line between a draft and a change others see want Kris's wording; reviewed, views differ: a masked Codex review prefers b), HNR only, since HNR is the evidenced scope and an owner-wide platform restriction wants its own decision) Confirm it: in Linear, Notion and Slack an agent drafts and Kris sends, publishes or moves state, written into `ki-delegation`'s authority tiers beside the publication ban.

b) Confirm it for HNR only, in hnr-principal's AGENTS.md.

c) Not a rule: the publication ban is enough.

### UNWRITTEN-RULES-CONFIDENTIAL - a confidential site is never made public

**Context:** The fourth HNR rule. Today no standard says it: the deny list bars "new publication" in a window and the privacy rules in `ki-diagrams` and the work-package standard bar private names in committed files, but nothing bars changing a confidential site's visibility, which cannot be undone once crawled.

**Query:** Should the rule be confirmed as standing, in general form?

**Options:**

a) (recommended, confidence high - an irreversible disclosure with no reading under which it should happen unasked) Confirm it in general form: a site, repository or note marked confidential is never made public without Kris's go, written into `ki-delegation`'s authority tiers, with HNR's list of confidential sites in hnr-principal's AGENTS.md.

b) Confirm it for HNR's sites only, in hnr-principal's AGENTS.md.

c) Not a rule.

**Permission prompts.** One scan, three queries: the cause, the call shapes that prompt, and whether the permission settings change.

### PERM-PROMPTS-SCRATCH - stop runs clearing their own temp directory

**Context:** Kris, 25 October: "Every now and then we get a prompt for permissions ... when you find out what it is, can you pass that to Ways of Working". Legal's read-only scan of 44 interactive and the background-run transcripts since 14 October found configuration is not the cause: every session runs in bypass mode and the only prompt bypass leaves is Claude Code's built-in `rm` safety check. It is call-shape driven: 203 background-run denials, 110 with a target under a workspace directory, which a run's temp directory is because the launcher adds it as a working directory, 91 with a shell-variable target, plus 34 compound commands denied for containing such an `rm` or a `git worktree remove`. Runs cannot ask, so they adapt; the same shape in an interactive session becomes a prompt for Kris, which approved prompts leave no trace of, so the interactive cause is probable, not proven. The standard sends runs to the cause: `ki-delegation`'s run packet says temporary output goes in `$TMPDIR/ki-agents/<run>/<name>/` and "`ki agent close` refuses while the directory holds anything", yet the same section records Kris's 20 October adoption of the directory "which `ki agent close` empties and removes". The two sentences disagree, and the first makes every run `rm` its scratch.

**Query:** Should runs leave their temp directory for `ki agent close` to empty and remove, the refusal sentence going?

**Options:**

a) (recommended, confidence high - 203 denials trace to runs clearing scratch the launcher already owns, and the standard already states the close behaviour in Kris's adopted words) Yes: `ki-delegation` says a run never removes its temp directory and `ki agent close` empties and removes it; a line to ki.tools-burndown confirms close does so.

b) Keep the refusal and add a `ki agent clean` a run calls instead of `rm`.

c) Leave the standard; have runs remove scratch file by file with literal paths.

### PERM-PROMPTS-SHAPES - name the call shapes that prompt

**Context:** The same scan. The shapes that trip the check are an `rm` with a glob, a shell-variable or a workspace-directory target, alone or inside a compound command, a `git worktree remove`, and a `sleep` of 60 seconds or more before a command, which the harness blocks; Kris's own user instructions already describe the `rm` case. Today neither `ki-coordination` nor `ki-delegation` names them; the coordinator style says only to use a bounded run or `ki agent close` for deletion. Not prompts, and needing nothing: Kris's own interruptions, commit hook time and a missing tool in runs. Legal's run also asked Kris to note the wording of the next prompt he sees so the interactive cause can be confirmed.

**Query:** Should both standards name these shapes and the alternatives, with a note on the interactive cause?

**Options:**

a) (recommended, confidence high - the shapes are observed in 237 denials and the alternatives already exist) Yes: `ki-coordination` and `ki-delegation` each list the shapes, coordinators use `ki agent close` or a bounded run for removal and runs use literal paths, and the note says the interactive cause is probable until Kris reports a prompt's wording.

b) Name them in `ki-delegation` only, for runs.

c) Do not: fix the cause under PERM-PROMPTS-SCRATCH and watch.

### PERM-PROMPTS-SETTINGS - whether to change the permission settings

**Context:** The same scan. The user settings chezmoi manages have no allow, ask or deny rules; the repository's 36 allow entries are read-only commands and moot under bypass; headless runs log "Ignoring 40 permissions.allow entries from .claude/settings.json: this workspace has not been trusted", harmless under bypass but voiding the repository allow list if bypass were dropped. Legal's third candidate: if Kris wants fewer prompts without bypass, add the read-only allow set and an explicit deny or ask list to the chezmoi-managed user settings, not per repository, and mark the workspaces trusted. A chezmoi change needs Kris's approval and a `chezmoi diff` review under his own instructions.

**Query:** Should the chezmoi-managed permission settings change now?

**Options:**

a) (recommended, confidence high - no current prompt comes from configuration, and the change pays only if bypass is dropped) Not now: fix the cause under PERM-PROMPTS-SCRATCH and PERM-PROMPTS-SHAPES, and revisit if Kris chooses to leave bypass mode.

b) Yes: a run under a machine grant adds the read-only allow set, an explicit deny or ask list and workspace trust to the chezmoi source, shown as a `chezmoi diff` for approval before apply.

c) Move the repository allow list to the user settings only, leaving bypass and trust as they are.

**Tending and findings.** Boundaries of a tending pass and of the finding kind, from the interim notes, and two tidy gaps.

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

### TIDY-GAPS - an orphan package and a missing source report

**Context:** `+/_WORK/ki.specifications/` in ki-principal holds only old reports, with no `work.md` or `messages.md`, so it has no identity or steward. Separately, harness record KI-HARNESS-REV-012 (Thoughtworks Radar input) links to `radar-confirm-2.report.md`, and no tracked copy exists anywhere. Creating package metadata or substituting another source would invent identity or provenance.

**Query:** Should the coordinator find the intended owner of the orphan package and the source report's durable home from their stewards before any repair?

**Options:**

a) (recommended, confidence high - preserves evidence and avoids inventing identity or provenance) Obtain both authoritative homes, then commission bounded repairs.

b) Keep both findings unresolved for Kris's next review.

**Repository standards, metadata and tools.** Repository metadata, record codes, partial repositories, diagram citations and how commands offer a preview.

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

### DIAGRAM-PRIVATE-CITATIONS - a code citation form for private repositories

**Context:** Kris, 24 October: settle a private-safe diagram citation form, "provided, of course, it's not causing a current failure somewhere"; no audit fails today. The `ki-diagrams` standard already says "Sources cite repository-relative paths. A repository URL in a source's metadata is the repository's own public remote or is omitted", its `traced` field takes repository-relative paths or pathspec globs, and its privacy rule bars a private repository's name, note content or commit subject from any committed source, SVG or HTML. What it lacks is a form for citing the revision and lines a diagram was traced from, because Archify's own citation object accepts a citation only with a repository URL. PERSONAL-TOWER-SITE-019 waits on the answer and PERSONAL-PRINCIPAL-045 shipped without line citations.

**Query:** Should `ki-diagrams` define a URL-free citation for private repositories, carried in the source's own metadata rather than Archify's citation object?

**Options:**

a) (recommended, confidence high - it extends the rule the standard already states, needs no new privacy exception, and the audit can check it mechanically) Yes: for a private repository, each `traced` entry may carry the short revision and a line range, `path:revision:lines`, with no URL; Archify's URL citation is used only where the remote is public; the audit accepts either form. A harness run writes it and Personal's two records follow.

b) Paths only: private repositories cite `traced` paths and nothing finer, as PERSONAL-PRINCIPAL-045 shipped, and the line-level ask is dropped.

c) Allow Archify's citation with the public mirror's URL where one exists and paths only where none does.

### CLI-PREVIEW - How public commands that change state offer a preview

**Context:** You settled that `mgit repair` writes by default, and on 24 October left the wider convention open. Today the two harness standards for tools ([tool repositories](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-tools/references/standards-tool-repositories.md) and [CLI conventions](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-tools/references/standards-cli-conventions.md)) still require a preview step before a repair writes, contradicting that decision. `mgit repair`, `ki repo repair` and `ki repo conform` already act by default; `ki repair` and Almanac repair keep preview gates. Some writes must keep their safeguards: Rig remove (deletes data), Rig repair (a reviewed proposal file), firewall and service changes, and remote host removal. The command inventory is retained in [wow-dryrun-survey.report.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/wow-dryrun-survey.report.md).

**Query:** Should public commands that change owned state write by default and offer `--dry-run`/`-n` as the preview, with both standards reconciled now and each tool changed later through its own work?

**Options:**

a) (recommended, confidence medium - reviewed; a masked blind review on Codex recommended it, keeping medium because your decision settled `mgit` only, not every shipped command) Write by default; `--dry-run` and `-n` show the same changes without applying them, and must prevent local and provider changes, not just the final write; `--check` is a read-only verification that fails on findings; `--apply`, `--write` and `--fix` are not routine write gates, and `--yes` only confirms. Keep named, documented exceptions for data deletion, publication, reviewed proposals and connection-critical changes. Reconcile both standards first, then change each tool through its owning work, with no fleet-wide flag migration.

b) Keep the current convention with `mgit repair` as the one exception, and hold the survey for a later decision.

**Skills and bootstrap.** Which skill owns the bootstrap checklist and what becomes of ki-trades.

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

**Acceptance.** One delivered record awaiting Kris's acceptance.

### ACCEPT - KI-PRINCIPAL-MOD-009 awaits your review

**Context:** [KI-PRINCIPAL-MOD-009](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-MOD-009-amend-adr-001-staging-wording.md) amends the staging wording of ADR-001 and is delivered and awaiting acceptance. [KI-PRINCIPAL-OPS-014](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-OPS-014-gfm-conversion.md) (GFM conversion) is not yet ready: it still needs its four-client render checks.

**Query:** Do you accept KI-PRINCIPAL-MOD-009 as done?

**Options:**

a) (recommended, confidence high - delivered, its checks pass and nothing depends on it remaining open) Accept it after reading the amended wording.

b) Return it with the change you want.

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
