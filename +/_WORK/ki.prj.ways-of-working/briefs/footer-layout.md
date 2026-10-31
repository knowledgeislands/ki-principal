# Brief: footer-layout

Work: ki.prj.ways-of-working, which owns `ki-coordination`. Authority: FOOTER-LAYOUT, confirmed by Kris on 31 October 2026, in `decisions.md`. Read both entries.

In ki-agentic-harness, rewrite the banner (footer) rules in `ki-coordination`, the output style and the Work Process wording if needed, so that the footer is, top to bottom:

1. `### <glyph state> · since <time>`, with the state only and no brackets;
2. the counts line;
3. a blank line, then the item bullets;
4. a blank line, then `↪️ draining → <target>` or `↪️ finishing → <target>`, only while heading for a hold or a handoff (replacing DRAIN-TARGET's bracketed heading and the form-line bracket);
5. a blank line, then one line per mode switched on: `👂 listening`, or `🔇 not listening` / `🔇 not listening while draining`, and `🔄 syncing for <host>` only on a host sync thread (replacing the "· sync thread for" suffix);
6. a blank line, then `🧵 <work-id>` last.

Update every example, the hold banner and the banner test. Keep the bottom-up reading order. Regenerate the surfaces, and run the banner test, the tests and the audit. Work in your own worktree, fast-forward `main`, commit by explicit path and push fast-forward only. Report in plain English.
