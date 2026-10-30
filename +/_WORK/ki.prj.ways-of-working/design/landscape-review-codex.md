# [Model](<../../../../Streams/Themes/model.md>) › [Ways of working](<../../../../Streams/Projects/ways-of-working.md>) › landscape-review-codex

**🤖 → 👤 Handoff to supervisor · Run report at 02:27 GMT · last mark 01:39 GMT**

---

## Done

- Independently reviewed the [landscape design](landscape.md), [brief](../briefs/landscape.md) and [explainer](landscape-explainer.md) against local sources on 30 October 2026; reviewed baseline `543c8e79`.
- Checked all 30 numbered claims and recommended options for the five requested decisions; no other review, run report or `queries.md` was read.
- Checked installed KI and Orca skills, version-matched Orca guides, command help, the Techné policy and the cited decision entries; material corrections are below.
- External vendor assertions remain unverified: this review's authority excludes network research beyond authorised Git synchronisation.
- This artefact is a review for the coordinator to merge, with no implementation or acceptance authority; delivery and gate evidence are recorded in the runtime handoff report.

## In Progress

Nothing is running. The coordinator owns merging the independent reviews and returning the revised design to Kris.

Outstanding - no action requested now: retain vendor claims as provisional until their primary sources are attached; verify Orca setup and actual wake delivery in a bounded trial before using them as operational guarantees.

## Findings

### LANDSCAPE-REVIEW - A sound separation with several overstated conclusions

**Goal:** Independently test the landscape's numbered claims and recommend ORCA-REACH, AGENT-HOME, WAKE, WORKTREE-OPTOUT and naming, as requested on 30 October 2026.

**Scope:** The three commissioned documents, installed skills and their relevant standards, local command help and version-matched Orca guides, the Techné focus policy, relevant owner decisions, and the local worktree implementation. No other reviewer output, run report, `queries.md`, remote service or live dispatch was inspected.

**As of:** 30 October 2026, 02:27 GMT, on sol; Orca 1.4.244 and `ki` 0.14.1. CLI presence establishes advertised capability, not successful operation on terra or vega.

My own view: keep repository-owned authority, portable work records and acceptance independent of dispatch. A small interchangeable launcher contract is useful. The landscape becomes less reliable where it turns that preference into claims of vendor incapability, exclusive host permission, or a prohibition that a later owner decision has already qualified. Twelve useful headings are a starting vocabulary; reliable adapters also need event identity, acknowledgement, recovery and destination semantics.

Evidence keys used below:

- **C:** Installed `ki-coordination`, especially [Headless passes](<../../../../.agents/skills/ki-coordination/references/standards-coordination.md#headless-passes>), report forms and launcher references.
- **D:** Installed `ki-delegation`, especially [Coordination](<../../../../.agents/skills/ki-delegation/references/standards-background-runs.md#coordination>), authority tiers, run events and monitoring.
- **G:** Installed `ki-git` [Git standard](<../../../../.agents/skills/ki-git/references/standards-git.md>), including local integration and worktree-run self-integration.
- **P:** [Techne Programme Focus](<../../../../Admin/Governance/Policies/Techne Programme Focus.md>), particularly Focus and Sessions; [work decisions](../decisions.md), especially KI-AGENTS-NAME, WAKE-SUBSTRATE on 26 October and ROLES-ORCHESTRATOR/ROLES-EITHER on 29 October.
- **K:** Local `ki agent --help`, `launch --help`, `wait --help`, `home --help`, `decide --help`, `reconcile --help` and `ki work --help`; [worktree implementation](</Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/worktrees.ts:42>).
- **O:** Installed `orca-cli` and `orchestration` stubs; guides returned by `orca skills get orca-cli --json` and `orca skills get orchestration --json`; local `orca --help`, `serve --help`, `orchestration worker-start --help` and `orchestration check --help`.
- **B:** Installed `ki-batch` [contract](</Users/krisbrown/.agents/skills/ki-batch/SKILL.md>) and [batch procedure](</Users/krisbrown/.agents/skills/ki-batch/references/standards-batch.md>).
- **T:** Installed [portable tokenomics](<../../../../.agents/skills/ki-tokenomics/SKILL.md>), [Codex adapter](<../../../../.agents/skills/ki-tokenomics-chatgpt/SKILL.md>) and the harness's [Claude adapter](</Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/environment/ki-tokenomics-claude/SKILL.md>).
- **W:** Installed [work-package contract](<../../../../.agents/skills/ki-work-package/SKILL.md>), [roadmap contract](<../../../../.agents/skills/ki-work-roadmap/SKILL.md>), [Paperclip adapter](<../../../../.agents/skills/ki-agent-coordination-paperclip/SKILL.md>) and [Orca evaluation outcome](<../../../../Streams/Projects/orca-evaluation.md>).
- **M:** Installed [binding contract](<../../../../.agents/skills/ki-binding/SKILL.md>) and [Codex housekeeping contract](<../../../../.agents/skills/ki-housekeeping-chatgpt/SKILL.md>).

Numbered claims, with one verdict, reason and checked evidence for each:

1. **Agree** - Layers are useful capability roles; thin product-specific bindings implement the portable method. Evidence: M, W and O.
2. **Agree** - A surface category accommodates editor, terminal and vault reader without giving any of them work authority. Evidence: brief, explainer and O.
3. **Add** - Distinguish committed local state from published remote state; Git durability is sound, but a register should be a supporting plane rather than the last stage of an execution chain. Evidence: G and W.
4. **Differ** - The complete KI authority and acceptance contract is distinctive; absence of all durable cross-host work, recorded approvals or separate review in every examined product is not established, and a server database can serve several hosts. Evidence: W's Paperclip boundary and O's remote Run semantics; vendor evidence is incomplete.
5. **Agree** - Prefer the selected launcher's live views and placement machinery while retaining enough status and recovery in the floor launcher to honour its contract. Evidence: K, O and C's monitoring obligations.
6. **Add** - `decide` and `reconcile` plainly mutate method records, but `prompts` prints openers and `home` also binds a runtime run to its work home; those four are not uniformly package writers. Evidence: K's individual subcommand help.
7. **Add** - The owner assigns a state-machine role to the thread agent; avoiding an overloaded skill name is sensible, but that decision does not reserve the word exclusively or forbid dispatch terminology. Evidence: P's ROLES-ORCHESTRATOR and ROLES-EITHER.
8. **Agree** - Keep the established coordination name while separating launcher mechanics through the contract. Evidence: C's ownership and P's role decisions.
9. **Agree** - Retaining `ki-delegation` and naming thin Orca/Paperclip adapters after it avoids a gratuitous portable-contract rename; the floor needs documented mechanics, not a duplicate skill. Evidence: D, O and W's Paperclip adapter.
10. **Add** - Keeping `ki agent` is a reasonable low-churn recommendation; KI-AGENTS-NAME preserves the owner's naming choice but does not itself specify a future `ki work` command migration. Evidence: P's 17 October wording recorded on 25 October and K.
11. **Add** - The twelve verbs cover the main cycle, but require attempt identity, delivery acknowledgement, outcome-unknown recovery and report availability rules before they are an executable contract. Evidence: O's FIFO Delivery/acknowledgement and Dispatch rules; K's `recover` and D's run events.
12. **Differ** - Local help shows no exposed KI-policy integration command in Orca or `ki agent`; it cannot establish Cursor as the sole native exception, and native Git merging is different from KI's verified serial integration policy. Evidence: K, O and G.
13. **Add** - Support isolated writing runs, with a read-only opt-out and no change-size exemption; reconcile current short-package and roadmap-ledger exceptions explicitly before treating this proposed baseline as installed policy. Evidence: brief, D's worktree trial, G and W's Paperclip roadmap exception.
14. **Agree** - Keep coordinating packages in their primary checkout so routing and owner-visible files stay current, while dispatching substantive edits under their own isolation rules. Evidence: G, C and [checkout isolation](checkout-isolation.md).
15. **Differ** - Registry recognition and integration are not the only remaining proofs: `--worktree` copies available dependencies and managed skill symlinks but starts from the supplied checkout's `HEAD`, so committed-main selection, missing prerequisites and correct primary package anchoring also need checks. Evidence: K's implementation and D's worktree-audit limitation.
16. **Add** - Require package/job identity and an explicit target chosen by the coordinator, while resolving each work's declared home rather than assuming every regular/ad hoc package resides in the Capital. Evidence: K's repository-oriented launch and W's package-home rules.
17. **Add** - Headless serve, remote worker placement and Codex are advertised locally; the beta label is not established by the checked help/compact guides, and no remote run was tested. Evidence: O's serve and worker-start help.
18. **Differ** - Techné-owned execution-fabric work and unattended host operation need the relevant owner decision, but the policy neither names an exclusive launcher nor bans every attended Orca worker on vega; durable-wake design was subsequently authorised under WAKE-SUBSTRATE. Evidence: P's Focus/Sessions, its 26 October decision and C's Headless passes.
19. **Add** - Keep tools-ki's working floor; restrict duplicate feature growth as an owner-approved direction, with room for contract correctness, isolation and recovery work rather than a blanket freeze. Evidence: K, D and the brief's unresolved AGENT-HOME choice.
20. **Differ** - One bounded armed wait is useful, but process completion alone does not prove coordinator wake/receipt, and durable wake is no longer wholly deferred. Evidence: O's best-effort attention and acknowledgement rules, K's unbounded-by-default wait interface, C's Headless passes and P's later WAKE-SUBSTRATE decision.
21. **Add** - Broad discovery triggers overlap and should be scoped, but the version-matched Orca guide confines its non-Orca prohibition to requested Orca provenance; prefer the full guide over the stub's broader wording. Evidence: installed stubs, O's role classification and G's conditional worktree choices.
22. **Agree** - Slim product-specific references and progressively reveal the coordination standard without losing authority/reporting requirements; its checked size is 216,988 bytes. Evidence: C and its installed file size; exact launcher-line counts need a documented counting scope.
23. **Add** - A thinner Paperclip relationship adapter is sensible, but preserve company jurisdiction, repository authority, remote-delivery and roadmap-ledger safeguards, and verify which declarations depend on it before unloading it. Evidence: W's installed adapter and its `ki-git` dependency.
24. **Differ** - Batch authorisation and a worker's delegation footer govern different things: a frozen repository-local item set, payload, window and completion target cannot be reduced to a generic footer without losing review and closure evidence. Evidence: B and D's authority-tier separation.
25. **Add** - The adapters exclude user-home/effective-session inspection, but portable tokenomics already names user/runtime attribution and output configuration; extend consent-bounded adapter evidence rather than broadening the portable policy as though it omitted those surfaces. Evidence: T and the measured 26,337-byte coordinator output-style file.
26. **Add** - Keep Git policy in `ki-git`, while delegation footers, owner grants and package lifecycle retain their distinct authority requirements and cite it; source ownership does not mean deleting necessary rendered instructions. Evidence: G, D's commit-trailer rule and C's generated surfaces.
27. **Agree** - Retain portable content and inventory with thin runtime-specific configuration/activation bindings; required hooks still need platform-specific verification. Evidence: M and G's hook ownership boundary.
28. **Differ** - The Techné host policy restricts unattended/scheduled agents, but KI already defines bounded unattended windows and authorised headless passes; distinguish method authority from permission to install or run on a particular host. Evidence: P and C's Unattended windows/Headless passes.
29. **Agree** - Treat runtime memory as a scoped aid and route reviewed durable learning to the repository; enabling memory or importing transcripts remains separately governed. Evidence: M and W's Paperclip memory guidance.
30. **Add** - Orca evaluation is the right owner, with a bounded first pilot after applicable prerequisites; an away grant matters only for unattended execution, and subjective naming or later features need not block an attended evaluation. Evidence: W's Project outcome, brief and P.

Additional corrections to carry into the merged design and explainer:

- **Evidence traceability:** The landscape refers to vendor URLs kept in research notes but does not include those URLs; attach primary references and dates beside volatile capability, licence, maturity and exclusivity claims before making them durable knowledge.
- **Scope of the explainer:** Project packages live in the Capital, but not every kind of coordinating package must; make the island/home distinction explicit, and replace the universal claim that tools cannot retain cross-host work with KI's replaceable repository-owned contract.
- **Wait and receive:** A blocking wait needs a runtime-supported background completion mechanism, bounded lifetime, resume/acknowledgement rules and a demonstrated wake. `ki agent wait --next` has no advertised timeout option; an adapter must supply the bound and avoid losing an event already marked seen.
- **Remote report paths:** A report path on a worker host is not automatically readable on the coordinator host; the adapter must prove transfer/availability and distinguish local integration from publishing and destination integration.
- **Isolation limits:** Worktrees isolate tracked files and indexes; they do not isolate shared source stores, credentials, providers or other mutable external resources. Keep those scope and ownership checks in the contract.
- **Read-only boundary:** The proposed invariant that workers never write the package needs a precise core-files boundary and explicit exceptions for authorised design artefacts such as this review; the work-folder contract already recognises those artefacts.
- **Context measurements:** Label description characters, file bytes, discovery entries and effective loaded tokens separately; on-disk inventory does not prove what a session loaded. The 26 KB style is a checked file size, not a verified largest contributor to effective standing context.
- **Roadmap skill overlap:** `ki-work-roadmap` explicitly owns the record model used by KB Streams, so its presence is not by itself redundant with the Streams container skill.

Queries raised: ORCA-REACH, AGENT-HOME, WAKE, WORKTREE-OPTOUT and ORCH-NAME below. These are recommendations for the merged design, not implementation requests or adopted decisions.

## Queries

### ORCA-REACH - Scope the first Orca deployment

**Context:** Local help advertises headless execution, remote workers and Codex. That proves capability discovery, not remote-host operation, and the Techné policy restricts unattended agents without naming a sole launcher.

**Query:** Where should the initial Orca evaluation run?

**Options:**

a) (recommended, confidence high - local capability evidence supports a reversible attended trial) Choose landscape option a's attended-Mac, package-opt-in trial and retain `ki agent` as the available floor; qualify the vega restriction as a deployment choice, with a separate remote-delivery decision and proof before expansion.

b) Choose option b and pair vega now under explicitly agreed attended-session and remote-delivery bounds; this review supplies no operational proof for that deployment.

