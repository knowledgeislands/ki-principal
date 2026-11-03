# [Knowledge Islands](/Users/krisbrown/kis/knowledge-islands/ki-principal/Admin/Governance/Charter.md) › State of play › how-we-work

**🤖 → 👤 Handoff to supervisor · Run report at 22:07 GMT · last mark 22:07 GMT**

---

## Done

- Design note written and committed in ki-principal `03a3fbc7`: [how-we-work.design.md](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.sop.main/_emerging/how-we-work.design.md). It folds HOW-WE-WORK, STATUS-FORM 1 to 3, URGENT-HANDOFF, ROUTE-UP, VALUES-UP-FRONT and FOOTER-GLYPHS into one model: values and focus goals up front in `work.md`, a goal-led Status form, a goal-setting pass, the `workers:` register as the source of who is live, urgent work escalating up the `parent` chain to the nearest live leader, three message flags and pointer broadcasts, and the new footer. It quotes and dates what Kris has already decided, lists nine decisions still needed, and ends with a six-step build plan.
- Markdown check on the note: passed. `ki repo audit` on ki-principal: failed, as it did before this run; none of its failures name the note (they are in `ki.sop.main` `state.md`, `messages.md` and other packages). ki-principal has no tests or type check.
- No standard was edited. No reply line was sent to the assistant repository, because the brief asked for none.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Six of the nine queries below are medium confidence. Before they reach Kris, the coordination standard asks for one masked blind review run; that is step 1 of the build plan and is for ki.sop.main to launch.
- `ki-work-design`'s independent-review stage has not run; the note says so and stays a draft until it has.
- HOW-WE-WORK, STATUS-FORM 1 to 3, URGENT-HANDOFF, ROUTE-UP and VALUES-UP-FRONT stay in `messages.md` for ki.sop.main to dispose of against this note.

## Queries

### VALUES-HOME - Where the shared values live

**Context:** Kris wants each package's values stated up front, and suggested that a Knowledge Islands "knowledge process" carry them. The piloted assistant package writes the five values in full in its own `work.md`. Copying them into every package means every package changes when the values do. Knowledge Islands Principal's [Work Process](/Users/krisbrown/kis/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Processes/Work Process/Work Process.md) note already holds the work model; a change there goes through the Enactment Process.

**Query:** Where should the shared values be written?

**Options:**

a) (recommended, confidence medium - one canonical home avoids drift, but Kris named a "knowledge process" note, which may mean a new note rather than the Work Process) Write them once in the Work Process note under an Enactment record, and give each `work.md` an optional one-line `## Values` section linking them and adding any of its own.

b) Write them once in a new Knowledge Process note in Knowledge Islands Principal, linked the same way.

c) Copy the full values line into every package's `work.md`, as the pilot does.

### STATUS-DETAIL - How much detail Status gives on what waits for Kris

**Context:** STATUS-FORM asked for no full queries in Status; HOW-WE-WORK later asked for "what is waiting on Kris in detail under the table". The Summary already gives each query in full with its options.

**Query:** Under the Status table, how much should each waiting item show?

**Options:**

a) (recommended, confidence medium - keeps Status short and leaves the full form to Summary, but "in detail" may mean more) One line per tag: the plain question and the recommended option, with a pointer to the Summary for the rest.

b) Each query in full, Context, Query and Options, as the Summary gives it.

### WHAT-I-HEARD - Which of Kris's words the read-back covers

**Context:** Status ends with "What I heard", a short read-back of Kris's words kept apart from decisions. Status never moves the mark, so it needs its own window.

**Query:** Which of Kris's words should "What I heard" cover?

**Options:**

a) (recommended, confidence medium - the mark is the window every other form already uses, and a cap keeps it short) Kris's words since the mark, newest first, at most five lines, each quoted or closely paraphrased, with no decision restated.

b) Only Kris's words since the last Status or Summary.

### GOAL-SETTING - What the goal-setting mode does

**Context:** HOW-WE-WORK names "a goal-setting mode" and nothing more. Goals and order now live in each Focus item. The interactive pass already asks one question at a time.

**Query:** What should the goal-setting mode be?

**Options:**

a) (recommended, confidence medium - reuses a shape Kris already uses, though Kris may have meant something broader) An owner-invoked pass, "goals" or `/ki-coordination goals`, walking each focus area one at a time to confirm or reword its goal and order, then writing `work.md`, logging Kris's words and closing with a Status.

