# GRANOLA-CHECKPOINT options

**Context:** KI-TOOL-KI-CLI-166 (/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-166-granola-acquired-folder-alone.md) made routine `ki acquire import --adapter granola` skip every meeting in the Acquired folder on membership alone, with no ledger lookup. Each import still runs `verifyGranolaCheckpoint`, which checks the document of every ledger entry. If a marked meeting's entry is still `staged` or `awaiting-review` and its staged capture was removed from the receiver without a disposition, the import stops, though the skip no longer reads the ledger.

**Query:** Should Acquired members also be exempt from this whole-ledger check?

a) Keep the check as it is, noted as an outstanding concern in the record. b) Exempt Acquired members from the check in a follow-up record, so membership overrides local evidence everywhere. c) Decide when accepting KI-TOOL-KI-CLI-166.
