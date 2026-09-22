---
name: implement
description: "Implement a piece of work based on a spec or set of tickets."
disable-model-invocation: true
---

Implement the work described by the user in the spec or tickets.

## Establish the boundary

Read the applicable repository instructions, active delivery contract, and agreed spec. Reuse completed design/research and existing claim IDs; do not restart those workflows. Record the starting commit, branch, worktree and pre-existing changes so the eventual review includes this work without attributing others' edits to it. A material unresolved design choice goes to the user.

Invoke `delivery-mode-engineering` through the harness's skill tool, or read its `SKILL.md` if no skill tool exists, for shared delivery context, present acceptance and review dispositions. Apply it within this work's authority and inherited contract. Preserve required core outcomes and justified growth boundaries while keeping operational promises scoped to current use.

Map the requested behavior to its observable acceptance checks. When changing truth-bearing behavior (an access decision, integrity check, cost, lifecycle, provenance, evidence status or audit receipt), invoke `assurance-case` for the compact claim/state/evidence matrix and falsification rules. Use the harness's skill tool, or read that skill's `SKILL.md` when no such tool exists. Ordinary changes need ordinary focused checks, not a new assurance document.

## Build and check

Invoke `tdd` through the harness's skill tool, or read its `SKILL.md` if no skill tool exists, before applying the following loop.

Use `tdd` at the agreed or existing public seams: one red-green-refactor slice at a time. Select relevant failure and mixed-state tests from the contract before implementing the branch they protect. Observe red for the intended defect, not an import/setup failure, then green. Keep policy, qualification, accounting and status precedence behind one typed implementation per seam where these are part of the changed behavior.

Run available type/static checks and focused tests regularly. Follow the repository's suite policy; run a broader suite for credible cross-cutting regressions or an explicit gate, rather than treating an unrelated legacy suite as automatic scope. Report baseline failures separately without weakening tests. Passing tests are evidence only when the described defect would make them fail.

## Review and hand off

Invoke `code-review` through the harness's skill tool, or read its `SKILL.md` if no skill tool exists, before orchestrating review.

Use `code-review` on the recorded baseline and the actual final state, including relevant staged, unstaged and untracked files. Give independent reviewers the same delivery context, contract, standards and source state, not the implementer's completion narrative. Validate serious findings with a focused counterexample or exact path analysis.

Select fixes using the shared Review dispositions and stopping rule in `delivery-mode-engineering`: fix authorized blockers and requested in-scope improvements, then rerun affected checks and review materially changed paths. Carry other dispositions separately instead of turning the entire report into a new task list. Resolve a repeated unsupported finding or oscillating interpretation against the governing requirement before another repair cycle; keep unresolved blockers visible. Stop when the selected readiness gate is evidenced and its blockers are closed.

Finish with separate **implemented**, **tested** (commands, outcomes and decisive red/green evidence), and **unvalidated** claims. Carry the delivery context by reference in the handoff. State review scope, remaining blockers, nonblocking dispositions and any live evidence still needed. Do not call deferred live checks complete.

Commit only when the user or repository policy authorizes it, staging an explicit path list. Implementation does not authorize deployment, live data/provider calls, profile/grant changes, migrations or remote pushes.
