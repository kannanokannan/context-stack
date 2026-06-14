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

## 2026-06-14 — Planning and Decision Split

**Decision:** Public repositories expose locked decisions only.
- Cross-project decisions that are confirmed and stable belong in this file
- Draft strategy, work sequencing, uncertainty, drift checks, and correction notes stay in private local planning files
- Public repo files must not become roadmaps, backlogs, or working todo lists

**Decision:** context-stack remains the public coordination layer.
- It owns canonical terminology, locked relationship decisions, and cross-stack framing
- It does not own implementation detail for individual pillar repos
- It does not publish unconfirmed stack changes before they are explicitly locked

---

## 2026-06-14 - v0.2 Applied-Use-Case Baseline

**Decision:** v0.2 confirms the current public stack model.
- ContextOps governs AI context lifecycle, ownership, provenance, freshness, and renewal
- ContextBoundary governs egress, capability exposure, invocation controls, approval, denial, and audit
- Sthala remains governed runtime placement and implementation under ContextBoundary
- Griha remains product/workflow proof-of-concept, not a fourth governance pillar

**Decision:** v0.2 introduces no new public layer.
- AgentAuthority is not part of the public stack model
- Authority placement is not a public Sthala term
- Candidate terms stay private or repo-local until a later decision promotes them

---

## Cross-Project Anti-Decisions (Standing)

These are permanent constraints across all three projects:

- None of the three projects is a SaaS product
- None replaces ITIL, TOGAF, COBIT, or NIST AI RMF
- None is vendor-specific or tied to a cloud provider
- ContextOps does not apply below Maturity Level 2
- Services firms are distribution channels, not competitors
- No new tooling required — the stack overlays existing enterprise tools
