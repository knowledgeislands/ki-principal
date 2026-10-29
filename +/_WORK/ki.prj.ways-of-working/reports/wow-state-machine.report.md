# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-state-machine

**🤖 → 👤 Handoff to supervisor · Run report at 20:54 GMT · last mark 16:18 GMT**

---

## Done

- Drew the work state machine with Archify: [work-state-machine.html](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/work-state-machine.html) and a static [work-state-machine.svg](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/work-state-machine.svg). It has eight states, with Bootstrap added, and 13 named transitions: open, re-bootstrap, pick up, report, send, receive (by the owner and by the worker), reply, hand off, answer, withdraw, hold, drain blocked, release and finish. Archify's automated checks passed, and I looked over both renders myself.
- Wrote the definitions note, [work-state-machine.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/work-state-machine.md), with the SVG embedded at the top. It covers:
  - a states table, giving each state's meaning, who holds the move, its banner and what must be true while in it;
  - a transitions table, giving each arc's trigger words, preconditions, the work it does and its postconditions with the commit. This follows TRANSITION-CONDITIONS, which you set while the run was going;
  - the hold arc's eight portability checks under DRAIN-MEANS;
  - where Handoff to target goes: a reply, the target taking ownership, a refusal or silence. None of these goes straight to On hold or Finished;
  - how a host move maps onto the machine;
  - the WORK-FOLDER-PURPOSE layout. Of today's file kinds, only run reports move, into `reports/`;
  - a rollout list and eight tagged decisions.
- Committed the three files as b9b0153d and pushed them. The first fast-forward pull was refused because six package-design commits from another session had landed. None touched these files, so the retry was a rebase pull, which the fetch grant allows; it replayed only this commit. Pre-commit audit: no findings on the three files.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- The rollout to the Work Process note, `ki-coordination`, `ki-work-package` and `tools-ki` waits on your decisions. It goes out as `messages.md` lines and is not started.
- The note goes to the `ki-work-design` review stage once you have read it.

## Queries

### BOOT-RECORD - Whether Bootstrap is recorded in the state file

**Context:** Bootstrap lasts one session turn of reading. Recording it would add a `bootstrap` value to `state.md`, `ki work status` and the Observatory, and a commit at every open. Leaving it transient keeps the recorded state as the state the work was in until the session picks up or reports. Then the package never says "bootstrap" after a session dies mid-read.

**Query:** Should Bootstrap be a recorded state value, or a transient state that exists only in the session?

**Options:**

a) (recommended, confidence medium - no reader needs it, and a crashed bootstrap leaves no stale value) Transient: draw and define it, but record no `state` value. The exit arc's commit is the first record.

b) Recorded: add `state: bootstrap` to the state file, `ki work status` and the Observatory, committed at open.

### BOOT-RECEIVE - Whether Bootstrap exits straight to With supervisor

**Context:** You said bootstrapping "can then transition to with worker or with supervisor". Today the standard sets With supervisor only on your receive, and a re-bootstrap report counts as a send. That would put the work in Handoff to supervisor until you say `with me`. You open the session and read the report live, but you may also open a session and walk away.

**Query:** When a bootstrap finds nothing for the worker, does the work go to With supervisor at once, or to Handoff to supervisor until you receive?

**Options:**

a) (recommended, confidence medium - follows your words and treats the opener as the receive, since you opened the session) The `report` arc goes to With supervisor, with `received` set at the opener.

b) The `report` arc goes to Handoff to supervisor, and your next word is the receive, as for any send.

### TARGET-RUN - Whether a work's own run can be a handoff target

**Context:** The Work Process note's states table says Handoff to `<target>` is "sent to other work, run or a person". The `ki-coordination` standard says work is With worker "while any of their items lies with a run". The machine follows the standard: a work's own runs keep it With worker, and a target is other work, a person or a repository's owner.

**Query:** Should the note's wording drop "run" as a target of a work's own handoff?

**Options:**

