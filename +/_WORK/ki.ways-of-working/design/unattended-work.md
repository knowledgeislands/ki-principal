# Unattended working: brief

**Owner:** Kris · **Owning repository:** knowledgeislands/ki-principal · **Date:** 2026-10-25

**Work:** `ki.ways-of-working`. Status: draft brief, written during the unattended window that opened at 01:07 GMT on 25 October. Reviews and the merged report follow under `ki-work-design`; nothing here changes a standard or grants anything.

## Problem

Unattended windows have run since 21 October on one-off grants, each recorded afresh, with no standing shape for going away, working while away and coming back. The gaps seen so far:

- **No mark at entry.** Until tonight no mark was struck as a window opened, so on return there was no baseline to walk through what landed. Kris: "for unattended periods of time, there's no mark".
- **Packed queries.** A query that bundles several decisions stalls whole while Kris is away, though some of its parts could have been answered and acted on before Kris left.
- **No plan.** Nothing records, at entry, what the window will run, what it will not, and why, so Kris cannot see the window's intent before leaving or measure the outcome against it on return.
- **Drift and late conflicts.** Work sits uncommitted in the work folder, primary checkouts fall behind their remotes, and a collision is found only when someone next pushes. Kris on 25 October: "it's not regularly getting updates, pushes, and pulls."
- **Choosing roadmap work.** No record says whether it may be done unattended, so a coordinator rereads every record to choose, and no record says when it is due or what it is working towards.
- **Wakes fail quietly.** Session wakes are best effort; two outages on 22 October cost wakes, and a missed wake, a usage-limit stop or a failed run is reported, if at all, in whatever shape the return report happens to take.
- **The window's clock.** Tonight's window crosses the end of British Summer Time at 02:00 BST on 25 October. "Grant to 09:00", given at 01:31 BST, was read back at 01:07 GMT as 08:00 GMT, while 9 a.m. on the wall clock after the change is 09:00 GMT. An end time without an unambiguous instant can be read two ways.

## Owner's proposal

Kris, 25 October, going to sleep (logged at 01:07 GMT):

> "you've had my remit to do or progress things unattended without me until 9 a.m. tomorrow morning. Interactively prompt me for any queries you might have. Remember to mark. You are free to push as well if you need to make this work."
>
> "I want you to think about this in terms of how we deal with unattended work for a fixed period of time, such as effectively going through the queries and planning ahead of time so that you can do that unattended. In particular, I think this ties into also the general point I made before in the ways of working ... about unattended working and flags like that being put on roadmap items and such."
>
> "for unattended periods of time, there's no mark. So, basically, as you're going into an unattended period, it should be a mark that's taken so that when I come back after that unattended period, we can effectively walk through all the changes that have landed."
>
> "if there's any packed questions or queries before I go, it's important that they're unpacked and questioned, and ... continuously look at the roadmap and progress things as much as you can ... progress as much of the roadmap as possible related to your area."
>
> "in the unattended working mode, we need to make sure that the git repos are resynced ... every change that's finished ... or every 15 minutes ... if we do get [collisions], that they get resolved as part of the unattended work."
>
> "regularly run git syncs here so that we can be sure that any conflicts are dealt with appropriately and swiftly"

Kris, 25 October 01:30 BST, on commit cadence: "when there's a lot of changes in the work folder, the work is sitting there for a while and it's not getting committed. This makes it really difficult to keep the Git repositories in sync with the origin and other things which are also modifying the work packages because it's not regularly getting updates, pushes, and pulls."

Kris, 24 October, through Personal's State of play (UNATTENDED-AND-DUE-DATES): "we need to push that into the ways of working thread as something that we need to do an assessment of", and on roadmap records, an explicit due date or key milestone date "of what they're working towards". Earlier the same day, in Personal: "we can go through roadmap items and we can then put on them about whether or not we can do them unattended. We could even set out in front what the criteria are for the work being completed unattended."

## Established facts

