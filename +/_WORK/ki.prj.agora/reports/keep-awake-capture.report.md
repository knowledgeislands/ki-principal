# KI > Techne > Agora › keep-awake-capture

**🤖 → 👤 Handoff to supervisor · Run report at 23:40 GMT · last mark 01:44 GMT · blocked**

---

## Done

- Drafted both records in full, ready to commit unchanged, in the run state folder's `keep-awake-capture.drafts/`: [KI-AGORA-WRK-003 Keep the host awake while work runs](/Users/krisbrown/.local/state/ki/agents/ki-prj-agora/keep-awake-capture.drafts/KI-AGORA-WRK-003-keep-host-awake-while-work-runs.md) and [KI-AGORA-LVL-001 Check host settings against Rig](/Users/krisbrown/.local/state/ki/agents/ki-prj-agora/keep-awake-capture.drafts/KI-AGORA-LVL-001-check-host-settings-against-rig.md). Both are triage, no horizon, medium priority, size m, assigned to `work/ki.prj.agora`, with the Goal, Context, Boundary and Discussion the brief asked for.
- Markdown check under the repository's own configuration: passed for both drafts.
- Nothing was written, reserved or committed in `apps-agora.local`; it is clean and level with `origin/main`.

## In Progress

Nothing. The capture itself is held for the query below.

## Queries

### Q1 - Who commits the two records

**Context**

`ki-next`'s capture rule carries Kris's CAPTURE-GATE a) of 19 October: "runs never create records; the owning work's coordinator captures". Its standard says a background run never creates a record and names the candidate in its report instead. This brief asks a background run to capture on the coordinator's behalf, which that rule does not allow, and the run rules say to stop rather than guess.

**Query**

How should the two records reach the repository?

**Options**

a) (recommended, confidence high - it keeps the gate as Kris set it and costs the coordinator two short commits) The coordinator captures them itself: commit the ledger advance (`LVL` to 1, `WRK` to 3) alone as the reservation, then copy the two drafts into `docs/roadmap/` unchanged and commit them with the `Work-Id: ki.prj.agora` trailer.

b) Kris confirms this run may capture on the coordinator's behalf, recorded in the decisions log, and the run is relaunched citing that entry.

### Q2 - Areas chosen

**Context**

The repository's areas are fixed. Keeping the host awake is filed under `WRK`, "Waking workers and run-once jobs", as it follows the work Agora sees running; checking host settings is filed under `LVL`, "Keeping level and the group's state", as it reports drift the way Agora reports checkouts.

**Query**

Do those areas stand?

**Options**

a) (recommended, confidence medium - both fit an existing area, and adding an area is a configuration change) Keep `WRK` and `LVL`.

b) Add a host area, such as `HST` for host settings and power, to `.ki.toml` and the ledger first, and file both records there.

🧵 ki.prj.agora
