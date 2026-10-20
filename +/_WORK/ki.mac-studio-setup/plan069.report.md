# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [Mac Studio setup](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/mac-studio-setup.md) › plan069

**🤖 → 👤 Handoff to supervisor · Run report at 01:43 BST · last mark 23:36 BST on 19 October**

---

## Done

- I shaped [KI-TOOL-RIG-CORE-069](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-069-dynamic-type-handler-fallback.md) in place and left it at **draft**. Ready can't honestly be reached yet: only a live handler change can show which native setter accepts a dynamic type. It is committed locally on `main` as `6e060d0` and not pushed.
- Diagnosis, from read-only checks on `sol`:
  - The bridge converts `toml` with a null conforming type and gets `dyn.age81k55rru`. `UTType` and `NSWorkspace` get a different identifier, `dyn.ah62d4rv4ge81k55rru` (conforming to `public.data`). Declared types such as `md`, `yaml` and `json` get the same identifier both ways.
  - Warp holds `toml` only through its extension claim; there is no stored handler entry for it.
  - The `NSWorkspace` setter exists, and the bridge can reach `UTType`. JXA can wait on a main-queue completion.
  - The -50 cause is still unproved.
- Plan: step 1 is an attended probe for Kris. It is a script in the record's Discussion that tries the three candidate setters in order, with a restore path back to Warp. Steps 2 to 7 then cover:
  - choosing the route
  - one identifier for both observe and apply
  - the named detail `undeclared-content-type` when assignment still fails
  - fixture tests
  - amendments to RIG-ORCH-044 and RIG-STATE-044, and the guide
  - the full gate
- I ran the probe's `observe` rung read-only and it works.
- Checks:
  - `git diff --check` passed.
  - `ki repo audit --repo .` shows no failures. Its warnings were already there before this run: rumdl template drift, Claude Desktop binding, and `size` missing on other records.
  - The pre-commit hook's 600 Bats tests passed.
- No handler, `duti`, apply or other live change was made, and no other session's changes were present.

## In Progress

Nothing is running. Delivery is blocked on the attended probe.

## Queries

### RIG-069-PROBE - Run the attended handler probe on sol

**Context:** Read-only observation narrowed the fault to the dynamic identifier. Choosing between the Launch Services setter on the `UTType` identifier and the asynchronous `NSWorkspace` setter needs one real assignment, and so does confirming the -50 cause. The probe sets `toml` to Zed, which is what the owner declared. Its restore path is to rerun the rung that worked with `/Applications/Warp.app dev.warp.Warp-Stable`; Finder's Get Info › Change All is the manual fallback.

**Query:** Will Kris run the step 1 probe in [KI-TOOL-RIG-CORE-069](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-069-dynamic-type-handler-fallback.md) on `sol`, record each rung's output in the record, and then approve Ready?

**Options:**

a) (recommended, confidence high - this is the only honest way to settle the route, and the change it makes is the declared intent with a simple restore) Kris runs the rungs `legacy`, `modern` and `workspace` in that order with `observe` after each, and stops at the first that makes Zed effective. The record then moves to Ready with step 2's route fixed.

b) Approve Ready now and have the implementation try both routes in code, with the probe deferred to the post-release carry. The record keeps more speculative bridge code, and the -50 cause stays unproved until the carry.

### 🤖 → 👤 Handoff to supervisor · since 01:43 BST

👤 1 with you · 🅿️ 0 parked

- [with you] RIG-069-PROBE attended handler probe · supervisor of ki.mac-studio-setup · since 01:43 BST
