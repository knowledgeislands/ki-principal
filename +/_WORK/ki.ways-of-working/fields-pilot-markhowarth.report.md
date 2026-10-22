# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › fields-pilot-markhowarth

**🤖 → 👤 Handoff to supervisor · Run report at 14:06 BST · last mark 13:37 BST**

---

## Done

The field migration pilot in apps-markhowarth.com is finished and pushed. All four open records had one mechanical fix: the retired `horizon: triage`. None named `initiative`, and none had a theme beside a Project. I made no kind or size proposals. The repository has no closed records.

- [VA-MARK-001](/Users/krisbrown/workspaces/valle-armonia/apps-markhowarth.com/docs/roadmap/VA-MARK-001-agree-site-identity.md) Agree site identity: before `status: draft`, `horizon: triage`, `theme: design`; after `status: triage` with no horizon, `theme: design` unchanged, `updated_at` advanced.
- [VA-MARK-002](/Users/krisbrown/workspaces/valle-armonia/apps-markhowarth.com/docs/roadmap/VA-MARK-002-decide-home-page.md) Decide home page: same before and after as VA-MARK-001.
- [VA-MARK-003](/Users/krisbrown/workspaces/valle-armonia/apps-markhowarth.com/docs/roadmap/VA-MARK-003-review-story-navigation.md) Review story navigation: same before and after as VA-MARK-001.
- [VA-MARK-004](/Users/krisbrown/workspaces/valle-armonia/apps-markhowarth.com/docs/roadmap/VA-MARK-004-agree-launch-arrangements.md) Agree launch arrangements: before `status: draft`, `horizon: triage`, `theme: launch`; after `status: triage` with no horizon, `theme: launch` unchanged, `updated_at` advanced.
- Method: `ki repo roadmap migrate --repo .` (ki 0.11.4) as a dry run. Its preview matched the standard's mechanical rule exactly, so I ran it again with `--apply`. I made no hand edits.
- Commit `41818bb` (chore(roadmap)), staged by explicit path, passed the lint-staged gate. It was the only commit stacked on `origin/main` and was pushed fast-forward; the branch is now level.
- `ki repo audit` before: failed, with 4 failures (one retired horizon per record) and 7 warnings.
- `ki repo audit` after: passes with 0 failures and 7 warnings. Four warnings are the expected missing `size` on each record, which waits for the ki release. Three were there before and are outside this run: no committed pre-commit gate, the `_ISSUES.md` ledger body in a superseded form, and the Capital's Project registry being unavailable.
- `bun run test`: passed before and after.
- `bun run self:typecheck`: passed before and after.
- Net record count in apps-markhowarth.com: 0 (4 records before and after).

For the later runs (personal-principal, hnr-principal, 5g-emerge-phase2, legal-principal):

- Use `ki repo roadmap migrate` in place of hand edits. It does the horizon and `waiting_on_trades` moves, but it never touches `theme`, `project` or `initiative`. Records that name `initiative`, or a theme beside a Project (personal-principal has 12 and 3), still need a separate scripted pass. Show its dry-run diff before writing.
- In these Streams Capitals, check first that `migrate` reads `Streams/Roadmap/` records. I tested only the `docs/roadmap/` adapter.
- For records moving from Waiting for or Parked to Hold, read the `hold` condition the tool writes. Any REVIEW placeholder is a gap the owner must fill, not a finished migration.
- Before applying, list each record's status beside its retired horizon. Mapping `horizon: triage` to `status: triage` takes adoption away from a draft, ready or in-progress record. Here that was four drafts (see the query below). A ready or in-progress record at that horizon should come to the owner rather than be migrated.
- Leave the pre-existing ledger and gate warnings alone, so the before-and-after audits compare only the field fixes.

## In Progress

Nothing.

## Queries

### MARK-READOPT - Whether the four VA-MARK records go back to adopted

**Context:** The standard's mechanical rule turned `horizon: triage` into `status: triage`. Before this run all four records were `status: draft`, so the owner had adopted them. Now they read as unadopted intake, and leaving triage needs the owner's approval. Each one waits on a decision from Mark.

**Query:** Should the four records stay in triage until Mark engages, or go back to adopted at once?

**Options:**

a) (recommended, confidence medium - the result is mechanical, as the standard requires, and nothing in the repository is in flight; adoption can follow through `ki-next` when Mark replies) Leave them in triage.

b) Adopt them now through `ki-next`: `status: draft`, `horizon: hold`, `hold.reason: waiting-for`, with Mark's decision as the condition.

### 🤖 → 👤 Handoff to supervisor · since 14:06 BST

👤 1 with you · 🤖 0 running · ⬆️ 0 unpushed

- [with you] MARK-READOPT · owner · since 14:06
- [pushed] apps-markhowarth.com field migration, 4 records · run/fields-pilot-markhowarth · since 14:05
