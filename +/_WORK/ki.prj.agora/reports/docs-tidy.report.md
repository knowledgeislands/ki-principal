# KI > Techne > Agora › docs-tidy

**🤖 → 👤 Handoff to supervisor · Run report at 23:20 GMT · last mark 00:04 GMT**

---

## New and noteworthy

- Agora's documentation stands tidy enough to hand on: one index, today's names throughout, every link in `docs/` resolving except two in roadmap records (below), and one owner per topic. The MCP specification now carries the Git store's modes of operation as its Section 11.
- The documents that were most out of date were the walkthrough (a dated record, now marked with what changed since) and the places that still said `ki-portal`, Agora Portal or the Agora app. The specification, protocol, interaction spec, README and AGENTS.md were already on today's names.
- Two things only code can finish: the Atlas's map still looks for the planar portal's island by the key `ki-portal`, and the walkthrough page is archify output that keeps the day's names (Queries 1 and 2).

## Done

- **Modes of operation** in `docs/spec/agora-mcp.md`, commit 0725c56: new Section 11 with 11.1 History is built in (going back in time; truncation by squash and forced push as Kris's act alone, never Agora's or an agent's, with what it costs and keeping the old history reachable), 11.2 Offline and online, fully distributed (the three rules that make the record converge, with a diagram), 11.3 the five write paths (a. local clone, b. direct to the remote, c. peer to peer, d. the MCP over any, e. future routes), each with who writes, ids and ordering, `since(ref)` and conflict and reconnection, 11.4 the paths side by side, 11.5 what every path keeps. The abstract, scope, contents and Appendix B name it; the later sections are renumbered 12 to 22 and the old "Modes" (the mount modes) is retitled "Mounts" so each word has one meaning; a new Q12 asks about receipt paths for a package seated on two Macs, the one conflict the add-only layout does not rule out. `self:check` passed; every internal anchor resolves.
- **The index**, `docs/README.md`, commit 017e071: every document in reading order with what it is for and its status (spec, how it works, protocol, interaction, MCP, identity, Atlas, wake map, architecture, walkthrough, API, roadmap), the Lantern and the configuration example beside them, who owns which topic, today's names in one place, where the decisions and the package's notes live, and the rule for generated pages. The README links to it. `self:check` and rumdl passed.
- **Names and facts**, commit 235c7ef (the walkthrough went in the same commit, as its earlier commit attempt had left it staged; `self:check` and rumdl passed). Each fixed passage:
  - `docs/spec/agent-interaction.md`: `krisb/ki-portal` → `krisb/ki-agora-beacon` in the summary, Section 10 (with "named `ki-portal` until 6 November 2026", BEACON-REPO) and Appendix B. Fixed.
  - `docs/spec/agora.md`: C12 now says the Beacon stays the tray app with small windows and the large window is the Atlas's (TWO-APPS); C14 no longer defers the identity document to a later slice; the Git boundary points at the MCP's Q1, the one proposed narrowing, and says the rule stands until Kris answers. Fixed.
  - `docs/design/identity.md`: owner `personal.reg.assistant-sol` → `ki.prj.agora`; the two notification examples name `personal.reg.inbox-sol`. Fixed.
  - `docs/design/wake-map.md`: Agora's call is `call/<work-id>` with `doorbell/` as the old path, not the other way round; the Beacon's Watching and Broadcasts menus, gone since PORTAL-SLIM, are replaced by the read endpoint's `threads` and `broadcasts` and the Atlas. Fixed.
  - `docs/design/architecture/index.md`: "the Atlas is the rich Electron app still to come" → built, linking the Atlas document. Fixed. The six pages and the explainer name no old app or repository (checked), so they stand.
  - `docs/design/agora-app.md`: `ki-portal` → `ki-agora-beacon` in the map table, a caption and What comes next. Fixed. (The atlas-nav run had already written Known Lands and Home there.)
  - `docs/how-agora-works.md`: "the app" → the Atlas in three places. Fixed.
  - `README.md`: links to the index; says the Atlas is Agora's window and the Observatory stays ki.prj.observatory's as tabs (it said the Observatory was the viewing app); the sidebar lists Home (who holds what), Known Lands under Work, the KIV's pages and the System foot; the map is Known Lands. Fixed.
  - `docs/walkthrough/README.md`: a **Since the walkthrough** note at the top (APP-NAMES, BEACON-REPO, KIV-TO-AGORA, AGORA-MCP-DESIGN); Agora Portal → Agora Beacon, the Agora app → the Agora Atlas and `ki-portal` → `ki-agora-beacon` throughout, keeping "planar portal"; topic 4 rewritten as the three apps with today's menu and the KIV as Agora's; **Since** lines under PORTAL-STORE (answered by BEACON-REPO and AGORA-MCP-DESIGN), VIEWER-SCOPE (option a in effect), AGORA-MCP (specified) and the disagreements on the tray's menu and whether Agora views; the link to the beacon repository's README repaired. Fixed, kept as a dated record. Its page is unchanged (Query 1).
- **Merged or left as one owner:** no two documents were found saying the same thing at length; the overlaps (README against the protocol on Agora's call, the walkthrough against the specs) are summaries that link to their owner, and the index names the owner of each topic. The Modes section is the one owner of the write paths; the mount section (12.4) now points at it instead of restating offline.
- **Links:** every link in `docs/`, the README, AGENTS.md and `ios/README.md` checked, files and anchors. Two do not resolve, both in roadmap records left untouched: `KI-AGORA-WRK-002` links a chezmoi record `PERSONAL-DOTFILES-UE-139` that is not in `~/.local/share/chezmoi/docs/roadmap/` (Query 3); `KI-AGORA-WRK-004`'s link to the Techne Programme Focus resolves once its `%20` is decoded, so it is sound.
- **Code comments:** none changed. Every "Portal" or "doorbell" left in `src/` is either a decision id (PORTAL-MENU-ORCA), a historical note that is correct (the installer retiring the old apps, the old bundle id) or behaviour (the doorbell path, the door's socket name). The one stale term that matters is behaviour, not a comment (Query 2).
- **Not touched:** `docs/api/view-v1.md` and its example, which the atlas-nav run was editing (now committed by it) and which are current; the roadmap records, which name history (KI-AGORA-NET-001 says the KIV lived at `personal/assistant/prototype/kiv/`, true when written); AGENTS.md and CLAUDE.md, current and outside the brief's paths.

## In Progress

- Nothing. The run is complete.

## Findings

### DOCS-OUTSIDE - Documents outside this repository that describe Agora

**Goal:** list each with a recommendation: move in, link or leave.

**Scope:** ki.prj.agora's work package in ki-principal (`+/_WORK/ki.prj.agora/`), the beacon repository, and the two Inbox notes the wake map draws on.

**As of:** 6 November 2026, 23:20 GMT.

| Document | What it is | Recommendation |
| --- | --- | --- |
| `_emerging/agora-vision.md` | Kris's picture of islands, portals and the Atlas, with his walkthrough corrections | Link, as the walkthrough and the Atlas document do; the specification owns purpose now, and the vision is his words, which belong with the package |
| `_emerging/agora-alignment.md` | The 21 conflicts and what resolves each | Link, as the specification does; it is the conflict record and the spec carries the settlements |
| `_emerging/agora-plan.md`, `agora-backlog.md`, `overnight-brief.md` | The plan, the 31-item backlog and the overnight way of working | Leave; package working notes of one night, already linked from the walkthrough where they matter. The backlog's live items should become roadmap records here as they are taken up, not be moved as a file |
| `_emerging/kiv-handover.md` | The KIV handover from personal.reg.inbox-sol with five open items | Leave for now; once the KIV's code moves here, its open items become this repository's roadmap records and the note can be retired |
| `identity/claude-design/` (the Atlas design pack, IA.md, the tray menu, who-is-doing-what, the Lantern's pack, diagrams, architecture.md) | The information architect's pack the Atlas follows | Link, as the Atlas document and the walkthrough do. Moving the pack in would make this repository the art's home before Kris has settled where large art lives (ART-HOME, open) |
| `identity/chatgpt/` (studies, badges, menu rings, icon) | The illustrator's art and index | Link; same reason. The agreed symbol and icon are already here as sources under `assets/` |
| `decisions.md`, `discussions.md`, `work.md`, `state.md`, `messages.md`, `reports/` | The package's own files and 37 run reports | Leave; they are the package's record, and the index says the decisions in capitals live there |
| `krisb/ki-agora-beacon` README and AGENTS.md | The planar portal's island, the watchman, the three portals | Link, as the MCP spec does as [BEACON-README]. One line there still says the protocol is drafted in `agora-protocol.md` and `agent-interaction.md`; adding `agora-mcp.md` is the watchman's or Kris's edit in that repository, not this run's |
| personal.reg.inbox-sol's `coordination/wake-research.md` and `session-coordination.spec.md` | What each vendor ships and the coordination words | Link, as the wake map does; they are the Inbox's |
| chezmoi `docs/guides/tools/claude-swap.md` | Names the account-switching idea the WRK-002 record cites | Leave |

## Queries

### Q1 - The walkthrough page and its archify source keep the day's names

**Context:** `docs/walkthrough/walkthrough.html` and `walkthrough.archify.txt` are generated; the page says Agora Portal 12 times and `ki-portal` 43 times, and draws two apps. The README beside it is on today's names and says the page keeps the names of the day. Regenerating means editing the archify source and rebuilding the page, which changes a dated artefact.

**Query:** rebuild the page on today's names, or keep it as the record of the day?

**Options:**

a) (recommended, confidence medium - the README carries the words and the Since note, and a dated page is honest about what Kris saw that morning) Keep the page as it is, with the README's note.

b) Edit the archify source to today's names and three apps and rebuild the page, in a short run with the archify skill.

### Q2 - The Atlas's map looks for the planar portal's island by its old key

**Context:** `src/app/renderer/index.ts` finds the planar portal's island with `item.key === 'ki-portal'`, so since BEACON-REPO the map falls back to drawing the portal from the household. This is behaviour, so it was out of this run's remit, and the file was in the atlas-nav run's hands.

**Query:** fix the key now?

**Options:**

a) (recommended, confidence high - a one-line change with a test, and the map is wrong until it lands) A small code slice: match `ki-agora-beacon`, keeping `ki-portal` as a fallback for a rig whose registry has not followed the rename, and update the comment.

b) Leave until the planar portal's island is drawn as such (What comes next in the Atlas document).

