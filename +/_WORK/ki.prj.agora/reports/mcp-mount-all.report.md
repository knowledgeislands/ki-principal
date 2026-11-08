# KI > Techne > Agora › mcp-mount-all

**🤖 → 👤 Handoff to supervisor · Run report at 04:17 GMT · last mark 00:04 GMT · blocked**

---

## New and noteworthy

The shared mount is built, tested and pushed. However, the live store refuses every write. The store repository has its own Markdown commit check (rumdl, a Markdown linter, run by its pre-commit hook), and it rejects every Agora message file. They have no blank line after the front matter, no level-one heading, and no final newline. Getting past it would mean bypassing the hook, which the rules forbid. Mounting a server whose writes always fail, for every agent, would do harm: each failed write also leaves a staged file that blocks all later writes. So I stopped before mounting.

**How an agent uses it (once mounted).** One shared `agora` server sits behind the mcporter bridge on each Mac, so every agent sees `agora__send`, `agora__inbox`, `agora__ack` and the rest. Because the mount is shared, an agent names itself on every write: `send` takes `from` (its own work id, such as `ki.prj.agora`), `to`, `territory` (such as `KI`), `kind` and `body`. It previews by default and writes only with `dry_run: false`. To read its mail it calls `inbox` with its own `work_id` and territory. It then calls `ack` or `reply` with `from` set to that same id. The rig (`sol` or `terra`) is filled in from the host name. The store trusts its owner: `from` is a claim, not a proof, as for `messages.md` today.

## Done

- Step 1, shared mount: **passed**. mcp-agora `3012cf3`, pushed. `MCP_AGORA_WORK_ID` is now optional. Without it, `send`, `reply`, `ack` and `presence` (and `harvest` when it writes) require `from`, validated as `<territory>.<level>.<name>`. `inbox` and `wait` already take the recipient's `work_id`. `MCP_AGORA_RIG` defaults to the short host name. A leading `~/` in `MCP_AGORA_STORE` expands on the server, because the chezmoi inventory expands only `args`, not `env`. The README and the tool descriptions state the trust model. `bun run check` passed, with 25 tests (5 new: work-id rules, config defaults, shared and fixed senders, and the advertised required `from`).
- Step 2, live test on sol in local mode: **failed at `send`**. The tool returned the store's rumdl rejection (rules MD071, MD041 and MD047). The commit-message hook (`ki git check-message`) accepts Agora's commit messages, so the Markdown check is the only blocker. `inbox` and `audit` worked, and returned nothing. `ack` was not reached. Nothing reached GitHub. I unstaged and removed my one failed message file, and the store clone is clean and level with `origin/main`. Remote mode was not tried.
- Step 3, mount for all agents: **stopped, not started**. The chezmoi inventory is unchanged. One finding for when it resumes: a `lifecycle: ephemeral` server is left out of the bridge's tool list, so marking `agora` that way would hide it from agents. The plan is the default keep-alive. That is safe once the store path exists on the machine, because the server fails at start only when its configuration is invalid.
- Step 4, terra: **stopped, not started**.

## In Progress

Nothing running. Steps 2 to 4 resume once Query MOUNT-1 is answered.

## Queries

### MOUNT-1 - Let Agora messages past the store's Markdown check

**Context:** `ki-agora-beacon` uses the standard KI pre-commit hook, which runs rumdl on every staged Markdown file. Agora message files and roster files are data with YAML front matter, not documents, and STORE.md requires each body to be kept exactly as sent. So the server cannot reshape them to suit the linter. This run may not change the store except through the MCP, and may not bypass hooks.

**Query:** How should the store's Markdown check treat `messages/` and `roster/`?

**Options:**

a) (recommended, confidence high - the files are machine-written data whose exact bytes are the contract) Add `messages` and `roster` to the `exclude` list in the store's `.rumdl.toml`, as one reviewed commit in `ki-agora-beacon`. Then rerun this run from step 2.

b) Make the server write lint-clean files: a blank line after the front matter, a heading and a final newline. That changes the STORE.md contract and the stored bytes of every body.

c) Change the store's hook to skip those folders. The hook is a byte-exact copy that `ki-repo` checks (HOOK-4), so it would show up as drift.

### MOUNT-2 - Clean up after a failed commit on a shared mount

**Context:** When a local write's commit fails, mcp-agora leaves its new file staged "for reconciliation", as its README says. On a mount that every agent shares, that one staged file blocks every later write by every agent until someone removes it by hand. That is what happened here, and I cleaned it up myself.

**Query:** Should mcp-agora remove its own just-written, uncommitted files when the commit step itself fails?

**Options:**

a) (recommended, confidence medium - nothing has been committed or published at that point, so nothing is lost, and one bad write no longer blocks every agent) Yes. Unstage and delete only the files that operation created, and keep today's behaviour for failures after the commit (push races and replay).

b) No. Keep failed writes visible and document the manual cleanup.

🧵 ki.prj.agora
