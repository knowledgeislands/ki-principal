# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-restart-consolidate

**🤖 → 👤 Handoff to supervisor · Run report at 21:58 BST · last mark 02:10 BST**

---

## Done

- Consolidated the RESTART-ON-SOL queue: every line in this work's [messages.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/messages.md), and the method lines State of play holds for Ways of working in its [messages.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/messages.md), which have not moved across yet. They are read against VA-CONSOLIDATE's seven-point model in [State of play's decisions](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/decisions.md) and grouped below by the seven areas. [va-consolidation.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/design/va-consolidation.md) and [skills-assessment.report.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/skills-assessment.report.md) were used as input only.
- Read-only. No standard, skill, note, record or package file was changed, nothing was sent to any territory and no agent was launched. The only commit is this report, `docs(work): ki.ways-of-working restart consolidation report`. Its pre-commit hooks ran, and the outcome is in the run report.
- Found already landed or stale, checked against the files on sol:
  - KI-SOP-PATTERN and SOP-SECONDARY are in the standard's [Secondary States of play](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md#secondary-states-of-play), and harness `main` is level with origin.
  - COORD2-RUBRIC's title check is fixed in harness `0aa9c4d2`. The optional `label` check at `coordination.ts:372` still compares the slug.
  - AWAY-GRANT is in the standard's Away grants and the coordinator style. Only the standing deny-list it proposed is open.
  - WAKE-SUBSTRATE was settled on 23 October as a): the completion watcher comes first and launchd waits.
  - TENDING-ROADMAP and Tending's working-area checks are done.
  - TAG-FORM, HOMEPAGE-SOURCE and KI-CODE are settled in the [repository metadata note](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/repository-metadata.md#decisions). RESTART-ON-SOL's "TAG-FORM is still Kris's to settle" is out of date.
  - Personal has finished moving from Initiatives to themes. Legal still has 7 files in `Streams/Initiatives/`, no `Streams/Themes/` and one `initiative:` field. HNR has one `initiative:` field.
  - The MOD ledger in [_ISSUES.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/_ISSUES.md) still reads `MOD: 9`.
  - Claude Code has a `-n, --name` launch flag that sets a session's display name. A session already running cannot rename itself.

### Priority order

1. **Coordination standard (area 1) - now.** This covers the report forms, commands and query handling Kris uses every day. THREAD-RENAME must land before KI > SoP bootstraps on Sol.
2. **Tending (area 2) - now.** Valle Armonia and Personal already run it as interim policy, and the fold is a design-note edit that needs no approval.
3. **REPO-METADATA (area 7) - next.** Its decisions are settled and wait to go into `ki-repo`. Nothing is tagged until then. This work's share, the note's Other territories sections, rides with the Tending unit.
4. **Initiatives to themes (area 4) - next.** Kris asked for mechanical enforcement, but only Legal and HNR still carry residue, so it needs a close date before checkers fail.
5. **Run rules (area 5) - next.** The secret-access rules are small and follow Kris's own direction. Diagram citations block nothing today.
6. **Roadmap and record shape (area 3) - next and later.** The MOD-LEDGER fix is trivial and goes now, the unattended-work assessment next, and due dates later because they need tools-ki.
7. **Homeless decisions (area 6) - later.** This is housekeeping in State of play's log, and nothing waits on it.

### First three units to launch

1. **coord-standard**, in a harness worktree: once Kris has answered THREAD-RENAME, SUMMARY-WINDOW, FINDINGS-SECTION, QUERY-RULES, COORD-COMMANDS and DRAIN-END, one run edits the ki-coordination standard, `SKILL.md`, the `ki-coordinator` output style and the banner test together, then regenerates with `ki dev skill generate ki-coordination --write`. THREAD-RENAME goes first and may ship alone if the other answers are still outstanding.
2. **tending-fold**, in ki-principal, design notes only, with no approval needed. In [tending.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/tending.md) it:
   - folds in [round 2](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/tending-round2-notes.md);
   - adds the level 3 agent-memory overlap check, the level 4 guidance-promotion question and the XDG-state check;
   - writes the Personal and Valle Armonia Other territories sections and answers Valle Armonia's five open points;
   - pins the dead territory-review link.

   It also writes the Other territories sections in [findings.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/findings.md) and [repository-metadata.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/repository-metadata.md), marks the Fibonacci text in [roadmap-sizing-and-burn-down.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/roadmap-sizing-and-burn-down.md) superseded, and advances the MOD ledger to 10.
3. **model-shape**, a `ki-work-design` brief in this work. It maps the single State of play cascade, packages against threads, relationship metadata and host-targeted lines, with the Work Process note change going through the Enactment Process. Kris asked for the model to be "mapped out", so the brief returns its own queries.

### Area 1 - The coordination standard

**1a. THREAD-RENAME (IMPORTANT).**

- **Asks:** Kris, 24 October: "When the thread bootstraps, is there a way that we can get it to rename itself so that it's got a good name ... If not, can we make sure that it states that in its summary reports as well?"
- **Conflicts:**
  - The standard already says a session takes its label "where the runtime can name a session". The `--name` flag is that means, but only for a launched session.
  - A `Rename this thread: /rename ...` line breaks the rule that no report emits "a send or resume prompt or paste instruction".
- **Proposed:** openers from `ki agent prompts` launch with `claude --name "<label> (<id>)"`. Bootstrap and re-bootstrap reports carry the `/rename` line as a named exception, for sessions opened by pasting. The standard, the style and the banner test change together.
- **Priority:** now. Kris wants it before the KI State of play bootstraps on Sol. Query THREAD-RENAME.

**1b. Report windows: SUMMARY-SINCE-MARK and SUMMARY-OUTSTANDING.**

- **Asks:**
  - Kris: "after this mark, what I'm expecting is done to say nothing since the last mark, and in progress to say nothing is running, in queries to say no outstanding queries ... and it says on hold at the end."
  - Kris: "all of this can be fed back to the ways of working to make sure that these summaries get clearer and better."
  - Outstanding carries only what this work holds. It has no push state, and it leaves out hand-offs already sent and items held by roadmap records.
- **Conflicts:**
  - [Report forms](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md#report-forms) windows the Summary "since your last message".
  - The recap's Outstanding carries open records forward across marks.
  - The owner report says "A handoff to other work stays outstanding until the owner expressly says it is done". That is an earlier owner position, which the 24 October words narrow.
- **Proposed:** the Summary's Done and In Progress window on the mark. Outstanding lists only this work's own holdings. A hand-off is reported once in Done when it is sent. Roadmap-held items stay in the roadmap. The recap and the full summary keep the longer look back.
- **Priority:** now. Query SUMMARY-WINDOW.

**1c. Findings and prompts: FINDINGS-SECTION and PROMPTS-IN-FULL.**

- **Asks:**
  - Kris: "if I ask you for some findings ... that needs to be in its own section in the summary, and repeat the same tables until we're happy with things."
  - Kris: "the prompts should be included in them in full. We shouldn't refer back to previous ones when we ask for a summary from a mark."
- **Conflicts:** the owner report has exactly three sections "every time", and the report rubric checks that shape. The Valle Armonia unclear points also need answers: is a brief-requested dispositions table a finding, and does a run write `findings/<tag>.md` when its brief names no file? Personal's `findings/REPO-META.md` is outside the `ki-work-package` closed list.
- **Proposed:** an optional `## Findings` section, shaped as in [findings.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/findings.md), present only when Kris asked for findings or a prompt to hand on. It is carried until a mark or until Kris is content, and each table opens with its goal. `findings/` joins the closed list.
- **Priority:** now. Valle Armonia and Personal already apply it. Query FINDINGS-SECTION.

**1d. Query handling: INTERACTIVE-QUERIES, INTERACTIVE-QUERIES-SELF-CONTAINED, INTERACTIVE-PASS-PROMPT, QUERIES-POSTED-FIRST and SPLIT-QUERIES.**

- **Asks:**
  - Kris: "the default is to log them in the summary ... But I might ask ... to go through them interactively."
  - Kris: "these new style prompts are amazing ... I get a lot more context from them."
  - Kris: "before you start those interactive ones, you also post them in full into the thread as well."
  - Kris: "if you feel like you can't give good level of confidence, even after review, to a particular query, then it might be worth splitting it up."
  - hnr's interactive-pass prompt should become the standard's interactive-pass form.
- **Conflicts:** none. Kris's personal `communication.md` already carries the interactive rules, and the standard's "a query the owner cannot answer with one instruction is two queries" already leans towards splitting. The standard is simply silent.
- **Proposed:** one Interactive pass subsection with these rules:
  - queries are posted in full first;
  - one or two at a time, each a self-contained block;
  - each answer is read back before the next pair;
  - a query still below high confidence after its review is split into tagged parts, each with its own confidence.
- **Priority:** now. Query QUERY-RULES.

**1e. Commands: COORD-COMMANDS, with DRAIN-END.**

- **Asks:** Kris: "you should be able to make that express or explicit by saying KI-coordination mark or KI-coordination hold or KI-coordination drain."
- **Conflicts:**
  - Only `summary`, `recap`, `full-summary` and `mark` exist as commands.
  - The Work Process note makes drain an activity inside the move to On hold, never a state.
  - DRAIN-END, already open in [queries.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/queries.md), decides how a drain check ends.
- **Proposed:** add `hold`, `drain`, `resume`, `send` and `receive`. `hold` is drain plus On hold. `drain` stops launching and lets runs finish while the work stays With worker, and its result goes where DRAIN-END decides. The spoken words stay as synonyms. The Work Process note is unchanged.
- **Priority:** now. Query COORD-COMMANDS.

**1f. The cascade model: SINGLE-THREAD, SOP-PROJECT-CARE, COORDINATOR-HOST, CHEZMOI-REMIT's host rule and WORK-PROCESS-NOTE.**

- **Asks:**
  - Kris: "there's a difference between work packages and threads, which are things working on the work packages ... we really only need to direct it through one single thread, which is focus at the state of play level, and it can then cascade down."
  - Kris: "we need to add to the metadata of the threads, what it's related to."
  - Kris: "coordination teams should use a hostname to understand who they're running on."
  - ki.chezmoi asks for the no-host rule to be reconciled with per-machine work.
  - hnr asks for one line on secondary States of play in the Work Process note.
- **Conflicts:**
  - Territory work "executes nothing" and writes into a package "only by adding a line to its `messages.md`" in the [Work Process note](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Processes/Work Process/Work Process.md>) and the standard's Territory work.
  - `parent` exists only on a secondary State of play.
  - The rule "Neither file names a host" in Picking work up, the "no host" prohibited payload in the work-package standard, and the requirement that a hold "never says which host the work comes back up on" all stand against host-targeted lines.
  - Some groundwork already exists:
    - the label may carry a `(<host>)` suffix for work limited to one machine, which already covers per-machine work;
    - a machine-local thread binding, `~/.local/state/ki/threads/<repository>/<slug>.json`, could tell State of play whether a Project has a live thread without putting host or session into the package.
- **Proposed:** the model-shape design brief (unit 3). Its outcome amends the Work Process note through the Enactment Process with a record, and the coordination and work-package standards. Host-targeted lines are one of its questions. COORDINATOR-HOST is the known conflict.
- **Priority:** now to shape, next to enact. No query yet; the brief brings them.

**1g. Wakes and ticks: CENTRAL-TICK, WAKE-SUBSTRATE and AWAY-GRANT.**

- **Asks:** Kris: "a scheduled job that runs for each territory against its capital, and it checks to see if anything has moved past its last tick point ... Just an idea to take forwards."
- **Conflicts:** the style says "Pursue the agreed completion watcher first; defer launchd, doorbells and extra liveness fields". WAKE-SUBSTRATE a) was settled on 23 October, and the away-grant recording is already in the standard.
- **Proposed:** keep CENTRAL-TICK as an idea on the [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) Project note under CAPTURE-GATE, beside the deferred launchd option. The standing deny-list goes with UNWRITTEN-RULES in area 5.
- **Priority:** later.

**1h. Tool defects routed here: `ki agent send` "no such run", and COORD2-RUBRIC's residue.**

- **Proposed:**
  - `ki agent send` failed for a live hnr run on 24 October 07:00 BST. It is tools-ki, which [work.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/work.md) puts with ki.tools-burndown, so it goes there as a line.
  - The COORD-2 `label` residue is a one-line fix that can go in the coord-standard run.
- **Priority:** next.

### Area 2 - Tending

**Lines:** METHOD, TENDING-ROUND-2, TENDING-GUIDANCE-OVERLAP, TENDING-SIZES, TENDING-XDG-STATE, the Tending parts of TENDING-PERSONAL and INTERIM-VA, and BASELINE with the guidance-promotion gaps from the skills assessment. TENDING-ROADMAP is done.

- **Asks:**
  - Kris: "I also meant auditing things like agents.md and claude.md to make sure that we weren't overlapping with things that are already in skills and the promotion of things into skills where there's commonality."
  - Kris: "we need to make sure that things like the XDG state is also considered and reviewed": machine-local state such as `~/.local/state/ki/agents/` run folders and reports.
  - Kris liked size shown as a T-shirt label, 👕 S.
  - The pilots also ask for a rule for regular-work packages naming their theme, a level 1 cross-reference check, a non-remote audit mode and a way to see member packages from the Capital.
- **Conflicts:**
  - None with a standard, because Tending is still a design note.
  - The `ki-work-roadmap` `size` values are `s`, `m`, `l` and `xl` with no `xs`, yet 👕 XS was used for BIND-2.
  - PMO level 1's "a planned Project has none" clashes with the seeding rule that lets State of play create an On hold package to queue a first message.
  - Whole-repository conform touches other packages' files in a shared Capital.
- **Proposed:**
  - The tending-fold run (unit 2).
  - A small `ki-work-roadmap` display convention: 👕 plus a capital letter, field values unchanged, no XS. It is carried in coord-standard's harness worktree, or alone if Kris prefers.
  - BASELINE, the Capital skill baseline, waits on State of play's blind review of the skills assessment, then comes here as level 4's question.
- **Priority:** now. Two territories run it today.

### Area 3 - Roadmap and record shape

**Lines:** UNATTENDED-AND-DUE-DATES, WORK-STATUS-FORM, MOD-LEDGER and SORT-ARM. CLI-FIELDS stays held.

- **Asks:**
  - Kris: "we need to push that into the ways of working thread as something that we need to do an assessment of." This means when an agent may complete roadmap work unattended, with Personal's [unattended-criteria.md](</Users/krisbrown/workspaces/personal/personal-principal/+/_WORK/kb/design/unattended-criteria.md>) as evidence.
  - Kris wants a due or key milestone date on records, "of what they're working towards".
  - Confirm the `ki work status` form for [KI-TOOL-KI-CLI-160](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-160-work-status-routing-view.md) and [KI-TOOL-KI-CLI-149](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-149-work-status-views-contract.md).
  - Advance the MOD ledger to 10.
  - SORT-ARM is open.
- **Conflicts:**
  - The `ki-work-roadmap` record format has no date field, and tools-ki parses the schema.
  - The 22 October decision lets three high-confidence reviewers move triage forward, which overlaps the unattended criteria.
  - `ki work status` is ki.tools-burndown's under [work.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/work.md).
- **Proposed:**
  - MOD-LEDGER rides the tending-fold run.
  - A read-only assessment run compares Personal's criteria with the 22 October consensus rule and the delegation authority tiers, and returns a proposed `ki-work-roadmap` rule and an optional `due` field. The field needs a tools-ki change through ki.tools-burndown.
  - WORK-STATUS-FORM is routed to ki.tools-burndown, which brings Kris its own query.
- **Priority:** MOD-LEDGER now; the assessment next; the due field later.

### Area 4 - Initiatives to themes

**Lines:** INITIATIVES-RESIDUE and THEME-REGISTRY-ENFORCE.

- **Asks:**
  - Kris: "does Knowledge Islands still support initiatives? If so, we need to path that back to Knowledge Islands to get that fixed."
  - Kris: "make sure that that is what is happening across all the rest as well, and make sure that that is enforced mechanically now."
- **Conflicts:**
  - The tolerance window has no end date and closes only at migration phase 5.
  - The roadmap-field backstop is 60 days after the accepting `ki` release.
  - Flipping the warnings now would fail Legal's and HNR's audits at once.
  - Kris's "across all the rest" is an express request to message those territories, so SOURCE-AGNOSTIC does not bar it.
- **Proposed:** message Legal's and HNR's States of play to migrate. Then turn the warnings into failures in the ki-coordination, ki-work-roadmap, ki-work and ki-repo-kb-activities checkers, together with tools-ki `registry.ts` through ki.tools-burndown, on a set date. The tolerance-window text in the standard closes at the same time.
- **Priority:** next. Query THEME-CLOSE.

### Area 5 - Run rules

**Lines:** OP-CACHE-RULE, CF-UNIFORM, DIAGRAM-PRIVATE-CITATIONS and UNWRITTEN-RULES. ZT-FINDINGS stays with State of play and is related.

- **Asks:**
  - Kris: "I really need the OP cache doing, please." The proposed rule is that runs read 1Password only through `op_cache` with `OP_CACHE_SERVICE_ACCOUNT_ONLY=1`.
  - Kris: "anything to do with my Cloudflare setup in reality should be uniform across whichever territory I'm working in. It shouldn't be baked into the territories information." A run reads a Cloudflare credential only through `~/bin/cf_token`, and no territory's notes record item or token ids.
  - Kris wants a private-safe diagram citation form, "provided, of course, it's not causing a current failure somewhere" (it is not).
  - Confirm the four unwritten HNR rules one by one.
- **Conflicts:**
  - The [background-run standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-delegation/references/standards-background-runs.md) bars reading secrets but names no helper.
  - Archify accepts a citation only with a repository URL, and the privacy rule bars naming a private repository.
  - UNWRITTEN-RULES a), settled under grant on 23 October, made none of the four a standing instruction. The new line, under "Move all three to Ways of Working", asks for Kris to confirm each, which would form AWAY-GRANT's missing deny-list.
