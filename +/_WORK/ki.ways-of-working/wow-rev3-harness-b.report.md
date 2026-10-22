# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-rev3-harness-b

**🤖 → 👤 Handoff to supervisor · Run report at 08:55 BST · last mark 08:24 BST**

---

## Done

VERDICT KI-HARNESS-GOV-189: ACCEPT · PRUNE: NO · confidence high · Narrowed level check and `[behind]` delivered and verified; four durable peer links, two with a stale "owns host moves" claim, would break.

VERDICT KI-HARNESS-OPS-010: ACCEPT · PRUNE: YES · confidence high · Goal and Steps met; knowledge homed in acquisition and KB intake standards; only transient Ways of working run reports link to it. Prune only after the acceptance commit.

VERDICT KI-HARNESS-OPS-011: ACCEPT · PRUNE: YES · confidence high · Goal and Steps met; guidance and adapter decision homed in the session-acquisition standard and ADR-KI-HARNESS-SKILLS-007; only transient run reports link to it. Prune only after the acceptance commit.

VERDICT KI-HARNESS-GOV-209: ACCEPT · PRUNE: NO · confidence high · Already accepted and done; State of play's live GOV209-ROLLOUT line still depends on the record, as do two other durable work files.

VERDICT NO-GATE: ACCEPT · PRUNE: NO · confidence high · Both Project hook variants run the staged, check-only `ki-repo` audit with `KI_REPO_OFFLINE=1`, and a real run under network denial made no provider call. No record exists, so nothing can be pruned.

Reviewed local `main` at `0809ff80`, including the NO-GATE repair `d9c4a6e2` and original delivery `52a719ee`. No record was changed, accepted or pruned, and no commit was made.

### Findings

