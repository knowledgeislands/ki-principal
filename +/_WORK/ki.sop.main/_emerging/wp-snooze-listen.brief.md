# Brief: wp-snooze-listen

From ki.sop.main (Knowledge Islands State of play). One bounded edit in `~/kis/knowledge-islands/ki-principal`.

## Task

In `Pillars/Philosophy/Model/Processes/Work Process/Work Process.md`, correct the wording on listening while On hold so it says: a thread stops listening while On hold, except 💤 Snoozing, which keeps listening and is released by a message or `resume`. Match the ki-coordination standard in `~/kis/knowledge-islands/ki-agentic-harness` at `5c118279` or later (Banner and hold sections). Change only the sentences that contradict this; keep the note's voice, British English and ASCII hyphens only.

## Authority

Kris's SNOOZE-ROUTE words, logged in `+/_WORK/ki.sop.main/decisions.md`, already authorise the Snoozing change to this note (ki-principal `17e56a25`); this corrects one sentence that change missed, at ki.reg.guilds' request WP-SNOOZE-LISTEN (2026-11-07). Touch no other file.

## Commit

Pull with `git -c pull.autostash=false -c rebase.autoStash=false pull --ff-only`. Run `rumdl fmt` and `rumdl check` on the note, commit it by explicit path with subject `docs(model): work process on hold stops listening except snoozing` and trailer `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`, then push fast-forward only. Never stash, rebase, reset, force or `--no-verify`; on divergence stop and report. A refused commit is a failure to report.

## Report

Write your report where the launcher's footer says: Done, In Progress, Queries; quote the before and after sentences and give the commit.
