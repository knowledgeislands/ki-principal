# [Knowledge Islands](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.sop.main/work.md) › State of play › method-intake

**🤖 → 👤 Handoff to supervisor · Run report at 03:24 GMT · last mark 29 Oct 16:17 GMT**

---

## Done

- Read every method request now homed in State of play (its queue history, Ways of working's messages, decisions and 13 parked discussion points, and tools-burndown's queue) and checked each against the current harness (`main` at `1b68359a`), tools-ki (`main` at `76fcdc48`) and chezmoi sources. Read-only: no repository edited, no commit.
- Found the real cause of the 3 November autostash: `pull.autostash` is not set anywhere. chezmoi's `dot_gitconfig` sets `pull.rebase = true` and `rebase.autoStash = true` globally (lines 59-62). `git pull` reads `rebase.autoStash` and passes it to the fast-forward path too, so even `git pull --ff-only` stashes a dirty tree. chezmoi's own guide (`docs/guides/tools/git.md`) claims `pull.ff = only`, which the file does not set: the guide and the config have drifted apart.
- Found two leftover `autostash` stashes in `/Users/krisbrown/kis/personal/assistant`, not one. Only the older one is the one AUTOSTASH-LEFTOVER checked. The newer one holds another session's uncommitted line. I reported both and dropped neither.
- Collision check: assistant-sol's `conform-knowledge-islands` (KIS-CONFORM) is running its final territory audit and sync check now, with legal, Valle Armonia, Sacred Inquiry and review-personal queued behind it. assistant-terra's conform runs cover HNR, TechMedix and Equal Remedy only. No build below should start in ki-agentic-harness or tools-ki until `conform-knowledge-islands` reports.

## In Progress

Nothing is running.

### Plan of record, request by request

