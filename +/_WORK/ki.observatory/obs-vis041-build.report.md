# [Model](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md>) › [Observatory](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md>) › obs-vis041-build

**🤖 → 👤 Handoff to supervisor · Run report at 01:15 BST**

---

## Done

[KI-OBSERVA-VIS-041 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/c1f008346dc085a0c25026ea5c9a08b383ef1d5b/docs/roadmap/KI-OBSERVA-VIS-041-git-view-replaces-repositories.md)'s read-parity phase is delivered and awaiting review. There were no writes, no launchers and no Claude suggestion. The commits are local on `main` and not pushed:

1. `fb456ef`: contracts and evidence, covering the root and folder labels, the unpushed and earlier commits, and the diff reader.
2. `45d5dea`: the `GET /api/repositories/diff` route, with OBS-CONTRACT-002 and the new OBS-BOUND-016 recorded in the specs.
3. `7b9e9e2`: the instrument, with tiles, search, filters, sort, the remembered arrangement, the heatmap, the detail additions, the flash and receipt, the read badge, the root error and root grouping.
4. `f58cc6e`: `degraded.test.ts` and the browser smoke check's Git viewer flow.
5. `b33412d`: the operator's guide and the CHANGELOG.
6. `d27363a`: the record, moved to awaiting-review with its Review section.

Check results:

1. Tests: pass, 8 of 8 tasks, with every existing Repositories test unchanged.
2. Typecheck: pass.
3. Lint: no errors. The 9 warnings are all in files outside this work.
4. Contract shapes: pass.
5. Roadmap audit: FAIL=0. Its 3 size warnings are on other records.
6. Browser smoke check: the Git viewer flow passes. Other flows fail, all outside this record's files, and I haven't compared them with a run before these changes (Query 1).
7. Service: restarted, and <http://127.0.0.1:1675/> answers.
8. Diff refusal: a path from the repository's list of changed files answers 200. A path outside that list, and a `../` path, both answer 403.

Live checklist, checked against the real 51-repository estate at both 1,440 px and 760 px. Neither width scrolls sideways or throws a page error.

1. Summary tiles: met.
2. Search: met.
3. Severity, root and folder filters: met. The folder filter is hidden because no repository here is nested.
4. Sortable columns: met. At 760 px the last-commit column, and its sort button, is dropped as declared.
5. Remembered arrangement: met. It is carried in the address and restored after a reload.
6. Heatmap: met.
7. Detail panel: met. The behind warning appears only in tests, because no live repository is behind.
8. After an operation: met in tests only. Running an operation live would be a write.
9. Read badge: met.
10. One-line root error: met in tests only. No live root fails.
11. Root grouping: met. chezmoi has its own group.

## In Progress

Nothing. The record is in awaiting-review, and accepting it is the owner's decision.

## Queries

**Context:** The full Chromium build is not installed, so I ran the browser smoke check on the headless Chromium shell. The Git viewer flow passes. Other flows report a dimming timing failure in every view and Mermaid frames being refused. I didn't compare these with a run on the commit before my changes, so I can't yet say they come from the headless shell rather than this work (medium confidence).

**Query:** How should the smoke check's other failures be confirmed?

**Options:**

a) (recommended, confidence high - confirming takes one run each and needs no change) In an interactive session, install the full Chromium build and run `bun run self:test:browser` on `04a2ebb` and on `d27363a`, then compare the two.

b) Accept the Git viewer flow alone as this record's smoke evidence.

c) Open a separate record for the smoke check under the headless shell.

**Context:** The detail panel keeps its existing list of the ten most recent commits, because the boundary kept it. That list now overlaps the new unpushed and earlier lists.

**Query:** Should the ten-commit list stay?

**Options:**

a) (recommended, confidence medium - the new lists cover the same commits more clearly) Drop it in a small follow-up once this record is accepted.

b) Keep it as it is.

c) Shorten it to commits older than the earlier five.

```text
Reply:
1: a | b | c
2: a | b | c
```