- **Proposed:**
  - One background-run rule for secrets through the dotfiles helpers, plus the matching line in `ki-repo-website-cloudflare`.
  - A citation-form proposal (revision, relative paths and lines, no URL) from a small run, with [KB-MIDNIGHT-TOWER-SITE-019](/Users/krisbrown/workspaces/personal/apps-tower.midnight.ninja/docs/roadmap/KB-MIDNIGHT-TOWER-SITE-019-redraw-mermaid-in-archify.md) waiting on it.
  - The four rules taken in an interactive pass as four split queries when Kris chooses. The 23 October a) stands meanwhile.
- **Priority:** the secrets rule next, citations later, the four rules later. Query RUN-SECRETS.

### Area 6 - Homeless decisions in State of play's log

Proposed homes, as one defaults query. State of play's log is edited by State of play, not by this work.

| Decision | Proposed home |
| --- | --- |
| PRFLOW (push straight to harness `main` after tests and audit) | ki-agentic-harness `AGENTS.md` contribution line |
| PIN (tools-ki CI builds its own `ki`) | tools-ki CI guide; strike with a pointer |
| Burn-down focus (14 October) | Superseded by CAPTURE-GATE and ROADMAP-CAP; strike, saying so |
| CAPTURE-GATE | Already in `ki-next` and `ki-delegation` at harness `071567a1`; strike with a pointer |
| GO-AHEAD (17 October "permission to get on with anything") | Spent, overtaken by later explicit grants; strike |
| KI-AGENTS-NAME ("Keep "agents"; ways of working logs the decision") | This work's decisions log, as Kris asked |
| CAPTURE-ONLY (17 October intake) | Spent with the intake; its rule lives in CAPTURE-GATE; strike |
| DIAGRAMS-BLACK | A defect, not a decision: check `themes.md` rendering, and if it still fails, State of play captures it for the diagram owner |
| RIG-REL-PATCH (follow-up releases stop and ask first) | `ki-repo-tools` release-on-demand policy, which already says it; strike with a pointer |
| SPEC-REVIEW (starts once the KI roadmap is near zero; the KI-RELEASE half is spent) | ki.portable-specifications' decisions log |

