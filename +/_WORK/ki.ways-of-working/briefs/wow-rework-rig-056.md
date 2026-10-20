# wow-rework-rig-056

Goal: rework KI-TOOL-RIG-CORE-056 after its failed independent review. The review commit 4efcee6b sits on branch run/wow-accept-rig-056 in the worktree /Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-accept-rig-056.work/review (tools-rig), not yet on main because tools-rig's full audit is red on the pre-existing SHELL-HOOK finding (routed to ki.tools-burndown as RIG-056-INTEGRATE). The review report is ~/.local/state/ki/agents/ways-of-working/wow-accept-rig-056.report.md.

Authority: Kris, 20 October 2026 22:03 BST: "Is there anything more that you can do by yourself without me? ... roadmap down".

Steps: work on top of 4efcee6b, in a new worktree branched from run/wow-accept-rig-056. Fix the three wording defects in the record's Discussion: no claim may assert exclusive access, durability across changes or restart behaviour beyond what the read-only evidence shows; relabel those as inferred or gap. Keep the report-only recommendation if it still follows. Read-only evidence only: no defaults writes, restarts, app launches or protected-container probes. Move the record back to awaiting review with a Review response in Discussion. Commit by explicit path on that branch. Do NOT fast-forward main or push: the red-gate rule blocks integration until RIG-056-INTEGRATE lands; leave the branch and worktree in place and name them in the report. Never --no-verify.

Constraints: British English, ASCII hyphens only. Create no new records.

Report: each defect and how it was fixed, branch name, commit SHA, worktree path.
