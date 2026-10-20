# Burn down tools-git-almanac's roadmap overnight

Kris, 20 October: "getting the roadmaps down to zero for all of tools, all of MCP, and all of the apps ... keep you know motoring through them, committing and pushing as you go." Nobody else is working on any machine tonight. Repository: `/Users/krisbrown/workspaces/knowledge-islands/tools-git-almanac`, roadmap in its `docs/roadmap/`.

First, wait until `/Users/krisbrown/.local/state/ki/agents/ways-of-working/apply-sweep.status` ends with `DONE` (check every minute), then pull.

Work through every open record, in this order: awaiting review and in progress, then Ready, then Now and Next drafts, then the rest.

- Work complete but not review-ready: run its gates, complete the review packet under `ki-work-roadmap`, set awaiting review.
- Ready or plannable within the record's scope: plan under `ki-work-roadmap` where needed, deliver under the repository's `AGENTS.md` and `ki-engineering`, in a Git worktree on branch `run/burn-tools-git-almanac`; run every gate; rebase and fast-forward your branch into local `main`, remove the worktree, and push `main` fast-forward only. Set the record awaiting review with a full packet.
- Needs Kris's own eyes, an attended or live action with side effects, credentials, publication, or a decision nothing covers: leave it and say why.
- Stale, superseded or duplicate: do not cancel; list it with evidence.
- Do not accept or prune: the coordinator gets an independent review and accepts.
- Stuck after a fair attempt: stop that item, record where, move on, and report the question with your recommendation.

Follow-ups never become records (CAPTURE-GATE): add a line to the owning work's `messages.md` in `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/<id>/` or an `Idea:` line on the Project note, and list them. Never `--no-verify` or force-push; push only commits made tonight by this programme, and if other sessions' commits are stacked, stop pushing that repository and say so. HOOK-GUARD: no `ki repo conform` without `--dry-run`. tools-ki is edited only in a worktree (`ki` runs from its primary checkout). Work outside the Techne Programme Focus in tools-techne stays an idea. British English, ASCII hyphens.

Report per record: state before and after, commits, gates, pushed or not, and anything Kris must do.
