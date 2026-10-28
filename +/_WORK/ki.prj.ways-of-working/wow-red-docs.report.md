# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-red-docs

**🤖 → 👤 Handoff to supervisor · Run report at 22:06 GMT · last mark 01:07 GMT**

---

## Done

- ki-design: the decision-record failures are cleared and pushed. Thirty `GDR-KI-DESIGN` records renamed to their title slugs (FILENAME-1), non-sibling links turned to plain text (BODY-11), forward citations of higher-numbered records removed (DEPENDS-4) and four titles quoted so front matter matches the heading (FM-6); every reference across the specs, boards, the board generator, the hexmap package and the handoff answer repointed. One commit, `docs(decisions): conform GDR-KI-DESIGN records to the decision-record rules`, on `main` and level with `origin/main`. Audit failures 127 before, 12 after; the 12 are below as queries.
- ki-principal: the mechanical failures are cleared and pushed in one commit, `docs(audit): clear the mechanical document-rule failures`, level with `origin/main`. Audit failures 242 before, 68 after.
  - COORD-7: 810 flagged identifiers in 129 reports across seven work folders. 759 are now linked: current records to their local file, pruned records to their last revision on GitHub found from local history, five 5G Emerge records in two checkouts to the newer checkout. One report used reference-style links, which the checker cannot read; they are inlined. 51 identifiers in 23 reports cannot be linked from this machine and are a query below.
  - COORD-12: seven reports opened with a `VERDICT:` line; it now sits beneath the bold form line, since no standard places it.
  - MD013 and related: the Context, Query, Options and lettered option lines in the reports are separated into paragraphs rather than merged into one line, which is what `rumdl --fix` would do and did in the trial. The commit hook then ran the formatter over every staged report and demanded the same across 65 of them, so the same separation was applied to all, the hook's other fixes (list and heading spacing, bare URLs, ordered-list numbering, an unused link definition) accepted, and four paragraphs the formatter had merged split back by hand.
  - BODY-11 in four `GDR-KI-PRINCIPAL` records (005, 010, 014, 015): links to Agents, the Lore Sheet and the Mill turned to plain text. Two reports repointed at the renamed ki-design records. `+/_ACQUIRED/README.md` created by the automatic conform (PRINCIPAL-5).
- Limitations: both CI runs were not watched, because the limits forbid any GitHub API call; the audit itself reads ki-design's GitHub live state as part of its own run. Three empty files, `ki-repo-harness.out`, `ki-repo-kb.out` and `ki-repo-tools.out`, appeared untracked at the ki-principal root at 21:53 GMT; they are not mine and were left. The fifteen untracked `wow-*.report.md` files were not touched; none carried a listed finding. Two `hnr-principal` reports still cite old ki-design filenames by pinned GitHub URL and were out of scope.

## In Progress

Nothing is running.

Outstanding - no action requested now: none.

## Queries

### RECORD-2 - work-package schema failures in thirteen folders

**Context:** Forty RECORD-2 failures remain in ki-principal, returned unfixed as the approval requires. They sit in `+/_WORK/ki` (7), `ki.portable-specifications` (6), `ki.mac-studio-setup` (4), `ki.baseline-rollout` (4), `ki.tools-burndown` (3), `ki.timelines` (3), `ki.ways-of-working` (2), `ki.regular` (2), `ki.chezmoi` (2), `ki.agent-host` (2), `ki.website` (1), `ki.paperclip-capture-and-rebuild` (1) and `ki.observatory` (1). The messages are the `work.md` front matter (`covers` must be the State of play register array, a parent field), the `messages.md` line shape (important lines, each message's form) and `state.md` fields. Each is a judgement about a live package's definition or queue.
**Query:** Should one bounded run fix the forty schema failures package by package, or should each steward fix its own?
**Options:**

a) (recommended, confidence medium - the shapes are mechanical but each package's `covers`, parent and queue lines carry meaning only its steward knows) One run per territory sweep: `+/_WORK/ki` and the Project packages ki.ways-of-working stewards, with a read-back of every changed field.

b) Each package's steward fixes its own at its next mark.

c) Leave them until the work-package standard settles.

### FOLDER-1 - extras in two work folders

**Context:** `ki.baseline-rollout` holds nine `report-*.md` files outside the closed list, the older single-file report shape, and `ki.mac-studio-setup` holds `design/adobe-remove.sh` and `spec-sched.brief.md`. Renaming or removing them changes those packages' history, so they came back as queries.
**Query:** Should the nine reports be renamed to `<name>.report.md`, and the script and brief moved or deleted?
**Options:**

a) (recommended, confidence high - the rename is the closed list's own shape and loses nothing) Rename the nine to `<name>.report.md`, move `adobe-remove.sh` beside its design note's diagram sources or delete it if the note no longer cites it, and keep `spec-sched.brief.md` as `briefs/spec-sched.brief.md`.

b) Delete the nine reports if their outcomes are homed, and the script and brief with them.

