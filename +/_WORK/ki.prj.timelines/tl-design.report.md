# [Foundations](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/foundations.md) › [Timelines](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/timelines.md) › tl-design

**🤖 → 👤 Handoff to supervisor · Run report at 23:32 BST · last mark 19:03 BST**

---

## Done

- Design brief written and committed: [timelines-skill-brief.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.timelines/design/timelines-skill-brief.md), commit `7f26676f`, local only; the pre-commit gate passed.
- The brief takes Kris's four settled points as fixed and puts 29 numbered points up for review. It adds three new findings: spans are a separate item type; subscribed calendars probably don't count towards free/busy, so a busy flag only blocks time when it is written into the owner's own calendar; and the Observatory can't serve feeds because it only listens on the local machine.
- Prompts for the two independent reviews and the merge are ready in the run's state folder: [tl-review-fable.prompt.md](/Users/krisbrown/.local/state/ki/agents/timelines/tl-review-fable.prompt.md), [tl-review-astra.prompt.md](/Users/krisbrown/.local/state/ki/agents/timelines/tl-review-astra.prompt.md) and [tl-merge.prompt.md](/Users/krisbrown/.local/state/ki/agents/timelines/tl-merge.prompt.md).
- Nothing outside `+/_WORK/ki.timelines/design/` was changed: not the 5G component, not legal's gantt and not [KI-HARNESS-GOV-222 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/f9da11ced73eaab512d5df6a4ef6d21f574ce89d/docs/roadmap/KI-HARNESS-GOV-222-timeline-and-calendar-skill.md). Nothing was pushed.

## In Progress

- The run stopped after the brief. The two reviews and the merged report are not done. This run was told not to start other agents, and the design standard forbids a merged report built on fewer than two independent reviews. The coordinator needs to launch the reviews (see REVIEW-LAUNCH).
- The queries below carry the brief's own recommendations, made before any review. Each is medium confidence, so the coordinator will send it for blind review. The merged report may change them.

Outstanding - no action requested now:

- Moving [KI-HARNESS-GOV-222 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/f9da11ced73eaab512d5df6a4ef6d21f574ce89d/docs/roadmap/KI-HARNESS-GOV-222-timeline-and-calendar-skill.md) from `project: observatory` to `project: timelines`, and its priority and plan, stay with the harness.
- legal's "FR Timeline to FDR" gantt stays as Mermaid until the skill exists.

## Queries

### REVIEW-LAUNCH - Launch the two reviews and the merge

**Context:** The design loop needs at least two independent reviews on different runtimes before a merged report. This run could not launch agents. The prompts are ready, and they match the pattern ki.ways-of-working used: Fable on Claude Code and Astra on Codex, both at high effort, then a merge gated on both.

**Query:** Should the coordinator launch the two reviews in parallel and then the merge once both finish?

**Options:**

a) (recommended, confidence high - this follows the design standard and the earlier Fable and Astra precedent) Launch `tl-review-fable` (`--runtime claude --model claude-fable-5-1 --effort high`) and `tl-review-astra` (`--runtime codex --effort high`, with the strongest Codex model of the day) from the ready prompts, then `tl-merge` with `--wait-for` on both.

b) Relaunch tl-design with authority to start its own reviewers and the merge.

### FEED-HOME - Where a private base without a site publishes its dates

**Context:** legal-principal and personal-principal have no site, and their dates are private. legal's include court dates. 5G serves public static `.ics` files, with a bypass around its Cloudflare Access gate. The Observatory listens only on the local machine, so no phone or hosted calendar can reach it. Subscribed calendars probably don't count towards the subscriber's own free/busy, so the settled `busy` flag only blocks time when items are written into the owner's own calendar. That claim is for the reviewers to check. `mcp-gsuite` and `mcp-m365` can already write calendar events.

**Query:** Where should a private base without a site publish its calendar sets?

**Options:**

a) (recommended, confidence medium - keeps private dates off any public URL and makes `busy` actually block time, but replaces "subscribe" with "write into" and needs a write credential; the coordinator will send this for blind review) Account sync: write each private set into a dedicated calendar in the owner's Google or Microsoft account through the existing MCP servers. Re-runs are keyed by event UID, so they update events rather than duplicate them. Sites keep static feeds for public sets.

b) A capability URL: an unguessable feed path on a public host. This keeps the subscribe model, but anyone who gets the URL sees every date.

c) A private feed host behind a token-checking Cloudflare Worker. This means new infrastructure to build and secure.

