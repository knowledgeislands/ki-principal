# orca-handover - hand the Orca trial evidence to ki.prj.orca-evaluation

Work: ki.prj.mac-studio-setup (KI > Rig > Mac Studio setup), package `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.mac-studio-setup/`. Authority: ORCA-HANDOVER and ORCA-EVAL in that package's `messages.md` (Kris, 30 October): hand the Orca trial evidence and ORCA-HOST to the new Project ki.prj.orca-evaluation (`/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.orca-evaluation/`) as a line in its `messages.md`; keep what concerns the Mac Studio itself here.

## Task

1. Read `design/orca-trial.md`, the `## Orca` section and Orca-related parts of `plan069.report.md`, and the ORCA-HOST, GO-PLAN and ORCA-SKILL and KI-AGENT-DISPATCH entries in `decisions.md` (read-only).
2. Bring `design/orca-trial.md` up to date with plan069's Orca outcome: heartbeats, the recovered asynchronous ask, the hook-policy ask timing out after ten minutes, worker_done reported `failed` only because publication was blocked by the no-stash rule versus lint-staged's backup stash (resolved by Kris's bounded exception), and the trial ending here after one unit when Kris returned this Project to `ki agent` on 30 October.
3. Move the trial log into the receiving package: copy it to `+/_WORK/ki.prj.orca-evaluation/design/orca-trial.md` (create `design/` there only if that package's `work.md` or the `ki-work-package` closed list allows a `design/` folder; otherwise keep the evidence in the message line with a GitHub link pinned to the commit that holds it here).
4. Append one line to `+/_WORK/ki.prj.orca-evaluation/messages.md` in the house message-line form (`- 2026-10-30 · ORCA-HANDOVER · KI > Rig > Mac Studio setup: ...`), giving ORCA-HOST in Kris's words, the evidence location, ORCA-SKILL's intent (a proposal for an Orca launcher under ki-delegation and ki-coordination after two or three units), and that this Project ran one unit before returning to `ki agent`.

Do not edit any other file in either package. Do not delete `design/orca-trial.md` or `plan069.report.md` here; the coordinator prunes them after receipt.

## Bounds

No system change, no sudo. Never stash, rebase, reset, force-push or use `--no-verify`. Commit only the files you changed, by explicit path, in ki-principal; pull fast-forward only and push. Leave other sessions' files untouched.

## Report

Write your run report (Done, In Progress, Queries) to `/Users/krisbrown/.local/state/ki/agents/ki-prj-mac-studio-setup/orca-handover.report.md`; the launcher homes it in the work package.
