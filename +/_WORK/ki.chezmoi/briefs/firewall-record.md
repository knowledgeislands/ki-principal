# Brief: firewall-record

Work: KI > Rig > chezmoi in `/Users/krisbrown/workspaces/knowledge-islands/ki-principal`. Authority: Kris, 19 October, RIG-FIREWALL-RUN a): after the attended Terra rehearsal passes, record the evidence in KI-TOOL-RIG-CORE-047 and write, gate and commit the `core` declaration. No push, no `chezmoi apply`, no `rig apply`, no `sudo`.

The rehearsal passed at 22:03–22:06 BST using `/Users/krisbrown/.local/state/ki/agents/chezmoi/firewall-rehearse-v2.md` (the blind-reviewed sequence; the review is in `firewall-seq-review.report.md` and the writer's checks in `firewall-seq-write.report.md`). Kris's output, verbatim:

```text
A0 (before): pf enabled: yes | daemon loaded: yes, last exit 0: yes
anchor rules: 8, match file: yes | parent calls anchor: yes
TOKENS: 546 pfctl 7339458489387109918 0 days 00:54:05
A0 RESULT: PROTECTED
B PASS 22:03:06: fresh SSH to terra, daemon loaded
A1: reload rc=0 | match file: yes | pf enabled: yes | parent calls anchor: yes | references 3 -> 3
A1 RESULT: RELOAD PROVEN
A2: REMOVED 22:04:26: anchor empty, daemon absent.
B PASS 22:04:59: fresh SSH to terra, daemon absent
RESTORING 22:05:17
bootstrap rc=0 | new run exit 0: yes | match file: yes | pf enabled: yes | parent calls anchor: yes | references 3 -> 4
A2 RESULT: RESTORED
B PASS 22:05:40: fresh SSH to terra, daemon loaded
A0 (after): pf enabled: yes | daemon loaded: yes, last exit 0: yes
anchor rules: 8, match file: yes | parent calls anchor: yes
TOKENS: 14331 pfctl 4286484510776417438 0 days 00:00:45; 546 pfctl 7339458489387109918 0 days 00:57:40
A0 RESULT: PROTECTED
```

Also record the following:

- The first attempt, at 21:07 BST, shut Terra down. A hand-run block expanded `launchctl bootout system/$L` with `L` empty (`firewall-freeze.report.md`).
- Rig's own firewall path rejects an empty locator, and the restore is unaffected.
- Not proven: Screen Sharing reachability over the tailnet, and LAN refusal with fresh flows.
- Sol still needs its own rehearsal before its `rig apply --sudo`.

All reports are in `/Users/krisbrown/.local/state/ki/agents/chezmoi/`.

Do:

1. Record the evidence in `/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md` under that repository's record rules. Run its gate, and commit by explicit path in tools-rig.
2. Do point 3 of the original firewall-rehearse brief. Read it with `git -C /Users/krisbrown/workspaces/knowledge-islands/ki-principal show f45b6d71^:'+/_WORK/ki.chezmoi/briefs/firewall-rehearse.md'`.
   - Write the `core` declaration in the chezmoi source, under `dot_config/rig/conf.d/`.
   - Record `rig doctor` finding counts before and after, and read every finding.
   - Run the full gate: `ki repo audit --repo .`, `node --test tests/*.test.mjs` and `rumdl check .`.
   - Commit by explicit path.
   - Show `chezmoi diff` in your report for the changed targets only. Do not apply.

Report under the owner report, with the work's report heading and `› firewall-record`.
