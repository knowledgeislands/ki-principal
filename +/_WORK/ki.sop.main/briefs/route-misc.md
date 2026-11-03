# route-misc (ki.sop.main)

Goal: deliver two authorised routes for State of play.

1. HEADER-ESTATE (line in `+/_WORK/ki.sop.main/messages.md`): append it as one line to `+/_WORK/ki.prj.chezmoi/messages.md`, naming the sender chain (personal.reg.rig-terra via personal.sop.main via ki.sop.main) and the brief path it cites.
2. AGORA-DECLARE (line in the same file): Kris chose Q2 a) on 3 Nov: declare `knowledgeislands/apps-agora.local` as a member of the Knowledge Islands territory in ki-principal's `.ki.toml` (`territory_members`, matching existing entries' shape), and in Known Lands (`Admin/Governance/Known Lands.md`) under its internal inventory if members are listed there (this is an owner-instructed bounded change, so no Enactment record is needed; cite the decision in the commit body). Run `ki repo audit --repo .` and `ki territory audit` if available, and report results. Then append a reply line to `/Users/krisbrown/kis/personal/assistant/+/_WORK/personal.reg.assistant-sol/messages.md` saying it is declared, with the commit.
3. Remove HEADER-ESTATE and AGORA-DECLARE from ki.sop.main/messages.md in your commit.

Commit by explicit path per repository, Conventional Commits, pull fast-forward only (use `git -c pull.autostash=false -c rebase.autoStash=false pull --ff-only`), push; if a pull cannot fast-forward or the tree has someone else's change in a file you need, stop and report. Never stash, rebase, reset, force or --no-verify. In the assistant repository an uncommitted line from personal.sop.main sits in personal.reg.assistant-terra/messages.md; do not touch that file.

Report: run report, Done per repository, any query for Kris in Context/Query/Options form.
