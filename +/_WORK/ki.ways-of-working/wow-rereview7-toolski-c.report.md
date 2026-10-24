VERDICT: REFUSE · confidence high - the admission tip refuses ordinary crashed legacy runs permanently, including the live `ways-of-working` run on this machine, which prior candidate `a7c80cd8`, primary `main` `6c4d2a1a` and origin `main` `51725e8b` all still read.

# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-rereview7-toolski-c

**🤖 → 👤 Handoff to supervisor · Run report at 13:59 BST**

---

## Done

Read-only review of `51725e8b..3a3407e0` from detached temporary worktrees at `3a3407e0` and `a7c80cd8`; no commits made, no record, remote or primary touched.

- Item 1 (legacy replay): FAIL, blocking finding 1 below.
- Item 2 (evidence preservation): PASS, with non-blocking finding 3.
- Item 3 (release workflow history): PASS. The ci build job and the release package job are the only jobs that run the suite or the audit, and both check out with `fetch-depth: 0`; `51725e8b` is on origin `main`, so `git archive` of the baseline resolves in CI.
- Item 4 (regressions): PASS. The legacy, sixth-review and baseline-upgrade tests fail on `a7c80cd8` (65 failed, 89 passed in that selection) and pass on `3a3407e0`.
- Item 5 gates on `3a3407e0`: FAIL overall. TypeScript PASS; Biome PASS; build PASS; full test suite PASS (96 files, 2127 tests); `KI_REPO_OFFLINE=1 ki repo audit` FAIL (one failure, blocking finding 2).
- Item 6 (admission plan): PASS with a note. Primary `main` carries two local commits over `7eb0f017`; `6c498f3a` is patch-identical to `805e4d36`, and `6c4d2a1a` matches `b2d8e795` except for a one-line rebase resolution in the home-report guard. The move from `6c4d2a1a` to `3a3407e0` is not a fast-forward (merge base `7eb0f017`), so the compare-and-swap must be a guarded ref update, not a `--ff-only` merge.

### Blocking findings

**1. Crashed legacy attempts are refused permanently.** `src/core/agent/events.ts:578-627` (`classifyLegacyFailures`, else-branch ending in the `ambiguous legacy failure` throw) and `src/core/agent/events.ts:571-576` (`legacyTerminalFailure`). A baseline run whose worker died and was then observed by the old CLI ends its journal with a launcher-derived `failed: exited without DONE (<last status line>)` event. The tip treats that wording as terminal vocabulary, finds no later event, no control history (the old CLI wrote none), no `no report` text and no cancelled queue entry, and throws. Every command that reads events (`status`, `wait`, `launch --relaunch`, `close`, `sweep`) then fails with `events-evidence-unverified`, and the recovery guide route cannot help because there is no snapshot or control evidence to preserve; the only escape is hand-editing the journal. The brief's requirement is that such runs are "neither lose a completion nor be refused permanently".

Reproduction, scenario: with the `baselineCli` helper from `agent-control.test.ts`, run `ki agent launch r worker . brief.md`, write `12:00 UTC - milestone: working` to `worker.status`, make the pid dead, run old `ki agent status r` (journal now ends with seq 3 `failed: exited without DONE (12:00 UTC - milestone: working)`), then run the tip's `ki agent status r`, `ki agent launch r worker . brief.md --relaunch` and `ki agent close r`. All three exit 1 with `ambiguous legacy failure at sequence 3; preserve status, snapshot and control evidence`. The same scenario passes on `a7c80cd8`.

Reproduction, live state: copy `~/.local/state/ki/agents` to a temporary `KI_STATE_HOME` and run the tip's `ki agent sweep` or `ki agent status ways-of-working`. The tip refuses with `ambiguous legacy failure at sequence 421` (agent `gov194-refresh`, attempt 1, `failed: exited without DONE (10:52 BST - DONE)`, no later events, no control attempts for that agent, v2 history present). Over the same copy, origin `main` `51725e8b` refuses no run, `a7c80cd8` and primary `main` refuse only `mac-studio-setup` (see finding 4), and the tip refuses `mac-studio-setup` and `ways-of-working`. The refusal first appears at `22e0ea9c`.

