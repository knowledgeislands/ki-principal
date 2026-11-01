# [Model](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-cleanup

**🤖 → 👤 Handoff to supervisor · Run report at 01:21 GMT · last mark 01:10 GMT**

---

## Done

All four steps of the [stock-take](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/stocktake-2026-11-01.md) are applied in [ki.prj.ways-of-working](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/work.md), one commit each, under UNLOGGED-QUERIES a, DESIGN-GRADUATION a, BROKEN-LINKS-LIVE a and BROKEN-LINKS-HISTORY a. The commit hook's repository audit passed on every commit.

- **Step 1 (`3716860d`).** Moved the 45 never-committed top-level reports into `reports/` and committed them, together with the untracked `principal-resolve-3` brief. Every later deletion can now be recovered from Git. The 45 are the stock-take's 40 plus five that landed since: `finished-tidy`, `hook-nostash`, `rename-paperclip`, `review-new-queries` and `stocktake`. I did not commit the two Z files in `reports/` (see Z-FILES below).
- **Step 2 (`f8c70a30`).** Added the ten settled-in-practice lines to `decisions.md`, plus one line listing what was copied. Copied 22 unlogged queries into `queries.md` under `## Open`, above `## Answered`, with no other heading changed. Each query below high confidence is marked "from stocktake; blind review needed", and CLOSE-BLOCKED and STREAMS-CHECKER-GAP also carry a note to check whether they have been overtaken. Two were not copied: SWEEP-GATE was already open, and IDEAS-HOME is now carried by IDEAS-REVISIT (1 November, 01:07 GMT). That is why 22 were copied, not 24.
- **Step 3 (`6940d245`).** Recorded the verdicts in `decisions.md` (one line per group, naming each file) and deleted 125 files:
  - 65 reports: 29 marked delete, 9 whose queries step 2 copied in, and 27 older ones in `reports/`.
  - 18 spent briefs: the stock-take's 15 plus `finished-tidy`, `hook-nostash` and `stocktake`, whose reports were received at 01:11 GMT.
  - 21 graduated design notes and 21 superseded ones.

  In 13 surviving files, 19 links to the removed files now point to `f8c70a30`, the last revision that holds them. This includes the AWAY-31-OCT link to `window-31-oct/sync.md` and the `state.md` pointer to the morning summary.
- **Kept in step 3.** I kept five superseded notes, `host-sync-report` and the four in `host-sync/`, because HOST-SYNC-CLOSE is still open and asks about exactly these notes. That is why 21 superseded notes were deleted, not 26. Also kept: the cited graduated notes (CITED-NOTES), the five old proposals (OLD-PROPOSALS), every live note, the reports not yet received or still unproved, and the five briefs the brief protects.
- **Step 4 (`5b18f7ca`).** Repaired broken links in 19 files, in live design notes, `decisions.md` and the surviving historical notes:
  - Links to renamed folders now point to the new names.
  - Links to pruned briefs and reports now point to the revision the text meant: `ef452184`, `d38088a3`, `16b968cc`, `fc1f0303` and `0a9e733f`, plus personal-principal `64cb2f75` for the terra sync brief.
  - Line numbers like `:42` were moved out of the link and into its text.
  - Nine links whose targets cannot be recovered are now labelled "unrecoverable" in the text. One is the `wow-admit-toolski-4` brief in `decisions.md`, linked twice, which was never committed.
  - Kris's quoted words are unchanged.
  - The link check now finds no broken links anywhere in the package except `reports/`.
  - A pull that could not fast-forward, caused by another session's `messages.md` line, was merged in a temporary worktree as `133a1c15`. The worktree has been removed.
- **Not changed, and why:**
  - `mod011-wording.md:36`: the stock-take says this link goes up one level too many, but it sits inside a proposed patch to the Work Process note, where it is correct. The stock-take was wrong here.
  - `capture-model/brief.md:75` and `gfm-migration.md:23`: these are examples inside code blocks, not real links.
  - 157 stale links inside the kept reports: reports are outside both BROKEN-LINKS scopes.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Run blind reviews on the 22 copied queries that are below high confidence, before they reach Kris.
- Receive `rename-paperclip.report.md` and `review-new-queries.report.md`; both are now committed in `reports/` but not yet received.

## Queries

### Z-FILES - Keep the two Z files uncommitted

**Context:** The brief asked for every never-committed report, including those in `reports/`, to be committed first. Only two such files are in `reports/`: `hold-request-20261030-z.md` and `z-session-retirement-20261030.md`, about retiring the Z session. The stock-take said to keep them out of any commit until PUBLIC-REPORT-AUDIENCE and PUBLIC-REPORT-RECOVERY are settled. Both questions were answered "a" on 1 November and are waiting for Kris to name the permitted audience and a private destination. Committing them and pushing would publish them to GitHub. I left them untracked and unchanged, so they are still the only copies.

**Query:** Should the two Z files stay uncommitted until the public-report questions are settled?

**Options:**

a) (recommended, confidence high - pushing them would publish material whose audience Kris has not yet named, and leaving them as they are changes nothing) Keep them uncommitted until PUBLIC-REPORT-AUDIENCE and PUBLIC-REPORT-RECOVERY are settled, then dispose of them as that decision says.

b) Commit them into `reports/` now, so Git keeps a copy, and accept that they become public.

### SWEEP-NOTE-LINKS - Tell two roadmap records where `roadmap-sweep` went

**Context:** Two records outside this package link to `design/roadmap-sweep.md`, which was deleted as superseded: [KI-OBSERVA-BRG-004](/Users/krisbrown/kis/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-004-turn-feedback-sending-on.md) (line 89) and [KI-TOOL-RIG-CORE-070](/Users/krisbrown/kis/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-070-handler-read-back-after-confirmation.md) (line 90). Both links were already broken before the deletion, because they use the old `~/workspaces/.../ki.ways-of-working/` path. The stock-take did not list them, so this run left them alone. The note's last version is in Git at `f8c70a30`. KI-OBSERVA-BRG-004 is also proposed for pruning under DONE-PRUNE.

**Query:** Should the owning works be told the note's pinned link?

**Options:**

a) (recommended, confidence medium - it costs one message line each and lets the owners decide, but the links were already broken and one record may be pruned soon) Send one line to the `messages.md` of the Observatory work and of the work that owns Rig, giving the pinned link `https://github.com/knowledgeislands/ki-principal/blob/f8c70a3000cdd7a531811ffe363884489eda0e50/+/_WORK/ki.prj.ways-of-working/design/roadmap-sweep.md`.

b) Leave them, since both links were already broken and the records are finished.

### 🤖 → 👤 Handoff to supervisor · since 01:21 GMT

👤 2 with you

- [with you] Z-FILES · owner · since 01:21
- [with you] SWEEP-NOTE-LINKS · owner · since 01:21

🧵 ki.prj.ways-of-working
