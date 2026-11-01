# [Model](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › discussions-plan

**🤖 → 👤 Handoff to supervisor · Run report at 00:24 GMT · last mark 13:55 GMT**

---

## Done

- Planned the DISCUSSIONS - b rollout (Kris, 1 November 2026, "Files too"), starting from [design/discussions/design.md](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/discussions/design.md). Nothing was changed and nothing committed; the plan exists only in this report, under Findings.
- Searched every repository under `/Users/krisbrown/kis/`, the chezmoi source and `/Users/krisbrown/workspaces/git/`. Readers and writers were found in 7 repositories: the harness, `tools-ki`, the Observatory, the website, chezmoi, and two Knowledge Islands Principal notes. There are 60 tracked `queries.md` files in 9 repositories, none in `+/_WORK_REVIEW/`, and no `discussions.md` yet.
- The hook line needs no change: `hooks/coordinator-reminder.sh` contains no query wording. The output style does change, and under the restart rule that is a trigger for every live coordinating thread.
- These hits are unrelated and stay out of scope: `tools-rig`'s `RIG-QUERY` spec, the 5G-EMERGE "source queries", HNR-PRINCIPAL-PRD-001's "Queries to settle", `ki-repo-kb` search "query" mode, and `tools-ki` `kb` search.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Harness `main` moved twice while this run was going (`fb19794d` to `30584fd2`). Runs `reports-folder` (worktree at `fb19794d`) and `quiet-listen` (`ki-agentic-harness-quiet-listen`) are still open against the same standards and rubrics. Harness unit U1 should start only after both land.
- The design note's "about 59 packages" is now 60.

## Findings

### PLAN - DISCUSSIONS rollout: readers, then writers, then the sweep

**Goal:** an ordered, owned rollout that renames queries to discussion points everywhere Kris reads, and `queries.md` to `discussions.md` in every package, with no point lost from view at any step.

**Scope:** every reader and writer of `queries.md`, the `## Queries` report section and the query vocabulary, across `/Users/krisbrown/kis/`, the chezmoi source and `/Users/krisbrown/workspaces/git/`. The plan changes nothing.

**As of:** 2 November 2026, 00:24 GMT. Harness at `30584fd2`.

#### Where the words live

| Repository · owner | Readers (parse the file or section) | Writers (wording and shapes) |
| --- | --- | --- |
| `ki-agentic-harness` · ki.prj.ways-of-working | `ki-work-package` rubric: `contexts/work-package.ts` (`PACKAGE_FILES`, the H1 `# <id> queries` with Open and Parked check, the legacy message), `contexts/work-folder.ts` (`QUERIES_FILE`, the report `## Queries` parse, the eight-point cap), `items/folder.ts`, `items/records.ts` and their tests. `ki-coordination` rubric: `contexts/coordination.ts` (the `## Queries` prose), `items/threads.ts`, `coordination.test.ts`. `ki-repo-kb` rubric: `contexts/kb.ts` (known package files), `items/index.test.ts` | `ki-coordination` `standards-coordination.md` (125 mentions), `SKILL.md` and its description, `references/rubric.md` and `scripts/banner.test.ts` (`queries parked`, `Query <n> of <total>`). Output style `output-styles/ki-coordinator.md` (17). `ki-work-package` `standards-work-package.md` (25), `SKILL.md` and its description, `rubric.md`. `ki-delegation` `assets/run-prompt.md` (Report paragraph), the four footers `assets/rules-{none,push,prune,release}.md`, `standards-background-runs.md` (12), `rubric.md`, `items/background-runs.ts`. Also `skills/README.md` and `ki-repo-kb/references/standards-frontmatter.md`. The `sources.md` files stay as history |
| `tools-ki` · ki.prj.tools-burndown | `src/core/agent/events.ts` `reportQueries`, which drives `ki agent wait` query events; `src/core/agent/thread.ts` `queryOptions`, which drives `ki agent decide <TAG> - <letter>`; tests `agent-events`, `agent-threads`, `agent-control`, `agent-control-matrix`, `agent-prompts` and fixture `agent-crash-child.ts` | `src/core/agent/runs.ts:420`, the progress protocol's "outstanding queries"; `docs/guides/user/background-agents.md` (the `decide` paragraph); the `decide` `--title` help |
| `apps-observatory.local` · ki.prj.observatory | `packages/contracts/src/review.ts` (`QUERIES_HEADING`, `OPEN_HEADING`, `QUERY_RULE`), `packages/evidence/src/review.ts` (`QUERIES` file name), `packages/evidence/src/focus.ts` (`+/_WORK/<id>/queries.md`), `work-package.ts`, and the tests and fixtures in both packages | `packages/instruments/src/registry.ts` (the instrument text), `docs/guides/operator/read-the-instruments.md`. PDR-KI-OBSERVA-010 stays as history |
| `apps-knowledgeislands.info` · ki.prj.website | none | `src/docs/ways-of-working/{work-packages,coordination,background-runs,the-work-model,tending}.md`, `src/docs/working-with-agents/{the-work-package,coordinating-background-agents}.md`, the diagrams `work-folder.*` and `coordinating-turn.*`, and `_data/skillCatalogue.json5`, which regenerates from skill descriptions |
| chezmoi source · ki.prj.chezmoi | none | `dot_claude/private_communication.md`: "Queries are logged in the written report", "Queries taken interactively". The second checkout `~/kis/personal/dotfiles`, same remote, follows by pull |
| `ki-principal` · ki.prj.ways-of-working | none | `Pillars/Philosophy/Model/Processes/Work Process/Work Process.md` (11 mentions). [GDR-KI-PRINCIPAL-009](/Users/krisbrown/kis/knowledge-islands/ki-principal/Admin/Governance/Decisions/GDR-KI-PRINCIPAL-009-the-work-model.md) (8) stays as a decision of its date |

