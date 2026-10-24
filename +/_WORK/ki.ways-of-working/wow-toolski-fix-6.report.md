# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-toolski-fix-6

**🤖 → 👤 Handoff to supervisor · Run report at 10:36 BST · last mark 08:24 BST**

---

## Done

Resolved reviewer a F1: legacy failures are classified before terminal ownership is trusted or checkpointed, using fixed launcher outcomes, retained status identity and confirmed control receipts. Worker failure progress stays non-terminal; ambiguous journal or pending evidence refuses with recovery guidance. Verified classifications survive later status changes through digest-checked checkpoint metadata, while the append-only journal retains its original bytes.

The CLI regressions execute untouched `51725e8b` before upgrading the same state, with and without snapshots, including failure text that collides with terminal wording. They require one completion, waiter notification, first report homing and no redelivery after retirement. Genuine historical terminal failures, pending publications and ambiguous evidence are covered. CI now fetches the baseline history required by these regressions.

Ordered range `51725e8b..219968a0`, oldest first:

- `805e4d36` — fix(agent): preserve terminal identity and confirmed control outcomes.
- `b2d8e795` — fix(agent): preserve evidence across interrupted control operations.
- `4cd0ab87` — fix(agent): recover interrupted preparations and event appends.
- `b3fec501` — test(agent): preserve history in renamed-folder fixture.
- `a7c80cd8` — fix(agent): classify legacy failure evidence before replay.
- `219968a0` — refactor(tooling): rename boundary install root to depcruise.

The migration is last: `a9aba774` rebased to `219968a0666cb055efcab4bccaf537b9974a455d`, after fix `a7c80cd830d9c1e0e05f75d4f8414909d1c20e90`.

- PASS — Full suite with coverage: 2,078 tests across 95 files; all 52 durable-I/O and controller-SIGKILL matrix tests included.
- PASS — Coverage: statements 16,881/16,881; branches 11,723/11,723; functions 3,592/3,592; lines 14,281/14,281; all 100%, with thresholds and exclusions unchanged.
- PASS — TypeScript: `tsc --noEmit`.
- PASS — Biome: full repository check; no errors, one existing informational suggestion.
- PASS — Build: canonical Bun compilation with its output outside the repository; compiled version and agent help smoke checks passed.
- PASS — Markdown: modified recovery guide checked with rumdl.
- PASS — Candidate `ki repo audit`: current Harness `db5e3cff`; exit 0, 17 skill passes, five skill warnings, zero failures, 12 warning findings.
- PASS — Pre-migration `ki repo audit` at CI's pinned KI `v0.12.0` and Harness `f4d6c521ef4859dc8965579bc39a5575004e3ac5`: exit 0, 18 skill passes, four skill warnings, zero failures, eight warning findings.
- PASS — Released audit provenance: cached `v0.12.0` source matched every tracked release-tag file before offline compilation; its executable reports `0.12.0`; the pinned Harness came from the local Git object cache.
- PASS — Commit hooks: pre-commit and Commitlint ran without bypass; exactly the five intended paths were committed, including the model co-author trailer.
- PASS — Rebase fidelity: final candidate tree equals the verified pre-rebase tree; every tracked file of both final commits equals its corresponding audited mirror; worktree and index are clean.
- PASS — Scope: primary `main` remains `6c4d2a1aeabdac5ce5ca2e4bd711908d043afcf3`; no admission, push, tag, release or roadmap record was made.

The test fence denies external IP traffic while allowing localhost fixtures and normal temporary-file writes, including the `/tmp` fallback. No tests were filtered or skipped in the full gates. Earlier validation found one uncovered historical-attempt branch and audit-copy identity/dependency-link setup errors; these were corrected before the final green rerun. Commitlint's initial message-length refusal was corrected by wrapping the message. The offline audits used disposable canonical `tools-ki` mirrors with real dependency copies and byte-verified source trees; hosted CI was not contacted.

## In Progress

Nothing is running.

Outstanding — no action requested now: admission and the later release remain with the supervisor. The exact admission plan is:

1. Admit through `a7c80cd830d9c1e0e05f75d4f8414909d1c20e90` now, retaining `tooling/boundaries` and CI's `KI_VERSION: v0.12.0`. The range `51725e8b..a7c80cd8` passed that release's audit offline; hold `219968a0` back. This is the verified green-CI admission candidate, subject to the eventual hosted run.
2. Handle the existing local-main mismatch deliberately: on a clean primary, use a guarded compare-and-swap from expected `6c4d2a1a` to the admitted fix tip and refresh its checkout. `6c498f3a` and `6c4d2a1a` are represented by rebased `805e4d36` and `b2d8e795`; this local admission is not a fast-forward. No such ref update was performed here.
3. Separately authorize release preparation: retain the old tooling layout and current CI pin while updating `canonicalHarnessRelease` to a published immutable Harness revision containing `db5e3cff`, with its verified archive digest and the new KI release version. Gate, admit, tag and publish that pin-carrying KI release through the normal release workflow. This release step must precede switching CI to it; neither the CI-pinned `v0.12.0` nor the current source pin `52779419` provides the new depcruise rule.
4. After that release is available and clean-install verified, rebase the held migration onto the release preparation and admit it together with a CI `KI_VERSION` bump to that exact released tag. Re-run the migration tree's audit with that release before admission. Release availability alone does not make today's migration commit green while CI still pins `v0.12.0`. Populate the primary's `tooling/depcruise/node_modules` at that later admission before launching agent worktrees.

## Queries

No outstanding queries.

### 🤖 → 👤 Handoff to supervisor · since 10:36 BST

🤖 0 running · 👤 1 you

- [with you] Review the fix and execute the staged admission plan · supervisor · since 10:36 BST

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
