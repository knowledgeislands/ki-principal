---
areas: { ECO: 14, EXT: 3, GOV: 33, MOD: 9, OPS: 13 }
---

# Roadmap issue ledger

This ledger reserves fixed issuing-area namespaces. Allocate the next work item in its area as one greater than that area's high-water mark; never lower a value or reuse an issued number after a record is pruned. Reserve a number by committing this ledger's advance on its own before writing the record. Areas are not mutable themes or groups.

- `ECO` reserves through `014`.
- `EXT` reserves through `003`.
- `GOV` reserves through `033`.
- `MOD` reserves through `009`.
- `OPS` reserves through `013`.