| Request | Owner (repo · skill) | Owner authority | Record | Size | Depends on / conflicts |
| --- | --- | --- | --- | --- | --- |
| FOOTER-GLYPHS | harness · `ki-coordination` (standard, output style `ki-coordinator.md`, rubric `threads.ts`, `banner.test.ts`), `ki-delegation` run-prompt and release/prune rules, `ki-bootstrap` standard, harness spec; ki-principal Work Process note (3 glyph uses) | Kris, 2 Nov 23:40 GMT, "now", relayed by assistant-terra; FOOTER-CONFIRM (household-sol, 3 Nov 00:30 GMT) asks for it again | none (message line) | M | Waits on FOOTER-SYNC-WORDING. Supersedes the `👂`/`🔄`/`🧵` lines from FOOTER-CAPABILITY-STATUS-2. Must land before START-NAME. tools-ki renders no footer glyphs, so it is harness-only. Then a REFRESH line to every live package |
| OPTION-CONFIDENCE | harness · `ki-coordination` query format, output style, run-prompt Report paragraph | parked, high, Kris's own proposal (1 Nov), not yet answered | none | S | Same files as FOOTER-GLYPHS, so fold it into that run if answered |
| AMEND-RACE | harness · `ki-git` (it has no amend rule today) | ACCEPT-BY-CRITERIA a), 31 Oct / 1 Nov: "amend in a shared checkout only inside the serialised write window after confirming `HEAD` is this session's own unpushed commit, otherwise make a new commit" | none | S | Same skill as GIT-REBASE and the never-stash wording, so one `ki-git` run |
| GIT-REBASE | harness · `ki-git`, `ki-delegation` resolve briefs, hold prompt | parked, medium, blind review differs | none | S | Joins the `ki-git` run once decided |
| AUTOSTASH-LEFTOVER plus 3 Nov evidence | chezmoi · `dot_gitconfig` and `docs/guides/tools/git.md` (household-sol and household-terra own chezmoi since PS-CHEZMOI, 1 Nov); assistant stashes · personal.reg.assistant-terra | AUTOSTASH-LEFTOVER a) parked high (drop the old stash after checking it against `314df11`); HOOK-STASH a), 1 Nov: never-stash rule | none | S | A message line to household-sol, not a build here. Stash drops happen only in the assistant's own run. `ki-git` could add a check that flags `rebase.autoStash` |
| SUB-PACKAGE | tools-ki · `src/core/work/identity.ts` `workNames` (returns 4-part ids as-is); harness · `ki-work-package`, `ki-coordination` naming | Kris about 00:00 GMT 2 Nov, piloted by the four pillars | none; KI-HARNESS-GOV-233 and KI-TOOL-KI-CLI-174 (typed naming) are done | S tools-ki + S harness | Pair with FOCUS-SLOT-OWNER and FOCUS-TOP (same `ki-work-package` text) |
| FOCUS-SLOT-OWNER | harness · `ki-work-package` | parked, medium, blind review differs | none | S | Joins the SUB-PACKAGE harness run |
| FOCUS-TOP | harness · `ki-work-package` rubric | parked, high, unanswered | none | S | Same run; household-sol moves its own section |
| LAUNCHER-PATHS with both addenda, plus REPORTS-HOMING (2) | tools-ki · `src/core/agent/thread.ts` (home binding about line 480, `moveReports` in close), `control-store.ts` | Kris via hnr.sop.5ge, 1 Nov: fix it "so we don't have to deal with this every time"; REPORTS-HOMING, Kris 2 Nov about 15:20 GMT | none | L | Partly done: `dc33823a` and `573207b6` refuse a gone repository, and a gone home can be re-recorded in an explicitly named repository. Still to do: rebind by matching origin remote and work folder, renamed work ids, relative homes, and gating close before it moves reports. First tools-ki build |
| RUN-CLOSE | tools-ki · `ki agent close` / `sweep` (`src/commands/agent/index.ts` about 468-503, `sweep.ts`) | Kris about 01:55 GMT 3 Nov, RUN-FOLDERS a | none | M | Same close path as LAUNCHER-PATHS, so chain after it |
| GRANOLA-COUNT | tools-ki · `src/core/acquire/granola/projection.ts:117` (still reads `screenshot_count`) | parked, high, reviewed agree, unanswered | none | M | Independent files, can run alongside LAUNCHER-PATHS. Holds the 28 Oct 5G Emerge screenshots |
| START-NAME | tools-ki · `src/core/work/prompts.ts`, `src/commands/agent/index.ts` | RENAME-NAME, Kris 1 Nov | tools-burndown queue line | S | After FOOTER-GLYPHS, because the name becomes the identity line (`🧵 🔑 <id>`, per THREAD-NAME) |
| WATCH-VERB | tools-ki · new `ki work watch` | INBOX-VERB, Kris 1 Nov | tools-burndown queue line | M | Probably overtaken by Agora's doorbell (AGORA-DOORBELL, 3 Nov), so held for Kris |
| AUDIT-HANG | tools-ki · `ki repo audit` | none needed (fault) | tools-burndown queue line | S-M | `conform-knowledge-islands` will show whether it still hangs. Check its report first |
| ANNOTATED-BOARD-SKILL with addendum | harness · `skills/design/ki-design-system` | Kris's request via assistant-terra, 3 Nov | none | M | Reads `krisb/assistant` `prototype/kiv/board/` (`a985c45`) and `aside/annotated-design-board.md` locally. Independent files |
| E2E-ADOPT, -KIND, -OFFRAMP, -HELPERS | harness · branch `ki-e2e` (`c8272712`, 2 ahead of `main`) | parked; KIND, OFFRAMP and HELPERS high and reviewed; ADOPT medium, review differs | none | S once decided | Branch is from 2 Nov and may need refreshing onto current `main` |
| DRYRUN-SCOPE | tools-ki, tools-rig, tools-techne · each CLI's command table | parked, high, reviewed agree, unanswered | none | L | Rollout comes later. tools-rig sits with the household threads, and tools-techne is limited by the Techne Programme Focus policy |
| Z-FILES-HOME | ki-principal · this territory's Ways of working package | parked, medium | none | S | Waits on Z-FILES (still parked) |

### Recommended order of build runs

Hold every run until assistant-sol's `conform-knowledge-islands` reports. Within each repository, runs go one at a time. The two repositories run in parallel, with about three runs at once.

1. **harness `footer-glyphs`** (M): FOOTER-GLYPHS, with OPTION-CONFIDENCE folded in if answered; ki-principal Work Process note in its own commit under Kris's "now"; REFRESH lines to live packages; reply to assistant-terra and household-sol.
2. **tools-ki `launcher-paths`** (L), in parallel with 1: LAUNCHER-PATHS with both addenda and REPORTS-HOMING (2); reply to hnr.sop.5ge and assistant-terra.
3. **tools-ki `granola-count`** (M), in parallel, if GRANOLA-COUNT a) is taken.
4. **harness `git-guards`** (S), after 1: AMEND-RACE, plus GIT-REBASE once decided, plus a check that warns when `rebase.autoStash` or `pull.autostash` is on.
5. **tools-ki `run-close`** (M), after 2.
6. **harness + tools-ki `sub-package`** (S + S), after 4 and 5: `workNames`, plus `ki-work-package` and `ki-coordination` wording, with FOCUS-SLOT-OWNER and FOCUS-TOP.
7. **tools-ki `start-name`** (S), after 1 and 6.
8. **harness `annotated-board`** (M), any time after 1 in the harness lane.
9. **harness `e2e-land`** (S), once E2E-ADOPT is decided.
10. Later: AUDIT-HANG (after the conform report), DRYRUN-SCOPE rollout (L), WATCH-VERB if still wanted.

