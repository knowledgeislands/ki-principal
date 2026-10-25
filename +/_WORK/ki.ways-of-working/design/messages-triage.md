# Messages triage - 25 October 2026

Run wow-messages-triage, for [ki.ways-of-working](../work.md). The nine routed lines in [messages.md](../messages.md) each ask for a change to a shared standard, which the unattended window to 08:00 GMT does not cover. This note turns each into the decision Kris must make on return, one `###` query per decision, answerable by letter. Two lines split into several queries where one answer would bundle unlike choices. Nothing here changes a standard; the lines stay in the queue until the coordinator disposes of them against Kris's answers.

Fourteen queries: eleven at high confidence, three at medium (UNATTENDED-AND-DUE-DATES, WAKE-SUBSTRATE, UNWRITTEN-RULES-DRAFTS). None has been through a blind review.

## Queries

### UNATTENDED-AND-DUE-DATES - adopt the eight criteria as the unattended assessment

**Context:** Kris, 24 October, through Personal's State of play: "we need to push that into the ways of working thread as something that we need to do an assessment of", and roadmap records should carry an explicit due date or key milestone date "of what they're working towards". The due-date half is done: DUE-FIELD was decided at 01:43 GMT today and harness `1af72f2e` added the optional `target` mapping (`date`, `kind` of `due` or `milestone`, `what`) to the `ki-work-roadmap` format standard, with the nearer date ordering work within one horizon and priority. The assessment half is not. Personal's prototype tests each record against eight ordered criteria, `no-owner-judgement`, `no-outward-act`, `one-repo-authority`, `reversible`, `self-verifiable`, `unblocked`, `scoped` and `agent-step`, the first failure deciding `unattended`, `near-miss` with one question, or `attended`; across 76 open Personal records it found 9, 21 and 46. Each criterion cites an existing rule rather than restating one, and eligibility is not authority. The open query UNATTENDED-FIELD asks only where a verdict is recorded (a record mapping or a per-window note) and bundles the criteria into that choice; the Codex blind review that kept it at medium asked for the criteria to be reviewed before they are standardised. Today `ki-delegation`'s unattended deny list says what a window never does and `ki-coordination`'s unattended windows section says what a coordinator may progress, but neither says how a record is judged eligible, and the format standard states "No unattended-eligibility field is adopted".

**Query:** Should the eight criteria, in their order with the three outcomes, become the eligibility assessment in `ki-delegation`, leaving UNATTENDED-FIELD to decide only where the verdict is recorded?

**Options:**

a) (recommended, confidence medium - the criteria sorted 76 real records cleanly and rest on rules already in the standards, but they have run on one territory and one review asked for scrutiny before standardising) Adopt them into `ki-delegation` beside the unattended deny list as the assessment every window plan uses, with a harness run writing them and the field question staying with UNATTENDED-FIELD.

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

a) (recommended, confidence medium - neither outage is cured by launchd, one being a usage limit and the other a blocked turn, yet it is the only wake that survives a quit and HNR's deploys wait on it) Lift the deferral in order: Ways of working writes the headless-pass contract (what a pass may do, its budget, its report) into `ki-coordination`, then sends the launchd job as a line to ki.chezmoi and ki.mac-studio-setup.

b) Keep the 23 October order: session-only wakes with stop words, revisit after the usage-limit and blocked-turn causes are addressed.

c) Build the launchd job first and write the contract from what it needs.

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

a) (recommended, confidence medium - it generalises the deny list's publication ban to attended turns, but the three platforms and the line between a draft and a change others see want Kris's wording) Confirm it: in Linear, Notion and Slack an agent drafts and Kris sends, publishes or moves state, written into `ki-delegation`'s authority tiers beside the publication ban.

b) Confirm it for HNR only, in hnr-principal's AGENTS.md.

c) Not a rule: the publication ban is enough.

### UNWRITTEN-RULES-CONFIDENTIAL - a confidential site is never made public

**Context:** The fourth HNR rule. Today no standard says it: the deny list bars "new publication" in a window and the privacy rules in `ki-diagrams` and the work-package standard bar private names in committed files, but nothing bars changing a confidential site's visibility, which cannot be undone once crawled.

**Query:** Should the rule be confirmed as standing, in general form?

**Options:**

a) (recommended, confidence high - an irreversible disclosure with no reading under which it should happen unasked) Confirm it in general form: a site, repository or note marked confidential is never made public without Kris's go, written into `ki-delegation`'s authority tiers, with HNR's list of confidential sites in hnr-principal's AGENTS.md.

b) Confirm it for HNR's sites only, in hnr-principal's AGENTS.md.

c) Not a rule.

### SIZE-LABEL - land the T-shirt display convention now

**Context:** Decided in substance. Kris, 24 October 08:42 BST: "I wonder if there's a way of showing T-shirt S, M, etc. next to it. And probably put it in a capital letter, almost like it's a label on a t-shirt." Under VA-HIGH a) on 25 October he sent it here as a message, read back as "TENDING-FOLD, SIZE-LABEL and PRODUCT-RECORDS go to their owning works tonight as messages". Today `ki-work-roadmap`'s Priority and size section defines `size` as `s`, `m`, `l` or `xl`, with `xl` split before Ready and no `xs`, and says nothing about display; Valle Armonia already shows 👕 S, 👕 M, 👕 L and 👕 XL in reports and messages, and one record was labelled 👕 XS against the vocabulary. The change is one paragraph: a display convention of 👕 plus the capital letter in reports and messages, field values unchanged, no XS. The deny list keeps standard changes out of tonight's window.

**Query:** Should it land now, and in which run?

**Options:**

a) (recommended, confidence high - decided, one paragraph, and WORK-LABEL is the same kind of change in the same repository) Land it on return in one harness run together with WORK-LABEL, the run's tests covering both.

b) Land it on return as a run of its own.

c) Hold it for the next harness batch.

### WORK-LABEL - name every piece of work as label then id

**Context:** Decided in substance. Kris, 25 October, on "Personal > Tower (personal.regular.tower)": "I like this label, the way that you put the work package in brackets after it at the end. Can we adopt that as a standard?" Today `ki-coordination`'s Work naming gives each work an id, slug and title, the label being the title plus a host suffix only where the work is limited to one machine, and the `<label> (<id>)` form appears only in the coordinator's closing thread line; the message sender label is `<Territory> > SoP:` with no id; regular and ad hoc work carry no thread line, so a regular thread had no settled way to name itself. The change: `ki-coordination` names `<label> (<id>)` as the work name used wherever a session names a piece of work, in replies, reports, message sender labels, hand-offs and openers, and the `ki-work-package` message line form gains the id after the sender label.

**Query:** Should it land now, and in which run?

**Options:**

a) (recommended, confidence high - decided, two short edits in the harness, and SIZE-LABEL shares the run) Land it on return in the one harness run with SIZE-LABEL, with a REFRESH line to live works afterwards.

b) Land it on return as a run of its own.

c) Land only the `ki-coordination` naming rule now and leave the message line form as it is.

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
