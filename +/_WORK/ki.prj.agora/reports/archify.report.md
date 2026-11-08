# KI > Techne > [Agora](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.agora/work.md) › archify

**🤖 → 👤 Handoff to supervisor · Run report at 04:22 GMT · last mark 00:04 GMT**

---

## New and noteworthy

- You can now open [What Agora is](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/design/architecture/what-agora-is.html). It is a one-page explainer that puts the conclusion first and links six diagrams, so you can see the whole of Agora in one place.
- Each diagram is an explorable page with light and dark themes. You can step through it and export it as an image. The six are: the system on two Macs, one Mac inside the portal, two Macs (portal traffic, a push crossing, a settle), the life of a message, presence with the keep-alive tiers, and the two layers.
- The diagrams use your terms throughout. The Agora portal is the tray process, portal traffic runs over Tailscale, agents enter through the entrance, and the durable layer is Git while the conversational layer is Agora.

## Done

- Drew Agora's architecture with archify into `docs/design/architecture/` in apps-agora.local. It has six diagrams, the "What Agora is" explainer and an [index](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/design/architecture/index.md) listing each one. The README now links to them from its opening paragraph.
- Commits `c8c2af5` (diagrams, explainer, index, README link) and `5743677` (the explainer's source, which the first commit missed). Both are pushed to `main`.
- Checks: archify's own checks passed on all seven pages, including the real-browser check on the six diagrams. `bun run self:check` passed, `bun run test` passed (280 tests), and the pre-commit Markdown lint passed.
- I looked at every diagram in light or dark screenshots. The explainer's small embedded overview has edge labels at about 7.7px on a 1440px screen. The optional readability check flags this, but the required checks pass, and its "Open interactive view" button shows the full-size diagram.
- Choices I made:
  - Each page records which parts are built today and which are only specified. The entrance, meeting place, said messages, meeting log and presence clocks are drawn as designed in the protocol draft, still awaiting your review (AGORA-BUILD b).
  - In the one-Mac diagram I left out the "pushed" line from the portal link to the level-keeper because it crossed another line. The level-keeper's label and a card cover it, and diagram 3 draws it in full.
  - Kris is not drawn in the overview, to keep both Macs readable. Kris appears at the tray in diagrams 2 and 5.
  - Diagram 3 adds `say` (specified) and `ack` to the portal traffic kinds you listed. "Call" is shown as `ring: a call`, its wire name.
  - The JSON source of each diagram is committed beside it so the pages can be regenerated. Archify's check receipts are not committed.
  - The explainer's source is kept as `what-agora-is.archify.txt`, not `.md`, because the repository's Markdown linter rejects archify's table rows.
  - The pages are self-contained HTML of about 0.8 MB each, 5.3 MB in total, committed to Git as text. They are not images, so the ART-INDEX question about large image files does not cover them.
  - Claude Design's three earlier Mermaid pictures stay in ki-principal. The index says the new diagrams replace them for the architecture.

## In Progress

- Nothing is running. Candidate roadmap record, not created: regenerate the diagrams whenever the protocol draft changes after your review, so the "specified" parts stay accurate.

## Queries

None.

🧵 ki.prj.agora
