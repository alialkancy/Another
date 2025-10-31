# Feel the AGI Plan

_Last updated: 2025-10-31 13:55Z_

Refer to `/codex/STATE.md` for the authoritative ticket dashboard.

## Execution Prompt

## Prompt — "Execute tickets or plan end-to-end (v1 minimal)"

You are at the **repository root**. This repo uses a lightweight, Markdown-based planning system under `/codex`. Your job is to **take one or more tickets, or an entire plan**, implement them end-to-end, open/merge PRs, and keep `/codex` up to date.

### The system (must follow exactly)

* **Files & folders**

  * `/codex/STATE.md` — single dashboard table.
  * `/codex/plans/*.md` — high-level plans.
  * `/codex/tickets/*.md` — **one file per ticket**. Tickets are **never moved or renamed**.
* **Ticket front-matter (exact keys)**

  * `id, title, status, priority, owner, created`
* **Allowed values**

  * `status`: `backlog | active | blocked | done | dropped`
  * `priority`: `P0 | P1 | P2 | P3`
* **Ticket body sections (in this order)**

  * `## Context` · `## Plan` · `## Acceptance` · `## Links` · `## Log`
* **Updates & logging**

  * Append timestamped lines to `## Log`. Format: `YYYY-MM-DD HH:MMZ — <action>`.
  * Add PR URLs under `## Links` → `PRs:`.
  * Update `/codex/STATE.md` after each work session.
* **Do not edit** tickets with `status: done` (typo fixes only).

### What you may change

* **Any application code** required to implement tickets.
* `/codex/**` files as described.
* You **must not** modify non-codex docs or meta unless a ticket explicitly requires it.

### Inputs (one of the following will be provided)

* **A list of ticket IDs** (e.g., `COD-2025-0007, COD-2025-0012`), **or**
* **A plan file** under `/codex/plans/` (e.g., `2025-10-07-infra-guardrails.md`), **or**
* **Nothing** (default: work the highest-priority `active` tickets from `/codex/STATE.md`; if none, pick top `backlog`).

> If a plan is provided, prioritize items listed under **Committed** in the order shown; then **Stretch**.

---

## Work cycle (repeat per ticket)

1. **Select ticket**

   * If given IDs: process them in the order provided.
   * If given a plan: pick the next uncompleted **Committed** item.
   * Else: choose the highest-priority item from `STATE.md` (`active` first, then `backlog`).
   * **Skip** tickets with `status: done` or `dropped`.

2. **Read & validate**

   * Open `/codex/tickets/<ID>-*.md`.
   * Ensure the front-matter keys are present. If missing or malformed, fix minimally.
   * If acceptance criteria are unclear, infer **2–5 objective checks** and insert under `## Acceptance` (keep concise).

3. **Activate**

   * If current `status` is `backlog`, set to `active`.
   * Append Log: `YYYY-MM-DD HH:MMZ — Started work; created branch <branch-name>`.

4. **Branch & implement**

   * Branch name: `codex/<ID>-<short-slug>`.
   * Make **small, reviewable** commits. Add/adjust tests first where feasible.
   * Keep changes scoped to the ticket's `## Plan` and acceptance.

5. **Quality gates**

   * Run tests/lint/format; add missing tests.
   * Update user/docs if the change alters behavior.
   * If blocked, set `status: blocked`, add a **one-line reason** in the Log and a short **Unblock plan** at the top of `## Plan`. Then **move on to the next ticket**.

