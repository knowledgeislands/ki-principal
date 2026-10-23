# ki.chezmoi messages

None.

- 2026-10-23 21:56 BST from va (Kris, routed): Tidy the Cloudflare user API tokens. There are 36 user tokens, many created per app with no expiry and duplicated, plus `workers-builds-kit` (1Password `a52xo4mqroqi6eqexuqhny67fu`), Kris's attempt to replace the per-Worker-build tokens with one. The user token `agentic-access` (`hsprfhlhi4eqnugcupyoct2uwu`) now holds User API Tokens Edit. Kris's intended practice is to grant per occasion, then strip back to that baseline. Review best practice, propose a consolidated set with expiries, and update `cf_token` and `docs/guides/tools/cloudflare-tokens.md`. Note: 1Password shows `agentic-access` expiring 30/09/2027, but Cloudflare shows no expiration.
