# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-rev-cli006-b

**🤖 → 👤 Handoff to supervisor · Run report at 03:07 BST · last mark 02:12 BST**

---

## Done

VERDICT: ACCEPT · confidence high · every Step and Verify item of [KI-TOOL-TECHNE-CLI-006](/Users/krisbrown/workspaces/knowledge-islands/tools-techne/docs/roadmap/KI-TOOL-TECHNE-CLI-006-guarded-host-commands.md) is delivered in tools-techne `41b6fd40` within its offline boundary, it matches the Harness contracts, and all gates pass on re-run. Prune only after the inbound links below are repaired in the same unit.

- **Scope met.** The CLI now reads structured safety status (`--json`, no `--fetch`) as the authoritative verdict, validated and failing closed, under status v3 and list v2. Exits are 0/3/4/1/255, and `--all` applies the declared precedence. A stopped or absent host is unknown (exit 4) with no SSH. The text read is an advisory second read with a five-second timeout. Stop runs the recipe's stop script under the operator profile; `--now` reaches only that script, and there is no fallback to a direct provider stop. Rebuild and withdraw run the destroy script under the administrator profile with exact operation and override arguments. The CLI never sets `CONFIRM_DESTROY_AGENT_HOST`, and the process environment passes through. Teardown now exits 2 with zero calls. Help, completion, manual, user guide, README and changelog all agree.
- **Harness contract matches** (local Harness `32f1b1e`): the manifest's `[operations.*]` entries and `[status.exit]` table; the `destroy.sh rebuild|withdraw [--discard … | --discard-unreadable-host]` grammar; `stop.sh [--now]`; and `status.sh [--json] [--fetch] [--connect-timeout]`.
- **Checks re-run** (offline, pinned Bun): test with coverage passed (109 tests, 100% statements, branches, functions and lines); typecheck, man lint, biome and rumdl passed; `git diff --check` on the commit passed; `ki repo audit` gave FAIL 0 with the 6 warnings the record notes.
- **Finding, low (plan wording):** rebuild and withdraw no longer run the CLI-side AWS identity or instance lookup that teardown did; the destroy script owns the account and stack checks (`EXPECTED_AWS_ACCOUNT`). This fits "invoke guards rather than reproduce them", and the user guide says so. The Review does not call out this reading of "preserve provider account/region/selector checks". Selector and provider-option checks are kept. Not blocking.
- **Finding, low (maintainability):** in `src/cli.ts`, `hostEnvironment` gives recipe values priority only for the script names `stop` and `destroy`, not for every parameter scoped to the running script. It is correct for today's manifest, but a future operation on another script would quietly get the adapter's profile. Not blocking.
- **Finding, cosmetic:** stop prints `stopping <id>` after the script has already waited until the host stopped.
- **Inbound links that pruning would break** (absolute links to the record file, all in ki-principal): `+/_WORK/ki.agent-host/queries.md:7` (CLI006-PLAN), `+/_WORK/ki/queries.md:9` (CLI006-READY), `+/_WORK/ki.estate-factorisation/queries.md:11` (HOST-GUARDS), `+/_WORK/ki.tools-burndown/decisions.md:30` and `+/_WORK/ki.ways-of-working/design/roadmap-sweep.md:126`. Run reports in `+/_WORK/ki.ways-of-working/` also link to it: burn-tools-techne, wow-burn-plan, wow-burn-techne, accept2-tools-techne, wow-overnight-sweep and prune-links. All three queries are stale: TECHNE-006-REVIEW has answered them. Mentions of the ID with no link, and the `KI-TOOL-KI-CLI-006` hits in tools-ki, do not break. No other tools-techne file references the record. `41b6fd40` is on the local `origin/main`, so a pinned blob URL can resolve once the done commit is pushed.
- **Knowledge homes:** the confirmation variable is documented in the Harness operator guide and `destroy.sh`. The JSON expiry/pin limitation and the reasons for the compatibility choices are in the tools-techne user guide and changelog. The only item with no other home is the record's note that an attended status, stop, rebuild or withdraw exercise on vega is Kris's to run (see Queries).

## In Progress

Nothing. No files changed, and no commit, acceptance or prune was made.

## Queries

### CLI006-LIVE - Where the attended vega exercise is recorded

**Context:** The record says no live check was needed for this offline delivery, and that any attended status, stop, rebuild or withdraw run on vega is Kris's binding-owner operation. Nothing outside the record says this, so pruning would lose it.

**Query:** Should a one-line note go into the agent-host work before the record is pruned?

**Options:** a) (recommended, confidence medium - it keeps a real next step for the owner without inventing a work record) add a line to `ki.agent-host` state.md, or to its messages.md from tools-techne, saying guarded stop, rebuild and withdraw are ready for Kris to exercise on vega, in the same unit that closes the stale CLI006-PLAN, CLI006-READY and HOST-GUARDS queries. b) Let it go: the user guide already says every live operation needs binding-owner authority.
