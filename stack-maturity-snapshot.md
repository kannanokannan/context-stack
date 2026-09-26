# Stack Maturity Snapshot

## Purpose

The stack has grown detailed within each project. An adopter needs one plain answer to "where does my organization stand overall" without reading every project's documentation first. This file provides that answer by aggregating existing ladders, not by adding.

## What This Is Not

This is not a new framework layer or a maturity model. It adds no requirements and introduces no criteria of its own. It is not a conformance or certification scheme and has no badge. If it ever required its own criteria, it would cease to be a snapshot.

## Pillar Ladders

| Pillar | Ladder | Range | Authority |
|---|---|---|---|
| ContextOps | Organizational maturity | Levels 1–5 | The [ContextOps repository](https://github.com/kannanokannan/ContextOps) |
| ContextBoundary | Runtime maturity | Levels 0–5 | [maturity-ladder.md](https://github.com/kannanokannan/ContextBoundary/blob/main/maturity-ladder.md) in the ContextBoundary repository |
| Sthala | Not yet defined | — | Open gap; see below |

Griha is excluded: it is a worked example and defines no maturity ladder of its own. Whether it belongs in a future snapshot is an open decision.

## Aggregation Rule

Overall stack standing is the lowest level reached across the defined pillar ladders.

An organization is only as governed as its weakest axis, so aggregation must not average away a gap; the rule is deterministic and involves no scoring, weighting, or judgement.

## Worked Example

**Illustrative only; not a claim about any real deployment.** ContextOps Level 2 with ContextBoundary runtime Level 1 yields a stack standing of Level 1. The stated next step is the specific work that raises the weakest defined pillar.

## Open Gap: Sthala

Sthala has no maturity ladder defined at this time, so the Snapshot aggregates over the defined ladders only. No Sthala ladder is invented here. When Sthala defines one, it is added to the table and enters the aggregation with no change to the aggregation rule.

## Maintenance

When a pillar changes its ladder, the pillar repository is updated first and this file follows, consistent with the [cross-repo release rule](./STACK_MANAGEMENT.md#cross-repo-release-rule).
