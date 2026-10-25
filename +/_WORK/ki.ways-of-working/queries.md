# ki.ways-of-working queries

## Open

### DRAIN-END - should an explicit drain check end with its DRAINED / NOT DRAINED line?

**Context:** When you asked a coordinator to drain, a prompt that put a final DRAINED / NOT DRAINED line last worked well; the standard requires every banner to end with the thread line. The coordination-lessons proposal and a blind review disagree. Nothing changes until you decide.

The proposal's view: put the DRAINED / NOT DRAINED line after the thread line, only for an explicit drain check, honouring the ending you asked for.

**Query:** Should an explicitly requested drain check end with the drain result after the thread line?

**Options:**

a) (recommended, confidence high - reviewed; one closing rule everywhere, no exception to maintain) Keep the thread line last in every case and put the drain result in Done.

b) Put the DRAINED / NOT DRAINED line after the thread line, only for an explicit drain check.

### SORT-ARM - cancel the conditional ARM Linux release record [KI-TOOL-KI-CLI-125](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-125-ki-release-contract.md)

**Context:** The record is held until an ARM Linux host is needed; vega is x86 and sol is macOS arm64, both already covered by release archives, and no ARM Linux host exists or is planned. It also carries a reusable release-contract requirement (per-platform archives, checksum manifest, signature, embedded installer key). The roadmap sort proposed cancelling it; a masked blind review agreed at high confidence, noting your 20 October review chose to keep it held.

**Query:** Should the record be cancelled, with ARM Linux kept as an Agent host Idea and the release-contract requirement kept as a short section in the tools-ki release guide?

**Options:**

a) (recommended, confidence high - reviewed; current hosts are covered and the requirement survives in the guide) Cancel it, add the ARM Linux Idea under the Agent host and the contract section to the release guide.

b) Keep it held until an ARM Linux host is needed.

### THREAD-RENAME - name each coordination thread at launch, and say so in the bootstrap report

**Context:** Kris asked for a bootstrapped thread to get a good name, or failing that for the report to say how. Claude Code's `--name` flag names a session at launch, but a running session cannot rename itself. A `/rename` line in a report breaks the current rule against paste instructions in reports. Kris wants this before KI > SoP bootstraps on Sol.

**Query:** Should openers launch with `--name`, with bootstrap and re-bootstrap reports also carrying one `Rename this thread: /rename <label> (<id>)` line as a named exception?

**Options:**

a) (recommended, confidence high - reviewed; launch naming alone leaves pasted openers unnamed, and one narrow rename line does not reopen the ban on send or resume prompts) Launch openers with `claude --name "<label> (<id>)"`, and add the rename line to bootstrap and re-bootstrap reports only.

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

A masked blind review on Codex disagreed: it would keep drain only inside hold, because the Work Process note defines drain as the activity leading into On hold and a standalone drain needs its own contract first.

**Query:** Should the skill gain `hold`, `drain`, `resume`, `send` and `receive`, with `drain` usable on its own?

**Options:**

a) (recommended, confidence medium - review disagrees; it gives you the drain word and needs no Work Process change) Add all five, where `hold` is drain plus On hold and `drain` alone stops launches and reports when everything has finished.

b) Add `hold`, `resume`, `send` and `receive`, with drain only ever part of hold.

### RUN-SECRETS - runs read secrets only through the dotfiles helpers

**Context:** Kris approved the 1Password cache ("I really need the OP cache doing") and said Cloudflare access "should be uniform across whichever territory I'm working in". The proposals are:

- runs read 1Password only through `op_cache`, in service-account-only mode;
- runs read Cloudflare credentials only through `~/bin/cf_token`;
- no territory's notes record item or token ids.

A sweep found no such ids in Knowledge Islands.

Update, 25 October: wow-method-lines found the 1Password half already landed, so only the Cloudflare half is still to decide.

**Query:** Should the background-run standard and the Cloudflare site rubric adopt this one secrets rule?

**Options:**

a) (recommended, confidence high - follows Kris's words; both helpers exist in chezmoi, and nothing currently breaks it) Adopt it in `ki-delegation` and `ki-repo-website-cloudflare` together.

b) Adopt the 1Password half now and the Cloudflare half once the Cloudflare guide is reviewed.

### THEME-CLOSE - set the date Initiatives stop being accepted

**Context:** Kris asked that the theme registry be used everywhere and "enforced mechanically now". Checkers still only warn on `Streams/Initiatives/` and `initiative:`, and the tolerance window has no end date. Personal has migrated. Legal still has 7 Initiative files and no Themes folder, and HNR has one `initiative:` field. Failing now would break both audits.