**Priority:** later. Query DECISION-HOMES.

### Area 7 - REPO-METADATA

**Lines:** the RESTART-ON-SOL route, METADATA-SETTLED, METADATA-STANDARD, KI-CODE, META-SETTLED-PERSONAL and the metadata parts of TENDING-PERSONAL and INTERIM-VA.

- **Asks:** Kris: "Once we've settled these things, we should make sure that we fold anything back ... so that we make sure that this becomes a standard." Kris on KI-CODE: "It's the skill which will mandate the KI ones that are mandatory for every KI repo, right?"
- **Conflicts:**
  - RESTART-ON-SOL says TAG-FORM is open, but it is settled.
  - The pilots found these open points:
    - no optional or shape-scoped tag type;
    - whether a code may equal the `territory_prefix`;
    - which `.ki.toml` table holds `homepage` and `keywords`;
    - dotted domain keywords cannot become GitHub topics;
    - `ki-repo-project` is used as a primary shape;
    - `MIT` on private sites;
    - `gh repo view` under briefs that bar remote calls;
    - whether wording-only description changes may go first.
  - The work's scope names neither `ki-repo` nor ki.baseline-rollout. State of play proposes ki.baseline-rollout for the standard and checker.
- **Proposed:** tending-fold writes the Other territories sections and a short answer to each open point. ki.baseline-rollout carries the `ki-repo` standard and checker change through State of play's route. Nothing is tagged until it lands, and each GitHub change needs Kris's approval.
- **Priority:** next. No query: State of play's route already covers the receiver, and the open points are design answers.

