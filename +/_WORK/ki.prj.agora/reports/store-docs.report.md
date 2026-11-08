# KI > Techne > Agora › store-docs

**🤖 → 👤 Handoff to supervisor · Run report at 04:26 GMT · last mark 00:04 GMT**

---

## New and noteworthy

- `krisb/ki-agora-beacon` now reads only as the Agora Beacon's store. Agents use it through the Agora MCP, each rig's Beacon is bound to one store and watches it, it has the two-folder layout and two modes, Git history is the archive and only Kris truncates it, and each person keeps one private store. It points to STORE.md for the contract. Portals, planes, the watchman and former names are gone.
- Agora's MCP specification is rewritten as an RFC-style draft of the system as decided and built. It describes Markdown messages, derived status with no receipts, the package-owned roster, the ten tools, shared and fixed mounts, local and remote modes, Git commit checkpoints, harvest and audit. The Beacon's binding, waking, the Atlas and Lantern views, remote mode in live use, the cloud one-shot commands, the mark Summary, the listening word, and the pilot and migration are marked **Planned**, and the agora-gap design is linked for them.
- In Agora's docs, the channel between Beacons is now "the peer link" (protocol Section 4 is renamed). The architecture diagrams were rebuilt from their sources. The model's three portals stay only where agent interaction explains the model.
- Left as they are on purpose: decision ids such as PORTAL-MINIMAL, the walkthrough (a dated record of the model), the `portal.sock` path and the retirement of `Agora Portal.app` (both real code facts), the design pack's page "Macs and the portal", and the roadmap records.
- AGENTS.md's rule that Agora never commits is unchanged, because the Beacon does not write the store yet. agora.md now names the store as the one exception the MCP writes today. The narrowing for the Beacon itself comes with the binding.

## Done

- ki-agora-beacon `docs: describe the repository as the Agora Beacon's store`: README, AGENTS.md and `.ki.toml` description. rumdl fmt and check passed, and so did the Markdown and commit-message hooks. Pushed.
- apps-agora.local `2f04856` `docs(spec): describe the Agora MCP and store as decided and built`: 21 files in README.md and docs/, including the archify pages rebuilt with finalize (all passed). rumdl and the commit hooks passed. In a clean worktree, `bun run self:check` passed and `bun run test` passed (568 tests). Pushed.
- apps-agora.local `docs(spec): name the read-receipt answer as an open question`: Markdown only, rumdl passed. Pushed.

## In Progress

Nothing is running.

## Queries

### Q1 - Read receipts

**Context:** MCP-OPEN took Q3's recommended answer. In the mcp-design report that answer was to keep read receipts in Git. Your store design and the build keep none, and reading changes nothing. The specification describes what is built and lists this as open question 8.

**Query:** Should reading stay free of side effects, as built?

**Options:**

a) (recommended, confidence high - it matches your AGORA-STORE design, the build and the gap design's own recommendation) Yes. Unread means not yet acknowledged or answered, and the specification drops question 8.

b) No. Add read receipts to the store as a new mcp-agora roadmap item.

### Q2 - A home for the agora-gap design

**Context:** The specification cites the agora-gap design for everything still planned. That design exists only in the run state folder (`agora-gap.design.md`). Its report is in ki-principal's reports folder and is not yet committed there.

**Query:** Should the design move into the package's design folder?

**Options:**

a) (recommended, confidence medium - a planned-work reference needs a durable, committed home) Yes. Copy it to ki-principal's `+/_WORK/ki.prj.agora/design/agora-gap.md` and point the specification's reference there.

b) No. Leave it where it is until the gap plan is decided.

### Q3 - The store's repository code

**Context:** `.ki.toml` still has `repo_code = "PERSONAL-PORTAL"`. This run was allowed to change only description fields.

**Query:** Should the code be renamed?

**Options:**

a) (recommended, confidence medium - it is the last portal name on the store, and nothing in it is published yet) Rename it to `PERSONAL-AGORA-STORE` in a small follow-up run, after checking nothing else refers to it.

b) Keep it as it is.

🧵 ki.prj.agora
