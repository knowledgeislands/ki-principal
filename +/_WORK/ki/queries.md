# ki queries

## Open

### REVIEW-HOLD - live or dead for six held work folders

since 2026-10-19 · from review-hold, reviewed by query-review-2 (agrees)

**Context:** Six work folders wait in `+/_WORK_REVIEW/`. ki.agent-host and ki.paperclip-capture-and-rebuild belong to active Techné Projects whose notes link design papers in these folders; ki.estate-factorisation is the only home of its active Project's close-out, whose phase gates are still open. ki.baseline-rollout is the old copy of a package rebuilt in `+/_WORK/` today; two parked items, CHECKLIST and the `update-ki-pin.yml` payload-field mismatch, exist only there. ki.regular.command-centre is carried by the Observatory and Ways of working Project notes. ki.regular.skill-reviews (ki-agentic-harness) is finished, its record accepted and pruned. On-hold work does not count against the cap. The reviewer adds that Agent host has a standing exemption from the Techne Programme Hold, so its package should not wait on the hold lifting.

**Query:** Should the three live folders return to `+/_WORK/` on hold and the other three be deleted?

**Options:**

a) (recommended, confidence medium - reviewed; deletion rests on the harness remote not being fetched) Move ki.agent-host, ki.estate-factorisation and ki.paperclip-capture-and-rebuild back as on-hold packages; copy the two baseline-rollout items into the live package's parked queries; then delete the three dead folders. b) As a), but delete ki.estate-factorisation too, after sending its four open items to State of play. c) Keep all six held until the Techne Programme Hold lifts; delete only command-centre and skill-reviews now.

### HOMELESS-STANDING - standing rules with no proper home

since 2026-10-19 · from sop-mark, reviewed by query-review-2 (disagrees)

**Context:** Six standing rules survive only in the decisions log: the roadmap burn-down focus (14 October), GO-AHEAD (17 October), PRFLOW and PIN (9 October), RIG-REL-PATCH's ask-first rule for follow-up releases (14 October), keeping the other territories parked (12 October), and SPEC-REVIEW and KI-RELEASE ordering (12 October). The reviewer points out that the standard asks for a `homeless:` flag only for standalone decisions, not every standing rule, and that the burn-down focus and GO-AHEAD are partly carried already, in KI-PRINCIPAL-ECO-013 and the Observatory Project note.

**Query:** How should these entries be handled?

**Options:**

a) (recommended, confidence medium - review disagrees; it would flag more than the standard asks) Add one `homeless:` line per rule to `state.md`, and route PRFLOW, PIN, RIG-REL-PATCH and the burn-down focus to ki.ways-of-working for a home in a standard or `AGENTS.md`. b) The reviewer's course: classify each entry first; route PRFLOW, PIN, RIG-REL-PATCH and the burn-down focus to ki.ways-of-working; carry live operational restrictions in `state.md` or queries; flag `homeless:` only genuinely standalone decisions. c) Leave them in the log and decide at the next mark.

### MODEL-FALLBACK - a time-limited instruction

since 2026-10-19 · from sop-mark, reviewed by query-review-2 (disagrees)

**Context:** On 14 October Kris said: "If any of our threads get stuck, change them to claude-opus-5-5 at their same effort, at least until the next reset." That reset has passed. The reviewer reads "at least until" as a minimum, not an expiry, and found that the Ways of working Project note already carries the fallback as an evaluation idea with interim manual use, so it does have a partial home.

**Query:** Can this instruction be struck at the next mark?

**Options:**

a) (recommended, confidence medium - review disagrees; the wording sets a minimum, not an end) Strike it at the next mark, and treat later expired, time-limited entries the same way. b) Keep it until Kris clarifies it or the standard says how such entries are handled. c) Strike it here as carried by the Ways of working Project note's evaluation idea.

### THREADS-CHECKINS - Kris's question on check-ins

since 2026-10-19 · from sop-restock, reviewed by query-review-2 (disagrees)

**Context:** On 15 October Kris asked how threads are used and why there are so many check-ins. Threads are now work folders, and the Work Process sets the states and moves. The reviewer notes the standard still requires timed updates at each launch, each finish and each five-minute wake while work runs, so adopting the model does not by itself answer whether the frequency is right for Kris.

**Query:** Can the question close as delivered by the work model?

**Options:**

a) (recommended, confidence medium - review disagrees; only Kris can say whether the frequency now suits) Close it as delivered, and raise it again only if check-ins still feel excessive. b) The reviewer's course: keep it open for a short explanation of the current cadence and a talk with Kris about frequency.

### TECHNE-FOCUS - reconcile the Techné focus with the programme hold

since 2026-10-19 · from Acquire intake (misrouted), reviewed by query-review-3 (agrees, with bounds)

**Context:** On 14 October Kris said, in a session that routed it to Acquire intake: "the hold is gone, but for now we're only focusing on setting up and running the Mac Studio and the agent host, and that any other pieces of work are not something that we're building as part of Techno just now [...] keep them as ideas". The governing [Techne Programme Hold](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Policies/Techne%20Programme%20Hold.md) policy still restricts remote agent execution, and [GDR-KI-PRINCIPAL-004](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/GDR-KI-PRINCIPAL-004-standing-agent-host-exemption-from-the-techne-programme-hold.md) exempts the agent host. Policy and instruction disagree, and REVIEW-HOLD's option c) leans on the hold.

**Query:** Should the hold policy be revised to record Kris's 14 October focus?

**Options:**

