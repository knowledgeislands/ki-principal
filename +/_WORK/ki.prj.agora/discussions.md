# ki.prj.agora discussions

## Open

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

### FOCUS-FIT - Agora waking workers within the Techne focus

focus: _emerging · since 2026-11-03 · from ki.sop.main FOCUS-FIT

**Context:** Agora sits under theme Techne beside ki.prj.agent-host. The [Techne Programme Focus](/Users/krisbrown/kis/knowledge-islands/ki-principal/Admin/Governance/Policies/Techne%20Programme%20Focus.md) lets agents run on sol and vega "only in sessions the binding owner opens, no unattended or scheduled agents". [KI-AGORA-WRK-001](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/KI-AGORA-WRK-001-wake-workers.md) has Agora start or steer runs through `ki agent`, which an always-on app would do without a session you opened.

**Query:** How does Agora waking workers fit the Techne focus?

**Options:**

a) (recommended, confidence high - a blind review chose the same course, and it keeps the policy as it stands) Agora may wake threads and runs you opened; starting fresh runs from standing briefs waits for your decision through the Enactment Process.

b) Amend the Techne Programme Focus through the Enactment Process to allow Agora-started runs on sol and vega within named bounds.

c) Park KI-AGORA-WRK-001 until the agent-host work settles.

### AGORA-COUNT-PLACE - Where the group count goes when the identity design lands

focus: identity · since 2026-11-03 · from assistant-sol ([discussions](https://github.com/krisb/assistant/blob/5f2655d9/%2B/_WORK/personal.reg.assistant-sol/discussions.md))

**Context:** Claude Design's identity branch (`design/agora-identity`, [KI-AGORA-TRY-001](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/KI-AGORA-TRY-001-menu-bar-identity.md)) swaps the text title for a symbol plus a count of things needing a look, so the new `Agora 2/2` text would disappear.

**Query:** Where should the members-present count appear once the identity work is merged?

**Options:**

a) (recommended, confidence medium - keeps the design's quiet icon and still answers "how many of us are here" at a glance) Icon-only title; the menu's first line reads, for example, "2 of 2 in Agora".

b) Keep `2/2` beside the symbol as well as the look count.

c) Drop the count and rely on the symbol's states.

## Parked

None
