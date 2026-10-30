<!-- rumdl-disable MD041 -->

### LAYOUT-SHAPE

**Context:** Kris set on 30 October that a work package keeps only its five files at the top level, with everything else grouped, possibly group first with briefs, design and reports beneath. Three shapes fit. A, kind-first: `reports/`, `briefs/` and `design/` folders, the cheapest change, but a matter stays spread across three folders and the tidy stays file by file. B, group-first with kind subfolders, as sketched: one folder per matter with `briefs/` and `reports/` inside, which needs an estate-wide ignore exception because `reports/` is ignored at any depth. C, group-first and flat: one folder per matter, with `<run>.brief.md` and `<run>.report.md` side by side and design files under plain names, needing no ignore change. The evidence suggests the sprawl comes mainly from retention, so the group earns its cost only as the unit of tidy. No shape has been piloted.

**Query:** Which layout should the pilot use?

**Options:**

1. A, kind-first, with a stricter tidy cadence instead of groups.
2. C, group-first and flat.
3. B, group-first with `briefs/` and `reports/` subfolders, plus the `ki-repo` ignore exception.

### LAYOUT-GROUP-TIDY

**Context:** Today's tidy deletes file by file, by explicit path, never folder-wide, and the steward judges each file's durable home. Under a group-first layout, a matter's files usually become homed together. The proposal is that once the steward judges a whole group closed, with outcomes homed, queries copied and design notes graduated or superseded, it deletes the group with one `git rm -r` naming that folder, in one commit, with Git keeping the history. Single-file deletion remains available.

**Query:** Should the tidy rule allow deleting one named, closed group folder whole?

**Options:**

1. No: keep file-by-file deletion inside groups.
2. Yes: a steward may delete one named, closed group in one commit.

### LAYOUT-PILOT-ORDER

**Context:** The rubric's FOLDER-1 fails any folder outside the closed list, the launcher homes reports only at the top level, and the Observatory reads only top-level reports and `design/`. Piloting this package before those change gives evidence sooner but shows rubric failures and hides moved reports from the Observatory and `ki agent decide`. Changing the standard and rubric first is a small harness change; the launcher and Observatory changes belong to other works and would take longer.

**Query:** In what order should the pilot run?

**Options:**

1. Pilot now, ahead of the rubric, and accept FOLDER-1 failures in this package until the harness catches up.
2. Wait until the launcher and Observatory changes have also landed.
3. Change the closed list and FOLDER rubric first, then pilot this package by hand, receiving and tidying before moving, with launcher and Observatory changes following.

### REVIEW-LIFT

**Context:** Under the query-review rule, a blind review that agrees with a recommendation lifts its confidence one level. A review can agree simply because the Context framed the question inside an earlier decision. The proposal: agreement that rests only on an earlier decision or on the framing is marked `reviewed, precedent only` and lifts nothing, and an option whose only stated reason is an earlier decision is capped at medium. This changes how confidence is earned across every query, and it will send more queries to Kris at medium.

**Query:** Should precedent alone stop counting towards confidence?

**Options:**

1. No: keep today's lift rule, relying on the independence sentence alone.
2. Yes: no lift from precedent-only agreement, and a precedent-only reason caps at medium.

### READ-FEEDBACK-NOW

**Context:** The closed list keeps owner feedback on documents as `feedback/<date>-<slug>.md` plus one `messages.md` line, and names only "the owner, through the Observatory" as its writer. Kris can read design notes in Obsidian today, but feedback longer than a spoken answer can be left only through the Observatory's `feedback-send`, which reads only top-level reports and `design/` notes and so loses sight of moved files until it is made group-aware. The proposal widens that row: the owner may write the package by hand, or the steward may write it verbatim from the owner's spoken words, committed with its message line in the same shape.

**Query:** Should feedback packages be writable now, outside the Observatory?

**Options:**

1. No: feedback stays spoken until the Observatory path is ready.
2. Yes, by the owner by hand or by the steward verbatim from the owner's words.

### ORCH-NAME

**Context:** On 30 October Kris asked: "If you put aside the rename cost, what is the feedback on naming then?" The earlier recommendation, to keep the current names, rested on the cost of renaming the output style, a 217 KB standard and every live package mid-rollout; both design reviews kept the names for that reason, and once it is removed the keep has no high-confidence footing. An independent naming review then judged each unit with rename cost excluded. Thread-governance skill: `ki-orchestration`, medium - `ki-coordination` is intelligible but broad, and a newcomer cannot tell whether it governs human collaboration, worker dispatch or project administration; orchestration names the agent that runs the package's state machine, the role Kris named "the orchestrator of the state machine" on 29 October. Output style: `ki-orchestrator`, medium - it names the role and drops "coordinator" as a fourth actor word beside orchestrator, worker and supervisor. Portable run contract: `ki-delegation`, high - an orchestrator delegates a bounded job and a worker returns evidence or a question; `ki-dispatch` understates the brief, authority and return, and `ki-orchestration` would put the thread's name on one of its contracts. Adapters: `ki-delegation-orca` and `ki-delegation-paperclip`, high, provided the Paperclip skill's wider remit (company boundaries, readiness, memory, delivery policy) is described honestly rather than relabelled; `ki-agent-coordination-paperclip` has no natural Orca sibling. Launcher: `ki agent`, medium, on its own merits - `ki orchestrate` implies the executable owns the package, `ki delegate` names one action of a group that also observes, steers and closes, and `ki run` is too broad; this is the least certain unit. Main risk: `ki-orchestration` overlaps Orca's installed `orchestration` skill in meaning, though not in identifier, so the descriptions must keep package governance and Orca mechanics apart. The review's strongest alternative keeps `ki-coordination` and `ki-coordinator`: coordination comfortably covers questions to Kris, decisions, handoffs and stewardship when no worker is running, and is less associated with an execution engine. It placed that second because it leaves "coordinator" as a synonym a newcomer must learn for the orchestrator. Overall confidence is medium: both leading sets are defensible and no newcomer has tested them. Moving `decide`, `reconcile`, `home` and `prompts` under `ki work` stays out of this query, under AGENT-HOME.

**Query:** Setting rename cost aside, which names should the thread skill and its style, the dispatch contract, its adapters and the command take?

**Options:**

1. Keep the current names: keep `ki-coordination`, `ki-coordinator`, `ki-delegation` and `ki agent`, and say in the Work Process note that the orchestrator role is exercised under `ki-coordination`.
2. Keep `ki-coordination` and `ki-coordinator` because coordination better conveys the whole human and agent governance practice, with the same `ki-delegation`, `ki-delegation-orca` and `ki-delegation-paperclip` family and `ki agent`.
3. Rename the thread skill `ki-orchestration` and the output style `ki-orchestrator`; keep `ki-delegation`, slimmed, as the portable contract, with adapters `ki-delegation-orca` and `ki-delegation-paperclip`, the second renamed from `ki-agent-coordination-paperclip` with its wider remit stated; keep `ki agent`.
