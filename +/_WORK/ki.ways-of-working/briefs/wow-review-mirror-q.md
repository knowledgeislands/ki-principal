# wow-review-mirror-q - blind review of four queries after the notion-mirror repository was deleted

Kris deleted `knowledgeislands/mcp-ki-kb-notion-mirror` on GitHub and locally on sol and terra on 26 October 2026. You are an independent reviewer. For each query, verify the Context's claims directly where you can, in ~/workspaces (ki-principal, apps-knowledgeislands.info, ki-design, hnr-principal, hnr-shared) and the chezmoi source at ~/.local/share/chezmoi. Pick the option you would recommend, confidence high, medium or low, one-line reason, and note any claim you found false. Do not read any queries.md, decisions.md or *.report.md file. Read-only: change nothing, commit nothing, read no secret values, do not open 1Password, Notion or any GitHub API.

Report under ## Done one ### section per tag: pick, confidence, reason, verified or refuted claims. Then ## In Progress (Nothing) and ## Queries (None).

## MIRROR-TOKEN - the Notion integration token and 1Password item

**Context:** `mcp-servers.yaml` draws the mirror's token from a 1Password item and chezmoi renders it in plain text into mcporter and Claude Desktop configuration. The server is gone, HNR has moved to publishing through pt.humansnotrobots.be, and this run's transcript saw the token once before masking. The brief forbids touching Notion and credentials, so this is yours.

**Query:** Should the Notion integration behind the mirror be revoked and its 1Password item deleted once the chezmoi change is applied?

**Options (unranked):**

- Keep the item and integration for now, in case the mirror is rebuilt from the deleted repository's history elsewhere.
- Revoke the integration in Notion and delete the 1Password item after `chezmoi apply` removes the last reference.

### MIRROR-NOTE - what happens to the Notion Mirror chapter note in ki-principal

**Context:** `Pillars/Philosophy/Model/Tools/Notion Mirror/Notion Mirror.md` documents a tool that no longer exists, with three inbound links from the Tools index, How Tools Connect and Knowledge Islands. Known Lands records retired islands as a dated prose line rather than a row.

**Query:** Should the Notion Mirror note be deleted with its inbound mentions, or kept as a historical note?

**Options (unranked):**

- Keep the note with `status: retired - October 2026` and a line saying the repository was deleted, so the model's tool chapter still shows what the mirror was.
- Delete the folder and the three inbound mentions, and record the retirement as one dated line in Known Lands, all under one Enactment record.

### MIRROR-SITE - the public website's project card

**Context:** knowledgeislands.info carries a full project card and two archipelago map entries for the mirror, all linking to a GitHub repository that now returns 404.

**Query:** Should the card and map entries be removed, or should the card stay as a retired project without the repository link?

**Options (unranked):**

- Keep the card marked retired with the link removed, adding a retired state to the site's project schema.
- Remove the card and the two data entries, regenerate the SVGs from ki-design and rebuild.

### MIRROR-FRONTMATTER - the 285 notes carrying mirror frontmatter in HNR

**Context:** 272 hnr-shared notes and 13 hnr-principal notes carry `kb_notion_mirror_*` keys written by the server: hashes, publish timestamps, Notion URLs, root flags and two exclusion flags. HNR's Notion removal is trashing the mirrored pages leaf to root, so the URLs will soon point at trashed pages. The `.meta/tools/mirror` scripts and the Architecture Tracker artifact read `kb_notion_mirror_url`.

**Query:** Should the handoff to `hnr.sop.sites` ask HNR to strip the frontmatter keys, or leave them as a record of what was published?

**Options (unranked):**

- Leave the keys in place as published-history evidence and only retire the activity, the Integrations row and the publish scripts.
- Ask HNR to strip the five keys in one bounded run after the Notion removal finishes, updating Frontmatter Conventions and the two scripts that read them.
