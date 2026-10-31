# Blind review 7 - masked packet

Six open queries for an independent view. Options are listed in no particular order and carry no recommendation. You may and should challenge earlier owner decisions and prior reasoning where the evidence warrants; an earlier decision is evidence, not a constraint.

## INBOX-VERB

**Context:** On 31 October 2026 Kris asked that an open coordinating thread have a way to wake up and check for new work. A coordinating thread's incoming queue is a `messages.md` file in its work folder, committed to Git. A proposed rule keeps one watcher armed while the thread is open: a detached shell loop that every two minutes compares the Git blob identifier of `messages.md` in local `main` and on `origin/main`, and exits on a change or after a time bound, so the session wakes. Every platform (Claude Code, Codex, Orca, Paperclip) needs the same watching; only how the loop's exit reaches the session differs. Nothing in `ki agent` or `ki work` (the `ki` command-line tool, owned by the tools-ki repository) watches `messages.md` today; until something does, each coordinator writes the loop by hand. `ki agent wait` already exists and waits for background-run events. A new command would belong to tools-ki, so this work could only ask for it by a line in that work's `messages.md`; the owning work decides how and when. The shape sketched is `ki work watch <work id> [--run <run>] --interval 120 --timeout <m>`, read-only apart from `git fetch`, printing one reason line (`message`, `run-event`, `timeout`) and exiting. Nothing has been prototyped.

**Query:** Should the watcher become one shared shell command in tools-ki?

**Options:**

- Extend `ki agent wait` instead: add `--timeout` and `--inbox <work id>` to the existing waiter.
- Ask tools-ki for a read-only `ki work watch` command by one `messages.md` line; the coordination surfaces carry the hand-written loop until it ships.
- Keep the loop as a documented snippet only: no tooling change; each runtime binding carries the loop.

## CODEX-WAKE

**Context:** In Claude Code, a background shell command's exit re-invokes the open session, so a watcher loop can wake it. Codex has no documented way for a background command to wake an open session. Codex CLI 0.166.0 has `codex queue --thread <id> --message <text> --resume`, which may let an outside watcher wake a thread; nothing has been run to prove it. On 30 October 2026 Kris decided (WAKE-SESSION) that the session wake is one waiter, and that each runtime's wake must be proved before anyone relies on it.

**Query:** How should a Codex coordinating thread get its inbox wake?

**Options:**

- Adopt `codex queue --resume` now as Codex's wake, proving it in use.
- Prove it in one attended trial on a scratch thread with Kris watching, and until then say plainly that a Codex coordinator checks the inbox only when Kris writes or a run event arrives.
- Treat Codex as having no inbox wake and coordinate waiting threads from Claude Code only.

## SENDER-NUDGE

**Context:** A sender hands work to another coordinating thread by writing one line in the receiver's `messages.md`, committed and pushed. Under the proposed watcher, the receiver sees a new line within about two minutes of the push, on any host. Orca 1.4.245 has a mailbox send (`orca orchestration send --to run:<id>`) that Orca's own documentation calls "best-effort attention only"; it reaches only a coordinator bound to an Orca Run on a reachable Orca runtime, and needs the receiver's routing record, which is machine-local, so a sender on another host cannot use it. On 31 October 2026 Kris's ORCA-ROUTING decision was relayed: `messages.md` stays the durable channel and an Orca send is only a wake, never the message. A planned pilot, ORCA-SUBAGENT-PILOT, will test whether an Orca mailbox send actually wakes a coordinator in an Orca chat.

**Query:** Should a sender also nudge the receiving thread after writing its `messages.md` line?

**Options:**

- Required nudge wherever the platform allows: every sender nudges when it can.
- No nudge now; senders write and push their line, nothing more; revisit after ORCA-SUBAGENT-PILOT.
- Optional same-host Orca nudge now: where the receiver has a verified routing record on this host, the sender adds a pointer-only `orchestration send` after its push.

## HOLDING-SCOPE

**Context:** Acquire is a repository where captured material lands and is curated into knowledge cards in its `knowledge/` folder; it was designed to dispatch curated material to each owning knowledge base (a "Capital"). On 30-31 October 2026 Kris decided in Acquire (GOAL-HOLDING-AREA) that Acquire is for now a holding area: "nothing migrates out", and dispatch is on hold. The shared capture skill `ki-acquire` has been reworded to say that neither captures nor cards leave Acquire. The decisions as relayed don't say outright whether the curated cards must also stay, or whether they may be reconciled into a Capital's knowledge graph. Acquire's own published text did not yet carry the decision, so its exact wording could not be read.

**Query:** Does the holding rule keep the curated cards in Acquire as well as the captures?

**Options:**

- No: only captures are held. Cards may be reconciled into their owning Capital's graph whenever they are ready, and the skill should say so.
- Yes: cards and captures both stay in Acquire until Kris lifts the holding area.

## IDEAS-ROADMAP-STANDARD

**Context:** On 30-31 October 2026 Kris decided (IDEAS-IN-GRAPH) that future ideas live in the knowledge graph as future concepts, not on the roadmap; the capture skill has been changed to say so. The `ki-work-roadmap` standard's Ideas and graduation section (`/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-work-roadmap/references/standards-repository-roadmaps.md`) already keeps ideas out of the record queue: it sends concepts to a Capital's Emerging Concepts note, and other ideas to `Idea:` bullets in Project or theme notes or to `_IDEAS.md` beside the roadmap. Where every idea finally lives is a separate open question, IDEAS-HOME, in a design for this work that Kris has not yet settled.

**Query:** Should the roadmap standard's ideas section change now, or wait for IDEAS-HOME?

**Options:**

- Change it now so that every future idea is a future concept in the graph, and retire `Idea:` bullets and `_IDEAS.md`.
- Leave the roadmap standard as it is; carry IDEAS-IN-GRAPH into IDEAS-HOME and change the standard once Kris settles that.

## ACQUISITION-PROCESS-NOTE

**Context:** The capture skill `ki-acquire` names the Acquisition Process note in Knowledge Islands Principal (`/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Processes/Acquisition Process/Acquisition Process.md`) as the owner of the long-term lifecycle. On 30-31 October 2026 Kris decided in Acquire that it is a staging area for the knowledge graph and for now a holding area with dispatch on hold, and that curation goes one item at a time. The note still describes dispatch to each principal followed by Acquire removing its copy, with no staging graph, no holding area and no item-by-item curation. It is canonical content, so changing it goes through the Enactment Process with Kris's approval. Acquire's own text carrying the 30-31 October decisions is not yet published; a separate short run is proposed to recheck the capture skill against that text once it is.

**Query:** Should the Acquisition Process note be revised to match the 30-31 October decisions?

**Options:**

- Leave the note until the holding area is lifted, and add one line saying that dispatch is currently on hold.
- After the capture skill has been rechecked against Acquire's published text, a bounded run drafts the revision for Kris's approval through the Enactment Process.
