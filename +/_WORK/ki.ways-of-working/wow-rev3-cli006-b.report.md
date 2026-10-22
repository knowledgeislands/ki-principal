# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-rev3-cli006-b

**🤖 → 👤 Handoff to supervisor · Run report at 08:30 BST · last mark 08:24 BST**

---

## Done

VERDICT: ACCEPT · confidence high · The fix closes the contradictory-evidence defect and every Step and Verify item is met, but pruning must wait until the record has been accepted and 19 inbound links reconciled.

I reviewed [KI-TOOL-TECHNE-CLI-006](/Users/krisbrown/workspaces/knowledge-islands/tools-techne/docs/roadmap/KI-TOOL-TECHNE-CLI-006-guarded-host-commands.md) on main at `492e0535`, which contains delivery `41b6fd40` and its recorded baseline `40156309`. The working tree was clean. The record has no section titled Done-when, so I judged it against its Goal, Boundary, eight checked Steps, Verify and Review.

### Acceptance: no blocking findings

- **Earlier refusal resolved.** [Repository validation](/Users/krisbrown/workspaces/knowledge-islands/tools-techne/src/harness.ts:236) now rejects two things: a repository labelled clean that has positive dirty, unpushed or stash counts, and an inspection problem on any repository whose state is not unknown. Public `runCli` regressions cover all four cases under clean, at-risk and unknown top-level outcomes. Each fails closed with exit 1, null safety and no raw text. I compared the rule with the Harness's [status script](/Users/krisbrown/workspaces/knowledge-islands/ki-techne-harness/operations/aws/agent-host/host/status.sh:138). The Harness sets a problem only together with unknown state, and sets clean only when all counts are zero. So the stricter check cannot turn a genuine Harness report into a false failure. Treating upstream ahead/behind counts as advisory matches the script's all-remotes definition of unpushed commits.
- **Other fixes verified.** Profile precedence now comes from the declared operation script, and an aliased-operation regression covers it. Stop reports `stopped` only after the stop script returns, and the Harness [stop script](/Users/krisbrown/workspaces/knowledge-islands/ki-techne-harness/operations/aws/agent-host/stop.sh:77) waits for `instance-stopped` before that. The Review wording on provider checks is now accurate: the CLI validates options and the explicit host, and leaves account, stack and same-host checks to the destroy script.
- **Rest of the boundary verified on source.** The structured read is authoritative and the advisory text read is bounded. Stopped or absent hosts exit 4 without SSH. `--all` uses the declared exit precedence. There is no provider-stop fallback. Removal refuses a non-interactive terminal and its dry run makes no calls. The CLI sets no confirmation variable. Teardown is now a diagnostic with no side effects. Help, completion, manual, user guide and changelog are aligned.

### Checks, run offline and serially

- Root and depcruise frozen offline installs: passed.
- Tests: passed, 115 across five files.
- Coverage: passed, 100% statements, branches, functions and lines.
- Typecheck, build, release fixture test, man lint, Biome, rumdl and `git diff --check` from the baseline to HEAD: passed.
- `ki repo audit`: passed, with no failures and six warnings.
- No tracked file changed. The checks refreshed ignored build, coverage and rumdl cache output in `tools-techne` (`dist/`, `reports/`, `.rumdl_cache/`) despite `--no-cache`, probably from the audit's own Markdown pass. The brief's write limit made no exception for this.

### Prune: blocked until these are fixed, in this order

