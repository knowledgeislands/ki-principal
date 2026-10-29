# Stop for a host move

Kris is moving from terra to sol. Each coordinating thread follows this page to bring its work to a portable rest on terra and pick it up on sol. It works under today's `ki-coordination` standard, using the steps under Putting work on hold, and it matches the agreed work state machine ([work-state-machine.md](work-state-machine.md)): this is the `stop` arc to At rest with reason `moving`, and on sol the `resume` arc into Bootstrap. Kris set the goal under MOVE-READY-GOAL and the test under DRAIN-MEANS and TRANSITION-CONDITIONS on 29 October 2026.

## What "stopped for a move" means

The work is stopped only when deleting the local checkout would lose nothing. In Kris's words: "there's no longer anything which is specific to a machine that might get lost if I was to delete the repository". Everything the work needs must be committed and pushed to origin, in every repository the work or its runs touched.

This message is Kris's `pause` for your work, whatever its current state.

## Steps, in order

1. **Read IMPORTANT messages** in your `messages.md` first, and act on them.
2. **Cancel every wake** this session holds: waiters, monitors, loops and scheduled checks.
3. **Drain.** Launch nothing new. Let any run that will finish within about 15 minutes finish. Stop any other at a safe point, record in `state.md`'s next steps where it stopped and how to restart it, and keep its brief in `briefs/`.
4. **Receive** every finished run: copy its queries into `queries.md` and home its outcome in a record, the decisions log, the package or a commit.
5. **Run the eight portability checks** in every repository the work or its runs touched:
   1. Nothing of this work is running, queued or scheduled.
   2. No uncommitted change of this work: commit by explicit path, pull fast-forward only, push fast-forward only. Never force, never `--no-verify`.
   3. Every run worktree removed once its work is on origin.
   4. Every branch either merged into `main` or pushed to origin.
   5. Stale remote-tracking branches pruned with `git fetch --prune`.
   6. No stash and no local-only ref holding this work's content.
   7. Every open PR recorded in `state.md` as merged, closed or named for its owner.
   8. Every runtime-only report homed: anything in `~/.local/state/ki/agents/<run>/` needed to resume is copied into the package, or its outcome is homed. Never copy a secret.
6. **Park** every open query under `## Parked` in `queries.md`, with its tag, one line of context and its recommended option. Strike a mark, strike decisions that have a durable home, and prune the work folder.
7. **Set the state.** In `state.md`'s front matter: `state: on-hold`, `hold.reason: moving to sol`, `hold.release: resume on sol`, and `since` with the time. Write the next steps for picking the work up on sol.
8. **Commit and push** the package by explicit path with the subject `docs(work): <id> hold, paused`, then push fast-forward only.
9. **Give the hold report** and nothing else: the report heading, the form line `**⏸️ On hold · Hold report at <local time> · mark <local time>**`, `## Done` with one line per repository, `## Parked` and `## Left over`, then the On hold banner with `⏸️ drained · 🅿️ <n> queries parked`, `[parked]` and `[release] resume on sol`, and the thread line last.

## If anything fails

If any step or check fails, or cannot be run (for example PR state when a provider call is not allowed): do **not** set `on-hold`. Report `NOT DRAINED` in `## Done` with the blocker in one line, leave everything else in place, and keep the work in its current state, marked blocked. A check that cannot be run is unknown, never passed.

Another session's uncommitted file or commit is named in the report and never touched.

## On sol

1. In each repository the work touches: `git fetch`, then check local `main` is level with `origin/main` (pull fast-forward only if behind; stop and report on divergence).
2. Open the thread with: `Re-bootstrap as <id> under ki-coordination.`
3. The coordinator moves the parked queries back to `## Open` and starts from `state.md`'s next steps.

## The message to send

One line, added to the top of each live work's `messages.md`, with `<id>` and the label filled in:

```markdown
- IMPORTANT · 2026-10-29 · HOST-MOVE · KI > Model > Ways of working (ki.prj.ways-of-working): Kris is moving hosts from terra to sol. Stop this work for the move now by following [Stop for a host move](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/stop-for-host-move.md): drain, run the eight portability checks, park queries, set `state: on-hold` with `hold.reason: moving to sol` and `hold.release: resume on sol`, commit `docs(work): <id> hold, paused`, push and give the hold report; if any check fails, report NOT DRAINED and leave everything in place. On sol: fetch, level check, then `Re-bootstrap as <id> under ki-coordination.`
```

## Live works to receive it

Every `+/_WORK/*/state.md` under `/Users/krisbrown/workspaces/` not on hold or finished, as of 29 October 2026, 22:25 GMT:

| Work id | Repository | State |
| --- | --- | --- |
| hnr.prj.5g-emerge-p2ms3 | hnr-principal | handoff-to-supervisor |
| hnr.prj.5g-emerge-phase2 | hnr-principal | handoff |
| hnr.prj.5g-emerge-phase3 | hnr-principal | with-worker |
| hnr.prj.developer-experience-and-build-pipelines | hnr-principal | handoff-to-supervisor |
| hnr.prj.m365-tenant | hnr-principal | with-worker |
| hnr.prj.product-management | hnr-principal | handoff-to-supervisor |
| hnr.prj.site-eit | hnr-principal | with-supervisor |
| hnr.prj.site-hr | hnr-principal | handoff-to-supervisor |
| hnr.prj.site-pt | hnr-principal | handoff-to-supervisor |
| hnr.reg.email-routing | hnr-principal | with-worker |
| hnr.sop.5ge | hnr-principal | handoff-to-supervisor |
| hnr.sop.main | hnr-principal | handoff-to-supervisor |
| hnr.sop.sites | hnr-principal | with-worker |
| ki.prj.chezmoi | ki-principal | handoff-to-supervisor |
| ki.prj.observatory | ki-principal | with-supervisor |
| ki.prj.ways-of-working | ki-principal | handoff-to-supervisor (the sender; stops last) |
| ki.sop.main | ki-principal | with-supervisor |
| personal.reg.acquire-intake | personal/acquire | handoff-to-supervisor |
| personal.reg.email-routing | personal-principal | with-supervisor |
| personal.reg.rig-sol | personal-principal | with-supervisor |
| personal.reg.rig-terra | personal-principal | handoff-to-supervisor |
| personal.reg.rig | personal-principal | handoff-to-supervisor |
| personal.reg.tower | personal-principal | with-supervisor |
| personal.sop.main | personal-principal | with-supervisor |
| va.sop.main | va-principal | with-supervisor |

Project and regular work stops before its territory's State of play (`*.sop.*`), which stops last in its territory, as the standard's territory hold sets.
