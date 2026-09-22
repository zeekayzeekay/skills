---
name: delivery-mode-engineering
description: Calibrate and enforce delivery rigor during substantial new or ongoing project or module work, including scoping, specs, PRDs, plans, implementation, reviews, and promotion. Use for spikes, personal dogfood, pilots, MVPs, and work whose future product ambitions are inflating today's bar. Excludes routine isolated bug fixes that do not change the initiative's delivery contract.
---

# Delivery-mode engineering

The declared **mode** sets today's acceptance bar. Build a **tracer**: the thinnest end-to-end path that answers the proof question for the named user. Hold the reachable **floor**. A future ambition may earn a narrow **seam**; it does not activate future machinery. Keep only concrete deferred obligations on the **ledger**, each behind a named **trigger**.

## Start the run

1. Identify the initiative and read its `ACTIVE` section in root `DELIVERY.md`, if present. Use an explicit mode already stated by the user. Otherwise infer Personal Dogfood when one developer is the named user in one environment; ask once only when plausible modes would materially change the work. Read [modes](references/modes.md) when choosing or challenging a mode.
2. Set authority per action:
   - `DRAFT`: the request authorizes analysis, advice, planning, or review only. Return proposals and findings without changing repository files, checks, rules, or implementation.
   - `APPLY`: the request explicitly authorizes creating or changing an artifact or implementation. Change only that scope: permission to write a plan is not permission to edit code; permission to review is not permission to fix.
3. For Personal Dogfood or higher, and for any multi-session or retained Spike, create or update the contract and its durable instruction-file pointer when repository changes are authorized, using [the contract procedure](references/contract.md). A truly disposable one-session Spike keeps its authority, mode, and proof question in the response or an explicitly requested throwaway artifact and creates no governance files. Under `DRAFT`, report a required missing contract or pointer instead of installing one.
4. If an existing binding rule or check conflicts with the chosen mode, follow [reconciliation](references/reconcile.md). The existing obligation remains until its re-tiering is approved and applied.

## Carry the delivery context

This skill owns delivery calibration; other skills apply it within their current task, not as an extra lifecycle phase. Reuse the active contract, settled decisions and claim IDs. A routine isolated fix inherits them without a new mode interview or governance files.

Across a spec, ticket, implementation, handoff or independent review, carry a reference to the matching contract section and the relevant current facts: supported workflows and inputs, required core outcomes and evidence, named users, environment and exposure, independent human contributors, accepted limitations, justified growth boundaries, and the readiness gate. Reference existing artifacts instead of copying the whole contract. If the receiving agent cannot access a source, include the necessary authorized excerpt and its origin. Label unresolved facts as unresolved.

Core quality is part of the proof: required retrieval, reasoning, decisions, processing and evaluations must produce the agreed useful results. Name observable outcomes that would expose a wrong result; merely running end to end or passing self-confirming tests is insufficient. Mode scales operational promises and evidence breadth, not the truth of these outcomes. An ordinary defect outside the agreed proof and reachable floor can still be an iteration.

Future ambition stays separate from present exposure. Parallel agents working for one owner are not additional human maintainers or product users. A second independent contributor changes coordination needs; a second user or public surface changes reachable outcomes. Apply the corresponding current obligations without importing every production practice.

## Classify current work

Every executable item is exactly one of:

- `PROOF`: removing it would prevent the named user from completing the declared happy path now, or prevent the build from producing observable evidence that answers the proof question. Convenience, generic quality, and possible future use fail this counterfactual.
- `FLOOR`: protects a presently reachable outcome. Record its asset, reachable path, consequence, invariant, cheapest adequate control now, and evidence.
- `SEAM`: passes the **OPTION** predicate below and adds only the named boundary.

The **OPTION** predicate, used for both `SEAM` and reconciliation's `PRESERVE`, requires all of:

1. A specific, credible future change is named.
2. Without the boundary, reversal would impose a concrete high cost on the current design or retained data.
3. One small boundary with one implementation avoids that cost now.
4. Its current cost is proportionate to the likely avoided reversal and fits the contract's seam ceiling. The ceiling is a maximum, never a target; zero is valid.

When the request names a future audience beyond the present named user (a team, customers, tenants, an installed or hosted product), read [scale-ready design](references/scale-ready-design.md) before classifying seams. Its day-0 rules are the boundaries such an ambition normally earns (each still passes the OPTION predicate above); its ledger names what the ambition does not earn and the trigger for each.

`LEDGER` is not executable work. Admit an item only when it is (a) concrete debt created by this slice, (b) a specific future task the user explicitly asks to track, or (c) a stronger mechanism deferred from a `FLOOR` invariant held now. Give every admitted item its observable trigger and source. Future ambition, generic promotion capabilities, and work admitted merely because a plausible trigger can be invented are omitted; promotion rediscovers real gaps from the target mode. An unclassified item is either classified or removed.

Make classification visible: prefix every executable item with its stable claim ID and class, such as `[P-001 PROOF]`, `[F-001 FLOOR]`, or `[S-001 SEAM]`. Prefix every manual check, automated test, metric, and evidence line with each `[P-###]` or `[F-###]` claim it supports. Use as many checks as the present claim warrants and none without an explicit mapping. Spike evidence may be disposable automation.

## Hold the floor

State safety as outcomes for the code and paths reachable now:

- retained irreplaceable data has a tested recovery copy independent of the currently credible local failure;
- sensitive data and credentials stay within their declared boundaries;
- paid use cannot exceed the user's explicit cap;
- destructive or externally visible effects cannot exceed clear current intent;
- untrusted input cannot cause unintended execution, loading, path escape, or network access;
- reachable interfaces are limited to their declared audience.

