# Brief: blind review of one owner query

Read-only. Write only ~/.local/state/ki/agents/ki-prj-orca-evaluation/review-worker-threads.report.md, then call worker_done with that path. Do not read anything under +/_WORK/ki.prj.orca-evaluation/ or any report under ~/.local/state/ki/agents/. You may check the facts below with `codex --help`, `codex archive --help`, `codex delete --help` and `orca orchestration --help`, read-only; change nothing.

Review this independently: reach your own view from the context and the options before considering any other view, and say where you disagree.

**Context:** The owner uses Orca (an agent-orchestration desktop app) as the main way to run agent workers across Macs. Each Codex worker Orca starts leaves a saved thread, opening "You are working inside Orca, a multi-agent IDE. You are a dispatched worker.", which shows in the ChatGPT desktop app's recent list on the Mac that ran it: 50 on terra and 3 on sol so far, a third Mac unknown. On 1 November 2026 the owner said these are ephemeral, unlike thinking threads, and "once they're finished with, I think they should just be deleted, and so they don't appear in things like recent lists". Each worker's brief and report are already kept in the owner's work records. Orca has no setting or command for this: releasing a worker keeps a copy of its output in Orca's own database but leaves the Codex thread. Codex's command line can archive a thread by id (reversible, `codex unarchive`) or delete it (permanent). Codex can start a never-saved thread, but only Orca can ask for that, and it does not; such a worker would leave no transcript for Orca to read while it runs. Nobody has asked Orca upstream for archive-on-release. Hand-editing app databases is ruled out: it broke Orca on 31 October.

**Query:** How should the existing worker threads be cleared, and new ones kept out of the recents list?

**Options (unranked):**

- Have a bounded run on each Mac archive, through `codex archive`, every thread whose opening line is the Orca worker preamble and whose Orca worker has been released, repeated after each Orca Run until Orca can do it; and file one Orca feature request for opt-in archive (or delete) of the Codex thread on worker release.
- Archive the existing ones by hand in the ChatGPT app and raise only the Orca feature request, accepting that new ones build up until Orca ships it.
- Delete instead of archive, with `codex delete`, for the same matched threads, after release.
- Leave them.

Give: your recommended option, confidence (high/medium/low) with a one-line reason, any option you would add or combine (for example archive now, delete after an interval), and any fact above you found wrong.
