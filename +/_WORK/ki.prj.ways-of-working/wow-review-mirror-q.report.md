# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of Working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-review-mirror-q

**🤖 → 👤 Handoff to supervisor · Run report at 22:21 GMT · last mark 01:07 GMT**

---

## Done

Local source review completed on 26 October 2026. No repository changes, commits, remote calls, credential access or excluded-file reads; only the requested status and report files were written.

### MIRROR-TOKEN

**Pick:** Revoke the integration and delete its 1Password item after the managed configuration change removes the last consumer.

**Confidence:** High.

**Reason:** A retired publisher has no continuing need for an active credential; rebuilding it later can use a fresh integration.

**Verified:** The [inventory](/Users/krisbrown/.local/share/chezmoi/.chezmoidata/mcp-servers.yaml:109) selects Claude Desktop and mcporter, references the deleted checkout and obtains the token through an `op:` reference. The [renderer](/Users/krisbrown/.local/share/chezmoi/.chezmoitemplates/mcp-servers-json:82) resolves that reference and serialises the result into JSON environment values. Both client templates use this renderer. The hosted Notion MCP is a separate inventory entry. The mirror checkout is absent locally; HNR's [site project](</Users/krisbrown/workspaces/humans-not-robots/hnr-principal/Streams/Projects/site-product.md:19>) names pt.humansnotrobots.be as its internal product site.

**Limits / false claims:** No local claim refuted. Actual rendered values, the 1Password item, integration state, transcript exposure, GitHub deletion/404 and deletion on the other machine were not inspected. Complete any remaining Notion removal that needs this integration before revoking it; removal of local configuration alone cannot establish that every consumer has finished.

### MIRROR-NOTE

**Pick:** Delete the folder and inbound mentions, and record the retirement as a dated line in Known Lands under one Enactment record.

**Confidence:** High.

**Reason:** The current tool chapter should describe available tools; a dated retirement entry and Git history preserve the historical record.

**Verified:** The chapter still describes the mirror as current. [Known Lands](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Known Lands.md:42>) still lists it as a member and records earlier retirements in dated prose below the table.

**Refuted:** There are two inbound Markdown links, from [Tools](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Tools/Tools.md:58>) and [Knowledge Islands](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Knowledge Islands.md:117>), plus a prose mention in [How Tools Connect](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Tools/How Tools Connect.md:49>), rather than three inbound links. All three mentioning notes need adjustment, including the Tools overview sentence.

### MIRROR-SITE

**Pick:** Remove the project card and map data entries, regenerate the SVGs using ki-design and rebuild.

**Confidence:** High.

**Reason:** Removing an unavailable project keeps the public catalogue accurate without adding a retirement feature solely for this deletion.

**Verified:** The [project entry](/Users/krisbrown/workspaces/knowledge-islands/apps-knowledgeislands.info/apps/site/src/_data/projects.json5:365) has adoption instructions and a repository link. The snapshot, generated chart manifest and both SVG layouts include the mirror; both SVGs link to its repository. The [validator](/Users/krisbrown/workspaces/knowledge-islands/apps-knowledgeislands.info/apps/site/scripts/verify-projects.ts:47) allows only published/source availability and requires a GitHub repository URL. The [provenance guide](/Users/krisbrown/workspaces/knowledge-islands/apps-knowledgeislands.info/docs/guides/developer/page-provenance.md:81) specifies snapshot refresh followed by design regeneration; the chart manifest is generated, so it should be regenerated rather than edited independently. ki-design contains the referenced archipelago renderer.

**Limits / false claims:** No local claim refuted. The remote 404 and currently deployed website were not checked.

### MIRROR-FRONTMATTER

**Pick:** Ask HNR to strip the five mirror keys in one bounded run after the Notion removal finishes, updating the conventions and consumers.

**Confidence:** High.

**Reason:** Obsolete publication controls and links to removed pages misdescribe the current publishing system; Git preserves their earlier values.

**Verified:** Five key names occur: `kb_notion_mirror_hash`, `kb_notion_mirror_published_at`, `kb_notion_mirror_url`, `kb_notion_mirror_root` and `kb_notion_mirror_exclude`. Both [.meta scripts](</Users/krisbrown/workspaces/humans-not-robots/hnr-principal/.meta/tools/mirror/README.md:26>) read the URL key, and the [Architecture Tracker recipe](</Users/krisbrown/workspaces/humans-not-robots/hnr-principal/Admin/Knowledge Management/Integrations/Claude/Live Artifacts/HNR Architecture Tracker Artifact.md:78>) consumes URLs and mirror freshness metadata. The receiver-owned run should cover the tracker as well as both scripts, Frontmatter Conventions, the activity and integration retirement; preserve `notion_source_url` provenance. The [sites state](</Users/krisbrown/workspaces/humans-not-robots/hnr-principal/+/_WORK/hnr.sop.sites/state.md:29>) already gates frontmatter removal on Notion reconciliation and archiving.

**Refuted:** Current local frontmatter counts are 272 hnr-shared notes and 2 hnr-principal notes, totalling 274, rather than 272 + 13 = 285. Both tracked-file and physical-file scans agree, excluding symlink duplicates and the forbidden filenames. The two principal notes contain only the exclusion key. Three notes overall carry that key: one shared and two principal.

**Limits:** The sites state records 483 pages in Trash and a root pointer to pt; leaf-to-root execution and current remote page state were not independently verified. Root/exclusion keys are publication controls in the conventions; server authorship of every key was not established from the deleted implementation.

## In Progress

Nothing.

## Queries

None.

### 🤖 → 👤 Handoff to supervisor · since 22:21 GMT

🤖 0 running · 👤 1 with you · ⛔ 0 blocked

- [handoff] Four-query independent review complete · supervisor · since 22:21 GMT

🧵 Coordination thread · Ways of Working (ki.ways-of-working)