a) (recommended, confidence high - reviewed; the reviewer agrees the focus should become durable policy, provided the hold's operating bounds carry over) Revise the policy through the Enactment Process to a focus rule: Mac Studio and agent host only, all other Techné work kept as ideas. Carry forward the hold's operating bounds (host scope, owner-opened sessions only, access controls, kill switch, teardown, protection of other remote services), and have Kris approve the exact replacement wording before GDR-KI-PRINCIPAL-004 is superseded or the wider hold is declared lifted. b) Keep the hold as written; treat the 14 October words as context only.

### CAPTURE-GATE - stop runs creating records

since 2026-10-19 · from [roadmap-census](roadmap-census.report.md)

**Context:** 209 records were added in the six days after the 14 October "no new feature records" focus. 57 open records (46%) are unadopted triage, mostly findings and follow-ups captured automatically by runs. The 14 October rule names what may be captured but never says who captures. `ki-next` permits triage capture without approval.

**Query:** Should only the coordinator of the owning work create records, with runs listing follow-ups in their reports?

**Options:**

a) (recommended, confidence high - the inflow data is direct and the rule only narrows who captures) Runs never capture. The owning work's coordinator captures only a blocker, a defect seen failing or a Kris request, naming the work. Ideas go to Project notes. Small audit fixes are done without a record. State of play adds this to every brief and routes a method change to ki.ways-of-working for `ki-next` and `ki-delegation`. b) Keep automatic triage capture but cap triage at 10 per repository.

### ROADMAP-CAP - caps and weekly measure

since 2026-10-19 · from [roadmap-census](roadmap-census.report.md), reviewed by query-review-3 (disagrees)

**Context:** The roadmap went from 148 to 16 in two weeks when focused, then back to 126 in seven days. There is no cap, so nothing forces a lane to close before it captures. The 14 October ROADMAP-SIZING decision already agreed daily count snapshots.

**Query:** Should the territory run to caps of 60 by 2 November and 40 by 16 November, with per-lane limits and a Monday measure?

**Options:**

a) (recommended, confidence medium - review disagrees; it finds no capacity basis for dated totals and would not block capture of defects) Territory 60 or fewer by 2 November and 40 or fewer by 16 November. Per lane: Now 5 or fewer, Awaiting review 5 or fewer, triage 10 or fewer. A lane at its cap closes before it captures. State of play reports per lane each Monday. b) The reviewer's course: trial per-Project limits of 5 Now and 5 Awaiting review, with triage above 10 triggering a disposition review; a Project at its limit starts no new work but still captures defects, blockers and Kris's requests; report each Monday alongside the daily snapshots; set territory targets after two comparable weekly measures. c) No hard caps; a weekly measure only.

### LANE-OWNERS - who owns each roadmap

since 2026-10-19 · from [roadmap-census](roadmap-census.report.md), reviewed by query-review-3 (disagrees)

**Context:** 36 open records have no live work: ki-design's 24, whose `project: ki-design` has no Project note, and the 12 email-routing drafts in mcp-m365 and mcp-gsuite. The other repositories map onto existing works. Seven holds share the agent-host unblocker. The reviewer found the 12 email-routing drafts already have a live work, [HNR Email routing](/Users/krisbrown/workspaces/humans-not-robots/hnr-principal/+/_WORK/hnr.email-routing/work.md).

**Query:** Do you agree the lane owners as proposed, with ki-design under ki.observatory and the email-routing cluster held as one?

**Options:**

a) (recommended, confidence medium - review disagrees; it would assign by record purpose, open ki.design and leave email routing with its existing work) ki.tools-burndown takes the tools repositories and mcp-git-audit. ki.observatory takes apps-observatory.local, ki-design and the website's design adoption. ki.ways-of-working takes ki-agentic-harness, ki-principal and ki-specifications. ki.chezmoi takes chezmoi. ki.mac-studio-setup takes the agent-host hold cluster and ki-techne-harness. The 12 email-routing records move to one hold until a Project opens. b) The reviewer's course: assign by each record's purpose: tools-ki, tools-mgit and tools-git-almanac to ki.tools-burndown; tools-rig and the agent-host unblock to ki.mac-studio-setup; chezmoi to ki.chezmoi; Observatory product work to ki.observatory; method work to ki.ways-of-working; estate rollout and diagram conversion to ki.baseline-rollout; portable specification work to ki.specifications. Propose a distinct ki.design work through the Project queue, assign mcp-git-audit explicitly, and leave the 12 email-routing drafts with HNR Email routing. c) Open a separate ki.design work, and give the email-routing records to ki.knowledge-acquisition.

### BURN-WAVE-1 - authorise the first wave

since 2026-10-19 · from [roadmap-census](roadmap-census.report.md)

**Context:** 22 records can close by acceptance or prune: 14 ki-design hand-off decisions, 3 tools-ki, 2 tools-rig, 1 harness, plus [KI-OBSERVA-VIS-031](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-031-who-is-working.md) and [KB-DOTFILES-UE-095](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-095-guide-continuity-check.md). About 12 more are cancellation, merge or idea candidates, listed under Done by repository. Together they take the territory from 125 to about 90. Since then `accept-awaiting` has accepted 20 Awaiting review records in five repositories, ki-design's batch among them, so what remains is mainly each lane's cancel, merge and idea list.

**Query:** Should each lane run its acceptance pass now and bring its cancel and merge list to you for one approval per lane?

**Options:**

a) (recommended, confidence high - acceptance stays with you per lane, and nothing is cancelled without your approval) Each lane owner runs one `ki-accept` pass on its Awaiting review records and presents its cancel, merge and idea list as a single query. The 14 ki-design records go as one batch. b) Present every record to you individually.
