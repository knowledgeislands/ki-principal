---
note_type: streams/design
status: draft
work: ki.ways-of-working
agent: wow-day-gov227-schema
written_at: 2026-10-21T14:14:00Z
---

# Repository storage declaration schema

This is a proposal for the short owner design session on [KI-HARNESS-GOV-227](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-227-repository-storage-declarations.md). Kris chose GOV227-SCHEMA a) in [owner answers, 21 October](../decisions.md#2026-10-21-1410-bst---owner-answers): design the schema in its own work, with a run preparing a draft. The query and its two options are preserved in this package's Git history, in `queries.md` at `8807fa78^`: a short session, recommended at high confidence because recovery and shared ownership remain undecided, or deferral to Future. This draft accepts neither the schema nor the delivery record and authorises no storage migration or machine change.

The recommendation is a versioned `storage` child of `[skills.ki-repo]`, with products, named XDG namespaces and separately classified locations. Keep the existing knowledge-base store roles and local bindings intact. A storage declaration describes intended behaviour; it does not prove that a directory exists, that an implementation follows XDG, or that content is safe to remove.

## Evidence and present contracts

The offline reading on 21 October covered these declarations, skills and readers:

- [Configuration ownership and repository kind](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/keystone/ki-repo/references/standards-configuration.md#repository-kind): `[skills.ki-repo]` owns `repo_type`, `primary_shape` and KB-only `store_roles`. The roles are `notes`, optionally `sources` and `legacy`; they are not XDG categories. Nested tables remain owned by their root skill.
- [Engineering XDG rule](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-engineering/references/standards-engineering.md#xdg-base-directory-paths-capability-repo-resolves-configdatacachestate-directory-on-host) and [tool repository standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-tools/references/standards-tool-repositories.md): engineering owns path resolution; the tool shape cannot supply declarations for every MCP server or app.
- [KB source relationships](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-kb/references/standards-source-mirrors.md) and [Project repository standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-project/references/standards-project-repository.md): source files, mirror metadata and repository shape retain their present owners. A Project's explicitly approved external source store does not become a KB `store_roles` declaration.
- [Local registry reader](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/storage/local-registry.ts): registry `schema = 1`; entries carry `repository`, physical `path`, optional `stores.sources`, `stores.legacy`, `absent_stores` and `search_boundary`. The selected real entries show ki-principal with a sources binding and tools-ki and the Harness without store bindings. No bound contents were opened; no physical source-store path is reproduced here.
- [Declaration reader](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/configuration/declaration.ts), [store inventory](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/storage/repository-stores.ts) and [registry projection](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/storage/registry-report.ts): roles are validated separately from bindings; availability distinguishes `available`, `unavailable`, `absent` and `missing`; the registry report intentionally omits physical paths. None provides a typed product-storage projection today.

The local repository registry is `$KI_STATE_HOME/registry.toml`, falling back through `$XDG_STATE_HOME/ki` to `~/.local/state/ki`. The separate harness acquisition configuration is `config.toml` under KI's config root. Registry registration is not acceptance of a declaration or permission to operate on its storage.

## Proposed ownership and schema

All fields below are proposed. `ki-repo` owns and validates the entire `.ki.toml` subtree `[skills.ki-repo.storage]`; tools-ki parses and projects it. Engineering retains resolver behaviour, and each product repository owns the truth of its declaration. Observatory consumes the projection without inferring lifecycle from XDG category, directory name, age or size.

| Container or field | Type | Required or default |
| --- | --- | --- |
| `storage.version` | Integer, exactly `1` | Required when `storage` exists |
| `storage.items` | Table keyed by product ID | Required; `{}` explicitly means no products in scope |
| `storage.namespaces` | Table keyed by namespace ID | Required; `{}` when no locations exist |
| `items.<id>.kind` | `tool`, `mcp-server` or `app` | Required |
| `items.<id>.locations` | Array of location tables | Required; `[]` explicitly means no host storage |
| `namespaces.<id>.category` | `config`, `data`, `cache` or `state` | Required |
| `namespaces.<id>.path` | Non-empty relative POSIX path | Required; relative to the XDG category root |
| `namespaces.<id>.owners` | Non-empty, unique product references | Required; includes every writer sharing the namespace |
| `namespaces.<id>.override_env` | Environment variable name | Optional; no product-specific override by default |
| `locations[].id` | Stable lowercase kebab-case ID | Required; unique within its product |
| `locations[].namespace` | Namespace ID in this declaration | Required |
| `locations[].path` | Relative POSIX path or `.` | Required; relative to the named namespace |
| `locations[].purpose` | Non-empty string | Required; says what is stored and why |
| `locations[].content` | `disposable`, `recoverable` or `knowledge` | Required; no inferred value |
| `locations[].canonical` | Boolean | Required; no inferred value |
| `locations[].recovery` | Non-empty recovery description | Required for `recoverable`; otherwise omitted |
| `locations[].owners` | Non-empty, unique product references | Defaults to the enclosing product |

Product and namespace IDs match `[a-z][a-z0-9]*(?:-[a-z0-9]+)*`. A product reference is its canonical repository URL plus `#<product-id>`, for example `https://github.com/knowledgeislands/tools-ki#ki`. The fragment is a logical product identifier, not a website anchor or instruction to contact GitHub. A repository may ship several products, including an app and an MCP server.

An omitted `storage` subtree means undeclared, never no storage. Once declared, every shipped product and every storage location must be covered; completeness is reviewed against implementation. An omitted category within a reviewed product means it has no locations there. A repository shipping no host product uses `items = {}` and `namespaces = {}`. No category is presumed disposable and no category is mandatory for a product.

**Resolution.** `category` selects the engineering-governed XDG root and its existing fallback. Append namespace `path`, then location `path`. If `override_env` is set and non-empty, it replaces the entire namespace root, not the XDG category root or the location path. It is an environment variable name only; its value is private runtime input. This models KI's existing `KI_STATE_HOME` and analogous overrides without embedding a user's home. This draft neither changes empty-variable handling nor establishes an exception to the engineering XDG rule. Products with file-level overrides or non-XDG defaults need an explicit mapping decision before their declaration is complete.

**Content.** `disposable` means losing it loses no unique knowledge and no required recovery input. `recoverable` means an identified surviving source and a stated procedure reproduce the required content; name both in `recovery`. `knowledge` means unique owner material or decisions whose loss is not covered by that guarantee. These are mutually exclusive assessments of loss, separate from `canonical`, which states whether this location is an authoritative source. Require `canonical = false` for disposable and recoverable content. Knowledge may be canonical or a non-reproducible working copy; neither implies deletion authority, backup coverage or permission to read it.

**Mixed and changing contents.** Split a mixed namespace into non-overlapping locations at the smallest useful boundary. A location may describe a whole subtree with `path = "."` only when one classification covers it. Do not declare a run-packet subtree universally recoverable merely because reports should eventually be homed in Git: before that receipt, it may contain unique knowledge. If content changes class through its lifecycle and cannot be split structurally, declare the conservative `knowledge` class and describe the transition in `purpose`; automatic disposal stays out of scope.

**Shared namespaces.** A namespace lists all writing products; read-only consumers are not owners. Each location lists its actual owners, a subset of its namespace owners, so sharing a parent does not imply co-ownership of every file. A shared namespace is repeated in each writing repository with the same category, path and complete owner set, though local namespace IDs may differ. Within one declaration, do not give the same category/path two namespace IDs. Cross-repository agreement is checked only against explicitly registered, readable checkouts. Missing peers remain unverified; conflicting claims are reported, never silently merged. Product-specific overrides may resolve differently on a machine; portable agreement does not establish physical co-location.

## What stays private and unchanged

- **Tracked `.ki.toml`:** repository identity, KB store roles and the proposed logical product storage contract. No username, absolute checkout, mounted source path, account identifier, environment value or credential.
- **Local `registry.toml`:** current repository URL-to-checkout mapping, `stores.sources`, `stores.legacy`, `absent_stores` and `search_boundary`, under its existing schema. Product storage adds no registry fields in this proposal. Registry bindings resolve repository-owned source material, not arbitrary application directories.
- **Other local configuration:** harness acquisition and local development selection retain their current owners; product override values stay in the existing runtime configuration. Do not move them into a public declaration or invent a new binding database.
- **Credentials:** remain in their existing credential store. Neither the repository declaration nor registry stores secret values. An audit reads declarations, never opens credential stores or expands stored source material.

The same word, storage, must not collapse two different relationships: ki-principal's `sources` role points to project material outside Git; tools-ki's XDG state contains the private registry that records that binding. Declaring the latter does not relocate the former under XDG.

## Worked examples from real repositories

These are proposed TOML fragments, not applied changes. The tools-ki example is a deliberately bounded slice, not a complete inventory of its four roots. The MCP example exposes an existing resolver mismatch. Neither should be copied as a claim that the product has completed adoption.

### tools-ki: private registry and personal configuration

The [KI resolver](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/paths.ts) implements product overrides before XDG defaults. Its [registry](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/storage/local-registry.ts) holds locally chosen bindings, and its [configuration reader](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/storage/registry.ts) reads harness acquisition choices. Treat those choices conservatively as knowledge: restoring a harness archive does not recover a user's binding decisions.

```toml
[skills.ki-repo.storage]
version = 1

[skills.ki-repo.storage.namespaces.ki-state]
category = "state"
path = "ki"
override_env = "KI_STATE_HOME"
owners = ["https://github.com/knowledgeislands/tools-ki#ki"]

[skills.ki-repo.storage.namespaces.ki-config]
category = "config"
path = "ki"
override_env = "KI_CONFIG_HOME"
owners = ["https://github.com/knowledgeislands/tools-ki#ki"]

[skills.ki-repo.storage.items.ki]
kind = "tool"

[[skills.ki-repo.storage.items.ki.locations]]
id = "repository-registry"
namespace = "ki-state"
path = "registry.toml"
purpose = "Repository checkouts, private store bindings and deliberate host absences."
content = "knowledge"
canonical = true

[[skills.ki-repo.storage.items.ki.locations]]
id = "personal-configuration"
namespace = "ki-config"
path = "config.toml"
purpose = "User-selected harness acquisition configuration and personal territory ordering."
content = "knowledge"
canonical = true
```

The installed harness is a candidate for `recoverable` only where the immutable acquisition reference or surviving local source is identified; a local-only source without a surviving copy is not. KB indexes, caches, installation receipts, development selections and agent packets need their own reviewed entries before this becomes a complete tools-ki declaration. Config rendered from a surviving managed source can be classified differently once that recovery source is evidenced; this proposal does not infer that every user's file is rendered.

### mcp-git-audit: audit history and a resolver gap

The [MCP configuration](/Users/krisbrown/workspaces/knowledge-islands/mcp-git-audit/src/config/index.ts) currently defaults the audit log beneath the literal home-relative `.local/state/mcp-git-audit` and allows `MCP_GIT_AUDIT_AUDIT_LOG_PATH` to override the file. Its [audit writer](/Users/krisbrown/workspaces/knowledge-islands/mcp-git-audit/src/utils/audit-log.ts) records invocation history and rotates it. Historical invocations cannot be recreated simply by rerunning a repository scan, so the conservative proposal is knowledge.

```toml
[skills.ki-repo.storage]
version = 1

[skills.ki-repo.storage.namespaces.audit-state]
category = "state"
path = "mcp-git-audit"
owners = ["https://github.com/knowledgeislands/mcp-git-audit#git-audit"]

[skills.ki-repo.storage.items.git-audit]
kind = "mcp-server"

[[skills.ki-repo.storage.items.git-audit.locations]]
id = "invocation-history"
namespace = "audit-state"
path = "."
purpose = "Original invocation audit history, including the active log and its rotations."
content = "knowledge"
canonical = true
```

This fragment is an XDG adoption target, not a truthful description of all current resolver behaviour. The namespace-wide `.` also needs confirmation that the product exclusively uses this directory for logs. Before adoption, its owner must settle the existing home-relative default and file-level override mapping. A repository declaration must not conceal these gaps; the audit records implementation alignment as unverified or mismatched. No MCP implementation change or new roadmap item is made by this run.

### ki-principal: a sources store is not application state

The island's [current declaration](../../../../.ki.toml) contains:

```toml
[skills.ki-repo]
repo_type = "kb"
primary_shape = "ki-repo-kb"
store_roles = ["notes", "sources"]
```

Those fields remain in place. `notes` resolves to the registered checkout. Its sources role is bound privately in the local registry; a missing binding is different from an explicit `absent_stores = ["sources"]`. Neither means the sources are disposable. The proposed product-storage addition, if the owner confirms this KB ships no host product, is:

```toml
[skills.ki-repo.storage]
version = 1
items = {}
namespaces = {}
```

This expresses an empty product inventory while retaining the external sources requirement. A Project with an approved source-store binding likewise keeps its opt-in and private binding, without acquiring KB-only `store_roles`. No OneDrive path, source-store creation or binding change follows from adopting this schema.

## Migration and delivery boundary

1. **Settle this draft with Kris.** Record the chosen schema, loss semantics and shared-namespace rule in the existing owner design work for [KI-HARNESS-GOV-227](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-227-repository-storage-declarations.md). Keep the record draft until its own planning resolves the remaining reader and specification obligations.
2. **Implement the contract in the Harness.** Extend `ki-repo`'s configuration standard, rubric, fixtures and generated publication; engineering adds its cross-reference. Missing storage declarations initially report undeclared coverage, not inferred empty storage. Reject malformed opted-in declarations immediately. No conformer guesses purposes, recoverability or owners.
3. **Expose it in tools-ki.** Its current parser carries skill configuration, but the named metadata and registry readers do not expose this typed contract. Plan a typed storage reader and a versioned machine projection before the Observatory depends on it; settle whether a portable specification is required in the delivery record. Default projection includes logical declarations and validation state only. Resolved physical paths belong to separately authorised local inspection, not the existing path-free registry report.
4. **Adopt per repository.** Inventory the implementation offline; have its owner review classifications, recovery evidence and all shared writers; add declarations through that repository's own process. Preserve current `store_roles`, registry schema and source-store bindings byte-for-byte. Missing or unavailable stores retain their existing meaning. Do not create, move, rebind or remove storage as part of adoption.
5. **Enable the Observatory phase after the reader exists.** It shows declared intent, unverified claims and observed availability separately. Only its tool-storage phase waits; other phases continue. Promote missing-declaration coverage to enforcement only after an explicitly agreed rollout boundary, not on installing the new Harness.

If another repository needs work, its owner receives one message in the owning work's `messages.md`; this draft creates no triage or roadmap records and makes no cross-repository write. Registry migration is deliberately none. Any later product-path migration needs a separate implementation plan and authority.

## Proposed audit rules

**Mechanical declaration checks:**

- Parse TOML, require integer `version = 1`, tables and arrays of the stated types, valid unique IDs and known keys only within the owned storage subtree. Unsupported versions fail closed. Absence of the subtree is undeclared coverage; explicit empty tables are a reviewed no-product claim.
- Require a product kind and explicit location array for each item. Resolve each location's namespace, reject unused namespace declarations, and require every local owner reference to name a declared product. Require the enclosing product among the owners of each location it writes, and those owners among its namespace owners. An app without host storage is valid with `locations = []`.
- Require normalised relative paths, with no leading slash, drive prefix, backslash, `~`, `..`, empty component, environment interpolation or glob. Permit `.` only for a location. Identical namespace category/path pairs are invalid within one declaration. Reject duplicate locations and overlapping locations in the same category after combining namespace and location paths; compare path components, not string prefixes.
- Require non-empty purpose, explicit content class and canonical flag. Reject `canonical = true` for disposable or recoverable content. Require a non-empty recovery description exactly when the class is recoverable. Schema validity alone does not validate the recovery claim.
- Require unique canonical product references in owner arrays, every location owner to belong to its namespace, and override names matching `[A-Z][A-Z0-9_]*`. Reject conflicting namespace override names for the same physical namespace claim; an unset override requires no registry entry.
- In an explicitly selected set of registered checkouts, group namespace claims by category and path and compare complete owner sets. Check co-owned location claims agree on their owners and classification. Unreadable or unregistered peers remain unverified with a warning; actual disagreement fails the selected agreement check. No network discovery, directory traversal or content read is part of declaration validation.

**Review and evidence checks:**

- Compare declared products and paths with the shipped implementation, including environment overrides and non-default XDG tests. Report omissions and resolver mismatches separately from a structurally valid table. Passing TOML shape is not a passing implementation audit.
- For each recoverable location, establish a surviving source and a feasible reconstruction procedure. For each knowledge location, establish who owns it and whether it is canonical. A backup claim requires evidence beyond the declaration; never infer it from cloud synchronisation or a conventional directory name.
- Review broad directories for mixed contents, conditional run-packet homing and shared writers. Read-only consumers cannot acquire ownership by appearing in an inventory. A cross-repository overlap is unverified until the relevant owners' declarations can be compared.
- Confirm declarations disclose no private physical bindings or secrets. Do not expand a source store, follow a symlink into it, probe live services, apply environment changes or offer deletion as an audit remedy.

Delivery fixtures should cover a valid tool, MCP server, app with no storage and KB with no products; missing and unsupported versions; malformed types and owner references; escaping and overlapping paths; absent recovery evidence; conflicting shared owners; unregistered peers; and non-default XDG/product overrides. These are proposed acceptance checks for delivery, not tests implemented by this drafting run.

## For the session

1. **SCHEMA-SHAPE:** Adopt `skills.ki-repo.storage` version 1 with products, namespaces and locations? Recommend yes, with explicit empty inventories and no default content class; confidence high. It fits the existing table ownership rule and keeps KB source roles separate.
2. **LOSS-AND-AUTHORITY:** Accept `disposable`, `recoverable` and `knowledge` plus an explicit canonical flag and required recovery explanation? Recommend yes, conservatively classifying mixed or lifecycle-dependent material as knowledge; confidence high. Keep disposal authority outside the declaration.
3. **SHARED-OWNERS:** Repeat complete namespace writer sets in participating repositories, with location owners as subsets? Recommend yes for this first schema, checking agreement over registered checkouts and warning on unavailable peers; confidence medium. It avoids a new central registry, at the cost of declarations needing to agree.
4. **RESOLVER-EXCEPTIONS:** Is namespace-root `override_env` sufficient for version 1, leaving file-level overrides and existing non-XDG defaults visibly unverified until their owner settles them? Recommend yes; confidence medium. It matches KI today without pretending the MCP example already complies; add a separate explicit mapping only if a real adopter requires it before release.
5. **ROLLOUT-AND-READER:** Begin with optional declarations, strict opted-in validation and a typed, path-free tools-ki projection before Observatory adoption? Recommend yes; confidence high. Set the later required-coverage boundary in the delivery plan, and settle the machine-contract specification there before the record becomes Ready.