### Q3 - A roadmap record links a chezmoi record that is not there

**Context:** `docs/roadmap/KI-AGORA-WRK-002-switch-claude-accounts.md` (triage) links `~/.local/share/chezmoi/docs/roadmap/PERSONAL-DOTFILES-UE-139-switch-claude-accounts-from-agora.md`, which does not exist; chezmoi's roadmap folder holds only its ledgers, and its Claude Swap guide still names UE-139. Work records are not this run's to edit.

**Query:** what should the link point at?

**Options:**

a) (recommended, confidence medium - the record is still in triage and the household owns the chezmoi side) Ask personal.reg.household-sol where UE-139 went (done, pruned or renamed) and repair the link in a later `ki-plan` pass on WRK-002.

b) Replace the link with the guide, `docs/guides/tools/claude-swap.md`, now.

### Q4 - When the old doorbell path stops

**Context:** the README, How Agora works, the specification (C6) and the wake map say `doorbell/<work-id>` is written until the first Agora built after 20 November 2026; FAST-MOVE (Kris, about 04:35 GMT) says drop it as soon as both households have installed the new Agora. The walkthrough lists this as a disagreement still open. The documents were left consistent with each other on the 20 November line, since the code still writes both paths.

**Query:** which line do the documents carry?

**Options:**

a) (recommended, confidence medium - it is what the code does, and the date is a safe upper bound) Keep 20 November in the documents until the code slice that stops the old path lands, then say so everywhere in that slice.

b) Change the documents now to "once both households have installed the new Agora", ahead of the code.

🧵 ki.prj.agora