b) Leave it out of this build and shape it after Status has been in use for a week.

### URGENT-CRITERIA - What counts as urgent

**Context:** Kris said "not everything" is an escalation. Escalation interrupts a leader and, where none is live, lets a sender do another work's unit, so the test matters.

**Query:** Which units may be sent as `URGENT`?

**Options:**

a) (recommended, confidence medium - both come from Kris's own words, the deadline from URGENT-HANDOFF and the rollout from HOW-WE-WORK) Only a unit with a stated deadline, or a process rollout other work must follow; anything else goes as an ordinary or `IMPORTANT` line.

b) Any unit the sender judges urgent, giving its reason in the line.

### LIVENESS - How a worker is judged live

**Context:** Escalation needs to know who is live. The `workers:` register in `state.md` is a pilot, not in the standard; Agora shows presence but is not yet relied on. A register entry can go stale when a session dies without updating it, as the 3 November usage-limit outage showed.

**Query:** What makes a worker count as live for escalation?

**Options:**

a) (recommended, confidence medium - it reuses fields already piloted and guards against stale entries, but the 30-minute bound is a guess) Its register entry says `status: active` and `listening: on`, and its package or Agora shows activity within the last 30 minutes; the register becomes a standard optional `state.md` field.

b) The register entry alone, trusted as written.

c) Agora presence alone, once Agora is relied on.

### MESSAGE-WORDS - How the three words are written

**Context:** The checker accepts one flag, `IMPORTANT`, in the leading slot and one tag; a held-territory run found that `SUPERSEDED <tag>` written as a two-word tag is rejected. A sender may already replace its own line not yet acted on.

**Query:** How should `URGENT`, `ACK` and `SUPERSEDED` be written in a message line?

**Options:**

a) (recommended, confidence high - it reuses the existing flag slot and the existing replace-own-line rule, so the checker changes least) As flags in the leading slot, `URGENT` carrying `by <deadline>` and sorting above `IMPORTANT`, `ACK` written into the sender's queue, and `SUPERSEDED` replacing the sender's own original line, each keeping the original tag.

b) As two-word tags, `ACK <tag>` and `SUPERSEDED <tag>`, with the checker widened to accept them.

### BROADCAST-POINTER - Where a broadcast's detail lives

**Context:** Long `REFRESH` broadcasts trip the 60-word message warning (LIFECYCLE-3) in every package that holds them. Today's REFRESH lines already link the standard at a pinned harness revision.

**Query:** Where should a broadcast's detail go so the line itself stays short?

**Options:**

a) (recommended, confidence high - the pinned standard and its commit message already exist, so nothing new needs keeping) A pointer line: what changed in one clause and a link to the standard section at its pinned revision, the harness commit message carrying the detail.

b) A broadcast note in the sender's work folder, linked from each line, kept until every receiver has taken it.

### FOOTER-SYNC-WORDING - Which wording the sync line uses

**Context:** Already with Kris from the method-intake run; it blocks only the sync line of FOOTER-GLYPHS. FOOTER-GLYPHS (Kris, 2 November 23:40 GMT, "now") writes the host sync line `⇄  syncing for <host>` and `⇏  not syncing for <host>`. household-sol's FOOTER-CONFIRM (3 November) reports that the later NAMES-ROLLOUT message wrote `⇄ syncing <host>`, without "for", and asks which is right.

**Query:** Should the sync line read "syncing for <host>" or "syncing <host>"?

**Options:**

a) (recommended, confidence high - it is Kris's own wording in the request that authorises the change, and keeps today's "syncing for <host>") `⇄  syncing for <host>` and `⇏  not syncing for <host>`.

b) `⇄  syncing <host>` and `⇏  not syncing <host>`.

### 🤖 → 👤 Handoff to supervisor · since 22:07 GMT

👤 9 with you

- [with you] VALUES-HOME, STATUS-DETAIL, WHAT-I-HEARD, GOAL-SETTING, URGENT-CRITERIA, LIVENESS · owner, after blind review · since 22:07
- [with you] MESSAGE-WORDS, BROADCAST-POINTER, FOOTER-SYNC-WORDING · owner · since 22:07

🧵 ki.sop.main
