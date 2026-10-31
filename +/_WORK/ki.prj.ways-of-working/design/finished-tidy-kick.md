# Finished-folder kick (FINISHED-TIDY-KICK)

Written by run `w-U8` on Saturday 31 October 2026, during the unattended window AWAY-31-OCT, for unit U8 of [the window plan](window-31-oct/plan.md).

## The ask

Relayed from personal.reg.acquire-intake at Kris's request on 30 October: Kris agrees a finished work should delete its own folder at its closing mark, as step 4 of Finishing Project work requires, but things fall through the gaps. When the main State of play notices a Finished work whose folder outlives its closing mark, it should give that work a kick. Today it only names the folder in that work's `messages.md`, "which no live coordinator then reads". In Kris's words: "Sort out the method so that the kick actually gets the folder deleted".

## The method today

At harness `a3fec58f`:

- `ki-coordination`, [Finishing Project work](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md#finishing-project-work), step 4: the work folder is deleted "at the mark that closes it", with the runs archived by `ki agent close` under its strict gate.
- `ki-coordination`, Pruning the work folder, **Flagging**: at its own mark, territory work names each folder the `ki-work-package` FOLDER rubric flags "in a line in that work's `messages.md`", and the owning coordinator prunes it at its next send.
- `ki-work-package`, [Tidying the work folder](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-work-package/references/standards-work-package.md#tidying-the-work-folder), **Who**: "Territory work never tidies another work folder". **Close-out**: a finished work's folder is deleted at the mark that closes it, once its decisions are homed, every finding settled and `design/` resolved.
- `ki-work-package`, Removal lifecycle: removal happens at the closing mark or on explicit user direction; an agent must not infer completion.
- `ki-work-package` rubric, FOLDER-4: "no finished work's folder outlives its closing mark". The check (`outlivesClosingMark` in `scripts/rubric/contexts/work-folder.ts`) fires only when the work is `finished` and its `mark` falls at or after its `since`.

## The gap

Three holes line up, so the folder is never deleted:

1. **Nobody holds the move.** Finished is 🏁, nobody's move. Once Kris says `finish` and the finishing thread ends, no coordinator will strike the closing mark. Reopening is a new opener from territory work, not a send.
2. **The check cannot see it.** FOLDER-4 waits for a closing mark at or after the finish. A work whose thread ended before that mark is never flagged, because its last mark is older than its finish. The check only catches the rarer case where the mark was struck and the delete then missed.
3. **The kick reaches nobody.** Even when flagged, the remedy is a line in the Finished work's own `messages.md`. A Finished work has no live coordinator to read it, so the line is a dead letter by construction. Territory work may not delete the folder itself.

## The knowledge-acquisition case

[ki.prj.knowledge-acquisition](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.knowledge-acquisition/state.md) shows all three. It finished on Kris's KA-FINISH word on 20 October (`since: 2026-10-20T04:14:07Z`), with every decision homed and `design/` resolved. Its last mark is 18 October, before the finish, so FOLDER-4 does not flag it. Its own next step is "delete this folder in one commit", which no session will take. State of play saw it and could only ask: the KA-CLOSE query in [ki.sop.main's queries](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.sop.main/queries.md), parked, asks whether a bounded run should close it. It is the only Finished folder in `+/_WORK/` today.

This unit does not delete that folder. KA-CLOSE stays with Kris.

## Options

a) **State of play closes it itself.** FOLDER-4 is fixed to flag every Finished folder, whatever its mark. At its own mark, State of play acts on each one rather than sending a message: it checks the close-out conditions (the work is `finished`, every decision homed, `design/` resolved, every finding settled, no open query, an empty `messages.md`, and no run running or queued for the work) and, if all hold, deletes the folder in one commit by explicit path, then archives the work's runs with `ki agent close` under its strict gate, never `--reconciled` without Kris. If any condition fails, it deletes nothing and puts one query to Kris in its own `queries.md`. This is a named exception to "territory work never tidies another work folder", for Finished work only.

b) **A blocking check on State of play's mark.** FOLDER-4 is fixed and made to block State of play's own mark while any Finished folder remains. This forces attention but names no one who may delete, so each mark either wedges or raises the same query again.

c) **The finishing thread deletes at once.** Steps 3 and 4 run in the same sitting: the finishing coordinator strikes the closing mark and deletes the folder as soon as Kris has seen the Finished report. This prevents new cases but does nothing for a thread that ends early or for folders already left behind, and it still leaves the check blind.

d) **A louder kick.** Keep the message, but flag it `IMPORTANT` or `FIRST-STEP`. It still has no reader, because nothing opens a Finished work.

## Recommendation

