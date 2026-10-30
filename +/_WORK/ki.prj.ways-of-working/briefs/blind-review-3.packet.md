<!-- rumdl-disable MD041 -->

### WAKE-HOST

**Context:** The Techne Programme Focus, set on 20 October, names two hosts, `vega` and sol, and allows agents on them only "in sessions the binding owner opens, with no unattended or scheduled agents". A launchd headless pass is a scheduled agent. WAKE-SUBSTRATE, a later decision in this work, does not amend a governance policy, so the pass may not run on sol or `vega` until the focus is changed through the Enactment Process. Terra, Kris's other Mac, is outside the focus. The job itself was sent to `ki.prj.chezmoi` and `ki.prj.mac-studio-setup`. A pass sees only its own host's runs, because `ki agent status` is host-local, while sol is where most coordination and the Orca trial now run. Whether a host is permitted at all is a separate matter from which host is chosen. The design treated scheduled runs as out of scope.

**Query:** On which host may the headless coordinator pass run?

**Options:**

- Propose an Enactment change to the Techne Programme Focus admitting the headless pass on sol, bounded as the standard sets it (shell-only trigger, named works only, `push` tier at most), so that the pass runs where coordination and Orca run.
- No host for now: session wakes only, until a work needs a durable wake and names its host in its own decision.
- Terra first, for works whose own decision names the pass; no pass on sol or `vega` unless the focus is later changed through the Enactment Process.
