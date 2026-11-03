# assistant-replies (ki.sop.main)

Goal: deliver two reply lines from ki.sop.main to `/Users/krisbrown/kis/personal/assistant/+/_WORK/personal.reg.assistant-sol/messages.md`, using the same method as the assistant-publish run (report: ki-principal `+/_WORK/ki.sop.main/reports/assistant-publish.report.md`): a temporary worktree from origin/main, commit, push fast-forward, remove the worktree; never touch the primary checkout's dirty files, never stash, reset, force or --no-verify.

1. AGORA-REPLY, the reply route-misc could not deliver (text in ki-principal `+/_WORK/ki.sop.main/reports/route-misc.report.md`), unless `git log origin/main` shows it already delivered.
2. `- 2026-11-03 · REG-ENTRY-ACK · KI > SoP (ki.sop.main): workers entry added to ki-principal +/_WORK/ki.sop.main/state.md (councillor, leaders, listening on), commit <the ki-principal commit "docs(work): ki.sop.main worker register entry">.`

Then, only if the primary checkout's `main` is a strict ancestor-equivalent (its local-only commits are already on origin by patch id, check with `git cherry origin/main`), report that; do not reset it. Report: run report naming the pushed commit.