### AGENT-HOME - Keep the floor and separate its responsibilities

**Context:** `ki agent` is the installed reference launcher. The Techné focus keeps execution-fabric work as an idea; method-log operations and runtime-to-work-home binding have different responsibilities.

**Query:** Where should dispatch remain while the portable contract is piloted?

**Options:**

a) (recommended, confidence high - preserves the working launcher within the current programme bounds) Choose option a: retain it in tools-ki, prioritise contract correctness over duplicate platform features, and design the method-command split individually before moving commands; retain Techné dispatch as an idea.

b) Choose option b only after an Enactment decision takes up Techné dispatch and sets its delivery bounds; do not move it now on the design's authority.

c) Choose option c and retire the floor only after another launcher meets the contract on every required host; that evidence is absent here.

### WAKE - Preserve the approved durable-wake direction

**Context:** The 26 October WAKE-SUBSTRATE decision lifted the launchd deferral in order, and the installed standard already defines Headless passes. Installation and host permission are separate; a live wait also needs a tested delivery/receipt path.

**Query:** Which wake recommendation should the merged design carry?

**Options:**

a) (recommended, confidence high - follows the later decision and the installed headless-pass contract) Amend option a: standardise one bounded armed native wait for live sessions, prove wake and acknowledgement per runtime, and retain the already-authorised headless-pass rollout sequence with explicit per-work/host permission; keep doorbells and extra liveness fields deferred.

