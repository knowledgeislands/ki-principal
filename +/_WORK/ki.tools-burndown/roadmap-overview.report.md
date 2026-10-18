# [Platform foundations](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Initiatives/platform-foundations.md) › [tools-burndown](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/tools-burndown.md) › roadmap-overview

**Run report at 22:34 BST · last mark none**

---

## Done

- Read every open roadmap record in tools-ki, tools-rig, tools-mgit, tools-git-almanac and tools-techne, and the CLI-shaped records in ki-agentic-harness, from each repository's `main` ref. Changed nothing in any repository; this report is the only file written, and it is uncommitted, as briefed.
- Read how mgit `sync`, `-B/--bare` and `-P/-L` work today, and what git-almanac does and explicitly will not do.
- Wrote the overview, the per-tool themes, a burn-down order and an mgit plan below.

Two reading caveats:

- **tools-ki has diverged.** Local `main` and `origin/main` have each moved on. Local `main` has 17 open records (the 17 you counted). `origin/main` also has three that are not on local `main`: [KI-TOOL-KI-CLI-141](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-141-granola-screenshots-markers.md), [KI-TOOL-KI-CLI-142](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-142-preserve-harness-release-settings.md) and [KI-TOOL-KI-CLI-143](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-143-separate-local-harness-paths.md). The other session's rebase will bring them together, giving 20. While the rebase is still running, the working tree has no files for KI-TOOL-KI-CLI-144 and KI-TOOL-KI-CLI-145, so their links below will not open until it finishes.
- **mgit re-read after mgit-diverge's commits.** By 22:33 BST tools-mgit `main` had the two KI-TOOL-MGIT-CLI-017 records merged into one, with MGIT-OUTPUT captured as [KI-TOOL-MGIT-CLI-018](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-018-estate-scale-output.md) and MGIT-ESCAPE as [KI-TOOL-MGIT-CLI-019](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-019-pass-through-escape-hatch.md). mgit-diverge was still writing its report then; the mgit section reflects that `main`.

### 1. Overview

| Tool | What it is for | Draft | Adopted / ready | In progress | Awaiting review | Held | Triage | What the open work adds up to |
|---|---|---|---|---|---|---|---|---|
| tools-ki (`ki`) | Bootstraps and audits KI repositories, and launches and coordinates background agents | 7 | 0 | 0 | 7 (+1 on origin) | 1 | 2 (+2 on origin) | Make background agents and coordinating threads reliable to run all day, and make `ki` handle real hosts honestly |
| tools-rig (`rig`) | Declares and applies one workstation set-up across machines | 1 | 1 | 0 | 1 | 3 | 6 | Make `rig doctor` trustworthy and bring the visible desktop (Dock, menu bar, repository lists) under declaration |
| tools-mgit (`mgit`) | Runs Git and other commands across many repositories | 0 | 0 | 0 | 1 | 0 | 2 | Turn mgit from "loop a command over repositories" into a fast, quiet estate tool: overview, safe parallel sync, clear escape hatches |
| tools-git-almanac (`git almanac`) | Calendars, authors and reports for one repository's history | 0 | 0 | 0 | 0 | 0 | 0 | Nothing open; feature-complete for its stated contract |
| tools-techne (`techne`) | Operator CLI for Techné agent hosts | 1 | 0 | 0 | 0 | 1 | 0 | Make host commands safe; both records sit behind the Techné programme hold |
| ki-agentic-harness (CLI-shaped only) | Standards and skills that the CLIs implement | 2 | 0 | 1 | 2 | 0 | 4 | The standards side of the same agent-run and Git hygiene work that tools-ki delivers |

The "Held" column counts drafts in the `hold` horizon. They are not counted again under Draft.

### 2. Per tool

#### tools-ki

**Theme A - background agents and threads you can trust.** This makes `ki agent` show what needs you in the right order and never lose or overwrite an agent's work. It also makes `ki agent` follow the brief it was given and know which thread it is.

