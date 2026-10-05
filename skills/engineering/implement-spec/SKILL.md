---
name: implement-spec
description: "Implement the result of /to-spec and /to-tickets in code."
disable-model-invocation: true
---

You have been provided a spec. This spec should have tickets associated with it, describing how to implement the spec.

The issue tracker should have been provided to you. If not, tell the user to run `/setup-matt-pocock-skills`.

The goal is the entire spec implemented on a single **integration branch**, with every ticket resolved the way the issue tracker closes work.

The tickets are not a list of steps. They are a **task graph** with blocking relationships between them. This means there is always a **frontier** of tickets which are ready to be grabbed.

Communication to and from subagents should be sparse. Communicate primarily through **context pointers**: to the spec, tickets, research notes, and previous commits. Don't duplicate information already available via pointers.

**Implementer subagents** should be run in the background where possible for maximum concurrency.

## Steps

1. Read the applicable repository instructions, active delivery contract, spec and tickets. Record the starting source state and understand the task graph. Invoke `delivery-mode-engineering` through the harness's skill tool, or read its `SKILL.md` if no skill tool exists. Reuse its shared delivery context, current acceptance and settled decisions.

2. (optional) Use an **exploration subagent** to conduct any exploration required by the tickets - relevant codebase files or external documentation. Ensure the exploration subagent can save files - it should save its markdown notes in a directory outside the repo, accessible by all future subagents. This lets **implementer subagents** focus on implementation rather than exploration.

3. Create the integration branch. If the issue tracker closes work through PRs, or the user asks for one, open a draft PR after the first merge in step 5 (a branch with no commits ahead of main can't open one), marked as closing the spec and tickets.

4. Use **implementer subagents** to implement each ticket, each in its own worktree on its own branch. Pass the governing delivery context, relevant claims and evidence requirements with the ticket pointers. Require each handoff to distinguish implemented, tested and unvalidated claims, with remaining blockers and other review dispositions. Each implementer subagent:
   - confirms its worktree is based on the integration branch before starting, and resets onto it if not;
   - invokes `tdd` through the harness's skill tool, or reads its `SKILL.md` when no skill tool exists, to build the ticket;
   - merges the integration branch tip into its own branch before reporting done

5. Once an **implementer subagent** completes, merge its work to the integration branch with a **merger subagent**.

6. If this changes the **frontier** of available tickets, kick off more **implementer subagents** to work on the new tickets. This allows for maximum concurrency.

7. Once all tickets are complete, invoke `code-review` through the harness's skill tool, or read its `SKILL.md` if no skill tool exists, against the recorded starting point and integrated source state. Give independent reviewers the same delivery context and raw evidence, without the implementers' completion narrative. Use delivery-mode engineering's Review rules to select authorized blockers and requested in-scope improvements for a single **implementer subagent**; carry other dispositions separately. Recheck affected claims and review materially changed paths. Apply the shared stopping rule to repeated or oscillating findings.


8. If a draft PR exists, mark it ready for review. Otherwise, resolve each ticket the way the issue tracker closes work, and report the integration branch. In either case, include a handoff referencing the contract, current and target mode when applicable, observed evidence, unresolved blockers and nonblocking dispositions. PR review status and ticket completion are separate from mode readiness: claim the selected readiness gate only when its mapped evidence is demonstrated and its blockers are closed. Keep missing live evidence unvalidated and promotion in progress until the target gate closes.


9. Clean up all **implementer subagent** worktrees.