**Query:** Should Legal and HNR be asked to migrate, with the checkers failing from a fixed date?

**Options:**

a) (recommended, confidence high - reviewed; a dated cutover ends open-ended tolerance without breaking Legal's and HNR's audits at once) Message Legal's and HNR's States of play now, and turn the warnings into failures on 7 November 2026, or earlier once a scan finds no residue.

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

### PROXY-SHAPER - the Headroom output shaper and compression in coordinator sessions

**Context:** The proxy appends an L2 steering block ("Never restate ... reference them by path and line instead") at the end of every system prompt, after the style. That conflicts with restating open queries in full, and the style already says no proxy shaping block shortens a report. Token mode also strips function words from Bash tool output, which corrupts templates read that way; Read-tool output arrived intact in this run. The Headroom proxy is connection-critical, so any change to it needs a tested restore path.

A masked blind review on Codex disagreed at high confidence: a style file cannot reliably override a conflicting system instruction, so it would turn the output shaper off for Claude Code through chezmoi, in a separately authorised run with a tested restore path, and verify repeated open queries and intact reads before finishing.

**Query:** Should the proxy stay as it is, with the read path fixed in the standard instead?

**Options:**

a) (recommended, confidence medium - review disagrees; no change to a connection-critical service, and the style's override held for the 21:53 Summary; the 23:20 link to the proxy is inferred) Leave Headroom unchanged; add to the standard's Bootstrap and Re-anchoring that the standard, style and package are read with the file-read tool, not the shell; the style names the shaper's "never restate" as overridden for open queries.

b) Turn the output shaper off for Claude Code (`HEADROOM_OUTPUT_SHAPER=0`, managed in chezmoi) under a run with a tested restore path.

### METHOD-NUDGE - warn when a coordinator's method_read lags

**Context:** At re-bootstrap the coordinator read harness revision 111b853a against `method_read: eff6163b`, 27 commits behind, but did not re-read the standard, update `method_read` or tell you what changed. Nothing mechanical catches this; the rubric says it cannot judge whether a coordinator refreshed.

**Query:** Should the coordinator hook print one warning line when the work's `state.md` `method_read` differs from the harness revision?

**Options:**

a) (recommended, confidence high - reviewed; one cheap advisory line makes a skipped refresh visible, comparing the method revision rather than harness HEAD, and only a real re-read updates `method_read`) Add the check to `hooks/coordinator-reminder.sh`, naming both revisions.

b) Leave it to coordinator habit and the bootstrap rule.

### REVIEW-CHECK - flag a query with two recommended options

**Context:** In the 21:53 Summary, COORD-COMMANDS and DRAIN-END each carried two "recommended by ..." options with two confidences, against the query-review rule: one recommended a), with its reason starting `review disagrees` and the reviewer's view in Context. Rubric item COORD-11 already checks confidence on recommended lines.

**Query:** Should COORD-11 also warn when a query carries more than one `(recommended` option?

**Options:**

a) (recommended, confidence high - a narrow warning beside an existing check, easily reversed) Extend COORD-11 to warn on a second recommended option in one query.

b) Leave it to coordinator habit.

### COMMIT-CADENCE - commit the work folder at every write and every wake

**Context:** You said on 25 October that work sits uncommitted in the work folder for a long time, which makes it hard to keep repositories in sync with the remote and with the other sessions that write into work packages. Today the standard requires a commit and push only at a send, an owner receive, a mark, a hold and finish, so message dispositions, queries, decisions, briefs, state changes and heartbeat wakes go uncommitted. The coordinator already works this way as a habit since 01:34 BST; this makes it the rule. The push half is PACKAGE-PUSH below. A masked blind review on Codex agreed, and both model-shape reviews corrected the pull: the standard allows only a fast-forward pull into a clean checkout, since a rebase refuses a dirty shared tree and autostash would touch another session's files. The unit committed is the smallest complete, verified one, and a clean wake makes no empty commit.

**Query:** Should the standard, the output style and the hook line require a commit by explicit path at every work-folder write and every wake, pulling with rebase first and pushing fast-forward, so no write stays uncommitted past the turn that made it?

**Options:**

a) (recommended, confidence high - reviewed; it closes the gap that leaves shared packages stale, with no new authority) Adopt the cadence: commit each complete unit by explicit path before the turn ends, pull fast-forward only into a clean checkout, commit a line written into other work's `messages.md` at once, and keep publication under the push rule.

