# mgit-chain brief

Work: ki.sop.main (KI > SoP). Host sol. Repository: `/Users/krisbrown/workspaces/knowledge-islands/tools-mgit`.

## Authority

Kris, 2026-10-28: "I like the chain thing, so we should add that pretty quickly. I wonder if we can just get ahead and do that right now." This authorises you to capture, plan and deliver one tools-mgit roadmap record for `mgit chain` under `ki-next`, `ki-plan` and `ki-implement`, and to leave it Awaiting review.

- Do not accept the record.
- Do not cut a release; releases ask first, under release-on-demand.
- Do not touch `mgit sync`'s behaviour. MGIT-PUSH-GUARD, MGIT-TOLERANT and a sync redesign are queued separately with ki.prj.tools-burndown.

## The design Kris agreed

- **Syntax:** `mgit chain <git command> [args...] --then <git command> [args...] [--then ...]`, with no quotes. `chain` takes the rest of the line raw, so mgit's option parser consumes neither the Git flags nor `--then`, and splits it at each literal `--then`. Each piece is one Git subcommand, run as ordinary pass-through commands are.
- **Per-repository pipeline:**
  - Inside each repository the steps run in order, and that repository's chain stops at its first failing step. Other repositories carry on.
  - Repositories run in parallel under `-j`, and `-v` streams them one at a time.
  - The usual selection options (`-t`, `--estate`, `--filter`, `-W` and so on) apply.
  - Mixing mgit-owned commands into a chain is out of scope for v1.
- **Output:** one block per repository naming each step's outcome, then one tally: completed, stopped at a step, and failed to start. Provide `--json` if the existing JSON result path makes that cheap.
- **Recipes:**
  - A recipe is set with `git config mgit.chain.<name> "<steps joined by --then>"` and run with `mgit chain <name>`.
  - If it can be done cleanly, also let `mgit <name>` run a recipe. A recipe must never shadow an mgit-owned command; it takes precedence over Git pass-through, and `-B` bypasses it.
  - If top-level recipes would be ambiguous, ship `mgit chain <name>` and raise the top-level form as a query.
- **Documentation and tests:** document the edge case of a path literally named `--then`. Update help, usage, the zsh completion, the man page and the README or guides, and add tests in the repository's own framework covering:
  - splitting, and that Git flags survive
  - stopping at the first failure while other repositories continue
  - parallel and verbose runs
  - recipes, including their precedence and the no-shadow rule

## Working rules

- Follow tools-mgit's `AGENTS.md`, its checks and `ki-engineering`.
- Check `git status` first. If another session has uncommitted changes in tools-mgit, stop and report rather than working around them.
- Commit by explicit path with Conventional Commit subjects. Run the repository's full checks, pull with rebase and push fast-forward only. Never force a push and never use `--no-verify`.

## Report

Write `/Users/krisbrown/.local/state/ki/agents/ki-sop-main/mgit-chain.report.md` in run-report form: Done, In Progress and Queries. Each query carries Context, Query and lettered Options, the recommended option first with its confidence and reason.
