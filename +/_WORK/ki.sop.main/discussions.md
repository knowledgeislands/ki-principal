# ki.sop.main discussions

## Open

### ACCEPT-KI-TOOL-RIG-CORE-070 - Accept the default-handler confirmation wait in Rig

focus: acceptance

**Context:** [KI-TOOL-RIG-CORE-070](/Users/krisbrown/kis/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-070-handler-read-back-after-confirmation.md) has been awaiting review since 27 October (commit `e882998`). It changes how `rig apply` sets a default app for a file type, such as Zed for `.toml`. When macOS asks you to confirm the change, Rig used to check straight away, see the old app and record a failure, so a second run was needed. Now it waits up to 120 seconds when run from a terminal, and not at all when unattended, with an environment variable to override the wait. It reports four outcomes separately: confirmed, unanswered or declined, unattended, and ineffective. The full test suite (648 tests) and the gate passed at delivery. Today's read-only re-check passed the default-applications tests (22 of 22, both new tests included), shellcheck and the assembly check. Not yet done: the record's own attended check, a real `rig apply` that raises the macOS prompt, which only you can do. sol currently has `.toml` opening in VS Code instead of Zed, so a `rig apply` there would raise that prompt. Two concerns remain: a declined prompt looks the same as an unanswered one, and a run piped from a terminal gets no wait unless the variable is set.

**Query:** Do you accept KI-TOOL-RIG-CORE-070 as done?

**Options:**

a) (recommended, confidence high - reviewed: the blind reviewer chose it independently, as one real prompt check meets the record's only outstanding Verify step) Accept it after one attended `rig apply` on sol: accept the macOS prompt for `.toml`, and confirm Rig records Zed as applied on that first run.

b) Accept it now on the test evidence, and treat the attended prompt as observed the next time a handler apply happens.

c) Leave it awaiting review until both terra and sol have shown the prompt behaviour.

### ACCEPT-PERSONAL-DOTFILES-UE-106 - Accept the Tower Assistant move to /Applications

focus: acceptance

**Context:** [PERSONAL-DOTFILES-UE-106](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/PERSONAL-DOTFILES-UE-106-apply-tower-assistant-at-applications.md) moved Tower Assistant 2.1 to `/Applications` on both Macs (commit `9667f9e`). Each Dock now points there, `rig doctor` no longer reports the missing Dock path, and the leftover test preference files on terra are gone: fourteen were removed rather than the planned eleven, with apps-tower's confirmation. The record's Verify asks for exactly two things: no test plists on terra, and no `dock-item-path-missing:tower-assistant` on either Mac. sol meets both today. I re-checked it read-only: the app is only in `/Applications`, there are no test plists, and `rig doctor` has no missing-path finding. terra rests on evidence from 24 October and could not be re-checked from sol. sol's `rig doctor` is still unhealthy for unrelated reasons, all outside this record: Dock order drift, `.toml` opening in VS Code, the Screen Sharing firewall anchor, UTM, and, new since 29 October, eight missing npm tools. The app's own attended checks stay with apps-tower (PERSONAL-TOWER-APP-005 and PERSONAL-TOWER-APP-006).

**Query:** Do you accept PERSONAL-DOTFILES-UE-106 as done?

**Options:**

a) (recommended, confidence high - reviewed: the blind reviewer chose it independently, as the record's narrow Verify is evidenced on both Macs and nothing shows terra has changed) Accept it now, leaving sol's other `rig doctor` findings to sol's health work.

b) Accept it only after a read-only `rig doctor` and test-plist check on terra confirms its half still holds.

c) Leave it awaiting review until apps-tower's attended checks (PERSONAL-TOWER-APP-005 and PERSONAL-TOWER-APP-006) are done.

### ACCEPT-KI-TOOL-MGIT-CLI-032 - accept `mgit chain`

focus: chain

**Context:** [KI-TOOL-MGIT-CLI-032](/Users/krisbrown/kis/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-032-chain-command.md), "Chain Git commands", was delivered on 28 October under MGIT-CHAIN and is Awaiting review: `mgit chain ... --then ...`, stop-at-first-failure per repository, recipes via `git config mgit.chain.<name>` and as top-level `mgit <name>`, docs and spec MGIT-WS-028; 151 of 151 bats tests pass. One pre-existing audit failure (SHELL-HOOK on `.githooks/pre-commit`) is untouched. No release cut.

**Query:** Review and accept it now, after CHAIN-QUIET, CHAIN-START-ENTER and CHAIN-START-FIRST are settled?

**Options:**

a) (recommended, confidence high - ACCEPT-BUNDLE, and the two output questions may change it first) Settle CHAIN-QUIET, CHAIN-START-ENTER and CHAIN-START-FIRST, then review it through `ki-accept`.

b) Leave it awaiting review.

### CHAIN-QUIET - Hide repositories where every step succeeded

focus: chain

**Context:** The brief asked for one block per repository, so the chain output prints every repository, including those where every step succeeded. Ordinary mgit commands show only repositories with output or a failure, then one line counting the quiet ones. Over the whole estate of about 50 repositories, a chain lists every one, which buries the few that stopped. The tally at the end still names each repository that did not complete.

**Query:** Should a chain show only the repositories that stopped or failed to start, plus any that printed something, and count the rest in the tally as ordinary commands do?

**Options:**

a) (recommended, confidence high - reviewed: the blind reviewer chose it independently, as it matches ordinary mgit reporting and makes exceptions easy to find across 50 repositories) Yes, as a small follow-up: hide repositories where every step succeeded with no output, and keep `-v` and `--json` showing everything.

b) Keep the current output, with every repository shown.

### CHAIN-START-ENTER - A checkout that cannot be entered

focus: chain

**Context:** The `mgit chain` tally has three outcomes, "failed to start", "stopped" and completed, and the three counts always add up to the number of repositories. The build and the blind reviewer agree that a repository whose checkout could not be entered has failed to start. This is the agreed half of the former CHAIN-START, split out under the method's rule that a query still below high after review is split into parts.

**Query:** Should a checkout that cannot be entered count as "failed to start"?

**Options:**

a) (recommended, confidence high - reviewed: the build and the blind reviewer agree) Yes, as built.

b) Count it as "stopped" instead.

### CHAIN-START-FIRST - A first step that runs and fails

focus: chain

**Context:** This is the disputed half of the former CHAIN-START. As built, a repository whose first step ran and failed counts as "failed to start", alongside a checkout that could not be entered. "Stopped" is a repository where a later step failed after at least one step completed. The record's Discussion section and the tests follow the build's reading.

**Query:** Should a first step that runs and fails count as "stopped" rather than "failed to start"?

**Options:**

a) (recommended, confidence medium - reviewed, views differ: the blind reviewer chose it at high confidence because a Git step that ran has started and may already have changed things; the build run preferred b)) Yes: count it as "stopped", and change the record's Discussion and the tests to match.

b) Keep it as built: count it as "failed to start", because a failing first step is the common case worth singling out.

### MAIL-ASKS - five mail-engine asks waiting for an owner

focus: aside

**Context:** HNR > Email routing (hnr.email-routing) sent four asks for the mail MCP servers, each decided by Kris on 27 or 28 October: ARCHIVE-ENGINE (an mcp-m365 last-touched clock from `lastModifiedDateTime`, filing from Outlook `Archive` into `_ARCHIVE` by a lasting last-working-folder record, unread-guard gaps and per-folder overdue counts), its ACTION-DONE extension (re-route archived action-folder mail into the matching `_ARCHIVE` mirror, unplaceable items to 000 Unknown), GMAIL-CLOCK (`historyId` and `internalDate` reads, a checkpoint log and a 14-day comparison in mcp-gsuite) and SENT-PASS (a sent-items pass, deleting confirmed meeting responses after 7 days, and per-item forward matches in the aged log, with tests; reply to hnr.email-routing when landed). A fifth, low-priority ask arrived on 31 October under Kris's CORR-GUARD-ASK a): a "reply sent" check in mcp-m365's aged routing, so an aged rule can skip a conversation Kris has not replied to; until it exists HNR keeps correspondence folders 231, 261 and 263 out of the 14-day archive, and it wants a reply in hnr.reg.email-routing's `messages.md` when it lands. The full lines are in [messages.md at 17f30843](https://github.com/knowledgeislands/ki-principal/blob/17f30843/+/_WORK/ki.sop.main/messages.md). No work owns the MCP server repositories: the parked MAIL-MCP-HOME asks the same question for eleven mail records, which the 27 October roadmap sweep has since moved to ideas in mcp-m365 and mcp-gsuite.

