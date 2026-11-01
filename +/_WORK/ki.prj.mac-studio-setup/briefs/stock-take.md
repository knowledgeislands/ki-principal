# Brief: stock-take for ki.prj.mac-studio-setup

## Goal

Kris (1 November, 00:40 GMT): "Can you take stock of this and see where at? I suspect quite a lot of these things have been dealt with." Establish, from evidence, which of this work's open, parked and held items are already settled, so the coordinator can clear them and put only live ones back to Kris.

## Read

- The work package `+/_WORK/ki.prj.mac-studio-setup/` in ki-principal: `state.md` (Now, Next steps, Held), `queries.md` (Open and Parked) and `messages.md` (retained Rig lines). Do not edit it.
- Evidence anywhere on this Mac, read-only: tools-rig (`~/kis/knowledge-islands/tools-rig`, its `docs/roadmap/`, `_IDEAS.md`, git log), chezmoi (`~/.local/share/chezmoi`, including PERSONAL-DOTFILES-UE-086 and its git log), tools-mgit, ki-principal's other work packages (`+/_WORK/*/decisions.md`, `messages.md`, especially ki.sop.main, ki.prj.chezmoi, ki.prj.tools-burndown, personal.reg.rig-terra in personal-principal), live sol state (`rig status`, `rig doctor`, `ls ~/Library/CloudStorage/OneDrive-Personal`, `ki doctor`, `~/.config/ki/config.toml`, installed apps such as Adobe leftovers, old checkouts), and GitHub via `gh` where it settles a question. Fetch is allowed; do not pull into other checkouts with local changes.

## Do

For every item - each Open and Parked query, each Held line, each Next step, each retained `messages.md` line and the four tools-rig records named in `state.md` - give one row: item, what the package says, current evidence (with path, commit or command), and a verdict: `settled` (say by what), `superseded` (by what), `partly` (what remains), `live` (unchanged), or `unknown` (what would settle it). Name any record whose roadmap state has moved (for example KI-TOOL-RIG-CORE-047, 068, 069, 070, 072, 053, 056, 057, 064, 067, KI-TOOL-RIG-DIST-011), linking each record's file by absolute path, or a pinned GitHub link if pruned. Say which queries could be retired outright and which need rewording for Kris.

Read-only. Change nothing on the machine, in any repository or package; run only read-only commands (no `rig apply`, no `sudo`).

## Report

Write the report as `stock-take.report.md` per the run packet, plain English, table first, then a short list of proposed package changes for the coordinator (queries to clear, to reword, Held lines to drop), each with a confidence level and reason.
