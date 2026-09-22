# Scale-ready design for a one-person start

Read this when the request names a future audience beyond the present named user (a team, customers,
tenants, an installed product, a hosted service) while today's build is for one person in one
environment. It decides which boundaries that ambition earns on day 0 and which it does not.

**Principle: design for principals and facts, not tenants and features.** The three later shapes
(personal local app → team install on the organisation's own machines → multi-tenant service) must each
be a *deployment and configuration* change over the same typed core and the same data. Today's build gets
exactly the fields and boundaries that are cheap now and impossible to reconstruct later, and nothing
else. Everything below is a `SEAM` only if it passes the OPTION predicate in `SKILL.md`; the day-0 list is
the set that normally does. Zero of the ledger items is built before its trigger.

## Day 0: what must be true of the first schema and the first module layout

| # | Rule | Why it cannot be retrofitted |
|---|---|---|
| 1 | **A principal on every durable fact.** Every record a person creates, changes, decides or is charged for carries an opaque, bounded `principal_id`. Its value comes from **one** configured source (a settings field with a fixed default such as `local-owner`); no literal is repeated in code, and a static check can enforce that. | The column is cheap to add later; the *history* is not. Every past change, correction and decision made before the column existed has no author, forever. "We add an owner column when we have users" loses exactly the audit a team will ask for. |
| 2 | **Ownership is a space; the person is provenance.** Every record belongs to a `space_id` (exactly one value exists today, e.g. `personal`); the creator or saver is recorded separately as provenance. | When a person leaves a team, their records must stay with the space. If the person *is* the owner column, offboarding orphans or deletes the team's data. |
| 3 | **Globally unique, stable identifiers** (ULID/UUID/content hash) as the durable identity; never machine-local autoincrement integers. | Two personal databases merged into one team space collide on integers; re-keying rewrites every reference. |
| 4 | **One decision point for access.** Exactly one function answers "may this principal perform this action on this record"; the service layer calls it on every read and write. Today it always allows. | Roles later are one more input to that function. Guards written per use-case or in the interface drift apart; the day someone audits them, no one can say what the policy is. |
| 5 | **Classification on records and one egress gate.** Each record carries a sensitivity/privacy class (one value is fine today). Anything that leaves the machine (fetching page titles, sync, a model call, sharing, telemetry) passes through one outbound gate that reads that class. If the app makes any outbound call on day 0, the gate exists on day 0. | Data-handling rules (what may reach which recipient) are the first thing a team or customer asks about; retrofitting them means finding every call site. |
| 6 | **Append-only history for human decisions and corrections**, each row stamped with the principal. Current state is a projection; corrections are never overwritten in place. | Overwritten corrections cannot be recovered or attributed; append-only rows are the audit trail teams and auditors expect, and they cost one insert. |
| 7 | **Content-addressed files under one configured root.** Durable references are hashes or record ids, never absolute host paths, and never a platform-specific path in code. | A reference that names a machine breaks on the second device, in object storage, and in every environment other than the first one. |
| 8 | **Configuration in one place** (principal, space, data root, recipients, caps). The environment (OS, paths, host, credentials) is deployment input, never a literal in source. | Anything hard-coded from the first environment is what breaks in the second. |
| 9 | **Forward-only numbered migrations from the first schema**, including for embedded databases. | A hand-edited schema has no history to bring a second install up to. |
| 10 | **One-direction layering with one implementation per boundary**: interface → service → domain → storage. The local listener is the future server's interface; the interface never reaches into storage. | A UI that speaks SQL is a rewrite when the store moves to a server. One implementation per boundary keeps the seam from becoming a framework. |
| 11 | **Caps in code for any paid or external effect**, reserved before the call and settled after, scoped by principal. | Spend and effect limits per person or team are a policy over the same scope key; without the key there is nothing to scope. |

Each row that applies is one `[S-### SEAM]` item with its reversal cost stated. Most cost a column, a
function or a config field. If a row costs more than that in the present stack, record why and defer it
with a trigger instead of building a bigger version.

## Ledger: what the ambition does *not* earn now

| Deferred | Trigger |
|---|---|
| Authentication, sign-in, SSO, sessions | a second named human user |
| Roles, groups, sharing rules, an admin interface | the same |
| Tenant or organisation entities, per-tenant isolation, row-level filtering | a request for a shared space across organisations |
| A server, shared database, sync, conflict handling | a second device or a second user |
| Billing, plans, entitlements, metering exports | the first paying customer |
| Audit export, retention policies, legal hold, compliance evidence | the first customer or auditor who asks |
| Observability stacks, deployment automation, multi-region | the declared production promise (see modes) |

A trigger firing is a report to the user, not permission. Promotion recomputes the real gaps from the
target mode; do not pre-build them.

## What each later step actually changes

- **Personal → team install:** `principal_id` is supplied by the organisation's login instead of the
  default; `space_id` gains a team value; the access function gains a role lookup; the egress gate gains
  the organisation's policy; organisation-held credentials replace personal ones. The schema is unchanged.
- **Team → multi-tenant service:** spaces nest under tenants; keys, isolation and residency become
  deployment configuration; billing and entitlements consult the same principal and space keys. The
  access function and egress gate are the same functions with more inputs.

If a step needs anything other than new values, new inputs to the two functions, and deployment
configuration, a day-0 rule was skipped.

## Rationalisations to refuse

| Excuse | Reality |
|---|---|
| "`ALTER TABLE … ADD COLUMN … DEFAULT` later is an afternoon" | The column is; the authorship of every earlier row is gone. |
| "Permissions go at the top of each use-case when we have users" | That is *n* decision points. Write the one function now; it returns allow. |
| "We only fetch page titles, that is not egress" | It is the first recipient. The gate that will later check classes must already be the path those calls take. |
| "Store attachments under the user's application-data folder" | Fine as the *configured default*; a literal path in code is the first environment leaking into all later ones. |
| "Integer ids are simpler for one user" | Merging two single-user databases is the first team task; integers make it a rewrite. |
| "Delete in place, it is my own data" | Trash, restore, sync tombstones and audit all need the soft-delete/append-only shape; none can be retrofitted onto hard deletes. |
| "The UI can query SQLite directly for now" | The loopback service is the future server; a UI on SQL is a second implementation of every read. |

## Worked example

A personal knowledge-base application (single owner, one laptop, embedded database, local files) applied
the rules as: `principal_id` in the settings model with a fixed default and a static test that the literal
appears in exactly one module; `space_id` on the content table with a default and a bounded check;
append-only event tables with an actor on every row and database-level immutability; one
`evaluate(record, recipient_profile, grants)` function as the only egress decision, reading a per-record
privacy class; content-addressed artifacts under the configured data root, referenced by hash; a budget
guard that reserves worst-case cost before any paid call and settles after; a content-free receipt for
every delegated job carrying the requesting principal. Team use was recorded as a deployment of the same
core behind a per-principal access boundary, triggered by a second named user, and nothing for it was
built. The same shape in a typed-language/relational stack is the same eleven rules: the column names,
the one policy function, the one settings object and the migration folder are what carry over, not the
database engine.
