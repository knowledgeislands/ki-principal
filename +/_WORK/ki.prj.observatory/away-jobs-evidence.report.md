# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › away-jobs-evidence

**🤖 → 👤 Handoff to supervisor · Run report at 01:12 GMT · last mark 01:04 GMT**

---

## Done

- Diagnosed the false-healthy mechanism with exact source predicates and isolated fixtures; no product, producer, work-package or scheduler changes and no commits.
- Final report validation passed: required sections, finding metadata, local links, thread line and unchanged source snapshot.
- Focused existing contract, evidence-port and viewer tests: 60 passed, 0 failed, 247 assertions; all schedule/process ports were fixtures.
- Producer classification reproduction: the extracted Python classifier returned `ok` for an agent success result whose final text contained a failed move; the text survived unchanged in the detail file. No wrapper, job or provider was invoked.
- Consumer reproduction: real `observeAutomation` with in-memory reporter files showed latest and five recent outcomes as `ok`, standing `ok`, and zero Beacon signals despite failed work in detail. Correctly reported `findings` propagated to latest, history and Beacon.
- Exact identity/configuration checks passed: reporter job `hnr-email-route-triage` matches Rig declaration ID, differs from launchd locator `uk.me.kris.rig.hnr-email-route-triage`, and is selected only by the laptop profile; its calendar has 65 records.
- Local evidence inventory passed: sol.local has 72 reporter history records, 18 each for four other jobs, and no Route Triage latest or history record. The reported six failures among fifteen runs remains incoming evidence, not an independently reproduced empirical count.
- Read the full run inbox repeatedly, including before verification and report completion; queue-writing and Git-window instructions addressed to other units were not acted on.

## In Progress

Nothing is running in this unit. The read-only investigation is complete; implementation, tracked documentation and any cross-package receipt remain with the coordinating owner under a separate bounded delivery brief.

Outstanding — no action requested now: a producer correction belongs to `ki.prj.chezmoi`; historical Route Triage records from the reporting host are needed to validate the six-of-fifteen claim and a robust compatibility parser. Do not retrieve them remotely under this brief. No service restart is due from this evidence-only pass.

## Findings

### OUTCOME-LOSS - Agent completion becomes job success before domain failures are classified

**Goal:** Explain why a run containing failed moves or tool calls reads healthy.

**Scope:** Local chezmoi source, its byte-identical installed scheduled scripts, the canonical Route Triage prompt and Observatory's actual parsing/projection functions. No provider output or secrets were inspected.

**As of:** 29 October 2026, 01:12 GMT, sol.local; no remote parity is claimed.

The first semantic loss is the shared agent wrapper. `scheduled_agent_run` considers Claude's result successful when `subtype == "success"` and `is_error is False`, subject to process exit, timeout and budget checks. That means the agent completed its turn successfully; it does not mean all attempted mailbox operations succeeded. The Route Triage executable then calls `scheduled_agent_finish` without arguments, which defaults to `ok`, notification policy `never`, and summary `Route Triage completed.`. `say` sends the final agent text as `--detail`. The reporter persists that detail, so the failure prose is retained on disk even though the machine outcome has already lost its meaning.

The second boundary is intentional information exclusion: Observatory `parseRun` validates and retains only `job`, `status`, `summary` and `finished`. It deliberately discards `detail` for privacy. It therefore sees the generic completion summary and the stated `ok`, not the prompt's readable Failures line. Reading the current record's `summary` alone cannot repair this case. The requested alternative of reading a summary's Failures section means parsing the final agent summary stored inside `detail`, in the backend, rather than handing raw detail to the browser.

The prompt explicitly requires every move, save or tool failure in `Failures`, and includes failures under `Needs you`. These are two different concerns: execution outcome and actionable/domain findings. A completed agent turn can legitimately produce `findings`; an agent/process failure should remain `failed`. Human judgement requests, flagged mail and low-confidence shadow verdicts can also be findings without any execution failure. A failure-evidence parser alone does not capture all those other findings.

Exact local source anchors:

- [shared wrapper](/Users/krisbrown/.local/share/chezmoi/bin/scheduled/scheduled_agent.bash:258): result classification; finish defaults near line 296; `say` near line 39.
- [Route Triage executable](/Users/krisbrown/.local/share/chezmoi/bin/scheduled/executable_rig-hnr-email-route-triage:9): short reporter ID; final calls are `scheduled_agent_run "$model"` and argument-free `scheduled_agent_finish`.
- [reporter](/Users/krisbrown/.local/share/chezmoi/bin/scheduled/executable_report:146): terminal JSON construction and optional `detail`/`run_id`; it records the supplied status rather than interpreting detail.
- [canonical Route Triage activity](</Users/krisbrown/workspaces/humans-not-robots/hnr-principal/Admin/Knowledge Management/Regular Activities/Email/Route Triage.md:168>): required final readable summary. Its `runs.jsonl` ledger is explicitly absent; it must not be invented as a current source.
- [consumer parser](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/contracts/src/automation.ts:132): no detail crosses the contract; [evidence port](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/evidence/src/automation.ts:197) applies this to latest and historical records.

The exact predicates verified that installed `report`, `scheduled_agent.bash` and `rig-hnr-email-route-triage` match their chezmoi source bytes; the executable sets the expected short ID and ends with the default finish call. A pure extracted classifier fixture, not a job invocation, demonstrated the successful-turn/failed-operation combination. The consumer fixture independently demonstrated the resulting false healthy latest and recent views.

### REPORT-CONTRACT - Proposed Observatory-owned scheduled reporting specification

**Goal:** Supply concrete content for SCHEDULED-REPORT-SPEC without editing tracked documentation.

**Scope:** Proposed `docs/specs/automation.md` area and `docs/specs/index.md` entry, alongside the existing `observatory/automation/v1` registration in `docs/specs/contracts.md`. Candidate requirements below are report content only; no identifiers are allocated and no new behaviour is silently accepted.

**As of:** 29 October 2026, 01:12 GMT; confirmed against local implementation and focused tests.

The specification should describe the consumer contract and link producer evidence, keeping ownership clear: chezmoi owns reporting and wrapper semantics, Rig owns declaration and schedule semantics, Observatory owns its projection, privacy boundary, freshness judgement and presentation. Wider specification reorganisation is outside the request.

**Reporter input and identity — proposed requirement, current behaviour conforms.** The backend MUST resolve its reporter directory from nonempty `SCHEDULED_REPORT_STATE`, otherwise nonempty `XDG_STATE_HOME` plus `scheduled-jobs`, otherwise `~/.local/state/scheduled-jobs`. Each nonhidden `<job>.json` creates one observed job row. A missing reporter directory is unobserved, distinct from an observed empty directory. The reporter's `job` MUST match Rig's unqualified scheduled-job `id`, not its `locator`, display name or `scheduled-job:ID` selector. A record naming a different job than its filename becomes unreadable. Verify with directory-resolution, malformed-record and exact-ID fixtures in `packages/evidence/src/automation.test.ts`.

**Terminal record — proposed requirement, current terminal behaviour conforms.** The reader MUST require `status` to be exactly `ok`, `findings` or `failed`, a nonempty summary and a parseable finish timestamp. Unknown status, malformed JSON, missing/invalid finish or empty summary MUST become unreadable, never silently healthy. `job` identifies the history row; an unattributable recent history line is counted. Producer terminal fields are `job: string`, `status: ok|findings|failed`, `summary: string`, `finished: UTC ISO timestamp`, optionally `detail: string` and `run_id: string`. The consumer currently uses `Date.parse`, which accepts more than strict UTC ISO; document that difference rather than claiming strict timestamp enforcement. Verify in contract and evidence tests.

**Lifecycle compatibility — specification gap requiring explicit disposition.** The local reporter also supports start records with `job`, `status: "started"`, summary `No terminal report yet.`, `started` and `run_id`, but no `finished`. Start writes latest only; terminal writes history. Run IDs deduplicate terminal reports, and an older run's terminal result is retained in history without overwriting a newer latest identity. Observatory currently treats `started` as unreadable; the fixture verified this. Do not describe current support as a running-job view, and do not fold lifecycle support into this failure repair without planning it. Reporter writes soft-fail and are not guaranteed transactions across history and latest; latest is replaced atomically while history is append-only and never trimmed. The consumer does not use `run_id` or `started`.

**Latest and recent results — proposed requirement, current behaviour conforms.** The view MUST show each latest record's outcome, summary and finish, and offer at most five history records per job, newest first. Latest is read from `<job>.json`; it is not synthesized from the newest history timestamp. History is consumed in append order backwards and truncated per job, not timestamp-sorted or deduplicated by this reader. Missing/unreadable history MUST preserve latest rows with an explanation. Backward reading stops once every filename-known job has five runs, or reaches the file start; unattributed-line counts describe only the portion read. Jobs existing only in history or only in Rig declarations do not currently create rows. Verify history-tail tests, missing/partial history tests and viewer expansion tests.