b) Leave the send, receive, mark and hold cadence as it is.

### PACKAGE-PUSH - push other sessions' work-folder commits stacked beneath your own

**Context:** You set on 14 October that a session pushes only when its own commits alone are stacked, and on 19 October that it never pushes another session's stacked commits. In a Capital those are nearly always other sessions' `+/_WORK/` commits, such as a `messages.md` line routed here, so the coordinator's push stalls until you push by hand. Your 14 October words allow pushing stacked commits a session is confident in and flagging the rest. The reviews disagree. The cadence blind review on Codex agreed, provided the session inspects every unpublished commit's changed paths, renames included, and stops on divergence or doubt. The Codex model-shape review rejected a push allowed by path alone, at high confidence, because briefs and decisions under `+/_WORK/` can carry unreviewed material, and asked for a bounded grant naming the publisher, repositories, branches and the check of each commit beneath. The Claude model-shape review agreed with the narrow exception but noted it does nothing while any product commit lies beneath, so it pairs it with each session pushing its own product commits at once, which your 14 October words already allow.

**Query:** May a session push a fast-forward stack in which other sessions' commits touch only `+/_WORK/` paths, keeping the own-commits-only rule for every other stacked commit?

**Options:**

a) (recommended, confidence medium - reviews disagree; a bounded grant removes the stall while answering the unreviewed-material concern) Yes, as a bounded grant: only this repository's coordinators, only `main` of the Capital, only when every other session's stacked commit touches `+/_WORK/` alone, each commit's paths checked, fast-forward only and never forced, with each session pushing its own product commits at once.

c) Yes, by path alone, with no named publisher or branch.

b) No, keep own-commits-only pushing and rely on COMMIT-CADENCE alone.

### CASCADE-STEWARD - a State of play looks after a Project package by explicit assignment and handover

**Context:** Kris wants one State of play thread to keep every Project package in its territory sorted unless the Project has its own coordination thread. The brief made the State of play the steward automatically whenever no thread is open, with a one-day flag on a quiet thread. The Codex review differs: nothing committed or local can show that a thread is alive, so inferring stewardship from an absent thread risks two writers or none. It wants an explicit assignment that changes only by an acknowledged handover, which stops the old steward, passes its runs in flight to the new one and is committed in one write. The Claude review agrees the State of play should steward by default, and it independently adds the same handover of runs in flight. Both drop the one-day flag, which would fire on a Project that is simply waiting on Kris. Both limit package creation to a registered Project within the cap, created in the state its actual move supports rather than `with-worker` by default.

**Query:** Should a State of play steward a Project package by an explicit committed assignment, set when it creates or adopts the package and changed only by an acknowledged handover when Kris opens or closes the Project's own thread?

**Options:**

a) (recommended, confidence high - reviews disagree on inferring stewardship from an absent thread; the state and session contracts give no liveness signal, and explicit assignment keeps the default Kris asked for) Yes: explicit assignment, acknowledged handover with runs in flight, no timeout takeover, creation only for a registered Project within the cap.

b) Infer it, as the brief proposed: the State of play steps in whenever no Project thread is open, with a flag on a quiet thread.

### STEWARD-FIELD - where a package records who looks after it

**Context:** The assignment needs a committed home that names a work, never a host or session. The brief proposed a new `state.md` field, `steward: self` or `steward: work/<sop id>`. Both reviews reject `self`, which is not a holder value, and both reject reading the assignment as the holder. The Claude review would reuse `work.md`'s existing `worker` field: `worker: work/va` when the State of play looks after the package, and `agent` when the Project's own thread does. That adds no field and leaves the closed field set unchanged. Stewardship changes only when Kris opens or closes a thread, the slow rate `work.md` suits, and the holder stays derived from `state` and `worker` as today. The Codex review wants a dedicated assignment with its own vocabulary, distinct from holder and session, and leaves the exact field to the design. A separate field keeps the assignment visible beside the state, and it avoids a third sense of "steward" only if it is named with care.

**Query:** Should the assignment be recorded in a new dedicated field rather than `work.md`'s existing `worker` field?

**Options:**

a) (recommended, confidence medium - reviews disagree; the Codex review and a masked blind review on Codex want a dedicated field, as lasting responsibility should not share a field with the holder that pick-up reads, while the Claude review prefers reusing `worker` as it adds no field) A new dedicated field, taking `work/<id>` values only, never `self`, changed or removed as part of the acknowledged handover.

