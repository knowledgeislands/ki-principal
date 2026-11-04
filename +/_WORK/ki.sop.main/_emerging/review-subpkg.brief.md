# review-subpkg (blind review)

Independent review: you have not seen anyone's recommendation; give your own. Do not read any `discussions.md`, `decisions.md` or `*.report.md` in a `+/_WORK/` folder.

## SUB-PACKAGE-COVERS - Whether a sub-package belongs in the main State of play's register

**Context:** I wrote that a sub-package names its parent package as `parent` and stays out of every State of play's `covers` register, because its parent is already listed there. The model note says nothing about coverage. Both audits now enforce this: a sub-package whose `parent` names anything other than its parent package fails.

**Query:** Should a sub-package stay out of the main State of play's `covers` register?

**Options (unranked):**

- List it in the main State of play's `covers` as well, so the register shows every live package, and relax the rule that a package under a State of play must be listed there.

- Keep it out of `covers`; the parent package answers for it.

Give your choice, confidence and a two-line reason. Read-only; no commits. Write it as your run report.
