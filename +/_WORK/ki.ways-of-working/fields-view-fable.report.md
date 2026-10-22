# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › fields-view-fable

**🤖 → 👤 Handoff to supervisor · Run report at 08:46 BST**

---

## Done

Read-only blind review of the work-record field model: no edits, commits or pushes anywhere, no gates run, net record count zero in every repository. Evidence: the [field survey](/Users/krisbrown/.local/state/ki/agents/ways-of-working/field-survey.report.md), the [work-item format](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-work-roadmap/references/standards-work-item-format.md), the [repository-roadmap standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-work-roadmap/references/standards-repository-roadmaps.md), the [Project registry](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-work/references/standards-project-registry.md), the [crosswalk](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-work/references/standards-change-management-adapters.md), the [decisions log](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/decisions.md) entries SIZE-PRIORITY, mark recap and ITEM-FIELDS, and the size-priority-2 change, which landed in ki-agentic-harness as `d9cd8718` while I read.

### 1. Field set as a whole - agree, with two adjustments (confidence medium)

The core is right for an owner-run, agent-heavy estate: identity, status and horizon as independent axes, build-order dependencies, baseline and timestamps give an agent everything it needs to pick, deliver and prove work, and nothing needs an owner, assignee or due date because the repository owns the record and `hold.review` covers the one date that matters. Redundant: `theme` beside `project` (12 records) is already declared redundant, so it should fail once the registry resolves, not warn. `purpose` is the weakest field (97 of 316, three values doing all the work); keep it optional, do not require it. Nothing is missing. `transferred_from` (7 records, checked by neither validator) is the next retirement candidate but harmless today.

Reason: the fields that matter are the ones a validator or a selection rule reads; everything else is cost on every capture.

### 2. Priority - agree, with one addition (confidence high)

Semantics and vocabulary are right: horizon says when, priority says how important within a horizon, and `high`, `medium`, `low` with absent reading as `medium` makes priority a sparse flag rather than a chore. What the standard still lacks is the interaction rule. Recommend one sentence: selection takes horizon first, then only unblocked records, then priority, then size smallest first as the last tie-break; priority never crosses horizons, so a `high` at `soon` never beats a `medium` at `next`, and when it should, the horizon moves. `ki work` lists in that order.

Reason: without a stated order two agents choosing "what is next" will choose differently.

### 3. Size - adjust (confidence medium)

The four values and the `xl` rule are right, but the one-line meanings measure human hours ("an hour or two", "about a day"), which an agent cannot observe and which say nothing about the record. For agent-delivered work size should measure delivery shape: `s` one run, one repository, one commit; `m` one run, one repository, several commits and a plan; `l` several chained runs or several repositories, a plan with Delegation; `xl` not one record, split before Ready. Size should drive exactly one hard rule: `status: ready` with `size: xl` fails. It should not drive scheduling. Requiring it at triage is acceptable because the judgement is cheap and it is the moment splitting is cheapest. Minor: the format lists `size` among the always-required fields while the window makes it warn-only; align the wording.

Reason: an agent's wall-clock is not a stable unit, but runs, repositories and commits are visible in the record and the logbook.

### 4. Tightening - agree, with a backstop (confidence medium)

Two validators disagreeing is the worst state, so tools-ki failing what the harness fails is right, and retired horizons already fail in the harness. Missing `kind` moving from warn to fail is right because kind decides the close condition. Two adjustments: the window's close condition ("no gaps estate-wide") has nothing driving it, so add a date backstop; and "fails what the harness fails" should hold by construction, through one shared field rule table (ki-specifications has no work-item schema today) rather than two hand-kept lists.

Reason: 11 repositories already carry shapes the harness fails, so a tighter validator nobody runs green changes nothing.

### 5. Clean-up - agree (confidence high)

Retiring `initiative` and `purpose: adoption` is right. Keeping `kind: decide`, `resolution_target` and `task_links` is also right: usage is the wrong test for a field that matters only at a rare event, and each is the sole pointer another rule depends on (graduation test b, prune safety for merged or duplicate cancellations, Paperclip's durable link).

### 6. Migration - adjust (confidence medium)

Most of the backlog is mechanical and should not wait on owner judgement: `horizon: triage` on a draft becomes `status: triage` with no horizon; `waiting-for` and `parked` become `hold` with the reason set and the condition lifted from the body or flagged; `initiative` becomes `theme`; `kind: deliver` where the record already carries Steps and Files touched. One run per repository, owner approval per repository. Only size needs judgement, and even there a run can propose from the plan shape for Kris to confirm. Order: retired horizons first, since they fail today, then kind, then size.

## In Progress

Nothing is running. Outstanding - no action requested now: none.

## Queries

### SIZE-MEANING - Measure size by delivery shape, and let xl block Ready

**Context:** The committed format defines `s` to `l` in human hours. Agents deliver most records, and the only thing size is asked to do is show effort and guide splitting.

**Query:** Should size be redefined by runs, repositories and commits, with `status: ready` failing on `size: xl`?

**Options:**

a) (recommended, confidence medium - delivery shape is observable in the record and the logbook, hours are not) Redefine the four meanings by delivery shape as in finding 3, add the one checker rule that Ready and `xl` cannot coexist, and align the required-fields sentence with the warn window.

b) Keep the hour-based meanings and add only the Ready-with-xl rule.

### SELECTION-ORDER - State how horizon, priority and size pick what is next

**Context:** Priority now sits beside horizon, but no standard says how the two combine, and `ki work` has no stated sort.

**Query:** Should the work-item format state the selection order horizon, then unblocked, then priority, then size smallest first, with priority never crossing horizons?

**Options:**

a) (recommended, confidence high - one stated order is the only way two agents choose the same next record) Add the sentence to the format and the crosswalk, and have the tools-ki handoff record sort `ki work` the same way.

b) Leave the order to each session's judgement.

### MECHANICAL-BACKFILL - Migrate the mechanical cases by run, with a dated window

**Context:** 55 retired horizons, 13 `initiative` fields, 12 redundant theme-beside-project cases and most of the 106 missing kinds are derivable from the record itself. The window closes only when `ki work` shows no gaps, and nothing drives that.

**Query:** Should one run per repository apply the mechanical migrations under owner approval, leaving only size to judgement, and should the window carry a date backstop?

**Options:**

a) (recommended, confidence medium - the mechanical cases already fail in the harness and owners have not moved them) Launch per-repository migration runs for horizons, initiative, kind and theme-beside-project, with size proposed from the plan shape for Kris to confirm, and set the window to close at the stated condition or on a fixed date, whichever is first.

b) Keep the decided shape: owners backfill everything by judgement and the window closes when `ki work` shows no gaps.

### ONE-RULE-TABLE - Hold validator parity by construction

**Context:** The harness checker and tools-ki `ki work` keep separate hand-written rules and have drifted before; ki-specifications has no work-item schema.

**Query:** Should the field rules live once, as a schema or rule table in ki-specifications or vendored from the harness into tools-ki with a drift check?

**Options:**

a) (recommended, confidence medium - parity by construction removes the recurring disagreement, but it is a tools-ki record of its own) Capture one tools-ki record to adopt a shared rule table after the current handoff lands.

b) Keep two lists and rely on the tools-ki handoff record to match the harness by hand.
