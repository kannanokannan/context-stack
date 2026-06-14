# Repository Map

This is the ownership map for the Context Stack.

Use this file when deciding where a change belongs.

## Canonical Workspace

```text
G:\My Drive\ai-stack
```

## Repositories

| Local folder | GitHub repo | Role |
|--------------|-------------|------|
| `context-stack` | `github.com/kannanokannan/context-stack` | Canonical terminology, locked decisions, stack management |
| `ContextOps` | `github.com/kannanokannan/ContextOps` | Enterprise AI context governance framework |
| `ContextBoundary` | `github.com/kannanokannan/ContextBoundary` | AI data egress governance specification |
| `Sthala` | `github.com/kannanokannan/Sthala` | Governed AI runtime placement reference framework |
| `Griha` | `github.com/kannanokannan/Griha` | Product and workflow layer above the stack |
| `kannanokannan.github.io` | `github.com/kannanokannan/kannanokannan.github.io` | Public website at `context-stack.org` |
| `context-stack-mcp` | `github.com/kannanokannan/context-stack-mcp` | MCP endpoint for assistant-facing access |

## Ownership Boundaries

### `context-stack`

Belongs here:

- Canonical glossary
- Locked cross-project decisions
- Repo ownership map
- Cross-repo release checklist
- Agent instructions for cross-project work

Does not belong here:

- Implementation details
- Project-specific roadmap
- Active backlog
- Temporary research notes

### `ContextOps`

Belongs here:

- Context governance framework
- Triad: People, Process, Context
- Spine: Capture, Curate, Supply, Renew
- Maturity model
- Named practices
- Context governance roles
- Self-assessment agent

Does not belong here:

- Egress tier policy
- Runtime implementation
- Website navigation
- MCP server code

### `ContextBoundary`

Belongs here:

- Egress Tier definitions
- Vendor zones
- Jurisdictional audit profiles
- Data movement policy
- ContextOps bridge mapping

Does not belong here:

- ContextOps maturity model
- Sthala runtime implementation details
- Product workflow copy

### `Sthala`

Belongs here:

- Runtime placement
- Governed runtime reference architecture
- Narrate/compute split
- Pipeline specification
- Build-time constraints

Does not belong here:

- General egress governance doctrine
- ContextOps practices
- Website SEO pages

### `Griha`

Belongs here:

- Product workflows
- User-facing governed AI experience
- Practical adoption layer
- Policy-bounded execution in product form

Does not belong here:

- Canonical terms
- Core governance doctrine
- Egress tier definitions

### `kannanokannan.github.io`

Belongs here:

- `context-stack.org`
- Public navigation
- Public guide pages
- Sitemap
- Search verification files
- LLM and crawler discoverability

Does not belong here:

- Core framework changes
- Repo-specific doctrine
- MCP server implementation

### `context-stack-mcp`

Belongs here:

- MCP endpoint
- Tool/resource exposure
- Assistant-facing routing
- Delivery access prompts

Does not belong here:

- Canonical terms
- Public website pages
- Source framework text unless mirrored from source repos

## Rule Of Thumb

If the change defines what the stack means, start in `context-stack`.

If the change defines how one pillar works, use that pillar repo.

If the change explains the stack to the public, use `kannanokannan.github.io`.

If the change helps assistants use the stack inside workflow, use `context-stack-mcp`.
