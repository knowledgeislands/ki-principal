# Brief: release Stoa 0.32.0 and close its governance gaps

Kris agreed STOA-RELEASE and STOA-GAPS on 2026-11-07 (logged in `+/_WORK/ki.sop.main/decisions.md`, "Six queries agreed"). Act within that only.

1. In `/Users/krisbrown/kis/knowledge-islands/packages-stoa`: release 0.32.0 from `main` (latest tag `v0.31.0`; three approved changes unreleased) following the repository's own documented release process: version, changelog, tag, GitHub release. If that process publishes to a public package registry (npm or similar), stop before that step and report it as a query: Kris's standing rule asks first. Consumers use local versions, so change no consumer.
2. In ki-principal: add `packages-stoa` to [Known Lands](Admin/Governance/Known Lands.md) beside the other package repositories, and to `.ki.toml` `territory_members`. Kris's explicit instruction stands in for an Enactment record; note that in the commit body. Run `ki repo` checks that cover these files if available.
3. Tell ki.prj.stoa (its `messages.md` `## Inbound`, sender `KI > SoP (🏛️ 🔑 ki.sop.main)`) that 0.32.0 is released and the governance gaps are closed.
4. Each repository: `rumdl fmt` / `rumdl check` on Markdown touched, commit by explicit path, lower-case subject, trailer `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`; pull `git -c pull.autostash=false -c rebase.autoStash=false pull --ff-only`; push fast-forward only. Never stash, rebase, reset, force or `--no-verify`.
5. Report outcomes, tag and release link, and any queries in Context/Query/Options form. Write your report where the launcher's footer says.
