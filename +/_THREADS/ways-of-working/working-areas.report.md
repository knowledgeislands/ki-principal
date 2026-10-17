# [Knowledge Islands model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Initiatives/knowledge-islands-model/knowledge-islands-model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working/ways-of-working.md) › working-areas

**Run report at 23:49 BST · last mark 22:34 BST**

---

## Done

- ki-agentic-harness `aa5d0b03` `docs(ki-repo-kb): call + and - working areas; staging is a state`, pushed fast-forward with no other session's commits carried. It changes ki-repo-kb (SKILL.md, knowledge-base, frontmatter, digest, sources and exemplars references, rubric items and the regenerated `references/rubric.md`), the rubric context in `kb.ts` (messages, plus the `STAGING` and `stagingAreas` identifiers renamed to `WORKING_AREAS` and `workingAreas`), the ki-repo-kb eval scenario and two ki-repo lines ("staging model" became "working-area model"). The knowledge-base standard now says once that staging is a state: material brought into a repository lands in the `+` working area and is staged there until it is accepted or routed.
- Harness checks: `bun run test` passed (1210 tests), `bunx tsc --noEmit` passed, the rubric publication check passed, and the `ki-repo` and `ki-skills` audits passed. `ki repo audit --skill ki-repo-kb` does not run in the harness, because the harness does not declare that skill, so I ran it against ki-principal instead. It passed with no failures; its 4 warnings are existing fleet findings, such as STREAM-10 on the website Project.
- ki-principal `4662b1e` `docs(model): call + and - working areas`, pushed fast-forward with no other session's commits carried. It covers 8 canonical notes: `AGENTS.md`, Structure, Session Digest, Health Check, Tools, How Tools Connect, KB Filesystem and [SDR-KI-PRINCIPAL-002](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/SDR-KI-PRINCIPAL-002-the-home-of-knowledge.md). The SDR keeps its sentence "Staging is not canonical knowledge", where staging is a state. The repository's commit gate passed.
- Kept as they were, because "staging" there means the act or state, the Git index, or acquisition mechanics: acquisition and housekeeping skills, ki-git (its "staging-area leftovers" row means Git index entries), ki-repo-mcp, roadmap records including [KI-HARNESS-GOV-203](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-203-git-clean-down-criteria.md), harness decision records, [ADR-KI-PRINCIPAL-001](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/ADR-KI-PRINCIPAL-001-provider-neutral-knowledge-acquisition.md), the Acquisition Process and Routing Rules.
- Another session's dirty file was left untouched: ki-principal `+/_THREADS/chezmoi/decisions.md`.

## In Progress

Nothing is running.

Outstanding - no action requested now

- tools-ki, which belongs to another session and was not edited, still names the `+` and `-` keys as staging in two places: `docs/guides/user/kb-search.md:25` ("quoted `"+"`/`"-"` staging keys") and `docs/specs/kb-search.md:21` ("staging keys projected as `inbound`/`outbound`"). It also has "staging-area leftovers" in [KI-TOOL-KI-CLI-140](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-140-git-hygiene-estate-audit.md) at lines 22 and 43, where it means the Git index and is a roadmap record, so it needs no change. These go to the coordinator as a Messages line for the tools-ki session.

## Queries

No outstanding queries

```text
No reply needed.
```

```text
╭─ run report · 2026-10-17T22:49:35Z ──────────────╮
│                                                  │
│  █▀▀▄ █▀▀▀ █▀▀▀ ▀▀█▀   · thread at rest          │
│  █▀▀▄ █▀▀  ▀▀▀█   █    · nothing running         │
│  █  █ █▄▄▄ ▄▄▄█   █    · nothing queued          │
│                                                  │
╰──────────────────────────────────────────────────╯
```

- [at rest] nothing running or queued
- [committed] ki-agentic-harness and ki-principal, pushed
