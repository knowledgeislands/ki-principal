# ki queries

## Open

### ACCEPT-WEBSITE - accept the website's design v1 record

**Context:** [KI-WEBSITE-SITE-044](/Users/krisbrown/workspaces/knowledge-islands/apps-knowledgeislands.info/docs/roadmap/KI-WEBSITE-SITE-044-design-v1.md), "Adopt ki-design v1", has been awaiting review since 20 October. It is the oldest record awaiting acceptance in the territory.

**Query:** Review and accept it now?

**Options:**

a) (recommended, confidence high - ACCEPT-BUNDLE puts the territory's unaccepted records first) Review it now through `ki-accept`.

b) Leave it awaiting review.

### ACCEPT-WOW - accept Ways of working's two records

**Context:** [KI-PRINCIPAL-OPS-014](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-OPS-014-gfm-conversion.md), the GFM conversion, has been awaiting review since 20 October, and [KI-PRINCIPAL-MOD-009](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-MOD-009-amend-adr-001-staging-wording.md), the ADR-001 staging wording, since 23 October.

**Query:** Review and accept them now, oldest first?

**Options:**

a) (recommended, confidence high - ACCEPT-BUNDLE, one bundle per work, oldest first) Review both now through `ki-accept`.

b) Leave them awaiting review.

### ACCEPT-OBSERVATORY - accept Observatory's two records

**Context:** [KI-OBSERVA-BRG-005](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-005-act-board-missing-parts.md) has been awaiting review since 20 October and [KI-OBSERVA-VIS-030](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-030-known-lands-chart.md) since 22 October. BRG-005 fails the roadmap audit on its Review and body order; ki.observatory has a message tonight (ROADMAP-AUDIT) to fix its structure first.

**Query:** Review and accept them once BRG-005's structure is fixed?

**Options:**

a) (recommended, confidence high - ACCEPT-BUNDLE, with the audit fix as a precondition) Review both through `ki-accept` once ki.observatory has fixed BRG-005.

b) Leave them awaiting review.

### ACCEPT-RIG - accept the Rig firewall record

**Context:** [KI-TOOL-RIG-CORE-062](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-062-own-address-firewall-destination.md), the own-address firewall destination, has been awaiting review since 22 October.

**Query:** Review and accept it now?

**Options:**

a) (recommended, confidence high - ACCEPT-BUNDLE) Review it now through `ki-accept`.

b) Leave it awaiting review.

### ACCEPT-CHEZMOI - accept the chezmoi latest-source record

**Context:** [PERSONAL-DOTFILES-UE-076](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/PERSONAL-DOTFILES-UE-076-always-run-latest-source.md), "always run the latest source", has been awaiting review since 24 October.

**Query:** Review and accept it now?

**Options:**

a) (recommended, confidence high - ACCEPT-BUNDLE) Review it now through `ki-accept`.

b) Leave it awaiting review.

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

## Parked

### ESTATE-CLOSE - retire Estate factorisation as prepared

**Context:** Under PROJECT-CLOSE a) (25 October) the retirement is prepared in [design/estate-factorisation-retirement.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/design/estate-factorisation-retirement.md): settle HOST-WRITES, ALIAS-OWNERS and RIG-REFS, route the parked queries to their works by message, then Kris accepts the close. Nothing is applied yet.

**Query:** Proceed with steps 1 and 2 of the note, with the close itself waiting for your acceptance?

**Options:**

a) (recommended, confidence high - restates Kris's own PROJECT-CLOSE a)) State of play sends the prerequisite and routing messages; Kris accepts the close once they are settled.

b) Amend the note first.

### SITE-DEPS - adopt the website's overdue dependencies

**Context:** apps-knowledgeislands.info fails DEPS-1: `@types/node` 26.6.5, `rumdl` 0.2.79 and Bun 1.4.3 are past the 14-day adoption window. Its work [ki.website](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.website/work.md) is seeded on hold; dependency freshness is a core requirement that a held queue does not exempt.

**Query:** Should a run adopt the updates now?

**Options:**

a) (recommended, confidence high - reviewed: the freshness rule is unconditional; the run updates the Bun pins in `packageManager` and `mise.toml` too) A bounded run adopts them with `bun run ki:deps:update`, verifies and commits.

b) Record a hold on the updates until the website work opens.

### PRE-REBASE-REF - the harness safety branch on terra

**Context:** fold-harness left a local safety branch `fold-harness/pre-rebase-main` in ki-agentic-harness on terra, pointing at the old harness main `57226cdea`. Harness main is pushed and level with origin; the branch exists on terra only and cannot be inspected from Sol.

**Query:** Should the safety branch be deleted?

**Options:**

a) (recommended, confidence high - reviewed: level main does not prove the old reference holds nothing unique, so the deletion waits on a check at terra) Delete it with `git branch -D` on terra after confirming `57226cdea`'s content is reachable from main or not needed.

b) Keep it as a recovery reference.

c) Delete it on terra now.

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