**Query:** Should these five asks go to whichever work you name under MAIL-MCP-HOME?

**Options:**

a) (recommended, confidence high - they share MAIL-MCP-HOME's owner gap, and one decision homes both) Settle MAIL-MCP-HOME now; State of play sends the five asks to the chosen work as its first messages.

b) Send them to ki.prj.tools-burndown now, widening it to the MCP servers for these asks only.

c) Send them to ki.reg.main as ad hoc work, leaving MAIL-MCP-HOME parked.

### STOA-HOME - open a Stoa Project in Knowledge Islands

focus: aside

**Context:** On 31 October HNR's State of play wrote that you chose to split HNR's portal-framework work: the Stoa part moves to Knowledge Islands, which already owns the `knowledgeislands/packages-stoa` repository, and HNR keeps the humansnotrobots.be platform. HNR asks Knowledge Islands to open a Stoa Project, for example `ki.prj.stoa`, covering Stoa releases, the lines telling consuming sites to re-copy Stoa, and DIAGRAM-ROLLOUT: moving the interactive diagram overlay used in 5G Emerge Phase 2 and 3 into Stoa as an optional part. HNR wants the package id back in hnr.sop.sites' `messages.md`. Earlier STOA-ICONS lines were routed on 30 October to whichever work owns packages-stoa; no Knowledge Islands work owns it today. Five Project threads are already open (ways of working, Mac Studio setup, Observatory, chezmoi, Orca evaluation), and on 30 October you called the cap guidance rather than a limit.

**Query:** Should State of play register a Stoa Project and seed its package on hold, ready for you to open?

**Options:**

a) (recommended, confidence high - it follows your own split decision, and seeding on hold opens no thread and starts no work) A run registers the Stoa Project, seeds `ki.prj.stoa` on hold until you open it, queues HNR's asks and the earlier STOA-ICONS lines as its first messages, and replies to hnr.sop.sites with the id.

b) Register and open it now as a sixth active Project thread.

c) Leave Stoa without a Knowledge Islands home for now and tell HNR so.

### ACCESS-ADMINS-ROUTE - send the Access admins pattern to other territories

focus: aside

**Context:** On 28 October at 18:40 GMT Kris asked HNR, for "all sites I run", for a per-site admins Access group with Kris as first member and a `/admin` application admitting only it, and said "send the equivalent to ki-principal for all sites I run". HNR has done its nine humansnotrobots.be sites ([access-admins note](https://github.com/krisb/hnr-principal/blob/2c23cccb/+/_WORK/hnr.prj.portal-framework/design/access-admins.md)); this tidy sent the KI sites to ki.prj.website and ki.prj.observatory. The rest belong to other territories: apps-dafacts.org (Equal Remedy), apps-kris.me.uk and apps-midnight.ninja with its legal, rig, tower and trip subdomains (Personal), apps-yorkphotosoc.org (TechMedix), apps-markhowarth.com and apps-vallearmonia.com (Valle Armonia). No standing route from State of play to those territories' States of play is recorded, and on 12 October you kept territories other than Personal and Valle Armonia parked. The full lines are in [messages.md at 17f30843](https://github.com/knowledgeislands/ki-principal/blob/17f30843/+/_WORK/ki.sop.main/messages.md).

**Query:** Should State of play send one line to each other territory's State of play naming its sites?

**Options:**

a) (recommended, confidence high - Kris's own words cover every site he runs, and a message only queues the work for each owner's own gates) Send one line each to Equal Remedy, Personal, TechMedix and Valle Armonia, quoting Kris, linking HNR's note and its two lessons (restore path first, 120 seconds to settle), asking each to confirm which sites sit behind Access first.

b) Send to Personal and Valle Armonia only, the territories running now, and park Equal Remedy and TechMedix.

c) Hold until you have said which sites sit behind Access.

### OBSOLETE-DROP - drop queries that events have overtaken

focus: aside

**Context:** The census found 15 parked or open queries whose subject no longer exists:

- ki.sop.main: 8.
- ki.prj.estate-factorisation: 4 (HOST-GUARDS, STORE-REPAIR, TRIAGE-OWNERS and DOCK).
- ki.prj.agent-host: 1 (CLI006-PLAN).
- ki.prj.chezmoi: 1 (WARP-HANDLER).
- ki.prj.baseline-rollout: 1 (VA-AREA-TITLES).

In each case the evidence is a committed acceptance or prune, or a deleted folder. Five more in ki.prj.mac-studio-setup are obsolete on evidence read only on sol: RIG-TRIAGE, SOL-SOURCES, SOL-HNR-HARNESS, SOL-KI-CONFIG-DRIFT and FW-LIVE. The tidy rules let only the owning work delete its own files. This query has not been blind reviewed, because this run could not launch a reviewer.

**Query:** Should each tidy run drop the queries that commits prove obsolete, logging each with its evidence, while bringing the sol-only five to Kris?

**Options:**

a) (recommended, confidence high - reviewed: a commit is direct evidence, but host evidence can drift) Each tidy drops the 15 commit-proven queries with a decisions-log line citing the commit, and puts the five sol-evidenced ones to Kris as a batch.

b) Put all 20 to Kris one by one before any drop.

c) Drop all 20 on the census evidence.

### OLD-ORPHANS - possible loss of old repository copies

focus: aside

**Context:** The OLD-ORPHANS query, parked in ki.prj.mac-studio-setup, concerns old orphaned repositories that were to be kept. This census found no checkout of them under `~/workspaces` and no bundle in OneDrive. If they existed only on a retired disk or host, the last copies may already be gone. This query has not been blind reviewed.

**Query:** Do you know where the old orphaned repositories now live?

**Options:**

a) (recommended, confidence high - reviewed: only Kris can say whether another copy exists, and nothing should be dropped while that is unknown) Kris names the location or confirms they are gone, and ki.prj.mac-studio-setup records the answer before its query is closed.

b) Treat them as lost and close the query.

### ADOBE-SCRIPT-HOME - where the Adobe removal script should live

focus: aside

**Context:** ki.prj.mac-studio-setup keeps `setup/adobe-remove.sh`, which removes Adobe Creative Cloud leftovers and acts only with `--apply`. A script breaks the work folder's closed list, so the package cannot pass its check while it sits there, and no other repository holds it. Rig's ideas KI-TOOL-RIG-CORE-072 and KI-TOOL-RIG-CORE-074 already cover app removal and use an Adobe script as a worked example; Rig has not acknowledged this one. The rest of the Adobe clean-up stays parked under ADOBE-DATA and ADOBE-RESTART.

**Query:** Where should the script go?

**Options:**

a) (recommended, confidence high - reviewed: Rig owns the removal capability this example informs, and keeping it as evidence preserves it without creating a separate personal tool) Send it to tools-rig as labelled Creative Cloud removal evidence, and delete the package copy once tools-rig holds a committed copy.

b) Move it into chezmoi as a personal maintenance script.

c) Delete it and leave the Adobe clean-up to an at-screen session, relying on Git history.

### GITCONFIG-AUTOSTASH - Turn off rebase autostash in your own Git configuration

**Context:** Your chezmoi-managed Git configuration (`dot_gitconfig`, line 62) sets `rebase.autoStash = true` with `pull.rebase = true`, so a plain `git pull` in a busy shared checkout silently stashes every uncommitted change, other sessions' included. That caused the 3 November conflict in the assistant repository. The harness now flags the setting (`ki-git` HYGIENE-3, harness `ec5d7bd8`). chezmoi belongs to the household threads since 1 November.

