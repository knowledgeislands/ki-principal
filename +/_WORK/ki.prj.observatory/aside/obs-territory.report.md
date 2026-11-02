# [KI](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.observatory/work.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.observatory/work.md) › obs-territory

**🤖 → 👤 Handoff to supervisor · Run report at 08:17 BST · last mark 08:17 BST · blocked**

---

## Done

- Reproduced the failure. `ki territory roots --null --territory knowledge-islands` and `ki territory audit --territory knowledge-islands` both exit 2 with "territory knowledge-islands member <https://github.com/knowledgeislands/ki-design> is not registered".
- Cause: registration. ki-principal commit a09bdfa added `ki-design` to the territory roster in `ki-principal/.ki.toml`. The checkout exists at `~/workspaces/knowledge-islands/ki-design` with a valid `.ki.toml`, but the checkout was never added to the local registry (`~/.local/state/ki/registry.toml`). `ki territory` refuses the whole territory while any member is unregistered.
- The Observatory's call is correct. It uses the right arguments and handle, it found `ki` (the exit was 2, not 127), and it reports the failure as designed. `ki` is behaving as specified. No commits, nothing pushed.
- `ki registry --repo ~/workspaces/knowledge-islands/ki-design add --dry-run` confirms that one registration would fix it. Per the brief, I have not applied it.

## In Progress

- Nothing.

## Queries

**Context:** The Knowledge Islands territory can't be observed until `ki-design` is registered on this machine. Registry changes are yours to apply. No Observatory restart is needed: the service runs `ki` on every observation, so it recovers on the next refresh.

**Query:** Shall the registration be applied?

**Options:** a) (recommended, confidence high - the dry run shows a single, clean registration) Run `ki registry --repo ~/workspaces/knowledge-islands/ki-design add`, then `ki territory audit --territory knowledge-islands` to confirm. b) Apply (a), and also capture a KI-OBSERVA record so the Observatory names the unregistered member in its message. Repository URLs aren't paths, so this wouldn't conflict with the rule against quoting paths. c) Apply (a), and also hand tools-ki a roadmap item to make `ki territory` select the registered members and only warn about the unregistered ones, instead of failing the whole territory.
