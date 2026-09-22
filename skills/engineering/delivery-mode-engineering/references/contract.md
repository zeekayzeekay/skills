# Delivery contract and persistence

Use root `DELIVERY.md`, with one section per ongoing or persisted initiative. It contains project facts; the skill contains the rules. A truly disposable one-session Spike is exempt: keep its authority, mode, and proof question in the response or an explicitly requested throwaway artifact. If that Spike will be retained or continue into another session, establish the contract and pointer before continuing.

## Authority and activation

- Under `DRAFT`, keep a proposed contract in the response or an explicitly requested planning artifact. It does not change repository rules or implementation.
- Under `APPLY`, a user-selected or unambiguous mode for an ongoing or persisted initiative may be recorded. A section is `ACTIVE` only after a binding repository instruction file points readers to it.
- Add a concise pointer to each existing binding instruction file the participating agents read (`AGENTS.md` or the repository's equivalent). If none exists, create the conventional root instruction file only when repository setup or implementation is authorized. Otherwise leave the section `PROPOSED` and report that cross-session persistence is not installed.
- A pointer should require readers doing substantial scoping, planning, implementation, or review to read the matching `ACTIVE` section in `DELIVERY.md`. It must not claim that unapproved re-tiering overrides existing rules.
- If existing rules conflict, keep the section `PROPOSED` until [reconciliation](reconcile.md) is approved and applied.

## Template

```markdown
# Delivery contract

## <initiative or module>

- Status: PROPOSED | ACTIVE
- Current mode: <selected mode>
- Promotion in progress: none | <target mode, requester/date, open gap IDs>
- Mode owner: <named user>
- Future ambition (OPTION input only): <possible later destination>
- Named user and audience now: <who can use it>
- Collaboration now: <independent human maintainers and needed coordination>
- Environment now: <actual OS, host, or deployment>
- Proof question: <one question this slice must answer>
- Happy path: Given <state>, when <action>, then <observable result>
- Supported inputs and core quality outcomes: <required useful results and decisive checks>
- Real dependencies exercised / accepted stubs: <list>
- Exposure now: <listeners, networks, users, trust boundaries>
- Paid, destructive, or externally visible effects and caps: <list>
- Seam ceiling: <maximum, including zero>
- Non-goals: <features and rigor outside this slice>
- Accepted limitations: <owner-approved limits and their effect on claims>
- Readiness gate: <selected mode's gate: PROOF_ANSWERED | DOGFOOD_READY | MODE_READY>
- Declared readiness outcomes and mapped evidence: <the selected mode's checkable outcomes>

### Mode history

| Date | From | To | Decided by | Reason |
|---|---|---|---|---|
| <date> | none | <selected mode> | <user> | Initial mode |

### Data register

| Asset | Sensitivity | Recoverability | Regeneration source, time/cost, and irreversible loss | Credible local loss and independent recovery evidence |
|---|---|---|---|---|
| <data> | public / private / secret / restricted | disposable / reconstructible / irreplaceable | <specific path and cost> | <failure; tested copy/restore, or n/a> |

### Proof register

| ID | Counterfactual and observable evidence |
|---|---|
| P-001 | <without this, happy path/proof fails; evidence> |

### Floor register

| ID | Asset and reachable path | Consequence and invariant | Cheapest adequate control now | Evidence |
|---|---|---|---|---|
| F-001 | <asset/path> | <failure/outcome> | <current control> | <check> |

### Seams

| ID | Future change | Concrete reversal cost | Smallest boundary and one implementation | Cost now |
|---|---|---|---|---|
| S-001 | <change> | <cost> | <boundary> | <cost> |

### Ledger

| ID | Deferred item | Admission basis | Observable trigger | Source |
|---|---|---|---|---|
| L-001 | <item> | current-slice debt / user-requested task / stronger mechanism for F-### | <condition> | <shortcut/request/floor ID> |

### Constraint register

<Include the stable-ID table from reconciliation only when repository rules were re-tiered.>
```

## Filling rules

- Give proof, floor, seam, ledger, and constraint entries stable IDs. Never renumber or reuse an ID; retain retired entries with their disposition.
- Record each data asset separately. Sensitivity, recoverability, and regeneration path/cost are independent facts; one never substitutes for another. Include manual corrections or annotations in irreversible loss. Retained irreplaceable data must cite a tested independent recovery copy adequate for the credible local failure, or be removed from the retained happy path.
- The seam ceiling is a maximum, not a quota. Every seam must pass the OPTION predicate in `SKILL.md`.
- Floor entries state outcomes and then the cheapest currently adequate mechanism. Stronger mechanisms require a ledger trigger.
- Prefix every executable task with `[P-### PROOF]`, `[F-### FLOOR]`, or `[S-### SEAM]`; prefix every check, test, metric, and evidence line with its supporting `[P-###]` or `[F-###]` IDs.
- Ledger entries remain outside the executable plan. Admit only debt created by the current slice, a specific future task the user explicitly requests tracked, or a stronger mechanism deferred from a current floor invariant. Omit generic higher-mode capabilities; promotion recomputes them when requested.
- `Current mode` is authoritative. Append every initial decision and promotion to Mode history; never rewrite history.
- Match the readiness gate to [modes](modes.md). For Limited Pilot, Public MVP, and Production, declare the initiative-specific acceptance and readiness outcomes before implementation.
- Keep `Current mode` unchanged while promotion gaps remain open. Record the target and open IDs in `Promotion in progress`; activate it and append Mode history only after its readiness evidence closes.
