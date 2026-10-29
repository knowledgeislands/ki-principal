# [Knowledge Islands model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Initiatives/knowledge-islands-model/knowledge-islands-model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working/ways-of-working.md) › drain-form

**Run report at 16:08 BST · last mark 23:22 BST**

---

## Done

- **Drain form landed in the harness and pushed** (`ki-agentic-harness` `5af53e4e`, fast-forward onto `2f85c068`). It captures Kris's DRAIN CHECK of 2026-10-15, "Add Drain as a thread state and a report form ("Drain report") beside Summary, Recap, Full summary and Re-bootstrap, and add the DRAINED footer frame below beside REST, BUSY and DONE. A drain report has no reply block and no Context/Query/Options; the queries live in the checkpoint." From now on, every thread that re-reads ki-pmo or gets the hook line uses it.
- **[The ki-pmo standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-pmo/references/standards-pmo.md)** now has the following:
  - a new section, "Draining a thread", that quotes Kris's five steps and the BUSY fallback word for word;
  - drain in the glossary, a thread state beside at rest, busy and done;
  - the drain report as the fourth report form, in the report-forms table, the owner-report sections rule, the practices list and the Close rule. Its form line is `**Drain report at <local time> · mark <local time>**`, its sections are Done, Parked and Left over, and it has no reply block;
  - in the Banner section, the DRAINED frame, its three-item list and the drain resume line, all exactly as Kris drew them.
- **Every surface that lists the forms or frames was updated to match:** the hook line and the ki-coordinator output style (both regenerated from the standard), the output-style generator (it now renders the two new blocks), the PMO-6 rubric item with its regenerated `rubric.md`, the ki-pmo skill description and notes, the source review, the harness spec and the regenerated skills catalogue.
- **Frame width is checked by script:** all 28 framed lines in the standard and all 21 in the output style are 52 code points. No glyph was changed. Kris drew the top border with the 22-character placeholder `<YYYY-MM-DDTHH:MM:SSZ>`, which makes that line 54. With a real 20-character time the `─` fill grows by two (12 for `drain report`), which brings it to 52. The banner test now asserts this.
- **Checks:** `bun run test` passed (1189 tests, 0 failures). `bunx tsc --noEmit` is clean. `ki repo audit --skill ki-skills` and the pre-commit gate both show WARN with no failures: the two warnings are stale refresh dates in other skills' sources, not this change. `ki repo audit --skill ki-pmo` fails only on PMO-7 findings in Kris's untracked `+/_THREADS/skill-reviews/` reports. They link KI-HARNESS-GOV-193 to `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-193-area-diagrams-with-html.md`, and that file does not exist. That is a fleet finding, not part of this change.
- **chezmoi needed no change.** Its `dot_claude/output-styles/symlink_ki-coordinator.md.tmpl` symlinks to the harness file, and `.chezmoidata/coordinator-hook.yaml` runs the hook from the harness checkout. Both are therefore live on terra already, with no `chezmoi apply`. The Codex trust hashes cover only the hook entry, which did not change, so they stay valid.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- **Nothing to apply on terra.** On sol, the harness checkout needs pulling to `5af53e4e` or later before the first resumed thread re-reads ki-pmo.
- **Left untouched:**
  - the untracked `+/_THREADS/` in the harness (Kris's skill-reviews);
  - Kris's layout files under `docs/diagrams/` and `ki-repo-harness`, none of which were dirty at commit time;
  - in ki-principal, another session's uncommitted changes to `+/_THREADS/mac-studio-bootstrap/chezmoi-fix.report.md` and `+/_THREADS/ways-of-working/decisions.md`.
- **This report is uncommitted** in `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/ways-of-working/`, for the thread to commit by explicit path with its folder.

## Queries

### DRAIN-STATE - where a drained checkpoint records its state

**Context:** Kris's step 3 says "set running to nothing and state to drained". A checkpoint's frontmatter `state` must stay `active`, because `ki-checkpoint` RESUME checks it and the thread on sol resumes from that record. So the standard writes the state as `Running: nothing` and `State: drained` lines in `Current state`, beside `Mark:`. It also says the resumed thread clears those two lines at its first checkpoint update, a step I added that Kris did not state. **Query:** Should a drain record its state as those two lines in `Current state`? **Options:** a) (recommended) keep it as landed: `Running: nothing` and `State: drained` in `Current state`, the frontmatter stays `active`, and the resumed thread clears the two lines b) add `drained` as a frontmatter state in the ki-checkpoint standard, which also changes RESUME validation

### DRAIN-HOST - the host name in the drain resume line

**Context:** The drain resume line was captured exactly as Kris wrote it: "Resume <label> on sol from its checkpoint under current ki-pmo and ki-delegation since <mark>: ...". It names sol, which fits today's move from terra. A later move between other hosts would need a different word. **Query:** Should the drain resume line keep "on sol" word for word? **Options:** a) (recommended) keep "on sol" for today's move and generalise to `on <host>` only when a different move needs it b) change it now to `on <host>`, with the host filled in like the label and the mark

```text
DRAIN-STATE

keep it as landed: Running: nothing and State: drained in the checkpoint's Current state, the frontmatter state stays active, and the resumed thread clears the two lines at its first checkpoint update

---

DRAIN-HOST

keep "on sol" in the drain resume line for today's move; generalise to on <host> only when a different move needs it
```

```text
╭─ run report · 2026-10-15T15:08:13Z ──────────────╮
│                                                  │
│  █▀▀▄ █▀▀▀ █▀▀▀ ▀▀█▀   · thread at rest          │
│  █▀▀▄ █▀▀  ▀▀▀█   █    · nothing running         │
│  █  █ █▄▄▄ ▄▄▄█   █    · nothing queued          │
│                                                  │
╰──────────────────────────────────────────────────╯

- [at rest] nothing running or queued
- [waiting] DRAIN-STATE
- [waiting] DRAIN-HOST
- [uncommitted] drain-form run report in the ways-of-working thread folder
```

```text
Resume KI Model: ways-of-working under current ki-pmo and ki-delegation since 23:22 BST: re-bootstrap, mark, fresh summary with carried-forward open points, take stock, restart authorised work, then banner.
```
