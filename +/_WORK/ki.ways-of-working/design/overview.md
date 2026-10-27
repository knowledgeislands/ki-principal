---
note_type: streams/design
updated: 2026-10-25T01:20:00Z
author: Written with Claude
---

# Ways of working: overview

**Owner:** Kris Brown · **Owning repository:** knowledgeislands/ki-principal · **Owning work:** `ki.ways-of-working` · **Date:** 2026-10-25, written during the unattended window opened at the 01:07 GMT mark

**Status:** a ten-minute morning read, standing at the 01:07 GMT mark plus the read-backs at 01:10 GMT. It decides nothing and changes no standard. Kris asked for "a really high level summary of all the ways of working enhancements that we've talked about doing what we plan to do with them", a "really quick think" on where work packages are homed against roadmap items across repositories, and where the messages stand. The skill-set definition pass Kris asked for at 01:10 GMT ("I want the set of skills to be well defined around this") follows this note and builds on it.

The work package is [work.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/work.md), [state.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/state.md), [queries.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/queries.md), [messages.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/messages.md) and [decisions.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/decisions.md). Query tags below are the open queries in `queries.md` unless marked as draft queries in the [unattended-work brief](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/unattended-work.md).

## 1. Enhancements

Status words: **landed** (with the revision), **decided** (owner answer logged, not yet in the standard), **open** (a query with Kris, with its recommended option), **draft** (a draft query in a design brief not yet with Kris), **idea**, or **needs an owner**.