1. **Accept first.** Commit the record's accepted terminal state with `ki-accept`, then prune it in a separate prune-only commit, as `ki-work-roadmap` requires.
2. **Tracked Principal links that would break (6 files, 6 links).** Retire each link or repoint it to an immutable history URL of the record at its accepted commit:
   - [ki/queries.md:9](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/queries.md): CLI006-READY is stale, because TECHNE-006-REVIEW a) answered it. Close the query.
   - [ki.agent-host/queries.md:7](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.agent-host/queries.md): CLI006-PLAN is stale. Close it.
   - [ki.estate-factorisation/queries.md:11](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.estate-factorisation/queries.md): HOST-GUARDS still says "Draft / Hold", which is stale. Close it.
   - [ki.tools-burndown/decisions.md:30](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown/decisions.md): this is a historical decision. Repoint it to the immutable URL.
   - [ki.ways-of-working/design/roadmap-sweep.md:126](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/roadmap-sweep.md): repoint or retire.
   - Related text that is not a link: [ki/state.md:45](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/state.md) still has a resume step to "dispatch a ki-plan run" for this record. Remove it. [ki.agent-host/decisions.md:310](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.agent-host/decisions.md) names the record as Decision 73's `home:`. Repoint that to the immutable URL.
3. **Untracked Principal run reports (10 files, 13 links).** These are all in `ki-principal/+/_WORK/ki.ways-of-working/`:
   - `accept2-tools-techne.report.md`, lines 10 and 40
   - `burn-tools-techne.report.md`, line 14
   - `prune-links.report.md`, line 10
   - `wow-burn-plan.report.md`, line 42
   - `wow-burn-techne.report.md`, line 9
   - `wow-fix-cli006.report.md`, lines 9 and 60
   - `wow-overnight-sweep.report.md`, line 107
   - `wow-rev-cli006-a.report.md`, lines 11 and 99
   - `wow-rev-cli006-b.report.md`, line 9
   - `wow-rev-cli006-c.report.md`, line 9

   Clear them through the work package's tidy step, or accept that they will dangle as transient run evidence. The three `briefs/wow-rev3-cli006-*.md` files name the path as code text, not as a link.

There are no inbound references inside `tools-techne` itself, and none in any other repository under `/Users/krisbrown/workspaces/knowledge-islands`. The scan covered hidden and ignored files, and excluded `.git`, `node_modules` and caches.

### Knowledge with no other durable home

Nothing blocks the prune. The [operator guide](/Users/krisbrown/workspaces/knowledge-islands/tools-techne/docs/guides/user/agent-host.md:108), manual and changelog already hold everything else the record says about behaviour and compatibility. The Harness operator guide documents the destroy confirmation variable. Three small items live only in the record:

- The upstream-drift-advisory rationale. Optional fix: add one sentence to the guide's status paragraph saying ahead/behind counts never change the verdict.
- The observation that the Harness manifest does not declare `CONFIRM_DESTROY_AGENT_HOST`.
- The missing JSON contract for expiry and pin warnings.

The last two are Harness-owned. If they are wanted, they go to the Harness as a `messages.md` line, not as a record.

## In Progress

Nothing running. No commit, acceptance, prune or edit to a peer repository was made.

## Queries

### TECHNE-006-ACCEPT — Accept now, prune after reconciliation

**Context:** The fixed delivery meets its plan and every offline gate passes. A prune needs an accepted terminal-state commit first, and has 6 tracked links and 4 stale entries in Principal to reconcile.

**Query:** Accept KI-TOOL-TECHNE-CLI-006 now and schedule the prune behind a Principal reference-reconciliation commit?

**Options:**

a) (recommended, confidence high - independently verified against the Harness contract, with every gate re-run) Accept now through `ki-accept`. Then one Principal run closes the three stale queries and the stale resume step, and repoints the tracked links and Decision 73's home. Then a separate prune-only commit.

b) Accept now and keep the record unpruned until the 12 November agent-host review.

c) Hold acceptance until an attended status, stop and rebuild exercise on vega, which the plan does not require.

### TECHNE-006-HARNESS-NOTE — Send the two Harness contract gaps as a message

**Context:** Only the record notes that the manifest does not declare the destroy confirmation variable, and that the Harness has no JSON contract for expiry warnings. Neither blocks this delivery.

**Query:** Send these to the Techne Harness as one `messages.md` line before the prune?

**Options:**

a) (recommended, confidence medium - this keeps the observation after the prune without creating a record anywhere) Send one non-blocking message line to the Harness work.

b) Let Git history of the pruned record be its only home.