[KI-HARNESS-GOV-189](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-189-move-thread-between-hosts.md) meets its narrowed Goal, Steps and Review. The [repository level check](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md#repository-level-check) covers cross-host resume, every mark and departure. It runs `mgit fetch` and then the `mcp-git-audit` ahead and behind report, carries `[behind]` until a fresh check proves the repository level, treats a failed check as unknown, and leaves the On hold form unchanged. Both banner definitions and the generated coordinator style carry `[behind]` and the triggers. The deferred host-move questions, the 14 October transfer evidence and the DONE-on-handover decision are homed in [deferred host-move evidence](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/sources.md#deferred-host-move-evidence). The record holds no other knowledge, so nothing is stranded.

[KI-HARNESS-OPS-010](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-OPS-010-receiver-local-acquisition-triage.md) is met. The [common acquisition standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/acquire/ki-acquire/references/standards-acquisition.md) carries the four evidenced dispositions, receiver-visible gaps and separate retirement authority. ACQUIRE-5 is extended in the generated rubric. The [KB intake rule](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-kb/references/standards-acquired-triage.md) is reached from `ki-repo-kb` and keeps packet handling separate. [KI-HARNESS-OPS-009](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-OPS-009-complete-ai-session-acquisition.md) now cites these standards rather than the record and names OPS-010 and OPS-011 only as bare identifiers. That resolves the hosted-locator availability blocker from the prior review: no history locator is needed any more.

[KI-HARNESS-OPS-011](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-OPS-011-separate-agent-session-acquisition.md) is met. `ki-acquire` routes to the [agent-session acquisition standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/acquire/ki-acquire/references/standards-agent-session-acquisition.md). It requires an owner-selected full-session exception, rules out routine bulk import and distinguishes the Claude repository/session read from the bounded preview. Both housekeeping skills route capture to it. [ADR-KI-HARNESS-SKILLS-007](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/decisions/ADR-KI-HARNESS-SKILLS-007-provider-neutral-ai-session-acquisition-and-adapter-pairing.md) records that the shared adapters keep their names. No unique knowledge remains in the record.

[KI-HARNESS-GOV-209](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-209-acquired-inbound-area.md) is `done` with its `## Done` section; the accepted state is committed at `52779419`, verified locally. Its rollout snapshot and accepted-delivery citation are homed in [principal sources](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-kb-principal/references/sources.md#acquired-scaffold-rollout). Pruning is still blocked, because State of play's queue line says the record "is pruned once that home…" and has not been repointed.

NO-GATE: both [package](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-project/assets/githooks/package/pre-commit) and [no-package](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-project/assets/githooks/no-package/pre-commit) variants prefix both `quiet_audit` attempts, the concise run and its full retry, with `KI_REPO_OFFLINE=1`. In the collector, `KI_REPO_OFFLINE=1` now skips GitHub before `gh auth status` and refuses `--org`. Both standards state the boundary. To test the real path I used a throwaway local clone of a Project repository, with a GitHub origin, a staged change and a `gh` shim that reports itself authenticated. All runs used the real `ki` CLI under `sandbox-exec`, which denied outbound network and file writes outside this run's temporary folder. The control run without the variable called `gh auth status` and `gh repo view`. Both offline attempts made no `gh` call, and the sandbox reported no network or write denial. Their FAIL findings were all clone setup: an unregistered checkout, runtime activation and declared identity.

Outstanding to the receivers, not a NO-GATE defect: the committed pre-commit hooks of all six repositories with the `ki-repo-project` primary shape differ from the new canonical assets, and none carries `KI_REPO_OFFLINE`. Those repositories are `apps-dafacts.org`, `apps-observatory.local`, `ki-design`, `ki-techne-harness`, `apps-kris.me.uk` and `acquire`. Each needs its own conform.

### Inbound references a prune would break

I searched every ordinary file under `/Users/krisbrown/workspaces/knowledge-islands`, including hidden and ignored material but excluding `.git`, `node_modules`, caches and builds, for each record's filename. I then classified each match. There are 66 matching lines, all absolute local links except one: the GOV-209 link at `wow-rev-harness-c.report.md:37` is pinned to `52779419` and survives. The harness itself has no live link to any of the four records. I added two roots outside the requested one, chezmoi and `personal/acquire`, because earlier evidence named them. Hosted-only peers were not scanned, so this is not a claim of exhaustive cross-repository coverage. Report paths below are in [the Ways of working work folder](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/) unless stated otherwise.

KI-HARNESS-GOV-189, durable sources, all blocking:

- [KI-TOOL-KI-CLI-145:43](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-145-thread-session-bindings-role.md) says GOV-189 "owns moving a thread between hosts". That claim is stale since the scope was narrowed and needs reconciling, not just a new link target.
- [KB-DOTFILES-UE-096:32](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-096-thread-identity-hook-registration.md), outside the requested root, makes the same stale ownership claim.
- [design/unparked-queries.md:54](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/unparked-queries.md).
- [design/roadmap-sweep.md:111](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/roadmap-sweep.md) still calls the record `superseded`.

KI-HARNESS-GOV-189, run reports:

- `wow-rev-harness-a` lines 11 and 19, `records-fold` 14, `wow-burn-plan` 27, `roadmap-sweep.report` 124 and `wow-burn-harness` 9.
- `harness-burn` lines 29 and 91, `sweep-queries` 105, `lane-triage` 58, `unpark-review` 65 and `harness-queries` 12.
- `wow-rev-harness-c` line 11, `wow-rev2-harness-a` 25, `wow-rev-harness-b` 13 and 50, `wow-fix-harness` 9, 13 and 25, `harness-moves` 9 and `sweep-review` 65.

KI-HARNESS-OPS-010, run reports only: `wow-rev-harness-a` lines 22 and 31, `wow-burn-plan` 32, `wow-burn-harness` 10, `wow-signoff-ops009` 10, `wow-rev-harness-c` 12, `wow-rev2-harness-a` 27, `wow-rev-harness-b` 14 and 62, and `wow-fix-harness` 10, 15 and 25.

KI-HARNESS-OPS-011, run reports only: `wow-rev-harness-a` line 33, `wow-burn-plan` 33, `wow-burn-harness` 11, `wow-signoff-ops009` 10, `wow-rev-harness-c` 13, `wow-rev2-harness-a` 29, `wow-rev-harness-b` 15, and `wow-fix-harness` 11, 15 and 25.

KI-HARNESS-GOV-209, durable sources:

- [State of play messages.md:54](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/messages.md) is the live GOV209-ROLLOUT line and the one that blocks.
- [knowledge-acquisition decisions.md:10](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.knowledge-acquisition/decisions.md).
- [design/roadmap-sweep.md:119](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/roadmap-sweep.md).
- Outside the requested root, the open brief [ka-finish.md:10](/Users/krisbrown/workspaces/personal/acquire/+/_WORK/kb.regular.acquire-intake/briefs/ka-finish.md).

KI-HARNESS-GOV-209, run reports:

- `wow-rev-harness-a` lines 43 and 52, `wow-burn-plan` 18 and `wow-day-gov-209-accept` 9 and 37.
- `wow-day-prune-review-1` 17, `-2` 10 and `-3` 10, `wow-burn-harness` 13, `harness-burn` 18, 29 and 65, and `harness-queries` 10.
- `wow-rev-harness-c` 14, `wow-rev2-harness-a` 31, `wow-rev-harness-b` 16, `wow-fix-harness` 12 and 25, and `wow-day-gov-209` 9, 17, 21 and 35.
- In Acquire's `kb.regular.acquire-intake` folder: `ka-close.report` 14, `ka-finish.report` 11 and `prune-007.report` 13 and 27.

None of the four records holds knowledge without another durable home.

### Checks

- `bun run test`: 1,431 passed, zero failed, run with the temporary directory confined to this run. Under my write-denying sandbox, `hooks/plan-sync.test.ts` failed; it passes unsandboxed, so that was a sandbox artefact, not a defect.
- `bunx --no-install tsc --noEmit` under network and write denial: passed.
- Hook and gate tests, covering canonical hooks, the Project gate and content-only evidence: 18 passed under network and write denial.
- Real-CLI offline check of the hook command, concise run and full retry: no provider call and no network attempt; the control run without the variable did call the provider.
- Durable-home spot checks for all four records: present.
- The primary checkout was clean before and after.
- Focused `ki repo audit` runs against the harness and commit hooks were not rerun. This read-only run would need an isolated audit home, and its brief allows no commit.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- KI-HARNESS-GOV-189, KI-HARNESS-OPS-010 and KI-HARNESS-OPS-011 stay `awaiting-review` until an authorised acceptance commit. Any prune must follow in a separate prune-only commit.
- The six stale Project pre-commit hooks need receiver-owned conforms.
- `ki-repo-kb-principal` receiver conformance stays with GOV209-ROLLOUT.

## Queries

### HARNESS-PRUNE-LINKS - Repair the surviving peer links before pruning

**Context:** KI-HARNESS-GOV-189 and KI-HARNESS-GOV-209 hold no stranded knowledge, but durable files still link to them. For GOV-189, tools-ki's KI-TOOL-KI-CLI-145 and chezmoi's KB-DOTFILES-UE-096 also state that it "owns moving a thread between hosts", which is no longer true. For GOV-209, State of play's GOV209-ROLLOUT queue line says the record is pruned once the rollout is homed, but it has not been repointed to the principal sources home. Two Ways of working design notes and the knowledge-acquisition decisions log also link the records. OPS-010 and OPS-011 have only transient run-report links.

**Query:** Should the repairs go to the owning works, with GOV-189 and GOV-209 kept until a fresh link preflight is clean, while OPS-010 and OPS-011 go on to acceptance and a separate prune?

**Options:**

a) (recommended, confidence high - every blocking line was read directly and keeping the records is reversible) Route the tools-ki, chezmoi and State of play repairs to their owners, and repoint the Ways of working design notes and decisions log in this work. Keep GOV-189 and GOV-209 until a fresh preflight is clean. Accept OPS-010 and OPS-011 now and prune them in a separate commit, letting their run-report links lapse with the reports.

b) Keep all four records and defer every prune until all the repairs land.

### 🤖 → 👤 Handoff to supervisor · since 08:55 BST

👤 1 with you

- [with you] HARNESS-PRUNE-LINKS · supervisor · since 08:55 BST

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