A reachable failure earns the cheapest adequate control now. If irreplaceable data is retained, its `FLOOR` must create and test a recovery copy that survives the failure it claims to cover, including device loss when the sole copy would otherwise live on that device. Otherwise the plan must avoid retaining that data. Transactional writes, idempotency, and a copy beside a migration are integrity controls; they do not establish recovery from loss of the device. Stronger mechanisms wait behind their trigger.

## Evidence accuracy in every mode

Personal Dogfood and Spike may reduce ceremony, coverage breadth and operational promises. They do not make a false privacy, integrity, spending, lifecycle or audit statement acceptable on a reachable path. Map these checks to the existing PROOF/FLOOR claim; do not add a new mode or a universal failure matrix.

For changed truth-bearing behavior, use the `assurance-case` skill when installed. It owns the compact claim/state/evidence matrix and falsification procedure. Without it, name the governing claim, relevant transition or mixed/stale/failure state, decisive observable, and the focused check that would fail if the claim were false. Keep the record in the existing plan/contract; do not create a second governance document.

Readiness evidence must distinguish implemented, tested, source-inspected and unvalidated claims. Passing tests alone do not show that their assertions detect the claimed defect. Keep unknown/unpriced cost distinct from zero, and missing checks distinct from successful checks. A deferred stronger mechanism is different from an incorrect fact reported by the mechanism already in use.

Exercise real dependencies only within current authority. A live check needing deployment, a profile/grant change, a migration, private-data access or spend remains unvalidated until separately authorized; neither a readiness gate nor this skill supplies that permission. Report the precise incomplete gate without claiming readiness. Respect explicit owner-approved qualifications in the active contract, and disclose the resulting limits.

## Choose one branch

### Plan or specify

Draft the contract and order a tracer against the real dependency where the main uncertainty lives. Put only visibly ID-prefixed `PROOF`, `FLOOR`, and qualifying `SEAM` items in the executable plan; keep the ledger separate. Prefix every test, metric, and evidence item with the claim ID it proves. Make the first end-to-end run the earliest feasible milestone. Under `APPLY`, persist the requested artifacts and contract; under `DRAFT`, return them without repository mutation.

Complete when the authority and mode are explicit, every executable item visibly carries a stable class/claim ID and passes its classifier, every evidence item visibly carries its `PROOF` or `FLOOR` ID, and every ledger row passes the admission rule.

### Implement

Execute the approved tracer and exercise the uncertain dependency for real. Classify any newly discovered scope before doing it. Stop at the selected mode's readiness gate in [modes](references/modes.md): `PROOF_ANSWERED` for Spike, `DOGFOOD_READY` for Personal Dogfood, or the contract's declared `MODE_READY` outcomes for Limited Pilot, Public MVP, and Production. A seam never determines readiness. Hand over the run instructions, evidence, and separate ledger; `VALIDATED` is the owner or users' judgment after use, never the agent's.

Complete when the selected readiness gate is demonstrated with its mapped evidence and no blocking claim for that gate remains open.

### Review

Treat a review-only request as `DRAFT`. Apply one current-delivery disposition to each material finding, independently of severity and whether it is reproduced, source-supported, an evidence gap or unconfirmed:

| Disposition | Meaning now |
|---|---|
| `PROOF_BLOCKER` | A required core outcome or binding current acceptance gate fails, or the evidence needed to claim the selected proof/readiness is materially insufficient. |
| `FLOOR_BLOCKER` | A presently reachable floor outcome fails or lacks the evidence necessary to claim its protection. |
| `ITERATION` | A useful improvement to current work that does not prevent the agreed proof or floor from holding. |
| `LEDGER` | A deferred obligation that passes the ledger admission rule above, with its source and observable trigger. |
| `OPTIONAL` | A suggestion with no current acceptance obligation and no admitted ledger obligation; omit it unless useful to the requested review. |

For a blocker, cite the governing current requirement or claim, reachable input/state or failed explicit gate, consequence, and decisive evidence or missing observable. Judge actual supported use and exposure: an unusual input can block if it reaches a floor violation, while a hypothetical future caller does not establish present reachability. Severity alone cannot supply that missing path. Preserve binding repository requirements until reconciliation is approved and applied.

Missing tests are evidence gaps, not automatically behavioral defects. If an essential core or floor claim remains unsubstantiated, block that readiness claim. If adequate decisive evidence already exists and no binding rule requires another durable test, classify the additional test proportionately. Keep unconfirmed concerns distinct from established failures; uncertainty blocks only when it leaves required readiness evidence missing.

A blocker is a recommendation for current work, not authorization to fix it. During authorized implementation, fix blockers and requested in-scope improvements, recheck affected claims, and stop at the selected readiness gate. Report other dispositions without converting them into automatic work. If the same finding recurs without new evidence, or fixes oscillate between interpretations, state the disputed requirement and evidence for resolution before another repair cycle. Do not resolve disagreement by silently lowering a requirement or declaring an unresolved blocker passed.

Complete when every finding is classified and supported; a read-only review leaves the repository unchanged.

### Promote

Enter this branch only when the user explicitly asks to change mode. A trigger firing is a report, not permission. Follow [promotion](references/promotion.md) for the gap analysis, current-mode update, and append-only history.

Complete under `DRAFT` when the gap analysis is delivered. Under `APPLY`, an unfinished target remains promotion-in-progress; promotion completes only after its target readiness gate is evidenced and the target mode is activated.

## Stop-and-correct signals

- An executable item lacks a valid counterfactual, reachable floor consequence, or passing OPTION predicate.
- A task or evidence line lacks its visible stable class/claim ID.
- The ledger contains generic promotion work, even when a plausible future trigger can be named.
- A contract claims `ACTIVE` without a durable binding-file pointer.
- A review or proposal mutates the repository under `DRAFT`.

Correct the classification or authority before continuing.
