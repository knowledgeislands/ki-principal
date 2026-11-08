# KI > Techne > Agora › package-plan

**🤖 → 👤 Handoff to supervisor · Run report at 23:26 GMT · last mark 00:04 GMT**

---

## New and noteworthy

- The package carries eleven hours of built work that the roadmap does not: of the thirty-odd candidates left in tonight's run reports, none is a record, and no roadmap area covers Atlas, the MCP or Lantern. The proposal captures nineteen records in three new areas and marks fourteen things as already done.
- Nothing is obsolete in the eight existing records, but two have waited for acceptance since 3 November (KI-AGORA-TRY-001 and KI-AGORA-NET-001), and both Macs run a build seventeen hours behind `main`; the install of the renamed apps is the step most other steps wait on.
- Two owed replies have no decision left to take: the Legal reply drafted in the wake-map report, and the note to personal.reg.inbox-sol that the wake architecture landed.
- Runs atlas-nav, guilds-table and docs-tidy were still going as this was written; the coordinator should take their reports before applying the tidy.

## Done

- The proposal is in [package-plan.package.md](/Users/krisbrown/.local/state/ki/agents/ki-prj-agora/package-plan.package.md): Part 1 the package tidy (a proposed `state.md` body, `work.md` corrections including the warden role, the decisions to strike or reduce to pointers, the discussions to strike, keep and add, the `_emerging` dispositions, the messages to take or prune); Part 2 the roadmap (each record's real status with evidence, what is done but uncaptured, nineteen records to capture with ids, goals, sources, sizes, priorities and proposed horizons, and what is a message rather than a record); Part 3 the sequenced plan with dependencies and what needs Kris first; Part 4 the nine queries below.
- Read only: no file changed in any repository, nothing committed, no agent started, no remote call.

## In Progress

- Nothing is running in this run.

## Queries

### RECORDS-ADOPT - Capture the records and adopt the Now ones

**Context:** Tonight's runs left about thirty candidates in their reports and none in the roadmap, as their briefs required. Part 2.3 of the proposal merges them into nineteen records in three new areas, `ATL` (Atlas), `MCP` (the MCP and store) and `LAN` (Lantern), each with a proposed horizon; the existing five areas do not name the viewer, the MCP or the phone. Capture to triage is within the coordinator's gate because Kris asked for the work; adopting a record to a horizon needs Kris's word.

**Query:** May the coordinator capture the nineteen records with the three new areas, and adopt KI-AGORA-ATL-002, NET-004, MCP-001 and MCP-002 to Now and the rest as the table proposes?

**Options:**

a) (recommended, confidence medium - the list follows Kris's own asks tonight and the capture rule, while the area names and horizons are the coordinator's judgement) Yes, as Part 2.3 proposes, areas included.

b) Capture all nineteen to triage with the new areas, and adopt nothing until the decisions sitting.

c) Capture only the Now four and leave the rest as ideas in the Project note.

### FOCUS-SHAPE - The package's focus list

**Context:** The current focus list (send ⭐, jobs, voice, identity, kiv, _emerging) predates tonight: the KIV send side is done by embedding, Atlas is where most work now goes, the MCP is a new line, and the voice bard path has had no work or record since 3 November. Part 1.2 proposes atlas ⭐, mcp, beacon, jobs, identity, kiv and _emerging, with voice moved to _emerging.

**Query:** Is the proposed focus list right, and is Atlas the primary focus?

**Options:**

a) (recommended, confidence medium - it matches where the runs and Kris's asks have gone since 20:00 GMT, though the MCP may be primary once its decisions are taken) Adopt the seven as proposed, Atlas primary.

b) The same seven with `mcp` primary.

c) Keep `send` as the name of focus 3 and keep `voice` as a focus.

### MCP-GO - Build the Agora MCP and run its pilot

**Context:** The MCP spec (`38321ba`) is written and nothing is built. Its eleven questions are open; the first, whether Beacon may commit and push `krisb/ki-agora-beacon` under `store/` only, add-only and fast-forward only, narrows "Agora never commits". Building KI-AGORA-MCP-001 needs that answer plus the store layout (Q2) and the server's home (Q10); the other eight can be taken as drafted and revisited in use.

**Query:** Should KI-AGORA-MCP-001 and the pilot KI-AGORA-MCP-002 go to Now, with Q1, Q2 and Q10 answered first and the rest taken as drafted?

**Options:**

a) (recommended, confidence medium - it is the fix for the evening's missed questions and the drafted choices follow Kris's 22:35 design, but the Beacon-commits narrowing is Kris's to grant) Yes: answer Q1, Q2 and Q10 now, take the rest as drafted, build MCP-001 then run the pilot.

b) Hold both until all eleven questions and the walkthrough's sixteen are settled in one sitting.

c) Build only the one-shot command and the repository store with the owner committing by hand, and decide the store writer after the pilot.

