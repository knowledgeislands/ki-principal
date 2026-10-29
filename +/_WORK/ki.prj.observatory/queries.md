# ki.prj.observatory queries

## Open

### RESTRUCTURE - Prepare remaining convergence choices

since 2026-10-20 · from obs-app044-plan and obs-review-4; factual reconciliation completed 29 October

**Context:** [KI-OBSERVA-APP-044](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md) remains Now/Draft/decide. Its [completed factual correction](away-app044-facts.report.md) now distinguishes the delivered five-area shell, Legacy and existing alias seam from the old proposal. That correction is done; choosing convergence is not. The earlier independent review supported incremental convergence at medium confidence with the step-3 gate retained. Council order, the Waiting/Review relationship, moving or retiring Work and each individual consolidation still need their own later decisions; this question selects none of them.

**Query:** Should the next design pass prepare the remaining convergence choices against the delivered design?

**Options:**

a) (recommended, confidence medium - earlier independent review supports incremental preparation, while the remaining design choices are still open) Prepare the remaining choices against the current five-area design, preserving every capability and address; return separate order, Waiting/Review and Work proposals for their own approval.

b) Keep convergence preparation parked pending the design thread's next instruction.

### TEN-COMMITS - Preserve history while considering duplicate rows

since 2026-10-20 · from obs-review-5

**Context:** The parked query asked whether to drop the Git detail panel's ten-commit list. The independent review found that it retains history missing from the newer lists, especially when no commits are unpushed, and recommended showing only commits older than the earlier-five list when both lists are visible, retaining all ten when nothing is unpushed. It also warned that splitting history by ahead count is not generally equivalent to upstream reachability in merged histories. Current presentation has not been re-verified in this pass; removing the list now would conflict with the retained lose-nothing instruction.

**Query:** Should a later bounded pass recheck the current panel and shape the review's history-preserving alternative?

**Options:**

a) (recommended, confidence medium - the independent review preserves useful history while removing overlap) Recheck the current panel, then propose only older non-overlapping commits when the newer lists appear, retaining all ten otherwise; preserve upstream-reachability correctness and require approval before implementation.

b) Keep all current lists unchanged and leave consolidation for later.

### MERMAID-HANDLER - Retain the hardening follow-up without claiming a bypass

since 2026-10-20 · from obs-review-6

**Context:** The parked query proposed stripping hostile Mermaid handlers earlier. The independent source review found the frame policy and final-output checks contained them, established no bypass and did not reproduce the intermediate handler lifetime. It preferred a future label-sanitising investigation over treating the existing allowance as a blocker. The inbox still forbids writing or updating Mermaid diagrams; this pass changes none and creates no record.

**Query:** Should the hardening follow-up remain a non-blocking candidate for a later investigation?

**Options:**

a) (recommended, confidence medium - the independent review found containment but left the intermediate path unexplained) Retain a non-blocking investigation of intermediate label rendering and earlier sanitising; preserve the policy and final-output checks, and let the owning coordinator decide capture after fresh evidence.

b) Leave the existing containment and smoke checks as they are, with the follow-up parked.

### BRIDGE-STALE - Decide whether to prepare machine-reader integration

since 2026-10-20 · independent blind review received 29 October

**Context:** Rig already supplies public JSON. Bridge still asks only for its version and reports Rig state unavailable; Automation reads declared scheduled jobs. [The blind review](away-bridge-blind-review.report.md) independently reproduced the omission but found no demonstrated breach of accepted behaviour: Machine remains an unadopted idea, and declarations do not establish observed health. The old request to review the gap is complete. The earlier proposal favoured preparing integration; the reviewer instead recommends keeping it parked, at high confidence, because scope and consolidation gates remain unresolved.

**Query:** Should bounded proposal preparation for the remaining Bridge machine-reader gap be taken up?

**Options:**

a) (recommended, confidence medium - review disagrees with proceeding now; the omission is real but its accepted scope is unsettled) Prepare only a bounded proposal using the existing Rig JSON contract, returning declaration coverage versus observed health as a separate choice before any implementation or adoption.

b) Follow the blind review: retain current behaviour and keep integration parked under the existing Machine and consolidation gates.

c) Consider wording and fixture hygiene only, explicitly leaving the reader omission unresolved; wording alone cannot close that omission.

### STATUS-REPAIR - Seek separate adoption for the correctness repair

since 2026-10-29 · from independent away-status-blind-review

**Context:** [The independent status review](away-status-blind-review.report.md) reproduces canonical exclusions being resurrected, ambiguous aliases being displayed by fast views, and historical package/run-home omissions. Ordinary Review also uses the fast path in current server defaults. Valid regular work and selected members already have flat coverage. These are separable correctness defects, outside [KI-OBSERVA-APP-044](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md)'s consolidation boundary. Preparation can establish latency, producer warnings/refusals and cross-repository-home limits; it cannot itself adopt a repair, choose global-home precedence or authorise delivery.

**Query:** Should a separate bounded canonical-reader repair be brought through adoption and an agreed plan?

