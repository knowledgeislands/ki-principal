---
note_type: pillars/note
updated: 2026-10-21T13:51:58Z
author: AI-assisted
---

# Principles

## Purpose

These principles guide engineering choices across the Knowledge Islands ecosystem.

They are decision criteria, not immutable implementation rules; trade-offs may justify exceptions when their rationale and consequences are explicit.

## Architecture Before Implementation

Establish responsibilities, interfaces, constraints, and operational consequences before committing to a detailed implementation.

Implementation work should make the architecture more concrete, not silently become the architecture.

## Clear Separation of Responsibilities

Assign distinct responsibilities to intent and planning, deterministic orchestration, persistent execution, engineering interaction, and governed knowledge.

Interfaces between these responsibilities should be explicit so that components can evolve independently and failures can be understood.

## Governed Knowledge by Design

Treat knowledge capture, retrieval, reuse, and change as governed activities.

Preserve context and provenance sufficiently for an engineer to assess whether knowledge remains applicable.

## Provider-Neutral Execution

Choose execution targets according to the workload and its constraints rather than provider preference alone.

The architecture must accommodate local, managed, elastic, and future dedicated execution without coupling the overall model to a single provider.

Apply neutrality beyond execution to models, agent frameworks, IDEs, orchestrators and vendors. Portability must not reduce every tool to the weakest shared feature set; use distinctive capabilities where they serve the workload, with the resulting constraints and trade-offs made explicit.

## Isolate Independently Acting Work

Give each independently acting agent task an execution boundary proportionate to its authority and risk. Prefer a disposable or explicitly resumable environment built from a portable declaration, with identity, state, credentials, network access, evidence return, and teardown made explicit.

Attached interactive assistance may share the engineer's working context when its scope and review boundary remain clear. Isolation follows the operating mode and consequences of the work, not the mere use of AI.

## Deterministic Control Around Probabilistic Capability

Use AI where reasoning, synthesis, or adaptation offers value, and use deterministic mechanisms where correctness, repeatability, or operational control is required.

The boundary between the two should be visible in both architecture and operations.

## Security and Privacy as Design Inputs

Consider data sensitivity, access, locality, isolation, and auditability when making architectural and execution decisions.

Security controls should follow the workload and its risk, not be added only after a system is operational.

## Evidence and Explicit Trade-offs

Record the evidence, alternatives, and consequences behind material decisions.

When a choice introduces a limitation or debt, document it so that future review can be intentional.

## Evolvable by Default

Prefer modular structures, replaceable components, and incremental change.

The knowledge base and the platform should be able to improve without requiring a wholesale rewrite or the loss of historical reasoning.

## FOSS-First and Inspectable

Prefer Free and Open Source Software and open standards where practical. High-quality freemium components may be appropriate, but avoid unnecessary proprietary lock-in. Core contracts should remain inspectable and portable.

## Adoption Provenance

The extension to Provider-Neutral Execution and FOSS-First and Inspectable originated in a ChatGPT conversation captured on 2026-10-03 and reconciled on 2026-10-11, when the other principles it proposed were found already held. Kris [adopted both on 2026-10-21](https://github.com/knowledgeislands/ki-principal/blob/d09a675653b3998b60361e71c13daa379e088d57/+/_WORK/ki.prj.ways-of-working/decisions.md#2026-10-21-1435-bst---candidate-principles-and-structure-todos) as qualified engineering decision criteria. Adoption grants no implementation, product, service or provider change. Related unsettled concepts remain in [Emerging Concepts](<../../Philosophy/Emerging Concepts/Emerging Concepts.md>).

## Provenance

Adopted into Knowledge Islands Principal from [the retained Techné source](https://github.com/knowledgeislands/ki-techne-principal/blob/b25e9c950fd87715d12f76b69bb2079c3a4fc054/Pillars/Engineering%20Practice/Foundations/Principles.md) at revision `b25e9c950fd87715d12f76b69bb2079c3a4fc054`. Knowledge Islands Principal owns this canonical engineering knowledge; the original source revision remains evidence.
