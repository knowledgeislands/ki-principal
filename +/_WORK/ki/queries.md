# ki queries

## Open

None.

## Parked

### ACCEPT-CHEZMOI - accept the chezmoi latest-source record

**Context:** [PERSONAL-DOTFILES-UE-076](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/PERSONAL-DOTFILES-UE-076-always-run-latest-source.md), "always run the latest source", has been awaiting review since 24 October.

**Query:** Review and accept it now?

**Options:**

a) (recommended, confidence high - ACCEPT-BUNDLE) Review it now through `ki-accept`.

b) Leave it awaiting review.

### ACCEPT-KI-WEBSITE-SITE-044 - accept the website's design v1

**Context:** [KI-WEBSITE-SITE-044 (pruned)](https://github.com/knowledgeislands/apps-knowledgeislands.info/blob/ae886e2b/docs/roadmap/KI-WEBSITE-SITE-044-design-v1.md) moves the site onto `ki-design`: its tokens, type, Voyage and Atlas navigation, the restyled home page, a new Field Guide and `sync:design`. It also includes the Port switch. Every gate in its Verify list passed again on `main` at `2628c48`. Two items are still open, and neither can be settled without the network or a person:

- **The private citation.** The Field Guide cites `knowledgeislands/ki-design`. The page-provenance guide forbids citing a source no reader can open. `ki-design`'s `.ki.toml` has declared `visibility = "public"` since 18 October, but the 20 October review found the repository returned 404 to anonymous readers. This run made no network call, so it is unconfirmed whether it is public now.
- **The visual check.** The record asks for a visual check at 1440 and 390 px in both colour schemes. It has not been repeated since the Port update.

**Query:** Accept KI-WEBSITE-SITE-044 once you have confirmed that `ki-design` opens for an anonymous reader and looked at the pages?

**Options:**

a) (recommended, confidence high - reviewed: both gaps can be closed by checking the delivered result before deciding whether a repair is needed) Open `https://github.com/knowledgeislands/ki-design`, and the Field Guide's exact pinned source, in a private window. Look at the home page, one inner page and the Field Guide at 1440 and 390 px, in light and dark, and record the results. If both checks are good, accept through `ki-accept`; if access or the visuals fail, return it for that specific repair and a refreshed review packet.

b) Accept now, knowing the Field Guide's citation may not yet open for readers.

c) Return it to implementation to drop or replace the `ki-design` citation, and to refresh the out-of-date packet lines, before acceptance.

### ACCEPT-KI-PRINCIPAL-OPS-014 - accept the GitHub-flavoured Markdown conversion

**Context:** [KI-PRINCIPAL-OPS-014 (pruned)](https://github.com/knowledgeislands/ki-principal/blob/da027e6d/Streams/Roadmap/KI-PRINCIPAL-OPS-014-gfm-conversion.md) converted ki-principal to GitHub-flavoured Markdown in nine commits, plus the 20 October owner answers (plain images, template links, Link Review). Acceptance tests 1, 2, 3 and 5 are evidenced, and this run confirmed tests 2 and 5 again: no wikilinks remain, and no failure falls on the converted paths. Acceptance test 4 is still open and is yours under RENDER-CHECK a): the final Step, a client render check of the Library heading link and an alert in GitHub, Obsidian, Zed and the Observatory, plus the four plain images. In the Observatory, the dropped heading fragment has to be either recorded as a failure or accepted as a fallback.

**Query:** Run the four client render checks, then accept KI-PRINCIPAL-OPS-014?

**Options:**

a) (recommended, confidence high - the record makes test 4 your check before acceptance, and every other test is evidenced) Run the four render checks and tell me each outcome, including how to treat the Observatory fragment. Then accept, with the outcomes recorded.

b) Accept now, expressly waiving acceptance test 4.

c) Leave it awaiting review until you have time for the render checks.

### ACCEPT-KI-PRINCIPAL-MOD-009 - accept the ADR-KI-PRINCIPAL-001 staging amendment

