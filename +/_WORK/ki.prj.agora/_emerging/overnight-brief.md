---
work: ki.prj.agora
session: interactive
written_at: 2026-11-06T04:20:00Z
---

# Agora overnight brief, 6 November 2026

Kris's direction given between 03:05 and 04:20 GMT, written down before he left the work unattended until 08:00 GMT. It is the working brief, not a standard; each rule below goes to its proper home (a skill) once agreed.

## What Agora is

Agora is the place on each Mac where agents show up to work together: "I'm come here, I'm going to interact, I'm showing up ... constructively, looking for agreement and resolution ... as well as information sharing". It is not where work runs and not a chat app; Orca stays where Kris talks to agents.

## Goals ("spot on", 03:24 GMT)

1. **Everyone hears.** A message, broadcast or mark reaches each agent, and Kris can see whether it was heard.
2. **Everyone is level.** Every checkout on every Mac keeps up to date all the time; anything stuck shows.
3. **Who's doing what.** Each live agent, its focus areas, whether it listens, what waits; this is also the address book for routing by focus.
4. **Speak to everyone from the tray.** Broadcast, Away, I'm back, Ping, Mark all.
5. **Quiet and dependable,** with one clear name: Agora's call.

Out for now: scheduled jobs, account switching, keep-awake and host settings (captured, not built); the coordination rules themselves (personal.reg.inbox-sol's); anything that starts an agent on its own.

## Way of working

- **Roles.** Leaders set direction. Enablers (the coordinating agents) hold work packages and usually do the work within their own team of runs. Doers are brought in when an enabler needs a skill it lacks, such as a designer (a Claude Design session) for Agora's look.
- **Focus areas route the work.** An agent's focus says what it looks after; an idea from anyone goes as a message to the agent whose focus covers it; work packages are fluid and take in new ideas. Skill work goes to KI State of play.
- **Work in progress only.** A work package holds what is in progress; a healthy roadmap sits behind it, and ideas behind that (personal.reg.inbox-sol's `method` focus owns how work moves between them).
- **Skills are the home of reusable knowledge and how to use it.** Each skill carries its rubric, standards, sources and specifications. Specifications are written like the Agent Host Protocol, in RFC style (MUST, SHOULD, MUST NOT). Knowledge packages without the "how to act" may come later. The decide-and-act on delivered information (made durable or discarded) is one such skill, already in hand with ki-principal.
- **Consensus and good decisions.** Agents propose, agree or object; Kris decides what is his; each decision is recorded once, by its owner.
- **Announce, then make durable.** An agent announces what is new and noteworthy; the assistants (the inbox agents) make it durable in the record. The assistant on the Mac where it started is first point of call, so it is written once, not twice.
- **Local first, then across Macs.** On one Mac, agents talk through Agora with simple, quick messages; between Macs the Agoras talk directly over the private network, and Git is the durable record. When two sides clash, the one that went first stands and the other brings its changes in on top: cooperation first.
- **Keep everyone alive.** Every hour each agent is asked to re-arm its listener (KEEPALIVE). Since most agents run inside Orca, Orca's own channels should also be used to warm up or bring back an agent that has fallen off what it was doing.

## Overnight (to 08:00 GMT)

Runs in `ki-prj-agora`, each tested and pushed in apps-agora.local: wake map (done: a file wait wakes a Claude Code agent; Orca can send into a terminal; Orca chats cannot yet be woken from outside), Agora's call rename with small fixes, specification draft (to be rewritten RFC-style in a skill once the approach is agreed), Mark all, live roster and focus address book, sync and the households' settle call, calmer tray. At 07:13 Agora announces the night's new and noteworthy to personal.reg.inbox-sol, which makes it durable in the record. The return report is at 08:00.

Bounds: nothing installed (the households install the new build when told), nothing posted outside Kris's repositories, no agent started on its own.

## Open for Kris

- Whether tonight's specification stays a draft until it is rewritten RFC-style in its skill.
- A Claude Design session as a doer for Agora's look (prompt given in the thread).
- Orca agent-to-agent: which Orca channels may warm up or bring back an agent, and when.