### Other

- Nothing in the queue fits none of the seven areas. THREAD-RENAME, FINDINGS-SECTION, PROMPTS-IN-FULL, SPLIT-QUERIES and the three HNR moves (WAKE-SUBSTRATE, AWAY-GRANT, UNWRITTEN-RULES) are placed in areas 1 and 5.
- These stay as they are: the RIG-ATTENDED walk-through stays parked; PAPERCLIP-REQ stays held; CLI-FIELDS stays held.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- After this report is received, the coordinator copies the queries below into `queries.md` and disposes of the queue lines this report covers.
- State of play has not yet moved its method lines across. This report covers them where they sit, so the move can be a single disposition line.

## Queries

DRAIN-END and SORT-ARM stay open in [queries.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/queries.md) and are not repeated here. Medium-confidence queries are marked for one masked blind review before they reach Kris.

### THREAD-RENAME - name each coordination thread at launch, and say so in the bootstrap report

**Context:** Kris asked for a bootstrapped thread to get a good name, or failing that for the report to say how. Claude Code's `--name` flag names a session at launch, but a running session cannot rename itself. A `/rename` line in a report breaks the current rule against paste instructions in reports. Kris wants this before KI > SoP bootstraps on Sol.

**Query:** Should openers launch with `--name`, with bootstrap and re-bootstrap reports also carrying one `Rename this thread: /rename <label> (<id>)` line as a named exception?

