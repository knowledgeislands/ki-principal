# Brief: accept-awaiting

You are a detached background agent for KI > SoP, the territory's State of play coordinator (work package `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/`). Kris, 19 October: "I think we should accept all the awaiting reviews." That is Kris's human approval, under `ki-accept`, for every record in Awaiting review.

## Task

1. Read `ki-accept`, `ki-work-roadmap`, `ki-repo-kb-streams` and `ki-git`, and the territory inventory in `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Known Lands.md`.
2. List every work record whose status is Awaiting review in each territory repository with a roadmap (`docs/roadmap/` or `Streams/Roadmap/`), including the chezmoi source at `/Users/krisbrown/.local/share/chezmoi`. Use `ki` roadmap commands where they work; otherwise read front matter.
3. Per repository, before writing: run `git status` and `ki agent status`. If a record file has uncommitted changes, or a running agent's step names that record, do not touch it: add one line to the owning work's `+/_WORK/<id>/messages.md` in ki-principal, `- 2026-10-19 <HH:MM BST> · from ki · ACCEPT-AWAITING: Kris approved accepting <ID>; accept it under ki-accept when your change lands.`
4. Accept every other record as done under `ki-accept`, Kris's approval standing for each, recording that approval in the record as the skill requires. Do not prune, do not cancel, do not push. Commit per repository by explicit path, subject `docs(roadmap): accept Awaiting review records, Kris approved`, letting hooks run. If a hook refuses, fix only what the refusal names in the records you touched; if you cannot, leave that repository uncommitted and report it. If the index is locked, wait and retry.

## Report

Report to the path your run packet names, as an owner report: a table of records accepted per repository with commit, records routed and why, and any refused or skipped, with the reason. Raise a query only for a decision Kris must take.
