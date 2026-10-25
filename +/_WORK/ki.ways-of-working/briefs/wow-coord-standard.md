# wow-coord-standard

## Goal

Make the ki-coordination changes Kris approved on 25 October, in ki-agentic-harness, and propose (not make) a commit-cadence rule.

## Approved, in Kris's answers

- REBOOT-SHAPE a) "Full report": the re-bootstrap report is a full owner report: heading, `Re-bootstrap at` form line, `## Done` (role and where the work stands), `## In Progress` (what is running), `## Queries` (every open query in full), then the banner. Remove "in three lines" / "three-line report" from the standard (Bootstrap step 7, Report forms) and its templates; hook rule 4 names re-bootstrap and full summary.
- GAP-SUMMARY a) "30-minute trigger": the first reply after 30 minutes or more without an owner message, while queries are with the owner, answers the message and then gives the Summary with every open query in full; the style carries the same trigger.

## Do

- Edit `skills/change-management/ki-coordination/references/standards-coordination.md`, `SKILL.md` where it repeats the rules, and the output style and hook line sources; run `ki dev skill generate ki-coordination --write`; run the banner test (`scripts/banner.test.ts`) and `ki repo audit --skill ki-coordination --repo .`; update the source review in `references/sources.md` as REFRESH requires.
- Commit in ki-agentic-harness by explicit path. Under PRFLOW and Kris's away grant to 09:00 BST, push straight to `main` fast-forward only, after a fresh `git pull --rebase`, once tests and audit pass, and only if your own commits alone are stacked; never force, never `--no-verify`. If anything fails, leave it committed locally and say so.
- The `ki agent prompts` opener text lives in tools-ki (`src/core/work/prompts.ts`): do not edit it; say in your report what wording it needs.
- COMMIT-CADENCE, propose only: Kris, 25 October: "when there's a lot of changes in the work folder, the work is sitting there for a while and it's not getting committed. This makes it really difficult to keep the Git repositories in sync with the origin and other things which are also modifying the work packages because it's not regularly getting updates, pushes, and pulls." Read the standard's committing, pruning and Pushing beneath other sessions sections, and draft the smallest rule change (e.g. commit, pull with rebase and push the work folder at every package write and every wake; how a coordinator handles other sessions' message commits stacked beneath its own). Return it as a query with exact wording; do not edit it in.

## Rules

Work only in ki-agentic-harness. Do not touch ki-principal packages, tools-ki or chezmoi. Do not launch agents. Report in the owner-report shape.

## Output

Report as your final message and in `/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-coord-standard.report.md`.