- [KI-TOOL-KI-CLI-123](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-123-agent-run-events.md) Agent run events - awaiting review
- [KI-TOOL-KI-CLI-127](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-127-agent-status-live-threads.md) Agent thread coordination commands - awaiting review
- [KI-TOOL-KI-CLI-133](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-133-retired-reports-come-back.md) Retired reports come back - awaiting review
- [KI-TOOL-KI-CLI-135](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-135-reused-agent-name-overwrites.md) Reused agent name overwrites - awaiting review
- [KI-TOOL-KI-CLI-134](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-134-launch-footer-follows-brief.md) Launch footer follows brief - draft, next
- [KI-TOOL-KI-CLI-137](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-137-agent-run-tmp-home.md) Agent run temporary home - draft, next
- [KI-TOOL-KI-CLI-144](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-144-older-runs-start-seen.md) Older runs start seen - triage. This is a follow-on defect of KI-TOOL-KI-CLI-123, so it is best delivered straight after 123 is accepted.
- [KI-TOOL-KI-CLI-145](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-145-thread-session-bindings-role.md) Thread session bindings - triage

**Theme B - honest host state.** This lets `ki` work on a machine that does not have every store or harness checkout, report that plainly and suggest the fix, without losing configuration.

- [KI-TOOL-KI-CLI-126](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-126-unavailable-store-breaks-repair.md) Unavailable store breaks repair - awaiting review; blocks 131
- [KI-TOOL-KI-CLI-131](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-131-host-absent-store-state.md) Host-absent store state - draft, next; blocked by 126, blocks 136
- [KI-TOOL-KI-CLI-136](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-136-errors-suggest-fixes.md) Errors suggest fixes - draft, next; blocked by 131
- [KI-TOOL-KI-CLI-142](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-142-preserve-harness-release-settings.md) Preserve harness release settings - triage, origin only. A real defect: rewriting the configuration drops the release settings.
- [KI-TOOL-KI-CLI-143](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-143-separate-local-harness-paths.md) Separate local harness paths - triage, origin only. This should follow 142.

**Theme C - records and skills tooling.** This keeps roadmap records clean and lets a skill's standard generate its own runtime files.

- [KI-TOOL-KI-CLI-130](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-130-skill-generated-surfaces.md) Generated skill surfaces - awaiting review
- [KI-TOOL-KI-CLI-138](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-138-warn-unknown-record-fields.md) Warn unknown record fields - awaiting review

**Theme D - knowledge acquisition.** This brings outside sources (Granola, EBU SharePoint) in safely and keeps them in step.

- [KI-TOOL-KI-CLI-141](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-141-granola-screenshots-markers.md) Granola screenshots and markers - awaiting review, origin only
- [KI-TOOL-KI-CLI-128](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-128-granola-retention-safeguards.md) Granola retention safeguards - draft, next. Work is parked on `origin/fix/granola-retention-20261014`, and the record has not moved since 14 October, so it is at risk of going stale.
- [KI-TOOL-KI-CLI-139](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-139-ebu-sources-sync.md) EBU sources sync - draft, next. It is also the record in conflict in the current rebase.

**Theme E - releases and estate hygiene.** This gives one signed release contract for every tool, and a fleet-wide check for stale branches and leftovers.

- [KI-TOOL-KI-CLI-125](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-125-ki-release-contract.md) KI release contract - draft, held
- [KI-TOOL-KI-CLI-140](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-140-git-hygiene-estate-audit.md) Git hygiene estate audit - draft, next. It overlaps heavily with the mgit estate overview; see the mgit plan.

#### tools-rig

**Theme A - a doctor you can believe.** This makes `rig doctor` name the real cause before an apply fails, instead of a misleading symptom.

