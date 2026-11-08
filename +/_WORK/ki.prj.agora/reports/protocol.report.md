# KI > Techne > Agora › protocol

**🤖 → 👤 Handoff to supervisor · Run report at 04:08 GMT · last mark 00:04 GMT**

---

## Done

- **The Agora protocol is written** as an RFC-style draft, [docs/spec/agora-protocol.md](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/spec/agora-protocol.md). It has the BCP 14 conformance paragraph, two conformance classes (an Agora and an agent), defined terms and roles, numbered sections with JSON message shapes, a security section, the relation to the Agent Host Protocol, eleven one-line open questions and an appendix showing which sections are built. It covers all fourteen points in the brief. Other documents are cited only through its References section, so it can move into a KI skill unchanged.
- **Links:** the plain-English [specification](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/spec/agora.md) now calls itself the overview and links the protocol, and the [README](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/README.md) links it beside the specification. No code changed.
- **Commit:** `f729314` `docs(spec): write the Agora protocol as an RFC-style draft`, pushed to `main`.
- **Checks:** Markdown lint (rumdl) passes on the three files; Biome does not check Markdown. With only this commit's files on top of `main`, `bun run self:check` and `bun run test` both pass (267 tests), run in a temporary worktree that has since been removed. In the shared checkout both fail, because of the tray-tidy run's unfinished `src/wording.ts` (5 tests in `src/wording.test.ts` and one formatting error). This run left that work alone.

**Choices made in the draft**, each one also an open question in the document where Kris may want a say:

1. The entrance is a Unix socket at `~/.local/state/ki/agora/entrance.sock`, open only to Kris's user, checked by the operating system's peer credentials. It is not the loopback port, which other users and browser pages can reach.
2. A seat is one per work id per Mac. A second join replaces the first, and the old session is told it was replaced.
3. Only an acknowledgement or a roll-call answer restarts an agent's keep-alive clock. Saying something proves the agent is alive, not that its listener is armed. The default listening period is two hours, between 5 minutes and 24 hours.
4. A roll call is the existing Ping, also delivered to each joined agent. Only Kris calls one.
5. The roster and the address book stay on the read-only feed, as the roster run built them. The meeting log, which holds agents' words, is read only through the entrance.
6. The address book only suggests, as built. Agora never routes on a lookup alone.
7. Each Mac has a **keeper**: its inbox agent makes announcements durable and answers `kept` with the commit. Everyone else leaves the record alone.
8. Messages agents say to each other use a new portal message, `say`. They are queued for an absent Mac like broadcasts. Each agent gets a new per-agent inbox file, while broadcasts keep their own file.
9. Anything that must matter after the roughly 24-hour meeting log forgets it goes through Git.
10. The settle call, built by the settle run while this one worked, is restated as built. The roster's built state is restated too.
11. The AHP mappings are marked "to check", because the run made no network call. The Agent2Agent Protocol is named as the nearer comparison for agent-to-agent talk.

**Roadmap record candidates** (none created): the meeting place's entrance (join, leave, say, ack, answer); agent presence with keep-alive tiers and lost reporting; the meeting log and catching up; the `say` portal message and the per-agent inbox file; the keeper's `kept` answer and the "not yet kept" tray line; telling Kris about agents that cannot be woken (wake map gap G7).

**Noticed:** the README still says the old `doorbell/` path stops after 20 November. Kris's FAST-MOVE says it stops as soon as both Macs run the new Agora. The protocol follows FAST-MOVE. The README line is left for the next docs slice.

## In Progress

Nothing. Building the entrance and agent presence waits for Kris's review (AGORA-BUILD b).

## New and noteworthy

- Kris can now read in one place, in plain MUST and SHOULD terms, how Agoras and agents behave. It covers what is built and what was settled tonight, with each section marked built or not.
- The meeting place, roll call with keep-alive tiers, the 24-hour meeting log and announcements written once by each Mac's keeper are now specified, ready for his review before anything is built.
- Eleven one-line open questions at the end of the protocol collect every choice the draft made on his behalf.

## Queries

### PROTOCOL-REVIEW - How to settle the protocol's open questions

**Context:** the draft makes eleven choices that Kris has not ruled on, listed in its Section 16. Examples are the entrance as a local socket, a new join replacing an old one, and only acknowledgements keeping an agent alive. Building the entrance waits for his review.

**Query:** how should the open questions be settled before the entrance is built?

**Options:**

a) (recommended, confidence medium - the draft's choices follow tonight's decisions, so a quick pass to accept or change each is enough) Go through the eleven questions with the coordinator in the morning. Answer each in a word, take the draft's choice where he has no view, and then build.

b) Treat the draft's choices as accepted and build the entrance now. Revisit any choice once it is in use.

c) Hold the build until the protocol moves into a KI skill with ki.sop.main.

🧵 ki.prj.agora
