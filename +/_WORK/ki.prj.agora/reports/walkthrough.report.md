# [KI > Techne > Agora](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.agora/work.md) › walkthrough

**🤖 → 👤 Handoff to supervisor · Run report at 05:55 GMT · last mark 00:04 GMT**

---

## Done

- **The walkthrough is ready for tomorrow.** [docs/walkthrough/README.md](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/walkthrough/README.md) gives the running order and seven topics: the conceptual model, the three portals, two modes of connectivity, the two apps, talking to each pair of agents, the Agent Host Protocol, and where things stand. Each topic has a plain-English explanation, links to its sources and diagrams, and its open decisions for Kris (16 in all, each with Context / Query / Options and a recommended option). The last section lists twelve places where the documents disagree, with the latest wording winning.
- **The page:** [docs/walkthrough/walkthrough.html](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/walkthrough/walkthrough.html), one archify explainer with the conclusion first and one panel per topic. It has a new model diagram (planes, territories, islands, the keepers and the three portals), a new sequence of an idea hopping from terra to sol through the capitals and both ki-portals, a chart of measured latency per pairing, and a table pointing to the six existing architecture diagrams and the art. Its source is `walkthrough.archify.txt` beside it.
- **The Agent Host Protocol, read first-hand** (read only) on 6 November 2026: the overview page (1.0.0 current, 1.1.0 in draft), the versioning and stability page, the spec/v1.0.0 release of 2 October 2026, and the repository README. Finding: AHP connects one host to many clients. It fits inside one plane, under the Agora Portal, for presence, turn state and waking chats. It has nothing for traffic between rigs. Its version list and numbered snapshots are worth adopting now.
- The illustrator's art and the information architect's design pack are linked where they live in ki-principal, not copied. The one keeper image, `portal-mirrored-relay.png`, is linked in topic 1.
- Commit `673160d` on `main` in apps-agora.local. Checks: self:check passed, tests passed (373), Markdown lint clean, archify's page checks passed and its browser visual check passed at 1280 and 1440 wide. I looked at the first screen myself; the rest had only the automated checks.

**Choices I made:**

- I followed Kris's 05:55 corrections (WALKTHROUGH-TERMS) over the brief's older wording: "two modes of connectivity", strategy and latency per pairing of agents, hilltop and capital for the portals, and the planar portal managed through Git.
- I put forward a design for `ki-portal`. It holds the register (rigs, Portal addresses, which territories each plane carries) and durable cross-plane messages. The watchman writes it, never the Portal. Live signals stay on Tailscale. This is open as PORTAL-STORE.
- I drew the model as a tree (plane, then territory, then island) because the first architecture-style drawing was too small to read. The sequence diagram shows the routes.
- Where documents disagree, I let the latest decision win and listed every disagreement in the README rather than editing the older documents. The decisions log gives some times out of order, so I went by the order of the entries.
- I made no changes to the specification, `AGENTS.md` or any other repository. The fixes that would follow from the decisions are listed below as roadmap candidates.

## In Progress

- **Roadmap candidates (none created):**
  - build the Portal's entrance and agent presence once the protocol is reviewed;
  - the Agora MCP over the entrance;
  - hop-by-hop addresses and a check-before-act message in the protocol;
  - add AHP's version list and sequence numbers to the protocol;
  - trial the Agora Portal as an AHP client of one local host;
  - rename layers to modes, and amend the specification and `AGENTS.md` for the two apps;
  - the `ki-portal` register and its portal adapter.
- The 16 decisions are for Kris to take at the walkthrough. They are in the README and on the page's last panel as a checklist.

## Queries

None. The decisions for Kris are in the walkthrough itself, so he can take them there.

## New and noteworthy

- You can now open one page, [the Agora walkthrough](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/walkthrough/walkthrough.html), and see the whole of Agora: the world, the portals, the two modes, the two apps, how fast each pair of agents hears, and where AHP fits.
- Every open decision about Agora is now in one place, each with a recommendation, so you can settle them in a single sitting.
- The Agent Host Protocol has now been read first-hand, with a table showing what Agora could take from it.

🧵 ki.prj.agora