### SPAN-FEED - How a feed carries a span

**Context:** Kris settled that a span never takes busy time and may show in the timeline view. How a feed carries one was left open. The brief gives items three types: milestone, event (including multi-day events such as 5G's JCB on 3-4 November) and span. Most of legal's "waiting on other side" rows are really single dates by which someone else should act.

**Query:** Should spans appear in calendar feeds at all?

**Options:**

a) (recommended, confidence medium - the calendar stays milestone-centred and nothing can block time by mistake; the coordinator will send this for blind review) No. Spans appear only in the timeline view. Where a span's end matters, that end is its own milestone item, which can go in a feed. The rubric fails a busy span.

b) Feeds carry spans as free all-day blocks across their dates.

c) Feeds carry only a span's start and end as two free markers.

### SKILL-SHAPE - One skill or a skill plus a view

**Context:** The views are the 5G site's List, Months and Runway views, and in a knowledge base, a generated timeline. The site rendering already belongs to the website skills, and in a base the live-artifact skill governs a Markdown source paired with rendered HTML.

**Query:** Should the timeline view live in the same skill as the dated items and feeds, or in its own skill?

**Options:**

a) (recommended, confidence medium - the view is generated from the same model, and the existing website and live-artifact skills already own its rendering; the coordinator will send this for blind review) One skill. It owns the item model, the feeds and a view JSON contract. Sites render that JSON with their own stack, and bases render it as a live-artifact pair.

b) A dated-items skill plus a separate timeline-view skill.

### SKILL-NAME - The skill's name

**Context:** The naming decision [ADR-KI-HARNESS-SKILLS-003](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/decisions/ADR-KI-HARNESS-SKILLS-003-dependency-order-for-multi-skill-composition.md) asks for a plural name when the skill governs a collection, and none of the three candidates is taken. `ki-calendars` suggests busy-time calendars, which Kris set aside in favour of milestones. "Timeline" is already a diagram type in `ki-diagrams` and Archify. "Key dates" names the single source that both outputs come from.

**Query:** Which name should the skill take?

**Options:**

a) (recommended, confidence medium - it names the canonical source rather than one output, and avoids both the busy-calendar reading and the clash with timeline diagrams; the coordinator will send this for blind review) `ki-key-dates`.

b) `ki-calendars`.

c) `ki-timelines`, matching the Project's name.

### CODE-HOME - Where the extracted code lives

**Context:** `ics.ts` and the view logic have no dependencies. `ki-diagrams` already keeps generator scripts inside the skill. Kris prefers a vendored copy with a drift check, or a pinned reference, over publishing a package. The 5G site imports the feed builder when it builds.

**Query:** Where should the shared feed builder, item model and rubric live?

**Options:**

a) (recommended, confidence medium - it follows the `ki-diagrams` precedent and Kris's preference for shared code, and it needs no package publication; the coordinator will send this for blind review) In the skill's own `scripts/` in the harness. 5G vendors a copy with a drift check, and `tools-ki` gains a command only if a stable machine contract is needed later.

b) A `ki` command in `tools-ki` that owns building and syncing.

c) A shared package used through a workspace or a pinned Git reference.

### ADOPTION-ORDER - Which base adopts first

**Context:** 5G already has the component and a public host, so adopting it there proves the extracted code behaves the same, with feeds unchanged except for `PRODID` and the busy properties, and removes its duplicate timeline list. legal has the most time-critical value, with dates running to February 2027, and is the first to use times, spans and private sync. personal-principal first needs its dates moved out of prose into frontmatter.

**Query:** What is the adoption order?

**Options:**

a) (recommended, confidence medium - the lowest-risk pilot proves the extraction before the private-sync work; the coordinator will send this for blind review) 5G Emerge as the pilot, then legal-principal, then personal-principal.

b) legal-principal as the pilot for early value, then 5G Emerge, then personal-principal.

### 🤖 → 👤 Handoff to supervisor · since 23:32 BST

👤 7 with you

- [with you] REVIEW-LAUNCH · supervisor · since 23:32
- [with you] FEED-HOME · supervisor · since 23:32
- [with you] SPAN-FEED · supervisor · since 23:32
- [with you] SKILL-SHAPE · supervisor · since 23:32
- [with you] SKILL-NAME · supervisor · since 23:32
- [with you] CODE-HOME · supervisor · since 23:32
- [with you] ADOPTION-ORDER · supervisor · since 23:32
- [committed] design brief, unpushed