**Query:** Should the chezmoi source stop turning on rebase autostash?

**Options:**

a) (recommended, confidence high - it caused the 3 November conflict and your never-stash rule of 1 November forbids it) State of play sends a line to personal.reg.household-sol to remove `autoStash = true` from `dot_gitconfig`, review `chezmoi diff` and apply it on both Macs; `pull.rebase` stays.

b) Keep the setting and rely on every session overriding it on each pull.

### CHEZMOI-FOLD - Fold the chezmoi Project into the household works now

**Context:** [ki.prj.chezmoi](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.chezmoi/state.md) has been with you since 24 October and has 42 waiting lines. On 1 November you said it folds into the household works (household-terra and household-sol), through a short handover note followed by a hold. That was relayed as the IMPORTANT HANDOVER-HOUSEHOLD line, and nobody has acted on it. The classification above shows most of its lines are already overtaken or belong to the household works. Since 3 November State of play coordinates all Knowledge Islands work (SOLE-THREAD).

**Query:** May State of play take ki.prj.chezmoi back from you and carry out your 1 November fold now?

**Options:**

a) (recommended, confidence high - reviewed: an independent reviewer agreed, since your recorded words already authorise the handover and hold, and moving the questions answers none of them) State of play launches one run that writes the handover note, sends each live line to household-terra, household-sol, the tools-rig lane or the harness as classified above, and puts chezmoi On hold pending close-out. Its four open discussions go across with the note.

b) You first answer chezmoi's four open discussions (ACCEPT-UE106, UTM-SOURCE, WARP-CONTAINER, WARP-HANDLER) yourself, then State of play runs the fold.

### UNTRACKED-REPORTS - What happens to other sessions' uncommitted reports in the handed-over works

**Context:** The four handed-over works hold 11 report files that were never committed. The sessions that made them have drained. They keep two packages failing their folder check, and household-sol asked for one of them. Their outcomes look recorded elsewhere, but no one has checked each. Deleting an uncommitted file cannot be undone, and committing one publishes it in ki-principal's public history while the publication question is open. An independent reviewer chose to keep them for now (high confidence): unlike committed files they can't be recovered from Git, and their homes are unchecked.

**Query:** How should State of play deal with these uncommitted reports?

**Options:**

a) (recommended, confidence high - reviewed: the reviewer chose keeping them at high, and nothing irreversible happens) Leave them in place for now; a read-only run checks where each one's outcome is recorded and lists them, and you decide on each from that list.

b) A run checks each one's home, copies its open questions into its package, then deletes it, keeping any with an unclear home.

c) Commit each into its package, making it public.

### BOARD-CAPTURE - Whether the harness should also drive the browser for design boards

**Context:** The design-system skill now gives any site the shared region collector, region codes and overlays for an annotated design board (harness `4721d886`). Each site still writes its own browser steps: screenshots, switching components through their states, publishing to its canvas. The harness already drives Chrome inside its diagrams skill, but that code is private to it, and sharing it touches a second skill. Only one site has a board so far.

**Query:** Should the design-system skill get its own capture step now, or only once a second site adopts the board?

**Options:**

a) (recommended, confidence high - reviewed: an independent reviewer also chose to wait, since one site's state setup is too little evidence for a reusable capture plan) Wait for a second site, then add capture by sharing the diagrams skill's Chrome driver.

b) Add a capture step now, sharing the Chrome driver.

### VALUES-HOME - Where the shared values live

**Context:** Kris wants each package's values stated up front, and suggested that a Knowledge Islands "knowledge process" carry them. The piloted assistant package writes the five values in full in its own `work.md`. Copying them into every package means every package changes when the values do. Knowledge Islands Principal's [Work Process](/Users/krisbrown/kis/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Processes/Work Process/Work Process.md) note already holds the work model; a change there goes through the Enactment Process.

**Query:** Where should the shared values be written?

**Options:**

a) (recommended, confidence high - reviewed: an independent reviewer chose the same course; one canonical home avoids drift, but Kris named a "knowledge process" note, which may mean a new note rather than the Work Process) Write them once in the Work Process note under an Enactment record, and give each `work.md` an optional one-line `## Values` section linking them and adding any of its own.

b) Write them once in a new Knowledge Process note in Knowledge Islands Principal, linked the same way.

c) Copy the full values line into every package's `work.md`, as the pilot does.

### STATUS-DETAIL - How much detail Status gives on what waits for Kris

**Context:** STATUS-FORM asked for no full queries in Status; HOW-WE-WORK later asked for "what is waiting on Kris in detail under the table". The Summary already gives each query in full with its options.

**Query:** Under the Status table, how much should each waiting item show?

**Options:**

a) (recommended, confidence high - reviewed: an independent reviewer chose the same course; keeps Status short and leaves the full form to Summary, but "in detail" may mean more) One line per tag: the plain question and the recommended option, with a pointer to the Summary for the rest.

b) Each query in full, Context, Query and Options, as the Summary gives it.

### WHAT-I-HEARD - Which of Kris's words the read-back covers

**Context:** Status ends with "What I heard", a short read-back of Kris's words kept apart from decisions. Status never moves the mark, so it needs its own window.

**Query:** Which of Kris's words should "What I heard" cover?

**Options:**

a) (recommended, confidence high - reviewed: an independent reviewer chose the same course; the mark is the window every other form already uses, and a cap keeps it short) Kris's words since the mark, newest first, at most five lines, each quoted or closely paraphrased, with no decision restated.

b) Only Kris's words since the last Status or Summary.

### GOAL-SETTING - What the goal-setting mode does

**Context:** HOW-WE-WORK names "a goal-setting mode" and nothing more. Goals and order now live in each Focus item. The interactive pass already asks one question at a time.

**Query:** What should the goal-setting mode be?

**Options:**

a) (recommended, confidence high - reviewed: an independent reviewer chose the same course; reuses a shape Kris already uses, though Kris may have meant something broader) An owner-invoked pass, "goals" or `/ki-coordination goals`, walking each focus area one at a time to confirm or reword its goal and order, then writing `work.md`, logging Kris's words and closing with a Status.

b) Leave it out of this build and shape it after Status has been in use for a week.

### URGENT-CRITERIA - What counts as urgent

**Context:** Kris said "not everything" is an escalation. Escalation interrupts a leader and, where none is live, lets a sender do another work's unit, so the test matters.

**Query:** Which units may be sent as `URGENT`?

**Options:**

a) (recommended, confidence high - reviewed: an independent reviewer chose the same course; both come from Kris's own words, the deadline from URGENT-HANDOFF and the rollout from HOW-WE-WORK) Only a unit with a stated deadline, or a process rollout other work must follow; anything else goes as an ordinary or `IMPORTANT` line.

b) Any unit the sender judges urgent, giving its reason in the line.

### LIVENESS - How a worker is judged live

**Context:** Escalation needs to know who is live. The `workers:` register in `state.md` is a pilot, not in the standard; Agora shows presence but is not yet relied on. A register entry can go stale when a session dies without updating it, as the 3 November usage-limit outage showed.

**Query:** What makes a worker count as live for escalation?

**Options:**

a) (recommended, confidence high - reviewed: an independent reviewer chose the same course; it reuses fields already piloted and guards against stale entries, but the 30-minute bound is a guess) Its register entry says `status: active` and `listening: on`, and its package or Agora shows activity within the last 30 minutes; the register becomes a standard optional `state.md` field.

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

### RENAME-FENCE - Records under a renamed work now carry over

**Context:** A test added on 28 Oct (`7f91270b`, KI-TOOL-KI-CLI-174) deliberately left a run's control record refused after its work was renamed, and needed a separate new run to continue. Your 1 Nov request, via hnr.sop.5ge, asked for renamed work ids to be followed. I replaced that test: a record made on this machine whose old home is gone now moves to the renamed work, and its earlier attempts stay valid under the former id.