**Context:** [KI-PRINCIPAL-MOD-009 (pruned)](https://github.com/knowledgeislands/ki-principal/blob/da027e6d/Streams/Roadmap/KI-PRINCIPAL-MOD-009-amend-adr-001-staging-wording.md) amended [ADR-KI-PRINCIPAL-001](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/ADR-KI-PRINCIPAL-001-provider-neutral-knowledge-acquisition.md) and the [Acquisition Process](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Processes/Acquisition Process/Acquisition Process.md>) in `3b1ade21` on 23 October. The changes stage material outside the receiving island, make delivery into `+/_ACQUIRED/` package acceptance, and call Acquire the port and sorting office, as CUSTOMS-WORDS a) approved. Checks pass on the delivered files. One problem: the rewritten Context sentence at line 18 says "The Harbour defined in SDR-KI-PRINCIPAL-002 is the island's incoming working area". [GDR-KI-PRINCIPAL-010](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/GDR-KI-PRINCIPAL-010-the-port.md) retired Harbour as a Knowledge Islands term on 18 October and made `+/` the Port's inbound side. The delivery therefore wrote a retired term back into a current ADR in the present tense. The References line describing SDR-KI-PRINCIPAL-002 is accurate as history. Against that, GDR-KI-PRINCIPAL-010's Consequences keep Harbour wording in earlier Decision Records as a historical record, to be read as the Port; but this sentence was rewritten in `3b1ade21`, after that decision.

**Query:** Return KI-PRINCIPAL-MOD-009 to implementation for a one-sentence fix of the Harbour wording, or accept it as it stands?

**Options:**

a) (recommended, confidence medium, review disagrees - a single sentence conflicts with GDR-KI-PRINCIPAL-010, but it can be read as SDR-KI-PRINCIPAL-002's historical name) Return it to implementation. Reword line 18 so that `+/` is the island's inbound side of the Port under GDR-KI-PRINCIPAL-010, cite `3b1ade21` in the record, then resubmit.

b) Accept as it stands, reading "Harbour" as SDR-KI-PRINCIPAL-002's own term; the blind reviewer prefers this at high, because GDR-KI-PRINCIPAL-010 expressly keeps Harbour wording in earlier Decision Records, and a one-sentence implementation cycle is not required for it alone, the ordinary acceptance gates staying separate.

### ACCEPT-KI-TOOL-RIG-CORE-062 - accept Rig's own-address firewall destination

**Context:** [KI-TOOL-RIG-CORE-062](https://github.com/knowledgeislands/tools-rig/blob/223ba459/docs/roadmap/KI-TOOL-RIG-CORE-062-own-address-firewall-destination.md) narrows the `macos-pf` anchor so it passes Tailscale sources only to the Mac's own tailnet addresses, discovered read-only from `ifconfig`. It refuses when no address can be found and reports a stale address. The gate refusal from 20 October is resolved, and today the full suite passes 645 of 645 and the audit has no failures. Its Verify list still asks for a read-only `ifconfig` on `terra` to confirm discovery under Homebrew `tailscaled`, and the 20 October reviewer asked for that evidence before resubmission. It was never obtained, and this run is barred from remote calls. The attended live rewrite of `sol`'s and `terra`'s anchors stays separate, connection-critical work with its rehearsed rollback. The on-link residual stays by your decision.

**Query:** Run the read-only `terra` check, then accept KI-TOOL-RIG-CORE-062?

**Options:**

a) (recommended, confidence high - reviewed: the named verification is still missing and can be completed without changing the firewall) Run `ssh terra /sbin/ifconfig | awk '/^[a-z]/{i=$1} /inet6? (100\.|fd7a:115c:a1e0)/{print i, $2}'` and tell me the output. If one `utun` interface carries both addresses, accept through `ki-accept`, with the output recorded. A different or ambiguous shape goes back to implementation review.

b) Accept now, carrying the terra check into the attended rollout, because Verify words it as "before any live apply".

c) Leave it awaiting review; the blind reviewer names this the proper interim state while terra is unavailable.

### ACCEPT-OBSERVATORY - accept the two Observatory records

**Context:** Under ACCEPT-OBSERVATORY a) (25 October) Kris chose to review and accept [KI-OBSERVA-BRG-005 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/0966ac3e/docs/roadmap/KI-OBSERVA-BRG-005-act-board-missing-parts.md) and [KI-OBSERVA-VIS-030 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/0966ac3e/docs/roadmap/KI-OBSERVA-VIS-030-known-lands-chart.md) through `ki-accept` once ki.observatory had fixed BRG-005's structure. BRG-005 now passes the roadmap audit, so that precondition is met. The review-prep run exited without finishing, so neither review is prepared yet.