- [KI-TOOL-RIG-CORE-052](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-052-doctor-service-launch-prerequisites.md) Doctor service launch prerequisites - triage
- [KI-TOOL-RIG-CORE-054](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-054-command-line-tools-check.md) Command Line Tools check - triage
- [KI-TOOL-RIG-CORE-055](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-055-interpreter-port-owner-matching.md) Interpreter port owner matching - triage
- [KI-TOOL-RIG-CORE-058](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-058-apply-lock-handler-history.md) Apply lock, handler history - triage. Two applies cannot collide, and handler failures show in status.

**Theme B - the visible desktop under declaration.** One declaration sets the Dock, menu bar and GitHub Desktop's repository list on every machine.

- [KI-TOOL-RIG-CORE-042](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-042-profile-filtered-dock-items.md) Profile-filtered Dock items - ready, now
- [KI-TOOL-RIG-CORE-053](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-053-macos-menu-bar-declarations.md) macOS menu bar declarations - triage
- [KI-TOOL-RIG-CORE-056](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-056-menu-bar-order-persistence.md) Menu bar order persistence - draft, future. An investigation that sits alongside 053. 053 only reports drift; 056 asks whether Rig could ever set the order. They can be planned together.
- [KI-TOOL-RIG-CORE-057](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-057-github-desktop-repository-list.md) GitHub Desktop repository list - triage. It relies on mgit's territory selection, which crosses into the mgit work.

**Theme C - remote access locked to the tailnet.**

- [KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md) Tailnet-only listener firewall - awaiting review. This is connection-critical, so its acceptance needs the tested restore path.

**Theme D - distribution and dev mode (all held).**

- [KI-TOOL-RIG-CORE-048](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-048-signed-release-install-kind.md) Signed-release install kind - draft, held. It depends on [KI-TOOL-KI-CLI-125](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-125-ki-release-contract.md) defining the signed release, so both should be released together.
- [KI-TOOL-RIG-CLI-026](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CLI-026-per-tool-development-mode-switch.md) Per-tool development mode switch - draft, held. This partly overlaps `ki dev` local/release switching and [KI-TOOL-KI-CLI-143](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-143-separate-local-harness-paths.md).
- [KI-TOOL-RIG-DIST-011](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-DIST-011-stale-terra-rig-link.md) Stale vega rig link - draft, held. Likely stale: the file is still named after `terra` but the title says `vega`, and it is a one-host fix that the vega rebuild may already have dealt with.

The running `rig-target-speed` agent has no record. It works under your direct instruction of 17 October.

#### tools-mgit

**Theme A - one member model.**

- [KI-TOOL-MGIT-CLI-017](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-017-unified-external-members.md) Unified external members - awaiting review
- The duplicate KI-TOOL-MGIT-CLI-017 capture ("Unify repository members", same number) has been merged into the record above by mgit-diverge, so that duplicate is resolved.

**Theme B - an estate tool rather than a loop.** Quiet, readable output at estate scale, plus escape hatches so mgit can own verbs without blocking plain Git.

- [KI-TOOL-MGIT-CLI-018](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-018-estate-scale-output.md) Estate-scale output (MGIT-OUTPUT) - triage
- [KI-TOOL-MGIT-CLI-019](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-019-pass-through-escape-hatch.md) Pass-through escape hatch (MGIT-ESCAPE) - triage. It notes a gap today: because mgit owns `worktree`, `git worktree` cannot be run across the set at all.

#### tools-git-almanac

No open records. Its specification lists "cross-repository aggregation" as an explicit non-goal. That matters for the mgit plan.

#### tools-techne

Both records are behind the [Techne Programme Hold](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Policies/Techne Programme Hold.md>). Local work on 009 is allowed, but any live host proof is not.

- [KI-TOOL-TECHNE-CLI-006](/Users/krisbrown/workspaces/knowledge-islands/tools-techne/docs/roadmap/KI-TOOL-TECHNE-CLI-006-guarded-host-commands.md) Guarded host commands - draft, held
- [KI-TOOL-TECHNE-CLI-009](/Users/krisbrown/workspaces/knowledge-islands/tools-techne/docs/roadmap/KI-TOOL-TECHNE-CLI-009-tailscale-oauth-binding-field.md) Tailscale OAuth binding field - draft, next

