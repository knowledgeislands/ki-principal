# assistant-publish (ki.sop.main)

Goal: publish ki.sop.main's one local commit in `/Users/krisbrown/kis/personal/assistant` ("docs(work): assistant-sol message from ki.sop.main", appending an AGORA-DOORBELL-ACK line to `+/_WORK/personal.reg.assistant-sol/messages.md`). Its push was rejected because origin moved on, and `pull` (pull.rebase set) refuses because another session, personal.sop.main, has an uncommitted line in `+/_WORK/personal.reg.assistant-terra/messages.md`.

Do it without stashing, rebasing a dirty tree, resetting or touching that file: work in a fresh linked worktree from origin/main (`git worktree add` under `/tmp`), cherry-pick the commit there, resolve any conflict in the sol messages file by keeping both sides, push to main fast-forward, remove the worktree, then fast-forward the primary checkout only if git allows it with the uncommitted file left untouched (`git merge --ff-only origin/main`); if not, leave it behind and say so. Never force or --no-verify.

Report: run report; Done names the pushed commit or why not.
