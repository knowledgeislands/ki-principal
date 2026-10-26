---
areas: { ECO: 14, EXT: 3, GOV: 35, MOD: 11, OPS: 14 }
---

# Roadmap issue ledger

This ledger reserves fixed issuing-area namespaces. Allocate the next work item in its area as one greater than that area's high-water mark; never lower a value or reuse an issued number after a record is pruned. Reserve a number by committing this ledger's advance on its own before writing the record. Areas are not mutable themes or groups.

- `ECO` reserves through `014`.
- `EXT` reserves through `003`.
- `GOV` reserves through `035`.
- `MOD` reserves through `011`.
- `OPS` reserves through `014`.
