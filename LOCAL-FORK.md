# Fork maintenance

This public branch of [zeekayzeekay/skills](https://github.com/zeekayzeekay/skills/tree/codex/engineering-skills) builds on [mattpocock/skills](https://github.com/mattpocock/skills) at `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`. It preserves upstream ancestry. The fork's `main` branch is not changed by publishing this branch.

## What differs

- `implement` maps agreed behavior to decisive checks, explicitly loads TDD/review, and distinguishes implemented, tested and unvalidated work.
- `tdd` uses red-green-refactor at agreed or existing public seams and tests relevant state transitions and compositions.
- `code-review` separates Standards, Spec and Assurance, includes relevant uncommitted files, and uses clean-context independent reviewers for substantial changes. It has no fixed 400-word limit.
- `assurance-case` is the shared compact claim/state/evidence method for consequential behavior. It is not a blanket production checklist.
- `ask-matt`, supporting references, invocation metadata and human-facing docs reflect these changes.

The upstream skill set is otherwise retained, including beta and miscellaneous skills. Their presence does not imply stable behavior or compatibility with every platform or harness. `retro` is still described by upstream as a design-notes stub. Deprecated names should not be installed.

`delivery-mode-engineering` is an optional separately maintained skill, not bundled into this fork. No private installation receipts, machine-specific logs or unrelated project records are included here.

## Install this branch

The commands below use the inspected `skills` CLI version 1.7.0 and require Node >=22.20.0. Inspect and back up existing same-name skills before replacement.

Clone the public branch and use the standard installer from the checkout:

```sh
git clone --branch codex/engineering-skills --single-branch https://github.com/zeekayzeekay/skills.git engineering-skills
cd engineering-skills
npx --yes skills@1.7.0 add . --global --agent codex claude-code --skill '*' --full-depth --yes
```

This tree contains 38 current upstream skills plus `assurance-case`. Full-depth discovery includes beta/miscellaneous skills that the promoted-only plugin does not ship. If a future upstream merge adds deprecated SKILL.md files, replace `'*'` with an explicit approved current-name list. Avoid `--all` unless you intend to install to every supported agent runtime.

The local-source installer copies into the shared skill directory and links Claude to those installed copies. It does not automatically retire renamed skills or replace older global GitHub lock entries. Back up the lock and change only entries owned by this fork; stale upstream entries can let a later upstream update overwrite custom skills. Keep machine-specific release receipts outside Git. New skills are available after the harness refreshes discovery; use a fresh task when earlier instructions are already loaded.

## Validate and update

From this checkout:

```sh
uv run --isolated --no-project --with PyYAML==6.0.3 python -B -X utf8 local/check_source.py
python -B -X utf8 -m unittest discover -s local -p test_verify_install.py -v
python -B -X utf8 local/verify_install.py <installed-skills-root> <claude-skills-root>
```

The installation verifier compares exact bytes, including reference files and invocation metadata. Run it against the same checkout used for installation; different Git line-ending settings can produce byte differences despite equal Git blobs. [Validation notes](local/VALIDATION.md) distinguish checks from limitations.

Keep your fork as `origin` and Matt's repository as `upstream`. Fetch upstream, review the changes and merge the selected upstream ref into this public branch. Check renamed/removed skills, invocation policies and local behavioral differences before reinstalling. `git diff upstream/main...HEAD` and `git log upstream/main..HEAD` show divergence.

Retain private audit branches locally if needed, but never merge or push them into the public branch: removing a private file in a later commit does not remove it from history. Transfer only reviewed public-safe changes. Back up owned installed copies before replacement and keep unrelated skill providers untouched. For rollback, restore only the affected owned copies and matching lock entries from that backup, preserving unrelated later updates.

## Attribution

The upstream MIT license and original attribution are retained. This is a separately maintained fork, not an upstream release. Public aihero.dev links in the docs describe upstream; changed local docs describe this branch.
