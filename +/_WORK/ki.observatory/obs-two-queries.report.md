# Model › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.observatory/work.md) › obs-two-queries

**🤖 → 👤 Handoff to supervisor · Run report at 00:18 BST**

---

## Done

Drafted the two owner queries below from the records and what they cite; read only, nothing changed or committed.

## In Progress

Nothing.

## Queries

### BANNER-GLYPHS

**Context:** [KI-DESIGN-OBS-015](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-OBS-015-banner-glyphs-question.md) is on hold for your answer only (review 2 November). The work model's banner writes five states with emoji (worker, supervisor, named target, on hold, finished), and the Observatory's Work tab prints them unchanged because you chose one notation everywhere ([PDR-KI-OBSERVA-008](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/decisions/PDR-KI-OBSERVA-008-line-glyphs-beside-tabs-and-subjects.md)). That makes it the one exception to the design's "no emoji" rule. ki-design has drawn five single-colour line glyphs, marked proposed and passing `lintIcon`: a mallet, a faceless head and shoulders, a map pin, an anchor and a pennant on a staff ([candidates](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/briefs/banner-glyph-candidates.md)). The notation belongs to the [`ki-coordination` standard's Banner section](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md#banner), so any change lands there first, then ki-design moves the glyphs into `@knowledgeislands/icons` and the Work tab follows. The hand-off text for the harness is already written ([answer file](/Users/krisbrown/workspaces/knowledge-islands/ki-design/-/observatory-handoff/ANSWER-2026-10-19.md)).

**Query:** Should the banner keep its emoji only, gain the line glyphs as an optional rendered form, or switch to line glyphs everywhere?

**Options:**
a) (recommended, confidence high - emoji still read in terminals, reports and commits, while rendered surfaces such as the Work tab lose their one "no emoji" exception) Keep the emoji as the standard's written notation and let a rendered surface draw the five line glyphs with the state's words beside them.
b) Keep the emoji as the only notation; OBS-015 closes with no change and the Work tab stays the documented exception.
c) Replace the emoji with line glyphs everywhere, which plain-text reports and terminals cannot show.

### STORAGE-OWNER

**Context:** [KI-OBSERVA-VIS-038](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-038-machine-instrument.md)'s tool-storage phase is a read-only view of what each tool stores across its XDG config, data, cache and state folders, and why. It reads repository-owned storage declarations alongside safe metadata. It waits only on which standard owns those declarations; the record rules out MCP binding governance and settles no schema ([decisions log](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.observatory/decisions.md), ROADMAP-CENSUS-2). Four candidates: [`ki-repo`](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/keystone/ki-repo/references/standards-configuration.md) owns every repository's contract and its `.ki.toml`, so it would cover tools, MCP servers and apps alike. [`ki-repo-tools`](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-tools/references/standards-tool-repositories.md) already requires a tool to follow XDG for what it writes, but covers only `tools-*` repositories. [`ki-engineering`](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-engineering/references/standards-engineering.md) owns how code resolves XDG paths, not what a tool declares. [Rig](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/README.md) catalogues every tool on the machine, third-party ones included, with purpose and rationale, but it is one tool's machine-side catalogue rather than a repository-owned standard.

**Query:** Which standard should own repository-owned storage declarations?

**Options:**
a) (recommended, confidence medium - it is the one repository-wide contract, so it covers tools, MCP servers and the Observatory itself, and `ki` can expose it as a stable machine contract) `ki-repo`, as a `.ki.toml` declaration, with `ki-engineering` keeping the path-resolution rule and Rig later adding third-party tools.
b) `ki-repo-tools`, extending its XDG rule into a declaration; this is narrower and leaves MCP servers and apps undeclared.
c) Rig's catalogue, which covers third-party tools but makes declarations machine-owned, not repository-owned.
d) `ki-engineering`, beside its XDG path rule, which stretches a code-toolchain standard into a declaration owner.
