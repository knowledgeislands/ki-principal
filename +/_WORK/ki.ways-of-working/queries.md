# ki.ways-of-working queries

## Open

### CONTRACT-ACCEPT - accept the agent control and launch-defaults draft

**Context:** Kris approved drafting CONTROL-CONTRACT and DEFAULTS-CONTRACT for acceptance before one tools-ki build. The [draft](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/agent-control-contract.md>) recommends: stop sends a verified SIGTERM to the run's own process group with a 30-second grace and no automatic hard kill; dequeue is transactional and refuses a worker that has already started; wake is tied to one exact native session with an absolute owner-authorised expiry and no blind retry; and seven launch roles set runtime, model, effort and footer, with explicit options winning inside role guards. Its proposed model pins and native wake support are not yet proven locally, so they stay disabled until evidence exists. The tools-ki command build comes before the Harness wording.

**Query:** Accept the draft's six recommendations and commission the bounded tools-ki build?

**Options:**

a) (recommended, confidence high - every control has an observable refusal path, and unproved capabilities stay off until evidenced) Accept all six and commission the build, requiring local evidence before enabling model pins or a native wake adapter.

b) Send named parts (stop, dequeue, wake, roles or the acceptance footer) back for revision first.

c) Defer the controls and keep naming runtime, model, effort and footer explicitly.

### RIG-RELEASE-REVIEW-BOUNDARY - tag tools-rig v0.8.0 with open review gates?

**Context:** v0.8.0's range contains KI-TOOL-RIG-CORE-053 (awaiting review), KI-TOOL-RIG-CORE-062 (in progress after refused acceptance) and KI-TOOL-RIG-CORE-047 (attended acceptance gaps); KI-TOOL-RIG-CORE-056 accepted the investigation only. All local gates pass; the CI pin is being repaired.

**Query:** Should tagging wait for those review gates, or proceed after green CI with them open?

**Options:**

a) (recommended by the release run, confidence high - keeps release and acceptance distinct) Hold tagging until the owning work settles the review gates; this waits on undated attended host work.

b) (recommended by the blind review, confidence medium - release policy does not require every included record closed; CORE-053 is observe-only, CORE-047's firewall already shipped in v0.7.0 and CORE-062 only narrows it with conservative refusal, but second-host discovery is unconfirmed) Tag after green CI and the normal release checks, carrying the open records and their limits into the release notes; publication is not record acceptance or permission for live convergence.

## Parked

- SITE-SOURCE - KI-WEBSITE-SITE-044's ki-design citation and visual checks; recommended a) keep awaiting review until ki-design is readable, then Kris's visual checks. Kris, 2026-10-21 14:10 BST: come back later.
- RIG-ATTENDED - Kris's attended Rig checks on sol and terra (CORE-069, CORE-068, then CORE-047 and -062); recommended a) one attended session in that order. Kris, 2026-10-21 14:10 BST: come back later.
- TECHNE-006-REVIEW - Kris reviews KI-TOOL-TECHNE-CLI-006's replanned guarded host commands; recommended a) review and release to Ready. Kris, 2026-10-21 14:10 BST: come back later.
- GOV189-SCOPE - Narrow KI-HARNESS-GOV-189 to the decided level check and [behind]; recommended a) narrow it. Kris, 2026-10-21 14:10 BST: come back later.
- GOV202-ADOPT - Adopt KI-HARNESS-GOV-202's skill-area stats badge; recommended a) adopt to Next, blind review prefers c) keep in triage. Kris, 2026-10-21 14:10 BST: come back later.
- EMERGING - KI-PRINCIPAL-MOD-008 Emerging Concepts; recommended a) adopt Fictional Lineage into Background, leave the other three open. Kris, 2026-10-21 14:10 BST: come back later.
- NO-GATE (with PKGLESS-GATE) - project shape commit gate; Kris will come back to it. a) `ki repo audit --skill ki-repo` staged, check-only; review prefers widening KI-HARNESS-GOV-225.
