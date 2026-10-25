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

### MEMBER-PACKAGE - a member repository's own regular work

**Context:** [personal.regular.acquire-intake](/Users/krisbrown/workspaces/personal/acquire/+/_WORK/personal.regular.acquire-intake/work.md) is a package held in the member repository `personal/acquire`, not in the Capital. The rubric bars only territory work outside a Capital, so this is allowed but undeclared anywhere. It is the only such case found. This query has not had a blind review.

**Query:** May a member repository hold a package for its own regular work, provided its `work.md` declares it as such?

**Options:**

a) (recommended, confidence high - reviewed; a masked blind review on Codex agreed, as it follows the existing split between regular work and coordination, with Project and territory work staying in the Capital; one case only, and regular work naturally sits with the code it runs against, but the pattern is unproven) Allow it for regular work only, declared in `work.md`; Project and territory work stay in the Capital.

b) Move every package into the Capital, including regular work.

### DENY-LIST - a standing default list of what a window never does

**Context:** Each grant tonight and before restated its exclusions by hand, and HNR proposed one standing list. The brief's list: no release, force-push or `--no-verify`; no acceptance, cancellation or prune beyond answers given at entry; no DNS, Cloudflare, GitHub settings, machine, scheduler, credential or connection-critical change; no message to a person or new publication; no standard or configuration change beyond answers given at entry. HNR's four unwritten rules would join only once Kris confirms each.

**Query:** Should every window carry this standing deny-list, with a grant lifting an item only by naming it?

**Options:**

a) (recommended, confidence high - reviewed; a masked blind review on Codex agreed that a common baseline reduces omissions; it generalises the exclusions every grant so far has written by hand) Adopt the standing list in `ki-delegation`, each grant naming any item it lifts; force-push and `--no-verify` stay prohibited, and none of the four unconfirmed HNR rules is added without confirmation.

b) Keep per-window exclusions only, as today.

### WINDOW-PLAN - whether Kris confirms the window plan before leaving

**Context:** The brief has the coordinator write a plan into `state.md` before Kris leaves: units in order with their authority, tier and dependencies, and the excluded units with reasons. Kris often grants a window as the last act before sleep.

**Query:** Should the window start without waiting for Kris to confirm its plan?

**Options:**

a) (recommended, confidence high - reviewed; a masked blind review on Codex agreed that an explicit bounded grant already authorises the attempt; Kris often leaves straight after granting, and the plan cannot exceed the grant) Show the plan in the entry report and start without confirmation; order, authority, dependencies and exclusions are recorded before implementation, and any unit whose authority still needs a decision is parked.

b) Start only once Kris has confirmed the plan.

### CONFLICT-RUN - who resolves a sync conflict while Kris is away

**Context:** Kris asked that collisions "get resolved as part of the unattended work". The standard lets the coordinator only fast-forward a clean checkout and sends repair to a run or Kris. The brief proposes a bounded resolve run at push tier, in its own worktree, rebasing only this work's own commits and resolving conflicts only in files they own; a conflict in another session's content or needing judgement stops it with a blocking query. Its push depends on SYNC-SCOPE and PACKAGE-PUSH.

**Query:** Should a sync that cannot fast-forward launch a bounded resolve run limited to this work's own commits?

**Options:**

a) (recommended, confidence high - reviewed; a masked blind review on Codex agreed, noting file ownership alone does not prove no other session has content in the file; it does what Kris asked without touching another session's work) Yes, a bounded resolve run at push tier, stopping on another session's content or a judgement call; the run works in its own worktree, rebases only this work's unpublished commits and verifies the result.

b) No, leave every conflict for Kris on return, as today.

### PROGRESS-SCOPE - what "progress the roadmap" may do unattended

**Context:** Kris asked to "progress as much of the roadmap as possible related to your area". Lifecycle moves split between agents and Kris: planning and delivery are an agent's, adoption, promotion and acceptance Kris's. `ki-batch` can run a frozen set of Ready records to `awaiting-review`, or to `done` when the grant says so.

**Query:** Should a window plan and deliver eligible records in its works' scope up to awaiting review, leaving adoption, promotion, acceptance and pruning to Kris?

**Options:**

a) (recommended, confidence high - reviewed; a masked blind review on Codex agreed, as it advances authorised work while keeping the human lifecycle decisions; it matches the lifecycle's existing split between agent and owner) Plan drafts to Ready and deliver Ready records to awaiting review, in `ki-batch` waves citing the grant; each wave is frozen before delivery, dependencies and the owner-queue cap are honoured, and adoption, discretionary promotion, acceptance and pruning stay with Kris.

b) As a), and also close to done records the grant names at entry.

c) Plan only, delivering nothing until Kris returns.

### UNATTENDED-FIELD - recording unattended eligibility on records

**Context:** Personal's prototype assessed 76 records against eight ordered criteria, 9 eligible, 21 near-miss and 46 attended, and proposed a record field. The brief proposes an optional `unattended` mapping in `ki-work-roadmap` with `verdict` (`eligible`, `near-miss`, `attended`), `criterion`, `question` and `assessed`, an absent mapping read as attended, and the criteria owned by `ki-delegation`.

**Query:** Should records carry this optional `unattended` mapping, with the eight criteria in `ki-delegation`?

**Options:**

a) (recommended, confidence medium - reviews disagree; a masked blind review on Codex would keep the assessment in a per-window note with no record field, as eligibility depends on the grant and can go stale, and review the eight criteria before standardising them, while Personal's assessment shows the criteria sort real records, and a field spares rereading every record at each window) Adopt the mapping and the criteria, refreshed at each status or horizon change.

b) Keep the assessment in a per-window note, with no record field.

### DUE-FIELD - recording a due date or milestone on records

**Context:** Kris asked for "an explicit due date or key milestone date ... of what they're working towards". Records carry no such date; selection runs horizon, priority, size. The brief proposes an optional `target` mapping, `date`, `kind` (`due` or `milestone`) and `what`, that orders records only within a horizon and priority and is flagged in views when near or past.

**Query:** Should records carry an optional `target` mapping with a date, a due-or-milestone kind and what it works towards?

**Options:**

a) (recommended, confidence high - reviewed; a masked blind review on Codex agreed, as kind and description make the date meaningful without turning every milestone into a deadline; it carries both of Kris's words, due date and milestone, and leaves the horizon rule intact) Adopt `target` as proposed; `target` orders records within the same horizon and priority after eligibility and dependency checks, and views flag near or past targets without changing lifecycle or horizon.

b) A single optional `due` date, with no kind or description.
