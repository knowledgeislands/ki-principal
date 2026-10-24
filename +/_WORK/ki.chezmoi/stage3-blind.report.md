# Targeted Rig apply follow-up › stage3-blind

**🤖 → 👤 Handoff to supervisor · Run report at 00:55 BST**

---

## Done

Reviewed both adapters and [KI-TOOL-RIG-CORE-069](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-069-dynamic-type-handler-fallback.md) at tools-rig `87fa261`; no repository changes or commits.

Native read-only handler check: `.sh` and `.zsh` resolve to declared, non-dynamic types and both retain Ghostty.

Read-only listener check: no TCP or UDP port-5900 rows were present in the current snapshot.

Repository checks: both working trees remain clean; no apply, sudo, remote operation or service change was run.

Report structure and local evidence links checked; implementation tests and doctor were not run.

## In Progress

Nothing is running. Firewall remediation remains with its held work stream; loaded kernel rules were not inspected or verified.

## Queries

### HANDLER-NEXT — Choose the manual Finder workaround

**Context:** The adapter accepts the native setter's success, then fails because immediate observation still differs; its confirmation wording is a generic suggestion, not detection of a dialog. See the [bridge](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/src/rig/29-default-applications.bash:14) and [read-back check](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/src/rig/29-default-applications.bash:171).

The native types are `public.shell-script` and `public.zsh-script`, whereas the existing record targets a dynamic TOML type and documents an earlier setter error of `-50`; a common root cause is unproved.

Safety: use trusted inert files and Get Info without opening them; Ghostty can execute scripts. Change All changes the content-type association globally, potentially covering other extensions sharing that type. Neither a successful Finder change nor a disappearing apply-failure finding establishes that the adapter defect is fixed.

**Query:** Should the owner set each handler to Zed through Finder, then rerun doctor?

**Options:**

a) (recommended, confidence medium - the native UI is a practical workaround, but success on this Mac remains untested) Use Get Info › Open with › Zed › Change All once for each type, then rerun doctor and read each handler finding; retain the declarations and record the outcome.

b) Hold both and retain them as related evidence for [KI-TOOL-RIG-CORE-069](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-069-dynamic-type-handler-fallback.md), explicitly distinguishing these declared-type ineffective assignments from its dynamic-type defect; this leaves scripts opening in Ghostty.

c) Retry attended apply only as an explicitly authorised diagnostic experiment; the existing bridge repeats registration and the same setter, with no explicit prompt handling or wait, so presence at the screen alone gives little reason to expect success.

### FIREWALL-WORDING — Investigate read-only now; keep repair held

**Context:** The [listener probe](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/src/rig/29-firewall.bash:314) takes a fresh `netstat -an` snapshot and flags declared wildcard listeners; the [observer](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/src/rig/29-firewall.bash:437) appends the exposure wording when drift reasons exist and that snapshot is non-empty.

Listeners can appear or disappear between runs without any firewall change; the current empty snapshot is consistent with the shortened wording, but cannot establish why the historical snapshot differed or whether traffic is actually reachable.

Safety: the probe does not inspect loaded pf rules or prove external reachability, and matches wildcard listeners rather than every possible non-tailnet bind. No firewall apply, reload, service toggle or network change is justified by the wording; connection-critical mutation still requires the held work's tested restore path.

**Query:** Should the wording change receive a bounded read-only check now while firewall changes remain held?

**Options:**

a) (recommended, confidence high - the wording depends on volatile listener state, not solely firewall configuration) Take the code inspection and current listener snapshot above as the initial investigation; preserve the anchor-drift finding and leave remediation held. If exact timing matters, compare contemporaneous listener snapshots under the same observation context.

b) Leave all further investigation with the held work stream; acceptable for scheduling, provided the missing exposure wording is never treated as a repaired firewall or proof of safety.
