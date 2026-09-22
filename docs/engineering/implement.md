## What it does

Builds the agreed work through small tested slices, then reviews the actual resulting files. This local variant separates implemented, tested and unvalidated claims; a passing suite is not a substitute for a decisive assertion.

## When to reach for it

Invoke `/implement` yourself for a concrete spec, ticket or settled plan. It remains user-invoked. It reuses completed design and research, asking only about material unresolved choices.

## Scope and evidence

The starting commit and existing changes define the review boundary. Ordinary changes get focused checks. Changed access, integrity, spending or audit behavior uses the shared `assurance-case` map to select relevant failure and mixed-state tests.

The loop is red-green-refactor at agreed or existing public seams. Broad-suite policy comes from the repository and regression risk, not an unconditional full-suite rule.

The bundled `delivery-mode-engineering` reference carries the same current acceptance criteria into implementation and review. Core outcomes remain required during dogfood; operational promises follow actual use and exposure. Existing contracts and settled planning are reused.

## Common questions

**Does it commit or deploy automatically?**

No. Commits follow user/repository authority with explicit staging. Deployment, live data/provider calls, migrations, profile/grant changes and pushes remain separate actions.

**What if review finds problems?**

It validates serious findings and uses their current-delivery dispositions to fix authorized blockers and requested improvements. Other findings remain separate from the executable work. Rechecks follow affected claims. When a finding repeats without new evidence or fixes oscillate, the disputed requirement is resolved before another repair cycle. Unresolved blockers and unexecuted live checks remain explicit.

**Can it miss defects even after this process?**

Yes. Evidence is bounded. The close-out names commands, decisive checks, review scope and limitations instead of declaring universal correctness.

## It's working if

- A relevant failure test goes red for the intended defect, then green.
- The review includes the work still uncommitted.
- The handoff distinguishes implemented, tested and unvalidated behavior.
- Implementation and review use the same acceptance bar and stop when its required evidence is established.

## Where it fits

The implementation step uses [tdd](https://aihero.dev/skills-tdd) and [code-review](https://aihero.dev/skills-code-review), with the local `assurance-case` reference for consequential claims. [ask-matt](https://aihero.dev/skills-ask-matt) maps the surrounding flows; a settled plan need not traverse them again.
