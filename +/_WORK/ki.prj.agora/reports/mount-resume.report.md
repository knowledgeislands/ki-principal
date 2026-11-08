# KI > Techne > Agora › mount-resume

**🤖 → 👤 Handoff to supervisor · Run report at 05:05 GMT · last mark 04:53 GMT · blocked**

---

## New and noteworthy

Agora is mounted for every agent on sol and works end to end: a live message was sent, read, acknowledged and audited through the shared mount, and both commits are on GitHub. Terra is cloned and built but not mounted. Its chezmoi checkout cannot fast-forward because another session left an uncommitted edit to `+/_WORK/personal.reg.household-sol/messages.md` there (since 01:58 GMT), and the incoming commits change that same file. I left it alone and stopped terra's mount.

Agents see nine tools, not ten. `harvest` is a destructive tool, and the mount runs at `write` access as the brief set, so the access gate hides it by design.

Terra's fresh store clone has no `core.hooksPath` set, so its commits would skip the store's rumdl and commit-message hooks. Sol's clone has it set to `.githooks`. The store's README does not say how to set it up; I left it unset.

**How an agent uses it.** One shared `agora` server sits behind the ki-mcporter bridge, so every agent sees `agora__send`, `agora__inbox`, `agora__ack`, `agora__reply`, `agora__wait`, `agora__who`, `agora__since`, `agora__audit` and `agora__presence`. Because the mount is shared, an agent names itself on every write. `send` takes `from` (its own work id, such as `ki.prj.agora`), `to`, `territory` (such as `KI`), `kind` and `body`. It previews by default and writes only with `dry_run: false`. To read its mail, an agent calls `inbox` with its own `work_id` and territory. Reading changes nothing: a message stays unread until it is acknowledged or answered. The agent then calls `ack` or `reply` with `from` set to that same id. The rig (`sol` or `terra`) comes from the host name. The store trusts its owner, so `from` is a claim, not a proof. Each write commits and pushes to the store on GitHub.

## Done

- MOUNT-1 a), store Markdown check: **passed**. ki-agora-beacon `5b85f83` excludes `messages/` and `roster/` from rumdl. The store's rumdl check passes, and the hook is untouched.
- MCP-READ a), specification: **passed**. apps-agora.local `3a909f8` drops open question 8. Section 6 already said unread means not yet acknowledged or answered; it now cites AGORA-STORE and MCP-READ, not the open questions. rumdl, `self:check` and `test` all pass.
- Step 3, chezmoi entry: **passed**. chezmoi `3ed23ae2` adds the `agora` entry with `clients: [mcporter]`, in local mode with `write` access and default keep-alive. The node tests (375 pass, 2 skipped) and rumdl pass. The scoped `chezmoi diff` of `~/.mcporter/mcporter.json` showed only the `agora` entry.
- Sol mount: **passed**. Applied that one target and restarted with `~/bin/launchd/mcporter-restart`; the scoped diff is now empty. Undo: revert `3ed23ae2`, apply the same target, and restart.
- Sol check 1, tools: **passed**. `mcporter list agora` and the bridge at `127.0.0.1:3333/mcp` both list the nine `agora__` tools.
- Sol check 2, live round trip as `ki.prj.agora` in local mode: **passed**. `send` created message `01a1b463-06fd-76ce-9660-21b63a667d88`, "MCP-MOUNT live test from sol", in commit `1a47bcb`. `inbox` returned it, `ack` committed `d9cbe9c`, and `audit` showed the message as acked. Both commits are on GitHub's `origin/main`. No write failed, so there was nothing to clean up.
- Sol check 3, store clone: **passed**. Clean, nothing staged, and level with `origin/main` at `d9cbe9c`.
- Terra preparation: **passed**. Cloned `mcp-agora` (at `3012cf3`) and `ki-agora-beacon` from GitHub. `bun install --frozen-lockfile` and `bun run build` succeeded. Undo: delete the two new clones.
- Terra mount: **stopped**. chezmoi is 26 commits behind and cannot fast-forward over the other session's dirty `messages.md`. Terra's checks 1 to 3 were not run, and no terra message was sent.

## In Progress

- Nothing running. Terra's mount waits on MOUNT-3.

## Queries

### MOUNT-3 - Terra's chezmoi checkout is blocked by another session's edit

**Context:** On terra, `~/.local/share/chezmoi` has uncommitted edits to `+/_WORK/personal.reg.household-sol/messages.md` and `+/_WORK/personal.reg.household-terra/messages.md`, made at 01:58 GMT. The 26 incoming commits change the first file, so a fast-forward would overwrite that edit. My rules forbid touching another session's changes.

**Query:** How should terra's checkout be cleared so its Agora mount can finish?

**Options:**

a) (recommended, confidence high - it keeps the other session's work in its owner's hands) The household package that owns those mailboxes commits or settles its two edits on terra. A short resume run then fast-forwards, applies the single mcporter target, restarts the bridge and runs terra's three checks with one live message.

b) A run stashes the two edits, fast-forwards, and puts them back, stopping if they conflict. This is quicker, but it handles another session's uncommitted work.

c) Leave terra unmounted for now. Terra's agents keep using `messages.md` until someone next works there.

### MOUNT-4 - Store hooks on a fresh clone

**Context:** A fresh clone of ki-agora-beacon does not set `core.hooksPath`. Sol's clone uses `.githooks`; terra's new clone has nothing, so its writes would skip the store's rumdl and commit-message hooks. The store's README does not cover setup.

**Query:** Should terra's clone get `core.hooksPath = .githooks`, as sol's has?

**Options:**

a) (recommended, confidence medium - it matches sol, and the mount still writes nothing on terra yet) Yes: the MOUNT-3 resume run sets it before terra's live test, and the store's README gains a setup line.

b) No: leave terra without hooks.

🧵 ki.prj.agora
