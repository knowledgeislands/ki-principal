# cg-review - blind review of three queries

Blind review. Do not read any `queries.md`, `decisions.md`, `+/_WORK/` file or run report. Read only ki-agentic-harness source, its roadmap records and the standards. Make no edits, commits, launches or network calls. For each query, choose an option (or propose another), give a confidence (high, medium, low) and one-line reason, plus any condition.

## WORKTREE-AUDIT

**Context:** Running `ki repo audit --repo .` in a fresh harness worktree gives false RUNTIMES-2 and REPO-REG-1 FAILs because the worktree is unregistered and has no skill links. Pointing `KI_DATA_HOME` and `KI_STATE_HOME` at an isolated temp home and running `ki repo repair --repo .` first avoids this without touching the real registry; CI runs the same order. CI pins `ki` v0.11.3; the recipe was proved on 0.12.0. **Query:** Where should this recipe live? **Options:** (unranked)

- A harness record adds the recipe to the harness `AGENTS.md` Verification line and `ki-delegation`'s worktree guidance.
- `ki repo audit` itself reports an unregistered or unlinked worktree as one setup finding instead of the FAILs (tools-ki change).
- Leave it in the run report only.

## HOOK-4-CLASS

**Context:** The harness pre-commit hook silently passed when `bun` was not on PATH; the fix makes it refuse before its content check, and a test now covers it. HOOK-4 in `ki-repo` does not require each external tool a hook calls to be tested in its refusal frame. How many hooks across the fleet would newly fail a tightened rule is unmeasured. **Query:** Should HOOK-4 require every external tool a hook calls to be tested in its refusal frame? **Options:** (unranked)

- Tighten HOOK-4 via a harness record, starting at WARN, after a fleet census.
- Keep HOOK-4 as is and rely on review.

## PLANNED-READY

**Context:** Seven harness draft records were planned: KI-HARNESS-GOV-200, -205, -214, -215, -220, -221, -223 (in `Streams/Roadmap/`). Five list open decisions under Dependencies / blocks (GOV-200 temp home and FAIL-or-WARN; GOV-205 token source, default form, optional `svg_form`; GOV-214 `written_at` and dropping `rebuilt_from`; GOV-221 reach, tracked Markdown only, keep-marker; GOV-223 key, retired islands, decline mapping). GOV-215 and GOV-220 have none. GOV-200's temp home and GOV-205's token source affect other repositories. **Query:** How should the seven records move to Ready? **Options:** (unranked)

- Take each record's listed answers and mark all seven Ready in one planning commit, splitting GOV-205 if its size warrants.
- Mark GOV-215 and GOV-220 Ready now and settle the others record by record.

## Report

Owner report: Done (pick, confidence, reason and conditions per query), In Progress, Queries.
