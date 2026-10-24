# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-day-impl-review-1

**🤖 → 👤 Handoff to supervisor · Run report at 18:27 BST · last mark 14:35 BST**

---

## Done

Verdict: CHANGES NEEDED

1. **Blocking - unreadable control state silently loses attempt history.** [control-store.ts:200](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/control-store.ts:200) uses the catch-all reader in [context.ts:53](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/context.ts:53), then treats any failed read as an absent store. With a writable run directory, making only `control.json` unreadable and queueing another name succeeds and replaces the projection with a fresh store: the existing attempt, history and operation map disappear. The old journal survives, but its attempt projection and ownership are lost. This is a silent fallback affecting currently available launches, contrary to the contract's identity and persistence safeguards. **Fix:** distinguish genuine absence from permission and I/O failures, fail closed on unreadable state, and refuse fresh initialisation when prior journal or control evidence exists. Add a CLI regression for file-level read denial, asserting unchanged bytes and no new queue entry or launch.

2. **Blocking - held work can start with stale authority evidence.** [runs.ts:818](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:818) validates the frozen selection once before the holding loop; [runs.ts:867](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts:867) starts the worker after the wait without revalidating it. In an evidence-enabled fixture, changing the cited authority heading during the first injected sleep and then opening the dependency gate still starts the worker successfully. The same missing check bypasses changes to acceptance records, review evidence or accepted model support while a holder waits. This violates the frozen-evidence requirements in the [accepted contract](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/agent-control-contract.md:137). **Fix:** revalidate the existing frozen selection inside the final spawn-authorisation transaction immediately before worker launch, preserving its original values and revision. Add during-wait authority, acceptance-digest and evidence-withdrawal cases; each must refuse the worker spawn.

3. **Blocking - one stopped attempt can produce multiple terminal stop events.** [events.ts:319](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:319) derives `stopped` for every unfinished stop operation whose target is now stopped, without recording which operation established that terminal transition. A legitimate crash snapshot containing one unfinished stop intent, followed by a successful second stop request and a status observation, produces two `stopped` events for attempt 1 despite only one signal. [controls.ts:161](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/controls.ts:161) can likewise attribute a fresh terminal event to the earlier interrupted request when retried. This breaches the contract's no-duplicate-terminal-events guarantee and can give `wait --next` two notifications for one transition. **Fix:** persist the operation responsible for the attempt's terminal transition, derive its event once, and make other requests reuse that event or return an idempotent no-op. Extend the interrupted-request tests to assert the whole attempt's terminal event count across different request IDs, observers and retries.

4. **Blocking - event observers still steal live locks by age.** [events.ts:72](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:72) deletes `events.lock` after 30 seconds without proving that its holder has ended. This primitive predates these commits, but the first stage now relies on it for its terminal-event guarantees. Pausing one observer in the injected containment inspection, advancing the clock by 31 seconds and running a second observer lets both enter the critical section and append separate `done` events for the same attempt. The new `control.lock` correctly avoids age/PID takeover; the observer path does not. **Fix:** give event publication ownership-safe exclusion and explicit recovery rather than age-based takeover, with bounded refusal when exclusion is uncertain. Add a concurrent-observer test with a live holder older than the threshold, asserting one terminal event and no takeover.

Reviewed commits `d6df59d99a32394973ad30e790e44580cc752cac` and `cb165c2009c45b3a291ac8c957976264097a2d9f`, their combined diff and added tests against the accepted contract in full.

Independent failure checks: all four findings reproduced through the public in-process CLI with isolated filesystem, process and clock fixtures; [procedure](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-review-1.evidence/repro.ts) and [observations](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-review-1.evidence/run3/repro.results.json) are retained.

Role-free compatibility: PASS against the first commit's parent for launch and queue with `--rules push`, `prune` and `release`, without `--authority`; runtime/model/effort defaults, footer content and normalised runtime invocation agree.

Decision reconciliation compatibility: PASS against that baseline for ordinary runs and runs literally named `inspect` and `resolve`, including heading/timestamp selection, home replacement, class changes, numbered entries, ambiguous/missing entries, help and invalid usage; [comparison procedure](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-review-1.evidence/compatibility.ts) and [results](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-impl-review-1.evidence/compatibility2/compatibility.results.json) are retained.

Stage and native-capability boundary: PASS on inspection. Wake is absent, candidate role profiles remain dormant, scoped acceptance remains unavailable without the joint Harness capability, and the native host supplies no fabricated containment or recovery proof. Fixture outcomes establish policy behaviour only; no native capability is proved by this review.

Test quality: the added tests predominantly exercise the supported CLI seam and injected ports, including useful refusal and replay cases. The four missing failure/interleaving cases above demonstrate why complete coverage does not establish the contract's safety guarantees. The full repository suite, coverage and other supplied gate claims were not rerun or independently recertified.

Read-only boundary: no repository changes, Git commits, tags, installs, live workers, real signals, remote calls or configuration changes; tools-ki remains clean at the reviewed main commit. Scratch evidence was moved outside the temporary run directory without deleting it.

## In Progress

Nothing is running.

Outstanding - no action requested now: the supervisor owns routing the four fixes and their regression tests. Keep Harness alignment and native-evidence enablement behind the independent-review gate until those fixes have been verified and reviewed.

## Queries

No outstanding queries.

### 🤖 → 👤 Handoff to supervisor · since 18:27 BST

🤖 0 running · 👤 1 with you · ⛔ 0 blocked

- [with you] First-stage implementation review and four blocking findings · supervisor · since 18:27 BST
