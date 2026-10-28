# [Foundations](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/foundations.md) › [Baseline rollout](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/baseline-rollout.md) › sizekind-2

**🤖 → 👤 Handoff to supervisor · Run report at 00:19 BST · last mark 23:56 BST**

---

## Done

Read-only run: no commits, no writes to any repository, `ki repo conform` never run. Ten repositories hold a `.ki.toml`. Six of them have records with gaps: 61 open records have no `size`, and 40 adopted open records have no `kind`. This matches the wave 1 sweep for every repository. Four repositories have no records at all: apps-dafacts.org, va-agentic-harness, tmx-agentic-harness and apps-yorkphotosoc.org.

- [er-agentic-harness](/Users/krisbrown/workspaces/equal-remedy/er-agentic-harness): 22 proposals (22 size, 22 kind), table below · no commit.
- [er-principal](/Users/krisbrown/workspaces/equal-remedy/er-principal): 8 proposals (8 size, 5 kind), table below · no commit.
- [va-principal](/Users/krisbrown/workspaces/valle-armonia/va-principal): 6 proposals (6 size, 1 kind), table below · no commit.
- [apps-vallearmonia.com](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com): 15 proposals (15 size, 10 kind), read as it stands after `va-plan`'s commit `f9733f2` (VA-WEBSITE-SITE-005 already carries a size), table below · no commit.
- [apps-markhowarth.com](/Users/krisbrown/workspaces/valle-armonia/apps-markhowarth.com): 4 proposals (4 size), table below · no commit.
- [tmx-principal](/Users/krisbrown/workspaces/techmedix/tmx-principal): 6 proposals (6 size, 2 kind), table below · no commit.

Size uses the standard's shapes: `s` is one run, one repository, one commit; `m` is one run with several commits and a plan; `l` is several chained runs or repositories; `xl` must be split. Kind is set only on adopted records (status past `triage`); a dash means none is needed.

### er-agentic-harness

Every candidate builds one self-contained `er-` skill in this repository, with its references, synthetic fixtures, tests and evaluations: one run with several commits, so `m`. All are Future drafts with promotion conditions still open, so every size is provisional and is revisited at planning.

