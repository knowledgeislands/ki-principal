# ki.prj.agora discussions

## Open

Since 8 November 2026 the working copy of every open query is the questions file Kris works through with the chat agent: `krisb/inbox` `+/_WORK/personal.reg.inbox-sputnik/agora/2026-11-08-from-ki.prj.agora-open-questions.md`. It holds the 15 queries below and adds AGORA-REMIT, VOICE-SCOPE, ORCA-SERVERS-HOME, ROSTER-FILL, ATLAS-ROLE, INBOX-SEATS, PACKAGE-HOME and SCHED-PARK. One query is held here only: STAGED-REPORTS, whether the reports other sessions staged in ki-principal (ki.prj.agora, ki.prj.ways-of-working, ki.sop.main) are left for their owners (recommended, medium confidence) or committed by this package. Answers come back as a message line in this package's Inbound; fold each into `decisions.md` and strike it here and in that file.

### SCHED-FIRST - Which jobs move to Agora first

focus: jobs · since 2026-11-06 · from scheduler-draft

**Context:** Four of today's jobs make no model call and run on both Macs: the morning check, log rotation, workstation health and the Rig update. Five jobs start an agent: Route Triage, the three switched-off jobs and the territory dispatcher. Those cannot move until FOCUS-FIT is settled.

**Query:** Which jobs should Agora take over first?

**Options:**

a) (recommended, confidence high - lowest risk, and proves the reporting before anything that matters depends on it) The four model-free jobs on both Macs, one at a time, each with its launchd job kept as a tested way back. terra's model-free jobs and the checkout refresh follow, and agent jobs come last.

b) Route Triage first, since its silent failure is what started this, once FOCUS-FIT allows it.

c) All of today's enabled jobs at once, when the tools-rig engine lands.

### SCHED-REPORT - How a failure or missed run reaches you

focus: jobs · since 2026-11-06 · from scheduler-draft

**Context:** The Observatory already showed both silent failures, but nobody was looking at it. You asked for failures and missed runs to be reported the same day.

**Query:** Where should a failed or missed run be reported?

**Options:**

a) (recommended, confidence medium - it reaches someone without being looked for and reuses Agora's existing doorbells, though each job then needs a named owner) Record it in Agora's state for the Observatory, and on the same day ring the doorbell of the package that owns the job, with a marker in the tray until it clears.

b) Tray marker and Observatory only.

c) A daily summary line in the morning report only.

### SCHED-PAUSED - How a paused job is declared

focus: jobs · since 2026-11-06 · from scheduler-draft

**Context:** The WhatsApp spool refresh has been paused at your word since 3 November, but its declaration still reads enabled, so it keeps running and failing every day.

**Query:** How should a paused job be declared?

**Options:**

a) (recommended, confidence medium - it uses Rig's existing vocabulary and needs no new engine work) Declare it disabled, with a rationale naming your word and its date. Agora reports it as off, not failing.

b) Rig gains a paused state carrying a reason and a review date, which Agora shows as paused.

c) Leave it enabled and have Agora stop reporting its failures.

### SCHED-ONE-RIG - Jobs that must run on exactly one Mac

focus: jobs · since 2026-11-06 · from scheduler-draft

**Context:** Route Triage and the legal jobs run only on terra today, through Rig's laptop profile, so that only one Mac sorts mail or commits a log. Run-once claims across the group belong to KI-AGORA-WRK-001.

**Query:** How should Agora keep such a job to one Mac?

**Options:**

a) (recommended, confidence high - it works now and leaves failover for later) Keep Rig's host selection for now, and add run-once claims with KI-AGORA-WRK-001 later so another Mac can take over safely.

b) Wait for run-once claims before moving any one-Mac job.

### MARK-WORDS - Whether a mark carries your own words

focus: send · since 2026-11-06 · from mark-all-scope

**Context:** `away` and `ping` broadcasts use fixed wording, while **Broadcast…** carries free text. Free text inside a mark could blur what the instruction is.

**Query:** Should a mark carry your own words as well as its two options (`only` and `no art`)?

**Options:**

a) (recommended, confidence medium - fixed words keep the instruction plain, and you can send words with **Broadcast…** straight after) Fixed words and the two options only.

b) An optional note typed in a small window, added after the fixed words.

### ORCA-WATCH - Watch the Orca chat-send work for you

focus: send · since 2026-11-05 · from ORCA-UPSTREAM

**Context:** Waking Orca chats ([KI-AGORA-WRK-001](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/KI-AGORA-WRK-001-wake-workers.md)) waits on Orca's pull request #33115, which adds `orca chat send`. It is still unmerged, last updated 2 November. Its issue, #33114, is active, with a new comment from another user at 20:57 GMT today. Nothing tells us when either one moves.

**Query:** Should something watch the issue and pull request, read-only, and tell you when there's a new reply, a merge or a release?

**Options:**

a) (recommended, confidence medium - it's read-only and cheap, and it's how we'll know when Orca chats can be woken) Yes: Agora checks both on its review interval with read-only GitHub calls and puts any change in the tray and in this package.

b) Yes, but as one of the rig's scheduled housekeeping jobs rather than inside Agora.

c) No: check by hand now and then.

### CONFIG-OWNER - Who owns Agora's settings file

focus: \_emerging · since 2026-11-04 · from personal.reg.household-sol AGORA-HANDOFF

**Context:** The Rig install plan has chezmoi write Agora's settings file, `~/.config/agora/config.toml`. Your settings-screen ideas (the permissions check and the switchable tree of territories and repositories) mean the app would write the same file. If both write it, chezmoi would undo your changes from the screen at its next apply.