**Options:**

a) (recommended, confidence high - independent fixtures establish a correctness defect separate from the unresolved restructure) Seek separate adoption and planning for one producer-authoritative status/home result across existing Work, Waiting and Review, preserving the current views; settle latency and producer boundaries before implementation.

b) Keep the demonstrated defects visible but defer adoption pending deployed-version or representative-estate evidence.

c) Reconsider APP-044's boundary explicitly before coupling this repair to consolidation; no such boundary change is approved here.

### SYNC-DIRECTION - Choose the candidate for design preparation

since 2026-10-29 · independent blind query review received

**Context:** The [merged sync paper](design/observatory-sync-report.md) compares A, attended passes under fresh grants; B, a Rig/chezmoi dispatcher child; C, Bridge scheduling/execution; D, Bridge requesting an external runner; and E, a direct per-host Rig scheduled activity invoking a deterministic Tools recipe. The merge preferred preparing E against A; [the blind query review](away-sync-query-review.report.md) independently recommends that same course. A running Bridge supplies no periodic execution mandate. Existing publication, repository, confidentiality and deployment gates apply whichever candidate is chosen. HOST-SYNC responsibility semantics remain with Ways of working, with any seat/failover change separately owned; this choice does not settle them.

**Query:** Which candidate should its owners develop into a reviewable plan?

**Options:**

a) (recommended, confidence high - reviewed, independent source review agrees that direct per-host activity is the simplest candidate to develop) Prepare E against A as the baseline, retaining Observatory as observer and leaving executor selection, authority and rollout for the later reviewed plan.

b) Retain A alone for now, using fresh bounded attended grants; defer scheduled design.

c) Prepare B instead, first showing the shared dispatcher value and resolving its narrower HNR remit.

d) Prepare C instead, explicitly reviewing the Observatory product and authority change.

e) Prepare D instead, first establishing an attended request need and separate request, authorisation and receipt contracts.

### PUBLIC-AUDIENCE - Establish the protected report audience

since 2026-10-29 · from the final publication-audience review request

**Context:** Principal is public according to the territory's current review. This run had explicit local commit authority and an explicit no-push limit; no separate publication boundary was established. The [product working contract](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/AGENTS.md#working-contract) keeps private repository identities, findings and activity local without such a boundary. At receipt commit `8e31eec9`, [away-jobs-evidence](away-jobs-evidence.report.md) contains HNR job identity, source references and operational findings, while [away-jobs-spec](away-jobs-spec.report.md) names the HNR receiving work. The [messages blob](messages.md) retains Personal/HNR work identities already present before that receipt; these are retained context, not all newly introduced by it. These three exact paths are the positively identified protected review subset; the other payloads have not been certified safe for public readership. A fresh authorised fetch now proves receipt 8e31eec9 is already in origin/main history; local-only task authority did not prevent publication by other work. Intended audience and response to that existing history are separate choices. Independent factual review is continuing. Local commits, existing remote reachability and the standing low-risk documentation rule supply no missing audience approval.

**Query:** What audience should govern these reports before any later publication decision?

**Options:**

a) (recommended, confidence high - the explicit local-data and no-push boundaries apply and no publication clearance was found) Withhold further publication of unreviewed material while the independent review establishes an exact audience boundary; make no history change under this handoff.

b) Supply an explicit audience and bounded content approval after that review; authorise any later publication or history remedy separately, without treating this option as a current push instruction.

### PUBLIC-EXPOSURE - Decide the response to observed remote history

since 2026-10-29 · from verified remote-containment steering

**Context:** A fresh authorised fetch establishes that the earlier nine away-run Principal commits, including receipt `8e31eec9` and the report/design commits, are ancestors of origin/main. The identified HNR report/context payload therefore exists in observed remote history; saying this worker did not push does not mean it stayed local. This run's four finalisation commits were not remote ancestors at that check. This proves remote reachability, not when or by whom publication happened, readership, indexing or credential exposure. No such exposure is established. The independent review has the exact findings. No visibility change, deletion, reset, rewrite or sanitisation is authorised.

**Query:** What follow-up should address the already-reachable protected review material?

**Options:**

a) (recommended, confidence high - remote ancestry is verified but audience and exposure consequences still need factual review) Complete the bounded audience/exposure assessment and bring a concrete response plan for Kris's separate decision, preserving all evidence and history meanwhile.

b) After reviewing the exact contents and audience, explicitly decide that no remedial action is needed; record that bounded disposition without implying approval for other private payloads.

c) Request a specific access or history response plan, with its consequences and restore/coordination requirements, for separate approval before any execution.

## Parked

No unanswered choice has been selected. Council/consolidation order, Waiting/Review, Work's destination and Rig declaration versus observed-health scope are separate downstream design questions, gated by their preparation decisions above. HOST-MEANING is receiver-owned at Ways of working, not an additional decision requested here. ACCEPT remains closed in the [sourced receipt](decisions.md#2026-10-29---accept-closed).