6. **Open PR**

   * One PR **per ticket** (unless extremely small changes; then you may batch closely related tickets—but prefer 1:1).
   * PR title: `<ID>: <short title>`.
   * PR body:

     * **Context** (2–4 lines)
     * **Changes** (bullets)
     * **Tests** (what was added/updated)
     * **Acceptance** (mirror ticket's checkboxes; mark those met)
     * **Risk/Rollback**
     * Link to the ticket file path.
   * Add the PR URL under the ticket's `## Links`.
   * Update `/codex/STATE.md` (`PRs` count, `Updated` date).

7. **Merge**

   * If you have permission and checks pass, **merge** (squash or merge-commit per repo norms).
   * If you cannot merge, set the PR to "ready for review", label as needed, and **continue** to the next ticket.

8. **Close out**

   * After merge:

     * Tick relevant `## Acceptance` checkboxes.
     * Set `status: done`.
     * Append Log: `YYYY-MM-DD HH:MMZ — Merged <PR-URL>; marking done.`
     * Update `/codex/STATE.md` row (`Status = done`, `PRs` count, `Updated` date).

---

## Creating **new tickets** (when appropriate)

Create a **new ticket** under `/codex/tickets/` if you encounter:

* A follow-up change that would expand scope materially,
* A bug uncovered during work that isn't a quick fix,
* A distinct task needed to unblock the current ticket.

**How to create (minimal)**

* Allocate the next ID: `COD-<YEAR>-<NNNN>` (scan existing IDs; zero-pad NNNN).
* Use the minimal front-matter with `status: backlog`, `priority: P1` unless context dictates otherwise.
* Keep body sections in required order and add a 1–2 line `## Plan`.
* Add a Log entry: `Imported during execution of <ID-where-found>.`
* Add a row to `/codex/STATE.md`.

---

## Plan handling

* Plans in `/codex/plans/*.md` are **selection guides**, not progress trackers.
* **Do not** edit plan contents for status; only use them to order work.
* If you need to record progress in a plan PR, append a short **"Progress"** section at the bottom (optional), listing completed IDs.

---

## Commit & PR standards

* **Commit message** (for main implementation commit):

  ```
  <ID>: <short imperative summary>

  Why:
  <1–3 lines>

  What:
  - change 1
  - change 2

  Tests:
  - test case 1
  ```
* **PR must link** back to the ticket file and mention the acceptance checks satisfied.

---

## When to stop

* All targeted tickets are either **done** or **blocked** with a clear reason and unblock plan, **or**
* You reached a natural stopping point with all PRs opened and `/codex/STATE.md` updated.

---

## Output checklist (each session)

* For each worked ticket:

  * Ticket file updated (status/log/links/acceptance).
  * Branch & PR opened; merged if permitted.
  * `/codex/STATE.md` updated.
* For any new tickets:

  * New file created with correct schema; added to `STATE.md`.

---

## Begin

* Identify targets:

  * If specific ticket IDs or a plan file were provided, use those.
  * Else, choose top-priority `active` tickets from `STATE.md`, then highest-priority `backlog`.
* Proceed with the **Work cycle** above, one ticket at a time.

## Tickets

| ID | Title | Status | Priority |
| --- | --- | --- | --- |
| [COD-2025-0001](../tickets/COD-2025-0001-baseline-login-requirements-architecture-and-guardrails.md) | Baseline Login Requirements, Architecture, and Guardrails | Done | P1 |
| [COD-2025-0006](../tickets/COD-2025-0006-finalize-auth-integration-contract-and-observability-spec.md) | Finalize Auth Integration Contract and Observability Spec | Done | P1 |
| [COD-2025-0010](../tickets/COD-2025-0010-responsive-shell-auth-hardening-qa-sign-off.md) | Responsive Shell Auth Hardening & QA Sign-off | Done | P1 |
| [COD-2025-0013](../tickets/COD-2025-0013-operationalize-observability-blueprint-dependency-closure.md) | Operationalize Observability Blueprint & Dependency Closure | Done | P1 |
| [COD-2025-0014](../tickets/COD-2025-0014-implement-auth-telemetry-pipeline-alert-policies.md) | Implement Auth Telemetry Pipeline & Alert Policies | Backlog | P1 |
| [COD-2025-0015](../tickets/COD-2025-0015-enterprise-runbooks-support-enablement-and-training.md) | Enterprise Runbooks, Support Enablement, and Training | Backlog | P1 |
| [COD-2025-0016](../tickets/COD-2025-0016-enterprise-regression-chaos-and-dr-validation.md) | Enterprise Regression, Chaos, and DR Validation | Backlog | P1 |
| [COD-2025-0017](../tickets/COD-2025-0017-launch-readiness-review-production-enablement.md) | Launch Readiness Review & Production Enablement | Backlog | P1 |
| [COD-2025-0002](../tickets/COD-2025-0002-implement-feature-flagged-responsive-login-shell.md) | Implement Feature-Flagged Responsive Login Shell | Backlog | P1 |
| [COD-2025-0003](../tickets/COD-2025-0003-integrate-authentication-logic-and-observability.md) | Integrate Authentication Logic and Observability | Backlog | P1 |
| [COD-2025-0004](../tickets/COD-2025-0004-automated-test-accessibility-and-telemetry-verification.md) | Automated Test, Accessibility, and Telemetry Verification | Backlog | P1 |
| [COD-2025-0005](../tickets/COD-2025-0005-finalize-documentation-and-launch-readiness.md) | Finalize Documentation and Launch Readiness | Backlog | P1 |
| [COD-2025-0007](../tickets/COD-2025-0007-wire-responsive-shell-to-auth-services-behind-feature-flag.md) | Wire Responsive Shell to Auth Services Behind Feature Flag | Backlog | P1 |
| [COD-2025-0008](../tickets/COD-2025-0008-quality-verification-accessibility-and-operational-hardening.md) | Quality Verification, Accessibility, and Operational Hardening | Backlog | P1 |
| [COD-2025-0009](../tickets/COD-2025-0009-launch-readiness-runbooks-and-progressive-rollout-plan.md) | Launch Readiness, Runbooks, and Progressive Rollout Plan | Backlog | P1 |
| [COD-2025-0011](../tickets/COD-2025-0011-enterprise-docs-runbooks-and-support-enablement.md) | Enterprise Docs, Runbooks, and Support Enablement | Backlog | P1 |
| [COD-2025-0012](../tickets/COD-2025-0012-launch-readiness-progressive-rollout-and-post-launch-monitor.md) | Launch Readiness, Progressive Rollout, and Post-Launch Monitoring | Backlog | P1 |

## Status Totals

- Active: 0
- Backlog: 13
- Done: 4

## Source Plan

```json
{
  "tickets": [
    {
      "title": "Operationalize Observability Blueprint & Dependency Closure",
      "description": "Convert the approved observability blueprint into an executable plan that locks sequencing with partner teams. Align data flows, access controls, and rollout timelines with SRE, security, data platform, and support so downstream implementation can land without blocking the enterprise launch window.",
      "acceptance_criteria": [
        "Observability implementation plan reviewed with platform SRE, security, data platform, and support leads covering data sources, emission formats, retention, and escalation paths",
        "Dependency matrix published outlining feature flags, IAM scopes, service accounts, and incident tooling integrations with named owners and landing dates",
        "Risks, open questions, and cross-team handoffs captured in the program tracker with owners and target resolution dates",
        "Sequencing plan documented showing how telemetry delivery, docs/runbooks, validation, and launch checkpoints align to the release calendar"
      ]
    },
    {
      "title": "Implement Auth Telemetry Pipeline & Alert Policies",
      "description": "Ship the instrumentation and configuration defined in the observability plan. Wire login services into centralized metrics, logs, and tracing stacks, enforce privacy guardrails, and stand up staging dashboards and alerts that underpin support runbooks and launch gating.",
      "acceptance_criteria": [
        "Telemetry code merged behind feature flags with unit/contract tests covering event emission, schema validation, and PII redaction",
        "Privacy, security, and data platform reviews sign off on schemas, retention windows, and data minimization controls prior to enabling the flags",
        "Dashboards and alert policies deployed in staging with documented thresholds, linked runbooks, and ownership recorded",
        "Synthetic login and failure smoke tests exercise metrics/logs/traces end-to-end in CI and staging with results archived and acknowledged by SRE/support"
      ]
    },
    {
      "title": "Enterprise Runbooks, Support Enablement, and Training",
      "description": "Finalize operational documentation and prepare support teams for the telemetry-backed enterprise login launch. Ensure runbooks reflect instrumentation, dashboards, alert paths, and rollback procedures, and confirm the support org is trained on the workflows.",
      "acceptance_criteria": [
        "Runbooks, SOPs, and knowledge base articles updated in-repo to cover telemetry signals, alert responses, rollback steps, and customer comms templates",
        "Support enablement sessions delivered with attendance captured, Q&A documented, and follow-up actions closed",
        "Staging dry run of an alert escalation executed using new dashboards with lessons incorporated into docs before sign-off",
        "Support and SRE leadership record approval of the operational playbooks in the project tracker"
      ]
    },
    {
      "title": "Enterprise Regression, Chaos, and DR Validation",
      "description": "Execute the full validation suite across enterprise identity providers, MFA paths, and failure scenarios. Layer in chaos experiments and disaster recovery drills to confirm resilience, ensuring findings feed back into remediation before launch gates.",
      "acceptance_criteria": [
        "Automated and manual regression results published covering all enterprise login permutations, with critical defects resolved or formally waived with VP approval",
        "Chaos experiments and DR drills documented with recovery metrics and evidence that runbooks remain accurate post-testing",
        "Security regression suite updated to include telemetry-related surfaces with results linked in the tracker and gaps triaged",
        "All remediation actions tracked with owners and due dates, with no high-severity issues left unassigned at exit"
      ]
    },
    {
      "title": "Launch Readiness Review & Production Enablement",
      "description": "Run the final cross-functional launch review to verify implementation, validation, and operational readiness. Confirm rollout strategy, post-launch monitoring, and communication cadences before recording the go/no-go decision with release management.",
      "acceptance_criteria": [
        "Launch readiness checklist completed with sign-offs from product, engineering, SRE, security, and support",
        "Progressive rollout plan, feature flag strategy, rollback playbook, and customer comms schedule documented and approved",
        "All high-severity defects closed or waived with explicit mitigation owners and timelines recorded",
        "Post-launch monitoring dashboards, alert routing, on-call rotations, and comms plan validated; go/no-go decision logged in the project tracker"
      ]
    }
  ]
}
```
