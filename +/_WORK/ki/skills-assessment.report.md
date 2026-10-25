# [Knowledge Islands](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Charter.md) › State of play › skills-assessment

**🤖 → 👤 Handoff to supervisor · Run report at 17:00 BST · last mark 02:05 BST on 20 October**

---

## Done

- Read-only assessment of the eight Capitals and their territory harnesses, under SKILLS-ASSESSMENT (Kris, 24 October). No commits; nothing edited or sent outside this report.
- Checks: `ki repo audit` ran offline on seven Capitals (ki 6 failing criteria, hnr 6, personal 5, tmx 4, er 3, si 2, va 1). On legal-principal it did not finish within 60 seconds, so legal has no audit result. None of the audit failures concern which skills are declared; they are content gates, listed under gap 14.

### 1. Matrix

Key: ✓ declared and linked · – missing · U declared in `.ki.toml` but not linked · L linked in `.claude/skills` and `.agents/skills` but not declared. The territory harnesses override nothing.

| Skill | ki | hnr | er | lgl | personal | tmx | va | si |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 21 core skills † | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| ki-work-roadmap | ✓ | ✓ | ✓ | ✓ | – | ✓ | U | ✓ |
| ki-agent-coordination-paperclip | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | L | ✓ |
| ki-acquire-granola | L | L | L | L | L | – | L | – |
| ki-work-recurring | – | ✓ | – | ✓ | – | – | – | – |
| ki-trades | ✓ | – | – | – | – | – | – | – |
| ki-engineering | ✓ | – ‡ | – | – ‡ | – | – | – | – |
| ki-diagrams | – | – | – | – | U | – | – | – |
| ki-subagents | – | – | – | L | – | – | – | – |
| Territory harness skills § | – | – | – | – | – | – | – | – |
| `ki-coordinator` output style | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Theme registry ¶ | ✓ | ✓ | – | Initiatives | ✓ | – | ✓ | – |
| Territory work in `+/_WORK/` | 14 | 25 | 1 | 1 | 5 | 1 | 4 | 1 |
| Local commands (`.claude/commands`) | 0 | 3 | 0 | 25 | 0 | 0 | 0 | 0 |

† ki-repo, ki-authoring, ki-repo-kb, ki-repo-kb-streams, ki-repo-kb-activities, ki-repo-kb-live-artifacts, ki-repo-kb-principal, ki-decision-records, ki-binding, ki-binding-claude, ki-binding-chatgpt, ki-housekeeping-claude, ki-housekeeping-chatgpt, ki-tokenomics, ki-tokenomics-claude, ki-tokenomics-chatgpt, ki-git, ki-work (adapter `kb-streams`), ki-work-package, ki-delegation, ki-coordination. Each runtime gets its own variant: the Claude variant links only to Claude, the ChatGPT variant only to Codex, as intended. ‡ Explicitly switched off with `coverage-engineering = false`. § Each territory harness adds one `<code>-extract-capability` skill, and hnr adds two more, `hnr-frontend-conventions` and `hnr-backend-conventions`. No Capital names its own territory harness in `[repo].harnesses`, so none of these skills reaches a Capital. ¶ `Streams/Themes/` and `Streams/Projects/`. Legal still uses the old `Streams/Initiatives/` (7 entries) and has two Projects; er, tmx and si have neither.

### 2. Where they are consistent

- All eight carry the same 21 core skills, adopt the same harness (`knowledgeislands/ki-agentic-harness`), declare `repo_type = "kb"` and `primary_shape = "ki-repo-kb"`, support all three runtimes and declare the `notes` and `sources` store roles.
- All eight set `auto_memory = "disabled"` for both housekeeping skills, use the `ki-coordinator` output style, have a `.codex/config.toml` and git-ignore their skill links.
- All eight have a territory work package in `+/_WORK/<code>/` with the five files. Each `CLAUDE.md` imports `AGENTS.md`. Each `AGENTS.md` sets an Enactment gate with the same exemptions and starts from `Admin/MEMORY.md`.

### 3. Gaps and divergences

