# Composition of the Context Stack

**Canonical. Ratified 2026-09-15. This file is the only place the stack's shape is defined.**

Every other document in every repository either links here or restates the one-line form below, byte-identical. A repository describes itself; it does not describe the stack's shape.

---

## The one-line form

> ContextOps and ContextBoundary are the specification layer. contextboundary-gw, Sthala and Griha are reference implementations that apply it.

That sentence is canonical. Where a surface needs the shape in one line, it uses exactly that text. The machine-readable copy is `stack.yaml` → `composition.canonical_one_line`.

## In full

The Context Stack is the **specification layer**: ContextOps and ContextBoundary. They stay separate on purpose — context ownership and data movement should not be collapsed into one control model.

Three repositories are **reference implementations** that apply that specification at different scales:

| Repository | Kind | Applies | Role |
|---|---|---|---|
| `ContextOps` | specification | — | Organizational context governance |
| `ContextBoundary` | specification | — | Data egress and action governance |
| `contextboundary-gw` | reference implementation | ContextBoundary | Reference gateway and conformance suite |
| `Sthala` | reference implementation | ContextOps, ContextBoundary | Governed runtime placement |
| `Griha` | reference implementation | ContextOps, ContextBoundary | Worked example for home and edge; applies Sthala's narrate/compute constraint |

Three further repositories are part of the program but are not part of the composition — they carry no specification and implement none:

| Repository | Kind | Role |
|---|---|---|
| `context-stack` | control plane | Canonical terminology, locked decisions, stack management |
| `context-stack-mcp` | access path | Assistant-facing MCP endpoint |
| `kannanokannan.github.io` | publishing surface | Public website at context-stack.org |

Specification and implementation are named separately because they are adopted separately. An organization can adopt ContextBoundary without running the gateway.

## What is not true

Two statements were retired on 2026-09-15 and must not reappear:

- **There are not "three sibling governance projects".** There are two specifications.
- **Nothing sits "above" anything.** Griha is not a product layer above the stack; it is a reference implementation beside the other two.

## Why this file exists

Before this file, six repositories each held their own paraphrase of the shape. The decision was ratified on 2026-09-15 and recorded as landed; an independent audit on 2026-09-22 found it contradicted in 45 lines across six repositories, 35 of which the then-current check could not detect. Six paraphrases drift. One statement, referenced, does not.

The rule that follows from it:

> **A repository may describe itself. It may not describe the stack's shape.**

The exceptions are enumerated in `stack.yaml` → `composition.canonical_surfaces`. Those files may state the shape, and a check asserts they state it identically.

## Changing this

The composition is a locked decision. Changing it means editing `DECISIONS.md`, this file and `stack.yaml` in one change, and re-running the stack verifier. Editing any other surface to disagree with this file is a defect, not a change.
