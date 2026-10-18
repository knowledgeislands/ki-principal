---
note_type: admin/governance/decision
id: GDR-KI-PRINCIPAL-012
title: 'Official, not canon'
date: 2026-10-18
updated: 2026-10-18
status: current
decision_type_url: https://knowledgeislands.info/specifications/decision-records/gdr
decision_type: governance
decision_depends_on: ['SDR-KI-PRINCIPAL-004', 'GDR-KI-PRINCIPAL-010', 'GDR-KI-PRINCIPAL-011']
---

# GDR-KI-PRINCIPAL-012: Official, not canon

## Context

Symbols, terms and other items in Knowledge Islands carry a status word saying how settled they are. The words in use were _canon_, _decided_ and _proposed_, with open questions listed separately, and [[GDR-KI-PRINCIPAL-010-the-port|GDR-KI-PRINCIPAL-010]] asked for items to be marked "as canon". "Canon" confused readers as a label. [GDR-KI-DESIGN-002](https://github.com/knowledgeislands/ki-design/blob/7db751f405d17a09790150aec9a7de6d4966f6a0/docs/decisions/GDR-KI-DESIGN-002-status-labels.md) in `ki-design` renamed the design system's labels to Official · Agreed · Proposed · Open.

On 2026-10-18 Kris asked for the change to reach the official terminology as well, and confirmed that "canonical knowledge" stays the term for ratified knowledge. Under [[SDR-KI-PRINCIPAL-004-the-enactment-process|SDR-KI-PRINCIPAL-004]] his explicit instruction for this bounded change is the ratification.

## Decision

**The status label for a symbol, term or other item is one of Official · Agreed · Proposed · Open, always in that order.** It matches GDR-KI-DESIGN-002:

- **Official** - ratified in Knowledge Islands Principal. Formerly _canon_.
- **Agreed** - agreed with the owner and being enacted into Knowledge Islands Principal. Formerly _decided_.
- **Proposed** - usable in drafts, never presented as settled.
- **Open** - a question still to answer.

**"Canonical knowledge" remains the Knowledge Islands term for ratified knowledge.** Knowledge that has passed the Enactment Process into Pillars or Resources is canonical knowledge, and wording such as "canonical content" and "the canonical record" is unchanged. Technical uses of "canonical" - a canonical repository, URL or identity - are unaffected.

## Consequences

- A status cell, chip or label says Official or Agreed, never canon or decided.
- [[GDR-KI-PRINCIPAL-010-the-port|GDR-KI-PRINCIPAL-010]] asks for its symbols to be marked as official.
- Roadmap records keep the wording they were written with, as a historical record.

## References

- [GDR-KI-DESIGN-002](https://github.com/knowledgeislands/ki-design/blob/7db751f405d17a09790150aec9a7de6d4966f6a0/docs/decisions/GDR-KI-DESIGN-002-status-labels.md) - the design-system status labels this record matches.
- [[SDR-KI-PRINCIPAL-004-the-enactment-process|SDR-KI-PRINCIPAL-004]] - an explicit owner instruction for a bounded change stands in for a proposal.
- [[GDR-KI-PRINCIPAL-010-the-port|GDR-KI-PRINCIPAL-010]] and [[GDR-KI-PRINCIPAL-011-the-capital|GDR-KI-PRINCIPAL-011]] - the symbol decisions whose status wording this record settles.
