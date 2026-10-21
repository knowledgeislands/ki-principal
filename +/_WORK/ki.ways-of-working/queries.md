# ki.ways-of-working queries

## Open

### TOOLSKI-TAG - tag and publish tools-ki v0.13.0

**Context:** v0.13.0 is verified and pushed at 65e062737e3efaa696c5d92aaf2f8fc8bf31d1e9, with the Harness archive pinned and exact-head CI observed; the tag and publication commands are in the [dossier](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-toolski-pin.report.md).

**Query:** Tag and publish v0.13.0 from the dossier?

**Options:**

a) (recommended, confidence high - every release gate passed on the exact commit) Kris tags and publishes with the dossier's commands.

b) Hold the release.

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
