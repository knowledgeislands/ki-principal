# wow-review-red-docs-q - blind review of five queries

You are an independent reviewer. For each query below, read only the repositories named in it (ki-principal at /Users/krisbrown/workspaces/knowledge-islands/ki-principal, ki-design at /Users/krisbrown/workspaces/knowledge-islands/ki-design), verify the Context's factual claims directly where you can, and pick the option you would recommend, with confidence high, medium or low and a one-line reason, noting any claim you found false. Do not read any queries.md, decisions.md or *.report.md file. Read-only: change no file, commit nothing, call no GitHub API.

Report under ## Done one ### section per tag: your pick, confidence, reason, and verified or refuted claims. Then ## In Progress (Nothing) and ## Queries (None).

## RECORD-2 - work-package schema failures in thirteen folders

**Context:** Forty RECORD-2 failures remain in ki-principal, returned unfixed as the approval requires. They sit in `+/_WORK/ki` (7), `ki.portable-specifications` (6), `ki.mac-studio-setup` (4), `ki.baseline-rollout` (4), `ki.tools-burndown` (3), `ki.timelines` (3), `ki.ways-of-working` (2), `ki.regular` (2), `ki.chezmoi` (2), `ki.agent-host` (2), `ki.website` (1), `ki.paperclip-capture-and-rebuild` (1) and `ki.observatory` (1). The messages are the `work.md` front matter (`covers` must be the State of play register array, a parent field), the `messages.md` line shape (important lines, each message's form) and `state.md` fields. Each is a judgement about a live package's definition or queue. **Query:** Should one bounded run fix the forty schema failures package by package, or should each steward fix its own?

**Options (unranked):**

- Leave them until the work-package standard settles.
- Each package's steward fixes its own at its next mark.
- One run per territory sweep: `+/_WORK/ki` and the Project packages ki.ways-of-working stewards, with a read-back of every changed field.

### FOLDER-1 - extras in two work folders

**Context:** `ki.baseline-rollout` holds nine `report-*.md` files outside the closed list, the older single-file report shape, and `ki.mac-studio-setup` holds `design/adobe-remove.sh` and `spec-sched.brief.md`. Renaming or removing them changes those packages' history, so they came back as queries. **Query:** Should the nine reports be renamed to `<name>.report.md`, and the script and brief moved or deleted?

**Options (unranked):**

- Delete the nine reports if their outcomes are homed, and the script and brief with them.
- Rename the nine to `<name>.report.md`, move `adobe-remove.sh` beside its design note's diagram sources or delete it if the note no longer cites it, and keep `spec-sched.brief.md` as `briefs/spec-sched.brief.md`.

### STRUCTURE-1 - ki.specifications holds no regular work file

**Context:** `+/_WORK/ki.specifications` fails because its `work.md` is not a regular file; the folder also carries two listed COORD-7 reports that are now fixed. **Query:** Should the work file be restored as a regular file from Git, or the folder closed?

**Options (unranked):**

- Close the folder under `ki-work-package` if the Project has moved.
- Restore `work.md` from its last committed version and re-audit.

### FILENAME-0 - OPEN.md in the ki-design decisions directory

**Context:** `docs/decisions/OPEN.md` is the open-questions list beside the records. It is read by `docs/design-review/generators/build-boards.ts` and linked from the README and several specs, so moving it is a small engineering change, not a mechanical one. **Query:** Where should the open-questions list live?

**Options (unranked):**

- Keep it and exempt it in the ki-design skill configuration.
- Move it to `docs/OPEN.md` and repoint the generator and links.

### ROUTE-1 - docs/spec is the live design specification

**Context:** ki-guides treats `docs/spec/` as a retired root, but in ki-design it holds the nineteen live specification pages. Moving them to `docs/specs/` under ki-specs is a reclassification of the design specification, not a rename. **Query:** Should the design specification adopt ki-specs under `docs/specs/`, or be declared a guide root?

**Options (unranked):**

- Declare `docs/spec/` in `.ki.toml` as the guide root and keep the pages as they are.
- Adopt ki-specs: rename to `docs/specs/`, add the ki-specs front matter in one run and repoint the links.
