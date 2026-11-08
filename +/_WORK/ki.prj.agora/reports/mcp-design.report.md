# KI > Techne > Agora › mcp-design

**🤖 → 👤 Handoff to supervisor · Run report at 22:56 GMT · last mark 00:04 GMT**

---

## New and noteworthy

- The Agora MCP and the beacon store now have an RFC-style specification, `docs/spec/agora-mcp.md` in apps-agora.local, written from Kris's design of 6 November (AGORA-MCP-DESIGN, BEACON-REPO) and from what went wrong that evening: ILL-24's two questions missed for 26 minutes behind the art it came with, the first briefs putting three writers in one file, a doer's line unheard for five minutes, and every message waiting behind its package's repository.
- The design's centre: one file per message, added and never edited, named by a time-ordered UUID, so two Macs never conflict; a message is `unread`, `read`, `acked` or `answered` per recipient, and a `question` or `brief` stays **open** until an `answer` names it, with `who()` showing what each agent owes and is owed; `wait` holds a turn with one blocking call instead of a shell loop; `since(ref)` returns everything after a Git commit ref, one linear checkpoint.
- One narrowing of "Agora never commits" is needed and is Q1 below: the Beacon acts for the watchman as the store writer, committing only add-only files under `store/` of `krisb/ki-agora-beacon`, fast-forward only.
- Roadmap candidates, not created: **the Agora MCP itself** (the server, the repository store, the one-shot command); **the pilot** (coordinator plus the two design doers over the tools, alongside the mailboxes, word-chain test then one real brief with a question each way, ILL-24 replayed as the acceptance case); and one record per migration step M1 to M8 (the doers, the work-package standard's Messages lines, the coordination method, the guilds and the binding inventory, the households' configuration and tokens, the watchman and the store writer, the enabler packages one at a time, retiring the old broadcast, ack and outbox paths).

## Done

- Read AGENTS.md, the three specifications, the walkthrough's AGORA-MCP, PORTAL-STORE and AHP-ADOPT, `door.ts`, `broadcast.ts`, `protocol.ts`, the ki-agora-beacon README and AGENTS.md (read only), the two doer mailboxes and the package's decisions log.
- Wrote `docs/spec/agora-mcp.md` (21 sections, three appendices): the message and its kinds, addresses and identity (one mount, one package; the owner as `owner`), the tools, the store contract, the four stores and which is right, the repository layout with territory folders, checkpoints, the four modes (stdio, tailnet HTTP on port 1679, cloud sessions, offline on one Mac), trust for local, tailnet and public mounts, territory boundaries with a recommendation, the mapping of Agora's call, `ring`, broadcasts and the outbox, pings, marks and the health tiers, presence words and kept checkouts, the mailbox as a view, the cloud route for Claude Design (three routes, the bridge recommended), the pilot, the migration table, security considerations and eleven open questions.
- Linked it from `docs/spec/agora.md` and the README. No code changed; no roadmap record created.
- Checks: `rumdl fmt` and `rumdl check` clean on the three files; `bun run self:check` passed (pre-existing Biome warnings only).
- Committed 38321ba by explicit path with `Work-Id: ki.prj.agora`, rebased on origin main and pushed fast-forward; the checkout is level with origin.

## In Progress

Nothing. The run is complete.

## Queries

### Q1 - May the Beacon commit to ki-agora-beacon?

**Context:** Kris's design has the Beacon write to the repository directly, and the specification makes the Beacon the store writer acting for the watchman. AGENTS.md and the Agora specification say Agora never commits or pushes. With one file per message named by its UUID, two Macs' commits never touch the same path, so replaying this Mac's unpublished add-only commits onto the remote head cannot meet a conflict ([spec Section 8.1.1](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/spec/agora-mcp.md)).

**Query:** may the Beacon commit and push to `krisb/ki-agora-beacon`, under `store/` only, add-only and fast-forward only, replaying its own add-only commits onto the remote head, as the one narrowing of "Agora never commits"?

**Options:**

a) (recommended, confidence high - the bound is small and checkable: one private repository, one folder, no edits, no merges, and a stop on any conflict; without it a message is not durable until a person commits it) Yes, under the five store-writer rules in the specification, and AGENTS.md says so.

b) One branch per Mac, so no replay is ever needed; the cost is two checkpoints for every reader and a record that is two histories rather than one.

c) The watchman stays a separate committer the Beacon only nudges; the cost is an agent and a delay before anything is durable, which is the failure the MCP is meant to fix.

### Q2 - One store or one per territory?

**Context:** the three-portal model has a message hop no further than it must, and each territory has a principal island. The checkpoint design wants one linear commit ref. Everything in the store today is Kris's own and private ([spec Section 13](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/spec/agora-mcp.md)).

**Query:** where do messages live?

**Options:**

a) (recommended, confidence medium - one commit ref gives one checkpoint and one history, the repository is private, and a folder per territory makes a later split a move with no change to any id or tool; medium because a territory shared with other people, such as HNR, would want its own store sooner) One store, `krisb/ki-agora-beacon`, with a folder per territory and a `planar` folder for what crosses territories or goes to everyone.

b) One store per territory in its principal repository, plus the planar store for what crosses; the model made literal, at the cost of a checkpoint per store and threads split across repositories.

c) One flat store with no folders; cheapest for the pilot, but a later split needs a pass over every file.

### Q3 - Read receipts in Git?

**Context:** a `read` receipt is one small file per message per reader, the chattiest thing in the store; `acked` and `answered` are rarer and matter more. The mailboxes today have no read state at all ([spec Section 9.2](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/spec/agora-mcp.md)).

