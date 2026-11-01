# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › landscape-rollout

**🤖 → 👤 Handoff to supervisor · Run report at 06:26 GMT · last mark 01:39 GMT**

---

## Done

- [ki.prj.orca-evaluation messages](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.orca-evaluation/messages.md), commit `2a212e88`, received three lines, each giving the decision's words and the 30 October date and citing [landscape-report](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/landscape-report.md):
  - ORCA-REACH: a), "as recommended but follow up in weeks time", follow-up due 6 November. Orca runs only on attended Macs, packages opt in, `ki agent` stays the only launcher on `vega`, and an always-on server goes through Enactment.
  - WAKE-SESSION: a). The Orca half is theirs: prove `orca orchestration check --wait` under the bounded single-waiter contract.
  - WAKE-DURABLE: a). The headless pass stays the durable wake, and Orca automations are not adopted as a wake.
  - The commit audit passed.
- [ki.prj.tools-burndown messages](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.tools-burndown/messages.md), commit `41482c27`, received three lines with the same date and reference:
  - AGENT-HOME: a), "as recommended but follow up in few days", follow-up due 2 November. `ki agent` stays in tools-ki as the floor launcher, and the `decide`, `reconcile`, `home` and `prompts` split is designed command by command in a tools-ki record.
  - WAKE-SESSION: a). The `ki agent wait` half is theirs: it has no timeout, and `--next` can lose a seen event.
  - WORKTREE-OPTOUT: a). The baseline waits for the integrate command and the four worktree prerequisites, captured as tools-ki records.
  - The commit audit passed.
- [queries.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/queries.md), commit `35504426`: the five answered queries left `## Open`. A new `## Answered` section holds one-line pointers to the [Owner answers entry](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/decisions.md#owner-answers-30-october-2026-0615-gmt). WAKE-HOST stays open. The commit audit passed.
- No roadmap record, skill or code was edited.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- These parts belong to this package and were not sent as messages:
  - the WAKE-SESSION `wait` verb in `ki-delegation`;
  - the WAKE-DURABLE correction of the landscape design and explainer;
  - the AGENT-HOME `Idea:` line on the [Techne theme page](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/techne.md). No work package clearly owns that page, so it was not routed (see AGENT-HOME-IDEA).
- The follow-ups fall due on 2 November (AGENT-HOME) and 6 November (ORCA-REACH).

## Queries

### AGENT-HOME-IDEA - Who writes the Techné dispatch `Idea:` line

**Context:** AGENT-HOME a) also says "Record Techné dispatch agent an `Idea:` line on Techne theme page". The Techne theme page lives in `Streams/Themes/techne.md`, and no work package's routing description claims it. Root `AGENTS.md` sends work that no package owns to State of play's `messages.md`.

**Query:** Should the `Idea:` line go to ki.sop.main as a message, or should this package write it itself?

**Options:**

a) (recommended, confidence medium - AGENTS.md routes unowned work to State of play, but this package may already own theme-page edits for its decisions) Send one line to ki.sop.main's `messages.md`.

b) This package's coordinator adds the line itself in a bounded run.

### ORCA-REACH-VEGA - Tell ki.prj.agent-host about the `vega` launcher choice

**Context:** ORCA-REACH a) keeps `ki agent` as the only launcher on `vega`, by choice. ki.prj.agent-host builds and runs `vega`. The line went only to ki.prj.orca-evaluation, which owns Orca use.

**Query:** Should ki.prj.agent-host also get a line about ORCA-REACH?

**Options:**

a) (recommended, confidence medium - the decision constrains vega's launcher, but the brief named only the Orca owner) Send one ORCA-REACH line to ki.prj.agent-host's `messages.md`.

b) Leave it with ki.prj.orca-evaluation only.
