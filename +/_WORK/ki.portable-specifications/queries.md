# ki.portable-specifications queries

## Open

### VALID-SKILL - Whether `knowledge` and `acquire` packages stay valid skills

since 2026-10-19 · from live-read · reviewed by query-review-4

**Context:** The live check found that the Agent Skills validator, `skills-ref`, rejects any top-level field except `name`, `description`, `license`, `compatibility`, `metadata` and `allowed-tools`. As drafted, `knowledge` adds `updated`, `acquired-with` and `spec` at the top level, and `acquire` requires `source` and `mutation` and adds `omissions` (a list), `produces` and `spec`, so the drafts' claims that "a conforming package is also a valid skill" and "an acquire package is a skill" are false. Agent Skills itself suggests `metadata` "to store additional properties not defined by the Agent Skills spec", and `metadata` holds strings only, so `omissions` becomes one string whose delimiter the spec must define. A valid skill also needs its entry file named `SKILL.md`, so the claim holds only for a package presented as a skill under that name. SPEC-LOCATION already put the single-value fields in `metadata`; this settles the list field and the claim. `work` makes no such claim.

**Query:** Should `knowledge` and `acquire` move every added field, the list included, into `metadata` so the valid-skill claim holds?

**Options:**

a) (recommended, confidence high - reviewed; `metadata` is Agent Skills' stated home for extra properties, and running the validator's field check confirms it clears the rejection) Move every added field into `metadata` for `knowledge` and `acquire`, `omissions` as one string with a defined delimiter, and keep the claim, qualified that the entry file must be presented as `SKILL.md`; `work` keeps its difference listed.

b) Keep the fields at top level, drop both claims, and say the packages share Agent Skills' layout but are not valid skills.

## Parked

None
