# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-day-contract-review-6

**🤖 → 👤 Handoff to supervisor · Run report at 15:13 BST**

---

## Done

- Verdict: **return one named part for revision first**, then accept. The part is the reconciliation command surface in [agent-control-contract.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/agent-control-contract.md) (Reconciliation section, and its references in Dequeue and Bounded wake). All six For Kris decisions (STOP-POLICY, QUEUE-CANCEL, WAKE-BOUNDARY, ROLE-PINS, ACCEPT-AUTHORITY, BUILD-ORDER) and the precedence policy are sound and should be accepted once that part is fixed; the builds then go in the draft's order with its evidence gates.
- Confidence: **high** - the one defect is verifiable from `ki agent --help`, and every "today's gap" claim checked against tools-ki source holds.
- Rationale:
  1. Correctness defect: `ki agent reconcile` already exists as `reconcile <run> <entry> [home]` for the decisions log. The proposed `ki agent reconcile inspect <run> --operation <id>` and `reconcile resolve` collide with it: `inspect` would parse as the run name. The draft does not mention the existing command, and AGENTS.md forbids re-homing or aliasing it without explicit authorisation, so a builder would have to guess or query. Fix: give the operation-recovery surface its own name (for example `ki agent operation inspect|resolve`) and update the four cross-references.
  2. Gap claims verified: `AgentProcesses` exposes launch, alive and sleep only; attempts record a PID and `{runtime, model, effort, workdir}`; dispatch splices `queue.jsonl` then launches with no claim journal; events carry only launch, held, progress, done, failed, blocked and needs-owner; no stop exists. The draft's identity, fence and transaction requirements are proportionate to that.
  3. ACCEPT-AUTHORITY is consistent with the installed Harness, whose tier table says no footer authorises accepting work; the draft correctly makes Harness wording a prerequisite with a refusal (`acceptance-contract-unavailable`), not a follow-up.
  4. Precedence (explicit option, accepted role profile, legacy default only without a role; no runtime inheriting the other's model; review and accept bound to the accepted Codex pin) has no inferred ordering and no silent fallback; dormant profiles and dry-run make a wrong pin visible before launch.
  5. Risk, not a defect: the stop containment bar (proof of coverage of descendants that `setsid` or re-group, with no enumerate-then-signal race) is unlikely to be met on macOS with Node alone, so the first build will probably ship stop as a refusal path only. The draft states this outcome plainly; accept it knowing confirmed stop may stay unsupported until a host facility is found.
  6. Same for wake: both runtimes stay unsupported until native lease and keyed-acknowledgement evidence exists, which neither `claude -p --resume` nor `codex exec resume` offers today. The later-build split and "return as a query" rule handle this correctly.
  7. No safety defect found: no control writes work-package state, accepts, prunes, pushes or escalates to SIGKILL; uncertainty is always visible and blocks replacement rather than retrying.
- Checks: draft read in full; `ki agent` and nine subcommand help pages read; `processes.ts`, `runtimes.ts`, `runs.ts` (launch, hold, queue, dispatch, wait) and `events.ts` read; Harness authority tiers read. No file changed, nothing committed, no remote call.

## In Progress

Nothing is running.

## Queries

### REVIEW-6-VERDICT — accept the contract after renaming the reconciliation commands

**Context** The draft's policy and all six For Kris recommendations hold against the tools-ki source and the installed Harness. Its only defect is that the proposed `ki agent reconcile inspect|resolve` surface collides with the existing `ki agent reconcile <run> <entry>` decisions-log command, which the draft does not acknowledge.

**Query** Should the draft be accepted as the build contract?

**Options** a) (recommended, confidence high - defect is a naming collision, fixable without touching policy) Return the Reconciliation command surface for a rename, then accept all six For Kris decisions and the precedence policy and commission the builds in the draft's order with its evidence gates. b) Accept as is and let the first build choose the name; this breaks the repository rule against guessing and re-homing commands. c) Defer the controls entirely; nothing in the review supports this.
