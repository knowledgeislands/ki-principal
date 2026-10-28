# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-skillset

**🤖 → 👤 Handoff to supervisor · Run report at 01:54 GMT · last mark 01:07 GMT**

---

## Done

- Wrote the skill-set model, [skill-set](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/skill-set.md>), committed in ki-principal as `25f7a99f` by explicit path, nothing else staged; pull fast-forward and push succeeded and the checkout is level with its remote.
- Units: all fourteen skills set out with job, boundary and hand-offs, in five layers (activation, definition of work, record life cycle, running and coordinating, continuity), plus the surfaces that are not skills (`ki agent`, `ki work status`, the hook, the output style, chezmoi, Rig, the Observatory, the Work Process note).
- Session kinds: conversational, coordination thread and State of play thread, with background runs as the fourth actor, the skills each uses, its reply form and what it commits.
- Kris's question answered: every Project package can have its own coordination thread, one at a time and only while active; dormant packages are stewarded by State of play or a secondary under CASCADE-STEWARD; regular and ad hoc packages never get one. The limits are the cap of three or four active packages and Kris's attention, not the skills.
- Bootstrap path: a six-outcome test for "works really well", then the fresh-machine steps and the fresh-session steps; the gap is that no skill owns the path between `ki-bootstrap` and the opener.
- Findings: nine contradictions (push rule, commit rule, hosts, one session per work, report homing, the turn's single package, pull mode, numbered decisions, in-session worker lanes), ten gaps and five overlaps, each with a recommended fix and owner. Most fixes are already authorised by logged decisions and fold into the planned harness run for coordination, work-package and delegation.
- Unattended window traced end to end in nine steps, each with its owning skill; it needs one section in `ki-coordination`, not a new skill, state or file.
- Check: the note has no em or en dashes, and every relative link resolves.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- The three queries below have not had their blind review; the coordinator should send each to one before they reach Kris.
- Of tonight's decisions, only REBOOT-SHAPE and GAP-SUMMARY have landed in the harness (`8cc42754`); COMMIT-CADENCE, PACKAGE-PUSH and the rest await the harness run already planned.

## Queries

### BOOT-HOME - Who owns the bootstrap from a fresh machine to a working coordinator

**Context:** `ki-bootstrap` covers the harness and skill activation and then stops; `ki-coordination` starts at the opener. Between them, chezmoi's hook and style binding, the Capital's declarations, `ki skill add ki-work-design`, the readiness checks and `ki agent prompts` with `claude --name` are written nowhere as one path, so a fresh machine can fail silently at the hook or the style. Kris's goal is that "when we do a bootstrap ... it works really well".

**Query:** Which skill holds the one bootstrap checklist?

**Options:**

a) (recommended, confidence medium - one owner per half keeps each skill's boundary; not yet reviewed) `ki-bootstrap` owns the machine half and ends with a "Ready to coordinate" check, later backed by a `ki doctor` item in `tools-ki`; `ki-coordination`'s Bootstrap gains a "Before the opener" step that cites it, and owns the session half as now

b) `ki-coordination` owns the whole path, machine half included, and `ki-bootstrap` links to it

c) a guide in ki-principal under `Pillars/` owns the narrative, and both skills link to it

### TRADES-FATE - What becomes of ki-trades now its hold is overdue

**Context:** `ki-trades` is on hold with a review due by 21 October 2026, now four days past, and its `HOLD-1` audit item warns. Existing trades keep full support. HANDOFF-AS-MESSAGE moved handoffs and rollouts to `messages.md`, so it now governs only the trade routes `.ki.toml` declares. The planned Trades revamp Project's outcome, a succinct trade policy granting the same as now, is that narrower job.

**Query:** Should `ki-trades` be narrowed now or kept on hold?

**Options:**

a) (recommended, confidence medium - matches what HANDOFF-AS-MESSAGE already decided and costs one bounded edit; not yet reviewed) narrow it to declared routes only, with a pointer to `messages.md` for everything else, and set its next review to when the Trades revamp opens

b) keep it on hold with a new review date, untouched until the Trades revamp opens

### RECAP-NAME - What ki-recap's checkpoint argument is called

**Context:** `ki-recap` offers `checkpoint <thread>`, which composes `ki-work-package` UPDATE. "Thread" now means a session acting on work, and the argument is really a work id. The three recap forms (one session, one work since its mark, the unattended window's return) otherwise have clean scopes.

**Query:** Should the argument become `checkpoint <work id>`?

**Options:**

a) (recommended, confidence high - the model made work the unit and the argument already resolves an id; not yet reviewed) rename it to `checkpoint <work id>`, accepting the old word through the tolerance window

b) keep `checkpoint <thread>` and define it in the Glossary as the work the thread carries

### 🤖 → 👤 Handoff to supervisor · since 01:54 GMT

👤 3 with you

- [with you] BOOT-HOME · owner · since 01:54
- [with you] TRADES-FATE · owner · since 01:54
- [with you] RECAP-NAME · owner · since 01:54
- [committed] work folder

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