- The standard records an away grant in the work's decisions log with its end time or return condition, work, permitted actions, exclusions, and wake and stop words, within `ki-delegation`'s authority limits; decisions outside it are parked; unattended work stops starting at expiry, explicit return or "stop the wake"; an ordinary steering message does not cancel the window; and the window promises only the authorised attempt, with usage-limit stops, missed processing and failed runs reported on return - [Coordinator responsiveness](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md#coordinator-responsiveness), Away grants.
- A separately requested schedule needs an explicit request or away grant and a `[scheduled]` banner item naming its mechanism, next firing, lifetime, expiry and "stop the wake" - the same section, Scheduled wakes.
- The heartbeat runs only while work lies with a worker, waking at least every 5 minutes; out-of-session runs wait for the owner until the completion watcher ships; session wakes are best effort - the same section, Heartbeat.
- WAKE-SUBSTRATE was taken on 23 October under Kris's 02:10 BST grant, reviewed at high: pursue the completion watcher first, label session wakes best effort, defer launchd, doorbells and liveness fields. The HNR line of 24 October still names a Rig launchd job as its leading idea - [decisions log](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/decisions.md), [messages](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/messages.md).
- UNWRITTEN-RULES was taken the same night: none of HNR's four inferred rules became standing instruction. The HNR line asks for each to be confirmed with Kris one by one - same sources.
- Tonight's grant: AWAY-GRANT at 01:31 BST, "Grant to 09:00", read as a window to 09:00 BST or Kris's return; work: launching this work's agents, committing, pushing this work's own commits fast-forward; exclusions: no standard or configuration change beyond Kris's answers in the thread, no DNS, Cloudflare or GitHub settings change, no release, no force-push; wake word "resume", stop word "stop the wake". The 01:07 GMT entry extended it: mark struck at entry, interactive query pass, sync after every finished change and at least every 15 minutes, pushing permitted for the sync fast-forward only, its scope over other sessions' stacked commits asked as SYNC-SCOPE - [decisions log](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/decisions.md).
- Clocks in Europe/London went back at 02:00 BST on 25 October 2026; the decisions log runs from a 02:03 BST entry to a 01:08 GMT one, and this machine's clock reads GMT.
- A session pushes fast-forward only when its own commits alone sit above the remote branch, and leaves other sessions' stacked commits to Kris, never as a "with you" item - [Pushing beneath other sessions](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md#pushing-beneath-other-sessions).
- The coordinator pulls primary checkouts only with `--ff-only` into a clean checkout, skipping and reporting a dirty or diverged one rather than stashing, rebasing or resetting it, and sends repair to a background agent or the owner - [Keeping primary checkouts current](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md#keeping-primary-checkouts-current).
- At every mark the coordinator runs `mgit fetch` across the work's repositories and reads `mcp-git-audit`'s ahead and behind report, carrying `[behind]` items until a fresh check proves them level; a failed check is unknown, never level - [Repository level check](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md#repository-level-check).
- A recap since the mark covers what was delivered, decided, started, stopped, blocked and captured since the mark; Outstanding carries forward across marks - [Recap since the mark](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md#recap-since-the-mark).
- Authority comes in four cumulative tiers, none, push, prune and release, plus single-ban grants for fetch and machine changes; no footer authorises accepting work, force-pushing, `--no-verify`, handling secrets or pushing another session's commits - [Authority tiers](/Users/krisbrown/.local/share/ki/harnesses/knowledgeislands/ki-agentic-harness/skills/governance/ki-delegation/references/standards-background-runs.md#authority-tiers).
- Parallel runs in one repository use their own worktrees and integrate by fast-forward into the primary checkout's `main`; a run that cannot fast-forward reports `stranded: <reason>` as a blocking query, never a quiet `DONE` - [Coordination](/Users/krisbrown/.local/share/ki/harnesses/knowledgeislands/ki-agentic-harness/skills/governance/ki-delegation/references/standards-background-runs.md#coordination).
- `ki-batch` already provides one bounded authority envelope over an exact, frozen set of Ready records in one repository, with `expires_at`, a `completion_target` of `awaiting-review` or `done`, and an outcome mode whose `authority_evidence` can cite an owner grant - [batch procedure](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-batch/references/standards-batch.md).
- Records carry no unattended or due-date field today; the only date a record carries besides timestamps is a held record's optional `hold.review`. Selection orders adoption, holds and dependencies, then horizon, then priority, then size, and priority never crosses horizons - [work-item format](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-work-roadmap/references/standards-work-item-format.md#priority-and-size).
- Personal's prototype tests each record against eight ordered criteria, `no-owner-judgement`, `no-outward-act`, `one-repo-authority`, `reversible`, `self-verifiable`, `unblocked`, `scoped` and `agent-step`, the first failure deciding one of three outcomes, `unattended`, `near-miss` with its one question, or `attended` with its failing criterion. Across 76 open Personal records it found 9 unattended, 21 near-miss and 46 attended, and it holds that eligibility is not authority - [unattended-criteria](/Users/krisbrown/workspaces/personal/personal-principal/+/_WORK/personal/design/unattended-criteria.md).
- Open queries this design leans on: COMMIT-CADENCE (high, reviewed), PACKAGE-PUSH (medium, reviews disagree), COORD-COMMANDS (medium, review disagrees) and DRAIN-END (high, reviewed) - [queries](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/queries.md).

## Reflection

### The window as a unit

1. An unattended window is an episode inside the work's With worker state, not an eighth state. While it is open the banner carries one `- [window] until <end> · stop the wake` item, as `[scheduled]` does, and the window needs no new field in `state.md`.
2. Authority and eligibility stay apart. The grant in the decisions log is the window's whole authority; a record's unattended flag only says whether the work could be done without Kris, and never authorises it.
3. A grant covering several works is recorded once, in the decisions log of the work Kris gave it to, and each other work's `state.md` next steps point at that entry, in line with CASCADE-REPORT's rule that a decision spanning Projects is kept once.
4. `/ki-coordination away <end>` and `/ki-coordination return` join the commands COORD-COMMANDS proposes, the spoken forms staying "while I am away" and Kris's first message or "resume".

### Entry

5. The grant entry states the end as one unambiguous instant, the local time with its zone and the UTC time beside it, next to Kris's own words. Where Kris's words could mean two instants, as across a clock change, the coordinator takes the earlier and says so in its read-back.
6. A standing default deny-list applies to every window, so a grant names only what it adds: no release, force-push or `--no-verify`; no acceptance, cancellation or prune beyond answers Kris gives at entry; no DNS, Cloudflare, GitHub settings, machine, scheduler, credential or connection-critical change; no message to a person and no publication beyond a deploy the repository already performs; no standard or configuration change beyond answers Kris gives at entry. Each of HNR's four unwritten rules joins the list only once Kris has confirmed it.
7. The mark is struck at entry, after the grant is logged and before the first launch. The same decisions entry records, for each repository in the window's scope, the short revision of `origin/main` and of local `main` at the mark, read in the level check the mark already runs. That baseline makes the return walk-through exact and needs no new field.
8. Before Kris leaves, the interactive pass takes every open query in full, one or two at a time, each answer read back. A packed query - one whose options bundle decisions that can be answered apart, or one that stays below high after review - is split first into separately tagged parts under SPLIT-QUERIES. A part left unanswered is parked for the window, and the work it gates is left out of the plan.
9. The coordinator writes a window plan into `state.md`'s next steps before Kris leaves: each unit in order, with its repository, the record or answer that authorises it, its tier, what it waits on and its expected size; then the excluded units, each with its reason. Kris sees it in the entry report, and the window does not wait for Kris to confirm it.
10. Entry checks run before the first launch: a green `main` in each repository a run will start from, the level check, and each primary checkout clean or named. A red baseline removes that repository's units from the plan, rather than stopping the window.
11. The plan is ranked so that the most valuable units land first, since a usage limit or outage can end the window's useful life early.

### During

12. Commit cadence follows COMMIT-CADENCE a): every complete unit is committed by explicit path before the turn that made it ends, and runs commit each step as they go.
13. Sync runs after every finished change and at least every 15 minutes: fetch, a fast-forward pull into each clean primary checkout in scope, and a fast-forward push of the coordinator's own commits, as far as SYNC-SCOPE and PACKAGE-PUSH allow. The 15-minute floor rides the existing 5-minute heartbeat, every third wake, and needs no separate scheduler.
14. A sync that cannot fast-forward never leads the coordinator to stash, rebase or reset. It launches a bounded resolve run at push tier in its own worktree, which rebases only the coordinator's and its runs' own commits onto the remote, resolves conflicts in files those commits own, reruns the gates and pushes fast-forward. A conflict in another session's content, or one needing judgement, stops the run and parks a blocking query for return, and that repository takes no further pushes in the window. A checkout left dirty by another session is skipped and named, never touched.
15. Progressing the roadmap means, for records flagged eligible in the window's works' scope ("related to your area"), planning a draft to Ready under `ki-plan` and delivering a Ready record to awaiting review under `ki-implement`, in waves through `ki-batch` outcome mode with the grant cited as `authority_evidence`. Adoption, horizon promotion, acceptance and pruning stay with Kris, as Personal's `agent-step` criterion holds. An unflagged record may be assessed and its flag proposed, but not delivered.
16. A query raised during the window goes into `queries.md`, and a blocking one parks its unit while the coordinator moves to the next eligible one. Medium- and low-confidence queries still go to their blind review in the window, so they reach Kris ready on return.
17. The failure modes are named in advance, and each is written into the decisions log as it happens: a session wake missed because the session was busy, compacted or ended; a usage-limit stop; a Claude Code, network or Headroom outage; a run that stops updating its status; a failed run; a stranded integration; a red gate; a rejected push; and a clock change crossing the end time. A trigger is never counted as processed work.
18. At expiry the coordinator stops launching, receives each run as it finishes and commits its result, and does not drain or hold. Runs still going at Kris's return are reported as running. The work stays With worker until the return report sends it to Kris.

### Return

19. Return is a send to Kris, Handoff to supervisor. Its report is the recap since the window's mark, extended across every repository in scope: for each repository, every commit between the entry baseline and its current `main`, the work's own units in detail, grouped by unit with what it changed and its checks, and other sessions' commits as a count naming their work where the subject shows it.
20. Each failure and stop from the window sits beside the unit it affected in `## Done`, and a closing Done line lists the window's misses in one place: missed wakes, usage-limit stops, failed and stranded runs, and units planned but never started, each with its reason.
21. After the report, Kris may walk through it interactively, one unit at a time, as in the query pass, with any `ACCEPT` bundle taken in the same walk-through.
22. The next mark is struck only once Kris has seen the return report or walked through it, so that the window stays the recap's window until then.

### Record flags

23. Records gain an optional `unattended` mapping, owned by `ki-work-roadmap`, recording an assessment rather than an authority:

    ```yaml
    unattended:
      verdict: eligible   # eligible | near-miss | attended
      criterion: null     # the first criterion failed; null when eligible
      question: null      # near-miss only: the one answer that would make it eligible
      assessed: 2026-10-25
    ```

    An absent mapping reads as unassessed, treated as attended. The assessment is refreshed whenever a record's status or horizon changes, since a stale verdict is worse than none.
24. The eight criteria are Personal's, adopted in order, with their wording owned by `ki-delegation` beside the authority tiers, since they test what an agent may do without Kris. `one-repo-authority` keeps its name: a window spans repositories, but each unit still runs in one.
25. Records gain an optional `target` mapping for what Kris asked for, "an explicit due date or key milestone date ... of what they're working towards":

    ```yaml
    target:
      date: 2026-10-31
      kind: due           # due: a hard date | milestone: an aim
      what: Halloween activity planned
    ```

    A target never moves a record across horizons, keeping the rule that priority does not cross them, but within one horizon and priority a nearer target goes first, and views flag a record whose target is near or past. `hold.review` stays separate, as the date to reconsider a hold.
26. `ki work status` and the roadmap checker read both mappings: a view of eligible records by work, and a view of targets by date. That tooling goes to ki.tools-burndown as a `messages.md` line once the fields are decided.

### Ownership and pilot

27. The window's life cycle - entry, during and return - lives in `ki-coordination`; the deny-list, the criteria and the resolve run in `ki-delegation`; the two fields in `ki-work-roadmap`; and the views in tools-ki.
28. The pilot is the next unattended window in `ki.ways-of-working` itself, then one window in Personal, which already holds the prototype assessment.

## Queries for the owner

These are the brief's own recommendations, before the two independent reviews and the merged report; every confidence below is unreviewed, and medium and low ones go to blind review before they reach Kris.

### WINDOW-CLOCK - how a window's end time is recorded

**Context:** Tonight's grant, "Grant to 09:00" at 01:31 BST, was read back after the clocks went back as 08:00 GMT, the same instant as 09:00 BST. 9 a.m. on the wall clock after the change is 09:00 GMT, an hour later. Any end time can be read two ways across a clock change, and the grant's authority depends on the instant.

**Query:** Should every grant record its end as one instant, local time with zone beside UTC, the earlier reading taken when Kris's words allow two?

**Options:**

a) (recommended, confidence high - stopping an hour early costs little and never exceeds authority) Record the end as local time with zone and UTC, take the earlier instant when ambiguous and say so in the read-back; tonight's window ends at 08:00 GMT.

b) Read the end as wall-clock time on Kris's return day; tonight's window ends at 09:00 GMT.

### DENY-LIST - a standing default list of what a window never does

**Context:** Each grant tonight and before restated its exclusions by hand, and HNR proposed one standing list. The brief's list is in point 6: no release, force-push or `--no-verify`; no acceptance, cancellation or prune beyond answers given at entry; no DNS, Cloudflare, GitHub settings, machine, scheduler, credential or connection-critical change; no message to a person or new publication; no standard or configuration change beyond answers given at entry. HNR's four unwritten rules would join only once Kris confirms each.

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
