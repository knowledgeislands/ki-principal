# ki.ways-of-working queries

## Open

### MGIT-RELEASE - When other machines get the -f change

since 2026-10-19 · from mgit-filter.report.md in the run state folder

**Context:** `main` now carries breaking changes since v0.17.0 (`-B/--bypass`, `learn` and dropping `-f`), but only this Mac runs the checkout; Terra and Sol keep v0.17.0, where `-f` still works.

**Query:** Should mgit be released now so every machine has the same flags, or wait until Kris finishes the hands-on check in KI-TOOL-MGIT-CLI-023?

**Options:**

a) (recommended, confidence medium - one release carries the hands-on fixes and avoids a second breaking bump) Wait for the KI-TOOL-MGIT-CLI-023 hands-on check, then release once under [Release mgit](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/guides/developer/releasing.md).

b) Release v0.18.0 now from `main`, so the machines agree today.

### PUSH-STACKED - Query text not recovered

since 2026-10-19 · named open in the decisions log at 14:17 BST on 19 October

**Context:** The decisions log records PUSH-STACKED as one of three open queries at 14:17 BST on 19 October; the other two, MIGRATE-GATE and KI-TOML-PACKAGE, were answered at 14:20 BST. Its full text was in a Summary that was not saved, and the migration pass could not recover it. The earlier answer, PUSH-STACKED a) "do not push over others' commits", still governs.

**Query:** What was the open PUSH-STACKED question, and is it still open?

**Options:**

a) (recommended, confidence low - the text is lost, so the worker restates it from its own context) The coordinator restates PUSH-STACKED in full at its next Summary, or deletes this entry if PUSH-HARD answered it.

b) Kris answers it in speech from memory.

## Parked

### DESK-CAM - Which webcam to buy for sol

since 2026-10-15 · from [webcam-compare](webcam-compare.report.md) · parked: listed as outstanding and not this work's; release: Kris's purchase decision

**Context:** Kris wants one webcam with good built-in microphones for calls first and dictation second, using sol's own speaker. The best fit is the Insta360 Link 2C Pro at £199.00 (B0G3SSQMJQ): 1/1.3-inch sensor, two beamforming mics with a Focus mode, built-in shutter, plain UVC/UAC, and an optional app available as a Homebrew cask. The cheaper alternative with the strongest mic hardware is the OBSBOT Tiny 3 Lite at £169.00 (B0G63LXK6R). The UGREEN FineCam Pro at £57.78 (B0FX5QMB6K) is the budget option, with little audio evidence. All prices were seen on the product pages on 15 Oct 2026. Buying is Kris's decision.

**Query:** Which webcam does Kris want for sol?

**Options:**

a) (recommended) Insta360 Link 2C Pro, £199.00, amazon.co.uk/dp/B0G3SSQMJQ; add the `insta360-link-controller` Homebrew cask to sol's Rig configuration once it arrives

b) OBSBOT Tiny 3 Lite, £169.00, amazon.co.uk/dp/B0G63LXK6R; OBSBOT Center installed by hand

c) OBSBOT Tiny 3, £296.00, amazon.co.uk/dp/B0G636CXQM, for the best-reviewed webcam mics and the largest sensor

d) UGREEN FineCam Pro, £57.78, amazon.co.uk/dp/B0FX5QMB6K, the budget option with no app

- Parked 2026-10-09: a gradual move from Obsidian-style to GitHub-flavoured Markdown, starting with a front-matter field declaring a note's flavour.