#### ki-agentic-harness (CLI-shaped records)

Each of these is the standards half of a tools-ki record. Each pair is best accepted together.

| Harness record | Status | tools-ki pair |
|---|---|---|
| [KI-HARNESS-GOV-175](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-175-delegation-run-events.md) Delegation run events | draft, next | KI-TOOL-KI-CLI-123 |
| [KI-HARNESS-GOV-199](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-199-thread-identity-role-native-sessions.md) Thread identity and role | in progress | KI-TOOL-KI-CLI-145 |
| [KI-HARNESS-GOV-196](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-196-scratch-output-in-temp.md) Scratch output in temp | triage | KI-TOOL-KI-CLI-137 |
| [KI-HARNESS-GOV-200](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-200-thread-folder-closed-list.md) Thread folder closed list | triage | KI-TOOL-KI-CLI-137, 133. **Overlaps GOV-196**: both set the temporary home rule, so they are candidates to merge |
| [KI-HARNESS-GOV-201](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-201-fetch-and-machine-grants.md) Fetch and machine grants | triage | KI-TOOL-KI-CLI-134 |
| [KI-HARNESS-GOV-189](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-189-move-thread-between-hosts.md) Move thread between hosts | triage | none yet; would need `ki agent` support |
| [KI-HARNESS-GOV-195](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-195-granola-screenshots-markers.md) Granola screenshots and markers | awaiting review | KI-TOOL-KI-CLI-141 |
| [KI-HARNESS-GOV-203](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-203-git-clean-down-criteria.md) Git clean-down criteria | awaiting review | KI-TOOL-KI-CLI-140, and the mgit estate overview |
| [KI-HARNESS-OPS-005](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-OPS-005-acquire-ai-sessions.md) Acquire AI sessions | awaiting review | none on main |

**Cross-tool overlaps in one place:**

- Estate Git hygiene: [KI-TOOL-KI-CLI-140](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-140-git-hygiene-estate-audit.md), [KI-HARNESS-GOV-203](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-203-git-clean-down-criteria.md), the proposed mgit overview, and git-almanac's look and feel.
- Signed releases: [KI-TOOL-KI-CLI-125](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-125-ki-release-contract.md) and [KI-TOOL-RIG-CORE-048](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-048-signed-release-install-kind.md).
- Local versus release tools: [KI-TOOL-RIG-CLI-026](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CLI-026-per-tool-development-mode-switch.md) and [KI-TOOL-KI-CLI-143](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-143-separate-local-harness-paths.md).
- Agent temporary home: [KI-TOOL-KI-CLI-137](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-137-agent-run-tmp-home.md), [KI-HARNESS-GOV-196](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-196-scratch-output-in-temp.md) and [KI-HARNESS-GOV-200](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-200-thread-folder-closed-list.md).

### 3. Suggested burn-down order

**tools-ki**

1. Finish the rebase so local and origin agree, then push. Everything else waits on this.
2. Accept the seven awaiting review in one sitting: 123, 126, 127, 130, 133, 135, 138, plus 141 from origin. Pair 123 with KI-HARNESS-GOV-175 and 141 with KI-HARNESS-GOV-195.
3. Do 144 straight after 123, because it fixes a fault 123 introduces.
4. Work through the store chain in order: 131 needs 126 accepted, and 136 needs 131.
5. Do the thread-agent fixes 134, 137 and 145, each with its harness partner (GOV-201, GOV-196/200 and GOV-199).
6. Then 142 before 143, and 140 once the estate overview question is decided.
7. Leave 128 and 139 to the acquisition Project, and leave 125 held until releases are on the agenda.

**tools-rig**

