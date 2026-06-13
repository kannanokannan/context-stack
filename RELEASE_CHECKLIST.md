# Release Checklist

Use this before committing or pushing public-facing changes across the Context Stack.

## 1. Pre-Flight

Confirm:

```text
Repo:
Path:
Remote:
Branch:
Git status:
Files changed:
Why these files:
Files not touched:
```

If the path is not under `G:\My Drive\ai-stack`, stop and re-check.

## 2. Ownership Check

Before editing:

- Does the change belong in this repo?
- Does it introduce a new term?
- Does it conflict with `GLOSSARY.md`?
- Does it change a locked decision in `DECISIONS.md`?
- Does another repo need a follow-up change?

## 3. Public-Facing Check

For docs, website, README, `llms.txt`, or public guide pages:

- Use durable language.
- Avoid transient market claims unless explicitly sourced and stable.
- Avoid hype words.
- Keep the framework, not MCP or tooling, as the hero.
- Check that links resolve.
- Check that navigation still makes sense.

## 4. Website Check

For `kannanokannan.github.io`:

- Verify local page renders.
- Verify desktop and mobile layout if visual structure changed.
- Update `sitemap.xml` for new public pages.
- Update `lastmod` for changed public pages.
- Keep `robots.txt` pointing to the sitemap.
- Verify live URL after push.

## 5. MCP Check

For `context-stack-mcp`:

- Confirm endpoint health.
- Confirm `/mcp` responds.
- Confirm exposed resources point to current source documents.
- Do not make MCP the governance authority.
- Keep MCP positioned as delivery access.

## 6. Source Repo Check

For pillar repos:

- Confirm terminology against `context-stack/GLOSSARY.md`.
- Confirm relationships against `context-stack/REPO_MAP.md`.
- Do not duplicate another repo's ownership.
- Do not add website-only positioning to source framework docs.

## 7. Commit Check

Before commit:

- Review `git diff`.
- Confirm no unrelated files are staged.
- Confirm local-only files are not staged.
- Use one commit per coherent change.

## 8. Push Check

After push:

- Confirm remote branch updated.
- For website/MCP, verify live endpoint.
- Update `G:\My Drive\ai-stack\STACK_WORKBOARD.local.md` if the active state changed.
