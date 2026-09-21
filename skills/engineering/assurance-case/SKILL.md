---
name: assurance-case
description: Build a compact, falsifiable claim-to-evidence map when implementing or reviewing changes to access decisions, integrity checks, cost accounting, lifecycle or audit receipts, provenance, or evidence-status aggregation. Use for mixed outcomes, stale state, alternate exits, and cache behavior that can make a system report the wrong fact. Not a general production-readiness checklist.
---

# Assurance case

A passing test is evidence only if the described defect would make that test fail. This skill owns the claim/state/evidence matrix and falsification rules used by `implement`, `tdd` and `code-review`. It is a bounded reasoning aid, not a new delivery mode or permission to change code.

## Select the claims

Read the actual contract and current code. Select only changed behavior and reachable affected paths that decide or report a consequential fact: permission, integrity, spending, dispatch, provenance or evidence support. Preserve the project's mode and authorized scope. Do not invent a production checklist for a cosmetic change or reopen completed research.

Use existing claim IDs. Keep the map in the working plan or review unless the project requires a durable artifact. A few rows usually suffice:

| Claim / source | Entry point and owning seam | Relevant states / precedence | Decisive observable and counterexample | Evidence / limits |
|---|---|---|---|---|
| Contract reference | Public entry and shared decision | Before → event → after; mixed-state winner | What must be reported or prevented; input that could falsify it | Command + result, source trace, or unvalidated |

List the transitions or precedence rules **before** implementing aggregation. Derive winners from the contract, not enum order. If the contract does not settle a material conflict, ask the user; do not encode a guess as policy.

## Trace and challenge

Follow each selected claim from its public entry through its decision to the returned result and durable record. Cover relevant callers and alternate exits, not just the changed helper. Choose reachable cases from these prompts; do not enumerate a blanket Cartesian product:

- **Mixed outcomes:** success plus contradiction, checked plus unchecked, usable data plus denied data. Does aggregation erase a stronger fact or leave a confident assertion unchanged?
- **Stale state / cache:** changed authority, qualification, integrity or source data. Which checks must run now? Preserve historical provenance while distinguishing original work/cost from this invocation's incremental work/cost; never rebill old usage or label unknown cost zero.
- **Failure boundaries:** preparation, pre-dispatch refusal, uncertain send, provider response, settlement and persistence. Does every actual attempt retain its identity, prepared fields and honest lifecycle, including exceptions after an external effect?
- **Policy and minimization:** do all eligible routes use the same decision and secret gate? Is disclosure built from the actual structured payload, not names, booleans or a proxy?
- **Defaults and loss:** can an omitted field mean free, supported, allowed, complete or zero loss? Do filters, caps and fallbacks retain a reason, count and attributable attempt where promised?

Prefer code that makes false combinations difficult: closed domain vocabularies, separate route method from rank basis, explicit unknown cost instead of a free default, a shared qualification/policy/disclosure seam, one status-precedence function, settlement exceptions carrying the known receipt, and cache APIs that require current authority/integrity checks. Apply only the patterns earned by the changed contract; do not create a framework to satisfy this list.

## Produce evidence

For each material claim, identify a focused test whose assertions would fail for the named counterexample. Use public interfaces, real aggregation/policy/storage where relevant, and fakes at external boundaries. Verify the returned answer **and** its contractual durable/accounting facts, not just that an object exists.

Record red for the intended defect, then green after the fix. An existing passing test may be checked with a small reversible fault injection in an isolated copy. Report exactly what changed, which assertion failed, and that the probe was discarded. Never weaken the test or alter shared user work for a sensitivity demonstration. Broad mutation campaigns are not required.

Static path analysis can substantiate a finding when execution is unavailable; label it as such. An unexecuted reproduction is not a reproduced bug. No live provider, deployment, profile/grant change, migration or private-data access follows from this skill.

## Stop honestly

Report implemented behavior, observed test evidence, source-only conclusions and unvalidated claims separately. A blocked live check is an evidence gap, not permission to run it or a passing gate. Do not claim exhaustive correctness from a bounded review. Keep acceptance tied to the current contract; ordinary defects outside it do not silently become production gates.