1. Accept 047, with its restore path.
2. Deliver 042, which is already ready.
3. Batch the doctor accuracy records 052, 054 and 055 as one wave, then do 058.
4. Plan 053 and 056 together, and do 057 after mgit's selection settles.
5. Leave 026, 048 and DIST-011 held. Check whether DIST-011 is still true on vega, and cancel it if not.

**tools-mgit**

See the plan below. 017 goes first.

**tools-techne**

Nothing to do until the hold lifts, except local work on 009 if you want it.

### 4. mgit plan proposal (design only)

**What exists today.** mgit is one 3,500-line Bash 3.2 script.

- `mgit <git-subcommand>` runs Git in every selected repository, one after another.
- `-B/--bare` already means "run this non-Git command". This clashes with what you asked for, where `--bare` would be the Git pass-through. "Bare" also already means a bare repository inside mgit: sync prints "bare repository (skipped)".
- `-P/--physical` (the default) and `-L/--follow-symlinks` already exist; they are just not obvious.
- `sync` goes through the repositories strictly one at a time. Each pull is `git pull --ff-only`, so it already never merges or rebases. When a branch has diverged, it prints "pull failed" with Git's raw text instead of a clear warning.

**What git-almanac offers.** git-almanac is TypeScript/Bun and works on a single repository, and its contract rules out cross-repository aggregation. mgit cannot import its code. What mgit can reuse is its conventions:

- quiet terminal output with an end-of-run verdict
- `doctor`/`diag` style pass/warn/fail counts
- `--format json|html` inferred from the output name
- a managed report folder under `reports/`, with its own manifest
- read-only local Git with no network by default

So mgit should copy the shape, not call the tool. If you later want a browsable HTML estate page, the clean way is for git-almanac to render mgit's JSON. That requires lifting git-almanac's non-goal, which is a decision for you (ESTATE-HOME).

**Proposed command shape:**

```text
mgit [selection] [command]

selection   --territory H | --estate | --principals | -f PREFIX | -W   (unchanged)
            --physical (default) | --follow-symlinks                   (renamed help, shown in diag)

own verbs   overview   estate view: branches, obsolete branches, outstanding work
            sync       parallel fetch, classify, fast-forward only, push; diverged = warn
            register | repair | doctor | diag | structure | worktree   (unchanged)

escapes     mgit --git <subcommand ...>   always plain Git, even where mgit has its own verb
            mgit --raw <command ...>      any shell command (replaces -B)
            mgit <other git subcommand>   still passes straight through, as now

output      progress bar on stderr while working (TTY only)
            results at the end, only repositories with something to say
            -v/--verbose shows every repository; --json for tools (ki, almanac)
            -j/--jobs N bounds parallelism (default about 8)
```

**How a run flows (diagram):**

```text
  selection ──► repo list ──► parallel worker pool (-j N) ──────────────► results table
  (ki roots,     (manifest     │  each worker writes one result file      (only changed /
   manifest,      or walk)     │  to a temp dir; main loop redraws        needs-attention
   filters)                    │  one progress line on stderr             rows; --json
                               ▼                                           for machines)
                    ┌──────────┴───────────┐
          overview  │ read-only facts      │ branch, upstream, ahead/behind, dirty,
                    │ (no network)         │ untracked, stashes, worktrees,
                    │                      │ local/remote branches merged or gone,
                    │                      │ age of last commit, automation/* branches
                    └──────────────────────┘
          sync      fetch (parallel) ──► classify ──► act
                                         │ current      → count only
                                         │ behind       → merge --ff-only @{u}
                                         │ ahead        → push
                                         │ diverged     → WARN, touch nothing
                                         │ dirty/detached/no upstream → WARN, skip
```

**Obsolete branch rule.** A branch is obsolete when any of these hold:

- it is merged into the default branch, or patch-equivalent to it
- its upstream is gone
- it is an `automation/*`, `dependabot/*` or `renovate/*` branch that is already merged
- it has been idle beyond a threshold

