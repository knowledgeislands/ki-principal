# [Knowledge Islands](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Charter.md) › State of play › sop-mark

**🤖 → 👤 Handoff to supervisor · Run report at 19:07 BST · last mark 18:58 BST**

---

## Done

- FIRST-STEP: checked `work.md` against `ki-work-package`. The description is 420 of the 500 allowed characters and has the routing shape, Goals links the Charter and Scope names neighbouring works by id, so the wording stays as it is. `method_read` in [state.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/state.md) is now 2026-10-19T17:59:32Z. Nothing else in `state.md` changed.
- Decisions strike, in [decisions.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/decisions.md): the log had 261 entries. 233 are struck outright, 28 are kept in full or in part, and none became a one-line pointer. The numbering is gone, and the kept entries sit under 24 dated headings in Kris's words. The file went from 123,648 bytes and 1,114 lines to 11,144 bytes and 117 lines.
  - I checked each home before striking:
    - the ki-coordination, ki-delegation, ki-work and ki-work-design standards;
    - the Project notes, Known Lands, ADR-KI-PRINCIPAL-007 and the Known World note;
    - the chezmoi guides, `config.toml` and the Claude template;
    - commit history for the roadmap records in nine repositories;
    - the folders on disk for the estate renames, the source stores and the eight agentic harnesses;
    - the open queries already held in `queries.md`.
  - Nothing was added to the file while I worked, so nothing was lost.
- Commit `6252698a`, `docs(work): ki mark, strike decisions`, includes `decisions.md` and `state.md` by explicit path. It passed the scoped audit with no failures. It is not pushed.
- Kept because I was unsure of a home (each is still in the log):
  - The deferral of Project closures (9 October) and the website record holds: no record by that id was found.
  - PRFLOW and PIN: no home found in the harness or tools-ki.
  - The STATE run-folder retention rule: found only in a sources file.
  - DESIGN-SYSTEM and its Techmedix caveat.
  - SPEC-REVIEW and KI-RELEASE ordering.
  - The parked split of macOS defaults out of Rig, and the clause keeping other territories parked.
  - The roadmap burn-down focus and RIG-REL-PATCH: found only inside an old re-bootstrap message in another work's log.
  - The capture-landing wishes, ROADMAP-SIZING and ROUTE-LOCAL.
  - The model fallback instruction.
  - GRANOLA-SUPPORT, BINARY-HOME and ACQ-FOCUS: found only in reports and dry runs.
  - The SEAT-RECORD host binding, FW-DECLARE, FW-DECLARE-NOW, the SSH-SPARE-KEY console note and TOML-OPENER: found only in Rig: chezmoi run reports.
  - FW-ADR: KI-TOOL-RIG-CORE-047 is still open and both ADRs are still proposed.
  - The intake items not yet homed (MGIT-ESCAPE, MGIT-OUTPUT, GIT-SURFACE, MAC-CLOUD, CAPTURE-ONLY, DIAGRAMS-BLACK).
  - AWAITING-REVIEW, KI-AGENTS-NAME, GO-AHEAD, PILOT-SEED and SEND-BACK.

## In Progress

Nothing is running from this run. `review-hold` runs separately in the same work folder.

Outstanding - no action requested now:

- The commit is local. It goes out with State of play's next push.

## Queries

### HOMELESS-STANDING - standing rules kept with no home in the work's next steps

**Context:** The decisions life cycle wants each standalone or standing entry that has no Decision Record yet to be carried as `homeless: <TAG>` in `state.md`'s next steps, so the Summary shows it. My brief let me change only `method_read` there. The standing entries kept in the log with no other home are:

- the roadmap burn-down focus (14 October);
- GO-AHEAD (17 October);
- PRFLOW and PIN (9 October);
- RIG-REL-PATCH's follow-up releases ask first (14 October);
- the other territories kept parked (12 October);
- SPEC-REVIEW and KI-RELEASE ordering (12 October).

**Query:** Should the coordinator add `homeless:` lines for these at its next state write and route each to a proper home?

**Options:**
a) (recommended, confidence medium - the standard asks for it, but which entries count as standalone is a judgement) The coordinator adds one `homeless: <TAG>` line per standing entry to `state.md`'s next steps and routes the harness and tools rules (PRFLOW, PIN, RIG-REL-PATCH, burn-down) to ki.ways-of-working for a home in a standard or `AGENTS.md`.
b) Leave them in the log until the next mark and decide then.

### CHEZMOI-CARRY - Rig: chezmoi items carried only in its run reports

**Context:** FW-DECLARE, FW-DECLARE-NOW, the SSH-SPARE-KEY console note, the SEAT-RECORD host binding (home to terra, hub to sol) and TOML-OPENER all govern live work in ki.chezmoi. Inside its package they appear only in run reports, which get deleted at its tidies. None of them is in its decisions log or queries, and the firewall declaration is not yet in the chezmoi source. So I kept them here rather than reducing them to pointers.

**Query:** Should State of play send ki.chezmoi one messages line asking it to carry these in its own package, so the next mark can strike them here?

**Options:**
a) (recommended, confidence high - this is a route line within State of play's authority, and it changes nothing in chezmoi) Send one line to ki.chezmoi's `messages.md` naming the five items, and strike them here once its package carries them.
b) Keep them here until ki.chezmoi finishes.

### MODEL-FALLBACK - a spent instruction kept

**Context:** On 14 October Kris said: "If any of our threads get stuck, change them to claude-opus-5-5 at their same effort, at least until the next reset." The reset it waited for has long passed. No home carries it, so under the strike rule I kept it.

**Query:** Can a time-bound instruction whose window has passed be struck at the next mark without a home?

**Options:**
a) (recommended, confidence medium - it no longer governs anything, but the strike rule as written needs a home) Yes: strike it at the next mark, and strike any later entry that is spent and bounded in time in the same way.
b) Keep it until the standard says how spent entries are handled.

### 🤖 → 👤 Handoff to supervisor · since 19:07 BST

👤 3 with you

- [with you] HOMELESS-STANDING · owner · since 19:07
- [with you] CHEZMOI-CARRY · owner · since 19:07
- [with you] MODEL-FALLBACK · owner · since 19:07
- [committed] work folder, not pushed