| Theme | Enhancement | Kris's ask, in brief | Status | Next step |
| --- | --- | --- | --- | --- |
| Reports and Summary | Re-bootstrap report and gap Summary | One report shape after a reboot or a long gap | Landed, harness `8cc42754` (REBOOT-SHAPE, GAP-SUMMARY) | None |
| | Summary window on the mark | Summary covers what changed since the mark, and what is still outstanding (SUMMARY-SINCE-MARK, SUMMARY-OUTSTANDING) | Decided, SUMMARY-WINDOW a) "Window on mark", 01:10 GMT | Harness coordination-standard run tonight |
| | Findings section | Carry findings, and the prompts behind them, in full in the report (FINDINGS-SECTION, PROMPTS-IN-FULL) | Open, FINDINGS-SECTION a) high | Kris answers; [findings](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/findings.md) holds the design |
| | One Summary across packages | One report when a coordinator steers several packages | Open, CASCADE-REPORT a) high | Kris answers |
| | Drain line | An explicit DRAINED / NOT DRAINED line at a drain | Open, DRAIN-END a) high | Kris answers |
| Queries | Split packed queries, interactive pass | Unpack bundled queries; take them interactively one or two at a time (SPLIT-QUERIES) | Open, QUERY-RULES a) high | Kris answers; the unattended brief leans on it |
| | Two-recommendation check | The rubric flags a query with two recommended options | Open, REVIEW-CHECK a) high | Kris answers |
| | Method nudge | Warn when a coordinator's `method_read` lags the standard | Open, METHOD-NUDGE a) high | Kris answers |
| | Unwritten rules | Confirm each of four unwritten habits one by one (UNWRITTEN-RULES) | Decided 23 Oct: none becomes a standing instruction; the one-by-one confirmation is not yet asked | Split into one query per rule |
| Commits and sync | Commit cadence | Commit and sync often enough that nothing drifts | Decided, COMMIT-CADENCE a) "Adopt cadence" | Harness coordination-standard run tonight |
| | Push scope in a window | Push all stacked commits while Kris is away | Decided, SYNC-SCOPE "Push all stacked", this window only | Applies until the window ends |
| | Pushing others' commits stacked beneath | Push another session's work-folder commits beneath one's own | Open, PACKAGE-PUSH a) medium, a bounded grant | Kris answers |
| | Operation cache rule | Keep operation caches out of commits | Landed, harness `1ec09f15` | None |
| Unattended work | Unattended window as a unit | A mark at entry, a plan, unpacked queries, roadmap progress, a return walk-through | Draft, [unattended-work brief](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/unattended-work.md) (`f7a2f0da`), reviews to follow | wow-unattended finishes the brief; blind reviews; merged report |
| | Wake substrate | Wake reliably while away (WAKE-SUBSTRATE) | Decided 23 Oct: completion watcher first, launchd deferred; in the style and standard; the watcher has not shipped | Build the completion watcher |
| | Away grant and deny-list | A standing shape for "while I am away" grants (AWAY-GRANT) | Grant rule landed in the standard and style; the deny-list is draft DENY-LIST | Unattended brief |
| | Unattended and due flags on records | Mark records safe to do unattended, and give them due or milestone dates (UNATTENDED-AND-DUE-DATES) | Draft, UNATTENDED-FIELD and DUE-FIELD | Unattended brief; tending's open "Due dates" question waits on it |
| | Window clock | An end time that cannot be read two ways | Draft, WINDOW-CLOCK | Unattended brief; see the note on tonight's end time under section 4 |
| | Run secrets | Runs read secrets only through the chezmoi helpers | Open, RUN-SECRETS a) high, Cloudflare half only | Kris answers |
| Cascade and stewardship | Secondary States of play | `<territory>.sop.<name>` with `parent` and `covers` | Landed, harness `703384eb`, tools-ki `5da74e0a` | None |
| | State of play looks after packageless Projects | Projects without a package are cared for (SOP-PROJECT-CARE) | Open, CASCADE-STEWARD a) high and STEWARD-FIELD a) medium | Kris answers; pilot in Valle Armonia |
| | One thread or many | A single thread, or a coordination thread per package (SINGLE-THREAD; Kris at 01:10 GMT) | Folded into the model-shape queries; the per-package question goes to the skill-set pass | Skill-set definition pass |
| | Thread naming | Name the coordination thread at launch and say so at bootstrap (THREAD-RENAME, IMPORTANT) | Open, THREAD-RENAME a) high, asked again | Kris answers before the KI State of play bootstraps on Sol |
| | Coordinator commands | Explicit hold, drain, resume, send and receive words (COORD-COMMANDS) | Open, COORD-COMMANDS a) medium, the blind review disagrees | Kris answers |
| | Decision homes and theme close | Home old State of play decisions; set when Initiatives stop being accepted | Open, DECISION-HOMES a) high, THEME-CLOSE a) high (7 Nov 2026 cutover) | Kris answers |
| Hosts | Host seat against host requirement | A package states what host it needs, never which seat it sits on (COORDINATOR-HOST) | Open, HOST-SEAT a) high, HOST-TARGET a) high | Kris answers; pilot in `ki.chezmoi` |
| | Proxy shaper | Whether the Headroom shaper and compression stay on in coordinator sessions | Open, PROXY-SHAPER a) medium, the review would turn it off, which is connection-critical | Kris answers; [KI-HARNESS-GOV-204](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/ideas/KI-HARNESS-GOV-204-pretooluse-quietening-hook.md) evidence review is due |
| Metadata and relations | Package relations | `parent` on every package, `covers` kept; how a record relates to its package | Open, RELATIONS a) high | Kris answers |
| | Work status form | One status form the CLI views share (WORK-STATUS-FORM) | Routed to `ki.tools-burndown` | `ki.tools-burndown` owns it |
| | Repository storage declarations | Repositories declare their storage | Draft record [KI-HARNESS-GOV-227](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/ideas/KI-HARNESS-GOV-227-repository-storage-declarations.md), project observatory; [schema draft](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/gov-227-storage-schema.md) here | `ki.observatory` plans it |
| | Where `ki-repo` work lives | Which work carries `ki-repo` changes | Open, KI-REPO-HOME a) high after review: `ki.baseline-rollout` | Kris answers |
| | Legacy prefixes and partial repositories | Old record prefixes; repositories only partly in the model | Open, LEGACY-PREFIX and PARTIAL-REPOS, both medium, the reviews disagree | Kris answers |
| | Private-safe diagram citations | A citation form for private sources in published diagrams (DIAGRAM-PRIVATE-CITATIONS) | Needs an owner; blocks [PERSONAL-TOWER-SITE-019](/Users/krisbrown/workspaces/personal/apps-tower.midnight.ninja/docs/roadmap/PERSONAL-TOWER-SITE-019-redraw-mermaid-in-archify.md) (named PERSONAL-TOWER-SITE-019 in the line) | Route to the `ki-diagrams` owner |
| Roadmap | Size label | 👕 plus a capital letter, no XS, in `ki-work-roadmap` (SIZE-LABEL) | Kept in the queue, outside the grant | Harness run once Kris confirms |
| | ARM release record | Cancel the conditional ARM Linux release record | Open, SORT-ARM a) high, on [KI-TOOL-KI-CLI-125](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/ideas/KI-TOOL-KI-CLI-125-ki-release-contract.md) | Kris answers |
| | Central tick | One central heartbeat rather than a wake per session (CENTRAL-TICK) | Idea | Add as an idea on the [Project note](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) |
| | Cloudflare production branch | Amend the Cloudflare hosting standard, sections 5 and 6 (CF-PRODUCTION-BRANCH, from HNR) | Needs an owner | Route to the `ki-repo-website-cloudflare` owner |
| Tending | Tending, structural and PMO tracks | Regular care of a territory's packages and roadmap, with dispositions | Draft, [tending](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/tending.md); interim policy in Valle Armonia and Personal | Fold the second round; settle its open questions, including member packages from the Capital |
| | Work Process note | Fold tonight's method lines into the Work Process note (WORK-PROCESS-NOTE) | Next step | Through the Enactment Process with its record |
| | Rubric label check | Optional `label` check in the coordination rubric (COORD2-RUBRIC) | Next step; the title half landed in harness `0aa9c4d2` | One-line fix at [coordination.ts:372](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/scripts/rubric/contexts/coordination.ts) in the next coordination-standard run |

