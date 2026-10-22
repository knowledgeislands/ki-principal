# ki.ways-of-working queries

## Open

### RIG-RELEASE-REVIEW-BOUNDARY - tag tools-rig v0.8.0 with open review gates?

**Context:** v0.8.0 is green on its exact commit a2bc10939462e387b18dcdaedb54e886ac00386a, with the dossier in `/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-ci-fix.report.md`. Its range contains KI-TOOL-RIG-CORE-053 (awaiting review), KI-TOOL-RIG-CORE-062 (in progress after refused acceptance) and KI-TOOL-RIG-CORE-047 (attended acceptance gaps); KI-TOOL-RIG-CORE-056 accepted the investigation only. All local gates pass; the CI pin is being repaired.

**Query:** Should tagging wait for those review gates, or proceed after green CI with them open?

**Options:**

a) (recommended by the release run, confidence high - keeps release and acceptance distinct) Hold tagging until the owning work settles the review gates; this waits on undated attended host work.

b) (recommended by the blind review, confidence medium - release policy does not require every included record closed; CORE-053 is observe-only, CORE-047's firewall already shipped in v0.7.0 and CORE-062 only narrows it with conservative refusal, but second-host discovery is unconfirmed) Tag after green CI and the normal release checks, carrying the open records and their limits into the release notes; publication is not record acceptance or permission for live convergence.

## Parked

- RIG-ATTENDED - Kris's attended Rig steps on sol and terra, commands in `/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-rig-attended-steps.report.md`; recommended a) CORE-069 on sol plus the look-only CORE-047 and CORE-062 checks first, CORE-068 and the live firewall rollout in a later sitting. Kris, 2026-10-22 02:26 BST: walk me through it in the morning.
