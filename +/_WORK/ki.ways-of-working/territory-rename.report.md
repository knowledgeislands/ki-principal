# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › territory-rename

**🤖 → 🧑 Handoff to supervisor · Run report at 11:43 BST · last mark 11:06 BST**

---

## Done

- Precondition met: `ki` 0.11.2 is installed, and the installed harness provides `ki-coordination`, `ki-work-design` and `ki-work-folder`.
- Every one of the seven repositories declared `[skills.ki-pmo]` and `[skills.ki-checkpoint]`. None declared `[skills.ki-pmo-design]`, and none has `.github/ki-version`, so I had no version bump to make.
- er-principal: `.ki.toml` renamed, repair healthy, commit `a86f32f` through the gate, pushed fast-forward.
- hnr-principal: `.ki.toml` renamed, repair healthy, commit `11538f2` through the gate, pushed fast-forward.
- legal-principal: `.ki.toml` renamed, repair healthy, commit `31f72086` through the gate, pushed fast-forward.
- si-principal (`/Users/krisbrown/workspaces/sacred-inquiry/si-principal`): `.ki.toml` renamed, repair healthy, commit `6afe662` through the gate, pushed fast-forward.
- tmx-principal: `.ki.toml` renamed, repair healthy, commit `416dd0e` through the gate, pushed fast-forward.
- va-principal: `.ki.toml` renamed, repair healthy, commit `9158b4d` through the gate, pushed fast-forward.
- personal-principal: `.ki.toml` renamed, repair healthy, commit `6824c941` through the gate, pushed fast-forward.
- Each commit changes only `.ki.toml`. Repair also relinked the gitignored `.claude/skills` and `.agents/skills` projections (it added `ki-coordination` and `ki-work-folder` and removed the dangling `ki-checkpoint`), but those are untracked, so no other file changed.
- Every repository was clean and level with origin before I started and is level after pushing. No other session's commits or dirty files were involved.
- Records: I opened none and closed none. The net change in open records is 0 in each of the seven repositories.
- Report path: the progress protocol makes this state file the only report path, so I wrote no copy to the work folder and made no ki-principal commit.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- `/Users/krisbrown/workspaces/personal/acquire/.ki.toml` still declares `[skills.ki-checkpoint]` (line 89). It is outside the seven authorised repositories, so I left it untouched.

## Queries

### ACQUIRE-RENAME - Rename the old skill name in acquire

**Context:** The acquire repository still declares `[skills.ki-checkpoint]`, which the 0.11.2 harness no longer provides under that name. This brief did not authorise acquire, so I did not touch it. It needs the same one-line rename, a repair, and a commit and push.

**Query:** Should acquire get the same rename in a follow-up run?

**Options:**
a) (recommended, confidence high - the same mechanical rename has just passed in seven repositories) Authorise a short follow-up run to rename it to `[skills.ki-work-folder]`, repair, commit and push, under the same rules.
b) Leave acquire as it is until its own owner session picks it up.
