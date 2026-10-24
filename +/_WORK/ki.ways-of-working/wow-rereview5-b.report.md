# [Model](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md>) › [Ways of working](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md>) › wow-rereview5-b

**🤖 → 👤 Handoff to supervisor · blocked · Run report at 08:56 BST · last mark 08:24 BST**

---

## Done

VERDICT: REFUSE · confidence high · fix-5 and the fixture are correct, and every offline gate passes, but `a9aba774` would turn CI's pinned-release audit red when pushed.

This was a blind, read-only review of `51725e8b..a9aba774` on `wow-toolski-integrate`. The worktree stayed clean throughout. I reran the gates in a disposable clone under this run's temporary folder.

- Full suite with coverage: PASS, 2,049 tests across 95 files, including the fault and SIGKILL matrices; LCOV totals are 100% for lines (14,228), branches (11,663) and functions (3,579).
- Types (`tsc --noEmit`): PASS. Lint (Biome): PASS. Build: PASS; the compiled binary reports `0.13.0`, and `agent --help` runs. Manual lint: PASS.
- Rebase fidelity: PASS. In the range-diff against `6c498f3a`/`6c4d2a1a`/`eb0e8b2e`, the only changes are the trailers and the resolution note. Against fix-5's tip, `a9aba774` differs only by the content of `51725e8b` and the rename. The `events.ts` resolution `done && homeReports && !seen.ended` keeps both gates.
- Fixture `b3fec501`: correct. It replaces a scenario the control contract now refuses: deleting `events.jsonl` beside prior evidence. In its place, the first end is published after the rename, with history intact. A mutation check shows it still exercises the rename-following lookup: if `earlierNames` is reduced to the present folder, the test fails, and it passes unmutated.
- Full `ki repo audit`: I did not rerun it. I relied on the PASS in the integrate-3 evidence, which used the development Harness checkout. That PASS is the source of the finding below.

**Finding F1 (blocking) — `a9aba774` fails CI's audit at the pinned Harness.** `.github/workflows/ci.yml` installs released KI `v0.12.0`, which acquires Harness `f4d6c521`. `v0.13.0` pins `52779419`. Both Harness versions require `tooling/boundaries/package.json`. Their DESIGN-2 check also fails unless `prepare` includes `bun install --frozen-lockfile --cwd tooling/boundaries`. The depcruise rule exists only in Harness `db5e3cff`, from 02:30 today, and no `tools-ki` release pins it. After the push, the `ki repo audit --repo .` step on `main` would fail DESIGN-2 and SCR-5 would warn.

Change needed: either keep `a9aba774` out of this push and admit and push `51725e8b..b3fec501`, or land it together with a `tools-ki` release whose canonical Harness pin contains `db5e3cff` and with `KI_VERSION` raised to that release in the same push. See Query AUDIT-SKEW.

**Finding F2 (non-blocking, admission mechanics) — admitting this to `main` is not a fast-forward.** Primary `main` is at `6c4d2a1a`. It carries `6c498f3a` and `6c4d2a1a` on `7eb0f017`, and they are superseded by `805e4d36` and `b2d8e795`. Admission therefore moves `main` back over two local commits rather than fast-forwarding.

Change needed: use a compare-and-swap `git update-ref refs/heads/main <tip> 6c4d2a1a` on the clean primary, then a checkout refresh. Record in the admission that the two dropped commits are represented by the rebased pair.

**Finding F3 (non-blocking, operational) — the primary checkout has no `tooling/depcruise/node_modules` yet.** If `a9aba774` is admitted, the primary checkout has only `tooling/boundaries/node_modules`. `prepareAgentWorktree` then copies no checker dependencies into agent worktrees, so `boundaries.test.ts` fails there until `bun install --frozen-lockfile --cwd tooling/depcruise` runs in the primary.

Change needed: run that install in the primary checkout, or move the existing directory there, right after admission. Remove the orphaned `tooling/boundaries/` directory.

**Finding F4 (cosmetic) — the trailer name differs between commits.** `b3fec501` and `a9aba774` use `Co-authored-by: GPT-6`, while the rebased fix-5 commits use `Codex (GPT-6)`. No change is required for admission.

## In Progress

Nothing is running. The disposable clones have been removed from this run's temporary folder.

## Queries

### AUDIT-SKEW — How to publish the depcruise rename while CI's pinned Harness still expects `tooling/boundaries`

**Context**: The current Harness (`db5e3cff`) requires `tooling/depcruise`. Every Harness that a released `tools-ki` pins still requires `tooling/boundaries`, and CI audits with released `v0.12.0`. Whichever layout `main` uses, one of the two audits fails until a release carries the new pin. Fix-5 and the fixture pass every gate and do not depend on the rename.

**Query**: Should this push hold `a9aba774` back until a release pins the depcruise Harness?

**Options**:
a) (recommended, confidence high - publishes the verified control contract now without a red CI on main) Admit and push `51725e8b..b3fec501`, and keep `a9aba774` on its branch. Land it in the same push as the release-pin and `KI_VERSION` bump. Until then, accept DESIGN-2 failing in local audits against the development Harness.
b) Admit and push the whole range now and accept a red CI audit on `main` until the next release.
c) Have the Harness accept both install roots for a transition window, then push the whole range once a release pins that Harness.

### 🤖 → 👤 Handoff to supervisor · since 08:56 BST

🤖 0 running · 👤 1 with you · ⛔ 1 blocked

- [with you] AUDIT-SKEW: choose how to publish the depcruise rename · supervisor · since 08:56 BST
- [blocked] Admit and push the `tools-ki` integration range · supervisor · since 08:56 BST
