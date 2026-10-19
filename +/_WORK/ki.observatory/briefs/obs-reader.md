# obs-reader - The Observatory reads both work-folder shapes

Run `obs-reader` for KI > Model > Observatory (`ki.observatory`), working in apps-observatory.local. Routed from KI > Model > Ways of working as WORK-PACKAGE-READER under the [work-package standard](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/work-package.md#migration), point 36.

1. Read that standard's Migration section and the `ki-work-package` skill. Find the existing roadmap record in apps-observatory.local that best covers the Observatory reading work folders (look first at KI-OBSERVA-VIS-025, KI-OBSERVA-VIS-026, KI-OBSERVA-VIS-037 and KI-OBSERVA-BCN-007) and fold this scope into it under `ki-plan`; open no new record.
2. Make the Observatory read both shapes: the five-file work package (`work.md` definition plus `state.md`, `queries.md`, `messages.md`, `decisions.md`) and the single-file work folder whose `work.md` carries state. Prefer `ki work status` where tools-ki exposes it; otherwise read the files, leaving a clear seam for `ki work status` later.
3. Move `review.ts`'s dating of review-held folders from `work.md` to `state.md` where `state.md` exists, falling back to `work.md`.
4. Confirm the Work Instrument shows a migrated folder, such as ki-principal's `+/_WORK/ki.observatory/`, unchanged from how it showed before migration; a test fixture of each shape is the evidence.
5. Verify under the repository's declared checks (`bun run` scripts), commit by explicit path in apps-observatory.local under `ki-git`, leave the record Awaiting review, and do not push. Touch no other repository and no file in ki-principal. Do not restart the Observatory service.

Report in owner-report shape, kept short: Done gives the record, what changed and the check results; say plainly whether the Work Instrument confirmation (item 4) holds, since KI > Model > Ways of working is blocked on it; Queries holds anything needing Kris, lettered options with the recommended one first and its confidence.
