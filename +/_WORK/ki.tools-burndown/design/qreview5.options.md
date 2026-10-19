# Options for blind review

## KNIP-HUSKY - Teach conform the Knip side of the hooks conversion

Context: `ki repo conform` in tools-ki now converts Husky repositories to committed `.githooks` (record KI-TOOL-KI-CLI-163, `src/core/repository/hooks.ts`). Knip saw Commitlint and lint-staged through its Husky plugin, which reads `.husky/`; once Husky goes it reports them unused and Knip fails. The pilot added them to `ignoreDependencies` by hand, and tonight's estate runs do the same by hand.

Query: Should conform's conversion add those Knip ignores itself, for repositories converted later and for new ones?

a) Extend the KI-TOOL-KI-CLI-163 conversion in a follow-up release, and have the harness's Knip guidance name it. b) Leave conform as it is; the estate runs fix it by hand and later conversions rely on the audit.
