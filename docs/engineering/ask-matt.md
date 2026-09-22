## What it does

Routes a situation to the appropriate skill or flow. It recommends the next step rather than restarting phases already completed. This local version maps the promoted, beta and miscellaneous skills, including `assurance-case` and the bundled `delivery-mode-engineering` reference.

## When to reach for it

Invoke `/ask-matt` yourself when several skills could fit. If you already know which skill you want, invoke that one directly.

## Prerequisites

The router does not install skills. A workflow that depends on an issue tracker may need [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills). A local review or implementation with an agreed contract does not need tracker setup merely to proceed.

## Flows, not mandatory ceremony

The main path runs from sharpening an idea to implementation and review, with prototypes and research only where useful. Existing settled work can enter at implementation. Red-green-refactor supplies feedback; review separates Standards, Spec and Assurance. The local assurance reference supports consequential claims without creating a new production gate.

Delivery-mode engineering runs across those steps: it keeps core outcomes, current rigor, accepted limitations and justified future boundaries consistent. It also owns review dispositions and the stopping rule. You can use it independently; bundling it does not create another phase or require a new interview for a routine fix.

Beta and miscellaneous tools are available in this installation but keep their upstream maturity and platform limits. In particular, upstream marks `retro` as a design-notes stub.

The beta `implement-spec` workflow carries the same delivery context and review dispositions through its parallel ticket work. Its final handoff distinguishes PR review status from demonstrated mode readiness and keeps unresolved evidence visible.

## Common questions

**Why is an installed skill absent from automatic discovery?**

User-invoked skills deliberately disable automatic invocation. Absence from the automatic list is not proof that the skill is uninstalled; inspect its local directory and invocation metadata.

**What if the router's summary disagrees with a skill?**

The target `SKILL.md` wins. Read it before making a load-bearing claim about behavior; the router is a secondary map.

**Where did writing-great-skills go?**

It was renamed to [writing-for-agents](https://aihero.dev/skills-writing-for-agents). The old name is retired, not kept as a competing copy.

**Will upstream updates erase local changes?**

Not through the documented local release process: merge upstream into the fork, validate, then install from that source. Installing directly from upstream at the same names can still overwrite custom copies.

## It's working if

- The proposed route starts from your current state, not a generic beginning.
- Recommendations distinguish stable skills from beta/tool-specific ones.
- A behavior claim is checked against the target skill.
- A simple change does not acquire unnecessary setup or assurance machinery.

## Where it fits

This is the map over [implement](https://aihero.dev/skills-implement), [code-review](https://aihero.dev/skills-code-review) and their neighbors, not an additional phase. It does not route arbitrary third-party skills. Local changed docs describe this fork; the linked public pages describe upstream.