The criteria should come from [KI-HARNESS-GOV-203](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-203-git-clean-down-criteria.md), so mgit and `ki` judge alike. mgit only shows obsolete branches and never deletes them. Proposing clean-down stays with `ki repo conform --skill ki-git` ([KI-TOOL-KI-CLI-140](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-140-git-hygiene-estate-audit.md)), which reads `mgit overview --json` instead of collecting the same facts a second time.

**Design risk.** Bash 3.2 has no `wait -n`. The worker pool would be background jobs writing result files, with a job-slot poll. This is doable and testable with bats, but it is the part most likely to grow. If it proves fragile, the fallback is a TypeScript/Bun mgit core, which is a larger, separate decision.

**Records needed (proposed, not created):**

| Order | Record | Action | What it covers |
|---|---|---|---|
| 1 | [KI-TOOL-MGIT-CLI-017](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-017-unified-external-members.md) | accept (mgit-review is lined up for it) | one member model |
| 2 | [KI-TOOL-MGIT-CLI-019](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-019-pass-through-escape-hatch.md) (MGIT-ESCAPE) | **reword** | `--git` and `--raw` escape hatches, retire `-B/--bare` with an error naming the replacement, clearer `-P/-L` help and `diag` line. Goes first among the new records because it is the breaking change, and it frees mgit to own verbs |
| 3 | [KI-TOOL-MGIT-CLI-018](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-018-estate-scale-output.md) (MGIT-OUTPUT) | **narrow** | one shared parallel runner and output layer (jobs, progress bar, results at end, changes-only, `--verbose`, `--json`) that every multi-repository command uses |
| 4 | new: Safe parallel sync | **new**, split from KI-TOOL-MGIT-CLI-018 | fetch in parallel, classify, fast-forward-only apply, push, diverged or dirty reported as a warning and never touched |
| 5 | new: Estate overview | **new** | `mgit overview` facts and table, the obsolete branch rule from KI-HARNESS-GOV-203, `--json` contract |
| 6 | KI-TOOL-KI-CLI-140 | **reword** in tools-ki (handoff) | consume `mgit overview --json` for rubric findings and conform proposals instead of its own collector |
| later | optional: git-almanac estate page | new, only if ESTATE-HOME b) | HTML rendering of mgit's JSON |

## In Progress

- `mgit-diverge` is writing its report. Its record changes are already on tools-mgit `main`, and the push is held until MGIT-ACCEPT.
- `mgit-review` is waiting for mgit-diverge to finish.
- `rig-target-speed` is still running in tools-rig.

Outstanding - no action requested now:

- The tools-ki rebase belongs to another session. Its links to KI-TOOL-KI-CLI-144 and KI-TOOL-KI-CLI-145 will not open until it finishes.
- This report is uncommitted, as briefed.

## Queries

### ESTATE-HOME - where the estate overview lives

**Context:** You want an Almanac-quality view of branches, obsolete branches and outstanding work across all repositories. Three places could own it. mgit already selects the estate and is the tool you use day to day. git-almanac has the polished renderers, but it is single-repository by contract, and cross-repository aggregation is an explicit non-goal. `ki` record KI-TOOL-KI-CLI-140 plans to collect the same Git facts for its rubric checks. Building it in more than one place means three collectors that drift apart.

**Query:** Which tool owns the estate overview facts and display?

**Options:**

a) (recommended) mgit owns it as `mgit overview`, with a terminal table and `--json`, copying git-almanac's output conventions. KI-TOOL-KI-CLI-140 is reworded to read mgit's JSON, and git-almanac stays single-repository.

b) git-almanac lifts its non-goal and gains an estate report rendered from mgit's JSON, giving an HTML page as well. mgit still collects the facts.

c) `ki` (KI-TOOL-KI-CLI-140) is the one collector, and mgit only displays what `ki` reports. mgit would then need `ki` installed for the overview.

### ESCAPE-NAMES - names for the escape hatches

