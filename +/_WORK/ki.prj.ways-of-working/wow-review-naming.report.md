# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-review-naming

**🤖 → 👤 Handoff to supervisor · Run report at 23:09 GMT · last mark 01:07 GMT**

---

## Done

- Completed an independent recommendation on NAMING-TO-KI; no repository changes or commits.
- Blindness check: did not read the work's queries, decisions or reports.
- Governance check: the principal and harness guidance retain receiving repositories' authority over their work.
- Naming check: the local canonical `ki-repo` repository standard contains no explicit reverse-domain naming rule; sampled KI, Personal and Valle Armonia checkout names use host order.
- Context check: no supplied fact was established to be wrong. HNR checkout directories on this machine still use host order, so the claimed nine GitHub renames and their completion across machines remain unverified. Registry and live Cloudflare connections were not inspected.
- Safety check: no remote calls, messages, service changes or repository writes; only the authorised run report and status files were written.

## In Progress

Nothing is running. The supervisor has the naming recommendation for the owner's decision.

## Queries

### NAMING-TO-KI - Adopt a naming convention without requiring an estate migration

**Context:** HNR reports renaming nine site repositories on 26 October 2026 to reverse-domain order, with hostnames, Worker names and work identifiers unchanged. Reverse-domain names group a domain's repositories together within its top-level domain, which is useful for browsing. That benefit supports a prospective convention, but does not itself justify changing existing repositories: renames require coordinating GitHub, two checkouts, registry identity and potentially build connections under the owner's limit against changes that could take a site down. Each territory retains its repository decisions. Existing host-order repositories can remain valid indefinitely; adoption need not create a migration obligation.

**Query:** Should Knowledge Islands adopt reverse-domain names for new site repositories while leaving each territory to decide whether to rename existing ones?

**Options:**

a) (recommended, confidence high - a prospective rule gains consistent grouping without requiring operational changes to existing sites) Adopt reverse-domain naming for new site repositories, record it in the harness [ki-repo standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/keystone/ki-repo/references/standards-repository.md), and send the proposal as a message to each territory's State of play. Leave existing names valid and any rename to the owning territory, with no deadline or automatic enforcement against them. Define the rule as reversing all hostname labels after `apps-`, including multi-part suffixes and nested subdomains: `kris.me.uk` becomes `apps-uk.me.kris`, and `rig.midnight.ninja` becomes `apps-ninja.midnight.rig`. This policy adoption changes no DNS, Cloudflare configuration or hostnames. Any later rename needs its own territory decision and assessment of the build connection and both checkouts; where the owner's site-safety limit cannot be met, retain the current name.

b) Decline: retain host-order naming as the estate convention and leave HNR's renames as its local choice. This avoids introducing a second estate naming form, but forgoes the domain-grouping benefit for new sites.

c) Adopt reverse-domain naming and send each territory a line to rename existing site repositories now. This achieves uniformity sooner, but imposes migration work and operational exposure without a demonstrated site or delivery benefit sufficient to justify it.

### 🤖 → 👤 Handoff to supervisor · since 23:09 GMT

👤 1 with you

- [with you] NAMING-TO-KI · supervisor · since 23:09 GMT

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
