# Brief: sop-tools

From ki.sop.main (🏛️ 🔑 ki.sop.main, Knowledge Islands State of play), run `sop-tools`. Work in `~/kis/knowledge-islands/ki-principal`; one line in another package's `messages.md` only where named.

## Authority

Kris, about 03:00 GMT on 7 November 2026 (QUARTERMASTER-SOP, relayed by personal.reg.household-sol as MSG-6f12f0d9): "the actual quartermaster should be ki.sop.tools, and it should live as a leader, I think, in the principle." and "I want you to change what the quartermaster will be, and then we'll create it somewhere." The catalogue entry landed at harness `efa0a3e9` (role quartermaster 🧰, leaders tier, seat `ki.sop.tools`, label KI > SoP (tools), a secondary State of play in ki-principal under ki.sop.main). Both logged in `+/_WORK/ki.sop.main/decisions.md`.

## Task

1. Read `~/kis/knowledge-islands/ki-agentic-harness/skills/governance/ki-work-package/references/standards-roles.md` (quartermaster row and seat paragraph), `standards-work-package.md` and the ki-coordination standard's sections on secondary State of play, Work naming and Opening work. Model the new package on an existing secondary State of play package if one exists in the estate (`grep -l "sop\." ~/kis/*/*/+/_WORK/*/work.md`), else on `+/_WORK/ki.sop.main/`.
2. Create `+/_WORK/ki.sop.tools/` with the five files: `work.md` (id `ki.sop.tools`, label KI > SoP (tools), `role: quartermaster`, level/type as a secondary State of play, parent ki.sop.main, routing description and goals from the catalogue row: the island's tools and MCP servers kept working, released and accounted for; never decides how a tool must behave (the guild's), heads the territory, or releases without Kris), `state.md` with `state: on-hold`, `hold.reason: paused`, `hold.release: when Kris opens this work`, empty `workers`, `discussions.md` and `decisions.md` empty apart from a first decisions entry citing the authority above, and `messages.md` with `## Inbound` and `## Outbound`.
3. Queue its first Inbound line, RIG-RETIRE from personal.reg.household-sol: find its exact text (look in `~/kis/personal/dotfiles/+/_WORK/personal.reg.household-sol/` messages, discussions, decisions and Outbound, and grep `RIG-RETIRE` across `~/kis/*/*/+/_WORK`), and copy it word for word with its sender; if no line exists yet, write one: `- 2026-11-07 · RIG-RETIRE · from Personal > Household > sol (personal.reg.household-sol) · Rig cannot retire a job that leaves a Mac's profile; first item for the quartermaster, per QUARTERMASTER-SOP`.
4. Register the seat wherever `ki agent prompts knowledgeislands` and the territory read their packages (check `ki agent prompts --help`, `.ki.toml`, and how `ki.sop.main` and `ki.prj.stoa` are listed), and add `ki.sop.tools` to `+/_WORK/ki.sop.main/work.md`'s covers. Run `ki agent prompts knowledgeislands 2>&1 | grep -A8 ki.sop.tools` and paste the opener in your report.
5. Tell household-sol once, at the top of its `## Inbound` in `~/kis/personal/dotfiles/+/_WORK/personal.reg.household-sol/messages.md`: `- 2026-11-07 · SOP-TOOLS-READY · from KI > SoP (🏛️ 🔑 ki.sop.main) · <HH:MM GMT> · ki.sop.tools exists in ki-principal (+/_WORK/ki.sop.tools/), on hold until Kris opens it; RIG-RETIRE is its first Inbound line`.
6. Do not open the seat, launch a session for it, or move tools-burndown, the Rig intake or the mail backlog: those remain an open query with Kris.

## Commit

In each repository: pull with `git -c pull.autostash=false -c rebase.autoStash=false pull --ff-only`; `rumdl fmt` then `rumdl check` on touched Markdown; commit by explicit path (git add new files first), lower-case Conventional Commit subject such as `docs(work): ki.sop.tools seed quartermaster seat on hold`, trailer `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`; push fast-forward only. Never stash, rebase, reset, force or `--no-verify` in any primary checkout; on divergence stop and report. A refused commit is a failure to report. Touch no other session's uncommitted files.

## Report

Write your report where the launcher's footer says: Done, In Progress, Queries; list the package files, the queued line, the registration and opener, the sender told, and each commit.
