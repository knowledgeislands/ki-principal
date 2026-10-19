# Brief: toml-review

Blind review of one query for KI > Rig > chezmoi, under the `ki-coordination` Query review rule. Check the claims directly, read-only, then return your own recommended option, a confidence and a one-line reason. Change nothing; no remote, `sudo` or `rig apply` call.

Evidence: `/Users/krisbrown/.local/state/ki/agents/chezmoi/apply-carry.report.md`; tools-rig `src/rig/29-default-applications.bash` in `/Users/krisbrown/workspaces/knowledge-islands/tools-rig`; the chezmoi source `/Users/krisbrown/.local/share/chezmoi` (`dot_config/rig/conf.d/`); `rig doctor` on this Mac.

## TOML-HANDLER

**Context:** The five Rig targets (Dock links, `.toml` handler, Paperclip held off) are applied on Sol, and the Dock is applied. `rig apply --target default-application:toml` fails with `handler assignment failed: -50`: `toml` has no registered content type, macOS gives it a dynamic one (`dyn.age81k55rru`), and `LSSetDefaultRoleHandlerForContentType` rejects that. Zed's and Warp's Info.plists list the extension but declare no type. `rig doctor` on Sol went from 1 finding to 3, both new ones from the failed TOML apply. Terra is not yet carried and will likely fail the same way. Kris asked for `.toml` to open in Zed.

**Query:** How should the TOML handler and Terra's carry proceed?

**Options:** a) Carry Terra now without the TOML target; capture a tools-rig record so `macos-handlers` falls back for dynamic types; accept the TOML drift finding on both Macs until it lands. b) Set the handler by hand in Finder (Get Info, Open with, Zed, Change All) on each Mac, then carry Terra in full. c) Pull `[default-application.toml]` from the declaration until tools-rig supports it, then carry Terra in full.

## Report

Owner report with heading `# KI > Rig > chezmoi › toml-review` and, under `## Done`, `TOML-HANDLER: <option>) confidence <level> - <reason>`, plus any claim in the Context you found false.
