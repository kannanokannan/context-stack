---
okf_version: "0.1"
title: Context Stack OKF Bridge
license: Apache-2.0
canonical_sources:
  - ../GLOSSARY.md
  - ../DECISIONS.md
  - ../REPO_MAP.md
  - ../STACK_MANAGEMENT.md
---

# Context Stack OKF Bridge

This directory exposes the Context Stack control-plane knowledge in an OKF-style layout.

It is a bridge, not a second source of truth. Canonical definitions, decisions, and repo ownership still live in:

- [GLOSSARY.md](../GLOSSARY.md)
- [DECISIONS.md](../DECISIONS.md)
- [REPO_MAP.md](../REPO_MAP.md)
- [STACK_MANAGEMENT.md](../STACK_MANAGEMENT.md)

## Entry Points

- [Family doctrine](family-doctrine.md)
- [Control plane](control-plane.md)
- [ContextOps](projects/contextops.md)
- [ContextBoundary](projects/contextboundary.md)
- [Sthala](projects/sthala.md)
- [Griha](projects/griha.md)
- [ContextBoundary and Sthala relationship](relationships/contextboundary-sthala.md)
- [Egress Tier](terms/egress-tier.md)
- [Authority Over Action](authority-over-action.md)

## Use

Agents may use this folder as a machine-readable navigation layer for the stack.

When a concept here conflicts with a canonical source, the canonical source wins.
