# Delivery modes

Use this reference when a mode is absent, ambiguous, or being changed. “MVP,” “POC,” and “prototype” are overloaded; select the actual operating promise.

| Mode | Purpose | Present bar | Readiness gate |
|---|---|---|---|
| **Spike** | Answer one technical or design question | Disposable implementation; manual evidence or disposable automated evidence; no obligation to build a durable test suite | `PROOF_ANSWERED`: the proof question has an observable answer; retain or discard the code independently |
| **Personal Dogfood** | The named owner uses and evolves it with real data | One named user, one declared environment, one happy path, reachable floor outcomes, reproducible start, and evidence mapped only to present proof or floor claims | `DOGFOOD_READY`: the named user can start it, complete the real happy path, observe the proof answer, and every reachable floor invariant holds |
| **Limited Pilot** | A few named trusted users try it | Recovery for retained pilot data, controlled onboarding/access, diagnostics for reachable failures, and safety for the actual exposed surface | `MODE_READY`: every pilot acceptance and readiness outcome declared in the active contract is evidenced |
| **Public MVP** | Validate value with outside users | Minimal features plus a production baseline for every public surface, non-owner data, paid effect, and support promise actually offered | `MODE_READY`: every public-MVP acceptance and readiness outcome declared in the active contract is evidenced |
| **Production** | Meet explicit operational promises | Declared scale, reliability, recovery, support, observability, deployment, and security guarantees | `MODE_READY`: every production acceptance and readiness outcome declared in the active contract is evidenced |

Rules across modes:

- Public MVP is minimal in features, not in safety for public users and exposed surfaces.
- Mode applies per initiative or module. A dogfood component touching production users or data inherits the higher reachable floor.
- Current mode and future ambition are separate. Future ambition can support a qualifying OPTION seam; it activates no work.
- Personal Dogfood is the default only when the developer is the sole named user in one environment and nothing in the request implies outside users or exposure.
- A routine isolated bug fix inherits an existing contract and does not reopen mode selection.
- Readiness is an evidence claim. `VALIDATED`, where relevant, is reserved for the owner or users after actual use.
- Every mode requires truthful evidence on reachable paths; lowering ceremony never changes unknown cost to zero, skipped validation to success, or an incorrect privacy/integrity receipt to acceptable debt. Use the evidence-accuracy section in `SKILL.md` without expanding the current gate.
- A lower mode changes future obligations. It does not by itself justify weakening or deleting useful capabilities or tests already built.
