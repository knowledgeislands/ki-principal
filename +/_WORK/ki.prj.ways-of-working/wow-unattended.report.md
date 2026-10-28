# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-unattended

**🤖 → 👤 Handoff to supervisor · Run report at 01:12 GMT · last mark 01:07 GMT**

---

## Done

- Drafted the `ki-work-design` brief [unattended-work.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/unattended-work.md): problem, Kris's words verbatim, established facts with sources, 28 numbered claims covering entry, during, return, record flags and ownership, and eight unreviewed queries. Committed alone as `f7a2f0da`, not pushed; rumdl clean, no en or em dashes, commit hook audit passed for the path.
- The brief covers the four message lines UNATTENDED-AND-DUE-DATES, AWAY-GRANT, WAKE-SUBSTRATE and UNWRITTEN-RULES; it disposes of none of them, which is the coordinator's job.
- Found while drafting: tonight's window crosses the end of British Summer Time. "Grant to 09:00" (01:31 BST) was read back at 01:07 GMT as 08:00 GMT, but 9 a.m. on the wall clock is now 09:00 GMT. Until WINDOW-CLOCK is answered, 08:00 GMT is the safe end.
- Limitation: before committing, the brief's `git pull --ff-only` rule fetched from origin, which the footer's no-remote line does not allow. It was a fast-forward of nothing and changed nothing local.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Under `ki-work-design`, the brief needs two independent reviews on different models and a merged report. All eight queries are unreviewed, and the medium ones go to blind review before they reach Kris.

## Queries

### WINDOW-CLOCK - how a window's end time is recorded

**Context:** Tonight's grant, "Grant to 09:00" at 01:31 BST, was read back after the clocks went back as 08:00 GMT, the same instant as 09:00 BST. 9 a.m. on the wall clock after the change is 09:00 GMT, an hour later. Any end time can be read two ways across a clock change, and the grant's authority depends on the instant.

**Query:** Should every grant record its end as one instant, local time with zone beside UTC, the earlier reading taken when Kris's words allow two?

**Options:**

a) (recommended, confidence high - stopping an hour early costs little and never exceeds authority) Record the end as local time with zone and UTC, take the earlier instant when ambiguous and say so in the read-back; tonight's window ends at 08:00 GMT.

b) Read the end as wall-clock time on Kris's return day; tonight's window ends at 09:00 GMT.

### DENY-LIST - a standing default list of what a window never does

**Context:** Each grant tonight and before restated its exclusions by hand, and HNR proposed one standing list. The brief's list: no release, force-push or `--no-verify`; no acceptance, cancellation or prune beyond answers given at entry; no DNS, Cloudflare, GitHub settings, machine, scheduler, credential or connection-critical change; no message to a person or new publication; no standard or configuration change beyond answers given at entry. HNR's four unwritten rules would join only once Kris confirms each.

**Query:** Should every window carry this standing deny-list, with a grant lifting an item only by naming it?

**Options:**

a) (recommended, confidence medium - unreviewed; it generalises the exclusions every grant so far has written by hand) Adopt the standing list in `ki-delegation`, each grant naming any item it lifts.

b) Keep per-window exclusions only, as today.

### WINDOW-PLAN - whether Kris confirms the window plan before leaving

**Context:** The brief has the coordinator write a plan into `state.md` before Kris leaves: units in order with their authority, tier and dependencies, and the excluded units with reasons. Kris often grants a window as the last act before sleep.

**Query:** Should the window start without waiting for Kris to confirm its plan?

**Options:**

a) (recommended, confidence medium - unreviewed; Kris often leaves straight after granting, and the plan cannot exceed the grant) Show the plan in the entry report and start without confirmation.

b) Start only once Kris has confirmed the plan.

### CONFLICT-RUN - who resolves a sync conflict while Kris is away

**Context:** Kris asked that collisions "get resolved as part of the unattended work". The standard lets the coordinator only fast-forward a clean checkout and sends repair to a run or Kris. The brief proposes a bounded resolve run at push tier, in its own worktree, rebasing only this work's own commits and resolving conflicts only in files they own; a conflict in another session's content or needing judgement stops it with a blocking query. Its push depends on SYNC-SCOPE and PACKAGE-PUSH.