**Query:** does the repository keep every `read` receipt, or only `acked` and `answered`?

**Options:**

a) (recommended, confidence medium - "has the other Mac even seen it" is the question the evening kept asking, and batching read receipts into the next commit keeps the cost to a few files a minute; medium because the store is add-only and the receipts are the one thing that grows fastest) Keep all three in the repository, batched; let configuration turn `read` off per Mac if it grows too fast.

b) Only `acked` and `answered` in the repository, with `read` in the live queue alone; unread on another Mac then means "not acknowledged or answered", as today.

### Q4 - The kinds and what needs a reply

**Context:** the specification sets six agent kinds, `brief`, `question`, `answer`, `art`, `ack` and `info`, plus the owner's `broadcast`, and makes `question` and `brief` need a reply by default so neither can vanish behind other work ([spec Section 4.2](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/spec/agora-mcp.md)).

**Query:** are the six right, and does a `brief` need a reply by default?

**Options:**

a) (recommended, confidence medium - a brief with no answer is exactly the silent handoff the evening produced, and a sender who wants only an acknowledgement can set it off) The six as drafted, with `question` and `brief` open by default.

b) The six, with only `question` open by default; a brief is closed by its `art` or an `ack`.

c) Fewer kinds: `say`, `question`, `answer` and `ack`, with art and briefs as tags.

### Q5 - Who may send a brief to whom

**Context:** the MCP carries messages and grants nothing; the coordination rules say who routes what. The specification lets any package send a brief to any package and leaves the recipient to judge authority ([spec Section 12.5](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/spec/agora-mcp.md)).

**Query:** does the MCP refuse a brief outside the routes the coordination rules allow, or carry it and let the recipient judge?

**Options:**

a) (recommended, confidence medium - the MCP would otherwise have to encode the coordination rules, which are personal.reg.inbox-sol's and change; a brief from a package with no authority is information under the recipient's rules) Carry it; the recipient judges, as today with a mailbox line.

b) Refuse it, with the allowed routes rendered into the MCP's configuration by the coordination method's owner.

### Q6 - Where a mark's Summary goes

**Context:** a mark arrives as a broadcast message; the agent strikes its mark and gives its Summary in its own conversation, which only the tool it runs in shows ([spec Section 14.4](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/spec/agora-mcp.md)).

**Query:** does the Summary stay in the agent's conversation, or come back as an `answer` to the mark so the Atlas shows every Summary in one place?

**Options:**

a) (recommended, confidence low - the Atlas showing every Summary at one mark is what Mark all is for, but it changes the reply form, which is the coordination method's, so it needs personal.reg.inbox-sol's agreement) As an `answer` to the mark, in addition to the conversation.

b) In the conversation only, as today; the store records only the acknowledgement.

### Q7 - The cloud route for the pilot

**Context:** Claude Design is not a tailnet node; it reaches sol through short bridge calls. Three routes are in the specification: its bridge running the one-shot command, a public mount through Tailscale Funnel with a token, or a cloud-hosted store ([spec Section 16](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/spec/agora-mcp.md)).

**Query:** which route does the pilot use?

**Options:**

a) (recommended, confidence medium - it is the route the session already uses for files, exposes nothing new, and a held `wait` inside one bridge call should give the same 7 to 10 second rounds; medium because a blocking command through the bridge was not measured) The bridge and the one-shot command.

b) Verify a Funnel mount with a per-identity token first, and use it if Claude Design can mount a custom remote MCP.

c) Wait for the cloud-hosted store.

### Q8 - The listening word for wait

**Context:** the footer's listening words are `agora-call`, `poll`, `on-open` and `off`, and they are personal.reg.inbox-sol's. An agent holding `wait` is listening through the MCP, and the Beacon still writes the call for it ([spec Section 14.5](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/spec/agora-mcp.md)).

**Query:** a new word, or the old one?

**Options:**

a) (recommended, confidence medium - it tells Kris at a glance which agents have moved, which matters during the migration) `agora-mcp`, proposed to personal.reg.inbox-sol.

b) Count it as `agora-call`, since the call is still written.

### Q9 - Whether join is required

**Context:** the specification keeps `join` and `leave` optional, with the entrance's `join` as the seat's source and a mount that never joins shown from its package's files ([spec Section 6.10](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/spec/agora-mcp.md)).

**Query:** optional, or the first call of every mount?

**Options:**

a) (recommended, confidence medium - a one-shot command through a bridge cannot hold a seat, and a mount's identity already names the package; a required join would shut that route out) Optional.

b) Required, so the roster is always from the tools.

### Q10 - The MCP's name and home

**Context:** the server shares the store and protocol code with the Beacon, and the estate has an `mcp-` repository convention ([spec Section 20](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/spec/agora-mcp.md), Q10).

**Query:** `agora-mcp` in apps-agora.local beside the Beacon, or its own repository?

**Options:**

a) (recommended, confidence medium - it is the Beacon's store and protocol with a second face, and one repository keeps the two level; the boundary rules already keep everything but `main.ts` free of Electron) In this repository, as `agora-mcp`, with its own module boundary.

b) Its own repository, `mcp-agora`, vendoring or pinning the shared code.

### Q11 - One combined checkpoint or one per store

**Context:** a reader with both stores gets `git:<commit>;live:<sequence>` and the MCP picks the part that applies ([spec Section 10](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/spec/agora-mcp.md)).

**Query:** one combined checkpoint, or one per store?

**Options:**

a) (recommended, confidence medium - a reader should not have to know how many stores stand behind the tools; the fallback by last id and time covers a part a store no longer knows) One combined checkpoint.

b) One per store, kept by the reader.

🧵 ki.prj.agora