| Record | State | size | kind | Confidence | Reason or uncertainty |
| --- | --- | --- | --- | --- | --- |
| [ER-HARNESS-001](/Users/krisbrown/workspaces/equal-remedy/er-agentic-harness/docs/roadmap/ER-HARNESS-001-review-capability-portfolio.md) | draft · next | m | decide | high | Closes on approving the portfolio and choosing the first wave; one independent review and reconciliation edits across 21 records |
| [ER-HARNESS-002](/Users/krisbrown/workspaces/equal-remedy/er-agentic-harness/docs/roadmap/ER-HARNESS-002-harden-capability-extraction.md) | draft · future | m | deliver | high | Moves and hardens an existing skill, adding a worksheet, a leakage gate and red-team fixtures |
| [ER-HARNESS-003](/Users/krisbrown/workspaces/equal-remedy/er-agentic-harness/docs/roadmap/ER-HARNESS-003-ingest-legal-sources.md) | draft · future | m | deliver | high | New skill with manifest schema, hashing and synthetic end-to-end ingestion |
| [ER-HARNESS-004](/Users/krisbrown/workspaces/equal-remedy/er-agentic-harness/docs/roadmap/ER-HARNESS-004-analyse-evidence.md) | draft · future | m | deliver | high | New skill; proposition schema and multi-format fixtures |
| [ER-HARNESS-005](/Users/krisbrown/workspaces/equal-remedy/er-agentic-harness/docs/roadmap/ER-HARNESS-005-curate-legal-authorities.md) | draft · future | m | deliver | medium | Five modes plus scheduled refresh; it may grow to `l` if topic packs are built in the same record |
| [ER-HARNESS-006](/Users/krisbrown/workspaces/equal-remedy/er-agentic-harness/docs/roadmap/ER-HARNESS-006-verify-legal-citations.md) | draft · future | m | deliver | high | New skill, bounded verification procedure |
| [ER-HARNESS-007](/Users/krisbrown/workspaces/equal-remedy/er-agentic-harness/docs/roadmap/ER-HARNESS-007-review-case-progress.md) | draft · future | m | deliver | high | New skill; portable case-stage schema |
| [ER-HARNESS-008](/Users/krisbrown/workspaces/equal-remedy/er-agentic-harness/docs/roadmap/ER-HARNESS-008-control-orders-directions.md) | draft · future | m | deliver | high | New skill; direction schema and date warnings |
| [ER-HARNESS-009](/Users/krisbrown/workspaces/equal-remedy/er-agentic-harness/docs/roadmap/ER-HARNESS-009-manage-legal-disclosure.md) | draft · future | m | deliver | high | New skill; disclosure-item schema and stop rules |
| [ER-HARNESS-010](/Users/krisbrown/workspaces/equal-remedy/er-agentic-harness/docs/roadmap/ER-HARNESS-010-manage-filing-service.md) | draft · future | m | deliver | high | New skill; packet manifest and proof schema |
| [ER-HARNESS-011](/Users/krisbrown/workspaces/equal-remedy/er-agentic-harness/docs/roadmap/ER-HARNESS-011-draft-legal-correspondence.md) | draft · future | m | deliver | high | New skill; the smallest of the set, but still references, fixtures and evaluations |
| [ER-HARNESS-012](/Users/krisbrown/workspaces/equal-remedy/er-agentic-harness/docs/roadmap/ER-HARNESS-012-draft-court-documents.md) | draft · future | m | deliver | high | Promotion conditions already bound it to two document types |
| [ER-HARNESS-013](/Users/krisbrown/workspaces/equal-remedy/er-agentic-harness/docs/roadmap/ER-HARNESS-013-stress-test-legal-work.md) | draft · future | m | deliver | high | New skill; severity and disposition vocabulary |
| [ER-HARNESS-014](/Users/krisbrown/workspaces/equal-remedy/er-agentic-harness/docs/roadmap/ER-HARNESS-014-produce-court-bundles.md) | draft · future | l | deliver | medium | Needs a PDF toolchain choice plus byte, page, index, bookmark and visual verification; likely chained runs |
| [ER-HARNESS-015](/Users/krisbrown/workspaces/equal-remedy/er-agentic-harness/docs/roadmap/ER-HARNESS-015-prepare-court-hearings.md) | draft · future | m | deliver | medium | Generic stage contract that specialist modules extend; it grows if modules are built with it |
| [ER-HARNESS-016](/Users/krisbrown/workspaces/equal-remedy/er-agentic-harness/docs/roadmap/ER-HARNESS-016-prepare-cross-examination.md) | draft · future | m | deliver | high | New skill; question-plan schema and fairness stops |
| [ER-HARNESS-017](/Users/krisbrown/workspaces/equal-remedy/er-agentic-harness/docs/roadmap/ER-HARNESS-017-analyse-legal-appeals.md) | draft · future | m | deliver | high | New skill; one jurisdiction |
| [ER-HARNESS-018](/Users/krisbrown/workspaces/equal-remedy/er-agentic-harness/docs/roadmap/ER-HARNESS-018-manage-judgments-transcripts.md) | draft · future | m | deliver | high | New skill; record-status vocabulary and correction workflow |
| [ER-HARNESS-019](/Users/krisbrown/workspaces/equal-remedy/er-agentic-harness/docs/roadmap/ER-HARNESS-019-run-private-children-cases.md) | draft · future | l | deliver | medium | Seven case stages; promotion conditions already say "choose bounded first stage", so it may split at planning |
| [ER-HARNESS-020](/Users/krisbrown/workspaces/equal-remedy/er-agentic-harness/docs/roadmap/ER-HARNESS-020-prepare-fact-finding-hearings.md) | draft · future | m | deliver | medium | One hearing type, but the PD12J validation and allegation fixtures are substantial |
| [ER-HARNESS-021](/Users/krisbrown/workspaces/equal-remedy/er-agentic-harness/docs/roadmap/ER-HARNESS-021-run-financial-remedies.md) | draft · future | l | deliver | medium | Nine stage modules, around 14 reference packs and calculation helpers; promotion conditions choose a first module, so it may split |
| [ER-HARNESS-022](/Users/krisbrown/workspaces/equal-remedy/er-agentic-harness/docs/roadmap/ER-HARNESS-022-handle-interim-finance.md) | draft · future | m | deliver | high | Bounded to two application types at first |

### er-principal

