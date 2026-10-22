# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-rev-cli006-c

**🤖 → 👤 Handoff to supervisor · Run report at 03:09 BST**

---

## Done

VERDICT: ACCEPT · confidence high · Commit 41b6fd40 delivers every Step and Verify item of [KI-TOOL-TECHNE-CLI-006](/Users/krisbrown/workspaces/knowledge-islands/tools-techne/docs/roadmap/KI-TOOL-TECHNE-CLI-006-guarded-host-commands.md) within its offline fixture boundary, all repository gates pass on an independent run, and nothing the record holds lacks a durable home.

- Scope matches the record: the commit touches only the CLI, parser, completion, harness and recipe modules, the public tests and fixture, the user guide, manual, README and changelog, plus the record itself; no provider, infrastructure, binding, dependency, Harness or Principal change, as Files touched requires.
- Step 1, operations parsing: `[operations.<name>]` is parsed with required summary and script, exposed through `recipe show --json`, resolved through the provider's paths, and a missing declaration or destroy path refuses before any subprocess; tested.
- Step 2, authoritative status: one `status --json` read per running host without `--fetch`, schema and exit-table validation, outcome/exit agreement, repository, problem and host shape checks, additive members preserved, `workspace.updates` projected from the same document, outer schemas bumped to host-status/v3 and host-status-list/v2, stopped or absent hosts report unknown and exit 4, legacy text-only recipes return unknown rather than clean, malformed or contradictory documents fail closed with exit 1 and no raw output, text mode adds one bounded advisory read with a five-second connect timeout whose failure only warns, and `--all` continues independently with the declared precedence 1, 255, 4, 3, 0. All of this is exercised through the public `runCli` seam with injected responses.
- Step 3, role-correct environments: for the stop and destroy scripts the binding's declared variables now override the adapter's default profile, so stop receives the operator profile and destroy the administrator profile as `AWS_PROFILE`; status and setup resolution is unchanged. Tests assert the exact environment for each.
- Step 4, stop: routed through the provider's stop script with `--now` forwarded, the explicit-host, selector, already-stopped and dry-run behaviour preserved, no CLI guard read, no provider fallback when the script is missing, and script failure propagated without raw output.
- Step 5, rebuild and withdraw: grammar validated before any call, including empty, blank, duplicate and repeated `--discard`, the mutually exclusive overrides, misplaced options and stray arguments; the operation resolves to the destroy path and runs interactively with exact operation and override argv under the administrator profile; the CLI never sets `CONFIRM_DESTROY_AGENT_HOST`, never terminates or provisions, dry runs make zero subprocess calls, noninteractive execution refuses, and every injected refusal or failure yields exit 1 with no success message. Argv and arguments match the Harness scripts at `32f1b1e4`.
- Step 6, teardown: exits 2 with guidance before option checks, so its old dry-run form also makes zero calls; its destructive handler and completion entries are gone; help, completion, user guide, manual, README and changelog are aligned and document the schema and exit changes, the unknown stopped-host state, overrides, role separation, the text-only expiry limitation and the binding owner's live authority.
- Independent gates, run offline with the pinned Bun 1.4.2: frozen install for root and depcruise passed; test passed; coverage passed; typecheck passed; build passed; release test passed; man lint passed; Biome passed; rumdl passed; `git diff --check` passed; `ki repo audit` passed with no FAIL findings and the pre-existing warnings only.
- Working tree clean after the gates; local `main` is level with `origin/main` by local refs, so a GitHub permalink to 41b6fd40 will resolve once pruned.
- Inbound references: none in durable documentation, specifications or any repository's roadmap. Every reference lives in ki-principal `+/_WORK` files, using local file links that pruning will break: the decisions logs of [ki.tools-burndown](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown/decisions.md) and ki.ways-of-working, the parked or open queries of [ki](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/queries.md), [ki.agent-host](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.agent-host/queries.md) and [ki.estate-factorisation](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.estate-factorisation/queries.md), the ways-of-working run reports, briefs and the roadmap sweep design note. These are work-package files that expect pruning; the CLI-009 precedent repointed such links to a pruned permalink.
- Knowledge with a durable home: the compatibility recommendations are in the changelog and guide; the undeclared confirmation variable is documented in the Harness operator guide and the tools-techne guide's pass-through statement; the text-only expiry limitation is in the guide and manual; the hold, release and replan history is in the decisions logs. No specification, decision record or handoff is owed by this record.
- Commits: none; read-only review.

## In Progress

Nothing is running.

Outstanding - no action requested now

- Receiver-owned: the CLI006-PLAN query in ki.agent-host queries is still listed as Open though Decision 73 answered it; the HOST-GUARDS and CLI006-READY parked entries are stale after the Ready release. Housekeeping for those threads when they next mark.
- Verification limitation: Harness risk-set, typed-confirmation and cleanup behaviour is modelled as injected script results, as the record states; no live host, AWS, SSH or Tailscale call was made here either.
- Interpretation note: rebuild and withdraw make no CLI-side account, role or instance check; the destroy script owns the account, stack and same-host checks through the declared environment. The guide and manual say so, and Step 5's "preserve provider checks" reads as satisfied by that delegation.

## Queries

### CLI006-CONFIRM - Confirmation variable pass-through stays as planned

**Context:** The delivered removal commands run scripts with the operator's inherited environment merged beneath the declared variables, so a stale `CONFIRM_DESTROY_AGENT_HOST` export would satisfy the destroy script's confirmation without fresh consent. This is exactly what Step 5 specifies and what you released to Ready under TECHNE-006-REVIEW a), yet the [ki queries](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/queries.md) still park CLI006-CONFIRM with a reviewer preferring a Harness-declared, interactively confirmed design. Acceptance does not depend on it; the Harness owns any change.

**Query:** Should the parked CLI006-CONFIRM be closed as settled by the Ready release, or carried forward as a non-blocking idea to the Harness?

**Options:** a) (recommended, confidence high - the Ready release already accepted the pass-through design and the limitation is documented in both guides) Close CLI006-CONFIRM as settled and accept the record. b) Accept the record and add one non-blocking handoff line to the Harness's work messages suggesting it declare the confirmation in the manifest. c) Hold acceptance until the confirmation design is revisited.
