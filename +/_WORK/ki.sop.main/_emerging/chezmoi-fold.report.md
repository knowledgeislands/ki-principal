# [KI > SoP](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.sop.main/work.md) › chezmoi-fold

**🤖 → 👤 Handoff to supervisor · Run report at 04:08 GMT · last mark 00:03 GMT**

---

## Done

- Folded [ki.prj.chezmoi](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.chezmoi/work.md) into the household works under CHEZMOI-HANDOVER a). The [handover note](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.chezmoi/_emerging/handover.md) says who takes each item. Every Inbound line's disposition is in its [decisions](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.chezmoi/decisions.md), and its queue is empty. The package is On hold with reason "folded into the household works" and release "close-out once the household works ACK". ki-principal `ebb55983`; lint passed, commit hooks passed, published.
- Sent to [personal.reg.household-terra](/Users/krisbrown/.local/share/chezmoi/+/_WORK/personal.reg.household-terra/messages.md):
  - MSG-dc361030: the handover, with TRUST-COMPLETE and VSCODE-LAYOUT
  - MSG-5af13654: MCP-PROCS
  - MSG-d845825f: TRIAGE-HOURS, TRIAGE-HOURS-APPLY and REROUTE-GRANT. Replies go to personal.reg.assistant-terra.
  - MSG-2c6d513d: BUILDS-TOKEN-PATH and JOB-TOKENS
  - MSG-47b31193: the Orca preferences items
  - MSG-65f69c1c: MGIT-SYNC-ADOPT
  - MSG-e069a853: INTERACTIVE-QUERIES
  - MSG-240e5015: terra's share of the checkout move
  - An ACK for MSG-b29708ed.
- Sent to [personal.reg.household-sol](/Users/krisbrown/.local/share/chezmoi/+/_WORK/personal.reg.household-sol/messages.md):
  - MSG-a0c8ba95: the handover, carrying the open questions UTM-SOURCE and WARP-CONTAINER
  - MSG-9d4e8503: sol's share of the move
  - MSG-9aaf78c8: WHATSAPP-MCP-SCOPE
  - MSG-db66d378: remove the rebase autostash. It asks household-sol to delete `autoStash = true` from `dot_gitconfig` (keeping `pull.rebase`), review `chezmoi diff` and apply on both Macs, and gives the reason. The chezmoi source itself is unchanged.
  - Commit: chezmoi `c5e2d035`. Lint passed and the commit is published.
- Sent to [ki.sop.tools](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.sop.tools/messages.md), the tools-rig lane:
  - MSG-734cb7e2: the scheduled-runner group (WAKE-SUBSTRATE, DISPATCHER, MGIT-SYNC-JOB). Its chezmoi records PERSONAL-DOTFILES-UE-126 and UE-137 are cancelled, and UE-137 says scheduling moves to Agora and tools-rig.
  - MSG-d3cd35cf: RIG-OWNS-CONFIG
- Sent to [ki.reg.guilds](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/+/_WORK/ki.reg.guilds/messages.md):
  - MSG-8e93a86a: HEADER-ESTATE
  - ACKs for the four REFRESH lines it sent
  - The SKILL-HARVEST reply, ACK MSG-c6fa7c81
  - The guild's own session has already taken and committed all of these (harness `25f04865`).
- Dropped two open questions as overtaken. ACCEPT-UE106: PERSONAL-DOTFILES-UE-106 was accepted in chezmoi `c625c662` and pruned in `646d1ff9`. WARP-HANDLER had already been dropped under OBSOLETE-DROP.
- Recorded all 15 messages in ki.sop.main's `## Outbound`. ki.sop.main's two REFRESH lines to chezmoi (MSG-4efdc82e, MSG-e864cdc7) were cleared from that Outbound as received.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Close-out waits on ACKs from personal.reg.household-terra (MSG-dc361030) and personal.reg.household-sol (MSG-a0c8ba95).
- Another State of play run sent ki.prj.chezmoi the line MSG-dc59c0e6 RIG-REFS while this run was working. That line is still uncommitted in the chezmoi package's `messages.md`, so I left it untouched for its sender to commit. Once committed, it is the package's only Inbound line, and State of play can route it to the household works under the fold.
- The checkout move is overtaken in part: checkouts landed at `~/kis/<territory>/<repo>`, not `~/world`, and `paperclip` was not moved out. MSG-240e5015 asks household-terra to check with Kris whether PAPERCLIP-EXTERNAL still stands.

## Queries

### HOLD-REASON - The hold reason uses words where the standard expects a fixed value

**Context:** The brief set ki.prj.chezmoi's hold reason to "folded into the household works", and that is what was written. The work-package standard expects the reason to be one of two fixed values: `paused` for an ordinary hold, or `more-expected` for one waiting on more messages. The `ki` tooling or the package checker may therefore flag this package.

**Query:** Should the hold reason become `paused`, with the explanation kept in the state file's prose?

**Options:**

a) (recommended, confidence medium - it keeps the package valid and loses nothing, but the brief chose these words on purpose) Set `hold.reason: paused`, and keep "folded into the household works" in the Now line and the release.

b) Keep the brief's words as they are, and accept any checker warning until close-out.