| Record | State | size | kind | Confidence | Reason or uncertainty |
| --- | --- | --- | --- | --- | --- |
| [ER-PRINCIPAL-004](/Users/krisbrown/workspaces/equal-remedy/er-principal/Streams/Roadmap/ER-PRINCIPAL-004-legal-and-policy-landscape.md) | draft · future | l | investigate | low | A broad research map whose audience and strands are not yet chosen; it may be `xl` and split by strand |
| [ER-PRINCIPAL-005](/Users/krisbrown/workspaces/equal-remedy/er-principal/Streams/Roadmap/ER-PRINCIPAL-005-harm-panel-and-parental-involvement.md) | draft · future | m | investigate | medium | Closes on verified findings about one report and its claims |
| [ER-PRINCIPAL-006](/Users/krisbrown/workspaces/equal-remedy/er-principal/Streams/Roadmap/ER-PRINCIPAL-006-parliamentary-engagement.md) | draft · future | m | deliver | medium | One briefing plus reusable correspondence; sending is out of scope |
| [ER-PRINCIPAL-007](/Users/krisbrown/workspaces/equal-remedy/er-principal/Streams/Roadmap/ER-PRINCIPAL-007-media-briefing.md) | draft · future | m | deliver | medium | One master briefing with red-team and anonymisation review |
| [ER-PRINCIPAL-008](/Users/krisbrown/workspaces/equal-remedy/er-principal/Streams/Roadmap/ER-PRINCIPAL-008-documentary-and-journalist-outreach.md) | draft · future | s | investigate | medium | Closes on an assessment of contacts against criteria; the evidence pack comes from ER-PRINCIPAL-007 |
| [ER-PRINCIPAL-011](/Users/krisbrown/workspaces/equal-remedy/er-principal/Streams/Roadmap/ER-PRINCIPAL-011-complete-source-mirrors.md) | triage | s | - | high | The store holds 6 files against 7 source notes; one template update plus the missing extracts |
| [ER-PRINCIPAL-013](/Users/krisbrown/workspaces/equal-remedy/er-principal/Streams/Roadmap/ER-PRINCIPAL-013-review-repository-naming.md) | triage | s | - | high | A proposal only, for three members |
| [ER-PRINCIPAL-014](/Users/krisbrown/workspaces/equal-remedy/er-principal/Streams/Roadmap/ER-PRINCIPAL-014-territory-alignment.md) | triage | l | (audit, already set) | medium | Registry, classification and governance repair across the Capital, the harness and the website |

### va-principal

| Record | State | size | kind | Confidence | Reason or uncertainty |
| --- | --- | --- | --- | --- | --- |
| [VA-PRINCIPAL-GOV-002](/Users/krisbrown/workspaces/valle-armonia/va-principal/Streams/Roadmap/VA-PRINCIPAL-GOV-002-establish-community-social-accounts.md) | triage | m | - | medium | Platform, custodian, recovery and permission decisions with Kit across up to three platforms |
| [VA-PRINCIPAL-GOV-003](/Users/krisbrown/workspaces/valle-armonia/va-principal/Streams/Roadmap/VA-PRINCIPAL-GOV-003-company-operations.md) | in-progress · now | s | deliver | medium | An approved two-file canonical patch; the open steps are review and integration only. Uncertainty: its remaining steps run through a Paperclip review flow that Paperclip's pause, until Wave F, may have stalled |
| [VA-PRINCIPAL-GOV-005](/Users/krisbrown/workspaces/valle-armonia/va-principal/Streams/Roadmap/VA-PRINCIPAL-GOV-005-audit-the-social-media-footprint.md) | triage | s | - | high | One inventory note of about nine presences |
| [VA-PRINCIPAL-GOV-006](/Users/krisbrown/workspaces/valle-armonia/va-principal/Streams/Roadmap/VA-PRINCIPAL-GOV-006-review-repository-naming.md) | triage | s | - | high | A proposal only |
| [VA-PRINCIPAL-KNW-001](/Users/krisbrown/workspaces/valle-armonia/va-principal/Streams/Roadmap/VA-PRINCIPAL-KNW-001-complete-source-mirrors.md) | triage | m | - | medium | The store holds 25 files and no mirrors exist yet; this is an inventory plus a mirror per kept document |
| [VA-PRINCIPAL-KNW-002](/Users/krisbrown/workspaces/valle-armonia/va-principal/Streams/Roadmap/VA-PRINCIPAL-KNW-002-bring-community-identity-into-principal.md) | triage | m | - | medium | Choose a canonical home and draft an Enactment proposal; the open questions need Kit |

### apps-vallearmonia.com