Taken together: two decided answers (COMMIT-CADENCE, SUMMARY-WINDOW) are ready to land tonight; twenty-two queries are open, almost all with a high-confidence recommendation; the unattended and tending designs are drafts; three lines need an owner outside this work.

## 2. Packages against roadmap records

### What the standards say now

- **Package home.** A package lives in `+/_WORK/<id>/` in the repository that owns the work, one per piece of work above a work item; a work item has no package, because its record is its home ([work-package standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-work-package/references/standards-work-package.md)). Only a Capital holds territory work ([coordination standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md)). Nothing says where a Project package lives; in practice every one is in its Capital, as `<territory>.<project>`.
- **Record home.** A record lives in the roadmap of the repository that owns it (`docs/roadmap/` or `Streams/Roadmap/`), and that repository owns its priority, plan and acceptance. Handoffs travel as messages, never as records (HANDOFF-AS-MESSAGE).
- **How a record finds its package.** A record's `project` names a slug in the Capital's `Streams/Projects/<slug>.md`, written `<territory>/<slug>` across territories; the package id follows as `<territory>.<slug>` ([Project registry](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-work/references/standards-project-registry.md)). Links point upward only: a Project note lists no records, and the tag confers membership, not authority. Project work works only its own Project's records, wherever they are.

### How it plays out

| Territory | Repositories | Records | Repositories holding records | Packages, all in the Capital |
| --- | --- | --- | --- | --- |
| KI | 24 | 64 | 11 | 16 |
| HNR | 28 | 116 | 20 | 25, mostly one per Project |
| Valle Armonia | 4 | 46 | 3 | 3 (`va`, `va.community-website`, `va.markhowarth-launch`) |

**Many repositories (KI, HNR).** The shape holds: packages gather in the Capital, records stay with the code they change, and `project` joins them. A Project such as `ki.ways-of-working` has records in ki-principal and tools-ki. What it lacks is the reverse view: finding a Project's records means scanning every roadmap, which the work status views ([KI-TOOL-KI-CLI-149](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/ideas/KI-TOOL-KI-CLI-149-work-status-views-contract.md), [KI-TOOL-KI-CLI-160](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-160-work-status-routing-view.md)) are meant to give once WORK-STATUS-FORM settles. Records with no `project` belong to no package: [KI-HARNESS-GOV-202](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-202-skill-area-stable-stats-badge.md), [KI-HARNESS-OPS-009](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/ideas/KI-HARNESS-OPS-009-complete-ai-session-acquisition.md) and [KI-HARNESS-REV-012](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/ideas/KI-HARNESS-REV-012-thoughtworks-radar-input.md) in the harness, and the four acquisition triage records KI-TOOL-KI-CLI-168 to 171 in tools-ki, are such orphans. ki-agentic-harness also has no work package of its own, the shape KI-REPO-HOME is circling.

