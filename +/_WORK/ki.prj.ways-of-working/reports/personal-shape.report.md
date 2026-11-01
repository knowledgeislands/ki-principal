# [Model](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › personal-shape

**🤖 → 👤 Handoff to supervisor · Run report at 12:31 GMT · last mark 01:41 GMT**

---

## Done

- Drafted the PERSONAL-SHAPE model, read-only, as five findings below: the units, authority, the per-host split, migration and what would break. Kris's words are in [ki.prj.ways-of-working decisions](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/decisions.md) (1 November, 12:21 GMT).
- Sources read: `ki-coordination` (levels, work naming, thread capabilities, assigned packages, secondary States of play, messages between work), `ki-work-package` (location and identity, entry points, messages lines, prohibited payloads), `ki-work`'s Project registry standard, `ki-delegation`; the KI [Charter](/Users/krisbrown/kis/knowledge-islands/ki-principal/Admin/Governance/Charter.md), [Known Lands](</Users/krisbrown/kis/knowledge-islands/ki-principal/Admin/Governance/Known Lands.md>), [Techne Programme Focus](</Users/krisbrown/kis/knowledge-islands/ki-principal/Admin/Governance/Policies/Techne Programme Focus.md>) and root `AGENTS.md`; Personal's `AGENTS.md`, [Charter](/Users/krisbrown/kis/personal/personal-principal/Admin/Governance/Charter.md), `.ki.toml` members and every package in its `+/_WORK/`; Acquire's `AGENTS.md` and [personal.reg.acquire-intake](/Users/krisbrown/kis/personal/acquire/+/_WORK/personal.reg.acquire-intake/work.md); and the definition and state of all 16 packages in ki-principal's `+/_WORK/`.
- Nothing changed and nothing committed; no checks were needed beyond reads. `ki agent prompts personal` warns that `kb.regular.site-tower/` has no `work.md` and that `personal.reg.email-routing`'s hold reason is invalid; both are Personal's, noted here only.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Every query below except PS-HOST and PS-HOME is at medium confidence, so under the query-review rule it needs one blind review before it reaches Kris. This run could not launch one.
- Brief for the coordinator: nothing should move until Kris answers PS-SHAPE. The other queries only matter if he picks a) or b) there.

## Findings

### PS-UNITS - Proposed units and what happens to each current package

**Goal:** name each work in the proposed shape, with its boundary and hand-offs, and classify every live KI package.

**Scope:** ki-principal's 16 packages, Personal's 10 and Acquire's one. Registered Projects with no package (such as `host-network`) are touched only where they bear on a move.

**As of:** 1 November 2026, 12:30 GMT, read from the working trees.

The governing idea: Knowledge Islands keeps the **products** it owns: the method (skills, standards, the Work Process note), the `ki` CLI, tools-rig, the harnesses, the Observatory and the agent host. Personal takes the **practice**: Kris's machines, his dotfiles, his day-to-day use of agents and Orca, and Acquire as his assistant. Every move below follows from where the repository or product actually lives. Personal's `.ki.toml` already lists `krisb/dotfiles` and `krisb/acquire` as Personal members, so chezmoi and Acquire are already Personal's repositories.

Proposed units:

| Work | Level | Home | Host | Owns | Boundary and hand-offs |
| --- | --- | --- | --- | --- | --- |
| `personal.sop.main` | territory | personal-principal | none | Personal's front door; `covers` gains the new and moved works | The Personal end of every cross-territory route (PS-ROUTE) |
| `personal.reg.ways-of-working` (new; title `Personal > Ways of working`) | regular (ad hoc) | personal-principal (PS-HOME) | None in the id. Runs carry `@terra` or `@sol` (PS-HOST) | How Kris actually works with agents on his Macs: thread practice, listening and host sync in daily use, Orca in daily use, the loop from Acquire's `actions/` to work, and trying method changes before KI adopts them | Out: the method product → `ki.prj.ways-of-working`; machine upkeep → rig-terra and rig-sol; intake → acquire-intake. Sends lessons and method needs as METHOD lines to KI |
| [`personal.reg.acquire-intake`](/Users/krisbrown/kis/personal/acquire/+/_WORK/personal.reg.acquire-intake/work.md) | regular | acquire (existing member home) | Either Mac, through host-bound runs | Unchanged | Its Out line still names the finished `ki.prj.knowledge-acquisition`; repoint it to `ki.prj.ways-of-working` for the `ki-acquire` method |
| [`personal.reg.rig-terra`](/Users/krisbrown/kis/personal/personal-principal/+/_WORK/personal.reg.rig-terra/work.md), [`personal.reg.rig-sol`](/Users/krisbrown/kis/personal/personal-principal/+/_WORK/personal.reg.rig-sol/work.md) | regular | personal-principal | Host-limited; each is its Mac's host sync thread | Unchanged; rig-sol also takes over Mac Studio setup's machine-side work (PS-STUDIO) | Tooling needs go to KI's tools-rig owner |
| [`personal.reg.rig`](/Users/krisbrown/kis/personal/personal-principal/+/_WORK/personal.reg.rig/work.md) | regular | personal-principal | none | Unchanged | - |
| `personal.prj.chezmoi` (moved) | project | personal-principal; theme `rig`, which Personal already has | none | The PERSONAL-DOTFILES-UE records in the dotfiles repository, reviewed applies, coverage and drift | Rig tooling → KI `tools-burndown`; `ki`/mgit → KI `tools-burndown`; the scheduled-runner design kept in step with `ki.prj.observatory` through PS-ROUTE |
| `personal.prj.orca-evaluation` (moved) | project | personal-principal; theme `rig`, or a new theme | none | Orca trials, how Kris uses Orca, upstream reports to Orca | Orca's place in the method (launcher, adapter, ORCA-ROUTING) stays with `ki.prj.ways-of-working` |
| `ki.sop.main` | territory | ki-principal | none | Unchanged; `covers` drops the moved works; method stewardship under STEWARD-HOME | The KI end of every cross-territory route |
| `ki.prj.ways-of-working` (trimmed) | project | ki-principal | none | The method product only: the Work Process note, `ki-coordination`, `ki-delegation`, `ki-work-package`, the output style, work-record fields and `ki-acquire` | Receives METHOD lines from Personal. Finishes into State of play stewardship when its own goal says so |
| `ki.prj.observatory` | project | ki-principal | none | Unchanged | - |
| `ki.prj.tools-burndown` | project | ki-principal | none | Unchanged, and takes the tools-rig lane: its records, their order and releases | Takes that lane from Mac Studio setup |
| `ki.prj.agent-host` | project | ki-principal | none | Unchanged; it also takes any item about sol as a Techné agent host under the Techne Programme Focus | - |

Classification of every current KI package:

| Package | Verdict | Reason |
| --- | --- | --- |
| [ki.prj.ways-of-working](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/work.md) | Stay, trimmed | Its scope is KI's method product, delivered in ki-agentic-harness (82 method commits since 20 October) and ki-principal's Pillars. It holds about 76 open queries, a 1,168-line decisions log, about 60 unpruned reports and 45 design notes, some of them cited by harness skills. Only the practice side moves, as new work |
| [ki.prj.mac-studio-setup](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.mac-studio-setup/work.md) | Close, split | Machine-side work → rig-sol, which already overlaps it. The tools-rig lane → tools-burndown, because tools-rig is KI's. Orca has already gone to orca-evaluation. Moving it whole would leave KI records run from Personal |
| [ki.prj.orca-evaluation](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.orca-evaluation/work.md) | Move | Kris's use of a tool on his own Macs. Small package (5 queries, 22-line log), two days old; SCOPE-SPLIT already separates out the method part |
| [ki.prj.chezmoi](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.chezmoi/work.md) | Move | Its records live in `krisb/dotfiles`, a Personal member, so a KI Project already runs another territory's repository |
| [ki.prj.tools-burndown](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.tools-burndown/work.md) | Stay | KI's CLI products; gains tools-rig |
| [ki.prj.agent-host](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.agent-host/work.md) | Stay | Techne Programme Focus |
| [ki.prj.baseline-rollout](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.baseline-rollout/work.md) | Stay | KI's rollout of its own baseline |
| [ki.prj.portable-specifications](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.portable-specifications/work.md) | Stay | KI product (the specifications) |
| [ki.prj.knowledge-acquisition](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.knowledge-acquisition/work.md) | Close | Already Finished; its folder deletion is due at its closing mark (QUICK-FIXES-FOLDER) |
| [ki.prj.estate-factorisation](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.estate-factorisation/work.md) | Close | Through the retirement plan already waiting on ESTATE-CLOSE |
| [ki.prj.paperclip-capture-and-rebuild](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.paperclip-capture-and-rebuild/work.md) | Stay, on hold | A Techné idea under the Focus |
| [ki.prj.timelines](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.timelines/work.md) | Stay | Harness skill (`ki-calendars`) |
| [ki.prj.website](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.website/work.md) | Stay | KI website |
| [ki.prj.observatory](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.observatory/work.md) | Stay | Named by Kris as durable |
| [ki.reg.main](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.reg.main/work.md), [ki.sop.main](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.sop.main/work.md) | Stay | Durable territory works |

### PS-AUTHORITY - How Personal-homed work would change KI-owned products

**Goal:** say how a Personal work gets a change into a KI product, and what that costs in speed.

**Scope:** the KI Charter, the `ki-coordination` Messages-between-work rule, and current practice.

**As of:** 1 November 2026.

- **Today:** Ways of working is a KI Project, so its runs commit straight into ki-agentic-harness and ki-principal under Kris's decisions. tools-ki changes go as lines to tools-burndown, the only tools-ki writer (OWNER-LANE).
- **The rules once work moves:** the Charter says territory gives no cross-repository write authority and that "no route grants peer write, scheduling, implementation, publication". The Sender rule in `ki-coordination` allows a message line only from coordinating work in the same Capital; territory work "alone writes to another Capital, through that Capital's territory work". Strictly read, a Personal work reaches a KI work in two hops: Personal's State of play, then KI's.
- **Practice already bends this:** personal.reg.rig-terra wrote DESKTOP-RESET and BACKUPS-DELETE straight into ki.prj.chezmoi's `messages.md` (see the `move-procedure-add` report). personal.reg.acquire-intake sent ACQUIRE-STRUCTURE-ALIGN straight into Ways of working's queue "at Kris's word".
- **Mechanisms:**
  - **Two hops through both States of play.** No new authority is needed. Neither State of play listens today, so each line waits for two coordinator pick-ups: hours to days, with three sessions reading every line.
  - **A standing direct message route.** Recorded as Kris's decision in both States of play's logs and later as a KI trade route once trades reopen. A named Personal work may add one line to a named KI work's queue, and the reverse. The KI receiver still owns priority, plan, delivery and acceptance, so no write authority moves. It costs one harness edit to the Sender rule, made by `ki.prj.ways-of-working`. Speed is close to today's if the KI receiver listens; otherwise one pick-up.
  - **A write grant letting Personal runs commit into KI repositories.** This conflicts with the Charter's "no peer write", so it is not offered as a recommendation.
- **Speed cost of the split, whichever route:** trying a method change becomes two works. Personal tries it and sends a line; KI changes the skill and sends a REFRESH back. That adds one hand-off and one coordinator turn per change compared with today's single thread. The design lab stops being the editor, which is the price of keeping KI's products owned in KI.

### PS-HOSTS - One Personal work with host-bound runs, or w-terra and w-sol

**Goal:** settle whether per-host Ways of working means separate works or one work run on each Mac.

**Scope:** the naming rule, the label rule, `@host` message lines, the host-seat prohibition and the Rig threads' pattern.

