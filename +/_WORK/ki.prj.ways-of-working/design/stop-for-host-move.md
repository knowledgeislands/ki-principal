# Stop for a host move

Kris is moving from terra to sol. Each coordinating thread follows this page to bring its work to a portable rest on terra and pick it up on sol. It works under today's `ki-coordination` standard, using the steps under Putting work on hold, and it matches the agreed work state machine ([work-state-machine.md](work-state-machine.md)): this is the `stop` arc to At rest with reason `moving`, and on sol the `resume` arc into Bootstrap. Kris set the goal under MOVE-READY-GOAL and the test under DRAIN-MEANS and TRANSITION-CONDITIONS on 29 October 2026.

## What "stopped for a move" means

The work is stopped only when deleting the local checkout would lose nothing. In Kris's words: "there's no longer anything which is specific to a machine that might get lost if I was to delete the repository". Everything the work needs must be committed and pushed to origin, in every repository the work or its runs touched.

The stop prompt below is Kris's `pause` for your work, whatever its current state.

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

Project and regular work stops before its territory's State of play (`*.sop.*`), which stops last in its territory, as the standard's territory hold sets.

## Prompts for threads

Kris gives these to threads himself; nothing is broadcast. Each is self-contained.

### Structure

```text
The work now follows a work state machine. Read it: /Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/work-state-machine.md

Start (wp) -open-> Bootstrap -ready-> Working.
Working: from Start (work), pick up when the work is clearly defined, or refine
it when it needs clarity; then cycle inform, receive, direct, receive; conclude
to End (work).
From End (work): -stop- (drain, portable) -> At rest (holding, waiting or moving),
and from At rest -resume-> Bootstrap; or -finish-> Finished.

Roles: supervisor, worker and orchestrator. Any AI or human can hold any role.

Today's `state.md` values map onto it:
- with-worker, handoff-to-supervisor, with-supervisor, handoff-to-worker: inside Working.
- handoff: At rest, waiting.
- on-hold: At rest, holding or moving.
- finished: Finished.

The stop arc and its postconditions for a host move are in:
/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/stop-for-host-move.md

Keep working under ki-coordination as before; read both notes, then carry on.
```

### Stop for the move

```text
Stop this work for the host move to sol: conclude, then take `stop` to At rest,
reason moving, following /Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/stop-for-host-move.md

Prove every postcondition, in every repository the work touched:
- Nothing only local: no uncommitted change, no unpushed commit, no unpushed
  branch; merge or push each.
- Run worktrees removed once spent; `git fetch --prune` run.
- No stash and no local-only ref holding the work's content.
- Every open PR recorded in `state.md`.
- Runtime-only run reports homed in the package or their outcome homed.
- Work package files tidied: content in its purpose folders, spent reports
  and briefs pruned.
- Open queries parked under `## Parked` in `queries.md`.
- `state.md` set to `state: on-hold`, `hold.reason: moving to sol`,
  `hold.release: resume on sol`; committed by explicit path and pushed
  fast-forward only.
Name another session's files in the report; never touch them.
If any check fails or cannot run, stay put and report NOT DRAINED with the
blocker. Otherwise give the hold report.

On sol: fetch, check each repository is level with origin, then:
Re-bootstrap as <id> under ki-coordination.
```