Messages, not builds: the AUTOSTASH-FIX chezmoi change goes to personal.reg.household-sol as one line, and the stash disposition goes to personal.reg.assistant-terra.

Outstanding - no action requested now:

- The four tools-burndown lines (WATCH-VERB, START-NAME, AUDIT-HANG, and REPORTS-HOMING routed there 2 Nov) stay in ki.prj.tools-burndown's queue until BURNDOWN-ITEMS is answered.
- Ways of working's 19-item AGENDA and the other parked points (LAYOUT, STANDARDS, ROUTE, TIDY, ORCA, HNR bundles and others) are outside this brief and stay parked in its [discussions](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/discussions.md).
- Whether ACCEPT-BY-CRITERIA (31 Oct) is a standing rule or applied only to that night's 25 queries is not settled in the log. This plan treats it as one pass and so assumes nothing new is accepted under it.

## Queries

### FOOTER-SYNC-WORDING - Which wording the sync line uses

**Context:** Kris's FOOTER-GLYPHS request (2 Nov, 23:40 GMT, "now") gives the host sync line as `⇄  syncing for <host>` and `⇏  not syncing for <host>`. household-sol's FOOTER-CONFIRM (3 Nov) reports that the pillars' later NAMES-ROLLOUT message writes `⇄ syncing <host>`, without "for", and asks which is right. The footers are drifting across the four pillars meanwhile.

**Query:** Should the sync line read "syncing for <host>" or "syncing <host>"?

**Options:**

a) (recommended, confidence high - it is Kris's own wording in the request that authorises the change, and it keeps today's "syncing for <host>") `⇄  syncing for <host>` and `⇏  not syncing for <host>`, as FOOTER-GLYPHS says.

b) `⇄  syncing <host>` and `⇏  not syncing <host>`, as NAMES-ROLLOUT wrote it.

### AUTOSTASH-FIX - Stop Git stashing on every pull

**Context:** The never-stash rule (HOOK-STASH, 1 Nov) says sessions never stash. But chezmoi's global Git settings turn on `pull.rebase` and `rebase.autoStash`, and Git uses the second even for a plain `git pull --ff-only`. So any pull in a checkout with another session's uncommitted edit quietly stashes that edit, which is what happened in the assistant on 3 Nov. Kris's own `git up` shortcut relies on the automatic stash. chezmoi now belongs to the household threads. This has not been through a blind review.

**Query:** Should the global setting go, keeping the automatic stash only inside `git up`?

**Options:**

a) (recommended, confidence medium - it removes the stash from every agent pull and keeps Kris's shortcut, but it changes a personal setting and has not been reviewed) Send household-sol one line: remove `rebase.autoStash`, set `pull.ff = only` as chezmoi's Git guide already claims, have `git up` pass `--autostash` itself, and correct the guide.

b) Remove `rebase.autoStash` and change nothing else, so `git up` refuses when there are uncommitted edits.

c) Leave the settings alone and rely on the `ki-git` rule and checks alone.

### AUTOSTASH-LEFTOVER - What happens to the two assistant stashes

**Context:** The assistant (`/Users/krisbrown/kis/personal/assistant`) now holds two automatic stashes. The older one holds only three lines that are already in commit `314df11`, and the parked recommendation, high confidence, is to drop it after a final check. The newer one, from 3 Nov, holds another session's uncommitted line, which may not be committed anywhere.

**Query:** Should assistant-terra check both stashes, drop the older one, and return the newer one's line to its owner before dropping it?

**Options:**

a) (recommended, confidence high - nothing is dropped until its content is confirmed to be in a commit or back in the working tree) Send assistant-terra one line: a bounded run drops `314df11`'s stash after the check, and restores or commits the newer stash's line with its owning session before dropping that stash.

b) Keep both and let the territory sweep raise them.

### BURNDOWN-ITEMS - Take tools-burndown's three lines into State of play

**Context:** tools-burndown is on hold and still holds WATCH-VERB (a `ki work watch` command Kris decided under INBOX-VERB, 1 Nov), START-NAME (start Claude sessions named after the thread, under RENAME-NAME, 1 Nov) and AUDIT-HANG (the tools-ki audit hanging). REPORTS-HOMING went there on 2 Nov as well. Kris said on 3 Nov "move all of the work to be coordinated through the SOP main". Agora's doorbell, live since 3 Nov, now does what WATCH-VERB was for.

**Query:** Should State of play take these lines from tools-burndown, building START-NAME and REPORTS-HOMING, checking AUDIT-HANG against the conform report, and holding WATCH-VERB?

**Options:**

