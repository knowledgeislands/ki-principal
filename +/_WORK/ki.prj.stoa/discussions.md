# ki.prj.stoa discussions

## Open

### STOA-AUDIT-REST - The rest of the audit findings

focus: _emerging

**Context:** You asked for Stoa's audit findings to be fixed. Most audits now pass. Three groups remain:

- **Decision records (293 findings).** 51 records keep the old portal-framework names (`ADR-PORTAL-FRAMEWORK-001` to `051`), and many lack standard sections. Fixing them renames ids that other repositories cite.
- **Engineering toolchain (18 findings).** Fixing these needs new development tools, renames the commands `test`, `typecheck` and `lint` that `AGENTS.md` and the sites' briefs use, and touches the vendored tree. Much of it depends on what the new package-repository skill says, which the guild now has.
- **GitHub.** Issues and Projects are switched on, though Stoa's work lives in its roadmap; the description and merge settings also differ from the standard.

**Query:** How far should the clean-up go now?

**Options:**

a) (recommended, confidence medium - it clears the safe findings now and leaves the toolchain to the skill that will define it) Switch GitHub Issues and Projects off now. Migrate the decision records to the `STOA` scope now, keeping their numbers and leaving a pointer from each old id. Adopt the toolchain once the package-repository skill settles it.

b) Do all three now, toolchain included, accepting that the command names change and the sites' briefs follow.

c) Switch GitHub off only, and turn the decision-record and engineering checks off for Stoa until the skill exists.

## Parked

None
