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

### LAUNCH-FIRST - start the first three units from the restart list

**Context:** The restart list recommends tending-fold (design notes only: Tending round 2, the agent-memory overlap, XDG-state and other-territory sections, MOD ledger to 10), coord-standard (one harness change to the standard, skill, style and banner test, after the area 1 answers; THREAD-RENAME may go first) and model-shape (a design brief mapping the single State of play cascade, packages against threads, relationship metadata and host-targeted lines, returning its own queries).

**Query:** Should tending-fold and model-shape start now, and coord-standard once the area 1 queries are answered?

**Options:**

a) (recommended, confidence high - tending-fold and model-shape change no standard, and coord-standard waits for the answers) Start tending-fold and model-shape now, coord-standard after the answers.

b) Start only tending-fold for now.

## Parked

- RIG-ATTENDED - Kris's attended Rig steps on sol and terra, commands in `/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-rig-attended-steps.report.md`; recommended a) CORE-069 on sol plus the look-only CORE-047 and CORE-062 checks first, CORE-068 and the live firewall rollout in a later sitting. Kris, 2026-10-22 02:26 BST: walk me through it in the morning. The tools-rig v0.8.0 tag waits on the same review gates (RIG-RELEASE-REVIEW-BOUNDARY a), 2026-10-23).
