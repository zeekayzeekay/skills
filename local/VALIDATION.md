# Validation and limitations

## Repeatable checks

- `check_source.py` parses frontmatter, verifies skill names and invocation-policy alignment, checks promoted plugin membership, and resolves local links in changed skills and their docs.
- `test_verify_install.py` checks exact equality, changed bytes, missing/extra files, and inclusion of real reference/UI files.
- `verify_install.py` compares the complete current skill source against explicitly supplied installation roots. Its output contains per-file hashes; save machine-specific release output outside Git.

The source check requires PyYAML; the other scripts use Python's standard library. The documented isolated `uv` command avoids changing an application's dependencies.

## Behavioral evidence

The skill instructions were previously exercised by bounded fresh-context probes. One inspection-dashboard review identified status precedence and message defects despite the original tests passing. A separate delivery-mode probe rejected a false readiness claim under an existing requirement while adding no assurance process to a cosmetic edit. These are individual smoke checks, not statistical or exhaustive validation. Private runner records are deliberately not published here.

The synthetic [inspection-dashboard fixture](evals/inspection-dashboard/contract.md) is included for repeatable probing. Its implementation is intentionally flawed, and its three singleton tests pass. Read the contract before inspecting `dashboard.py`, then challenge aggregation and message correctness through its public interface. Do not treat the fixture as production code or the passing original tests as proof of its contract.

## Known tool limitations

The bundled generic skill validator used during preparation rejected existing upstream `disable-model-invocation` and `argument-hint` fields because its allowlist did not recognize those harness fields. They were retained; the targeted YAML and cross-harness checks cover them.

Strict marketplace validation passed during preparation. Explicit plugin validation passed without strict mode; strict plugin validation reported that root CLAUDE.md is not loaded as plugin project context. That same warning reproduced on untouched upstream. This fork does not claim an all-green strict-plugin check.

No full multi-model evaluation, implicit-invocation study or exhaustive behavioral review of untouched upstream beta/misc skills was performed. Instructions support better decisions but cannot guarantee agent compliance or defect-free output.