a) (recommended, confidence high - the standard is explicit, every banner and heartbeat rule assumes it, and only the note's table differs) Yes: a work's own runs always keep it With worker. Amend the note's table to "other work, a person or a repository's owner".

b) No: let a run be a target. A work whose only item is a long run would then show Handoff to `run/<name>`, with no heartbeat.

### TARGET-SILENT - How a handoff to a silent target ends

**Context:** A target that never answers leaves the work in Handoff to target indefinitely. Stewardship already refuses timeout takeovers, a routed work cannot reject a unit, and the worker holds no move while the target does.

**Query:** How does a handoff to a silent target end?

**Options:**

a) (recommended, confidence medium - keeps the holder rule and the no-timeout precedent while making the wait visible) Only you withdraw it, by a steer. The banner shows the handoff's age, and territory work flags one older than 7 days at its mark.

b) The worker withdraws it itself after a set time, such as 7 days, and sends it to you.

### HOST-MOVE-PATH - Whether a planned host move must pass through On hold

**Context:** The standard says a hold "serves a move between hosts", and the terra-to-sol move of 29 October went through a drain. A hold also parks every query and strikes the mark, which a move between your own Macs may not need. The portability checks alone would protect the move.

**Query:** Must a planned host move go through On hold, or may it re-bootstrap directly once the portability checks pass?

**Options:**

a) (recommended, confidence medium - one path, already in the standard and in use, with the portability checks proven on it) Every planned move goes through `hold` and `release`.

b) Allow a direct move from With supervisor or Handoff to supervisor: run the portability checks without parking, then re-bootstrap on the new host.

### REPORTS-NAME - How a report is named inside reports/

**Context:** Reports are named `<run>.report.md` today. The launcher, the rubric and the links in decisions and reports all use that name. Inside `reports/` the suffix repeats the folder name.

**Query:** Keep `reports/<run>.report.md`, or shorten to `reports/<run>.md`?

**Options:**

a) (recommended, confidence high - a plain move keeps every reader and existing name working, and Git follows the rename without edits) Keep `reports/<run>.report.md`.

b) Shorten to `reports/<run>.md`, and change the launcher, the rubric and the links.

### FOLDER-MIGRATE - How existing root reports move into reports/

**Context:** This package alone holds 86 reports at its root, and many are already tidy candidates. Links in decisions and reports point at the root paths, and a recap reads a deleted report from its last revision.

**Query:** How should existing root reports move once the standard changes?

**Options:**

a) (recommended, confidence medium - tidying first moves the fewest files, and one move per package by its steward lets links be rewritten in the same commit) Each package's steward tidies at its next mark, then moves the remaining reports into `reports/` with `git mv` in one commit, rewriting links into them.

b) Leave existing root reports where they are under a tolerance window; only new reports go into `reports/`.

### ARC-NAMES - Adopt the transition names

**Context:** The machine reuses send, receive, reply, hold, release, finish, pick up and re-bootstrap. It adds hand off, answer, withdraw, report and drain blocked, with proposed commit subjects for the new arcs. The note's other words are agreed to be proven in use.

**Query:** Should the transition names be adopted as drawn, for the Words table and the commit subjects?

**Options:**

a) (recommended, confidence medium - they reuse every word the standard already has and name only the arcs it leaves unnamed) Adopt them as drawn, to be proven in use like the other words.

b) Rename some arcs first, naming which.

### 🤖 → 👤 Handoff to supervisor · since 20:54 GMT

👤 8 with you

- [with you] BOOT-RECORD · owner · since 20:54
- [with you] BOOT-RECEIVE · owner · since 20:54
- [with you] TARGET-RUN · owner · since 20:54
- [with you] TARGET-SILENT · owner · since 20:54
- [with you] HOST-MOVE-PATH · owner · since 20:54
- [with you] REPORTS-NAME · owner · since 20:54
- [with you] FOLDER-MIGRATE · owner · since 20:54
- [with you] ARC-NAMES · owner · since 20:54
- [committed] work state machine design

🧵 ki.prj.ways-of-working
