# Feel the AGI Plan

_Last updated: 2025-10-31 13:40Z_

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
| [COD-2025-0006](../tickets/COD-2025-0006-finalize-auth-integration-contract-and-observability-spec.md) | Finalize Auth Integration Contract and Observability Spec | Active | P1 |
| [COD-2025-0007](../tickets/COD-2025-0007-wire-responsive-shell-to-auth-services-behind-feature-flag.md) | Wire Responsive Shell to Auth Services Behind Feature Flag | Backlog | P1 |
| [COD-2025-0008](../tickets/COD-2025-0008-quality-verification-accessibility-and-operational-hardening.md) | Quality Verification, Accessibility, and Operational Hardening | Backlog | P1 |
| [COD-2025-0009](../tickets/COD-2025-0009-launch-readiness-runbooks-and-progressive-rollout-plan.md) | Launch Readiness, Runbooks, and Progressive Rollout Plan | Backlog | P1 |
| [COD-2025-0002](../tickets/COD-2025-0002-implement-feature-flagged-responsive-login-shell.md) | Implement Feature-Flagged Responsive Login Shell | Backlog | P1 |
| [COD-2025-0003](../tickets/COD-2025-0003-integrate-authentication-logic-and-observability.md) | Integrate Authentication Logic and Observability | Backlog | P1 |
| [COD-2025-0004](../tickets/COD-2025-0004-automated-test-accessibility-and-telemetry-verification.md) | Automated Test, Accessibility, and Telemetry Verification | Backlog | P1 |
| [COD-2025-0005](../tickets/COD-2025-0005-finalize-documentation-and-launch-readiness.md) | Finalize Documentation and Launch Readiness | Backlog | P1 |

## Status Totals

- Active: 1
- Backlog: 7
- Done: 1

## Source Plan

```json
{
  "tickets": [
    {
      "title": "Finalize Auth Integration Contract and Observability Spec",
      "description": "Produce the detailed integration source of truth linking the responsive shell, backend auth services, and identity provider. Capture sequence diagrams, API contracts, feature-flag behavior, and resiliency expectations so implementation can proceed without ambiguity. Extend the document with data-handling notes (PII redaction, retention windows) and confirm infrastructure prerequisites or migrations. Pair this with a full observability spec enumerating metrics, traces, logs, dashboards, alert thresholds, and ownership, aligning with security, platform, and data teams before coding continues.",
      "acceptance_criteria": [
        "Versioned integration spec includes auth sequence diagrams, API contracts, retry/backoff semantics, session lifetime, rate limiting, fallback paths, and data-handling requirements; approved by security, platform, and identity provider reviewers",
        "Observability spec lists metrics, logs, traces, dashboards, alert thresholds, sampling, and data retention with named owners; sign-off recorded with data platform and observability leads",
        "Cross-team dependencies (identity provider updates, infrastructure tasks, feature-flag config) captured on the project board with owners, target dates, and tracked risks",
        "Implementation readiness review held with FE, BE, security, and observability leads; approval recorded in the ticket"
      ]
    },
    {
      "title": "Wire Responsive Shell to Auth Services Behind Feature Flag",
      "description": "Implement the end-to-end auth handshake using the signed-off contract, ensuring the responsive shell negotiates tokens securely with backend services and gracefully falls back when the flag is disabled. Add resilient error handling, rate-limit awareness, and retries, and validate session persistence against compliance guidance. Instrument telemetry exactly as specified and coordinate with DevOps to propagate feature-flag configurations across environments, performing staging rollouts that vet both success and failure paths with QA and security partners.",
      "acceptance_criteria": [
        "Feature flag toggles the new auth path on/off without regression; staging end-to-end tests validate login success, failure messaging, and legacy fallback behavior with proper session/token handling",
        "Automated unit and integration tests cover success, retry, timeout, and error scenarios, including telemetry emission and token lifecycle edge cases; results linked in the ticket",
        "Telemetry events (login success/failure, flag transitions, retry counts) flow into agreed staging dashboards with schemas validated for redaction and field completeness",
        "Feature-flag configurations deployed across dev/staging environments with DevOps; pair review with backend owner completed and security/QA sign-offs recorded"
      ]
    },
    {
      "title": "Quality Verification, Accessibility, and Operational Hardening",
      "description": "Bring the implementation to launch-quality by expanding automated coverage, executing manual QA, and hardening accessibility and operational posture. Close the loop on responsiveness across devices, validate telemetry health checks, and resolve identified defects. Ensure WCAG compliance, refresh security/privacy scans, and exercise observability alerts so on-call teams can respond confidently.",
      "acceptance_criteria": [
        "CI passes full suite of unit, integration, and E2E tests with new cases covering responsive interactions, auth edge cases, and telemetry hooks; coverage deltas documented",
        "Manual QA matrix across supported browsers/devices and feature-flag states executed with findings triaged and resolved",
        "Accessibility audit against WCAG 2.1 AA completed, remediations verified, and accessibility reviewer approval captured",
        "Security/privacy checks (static analysis, dependency scan, token storage review) updated for the new auth path; issues resolved or exceptions approved",
        "Observability dry run performed by triggering synthetic success/failure signals to validate alert thresholds, routing, and on-call readiness"
      ]
    },
    {
      "title": "Launch Readiness, Runbooks, and Progressive Rollout Plan",
      "description": "Consolidate all artifacts and operational agreements required for launch. Finalize runbooks, rollback and comms plans, and confirm production monitoring stands ready. Define the staged rollout strategy, success metrics, and abort criteria, securing approvals from product, release, and support stakeholders so the team can execute the launch confidently.",
      "acceptance_criteria": [
        "Launch go/no-go checklist completed with runbook, rollback strategy, customer-facing release notes, and support FAQs approved by product and release management",
        "Production dashboards and alerts deployed with owners, escalation paths, and data-retention confirmations documented",
        "Progressive rollout plan defines flag ramp schedule, success and abort metrics, and communication cadence; sign-off from release management and support captured",
        "Final readiness approvals recorded from QA lead, accessibility lead, security representative, and release manager"
      ]
    }
  ]
}
```
