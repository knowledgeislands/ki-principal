# ki.prj.agora discussions

## Open

### AGORA-START - Which Agora work starts first

focus: _emerging · since 2026-11-03 · opening

**Context:** The hand-over brings four focus lines and three triage records ([KI-AGORA-APP-001](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/KI-AGORA-APP-001-package-and-relaunch.md) package and relaunch, [KI-AGORA-NET-001](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/KI-AGORA-NET-001-observatory-read-endpoint.md) Observatory read endpoint, [KI-AGORA-WRK-001](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/KI-AGORA-WRK-001-wake-workers.md) wake workers). KIV-SEND has a waiting consumer, assistant-terra.kiv's KIV-ELECTRON. Nothing is running.

**Query:** What should the first run be?

**Options:**

a) (recommended, confidence medium - the only line another thread is blocked on) Plan and build KIV-SEND, Agora's send side for the KIV Electron app, capturing it as a record first.

b) Plan KI-AGORA-APP-001, package and relaunch, so every later slice ships through a packaged app.

c) Start ORCA-WAKE, waking Orca chat threads (Orca #33114).

### FOCUS-FIT - Agora waking workers within the Techne focus

focus: _emerging · since 2026-11-03 · from ki.sop.main FOCUS-FIT

**Context:** Agora sits under theme Techne beside ki.prj.agent-host. The [Techne Programme Focus](/Users/krisbrown/kis/knowledge-islands/ki-principal/Admin/Governance/Policies/Techne%20Programme%20Focus.md) lets agents run on sol and vega "only in sessions the binding owner opens, no unattended or scheduled agents". [KI-AGORA-WRK-001](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/KI-AGORA-WRK-001-wake-workers.md) has Agora start or steer runs through `ki agent`, which an always-on app would do without a session you opened.

**Query:** How does Agora waking workers fit the Techne focus?

**Options:**

a) (recommended, confidence medium - keeps the policy as it stands and still lets slices land) Agora only wakes or steers runs inside a session you opened, such as a thread's own run queue; anything that starts a run on its own waits for a policy change through the Enactment Process.

b) Amend the Techne Programme Focus through the Enactment Process to allow Agora-started runs on sol and vega within named bounds.

c) Park KI-AGORA-WRK-001 until the agent-host work settles.

### BCAST-THREADS - Teaching threads to read broadcasts

focus: send · since 2026-11-03 · from assistant-sol ([discussions](https://github.com/krisb/assistant/blob/5f2655d9/%2B/_WORK/personal.reg.assistant-sol/discussions.md))

**Context:** Agora delivers broadcasts, but a thread only acts on one if its listening loop reads the broadcast file at each doorbell wake and records an Away as an unattended window. The README and `AGENTS.md` say so; the `ki-coordination` method does not yet mention Agora broadcasts, so threads will not read the file.

**Query:** Should reading broadcasts be added to the coordinating method?

**Options:**

a) (recommended, confidence medium - reaches every thread through the one source they already re-read, and leaves Agora unchanged) Send ways-of-working a line to add it to `ki-coordination`: at each doorbell wake read the broadcast file, treat an `away` entry as an unattended window and `back` as the return.

b) Each thread reads the file only when the doorbell line starts `broadcast`. Simpler, but a news ring can overwrite a broadcast ring and the broadcast is missed.

c) Leave it in the README for now and add it to the method after you have tried a broadcast.

### BCAST-AUTHORITY - What an Away grants

focus: send · since 2026-11-03 · from assistant-sol ([discussions](https://github.com/krisb/assistant/blob/5f2655d9/%2B/_WORK/personal.reg.assistant-sol/discussions.md))

**Context:** As you asked, an Away broadcast says only "within your existing authority". Under `ki-coordination` an unattended window is opened by a grant recorded in the decisions log. A thread could read your Away words as that grant, limited to its existing authority, or only notice you are away.

**Query:** Should a thread treat an Away broadcast as opening an unattended window on its own, or only notice it?

**Options:**

a) (recommended, confidence medium - matches "do as much as you can" while keeping each thread inside what it is already allowed to do) Opening a window: the thread records the grant and end time in its decisions log, works within its existing authority, and gives a return report at the end or when you are back.

b) Only notice: threads keep working as they would and write a return report without opening a window.

### AGORA-COUNT-PLACE - Where the group count goes when the identity design lands

focus: identity · since 2026-11-03 · from assistant-sol ([discussions](https://github.com/krisb/assistant/blob/5f2655d9/%2B/_WORK/personal.reg.assistant-sol/discussions.md))

**Context:** Claude Design's identity branch (`design/agora-identity`, [KI-AGORA-TRY-001](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/KI-AGORA-TRY-001-menu-bar-identity.md)) swaps the text title for a symbol plus a count of things needing a look, so the new `Agora 2/2` text would disappear.

**Query:** Where should the members-present count appear once the identity work is merged?

**Options:**

a) (recommended, confidence medium - keeps the design's quiet icon and still answers "how many of us are here" at a glance) Icon-only title; the menu's first line reads, for example, "2 of 2 in Agora".

b) Keep `2/2` beside the symbol as well as the look count.

c) Drop the count and rely on the symbol's states.

### WORK-ID-TRAILER - A Work-Id trailer on a thread's own commits

focus: send · since 2026-11-03 · from assistant-sol ([discussions](https://github.com/krisb/assistant/blob/5f2655d9/%2B/_WORK/personal.reg.assistant-sol/discussions.md))

**Context:** Agora can skip ringing a thread for its own commits only if each commit names its work package. Ringing only on added lines already silences the common case.

**Query:** Should the house add a `Work-Id: <package>` trailer to commits a thread makes in its own work folder?

**Options:**

a) (recommended, confidence medium - the only reliable signal, at one line per commit) Yes: ask Ways of working, through ki.sop.main, to add it to `ki-coordination`'s commit rules.

b) Leave it optional and rely on ringing only on added lines.

## Parked

None
