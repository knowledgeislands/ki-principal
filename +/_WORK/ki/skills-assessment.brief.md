# skills-assessment brief

Run for KI > SoP (`ki`), under SKILLS-ASSESSMENT in [decisions.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/decisions.md) (Kris, 24 October). This is a quick, read-only assessment.

## Goal

Compare the skills and behaviours of the eight territory Capitals, so Kris can see where they are consistent and where the gaps are. The aim is that every principal repository has consistent skills and behaviours.

## Scope

The eight Capitals:

- `knowledge-islands/ki-principal`
- `humans-not-robots/hnr-principal`
- `equal-remedy/er-principal`
- `legal/legal-principal`
- `personal/personal-principal`
- `techmedix/tmx-principal`
- `valle-armonia/va-principal`
- `sacred-inquiry/si-principal`

All are under `/Users/krisbrown/workspaces/`.

For each Capital, read:

- the skills it declares in `.ki.toml` and their overlays;
- its `AGENTS.md` and `CLAUDE.md`, and any project skills or rules (`.claude/`, `.agents/`);
- whether it holds territory work in `+/_WORK/`, and the shape of that work;
- whether it uses the theme registry or the old `Streams/Initiatives/`.

Then read its territory harness, `<territory>/*-agentic-harness`, for skills it adds or overrides. Use `ki repo audit --repo <path>` only where it runs quickly and offline. Do not conform anything.

## Output

Write the report to `/Users/krisbrown/.local/state/ki/agents/ki/skills-assessment.report.md`, as an owner report under `ki-delegation`. It is short:

1. A matrix of skills (rows) against the eight Capitals (columns), marked declared, missing or overridden.
2. Where they are consistent.
3. The gaps and divergences, one line each, including local guidance in `AGENTS.md` or `CLAUDE.md` that duplicates a skill or should be promoted into one.
4. A proposed baseline skill set for a Capital.
5. Queries for Kris (Context, Query, Options, with a) recommended and its confidence). Mark any medium- or low-confidence query `needs blind review`.

## Limits

- Read-only. Edit, commit and create nothing outside the report.
- Send nothing to any territory.
