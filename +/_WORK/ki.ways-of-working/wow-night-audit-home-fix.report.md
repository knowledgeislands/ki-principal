# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-night-audit-home-fix

**🤖 → 👤 Handoff to supervisor · Run report at 02:25 BST · last mark 01:40 BST**

---

## Done

- HARNESS-AUDIT-HOME fixed in the [audit home README](/Users/krisbrown/.local/state/ki/agents/ways-of-working/audit-home/README.md); no helper file was added. The block now captures the real user's installed Bun 1.4.2 and Node 24.21.0 by absolute path before `HOME` moves, puts them first on `PATH` with the mise shims left off, and points every `MISE_*` directory at the copied home with `MISE_OFFLINE=1`. A stray mise call now fails at once instead of installing anything.
- Two more gaps came up in the proof and are fixed in the same block. First, `ki dev local on` refused the seed's full `git archive` copy as "unrecognised state", so the harness steps now trim the run's own copy to `.ki.toml`, `skills`, `subagents` and `hooks`; the seed itself is untouched. Second, a fresh worktree has no `node_modules`, so the engineering gates tried `bunx` downloads; the block now borrows the primary checkout's `node_modules` through a link while `bun.lock` matches, and removes the link afterwards.
- The README's rationale and Proof sections are updated to match, and the old note that the `ki dev local` steps were never exercised is gone.
- Proof, KI Agentic Harness: the README's exact block, with the harness lines active, ran under `net-deny.sb` in a throwaway detached worktree of local `main`. Every step exited 0, including both `ki dev local` steps, and the audit returned PASS=28 WARN=7 FAIL=0. [Log](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-night-audit-home-fix.harness-audit.log).
- Proof, `tools-rig`: the same block ran in a throwaway detached worktree of local `main`. Every step exited 0 and the audit returned PASS=15 WARN=5 FAIL=0. [Log](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-night-audit-home-fix.tools-rig-audit.log).
- Mise never ran in either proof: no mise directory appeared in either temporary home, and neither log has any mise output.
- Both worktrees were left with no changes, then removed. Both temporary homes were removed by the block itself, and the run's temporary directory is empty.
- The real registry checksums are unchanged: `registry.toml`, `locals.toml`, `installation.toml`, `config.toml`, `~/.claude/settings.json` and the installed-harness listing match before and after.
- The real mise top-level folder's modified time changed once, at 02:23:21, while the proofs were running. It still holds the same four entries, and `installs`, `bun`, `node`, `shims` and `~/.config/mise/config.toml` all keep their old dates (14 to 20 October). The proof runs pointed mise elsewhere and never started it, and re-entering both worktrees from the agent's own shell did not change the time again. Most likely a concurrent session's mise touched it, but that is not proven.
- No commits, no remote calls and no environment changes were made.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- `wow-night-harness-queue-b` can now be dispatched again with the updated README. Its clean baseline worktree is still kept for reuse.
- The block names Bun 1.4.2 and Node 24.21.0, the global pins in `~/.config/mise/config.toml`. If those pins change, the README says how to update the two paths.

## Queries

No outstanding queries

### 🤖 → 👤 Handoff to supervisor · since 02:25 BST

🤖 0 running · 👤 0 with you

- [done] HARNESS-AUDIT-HOME audit home fixed and proven on harness and tools-rig worktrees · wow-night-audit-home-fix · since 02:25
- [waiting] redispatch harness queue delivery · ki.ways-of-working coordinator · since 02:25
