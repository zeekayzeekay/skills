# Promotion

Use this branch only when the user explicitly asks to change the initiative's mode. A trigger firing is evidence for a promotion decision, not permission to promote or implement.

## Gap analysis

1. Read the `ACTIVE` contract, current implementation, and target bar in [modes](modes.md).
2. Recompute the gap from verified current state; generic higher-mode capabilities belong here when promotion is requested, never in an earlier dogfood ledger. List only:
   - target-mode outcomes not satisfied by the verified current build;
   - ledger obligations whose recorded triggers have actually fired;
   - new floor outcomes made reachable by the requested audience, exposure, data, effects, or environment.
3. Give each gap a `PROOF`, `FLOOR`, or qualifying `SEAM` classification and map its evidence. Omit untriggered future inventory.
4. Under `DRAFT`, return the gap analysis without repository mutation.
5. Under `APPLY`, record `Promotion in progress` with target mode, requester/date, and open gap IDs while leaving `Current mode` and Mode history unchanged. Implement only the approved gaps through the implementation branch.
6. When every target-mode readiness outcome has mapped evidence and no target blocker remains, set `Current mode` to the target, append one Mode history row with date, from/to modes, decider, and reason, then clear `Promotion in progress`. Preserve earlier rows.

Planning or starting promotion does not complete it. Promotion is complete only when the target readiness gate is evidenced, the current mode and append-only history agree, and no untriggered item entered the plan.

## Common trigger examples

These are prompts for a promotion-time gap analysis, not an automatic checklist and not candidates for pre-populating a ledger:

| Observable trigger | Possible newly reachable outcome |
|---|---|
| First non-owner user | Identity, access, and recovery appropriate to that user |
| Public endpoint | Safety and abuse controls for that exposed surface |
| Retained data becomes irreplaceable | Tested backup, migration, and recovery outcomes |
| Paid operation runs for others or at material scale | Per-user caps, metering accuracy, and abuse containment |
| Second operating system is selected | Packaging and behavior for that named platform |
| Remote or unattended execution is enabled | Bounded retries, failure visibility, and operator control |
| Public paid release is scheduled | Distribution, updates, legal, support, and privacy promises actually offered |
| Measured workload misses its target | Profiling and capacity work against that workload |
| Untrusted input reaches execution, loading, or path selection | Containment for that reachable path |

Promotion begins from the product the user has validated, not from a hypothetical production system.
