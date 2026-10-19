# query-review-6

Blind review of two queries. Read-only: make no writes and no commits. Read the records and `ki-principal/Admin/Governance/Policies/Techne Programme Focus.md`, then give your own recommendation for each, with its confidence (high, medium or low) and your reasons.

1. **CHAIN-GATE.** KI-TECHNE-OPS-018 in ki-techne-harness (converge vega's tools through Rig) is held until Rig installs a signed `ki` release and `rig status` stays clean through a pin bump on vega. KI-TOOL-RIG-CORE-048 in tools-rig (a signed-release install kind) is held until vega is rebuilt and OPS-018 comes off hold. vega was rebuilt on 14 October. KI-TECHNE-OPS-024 (weekly pin bump) waits on a role-profile move inside OPS-018. The 14 October burn-down focus asks that the roadmap not be widened. Options:
   - A: release CORE-048 to `soon` with a Shaping section, and keep OPS-018 and OPS-024 held until it is delivered.
   - B: keep all three held, with CORE-048's condition reworded to "Kris takes up converging vega's tools through Rig".
   - C: split the role-profile move out of OPS-018 so OPS-024 can proceed on its own.
2. **CLI125-HOLD.** KI-TOOL-KI-CLI-125 in tools-ki (one KI release contract, adding a linux-arm64 archive) is held until "an ARM host is needed, or vega is rebuilt". vega was rebuilt as an x86 `t3.medium`, and no ARM host is planned. Options:
   - A: keep it held, with the condition reduced to "An ARM host is needed".
   - B: release it to `soon` with a Shaping section.

Report to the path your run packet names, as an owner report: Done, In Progress, Queries.
