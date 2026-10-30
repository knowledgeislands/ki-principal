<!-- rumdl-disable MD041 -->

### WORKER-WAIT-GATED

**Context:** Some authorised units cannot be briefed or queued yet because they wait on something outside this work's runs: another work's reply, a person, a date, a host, or model capacity lost to a usage limit or outage. Nothing will start them until someone acts on an event. While other units run or are queued the work is With worker anyway; the question arises only when gated units are all that remain. The current capacity rule would keep such work with the worker indefinitely, which can show a With worker with nothing running and no heartbeat for days. REST-PORTABLE makes At rest · waiting the honest state for a real wait, but at the cost of the full stop: drain, the portability checks, parked queries and a struck mark, even for a short reply. A live coordinator wakes at least every five minutes and reads `messages.md` at each wake, so it notices a reply line; once the session ends nothing does, unless a granted headless pass names the work.

**Query:** When gated units are all the authorised work that remains, does the work stay With worker or stop to At rest · waiting?

**Options:**

- Stay With worker while any authorised gated unit remains, however long the gate, each shown as an item naming it.
- Stop to At rest · waiting as soon as nothing of this work is running or queued, however short the gate.
- Stay With worker, each gate shown as an item naming it, `[handoff]` where it is other work or a person, only while the orchestrator session that will act on it is open and waking; conclude and stop to At rest · waiting, the gate as release, before that session ends or when the gate is a date or outlasts it.

### HOST-CADENCE

**Context:** Kris's shape is hourly, publishing primaries "on the hour" and secondaries "five minutes later". Each territory has one primary host, so at any slot the two hosts touch disjoint territories, and the brief's extra two-minute host stagger protects nothing measured. No phase duration, sleep or wake behaviour has been measured, and offsets confer no exclusion or completion proof. The reviewers disagree: Claude recommends Kris's `:00` primary and `:05` secondary on both hosts at medium confidence, because the sets are disjoint and the attended run measures duration before activation; Codex recommends measuring attended passes first and keeping the hourly pattern only as a candidate, at medium confidence, because durations and wake behaviour are unverified. Both accept one attended run per host before any recurrence. An earlier blind review preferred measuring first. Nothing is activated either way.

**Query:** Should Rig prepare Kris's hourly `:00`/`:05` cadence now, confirmed by each host's attended run, or leave the cadence unchosen until measured?

**Options:**

- Prepare the brief's staggered phases: Terra primary `:00` and secondary `:05`, Sol primary `:02` and secondary `:07`.
- Keep cadence unchosen; prepare attended passes only, and return a recurring plan once they have measured phase duration and wake behaviour.
- Prepare hourly phases on both hosts: primary `:00`, secondary `:05`, a pull-only read-back shortly after, each host's first attended run confirming phase duration fits before activation.

### HOST-COVERAGE

**Context:** Kris asked for a dotfiles entry naming "per territory" the primary and secondary host. Both reviewers have Rig and chezmoi propose the map and Kris approve it before any configuration or operation, at territory grain with explicit exclusions, the chezmoi source as a named member and the resolved per-repository membership recorded per occurrence. [ADR-KI-PRINCIPAL-007](../../../../Admin/Governance/Decisions/ADR-KI-PRINCIPAL-007-territory-seats-on-hosts.md) says "Each territory has one seat and one standby", and the sender's line named `seats.yaml` as the nearest entry, but seats mean coordination landing, not sync primacy. The reviewers disagree: Claude recommends starting the proposal from seat host as primary and standby as secondary, active-active territories primary on the hub, for Kris to confirm in one answer, and saying when HNR joins, at medium confidence; Codex recommends not inferring from seats, enumerating repository, branch and phase eligibility, and piloting one jointly nominated non-HNR, non-deploying repository, at high confidence.

**Query:** Should Rig and chezmoi start their proposed map from the seats, for Kris to confirm or amend, or build it without that starting point?

**Options:**

- Kris supplies the map and pilot repository directly; the receiving owners verify eligibility and prepare its bounded plan.
- Rig and chezmoi propose a territory-grain map starting from seat host as primary and standby as secondary, active-active territories primary on the hub, with exclusions, resolved membership and the point at which HNR joins; Kris approves or amends it before configuration; the first attended run uses one non-HNR, non-deploying repository.
- Rig and chezmoi propose the map without the seats starting point, enumerating repository, branch and phase eligibility, and return it for approval before configuration, starting from one jointly nominated non-HNR, non-deploying pilot repository.

### HOST-READBACK

**Context:** Kris said "we probably want to do a resync as well in short order after it". Next-hour read-back leaves secondary-origin work about 55 minutes before the primary consumes it. Both reviewers now prefer a prompt pull-only read-back, keeping next-occurrence recovery: Claude at `:10` on each primary, at medium confidence, because it is what Kris described and costs one fetch; Codex at `:10`/`:12` if the hourly candidate holds, at medium confidence, because exact slots depend on measured duration. An earlier blind query review agreed with next-hour read-back at high confidence; it predates both design reviews. Read-back matters only for published work, so it depends on HOST-SECONDARY-PUBLISH, and its slot follows HOST-CADENCE. It adds no publication authority or acknowledgement.

**Query:** Should each primary run a short pull-only read-back after the secondary phase, or wait for its next hourly occurrence?

**Options:**

- Read published secondary-origin updates at the start of the primary's next hourly occurrence, stating the roughly 55-minute delay.
- Prepare a pull-only read-back on each primary shortly after the secondary phase, its slot following HOST-CADENCE, keeping next-occurrence recovery for late or missing work and promising no immediate convergence.
