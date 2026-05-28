# context-stack

Canonical coordination layer for three sibling open-source AI governance projects.

| Project | Question it answers | Status |
|---------|-------------------|--------|
| [ContextOps](https://github.com/kannanokannan/ContextOps) | How does an org govern its AI context? | v0.1 active |
| [ContextBoundary](https://github.com/kannanokannan/ContextBoundary) | Where is data allowed to go? | v0.1 active |
| [Sthala](https://github.com/kannanokannan/Sthala) | Where does the AI actually run? | v0.1 Alpha |
| [Griha](https://github.com/kannanokannan/Griha) | Product layer — inherits all three principles | Proof of concept |

Griha is the product layer above the three governance projects — it inherits ContextOps, ContextBoundary, and Sthala principles in a working system.

All Apache 2.0. All at github.com/kannanokannan.

## What This Repo Does

- **GLOSSARY.md** — single source of truth for all terminology used across the three projects
- **DECISIONS.md** — locked cross-project decisions log with dates
- **CLAUDE.md** — agent briefing for any LLM working across the stack

## What This Repo Does Not Do

- No implementation detail (lives in each project repo)
- No roadmap or backlog (lives in Drive)
- No SaaS, no product, no vendor lock-in

## Relationships

```
ContextOps          → governs organisational AI context lifecycle
ContextBoundary     → governs where data is allowed to flow (horizontal layer)
Sthala              → one compliant on-premise implementation under ContextBoundary
```

ContextBoundary is deployment-agnostic. Sthala is one vertical that consumes it.
Do not conflate the three.
