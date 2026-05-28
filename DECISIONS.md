# DECISIONS.md — Cross-Project Locked Decisions

Locked decisions that govern all three projects. Dated. Do not revert without explicit discussion.

---

## 2026-05-27 — ContextBoundary

**Decision:** Tier numbering is egress-centric and locked.
- Tier I = never leaves (most restrictive)
- Tier III = explicit API escalation (least restrictive)
- Lower number = higher protection
- Do not invert this under any circumstances

**Decision:** Scope is deployment-agnostic.
- ContextBoundary governs egress from any AI deployment — cloud, on-prem, hybrid, edge
- Do not anchor language to "local AI" or "on-prem AI"
- Sthala is a consumer of ContextBoundary, not its scope

**Decision:** Version label is "v0.1" — no "Draft" suffix, ever.

**Decision:** Repo name stays "ContextBoundary".
- Disambiguation line added to README: not the DDD/Event Storming term, not the UIKit API

---

## 2026-05-27 — Cross-Project

**Decision:** "Privacy tier" is banned language across all three projects.
- Use "Egress Tier" as the primary label

**Decision:** Sthala is one compliant vertical implementation under ContextBoundary.
- Sthala is not a peer of ContextBoundary
- Sthala consumes ContextBoundary's egress contract

---

## Cross-Project Anti-Decisions (Standing)

These are permanent constraints across all three projects:

- None of the three projects is a SaaS product
- None replaces ITIL, TOGAF, COBIT, or NIST AI RMF
- None is vendor-specific or tied to a cloud provider
- ContextOps does not apply below Maturity Level 2
- Services firms are distribution channels, not competitors
- No new tooling required — the stack overlays existing enterprise tools
