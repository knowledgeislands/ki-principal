# [Knowledge Islands model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Initiatives/knowledge-islands-model/knowledge-islands-model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working/ways-of-working.md) › restart-standard

**Run report at 23:04 BST · last mark 22:34 BST**

---

## Done

Acting on RESTART-AGREE, as Kris gave it on 17 October: "Agree the restart design section 1 as written: one ki-agentic-harness run, after any QUIET-STYLE run, writes the section 1.4 wording into ki-pmo, ki-delegation and ki-checkpoint, regenerates the surfaces with ki dev skill generate ki-pmo --write and pushes; ways of working then converts its checkpoint, writes READY into the state-of-play Messages block and tells me." Also acting on RUN-HYGIENE: "each thread fixes its checkpoint form and adds role on its FIRST-STEP line at restart, and the generic brief footer gives way to an explicit push rule in the brief."

- ki-pmo: section 1.4 of the [restart design](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/ways-of-working/restart.report.md) is now in the standard, re-based on the current text after the heading and quiet-tools changes. "Directions from the state-of-play thread" is now "Messages between threads": any coordinating thread in the same Capital may send a line, and state of play still routes Kris's dumps and is the only route to another Capital. Bootstrap gains the messages step, with `FIRST-STEP` lines first. Picking up a thread makes the resume line the only restart prompt, with `READY` lines setting the restart order. Commits now happen at each resting point, mark and hold. A drain copies open queries and stopped briefs into the checkpoint and sweeps for leftovers.
- ki-pmo, folded in where section 1.4 depends on it: every link to the renamed section is updated. The Thread types paragraph no longer says a coordination thread may send messages only through state of play. The hook line and the output-style source now say "Messages block ... FIRST-STEP first".
- ki-delegation: the Run packet table now lists the runtime files the launcher already writes. Run reports are written to the state folder and copied into the thread folder only while they are still open. The decisions log is now committed at each resting point, mark and hold. Authority tiers says an explicit push rule in a brief overrides the footer's no-push line. Coordinating threads says each thread adds `role` and fixes its checkpoint form on its `FIRST-STEP` line at restart.
- ki-delegation, beyond the literal brief: `rules-none.md` now also says the task's push rule overrides it. Without that, an agent reading only the footer would still see "never push". The footer rubric's required wording is unchanged.
- ki-checkpoint: a line added to another thread's messages block is not an update and does not advance `updated_at`. A coordinating checkpoint gains `role` at the latest on its `FIRST-STEP` line.
- Regenerated the hook line and the `ki-coordinator` output style with the tools-ki `ki` binary. Updated the banner and hook tests and added a sources entry to each of the three skills.
- Checks: `bun run test` passed, after the hook test was updated to the new hook line. `bunx tsc --noEmit` passed. The ki-delegation and ki-checkpoint audits passed. The commit gate passed.
- ki-pmo audit: this fails with four PMO-7 unlinked or missing record links in `+/_THREADS/skill-reviews/`, which this change does not touch. It also gives one PMO-9 warning: briefs left in that folder. These are fleet findings, not failures of this change.
- Committed `0e4cdebd docs(ki-pmo): adopt the restart standard for state, messaging and restart prompts` in ki-agentic-harness. Pushed fast-forward with only this commit stacked; the harness is level with origin.
- Committed this report alone in ki-principal and pushed it fast-forward under ROUTINE. It carried two commits from another session beneath it: `6be6d75 docs(threads): log the thread-states direction` and `21d5c8d docs(threads): correct the thread-states decision time`.
- For tools burndown: the generic Rules footer text is not in tools-ki. It lives in the harness asset `skills/governance/ki-delegation/assets/rules-none.md`, and tools-ki only names that file in a test. So the footer itself needs no tools-ki change.

## In Progress

Nothing is running for this run.

### Outstanding - no action requested now

- The Run packet section still says "`ki agent` is the only writer of the knowledge files there". Until tools-ki changes its default report path, the launcher and briefs still write reports straight into the thread folder. That tooling is already inside [KI-TOOL-KI-CLI-137](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-137-agent-run-tmp-home.md) through tools burndown. The sentence should be revisited when it lands.
- The `skill-reviews` thread folder needs its PMO-7 links fixed and its briefs moved out by its owning thread.
- Next, under RESTART-AGREE, the ways-of-working thread converts its checkpoint, writes `READY` into the state-of-play Messages block and tells Kris.

## Queries

No outstanding queries.

```text
No reply needed.
```

```text
╭─ run report · 2026-10-17T22:03:23Z ──────────────╮
│                                                  │
│  █▀▀▄ █  █ █▀▀▀ █  █   · thread busy             │
│  █▀▀▄ █  █ ▀▀▀█  ▀█▀   · running or queued work  │
│  █▄▄▀ █▄▄█ ▄▄▄█   █    · lines below say which   │
│                                                  │
╰──────────────────────────────────────────────────╯
```

- [running] thread-states - thread-states design
- [queued] harness-records - after restart-standard
- [committed] ki-agentic-harness 0e4cdebd, pushed