**As of:** 1 November 2026.

- The naming rule says a work id segment "never holds ... a host", and an ad hoc slug "never carries a date or host". The label alone carries `(<host>)`, and only "if its limited to that machine". `w-terra` and `w-sol` as ids would break this.
- `personal.reg.rig-terra` and `personal.reg.rig-sol` already carry a host in their ids. They predate or tolerate the rule, and are genuinely machine-limited works. They are a precedent, but a non-conforming one.
- The rules already provide the per-host mechanism. A message line may carry `@terra` or `@sol`, which restricts only device-dependent execution. A brief or record may name a required host. A session's host seat never goes into a package. So one work, run from a long-lived session on each Mac, fits the rules with nothing new. Each Mac already has its host sync thread (the Rig threads, which listen).
- The same applies to Acquire on both Macs. `personal.reg.acquire-intake` stays one work: Git carries its package between hosts, the KIV viewer runs locally on whichever Mac is in use, and host-bound actions go as `@host` lines.
- **Constraint to check, not settled here:** the Techne Programme Focus says agents on the Mac Studio run "only in sessions the binding owner opens, with no unattended or scheduled agents". Moving work into Personal does not lift that for sol.

### PS-MIGRATION - Moving a live package across Capitals, and what breaks

**Goal:** give the steps to move a live package, and what would break.

**Scope:** the work-package and coordination standards, the runtime state folders, openers and links.

**As of:** 1 November 2026.

No cross-Capital move procedure exists in `ki-work-package`. Its rules shape one:

- The territory segment changes, so the new id is new work. In effect this is a close in KI and an open in Personal, carrying content across.
- "Two physical definitions for one work are ambiguous", so the two must never both be live.
- A Project package must be Capital-homed, so moved Projects go to personal-principal, never Acquire.

Steps, per package:

1. **Decide and register:** record Kris's decision in both States of play's logs. Register the Project note in personal-principal's `Streams/Projects/`. Check Personal's active-Project cap; tower-public-site is already with a worker.
2. **Drain the source:** nothing running; receive reports; copy their queries into `queries.md`; park queries; strike a mark; commit and push. The source goes On hold.
3. **Seed the destination On hold:** a five-file package in personal-principal with the new id, `parent: personal.sop.main`, title and H1s; current `method_read`. Carry decisions that still govern, each with a pointer to the KI log at a pinned revision. Copy queries whole, re-tagged as `(new id, tag)`. Copy unacted message lines; carry live design notes; home or prune reports first, and point to the rest at a pinned revision.
4. **Retire the source:** delete the KI folder in one commit naming the new home. Drop it from `ki.sop.main` `covers` and add it to `personal.sop.main` `covers`. Give the KI Project note a moved close-out linking the Personal note.
5. **Repoint:** every Out line, next step and message that names the old id, in both territories; records' `project:` fields in the dotfiles repository; Observatory and `ki work status` territory views.
6. **Runtime, per host:** the old run folder `~/.local/state/ki/agents/<old slug>/` keeps its name, as the rename rule says. Session bindings in `~/.local/state/ki/threads/<repository>/<slug>.json` are rebuilt on each host. Orca threads reopen with the new opener from `ki agent prompts personal`, which reflects the move automatically.
7. **Open:** Kris opens the Personal package.

What would break:

- Old openers pasted into Orca or Claude sessions find no package and fail to bootstrap.
- Lines in flight between the moved work and KI works become cross-Capital. One example is the WAKE-SUBSTRATE and MGIT-SYNC-ADOPT queue in chezmoi, which runs with tools-burndown and the Observatory. They need PS-ROUTE in place first.
- Query identities change, so read-backs in other logs point at the old `(work id, tag)`.
- Links into moved design notes from harness skills and other packages break. This is why Ways of working is not moved whole: CITED-NOTES shows harness skills cite its notes.
- Already broken, whatever is decided: 14 KI `work.md` files, and Personal's, still link `/Users/krisbrown/workspaces/...` paths from before the move to `~/kis`. The rig-sol line in chezmoi's state still names `personal.regular.rig-sol`.
- Visibility: personal-principal is private. Moving Kris's machine and assistant detail out of the KI Capital narrows its exposure; nothing moves the other way.

