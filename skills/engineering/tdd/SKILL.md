---
name: tdd
description: Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions "red-green-refactor", or wants integration tests.
---

# Test-Driven Development

TDD is the red → green → refactor loop. This skill is the reference that makes that loop produce tests worth keeping: what a good test is, where tests go, the anti-patterns, and the rules of the loop. Every section applies on every cycle: consult them before and during the loop, not after.

When exploring the codebase, read `CONTEXT.md` (if it exists) so test names and interface vocabulary match the project's domain language, and respect ADRs in the area you're touching.

## What a good test is

Tests verify behavior through public interfaces, not implementation details. Code can change entirely; tests shouldn't. A good test reads like a specification: "user can checkout with valid cart" tells you exactly what capability exists, and it survives refactors because it doesn't care about internal structure.

See [tests.md](tests.md) for examples and [mocking.md](mocking.md) for mocking guidelines.

## Seams: where tests go

A **seam** is the public boundary you test at: the interface where you observe behavior without reaching inside. Tests live at seams, never against internals.

**Test at agreed or existing public seams.** State the seams under test and reuse the task's agreed interfaces. For an authorized implementation, an existing public interface is enough to proceed; ask when choosing a new interface would materially change the design or scope. Do not require renewed approval for every regression test. You cannot test everything: select critical paths and complex logic from the actual contract.

Ask when unresolved: "What's the public interface, and which seams should we test?"

When the shape of that interface is itself in question (how deep the module is, where the seam belongs, what the interface should expose), call the Skill tool with "codebase-design" for the vocabulary. It is the shared source of the module, interface, depth, seam, adapter, leverage and locality terms, and it is a reference to consult, not a session to run.

## Anti-patterns

- **Implementation-coupled**: mocks internal collaborators, tests private methods, or relies on incidental storage details. Persisted audit records and the external dispatch boundary are legitimate observable interfaces when the contract explicitly promises them; see [tests.md](tests.md). The tell: the test breaks when you refactor but behavior hasn't changed.
- **Tautological**: the assertion recomputes the expected value the way the code does (`expect(add(a, b)).toBe(a + b)`, a snapshot derived by hand the same way, a constant asserted equal to itself), so it passes by construction and can never disagree with the code. Expected values must come from an independent source of truth: a known-good literal, a worked example, the spec.
- **Horizontal slicing**: writing all tests first, then all implementation. Bulk tests verify _imagined_ behavior: you test the _shape_ of things rather than user-facing behavior, the tests go insensitive to real changes, and you commit to test structure before understanding the implementation. Work in **vertical slices** instead: one test → one implementation → repeat, each test a **tracer bullet** that responds to what the last cycle taught you.

## Rules of the loop

- **Red before green.** Write the failing test first, then only enough code to pass it. Don't anticipate future tests or add speculative features.
- **One slice at a time.** One seam, one test, one minimal implementation per cycle.
- **Refactor while green.** Consolidate duplicate seams and improve names/types without changing behavior; rerun the same behavioral tests. Review is an additional check, not the first time implementation quality matters. Do not expand into unrelated cleanup.

## Truth-bearing behavior

When the change reports or decides access, integrity, money, lifecycle, provenance or evidence status, invoke `assurance-case` (or read its `SKILL.md`) and use its single claim/state/evidence matrix. Test the relevant transitions and compositions at the public seam, not merely one happy example per enum value. A mixed result, alternate exit, stale input or cache hit may change what the caller is told even when every leaf function passes.

For each material claim, name the defect the assertion detects. Observe the focused test fail with that defect and pass with the fix. A small reversible fault probe in an isolated copy can establish sensitivity when an existing passing test is the evidence; do not mutate shared work or demand a full mutation-testing campaign. A passing command without a decisive assertion is not proof. If red or the real dependency cannot be exercised safely, report that evidence gap instead of claiming TDD completion.
