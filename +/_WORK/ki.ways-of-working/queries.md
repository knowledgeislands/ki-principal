# ki.ways-of-working queries

## Open

### RIG-RELEASE-REVIEW-BOUNDARY - tag tools-rig v0.8.0 with open review gates?

**Context:** v0.8.0 is green on its exact commit a2bc10939462e387b18dcdaedb54e886ac00386a, with the dossier in `/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-rig-ci-fix.report.md`. Its range contains KI-TOOL-RIG-CORE-053 (awaiting review), KI-TOOL-RIG-CORE-062 (in progress after refused acceptance) and KI-TOOL-RIG-CORE-047 (attended acceptance gaps); KI-TOOL-RIG-CORE-056 accepted the investigation only. All local gates pass; the CI pin is being repaired.

**Query:** Should tagging wait for those review gates, or proceed after green CI with them open?

**Options:**

a) (recommended by the release run, confidence high - keeps release and acceptance distinct) Hold tagging until the owning work settles the review gates; this waits on undated attended host work.

b) (recommended by the blind review, confidence medium - release policy does not require every included record closed; CORE-053 is observe-only, CORE-047's firewall already shipped in v0.7.0 and CORE-062 only narrows it with conservative refusal, but second-host discovery is unconfirmed) Tag after green CI and the normal release checks, carrying the open records and their limits into the release notes; publication is not record acceptance or permission for live convergence.

### CUSTOMS-WORDS - drop "Customs" and "clearance" from Acquire?

**Context:** KI-PRINCIPAL-MOD-009 amends ADR-KI-PRINCIPAL-001's staging wording to the 20 October Acquire model. On 18 October you adopted "Customs" and "clearance" for Acquire, recorded only in a retired note; you have since called Acquire "simply a sorting office", and the Glossary already uses Customs for an island's boundary rules.

**Query:** Drop "Customs" and "clearance", keeping "the port" and "sorting office"?

**Options:**

a) (recommended, confidence high - reviewed: the Glossary clash is real and your later words point this way) Drop them; a run drafts the exact wording for your confirmation and takes KI-PRINCIPAL-MOD-009 to awaiting-review.

b) Keep "Customs" as the facility and "clearance" as its act, resolving the Glossary clash in the same amendment.

### TAGS-NEXT - keep the 27-note tags pilot and take the convention forward?

**Context:** The pilot found 4-11 tag results against 19-127 full-text results; tags helped most for subjects that cross zones (governance, work) and added little where one chapter already gathers a subject. The figures were self-scored; the change is one revertible commit.

**Query:** Keep the pilot tags and reconcile the Tags convention, or revert?

**Options:**

a) (recommended, confidence high - reviewed: consistent across five questions) Keep them; reconcile the Tags convention through the Enactment Process, tagging only cross-zone subjects, leaving `card/*`, `date/*` and `source/*` for later.

b) Keep them but take no further step until a whole-site review.

c) Revert the pilot and rely on folders, links and full text.

### ECO013-CANCEL - approve cancelling and pruning KI-PRINCIPAL-ECO-013?

**Context:** Overnight a run cancelled KI-PRINCIPAL-ECO-013 (PMO extraction pilot) as superseded. Two high-confidence reviews refused pruning: your overnight grant does not plainly approve this cancellation, the ki-accept step was skipped and a link survives. It stays cancelled and unpruned.

**Query:** Approve the cancellation so a run can complete ki-accept, repair the link and prune it?

**Options:**

a) (recommended, confidence medium - the reviews agree it is superseded but want your explicit word) Approve; ki-accept, link repair and prune follow.

b) Reopen it as draft.

## Parked

- RIG-ATTENDED - Kris's attended Rig steps on sol and terra, commands in `/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-rig-attended-steps.report.md`; recommended a) CORE-069 on sol plus the look-only CORE-047 and CORE-062 checks first, CORE-068 and the live firewall rollout in a later sitting. Kris, 2026-10-22 02:26 BST: walk me through it in the morning.
