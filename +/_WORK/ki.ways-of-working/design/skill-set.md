---
note_type: streams/design
updated: 2026-10-25T01:55:00Z
author: Written with Claude
---

# Ways of working: the skill set

**Owner:** Kris Brown · **Owning repository:** knowledgeislands/ki-principal · **Owning work:** `ki.ways-of-working` · **Date:** 2026-10-25, written during the unattended window opened at the 01:07 GMT mark

**Status:** a model for Kris to sanity-check, under the cross-project rule "name each unit of comprehension, state its boundary and hand-offs, and surface the model for a sanity check before implementing". It decides nothing, proposes no implementation and changes no skill. It answers Kris's goal of 01:10 GMT, "come back and the ways of working be fully bottomed out with some really clear thinking. I want the set of skills to be well defined around this ... when we do a bootstrap ... it works really well", and his question whether every work package can have its own coordination thread. It builds on [overview](overview.md), [unattended-work](unattended-work.md) and [model-shape-report](model-shape-report.md), and reads the fourteen skills as they stand at harness revision `0f671e4f`. Its predecessor under the thread model is the 13 October [change-management-report](change-management-report.md), whose six units (work, PMO, delegation, continuity, design loop, model policy) map onto the layers below.

## Contents

- [Summary](#summary)
- [The set in five layers](#the-set-in-five-layers)
- [Units](#units)
- [Session kinds](#session-kinds)
- [A coordination thread for every work package](#a-coordination-thread-for-every-work-package)
- [The bootstrap path](#the-bootstrap-path)
- [Overlaps, gaps and contradictions](#overlaps-gaps-and-contradictions)
- [The unattended window, end to end](#the-unattended-window-end-to-end)
- [Queries](#queries)
- [Rollout notes](#rollout-notes)

## Summary

- **The set is sound in shape and stale in places.** Fourteen skills fall into five layers with clean boundaries: activation, the definition of work, the record life cycle, running and coordinating work, and continuity. Every skill has one job that no other skill does. The faults are not missing skills but text that predates the 25 October decisions, one missing narrative (the bootstrap) and one function spread over four skills (the unattended window).
- **Every Project package can have its own coordination thread, and should only when it is active.** One seated thread per active Project package is the default. Dormant packages are stewarded by State of play, or a secondary State of play, under CASCADE-STEWARD. Regular and ad hoc packages never get a coordination thread. What limits the number is the active-work cap of three or four and Kris's attention (eight open queries and eight records to accept per work), not the skills. See [A coordination thread for every work package](#a-coordination-thread-for-every-work-package).
- **The bootstrap has no owner.** `ki-bootstrap` stops at skill activation and `ki-coordination` starts at the opener. The steps between them (chezmoi binding the hook and output style, the Capital's declarations, `ki agent prompts`, naming the session) are written nowhere as one path. This is the single change that most serves "when we do a bootstrap ... it works really well". See [The bootstrap path](#the-bootstrap-path) and BOOT-HOME.
- **Nine contradictions, nearly all from decided-but-not-landed rules.** The push rule, the commit rule, hosts, one session per piece of work, report homing, the singular-package turn, pull mode, numbered decisions and in-session worker lanes each say one thing in the skill and another in Kris's 25 October decisions. Each has a one-sentence fix and an owner; none needs a new decision except where flagged.
- **The unattended window needs one owner.** Its life cycle should sit in `ki-coordination` as one section, citing `ki-delegation` for the deny-list and authority, `ki-batch` for envelopes inside the window and `ki-work-roadmap` for the fields. Tonight's window ran on decisions logged in this package rather than on a standard, which worked because one coordinator held it all in mind.
- **Three queries** are for Kris: BOOT-HOME, TRADES-FATE and RECAP-NAME. None has had its blind review yet; the coordinator sends them before they reach Kris.

## The set in five layers

```text
 Layer 0  Activation          ki-bootstrap  (with tools-ki `ki`, chezmoi, Rig)
              |  installs the harness, activates process skills, projects declared skills
              v
 Layer 1  Definition of work  ki-work  ->  ki-work-roadmap        ki-work-package
              |  adapter and Project registry; records; the five-file package
              v
 Layer 2  Record life cycle   ki-work-design -> ki-next -> ki-plan -> ki-implement -> ki-accept
              |                                  \________ ki-batch (envelope) ________/
              v
 Layer 3  Running and         ki-delegation (runs)  <-  ki-coordination (sessions that coordinate)
          coordinating            launched by `ki agent`; hook and output style generated from ki-coordination
              |
              v
 Layer 4  Continuity          ki-recap (one session)   ki-coordination recap, Summary, mark (one work)

 Retiring  ki-trades           on hold since 14 October; superseded for handoffs by HANDOFF-AS-MESSAGE
```

The arrows are hand-offs, not dependencies. Two facts shape everything below:

- **Process skills travel; governance skills stay home.** `ki bootstrap` activates seven process skills at user scope: `ki-bootstrap`, `ki-next`, `ki-plan`, `ki-implement`, `ki-accept`, `ki-batch` and `ki-recap`. The governance skills (`ki-work`, `ki-work-roadmap`, `ki-work-package`, `ki-delegation`, `ki-coordination`, `ki-trades`) reach a session only through the repository it starts in, by `.ki.toml` declaration and `ki repo skill add`. So a coordinator must start in the Capital, and a run sent into another repository must be told where that repository's governance skills are, as the bootstrap standard's Skill access in delegated work sets.
- **`ki-work-design` is a process skill outside the core seven.** It is declared `invocation-only` but `ki bootstrap` does not activate it, so it depends on a separate `ki skill add`. Gap G3.

## Units

Each unit is named, with its job, its boundary and its hand-offs. "Kind" is its `ki-kind` and how it reaches a session.

### ki-bootstrap - activation

- **Job:** explain and verify first-time activation: the verified canonical harness, user-scope process skills, repository-scope declarations, local harness development and managed-state recovery.
- **Boundary:** guidance only; `tools-ki` owns every command. It does not declare governance in any repository, and says nothing about coordinating sessions, the hook, the output style or openers.
- **Hands to:** `ki-repo` for `.ki.toml` coverage; implicitly, nobody for the coordinator half of a bootstrap (gap G1).
- **Kind:** process, core.

### ki-work - the forward-work adapter and registry

- **Job:** select one adapter per repository (local roadmap, KB Streams, GitHub Issues or Linear), own the shared life-cycle vocabulary, the Project registry standard (themes and Projects in the Capital's `Streams/`) and the `+/_BATCHES/` scaffold.
- **Boundary:** chooses and audits; the adapter owns record shape and the process skills own transitions.
- **Hands to:** `ki-work-roadmap` or `ki-repo-kb-streams` for records; `ki-coordination` for the work naming that reads Project slugs.
- **Kind:** governance, declared.

### ki-work-roadmap - work records

- **Job:** the record model: flat records, horizons, the status life cycle (draft, ready, in-progress, awaiting-review, done), dependencies, triage, `_ISSUES.md`, done-before-prune boundaries, and the `project` field that links a record to its Project and so to its package.
- **Boundary:** shape and audit only; it never moves a record.
- **Hands to:** the four process skills for every transition; Decision Records for rationale.
- **Carries forward:** the `initiative` field, legacy since THEME-CLOSE, until the 7 November 2026 cutover (G10). The decided `unattended` and `target` fields are not yet in it (G7).
- **Kind:** governance, declared.

### ki-work-package - the package

- **Job:** the five files of one piece of work in `+/_WORK/<id>/` (`work.md`, `state.md`, `queries.md`, `messages.md`, `decisions.md`), the closed list, entry points (who may write what), message line shape, tidy and close-out, `+/_WORK_REVIEW/`, and the native-session binding; modes create, update, resume, audit, tidy and remove.
- **Boundary:** the folder and its files. When to tidy, whether an outcome is homed and how a decision is logged are `ki-coordination`'s.
- **Hands to:** `ki-coordination` for timing and judgement; `ki-recap` composes its UPDATE mode at a checkpoint.
- **Stale text:** "never a host" (C3), "a native session belongs to at most one piece of work" (C4), and a closed list without `findings/` (G7).
- **Kind:** governance, detected.

### ki-work-design - shaping before records

- **Job:** shape a new Project, theme or cross-cutting model before any record exists: brief, independent reviews, one merged report, the owner's decisions and a piloted rollout, all in `+/_WORK/<id>/design/`.
- **Boundary:** undecided shape only. Known work goes to `ki-next`; a ready record to `ki-plan`. Graduation and deletion of design notes are its own.
- **Hands to:** `ki-next` to capture the records a rollout needs; Decision Records for standalone decisions.
- **Stale text:** decisions "numbered against the report's decisions" in its standard and its `assets/decisions.md` (C8).
- **Kind:** process, not core (G3).

### ki-next - capture and selection

- **Job:** capture substantive prospective work as unadopted triage records; select, adopt, promote, defer, hold and release work in the queue; screen for synergy.
- **Boundary:** under CAPTURE-GATE a background run never creates a record, and adoption needs human approval. It does not ready, deliver or close.
- **Hands to:** `ki-plan` (readiness), `ki-accept` (cancellation), `ki-batch` (a synergistic set).
- **Kind:** process, core.

### ki-plan - readiness

- **Job:** shape one selected Now or Next draft until it is Ready.
- **Boundary:** never captures, selects, implements or closes.
- **Hands to:** `ki-implement`.
- **Kind:** process, core.

### ki-implement - delivery

- **Job:** deliver one Ready record from an immutable baseline through verification to awaiting-review.
- **Boundary:** never selects, replans, self-accepts, prunes, pushes, releases or widens authority.
- **Hands to:** `ki-accept`, through Kris.
- **Conflict:** "when `ki-delegation` is active in the same scope ... keep the primary agent available as coordinator while bounded subagents execute the approved worker lanes" reads against the coordinator's rule that every unit goes to a detached background agent and that an in-session subagent is not one (C9).
- **Kind:** process, core.

### ki-accept - closure

- **Job:** close a reviewed record as done, cancel an open record with an approved resolution, prune selected terminal records; ACCEPT-BUNDLE batch closure of named records.
- **Boundary:** human approval always; never delivers.
- **Hands to:** the prune-only commit; `ki-coordination` brings the bundle.
- **Kind:** process, core.

### ki-batch - the authority envelope

- **Job:** one bounded envelope over an exact set of Ready records in one repository, in reviewed-item or outcome mode, with `expires_at`, `completion_target`, `authority_evidence` and the `safe-local-v1` profile.
- **Boundary:** one repository, one window; each record's planning, delivery and closure stay with their skills.
- **Hands to:** `ki-plan`, `ki-implement`, `ki-accept` per record.
- **Overlap:** with the away grant (O3).
- **Kind:** process, core.

### ki-delegation - background runs

- **Job:** the background-run contract: detachment, the run packet, prompt shape and brief-writing, authority tiers (none, push, prune, release) and footers, the launcher's part of the decisions log, coordination between runs, the run queue and monitoring; durable packets for high-risk handoffs.
- **Boundary:** the run side. It never decides how a coordinator reports; it links to the owner report.
- **Hands to:** `ki agent` (launcher), `ki-coordination` (the report shape).
- **Stale text:** the run report is homed in the launching work's folder, against CASCADE-REPORT (C5).
- **Kind:** governance, declared.

### ki-coordination - sessions that coordinate, and how every session replies

- **Job:** the responsive coordinator and its three hard rules; the turn budget and heartbeat; levels, forms and work naming; openers and bootstrap; states, moves and receive words; the report heading, owner report, Needs tags, glyph banner and thread line; Summary, recap since the mark, full summary and hold report; the message queue, routing and route receipt; decision classes and life cycle; design-note review; Finished; the working rules; the three reply forms every session uses; and the generated surfaces (hook line, output style, run-prompt report paragraph).
- **Boundary:** never launches, briefs or monitors runs (`ki-delegation`), never defines the package (`ki-work-package`), never summarises one ordinary session (`ki-recap`).
- **Hands to:** `ki-delegation` for every unit of work; `ki-work-package` for the files; `ki-accept` for bundles; `ki-next` for capture by the receiver.
- **Stale text:** C1, C2, C3, C4, C6, C7 and G2 below; COORD-COMMANDS, THREAD-RENAME, METHOD-NUDGE and REVIEW-CHECK decided but not landed (G7).
- **Kind:** governance, declared; it depends on `ki-delegation` and `ki-work-package`.

### ki-recap - one session

- **Job:** recap the live session: changes, decisions, touched files, unfinished work, routes for durable learning; `checkpoint <thread>` hands evidence to `ki-work-package` UPDATE.
- **Boundary:** one session, lower level than a work; shares no format with the coordinator's recap since the mark.
- **Overlap:** three recaps (O1); the `thread` wording (RECAP-NAME).
- **Kind:** process, core.

### ki-trades - directional trades between repositories

- **Job:** routes, records, authority, receipt, decisions, release and pruning of trades between repositories.
- **Boundary:** on hold ("submit no new trade until the territory model is settled"), due review by 21 October 2026, now overdue, which its own `HOLD-1` audit item warns on. HANDOFF-AS-MESSAGE (20 October) moved handoffs and rollouts to `messages.md`, leaving it only the routes `.ki.toml` declares. The planned [Trades revamp](../../../../Streams/Projects/trades-revamp.md) Project owns its shape.
- **Kind:** governance, declared. See TRADES-FATE.

### Surfaces that are not skills

| Surface | Owner | Part in the set |
| --- | --- | --- |
| `ki agent` (launch, queue, status, prompts, decide, close) | `tools-ki` | launches every run, prints every opener, closes runs under the strict gate |
| `ki work status` | `tools-ki` | the five views across a territory, derived from package front matter |
| `hooks/coordinator-reminder.sh` | harness, generated from `ki-coordination` | one line on each owner message in a declaring repository; silent in `KI_AGENT_RUN` |
| `output-styles/ki-coordinator.md` | harness, generated from `ki-coordination` | the owner-report contract as the session's style |
| chezmoi | the user environment | links the style, registers the hook, places the CLAUDE files |
| Rig (`tools-rig`) | workstation | the machine inventory HOST-SEAT reads; installs the tools |
| the Observatory | `apps-observatory.local` | renders the views and the Work tab; writes feedback packages |
| The [Work Process](<../../../../Pillars/Philosophy/Model/Processes/Work Process/Work Process.md>) note | ki-principal | the model every skill cites and none restates |

## Session kinds

Kris's three kinds, with the fourth actor every coordinator depends on:

| | Conversational | Coordination thread | State of play thread | Background run |
| --- | --- | --- | --- | --- |
| Works | one bounded matter, or regular or ad hoc work `<t>.regular[.<slug>]` | one Project's work, `<t>.<project>` | the territory, `<t>`, or a secondary `<t>.sop.<name>` | one brief |
| Opened by | Kris, in any repository | Kris, with the Project opener from `ki agent prompts <t>`, in the Capital | Kris, with the territory or secondary opener, in the Capital | a coordinator, through `ki agent` |
| `work.md` level | `regular`, or none | `project` | `territory` | the work it serves |
| Does substantive work | yes | no; bookkeeping and one-line fixes only | no; dispatch only | yes, within its authority footer |
| Reply form | plain reply; the completed-work owner report, without heading or banner, when a unit ends | coordinator forms with heading and banner | coordinator forms, `› State of play` | its brief's report rule |
| Skills it uses | the process skills directly (`ki-next`, `ki-plan`, `ki-implement`, `ki-accept`, `ki-recap`, `ki-work-design`); `ki-work-package` when it has an ad hoc folder | `ki-coordination`, `ki-delegation`, `ki-work-package`; brings `ki-accept` bundles; its runs use the process skills | the same, plus routing, the registry under `ki-work`, acceptance-first, `REVIEW-HOLD`, the worktree sweep and method stewardship | the process skill its brief names, `ki-git`, the target repository's governance skills by path |
| Hook and style | hook fires if the repository declares `ki-coordination`; the style says set it aside | both apply | both apply | hook silent; style not used |
| Commits | its own unit, by explicit path | its package at each unit, send, receive, mark and hold | the same, and one line into each receiving `messages.md` | its own unit, in its worktree |

Three things in this table are not yet written down anywhere as one rule:

- **Which kind a session is.** It is derived, at bootstrap step 3 of `ki-coordination`, from the opener matched against `work.md`'s `level`; a session with no opener is conversational. That works, but no section says "a session is one of three kinds", and the hook fires in a conversational session in the Capital, relying on the style's "set aside" paragraph (G4).
- **Regular work has no thread.** It is self-coordinating under the Capital's Activity notes and `ki-work-recurring`; State of play may talk about it and message it but does not dispatch it. Ad hoc work is worked conversationally, with a folder only when it needs one.
- **A background run is not a session kind for Kris.** He never talks to it; he sees it only through its coordinator. This is why every unit goes to one: the run carries the depth and the coordinator stays responsive.

## A coordination thread for every work package

Kris asked whether every work package can have its own coordination thread.

**Answer: yes for every Project package, one at a time, and only while it is active; never for regular or ad hoc packages; and territory packages always have theirs.**

- **What the skills allow.** Every Project package has an opener, printed by `ki agent prompts <territory>` from its `work.md`, so any registered Project's package can be opened as its own thread. The skills put no limit on the number of packages; the model forbids only two threads seated in one package at once.
- **What CASCADE-STEWARD adds.** Accepted on 25 October: each package has one assigned steward, by explicit assignment and acknowledged handover, never inferred. A thread is seated in one package and may act in the others it stewards, one package per turn. By default State of play stewards every package without a thread of its own, or the secondary covering it. So "its own thread" is the case where the steward is a thread seated in that package, and a package without one is never orphaned.
- **What limits it.** The territory cap of three or four active Project packages, now counting packages; about three runs per thread; and Kris's attention, capped at eight open queries and eight records to accept per work. Past four active threads Kris is the bottleneck, not the machine. A secondary State of play is the designed answer when one territory has more active work than one State of play can hold, as HNR's 5ge and sites show.
- **What it should not be.** A package for regular work or ad hoc work never gets a coordination thread: it has no runs of its own to coordinate. A dormant Project package should not keep a thread open; it goes On hold, and State of play holds it.

**Recommended practice**, which needs no new decision: open a thread for a Project package when it has active work to drive and a slot under the cap; let it steward only its own package unless Kris assigns it another; put it On hold when the wave ends, which hands stewardship back to State of play; and use a secondary State of play rather than raising the cap.

## The bootstrap path

### What "works really well" means

A bootstrap has worked when, without Kris correcting anything:

1. the session is named `<label> (<id>)` and its thread line matches `work.md`;
2. the first reply is the full re-bootstrap report, heading and banner exact, every open query in full;
3. `messages.md` was taken important lines first, and each line's disposition is committed;
4. `method_read` equals the harness revision and any change was named in one line;
5. `ki agent status` and the banner agree on what is running;
6. the next owner message gets an answer within one short turn, with no foreground wait.

### From a fresh machine

| Step | Command or surface | Owner today |
| --- | --- | --- |
| 1. Tools and checkouts | the workstation tooling (Rig, Homebrew tap) installs `ki`, `mgit` and `mcp-git-audit`; the repositories are cloned; `ki registry` owns their paths | Rig, `tools-ki` |
| 2. User environment | `chezmoi apply`: the CLAUDE files, the hook registered at `UserPromptSubmit` and `SessionStart`, `~/.claude/output-styles/ki-coordinator.md` linked to the primary harness checkout; credentials from the secret store, never the repository | chezmoi; described only in a `ki-coordination` paragraph |
| 3. Harness and process skills | `ki bootstrap`, then `ki skill add ki-work-design` | `ki-bootstrap`; the second step is unwritten (G3) |
| 4. Repository declarations | the Capital's `.ki.toml` declares `ki-work`, `ki-work-roadmap`, `ki-work-package`, `ki-delegation` and `ki-coordination`; `ki repo skill add` projects them; tracked `.claude/settings.json` selects `"outputStyle": "ki-coordinator"` | `ki-repo`, `ki-bootstrap` |
| 5. Check | `ki doctor`, `ki diag --full`, `ki repo audit --skill ki-coordination --repo <capital>` (the binding check), `mgit fetch` and the level check | each tool; no checklist names them together |
| 6. New session | runtimes re-scan only at start | `ki-bootstrap` |

Steps 2 and 5 are where a fresh machine fails silently: a missing hook or a stale style gives a coordinator that looks right and drifts, and nothing names the six checks as one readiness test.

### From a fresh session to a working coordinator

1. **Get the opener.** `ki agent prompts <territory>` prints it from `work.md`, never from a report.
2. **Start and name.** In the Capital's primary checkout, `claude --name "<label> (<id>)"` under THREAD-RENAME; an already-open session gets the `/rename` line the re-bootstrap report carries.
3. **Paste the opener.** `SessionStart` injects the hook line; the style is already selected.
4. **Bootstrap, in `ki-coordination`'s seven steps:** read the standard and the Work Process note; reconcile `ki agent status`; resolve the id and read the five files, `messages.md` first; compare `method_read`; check `level` against the opener; act on each message line, important first; as State of play, bring acceptance bundles first and, as the main, `REVIEW-HOLD`; strike a mark if none; give the full re-bootstrap report.
5. **Settle the heartbeat.** Arm the five-minute background check only if work lies with a worker.

Before step 1 on a host other than the last one, the repository level check runs; the package must be pulled level or the bootstrap reads stale state.

**Where it breaks today:** the refresh rule's path omits `ki-delegation` and the output style, so a change to either is missed (G2); the package can sit behind its remote on a new host; and a session opened outside the Capital gets neither hook nor style and has no way to know.

## Overlaps, gaps and contradictions

Each finding has a tag, the text against the rule, a recommended fix and the unit that owns the fix. "Decided" means a logged decision already authorises the fix; only the queries need Kris.

### Contradictions

| Tag | Where | Against | Recommended fix | Owner |
| --- | --- | --- | --- | --- |
| C1 PUSH-RULE | `ki-coordination` Notes, Pushing beneath other sessions, the output style; the Work Process note's On hold banner `[unpushed]` and "Kris pushes them" | PACKAGE-PUSH, 25 October: "Tonight's rule always", push everything stacked on `main` fast-forward only, stopping on divergence | rewrite the section to PACKAGE-PUSH, regenerate the style and hook, drop `[unpushed]` from the note. Decided | `ki-coordination`; the note through the ki-principal record |
| C2 COMMIT-WHEN | Work Process note "Only sends and the supervisor's receives commit"; States and moves "Only sends and the owner's receives commit" | COMMIT-CADENCE a); the standard's own Committing the work folder | the note's Git is the logbook says moves commit with move subjects and every complete unit commits too. Decided | the note, `ki-coordination` |
| C3 HOST | "no work package names a host" in `ki-coordination` Notes, Picking work up, `ki-work-package` | HOST-SEAT and HOST-TARGET, accepted in the high bloc | `work.md` may name a seat and a requirement from the machine inventory; `state.md` never names a host; requirements restrict execution only. Decided | `ki-work-package`, `ki-coordination` |
| C4 ONE-SESSION | Glossary "a session works at most one piece of coordinating work"; `ki-work-package` "a native session belongs to at most one piece of work" | CASCADE-STEWARD | "a session is seated in at most one package and may act in the packages it stewards, one per turn". Decided | both |
| C5 REPORT-HOME | `ki-delegation`: the run report is homed in the launching work's folder | CASCADE-REPORT | homed in the reporting package's folder, the work the run reports to. Decided | `ki-delegation` |
| C6 TURN-PACKAGE | the turn budget's reads and writes name "the work package" | CASCADE: one package per turn | "one package per turn", the cap counting packages. Decided | `ki-coordination` |
| C7 PULL-MODE | Putting work on hold: "pull with rebase" | COMMIT-CADENCE a) pull ff-only into a clean checkout; CONFLICT-RUN rebases only a run's own unpublished commits in its own worktree | the drain pulls ff-only and falls to CONFLICT-RUN on divergence. Decided | `ki-coordination`, the style |
| C8 NUMBERED | `ki-work-design` standard and `assets/decisions.md`: the owner's words "numbered against the report's decisions" | decisions carry tags, never numbers (14 October) | "keyed by the report's decision tags"; the brief's numbered reflection points can stay, being claims, not decisions. Mechanical | `ki-work-design` |
| C9 LANES | `ki-implement` step 4: with `ki-delegation` active, "bounded subagents execute the approved worker lanes" | rule 2: every unit of work goes to a detached background agent; an in-session subagent is not one | worker lanes go to `ki agent` runs when a coordinator holds the work; a background run delivering one record may still use bounded subagents inside itself. Decided by rule 2 | `ki-implement` |

### Gaps

| Tag | Gap | Recommended fix | Owner |
| --- | --- | --- | --- |
| G1 BOOTSTRAP-OWNER | no skill holds the path from a fresh machine to a working coordinator | see BOOT-HOME | query |
| G2 REFRESH-PATH | `method_read` compares only `ki-coordination` and `ki-work-package`; a change to `ki-delegation`, the output style or the Work Process note is missed | add `skills/governance/ki-delegation` and `output-styles/ki-coordinator.md` to the path; METHOD-NUDGE's hook warns when it lags | `ki-coordination` |
| G3 DESIGN-ACTIVATION | `ki-work-design` is not among the core skills `ki bootstrap` activates | add it to the core list, or name `ki skill add ki-work-design` in the bootstrap checklist | `ki-bootstrap`, `tools-ki` |
| G4 SESSION-KIND | no section says a session is one of three kinds, or how it knows | a short Session kinds section in `ki-coordination` beside Reply forms, from the table above | `ki-coordination` |
| G5 WINDOW-OWNER | the unattended window is spread over away grants and scheduled wakes (`ki-coordination`), authority tiers (`ki-delegation`), envelopes (`ki-batch`) and fields (`ki-work-roadmap`) | one Unattended window section in `ki-coordination`, as [unattended-work](unattended-work.md) proposes and the next section traces | `ki-coordination` |
| G6 WATCHER | the completion watcher has not shipped; session wakes are best effort | the window plan says so and depends on the coordinator's own check; the watcher stays `tools-ki`'s, first in line under OOS-WAKE | `tools-ki` |
| G7 LANDING | decided, not landed: COMMIT-CADENCE, PACKAGE-PUSH, COORD-COMMANDS (hold, drain, resume, send, receive), FINDINGS-SECTION (`findings/` in the closed list), THREAD-RENAME, METHOD-NUDGE, REVIEW-CHECK, the cascade set, the `unattended` and `target` fields | the harness record for coordination, work-package and delegation that [model-shape-report](model-shape-report.md)'s rollout names; one harness run, chained | harness |
| G8 PROJECT-LINK | nothing checks that a record's `project` resolves to a package, records exist with none, and there is no reverse view | a rubric item and WORK-STATUS-FORM's reverse view, as [overview](overview.md) sets | `ki-work-roadmap`, `tools-ki` |
| G9 CAPTURE-IN-WINDOW | CAPTURE-GATE forbids a run creating a record; PROGRESS-SCOPE lets runs progress existing records in the window; nothing says where a run's new finding goes | a run writes it into the package's `findings/` or a query; the coordinator captures at return. No conflict once written | `ki-coordination`, `ki-next` |
| G10 INITIATIVE | `ki-work-roadmap` still carries `initiative` | removed at the THEME-CLOSE cutover, 7 November 2026. Decided | `ki-work-roadmap` |

### Overlaps

| Tag | Overlap | Recommended boundary |
| --- | --- | --- |
| O1 RECAPS | `ki-recap` (one session), `ki-coordination`'s recap since the mark (one work) and the window's return report all "recap"; `ki-recap checkpoint <thread>` composes `ki-work-package` UPDATE | keep three forms with three scopes: session, work, window. The return report is a recap since the window's mark across the window's repositories, owned by `ki-coordination`. See RECAP-NAME for the checkpoint word |
| O2 REPORTS | the run report and the owner report | already resolved: `ki-coordination` owns the shape, `ki-delegation` links to it, both generated. Healthy |
| O3 AUTHORITY | the away grant and the `ki-batch` envelope both bound a window | the grant is the authority; each batch is a per-repository envelope inside it, citing it in `authority_evidence`, expiring no later than it and never widening it |
| O4 INTAKE | `ki-work-design`, `ki-next` capture and `messages.md` all take in new work | healthy as written: design for undecided shape, `ki-next` for known work the receiver owns, messages for handoffs and routes |
| O5 DECISIONS | the decisions log in `ki-coordination` and the launcher's part in `ki-delegation` | healthy: entry rules and life cycle in `ki-coordination`, adoption and the close gate in `ki-delegation` |

## The unattended window, end to end

The window as it should run once G5 lands, each step with its owning skill. Tonight's window ran this way from decisions in this package; the standard does not yet say it.

1. **Grant** (`ki-coordination`, away grants). Kris grants a window in words: end time, work, permitted actions, exclusions, wake and stop words. The coordinator logs it in `decisions.md` in that turn, the end written as local time with zone and UTC under WINDOW-CLOCK, the earlier instant taken when ambiguous. The grant is the authority; an `unattended` flag on a record is eligibility only.
2. **Entry** (`ki-coordination`, with `ki-delegation`'s deny-list). Strike the mark with each repository's origin and local revision; take the interactive pass so open queries are answered or packed and split; write the window plan into `state.md` under WINDOW-PLAN; run the entry checks; rank the units by value; add a `[window]` banner item. The window is an episode within With worker, not a state.
3. **Launch** (`ki-delegation`). Each unit goes to a detached run whose brief cites the grant, carries the deny-list and the target repository's standing rules, names the authority tier (none or push; never prune or release unless granted) and sets the progress protocol. Same-file units are chained; different repositories run in parallel; about three at once.
4. **Progress** (`ki-plan`, `ki-implement`, `ki-batch`). Under PROGRESS-SCOPE runs ready and deliver existing records in outcome waves; adoption, promotion, acceptance and pruning stay with Kris. New findings go to `findings/` or a query, not a record (G9).
5. **Commit and sync** (`ki-coordination`, `ki-git`). Every complete unit commits by explicit path before its turn ends; every third wake (about 15 minutes) the coordinator pulls ff-only and pushes everything stacked under PACKAGE-PUSH; a divergence starts a CONFLICT-RUN that rebases only that run's own unpublished commits and stops on anything else.
6. **Wake** (`ki-coordination` heartbeat). The coordinator's own five-minute check is the only wake, because the watcher has not shipped (G6). A usage-limit stop or a missed wake is logged as a failure mode, never treated as processed work.
7. **Queries** (`ki-coordination`, query review). Each new medium or low query goes to one blind review run; the result is held for return. Nothing waits on Kris mid-window.
8. **Expiry** (`ki-coordination`). At the end time, explicit return or "stop the wake", the coordinator stops launching; running units finish or stop at a safe point; nothing new starts in the last fifteen minutes. It does not drain unless Kris says `pause`.
9. **Return** (`ki-coordination`). A send: the return report is a recap since the window's mark across every repository the window touched, listing misses (failed runs, usage stops, missed wakes); then the interactive walk-through of queries; the next mark only after it.

The window has no new state, no new file and no new skill: it is a grant, a plan in `state.md`, a banner item and a recap. That is the over-engineering steer of 22 October applied.

## Queries

These have not had their blind review. The coordinator sends each to one before it reaches Kris.

### BOOT-HOME - Who owns the bootstrap from a fresh machine to a working coordinator

**Context:** `ki-bootstrap` covers the harness and skill activation and stops; `ki-coordination` starts at the opener. Between them, chezmoi's hook and style binding, the Capital's declarations, `ki skill add ki-work-design`, the six readiness checks and `ki agent prompts` with `claude --name` are written nowhere as one path, and a fresh machine can fail silently at the hook or the style. Kris's goal is that "when we do a bootstrap ... it works really well".

**Query:** Which skill holds the one bootstrap checklist?

**Options:**

a) (recommended, confidence medium - one owner per half keeps each skill's boundary; not yet reviewed) `ki-bootstrap` owns the machine half to step 6 and ends with a "Ready to coordinate" check, which `tools-ki` later backs with a `ki doctor` item; `ki-coordination`'s Bootstrap gains a "Before the opener" step that cites it, then owns the session half as now

b) `ki-coordination` owns the whole path, machine half included, and `ki-bootstrap` links to it

c) a guide in ki-principal under `Pillars/` owns the narrative, and both skills link to it

### TRADES-FATE - What becomes of ki-trades now its hold is overdue

**Context:** `ki-trades` is on hold with a review due by 21 October 2026, now four days past, and its `HOLD-1` audit item warns. Existing trades keep full support. HANDOFF-AS-MESSAGE moved handoffs and rollouts to `messages.md`, so it governs only the trade routes `.ki.toml` declares. The planned [Trades revamp](../../../../Streams/Projects/trades-revamp.md) Project's outcome is a succinct trade policy that grants the same, which is that narrower job.

**Query:** Should `ki-trades` be narrowed now or kept on hold?

**Options:**

a) (recommended, confidence medium - matches what HANDOFF-AS-MESSAGE already decided and costs one bounded edit; not yet reviewed) narrow it to declared routes only, with a pointer to `messages.md` for everything else, and set its next review to the Trades revamp's opening

b) keep it on hold with a new review date, untouched until the Trades revamp opens

### RECAP-NAME - What ki-recap's checkpoint argument is called

**Context:** `ki-recap` offers `checkpoint <thread>`, which composes `ki-work-package` UPDATE. "Thread" is now the word for a session acting on work; the argument is in fact a work id. The three recap forms (session, work, window) otherwise have clean scopes.

**Query:** Should the argument become `checkpoint <work id>`?

**Options:**

a) (recommended, confidence high - the model made work the unit and the argument already resolves an id; not yet reviewed) rename it to `checkpoint <work id>`, accepting the old word through the tolerance window

b) keep `checkpoint <thread>` and define it in the Glossary as the work the thread carries

## Rollout notes

No implementation is proposed here. When Kris has sanity-checked the model, the fixes fall into three bundles, each through its owning repository's process:

1. **The harness run already named** for coordination, work-package and delegation (G7) takes C1 to C7, C9, G2, G4, G5 and G9, and regenerates the hook and style once. It is chained after tonight's COMMIT-CADENCE run, since both edit the coordination standard.
2. **A ki-principal record** for the Work Process note and GDR-KI-PRINCIPAL-009 takes C1's and C2's halves in the note, under the Enactment Process.
3. **Small mechanical edits** take C8, G3, G10 and whichever answers BOOT-HOME, TRADES-FATE and RECAP-NAME bring; `tools-ki` takes G6 and G8's checks as lines in the tools-burndown work's `messages.md`, under HANDOFF-AS-MESSAGE.

The pilot stays as [unattended-work](unattended-work.md) set it: ki.ways-of-working first, then Personal. The bootstrap checklist is tested by opening one dormant Project package on a second Mac from a fresh session and scoring it against the six "works really well" outcomes.
