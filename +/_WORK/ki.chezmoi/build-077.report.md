# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › build-077

**🤖 → 👤 Handoff to supervisor · Run report at 03:12 BST**

---

## Done

- [KB-DOTFILES-UE-077](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-077-reorganise-1password-vaults-safely.md) moved to Ready under READY-077 a) (Decision 156), in commit `3d4329f`.
- The three source fixes are built, in commit `70cbf2f`. The chezmoi guide's examples now read through `op_cache` against `Automation`, with `<vault>` placeholders for the attended commands. Its Service account section gains the background-agent paragraph, and the Rig guide points to it. The `op_cache` test fixture now uses the neutral vault `Elsewhere`.
- The setup guide names the age recovery document's vault as **Personal - Kris**, by vault name only (Decision 161).
- The record shows the cache expiry as done by Kris on Terra and Sol (CACHE-DISPOSAL). Kris's attended step on both Macs now includes `security delete-generic-password -s ki-op-service-account-rig`, with an absent entry counting as clean (RIG-KEYCHAIN a)). Its review packet is written.
- Verify searches: only the known Warp-tab false match remains. The second search now excludes `docs/roadmap`, because the record names the Keychain entry on purpose.
- Gate: `ki repo audit --repo .` has no failures and 12 warnings, the same set as before and within the baseline plus `CLAUDEBIND-1`. `node --test tests/*.test.mjs` passes 290 of 292, with 2 existing skips. `rumdl check .` is clean.
- No `op` command was run, no cache or Keychain was touched, nothing was pushed, and no `.git/*.lock` remains.

## In Progress

- [KB-DOTFILES-UE-077](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-077-reorganise-1password-vaults-safely.md) is at **In progress**, not Awaiting review. Only Kris's attended Keychain step remains, but `ki repo audit` fails ITEM-3 while any Step is unticked in an Awaiting review record. So I held the record at the brief's other state to keep the gate green.

## Queries

**Context:** The brief asked for Awaiting review if only the attended Keychain step remained. The audit rule ITEM-3 refuses that state while the step is unticked, so [KB-DOTFILES-UE-077](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-077-reorganise-1password-vaults-safely.md) is at In progress.

**Query:** How should the record reach review?

**Options:**

a) (recommended, confidence high - it keeps the gate green and is a record-only change) Kris runs the Keychain command on Terra and Sol and says when. A short run then ticks the step with both dates and moves the record to Awaiting review.

b) (confidence medium - it reaches review now, but changes the plan's shape) Move the Keychain step out of Steps into an acceptance condition. The record could then go to Awaiting review at once.

c) (confidence low - it bends the lifecycle) Accept the record with the Keychain step as a follow-up note.
