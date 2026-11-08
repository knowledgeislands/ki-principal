# KI > Techne > Agora › scheduler-draft

**🤖 → 👤 Handoff to supervisor · Run report at 00:19 GMT · last mark 00:04 GMT**

---

## Done

- Drafted one triage record, high priority, in area `WRK` as KI-AGORA-WRK-004, "Run the rig's scheduled jobs", at [`scheduler-draft.drafts/KI-AGORA-WRK-004-run-the-rigs-scheduled-jobs.md`](/Users/krisbrown/.local/state/ki/agents/ki-prj-agora/scheduler-draft.drafts/KI-AGORA-WRK-004-run-the-rigs-scheduled-jobs.md). It has Goal, Context with Kris's words and a table of all thirteen first jobs, Boundary, Dependencies and Discussion, and links PERSONAL-DOTFILES-UE-137 at chezmoi `58ca9ef`.
- `rumdl check` with the repository's configuration: no issues.
- Repository unchanged; nothing committed.

Before capturing it, the coordinator reserves `WRK-004` in `docs/roadmap/_ISSUES.md` in a commit of its own. The ledger's front matter already reads `WRK: 3`, but its prose list still says `WRK` through `002` and `LVL` through `000`, so that capture is a chance to bring the list level.

## In Progress

Nothing. The job table's last-run column reads sol's launchd only, since this run is on sol. terra's laptop jobs were taken from PERSONAL-DOTFILES-UE-137 and the declarations, not checked live.

## Queries

### SCHED-FIRST - Which jobs move to Agora first

**Context:** Four of today's jobs make no model call and run on both Macs: the morning check, log rotation, workstation health and the Rig update. Five jobs start an agent: Route Triage, the three switched-off jobs and the territory dispatcher. Those cannot move until FOCUS-FIT is settled.

**Query:** Which jobs should Agora take over first?

**Options:**

a) (recommended, confidence high - lowest risk, and proves the reporting before anything that matters depends on it) The four model-free jobs on both Macs, one at a time, each with its launchd job kept as a tested way back. terra's model-free jobs and the checkout refresh follow, and agent jobs come last.

b) Route Triage first, since its silent failure is what started this, once FOCUS-FIT allows it.

c) All of today's enabled jobs at once, when the tools-rig engine lands.

### SCHED-REPORT - How a failure or missed run reaches you

**Context:** The Observatory already showed both silent failures, but nobody was looking at it. You asked for failures and missed runs to be reported the same day.

**Query:** Where should a failed or missed run be reported?

**Options:**

a) (recommended, confidence medium - it reaches someone without being looked for and reuses Agora's existing doorbells, though each job then needs a named owner) Record it in Agora's state for the Observatory, and on the same day ring the doorbell of the package that owns the job, with a marker in the tray until it clears.

b) Tray marker and Observatory only.

c) A daily summary line in the morning report only.

### SCHED-FOCUS-HOST - Does the focus bound cover terra

**Context:** The [Techne Programme Focus](/Users/krisbrown/kis/knowledge-islands/ki-principal/Admin/Governance/Policies/Techne%20Programme%20Focus.md) rules out unattended or scheduled agents on its two hosts, sol and vega. Today's agent jobs run unattended on terra under launchd, outside those named hosts. The brief holds every agent job back until FOCUS-FIT is answered.

**Query:** When Agora runs an agent job on terra, does the focus bound apply?

**Options:**

a) (recommended, confidence medium - it keeps one rule for anything Agora starts, whichever Mac it is on) Yes. Any job Agora runs that starts an agent waits for your FOCUS-FIT answer or an Enactment decision, on every Mac.

b) No. The bound covers sol and vega only, so terra's agent jobs may move under Agora as they run today.

### SCHED-PAUSED - How a paused job is declared

**Context:** The WhatsApp spool refresh has been paused at your word since 3 November, but its declaration still reads enabled, so it keeps running and failing every day.

**Query:** How should a paused job be declared?

**Options:**

a) (recommended, confidence medium - it uses Rig's existing vocabulary and needs no new engine work) Declare it disabled, with a rationale naming your word and its date. Agora reports it as off, not failing.

b) Rig gains a paused state carrying a reason and a review date, which Agora shows as paused.

c) Leave it enabled and have Agora stop reporting its failures.

### SCHED-ONE-RIG - Jobs that must run on exactly one Mac

**Context:** Route Triage and the legal jobs run only on terra today, through Rig's laptop profile, so that only one Mac sorts mail or commits a log. Run-once claims across the group belong to KI-AGORA-WRK-001.

**Query:** How should Agora keep such a job to one Mac?

**Options:**

a) (recommended, confidence high - it works now and leaves failover for later) Keep Rig's host selection for now, and add run-once claims with KI-AGORA-WRK-001 later so another Mac can take over safely.

b) Wait for run-once claims before moving any one-Mac job.

🧵 ki.prj.agora