## Queries

### PS-SHAPE - How much of the nascent side to move to Personal

**Context:** Kris asked whether Ways of working, Mac Studio setup and Orca evaluation should leave Knowledge Islands for Personal, beside Acquire and the per-Mac Rig threads, so that KI keeps only its durable work: State of play and the Observatory. The read shows two kinds of work mixed together. One is the practice side: Kris's Macs, his dotfiles, his use of Orca and agents, and Acquire as his assistant. Its repositories (dotfiles, acquire) already belong to Personal. The other is KI's own products: the method skills and standards, the `ki` CLI, tools-rig and the agent host. Ways of working is mostly the second kind. Its runs edit the harness directly, and it holds about 76 open queries and many design notes the harness cites.

**Query:** Should the move cover only the practice side, everything including Ways of working, or nothing?

**Options:**

a) (recommended, confidence medium - it follows where each repository and product already lives; not yet blind-reviewed) Move only the practice side. Orca evaluation and chezmoi move. Mac Studio setup splits between rig-sol and tools-burndown. A new Personal ways-of-working work takes Kris's daily practice. KI keeps a trimmed Ways of working for the method product until it finishes into State of play.

b) Move everything, Ways of working included, and route every method change back to KI owners by message. This is the slowest method loop and the biggest migration.

c) Keep things as they are and only repoint the stale links.

### PS-ROUTE - How Personal work asks KI work for changes

**Context:** Once work sits in Personal, it cannot edit KI repositories; the Charter gives no peer write. Under the current message rule, only a territory's State of play may write to another territory, so a Personal work's request would pass through both States of play, neither of which listens today. In practice two Personal works have already written straight into KI queues: rig-terra into chezmoi, and acquire-intake into Ways of working at Kris's word.

**Query:** Which route should carry requests between named Personal works and named KI works?

**Options:**

a) (recommended, confidence medium - it keeps every KI product decision with its KI owner and keeps today's speed; not yet blind-reviewed) A standing direct route: Kris records which Personal works may add one line to which KI works' queues, and the reverse. KI's Ways of working amends the Sender rule to allow it, and it becomes a KI trade route once trades reopen.

b) Strict two hops through both States of play, with no rule change: the slowest option, with three sessions reading every line.

c) A recorded write grant for Personal runs in KI repositories. This conflicts with the Charter.

### PS-HOST - One Personal ways-of-working work or one per Mac

**Context:** Kris floated "w-terra" and "w-sol". The naming rule says a work id never carries a host; only a label may carry `(terra)`, and only when the work is limited to that machine. A message line can already be bound to a Mac with `@terra` or `@sol`, and each Mac already has a long-lived Rig thread that listens and syncs. rig-terra and rig-sol do carry hosts in their ids, a precedent that does not conform.

**Query:** Should per-Mac working be one work run on each Mac, or two works?

**Options:**

a) (recommended, confidence high - it meets the naming rule and uses the existing host-binding mechanism with nothing new) One work, `personal.reg.ways-of-working`, with per-Mac jobs sent as `@terra` or `@sol` lines and a long-lived session on each Mac. Acquire is treated the same way on both Macs.

b) Two works, `w-terra` and `w-sol`, following the Rig threads. This needs an exception to the naming rule.

c) No new work: the per-Mac practice goes into rig-terra and rig-sol themselves.

### PS-HOME - Where the new Personal ways-of-working work lives

**Context:** Kris links this work closely to Acquire. Regular work may live in a member repository if Kris approves. But Acquire's `AGENTS.md` says: "Do not create another work identity" there. Projects must live in the Capital, personal-principal.

**Query:** Should the new work live in personal-principal or in Acquire?

