# [Model](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › launcher-reports

**🤖 → 👤 Handoff to supervisor · Run report at 16:36 GMT · last mark 15:24 GMT**

---

## Done

- **Fix 1, where reports go.** The launcher now puts each finished run's report next to its brief. If the brief sits in a focus folder (`+/_WORK/<id>/<focus>/`), the report goes there. Otherwise it goes in `+/_WORK/<id>/reports/`. It never goes at the top level any more. The launcher remembers where the brief was even when the run is queued. Everything that looks for reports now checks the focus folder, then `reports/`, then the old top level: the TAG lookup in `decide`, the checks for a name already in use and for a relaunch, the reviewer evidence check, the queries the launcher reads from a report, and the moving-in of reports during `decide` and `close`.
- **Fix 2, `close` and bad homes.** Before moving anything, `ki agent close` now refuses a run whose home is a relative path, has disappeared, or is not inside a registered repository. Nothing ever follows a relative home through the registry, and the launcher no longer homes a report into a home that is relative or gone. That is how the stray `legal/legal-principal/+/_WORK/lgl/` tree ended up inside ki-principal. I found no copy of that tree today.
- **Fix 3, moved run groups.** If a run group's control record still points at a work home that no longer exists after a repository move, `ki agent home <run> --work <id>` now moves the record to the new home and says so. It only does this for a record made on the same machine for the same work, so the machine check still applies, and earlier attempts stay valid under the old home. The `control-home-unverified` error now gives both the stored and current home as well as both machines, and says how to fix it.
- **Tests and documents.** New tests cover a brief in a focus folder, a brief elsewhere, a queued brief, the name-in-use and relaunch checks in a focus folder, the TAG lookup in all three places, `close` refusing a relative, gone or unregistered home without moving anything, and the control-record move, including refusal for another machine and for an old home that still exists. I updated the existing tests to the new places and updated the man page, the command inventory, the user guide and the changelog.
- **Commit and checks.** One commit, `2a2eab2a fix(agent): home reports beside their brief and guard moved homes`, with the `Host: sol` and co-author trailers, now on `main`. Full test suite: passed, 2179 of 2179. Type check: passed. Biome lint: passed. Man page lint: passed. Commit gate: passed.
- **The installed `ki` on sol already runs this fix.** `~/.local/bin/ki` comes before the Homebrew copy on the PATH, and it is a small script that runs `bun` on the main checkout's `src/main.ts`. So the fix took effect when `main` moved forward, and Kris doesn't need to install anything. The Homebrew `/opt/homebrew/bin/ki` is a release copy and still has the old behaviour, but it only runs if the PATH order changes.
- **Reports still at the top level (not moved), 16:36 GMT.** There are 36 in total, not the roughly 385 that personal.reg.assistant-terra reported. Most have already been moved into focus folders. Three of the four ki-principal ones were written today by the old launcher, before this fix.

| Repository | Work (steward) | Top-level reports |
| --- | --- | --- |
| personal/personal-principal | `personal.reg.tower` | 32 |
| knowledge-islands/ki-principal | `ki.prj.ways-of-working` | 2 |
| knowledge-islands/ki-principal | `ki.prj.observatory` | 1 |
| knowledge-islands/ki-principal | `ki.prj.mac-studio-setup` | 1 |

There are none in the other `kis` repositories, the `workspaces/git` repositories or chezmoi. One report also sits in a `reports/` folder: `kb.regular.site-tower`, in personal-principal. That place is still allowed during the transition.

## In Progress

- The `ki-prj-ways-of-working` run group still refuses launches until its control record is moved. See CONTROL-REHOME.
- Known gap: the reviewer evidence check for an attempt launched *before* a repository move still looks for the report under the old home path.

## Queries

### CONTROL-REHOME - Move the ki-prj-ways-of-working control record now

**Context**

The fix is live, but I did not run it on the live run group. That record belongs to other runs, and the brief told me not to edit control files. The group's control record still points at `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working`. That path no longer exists. The run's home (`thread.json`) already points at the new `/Users/krisbrown/kis/...` home.

**Query**

Who should run `ki agent home ki-prj-ways-of-working --work ki.prj.ways-of-working` so launches in that group work again?

**Options**

a) (recommended, confidence high - the command checks the machine and the work, refuses if the old home still exists, and moves no files) The coordinator runs it once, before the next launch in that group.

b) Kris runs it at the terminal.

c) Leave the record as it is and keep launching in the separate `ki-project-ways-of-working` group.

### 🤖 → 👤 Handoff to supervisor · since 16:36 GMT

👤 1 with you

- [with you] move the ki-prj-ways-of-working control record (CONTROL-REHOME) · 👤 · since 16:36 GMT

🧵 ki.prj.ways-of-working
