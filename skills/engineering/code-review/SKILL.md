---
name: code-review
description: "Review a fixed scope along Standards, Spec and Assurance axes. Use for a branch, PR, uncommitted work, or review since a fixed point. Check documented rules, required behavior, and whether evidence can detect consequential defects. Independent reviewers work from contracts and source, not completion claims."
---

# Code review

Keep three axes separate:

- **Standards:** documented coding rules, plus the heuristic [smell baseline](SMELLS.md).
- **Spec:** missing, partial, wrong or unrequested behavior against the actual contract.
- **Assurance:** whether tests and records substantiate the consequential claims being made.

Review does not authorize fixes, commits, live calls or changes to user data. A delegated leaf reviewer performs its assigned axis directly: **do not invoke this skill recursively or spawn further agents**.

## Pin the source state

Resolve the baseline from the user's ref or the implementation's recorded starting point. Ask if it is genuinely ambiguous. Record the absolute worktree, baseline SHA, HEAD, status and requested scope.

For a branch/PR, compare its merge-base to the requested tip. For work in progress, inspect the combined tracked state with `git diff <resolved-base>`, also inspect `git diff --cached`, `git diff`, and explicitly list relevant untracked files with `git ls-files --others --exclude-standard`. A HEAD-only diff does not review uncommitted work. Never add ignored/private files just to make a review snapshot. Distinguish pre-existing changes from the requested slice. Resolve renames and final line numbers from current source.

Freeze a snapshot when useful, or fingerprint the reviewed files and recheck them at the end. If HEAD or files changed during review, qualify the result and recheck affected paths. An empty committed diff is not an empty review when relevant uncommitted files exist.

## Find the governing sources

Use an explicit user-provided contract/spec first, then the active repository contract, then linked issues and matching spec files. Read relevant `AGENTS.md`, ADRs and standards, following their precedence. An issue tracker is optional when the requirements are already local. Ask only for a missing material source; with none, mark Spec unassessed instead of inventing requirements.

For changed access, integrity, spending, lifecycle, provenance, evidence-status or audit paths, invoke `assurance-case` (or read its `SKILL.md`) for the shared matrix and falsification rules. For low-risk changes, keep Assurance to the relevant evidence and test sensitivity; no mandatory matrix, fault campaign or production audit.

## Independent passes

For substantial or consequential changes, use separate clean-context subagents for the three axes when available. Supply only the task boundary, pinned source/snapshot, contract, standards, relevant raw fixtures and safe test commands. **Do not supply the implementer's completion narrative, suspected defects, proposed fixes or another reviewer's conclusions.** Explicitly forbid recursive delegation and source edits. Do not inherit the authoring conversation.

Give each reviewer a bounded assignment:

- **Standards:** cite the rule and affected code for a hard breach. Label smells as judgment calls. Repository rules override the heuristic baseline; do not repeat mechanically enforced style findings.
- **Spec:** cite the contract and trace the affected public path, including reachable alternate exits. State the input/state, actual result, required result and consequence.
- **Assurance:** challenge the claimed evidence with relevant transitions, mixed states, precedence, defaults, stale/cache behavior and before/after-effect failures. Run safe focused counterexamples for serious suspected defects. Check whether the current tests would fail for that defect, not merely whether they pass.

There is no fixed word cap. Require enough source and reproduction detail to make each material finding actionable; omit repetitive prose. For a small change, direct separated passes suffice. If clean-context delegation is unavailable, disclose that the review was not independent; never simulate an independent verdict.

## Verify and report

Treat reviewer output as hypotheses until checked. Verify material citations and the causal path; confirm blockers/majors with a safe targeted reproduction where feasible. Keep temporary probes outside the user's worktree. If execution requires missing permission or infrastructure, use exact source analysis and label the finding **source-verified, not reproduced**. Separate reproduced defects, source-supported defects, evidence gaps and unconfirmed concerns.

Report under **Standards**, **Spec** and **Assurance**, retaining their distinct meanings. Cross-reference overlapping findings rather than counting one defect twice. Include severity, precise location, governing claim, failing state, observable consequence and the smallest useful correction or missing check. A hard standards breach needs a documented rule; an Assurance gap is not automatically a proven behavioral defect.

Close with counts and worst issue per axis, the exact reviewed state, commands/results, skipped paths and remaining uncertainty. No findings means none found in this bounded scope, not proof of correctness. Review the materially changed paths after authorized fixes; do not recurse until every stylistic preference disappears.
