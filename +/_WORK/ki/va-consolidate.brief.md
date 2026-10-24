# va-consolidate brief

Run for KI > SoP (`ki`), under VA-CONSOLIDATE in [decisions.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/decisions.md) (Kris, 24 October 16:46 BST). Read that entry first: it holds Kris's instruction and his seven-point model word for word.

## Goal

Consolidate every line from VA > SoP (va) into one clear, coherent set. Group the lines by theme and merge the duplicates. Note any conflict with the coordination standard or the Work Process note. Propose the records or standard changes each group needs, and bring them back to Kris as queries. Kris's quoted words are the source: keep them verbatim in every consolidated line.

## Sources

The va lines are in two queues. Read both in full:

- `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/messages.md`. The va lines are METHOD (Tending), TENDING-SIZES, TENDING-ROUND-2, TENDING-GUIDANCE-OVERLAP, SUMMARY-OUTSTANDING (this one includes the Tending working-area check), TENDING-ROADMAP, COORD-COMMANDS, SUMMARY-SINCE-MARK, SOP-PROJECT-CARE and SINGLE-THREAD.
- `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/messages.md`. The va lines are Always Use HTTPS (23 October 20:30), the ki-repo `node_modules` ignore rule (23 October 23:05), SANCTUARY-STAGE5, COV-1-SUBAGENTS, HARNESS-ORIENTATION, BIND-2, BIND-2-DONE, COV-1-NOT-LIVE and SOP-SECONDARY-MERGED.

Where the standards are silent, the va authority behind each line is in `/Users/krisbrown/workspaces/valle-armonia/va-principal/+/_WORK/va/decisions.md`.

Read the lines against these four sources:

- The coordination standard: `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md` and the skill's `SKILL.md` (its Operating modes).
- The work package standard: `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-work-package/references/standards-work-package.md`.
- The Work Process note: `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Processes/Work Process/Work Process.md`.
- The Tending design notes: `+/_WORK/ki.ways-of-working/design/tending.md` and `tending-round2-notes.md`, and the sizing note `roadmap-sizing-and-burn-down.md`.

The harness primary checkout may be on a branch other than `main`. Read `main` with `git -C <harness> show main:<path>`, and say which revision you read.

One line is related but not from va: COORDINATOR-HOST, from Rig > chezmoi > SoP. It touches model point 4 (metadata) and the standard's rule that no work package names a host. Treat it in the same group and mark it as not from va.

## What to produce

1. `+/_WORK/ki/design/va-consolidation.md`, with one section per theme. Each section carries:
   - the consolidated line or lines, keeping Kris's quoted words verbatim, with the source tags they replace;
   - what is already done, citing the commit or file, so the line can be cleared;
   - each conflict with the coordination standard, the work package standard or the Work Process note, citing the section;
   - each conflict with Kris's seven-point model;
   - the proposed change: a standard edit (which skill, which section, in one or two sentences) or a record (which repository, under `ki-next`, and only where CAPTURE-GATE allows: a blocker, a defect seen failing, or a Kris request);
   - which work should carry it: ki.ways-of-working for method design, State of play, or another named work.

   Separate the method lines from the product and defect lines (HTTPS, `node_modules`, Sanctuary, harness orientation), and mark the lines that are already cleared (BIND-2, COV-1, SOP-SECONDARY-MERGED).
2. `+/_WORK/ki/va-consolidate.report.md`, an owner report under `ki-delegation`.
   - Queries: one `###` per decision Kris must make, under a stable mnemonic tag, with Context, Query and Options.
   - Option a) is recommended and states its confidence and a one-line reason.
   - Group the queries so there are at most eight.
   - Mark each medium- or low-confidence query `needs blind review`. The coordinator runs that review; you do not.

## Authority and limits

- Read-only apart from the two files above. Change no standard, skill, Work Process note or record, and create no record (CAPTURE-GATE).
- Remove or edit no `messages.md` line in either package, and leave `ki.ways-of-working`'s package untouched.
- Commit only the two files, staged by explicit path under `ki-git`, with the subject `docs(work): ki va-consolidate`. Do not push.
- Keep British English and ASCII hyphens. Link every record identifier by absolute path, or to its pinned GitHub revision where it has been pruned.
