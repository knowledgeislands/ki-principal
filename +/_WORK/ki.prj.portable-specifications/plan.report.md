# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Specifications](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/specifications.md) › plan

**🤖 → 👤 Handoff to supervisor · Run report at 23:37 BST · last mark 19:00 BST**

---

## Done

- I wrote [design/plan.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.specifications/design/plan.md). It is uncommitted, and I wrote no other file.
- I checked every claim in the five open queries. The checks used local sources only. I compared the Agent Skills claims with the harness's local reference, last refreshed on 26 September. I did not read the live agentskills.io page, because the brief forbade network calls.
- **PROJECT-NAME:** the claims hold. Two points are new:
  - Kris's own words were "start a project under model called specifications".
  - The paused Project's review of KI Specifications is a prerequisite for the final move. That repository still says "next number is `KIS-0001`", which is a retired number, and it still ships the retired Knowledge Package templates and schema.
  - The step "register on the Model theme page" does not exist, because no theme page lists Projects.
- **SPEC-HOME:** the claims hold. The Claude Design session in the website is not visible locally. The website is marked paused, but it had 13 commits today.
- **ENTRY-NAMES:**
  - Wrong: "a case-only rename needs a two-step `git mv` on macOS". A single `git mv` works on this machine.
  - Stale: "the current migration pass". That pass has already run over 33 `work.md` files, and `ki` 0.11.5 now reads the new shape.
  - Not checkable locally, and probably wrong: "Agent Skills keeps every other file lower-case".
- **SPEC-VERSION:** the claims hold, except "`metadata.version`", which is not checkable locally. None of the drafts' validation sections checks the `spec` field.
- **CONFORMANCE-LEVELS:** the claims hold. The graded templates from the retired KIS-0001 are still in ki-specifications.
- **The drafts' Agent Skills claims:** the layout, field and limit claims are confirmed.
  - Wrong: listing "an upper-case entry file" as something reused from Agent Skills. Agent Skills fixes one name, `SKILL.md`, not a rule that entry files are upper case.
  - Probably wrong: "a conforming package is also a valid skill". From memory, the `skills-ref` validator rejects the drafts' extra top-level keys.
- **`work` draft:** it does build in house ways of working:
  - the order and priority rules for the messages queue;
  - the query form, with tags and the recommended option first;
  - how decisions entries are written and later reduced to pointers;
  - the section caps in `state.md`;
  - a routing description tier.

  Those rules belong in the house profile. As drafted, the house work package does not conform either: `id`, `since`, the seven states and possibly the `WORK.md` file name would all have to change.
- **`knowledge` draft:** it passes the description test. It lacks a cue for audience and depth, it does not put `updated` in the first disclosure tier, and it names no owner.
- **`acquire` draft:** it is about acquisition itself. Its required checksums and coverage levels are too heavy for learning how to use a tool. Neither spec owns curation, the step that turns captured material into a knowledge package.
- **Plan steps:**
  - Get the owner answers.
  - 1 live check and 2 Project note, in parallel.
  - 3 revise the drafts, 4 blind review, 5 Kris approves the texts.
  - 6a-6c home the specs in `ki-work-package`, `ki-acquire` and a new knowledge skill, in parallel. Each spec becomes a `references/standards-<name>-spec.md` file.
  - 7 house conformance, only if WORK-PROFILE asks for it.
  - 8 publish at `/specs/` through the website's roadmap, in parallel with 9 the readiness clean-up of KI Specifications.
  - 10 hand the move to KI Specifications, gated on Kris restarting it at v1.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- `design/plan.md` is uncommitted. Commit it at receive.
- Two later queries are named in the plan and will be raised when their steps come: SPEC-TEXT at step 5 and SPEC-PUBLISH at step 8.
- I have not sent the medium-confidence queries below for blind review. That review is due before they reach Kris.
- HOOK-GUARD still applies to every brief.

## Queries

### WORK-PROFILE - Must the house work package conform to the portable `work` spec?

**Context:** The `work` draft requires `name`, `updated`, four states and possibly `WORK.md`. The house package uses `id`, `since`, seven states and `work.md`. Its readers are `ki work status`, the Observatory, `ki agent close` and the rubrics. `specs.md` treats the house as a mapped profile, and also says that "to conform" it must change. ENTRY-NAMES covers only the file name.

**Query:** Should the house package stay a mapped profile of `work`, or be changed to conform to it?

**Options:**

a) (recommended, confidence medium - this leaves the readers and 33 live packages alone, but the case is not reviewed) Keep the house as a mapped profile. The spec stays aligned with Agent Skills. ENTRY-NAMES then decides only the spec's file name, and the house's ways of working move out of the spec into the profile.

b) Make the house conform. ki.ways-of-working runs a second estate-wide rename, with reader changes routed to ki.tools-burndown and ki.observatory.

c) Bend the spec to the house: `id`, `since`, seven states and `work.md`.

### KNOWLEDGE-SKILL - Which skill owns the `knowledge` spec?