a) (recommended, confidence high - reviewed: a masked blind review on Codex chose the same course on its own; it is the only option that both finds every left-behind folder and names who deletes it, and Git keeps the folder, so a delete is easily undone)

Option c) is a sensible addition later, but not needed for Kris's ask.

## Blind review

Run `w-U8-review` (Codex, high effort, masked: it saw the Context, the Query and the options unranked, and read no queries, decisions, messages, reports or this note) recommended the same course, option a), at high confidence. It added five points, all folded into the draft below:

1. State of play deletes only at an owner-authorised mark whose report names the folder. Showing a Finished report is not by itself permission to strike a mark.
2. The close-out checks include that other durable information has reached its owners, not only decisions.
3. The runs are archived with `ki agent close` before the folder is deleted, so a gate refusal leaves the package intact. State of play never supplies the `--reconciled` waiver.
4. The exception covers administrative close-out only. It reopens nothing, accepts nothing and settles nothing for Kris.
5. The listing could tell a folder awaiting its closing mark apart from one already overdue. This is not in the draft; it needs a second rubric status and can follow.

It also said the course is not plainly within Kris's words. Kris agreed that a finished work deletes its own folder; letting State of play delete another work's folder is a named exception to a significant ownership rule, "territory work never tidies another work folder", and needs Kris's explicit adoption. The request to fix the method is not itself permission.

It corrected one point in the gap analysis: under today's definition the knowledge-acquisition folder has not "outlived its closing mark", because no closing mark was ever struck. It is stranded before that mark. Flagging every Finished folder is a deliberate change of coverage, not a bug fix.

## Outcome

Because of the review's authority point, the standard is not changed in this window. The method change is put to Kris as the FINISHED-TIDY-KICK query in this package's [queries](../queries.md). KA-CLOSE in ki.sop.main stays with Kris, and nothing is done to the knowledge-acquisition folder.

## Drafted change (not applied)

Drafted and tested in a throwaway harness worktree from `a3fec58f`, then discarded; the focused `ki-work-package` and `ki-coordination` tests passed (169) and the type check was clean. If Kris adopts option a), a run can re-apply it:

- **`ki-work-package` standard, Tidying the work folder.** **Who** gains: "The one exception is a finished work's folder, which no coordinator reads once the work is Finished: territory work closes it itself under Close-out." **Close-out** gains: "Where the folder outlives the finishing thread, territory work closes it at an owner-authorised mark of its own whose report names the folder, so that the folder is deleted rather than flagged, as Kris asked under FINISHED-TIDY-KICK on 30 October 2026: "Sort out the method so that the kick actually gets the folder deleted". This is administrative close-out only: it reopens nothing, accepts nothing and settles nothing on the owner's behalf. It first checks that the state is `finished`, every decision is homed and other durable information has reached its owners, `design/` is resolved, every finding is settled with its disposition recorded, `queries.md` holds no open query, `messages.md` holds no line, and no run of the work is running or queued. If all hold, it archives the work's runs with `ki agent close` under its strict gate first, never supplying `--reconciled`, which stays the owner's waiver, so that a gate refusal leaves the package intact, and then deletes the folder in one commit by explicit path, `docs(work): <id> close-out`. If any check fails, it deletes nothing and puts one query to the owner in its own `queries.md`, never a line in the finished work's `messages.md`."
- **`ki-work-package` standard, Removal lifecycle.** The deletion is "by the finishing coordinator or, where the folder outlives the finishing thread, by territory work at its own mark".
- **`ki-coordination` standard, Finishing Project work, step 4.** Adds: "Where the folder outlives the finishing thread, territory work closes it at an owner-authorised mark of its own whose report names the folder, under that close-out, rather than naming it in the finished work's `messages.md`, which no coordinator reads", with Kris's words.
- **`ki-coordination` standard, Pruning the work folder, Flagging.** The FOLDER items list "every finished work's folder", and territory work closes a finished work's folder itself instead of naming it in a message line.
- **`ki-coordination` standard, output-style source, and the generated `output-styles/ki-coordinator.md`.** "Territory work names each work folder ... at its own mark, except a finished work's folder, which it closes itself under the `ki-work-package` close-out."
- **FOLDER-4 rubric item** (`scripts/rubric/items/folder.ts`, `scripts/rubric/contexts/work-folder.ts` and its test, and the generated `references/rubric.md`). `outlivesClosingMark` becomes `awaitsCloseOut`, true for every `finished` folder whatever its mark. The title becomes "no finished work's folder is left standing", and the guidance names who closes it.

The `ki dev skill rubric` and `ki dev skill generate` writers publish only into the dev-linked primary checkout, so a run in its own worktree regenerates the output style through the generator module directly and the rubric line by hand, as the draft did.