a) (recommended, confidence medium - Kris's 3 Nov words cover it, but tools-burndown is a separate Project and the transfer needs your permission) Yes. Move the four lines here, fold REPORTS-HOMING into `launcher-paths`, and park WATCH-VERB as overtaken by Agora unless you still want it.

b) Take them but build WATCH-VERB too.

c) Leave them with tools-burndown until it reopens.

### PARKED-HIGH - Take the recommended course on six high-confidence parked points

**Context:** Six method points parked by Ways of working each carry a high-confidence recommendation that no reviewer disputed. OPTION-CONFIDENCE: every option carries its own confidence (your own proposal, 1 Nov). FOCUS-TOP: household-sol moves its Focus section below Scope. GRANOLA-COUNT: check screenshots against Granola's full attachment list, never treating an untyped attachment as a screenshot; this unlocks the 28 Oct 5G Emerge screenshots. E2E-KIND: `ki-e2e` stays a process skill for now. E2E-OFFRAMP: two neighbouring skills point to it. E2E-HELPERS: sites copy the helpers for now. DRYRUN-SCOPE (dry-run by default only for commands that work out their own changes) is also high, but it is a large rollout, so it is left out of this bundle. Each is easily undone.

**Query:** Should these six be taken as answered with their recommended options, as one bundle?

**Options:**

a) (recommended, confidence high - each is high, reviewed or your own words, wording-sized and easily undone) Yes, all six, built in the runs the plan names.

b) Take them one at a time interactively.

### GIT-REBASE - May a run tidy its own commits instead of merging

**Context:** The rules allow a resolve run to rebase its own unpublished commits in its private copy. Since 31 Oct, though, briefs have told runs to merge, which produced nine extra merge commits in ki-principal. On 1 Nov you said rebasing "in some situations absolutely has merit … I prefer not to pollute a tree with mergers … Maybe with everything now happening with work trees, merging is more preferable". The blind review prefers merging, because a rebased branch often still cannot fast-forward once others have pushed.

**Query:** Should runs rebase their own unpublished commits in their private copy, with the shared checkout keeping its ban?

**Options:**

a) (recommended, confidence medium - matches the written rules and your dislike of merge clutter; the blind review disagrees) Rebase only in a run's private copy, keep merges where a rebase cannot settle cleanly, and bring the briefs into line.

b) Merge everywhere, and rewrite the rules to say so.

c) Leave the rules and briefs mismatched.

### E2E-ADOPT - Land the end-to-end testing skill now or after a trial

**Context:** `ki-e2e` sits on harness branch `ki-e2e`, two commits ahead of `main`, with its checks passing. The blind review prefers trying it end to end in one real site first.

**Query:** Should the branch be landed after your review, or only after a site trial?

**Options:**

a) (recommended, confidence medium - its checks pass, but the pinned versions are unverified and the review prefers a trial) Land it after your review, refreshed onto current `main`.

b) Trial it in one site first, then decide.

### FOCUS-SLOT-OWNER - Whose focus area a message line names

**Context:** A message line may carry a `focus:` label. In the pilot a sender labelled a line with its own area. The blind review, at high confidence, says the label should use the receiver's areas, because the line sits in the receiver's queue.

**Query:** Should a message line's focus label name the sender's area or the receiver's?

**Options:**

a) (recommended, confidence medium - matches the pilot and keeps "only the owning thread assigns" true; the blind review disagrees) The sender's area. The receiver assigns its own area when it acts.

b) The receiver's area, written only when echoing the receiver's own assignment.

### Z-FILES-HOME - Where the two uncommitted Z files go

**Context:** Two never-committed files sit in Ways of working's `reports/` folder. Z-FILES, still parked, says to keep them out of every commit. Moving them clears the package's one audit failure.

**Query:** Should a small run move them, uncommitted, into `package-layout/` and remove `reports/`?

**Options:**

a) (recommended, confidence medium - it clears the audit and keeps them uncommitted, but it changes the path Z-FILES names) Yes, with a plain move, updating the path in Z-FILES.

b) Leave them until Z-FILES is answered.

### 🤖 → 👤 Handoff to supervisor · since 03:24 GMT

👤 9 with you

- [with you] FOOTER-SYNC-WORDING · owner · since 03:24
- [with you] AUTOSTASH-FIX · owner · since 03:24
- [with you] AUTOSTASH-LEFTOVER · owner · since 03:24
- [with you] BURNDOWN-ITEMS · owner · since 03:24
- [with you] PARKED-HIGH · owner · since 03:24
- [with you] GIT-REBASE · owner · since 03:24
- [with you] E2E-ADOPT · owner · since 03:24
- [with you] FOCUS-SLOT-OWNER · owner · since 03:24
- [with you] Z-FILES-HOME · owner · since 03:24

🧵 ki.sop.main