**Context:** You asked for `--bare` to run the Git subcommand past mgit's own verbs, and for `--raw` to replace `-B`. Today `-B/--bare` already means "run a non-Git command". Flipping its meaning would silently turn an old `mgit --bare npm test` into `git npm test`. "Bare" also already means a bare repository inside mgit.

**Query:** Which flag names should the escape hatches use?

**Options:**

a) (recommended) `--git` (`-G`) for plain Git and `--raw` (`-R`) for shell commands. `-B/--bare` is retired with an error naming `--raw`.

b) Keep your words: `--raw` replaces `-B` now. `--bare` errors for one release, then becomes the Git pass-through.

### OVERVIEW-VERB - name of the richer status

**Context:** The estate view needs a verb. If mgit takes `status` for it, plain `mgit status` stops being Git's status, and you would type `mgit --git status` for that.

**Query:** Should the estate view be a new verb or take over `status`?

**Options:**

a) (recommended) New verb `mgit overview`, leaving `mgit status` as plain Git.

b) `mgit status` becomes the estate view, and plain Git status moves to `mgit --git status`.

### MGIT-RECORDS - capture the mgit plan as records

**Context:** The plan needs: KI-TOOL-MGIT-CLI-019 (MGIT-ESCAPE) reworded; KI-TOOL-MGIT-CLI-018 (MGIT-OUTPUT) narrowed to the shared runner and output; two new records, Safe parallel sync and Estate overview; and a handoff to reword KI-TOOL-KI-CLI-140. Once mgit-diverge has finished, this can run as one tools-mgit capture under `ki-next`, plus one handoff line to tools-ki.

**Query:** Shall a run capture these records in the order above once mgit-diverge finishes?

**Options:**

a) (recommended) Yes. After mgit-diverge, one run rewords KI-TOOL-MGIT-CLI-019 and KI-TOOL-MGIT-CLI-018, captures Safe parallel sync and Estate overview as triage in tools-mgit, and adds a KI-TOOL-KI-CLI-140 rewording handoff to tools-ki, all following the ESTATE-HOME, ESCAPE-NAMES and OVERVIEW-VERB answers.

b) Hold the records until you have reviewed this plan in conversation.

```text
ESTATE-HOME

a) mgit owns the estate overview as `mgit overview` (terminal table plus --json), copying git-almanac's output conventions; reword KI-TOOL-KI-CLI-140 to read mgit's JSON; git-almanac stays single-repository.

---

ESCAPE-NAMES

a) Use `--git` (-G) for plain Git pass-through and `--raw` (-R) for shell commands; retire `-B/--bare` with an error that names `--raw`.

---

OVERVIEW-VERB

a) Add a new verb `mgit overview` for the estate view and leave `mgit status` as plain Git.

---

MGIT-RECORDS

a) Once mgit-diverge finishes, launch one run that rewords KI-TOOL-MGIT-CLI-019 and KI-TOOL-MGIT-CLI-018, captures Safe parallel sync and Estate overview as triage records in tools-mgit, and adds a KI-TOOL-KI-CLI-140 rewording handoff to tools-ki, following the ESTATE-HOME, ESCAPE-NAMES and OVERVIEW-VERB answers.
```

```text
╭─ run report · 2026-10-17T21:34:00Z ──────────────╮
│                                                  │
│  █▀▀▄ █  █ █▀▀▀ █  █   · thread busy             │
│  █▀▀▄ █  █ ▀▀▀█  ▀█▀   · running or queued work  │
│  █▄▄▀ █▄▄█ ▄▄▄█   █    · lines below say which   │
│                                                  │
╰──────────────────────────────────────────────────╯
```

- [running] mgit-diverge - writing its report; records already on tools-mgit main
- [queued] mgit-review - after mgit-diverge
- [running] rig-target-speed - rig target speed
- [waiting] ESTATE-HOME
- [waiting] ESCAPE-NAMES
- [waiting] OVERVIEW-VERB
- [waiting] MGIT-RECORDS
- [uncommitted] this report, as briefed