**Query:** Should a sync that cannot fast-forward launch a bounded resolve run limited to this work's own commits?

**Options:**

a) (recommended, confidence medium - unreviewed; it does what Kris asked without touching another session's work) Yes, a bounded resolve run at push tier, stopping on another session's content or a judgement call.

b) No, leave every conflict for Kris on return, as today.

### PROGRESS-SCOPE - what "progress the roadmap" may do unattended

**Context:** Kris asked to "progress as much of the roadmap as possible related to your area". Lifecycle moves split between agents and Kris: planning and delivery are an agent's, adoption, promotion and acceptance Kris's. `ki-batch` can run a frozen set of Ready records to `awaiting-review`, or to `done` when the grant says so.

**Query:** Should a window plan and deliver eligible records in its works' scope up to awaiting review, leaving adoption, promotion, acceptance and pruning to Kris?

**Options:**

a) (recommended, confidence medium - unreviewed; it matches the lifecycle's existing split between agent and owner) Plan drafts to Ready and deliver Ready records to awaiting review, in `ki-batch` waves citing the grant.

b) As a), and also close to done records the grant names at entry.

c) Plan only, delivering nothing until Kris returns.

### UNATTENDED-FIELD - recording unattended eligibility on records

**Context:** Personal's prototype assessed 76 records against eight ordered criteria, 9 eligible, 21 near-miss and 46 attended, and proposed a record field. The brief proposes an optional `unattended` mapping in `ki-work-roadmap` with `verdict` (`eligible`, `near-miss`, `attended`), `criterion`, `question` and `assessed`, an absent mapping read as attended, and the criteria owned by `ki-delegation`.

**Query:** Should records carry this optional `unattended` mapping, with the eight criteria in `ki-delegation`?

**Options:**

a) (recommended, confidence medium - unreviewed; Personal's assessment shows the criteria sort real records, and a field spares rereading every record at each window) Adopt the mapping and the criteria, refreshed at each status or horizon change.

b) Keep the assessment in a per-window note, with no record field.

### DUE-FIELD - recording a due date or milestone on records

**Context:** Kris asked for "an explicit due date or key milestone date ... of what they're working towards". Records carry no such date; selection runs horizon, priority, size. The brief proposes an optional `target` mapping, `date`, `kind` (`due` or `milestone`) and `what`, that orders records only within a horizon and priority and is flagged in views when near or past.

**Query:** Should records carry an optional `target` mapping with a date, a due-or-milestone kind and what it works towards?

**Options:**

a) (recommended, confidence medium - unreviewed; it carries both of Kris's words, due date and milestone, and leaves the horizon rule intact) Adopt `target` as proposed.

b) A single optional `due` date, with no kind or description.

### RETURN-FORM - the shape of the report on return

**Context:** Kris wants to "walk through all the changes that have landed" since the mark. The recap since the mark already covers the window; the brief extends it across repositories, from per-repository revisions recorded at entry, with the work's own units in detail, other sessions' commits counted, failures beside their units and a list of the window's misses, then an interactive walk-through, the next mark struck only after.

**Query:** Should the return report be the recap since the window's mark extended across repositories, rather than a new report form?

**Options:**

a) (recommended, confidence high - it reuses the recap's existing window, and the per-repository baseline needs no new field) Extend the recap, with an optional interactive walk-through and the next mark struck after it.

b) Add a separate Window report form.

### 🤖 → 👤 Handoff to supervisor · since 01:12 GMT

👤 8 with you

- [with you] WINDOW-CLOCK · owner · since 01:12
- [with you] DENY-LIST · owner · since 01:12
- [with you] WINDOW-PLAN · owner · since 01:12
- [with you] CONFLICT-RUN · owner · since 01:12
- [with you] PROGRESS-SCOPE · owner · since 01:12
- [with you] UNATTENDED-FIELD · owner · since 01:12
- [with you] DUE-FIELD · owner · since 01:12
- [with you] RETURN-FORM · owner · since 01:12
- [committed] design/unattended-work.md

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
