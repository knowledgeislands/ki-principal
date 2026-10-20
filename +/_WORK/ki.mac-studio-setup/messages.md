# ki.mac-studio-setup messages

- 2026-10-20 01:47 BST · from ki (State of play), routed from ki.observatory, RIG-SCHEDULE-ENCODING, not blocking · route to the work that owns tools-rig (Rig) a handoff for tools-rig to specify the `schedule` string encoding in `rig show --format json` (`calendar:`/`interval:` prefixes, records joined by `;`), or add an additive structured schedule field. RIG-STATE-033 and RIG-CONF-016 cover the values and grammar but not the encoding; KI-OBSERVA-VIS-022 now parses it strictly with a 26-hour fallback. Not blocking.
