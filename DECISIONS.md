# DECISIONS.md — Cross-Project Locked Decisions

Locked decisions that govern every repository in the Context Stack. Dated. Do not revert without explicit discussion. Dated entries are history: a later entry supersedes an earlier one, it does not edit it.

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

## 2026-07-16 — Agent Authority Promoted to Public Module Status

**Decision:** Agent Authority is part of the public stack model, as a module — not a layer.
- Supersedes the 2026-06-14 restriction ("AgentAuthority is not part of the public stack model"), which was overtaken by the 2026-07-06 publication of the module in ContextOps, ContextBoundary, and okf/.
- ContextOps `agent-authority.md` owns the governance definition (A1–A4: accountable ownership, Autonomy Tier, Least Agency, Tool Supply Policy).
- ContextBoundary `agent-authority-enforcement.md` owns the runtime controls (E1–E3: identity at invocation, autonomy-tier gating, tool supply-chain filtering).
- okf/authority-over-action.md is the doctrine entry; canonical source remains ContextOps.
- Agent Authority is NOT a fourth governance pillar and NOT a new stack layer. It extends existing pillars.
- Canonical terms registered in GLOSSARY.md same date.

---

## 2026-07-27 — Stack Maturity Snapshot

**Decision:** The Stack Maturity Snapshot lives in `context-stack` as a purely derivative control-plane view.
- It aggregates the defined pillar ladders by their lowest defined level and adds no requirements of its own.
- ContextOps retains ownership of organizational maturity; ContextBoundary retains ownership of runtime maturity.

---

## 2026-09-15 — Composition

**Decision:** The Context Stack is the specification layer. Three repositories are reference implementations that apply it.
- ContextOps and ContextBoundary are the specification layer. contextboundary-gw, Sthala and Griha are reference implementations that apply it.
- The canonical statement is COMPOSITION.md. The machine-readable copy is `stack.yaml` -> `composition`. Changing the composition means changing DECISIONS.md, COMPOSITION.md and stack.yaml in one change.
- context-stack (control plane), context-stack-mcp (access path) and kannanokannan.github.io (publishing surface) are part of the program, not of the composition.
- Retired: "three sibling governance projects", and any framing that puts Griha, or anything else, above the stack.
- Supersedes the 2026-06-14 v0.2 baseline line "Griha remains product/workflow proof-of-concept". Griha is a reference implementation: a worked example for home and edge.
- Where an earlier entry says "all three projects", it means the specifications and the reference implementations.

**Decision:** A repository may describe itself. It may not describe the stack's shape.
- The files permitted to state the shape are enumerated in `stack.yaml` -> `composition.canonical_surfaces`, and they state it in the canonical words.

Ratified 2026-09-15. Published in COMPOSITION.md before this entry existed; recorded here so the decision log and the composition agree.

---

## Cross-Project Anti-Decisions (Standing)

These are permanent constraints across all three projects:

- None of the three projects is a SaaS product
- None replaces ITIL, TOGAF, COBIT, or NIST AI RMF
- None is vendor-specific or tied to a cloud provider
- ContextOps does not apply below Maturity Level 2
- Services firms are distribution channels, not competitors
- No new tooling required — the stack overlays existing enterprise tools
