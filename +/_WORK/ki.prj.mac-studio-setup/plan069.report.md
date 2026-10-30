# Mac Studio setup - plan069

**Run report at 00:39 GMT on 30 October 2026**

## Done

Planned [KI-TOOL-RIG-CORE-069](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-069-dynamic-type-handler-fallback.md) as far as GO-PLAN a) permits. The resulting status is `draft`, horizon `now`, size `s`; `created_at` and `baseline_ref: null` are preserved. Ready is blocked on RIG-069-PROBE, the missing attended sol setter/read-back evidence, followed by approval of the evidenced plan.

Only the target record changed in tools-rig. No roadmap index change was needed. The plan now accounts for the later terra success and the delivered confirmation helper, distinguishes successful legacy assignment from a need for either alternative route, defines failure/timeout and observation checks, and names the specifications, guide, man page and changelog that a future implementation must align. The historical probe remains a proposal requiring separate authority, current baseline checks and agreed restoration.

The planning record was committed as `9297c9caeb23e77c1d6a02eafc38361104de8d5f` and pushed to tools-rig `origin/main` after `git pull --ff-only`. The report is the sole intended ki-principal change. Its initial publication was blocked by the task's no-stash rule and the commit hook's automatic backup; Kris subsequently granted an explicit report-only exception, allowing publication with the normal hook and checks enabled.

### Evidence and record history

- Planning source baseline: tools-rig `80ab019ae96fa4b01adfa28ecd7622ce59b73b44`. The complete record history was inspected before shaping, including the actual 23 October diff.
- `4f97d743b1942f5b6e78c03e5f92d0d01062ad77`, 19 October: captured the dynamic-type handler failure.
- `2b4e2efda0d8ce7e62427e5d29d0e8d737ec065c`, 20 October: adopted the record into Now for diagnosis and planning without a live handler change.
- `6e060d096f1f39fc297fcc4589c43a8f86b6b4bc`, 20 October: added the read-only sol diagnosis and attended `legacy`, `modern`, `workspace` probe proposal, retaining draft.
- `6ecdd0457bf89cccceaa2b1d2725c6a35dd9c7cf`, 23 October: added terra's successful TOML assignment after consent and a second apply. It explicitly leaves sol's TOML held and asks for the sol probe; it supplies no rung results or chosen alternative setter. There is no subsequent record-history evidence settling that probe.
- `e882998f9142fed2fe502bf23b5062af709f9269`, 27 October: delivered the confirmation helper described by [KI-TOOL-RIG-CORE-070](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-070-handler-read-back-after-confirmation.md). Its awaiting-review status is unchanged. Source inspection confirms the bridge still uses the null-conforming legacy identifier and setter, and exits on a setter error before the helper runs. Thus the helper cannot itself explain or resolve the recorded sol -50.

Terra proves the existing setter can assign its dynamic TOML type; it refutes a universal rejection claim. It does not establish sol's setter behaviour or the cause of its earlier failure. Interface availability and mocked tests cannot provide that native evidence.

### Verification

The complete local gate finished: all 648 Bats tests passed with stdin redirected from /dev/null; ShellCheck, Bash syntax checks, assembly consistency, benchmarks, native-provider version smoke checks, mandoc lint and whitespace checks passed. The initial interrupted run did not produce a test result; only its unfinished suite was restarted. The target record passes rumdl and exact assertions for unchanged identity, status, horizon, size, dependency fields and creation timestamp. The related handler read-back record is unchanged.

The selected work adapter is explicitly `roadmap`, with its owner table present. The base work-selection audit passed. The roadmap adapter audit has no target-record finding and one pre-existing warning: [KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md) has no size. The coordinator explicitly authorised continuing with 069 alone, leaving 047 untouched.

The full repository audit returned no failures and four warnings: the same missing size, `.rumdl.toml` template drift, missing repository maturity, and non-canonical pre-commit hook text. These are outside the two-file ownership boundary and were not repaired. A warning-free repository-wide audit is not claimed.

### Scope and working-tree state

No sudo, handler setter, Launch Services write, duti call, live probe, live Rig apply, implementation or acceptance was performed. The code, tests and specifications were inspected; no runtime or system configuration was changed. No branch, manual stash, rebase, reset, force-push or hook bypass was used. The later owner approval permits only the normal hook-managed backup for the report commit.

Tools-rig started clean. Ki-principal was one commit behind origin and was fast-forwarded from `06ecd8de7f7f4936b92f0926d5d289fd337b8839` to `8dcf69f5eeca55dbfb7d9343546de3de6586b457` before the report write, as the coordinator directed. Its four pre-existing untracked reports belong to another session and were left untouched:

