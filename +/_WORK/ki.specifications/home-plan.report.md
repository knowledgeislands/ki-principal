# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Portable specifications](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/portable-specifications.md) › home-plan

**🤖 → 👤 Handoff to supervisor · Run report at 01:09 BST · last mark 23:45 BST**

---

## Done

- Wrote [design/home-plan.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/home-plan.md), the ready-to-run plan for step 6, checked against ki-agentic-harness as it stands, with a clean working tree. Nothing else was written, nothing was committed and the harness was not changed.
- The common transform: each homed reference is its approved draft with only four changes. The Status line becomes version 1, the CC BY 4.0 attribution is kept word for word, the nine links between the specifications become plain names, and a Contents list is added because each file is over the 100-line warning limit.
- 6a, ki-work-package: adds `standards-work-spec.md` and the house profile as `standards-work-spec-profile.md`, beside the standard, which does not change. SKILL.md gets one new Shared model bullet, sources.md gets two new rows, and the rubric gets a SPEC family with SPEC-1, then is regenerated.
- 6b, ki-acquire: adds `standards-acquire-spec.md`. SKILL.md gets one paragraph, sources.md gets two bullets, and the rubric gets SPEC-1, then is regenerated. There is no profile file; the provider front matter mapping is recorded as provenance.
- 6c, the new ki-knowledge-package: a declaration-only governance skill. The plan gives its SKILL.md in full, the reference, sources.md (external-spec, quarterly), a copy of the shared rubric module, and the CONFIG, SPEC and RUBRIC families with a test. To register it: the harness `.ki.toml`, the Records group in skill-functions.ts, a reciprocal off-ramp in the ki-skills description, and then regenerating the catalogue, the root README counts (64 to 65 skills, 53 to 54 governance) and two diagrams. The rubric that checks packages themselves is left for later, as KNOWLEDGE-SKILL said.
- Checks for each run, one after another: the tests, tsc, the rubric verify, the ki-skills audit and the skill's own audit. 6c also runs the ki-repo-harness and ki-diagrams audits. The pre-commit hook is never bypassed.
- Running in parallel: the three runs write disjoint sets of files, and only 6c changes the catalogue. 6b and 6c can start as soon as SPEC-TEXT is accepted. 6a waits for ki.ways-of-working's ENTRY-NAMES harness run, because that run edits the same files. In the shared working tree, each run commits only its own paths, waits for the index lock rather than removing it, and treats a whole-tree check that fails only on another run's files as a reason to wait, not to fix.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- ki-work-package's copy of the shared rubric module is older than the provider. SPEC-1 does not need it updated, so 6a leaves it alone.
- `design/specs/specs.md` and `design/spec-areas.md` graduate at the mark after 6c. Before spec-areas.md is deleted, its inventory of retired material should go into the step 9 handoff.
- The D1 and D2 Agent Skills reference drift from the live check belongs to the ki-skills REFRESH, not to step 6.
- An off-ramp in ki-repo-kb is needed only if the COLL-2 read in 6c finds the descriptions collide.

## Queries

### HOMING-EDITS - accept the four homing edits as part of the spec text

**Context:** SPEC-TEXT is your approval of the three texts. Homing them into the harness needs four mechanical edits:
1. a version 1 Status line;
2. the attribution kept as it is;
3. links between the specifications made into plain names, because a relative link across skills breaks the harness link rule and naming house skills would make the specs house-specific;
4. a Contents list.

Any other wording change would come back to you.

**Query:** Do you accept these four edits as part of approving SPEC-TEXT, so the homed files count as your approved text?

**Options:**
a) (recommended, confidence high - each edit is mechanical and changes no rule) Accept them with SPEC-TEXT; each run applies only these four.
b) Approve each homed file again after its run.

### CATALOGUE-WRITE - one write-mode catalogue regeneration in 6c

**Context:** Adding a skill means regenerating the harness catalogue, the root README counts and two diagram files, which are checked as must-haves. The tool that writes them is `ki repo conform --skill ki-repo-harness` in write mode. HOOK-GUARD still applies in ki.ways-of-working's state, and every brief bans conform without `--dry-run`. mac-studio-setup's log calls HOOK-GUARD superseded but keeps the caution.

**Query:** May the 6c run's brief allow exactly one write-mode `ki repo conform --skill ki-repo-harness` in the harness, with every other conform staying dry-run?

**Options:**
a) (recommended, confidence medium - the generator is the only route the harness supports, but the HOOK-GUARD status is not settled in one place) Allow that one command in 6c's brief, run with `--dry-run` first and its diff checked before writing.
b) Keep the ban: 6c writes the generated sections by hand and the ki-repo-harness audit verifies them.

### HOMING-REVIEW - harness records and review for step 6

**Context:** The plan gates step 6 on "a harness record under ki-next, Steward review". The harness's last record is KI-HARNESS-GOV-227. The Paperclip Steward flow applies to Paperclip deliveries, and these are coordinator runs.

**Query:** How should step 6 be recorded and reviewed?

**Options:**
a) (recommended, confidence medium - it keeps the harness's record trail without waiting on Paperclip) One small run captures three harness records, one for each of 6a, 6b and 6c, before they start; each homing run then gets one blind Codex review in place of the Steward before you accept it.
b) Send all three through the Paperclip Steward and Convenor flow.

### 🤖 → 👤 Handoff to supervisor · since 01:09 BST

👤 3 with you

- [with you] HOMING-EDITS · owner · since 01:09 BST
- [with you] CATALOGUE-WRITE · owner · since 01:09 BST
- [with you] HOMING-REVIEW · owner · since 01:09 BST
- [uncommitted] design/home-plan.md
