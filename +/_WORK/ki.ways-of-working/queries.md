# ki.ways-of-working queries

## Open

### DRAIN-END - should an explicit drain check end with its DRAINED / NOT DRAINED line?

**Context:** When you asked a coordinator to drain, a prompt that put a final DRAINED / NOT DRAINED line last worked well; the standard requires every banner to end with the thread line. The coordination-lessons proposal and a blind review disagree. Nothing changes until you decide.

**Query:** Should an explicitly requested drain check end with the drain result after the thread line?

**Options:**

a) (recommended by the blind review, confidence high - one closing rule everywhere, no exception to maintain) Keep the thread line last in every case and put the drain result in Done.

b) (recommended by the proposal, confidence medium - honours the ending you asked for) Put the DRAINED / NOT DRAINED line after the thread line, only for an explicit drain check.

### SORT-ARM - cancel the conditional ARM Linux release record [KI-TOOL-KI-CLI-125](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-125-ki-release-contract.md)

**Context:** The record is held until an ARM Linux host is needed; vega is x86 and sol is macOS arm64, both already covered by release archives, and no ARM Linux host exists or is planned. It also carries a reusable release-contract requirement (per-platform archives, checksum manifest, signature, embedded installer key). The roadmap sort proposed cancelling it; a masked blind review agreed at high confidence, noting your 20 October review chose to keep it held.

**Query:** Should the record be cancelled, with ARM Linux kept as an Agent host Idea and the release-contract requirement kept as a short section in the tools-ki release guide?

**Options:**

a) (recommended, confidence high - reviewed; current hosts are covered and the requirement survives in the guide) Cancel it, add the ARM Linux Idea under the Agent host and the contract section to the release guide.

b) Keep it held until an ARM Linux host is needed.

## Parked

- RIG-ATTENDED - Kris's attended Rig steps on sol and terra, commands in `/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-rig-attended-steps.report.md`; recommended a) CORE-069 on sol plus the look-only CORE-047 and CORE-062 checks first, CORE-068 and the live firewall rollout in a later sitting. Kris, 2026-10-22 02:26 BST: walk me through it in the morning. The tools-rig v0.8.0 tag waits on the same review gates (RIG-RELEASE-REVIEW-BOUNDARY a), 2026-10-23).
