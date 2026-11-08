# ki.prj.stoa discussions

## Open

### STOA-AREAS - eleven new roadmap area codes

focus: _emerging

**Context:** packages-stoa declares one roadmap area, `CMD`. The drafts use eleven more, one for each unit or concern: `CAL`, `HDR`, `THEME`, `BASE` (first paint across units), `TOOL`, `WB` (workbench), `REG` (consumer register), `LINK` (heading links), `PAGE`, `PRINT` and `DIAG`. An area code is fixed once issued, so this is the moment to choose.

**Query:** Capture with the eleven codes as drafted?

**Options:**

a) (recommended, confidence medium - one code for each unit matches the brief's examples and keeps later records easy to place) Yes, declare all eleven in `.ki.toml` and the ledger.

b) Fold the one-record areas into broader ones, for example `TOOL` and `WB` into `TOOL`, and `LINK` and `PRINT` into `PAGE`.

### STOA-TOOL-SCOPE - Biome fix with no consumer template

focus: _emerging

**Context:** STOA-TOOLING item 1 asks Stoa to "fold a fix into the consumer template", but packages-stoa has no consumer template. Sites are set up from the package README. STOA-TOOL-001 is drafted as a README note telling sites to switch off Biome's Markdown handling and keep `keywords` out of Syncpack's sort.

**Query:** Is a README note enough?

**Options:**

a) (recommended, confidence medium - Stoa ships no site scaffolding, and a template elsewhere belongs to its owner) Yes, a README note in Stoa, and tell hnr.sop.sites that any site template is theirs to fix.

b) Have Stoa ship a consumer `biome.json` fragment as well, which widens what sites vendor.

## Parked

None
