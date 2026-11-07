# ki.prj.stoa discussions

## Open

### STOA-033 - Release 0.33.0 with the clean-up

focus: _emerging

**Context:** The clean-up changed the code sites copy, and sites only get it in a release. It removes the old `PORTAL_FRAMEWORK_CHECKOUT` setting from the vendoring tools, which is Breaking: a site that still sets it must drop it. It also renames a test helper and puts every name in Stoa terms. HNR is only now starting to re-vendor 0.32.0.

**Query:** Release 0.33.0 now?

**Options:**

a) (recommended, confidence high - the sites re-vendor once instead of twice, and the Breaking change reaches them with clear instructions) Release 0.33.0 now, then send each site the re-vendor line and the instruction to drop the old setting.

b) Wait for the next feature, such as the Calendar fixes in the inbox, and release them together.

## Parked

None
