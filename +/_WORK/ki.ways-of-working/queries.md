# ki.ways-of-working queries

## Open

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

a) (recommended, confidence high - reviewed; a masked blind review on Codex agreed, as repository conformance fits Baseline rollout's outcome and keeps this work's method boundary; repository metadata is baseline conformance across every repository, and State of play already routed it there) ki.baseline-rollout carries the `ki-repo` change, the repo-code cap wording included, and its `work.md` Out line reads "work-model harness skills and standards (ki.ways-of-working)".

b) ki.ways-of-working carries it, and its scope widens to `ki-repo`'s repository contract.

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

## Parked

- PROXY-SHAPER - the Headroom shaper's "never restate" block and Bash compression in coordinator sessions; recommended a) leave the proxy and fix the read path in the standard, medium, review disagrees (Codex would turn the shaper off through chezmoi with a tested restore path). Kris, 2026-10-25: "I'm not really sure what to do about this one ... Maybe it's something we can come back to."
- RIG-ATTENDED - Kris's attended Rig steps on sol and terra, commands in `/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-rig-attended-steps.report.md`; recommended a) CORE-069 on sol plus the look-only CORE-047 and CORE-062 checks first, CORE-068 and the live firewall rollout in a later sitting. Kris, 2026-10-22 02:26 BST: walk me through it in the morning. The tools-rig v0.8.0 tag waits on the same review gates (RIG-RELEASE-REVIEW-BOUNDARY a), 2026-10-23).