b) Reuse `work.md`'s `worker`: `worker: work/<sop id>` while the State of play looks after the package, `agent` while its own thread does.

### CASCADE-REPORT - one Summary for several packages

**Context:** When the State of play thread works several Project packages, Kris still gets one Summary from it. Both reviews agree with the brief that each item names its package, each query lives in its Project's `queries.md` and Kris's answer is logged in that Project's `decisions.md`, so any package can be picked up alone. Codex adds three points. Two packages may use the same tag, so a query is named by work and tag. Each package keeps its own state, mark and beat, so a territory mark, or Kris's acknowledgement of the Summary, moves only the work it clearly names. A decision spanning Projects is kept once at the territory, not copied as several grants. Claude adds that the five-call turn budget reads "the work package", singular, so a State of play turn should act in one package at a time and roll the rest up from `ki work status`.

**Query:** Should the State of play's Summary report each package as its own work, with work-qualified query tags, per-package marks and one package acted on per turn?

**Options:**

a) (recommended, confidence high - both reviews agree, and it keeps today's rule that queries and decisions live in the package) Yes, with all four additions.

b) One Summary as the brief proposed, without per-package marks or the one-package turn.

### RELATIONS - what a package and a record say they relate to

**Context:** Kris asked that the metadata say what each piece of work is related to. Both reviews agree that every package below the main should name the State of play that coordinates it as `parent`, so a package read alone shows its territory, Project, theme and coordinator. For ad hoc work, `parent` means the coordinating State of play, not the regular-work parent its id nests under. The brief would then derive a secondary's `covers` list from those `parent` fields and retire it. Both reviews reject that, for two reasons: coverage of a registered Project must hold before its package exists and after it is pruned, and a coverage change would become a write to every moved Project's file instead of one commit in the main's. On records, both agree that a record's `project` field finds its package through the registry. Codex notes it authorises nothing: selection into `now` neither opens work nor grants execution, the steward writes the link into its next steps, and a record with no `project` goes first to its existing owner, such as regular work, before State of play routes it.

**Query:** Should every package below the main carry `parent`, with `covers` kept as the main's register and checked against it, and a record's `project` used only to find its package?

**Options:**

a) (recommended, confidence high - both reviews agree; it answers Kris's metadata ask without losing coverage of Projects that have no package) Yes.

b) As the brief proposed: `covers` derived from `parent` and retired after a tolerance window.

### HOST-SEAT - committed host requirements, never a committed seat

**Context:** Kris asked that coordinators know which machine they run on, so that work aimed at particular machines can be handled. The work-package standard contradicts itself: it says a package names "no host", yet it allows a `(<host>)` label suffix for machine-limited work. Both reviews agree with the brief's resolution. The prohibition protects a thread's seat, meaning where it runs and will resume; that goes stale at every move, so it stays out of every package, hold and report. A requirement, meaning a host or category the work needs, is a fact about the work and may sit on a message line, a brief, a record or a package's label. Both want host and category names taken from the territory's machine inventory, which Rig owns for Knowledge Islands. Claude adds that the coordinator should map the local machine to that inventory rather than trust raw `hostname -s`, whose result on a Mac depends on network settings.

**Query:** Should the no-host rule narrow to the seat, allowing a host or category requirement on a line, brief, record or label, with each coordinator establishing its host from the machine inventory at bootstrap and re-anchoring?

**Options:**

a) (recommended, confidence high - both reviews agree, and it resolves a contradiction in the standard by narrowing rather than deleting the rule) Yes.

b) Keep the blanket no-host rule and drop the label suffix.

### HOST-TARGET - what a host requirement restricts

**Context:** Once requirements are allowed, a coordinator on one machine will meet lines meant for another. The brief and the Claude review would have a thread act only on lines that are untagged or tagged for its own host or category, leave the rest queued and count them in its banner. Claude adds an age flag, so that a line no live thread can take does not wait unseen. The Codex review differs: only device-dependent execution needs the device, so a coordinator elsewhere may still acknowledge the line, plan it, ask Kris about it or dispatch a run to an eligible host. A blanket skip also breaks the queue's order when the first line, or an IMPORTANT line, is for another host. Codex also wants concrete hosts told apart from categories, and rules for unknown or renamed names, before the syntax is adopted. Both agree the syntax is an optional `@<host or category>` after the date, and that the pilot runs in `ki.chezmoi`.

