# wow-tidy-principal - tidy ki-principal's working areas and work packages

## Authority

Kris, 2026-10-22 22:50 BST: "Can you take a mark at this point and can you go over the work folder? I think you can delete the work review one for example and then also just tidy up the inbound and outbound working areas in general. But for example, I can see a diagram/slash change management skills that probably needs to be tidied up, all of the work packages under the plus slash underscore work needs tidying up. So just get as much tidy as you can. You don't need to check with me, you just need to make it happen on those ones and get everything fully committed". Kris holds exclusive KI control from 14:03 today, so no other coordinator is working these packages.

## Task

In `/Users/krisbrown/workspaces/knowledge-islands/ki-principal` (the primary checkout, branch `main`), leave the working areas tidy and everything committed:

1. Delete `+/_WORK_REVIEW/` after checking that nothing in it is unique work that a live package still needs; record anything worth keeping in its owning package first.
2. Tidy `+/diagrams/` (including `change-management-skills`, a finished render whose source lives in this work's `design/`): delete delivered or superseded artefacts; keep only what a live package still uses.
3. Tidy `+` and `-` generally (`+/_TRADES`, `-/_DIGESTS`, `-/_TRADES` and loose files), keeping each area's index or README. Route triage that has an obvious home under Routing Rules (`Admin/Governance/Conventions/Admin Conventions/Routing Rules.md`); delete what is stale, delivered or duplicated in Git history; list anything you cannot place. Never touch `+/_Voice Notes/`.
4. For every package under `+/_WORK/<id>/`, prune under the `ki-coordination` standard's pruning rule: keep the five package files, open briefs, reports whose outcome is not yet homed, and live design notes; delete received briefs, reports whose queries are answered and whose outcome has a home (a record, a decisions log, the package, a commit), and graduated or superseded design notes. In each package's own `decisions.md`, strike decisions that a durable home now wholly carries. Do not change any package's `state.md` state or queries. In `ki.ways-of-working`, keep `briefs/wow-tidy-principal.md`, `briefs/wow-commit-territory.md` and the reports `wow-provenance-receivers`, `wow-rev-receivers`, `wow-rereview8-toolski-*` and `wow-toolski-fix-8b`.
5. Receiver copies (Kris answered RECEIVER-COPIES a) and BASELINE-REPORTS a)): using the manifest in `/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-provenance-receivers.report.md`, remove the 388 verification copies, keeping the three linked ones (burnrig, acceptgit, mgit-prune) and the three acquire copies in `/Users/krisbrown/workspaces/personal/acquire/+/_WORK/kb.regular.acquire-intake/` are among the 391 and go too unless linked; first recheck that each file is unchanged, its runtime source is retained, and nothing links to it. Restore the nine `+/_WORK/ki.baseline-rollout/*.report.md` files from `HEAD` after rechecking that they still match the manifest. Step 4's pruning may then remove them too if their outcome is homed.
6. Commit everything left uncommitted in ki-principal in coherent commits by explicit path (`docs(work): ...`, `docs(triage): ...` and so on), each passing the hooks. If a dirty file is clearly mid-edit by something you cannot identify, leave it and name it.

## Bounds

ki-principal primary and the three acquire files only. Do not edit `Admin`, `Pillars` or `Resources` content beyond routing a triage note to its obvious home. No push, no `--no-verify`, no force, no history rewrite. Do not touch live agent state under `~/.local/state/ki/`.

## Report

First line `VERDICT: DONE|PARTIAL · confidence <level> - <one line>`. Then per area what was deleted, routed, restored and kept, the commits made, anything left uncommitted and why, and anything you could not place, as queries.