**Query:** Is carrying the record over, rather than refusing it, what you want?

**Options:**

a) (recommended, confidence high - reviewed: an independent reviewer chose the same, since continuity is justified when the rename is verified and earlier identities are kept) Yes. Keep the new behaviour.

b) No. Keep refusing, with only the single repair command offered.

### EDA-HOME - Where the Exchange Dynamics Analysis method should live

**Context:** Kris wants a reusable way to analyse a conversation once and present it several ways: as an infographic, a report or an interactive view. It has four parts: the method, a data format (a JSON schema), a visual layout and step-by-step instructions for an agent. The existing skills `archify` and `dataviz` only draw. Neither is owned by Knowledge Islands, and `archify` comes from an outside author, so extending either would mean keeping our own copy of someone else's code. A skill in the KI Agentic Harness can be used from any repository and can include the data format, a checking script and an example. A note in Pillars can only be read inside this island. The harness has no group of skills for analysis yet; the closest group is `acquire`, which already handles turning sources into structured knowledge.

**Query:** Where should the method live?

**Options:**

a) (recommended, confidence high - reviewed: an independent reviewer chose the same; the harness is the strong fit, though analysis reaches beyond capture) A new harness skill, `ki-exchange-dynamics`, in the `acquire` group of ki-agentic-harness. It would hold the method, data format, visual layout, agent steps and the invented example, and it would use archify and dataviz to draw. Ki-principal would get an optional short note in Emerging Concepts that points to the skill.

b) The same skill, but in a new `analysis` group of skills, in case more analysis methods follow.

c) A Pillars note in ki-principal only, with no skill. Agents in other repositories could not use it directly, and every change would need the Enactment Process.

d) Extend `archify` or `dataviz` to carry the method.

### REPLY-BLOCK-SUMMARY - Should the new Summary end its queries with a copyable reply block?

**Context:** The approved design note says `## Queries` lists every open query in full "then the copyable reply block". The coordination standard has carried no reply block since Kris's REPLY-BLOCK decision of 18 October: Kris answers by voice, by tag or in order. This run's brief asked only for "`## Queries` in full". I landed the Summary without a reply block, so REPLY-BLOCK still stands.

**Query:** Should the Summary's Queries section end with a copyable reply block, as the design note says?

**Options:**

a) (recommended, confidence high - reviewed: an independent reviewer chose the same, since it keeps your spoken-answer way of working) Keep no reply block. The design note's phrase is read as left over from before REPLY-BLOCK, and household-terra is told so.

b) Add a copyable reply block at the end of the Summary's Queries, reversing REPLY-BLOCK for the Summary only.

c) Bring the reply block back in every owner report, reversing REPLY-BLOCK entirely.

### ACCEPT-KI-TOOL-MGIT-CLI-033 - Accept the sync push guard

**Context:** [KI-TOOL-MGIT-CLI-033](/Users/krisbrown/kis/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-033-sync-push-guard.md) (`mgit sync` pushes only with `--push`, which Kris adopted after a blind review on 25 October) was delivered on 31 October (tools-mgit `f67e255`) and is awaiting review. Its only acceptance question sits among Ways of working's parked queries, and State of play has no ACCEPT query for it, though ACCEPT-BUNDLE (Kris, 20 October) has State of play bring every record awaiting acceptance "as the first point of call".

**Query:** Should State of play add this record to the `mgit` acceptance with KI-TOOL-MGIT-CLI-032?

**Options:**

a) (recommended, confidence high - the same repository and reviewer as CLI-032, and ACCEPT-BUNDLE asks for exactly this) Add ACCEPT-KI-TOOL-MGIT-CLI-033 beside ACCEPT-KI-TOOL-MGIT-CLI-032, oldest first, with a fresh review-prep run before you accept through `ki-accept`.

b) Leave it with Ways of working until that work opens again.

### STALE-ACCEPTS - Drop four acceptance queries whose records are already accepted

**Context:** Four parked State of play queries ask Kris to accept records that were accepted and pruned on 27 October: [KI-WEBSITE-SITE-044 (pruned)](https://github.com/knowledgeislands/apps-knowledgeislands.info/blob/ae886e2b/docs/roadmap/KI-WEBSITE-SITE-044-design-v1.md) in apps-knowledgeislands.info `fdc1ac2`, [KI-PRINCIPAL-OPS-014 (pruned)](https://github.com/knowledgeislands/ki-principal/blob/1fba2fb7/Streams/Roadmap/KI-PRINCIPAL-OPS-014-gfm-conversion.md) and [KI-PRINCIPAL-MOD-009 (pruned)](https://github.com/knowledgeislands/ki-principal/blob/1fba2fb7/Streams/Roadmap/KI-PRINCIPAL-MOD-009-amend-adr-001-staging-wording.md) in ki-principal `a88b2f92`, and [KI-TOOL-RIG-CORE-062 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/14715c30/docs/roadmap/KI-TOOL-RIG-CORE-062-own-address-firewall-destination.md) in tools-rig `033d952`, each "chore(roadmap): prune ... done work records". I checked each deletion commit directly. OBSOLETE-DROP, still open, asks the general version of this question.

**Query:** May State of play drop ACCEPT-KI-WEBSITE-SITE-044, ACCEPT-KI-PRINCIPAL-OPS-014, ACCEPT-KI-PRINCIPAL-MOD-009 and ACCEPT-KI-TOOL-RIG-CORE-062, logging each prune commit?

**Options:**

a) (recommended, confidence high - the prune commits show each record done and gone, and dropping a query changes no record) Drop the four, one decisions-log line each citing its commit, and treat this as part of OBSOLETE-DROP a).

b) Keep them parked until you answer OBSOLETE-DROP.

### BRANCH-SWEEP - Clear merged branches and the worktrees of finished runs

**Context:** Every repository is level with GitHub, but finished runs left branches and working copies behind. Merged into `main` and safe to remove by Git's own check: ki-agentic-harness `finished-tidy`, `quiet-listen` and `rename-paperclip`; tools-ki `wow-rel-0141`; tools-rig `run/wow-night-rig-048-f` and `run/wow-night-rig-056-e`; the remote `ways-of-working-learn` in apps-knowledgeislands.info. Most still have a worktree (a second working copy of the repository) under `~/.local/state/ki/agents/` or `$TMPDIR`, from Ways of working runs that `ki agent status` no longer lists. I did not check those worktrees for uncommitted files.

**Query:** Should one housekeeping run remove the merged branches and their worktrees?

**Options:**

a) (recommended, confidence high - reviewed: an independent reviewer chose the same, provided each removal is checked fresh and uses Git's normal non-forcing commands, leaving anything dirty, active or uncertain untouched) One bounded run checks each worktree is clean, removes clean ones with `git worktree remove` and their merged branches with `git branch -d`, and lists any dirty one for you without touching it.

b) Leave them until each owning Project closes.

### UNMERGED-STRAYS - Decide the unmerged branches finished runs left

**Context:** Eight branches hold commits not on `main`, from runs that have finished: tools-ki `wow-close-done-2` and `wow-day-impl-fix-5` (21 and 22 October, `ki agent` recovery fixes); ki-agentic-harness `ki-e2e` and `orca-adapter` (1 and 2 November, draft skills); tools-rig `run/wow-accept-rig-056` and `run/wow-rework-rig-056` (20 October, KI-TOOL-RIG-CORE-056 evidence); apps-observatory.local `z-retirement/observatory-20261030` (30 October retirement evidence, also on GitHub); ki-principal `run/wow-mod011-approved-candidate-mpg8sgz6`, the same two commits as GitHub's `wip/z-retired-mod011-20261030` (28 October, KI-PRINCIPAL-MOD-011 candidate); chezmoi `tower-nudge-retire` (3 November). Some may be superseded by later work on `main`; none has been compared.

**Query:** Should a read-only run compare each branch with `main` and bring you a keep, merge or drop list?

**Options:**