**Few repositories (Valle Armonia).** Six Projects, three packages. Four Projects have records but no package: knowledge-intake (6), sanctuary-library (5), social-and-identity (2) and territory-alignment (1). Under CASCADE-STEWARD the State of play looks after them until one needs its own package. A small territory may never want a package per Project, and the model should not push it there.

**The gaps.**

1. No standard says a Project package lives in the Capital, though every one does.
2. A member repository can hold a package: [personal.regular.acquire-intake](/Users/krisbrown/workspaces/personal/acquire/+/_WORK/personal.regular.acquire-intake/work.md) sits in `personal/acquire`. The rubric bars only territory work outside a Capital, so this is allowed but undeclared.
3. Nothing checks that a record's `project` resolves, or that a Project with live records has a package or a steward. Tending already names the first as a mechanical-check candidate (VA-WEBSITE-SANC-011 names a Project that does not resolve).
4. The reverse view, Project to records, waits on WORK-STATUS-FORM.

### Options

- **A. Packages in the Capital, records where they belong (recommended).** Write down what is already true: every Project package lives in the Capital, records stay in their owning repositories, and `project` is the only link. The State of play stewards packageless Projects and seeds a package on first need. Add one mechanical check, in tending or the rubric, that every record's `project` resolves. Regular work in a member repository may keep its package there, declared in its `work.md`. No migration; fits all three territories as they stand; keeps to the over-engineering steer.
- **B. Package beside its records.** A Project package lives in the repository holding most of its records, such as `ki.tools-burndown` in tools-ki. Closer to the code, but Projects span repositories, the Capital loses its single view, and a Project whose records move would have to move its package too.
- **C. Records inside the package.** A Project's records live in its package or the Capital's roadmap. One place to look, but it overturns repository ownership of records and HANDOFF-AS-MESSAGE, and needs a large migration.

### Queries this needs

Named here, not decided; each is separate so that it can be answered alone.

- **PACKAGE-HOME** - whether the standard says every Project package lives in its Capital (option A against B).
- **MEMBER-PACKAGE** - whether a member repository may hold a package for its own regular work, declared in its `work.md`.
- **RECORD-RESOLVES** - whether a mechanical check flags a record whose `project` does not resolve, and where it runs (tending or the rubric).

They touch RELATIONS, CASCADE-STEWARD and KI-REPO-HOME, and should be asked alongside them.

## 3. Message queue

Seventeen lines remain in [messages.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/messages.md), in queue order.

| Line | Disposition | Where |
| --- | --- | --- |
| UNATTENDED-AND-DUE-DATES (Personal) | Covered by draft queries | UNATTENDED-FIELD and DUE-FIELD in the unattended brief |
| DIAGRAM-PRIVATE-CITATIONS (Personal) | Needs an owner; outside this scope; blocks the record beside it | [PERSONAL-TOWER-SITE-019](/Users/krisbrown/workspaces/personal/apps-tower.midnight.ninja/docs/roadmap/PERSONAL-TOWER-SITE-019-redraw-mermaid-in-archify.md) (named PERSONAL-TOWER-SITE-019 in the line); return to State of play for the `ki-diagrams` owner |
| SUMMARY-OUTSTANDING (Valle Armonia) | Covered by a decided answer, not yet landed | SUMMARY-WINDOW a); coordination-standard run |
| COORDINATOR-HOST (chezmoi) | Covered by open queries | HOST-SEAT, HOST-TARGET |
| COORD-COMMANDS | Covered by an open query | COORD-COMMANDS |
| SUMMARY-SINCE-MARK | Covered by a decided answer, not yet landed | SUMMARY-WINDOW a) |
| SOP-PROJECT-CARE | Covered by open queries | CASCADE-STEWARD, STEWARD-FIELD, RELATIONS |
| SINGLE-THREAD | Covered by the model-shape queries; the per-package thread question is a next step | Skill-set definition pass |
| FINDINGS-SECTION | Covered by an open query | FINDINGS-SECTION |
| SPLIT-QUERIES | Covered by an open query | QUERY-RULES |
| WAKE-SUBSTRATE | Carried: decided 23 Oct and in the style and standard; can be removed | The completion watcher, still to build |
| AWAY-GRANT | Carried for the grant rule; the deny-list is a draft query | DENY-LIST in the unattended brief |
| UNWRITTEN-RULES | Next step: one query per rule; none written yet | `queries.md` |
| PROMPTS-IN-FULL | Covered by an open query | FINDINGS-SECTION, its carrying-prompts part |
| IMPORTANT THREAD-RENAME | Covered by an open query, asked again; wanted before the KI State of play bootstraps on Sol | THREAD-RENAME |
| CF-PRODUCTION-BRANCH (HNR) | Needs an owner; outside this scope | Return to State of play for the `ki-repo-website-cloudflare` owner, likely `ki.baseline-rollout` |
| SIZE-LABEL | Next step, kept outside the grant; this work owns record fields | Harness run once Kris confirms |

