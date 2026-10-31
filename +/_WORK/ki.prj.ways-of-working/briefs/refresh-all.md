# Brief: refresh-all

Work: ki.prj.ways-of-working. Authority: REFRESH-ROLLOUT and LANDED-NOTICE, Kris, 31 October 2026, in `decisions.md`.

Find every live coordinating work package, any `+/_WORK/<id>/` whose `state.md` is not `finished`, in each Capital under `/Users/krisbrown/workspaces/*/*-principal/` and in `/Users/krisbrown/workspaces/personal/acquire/`. Add one IMPORTANT REFRESH line to each `messages.md`, from "KI > Model > Ways of working (ki.prj.ways-of-working)", naming the harness revision now on `main`. It says in plain English what changed today and what the thread must now do differently:

1. Questions use the two-reply card pattern: context as the reply's last text, then the card in the next reply after a short timer.
2. Plain English everywhere.
3. Listening is opt-in, and a listening thread tends its own package.
4. The new footer layout: state heading, counts, bullets, a "heading for" line, mode lines, then the thread line.
5. Owner feedback arrives as message lines.
6. Landed notices: say how your behaviour changed.

It closes by telling the thread to reread `ki-coordination` before its next reply.

Commit each `messages.md` alone in its own repository by explicit path and push fast-forward only; stop on divergence for that repository, report it and carry on. Report the count and any failures.