**Query:** Who should own the settings file once a settings screen exists?

**Options:**

a) (recommended, confidence medium - avoids the two fighting over one file, and keeps a fresh rig set up with no clicks) chezmoi writes first-run defaults only; after that the app owns the file.

b) chezmoi owns the file, and the settings screen only shows settings without changing them.

c) Split it: chezmoi owns a base file and the app writes its own overrides beside it.

### AGORA-START - What follows the mark broadcast

focus: _emerging · since 2026-11-03 · opening

**Context:** The hand-over brings four focus lines and three triage records ([KI-AGORA-APP-001](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/KI-AGORA-APP-001-package-and-relaunch.md) package and relaunch, [KI-AGORA-NET-001](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/KI-AGORA-NET-001-observatory-read-endpoint.md) Observatory read endpoint, [KI-AGORA-WRK-001](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/KI-AGORA-WRK-001-wake-workers.md) wake workers). KIV-SEND has a waiting consumer, assistant-terra.kiv's KIV-ELECTRON. Nothing is running.

**Query:** Once the mark broadcast (MARK-ALL) is done, what should come next?

**Options:**

a) (recommended, confidence medium - the only line another thread is blocked on) Plan and build KIV-SEND, Agora's send side for the KIV Electron app, capturing it as a record first.

b) Plan KI-AGORA-APP-001, package and relaunch, so every later slice ships through a packaged app.

c) Start ORCA-WAKE, waking Orca chat threads (Orca #33114).

### AGORA-COUNT-PLACE - Where the group count goes when the identity design lands

focus: identity · since 2026-11-03 · from assistant-sol ([discussions](https://github.com/krisb/assistant/blob/5f2655d9/%2B/_WORK/personal.reg.assistant-sol/discussions.md))

**Context:** Claude Design's identity branch (`design/agora-identity`, [KI-AGORA-TRY-001](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/KI-AGORA-TRY-001-menu-bar-identity.md)) swaps the text title for a symbol plus a count of things needing a look, so the new `Agora 2/2` text would disappear.

**Query:** Where should the members-present count appear once the identity work is merged?

**Options:**

a) (recommended, confidence medium - keeps the design's quiet icon and still answers "how many of us are here" at a glance) Icon-only title; the menu's first line reads, for example, "2 of 2 in Agora".

b) Keep `2/2` beside the symbol as well as the look count.

c) Drop the count and rely on the symbol's states.

### STORE-CODE - The store's repository code

focus: mcp · since 2026-11-07 · from store-docs

**Context:** `ki-agora-beacon`'s `.ki.toml` still has `repo_code = "PERSONAL-PORTAL"`, the last portal name on the store.

**Query:** Should the code be renamed?

**Options:**

a) (recommended, confidence medium - nothing in it is published yet) Rename it to `PERSONAL-AGORA-STORE` in a small run, after checking nothing else refers to it.

b) Keep it.

### TRY-NOTICES - Repeating checkout notices

focus: beacon · since 2026-11-07 · from review-packets

**Context:** The Beacon announces a checkout again each time its state changes (`ki-principal` 20 times in 36 minutes on sol). The identity document says a thing is announced once, and again only if it settles and comes back.

**Query:** Should a checkout be announced only once until it is level and clean again?

**Options:**

a) (recommended, confidence medium - matches the agreed design and stops the noise) Yes: capture it as a fix before accepting KI-AGORA-TRY-001.

b) No: accept today's behaviour and note it in the record.

### NET-ADOPT - Adopt and rename the read endpoint

focus: beacon · since 2026-11-07 · from review-packets

**Context:** KI-AGORA-NET-001 is built and every live check passes on both Macs, but it is still in triage. Its title names the Observatory, which does not read it yet; the Atlas and the KIV do.

**Query:** Should it be adopted with the Atlas and KIV as its viewers, so it can go to review?

**Options:**

a) (recommended, confidence medium - the build meets the goal for its real users) Yes: adopt it, retitle it the Agora read endpoint, and leave the Observatory's reading as a later record.

b) Adopt it as it stands, open until the Observatory reads it.

### WAKE-PROVE - Prove the wake line into a live agent

focus: wake · since 2026-11-07 · from wake-note

**Context:** The Orca wake route is built and proven into a shell, never into a live agent thread. Legal has been told it is unproven (MSG-6d1b06d6). It can be proven over SSH, with no screen.

**Query:** Will you open one test Claude thread in an Orca terminal so the first real wake can be watched?

**Options:**

a) (recommended, confidence high - it is the one missing proof and needs only a terminal) Yes: open one; the coordinator registers it and watches the first wake.

b) Not yet: Legal stays told it is unproven.

### MOUNT-5 - Notice for household-terra

focus: mount · since 2026-11-07 · from terra-mount

**Context:** The terra-mount brief named a household-terra mailbox path that does not exist; household mailboxes live in the chezmoi repository. household-terra already ACKed Legal at 13:49 GMT.

**Query:** Should anything more be sent to household-terra about the terra mount?

**Options:**

a) (recommended, confidence medium - its ACK to Legal shows it already has the change) No: send nothing more.

b) Send a short notice to its chezmoi mailbox.

### WAKE-MAP-FOLD - Fold the wake map into the wake architecture note

focus: wake · since 2026-11-07 · from wake-note

**Context:** `docs/design/wake-map.md` (6 November) overlaps the new `docs/design/wake-architecture.md`.

**Query:** Should the wake map be folded into the new note and removed?

**Options:**

a) (recommended, confidence medium - one note avoids drift, but the map may hold detail worth checking first) Yes: a run folds it in and removes it.

b) Keep both, each linking the other.

## Parked

None
