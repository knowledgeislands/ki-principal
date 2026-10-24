# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-rev3-cli006-c

**🤖 → 👤 Handoff to supervisor · Run report at 08:32 BST · last mark 08:24 BST**

---

## Done

VERDICT: ACCEPT · confidence high · The delivery meets every Step, its Verify and the six-part Review on current main; accept now, but prune only after the committed `done` state and the 21 inbound Principal links are reconciled.

Reviewed [KI-TOOL-TECHNE-CLI-006](/Users/krisbrown/workspaces/knowledge-islands/tools-techne/docs/roadmap/KI-TOOL-TECHNE-CLI-006-guarded-host-commands.md) at tools-techne `492e05359729e80515b789fdb014eee392b2f8e3` (delivery `41b6fd40`, repair `492e0535`), with the recorded baseline `40156309` an ancestor and the working tree clean before and after the checks. The record has no separately titled Done-when; its Goal, Boundary, eight checked Steps, Verify and Review supplied the criteria. The adapter is the local roadmap, status `awaiting-review`, horizon `now`. The Review packet carries `### Delivered`, `### Change Summary`, `### Verification`, `### Outstanding concerns`, `### Post-change review` and `### Mini recap` once each, in order, immediately before `## Discussion`. I read the fix report and the refusal the brief named, and located link lines in the other reviewers' files mechanically without reading their content.

### Finding 1 - Delivery matches the plan and the Harness contract; accept

No code or evidence change is needed. Against the local Harness at `32f1b1e489a6f9a38bb2578b15150a13f04775db`, the one the record cites:

- [Recipe parsing](/Users/krisbrown/workspaces/knowledge-islands/tools-techne/src/recipes.ts:117) reads `[operations.<name>]` with summary and script, exposes them through `recipe show --json`, and a missing or malformed declaration refuses rebuild and withdraw before any subprocess.
- [Workspace status](/Users/krisbrown/workspaces/knowledge-islands/tools-techne/src/harness.ts:138) makes one `status --json` read without `--fetch`, validates schema `techne/host-workspace/v1`, the exit map, outcome/exit agreement, `generated_at`, `workspace`, `fetched`, `host.hostname`, nullable `host.id`, repository and problem shapes, and the cross-field rules the repair added; these match the field names the Harness host script emits. Unknown members survive in `workspace.safety`; `workspace.updates` is projected from the same document and malformed updates are dropped without changing the verdict. Text mode adds one advisory `--connect-timeout 5` read whose exit 3 or 4 is a report, not a failure.
- [CLI status](/Users/krisbrown/workspaces/knowledge-islands/tools-techne/src/cli.ts:650) returns `unknown` with a skipped report and no subprocess for a stopped or absent host, emits `techne/host-status/v3` and `techne/host-status-list/v2`, continues across `--all` and applies precedence 1, 255, 4, 3, 0.
- [Script environment](/Users/krisbrown/workspaces/knowledge-islands/tools-techne/src/cli.ts:323) lets a parameter scoped to stop or to any declared operation script win over the adapter's default profile, so stop runs under the operator profile and destroy under the administrator profile; `--aws-profile` and `--aws-operator-profile` still flow through the adapter's resolved values. Status and setup precedence is unchanged.
- [Stop](/Users/krisbrown/workspaces/knowledge-islands/tools-techne/src/cli.ts:792) keeps the explicit-host, selector and already-stopped checks, runs the recipe stop script with `--now` forwarded, and has no provider fallback when the script is missing.
- [Removal](/Users/krisbrown/workspaces/knowledge-islands/tools-techne/src/cli.ts:823) validates grammar first, refuses non-interactive execution, resolves the operation to the destroy path, passes exactly `<operation> [--discard ...| --discard-unreadable-host]` as the Harness destroy script expects, sets no `CONFIRM_DESTROY_AGENT_HOST`, never terminates or provisions, and a dry run makes no call. Teardown exits 2 before option checks with zero calls.
- README, the [agent-host guide](/Users/krisbrown/workspaces/knowledge-islands/tools-techne/docs/guides/user/agent-host.md:105), the manual, completion and the changelog agree with the code; no stale `teardown` instruction, `host-status/v2` or `host-status-list/v1` reference remains outside the record.

The public `runCli` tests cover the Verify list: outcome exits, malformed and contradictory documents, dropped updates, legacy text fallback that exits 4, stopped-host unknown, advisory expiry and pin text, mixed `--all` precedence and continuation, stop argv and operator environment, removal argv, administrator environment, absent confirmation variable, every injected guard result, aliased operation-script profile, grammar refusals, non-interactive refusal and zero-effect teardown.

Checks, all run offline from the repository root with the pinned Bun 1.4.2 and `--ignore-scripts`, so no lifecycle hook, hooks-path change or network call ran:

- Root frozen offline install: passed, lockfile unchanged.
- Depcruise frozen offline install: passed, lockfile unchanged.
- Tests: passed, 115 tests across five files.
- Coverage: passed at the 100% thresholds.
- Typecheck: passed.
- Build: passed.
- Release test: passed with local archive and installer fixtures.
- Man lint: passed.
- Biome: passed.
- rumdl with `--no-cache`: passed.
- Full `ki repo audit`: passed, zero failures and six warnings, judged by the record's Verify criterion of no failures; I did not re-verify that the warnings predate the delivery.
- `git diff --check`: passed.