**Query:** Rerun the review prep, then accept both records, oldest first?

**Options:**

a) (recommended, confidence high - restates Kris's own ACCEPT-OBSERVATORY a), its precondition now met) Rerun the review prep: check each record is still Awaiting review and each criterion against its evidence, then bring each disposition to Kris for acceptance through `ki-accept`.

b) Leave both awaiting review.

### AGENT-HOST - unstick the agent host work

**Context:** [ki.agent-host](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.agent-host/work.md) has sat With worker with no live session, and Kris's own IMPORTANT DRAIN line of 22 October is still unread at the top of its `messages.md`, with the two REFRESH lines beside it. No run can drain another work on State of play's authority.

**Query:** Open the agent host thread so it takes DRAIN and REFRESH first?

**Options:**

a) (recommended, confidence high - Kris's own instruction is waiting in its queue) Open its thread from `ki agent prompts ki`; it acts on DRAIN and the REFRESH re-reads before anything else.

b) Leave it until the Techne programme work resumes.

### CLI006-CONFIRM - confirmation design for the guarded host commands

**Context:** [KI-TOOL-TECHNE-CLI-006 (pruned)](https://github.com/knowledgeislands/tools-techne/blob/ffcaf0c099f1d3019247ff97466754b8a7312166/docs/roadmap/KI-TOOL-TECHNE-CLI-006-guarded-host-commands.md) must decide how `techne host rebuild` and `withdraw` meet `destroy.sh`'s `CONFIRM_DESTROY_AGENT_HOST`: a stale exported value could confirm a destroy on a clean host.

**Query:** Which confirmation design should the plan carry?

**Options:**

a) (recommended, confidence medium, review disagrees - the narrowest change to the existing script) Pass the confirmation through, scoped to the one command.

b) A Harness-declared confirmation with fresh interactive consent; the blind reviewer prefers this at high.

### CLI006-READY - set the guarded host commands record to Ready

**Context:** KI-TOOL-TECHNE-CLI-006 was replanned at tools-techne `31c7b7d` and its audits pass; it sits inside the Techne programme focus. Its handling of the destroy confirmation, CLI006-CONFIRM above, is part of the plan that would be made Ready.

**Query:** In what order should the plan reach Ready?

**Options:**

a) (recommended, confidence medium, review disagrees - the blind reviewer chose this at high because the confirmation design is part of the plan; the earlier ranking put review-now first) Settle CLI006-CONFIRM, then Kris reviews the plan and a ki-plan run sets it to Ready.

b) Kris reviews the present plan now and a ki-plan run sets it to Ready.

### ESTATE-CLOSE - retire Estate factorisation as prepared

**Context:** Under PROJECT-CLOSE a) (25 October) the retirement is prepared in [design/estate-factorisation-retirement.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/design/estate-factorisation-retirement.md): settle HOST-WRITES, ALIAS-OWNERS and RIG-REFS, route the parked queries to their works by message, then Kris accepts the close. Nothing is applied yet.

**Query:** Proceed with steps 1 and 2 of the note, with the close itself waiting for your acceptance?

**Options:**

a) (recommended, confidence high - restates Kris's own PROJECT-CLOSE a)) State of play sends the prerequisite and routing messages; Kris accepts the close once they are settled.

b) Amend the note first.

### KA-CLOSE - close the finished Knowledge acquisition work

**Context:** [ki.knowledge-acquisition](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.knowledge-acquisition/work.md) has been Finished since 20 October on Kris's word, all its decisions homed; its [Project](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/knowledge-acquisition.md) is `completed`, and its own next step is to delete the folder in one commit at the closing mark and archive its runs. State of play may not remove another work's folder on its own authority.

**Query:** Should a bounded run close it now?

**Options:**

a) (recommended, confidence high - reviewed: Finished and completed are both recorded; Kris authorises the closing mark and package scope) A bounded run strikes its closing mark, removes the package in one commit by explicit path and archives its runs with `ki agent close`.