b) Choose option b and introduce Orca automation as the durable wake only after an explicit new choice reconciles it with the existing headless-pass direction and the Techné host bounds.

### WORKTREE-OPTOUT - Exempt only genuinely read-only runs

**Context:** The brief proposes worktrees for writing runs. Installed guidance still has short-package and serial-roadmap exceptions, and the available worktree launcher starts at the supplied checkout's `HEAD` with available dependencies and skill links.

**Query:** Which runs may opt out of the proposed isolation baseline?

**Options:**

a) (recommended, confidence high - the boundary depends on mutation and shared Git state rather than edit size) Allow only runs writing nothing inside a repository to opt out, with reports outside repositories; retain coordinators on primary `main`, and reconcile allocation exceptions and verify baseline/setup/package-home/integration checks before rollout.

b) Also exempt trivial writing runs under an explicit serial write window; this keeps a shared-index exception and needs a separately defined boundary and justification.

### ORCH-NAME - Keep the established portable names

**Context:** The owner uses orchestrator for the package state-machine role, while the installed delegation skill already claims the portable contract. Naming the adapter family does not require moving commands or rewriting standards first.

**Query:** Which names should the merged design recommend?

**Options:**

a) (recommended, confidence medium - preserves recognisable boundaries with minimal churn, while the final vocabulary is the owner's preference) Keep `ki-coordination`, `ki-delegation` and `ki agent`; use `ki-delegation-orca` and `ki-delegation-paperclip` for proposed adapters, with no separate floor-launcher skill.

b) Keep `ki-coordination` and rename the portable dispatch family to `ki-orchestration` with matching adapters, defining clearly how that capability differs from the state-machine orchestrator role.

### 🤖 → 👤 Handoff to supervisor · since 02:27 GMT

🤖 0 running · 👤 5 recommendations with supervisor · ⛔ 0 blocked

- [with you] independent landscape review and five recommendations · supervisor · since 02:27 GMT
- [committed] review artefact; delivery commit recorded in the runtime handoff

🧵 ki.prj.ways-of-working