**Rig projection — proposed requirement, current behaviour conforms to implementation evidence.** The backend MUST retain only `id`, `desired` and `schedule` from `kind == "scheduled-job"` resources of `rig show --format json`. No locator, program, environment or other declaration content reaches this projection. The exact ID join for Route Triage is `hnr-email-route-triage`; the launchd label is operational identity, not reporter identity. Absence from this host's selected profile is not proof of an unmanaged scheduler job. Verify `parseRigScheduledJobs` projection and missing/disabled/matched schedule tests. Rig's RIG-CONF-016 owns declaration fields; RIG-STATE-033 owns JSON projection generally. The current schedule string encoding is demonstrated by `rig_resource_schedule_summary` in tools-rig `src/rig/30-commands.bash:1574`, rather than a separately versioned schedule schema promise.

**Schedule encoding and freshness — proposed requirement, current behaviour conforms.** Read exactly `interval:<positive decimal seconds>` or `calendar:<comma-separated key=value record>[;<record>...]`. Calendar keys are unique `minute`, `hour`, `day`, `weekday`, `month`; bounds are respectively 0–59, 0–23, 1–31, 0–7 and 1–12. Weekday 0 and 7 mean Sunday; fields not supplied are unconstrained, calendar records are alternatives, and day/weekday together use the existing OR semantics. Unknown fields, repeated fields, empty calendars or invalid intervals are refused with safe reasons. Calendar evaluation uses the host's timezone and looks back at most 400 days. A readable job is overdue strictly after the most recent scheduled run plus two hours if its latest finish predates that run; interval jobs use latest finish plus interval plus two hours. Disabled declarations are never overdue. Unknown/missing/unreadable schedules use strictly more than 26 hours since finish, with the fallback reason shown. Unreadable records are not additionally marked overdue. Verify calendar, interval, disabled, fallback, weekday/weekend, DST skip/repeat and exact-boundary tests.

**Status, standing and attention — proposed requirement, current behaviour conforms to stated inputs.** Preserve outcome separately from freshness: rank `failed`, `unreadable`, `overdue`, `findings`, `ok`, then job ID. A status may remain `ok` while standing is overdue. Failed, unreadable and overdue produce attention signals; findings produce a note. Each signal's subject has a visible job row. Historical failures remain visible in recent runs but do not independently make a latest-healthy job emit a Beacon failure signal. A request for historical alerts would be an additional product decision. Verify contract ranking/signals tests and viewer signal-landing test.

**Privacy and mechanical operation — proposed requirement, current behaviour conforms.** The browser MUST receive only typed projection data with redacted summaries; raw detail, state directory, credentials, provider declarations and local paths MUST remain backend-local. Missing Rig or reporter evidence MUST yield an explicit degraded observation without invoking a job or requiring an LLM/provider MCP. Existing focused tests cover redaction, omitted detail, missing sources, invalid Rig answers and timeouts. The full product mechanical-first gate remains `apps/site/src/degraded.test.ts`; it was not executed here because it starts local services, prohibited by this brief.

**Failure evidence — proposed unnumbered Gap, current product lacks this behaviour.** Completed agent runs whose retained final summary positively states failed moves/saves/tools should be visible as findings, both latest and recent, while preserving the producer's reported execution outcome. Missing detail, an omitted Failures line, explicit no-failure values and unrecognized/ambiguous prose need distinct treatment; absence of parseable evidence cannot prove all work succeeded. This changes accepted projection semantics and requires a planned consumer change, or producer correction, before a requirement is promoted as conforming.

### FOLLOW-UP - Smallest consumer repair and receiver-owned correction

**Goal:** Bound subsequent work without changing another package or lifting product holds.

**Scope:** Recommendation only; SCHEDULED-RESULTS and SCHEDULED-REPORT-SPEC are the applicable incoming instructions in [ki.prj.observatory messages](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.observatory/messages.md:34).

**As of:** 29 October 2026, 01:12 GMT.

For future runs, the clean correction is receiver-owned: chezmoi should distinguish successful agent completion from actionable final findings and report `findings` with a useful safe short summary. Existing Observatory paths already display that status for latest and history. Keep hard process/agent failures as `failed`; the `findings` outcome should not turn partial mailbox failure into a claim that the wrapper crashed. A reliable structured final outcome is preferable to interpreting arbitrary prose, but its prompt/wrapper protocol needs receiver-owned design and tests. Do not change the generic reporter to infer domain results, and do not rewrite historical reporter files in place.

