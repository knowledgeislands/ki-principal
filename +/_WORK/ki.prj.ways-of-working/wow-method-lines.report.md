# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-method-lines

**🤖 → 👤 Handoff to supervisor · Run report at 01:04 GMT · last mark 02:10 BST (23 October)**

---

## Done

- Sorted all fifteen METHOD-LINES lines in [method-lines.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/method-lines.md), committed in ki-principal `76107af7` with only that path staged; the pre-commit hooks passed, and nothing was pulled or pushed because the checkout holds other sessions' uncommitted files.
- Already carried, so these lines can be removed: KI-SOP-PATTERN and SOP-SECONDARY (on harness `main` at `703384eb`, tools-ki `5da74e0a`), OP-CACHE-RULE (background-run standard, harness `1ec09f15`), MOD-LEDGER (`_ISSUES.md` reads `MOD: 10`).
- Covered by open queries already in `queries.md`: INTERACTIVE-QUERIES with SELF-CONTAINED and PASS-PROMPT (QUERY-RULES), INITIATIVES-RESIDUE and THEME-REGISTRY-ENFORCE (THEME-CLOSE), CF-UNIFORM (RUN-SECRETS), CHEZMOI-REMIT's no-host rule (HOST-SEAT, HOST-TARGET).
- Open, with a small next step that needs no new decision: WORK-PROCESS-NOTE rides the Work Process note record planned in the model-shape report; CENTRAL-TICK becomes an idea line on the Ways of working Project note; COORD2-RUBRIC's remaining `label` check at `coordination.ts:372` is a one-line fix for the next coord-standard run; WORK-STATUS-FORM goes to ki.tools-burndown, with its message line drafted in the note.
- Correction: the 1Password half of RUN-SECRETS has already landed, so that query should be narrowed to the Cloudflare half.
- REPO-METADATA's method half is carried by the repository metadata note, and PERSONAL-RESERVED's pointer request is already met there. Two points in the note remain open: optional tag types, and README restatement.
- PERSONAL-RESERVED's two findings now have owners:
  - The 24-character cap exists only in `ki-repo`'s shared identifier grammar, with no standard text. The `ki-repo` standard owns it, and the work that carries it is KI-REPO-HOME.
  - The prefix checks are in `ki-repo-kb-streams` and `ki-work-roadmap`. Work-record identifiers are this work's scope, so this work owns them.
  - Message lines for both are drafted in the note. Nothing was written into another work's files.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- When the coordinator receives this report, it removes METHOD-LINES and PERSONAL-RESERVED from `messages.md`, sends the WORK-STATUS-FORM line to ki.tools-burndown, and narrows RUN-SECRETS.
- The three queries below are all medium confidence. Each goes to one masked blind review before it reaches Kris.

## Queries

### KI-REPO-HOME - which work carries `ki-repo` standard and checker changes

**Context:** State of play queued REPO-METADATA's `ki-repo` change with ki.baseline-rollout: the hyphen-only `ki-` topics and the `territory_code` and `territory_tag_types` keys. That work's `work.md`, however, puts "harness skills and standards" out of its scope and gives them to ki.ways-of-working. This work's own scope covers the work model, coordination, delegation and work-record standards, not repository metadata. Wording for the 24-character `repo_code` cap, from PERSONAL-RESERVED, would ride with whichever work carries the `ki-repo` change. Personal has already shortened its two site codes, so nothing is blocked.

**Query:** Should ki.baseline-rollout carry `ki-repo` standard and checker changes, with its Out line narrowed to the work-model skills?

**Options:**

a) (recommended, confidence medium - needs blind review; repository metadata is baseline conformance across every repository, and State of play already routed it there) ki.baseline-rollout carries the `ki-repo` change, the repo-code cap wording included, and its `work.md` Out line reads "work-model harness skills and standards (ki.ways-of-working)".

b) ki.ways-of-working carries it, and its scope widens to `ki-repo`'s repository contract.

### LEGACY-PREFIX - how a `repo_code` rename passes the streams and roadmap audits

**Context:** the `ki-repo-kb-streams` streams audit and `ki-work-roadmap`'s checks fail every record not prefixed with the current `repo_code`. A rename therefore has to happen in one sweep, or the repository fails its audit until every record has moved. Personal is renaming KB to PERSONAL that way now. An allowance, an optional list of former codes that existing records may keep while new records take the new code, would allow a gradual path. It would need both checkers and the tools-ki readers to change.

**Query:** Should a `repo_code` rename stay a one-sweep change, written into `ki-work-roadmap`, rather than gaining a legacy-prefix allowance?

**Options:**

a) (recommended, confidence medium - needs blind review; renames are rare and Personal's runs as one sweep, so documenting the sweep costs one paragraph where the allowance costs two checkers and tools-ki) Write the rename into `ki-work-roadmap` as one sweep: every record and in-repository reference in one commit, pruned links keeping their pinned revisions.

b) Add an optional legacy-prefix list accepted by both audits for existing records only, with new records required to use the current code.

### PARTIAL-REPOS - how a repository with only Pillars and Resources fits the model

**Context:** HNR keeps hnr-shared, which holds only Pillars and Resources, beside hnr-principal. ZONE-1 requires all five zones, and the registry binds one source store per declared repository, so hnr-shared cannot be declared. Its store is written up only in tracked notes, so `ki repo store` and the source audits do not see it. Kris asked Knowledge Islands to decide where partial repositories fit, and whether a person keeps a personal "work" knowledge base beside a person-agnostic company Capital, adding: "there's [a] kind [of] weird thing here we maybe need to come back to." The question reaches the Structure note, `ki-repo-kb` and tools-ki, beyond this work's method scope.

**Query:** Should PARTIAL-REPOS wait as an idea until Kris opens it, rather than starting a design now?

**Options:**

a) (recommended, confidence medium - needs blind review; Kris's own words defer it, and nothing is broken beyond HNR's tracked-notes workaround) Record it as an idea on the Ways of working Project note with the HNR evidence linked, and start a `ki-work-design` brief when Kris opens it.

b) Start a `ki-work-design` brief now covering partial repositories, the personal "work" knowledge base and the store-binding gap.

### 🤖 → 👤 Handoff to supervisor · since 01:04 GMT

👤 3 with you

- [with you] KI-REPO-HOME · owner · since 01:04
- [with you] LEGACY-PREFIX · owner · since 01:04
- [with you] PARTIAL-REPOS · owner · since 01:04
- [committed] design/method-lines.md

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
