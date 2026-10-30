<!-- rumdl-disable MD041 -->

### ORCH-NAME

**Context:** The brief proposed `ki-coordination` for working the package with Kris and `ki-orchestration` for the portable half of `ki-delegation`, with Orca and Paperclip adapters and `ki agent` possibly renamed `ki orchestrate`. On 29 October Kris named the thread agent "the orchestrator of the state machine", and that is the role `ki-coordination` governs. Orca, Oz and Paperclip all use "orchestration" to mean driving agents. KI-AGENTS-NAME, 17 October, says: "Keep "agents" ... nothing is renamed." `ki-delegation` already calls itself runtime-neutral.

**Query:** Which names should the coordination skill, the dispatch contract, its adapters and the command take?

**Options:**

- Rename `ki-coordination` to `ki-orchestration` to match the role word; for dispatch, keep `ki-delegation`, slimmed, as the portable contract, with adapters `ki-delegation-orca` and `ki-delegation-paperclip`, the second renamed from `ki-agent-coordination-paperclip`, keep `ki agent`, and move `decide`, `reconcile`, `home` and `prompts` under `ki work`.
- Keep `ki-coordination`. Keep `ki-delegation`, slimmed, as the portable contract, with adapters `ki-delegation-orca` and `ki-delegation-paperclip`, the second renamed from `ki-agent-coordination-paperclip`. Keep `ki agent`, and move `decide`, `reconcile`, `home` and `prompts` under `ki work`.
- The brief's family: `ki-orchestration`, `ki-orchestration-orca` and `ki-orchestration-paperclip` for dispatch, with `ki-coordination` unchanged.

### WORKTREE-OPTOUT

**Context:** Kris wants every writing run, under every launcher, in its own worktree, merged back to `main` fast-forward and verified. Coordinators stay on primary `main`. The collisions recorded in checkout-isolation came from the shared index and lock, not from the size of the change. A worktree costs about 0.2 seconds, plus about 1.5 seconds to clone dependencies.

**Query:** Which runs may skip the worktree?

**Options:**

- Let trivial single-file runs in a knowledge base write in the primary checkout as well.
- Only read-only runs that write nothing inside any repository. Trivial writing runs get no exception.
