# ki.agent-host queries

## Open

### CHAIN-GATE - The Rig convergence holds wait on each other

**Context:** [KI-TECHNE-OPS-018](/Users/krisbrown/workspaces/knowledge-islands/ki-techne-harness/docs/roadmap/KI-TECHNE-OPS-018-converge-tools-through-rig.md) (converge vega's tools through Rig) is held until Rig installs a signed `ki` release and `rig status` stays clean through a pin bump on the rebuilt vega. Rig's install kind for that, [KI-TOOL-RIG-CORE-048](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-048-signed-release-install-kind.md), is held until vega is rebuilt and the harness's converge-through-Rig work leaves its hold. vega was rebuilt on 14 October, so the only thing keeping both held is that each waits for the other. [KI-TECHNE-OPS-024](/Users/krisbrown/workspaces/knowledge-islands/ki-techne-harness/docs/roadmap/KI-TECHNE-OPS-024-weekly-pin-bump.md) (weekly pin bump) waits for the role-profile move to `roles/`, which was merged into KI-TECHNE-OPS-018, so it is caught in the same loop. The Techne Programme Focus keeps vega in scope, but the 14 October burn-down asks for no widening.

**Query:** Should Rig's signed-release install kind be released so the chain can move?

**Options:** a) (recommended, confidence medium - it is the only gate left in the loop and serves vega, but it puts a capability record back in the queue during the burn-down) Release KI-TOOL-RIG-CORE-048 in tools-rig to `soon`, with Shaping, leaving KI-TECHNE-OPS-018 and KI-TECHNE-OPS-024 held until it delivers. b) Keep all three held and re-word KI-TOOL-RIG-CORE-048's condition to "Kris takes up converging vega's tools through Rig", so the loop waits on a named decision rather than on itself. c) Separate the role-profile move from KI-TECHNE-OPS-018 so KI-TECHNE-OPS-024 can proceed on its own, leaving the Rig gates as they are.

### CLI125-HOLD - The ki release contract's hold condition is met but nothing needs it yet

**Context:** [KI-TOOL-KI-CLI-125](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-125-ki-release-contract.md) (one KI release contract with a linux-arm64 archive) is held until "an ARM host is needed, or vega is rebuilt", and its adoption note says to review it with the vega rebuild. vega was rebuilt on 14 October as an x86 `t3.medium`, no ARM host exists or is planned, `ki` already ships signed archives for the three platforms in use, and Rig's install kind does not depend on it. tools-ki has another session's uncommitted changes, though not in this record.

**Query:** Now that vega is rebuilt, should the release-contract record be released or held on the ARM need alone?

**Options:** a) (recommended, confidence medium - the rebuild was a review trigger, and the fresh review finds no current need, but the contract write-up could also help Rig's install kind) Keep it on hold, re-worded to "An ARM host is needed", with the same review date. b) Release it to `soon` with Shaping, so the contract is written down ahead of any ARM host.

### CLI006-PLAN - The guarded host commands plan is back in the queue

**Context:** [KI-TOOL-TECHNE-CLI-006](/Users/krisbrown/workspaces/knowledge-islands/tools-techne/docs/roadmap/KI-TOOL-TECHNE-CLI-006-guarded-host-commands.md) was released to `next` this run, because its hold waited only for agent-host work to resume. Its plan was published on 12 October and waits for your review before Ready. Its source review predates the host-patching work, which has since been accepted, and the plan itself says the guarded status must be re-grounded against that result.

**Query:** How should the plan reach Ready?

**Options:** a) (recommended, confidence high - the plan's sources are eight days old and it names the re-grounding itself) Have a ki-plan run re-ground the plan against today's tools-techne and harness sources and bring it to you for Ready. b) Review the 12 October plan as it stands. c) Leave it at draft `next` until the Rig chain moves.

## Parked

- **DEV-MODE** (with State of play): Kris chose that Rig owns `rig dev local|release <tool>`; handed to State of play on 14 October, which holds it with RIG-LINK for Kris's decision. Recommended: leave it with State of play.
- **RIG-LINK** (with State of play): `~/.local/bin/rig` links to the retired `~/workspaces/kit/knowledgeislands/tools-rig` path and is broken; it belongs to the Rig work. Recommended: leave it with State of play.
- **Firewall** (with ki.mac-studio-setup): KI-TOOL-RIG-CORE-047 (macOS) and KI-TOOL-RIG-CORE-051 (Linux nftables) were delivered there; nothing is planned here. Recommended: leave it with that work.
- **HARNESS-INSTRUCTIONS** (parked 9 October): Kris wants the Claude and Codex instructions to become skills from a personal harness, leaving thin `CLAUDE.md` and `AGENTS.md`. Recommended: raise it with State of play when picked up.