The smallest Observatory-only compatibility repair is a job-scoped, pure backend reader of the known Route Triage final-summary format in `detail`, applied consistently to each latest and history record. On positive failure evidence with reported `ok`, project a findings result with a fixed safe summary explaining that the wrapper reported ok while its final summary reports failed work. Keep the original status explicit in that safe explanation; never mislabel it as producer-reported findings or raw process failure. This can reuse the existing findings chip, history rows and Beacon classification without new scheduler actions. The API contract's current wording describes status as reported, so even this small projection needs a documented semantics decision; a separate typed `reportedStatus`/failure-evidence field is clearer if independently showing both becomes necessary, but is a larger contract change.

Do not ship a global search for “failure” or expose raw detail. The prompt uses a plain `Failures <text>` line, not a guaranteed Markdown heading; test actual specimens before freezing a parser. Recognize the supported line/section boundary and explicit negative forms; restrict interpretation to that section so “no failures”, quoted examples and failures in other prose do not become positives. Unrecognized text should remain unknown failure evidence rather than classified clean. A nonempty unknown section must not silently count as no failures. Historical compatibility is the reason a consumer repair may still be useful after the producer is corrected.

Bounded next plan, subject to a new authorised planning/delivery brief:

1. Observatory: draft the one automation specification area and index entry from the current-behaviour clauses above; retain lifecycle and failure-evidence changes as Gaps. No redesign, scheduler ownership or wider spec tidying.
2. Obtain an authorised local-only sample of the original Route Triage records, sanitised into fixtures; substantiate the reported six-of-fifteen count. No evidence was available on sol.local to do that now.
3. Observatory: plan the smallest job-scoped compatibility interpretation and its declared status semantics. Apply to both latest and recent records in one pass; preserve raw detail exclusion, safe reasons, failed status precedence, overdue logic and existing views.
4. Coordinator: only when authorised, hand the prospective wrapper correction to `ki.prj.chezmoi` and reply to `hnr.reg.email-routing` with the selected approach. This run sent neither message.

Meaningful follow-up tests: positive move/save/tool failures in supported plain and headed summary forms; explicit none/zero failures; missing/empty detail; omitted or ambiguous failure section; misleading words elsewhere; successful process plus operational failure; nonzero process/agent error/budget/timeout; unchanged failed/unreadable precedence; latest healthy plus historical failing run; newest five limit; new `findings` records alongside old `ok` records; redaction and raw-detail exclusion for both latest and history; signal landing; full mechanical-first gate when service-starting checks are authorised. Producer tests should check semantic findings in otherwise successful agent results, which current runner tests do not establish.

Existing work: [KI-OBSERVA-VIS-022, accepted before pruning](https://github.com/knowledgeislands/apps-observatory.local/blob/e23d85acb3404c2a9cc8ce52bf7bad8b72093a61/docs/roadmap/KI-OBSERVA-VIS-022-judge-overdue-against-each-job-schedule.md) is the direct schedule/freshness lineage, verified from local Git objects without fetching the link. [KI-OBSERVA-APP-044](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md) governs broader consolidation; [KI-OBSERVA-VIS-045](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-045-workers-instrument.md) is held draft Workers consolidation, not authority for this isolated reader correction. No live Ready schedule-result record was found. Do not reopen/prune records or treat these held consolidations as approval to implement.

Coordinator method reminder: state records `method_read: afb126f2`; the current incoming queue releases only NAMING-PAUSE metadata writes. Before any delivery dispatch, read `standards-coordination.md` sections “Messages between work”, “Unattended windows”, “Headless passes” and “Reply forms”, and background-run sections “Authority tiers”, “Coordination” and “Reporting”. Preserve package priority, seven-state authority, unanswered queries and the empty Ready delivery set. The present report needs no staging window and grants no product implementation authority.

## Queries

No outstanding queries from this read-only unit. Missing original Route Triage run evidence is a verification limitation carried above, not a reason to request remote access or silently widen this brief.

### 🤖 → 👤 Handoff to supervisor · since 01:12 GMT

🤖 0 running · 👤 1 with you · ⛔ 0 blocked

- [handoff] Scheduled-run diagnosis and proposed reporting contract · Observatory coordinator · since 01:12 GMT

🧵 ki.prj.observatory
