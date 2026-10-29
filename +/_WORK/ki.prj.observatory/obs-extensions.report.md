# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-extensions

**🤖 → 👤 Handoff to supervisor · Run report at 20:33 BST · last mark 20:20 BST**

---

## Done

- I rewrote [live-artifacts.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.observatory/design/live-artifacts.md) in place as an extension model. Each live artifact stays owned by its repository and declares which Instrument it extends. The model has five parts: three optional manifest keys; Extended by links from the Instrument, with back-links over the MCP Apps wire; the Observatory's design tokens handed over at start, so an artifact looks native in the frame and keeps its own look in Cowork; three tiers of data access (portable, its own server, provider or inference); and a table of what runs on the Observatory, in Cowork or on a published site.
- Built-in views: an Instrument stays as the floor and the richer artifact becomes the preferred surface. The Instrument keeps the Beacon signals, the degraded behaviour and the receipted operations, and it links to the artifact rather than growing to match it.
- Kit Git Repo Audit against Repositories is the worked case, and Kit Git Repo Audit is kept. I checked its stale roots directly: the page's `ROOT_DEFS` still scans `~/workspaces/hnr` and `~/workspaces/kit`, which no longer exist. The `mcp-git-audit` safe roots in chezmoi already list all eight territories, so the fix belongs to `personal-principal` alone.
- I re-sorted all 15 artifacts and both sites into six orders, plus a no-action list, and redrew the Mermaid diagram. The note gives three forks, each with two alternatives and their costs: how an artifact reaches its own server, what an Instrument does beside a richer artifact, and where an artifact registers.
- Committed `42e1e77` by explicit path. Pre-commit lint and repository audit passed; fetch passed. Not pushed, because a commit that is not mine is stacked with it (see PUSH-STACK).
- Limitations: I checked the diagram by eye only. The MCP Apps request names for back-links and host context still need checking against SEP-1865. No records were captured and no product changed.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Any approved step is a handoff to the repository that owns it: `personal-principal`, `hnr-principal`, `legal-principal` and `apps-observatory.local`.
- Under the progress protocol, this report is at the state path only, not in the work folder.
- I left other sessions' uncommitted changes in `ki-principal` untouched. They are under `+/_WORK/ki.chezmoi/`, `+/_WORK/ki.knowledge-acquisition/` and `+/_WORK/ki.ways-of-working/`, plus three untracked files.

## Queries

### PUSH-STACK - Push the stacked coordinator commit with this run's commit

**Context:** `origin/main` is behind by two commits, and nothing comes the other way. One is this run's `42e1e77`. The other is `b6c6650`, "docs(work): ki.observatory NO-MERMAID", made at 20:32: one line added to the Observatory decisions log, apparently by the coordinator. The brief allows a push only when my commit is the only one stacked.

**Query:** Should both commits be pushed fast-forward now?

**Options:** a) (recommended, confidence high - the other commit is one line of this work's own decisions log) The coordinator pushes both fast-forward after reading `b6c6650`. b) Hold both until the next mark.

### EXT-MODEL - Adopt the extension model and its order

**Context:** Order 1 needs no product work: fix and register Kit Git Repo Audit, and give manifests to HNR Council and the three legal artifacts. Order 2 is the first Observatory unit: the manifest keys, Extended by links, an Artifacts directory grouped by Instrument, and design tokens handed to the frame. Order 3 is Estate Map and HNR Streams Tracker, each after a move. Order 4 is a read port from the Observatory to `mcp-git-audit`; writes come later as confirmed Bridge operations. Order 5 is Kit Claude Housekeeping on the same pattern. Order 6 only lists the five artifacts that need a provider or an LLM, which stay in Cowork. Each fork's recommended alternative is assumed: reads go through mcporter, the Instrument stays as the floor, and artifacts register under `Admin/Operations/Live Artifacts/`.

**Query:** Do you adopt the model with the recommended forks, so each owning repository can be handed its first step?

**Options:** a) (recommended, confidence medium - order 1 rests on checked manifests, roots and tool calls, but the MCP Apps request names and the first server port are still unshaped) Adopt it all. Send order 1 as handoffs now, and take order 2 into `apps-observatory.local` as the Project's next unit after KI-OBSERVA-BRG-002. b) Adopt order 1 only. Decide the Observatory units once Kit Git Repo Audit runs again in Cowork. c) Adopt it with link-out only (Fork 1 b): no server ports, so Kit Git Repo Audit and Housekeeping stay in Cowork, and the Observatory just lists them and links to them.

### EXT-ROOTS - Hand the Kit Git Repo Audit fix to personal-principal now

**Context:** In Cowork today the artifact finds no repository except chezmoi, because its roots no longer exist. The fix sits entirely in `personal-principal`: replace `ROOT_DEFS` with the territory roots, give the pair one stem under `Admin/Operations/Live Artifacts/` with a manifest, and re-save it into Cowork. Its commit suggestion uses `askClaude` and writes a plain line rather than a Conventional Commit, which its owner may want to change at the same time. It does not depend on EXT-MODEL.

**Query:** Should the roots fix go to `personal-principal` as a handoff now, ahead of EXT-MODEL?

**Options:** a) (recommended, confidence high - the stale roots and the current safe roots were both read directly) Send it now, including the move and the manifest, and add the Conventional Commit suggestion as an optional item. b) Send the roots fix only, and leave the move and manifest for when EXT-MODEL is decided.

### 🤖 → 👤 Handoff to supervisor · since 20:33 BST

👤 3 with you

- [with you] PUSH-STACK · owner · since 20:33
- [with you] EXT-MODEL · owner · since 20:33
- [with you] EXT-ROOTS · owner · since 20:33
- [committed] design/live-artifacts.md as `42e1e77`
- [unpushed] `42e1e77` and `b6c6650` on main