a) (recommended, confidence high - read-only, and nothing is lost while you decide) One read-only run reports, per branch, whether `main` already carries its change, which work owns it and a recommended disposition; nothing is deleted.

b) Leave them for each owning Project.

### RESUME-SPECS - Resume Portable specifications

**Context:** [ki.prj.portable-specifications](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.portable-specifications/state.md) has been paused since 20 October, released only when Kris says resume. Its draft 0.8 specifications passed six blind reviews, the last finding nothing, and its two parked queries, SPEC-TEXT and HOMING-EDITS, are both recommended at high confidence. Resuming means planning KI-HARNESS-GOV-229 and KI-HARNESS-GOV-230 to Ready in the harness, which the summary-model and emerging-only chain also edits. Timelines and Baseline rollout are paused the same way, with two and fifteen parked queries.

**Query:** Should Portable specifications resume now, with the other two paused works left as they are?

**Options:**

a) (recommended, confidence high - reviewed: an independent reviewer chose the same; owner review can resume now while the harness chain finishes) Resume Portable specifications only: put SPEC-TEXT and HOMING-EDITS to you, then plan its harness records after the harness chain finishes.

b) Keep all three paused until the open method queries are settled.

### ORCA-CLOSE-HOME - Where the Orca evaluation's leftovers live before its folder is deleted

**Context:** The Orca evaluation Project ([ki.prj.orca-evaluation](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.orca-evaluation/work.md)) was handed to the assistants on 2 November. Its folder was due to be deleted once the assistant acknowledged the handover, and the assistant has now done so. Before a folder is deleted, the method requires everything still useful in it to have a home somewhere else. Two things don't yet. First, the five questions you haven't answered: SCOPE-SPLIT, ORCA-UPSTREAM, THREADS-TRY, THREADS-SWEEP and THREADS-FR. The assistant logged that it received them but never copied them into its own list of open questions. Second, three notes live only in this folder: the trial log, the handover note and the draft proposal for an Orca launcher. The assistant and Ways of working both link to them there. Git would still keep everything after deletion, but those links would break and the five questions would be held nowhere live.

**Query:** Should the Orca folder stay on hold until its questions and notes have a live home, or be closed now with Git as the only record?

**Options:**

a) (recommended, confidence high - reviewed: an independent reviewer chose the same, keeping the five questions where you will see them) Keep it on hold. Send assistant-sol one line asking it to copy the five questions into its own `discussions.md` and to take the trial log and handover note into its package. Leave the launcher proposal with Ways of working until the Orca adapter lands or is dropped. State of play then closes the folder once both are done.

b) Take the five questions into ki.sop.main's own `discussions.md`, since it already coordinates this work. Close the folder as soon as the three notes are homed.

c) Close it now: mark it finished and delete the folder, with Git history and ki.sop.main's handover-intake report as the only record of the questions and notes.

### STRAY-BLIND-REPORT - Home the untracked blind-review report of 1 November

**Context:** `blind-review-stocktake.report.md` sits at the top of the Observatory package folder. It has never been committed to Git, here or (per the STRAY-REPORTS-SOL line) on sol. The Observatory coordinator recorded it as received on 1 November (STOCKTAKE-RECEIPT), and its outcome is already in the ten parked discussions. This run left it untouched, because its rules forbid touching another session's uncommitted file. Deleting it would lose the text for good, since Git has no copy.

**Query:** Should the report be committed into the package's `stocktake/` folder, so that Git keeps it and a later mark can prune it?

**Options:**

a) (recommended, confidence high - reviewed: an independent reviewer chose the same, provided the move is verified before the request line is cleared) Have a State of play run move it into `stocktake/` beside `stocktake.report.md` and commit it there. The run then removes the STRAY-REPORTS-SOL line and tells sol it is done.

b) Delete it as already received, accepting that its text is lost.

c) Leave it where it is until the TIDY-RUN discussion is answered.

### TOOLS-RIG-LANE - Who carries the Rig tooling work once Mac Studio setup closes

**Context:** On 17 October Kris gave Mac Studio setup the tools-rig lane (RIG-OWNER). The household works that took over the Mac Studio on 2 November exclude Rig tooling changes, and no other work names tools-rig. Without an owner are the open records [KI-TOOL-RIG-CORE-047](/Users/krisbrown/kis/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md), [KI-TOOL-RIG-CORE-068](/Users/krisbrown/kis/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-068-replaced-pf-root-ruleset-bypass.md), [KI-TOOL-RIG-CORE-069](/Users/krisbrown/kis/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-069-dynamic-type-handler-fallback.md), [KI-TOOL-RIG-CORE-070](/Users/krisbrown/kis/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-070-handler-read-back-after-confirmation.md), [KI-TOOL-RIG-CORE-075](/Users/krisbrown/kis/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-075-restart-services-after-upgrade.md) and [KI-TOOL-RIG-CORE-076](/Users/krisbrown/kis/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-076-host-defaults-and-power.md). Also without an owner are eleven Rig message lines and the spec-sched brief. On 1 November Kris said Knowledge Islands' method work goes to State of play when a work closes (PS-METHOD-HOME). This query gates the [close-out plan](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.mac-studio-setup/setup/close-out.md): every "lane" row waits on it. It is parked unchanged in the package's discussions.

**Query:** Which work should carry the tools-rig lane after Mac Studio setup closes?

**Options:**

a) (recommended, confidence high - reviewed: State of play's definition takes work without an owner, while tools-burndown and both household works exclude Rig tooling; holding the lane means keeping and routing requests, not delivering Project work itself) State of play holds the lane, receives the retained Rig lines at close-out, and dispatches tools-rig work until Kris opens a dedicated Rig work.

b) ki.prj.tools-burndown takes tools-rig alongside tools-ki and tools-mgit.

c) personal.reg.household-sol takes Rig tooling too, widening its scope.

### RIG-INTAKE - What happens to the retained Rig capability lines

**Context:** Nine lines (eleven bullets) of Rig requests have waited in Mac Studio setup since 29 October. On 14 October Kris set BURN-DOWN: "burn the roadmap down; no new feature records". On 19 October CAPTURE-GATE refined it: capture only blockers, defects seen failing or items Kris asked for, and put ideas in `_IDEAS.md`. Four lines are Kris's own asks: RIG-TUI, RIG-SSH-CHECK, RIG-COMMENT-KIND, and RIG-APP-FOOTPRINT with its RIG-NOTIFICATIONS and RIG-MACHINE-MANAGEMENT companions. RIG-CLI-CONSISTENCY reports defects seen failing on sol. The footprint group's natural home, [KI-TOOL-RIG-CORE-072](/Users/krisbrown/kis/knowledge-islands/tools-rig/docs/ideas/KI-TOOL-RIG-CORE-072-application-configuration-touch-points.md), was moved to ideas on 27 October. The per-line table is in [rig-intake.report.md](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.mac-studio-setup/setup/rig-intake.report.md). This query decides what the lane does with each line, so nothing in the close-out plan routes before it is answered. It is parked unchanged in the package's discussions.

**Query:** Should the lines be handled as the table proposes: four triage captures, the footprint group held with the KI-TOOL-RIG-CORE-072 idea, and two returns?

**Options:**

a) (recommended, confidence high - reviewed: the blind review independently chose this course, since CAPTURE-GATE admits Kris's explicit asks and defects seen failing, and the 27 October deferral of KI-TOOL-RIG-CORE-072 stands until Kris brings it back) Capture four unadopted tools-rig triage records: RIG-TUI, RIG-SSH-CHECK, RIG-COMMENT-KIND, and one bounded RIG-CLI-CONSISTENCY record separating real failures from intended behaviour. Hold the footprint group with the KI-TOOL-RIG-CORE-072 idea, keeping its wording. Return WAKE-SUBSTRATE to State of play and RIG-REMINDER-DOCTOR to its originating work, with the evidence.

b) Strict BURN-DOWN: capture only RIG-TUI and RIG-SSH-CHECK, which Kris named as idea records. Hold RIG-COMMENT-KIND and RIG-CLI-CONSISTENCY as `_IDEAS.md` bullets, and the footprint group with KI-TOOL-RIG-CORE-072. The returns stay as in a).

