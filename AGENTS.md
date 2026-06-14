# AGENTS.md — context-stack Agent Briefing

Read this before touching any file in this repo.

## What This Repo Is

context-stack is the canonical coordination layer above three sibling open-source projects. It holds locked decisions, canonical terminology, and family framing — nothing else.

**This repo contains only confirmed, locked content. No parked items. No roadmap. No backlog.**
Planning and roadmap live in Google Drive.

## The Three Projects

| Project | Answers | Repo |
|---------|---------|------|
| ContextOps | How does an org govern its AI context? | https://github.com/kannanokannan/ContextOps |
| ContextBoundary | Where is data allowed to go? | https://github.com/kannanokannan/ContextBoundary |
| Sthala | Where does the AI actually run? | https://github.com/kannanokannan/Sthala |

## Relationships (Do Not Conflate)

- ContextOps = organisational governance layer
- ContextBoundary = horizontal egress governing layer (deployment-agnostic)
- Sthala = governed runtime placement reference under ContextBoundary
- ContextBoundary is not Sthala. Sthala is a consumer of ContextBoundary, not a peer.

## How To Use This Repo

- Before introducing any new term across any of the three projects: check GLOSSARY.md
- Before making any cross-project decision: check DECISIONS.md
- If a term isn't in GLOSSARY.md: propose it here first, then propagate to the project repos

## Rules

- Only locked, confirmed content goes here
- No version suffixes like "Draft"
- No parked or aspirational items
- No project-specific implementation detail — that belongs in the project's own AGENTS.md
- Vendor-neutral language throughout
- All three projects are Apache 2.0 — no license drift

## Commit Style

Single-topic commits. Example:
```
Add egress tier terms to GLOSSARY.md

- Tier I / II / III definitions locked
- Five-zone model added
- Banned terms list updated
```