- `+/_WORK/ki.prj.ways-of-working/sol-finish-line-plan.report.md`
- `+/_WORK/ki.prj.ways-of-working/sol-host-sync-design.report.md`
- `+/_WORK/ki.prj.ways-of-working/sol-private-report-assessment.report.md`
- `+/_WORK/ki.prj.ways-of-working/sol-state-machine-readiness.report.md`

### PLAN069-AUDIT - Unrelated roadmap warning

**Context:** The ki-plan preflight requires stopping on any adapter warning. The only roadmap warning is the unrelated missing size on the tailnet listener record, which this dispatch cannot edit.

**Query:** May planning proceed on 069 alone while leaving that record unchanged and documenting the exception?

**Options:**

a) (recommended, confidence high - the warning is outside the target record and ownership boundary) Proceed with 069 only and document the warning.

b) Stop with a report only.

The coordinator answered a) in Orca reply `msg_39e044ef75be` to question `msg_2798f3d26c42`, noting that Kris has the unrelated record waiting on terra.

### PLAN069-GIT - Serial Git write windows

**Context:** Both repositories are shared checkouts. Publication needs a short serial staging/commit/pull/push window without taking another actor's paths or staging.

**Query:** May this worker take the tools-rig and ki-principal Git write windows sequentially for its exact owned paths?

**Options:**

a) (recommended, confidence high - explicit ownership and a rechecked empty index keep the bounded writes separate) Take both windows sequentially.

b) Wait for another writer.

The coordinator answered a) in reply `msg_69f5ec055aee` to question `msg_00f183ef9bdd`, and reserved both windows until worker_done. It also directed the initial principal fast-forward and preservation of the four untracked reports.

### PLAN069-HOOK - Commit-hook backup

**Context:** The task prohibits stashing and bypassing hooks. Ki-principal's unchanged pre-commit hook runs `lint-staged --quiet`; inspection of the installed implementation shows that it creates and later drops an automatic Git backup stash. There are no unrelated tracked changes, but the four unrelated untracked reports must remain untouched. This blocked the original report commit.

**Query:** Does the no-stash boundary permit the normal hook-managed backup for this report-only commit, or must the report remain uncommitted?

**Options:**

a) (recommended, confidence high - the inspected backup is hook-managed and only the owned report would be staged) Permit the normal hook-managed backup only; retain the hook and all other boundaries.

b) Keep the absolute no-stash rule and leave the report commit blocked.

**Resolved:** Kris explicitly approved the normal hook-managed backup for this report-only commit on 30 October 2026, replying "Yes, you may" after the conflict was explained. This permits the existing commit hook to run unchanged, with only the report staged and unrelated files untouched.

## In Progress

Nothing running at completion. The record is waiting for Kris's separately authorised attended sol probe and the resulting plan approval; implementation has not started. The report-publication policy conflict is resolved by the owner approval recorded above.

Outstanding - no action requested now: the four unrelated repository audit warnings remain outside this dispatch. The related handler read-back implementation exists and is not a build-order blocker; its review remains with its owner.

## Orca

Periodic heartbeats were sent during planning and verification; no background heartbeat loop was used. The interrupted turn stopped the unfinished test process, which was restarted without repeating completed checks. The first asynchronous ask result was recovered by resuming its existing message ID, without creating a duplicate question. The hook-policy ask timed out after ten minutes without an answer, and an escalation was sent. The original dispatch settled with one worker_done using outcome failed because report publication was then blocked. Kris later resolved that policy conflict directly in this chat; this report's publication is a direct owner-authorised follow-up to the settled dispatch.

## Queries

### RIG-069-PROBE - Native setter evidence

**Context:** The record remains draft because the 23 October update proves a successful legacy TOML assignment on terra but contains no attended sol probe result. Sol's recorded -50 occurs before the delivered confirmation helper, and read-only inspection cannot choose between legacy success with consent, a different identifier, or the NSWorkspace setter. A speculative fallback would therefore be unproved.

**Query:** Will Kris separately authorise and attend the bounded sol probe in step 1, then return each rung's result, effective read-back after consent and restoration outcome so the route can be settled and the plan approved?

**Options:**

a) (recommended, confidence high - attended sol evidence is the missing fact and keeps this planning run within its read-only machine boundary) Keep [KI-TOOL-RIG-CORE-069](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-069-dynamic-type-handler-fallback.md) draft and arrange the bounded `legacy`, `modern`, `workspace` probe with Kris, using `observe` after each. No live change is authorised by this report.

b) Keep the record draft and defer the probe; sol's TOML hold remains and implementation cannot start.

```text
RIG-069-PROBE a) Keep KI-TOOL-RIG-CORE-069 draft and arrange the bounded attended sol probe; settle and approve the route before Ready.
```