c) Honour the IMPORTANT footprint ask now: bring KI-TOOL-RIG-CORE-072 back from ideas as a triage record carrying the whole footprint group, plus everything else in a).

### WATCH-AGORA - Whether `ki work watch` is still wanted now Agora rings a doorbell

This is also written into [discussions](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.tools-burndown/discussions.md). It is medium confidence, so it needs one blind review before it goes to Kris.

**Context:** On 1 November Kris decided INBOX-VERB: a read-only command, `ki work watch <work id>`, that waits quietly and wakes a thread when a message lands or a run finishes (the WATCH-VERB line). On 3 November Agora began waking threads itself through a doorbell file (AGORA-DOORBELL), and State of play's own wake now uses it. The method intake of 3 November thought the command was probably no longer needed, but that question never reached Kris.

**Query:** Should tools-ki still build `ki work watch`?

**Options:**

a) (recommended, confidence medium - reviewed, views differ: Agora's doorbell already does the waking, and a second watcher would duplicate it; the independent reviewer chose b) at medium, because the doorbell leaves gaps on hosts or runtimes without Agora) Drop WATCH-VERB as no longer needed now Agora's doorbell exists, keeping its design for reference.

b) Build it anyway, as a bounded fallback for runtimes or hosts without Agora, using Agora's doorbell where it already wakes the thread; the reviewer's choice.

### KA-CLOSE - close the finished Knowledge acquisition work

focus: aside

**Context:** [ki.prj.knowledge-acquisition](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.knowledge-acquisition/work.md) has been Finished since 20 October on Kris's word, all its decisions homed; its [Project](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/knowledge-acquisition.md) is `completed`, and its own next step is to delete the folder in one commit at the closing mark and archive its runs. State of play may not remove another work's folder on its own authority.

**Query:** Should a bounded run close it now?

**Options:**

a) (recommended, confidence high - reviewed: Finished and completed are both recorded; Kris authorises the closing mark and package scope) A bounded run strikes its closing mark, removes the package in one commit by explicit path and archives its runs with `ki agent close`.

b) Leave the folder until Kris opens that work's thread.

### AUDIT-ORPHANS - A stopped audit leaves its test run going

**Context:** When an audit is stopped part-way, for instance by an agent's command time limit, the full test run it started keeps going in the background and holds the coverage report folder. The next audit of the same checkout then fails at once with "already in use by another Vitest process", or both runs slow each other down. I saw this happen today. The test run is started by the ki-engineering skill's evidence code in the harness, not by tools-ki's audit code, so it was outside this run's scope. The minute-by-minute line now makes stopping less likely, but doesn't prevent it.

**Query:** Should a stopped audit also stop the test run it started?

**Options:**

a) (recommended, confidence medium - it removes the collision, but the right place for the change, the harness evidence code or tools-ki, isn't settled) Record it as a work item for the harness's ki-engineering evidence code: stop its child processes when the audit is interrupted.

b) Leave it, and rely on agents running the audit in the background with a long enough time limit.

## Parked

### ACCEPT-CHEZMOI - accept the chezmoi latest-source record

focus: acceptance

**Context:** [PERSONAL-DOTFILES-UE-076](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/PERSONAL-DOTFILES-UE-076-always-run-latest-source.md), "always run the latest source", has been awaiting review since 24 October.

**Query:** Review and accept it now?

**Options:**

a) (recommended, confidence high - ACCEPT-BUNDLE) Review it now through `ki-accept`.

b) Leave it awaiting review.

### ACCEPT-KI-WEBSITE-SITE-044 - accept the website's design v1

focus: acceptance

**Context:** [KI-WEBSITE-SITE-044 (pruned)](https://github.com/knowledgeislands/apps-knowledgeislands.info/blob/ae886e2b/docs/roadmap/KI-WEBSITE-SITE-044-design-v1.md) moves the site onto `ki-design`: its tokens, type, Voyage and Atlas navigation, the restyled home page, a new Field Guide and `sync:design`. It also includes the Port switch. Every gate in its Verify list passed again on `main` at `2628c48`. Two items are still open, and neither can be settled without the network or a person:

- **The private citation.** The Field Guide cites `knowledgeislands/ki-design`. The page-provenance guide forbids citing a source no reader can open. `ki-design`'s `.ki.toml` has declared `visibility = "public"` since 18 October, but the 20 October review found the repository returned 404 to anonymous readers. This run made no network call, so it is unconfirmed whether it is public now.
- **The visual check.** The record asks for a visual check at 1440 and 390 px in both colour schemes. It has not been repeated since the Port update.

**Query:** Accept KI-WEBSITE-SITE-044 once you have confirmed that `ki-design` opens for an anonymous reader and looked at the pages?

**Options:**

a) (recommended, confidence high - reviewed: both gaps can be closed by checking the delivered result before deciding whether a repair is needed) Open `https://github.com/knowledgeislands/ki-design`, and the Field Guide's exact pinned source, in a private window. Look at the home page, one inner page and the Field Guide at 1440 and 390 px, in light and dark, and record the results. If both checks are good, accept through `ki-accept`; if access or the visuals fail, return it for that specific repair and a refreshed review packet.

b) Accept now, knowing the Field Guide's citation may not yet open for readers.

c) Return it to implementation to drop or replace the `ki-design` citation, and to refresh the out-of-date packet lines, before acceptance.

### ACCEPT-KI-PRINCIPAL-OPS-014 - accept the GitHub-flavoured Markdown conversion

focus: acceptance

**Context:** [KI-PRINCIPAL-OPS-014 (pruned)](https://github.com/knowledgeislands/ki-principal/blob/da027e6d/Streams/Roadmap/KI-PRINCIPAL-OPS-014-gfm-conversion.md) converted ki-principal to GitHub-flavoured Markdown in nine commits, plus the 20 October owner answers (plain images, template links, Link Review). Acceptance tests 1, 2, 3 and 5 are evidenced, and this run confirmed tests 2 and 5 again: no wikilinks remain, and no failure falls on the converted paths. Acceptance test 4 is still open and is yours under RENDER-CHECK a): the final Step, a client render check of the Library heading link and an alert in GitHub, Obsidian, Zed and the Observatory, plus the four plain images. In the Observatory, the dropped heading fragment has to be either recorded as a failure or accepted as a fallback.

**Query:** Run the four client render checks, then accept KI-PRINCIPAL-OPS-014?

**Options:**

a) (recommended, confidence high - the record makes test 4 your check before acceptance, and every other test is evidenced) Run the four render checks and tell me each outcome, including how to treat the Observatory fragment. Then accept, with the outcomes recorded.

b) Accept now, expressly waiving acceptance test 4.

c) Leave it awaiting review until you have time for the render checks.

### ACCEPT-KI-PRINCIPAL-MOD-009 - accept the ADR-KI-PRINCIPAL-001 staging amendment

focus: acceptance