**Context:** Under SPEC-HOME a), each spec lives in its owning skill for now. `ki-work-package` and `ki-acquire` can own two of them, but no harness skill covers curated knowledge packages. The existing skills closest to it are `ki-repo-kb` (island structure), `ki-authoring` (writing standards) and `ki-skills` (which holds the Agent Skills reference).

**Query:** Where should the `knowledge` spec be homed?

**Options:**

a) (recommended, confidence medium - this gives a clear owner and mirrors the other two specs, but the case is not reviewed) A new governance skill, for example `ki-knowledge-package`, that owns the spec and later its rubric.

b) `ki-repo-kb`, as a reference alongside the island method.

c) `ki-skills`, next to the Agent Skills reference.

### SPEC-LIVE-READ - One read-only check of agentskills.io

**Context:** Four points rest on memory or on a reference that is three weeks old:

- whether Agent Skills keeps other files lower-case;
- `metadata.version`;
- whether `skills-ref` rejects unknown top-level keys, which decides whether "is also a valid skill" can stand;
- the licence of the spec text, which the drafts copy closely.

**Query:** May the next run read the live specification page, its licence and the `skills-ref` validator source, read-only?

**Options:**

a) (recommended, confidence high - read-only and reversible, and steps 3 and 8 depend on it) Yes, in one run that writes `design/agentskills-check.md`.

b) No. Drop the "valid skill" claims and treat the licence as unknown until publication.

### MOVE-GATE - Where does this Project finish?

**Context:** The move into KI Specifications depends on Kris restarting that repository at its v1 boundary. That decision is outside this Project, and the date is unknown.

**Query:** Should the Project close once the specs are published and the move is handed off, or stay open until KI Specifications accepts them?

**Options:**

a) (recommended, confidence medium - the Project can then finish, and the handoff carries the move, but the case is not reviewed) Finish at publication, with a blocking handoff record in KI Specifications' roadmap.

b) Stay open, on hold after publication, until KI Specifications restarts and accepts the KIPs.

### PROJECT-NAME - correction

**Context:** The review preferred b), a new slug. Two new facts favour a):

- Kris's words were "start a project under model called specifications".
- The paused Project's review of KI Specifications is a prerequisite for this Project's final move. That repository's numbering contradicts itself, and it still ships the retired Knowledge Package templates and schema.

Option c) would have to rewrite links in `website.md`, `trades-revamp.md`, `specification-review.md` and `Projects.md`. The next step, "register on the Model theme page", should be dropped, because theme pages list no Projects.

**Query:** Should the paused Specifications Project be folded into this work?

**Options:**

a) (recommended, confidence medium - Kris's own words and the dependency support it, but the earlier review disagreed) Fold it in. The outcome becomes the three specs plus the readiness of KI Specifications, and the KBEP and KBIP dispositions carry over.

b) Give this work a new slug, and keep the paused Project for later.

c) Rename the paused Project and reuse `specifications`.

### ENTRY-NAMES - correction

**Context:** Three claims in the query's Context need correcting:

- "Two-step `git mv` on macOS" is wrong: a single `git mv` stages the case-only rename here.
- "The current migration pass" is stale: that pass has already run over 33 packages.
- "Agent Skills keeps every other file lower-case" cannot be checked locally, and the live examples may use `REFERENCE.md`.

The real hazard is different. On macOS, a reader still opening `work.md` keeps working by accident and fails only on Linux CI. If WORK-PROFILE a) is chosen, this query covers only the spec's file name.

**Query:** Should the spec's entry files be named `WORK.md`, `KNOWLEDGE.md` and `ACQUIRE.md`, or `work.md`, `knowledge.md` and `acquire.md`?

**Options:**

a) (recommended, confidence medium - this matches the live house name and avoids a second rename, and the review already preferred it) Lower case.

b) Upper case, to mirror `SKILL.md`.

### SPEC-VERSION - correction

**Context:** Every draft adds keys at the top level: `spec`, `updated`, `acquired-with`, `source`, `mutation`, `omissions` and `produces`. Agent Skills' optional fields are a closed list, and its `metadata` field maps strings to strings. If `skills-ref` rejects unknown keys, top-level `spec` breaks validity as a skill. `metadata.spec` would not. The `omissions` list cannot go into `metadata`.

**Query:** Should the spec version stay as an optional top-level `spec` field?

**Options:**

a) (recommended, confidence medium - this is the safe choice until SPEC-LIVE-READ, but the case is not reviewed) Keep `spec` optional, but put it in `metadata.spec` together with the other single-value fields. Decide where lists go after the live check.

b) Keep the top-level `spec`, as the query recommends, and drop the "valid skill" claims.

### 🤖 → 👤 Handoff to supervisor · since 23:37 BST

👤 4 new queries for supervisor · 3 corrections

- [with you] WORK-PROFILE, KNOWLEDGE-SKILL, SPEC-LIVE-READ, MOVE-GATE · supervisor · since 23:37
- [with you] corrections to PROJECT-NAME, ENTRY-NAMES, SPEC-VERSION · supervisor · since 23:37
- [uncommitted] design/plan.md