#### Packages to rename

| Repository | Packages | Live files that link `queries.md` |
| --- | --- | --- |
| `hnr-principal` | 26 | 12 |
| `ki-principal` | 16 | 12 |
| `personal-principal` | 9 | 7 |
| `va-principal` | 4 | 1 |
| `er-principal`, `legal-principal`, `si-principal`, `tmx-principal`, `acquire` | 1 each | 1 in `legal-principal`, otherwise 0 |
| **Total** | **60 in 9 repositories** | 33 |

"Live files" means each package's `state.md`, `work.md`, `messages.md` and queries file. Reports and decision logs that mention `queries.md` (about 120 more files) are history and keep their text.

#### The tolerance-window rule

1. **Opens** at gate G1, once units U1 to U3 are released and installed on sol and terra.
2. **While open, every reader:**
   - accepts `discussions.md` or `queries.md`, preferring `discussions.md`;
   - accepts `## Discussion` or `## Queries` in reports and single-file `work.md`;
   - accepts a package H1 of either `# <id> discussions` or `# <id> queries`, still with `## Open` and `## Parked`.

   A package holding both files fails the `ki-work-package` rubric, and the other readers read `discussions.md` and flag it.
3. **Writers switch only after G1** (U4). Runs and coordinators write `## Discussion` in reports. A new package is created with `discussions.md`. An existing package keeps writing whichever file it holds. Nothing creates a `queries.md` after U4.
4. **Closes** (U11) once the sweep is confirmed on both Macs, meaning no `queries.md` under any `+/_WORK/` on sol or terra:
   - a leftover `queries.md` becomes a rubric failure, and the standard drops its both-names paragraph;
   - `tools-ki` and the Observatory drop the file-name fallback at their next ordinary change;
   - `## Queries` in reports stays accepted for good, as `## Outstanding queries` already is, because past reports keep it.
5. **Machine names stay**: the `query` event kind in `ki agent wait`, JSON fields, function names and the Observatory's API fields. Only text Kris reads changes. This follows the decision's "everywhere Kris reads".

#### Ordered units