WAKE-SUBSTRATE can go now; SUMMARY-SINCE-MARK and SUMMARY-OUTSTANDING go once SUMMARY-WINDOW lands; DIAGRAM-PRIVATE-CITATIONS and CF-PRODUCTION-BRANCH go back to State of play for an owner; the rest wait on Kris's answers or a next step.

## 4. Roadmap in this area

Records whose `project` is `ways-of-working`, and the nearby records this package steers. None of them can move tonight without Kris; what can move unattended is package work under decided answers.

**Can progress unattended tonight, on decided answers.**

- The coordination-standard run landing COMMIT-CADENCE a) and SUMMARY-WINDOW a), with the COORD2-RUBRIC label fix at [coordination.ts:372](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/scripts/rubric/contexts/coordination.ts) folded in. Package work; no record.
- The CENTRAL-TICK idea line on the [Project note](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md).
- The WORK-PROCESS-NOTE fold, through the Enactment Process with its record.
- The unattended-work brief through blind review to a merged report, deciding nothing.

**Need Kris.**

| Record | Status | What it waits on |
| --- | --- | --- |
| [KI-PRINCIPAL-OPS-014 (pruned)](https://github.com/knowledgeislands/ki-principal/blob/da027e6d/Streams/Roadmap/KI-PRINCIPAL-OPS-014-gfm-conversion.md) | Now, awaiting review | Kris's acceptance (ACCEPT); runs cannot accept |
| [KI-PRINCIPAL-MOD-009 (pruned)](https://github.com/knowledgeislands/ki-principal/blob/da027e6d/Streams/Roadmap/KI-PRINCIPAL-MOD-009-amend-adr-001-staging-wording.md) | Now, awaiting review | Kris's acceptance (ACCEPT) |
| [KI-HARNESS-GOV-204](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/ideas/KI-HARNESS-GOV-204-pretooluse-quietening-hook.md) | Hold, review date 2026-10-24, now due | Kris reviews a week of evidence from the quiet cuts; bears on PROXY-SHAPER |

**Blocked on a query or another work.**

| Record | Status | Blocked on |
| --- | --- | --- |
| [KI-TOOL-KI-CLI-145](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/ideas/KI-TOOL-KI-CLI-145-thread-session-bindings-role.md) | Soon, draft | THREAD-RENAME |
| [KI-TOOL-KI-CLI-160](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-160-work-status-routing-view.md) | Soon, draft | WORK-STATUS-FORM, with `ki.tools-burndown` |
| [KI-TOOL-KI-CLI-149](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/ideas/KI-TOOL-KI-CLI-149-work-status-views-contract.md) | Soon, draft; project observatory | WORK-STATUS-FORM |
| [KI-TOOL-KI-CLI-125](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/ideas/KI-TOOL-KI-CLI-125-ki-release-contract.md) | Hold; project agent-host | SORT-ARM |
| [KI-HARNESS-GOV-227](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/ideas/KI-HARNESS-GOV-227-repository-storage-declarations.md) | Next, draft; project observatory | Not blocked, but `ki.observatory` owns its planning; the schema draft here could go to it as a message |

**Tonight's end time.** The grant was read back at 01:07 GMT as ending at 08:00 GMT. Kris said "until 9 a.m.", at 01:31 BST, before British Summer Time ended; 9 a.m. on the wall clock this morning is 09:00 GMT. The window stops an hour early on the safe side; draft WINDOW-CLOCK addresses it for future windows.