### ENTRANCE-VS-MCP - The protocol's entrance against the MCP

**Context:** The protocol draft of 04:08 GMT specified a local entrance (a socket with join, leave, say, acknowledge and roll call) and asked for Kris's review before building it. Kris's 22:35 MCP design puts the same verbs behind MCP tools over interchangeable stores. Building both would be two entrances.

**Query:** Does the MCP replace the protocol's entrance, leaving the protocol spec to Beacon-to-Beacon traffic between Macs?

**Options:**

a) (recommended, confidence medium - one entrance is simpler and the MCP is the later, fuller design, though the protocol's presence and meeting-log sections still need a home) Yes: the MCP is the entrance; the protocol spec keeps presence, the meeting log and the portal traffic, aligned by KI-AGORA-MCP-005.

b) Keep both: the socket entrance for local agents and the MCP as a face over it.

### DOORBELL-END - When the old `doorbell/` path stops

**Context:** Every call is written to both `call/` and the old `doorbell/`, and the README still names 20 November. Kris said on 6 November (FAST-MOVE) that legacy support should last hours, not weeks. On sol only ki.reg.guilds waits on `call/`; four threads' files sit under `doorbell/`, though their health ACKs say they re-arm on both paths. terra's threads have not been checked.

**Query:** When should Agora stop writing `doorbell/`?

**Options:**

a) (recommended, confidence medium - it follows FAST-MOVE and the ACKs show the sol threads already wait on both, but terra's threads are unverified) With the first install after the Atlas runs land, after one health line tells every watched thread and each ACK names `call/`; any thread that does not answer is named to Kris before the switch.

b) Now, in the next release, telling the threads by broadcast afterwards.

c) On 20 November as the README says.

### KIV-WRITE - The KIV's one write, now that it is Agora's

**Context:** Agora's spec and `AGENTS.md` say Agora never edits knowledge. The KIV, which Agora now owns and embeds, has one write: deferring an action card changes its due date and adds a line, without committing. The embedded Actions tab still allows it. KI-AGORA-ATL-007, the code move, needs this settled.

**Query:** Should the KIV keep its defer action?

**Options:**

a) (recommended, confidence medium - it is a deliberate click of Kris's, commits nothing, and removing it loses a working feature) Keep it as the one named exception, written into the boundary.

b) Turn deferring off in the embedded KIV so it only reads.

c) Leave deferring to an inbox-owned tool and drop it from the KIV when its code moves.

### PING - Ping's sending side

**Context:** Since the tray was slimmed, nothing sends a ping; `ping()` and its text have no caller, and the spec's goal 4 still names Ping among what reaches every agent from one action. Claude Design's Lantern screen gives the phone one brass action, "Ping everyone". Answers and acknowledgements stay either way, because a mark takes the ping's path.

**Query:** Should Ping be removed, or added to Atlas and Lantern?

**Options:**

a) (recommended, confidence medium - the Lantern design wants it and it is the lightest "are you there" from a phone, but it adds a verb to Beacon's door) Add a `ping` verb to Beacon's door with a button in Atlas's toolbar and Lantern's one action.

b) Remove the sending side and reword goal 4 to Broadcast, Away, I'm back and Mark.

### UPDATE-PATH - What Check for Updates does

**Context:** Check for Updates compares the installed build with `origin/main` and shows the install command with a Copy button; Agora installs nothing, and the households install under AGORA-INSTALL-GRANT. Every new build waits for a household's turn, and the installed apps on both Macs are seventeen hours behind `main`.

**Query:** When a newer Agora is available, what should a click do?

**Options:**

a) (recommended, confidence medium - it keeps Kris in control of each install and removes the wait, but it narrows "Agora installs nothing" to "only at Kris's click") Run `bun run self:install` from the source checkout at Kris's click, after showing what will change.

b) Send the household a message asking for the install, and show that it was sent.

c) Keep showing the command only.

### ACCEPT - Two records for acceptance

**Context:** [KI-AGORA-TRY-001](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/KI-AGORA-TRY-001-menu-bar-identity.md), the menu-bar identity, has awaited review since 3 November; its tray has since been calmed, given Orca's menu and renamed, with `docs/design/identity.md` kept current, so the review is of today's tray on both Macs. [KI-AGORA-NET-001](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/KI-AGORA-NET-001-observatory-read-endpoint.md), the read endpoint, was built on 3 November while still in triage and is what Atlas, Lantern and the Observatory read.

**Query:** Should both be accepted as done, with NET-001 adopted and closed in one step?

**Options:**

a) (recommended, confidence medium - both are in daily use on both Macs, but Kris has not yet seen the renamed tray, which the next install brings) Accept NET-001 now, and TRY-001 after Kris has seen the renamed tray on the next install.

b) Accept both now.

c) Keep TRY-001 open until Lantern and the badges land, and accept NET-001 now.

🧵 ki.prj.agora
