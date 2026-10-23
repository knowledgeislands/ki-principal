# Rig radar › radar-public-blind

**🤖 → 👤 Handoff to supervisor · Run report at 08:26 BST**

---

## Done

Independent review complete: recommend the first option, confidence high — public rings and Hold replacements communicate useful direction while preserving the public-view boundary and keeping trial management private.

Catalogue check passes: [Orca's declaration](/Users/krisbrown/.local/share/chezmoi/dot_config/rig/conf.d/private_10-applications.toml:847) is laptop-only; it is absent from the site's stored export.

Pipeline check passes: the [site pull](/Users/krisbrown/workspaces/personal/apps-rig.midnight.ninja/apps/site-rig/pipeline/pull.ts:28) explicitly exports `public` and intersects supplementary host membership with that selection.

Policy check passes: [RIG-PUB-012](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/specs/publishing.md:163) excludes retired declarations and observations regardless of view membership; [public relationship closure](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/specs/publishing.md:27) also excludes private relationship targets.

Report structure and source predicates pass; Markdown check passes with the repository configuration.

No repository changes or commits; no remote calls, provider commands or runtime tests. The excluded work folder was not read.

## In Progress

Nothing running. This is a recommendation for future behaviour: the inspected catalogue and stored public export do not yet contain structured radar fields.

## Queries

### RADAR-PUBLIC - How much radar should the public site show?

**Context:** The site is a curated public projection of Kris's setup. Orca's current trial does not authorise its publication, and retired tools must remain outside the projection.

**Query:** Which radar information should appear for tools selected by `public`?

**Options:**

a) (recommended, confidence high - Rings and replacements explain direction without publishing private review operations.) Show the ring and Hold replacement for public tools; omit review dates, checks and retired lists. Trial tools appear only after explicit public membership.

b) Show rings, dates and checks for every public tool. This adds maintenance pressure and can expose workflows, private dependencies or internal plans through free text; tool membership alone does not review those disclosures.

c) Show rings only. This preserves a narrow projection but leaves a Hold tool's visitor without the useful answer to what should replace it.

d) Additional option: use a), then allow a separately authored public trial summary by explicit opt-in if a future public Trial tool needs explanation. Keep the actual dated review and named checks private.

**Risks the options miss:** A public Hold tool can name a private replacement. Apply public relationship closure to replacement references, including prose and links, rather than publishing the private target. Explain that this is the public subset so an empty Trial ring is not read as an absence of experiments. When a tool retires, remove it from every generated site artefact and supplementary dataset; hiding its row leaves stale disclosure. Previously published copies cannot be recalled. Radar fields require an explicit export-contract and consumer review because the current allow-list does not include them.
