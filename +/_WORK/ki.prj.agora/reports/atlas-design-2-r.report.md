# KI > Techne > Agora › atlas-design-2

**🤖 → 👤 Handoff to supervisor · Run report at 04:11 GMT · last mark 00:04 GMT**

---

## New and noteworthy

Applied the revised shell (0.4), compact bar (0.5), Home (9.1) and Guilds (8.2), including DESIGN-14 and DESIGN-15. Home and the bell now share one attention list; map trays pin beside the page. Project packages without a recorded role show No role; Agora remains Warden.

## Done

- Resumed after guilds-table-r and lantern-roadmap finished. The earlier atlas-design-2 attempt stopped at its prerequisite gate without an implementation or report; this run continued from the delivered Home and Guilds work on main.
- Shell: six folding sections, Art gallery under Work, small eyebrows and AGO/WRK/GLD/OBS/KIV/SYS in icon mode; Home only from the logo, with its tooltip. Kept the revised Home/Known Lands/Observatory/Art gallery page numbers.
- Compact bar: one 36-point row, presence chips up to three rigs and a worst-first floating list above three, shared bell/count/words leading to Home’s Needs a look, icon actions, time, pin and theme, with word tooltips on hover and keyboard focus. Removed At a glance from the bar and map tray.
- Home: urgent-first attention rows each have an explanation, next step and one action; one holder table by tier or rig includes running doers, recorded roles, focus and states; disagreement footnotes and the selected row’s record/catalogue tray follow; unfilled seats have a separate Yours to approve section and one brass review control.
- Guilds: compact scrolling shields with All guilds frozen, fade and arrows; separate kind/applicability tallies, context, Filter, find and Guild/ki-kind/None grouping; folding guild summaries and Show N more; all metadata columns with any for unset runtimes; front matter, body and file tabs in the right tray, with no bottom pane. Captured the 8.2c, 8.2d and 8.2e states.
- Pinned/floating rules: map selections push the page narrower, tab selections are kept, one floating menu opens at a time, outside clicks dismiss it, and Escape closes it before the tray or bottom pane.
- Portal lookup prefers ki-agora-beacon, falls back to ki-portal and retains the household fallback when neither exists. Regression tests cover the rename, both entries together and the absent-entry case.
- bun run self:check — passed, with existing/nonblocking style warnings. The new pure attention module is included in the enforced browser boundary.
- bun run test — passed, 567 tests across 57 files.
- Markdown checks — passed for README.md and docs/design/agora-app.md.
- Throwaway capture run — passed 32 interaction/layout assertions with no renderer errors. Compared light and dark captures against 0.4, 0.5, 9.1 and 8.2; no installed app was relaunched, replaced, packaged or installed.
- Evidence: [Home light](/Users/krisbrown/.local/state/ki/agents/ki-prj-agora/atlas-design-2-r.evidence/home-light.png), [Home dark](/Users/krisbrown/.local/state/ki/agents/ki-prj-agora/atlas-design-2-r.evidence/home-dark.png), [ten rigs and pinned tray](/Users/krisbrown/.local/state/ki/agents/ki-prj-agora/atlas-design-2-r.evidence/presence-ten-dark.png), [Guilds light tray](/Users/krisbrown/.local/state/ki/agents/ki-prj-agora/atlas-design-2-r.evidence/guilds-tray-light.png), [Guilds scrolled dark](/Users/krisbrown/.local/state/ki/agents/ki-prj-agora/atlas-design-2-r.evidence/guilds-scroll-dark.png), [Guilds references dark](/Users/krisbrown/.local/state/ki/agents/ki-prj-agora/atlas-design-2-r.evidence/guilds-files-dark.png), and [capture assertions](/Users/krisbrown/.local/state/ki/agents/ki-prj-agora/atlas-design-2-r.evidence/capture-result.json).
- Read the complete run inbox. Relevant shell, logo, map, naming and search steering is preserved; historical installation, Lantern, interaction-protocol and other-run instructions were outside this run. The pack contains IA.md, README.md and index.html, but no index.md.
- Commit `8bc0417` — feat(atlas): align shell, Home and Guilds with revised designs. Inspected the hook-backed commit: exactly the thirteen owned paths, with the required Work-Id and model co-author trailers.

## In Progress

Nothing running. Delivery awaits supervisor review. No roadmap record was created and no other repository was changed.

Outstanding - no action requested now: the current upstream status has no live human-session signal; With you is explicitly described as the package’s recorded handoff. Broadcast history/recipient receipts are not in the current view, and that page says so. Approval/package creation remains in the owning thread; the brass control reviews proposed seats rather than granting authority. These limits are visible in the app and documented.

The unrelated ios/AgoraBeacon.xcodeproj/project.pbxproj working change remains untouched.

## Queries

None.

🧵 ki.prj.agora
