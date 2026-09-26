# Stack Management

This file defines how to manage the Context Stack as one project without merging the repos.

The repos stay separate. The operating model is shared.

## Control Plane

Use `context-stack` as the control plane for cross-project work.

Before changing any pillar repo, check:

1. `GLOSSARY.md` for canonical terminology.
2. `DECISIONS.md` for locked cross-project decisions.
3. `REPO_MAP.md` for ownership boundaries.
4. `RELEASE_CHECKLIST.md` before public-facing commits.

Do not use an old checkout under `Downloads` as the active workspace. The working stack is the single local directory where all Context Stack repositories sit side by side:

```text
<workspace-root>
```

## Repo Roles

| Repo | Role | Owns |
|------|------|------|
| `context-stack` | Control plane | Terminology, decisions, composition, repo ownership, release checks |
| `ContextOps` | Specification | Organizational context governance: roles, practices, maturity, context lifecycle |
| `ContextBoundary` | Specification | Data egress and action governance: data movement, tiers, zones, jurisdiction profiles |
| `contextboundary-gw` | Reference implementation | ContextBoundary reference gateway, compiled policy, conformance suite |
| `Sthala` | Reference implementation | Governed runtime placement; applies ContextOps and ContextBoundary |
| `Griha` | Reference implementation | Worked example for home and edge; applies Sthala's narrate/compute constraint |
| `kannanokannan.github.io` | Publishing surface | Website, discoverability, sitemap, public navigation |
| `context-stack-mcp` | Access path | MCP endpoint and assistant-facing access to the stack |

## Pre-Flight For Any Codex Session

Before editing, print or verify:

```text
Repo:
Path:
Remote:
Branch:
Git status:
Files likely to change:
Files that must not be touched:
Reason this repo is the right owner:
```

If the repo does not match the requested work, stop and switch before editing.

## Change Routing

Use this routing rule:

| Change type | Primary repo | Also check |
|-------------|--------------|------------|
| New cross-project term | `context-stack` | `GLOSSARY.md` |
| New cross-project decision | `context-stack` | `DECISIONS.md` |
| Context lifecycle or maturity | `ContextOps` | `context-stack` terms |
| Cross-project maturity snapshot | `context-stack` | ContextOps, ContextBoundary, Sthala |
| Data egress or sovereignty | `ContextBoundary` | `context-stack` terms |
| Runtime placement | `Sthala` | `ContextBoundary` contract |
| Worked-example workflow | `Griha` | `ContextOps`, `ContextBoundary`, `Sthala` |
| Public positioning | `kannanokannan.github.io` | all source repos |
| Assistant/MCP access | `context-stack-mcp` | `context-stack`, source repos |

## Cross-Repo Release Rule

When a change affects more than one repo:

1. Update the source repo first.
2. Update `context-stack` only if terminology or locked decisions changed.
3. Update the website only if public positioning or navigation changed.
4. Update MCP only if assistant-facing discovery or routing changed.
5. Verify live URLs after pushing website or MCP changes.

Do not create a cross-repo commit unless each repo has a clear reason to change.

## Local Workboard

Live work status belongs outside git:

```text
<workspace-root>\STACK_WORKBOARD.local.md
```

That file is for active work, current repo, last push, and next checks. It is not a source artifact and must not be committed.
