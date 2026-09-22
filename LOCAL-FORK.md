# Fork maintenance

This fork's [main branch](https://github.com/zeekayzeekay/skills/tree/main) contains the customized skills. The initial customized release builds on [mattpocock/skills](https://github.com/mattpocock/skills) at `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`, preserving upstream ancestry. The original customization branch has been merged into this fork's `main`.

## Sources and active installation

| Component | Role |
|---|---|
| `upstream` = `mattpocock/skills` | Source of Matt's future changes; not a destination for our pushes |
| `origin` = `zeekayzeekay/skills` | Our hosted fork; `main` is the reviewed default version |
| Local public checkout | Workspace for changes and upstream integration, developed on a branch from `origin/main` |
| Shared `.agents/skills` directories | Installed copies of one validated checkout, discovered natively by compatible agents |
| Agent-specific skill-directory junctions | Point to those shared installed copies where the installer needs an alias |
| Standalone `delivery-mode-engineering` repository | Canonical source for the locally created delivery skill; update and validate it before syncing this fork's mirror |

There is no automatic GitHub-to-installation synchronization. Fetching, merging or pushing changes does not update active skill copies; installation is a separate, explicit release step. Git's shared ancestry lets us inspect divergence and merge upstream changes while retaining our customizations.

`delivery-mode-engineering` remains canonically maintained in its standalone Git repository. This fork carries a reviewed mirror so the complete skill set can be installed on another machine. Make delivery-skill changes in the standalone repository first, commit and validate them there, then sync the mirror and record its source revision in this file. On the canonical development machine, the shared installed skill may be a direct junction to that standalone checkout; inspect the actual link target before an all-skills install and never silently replace it with the mirror. Other machines may use the validated copied bundle.

## What differs

- `implement` maps agreed behavior to decisive checks, explicitly loads TDD/review, and distinguishes implemented, tested and unvalidated work.
- `tdd` uses red-green-refactor at agreed or existing public seams and tests relevant state transitions and compositions.
- `code-review` separates Standards, Spec and Assurance, includes relevant uncommitted files, and uses clean-context independent reviewers with the same delivery context for substantial changes. Severity and current-delivery disposition are separate. It has no fixed 400-word limit.
- `assurance-case` is the shared compact claim/state/evidence method for consequential behavior. It is not a blanket production checklist.
- `delivery-mode-engineering` owns current acceptance, review dispositions and justified future boundaries. Specs, tickets, implementation and handoffs carry the same context without restarting settled work. Required core outcomes stay evidenced in every mode.
- `ask-matt`, supporting references, invocation metadata and human-facing docs reflect these changes.

The upstream skill set is otherwise retained, including beta and miscellaneous skills. Their presence does not imply stable behavior or compatibility with every platform or harness. `retro` is still described by upstream as a design-notes stub. Deprecated names should not be installed.

Delivery calibration is independently usable and adds no mandatory lifecycle phase. No private installation receipts, machine-specific logs or unrelated project records are included here.

## Install a reviewed release

The commands below use the inspected `skills` CLI version 1.7.0 and require Node >=22.20.0. Inspect and back up existing same-name skills before replacement.

Clone our fork's `main` and use the standard installer from the reviewed checkout:

```sh
git clone --branch main --single-branch https://github.com/zeekayzeekay/skills.git engineering-skills
cd engineering-skills
npx --yes skills@1.7.0 add . --global --agent codex claude-code grok cursor gemini-cli github-copilot --skill '*' --full-depth --yes
```

Select explicit agent targets for the configured runtimes; the command above covers Codex, Claude Code, Grok Build, Cursor, Gemini CLI and GitHub Copilot. When launched inside an agent, the installer can otherwise select only that caller and its universal targets. Add a newly installed runtime through the standard installer's supported agent target rather than keeping an independently edited copy.

The bundled release contains 38 upstream skills plus `assurance-case` and `delivery-mode-engineering`. The installation policy includes all current engineering, productivity, beta and miscellaneous skills; the plugin ships only the promoted subset. Recompute the current names for each release. If deprecated SKILL.md files are present, replace `'*'` with an explicit approved current-name list. Avoid `--all` unless you intend to install to every supported agent runtime. Do not use `scripts/link-skills.sh` for this snapshot workflow: its bucket selection and live source links have different semantics.

On the machine that owns the canonical standalone delivery-skill checkout, preserve its verified junction: install the other skills from this fork with an explicit current-name list that excludes `delivery-mode-engineering`, or restore and re-verify that junction immediately after a snapshot install. The vendored copy is a distribution mirror, not the authoring source.