**Options:**

a) (recommended, confidence medium - needs blind review; covers both launched and pasted sessions, at the cost of one exception to the no-paste rule) Launch openers with `claude --name "<label> (<id>)"`, and add the rename line to bootstrap and re-bootstrap reports only.

b) Launch openers with `--name` only, and keep reports free of paste lines.

### SUMMARY-WINDOW - window the Summary on the mark and narrow Outstanding

**Context:** Kris said that after a mark a Summary should show nothing done, nothing running and no queries. Kris also said Outstanding should hold only what this work carries, with no push state, no hand-offs already sent and nothing waiting in a roadmap. The standard windows the Summary "since your last message". It also keeps a hand-off outstanding until Kris says it is done, an earlier position.

**Query:** Should the Summary's Done and In Progress window on the mark, with Outstanding limited to this work's own holdings and the earlier hand-off rule superseded?

**Options:**

a) (recommended, confidence high - Kris's own words on 24 October, the later and narrower position) Window the Summary on the mark, report a hand-off once in Done, leave roadmap-held items to the roadmap, and keep the recap and full summary as the longer views.

b) Narrow Outstanding only, and keep the Summary window as "since your last message".

### FINDINGS-SECTION - add a Findings section to the owner report

**Context:** Kris asked for findings to sit in their own section, repeated until Kris is content, with each table opening with its goal. Kris also asked for prompts to hand on to be carried in full. Valle Armonia and Personal already use it as interim policy, and it worked. The owner report today has exactly three sections.

