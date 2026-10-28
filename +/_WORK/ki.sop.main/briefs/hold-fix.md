# hold-fix: give four on-hold packages a valid hold block

Authority: mechanical front-matter repair in ki-principal work packages covered by ki.sop.main; no other change. Kris pasted the `ki` warnings on 28 October for this to be dealt with.

`ki` warns "hold.reason must be paused or more-expected while on hold" for:

- `+/_WORK/ki.prj.baseline-rollout/state.md`
- `+/_WORK/ki.prj.mac-studio-setup/state.md`
- `+/_WORK/ki.prj.portable-specifications/state.md`
- `+/_WORK/ki.prj.timelines/state.md`

Each has `state: on-hold` and no `hold:` block. For each:

1. Read the body (`## Now`, next steps) to judge whether the hold is a plain pause or "more expected". Default `paused`.
2. Insert directly after `state: on-hold`, matching `+/_WORK/ki.prj.observatory/state.md`:

   ```text
   hold:
     reason: paused
     release: Kris says resume
   ```

   Use a release the body states, if it states one; otherwise `Kris says resume`. Change nothing else.
3. Check every other `+/_WORK/*/state.md` with `state: on-hold` the same way and fix those too, naming each in the report.
4. Confirm the warnings are gone (`ki agent prompts >/dev/null` in ki-principal prints them).
5. Commit by explicit path only, subject `docs(work): ki.sop.main hold-fix, valid hold blocks`, ending `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. Fetch, pull fast-forward only and push fast-forward only; never force or `--no-verify`, and stop on divergence. Leave any other session's uncommitted file alone and name it.

Report to `/Users/krisbrown/.local/state/ki/agents/ki-sop-main/hold-fix.report.md` in owner-report form: Done (each package with the reason and release chosen), In Progress, Queries (or "No outstanding queries").
