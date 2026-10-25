# wow-window-blind

## Goal

Masked blind review of seven questions before Kris sees them. For each, give your own recommendation, with a confidence (high, medium or low) and a one-line reason. Do not read any `queries.md`, `decisions.md`, run report or `design/` file in any work package.

## Read

Only: in ki-agentic-harness, the `ki-coordination`, `ki-delegation`, `ki-work-package`, `ki-work-roadmap` and `ki-batch` standards.

## Questions

### MEMBER-PACKAGE

Context: [personal.regular.acquire-intake](/Users/krisbrown/workspaces/personal/acquire/+/_WORK/personal.regular.acquire-intake/work.md) is a package held in the member repository `personal/acquire`, not in the Capital. The rubric bars only territory work outside a Capital, so this is allowed but undeclared anywhere. It is the only such case found. This query has not had a blind review.

Question: May a member repository hold a package for its own regular work, provided its `work.md` declares it as such?

Options (unranked):

- Move every package into the Capital, including regular work.
- Allow it for regular work only, declared in `work.md`; Project and territory work stay in the Capital.

### DENY-LIST

Context: Each grant tonight and before restated its exclusions by hand, and HNR proposed one standing list. The brief's list: no release, force-push or `--no-verify`; no acceptance, cancellation or prune beyond answers given at entry; no DNS, Cloudflare, GitHub settings, machine, scheduler, credential or connection-critical change; no message to a person or new publication; no standard or configuration change beyond answers given at entry. HNR's four unwritten rules would join only once Kris confirms each.

Question: Should every window carry this standing deny-list, with a grant lifting an item only by naming it?

Options (unranked):

- Keep per-window exclusions only, as today.
- Adopt the standing list in `ki-delegation`, each grant naming any item it lifts.

### WINDOW-PLAN

Context: The brief has the coordinator write a plan into `state.md` before Kris leaves: units in order with their authority, tier and dependencies, and the excluded units with reasons. Kris often grants a window as the last act before sleep.

Question: Should the window start without waiting for Kris to confirm its plan?

Options (unranked):

- Start only once Kris has confirmed the plan.
- Show the plan in the entry report and start without confirmation.

### CONFLICT-RUN

Context: Kris asked that collisions "get resolved as part of the unattended work". The standard lets the coordinator only fast-forward a clean checkout and sends repair to a run or Kris. The brief proposes a bounded resolve run at push tier, in its own worktree, rebasing only this work's own commits and resolving conflicts only in files they own; a conflict in another session's content or needing judgement stops it with a blocking query. Its push depends on SYNC-SCOPE and PACKAGE-PUSH.

Question: Should a sync that cannot fast-forward launch a bounded resolve run limited to this work's own commits?

Options (unranked):

- No, leave every conflict for Kris on return, as today.
- Yes, a bounded resolve run at push tier, stopping on another session's content or a judgement call.

### PROGRESS-SCOPE

Context: Kris asked to "progress as much of the roadmap as possible related to your area". Lifecycle moves split between agents and Kris: planning and delivery are an agent's, adoption, promotion and acceptance Kris's. `ki-batch` can run a frozen set of Ready records to `awaiting-review`, or to `done` when the grant says so.

Question: Should a window plan and deliver eligible records in its works' scope up to awaiting review, leaving adoption, promotion, acceptance and pruning to Kris?

Options (unranked):

- Plan only, delivering nothing until Kris returns.
- As a), and also close to done records the grant names at entry.
- Plan drafts to Ready and deliver Ready records to awaiting review, in `ki-batch` waves citing the grant.

### UNATTENDED-FIELD

Context: Personal's prototype assessed 76 records against eight ordered criteria, 9 eligible, 21 near-miss and 46 attended, and proposed a record field. The brief proposes an optional `unattended` mapping in `ki-work-roadmap` with `verdict` (`eligible`, `near-miss`, `attended`), `criterion`, `question` and `assessed`, an absent mapping read as attended, and the criteria owned by `ki-delegation`.

Question: Should records carry this optional `unattended` mapping, with the eight criteria in `ki-delegation`?

Options (unranked):

- Keep the assessment in a per-window note, with no record field.
- Adopt the mapping and the criteria, refreshed at each status or horizon change.

### DUE-FIELD

Context: Kris asked for "an explicit due date or key milestone date ... of what they're working towards". Records carry no such date; selection runs horizon, priority, size. The brief proposes an optional `target` mapping, `date`, `kind` (`due` or `milestone`) and `what`, that orders records only within a horizon and priority and is flagged in views when near or past.

Question: Should records carry an optional `target` mapping with a date, a due-or-milestone kind and what it works towards?

Options (unranked):

- A single optional `due` date, with no kind or description.
- Adopt `target` as proposed.

## Rules

Read only; write nothing in any repository; no network calls; launch no agents. Report in the owner-report shape with one query per question, your recommendation as a), and the banner.
