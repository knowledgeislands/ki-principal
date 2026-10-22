# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-day-impl-review-3

**🤖 → 👤 Handoff to supervisor · Run report at 18:28 BST · last mark 14:35 BST**

---

## Done

Verdict: ACCEPT

The two commits (`d6df59d9` and `cb165c20`) implement the first build stage of the accepted agent control contract. Every blocking property I looked for holds; the findings below are advisory.

Read the accepted contract in full and both commits' diffs and tests. Ran the full suite with coverage in a scratch copy of `cb165c20` under the temp directory: passed, after the boundaries test needed the primary checkout's tooling dependencies linked in (an archive-extraction artefact, not a code fault). Ran Biome in the scratch copy: clean. No checkout was edited.

**Contract conformance confirmed**

- Attempt identity, containment refusal, stop, dequeue and spawn reconciliation are present with the contract's outcome vocabulary and exit codes (`src/core/agent/controls.ts`, `src/commands/agent/control.ts:1-80`). Receipts, control state, launch receipts, evidence and acceptance carry the contract's schema identifiers.
- No silent fallbacks. The host supplies neither a control adapter (`src/core/agent/processes.ts`, `hostAgentProcesses` has no `control`) nor launch evidence (`src/core/agent/launch-evidence.ts`), so native stop refuses with `containment-unverified` and never signals, and every role resolves to `profile-dormant` or `model-evidence-unavailable`. Accept-role launches refuse with `acceptance-contract-unavailable` until the capability is present. Tests at `src/tests/cli/agent-control.test.ts:2365-2373` and the dormant-profile dry-run tests confirm this with zero launches and zero signals.
- No unsafe recovery. `controlTransaction` in `src/core/agent/control-store.ts` creates `control.lock` with `wx`, retries a bounded number of times and then refuses with `control-transaction-busy`; there is no age or PID takeover (test at `src/tests/cli/agent-control.test.ts:1133-1142`). `ownsScope` in `src/core/agent/scope.ts` requires token, scope, launcher and full process identity; PID alone never confers ownership (PID-reuse test at line 2159). Spawn recovery requires an authority heading digest, a closed evidence shape with absolute proof paths and matching digests, and agreement between `verifyRecovery` and a fresh inspection before any state changes.
- No mutable history. Receipts are written `wx` and a repeated identical request returns the stored receipt, while a differing payload refuses with `request-conflict`. The journal records intent before effect and replay cross-checks journal against projection, throwing `control-state-unverified` on mismatch. Terminal states are never overwritten: a stopped attempt whose status file later says `DONE` stays stopped (test at line 2340).
- Role-free `--rules` launches unchanged. Omitted runtime and rules still resolve to `claude` and `none`; `push|prune|release` tiers need no `--authority`, keep their footer and are labelled `path: 'legacy'` (test at line 2521). `ki agent reconcile` keeps its grammar and the help/usage test at line 2258 proves recover and reconcile stay distinct.
- Wake is absent from commands, help, man page and guide, and the guide says so.
- Tests exercise real behaviour. The mock control adapter models containment, ownership loss, descendants, inspection errors, PID reuse, lost acknowledgements and crash points; the crash-simulation tests inject faults by editing state files, which is injected-fault testing rather than contortion. Races (gate opening versus stop, two observers, concurrent dequeue and dispatch) are driven through the public CLI seam.

**Advisory findings**

1. `src/core/agent/runs.ts:1022-1024`, advisory. `summary()` now marks a run live whenever its queue is non-empty, even with no dispatcher and no held or running agent. This is consistent with the contract's view that a queued entry is owned work, but it changes `ki agent status` and the `send` liveness check for existing role-free runs whose dispatcher has died. Fix: either note it in the compatibility section of `CHANGELOG.md` or keep the previous dispatcher-dependent liveness for runs without a control store.

2. `src/core/agent/runs.ts:290-296` with `src/tests/cli/agent.test.ts:626`, advisory. A held role-free agent whose gate closes now renders as `one: failed` in `ki agent status` where it previously rendered `EXITED WITHOUT DONE (gate cannot open: ...)`. The reason text is still in the events log but no longer on the status line. This is a visible wording change for role-free runs that the compatibility promise does not mention. Fix: carry the closed-gate reason into the `failed` status line, or record the change in the `CHANGELOG.md` compatibility section.

3. `src/core/agent/runs.ts:1302` and the dispatcher pass, advisory. A legacy dispatcher spawn failure now leaves the entry fenced as `claim-unconfirmed` with exit 1 (test at `src/tests/cli/agent.test.ts:1838`) instead of dropping it as `failed`. This is the contract's intended behaviour, but a role-free operator now needs `ki agent recover resolve`, which no native adapter can satisfy, to clear the entry. Fix: state in the user guide how a role-free operator clears a fenced legacy entry on the current native adapters, or confirm that this fencing is accepted for the first stage.

4. `src/core/agent/control-store.ts:256-268`, advisory. `verifyStore` binds control authority to the current `hostname()`. A renamed machine, or a state folder synced between machines, refuses every control operation. The refusal is safe and explicit, so this is not a defect, but the message should say that the machine name differs so the operator does not read it as corruption. Fix: name the stored and current machine in the refusal reason.

5. `src/core/agent/runs.ts:1302-1320`, advisory. `drop()` for a legacy queue entry rewrites `queue.jsonl` from the merged projection, so a legacy line gains any normalisation the store applies. Harmless today because the merge is lossless, but it is the one place a legacy artefact is rewritten rather than appended to. Fix: none required now; keep in view if legacy queue lines ever gain fields the store does not carry.

6. `CHANGELOG.md` command list, advisory. The new entries describe the commands and the refusal posture but do not list items 1 to 3 above as behaviour changes for role-free runs. Fix: add one compatibility bullet covering live-while-queued, the `failed` status wording and the fenced dispatcher failure.

No scope drift found: `sweep`, `close`, `reconcile`, `decide` and the thread-folder model are untouched beyond the `requireWorkHome` flag that control needs. Role profiles are present only as a dormant table and cannot be selected.

## In Progress

Nothing. The review is complete and the scratch copy and logs remain under `/var/folders/6b/b4c73j8s6w12g2k9_yl652_h0000gn/T/ki-agents/ways-of-working/wow-day-impl-review-3/`.

## Queries

**Context** Findings 1 to 3 are visible changes to role-free run behaviour that the contract's compatibility promise does not mention and the changelog does not list. **Query** Should the implementer document these three changes or restore the previous role-free behaviour? **Options** a) (recommended, confidence high - the changes follow directly from the contract's ownership model and are safe refusals, so a changelog note is sufficient) Accept the behaviour and add one compatibility bullet to `CHANGELOG.md` before release. b) Restore dispatcher-dependent liveness and the `EXITED WITHOUT DONE` wording for runs without a control store, keeping the new behaviour only once an attempt has a control record. c) Defer the question to the second build stage and release as-is.
