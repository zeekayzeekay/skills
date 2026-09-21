## What it does

Reviews one pinned source state along Standards, Spec and Assurance axes. This local variant reviews relevant uncommitted files too and checks material findings before presenting them as established defects.

## When to reach for it

Type `/code-review`, or let the agent invoke it for a branch, PR or work-in-progress review. Provide a baseline, or reuse the implementation's recorded starting point. Review is read-only unless fixes are separately authorized.

## Three questions

| Axis | Question | Evidence |
|---|---|---|
| Standards | Does it follow the documented rules? | Rule plus affected code; smells are labeled judgment calls |
| Spec | Does it do what was asked? | Contract plus the reachable causal path |
| Assurance | Do the tests and records establish the claims? | Decisive assertions, safe counterexamples and explicit gaps |

Substantial changes use clean-context reviewers when available. They receive the contract and source, not the implementer's success story. The shared `assurance-case` reference owns the detailed falsification method; low-risk reviews stay small.

## Common questions

**Will it review code before I commit?**

Yes. It records the baseline, HEAD and working-tree state, then includes relevant staged, unstaged and untracked files. Ignored/private files are not swept into review.

**Can the reviewers recursively launch more reviewers?**

No. Leaf assignments explicitly prohibit invoking the orchestrator or delegating again. When independent contexts are unavailable, the result says so.

**Are all findings proven?**

No. The report distinguishes reproduced defects, source-supported defects, evidence gaps and unconfirmed concerns. Safe serious counterexamples are executed where feasible; missing infrastructure is not invented.

**Is there still a 400-word limit?**

No. Material findings need enough evidence to act on. Repetitive prose is still omitted, and one defect appearing on two axes is cross-referenced rather than counted twice.

**Does a clean review guarantee correctness?**

No. It reports the exact reviewed state and limits. New fixes earn rechecks of affected paths, not an endless cycle of stylistic cleanup.

## It's working if

- Reviewers see raw contracts and code before completion claims.
- Findings cite current source and a specific violated requirement or evidence gap.
- The final report identifies what ran, what could not run and which state was reviewed.
- Review alone causes no source edits or live side effects.

## Where it fits

[implement](https://aihero.dev/skills-implement) invokes review before authorized handoff or commit. [tdd](https://aihero.dev/skills-tdd) supplies the test evidence it challenges. [ask-matt](https://aihero.dev/skills-ask-matt) maps broader flows.
