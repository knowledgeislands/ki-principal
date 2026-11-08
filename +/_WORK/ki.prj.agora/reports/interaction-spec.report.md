# [KI > Techne > Agora](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.agora/work.md) › interaction-spec

**🤖 → 👤 Handoff to supervisor · Run report at 05:01 GMT · last mark 00:04 GMT**

---

## Done

- **The agent interaction specification.** It is written at [docs/spec/agent-interaction.md](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/spec/agent-interaction.md) as an RFC-style draft using the BCP 14 keywords. It opens with a short plain-English summary for Kris, then covers:
  - **Harness profiles** for seven surfaces: Claude Code in an Orca chat and in an Orca terminal, Codex in Orca, Codex in the ChatGPT desktop app, Claude Desktop, Claude Design and other cloud sessions, and background `ki agent` runs. Each profile says whether the surface can listen, whether and how it can be woken, whether it can reach sol's files, what it must do to stay reachable, and the latency measured tonight.
  - **The mailbox model.** One writer per direction, ids, and acknowledgements tracked by id. It also covers watching for changes with a scan as fallback, combining several messages into one wake, retries that never repeat work, pruning, and the coordinator as the only committer.
  - **The Agora Portal as the meeting point,** set as the target, with mailboxes as today's fallback.
  - **Keeping awake:** listeners, health pings, ALIVE and STILL-HERE heartbeats with their acknowledgements, and how a coordinator keeps itself awake.
  - **Seven open items** (O1 to O7), each with an owner.
  - **Tonight's timings** in an appendix.
- **Links.** The Agora protocol now links to the new specification in three places: its status paragraph, its delivery-routes section and its references. The new specification links back to the protocol throughout. The README now names it.
- **Commits.** apps-agora.local `1855d30`, pushed. ki-principal `a89167f0` adds one line under "Built tonight" in [agora-plan.md](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.agora/_emerging/agora-plan.md), pushed.
- **Checks.** `bun run self:check` and `bun run test` both failed in the shared checkout. The failures come from another session's unfinished, uncommitted edits to `src/` (`wording.ts`, `menu.ts`, `main.ts` and the new `open.ts`), which I left alone. I ran both checks again on a clean copy of `HEAD` with my three documents added, and both passed: 31 test files, 340 tests. The ki-principal commit passed its pre-commit gate.

Choices I made:

- **Doers' working words.** The spec writes down how the doers work today as rules. A doer writes only its own Outbound (CD-1), so the first briefs' "reply in ki.prj.agora's Inbound" is recorded as replaced. Messages are tracked by id, not by line count, as the illustrator suggested in GAME-2385-IMPROVE.
- **Two additions to the Portal, beyond the protocol draft.**
  - A **file drop** (`$STATE/drop/<work-id>/<id>.json`). Claude Design reaches sol only through short bridge calls, so it cannot use a socket entrance.
  - A **cursor file** next to each inbox note, plus a `GET /v1/inbox?after=<id>&wait=` read. A polling agent can check one small file or make one cheap call.

  I also added acknowledgement of several ids at once, and doer seats named `<coordinator>.<focus>` as DOER-PACKAGES names them.
- **Mailbox file layout.** I specified one file with two parts, each written only by its own side and replaced whole on each write, as today. I recorded splitting it into two files as open item O5 rather than requiring it now.
- **Which layer carries what.** Under TWO-LAYERS, briefs and their acknowledgements stay in the committed mailbox. Games, tests and heartbeats move to the Portal once it exists.
- **Background runs.** I profiled their wake route as `ki agent send`, read at the run's next status. I took this from `ki agent send --help`; it was not measured tonight.

## In Progress

Nothing. Roadmap record candidates for the open items (none created):

- Agora watches local writes to watched packages and doer mailboxes (O4, DOER-WATCH).
- Split each doer mailbox into one file per direction when doers get sub-packages (O5, DOER-PACKAGES).
- The Portal's file drop, per-agent queues, cursor file and `GET /v1/inbox` read (Section 5.3), built with the entrance.
- Verify whether `SendMessage` reaches a Claude Design session (O3).

## Queries

### Q1 - A shared Codex daemon on sol

**Context:** Codex in the ChatGPT desktop app hears only while it holds its turn open. `codex queue --resume` needs a shared Codex daemon, and none runs on sol: the ChatGPT app keeps its chat to its own process. Without one, nothing can wake the illustrator once its turn ends. This is open item O1 in the specification, already listed as "Next, with Kris" under ILLUSTRATOR-LINK.

**Query:** Should a shared Codex daemon run on sol, with Codex doers opened through it so that a queued nudge can wake them?

**Options:**

a) (recommended, confidence medium - it is the only route found that wakes a Codex chat from outside, and it starts no new agent) Pilot it on sol with one test Codex session, then move the illustrator over if it wakes cleanly.

b) Keep the illustrator's own listening loop as the only route, and accept that the illustrator goes silent when its turn ends.

c) Run Codex doers only in Orca terminals, where Agora's terminal send already wakes them.

## New and noteworthy

- One specification now says how each tool you use is reached by the others. It covers Claude Code, Codex, ChatGPT's Codex, Claude Desktop, Claude Design and background runs, with tonight's timings: about 8 to 10 seconds a round for the illustrator, and its own check interval for Claude Design.
- It records the working rules from tonight's ping-pong and word games: one writer per direction, messages tracked by id, and the coordinator as the only committer. Any new doer can be set up the same way.
- It sets the Agora Portal as the meeting point where agents cannot reach each other. It also lists what the Portal still needs before agents can stop reading each other's files, ready for your morning review of the protocol.

🧵 ki.prj.agora