The checks wrote only to Git-ignored paths (`reports/`, `dist/`, the release test's temporary stage); no tracked file changed and the tree is clean.

### Finding 2 - Do not prune yet: 21 surviving links in 16 Principal files would dangle

Blocks pruning only, not acceptance. Every link below targets the record's local path. The owning Principal work must reconcile or repoint them, to durable guidance or a verified immutable history URL, in a committed change ahead of a prune-only commit; this run had no peer-edit authority and touched none. The scan covered every repository under `/Users/krisbrown/workspaces/knowledge-islands`, excluding Git internals, dependencies, build output, reports and formatter caches; it needed no remote.

- [State of play queries](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/queries.md:9), the parked CLI006-READY query.
- [Agent-host queries](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.agent-host/queries.md:7), the CLI006-PLAN query.
- [Estate-factorisation queries](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.estate-factorisation/queries.md:11), HOST-GUARDS.
- [Tools-burndown decisions](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown/decisions.md:30), HOST-GUARDS.
- [Roadmap sweep design note](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/roadmap-sweep.md:126).
- [Overnight sweep report](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/wow-overnight-sweep.report.md:107).
- [Second acceptance report](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/accept2-tools-techne.report.md:10), and again on line 40.
- [Pruning-links report](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/prune-links.report.md:10).
- [Burn planning report](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/wow-burn-plan.report.md:42).
- [Techne burn report](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/wow-burn-techne.report.md:9).
- [Earlier Techne burn report](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/burn-tools-techne.report.md:14).
- [Fix report](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/wow-fix-cli006.report.md:9), and again on line 60.
- [First review report a](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/wow-rev-cli006-a.report.md:11), and again on line 99.
- [First review report b](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/wow-rev-cli006-b.report.md:9).
- [First review report c](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/wow-rev-cli006-c.report.md:9).
- [Brief a](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/briefs/wow-rev3-cli006-a.md:7), [brief b](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/briefs/wow-rev3-cli006-b.md:7) and [brief c](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/briefs/wow-rev3-cli006-c.md:7) of this review round.

Bare identifier mentions elsewhere are history, not dangling links, but four live entries still state a superseded disposition and should be closed in the same reconciliation: the parked CLI006-READY and CLI006-CONFIRM queries in [State of play queries](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/queries.md:9), the resume step in [State of play state](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/state.md:45) that still plans a ki-plan dispatch, the CLI006-PLAN query in agent-host, and HOST-GUARDS in estate-factorisation, which still says Draft on hold. The Ready release and pass-through confirmation design were adopted under TECHNE-006-REVIEW in [Ways-of-working decisions](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/decisions.md:309).

### Finding 3 - Two Harness-side ideas have no home outside the record

Non-blocking; home them before the prune with one handoff line in the agent-host work's `messages.md`, per the handoff-as-message rule in tools-techne's AGENTS.md. The record's Current state and Outstanding concerns observe that the destroy script requires `CONFIRM_DESTROY_AGENT_HOST` although the recipe manifest does not declare it, and that expiry and pin warnings exist only in the Harness text route. The CLI consequences are durably documented in the user guide, manual and changelog, and the variable itself in the Harness operator guide, but the suggestions that the manifest declare the confirmation variable and a JSON expiry/pin contract live only in the record and the parked CLI006-CONFIRM query. Everything else in the record has a durable home: policy in ODR-KI-PRINCIPAL-001, authority history in the Principal decisions logs, and the command, schema, exit, role and override contract in tools-techne's guides, manual, changelog and public tests.

### Finding 4 - Minor changelog duplication

Non-blocking; fix at the next changelog touch. Under Unreleased › Breaking, the first bullet and the `EXPECTED_AWS_ACCOUNT` bullet both state that `host status --json` now reports `techne/host-status/v3`.

### Acceptance sequence

1. Record `done` with its `## Done` closure against the Review packet, keeping `baseline_ref`, and commit it in tools-techne.
2. In ki-principal, repoint or retire the 21 links and close the four stale entries, and add the Harness handoff line, in a committed change.
3. Only then prune with a dedicated `chore(roadmap): prune 1 done work record` commit listing `- KI-TOOL-TECHNE-CLI-006`.

No commit, acceptance, prune, remote call, environment change or peer edit was made by this run.

## In Progress

Nothing. This independent review is complete; the supervisor owns closure and the Principal reconciliation.

## Queries

None.

### 🤖 → 👤 Handoff to supervisor · since 08:32 BST

🎯 1 handoff · 📥 1 to accept

- [handoff] Accept [KI-TOOL-TECHNE-CLI-006](/Users/krisbrown/workspaces/knowledge-islands/tools-techne/docs/roadmap/KI-TOOL-TECHNE-CLI-006-guarded-host-commands.md), then reconcile the Principal links before pruning · ways-of-working supervisor · since 08:32 BST
