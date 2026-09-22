# Reconciling existing repository rules

Use this branch when a chosen mode is lower than a binding instruction, CI gate, contributing rule, decision, or checked-in acceptance bar. Existing obligations and checks remain binding until the user approves a re-tiering and it is applied.

Re-tiering is forward-only by default: it changes what future work must add or prove. Useful code, controls, and tests already built remain in place and may continue supplying evidence without becoming new obligations. A lower mode alone is not a reason to weaken or delete them; removal needs independent evidence of current cost or harm and explicit user authorization.

## DRAFT: build the proposal

1. Inventory every conflicting rule and the check or implementation that enforces it. Quote the exact text with source location, inspect the present code, and distinguish already implemented capability from proposed work. Make no unsupported current-state claim.
2. Assign each constraint a stable `C-###` ID. Preserve existing decision IDs as sources, never renumber IDs, and retain superseded rows in history.
3. Identify the invariant the rule protects, then propose one tier:
   - `NOW`: required by the current `PROOF` counterfactual or a reachable `FLOOR` outcome.
   - `PRESERVE`: passes the same OPTION predicate as a `SEAM`; keep only its smallest boundary or data shape with one implementation.
   - `TRIGGER`: no new implementation or evidence obligation; activate only on the named observable condition. Retain useful implementation and tests that already exist.
   - `REMOVE`: no present value and no credible trigger. Deleting or weakening existing implementation still requires an independent value case and explicit user approval.
4. Include process rules: review depth, ticket/session limits, acceptance inventories, branch policy, and evidence requirements are constraints too.
5. Present the proposed register without changing repository files, checks, plans, or code:

| ID | Source and exact rule | Protected invariant | Observed present state | Proposed tier | Current obligation or trigger | Supersedes |
|---|---|---|---|---|---|---|
| C-001 | `<path:line>`: “…” | <outcome> | <verified fact> | NOW / PRESERVE / TRIGGER / REMOVE | <work kept now or observable trigger> | <decision/row or none> |

The proposal is complete when every conflicting code and process rule has one stable row, every `PRESERVE` passes OPTION, every `TRIGGER` is observable, and the current-state claims are verified.

## APPLY: enact an approved register

Enter only when the user has approved the proposal or supplied an already approved register.

1. Write the approved stable-ID register into the initiative's `DELIVERY.md` section.
2. Amend binding instruction files so their delivery pointer names `DELIVERY.md`. Replace or annotate conflicting commands with their `C-###` tier; keep full trigger text in the register rather than duplicating it.
3. Change future planning and acceptance obligations to match the approved tiers. Preserve useful existing implementation and tests, including evidence stronger than the lower mode requires. Delete or weaken them only when the approved proposal separately identifies their current cost or harm and the user authorizes that cleanup. Preserve checks for `NOW` and the narrow option retained by `PRESERVE`.
4. Mark the contract `ACTIVE`, record approver/date, and run the remaining relevant checks.

Application is complete when no binding sentence commands new deferred machinery, every changed constraint retains its stable history, useful existing capability remains intact unless separately approved for removal, the durable pointer works, and the applicable checks pass.

## Later rules

Classify later proposals from evidence rather than defaulting them to a tier. A reachable proof or floor need is `NOW`; a passing OPTION may be `PRESERVE`; a concrete future condition may be `TRIGGER`; otherwise omit it. A trigger firing is reported to the user and does not itself authorize implementation.
