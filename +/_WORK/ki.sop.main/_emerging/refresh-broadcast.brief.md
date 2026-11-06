# Brief: refresh-broadcast

Work: ki.sop.main. Take the line MSG-63625521 REFRESH-REQUEST from ki.reg.guilds in `+/_WORK/ki.sop.main/messages.md` `## Inbound`: read it in full and do what it asks within State of play's authority.

1. Broadcast it as one `IMPORTANT · REFRESH` line, with a fresh `MSG-` id from uuidgen, in each live work package's `messages.md` `## Inbound` across the Knowledge Islands territory, using the territory list `ki agent prompts knowledge-islands` (or `covers` in `+/_WORK/ki.sop.main/work.md`) gives. Packages in other territories are out of scope unless the line names them. The line is a one-clause pointer to ki-agentic-harness `056996c0` and its ki-git "Checks before committing" section, quoting the rule in a sentence.
2. Put each sent line in ki.sop.main's `## Outbound` as awaiting ACK.
3. Put `- 2026-11-06 · ACK MSG-63625521 · from ki.sop.main · <HH:MM GMT>` at the top of ki.reg.guilds' `## Inbound` (ki-agentic-harness), record the disposition in ki.sop.main's `decisions.md` and remove the line.
4. Set `method_read: 056996c0` in ki.sop.main's `state.md` front matter.

Rules: apply the new rule yourself: run `rumdl fmt` then `rumdl check` on every file before committing, treat a refused commit as a failure, and confirm `git status` is clean on committed paths before pushing. Commit by explicit path, lower-case conventional subject, trailer `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. Pull fast-forward only with autostash off; never stash, rebase or reset; use a temporary worktree from origin/main where a checkout is dirty, then remove it. Push fast-forward only. Write nothing in another package beyond one line in its messages.md. Report one line per package with its id, plus failures.
