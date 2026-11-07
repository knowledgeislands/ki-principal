# ki.prj.stoa discussions

## Open

### STOA-ADAPTER - packages-stoa cannot record acceptances yet

focus: _emerging

**Context:** The release run found everything ready for 0.32.0: tests, typecheck and lint pass, and in the workbench the Command K palette and all 44 new icons work. It stopped before releasing because `ki-accept` refuses to close [STOA-CMD-001](/Users/krisbrown/kis/knowledge-islands/packages-stoa/docs/roadmap/STOA-CMD-001-command-k-palette.md). `packages-stoa` has no `.ki.toml`, the file that tells KI tools how a repository keeps its work records, and it has never had one. Adding that file also declares the whole repository conformant with the KI repository standard. That brings it under the repository audits and may surface further work. The record is otherwise ready to accept, and nothing was committed or pushed.

**Query:** Release 0.32.0 now and accept STOA-CMD-001 later, or declare the repository first and do both together?

**Options:**

a) (recommended, confidence medium - the sites are waiting on the release, the acceptance is only bookkeeping, and the declaration is a wider change than this release) Release 0.32.0 now with STOA-CMD-001 left awaiting review. A separate run then adds the `.ki.toml` declaration and accepts STOA-CMD-001 once it lands.

b) First a short run adds `.ki.toml` with the roadmap declared and checks the audit. Then the release brief reruns unchanged, accepting and releasing together. This is what the release run recommended, but the release waits on whatever the audit turns up.

c) Waive the check for this one closure and mark STOA-CMD-001 done by hand before releasing. The skill allows no fallback, so this needs your explicit words.

## Parked

None