### STRUCTURE-1 - ki.specifications holds no regular work file

**Context:** `+/_WORK/ki.specifications` fails because its `work.md` is not a regular file; the folder also carries two listed COORD-7 reports that are now fixed.
**Query:** Should the work file be restored as a regular file from Git, or the folder closed?
**Options:**

a) (recommended, confidence medium - I did not open the folder beyond the audit line, so the cause is unverified) Restore `work.md` from its last committed version and re-audit.

b) Close the folder under `ki-work-package` if the Project has moved.

### COORD-7-REST - fifty-one identifiers with no local target

**Context:** Three groups remain in 23 reports. First, 21 `PERSONAL-PRINCIPAL` and `PERSONAL-TOWER-SITE` records whose files are absent from both the working tree and the whole local history of `personal-principal` and `apps-tower.midnight.ninja`, so those checkouts are behind the machine that pruned them, and `KB-ACQUIRE-002` and `-005`, found in no local repository. Second, 25 identifiers that match the record pattern but are not records: `RIG-CONF-016`, `RIG-STATE-033` and other tools-rig specification clauses, the `OBS-ACT-014`, `OBS-BOUND-016` and `OBS-CONTRACT-002` query tags, `PRUNE-GOV-201`, `SPLIT-5GE-004`, `SITE-RT-033` and `MGIT-WS-009`. Most sit in `ki.baseline-rollout/sizekind-1.report.md` (20) and `ki.mac-studio-setup`.
**Query:** Should the personal checkouts be fetched so the pruned links can be written, and should the non-record identifiers be exempted or rewritten?
**Options:**

a) (recommended, confidence high - fetching is read-only and the identifiers are verifiably not records) Authorise a fetch of `personal-principal` and `apps-tower.midnight.ninja` so a short run writes the pruned links, and let the same run rewrite the 25 tag-like identifiers in code spans so the checker passes them as text.

b) Leave the 51 as the standing floor for these reports and change the checker to skip identifiers that match no registered prefix.

### FILENAME-0 - OPEN.md in the ki-design decisions directory

**Context:** `docs/decisions/OPEN.md` is the open-questions list beside the records. It is read by `docs/design-review/generators/build-boards.ts` and linked from the README and several specs, so moving it is a small engineering change, not a mechanical one.
**Query:** Where should the open-questions list live?
**Options:**

a) (recommended, confidence high - keeps the file one directory up with its generator and links repointed in the same commit) Move it to `docs/OPEN.md` and repoint the generator and links.

b) Keep it and exempt it in the ki-design skill configuration.

### ROUTE-1 - docs/spec is the live design specification

**Context:** ki-guides treats `docs/spec/` as a retired root, but in ki-design it holds the nineteen live specification pages. Moving them to `docs/specs/` under ki-specs is a reclassification of the design specification, not a rename.
**Query:** Should the design specification adopt ki-specs under `docs/specs/`, or be declared a guide root?
**Options:**

a) (recommended, confidence medium - ki-specs is the territory's shape for accepted behaviour, but the pages mix rationale and specification) Adopt ki-specs: rename to `docs/specs/`, add the ki-specs front matter in one run and repoint the links.

b) Declare `docs/spec/` in `.ki.toml` as the guide root and keep the pages as they are.

### GH-LIVE - nine GitHub settings findings in ki-design

**Context:** The audit's live-state rules fail on the repository's GitHub settings: empty description (GH-3), merge methods and head-branch deletion (MERGE-1), Issues and Projects enabled (TOGGLE-1), no topics (TOPICS-1), Dependabot security updates and branch updating off (DEP-1), secret scanning and push protection off (SEC-1). The limits forbid any GitHub change from this run.
**Query:** May one bounded run apply the standard settings through `ki repo conform`?
**Options:**

a) (recommended, confidence high - these are the territory's declared settings and the conform applies them idempotently) Authorise one run with the GitHub call lifted for `knowledgeislands/ki-design` only.

b) Set them by hand from the GitHub settings page.

### BIO-1 - absent from this audit

**Context:** The approval bounds BIO-1's configuration migration separately. Neither audit reported a BIO-1 failure, so nothing was done and nothing is pending from this run.
**Query:** Is a separate BIO-1 unit still wanted?
**Options:**

a) (recommended, confidence high - the rule produced no finding in either repository) Drop it unless a later audit raises it.

b) Brief a separate run to check the configuration anyway.

### CI-WATCH - the CI runs were not observed

**Context:** The brief asks for both CI runs to be watched, and its limits forbid any GitHub API call, which is the only way to read a run's result. Both pushes are level with `origin/main`; the ki-principal commit passed the repository's own scoped audit in its hook.
**Query:** How should a run observe CI when the API is closed to it?
**Options:**

a) (recommended, confidence high - a read-only run watch is the smallest lift) Lift `gh run watch` for pushed commits in future briefs that ask for CI observation.

b) Leave CI observation to the coordinator's next check.