**Context:** [KI-PRINCIPAL-MOD-009 (pruned)](https://github.com/knowledgeislands/ki-principal/blob/da027e6d/Streams/Roadmap/KI-PRINCIPAL-MOD-009-amend-adr-001-staging-wording.md) amended [ADR-KI-PRINCIPAL-001](/Users/krisbrown/kis/knowledge-islands/ki-principal/Admin/Governance/Decisions/ADR-KI-PRINCIPAL-001-provider-neutral-knowledge-acquisition.md) and the [Acquisition Process](</Users/krisbrown/kis/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Processes/Acquisition Process/Acquisition Process.md>) in `3b1ade21` on 23 October. The changes stage material outside the receiving island, make delivery into `+/_ACQUIRED/` package acceptance, and call Acquire the port and sorting office, as CUSTOMS-WORDS a) approved. Checks pass on the delivered files. One problem: the rewritten Context sentence at line 18 says "The Harbour defined in SDR-KI-PRINCIPAL-002 is the island's incoming working area". [GDR-KI-PRINCIPAL-010](/Users/krisbrown/kis/knowledge-islands/ki-principal/Admin/Governance/Decisions/GDR-KI-PRINCIPAL-010-the-port.md) retired Harbour as a Knowledge Islands term on 18 October and made `+/` the Port's inbound side. The delivery therefore wrote a retired term back into a current ADR in the present tense. The References line describing SDR-KI-PRINCIPAL-002 is accurate as history. Against that, GDR-KI-PRINCIPAL-010's Consequences keep Harbour wording in earlier Decision Records as a historical record, to be read as the Port; but this sentence was rewritten in `3b1ade21`, after that decision.

**Query:** Return KI-PRINCIPAL-MOD-009 to implementation for a one-sentence fix of the Harbour wording, or accept it as it stands?

**Options:**

a) (recommended, confidence medium, review disagrees - a single sentence conflicts with GDR-KI-PRINCIPAL-010, but it can be read as SDR-KI-PRINCIPAL-002's historical name) Return it to implementation. Reword line 18 so that `+/` is the island's inbound side of the Port under GDR-KI-PRINCIPAL-010, cite `3b1ade21` in the record, then resubmit.

b) Accept as it stands, reading "Harbour" as SDR-KI-PRINCIPAL-002's own term; the blind reviewer prefers this at high, because GDR-KI-PRINCIPAL-010 expressly keeps Harbour wording in earlier Decision Records, and a one-sentence implementation cycle is not required for it alone, the ordinary acceptance gates staying separate.

### ACCEPT-KI-TOOL-RIG-CORE-062 - accept Rig's own-address firewall destination

focus: acceptance

**Context:** [KI-TOOL-RIG-CORE-062](https://github.com/knowledgeislands/tools-rig/blob/223ba459/docs/roadmap/KI-TOOL-RIG-CORE-062-own-address-firewall-destination.md) narrows the `macos-pf` anchor so it passes Tailscale sources only to the Mac's own tailnet addresses, discovered read-only from `ifconfig`. It refuses when no address can be found and reports a stale address. The gate refusal from 20 October is resolved, and today the full suite passes 645 of 645 and the audit has no failures. Its Verify list still asks for a read-only `ifconfig` on `terra` to confirm discovery under Homebrew `tailscaled`, and the 20 October reviewer asked for that evidence before resubmission. It was never obtained, and this run is barred from remote calls. The attended live rewrite of `sol`'s and `terra`'s anchors stays separate, connection-critical work with its rehearsed rollback. The on-link residual stays by your decision.

**Query:** Run the read-only `terra` check, then accept KI-TOOL-RIG-CORE-062?

**Options:**

a) (recommended, confidence high - reviewed: the named verification is still missing and can be completed without changing the firewall) Run `ssh terra /sbin/ifconfig | awk '/^[a-z]/{i=$1} /inet6? (100\.|fd7a:115c:a1e0)/{print i, $2}'` and tell me the output. If one `utun` interface carries both addresses, accept through `ki-accept`, with the output recorded. A different or ambiguous shape goes back to implementation review.

b) Accept now, carrying the terra check into the attended rollout, because Verify words it as "before any live apply".

c) Leave it awaiting review; the blind reviewer names this the proper interim state while terra is unavailable.

### ACCEPT-OBSERVATORY - accept the two Observatory records

focus: acceptance

**Context:** Under ACCEPT-OBSERVATORY a) (25 October) Kris chose to review and accept [KI-OBSERVA-BRG-005 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/0966ac3e/docs/roadmap/KI-OBSERVA-BRG-005-act-board-missing-parts.md) and [KI-OBSERVA-VIS-030 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/0966ac3e/docs/roadmap/KI-OBSERVA-VIS-030-known-lands-chart.md) through `ki-accept` once ki.prj.observatory had fixed BRG-005's structure. BRG-005 now passes the roadmap audit, so that precondition is met. The review-prep run exited without finishing, so neither review is prepared yet.

**Query:** Rerun the review prep, then accept both records, oldest first?

**Options:**

a) (recommended, confidence high - restates Kris's own ACCEPT-OBSERVATORY a), its precondition now met) Rerun the review prep: check each record is still Awaiting review and each criterion against its evidence, then bring each disposition to Kris for acceptance through `ki-accept`.

b) Leave both awaiting review.

### AGENT-HOST - unstick the agent host work

focus: aside

**Context:** [ki.prj.agent-host](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.agent-host/work.md) has sat With worker with no live session, and Kris's own IMPORTANT DRAIN line of 22 October is still unread at the top of its `messages.md`, with the two REFRESH lines beside it. No run can drain another work on State of play's authority.

**Query:** Open the agent host thread so it takes DRAIN and REFRESH first?

**Options:**

a) (recommended, confidence high - Kris's own instruction is waiting in its queue) Open its thread from `ki agent prompts ki`; it acts on DRAIN and the REFRESH re-reads before anything else.

b) Leave it until the Techne programme work resumes.

### CLI006-CONFIRM - confirmation design for the guarded host commands

focus: aside

**Context:** [KI-TOOL-TECHNE-CLI-006 (pruned)](https://github.com/knowledgeislands/tools-techne/blob/ffcaf0c099f1d3019247ff97466754b8a7312166/docs/roadmap/KI-TOOL-TECHNE-CLI-006-guarded-host-commands.md) must decide how `techne host rebuild` and `withdraw` meet `destroy.sh`'s `CONFIRM_DESTROY_AGENT_HOST`: a stale exported value could confirm a destroy on a clean host.

**Query:** Which confirmation design should the plan carry?

**Options:**

a) (recommended, confidence medium, review disagrees - the narrowest change to the existing script) Pass the confirmation through, scoped to the one command.

b) A Harness-declared confirmation with fresh interactive consent; the blind reviewer prefers this at high.

### CLI006-READY - set the guarded host commands record to Ready

focus: aside

**Context:** KI-TOOL-TECHNE-CLI-006 was replanned at tools-techne `31c7b7d` and its audits pass; it sits inside the Techne programme focus. Its handling of the destroy confirmation, CLI006-CONFIRM above, is part of the plan that would be made Ready.

**Query:** In what order should the plan reach Ready?

**Options:**

a) (recommended, confidence medium, review disagrees - the blind reviewer chose this at high because the confirmation design is part of the plan; the earlier ranking put review-now first) Settle CLI006-CONFIRM, then Kris reviews the plan and a ki-plan run sets it to Ready.

b) Kris reviews the present plan now and a ki-plan run sets it to Ready.

### ESTATE-CLOSE - retire Estate factorisation as prepared

focus: aside

**Context:** Under PROJECT-CLOSE a) (25 October) the retirement is prepared in [design/estate-factorisation-retirement.md](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.sop.main/_emerging/estate-factorisation-retirement.md): settle HOST-WRITES, ALIAS-OWNERS and RIG-REFS, route the parked queries to their works by message, then Kris accepts the close. Nothing is applied yet.

**Query:** Proceed with steps 1 and 2 of the note, with the close itself waiting for your acceptance?

**Options:**

a) (recommended, confidence high - restates Kris's own PROJECT-CLOSE a)) State of play sends the prerequisite and routing messages; Kris accepts the close once they are settled.

b) Amend the note first.

### SPECS-FOLDER - 25 unowned reports in ki.specifications

focus: aside

**Context:** `+/_WORK/ki.specifications/` has no `work.md` and holds 25 untracked run reports (plan, draft-review, revise, query-review, home-plan and others) from 24 October 21:10, so the work-package audit fails STRUCTURE-1. The [Specifications](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/specifications.md) Project is paused and a separate [ki.prj.portable-specifications](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.portable-specifications/work.md) package exists. Which session produced the reports is not known; nothing has been touched.

**Query:** Which session or work owns these reports?

**Options:**

a) (recommended, confidence high - reviewed: unknown ownership cannot justify inventing a package or moving the reports) Leave them untouched until Kris names the owning session or work, which then homes them.