**2. The repository audit fails on the tip, and the held-back commit is the fix.** `package.json:56` at `3a3407e0`. The installed ki-engineering audit's DESIGN-2 criterion now requires the root prepare script to run `bun install --frozen-lockfile --cwd tooling/depcruise`; the tip still provisions `tooling/boundaries`, so `KI_REPO_OFFLINE=1 ki repo audit --repo .` exits 1 with `repository audit found failures`. The prepare script is byte-identical at origin `main` `51725e8b`, so the range does not introduce the failure, but the admission plan holds back `d4849813`, which is the commit that renames the tooling to `depcruise` and satisfies the criterion. Admitting `3a3407e0` alone therefore leaves `main` failing its own audit gate. I did not run the audit at `d4849813`, so its pass is unverified. The same audit also warns under SCR-5 that prepare should be only the hooks-path command, which contradicts DESIGN-2; that inconsistency sits in the harness, not this repository.

Reproduction: build the tip, then run `KI_REPO_OFFLINE=1 ./dist/ki repo audit --repo .` from the checkout and read the ki-engineering section of the output.

### Non-blocking findings

**3. Snapshot loss after upgrade replays a duplicate progress event.** `src/core/agent/events.ts:724-741` (`readSnapshot`). A baseline journal `launch, progress "working", failed "no report"` with `worker.status` still `12:00 UTC - milestone: working`, upgraded by the tip and then with `events.state.json` removed, replays a fourth event `progress "working"` carrying `statusLine` and the fixture clock's `at`, so the journal grows from three to four events although nothing happened. Completion is preserved, so this is evidence noise rather than loss.

**4. Pre-existing refusal of `mac-studio-setup`.** The copied live state's `mac-studio-setup` run fails with `journal has lost an observed terminal outcome` on the tip, on `a7c80cd8` and on primary `main` (snapshot marks `adobe-clear`, `adobe-dryrun`, `rig-lane` and `thread-tidy` ended, `rig-lane` has only a needs-owner event, no `events.history` marker). Not introduced by this range, but the tip's recovery route should be checked against it before admission.

**5. Audit duration.** `ki repo audit` on this repository runs the coverage suite inside the engineering audit, so a 540-second wall limit kills it on a loaded machine; the brief's gate needs a limit of about 30 minutes or an idle machine.

### Gate lines

- Full test suite on `3a3407e0`: PASS (96 files, 2127 tests)
- TypeScript (`tsc`) on `3a3407e0`: PASS
- Biome on `3a3407e0`: PASS
- Build (`bun run build`) on `3a3407e0`: PASS
- `KI_REPO_OFFLINE=1 ki repo audit --repo .` on `3a3407e0`: FAIL (PASS=17 WARN=4 FAIL=1; the failure is DESIGN-2 below)
- Regressions on `a7c80cd8`: FAIL as expected (65 failed, 89 passed in the legacy and upgrade selection)
- Regressions on `3a3407e0`: PASS

## In Progress

Nothing. Temporary worktrees and copies under `$TMPDIR/ki-agents/ways-of-working/wow-rereview7-toolski-c` were removed after the gates finished.

## Queries

**Context** The tip refuses the live `ways-of-working` run and any baseline run that crashed without a relaunch, because `classifyLegacyFailures` has no escape for launcher-derived `exited without DONE (...)` and `attempt failed` events that lack control history.

**Query** How should the fix treat a launcher-derived legacy failure with no later event, no control history and no snapshot or status contradiction?

**Options** a) (recommended, confidence high - this is exactly what the old CLI recorded when it observed a dead worker, and the snapshot of that time agrees) treat it as terminal when the current snapshot for that attempt is `ended`, or when the agent has no live pid and no newer attempt, and keep the ambiguity refusal only when a snapshot or status line contradicts it. b) Keep the refusal and extend the recovery guide with a documented journal repair command, accepting that every pre-upgrade crashed run needs manual repair. c) Admit now and fix forward, accepting that `ki agent sweep` and `ki agent status ways-of-working` fail on this machine until the follow-up lands.
