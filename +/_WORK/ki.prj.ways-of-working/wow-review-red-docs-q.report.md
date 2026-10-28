# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-review-red-docs-q

**🤖 → 👤 Handoff to supervisor · Run report at 22:11 GMT · last mark 01:07 GMT**

---

## Done

Reviewed all five queries against local evidence. Commits: none; repository changes: none. No excluded files were read, no remote calls made and no subagents used. Verification covers permitted definitions, states, queues, documentation, directory entries and local Git history; it does not reproduce an audit that would read the excluded files.

### RECORD-2 - Work-package schema failures

**Pick:** Each package's steward fixes its own at its next mark. **Confidence:** medium.

**Reason:** Definition, queue and state corrections belong to the explicitly assigned steward; the permitted evidence does not establish a shared steward authorised to edit every package.

**Verified:** All thirteen named packages exist; the main definition lacks `covers`, and all twelve other definitions lack `parent`. Queue-order and state-schema defects are also visible. The [stewardship rule](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/.agents/skills/ki-work-package/references/standards-work-package.md:110) allows an explicitly assigned State of play to act as steward, so a later bounded sweep of its assigned packages is possible.

**Correction/limit:** The supplied package subtotals total **38**, not 40. The exact current failure count, prior approval and committed stewardship assignments were not independently established within the blind-review restrictions. Do not invent coverage from the folder inventory.

### FOLDER-1 - Extras in two work folders

**Pick:** The second option, qualified: rename retained reports and move the brief; the script must leave the work folder. **Confidence:** medium.

**Reason:** Preserve material until its durable home is established, while conforming to the closed list; proximity to diagram sources does not make an operational script admissible.

**Verified/refuted:** There are **ten**, not nine, `report-*.md` files in `ki.baseline-rollout`. Both Mac Studio extras exist, and [the design note still cites the script](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.mac-studio-setup/design/design.md:15). Moving the brief under `briefs/` fits the standard. Moving the script beside diagram sources inside `design/` still violates the [explicit script exclusion](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/.agents/skills/ki-work-package/references/standards-work-package.md:82). Neither option is fully compliant as written: retain a needed script in an agreed home outside the package and update its citation. Report outcomes and brief receipt were not verified from excluded material.

### STRUCTURE-1 - Missing work file

**Pick:** Close the obsolete folder under `ki-work-package`, after the steward's close-out checks. **Confidence:** high.

**Reason:** Restoring the old definition would recreate work that has already moved to the live Portable specifications package.

**Verified:** `ki.specifications/work.md` is absent, rather than a symlink or special file. Local Git records an exact rename to `ki.portable-specifications/work.md` in `a90aea3b`; [the Project note confirms the rename](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/portable-specifications.md:20). The remaining folder contains only report files.

**Correction/limit:** This is not evidence that the distinct, paused Specifications Project is finished. The claim that two COORD-7 report defects are fixed was not checked because reading those reports is prohibited. Close-out still requires confirming that retained outcomes and queries are homed; nothing was deleted.

### FILENAME-0 - Open questions beside decision records

**Pick:** Move the list to `docs/OPEN.md` and repoint the generator and links. **Confidence:** high.

**Reason:** An open-question list is not a Decision Record, and the decisions collection explicitly admits only records and its index.

**Verified:** The list describes open questions; [the generator reads its exact path](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/design-review/generators/build-boards.ts:238), and the README, AGENTS.md, DESIGN.md and several specification pages reference it. Its own relative links also need updating. This is a bounded engineering change. No factual claim in the Context was refuted.

### ROUTE-1 - Live design specification

**Pick:** Adopt `ki-specs` under `docs/specs/`, updating metadata and references in one bounded change. **Confidence:** high.

**Reason:** The collection defines design rules, contracts and verification floors; declaring it a guide root would misclassify its purpose and contradict the guide standard's explicit migration rule.

**Verified:** The guide standard retires `docs/spec/` and directs behavioural specifications to `docs/specs/`. The current index calls this the design spec, and [accessibility defines tested floors](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/spec/accessibility.md:8).

**Qualification:** There are **19 Markdown files**, including the index and migration map, rather than nineteen substantive specification pages. The two hex-terrain proposals are draft; migration must preserve their status and must not imply acceptance. Ancillary pages need classification. The exact `ki-specs` metadata requirements were not verified because that skill is not installed in either repository's skill directory.

## In Progress

Nothing.

## Queries

None.

### 🤖 → 👤 Handoff to supervisor · since 22:11 GMT

🤖 0 running · 👤 1 with you · ⛔ 0 blocked (this run only)

- [with you] Five blind-review recommendations · owner · since 22:11 GMT

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
