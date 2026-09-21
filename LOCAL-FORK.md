# Fork maintenance

This fork's [main branch](https://github.com/zeekayzeekay/skills/tree/main) contains the customized skills. The initial customized release builds on [mattpocock/skills](https://github.com/mattpocock/skills) at `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`, preserving upstream ancestry. The original customization branch has been merged into this fork's `main`.

## Sources and active installation

| Component | Role |
|---|---|
| `upstream` = `mattpocock/skills` | Source of Matt's future changes; not a destination for our pushes |
| `origin` = `zeekayzeekay/skills` | Our hosted fork; `main` is the reviewed default version |
| Local public checkout | Workspace for changes and upstream integration, developed on a branch from `origin/main` |
| Shared `.agents/skills` directories | Installed copies of a validated checkout, read by Codex |
| Claude skill-directory junctions | Point to those shared installed copies, not the source checkout |

There is no automatic GitHub-to-installation synchronization. Fetching, merging or pushing changes does not update active skill copies; installation is a separate, explicit release step. Git's shared ancestry lets us inspect divergence and merge upstream changes while retaining our customizations.

The separate `delivery-mode-engineering` skill is not part of this fork. Where it is installed through a direct junction to its own source repository, source edits are immediately active. Check the actual link target before editing or updating it; do not treat it as one of this fork's copied releases.

## What differs

- `implement` maps agreed behavior to decisive checks, explicitly loads TDD/review, and distinguishes implemented, tested and unvalidated work.
- `tdd` uses red-green-refactor at agreed or existing public seams and tests relevant state transitions and compositions.
- `code-review` separates Standards, Spec and Assurance, includes relevant uncommitted files, and uses clean-context independent reviewers for substantial changes. It has no fixed 400-word limit.
- `assurance-case` is the shared compact claim/state/evidence method for consequential behavior. It is not a blanket production checklist.
- `ask-matt`, supporting references, invocation metadata and human-facing docs reflect these changes.

The upstream skill set is otherwise retained, including beta and miscellaneous skills. Their presence does not imply stable behavior or compatibility with every platform or harness. `retro` is still described by upstream as a design-notes stub. Deprecated names should not be installed.

`delivery-mode-engineering` is an optional separately maintained skill, not bundled into this fork. No private installation receipts, machine-specific logs or unrelated project records are included here.

## Install a reviewed release

The commands below use the inspected `skills` CLI version 1.7.0 and require Node >=22.20.0. Inspect and back up existing same-name skills before replacement.

Clone our fork's `main` and use the standard installer from the reviewed checkout:

```sh
git clone --branch main --single-branch https://github.com/zeekayzeekay/skills.git engineering-skills
cd engineering-skills
npx --yes skills@1.7.0 add . --global --agent codex claude-code --skill '*' --full-depth --yes
```

The initial customized release contains 38 upstream skills plus `assurance-case`. The installation policy includes all current engineering, productivity, beta and miscellaneous skills; the plugin ships only the promoted subset. Recompute the current names for each release. If deprecated SKILL.md files are present, replace `'*'` with an explicit approved current-name list. Avoid `--all` unless you intend to install to every supported agent runtime. Do not use `scripts/link-skills.sh` for this snapshot workflow: its bucket selection and live source links have different semantics.

The local-source installer copies into the shared skill directory and links Claude to those installed copies. It does not automatically retire renamed skills or replace older global GitHub lock entries. Back up the lock and change only entries owned by this fork; stale upstream entries can let a later upstream update overwrite custom skills. Keep machine-specific release receipts outside Git. New skills are available after the harness refreshes discovery; use a fresh task when earlier instructions are already loaded.

## Validate and update

From this checkout:

```sh
uv run --isolated --no-project --with PyYAML==6.0.3 python -B -X utf8 local/check_source.py
python -B -X utf8 -m unittest discover -s local -p test_verify_install.py -v
python -B -X utf8 local/verify_install.py <installed-skills-root> <claude-skills-root>
```

The installation verifier compares exact bytes, including reference files and invocation metadata. Run it against the same checkout used for installation; different Git line-ending settings can produce byte differences despite equal Git blobs. [Validation notes](local/VALIDATION.md) distinguish checks from limitations.

For an authorized upstream update:

1. Check the current branch, worktree, remotes and uncommitted state. Preserve unrelated work and inspect the active installation for local edits. Keep `origin` as our fork and `upstream` as Matt's repository; add a missing `upstream` only after verifying its URL. Fetch both remotes and start an integration branch from current `origin/main`.
2. Record the upstream commit being considered. Inspect new upstream commits, skill content, new/renamed/deprecated skills, invocation metadata and relevant references. Compare the fork-specific behavior listed above; a clean textual merge is not evidence that its meaning survived.
3. Merge the selected upstream ref into the integration branch. Preserve our customizations unless the owner explicitly approves replacing them. Resolve conflicts from both sides' intent, and remove retired names only from this fork's owned installation set after backing them up.
4. Run the structural checks and focused tests above. For material skill-behavior changes, use bounded fresh-context probes and an ordinary-change control where useful. Update affected docs/router entries and report known validator limitations rather than calling them passes.
5. Inspect the exact outgoing diff and reachable commit history for private paths, receipts, secrets and unrelated project records. Commit an explicit path list, push only the intended public branch to `origin`, and obtain the required review/merge approval before it enters `main`. Maintenance instructions do not authorize upstream pushes, automatic merges or scheduled updates.
6. Before installation, back up affected owned skill directories and installer metadata outside skill discovery. Install from the reviewed checkout, reconcile new/renamed/retired names and stale upstream-owned lock entries, then compare every installed file with the source. Preserve other skill providers and report any drift instead of overwriting unexplained edits.
7. Keep the release's source/upstream commits, validation results, per-file hashes and backup location in a private local receipt. Report separately what was merged/pushed and what was actually installed. Confirm the harness sees the new release on its next discovery refresh.

Use `git diff upstream/main...HEAD` and `git log upstream/main..HEAD` to inspect our changes since the shared ancestor. They show divergence, not proof that the branch includes every latest upstream commit.

Retain private audit branches locally if needed, but never merge or push them into the public branch: removing a private file in a later commit does not remove it from history. Transfer only reviewed public-safe changes. Back up owned installed copies before replacement and keep unrelated skill providers untouched. For rollback, restore only the affected owned copies and matching lock entries from that backup, preserving unrelated later updates.

## Attribution

The upstream MIT license and original attribution are retained. This is a separately maintained fork, not an upstream release. Public aihero.dev links in the docs describe upstream; changed local docs describe this branch.
