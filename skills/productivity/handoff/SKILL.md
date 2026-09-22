---
name: handoff
description: Compact the current conversation into a handoff document for another agent to pick up.
argument-hint: "What will the next session be used for?"
disable-model-invocation: true
---

Write a handoff document summarising the current conversation so a fresh agent can continue the work. Save to the temporary directory of the user's OS - not the current workspace.

Include a "suggested skills" section in the document, naming which skills the next agent should call the Skill tool for.

Do not duplicate content already captured in other artifacts (specs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.

For development work, invoke `delivery-mode-engineering` through the harness's skill tool, or read its `SKILL.md` if no skill tool exists, to carry the shared delivery context without reopening settled decisions. Name the governing section and applicable acceptance claims, evidence limits and review dispositions so a new agent uses the same bar. If a destination cannot read an artifact, include the necessary authorized excerpt with its origin.

For an independent review handoff, supply the contract, delivery definitions, source state and raw evidence. Omit the implementer's completion narrative, suspected defects and proposed fixes from that reviewer input; a continuation handoff may retain progress and unresolved hypotheses as such.

Redact any sensitive information, such as API keys, passwords, or personally identifiable information.

If the user passed arguments, treat them as a description of what the next session will focus on and tailor the doc accordingly.
