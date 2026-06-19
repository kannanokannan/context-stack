---
type: relationship
title: ContextBoundary and Sthala
canonical_source: ../../DECISIONS.md
related:
  - ../projects/contextboundary.md
  - ../projects/sthala.md
  - ../terms/egress-tier.md
---

# ContextBoundary and Sthala

ContextBoundary is the horizontal egress governance layer.

Sthala is a governed runtime placement reference that consumes ContextBoundary's egress contract.

Do not conflate them:

- ContextBoundary governs where data is allowed to flow.
- Sthala governs how a compliant runtime is placed and constrained.
- Sthala is a consumer of ContextBoundary, not a peer layer beside it.