b) Leave the folder until Kris opens that work's thread.

### SPECS-FOLDER - 25 unowned reports in ki.specifications

**Context:** `+/_WORK/ki.specifications/` has no `work.md` and holds 25 untracked run reports (plan, draft-review, revise, query-review, home-plan and others) from 24 October 21:10, so the work-package audit fails STRUCTURE-1. The [Specifications](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/specifications.md) Project is paused and a separate [ki.portable-specifications](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/work.md) package exists. Which session produced the reports is not known; nothing has been touched.

**Query:** Which session or work owns these reports?

**Options:**

a) (recommended, confidence high - reviewed: unknown ownership cannot justify inventing a package or moving the reports) Leave them untouched until Kris names the owning session or work, which then homes them.

b) Seed a minimal on-hold `ki.specifications` package around them.

c) Move them into ki.portable-specifications.

### MAIL-MCP-HOME - a home for the mail MCP records

**Context:** Eleven draft records for the mail MCP servers, KI-MCP-M365-TOOL-011 to TOOL-019 in mcp-m365 and KI-MCP-GSUITE-TOOL-008 and TOOL-009 in mcp-gsuite, plus [PERSONAL-DOTFILES-UE-097](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/PERSONAL-DOTFILES-UE-097-configure-gmail-routing-paths.md) in chezmoi, came to Knowledge Islands on 21 October: "For now, I think it's best to go back to the MCP. So, something in Knowledge Island." No work owns the MCP server repositories: ki.tools-burndown covers the `ki` CLI and Git tools, and ki.regular takes small one-off work.

**Query:** Which work should own these records?

**Options:**

a) (recommended, confidence high - reviewed: a coherent twelve-record backlog warrants a named owner) Kris registers a mail MCP Project and State of play seeds its package with the records as its first message.

b) ki.tools-burndown widens its scope to the MCP servers.

c) ki.regular holds them as drafts until Kris prioritises them.

### ACQUIRE-HOME - a home for CODEX-SESSIONS and DEFUDDLE-SKILL

**Context:** CODEX-SESSIONS manages repository-agent sessions, Codex and Zed external-agent ones included, through their local lifecycle from the `ki-housekeeping-chatgpt` inventory, with no transcript archive. DEFUDDLE-SKILL adds a `ki-acquire-web` provider skill using the pinned `defuddle` CLI, never its hosted API, trialled before adoption. Their natural owner, Knowledge acquisition, is completed.

**Query:** Where should these two go?

**Options:**

a) (recommended, confidence high - reviewed: each delivery can be bounded on its own without reopening a finished outcome; the open Codex states and cleanup policy are settled at planning) Route both to [ki.regular](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.regular/work.md) as separate pieces of harness skill work.

b) Route both to ki.ways-of-working.

c) Reopen Knowledge acquisition, or register a successor Project, for both.

d) Route both to ki.baseline-rollout.

### SANCTUARY-STAGE5 - take the Sanctuary package at stage 5

**Context:** Under [ADR-VA-WEBSITE-009](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/decisions/ADR-VA-WEBSITE-009-the-sanctuary-becomes-a-shared-editorial-library.md), Valle Armonia builds the Sanctuary editor through stages 2 to 4 and Knowledge Islands is asked to own stage 5: a separate vendored package repository, with packages-portal-commons the nearest precedent. Valle Armonia hands over verified code, fixtures and adapter contracts at stage 4 and asks for agreement before VA-WEBSITE-SANC-008 is readied.

**Query:** Should Knowledge Islands agree now to take stage 5?

**Options:**

a) (recommended, confidence medium, review disagrees - Knowledge Islands decides Project and repository when there is something to receive) Agree now, and set its Project and repository at the stage 4 handover.

b) Agree in principle, with Knowledge Islands reviewing the adapter contracts and fixture shape before stage 4 starts; the blind reviewer prefers this at medium, to check the portability boundary before extraction hardens it.

c) Decline for now; Valle Armonia keeps the Sanctuary.

### BASELINE - one baseline for every Capital

**Context:** The eight Capitals share 21 core skills but differ on `ki-work-roadmap`, `ki-work-recurring`, Paperclip, acquisition skills, configuration and `AGENTS.md` shape ([skills-assessment.report.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/skills-assessment.report.md)).

