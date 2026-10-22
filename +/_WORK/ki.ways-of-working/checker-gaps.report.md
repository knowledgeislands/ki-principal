# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › checker-gaps

**🤖 → 👤 Handoff to supervisor · blocked · Run report at 00:30 BST · last mark 23:40 BST**

---

## Done

Implemented the candidate in fresh worktree `/Users/krisbrown/.local/state/ki/worktrees/checker-gaps-20261020`, branch `checker-gaps`, based on `95d36f86`. No commit, integration, fetch or push: the task requires the full test suite to pass before committing.

Extracted the local adapter's existing area-title validation and record-to-declared-area identity check into its published `roadmap-areas` module, with an explicitly declared, byte-identical Streams copy. Both adapters call that shared implementation; the local adapter retains FAIL. Streams adds STREAM-13 and STREAM-14 at WARN, with diagnostic-only remediation, fixtures for both checks, positive issuing-mode cases and a shared-copy parity test. Updated the generated Streams rubric, structure standard and criterion inventory expectations.

FAIL impact, checked read-only across seven principal islands: hnr-principal and tmx-principal would fail the area-title check; va-principal would fail the declaration check for eight current GOV/KNW records. ki-principal, legal-principal, personal-principal and er-principal pass both new checks. No island was changed and no work record was created.

Tests: 1,315 pass; four existing hook tests fail, and those same four reproduce on unchanged primary `main` at `95d36f86`.

Type check: PASS.

Biome: PASS for all nine touched TypeScript files.

Markdown: PASS for all four touched Markdown files.

Focused candidate audits: ki-work-roadmap, ki-repo-kb-streams and ki-skills complete through the existing KI host against worktree catalogues, with no FAIL; roadmap retains 17 existing size warnings. The ordinary Streams CLI selection on this Project repository refuses an undeclared adapter, so its candidate catalogue was supplied directly to the same host without changing installed configuration.

Shared-module parity and Git whitespace checks: PASS.

## In Progress

Delivery is blocked before commit. The complete candidate remains unstaged in the worktree above; the primary checkout is untouched. The worktree is retained because removing it now would discard the uncommitted implementation. Commit, any authorised publication and worktree retirement remain outstanding.

The baseline failures are in [pre-commit.test.ts](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/hooks/pre-commit.test.ts:88), [commit-msg.test.ts](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/hooks/commit-msg.test.ts:25) and [git-hook-stub.test.ts](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/hooks/git-hook-stub.test.ts:111). They still assume retired Husky paths or stubs after the committed-githooks migration. I have not changed those unrelated tests or bypassed any gate.

## Queries

### HOOK-TESTS - Clear the existing full-suite blocker

**Context:** The brief says all tests must pass before commit and to stop on a blocker. Four unrelated hook tests fail on unchanged main as well as on this candidate; all candidate-specific tests pass. No commit has been attempted.

**Query:** Should the hook migration's owning work repair these tests before checker-gaps resumes, or should this run's scope expand to repair them?

**Options:** a) (recommended, confidence high - preserves this bounded task and lets the hook migration own its tests) Repair the baseline tests in their owning work, then resume checker-gaps to reconcile that change, rerun the gates, commit by explicit paths and retire its worktree. b) Authorise checker-gaps to repair the four hook tests as additional scope, then rerun all gates before committing.

```text
HOOK-TESTS: a
```

### 🤖 → 👤 Handoff to supervisor · blocked · since 00:30 BST

👤 1 with you

- [with you] HOOK-TESTS · supervisor · since 00:30 BST