**Options:**

a) (recommended, confidence high - Acquire's own instructions forbid a second work identity there) personal-principal, with Acquire's actions reaching it as message lines from acquire-intake.

b) Acquire, beside acquire-intake. This needs Acquire's `AGENTS.md` changed first.

### PS-STUDIO - What happens to Mac Studio setup

**Context:** [ki.prj.mac-studio-setup](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.mac-studio-setup/work.md) mixes three things:

- sol's machine work, which [personal.reg.rig-sol](/Users/krisbrown/kis/personal/personal-principal/+/_WORK/personal.reg.rig-sol/work.md) already largely does.
- The tools-rig lane: KI-TOOL-RIG records and their order. tools-rig is a KI product.
- Orca trials, already handed to orca-evaluation.

**Query:** Should Mac Studio setup close and split, move whole, or stay?

**Options:**

a) (recommended, confidence medium - each part goes to the owner of its repository; not yet blind-reviewed) Close it in KI. sol's machine work goes to rig-sol, the tools-rig lane to tools-burndown, and any Techné agent-host item to agent-host.

b) Move it whole to Personal as `personal.prj.mac-studio-setup`, running tools-rig records across the route.

c) Keep it in KI.

### PS-CHEZMOI - Whether chezmoi moves

**Context:** [ki.prj.chezmoi](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.chezmoi/work.md) works the PERSONAL-DOTFILES-UE records in `krisb/dotfiles`, which Personal's `.ki.toml` lists as a Personal member. Personal already has a `rig` theme. Its queue includes a scheduled-runner design shared with the Observatory and tools-burndown.

**Query:** Should chezmoi become a Personal Project, fold into Personal's regular Rig work, or stay?

**Options:**

a) (recommended, confidence medium - its records already live in a Personal repository; not yet blind-reviewed) Move it as `personal.prj.chezmoi` under the `rig` theme, after the route in PS-ROUTE exists for its shared queue.

b) Fold it into `personal.reg.rig` as regular upkeep.

c) Keep it in KI.

### PS-ORCA - Whether Orca evaluation moves

**Context:** [ki.prj.orca-evaluation](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.orca-evaluation/work.md) is two days old and small, and its SCOPE-SPLIT query, with Kris, already hands its method questions to Ways of working. What remains is how Kris uses Orca on his Macs.

**Query:** Should Orca evaluation become a Personal Project?

**Options:**

a) (recommended, confidence medium - what remains after SCOPE-SPLIT is Kris's own tool use; not yet blind-reviewed) Move it as `personal.prj.orca-evaluation` once SCOPE-SPLIT is answered, and use it as the pilot move.

b) Fold it into the new Personal ways-of-working work.

c) Keep it in KI.

### PS-ORDER - Order of the moves

**Context:** The standards have no procedure for moving a package between Capitals, and a careless move can leave one work live in two places. Orca evaluation is the smallest package; Ways of working is the largest.

**Query:** Should the moves go one at a time, starting with a pilot?

**Options:**

a) (recommended, confidence medium - a pilot turns the steps into a written procedure before larger packages move; not yet blind-reviewed) First put the route in place. Then pilot with Orca evaluation and have KI's Ways of working write the move procedure into `ki-work-package` from it. Then move chezmoi, then split Mac Studio setup, and trim Ways of working last.

b) Move everything in one drained window.

### 🤖 → 👤 Handoff to supervisor · since 12:31 GMT

👤 8 with you

- [with you] PS-SHAPE · owner · since 12:31
- [with you] PS-ROUTE · owner · since 12:31
- [with you] PS-HOST · owner · since 12:31
- [with you] PS-HOME · owner · since 12:31
- [with you] PS-STUDIO · owner · since 12:31
- [with you] PS-CHEZMOI · owner · since 12:31
- [with you] PS-ORCA · owner · since 12:31
- [with you] PS-ORDER · owner · since 12:31

🧵 ki.prj.ways-of-working