| Record | State | size | kind | Confidence | Reason or uncertainty |
| --- | --- | --- | --- | --- | --- |
| [VA-WEBSITE-CONT-001](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-CONT-001-refresh-volunteer-and-guest-content.md) | draft · hold | s | deliver | medium | Publishes two pages from supplied copy; it grows if Tamsin's drafts need restructuring |
| [VA-WEBSITE-CONT-002](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-CONT-002-write-education-centre-content.md) | draft · hold | s | deliver | medium | Publishes one page from supplied copy |
| [VA-WEBSITE-CONT-004](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-CONT-004-add-a-visit-us-page.md) | draft · hold | s | deliver | high | One page plus nav and Belong footer links |
| [VA-WEBSITE-CONT-005](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-CONT-005-resolve-image-review-flags.md) | draft · now | m | deliver | high | Six steps over four image groups, with several commits and Kit's choices |
| [VA-WEBSITE-GOV-004](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-GOV-004-decide-sources-directory.md) | triage | s | - | medium | Inventory and a per-file decision. Finding: no `sources-vallearmonia-website` folder exists at the OneDrive root now, so the record may close on a finding |
| [VA-WEBSITE-MEM-001](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-MEM-001-add-member-protected-area.md) | draft · future | m | deliver | low | Cloudflare Access policy plus protected paths; the size depends on a community decision not yet taken |
| [VA-WEBSITE-OPS-003](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-OPS-003-rotate-security-txt-expiry-2027.md) | draft · hold | s | deliver | high | One dated field change |
| [VA-WEBSITE-OPS-004](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-OPS-004-adopt-happy-dom-21.md) | draft · next | s | (deliver, already set) | high | The site-logo tests plus one version bump |
| [VA-WEBSITE-SANC-008](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-SANC-008-package-the-sanctuary.md) | draft · next | l, or m after a split | deliver | medium | The record's own Size topic calls stages 2 to 4 three chained runs. If SANC008-SPLIT goes ahead, this record is `m` and the new stage 4 record is about `m` to `l` |
| [VA-WEBSITE-SANC-009](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-SANC-009-close-the-editorial-audit.md) | draft · now | s | audit | medium | Checks shipped state against the audit document and closes it. Uncertainty: the document is private to Kit, so the work happens outside the repository and could arguably be `deliver` |
| [VA-WEBSITE-SITE-001](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-SITE-001-extract-pachamama-editorial-approach.md) | draft · future | m | investigate | medium | Closes on a documented approach; no package or repository has been chosen yet |
| [VA-WEBSITE-SITE-002](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-SITE-002-refresh-the-logo-mark.md) | awaiting-review · now | m | (deliver, already set) | high | Delivered in seven steps across six commits |
| [VA-WEBSITE-SITE-003](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-SITE-003-consolidate-the-design-system.md) | awaiting-review · now | m | (deliver, already set) | medium | Eight broad steps delivered, and only two commits name the record; it could fairly be `l` |
| [VA-WEBSITE-SITE-004](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-SITE-004-choose-the-home-page-layout.md) | draft · next | s | (decide, already set) | high | Two options, screenshots, and Kit's recorded choice |
| [VA-WEBSITE-WEB-001](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-WEB-001-track-public-read-only-webmcp.md) | draft · hold | m | deliver | low | Waits on WebMCP becoming stable; the interface scope cannot be sized until then |

### apps-markhowarth.com

All four are triage records, so none needs a kind. Each closes on a decision Mark records (`decide` at adoption).

| Record | State | size | kind | Confidence | Reason or uncertainty |
| --- | --- | --- | --- | --- | --- |
| [VA-MARK-001](/Users/krisbrown/workspaces/valle-armonia/apps-markhowarth.com/docs/roadmap/VA-MARK-001-agree-site-identity.md) | triage | s | - | high | Records Mark's agreement only |
| [VA-MARK-002](/Users/krisbrown/workspaces/valle-armonia/apps-markhowarth.com/docs/roadmap/VA-MARK-002-decide-home-page.md) | triage | s | - | high | Decides the home page message and route only |
| [VA-MARK-003](/Users/krisbrown/workspaces/valle-armonia/apps-markhowarth.com/docs/roadmap/VA-MARK-003-review-story-navigation.md) | triage | s | - | medium | A review with Mark; any navigation changes it finds could add a commit |
| [VA-MARK-004](/Users/krisbrown/workspaces/valle-armonia/apps-markhowarth.com/docs/roadmap/VA-MARK-004-agree-launch-arrangements.md) | triage | s | - | high | Records the agreement only; launch is separate |

### tmx-principal