1. Personal declares no `ki-work-roadmap`, so its records have no area codes (`PERSONAL-PRINCIPAL-022`). er declares the skill but gives no areas (`ER-PRINCIPAL-014`).
2. va declares `ki-work-roadmap` but it is not linked, and has `ki-agent-coordination-paperclip` linked but not declared. Its links look stale against its `.ki.toml`.
3. Personal declares `ki-diagrams`, but it is not linked.
4. `ki-acquire-granola` is linked in six Capitals but declared in none, which suggests a user-scope or acquisition link outside `.ki.toml`. tmx and si do not have it.
5. Legal has `ki-subagents` linked but not declared.
6. `ki-work-recurring` is declared only in hnr and legal, although all eight declare `ki-repo-kb-activities`.
7. `ki-trades` is declared only in ki. Under HANDOFF-AS-MESSAGE it may not be needed in a Capital's baseline at all.
8. The `ki-repo-kb-streams` `process_note` setting is missing in hnr and personal. er writes it with a `.md` suffix where the others write it without.
9. No territory harness is wired to its Capital (matrix note §). The `*-extract-capability` skills are therefore unused where the territory's direction is set.
10. The theme registry is missing in er, tmx and si, and legal is still on `Streams/Initiatives/`. Records to fix this already exist for three of them: [TMX-PRINCIPAL-KB-009](/Users/krisbrown/workspaces/techmedix/tmx-principal/Streams/Roadmap/TMX-PRINCIPAL-KB-009-establish-theme-registry.md), [SI-PRINCIPAL-KB-002](/Users/krisbrown/workspaces/sacred-inquiry/si-principal/Streams/Roadmap/SI-PRINCIPAL-KB-002-establish-theme-registry.md) and [LGL-PRINCIPAL-OPS-029](/Users/krisbrown/workspaces/legal/legal-principal/Streams/Roadmap/LGL-PRINCIPAL-OPS-029-migrate-initiatives-to-themes.md). er has none.
11. The hnr `AGENTS.md` (119 lines) still uses the old template. It restates what `ki-repo-kb` owns (index notes, Calendar layout, session digests, querying, note format), uses `[[wikilinks]]` and em-dashes, and calls the governance notes "KB Specifics" where the others say `Admin/Governance/`. Its `CLAUDE.md` contains a Headroom learn block with stale paths (`kit-hnr`, `/Users/krisbrown/kis/hnr`).
12. Legal's `CLAUDE.md` (262 lines) holds runtime-neutral case mandates that belong in `AGENTS.md`: the triple-check, the adversarial stress-test, authority verification and the pre-filing disciplines. These recurring disciplines are candidates for a legal harness skill. Its 25 slash commands are also local skill-like procedures.
13. hnr's `granola-sync` command and legal's `legal-file-system-granola-import` command duplicate `ki-acquire-granola`. hnr's `.claude/tasks/email-triage/` Python scripts overlap with the mcp-m365 routing tools.
14. The audit content failures repeat across Capitals:
    - the Markdown mechanical gate fails in ki, hnr, er and personal;
    - the acquired-packet scaffold check fails in ki, hnr, er, personal and tmx;
    - the closed-schema check on work-package files fails in most Capitals;
    - `.rumdl.toml` has drifted from the house template in most Capitals;
    - tmx has 48 packet-structure failures under `ki-delegation`.
15. Only va declares `maturity`.
16. Only ki and legal set `ki-tokenomics` options. hnr and legal rely on the housekeeping setting and do not set `autoMemoryEnabled` in `.claude/settings.json`.
17. tmx, si and personal restate their stores and the Enactment gate in both `AGENTS.md` and `CLAUDE.md`. Every `AGENTS.md` restates the Enactment gate, which `ki-repo-kb-streams` or `ki-repo-kb-principal` could own in one line. The store-alias and mirroring rules repeated in tmx, si, legal, er and personal are a candidate for a `ki-repo-kb` sources-store section.
18. Only ki's `AGENTS.md` states territorial authority and the cross-repository choreography (handoffs travel as messages). The other seven do not, although HANDOFF-AS-MESSAGE binds every territory.
19. Legacy "Kit" naming survives in personal (`repo_code = "PERSONAL-PRINCIPAL"`, `kb.*` work ids, Paperclip `KIT`, "Kit Principal"), in legal (`kit-legal-notes`) and in tmx (`kit-techmedix-*`).
20. The lifecycle skills (`ki-next`, `ki-plan`, `ki-implement`, `ki-accept`, `ki-batch`, `ki-recap`, `ki-work-design`) are declared in no Capital. They come only from user scope, so Codex or another machine may not have them.

### 4. Proposed baseline for a Capital

- **Skills:** the 21 core skills, plus `ki-work-roadmap` with declared areas, `ki-work-recurring` (since every Capital has Activities), `ki-agent-coordination-paperclip` where the territory has a Paperclip company, and the territory harness in `[repo].harnesses`. Opt-in, declared explicitly rather than linked silently: `ki-acquire-granola` and other acquisition skills, `ki-engineering` only with a real toolchain, `ki-diagrams`.
- **Configuration:** `ki-repo-kb-streams.process_note` set to `Admin/Operations/Processes/Enactment Process`, `maturity` declared, `outputStyle = "ki-coordinator"` and `autoMemoryEnabled = false` in `.claude/settings.json`.
- **Structure:** a territory package in `+/_WORK/<code>/` and a theme registry in `Streams/Themes/` and `Streams/Projects/`.
- **Guidance:** `AGENTS.md` in the ki-principal shape (identity, territorial authority, the choreography line, the Enactment gate in one line, local choices only), and `CLAUDE.md` holding only `@AGENTS.md` and Claude-specific lines.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Legal's audit result is missing, because it did not finish within 60 seconds.
- Queries BASELINE, HARNESS-LINK, GRANOLA and LEGAL-GUIDANCE are medium confidence and are marked `needs blind review`. No review has been run.