**Query:** Should one baseline become the standard for every Capital?

**Options:**

a) (recommended, confidence high - reviewed: a common minimum with conditional capabilities, keeping local integration settings and receiver-led adoption) Adopt the baseline, record it in `ki-repo-kb-principal`'s standard through ki.ways-of-working, and message each territory's State of play to conform its own Capital.

b) Adopt only the skill list now.

c) Leave each Capital as it is and fix only broken links.

### HARNESS-LINK - list each territory harness in its Capital

**Context:** Every territory harness adds a `<code>-extract-capability` skill, and hnr two engineering-convention skills, but all eight Capitals list only the KI harness in `[repo].harnesses`, so those skills reach no Capital.

**Query:** Should each Capital list its own territory harness alongside the KI harness?

**Options:**

a) (recommended, confidence high - reviewed: the extraction skills are invocation-only and protect source ownership, so linking grants no cross-repository authority) Add `<territory>/<code>-agentic-harness` to each Capital's `[repo].harnesses`.

b) Leave territory harnesses linked to their code repositories only.

### GRANOLA - declare Granola acquisition where it runs

**Context:** `ki-acquire-granola` is linked in six Capitals without being declared. hnr keeps a local `granola-sync` command; the blind review found legal's command and activity already retire direct import in favour of central acquisition, so the duplication claim is outdated for legal.

**Query:** How should Capitals that acquire from Granola carry the skill?

**Options:**

a) (recommended, confidence medium, review partly disagrees - one consistent declaration) Declare `ki-acquire-granola` in ki, hnr, er, legal, personal and va, and retire the local commands once their routing is in the skill's configuration.

b) Declare it only where capture actually runs, keep central capture with local reconciliation, and retire a local importer only after its routing is verified; the blind reviewer proposes this at high.

c) Unlink it where no acquisition happens and keep the local commands.

### LEGAL-GUIDANCE - legal's mandates into AGENTS.md

**Context:** Legal's `CLAUDE.md` holds 262 lines including its runtime-neutral case mandates (triple-check, adversarial stress-test, authority verification, pre-filing disciplines); its `AGENTS.md` only points to them, and Codex does not read `CLAUDE.md`. Legal work is high-stakes.

**Query:** Should legal move its mandates into `AGENTS.md` and promote its disciplines into harness skills?

**Options:**

a) (recommended, confidence high - reviewed: shared obligations belong in the shared entry point, and planned skills can verify the repeatable disciplines) Move the mandates table to `AGENTS.md` now and raise a record to promote the disciplines and commands into `legal-agentic-harness` skills.

b) Move the mandates only.

c) Leave legal unchanged.

### HNR-GUIDANCE - rewrite hnr's AGENTS.md

**Context:** hnr's `AGENTS.md` is out of shape against the Capital baseline and carries a stale Headroom block ([skills-assessment.report.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/skills-assessment.report.md)).

**Query:** Should hnr rewrite it?

**Options:**

a) (recommended, confidence high - a mechanical correction inside hnr's own authority) Message HNR's State of play to rewrite its `AGENTS.md` and drop the stale block.

b) Leave it until BASELINE is settled.

### THEME-REGISTRY - territory theme registries

**Context:** tmx, si and legal follow their own theme records; er has none.

**Query:** Should er be asked to capture one?

**Options:**

a) (recommended, confidence high - brings the last Capital into line with THEME-REGISTRY-ENFORCE) tmx, si and legal follow their own records, and er's State of play is asked by message to capture one.

b) Leave er without a theme registry.

### PRE-REBASE-REF - the harness safety branch on terra

**Context:** fold-harness left a local safety branch `fold-harness/pre-rebase-main` in ki-agentic-harness on terra, pointing at the old harness main `57226cdea`. Harness main is pushed and level with origin; the branch exists on terra only and cannot be inspected from Sol.

**Query:** Should the safety branch be deleted?

**Options:**

a) (recommended, confidence high - reviewed: level main does not prove the old reference holds nothing unique, so the deletion waits on a check at terra) Delete it with `git branch -D` on terra after confirming `57226cdea`'s content is reachable from main or not needed.

b) Keep it as a recovery reference.

c) Delete it on terra now.
