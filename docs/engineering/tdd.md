## What it does

Builds behavior through red-green-refactor at public seams. In this local variant, refactoring happens while green and review remains an additional independent check.

## When to reach for it

Type `/tdd`, or let the agent use it for test-first features and bug fixes. A cosmetic change with no behavioral claim does not earn a synthetic test or a failure matrix.

## The loop and its boundary

Name the observable behavior, write one decisive failing test, make it pass, then consolidate duplication without changing behavior. Existing public interfaces suffice for an authorized fix; ask the user when a new seam would materially change the design.

For consequential status, cost, access or audit behavior, the shared `assurance-case` reference selects relevant transitions and compositions. It is not a mandate to test every possible combination.

## Common questions

**Does this version include refactoring?**

Yes. Removing duplication and strengthening domain types while green is part of the loop, not work postponed entirely to review.

**Do I need to approve every regression test?**

No. Existing or already-agreed seams can be used directly. New interfaces with material tradeoffs still require a decision.

**Are database queries and call-count assertions always bad?**

No. If durable audit rows are the promised interface, inspect them in an isolated real store. If a denied operation must never reach a provider, zero calls at that external boundary is meaningful. Incidental internal ordering remains a poor test.

**How do we know a passing test proves anything?**

Name the defect and observe that it makes the assertion fail. Use red/green evidence or a small isolated fault probe, not a mandatory broad mutation campaign. Missing execution is reported honestly.

## It's working if

- The failure is the expected behavioral assertion, not broken setup.
- Mixed outcomes and alternate exits are checked when they threaten the changed claim.
- Internal refactors leave behavioral tests green.
- Live services and private data are not used merely to satisfy the loop.

## Where it fits

[implement](https://aihero.dev/skills-implement) drives this method; [code-review](https://aihero.dev/skills-code-review) challenges the result. [codebase-design](https://aihero.dev/skills-codebase-design) supplies seam vocabulary. [ask-matt](https://aihero.dev/skills-ask-matt) routes broader requests.