**Query:** Should the owner report gain an optional `## Findings` section, as set out in the findings design note, with `findings/` allowed in a work package?

**Options:**

a) (recommended, confidence high - two territories have used it without trouble and it follows Kris's words) Adopt it as an optional section, carried until a mark or until Kris is content, prompts in full included.

b) Keep three sections and carry findings in Done.

### QUERY-RULES - write the interactive pass and query splitting into the standard

**Context:** Kris set out how queries are taken interactively:

- the Summary stays the default;
- on request, queries are posted in full first;
- they are then taken one or two at a time, each a self-contained block;
- each answer is read back before the next pair.

Kris also asked that a query still below high confidence after review be split into separately tagged parts. Kris's personal settings carry most of this already, but the standard does not.

**Query:** Should the standard adopt these rules, with hnr's prompt as the interactive-pass form?

**Options:**

a) (recommended, confidence high - each rule is Kris's own words, and none conflicts with the standard) Adopt the interactive pass and the split rule together.

b) Adopt the interactive pass now and leave splitting for later.

### COORD-COMMANDS - add explicit commands for hold, drain, resume, send and receive

**Context:** Kris wants to say a move as a command, such as `/ki-coordination hold`. Today only summary, recap, full-summary and mark are commands. In the Work Process note, drain is an activity inside the move to On hold, not a state. A standalone drain would stop new launches while the work stays With worker, and DRAIN-END decides how it reports.