| Record | State | size | kind | Confidence | Reason or uncertainty |
| --- | --- | --- | --- | --- | --- |
| [TMX-PRINCIPAL-CO-001](/Users/krisbrown/workspaces/techmedix/tmx-principal/Streams/Roadmap/TMX-PRINCIPAL-CO-001-commercial-spine.md) | draft · next | l | deliver | medium | 17 open steps across the roster, the chronology and the Sage Audit Trail analysis; it may need splitting before Ready |
| [TMX-PRINCIPAL-CO-002](/Users/krisbrown/workspaces/techmedix/tmx-principal/Streams/Roadmap/TMX-PRINCIPAL-CO-002-finance-evidence-register.md) | in-progress · now | l | deliver | medium | Seven open steps across eight financial years and three workbook outputs |
| [TMX-PRINCIPAL-CO-006](/Users/krisbrown/workspaces/techmedix/tmx-principal/Streams/Roadmap/TMX-PRINCIPAL-CO-006-resolve-ico-data-protection-fee.md) | triage | s | - | high | Reconcile two references and decide; payment is out of scope. See ICO-DATE |
| [TMX-PRINCIPAL-KB-003](/Users/krisbrown/workspaces/techmedix/tmx-principal/Streams/Roadmap/TMX-PRINCIPAL-KB-003-complete-source-mirrors.md) | triage | l | - | low | The store holds 1,374 files. TMX-PRINCIPAL-CO-001 says every filed original already has a companion note, so the real gap may be shape conformance only, which is much smaller. It needs an inventory before the size is trusted |
| [TMX-PRINCIPAL-KB-006](/Users/krisbrown/workspaces/techmedix/tmx-principal/Streams/Roadmap/TMX-PRINCIPAL-KB-006-review-repository-naming.md) | triage | s | - | high | A proposal only |
| [TMX-PRINCIPAL-KB-007](/Users/krisbrown/workspaces/techmedix/tmx-principal/Streams/Roadmap/TMX-PRINCIPAL-KB-007-territory-work-governance-alignment.md) | triage | m | - | medium | A proposal map and conformance route for one Capital, the same pattern as ER-PRINCIPAL-014 but over fewer repositories |

## In Progress

Nothing is running.

Outstanding - no action requested now:

- The coordinator's blind-review rule for medium- and low-confidence queries has not been applied: this run had no subagents.
- [VA-WEBSITE-GOV-004](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-GOV-004-decide-sources-directory.md): the directory it names was not found at the OneDrive root. Valle Armonia's website can confirm this at planning.
- [VA-WEBSITE-SANC-008](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-SANC-008-package-the-sanctuary.md)'s size follows the open SANC008-SPLIT answer, which is already in `queries.md`.

## Queries

### SIZEKIND-CONFIRM - Confirm the size and kind tables for the three territories

**Context:** The tables above propose 61 sizes and 40 kinds across six repositories. Each row carries its own confidence. 57 rows are high or medium and rest on the record text and the standard's shapes. The 4 low rows (ER-PRINCIPAL-004, VA-WEBSITE-MEM-001, VA-WEBSITE-WEB-001 and TMX-PRINCIPAL-KB-003) are flagged as needing investigation. The standard says a run proposes and you confirm, one repository at a time, before a write pass. Each write pass stages one repository's records by explicit path and follows that repository's AGENTS.md.

**Query:** Which proposals should the write passes apply?

**Options:**

a) (recommended, confidence medium - the high and medium rows follow the record text closely, and the low rows are honest guesses the standard says to investigate) Apply every high and medium row in all six repositories, one write run per repository, and leave the low rows without `size` until each record's next planning pass.

b) Apply every row, low ones included, and revisit sizes before Ready as the standard already requires.

c) Confirm repository by repository, starting with the largest, er-agentic-harness.

### ICO-DATE - TechMedix's ICO registration may already have lapsed

**Context:** [TMX-PRINCIPAL-CO-006](/Users/krisbrown/workspaces/techmedix/tmx-principal/Streams/Roadmap/TMX-PRINCIPAL-CO-006-resolve-ico-data-protection-fee.md) is unadopted triage. It records renewal coverage through 16 October 2026, an unpaid reminder dated 16 September, and a goal of avoiding "a registration lapse or a duplicate payment". Today is 20 October, four days after that coverage date. This run cannot see whether anything has been paid. Adoption and priority belong to TechMedix's Capital, not to this rollout.

**Query:** Should the ICO question be raised with TechMedix's Capital now, outside the size and kind backfill?

**Options:**

a) (recommended, confidence medium - the date has passed on the record's own evidence, but payment may have happened outside the repository) Route one line to the TechMedix master thread's `messages.md` asking it to check the registration status and consider adopting the record at `high` priority.

b) Leave it as triage with size `s` and let TechMedix pick it up in its own time.