The local-source installer copies into the shared skill directory and creates agent aliases where needed. The inspected Grok Build also discovers the shared directory natively. Preserve a single installed source even when several discovery paths exist. The installer does not automatically retire renamed skills or replace older global GitHub lock entries. Back up the lock and change only entries owned by this fork; remove stale upstream records for locally released skills so a later upstream update cannot overwrite customizations. Record local release provenance in the private receipt rather than inventing unsupported lock fields. Keep machine-specific release receipts outside Git. New skills are available after the harness refreshes discovery; use a fresh task when earlier instructions are already loaded.

## Validate and update

From this checkout:

```sh
uv run --isolated --no-project --with PyYAML==6.0.3 python -B -X utf8 local/check_source.py
python -B -X utf8 -m unittest discover -s local -p test_verify_install.py -v
python -B -X utf8 local/verify_install.py <installed-skills-root> <claude-skills-root>
```

The installation verifier compares exact bytes, including reference files and invocation metadata. Run it once for the shared root and again for each actual alias root; the optional second argument remains compatible with the existing Claude command. Agents discovering the shared root do not need duplicate copies. Inspect resolved link targets as well as bytes, then use each available runtime's discovery mechanism (for example, Grok's `inspect --json`, filtered to skill data). Filesystem equality alone is not a claim of runtime discovery or automatic invocation. Run against the same checkout used for installation; different Git line-ending settings can produce byte differences despite equal Git blobs. [Validation notes](local/VALIDATION.md) distinguish checks from limitations.

For an authorized upstream update:

1. Check the current branch, worktree, remotes and uncommitted state. Preserve unrelated work and inspect the active installation for local edits. Keep `origin` as our fork and `upstream` as Matt's repository; add a missing `upstream` only after verifying its URL. Fetch both remotes and start an integration branch from current `origin/main`.
2. Record the upstream commit being considered. Inspect new upstream commits, skill content, new/renamed/deprecated skills, invocation metadata and relevant references. Compare the fork-specific behavior listed above; a clean textual merge is not evidence that its meaning survived.
3. Merge the selected upstream ref into the integration branch. Preserve our customizations unless the owner explicitly approves replacing them. Resolve conflicts from both sides' intent, and remove retired names only from this fork's owned installation set after backing them up.
4. Run the structural checks and focused tests above. For material skill-behavior changes, use bounded fresh-context probes and an ordinary-change control where useful. Update affected docs/router entries and report known validator limitations rather than calling them passes.
5. Inspect the exact outgoing diff and reachable commit history for private paths, receipts, secrets and unrelated project records. Commit an explicit path list, push only the intended public branch to `origin`, and obtain the required review/merge approval before it enters `main`. Maintenance instructions do not authorize upstream pushes, automatic merges or scheduled updates.
6. Before installation, back up affected owned skill directories and installer metadata outside skill discovery. Install from the reviewed checkout, reconcile new/renamed/retired names and stale upstream-owned lock entries, then compare every installed file with the source. Preserve other skill providers and report any drift instead of overwriting unexplained edits.
7. Keep the release's source/upstream commits, uncommitted patch fingerprint when applicable, validation results, per-file hashes, installed targets and backup location in a private local receipt. Report separately what was merged/pushed and what was actually installed. Confirm each available harness sees the new release on its next discovery refresh; report unavailable runtimes separately. Restore owned copies, link targets and matching lock entries from backup if installation verification fails.

Use `git diff upstream/main...HEAD` and `git log upstream/main..HEAD` to inspect our changes since the shared ancestor. They show divergence, not proof that the branch includes every latest upstream commit.

Retain private audit branches locally if needed, but never merge or push them into the public branch: removing a private file in a later commit does not remove it from history. Transfer only reviewed public-safe changes. Back up owned installed copies before replacement and keep unrelated skill providers untouched. For rollback, restore only the affected owned copies and matching lock entries from that backup, preserving unrelated later updates.

## Attribution

The upstream MIT license and original attribution are retained. This is a separately maintained fork, not an upstream release. Public aihero.dev links in the docs describe upstream; changed local docs describe this branch.

Delivery-mode engineering is mirrored from standalone revision `05eae159fdca7c58fd783306aba8209ad287239a`. Its original MIT notice is retained inside the bundled skill. Subsequent delivery-skill changes start in that standalone repository and are synced here through a reviewed branch.
