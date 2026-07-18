## Family Doctrine

> Probabilistic intelligence must operate inside deterministic governance boundaries.

This is the unifying principle across ContextOps, ContextBoundary, and Sthala. All three projects exist to implement this doctrine at different layers — organisational governance, data egress control, and execution architecture respectively.

Do not introduce any term, feature, or design decision across the three projects that contradicts this doctrine.

---

# GLOSSARY.md — Canonical Terminology

Single source of truth for all terms used across ContextOps, ContextBoundary, and Sthala.

Before introducing a new term in any project repo, it must be defined here first.

---

## Cross-Project Terms

| Term | Definition | Used In |
|------|-----------|---------|
| Context Stack | The three sibling projects together (ContextOps + ContextBoundary + Sthala) | All |
| Apache 2.0 | The license for all three projects — no exceptions | All |

---

## Griha Terms

| Term | Definition |
|------|-----------|
| Policy-bounded execution | Device or system actions that can only occur after passing deterministic validation and policy checks |
| Approval gate | Human-in-the-loop checkpoint required before high-risk actions execute |
| Provenance | Audit trail recording every intent, validation decision, and device action |
| Product layer | Griha's position in the stack — above the three governance projects, inheriting all their principles |

---

## ContextOps Terms

| Term | Definition |
|------|-----------|
| Triad | The three pillars of ContextOps: People · Process · Context |
| Spine | The four-stage lifecycle: Capture → Curate → Supply → Renew |
| Capture | Spine stage 1 — identifying and acquiring context inputs |
| Curate | Spine stage 2 — validating, enriching, and structuring context |
| Supply | Spine stage 3 — delivering context to AI systems at runtime |
| Renew | Spine stage 4 — retiring, refreshing, and governing context over time |
| Maturity Level | Five-level scale (1–5). ContextOps applies at Level 2 and above only |
| Context Architect | Role: designs the context governance structure |
| Context Owner | Role: accountable for a context domain |
| Context Curator | Role: maintains and validates context quality |
| AI Onboarding Manager | Role: manages AI system intake and context bootstrapping |
| Agent Operations Lead | Role: runs day-to-day agent context operations |
| Context Freshness Score | Metric: measures how current and valid the context supply is |
| Pilot-to-Production Conversion Rate | Metric: % of AI pilots that reach production |
| Two-Cost-Line Ratio | Metric: ratio of context production cost to context failure cost |
| Two-Cost-Line Diagnostic | Tool: identifies whether context costs or failure costs dominate |
| Agent Authority | Module (2026-07-06): governance of what an agent is permitted to do and who is accountable. Governance defined in ContextOps `agent-authority.md`; enforced by ContextBoundary. A module, not a stack layer |
| Agent Accountability | Every agent has a single named accountable human owner. An agent with no accountable owner is out of policy by definition (A1) |
| Autonomy Tier | Classification of how much an agent may do before a human decision is required — Trust Classification applied to action (A2). Distinct from Egress Tier |
| Least Agency | Default stance: minimum Autonomy Tier and minimum tool surface sufficient for purpose; escalation is explicit, owned, time-bound (A3) |
| Tool Supply Policy | Which tool/MCP sources an agent may consume, governed as a supply chain by source trust classification (A4) |

---

## ContextBoundary Terms

| Term | Definition |
|------|-----------|
| Egress Tier | Classification of where data is permitted to flow. Use "Egress Tier" — never "Privacy Tier" |
| Tier I | Never leaves the system. Most restrictive. Applies to sovereign data, PII, regulated records |
| Tier II | Anonymised aggregates only, with consent. Applies to behavioural metrics, derived insights |
| Tier III | Explicit per-call API escalation. Least restrictive. Applies to public data, sanctioned lookups |
| Customer Sovereign Zone | Zone 1 — data that never leaves the customer boundary |
| AMS / Service Vendor Zone | Zone 2 — managed service providers operating in-boundary |
| Product Vendor Zone | Zone 3 — software vendors with scoped data access |
| Compute Vendor Zone | Zone 4 — infrastructure and cloud compute providers |
| LLM Vendor Zone | Zone 5 — model inference providers |
| Context Isolation | The property of keeping context within its permitted zone |
| Agent-External Attestation | Verification that an agent's egress actions conform to the declared tier |
| Deployment-Agnostic | ContextBoundary governs egress regardless of where the AI runs (cloud, on-prem, hybrid, edge) |
| GDPR Audit Profile | ContextBoundary's first jurisdiction implementation — maps tiers to GDPR obligations |
| Identity at Invocation | Agent Authority control E1: every invocation bound to the calling agent's accountable identity; unbindable invocations are blocked |
| Autonomy-Tier Gating | Agent Authority control E2: discovery, invocation, and approval requirements gated on the agent's Autonomy Tier |
| Tool Supply-Chain Filtering | Agent Authority control E3: untrusted-source tools/MCP capabilities filtered at discovery, before invocation is possible |

---

## Sthala Terms

| Term | Definition |
|------|-----------|
| Six-Layer Pipeline | Sthala's core processing sequence: Ingest → Extract → Verify → Compute → Narrate → Egress |
| Ingest | Pipeline layer 1 — receiving raw data inputs |
| Extract | Pipeline layer 2 — LLM-driven structured extraction from raw inputs |
| Verify | Pipeline layer 3 — validation of extracted output before computation |
| Compute | Pipeline layer 4 — deterministic code execution only. No LLMs at this layer |
| Narrate | Pipeline layer 5 — LLM-driven synthesis and explanation of computed results |
| Egress | Pipeline layer 6 — output delivery under ContextBoundary tier rules |
| Narrate/Compute Split | Core architectural constraint: LLMs handle Extract and Narrate only. All computation is code. Enforced at build time by linter |
| Recipe | A vertical deployment unit — a pre-configured pipeline for a specific domain and country |
| Profile | A YAML configuration preset defining model selection, hardware tier, and compliance posture |
| Airgapped | Sthala's default posture — no external network calls unless explicitly configured |

---

## Banned Terms

Do not use these in any project repo. They are either imprecise, misleading, or actively harmful to the project positioning.

| Banned Term | Use Instead | Reason |
|-------------|-------------|--------|
| Privacy Tier | Egress Tier | Egress-centric model, not privacy-centric |
| Local AI | (describe the deployment specifically) | Too narrow, anchors ContextBoundary to on-prem |
| On-prem AI | (describe the deployment specifically) | Same as above |
| Sovereign AI | (avoid or be specific) | Becoming compliance theatre per 2026 community feedback |
| Draft | (omit — use version number only) | Version labels never carry "Draft" suffix |
| Privacy tier | Egress Tier | Case variant of the same ban |