**Query:** Should a host requirement restrict only device-dependent execution, leaving any coordinator free to acknowledge, plan, ask about or dispatch the line in queue order?

**Options:**

a) (recommended, confidence high - reviewed; a masked blind review on Codex agreed that restricting execution only keeps queue order and IMPORTANT lines intact, adding that the pending execution or handover is recorded durably and acknowledgement never counts as completion) Yes, with an age flag on lines no eligible host has taken, and host-versus-category rules settled before adoption.

b) A thread acts only on lines for its own host or category and leaves the rest queued and counted, as the brief proposed.

### KI-REPO-HOME - which work carries `ki-repo` standard and checker changes

**Context:** State of play queued REPO-METADATA's `ki-repo` change with ki.baseline-rollout: the hyphen-only `ki-` topics and the `territory_code` and `territory_tag_types` keys. That work's `work.md`, however, puts "harness skills and standards" out of its scope and gives them to ki.ways-of-working. This work's own scope covers the work model, coordination, delegation and work-record standards, not repository metadata. Wording for the 24-character `repo_code` cap, from PERSONAL-RESERVED, would ride with whichever work carries the `ki-repo` change. Personal has already shortened its two site codes, so nothing is blocked.

**Query:** Should ki.baseline-rollout carry `ki-repo` standard and checker changes, with its Out line narrowed to the work-model skills?

**Options:**

a) (recommended, confidence medium - needs blind review; repository metadata is baseline conformance across every repository, and State of play already routed it there) ki.baseline-rollout carries the `ki-repo` change, the repo-code cap wording included, and its `work.md` Out line reads "work-model harness skills and standards (ki.ways-of-working)".

b) ki.ways-of-working carries it, and its scope widens to `ki-repo`'s repository contract.

### LEGACY-PREFIX - how a `repo_code` rename passes the streams and roadmap audits

**Context:** the `ki-repo-kb-streams` streams audit and `ki-work-roadmap`'s checks fail every record not prefixed with the current `repo_code`. A rename therefore has to happen in one sweep, or the repository fails its audit until every record has moved. Personal is renaming KB to PERSONAL that way now. An allowance, an optional list of former codes that existing records may keep while new records take the new code, would allow a gradual path. It would need both checkers and the tools-ki readers to change.

**Query:** Should a `repo_code` rename stay a one-sweep change, written into `ki-work-roadmap`, rather than gaining a legacy-prefix allowance?

**Options:**

a) (recommended, confidence medium - needs blind review; renames are rare and Personal's runs as one sweep, so documenting the sweep costs one paragraph where the allowance costs two checkers and tools-ki) Write the rename into `ki-work-roadmap` as one sweep: every record and in-repository reference in one commit, pruned links keeping their pinned revisions.

b) Add an optional legacy-prefix list accepted by both audits for existing records only, with new records required to use the current code.

### PARTIAL-REPOS - how a repository with only Pillars and Resources fits the model

**Context:** HNR keeps hnr-shared, which holds only Pillars and Resources, beside hnr-principal. ZONE-1 requires all five zones, and the registry binds one source store per declared repository, so hnr-shared cannot be declared. Its store is written up only in tracked notes, so `ki repo store` and the source audits do not see it. Kris asked Knowledge Islands to decide where partial repositories fit, and whether a person keeps a personal "work" knowledge base beside a person-agnostic company Capital, adding: "there's [a] kind [of] weird thing here we maybe need to come back to." The question reaches the Structure note, `ki-repo-kb` and tools-ki, beyond this work's method scope.

**Query:** Should PARTIAL-REPOS wait as an idea until Kris opens it, rather than starting a design now?

**Options:**

a) (recommended, confidence medium - needs blind review; Kris's own words defer it, and nothing is broken beyond HNR's tracked-notes workaround) Record it as an idea on the Ways of working Project note with the HNR evidence linked, and start a `ki-work-design` brief when Kris opens it.

b) Start a `ki-work-design` brief now covering partial repositories, the personal "work" knowledge base and the store-binding gap.

## Parked

- RIG-ATTENDED - Kris's attended Rig steps on sol and terra, commands in `/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-rig-attended-steps.report.md`; recommended a) CORE-069 on sol plus the look-only CORE-047 and CORE-062 checks first, CORE-068 and the live firewall rollout in a later sitting. Kris, 2026-10-22 02:26 BST: walk me through it in the morning. The tools-rig v0.8.0 tag waits on the same review gates (RIG-RELEASE-REVIEW-BOUNDARY a), 2026-10-23).