b) Seed a minimal on-hold `ki.specifications` package around them.

c) Move them into ki.prj.portable-specifications.

### MAIL-MCP-HOME - a home for the mail MCP records

focus: aside

**Context:** Eleven draft records for the mail MCP servers, KI-MCP-M365-TOOL-011 to TOOL-019 in mcp-m365 and KI-MCP-GSUITE-TOOL-008 and TOOL-009 in mcp-gsuite, plus [PERSONAL-DOTFILES-UE-097](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/PERSONAL-DOTFILES-UE-097-configure-gmail-routing-paths.md) in chezmoi, came to Knowledge Islands on 21 October: "For now, I think it's best to go back to the MCP. So, something in Knowledge Island." No work owns the MCP server repositories: ki.prj.tools-burndown covers the `ki` CLI and Git tools, and ki.reg.main takes small one-off work.

**Query:** Which work should own these records?

**Options:**

a) (recommended, confidence high - reviewed: a coherent twelve-record backlog warrants a named owner) Kris registers a mail MCP Project and State of play seeds its package with the records as its first message.

b) ki.prj.tools-burndown widens its scope to the MCP servers.

c) ki.reg.main holds them as drafts until Kris prioritises them.

### ACQUIRE-HOME - a home for CODEX-SESSIONS and DEFUDDLE-SKILL

focus: aside

**Context:** CODEX-SESSIONS manages repository-agent sessions, Codex and Zed external-agent ones included, through their local lifecycle from the `ki-housekeeping-chatgpt` inventory, with no transcript archive. DEFUDDLE-SKILL adds a `ki-acquire-web` provider skill using the pinned `defuddle` CLI, never its hosted API, trialled before adoption. Their natural owner, Knowledge acquisition, is completed.

**Query:** Where should these two go?

**Options:**

a) (recommended, confidence high - reviewed: each delivery can be bounded on its own without reopening a finished outcome; the open Codex states and cleanup policy are settled at planning) Route both to [ki.reg.main](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.reg.main/work.md) as separate pieces of harness skill work.

b) Route both to ki.prj.ways-of-working.

c) Reopen Knowledge acquisition, or register a successor Project, for both.

d) Route both to ki.prj.baseline-rollout.

### SANCTUARY-STAGE5 - take the Sanctuary package at stage 5

focus: aside

**Context:** Under [ADR-VA-WEBSITE-009](/Users/krisbrown/kis/valle-armonia/apps-vallearmonia.com/docs/decisions/ADR-VA-WEBSITE-009-the-sanctuary-becomes-a-shared-editorial-library.md), Valle Armonia builds the Sanctuary editor through stages 2 to 4 and Knowledge Islands is asked to own stage 5: a separate vendored package repository, with packages-portal-commons the nearest precedent. Valle Armonia hands over verified code, fixtures and adapter contracts at stage 4 and asks for agreement before VA-WEBSITE-SANC-008 is readied.

**Query:** Should Knowledge Islands agree now to take stage 5?

**Options:**

a) (recommended, confidence medium, review disagrees - Knowledge Islands decides Project and repository when there is something to receive) Agree now, and set its Project and repository at the stage 4 handover.

b) Agree in principle, with Knowledge Islands reviewing the adapter contracts and fixture shape before stage 4 starts; the blind reviewer prefers this at medium, to check the portability boundary before extraction hardens it.

c) Decline for now; Valle Armonia keeps the Sanctuary.

### BASELINE - one baseline for every Capital

focus: aside

**Context:** The eight Capitals share 21 core skills but differ on `ki-work-roadmap`, `ki-work-recurring`, Paperclip, acquisition skills, configuration and `AGENTS.md` shape ([skills-assessment.report.md](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.sop.main/_emerging/skills-assessment.report.md)).

**Query:** Should one baseline become the standard for every Capital?

**Options:**

a) (recommended, confidence high - reviewed: a common minimum with conditional capabilities, keeping local integration settings and receiver-led adoption) Adopt the baseline, record it in `ki-repo-kb-principal`'s standard through ki.prj.ways-of-working, and message each territory's State of play to conform its own Capital.

b) Adopt only the skill list now.

c) Leave each Capital as it is and fix only broken links.

### HARNESS-LINK - list each territory harness in its Capital

focus: aside

**Context:** Every territory harness adds a `<code>-extract-capability` skill, and hnr two engineering-convention skills, but all eight Capitals list only the KI harness in `[repo].harnesses`, so those skills reach no Capital.

**Query:** Should each Capital list its own territory harness alongside the KI harness?

**Options:**

a) (recommended, confidence high - reviewed: the extraction skills are invocation-only and protect source ownership, so linking grants no cross-repository authority) Add `<territory>/<code>-agentic-harness` to each Capital's `[repo].harnesses`.

b) Leave territory harnesses linked to their code repositories only.

### GRANOLA - declare Granola acquisition where it runs

focus: aside

**Context:** `ki-acquire-granola` is linked in six Capitals without being declared. hnr keeps a local `granola-sync` command; the blind review found legal's command and activity already retire direct import in favour of central acquisition, so the duplication claim is outdated for legal.

**Query:** How should Capitals that acquire from Granola carry the skill?

**Options:**

a) (recommended, confidence medium, review partly disagrees - one consistent declaration) Declare `ki-acquire-granola` in ki, hnr, er, legal, personal and va, and retire the local commands once their routing is in the skill's configuration.

b) Declare it only where capture actually runs, keep central capture with local reconciliation, and retire a local importer only after its routing is verified; the blind reviewer proposes this at high.

c) Unlink it where no acquisition happens and keep the local commands.

### LEGAL-GUIDANCE - legal's mandates into AGENTS.md

focus: aside

**Context:** Legal's `CLAUDE.md` holds 262 lines including its runtime-neutral case mandates (triple-check, adversarial stress-test, authority verification, pre-filing disciplines); its `AGENTS.md` only points to them, and Codex does not read `CLAUDE.md`. Legal work is high-stakes.

**Query:** Should legal move its mandates into `AGENTS.md` and promote its disciplines into harness skills?

**Options:**

a) (recommended, confidence high - reviewed: shared obligations belong in the shared entry point, and planned skills can verify the repeatable disciplines) Move the mandates table to `AGENTS.md` now and raise a record to promote the disciplines and commands into `legal-agentic-harness` skills.

b) Move the mandates only.

c) Leave legal unchanged.

### HNR-GUIDANCE - rewrite hnr's AGENTS.md

focus: aside

**Context:** hnr's `AGENTS.md` is out of shape against the Capital baseline and carries a stale Headroom block ([skills-assessment.report.md](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.sop.main/_emerging/skills-assessment.report.md)).

**Query:** Should hnr rewrite it?

**Options:**

a) (recommended, confidence high - a mechanical correction inside hnr's own authority) Message HNR's State of play to rewrite its `AGENTS.md` and drop the stale block.

b) Leave it until BASELINE is settled.

### THEME-REGISTRY - territory theme registries

focus: themes

**Context:** tmx, si and legal follow their own theme records; er has none.

**Query:** Should er be asked to capture one?

**Options:**

a) (recommended, confidence high - brings the last Capital into line with THEME-REGISTRY-ENFORCE) tmx, si and legal follow their own records, and er's State of play is asked by message to capture one.

b) Leave er without a theme registry.

### PRE-REBASE-REF - the harness safety branch on terra

focus: aside

**Context:** fold-harness left a local safety branch `fold-harness/pre-rebase-main` in ki-agentic-harness on terra, pointing at the old harness main `57226cdea`. Harness main is pushed and level with origin; the branch exists on terra only and cannot be inspected from Sol.

**Query:** Should the safety branch be deleted?

**Options:**

a) (recommended, confidence high - reviewed: level main does not prove the old reference holds nothing unique, so the deletion waits on a check at terra) Delete it with `git branch -D` on terra after confirming `57226cdea`'s content is reachable from main or not needed.

b) Keep it as a recovery reference.

c) Delete it on terra now.
