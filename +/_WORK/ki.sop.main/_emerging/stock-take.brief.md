# stock-take (ki.sop.main)

Goal: Kris (about 01:55 GMT 4 Nov): "go and get lots of information and try to start moving forwards things overall on the Knowledge Islands of work packages". Read-only. Build one picture of every Knowledge Islands work package and its repositories, so State of play can launch the next authorised units.

Cover every package under `/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/` that ki.sop.main's `work.md` `covers` lists (plus ki.prj.agora): its state, its queue (`messages.md`, IMPORTANT first), its open and parked discussions, and its Project's roadmap records in their repositories (Now and Next, Ready, in progress, awaiting review), plus each repository's level against GitHub and any stray branches. Skip ki.prj.agora's own queue beyond a line (its thread is live).

Write `/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.sop.main/_emerging/stock-take.findings.md` (commit only that file): one table per package; then a ranked list of **next units State of play may launch now under existing authority** (each with repository, the decision or record that authorises it, size S/M/L, what it waits on, and which units touch the same files so must chain); then units that need Kris, as queries in Context/Query/Options form with recommended option and confidence; then anything stale, overtaken or broken. Quote the decision words and dates you rely on. Do not change any other file.

Commit by explicit path; pull with `git -c pull.autostash=false -c rebase.autoStash=false pull --ff-only`; push fast-forward only. Never stash, reset, force or --no-verify. Report: run report pointing at the findings.
