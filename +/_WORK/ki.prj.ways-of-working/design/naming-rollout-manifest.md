# Mechanical naming rollout manifest

Owner-authorised folder-first pass on 28 October 2026. Classification uses `work.md` level and Project slug. It changes identity, parent/covers and exact current links only; no lifecycle transition, mark, owner, Project slug or historical message/run provenance changes.

## Bounded result

26 package folders renamed; five already correct; seven non-HNR main SoPs retained and renamed; HNR has an existing main and two secondary SoPs, read-only. Zero SoPs created. No destination collisions or folder deferrals. The earlier active-writer exceptions were superseded by the owner's explicit rename-now instruction.

## Old and new names

- `er` -> `er.sop.main` (rename).
- `ki` -> `ki.sop.main` (rename).
- `ki.agent-host` -> `ki.prj.agent-host` (rename).
- `ki.baseline-rollout` -> `ki.prj.baseline-rollout` (rename).
- `ki.chezmoi` -> `ki.prj.chezmoi` (rename).
- `ki.estate-factorisation` -> `ki.prj.estate-factorisation` (rename).
- `ki.knowledge-acquisition` -> `ki.prj.knowledge-acquisition` (rename).
- `ki.mac-studio-setup` -> `ki.prj.mac-studio-setup` (rename).
- `ki.observatory` -> `ki.prj.observatory` (rename).
- `ki.paperclip-capture-and-rebuild` -> `ki.prj.paperclip-capture-and-rebuild` (rename).
- `ki.portable-specifications` -> `ki.prj.portable-specifications` (rename).
- `ki.regular` -> `ki.regular.main` (rename).
- `ki.timelines` -> `ki.prj.timelines` (rename).
- `ki.tools-burndown` -> `ki.prj.tools-burndown` (rename).
- `ki.ways-of-working` -> `ki.prj.ways-of-working` (rename).
- `ki.website` -> `ki.prj.website` (rename).
- `lgl` -> `lgl.sop.main` (rename).
- `personal.regular.acquire-intake` -> `personal.regular.acquire-intake` (already correct).
- `personal` -> `personal.sop.main` (rename).
- `personal.family-and-friends` -> `personal.prj.family-and-friends` (rename).
- `personal.personal-health` -> `personal.prj.personal-health` (rename).
- `personal.regular.rig` -> `personal.regular.rig` (already correct).
- `personal.regular.rig-sol` -> `personal.regular.rig-sol` (already correct).
- `personal.regular.rig-terra` -> `personal.regular.rig-terra` (already correct).
- `personal.regular.tower` -> `personal.regular.tower` (already correct).
- `si` -> `si.sop.main` (rename).
- `tmx` -> `tmx.sop.main` (rename).
- `va` -> `va.sop.main` (rename).
- `va.community-website` -> `va.prj.community-website` (rename).
- `va.knowledge-intake` -> `va.prj.knowledge-intake` (rename).
- `va.markhowarth-launch` -> `va.prj.markhowarth-launch` (rename).

## Continuity and rollback

All rename paths are enumerated from the pre-move tracked index, with each old/new file staged explicitly. Existing tracked non-Markdown design artifacts move unchanged, including scripts and diagrams; moving them does not change runtime behaviour. Historical report/design/message bodies are retained. Only current five-file identity headings/front matter and live work/state/query references are updated.

122 private untracked reports moved physically with Ways of working; their byte snapshots remain outside Git and all SHA-256 checks pass. Their private path/hash manifest is deliberately excluded from this tracked note. Aggregate verification digest: `d975c5cad5b6374438eef90398022ee951b557fe60c2eb6c317b7334591dbb8c`.

The actual `ki agent home ways-of-working --work ki.prj.ways-of-working --repo <Principal>` setter succeeded; read-back resolves the new folder. Other recorded mutable homes follow the same exact mapping. Immutable launch identities, native UUIDs and runtime directory names remain unchanged. The old names remain in immutable provenance.

Rollback is a compensating explicit-path rename and identity/reference commit, after checking for intervening writers and new inbox lines. Restore the prior mutable thread-home pointer through `ki agent home`; never reset shared history or rewrite immutable launch records. Prior tracked bytes remain recoverable from each migration commit's first parent; private bytes remain in the moved folder and the external snapshot.

## Coverage limits

The bounded scan resolves only exact declared `territory_members` against the local registry. Personal trip, Legal site and Techmedix archived site identities have no exact registered checkout here; do not guess paths. HNR roots and refs are never fetched or written. The review area contains only the harness README; no review packages or legacy checkpoint/thread SoPs were found in resolved roots. A leftover `ki.specifications` directory has no `work.md` and is not a package.

The second bounded naming sweep completed at 22:14:40 GMT (at least ten minutes after the owner steer): all 31 non-HNR packages have canonical names, with zero new or remaining stragglers. Mandatory commit hooks and focused preservation checks are used; unrelated estate-wide repairs remain out of scope.