| # | Unit | Repository · owner | Size | Waits on |
| --- | --- | --- | --- | --- |
| U1 | **Harness readers.** Make the rubrics and tests listed above accept both file names, both section names and both H1s, and fail a package holding both files. Add the reader half of the tolerance paragraph to `standards-work-package.md`. Release | `ki-agentic-harness` · this work | M | `reports-folder` and `quiet-listen` landed (same files) |
| U2 | **`ki` readers.** `reportQueries` and `queryOptions` accept `## Discussion`; tests cover both; release | `tools-ki` · ki.prj.tools-burndown | S | nothing; parallel with U1 |
| U3 | **Observatory readers.** Read `discussions.md` first, then `queries.md`; accept both section names; flag a package holding both; tests and fixtures cover both; deploy | `apps-observatory.local` · ki.prj.observatory | M | nothing; parallel with U1 |
| G1 | **Gate.** U1 to U3 installed on sol and terra (harness and `ki` updated on each Mac; the Observatory restarted) | Kris or each Mac's Rig thread | - | U1, U2, U3 |
| U4 | **Harness writers.** Make the vocabulary change in the coordination and work-package standards, the output style, the delegation run prompt, footers and standard, the rubric texts, the banner test and the skill descriptions:<br>• Discussion, Point n of total, tags, blocking point;<br>• the closing list of decisions reached before the mark;<br>• "noted, no decision";<br>• new packages get `discussions.md`, and State of play's package-creation rule says "empty discussions";<br>• the H1 `# <id> discussions`.<br>Release, then send the REFRESH line to every live package | `ki-agentic-harness` · this work | L | G1 |
| U5 | **Wording followers**, in parallel:<br>• (a) `ki` run-prompt wording, guide and help;<br>• (b) Observatory instrument text and guide;<br>• (c) the Work Process note in `ki-principal` (Kris's decision stands in for the Enactment record);<br>• (d) chezmoi `private_communication.md`, applied on both Macs after a reviewed `chezmoi diff`;<br>• (e) the website pages and diagrams | (a) ki.prj.tools-burndown, (b) ki.prj.observatory, (c) this work, (d) ki.prj.chezmoi, (e) ki.prj.website | S, S, S, S, M | U4 |
| U6 | **Sweep pilot: `ki-principal`, 16 packages.** One run per repository does the following:<br>• `git mv queries.md discussions.md`;<br>• retitles the H1;<br>• repoints links in the live files and live design notes, leaving history;<br>• runs the `ki-work-package` rubric;<br>• commits, then pushes fast-forward only under an explicit push rule in its brief;<br>• stops on a live run, an uncommitted package file or divergence | `ki-principal` · this work | M | U4 installed on both Macs; every live package in the repository has `method_read` at or after U4, or is on hold; the repository is clean and level on both Macs (SWEEP-GATE); the repository's TOP-LEVEL-SWEEP-MOVE run finished; no `~/world` repository move under way |
| U7 | **Sweep the rest, three at a time:**<br>• `hnr-principal` (26, M) and `personal-principal` (9, S);<br>• `va-principal` (4), `er-principal`, `legal-principal`, `si-principal`, `tmx-principal` and `acquire` (1 each), XS each | each repository · this work, with a heads-up line to its State of play | 9 runs in all, U6 included | U6 clean, plus U6's per-repository gates |
| U8 | **Close the window**, as in step 4 of the rule | harness · this work; lines to ki.prj.tools-burndown and ki.prj.observatory | S | U7 confirmed on both Macs |

Chain U1 and U4, which touch the same harness files. Run different repositories in parallel. The critical path is U1 → G1 → U4 → install on both Macs → U6 → U7 → U8.

#### Draft message lines

ki.prj.tools-burndown `messages.md`, now:

```markdown
- 2026-11-02 · DISCUSSIONS-KI · KI > Model > Ways of working (ki.prj.ways-of-working): Kris decided DISCUSSIONS - b on 1 November 2026 ("Files too"): queries become discussion points, the report section `## Queries` becomes `## Discussion`, and each package's `queries.md` becomes `discussions.md`, readers first. Your half now: `reportQueries` in `src/core/agent/events.ts` and `queryOptions` in `src/core/agent/thread.ts` accept `## Discussion` beside `## Queries` and `## Outstanding queries` (both old names kept for good, for older reports), with `agent-events`, `agent-threads` and `agent-control` tests covering both; release, install on sol and terra, and send a receipt line. Later, once the DISCUSSIONS REFRESH line reaches you: the progress protocol's "outstanding queries" in `src/core/agent/runs.ts` becomes "outstanding discussion points", and `docs/guides/user/background-agents.md` and the `decide` help follow. Machine names (the `query` event kind, JSON fields, function names) stay. After the territory sweep a closing line will ask you to drop any `queries.md` fallback at your next change.
```

ki.prj.observatory `messages.md`, now:

```markdown
- 2026-11-02 · DISCUSSIONS-OBS · KI > Model > Ways of working (ki.prj.ways-of-working): Kris decided DISCUSSIONS - b on 1 November 2026 ("Files too"): queries become discussion points, the report section `## Queries` becomes `## Discussion`, and each package's `queries.md` becomes `discussions.md`, readers first. Your half now: `packages/contracts/src/review.ts` (`QUERIES_HEADING`, `QUERY_RULE`) accepts `## Discussion` beside `## Queries`; `packages/evidence/src/review.ts` and `focus.ts` read `+/_WORK/<id>/discussions.md` first and `queries.md` otherwise, reading `discussions.md` and flagging the package when both exist; package H1 may be `# <id> discussions` or `# <id> queries`, still with `## Open` and `## Parked`; tests and fixtures cover both; deploy on sol and terra and send a receipt line. Later, once the DISCUSSIONS REFRESH line reaches you: the instrument text in `packages/instruments/src/registry.ts` and `docs/guides/operator/read-the-instruments.md` say discussion points and `discussions.md`. API field names stay; PDR-KI-OBSERVA-010 stays as history.
```

Every live package's `messages.md`, at U4:

```markdown
- IMPORTANT · <date> · REFRESH · KI > Model > Ways of working (ki.prj.ways-of-working): Read [coordination](/Users/krisbrown/.agents/skills/ki-coordination/references/standards-coordination.md) and [work package](/Users/krisbrown/.agents/skills/ki-work-package/references/standards-work-package.md) at `<revision>` before your next report, then record method_read. Under DISCUSSIONS (Kris, 1 November 2026) your report section is `## Discussion`, the pass counts "Point <n> of <total>", a finished discussion lists the decisions it reached before the mark, and a point may close "noted, no decision". Keep writing your existing `queries.md` until the sweep renames it to `discussions.md`; never create a new `queries.md`. The output style changed, so restart this thread when convenient.
```

ki.prj.chezmoi `messages.md`, at U4:

```markdown
- <date> · DISCUSSIONS-COMMS · KI > Model > Ways of working (ki.prj.ways-of-working): under DISCUSSIONS (Kris, 1 November 2026) queries are now discussion points. In `dot_claude/private_communication.md`, "Queries are logged in the written report" and "Queries taken interactively" become discussion points, keeping the Context, Query and Options shape and the recommended-first rule; review `chezmoi diff` and apply on sol and terra.
```

ki.prj.website `messages.md`, at U4:

```markdown
- <date> · DISCUSSIONS-SITE · KI > Model > Ways of working (ki.prj.ways-of-working): under DISCUSSIONS (Kris, 1 November 2026) queries are discussion points, the report section is `## Discussion` and the package file is `discussions.md` (harness `<revision>`). Please update `src/docs/ways-of-working/{work-packages,coordination,background-runs,the-work-model,tending}.md`, `src/docs/working-with-agents/{the-work-package,coordinating-background-agents}.md` and the `work-folder` and `coordinating-turn` diagrams, in plain English, and regenerate the skill catalogue from the released skill descriptions.
```

Each swept repository's State of play `messages.md` (hnr.sop.main, personal.sop.main, va.sop.main, er.sop.main, lgl.sop.main, si.sop.main, tmx.sop.main; personal.reg.acquire-intake for `acquire`), before its run:

```markdown
- <date> · DISCUSSIONS-SWEEP · KI > Model > Ways of working (ki.prj.ways-of-working): under DISCUSSIONS (Kris, 1 November 2026) one run will rename `queries.md` to `discussions.md` in this repository's <n> work packages once the repository is clean and level on sol and terra, then push. Commit and push your package files before it runs and pull straight after; nothing else in your package changes.
```

## Queries

### SWEEP-GATE - What "both Macs level" means before each repository is swept

**Context:** On 31 October Kris asked that the rename sweep wait until "host sync has both Macs level", to avoid clashes between the two Macs, sol and terra. Host sync is not yet running routinely. Sol's sync loop stopped at its session restart on 31 October and has not resumed, and no host-sync executor or schedule has been chosen. A wholesale move of every repository to `~/world/<territory>/<repo>` is also being prepared. The sweep renames a file in 60 work packages across 9 repositories. If either Mac holds unpushed changes to those packages, or the move happens mid-sweep, the two copies drift apart and someone has to merge them by hand.

**Query:** Should each repository's sweep wait for a one-off check that that repository is clean and level on both Macs, or wait until host sync runs routinely and the repository move is finished?

**Options:**

a) (recommended, confidence medium - it meets the aim of Kris's words without waiting on host sync, which has no date; but it reads "host sync" as a check rather than the running service) Just before each repository's run, each Mac's Rig thread or Kris makes a fresh one-off check that the repository is committed, pushed and level on both Macs. The run then renames and pushes at once, and the other Mac pulls before any coordinator there writes. No sweep runs while the `~/world` move is under way.

b) Hold the whole sweep until host sync runs routinely on both Macs and the `~/world` move has finished. The readers and writers (U1 to U5) go ahead meanwhile, and the old and new names live side by side until then.

### 🤖 → 👤 Handoff to supervisor · since 00:24 GMT

👤 1 with you

- [with you] SWEEP-GATE · owner · since 00:24

🧵 ki.prj.ways-of-working
