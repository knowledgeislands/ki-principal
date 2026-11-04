# review-hold-states (blind review)

Independent review: you have not seen anyone's recommendation; give your own for each. Do not read any `discussions.md`, `decisions.md`, `*.report.md` or `*.design.md` in a `+/_WORK/` folder. You may read the Work Process note in ki-principal (`Pillars/Philosophy/Model/Processes/Work Process/Work Process.md`) and the ki-coordination and ki-work-package standards in /Users/krisbrown/kis/knowledge-islands/ki-agentic-harness. Background, as dated facts: on 4 November Kris said "On hold" reads as stopped, yet a package resting with nothing in hand still receives and acts on work, including urgent lines; he agreed the idle case is a subcategory of On hold; he gave footer examples `💤 On hold · more expected · listening` and `⏸️ On hold · paused until <release>`; and he wants it thought through before changes go out.

## HOLD-IDLE - What the idle case is

**Context:** Kris agrees that a package resting with nothing in hand is a kind of On hold. Today On hold has two reasons, paused and more expected, and only Kris can set either. Idle behaves exactly like more expected: it rests and new work releases it. The only difference is that the worker reaches it by itself.

**Query:** Should idle be recorded as more expected plus a note of who set it, or as a third reason of its own?

**Options (unranked):**

- Idle is not a hold: the work stays With supervisor and the banner adds a "resting" line.

- Idle becomes a third reason, `hold.reason: idle`, beside paused and more expected.

- Idle is more expected set by the worker, recorded `hold.set_by: worker` and shown as `💤 On hold · idle`; there are still two reasons.

## HOLD-SELF - Whether a worker may put its own work on hold

**Context:** The [Work Process](</Users/krisbrown/kis/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Processes/Work Process/Work Process.md>) note lets only Kris agree a hold, from With supervisor. The first-message exception already creates packages On hold without Kris. household-terra put itself on hold at 23:50 GMT on 3 November after a `mark`, which the note does not allow. Even so, it behaved the way Kris wants a resting package to behave.

**Query:** May a worker put its own work into the idle hold, and if so, under what conditions?

**Options (unranked):**

- No: a worker may only propose a hold in its send, and a resting package stays With supervisor until Kris says `done for now`.

- Yes, but only into idle and only when all five conditions hold: nothing running or queued, nothing handed off, no unread message, no query with Kris, everything pushed. Paused and done for now stay Kris's words.

## HOLD-URGENT - Whether a paused package acts on urgent lines

**Context:** Today a line sent to paused work waits unread, and State of play shows how many are waiting. Important lines wait too. The draft how-we-work design sends urgent work to a live owner, or up to a live leader, rather than into a sleeping queue.

**Query:** What should happen when an IMPORTANT line lands on paused work?

**Options (unranked):**

- The package handles IMPORTANT lines where it is and stays paused.

- An IMPORTANT line ends a paused hold by itself and moves the work to Handoff to worker.

- The line waits. State of play puts it to Kris as a `resume` query, and genuinely urgent work goes to a live owner instead.

## HOLD-LISTEN - Which holds listen

**Context:** Under LISTEN-STATUS on 31 October 2026, Kris set that a listening thread stops listening while On hold. Kris's example for this request, `💤 On hold · more expected · listening`, shows a held thread listening, and household-terra did listen while held. New work is what ends a more-expected hold, and a listening thread can catch it at once.

**Query:** Should more expected, including idle, keep listening on threads that have listening switched on?

**Options (unranked):**

- Keep LISTEN-STATUS as it is: nothing On hold listens, and new work is found when a session next opens the work.

- Yes for more expected and idle; paused never listens. This revisits LISTEN-STATUS for more expected only.

## HOLD-FOOTER - How each hold reads in the footer

**Context:** Today the banner heading reads `⏸️ On hold` for both reasons, sometimes with the paused release written in. Kris's examples are `💤 On hold · more expected · listening` and `⏸️ On hold · paused until <release>`. Under FOOTER-LAYOUT (31 October), modes such as listening sit on their own lines. Under FOOTER-AGORA (3 November), what the footer shows is `ki.prj.agora`'s to decide, and `ki.sop.main` keeps the state words.

**Query:** How should the hold heading show the reason and listening?

**Options (unranked):**

- Follow Kris's example: the reason and listening both in the heading, `💤 On hold · more expected · listening`, with no separate listening line on a held banner.

- ⏸️ for paused and 💤 for more expected and idle, the reason and any release always in the heading, listening on its own line; send the wording to Agora to draw.

## HOLD-DIAGRAM - Where the flow diagram lives

**Context:** `work-model.svg` in the Work Process note shows how the work is organised, not how it moves between states. Kris asked to see the states as a flow. The note already pairs its picture with a plain-text version for viewers that cannot show it.

**Query:** Where should the state-flow diagram go, and in what form?

**Options (unranked):**

- An Archify SVG made under `ki-diagrams` and committed beside `work-model.svg`.

- Mermaid, a diagram written as text, in the Work Process note under The seven states, with a plain-text version beside it, through one Enactment record.

## HOLD-TERRA - What to do with household-terra's hold now

**Context:** household-terra has been On hold, more expected, since 23:50 GMT on 3 November. It set the hold itself after a `mark`, and it is still listening. Today's note does not allow that hold; under this proposal it would be a lawful idle hold.

**Query:** Should household-terra's state be corrected now, or left until the decisions land?

**Options (unranked):**

- Put it back to With supervisor now and stop its listening while the design is decided.

- Leave it, record the exception in the note, and send it a refresh line once the standard changes, so it is re-recorded as idle or reverted as decided.

For each: your choice, confidence and a two-line reason. Read-only; no commits. Write it as your run report.
