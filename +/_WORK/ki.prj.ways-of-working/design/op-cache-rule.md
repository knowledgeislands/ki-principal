# OP-CACHE - cached 1Password reads in delegation guidance

Draft for the coordinator of `ki.prj.ways-of-working`, from the `op-cache-rule` run on 30 October 2026. No skill or tool has been changed.

## Source

OP-CACHE, received 30 October 2026 from `hnr.sop.main`. Kris: "agents should be using cached_op", not repeated `op` calls.

## The reader, as verified

Read from the chezmoi source only; neither script was run and no secret value was read.

- `~/bin/chezmoi/op_cache` (source `bin/chezmoi/executable_op_cache`) is invoked as `~/bin/chezmoi/op_cache "op://<vault>/<item>/<field>"` and prints the field. One `op item get` fills the whole item into `~/.cache/op-cache/<item-uuid>.json` (mode 600) for a 24-hour window aligned to local midnight, so a day costs at most one prompt per item, and several fields of one item cost one.
- A refresh tries the read-only service account "Automation" first, which never prompts. With `OP_CACHE_SERVICE_ACCOUNT_ONLY=1` it never falls back to the desktop app: an item the service account cannot read exits 3 instead of prompting. Background runs set it.
- `~/bin/chezmoi/op_cache --tag <tag> [--vault <vault>]` lists the ids of tagged items, Automation by default, through the service account only, reading no field.
- `chezmoi_op` (source `bin/executable_chezmoi_op`) manages the cache: `chezmoi_op cache list`, `chezmoi_op cache expire [<uuid>...]`, `chezmoi_op set <ref> [value]` and `chezmoi_op alias`. It is Kris's tool for the cache, not a reader for agents.
- chezmoi's own guide, `docs/guides/tools/chezmoi.md`, already says a background agent reads a secret only through `op_cache` with the service-account-only setting and stops and reports an item outside Automation.

## Where the guidance stands

- `ki-delegation`'s [background-run standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-delegation/references/standards-background-runs.md), Authority tiers, already holds the rule (RUN-SECRETS): "use the managed `op_cache` helper with `OP_CACHE_SERVICE_ACCOUNT_ONLY=1`, never call `op` directly". It gives neither the path nor the invocation, and it does not carry Kris's words.
- The authority footers, `assets/rules-none.md`, `rules-push.md`, `rules-prune.md` and `rules-release.md`, say only "Do not read or print secrets". `assets/grant-machine.md` says "Credentials stay banned: make no credential change, and do not read or print secrets". So a brief carries the ban but not the reader to use when a task does authorise a read.
- The brief template `assets/run-prompt.md` carries no credential line; the footer is appended to it, so the footer is the right carrier.
- `scripts/rubric/contexts/footers.ts` requires the phrase "Do not read or print secrets" in every tier footer.
- `ki agent launch` in tools-ki (`src/core/agent/runs.ts`) reads each footer from the pinned harness's `ki-delegation/assets/rules-<tier>.md` and `grant-<name>.md` at launch, so it renders no footer text of its own. No tools-ki change is needed and no message goes to `ki.prj.tools-burndown`.

## Drafted text

### 1. Each tier footer

In `rules-none.md`, `rules-push.md`, `rules-prune.md` and `rules-release.md`, add this sentence after "Do not read or print secrets." in the remote-call line:

> Where the task authorises a 1Password read, read only through `~/bin/chezmoi/op_cache "op://<vault>/<item>/<field>"` with `OP_CACHE_SERVICE_ACCOUNT_ONLY=1`, never through `op` itself, and stop and report if it exits 3, under the standard's [cached-reader rule](../references/standards-background-runs.md#authority-tiers).

### 2. The machine grant

In `grant-machine.md`, after "do not read or print secrets", add:

> ; a 1Password read the task authorises still goes only through `~/bin/chezmoi/op_cache`, never through `op` itself.

### 3. The background-run standard

Replace the opening of the RUN-SECRETS paragraph in Authority tiers, up to "use `op_cache --tag <tag>` for discovery.", with:

> In Kris's managed environment, when a task separately authorises a 1Password read, read only through the managed cached reader, `~/bin/chezmoi/op_cache "op://<vault>/<item>/<field>"`, with `OP_CACHE_SERVICE_ACCOUNT_ONLY=1`, and use `~/bin/chezmoi/op_cache --tag <tag> [--vault <vault>]` for discovery. Never call `op` directly or repeatedly: the reader caches each item for a day, so a run costs at most one read per item per day. Leave `chezmoi_op`, which manages the cache, to Kris. Kris set this on 30 October 2026 under OP-CACHE: "agents should be using cached_op".

The rest of the paragraph stays as it is.

### 4. The footer rubric

Add `'~/bin/chezmoi/op_cache'` to the required phrases in `scripts/rubric/contexts/footers.ts`, beside `'Do not read or print secrets'`, so a footer that drops the reader fails the rubric. The harness's footer tests will need the same phrase.

### 5. Provenance

Add a line to `references/sources.md` naming OP-CACHE, its date and Kris's words.

## Not changed

- The standard's personal-environment scope stays: the rule names Kris's managed environment and grants no credential authority.
- The Cloudflare half of RUN-SECRETS, `~/bin/cf_token`, is untouched.
