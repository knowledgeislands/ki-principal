# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-day-contract-review-5

**🤖 → 👤 Handoff to supervisor · Run report at 15:12 BST**

---

## Done

Reviewed the revised [agent control contract](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/agent-control-contract.md) against `ki agent` help and the tools-ki agent source (`processes.ts`, `runs.ts`, `events.ts`); no change, commit or remote call made.

**Verdict:** return named parts for revision first, narrowly: the reconciliation command name and the push-authority scope. Every For Kris decision (STOP-POLICY, QUEUE-CANCEL, WAKE-BOUNDARY, ROLE-PINS, ACCEPT-AUTHORITY, BUILD-ORDER) is otherwise acceptable as written.

**Confidence:** medium. The two defects are certain, but each is a small edit that could also be taken as an amendment at acceptance.

**Rationale:**

1. Command collision (correctness). `ki agent reconcile <run> <entry> [home]` already exists and writes a decision's durable home in the decisions log; `close` also names a "reconcile gate". The proposed `reconcile inspect|resolve <run>` would parse `inspect` as a run name. AGENTS.md forbids compatibility aliases, so a build would stop on this at once. Rename the surface (for example `ki agent recover inspect|resolve`) everywhere it appears: the reconciliation section, dequeue receipts and tests 4, 7 and 9.
2. Push-authority scope (correctness and compatibility). Line 126 makes `push`, `prune` and `release` need `--authority` without saying whether this covers role-free launches. Line 122 keeps the role-free path for compatibility, but today `--rules push` needs no reference. State whether role-free `--rules push|prune|release` now needs `--authority`. If it does, list it in Today's gap as a breaking change and get the Harness to align before release.
3. Safety holds. Stop refuses without verified whole-attempt containment and never sends SIGKILL. Dequeue has transactional claims and tombstones. Wake waits on native exclusion and acknowledgement evidence, and roles stay dormant without evidence. Each failure mode refuses or leaves things visible rather than guessing.
4. Expectation to state plainly. macOS has no cgroup-style containment, so the first build may ship stop as `containment-unverified` on this host. With dormant pins it may also enable no role default. Kris should accept that a bare-minimum outcome is a valid pass, or name the evaluation run that would unlock the pins.
5. Build note: `events.ts` derives `failed: exited without DONE` for any dead process. The build must suppress that after a confirmed stop. Test 5 covers this implicitly; naming it would help.

## In Progress

Nothing.

## Queries

None. The verdict above is the answer to the brief's query.
