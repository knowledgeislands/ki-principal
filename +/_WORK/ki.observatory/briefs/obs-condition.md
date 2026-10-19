# obs-condition - Handoffs for island maturity and decline

This run is for KI > Model > Observatory (`ki.observatory`), under the cross-repository choreography in ki-principal `AGENTS.md`. On 2026-10-19 Kris decided (CONDITION-TOML in ki-principal `+/_WORK/ki.observatory/decisions.md`) that each island declares its maturity in its `.ki.toml`, from a fixed scale the ki-repo standard defines, and that decline or ruin comes from `ki repo audit` health. The Observatory reads both through `ki` rather than inventing them.

1. In ki-agentic-harness, add one roadmap record under `ki-work-roadmap` for work another repository must deliver. It should cover the ki-repo standard defining the maturity scale and the `.ki.toml` key, and the audit criterion that checks the key. Draft the scale from Kris's words, quoted in the decisions entry STEP3-ANSWERS: an island's level of development, such as settled or thriving. Mark the scale's names as a proposal for Kris.
2. In tools-ki, add one roadmap record for `ki` to expose each island's declared maturity and its audit-derived health, so the Observatory can read them, for example through `ki work status` or a territory view. Make it depend on the harness record.
3. Link both records to KI-OBSERVA-BCN-008 and KI-OBSERVA-VIS-030 in apps-observatory.local. Edit nothing in apps-observatory.local, because run obs-accept is editing it.
4. Follow each repository's own conventions and checks. Commit by explicit path under `ki-git`, and do not push.

Report in owner-report shape, kept short: Done gives both records with their links. Queries: the proposed scale names for Kris, with lettered options, the recommended one first with its confidence.
