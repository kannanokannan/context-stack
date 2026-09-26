# context-stack

Control plane for the Context Stack: canonical terminology, locked decisions, the composition, and stack management.

Current coordination baseline: v0.2. Individual project versions remain listed below.

## The Problem

Modern AI systems let interpretation, decision-making, and execution share one trust boundary. That lets probabilistic systems directly own deterministic consequences — the root cause of prompt injection, unsafe automation, context contamination, and authority confusion.

The context-stack separates interpretation from authority: intelligence proposes, governance validates, execution authorizes. Intelligence can suggest anything. Authority stays deterministic.

---

| Project | Kind | Role | Status |
|---------|------|------|--------|
| [ContextOps](https://github.com/kannanokannan/ContextOps) | Specification | Organizational context governance | v0.1 active |
| [ContextBoundary](https://github.com/kannanokannan/ContextBoundary) | Specification | Data egress and action governance | v0.1 active |
| [contextboundary-gw](https://github.com/kannanokannan/contextboundary-gw) | Reference implementation | Reference gateway and conformance suite | v1.1.0 |
| [Sthala](https://github.com/kannanokannan/Sthala) | Reference implementation | Governed runtime placement | v0.1 Alpha |
| [Griha](https://github.com/kannanokannan/Griha) | Reference implementation | Worked example for home and edge; applies Sthala's narrate/compute constraint | Proof of concept |

ContextOps and ContextBoundary are the specification layer. contextboundary-gw, Sthala and Griha are reference implementations that apply it. See [COMPOSITION.md](COMPOSITION.md).

All Apache 2.0. All at github.com/kannanokannan.

## What This Repo Does

- **GLOSSARY.md** — single source of truth for all terminology used across the stack
- **DECISIONS.md** — locked cross-project decisions log with dates
- **CLAUDE.md** — agent briefing for any LLM working across the stack
- **STACK_MANAGEMENT.md** — operating model for managing the repos as one stack
- **REPO_MAP.md** — repo ownership boundaries
- **stack-maturity-snapshot.md** — derivative cross-project maturity view
- **RELEASE_CHECKLIST.md** — pre-flight and release checks
- **okf/** — OKF-style bridge for agent-readable navigation; canonical sources remain the files above

## OKF Bridge

The `okf/` folder exposes the stack's control-plane knowledge in an Open Knowledge Format style layout for agents.

This is a bridge, not a new source of truth. The canonical sources remain `GLOSSARY.md`, `DECISIONS.md`, `REPO_MAP.md`, and `STACK_MANAGEMENT.md`.

Use `okf/index.md` as the agent-readable entry point for:

- family doctrine
- project roles
- ContextBoundary / Sthala relationship
- Egress Tier terminology
- links back to canonical control-plane files

Shared stack meaning belongs here in `context-stack`. Repo-local OKF folders, if added later, should contain only repo-owned domain knowledge and should link back to this central bridge.

## What This Repo Does Not Do

- No implementation detail (lives in each project repo)
- No roadmap or backlog (lives in Drive)
- No SaaS, no product, no vendor lock-in

## Relationships

```
ContextOps          → governs organisational AI context lifecycle
ContextBoundary     → governs where data is allowed to flow (horizontal layer)
contextboundary-gw  → reference gateway that enforces ContextBoundary deterministically
Sthala              → governed runtime placement; consumes ContextBoundary's egress contract
Griha               → worked example for home and edge; applies Sthala's narrate/compute constraint
```

ContextBoundary is deployment-agnostic. Sthala consumes it; it is not its scope.
Do not conflate them.
