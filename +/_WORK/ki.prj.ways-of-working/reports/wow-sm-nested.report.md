# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-sm-nested

**🤖 → 👤 Handoff to supervisor · Run report at 21:55 GMT · last mark 16:18 GMT**

---

## Done

- I redrew the [work state machine](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/work-state-machine.md) to Kris's nested shape (c44960e3), with its [SVG](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/work-state-machine.svg) and [interactive view](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/work-state-machine.html). A composite Work state holds the cycle: inform, receive, direct, receive. Bootstrap enters Work by pick up or report. Stop takes the work to At rest, which carries a reason (holding, waiting or moving). At rest leaves by finish or resume. The Archify checks passed, and I looked at a rendered image of the drawing.
- I rewrote the States and Transitions tables. Each transition keeps its preconditions, the work on the arc and its postconditions, and stop carries drain and the eight portability checks. The note maps the old names to the new and keeps the folder layout section. It also adds a short table of At rest reasons, saying what releases each one.
- I replaced the Decisions for Kris with five open queries. The note says which of the first draft's queries this shape settles: BOOT-RECEIVE, TARGET-RUN, TARGET-SILENT, HOST-MOVE-PATH and ARC-NAMES. It says which carry over unchanged: BOOT-RECORD, REPORTS-NAME and FOLDER-MIGRATE.
- I committed WORK-CYCLE-SHAPE in [the decisions log](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/decisions.md) with the design. The pull could not fast-forward because another session had added entries to the same log. Both sides only added entries, so I kept both in merge 174ece26 and published it. One gap: the merge commit used Git's default message, which has no co-author trailer. It cannot be amended now without a force-push.

## In Progress

Nothing is running.

Outstanding - no action requested now: the briefs for this run and for wow-sync-2 are still untracked in `briefs/`. They belong to the coordinator, so I left them alone.

## Queries

### REST-PORTABLE - Whether every At rest reason needs full portability

**Context:** Under TRANSITION-CONDITIONS, Kris made portability the postcondition of going to rest: deleting the checkout loses nothing. A waiting rest may be short, for example waiting an hour for a reply from other work on the same host. Full portability would then mean stopping long runs, parking every query and striking the mark each time.

**Query:** Does stop need the full portability checks for every reason, or only a lighter check for waiting?

**Options:**

a) (recommended, confidence medium - one postcondition keeps At rest a single state with a single guarantee) Every reason needs full portability. A short wait stays inside Work, With worker, with the wait shown in the banner.

b) Waiting needs only everything committed and pushed. Holding and moving need the full checks.

### WAIT-RESUME - How a waiting rest resumes when the response arrives

**Context:** Nobody holds the move while the work is At rest. When the target's reply lands in this work's `messages.md`, nothing notices it unless a session is opened. Territory work already sweeps inboxes at its mark, and timeout takeovers are not allowed.

**Query:** When the response arrives, what moves the work from waiting to Bootstrap?

**Options:**

a) (recommended, confidence medium - only Kris or an opener resumes work, and no new wake mechanism is needed) The reply line is the release. Territory work flags it at its next mark, and Kris resumes the work with an opener.

b) The reply line resumes the work automatically: the session that replies, or a headless pass, opens a Bootstrap.

### FINISH-FROM - Whether finish is only from At rest

**Context:** Kris's shape draws finish only from At rest. Today Kris can also finish from With supervisor, and the first draft allowed that too.

**Query:** Is finish allowed only from At rest?

**Options:**

a) (recommended, confidence high - it follows Kris's drawing, and close-out already needs everything the stop postcondition proves) Only from At rest. Finishing from Work means a stop and then a finish, in one turn when the checks pass.

b) Also allow finish directly from With supervisor, with the portability checks as its preconditions.

### WORK-REENTRY - How a fresh session re-enters live work

**Context:** In Kris's shape, only resume from At rest leads into Bootstrap. A compaction, a model switch, a lost host or a new session can also hit work that is still in Work, and each needs a bootstrap read. The first draft drew a re-bootstrap arc from every live state.

**Query:** How is a re-bootstrap of live work modelled?

**Options:**

a) (recommended, confidence medium - a re-read changes no state, and the drawing stays as Kris set it) As a re-entry inside Work, with no arc drawn. The session reads the package as Bootstrap does and the recorded state stays the same.

b) As a drawn re-bootstrap arc from Work to Bootstrap.

### REST-NAMES - Whether to keep the working names

**Context:** Kris said "some of these names could be refined". The shape uses inform, direct, stop, At rest, holding, waiting and moving. Today's commit subjects and banners still say send, hold, On hold and Handoff to target.

**Query:** Do we adopt the names as drawn and rename commit subjects and banners to match?

**Options:**

a) (recommended, confidence medium - they are Kris's own words and read plainly, and the other words in the note were settled the same way) Adopt them as drawn and prove them in use.

b) Refine some names first, naming which ones.
