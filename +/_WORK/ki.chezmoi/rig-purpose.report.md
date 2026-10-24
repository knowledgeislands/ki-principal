# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › rig-purpose

**🤖 → 👤 Handoff to supervisor · Run report at 05:18 BST**

---

## Done

Every Rig purpose now follows [Decision 179](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.chezmoi/decisions.md): 191 tools and 55 macOS settings say what they are for in one short line. Nothing says why an item is kept or how it is installed, and no placeholders remain. Fourteen tools carry a separate comment: nine from Decisions 153 and 154, and five real dependencies such as 1Password CLI signing in through the desktop app.

- Commit `a59b19f`, fix(rig): state each tool's purpose factually in one line. Covers applications, command-line and Homebrew.
- Commit `c65e539`, fix(rig): describe what each macOS setting does.
- Commit `d46a2ed`, docs(roadmap): rescope [KB-DOTFILES-UE-027](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-027-honest-rationales-per-tool.md) to factual purposes (Decision 179).
  - [The worksheet](/Users/krisbrown/.local/share/chezmoi/-/rig-rationale-review.md) is now Kris's review list. It has every purpose and comment, plus the candidate comments that were left out.
  - The record supersedes the unconfirmed-rationale question and the DisplayLink and Outlook questions.
  - It stays on hold until Kris reviews the list, and its status is still draft.
- `tool.spark` is now described as Shadowlab's Spark, "Launch applications and scripts with global keyboard shortcuts." Spark Mail is still `tool.spark-desktop`, with the comment "The default mail app."
- Ten examples, before and after:

| Item | Before | After |
| --- | --- | --- |
| `tool.ack` | Provide the ack Homebrew package for the workstation. | Fast grep-like code search. |
| `tool.jq` | Provide the jq Homebrew package for the workstation. | Query and transform JSON. |
| `tool.zoom` | Video meetings where Zoom is the required platform. Its rationale explained why it was installed. | Purpose unchanged; the installation reason is gone. |
| `tool.ghostty` | Fast native terminal kept as an alternative to Warp. | Fast native terminal. |
| `tool.rendapp` | Rendering workflow retained in the active Dock. | Companion app for The Tower idle game. |
| `tool.codex` | OpenAI's primary coding agent and desktop development workspace. Rationale "Kept as the second coding agent…" | OpenAI's coding agent and desktop workspace. |
| `tool.beyond-compare` | Primary visual file and directory comparison tool. | Compare and merge files and folders side by side. |
| `tool.path-finder` | Current power-user Finder alternative while ForkLift remains under evaluation. | Power-user file manager. Comment: "The longer-term Finder replacement is still open; ForkLift is under evaluation." |
| `setting.dock-autohide` | Keep this reviewed macOS preference declarative. Review needed… | Hide the Dock until the pointer reaches it. |
| `setting.global-show-all-extensions` | Keep this reviewed macOS preference declarative. Review needed… | Show every filename extension. |

- `node --test tests/*.test.mjs`: 290 pass, 0 fail, 2 skipped.
- `rumdl check .`: no issues.
- `ki repo audit --repo .`: PASS, 11 warnings, all inside the permitted baseline plus CLAUDEBIND-1.
- `rig doctor`: 4 findings before and 4 after.
  - Unchanged: the `utm` App Store source drift, the toml default handler (Warp where Zed is declared), and one past apply failure on that handler.
  - Changed: the screen-sharing firewall anchor now also reports `exposed-beyond-tailnet`, which was not there at 05:03. See the FIREWALL-EXPOSURE query.
- No `.git` lock files remain, and nothing was applied.
- Uncommitted changes from other work are untouched: `.chezmoidata/trusted-folders.yaml`, the `workspaces/vscode/` files, and `docs/roadmap/KB-DOTFILES-UE-035-install-whatsapp-spool-refresh.md`.

## In Progress

- **Kris's review:** Kris reviews the list in [the worksheet](/Users/krisbrown/.local/share/chezmoi/-/rig-rationale-review.md). [KB-DOTFILES-UE-027](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-027-honest-rationales-per-tool.md) stays on hold until then.
- **The `rationale` field:** Rig requires a non-empty `rationale` and has no separate comment field. For now, where there is no comment, `rationale` repeats the purpose word for word.
  - The purpose-render run should hide the subtext line wherever the two match.
  - Otherwise the Rig site shows each purpose twice.
- **Not applied yet:** these commits, and earlier ones from other runs, have not been applied.
  - The live `~/.config/rig/conf.d` copies of the applications and Homebrew fragments already differed from source before this run.
  - Applying fragments 10, 15, 16 and 40 needs Kris's approval. Only text changes, so `rig status` counts should not move.

## Queries

**FIREWALL-EXPOSURE**

**Context:** Between 05:03 and 05:16 BST, `rig doctor`'s screen-sharing firewall finding changed from `anchor-changed` to `anchor-changed,exposed-beyond-tailnet`. This run applied nothing and made no firewall change.

**Query:** Should Kris check now whether Screen Sharing on this Mac can be reached from outside the tailnet?

**Options:**

a) (recommended, confidence high - this is a live security exposure that turned up during the run, and its cause is unknown) The coordinator raises it with Kris now. Kris reviews the anchor and runs `rig apply` for `firewall.screen-sharing-tailnet` if it is safe to do so.

b) Leave it as an existing finding for the next Rig health pass.

**SPARK-TOOL**

**Context:** `tool.spark` is Shadowlab's Spark, a keyboard-shortcut launcher. In [Decision 154](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.chezmoi/decisions.md), Kris said they would like to use it more but have not tried it much recently. Alfred already covers launching and shortcuts.

**Query:** Keep `tool.spark` or retire it?

**Options:**

a) (recommended, confidence medium - it overlaps Alfred, which is the declared single launcher, and is barely used) Retire it through the `ki-self` application lifecycle.

b) Keep it as it is now, with no comment.

c) Keep it and restore Kris's own words as its comment.

**RATIONALE-FIELD**

**Context:** tools-rig requires a non-empty `rationale` on every tool and setting. Decision 179 makes the reason optional, so for now most entries repeat their purpose.

**Query:** How should tools-rig hold the optional comment?

**Options:**

a) (recommended, confidence medium - this is the smallest schema change, and it keeps the existing field name for the 14 real comments) Make `rationale` optional in tools-rig. This repository then drops the repeated purposes, under [KB-DOTFILES-UE-027](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-027-honest-rationales-per-tool.md).

b) Add a new optional `comment` field and retire `rationale`.

c) Keep the duplication and rely on the site hiding the subtext where the two match.

**CORE-SET-COMMENTS**

**Context:** Decision 49, under KB-DOTFILES-UE-079 (no local record file remains), gave core-set reasons for Diagram, Google Drive, Home Assistant and HP. Those reasons fall outside Decisions 145 to 178. They are now listed in the worksheet as candidate comments, not written into the declarations.

**Query:** Restore them as comments?

**Options:**

a) (recommended, confidence low - they are Kris's own reasons, but Decision 179 named only 145 to 178) Restore them as comments, since Kris gave them.

b) Leave them in the worksheet for Kris's review.
