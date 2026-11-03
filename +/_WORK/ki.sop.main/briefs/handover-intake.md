# handover-intake (ki.sop.main)

Goal: take up, for State of play (ki.sop.main), the four Knowledge Islands works whose coordination Kris moved to it on 3 November ("move all of the work to be coordinated through the SOP main"; SOLE-THREAD in ki.sop.main decisions.md), and tidy the territory's packages so each sits at a clean, true baseline.

Read first: ki-work-package and ki-coordination standards (harness at /Users/krisbrown/kis/knowledge-islands/ki-agentic-harness), then `+/_WORK/ki.sop.main/messages.md` lines AUDIT-FIXES, PACKAGE-FLAGS, MOVED-NOTE-LINKS and REPORTS-MOVED (full text there), and the handover lines in git history: `git log -p -3 -- +/_WORK/ki.sop.main/messages.md` (HAND-TO-SOP, MAC-STUDIO-HANDOVER, WOW-HANDOVER, ORCA-EVAL-TO-SOP).

Do, in ki-principal only:

1. For ki.prj.observatory, ki.prj.mac-studio-setup, ki.prj.ways-of-working and ki.prj.orca-evaluation: append an acknowledgement to each decisions.md ("coordination taken up by ki.sop.main, 3 Nov, under SOLE-THREAD"); leave each On hold; set orca-evaluation's hold reason to `paused`. Do not answer or drop any parked discussion.
2. AUDIT-FIXES: for ki.prj.chezmoi (handed back, 40 lines waiting) and ki.prj.mac-studio-setup (IMPORTANT RIG-APP-FOOTPRINT waiting since 20 Oct), and ki.prj.observatory's backlog, do not execute their lines; classify each waiting line as: still live / overtaken (with commit evidence) / belongs elsewhere (name where). ki.prj.tools-burndown holds a RESUME line from 31 Oct ("Release it, one fix at a time"): if it is Kris's word, release the hold in state.md per the standard and record it; otherwise say why not.
3. PACKAGE-FLAGS: fix the mechanical rubric findings (IMPORTANT lines first in queue order, stray files into focus folders or pruned only where their outcome is homed, spent briefs deleted by explicit path); never delete a report whose outcome is not homed. REPORTS-MOVED: prune ki.prj.ways-of-working/reports/ by the same rule.
4. MOVED-NOTE-LINKS: repoint links in `Streams/Projects/host-network.md` and `Streams/Projects/observatory.md` from `/Users/krisbrown/workspaces/` to the `~/kis` path (absolute `/Users/krisbrown/kis/knowledge-islands/ki-principal/...`), and sweep other `+/_WORK/` and `Streams/` links still naming `/Users/krisbrown/kis/knowledge-islands/` the same way.
5. Remove AUDIT-FIXES, PACKAGE-FLAGS, MOVED-NOTE-LINKS and REPORTS-MOVED from ki.sop.main/messages.md in your final commit; touch nothing else in ki.sop.main.

Do not touch other sessions' uncommitted files (many untracked reports exist under ki.prj.ways-of-working; leave untracked files you did not create alone, but list them). Commit by explicit path with Conventional Commits, pull fast-forward only, push; never stash, rebase, reset, force or --no-verify.

Report: a run report with Done (one line per package), the consolidated list of every parked discussion across the four packages as (work id, tag, one-line context, its recommended option), the classified waiting lines, and any query for Kris in Context/Query/Options form.