## Queries

### BASELINE - Adopt a Capital baseline skill set

**Context:** The eight Capitals share 21 core skills but differ on `ki-work-roadmap`, `ki-work-recurring`, Paperclip, acquisition skills, configuration and `AGENTS.md` shape (section 3). Section 4 proposes a baseline. Under HANDOFF-AS-MESSAGE, each territory would conform its own Capital, prompted by a message.

**Query:** Should the section 4 baseline become the standard for every Capital?

**Options:** a) (recommended, confidence medium - needs blind review; it fixes most gaps in one move, but which skills count as opt-in is a judgement) Adopt the baseline, record it in `ki-repo-kb-principal`'s standard through ki.ways-of-working, and send each territory's State of play a conform message. b) Adopt only the skill list now and leave configuration and `AGENTS.md` shape for later. c) Leave each Capital as it is and fix only the broken links (gaps 2, 3 and 5).

### HARNESS-LINK - Wire each territory harness into its Capital

**Context:** Every territory harness adds a `<code>-extract-capability` skill (hnr also adds two engineering-convention skills), but no Capital lists its harness in `[repo].harnesses`, so these skills reach no Capital.

**Query:** Should each Capital list its own territory harness alongside the KI harness?

**Options:** a) (recommended, confidence medium - needs blind review; it puts territory capability where direction is set, but the hnr engineering skills may belong only in the code repositories) Add `<territory>/<code>-agentic-harness` to each Capital's `[repo].harnesses`. b) Leave the harnesses linked only to their member code repositories.

### GRANOLA - Declare acquisition skills explicitly

**Context:** `ki-acquire-granola` is linked in six Capitals without being declared, and hnr and legal also keep their own Granola commands that duplicate it.

**Query:** Should Capitals that acquire from Granola declare the skill and retire their local commands?

**Options:** a) (recommended, confidence medium - needs blind review; the skill is canonical, but the local commands may carry territory routing the skill does not have yet) Declare `ki-acquire-granola` in ki, hnr, er, legal, personal and va, and retire hnr's `granola-sync` and legal's `legal-file-system-granola-import` once their routing is in the skill's configuration. b) Unlink it where no acquisition happens, and keep the local commands.

### LEGAL-GUIDANCE - Move legal's mandates and promote its disciplines

**Context:** Legal's `CLAUDE.md` holds 262 lines of runtime-neutral case mandates (the triple-check, the adversarial stress-test, authority verification, the pre-filing disciplines) plus 25 commands. That breaks the split where `AGENTS.md` carries shared guidance and `CLAUDE.md` only Claude-specific additions, and Codex does not see these mandates.

**Query:** Should legal move its mandates into `AGENTS.md` and promote its repeatable disciplines into a legal harness skill?

**Options:** a) (recommended, confidence medium - needs blind review; Codex currently misses binding case rules, but legal work is high-stakes and the move needs care) Legal moves the mandates table to `AGENTS.md` now and raises a record to promote the disciplines and commands into `legal-agentic-harness` skills. b) Move the mandates only, and keep the commands as they are. c) Leave legal unchanged.

### HNR-GUIDANCE - Rewrite hnr's AGENTS.md and CLAUDE.md

**Context:** hnr's `AGENTS.md` uses the old template and restates `ki-repo-kb`, and its `CLAUDE.md` Headroom block points at paths that no longer exist (`kit-hnr`, `/Users/krisbrown/kis/hnr`). I checked both directly.

**Query:** Should hnr bring its guidance into the ki-principal shape?

**Options:** a) (recommended, confidence high - verified stale and duplicated content; the change is reversible through the Enactment Process) Send HN > SoP a message to rewrite `AGENTS.md` in the ki-principal shape and drop or regenerate the Headroom block. b) Only regenerate the Headroom block.

### THEME-REGISTRY - Finish the theme-registry migration

**Context:** er, tmx and si have no theme registry, and legal is still on `Streams/Initiatives/`. tmx, si and legal already have records for this (gap 10); er does not.

**Query:** Should the territories finish the migration, with er prompted to capture its own record?

**Options:** a) (recommended, confidence high - three records already exist; only er lacks one) Leave tmx, si and legal to their records, and send ER > SoP one message asking it to capture and schedule its registry. b) Defer all four until the baseline is settled.

### 🤖 → 👤 Handoff to supervisor · since 17:00 BST

👤 6 with you

- [with you] BASELINE · owner · since 17:00
- [with you] HARNESS-LINK · owner · since 17:00
- [with you] GRANOLA · owner · since 17:00
- [with you] LEGAL-GUIDANCE · owner · since 17:00
- [with you] HNR-GUIDANCE · owner · since 17:00
- [with you] THEME-REGISTRY · owner · since 17:00

🧵 State of play thread · KI > SoP (ki)
