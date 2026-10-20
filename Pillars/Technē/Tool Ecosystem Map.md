---
note_type: pillars/note
updated: 2026-10-19T23:16:23Z
author: AI-assisted
---

# Tool Ecosystem Map

## Overview

The Knowledge Islands tooling layer combines governed knowledge, reusable capabilities, independently owned products and publication. [Known Lands](<../../Admin/Governance/Known Lands.md>) supplies canonical membership and ownership boundaries; [Ecosystem fundamentals](../../Admin/Governance/Decisions/GDR-KI-PRINCIPAL-006-knowledge-islands-ecosystem-fundamentals.md) supplies the shared routing decision.

## Components

| Repository | Role | Owned concern |
| --- | --- | --- |
| `ki-principal` | Capital and knowledge | Philosophy, governance and engineering practice |
| `ki-agentic-harness` | Reusable capabilities | Agent-facing contracts and conformance |
| `tools-ki` | Governance host | Executable KI operations and projections |
| `ki-techne-harness` | Implementation product | Controller and execution fabric |
| `tools-techne` | Implementation product | Operator CLI, diagnostics and releases |
| `apps-knowledgeislands.info` | Publication | Selected source-labelled public material |
| `ki-specifications` | Dormant standards home | Possible portable contracts after overall V1 |

## Knowledge and implementation

[Engineering Practice](<../Engineering Practice/Engineering Practice.md>) is Knowledge Islands Principal's canonical engineering discipline. [Implementation ownership](../../Admin/Governance/Decisions/ADR-KI-PRINCIPAL-006-techne-implementation-ownership.md) preserves the separate harness and CLI product boundaries; neither product becomes the knowledge owner.

Reusable agentic capabilities belong to the KI Agentic Harness. The `ki` executable owns its implemented governance operations; governance does not become infrastructure control through proximity to a controller or provider.

## Integrations and publication

MCP and environment tools provide specific capabilities under their own repository contracts. Their current identities and relationships are recorded in [Known Lands](<../../Admin/Governance/Known Lands.md>), rather than inferred from an older tool-name list.

The website selects and publishes material under its own authority without acquiring source ownership. Specifications is dormant before overall V1; repository-local contracts remain with their owners.

## Hold and retired source

The former Techné knowledge repository, `ki-techne-principal`, was retired on 4 October 2026 and is archived read-only as historical evidence. It holds no live work; its snapshots are noncanonical, and its decision copies are frozen projections of the Arcadia-maintained records.

The [Techne Programme Focus](<../../Admin/Governance/Policies/Techne Programme Focus.md>) governs the harness and operator CLI. This map changes neither services, runtime bindings, work states nor release authority.
