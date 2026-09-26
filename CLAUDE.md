# CLAUDE.md — context-stack Agent Briefing

Read this before touching any file in this repo.

## What This Repo Is

context-stack is the stack's control plane. It holds locked decisions, canonical terminology, the composition, and stack management — nothing else. It is not part of the composition.

**This repo contains only confirmed, locked content. No parked items. No roadmap. No backlog.**
Planning and roadmap live in Google Drive.

## The Composition

ContextOps and ContextBoundary are the specification layer. contextboundary-gw, Sthala and Griha are reference implementations that apply it.

Defined once, in COMPOSITION.md. Each repository's kind and role are recorded as data in `stack.yaml` -> `composition.roles`. Do not restate the shape anywhere else; quote the sentence above byte-identical or link to COMPOSITION.md.

## Relationships (Do Not Conflate)

- ContextOps = organisational governance layer
- ContextBoundary = horizontal egress governing layer (deployment-agnostic)
- Sthala = reference implementation for governed runtime placement; it consumes ContextBoundary's egress contract
- ContextBoundary is not Sthala. Sthala is a consumer of ContextBoundary, not a peer.

## How To Use This Repo

- Before introducing any new term in any repository of the stack: check GLOSSARY.md
- Before making any cross-project decision: check DECISIONS.md
- Before routing work across repos: check STACK_MANAGEMENT.md
- Before editing a project repo: check REPO_MAP.md
- Before release or public-facing changes: check RELEASE_CHECKLIST.md
- If a term isn't in GLOSSARY.md: propose it here first, then propagate to the project repos

## Rules

- Only locked, confirmed content goes here
- No version suffixes like "Draft"
- No parked or aspirational items
- No project-specific implementation detail — that belongs in the project's own CLAUDE.md
- Vendor-neutral language throughout
- Every repository in the stack is Apache 2.0 — no license drift

## Commit Style

Single-topic commits. Example:
```
Add egress tier terms to GLOSSARY.md

- Tier I / II / III definitions locked
- Five-zone model added
- Banned terms list updated
```
