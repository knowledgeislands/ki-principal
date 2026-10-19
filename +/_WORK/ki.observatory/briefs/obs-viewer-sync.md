# obs-viewer-sync - Saved diagram viewers kept in sync, and the maturity scale

This run is for KI > Model > Observatory (`ki.observatory`) in ki-agentic-harness. Kris's words are in ki-principal `+/_WORK/ki.observatory/decisions.md` under OVERLAY-SYNC and MATURITY-FOUR. The evidence is in `~/.local/state/ki/agents/observatory/obs-overlay-review.report.md`.

1. OVERLAY-SYNC: add one roadmap record under `ki-work-roadmap` for keeping saved Archify viewers in sync mechanically.
   - Rendering writes each saved HTML viewer together with a portable receipt of the source hash, the HTML hash and the renderer's identity.
   - `ki repo audit` and the staged-snapshot commit check fail when a receipt is missing or doesn't match.
   - Keep `last_checked` for its separate question: whether the diagram still describes its traced code.
   - Cover the 12 manifest entries in the harness, and note the 5G Emerge phase 2 and 3 sites as later adopters. Phase 2 already has receipts with hashes.
   - If tools-ki needs a matching `ki` change, name it in the record as a dependency; don't write in tools-ki.
2. MATURITY-FOUR: update KI-HARNESS-GOV-223 so the maturity scale is `founding`, `growing`, `settled`, `thriving` as Kris decided, and is no longer marked as a proposal.
3. Run the repository's checks and `ki repo audit --skill ki-work-roadmap`. Commit by explicit path under `ki-git`, and do not push.

Report in owner-report shape, kept short: Done gives the new record with its link and the GOV-223 change. Queries holds only what needs Kris.
