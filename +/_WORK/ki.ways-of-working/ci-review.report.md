# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › ci-review

**🤖 → 👤 Handoff to supervisor · Run report at 02:41 BST · last mark 02:01 BST**

---

## Done

- Pick: a), confidence medium. Reason: selective isolation addresses the demonstrated collisions while preserving Kris's primary-checkout workflow and allowing a reversible knowledge-base pilot.
- Condition on a): serialise the entire shared-checkout Git write window, including hooks and post-commit verification; pathspecs protect file selection but do not isolate working files, prevent same-path edits or serialise HEAD.
- Condition on a): establish dependency and runtime parity before judging worktree audits; assess a named committed revision and revalidate against current main before serial integration. For the pilot, count swept files, false audit findings and integration failures as well as lock waits.
- Incident evidence: the permitted retros describe lock contention, swept staging, half-saved-file audit findings and historical unpushed stacks; e0489e42 and 0836bcae contain changes across the named works. The approximate count of 12 distinct collisions was not independently deduplicated.
- Worktree creation passed: ki-principal 0.170 s; ki-agentic-harness 0.273 s, one detached checkout each.
- Dependency and activation claim confirmed: both scratch checkouts lacked node_modules and runtime skill links; their unprepared hooks refused to run. With dependencies linked locally, the principal repository audit still found eight activation failures and one missing-registration failure, versus zero failures in the primary checkout.
- Hook timing qualified: with linked dependencies, staged Markdown probes passed in 0.730 s and 0.445 s respectively; approximately 2 s is workload-dependent, not an established general cost. These probes did not exercise TypeScript or skill-change gates.
- Launcher claim overstated: --repo need not always name the primary checkout. [thread.ts](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/thread.ts:255) reuses a recorded home; a new home can resolve from a scratch working directory. Explicit --repo primary is a useful routing safeguard for new launches, not a hard launcher requirement.
- Private-index risk supported, with a verification limit: an index initialised from the parent revision retained one unrelated reversal against current HEAD. Hook source provides no general ownership or stale-HEAD guard; no actual commit was made, so silent reversion through the complete hook-backed commit sequence was not reproduced.
- Pathspec behaviour partly verified: a commit dry run selected only the requested probe, preserved the separately staged file and left the ordinary index tree unchanged. Installed lint-staged also explicitly handles Git's temporary pathspec index; post-commit consistency remains untested under the no-commits restriction.
- Owner preference confirmed in the 18 October decision entry: ordinary work should be able to use main. Current ki-principal had zero commits ahead of its cached upstream when checked; this does not disprove the historical unpushed stack, and no remote state was refreshed.
- Blinding limitation: a targeted search for the owner's earlier ruling also returned a later [decision-log entry](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/decisions.md:525) summarising the previous recommendation. No excluded file or run report was opened, but this recommendation cannot be counted as fully blind.
- Cleanup passed: both disposable worktrees and all temporary output were removed; no primary-checkout source edits, commits, launches or network calls were made.

## In Progress

Nothing running. Full hook-backed commit behaviour remains untested because the brief forbids commits.

## Queries

No outstanding queries.

### 🤖 → 👤 Handoff to supervisor · since 02:41 BST

🤖 0 running · 👤 1 with you · ⛔ 0 blocked

- [with you] CHECKOUT-ISOLATION review, including its blinding limitation · supervisor · since 02:41 BST