**Query:** Should the skill gain `hold`, `drain`, `resume`, `send` and `receive`, with `drain` usable on its own?

**Options:**

a) (recommended, confidence medium - needs blind review; a standalone drain is new behaviour, but it needs no change to the Work Process note) Add all five; `hold` is drain plus On hold; `drain` alone stops launches and reports when the work has drained.

b) Add `hold`, `resume`, `send` and `receive`, with drain only ever part of hold.

### RUN-SECRETS - runs read secrets only through the dotfiles helpers

**Context:** Kris approved the 1Password cache ("I really need the OP cache doing") and said Cloudflare access "should be uniform across whichever territory I'm working in". The proposals are:

- runs read 1Password only through `op_cache`, in service-account-only mode;
- runs read Cloudflare credentials only through `~/bin/cf_token`;
- no territory's notes record item or token ids.

A sweep found no such ids in Knowledge Islands.

**Query:** Should the background-run standard and the Cloudflare site rubric adopt this one secrets rule?

**Options:**

a) (recommended, confidence high - follows Kris's words; both helpers exist in chezmoi, and nothing currently breaks it) Adopt it in `ki-delegation` and `ki-repo-website-cloudflare` together.

b) Adopt the 1Password half now and the Cloudflare half once the Cloudflare guide is reviewed.

### THEME-CLOSE - set the date Initiatives stop being accepted

**Context:** Kris asked that the theme registry be used everywhere and "enforced mechanically now". Checkers still only warn on `Streams/Initiatives/` and `initiative:`, and the tolerance window has no end date. Personal has migrated. Legal still has 7 Initiative files and no Themes folder, and HNR has one `initiative:` field. Failing now would break both audits.

**Query:** Should Legal and HNR be asked to migrate, with the checkers failing from a fixed date?

**Options:**

a) (recommended, confidence medium - needs blind review; the date is a judgement) Message Legal's and HNR's States of play now, and turn the warnings into failures on 7 November 2026, or earlier once a scan finds no residue.

b) Turn the warnings into failures at once and let Legal and HNR fix their audits.

### DECISION-HOMES - home State of play's older decisions as proposed (defaults)

**Context:** each of these lines is a low-stakes, reversible proposed home for one of State of play's older homeless decisions. The full table is in Area 6.

- PRFLOW goes to the harness `AGENTS.md`.
- PIN goes to the tools-ki CI guide.
- The 14 October burn-down focus is struck as superseded by CAPTURE-GATE and ROADMAP-CAP.
- CAPTURE-GATE is struck, pointing to `ki-next`.
- GO-AHEAD is struck as spent.
- KI-AGENTS-NAME goes to this work's decisions log.
- CAPTURE-ONLY is struck as spent.
- DIAGRAMS-BLACK is checked and captured only if it still fails.
- RIG-REL-PATCH is struck, pointing to the release policy.
- SPEC-REVIEW goes to ki.portable-specifications.

**Query:** Keep these defaults?

**Options:**

a) (recommended, confidence high - each choice is low-stakes and reversible) Keep the defaults.

b) Object to the ones you name.

### 🤖 → 👤 Handoff to supervisor · since 21:58 BST

👤 10 with you

- [with you] THREAD-RENAME · owner · since 21:58
- [with you] SUMMARY-WINDOW · owner · since 21:58
- [with you] FINDINGS-SECTION · owner · since 21:58
- [with you] QUERY-RULES · owner · since 21:58
- [with you] COORD-COMMANDS · owner · since 21:58
- [with you] RUN-SECRETS · owner · since 21:58
- [with you] THEME-CLOSE · owner · since 21:58
- [with you] DECISION-HOMES · owner · since 21:58
- [with you] DRAIN-END · owner · since 23 Oct
- [with you] SORT-ARM · owner · since 23 Oct
- [committed] restart-consolidate.report.md

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
