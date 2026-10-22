# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › link1-baseline

**🤖 → 👤 Handoff to supervisor · Run report at 22:17 BST · last mark 22:12 BST**

---

## Done

Commit `1b8ab57b` — `fix(ki-repo-kb): warn on link resolution until strict opt-in`; eight explicit harness paths, hook-verified, with the GPT-6 co-author trailer.

LINK-1 — restored the pre-`2d28656f` ambiguous-wikilink failure boundary; separate resolution findings now WARN, including missing, wrong-case and template targets.

Strict resolution — supported through boolean `strict_link_resolution = true` in `[skills.ki-repo-kb]`; absent or false preserves WARN, and invalid value types fail configuration validation.

Fixtures — 26 focused tests passed, covering resolution syntax and casing, working-area ambiguity boundaries, default/false/true opt-in, invalid types and hosted severity overrides.

Harness tests — 1,294 passed; zero failures.

Type check — passed.

Focused audits — ki-skills, ki-authoring and ki-engineering passed; the changed KB rubric ran in each island's full audit.

Full harness audit — zero failing skills/findings; 86 warning findings across four skills.

Generated publication — rubric regenerated and verified; ki-repo-kb supplies no additional generated surfaces.

Publication — pulled with rebase and pushed fast-forward to `origin/main`; only this run's commit was unpublished. Post-hook committed paths matched the intended eight; checkout clean and local/remote-tracking heads equal on `sol.local`.

### Full island audit baseline

Same installed CLI (`ki` 0.11.5), same live island checkouts, complete unscoped audits. The before run loaded an archived harness at `9c17df3c` through a process-local data-directory override; the after run loaded the primary harness checkout based on `af4cb478` plus this fix. No island files or persistent bindings were edited.

P/W/F below counts skill verdicts; finding counts are individual findings. Every full island audit still exits nonzero for recorded pre-existing failures.

| Island | Before P/W/F | After P/W/F | Before findings F/W | After findings F/W | New FAIL subjects |
| --- | --- | --- | --- | --- | --- |
| ki-principal | 18/2/5 | 18/3/4 | 34/35 | 26/36 | 0 |
| personal-principal | 14/2/6 | 14/3/5 | 24/52 | 16/53 | 0 |
| hnr-principal | 17/1/5 | 17/2/4 | 22/50 | 14/51 | 0 |

Comparison — no added FAIL criterion/subject pairs or increased multiplicities; legacy LINK-1 failure samples matched exactly after normalising their explanatory prefix. ki-principal remains free of legacy LINK-1 failures; personal-principal and hnr-principal retain theirs, alongside separate resolution warnings.

### Recorded pre-existing failure counts

| Island | Criterion | Before | After |
| --- | --- | --- | --- |
| ki-principal | BODY-11 | 2 | 2 |
| ki-principal | COORD-7 | 1 | 1 |
| ki-principal | DEPENDS-4 | 2 | 2 |
| ki-principal | KNIP-2 | 1 | 1 |
| ki-principal | RECORD-2 | 19 | 19 |
| ki-principal | RUNTIMES-2 | 8 | 0 |
| ki-principal | TSC-1 | 1 | 1 |
| personal-principal | BODY-11 | 4 | 4 |
| personal-principal | COORD-7 | 5 | 5 |
| personal-principal | LINK-1 | 1 | 1 |
| personal-principal | MD-mech | 1 | 1 |
| personal-principal | RECORD-2 | 5 | 5 |
| personal-principal | RUNTIMES-2 | 8 | 0 |
| hnr-principal | LINK-1 | 1 | 1 |
| hnr-principal | MD-mech | 1 | 1 |
| hnr-principal | NOTE-1c | 1 | 1 |
| hnr-principal | RECORD-2 | 3 | 3 |
| hnr-principal | RUNTIMES-2 | 8 | 0 |
| hnr-principal | STREAM-9 | 8 | 8 |

Checkout heads observed during comparison: ki-principal `346275ee`; personal-principal `fe2d0ae6`; hnr-principal `14e846a7`. These were live checkouts, not frozen repository snapshots.

## In Progress

Nothing running. The recorded island failures remain outside this harness fix's scope.

## Queries

None.

### 🤖 → 👤 Handoff to supervisor · since 22:17 BST

🤖 0 running · 👤 1 with you · ⛔ 0 blocked

- [handoff-to-supervisor] link1-baseline review · ki.ways-of-working coordinator · since 22:17 BST
