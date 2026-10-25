# wow-review-triage - masked blind review of three owner queries

You are an independent reviewer. Read only what this brief and the evidence it links name; never read anything under `+/_WORK/ki.ways-of-working/` other than files a Context links, and never read `design/messages-triage.md`, `queries.md`, `decisions.md` or any run report.

For each query below, the options are listed in no order. Read the evidence, then give for each one recommendation with confidence high, medium or low and a one-line reason, and the strongest point for the best other option. Write nothing in any repository.

## UNATTENDED-AND-DUE-DATES - adopt the eight criteria as the unattended assessment

**Context:** Kris, 24 October, through Personal's State of play: "we need to push that into the ways of working thread as something that we need to do an assessment of", and roadmap records should carry an explicit due date or key milestone date "of what they're working towards". The due-date half is done: DUE-FIELD was decided at 01:43 GMT today and harness `1af72f2e` added the optional `target` mapping (`date`, `kind` of `due` or `milestone`, `what`) to the `ki-work-roadmap` format standard, with the nearer date ordering work within one horizon and priority. The assessment half is not. Personal's prototype tests each record against eight ordered criteria, `no-owner-judgement`, `no-outward-act`, `one-repo-authority`, `reversible`, `self-verifiable`, `unblocked`, `scoped` and `agent-step`, the first failure deciding `unattended`, `near-miss` with one question, or `attended`; across 76 open Personal records it found 9, 21 and 46. Each criterion cites an existing rule rather than restating one, and eligibility is not authority. The open query UNATTENDED-FIELD asks only where a verdict is recorded (a record mapping or a per-window note) and bundles the criteria into that choice; the Codex blind review that kept it at medium asked for the criteria to be reviewed before they are standardised. Today `ki-delegation`'s unattended deny list says what a window never does and `ki-coordination`'s unattended windows section says what a coordinator may progress, but neither says how a record is judged eligible, and the format standard states "No unattended-eligibility field is adopted".

**Query:** Should the eight criteria, in their order with the three outcomes, become the eligibility assessment in `ki-delegation`, leaving UNATTENDED-FIELD to decide only where the verdict is recorded?

**Options (unranked):**

- Adopt them into `ki-delegation` beside the unattended deny list as the assessment every window plan uses, with a harness run writing them and the field question staying with UNATTENDED-FIELD.

- Pilot them on one more territory's roadmap in a design note first, then adopt with the lessons.

- Keep them as Personal's local prototype and let each territory judge eligibility in its window plan.

### WAKE-SUBSTRATE - whether the outage evidence lifts the launchd deferral

**Context:** Moved from hnr's parked queries on 24 October by Kris's "Move all three to Ways of Working". On 23 October at 02:37 BST, under Kris's grant to act where confidence is high, the coordinator took WAKE-SUBSTRATE a) as reviewed to high: pursue the completion watcher first, label session wakes best effort, defer launchd, doorbells and liveness fields. The watcher has since shipped as `ki agent wait --next` in tools-ki and the standard's Monitoring section. HNR's debrief reports the two 22 October outages: between 03:21 and 05:00 BST every wake hit the plan's session usage limit, and between 06:25 and 07:30 BST the coordinator sat inside one turn waiting on two `rm -rf` permission prompts; it names idle-only firing the main hazard, since a blocked turn silences every wake and notification, and recommends one Rig launchd job on `StartCalendarInterval` running a shell-only check (has `messages.md` changed, has a run finished, has a deadline passed) that spends model time only when something is new, built by Rig and chezmoi once Kris chooses it, with Ways of working writing the contract for a headless coordinator pass. HNR has stopped its own wakes and deploys sites only on request until a durable wake exists. Claude Code's schedules remain session-only and fire only when the session is idle.

**Query:** Should the launchd shell-check wake now become the next unit after the completion watcher, or stay deferred?

**Options (unranked):**

- Lift the deferral in order: Ways of working writes the headless-pass contract (what a pass may do, its budget, its report) into `ki-coordination`, then sends the launchd job as a line to ki.chezmoi and ki.mac-studio-setup.

- Keep the 23 October order: session-only wakes with stop words, revisit after the usage-limit and blocked-turn causes are addressed.

- Build the launchd job first and write the contract from what it needs.

### UNWRITTEN-RULES-DRAFTS - drafts only in Linear, Notion and Slack

**Context:** The third HNR rule: an agent creates drafts in Linear, Notion and Slack and never sends, publishes or changes state others see. Today the deny list bars "messages to people or new publication" in an unattended window, and the authority tiers say no footer authorises "publication outside the cited task"; neither names these three platforms or covers an attended turn. The MCP tools for all three can write directly.

**Query:** Should the rule be confirmed as standing for every session, and where should it live?

**Options (unranked):**

- Confirm it: in Linear, Notion and Slack an agent drafts and Kris sends, publishes or moves state, written into `ki-delegation`'s authority tiers beside the publication ban.

- Confirm it for HNR only, in hnr-principal's AGENTS.md.

- Not a rule: the publication ban is enough.
