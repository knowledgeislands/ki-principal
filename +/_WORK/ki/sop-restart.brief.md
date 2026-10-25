# sop-restart brief

You are a background run for KI > SoP (`ki`), the Knowledge Islands State of play, on Sol, working in `/Users/krisbrown/workspaces/knowledge-islands/ki-principal`. Kris is asleep. Your authority is the overnight grant recorded in [decisions.md](decisions.md) under "2026-10-25 · AWAY-GRANT-SOL and STACKED-PUSH": read that section first and stay inside it. Follow `ki-delegation`, `ki-work-package`, `ki-git` and `ki-coordination`, and read `Pillars/Philosophy/Model/Processes/Work Process/Work Process.md`.

## Steps, in order

1. **Level ki-principal (STACKED-PUSH a).** `main` is 10 or more commits ahead of origin and 1 behind; the clash is in `+/_WORK/ki/messages.md`, where origin added a PARTIAL-REPOS line from hnr. Run `git pull --rebase`, resolve by keeping both sides' lines, continue, then `git push` fast-forward only. Never force-push, never skip hooks. If another conflict needs judgement, stop and report it.
2. **Take RESTART-ON-SOL**, the IMPORTANT line at the top of `+/_WORK/ki/messages.md`, alongside the top line of `+/_WORK/ki.ways-of-working/messages.md`. Follow its sub-bullets, observing SOURCE-AGNOSTIC:
   - Move the method lines it names to ki.ways-of-working's `messages.md` as one consolidated line, then remove them here.
   - For this work's half (items 1 to 8), route each line as a message to the receiving work's `messages.md` (or the owning repository's State of play), as `ki-coordination` and HANDOFF-AS-MESSAGE require, never as a roadmap record. Do what State of play's authority covers; anything needing Kris goes into `+/_WORK/ki/queries.md`.
   - Tidy State of play's own packages (item 4), pruning only inside work folders.
   - Clear the resolved lines (item 5); clear SOP-SECONDARY-MERGED only if the harness's local `main` is level with origin.
   - Record each line's disposition and remove it in the commit that names it.
3. **VA-HIGH a)**: send TENDING-FOLD, SIZE-LABEL and PRODUCT-RECORDS (see `queries.md` Parked, "From va-consolidate") as messages to their owning works, and mark them sent in `queries.md`.
4. **PROJECT-CLOSE a)**: prepare the retirement of [Estate factorisation](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/estate-factorisation.md) as a design note in `+/_WORK/ki/design/estate-factorisation-retirement.md`, covering the routing the query lists. Do not edit `Streams/Projects/`, do not close anything and accept nothing.
5. **Blind reviews**: for every remaining medium- or low-confidence query bound for Kris, and every destructive one (SITE-HOOKS, PRE-REBASE-REF), run one masked blind review (Context and Query only, options unranked) on the strongest model at high effort, under Codex where you can (`ki agent launch --runtime codex`). Record the outcomes in `queries.md`.
6. **Morning list**: write Kris one prioritised list of what remains for Kris, with the ACCEPT-BUNDLE sweep first, in your report.

## Limits

No acceptances; no changes to `Admin/`, `Pillars/` or `Resources/`; no deletion beyond work-folder pruning; no external publication beyond pushing ki-principal and any repository you committed to, fast-forward only. Leave `tools-ki` alone. Never touch `+/_Voice Notes/`. Commit by explicit path with Conventional Commit subjects `docs(work): ki …`, ending with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. Pull with rebase before each push.

## Report

Write `sop-restart.report.md` beside this brief: Done, In Progress and Queries in the `ki-coordination` owner-report shape, every query in full with Context, Query and Options, recommended first with confidence and reason, plus the prioritised morning list.
