# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › fold-076

**🤖 → 👤 Handoff to supervisor · Run report at 03:21 BST · last mark 01:30 BST**

---

## Done

- [KB-DOTFILES-UE-076](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-076-always-run-latest-source.md) is planned from Decision 157 and stays draft at Next, committed locally as `4cd2f42`. The steps are:
  - A source-state helper whose `--fetch` mode does a bounded fetch only and writes a timestamped state file.
  - A step at the start of `rig-update` that never skips the upgrade and makes every state other than current `findings`.
  - A prompt signal (`src⇣N`, `src⇡N`, `src?`) read without network, separate from `⚙N`, stale after 36 hours.
  - Tests against a temporary bare upstream, and three guide updates.
- The Goal and Boundary now say that every pull is attended. The record says why: SOURCE-REFRESH b) went against the old automatic fast-forward. The grounding's `dirty` and `busy` states are gone, because nothing writes to the working tree.
- The record gained `size: m`, which clears its migration-window warning from the baseline.
- Gate: `ki repo audit` passed with only the permitted baseline warnings and `CLAUDEBIND-1`; `node --test tests/*.test.mjs` passed; `rumdl check .` passed. The tree is clean and no `.git/*.lock` is left.

## In Progress

Nothing. The record waits for Kris's Ready decision.

## Queries

### PENDING-REVIEW: how the prompt shows "pulled changes still need target review" (gap 9)

**Context:** The plan keeps the existing `⚙N` count from `chezmoi status` as this signal, next to a new `src…` signal for source freshness. `⚙N` also counts targets edited in place, so it cannot single out pulled changes. chezmoi does not record which revision was last applied.

**Query:** Is `⚙N` enough, or should delivery add a `run_after_` script that records the applied revision, so the prompt can count source commits not yet applied?

**Options:** a) (recommended, confidence medium-high - both kinds of change need the same `chezmoi diff` review, the count already rises after a pull, and it adds no new apply-time script) keep `⚙N` as planned. b) add a `run_after_` script that records `HEAD` on each apply, plus a third prompt count. c) defer it to a follow-up record.

### READY-076: move the record to Ready

**Context:** The plan has concrete steps, files and checks, with no blockers. Whether launchd can fetch over SSH is unknown, but if it cannot, the source reads `unknown` and the run reports `findings`, so it is not a blocker.

**Query:** Approve [KB-DOTFILES-UE-076](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-076-always-run-latest-source.md) as Ready, with PENDING-REVIEW answered?

**Options:** a) (recommended, confidence medium - the plan follows all three decisions directly; the only open choice is PENDING-REVIEW) Ready once PENDING-REVIEW is answered. b) keep it draft for another review of the plan.
