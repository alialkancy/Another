# Feel the AGI Plan

_Last updated: 2025-10-31 13:32Z_

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
| [COD-2025-0001](../tickets/COD-2025-0001-baseline-login-requirements-architecture-and-guardrails.md) | Baseline Login Requirements, Architecture, and Guardrails | Active | P1 |
| [COD-2025-0002](../tickets/COD-2025-0002-implement-feature-flagged-responsive-login-shell.md) | Implement Feature-Flagged Responsive Login Shell | Backlog | P1 |
| [COD-2025-0003](../tickets/COD-2025-0003-integrate-authentication-logic-and-observability.md) | Integrate Authentication Logic and Observability | Backlog | P1 |
| [COD-2025-0004](../tickets/COD-2025-0004-automated-test-accessibility-and-telemetry-verification.md) | Automated Test, Accessibility, and Telemetry Verification | Backlog | P1 |
| [COD-2025-0005](../tickets/COD-2025-0005-finalize-documentation-and-launch-readiness.md) | Finalize Documentation and Launch Readiness | Backlog | P1 |

## Status Totals

- Active: 1
- Backlog: 4

## Source Plan

```json
{
  "tickets": [
    {
      "title": "Baseline Login Requirements, Architecture, and Guardrails",
      "description": "Run a focused discovery with product, design, security, auth-platform, and analytics stakeholders to finalize functional and non-functional requirements for the new login page. Audit existing authentication flows, routing, localization, telemetry, and shared UI components to document integration points, constraints, and data contracts. Produce an architecture brief that maps UI states, error handling, feature flag strategy, observability hooks, and rollback considerations. Capture compliance/privacy concerns, dependency timelines, and owners so downstream execution has clear guardrails.",
      "acceptance_criteria": [
        "Signed-off login requirements covering functional scope, accessibility, performance, and localization expectations from product, design, and security",
        "Architecture brief detailing UI composition, state management, service/API interactions, data contracts, telemetry events, feature flag strategy, and rollback approach",
        "Dependency and risk register including compliance/privacy items, backend/config prerequisites, and mitigation owners with due dates",
        "All artifacts linked in the project knowledge base with reviewer access and documented open questions"
      ]
    },
    {
      "title": "Implement Feature-Flagged Responsive Login Shell",
      "description": "Implement the agreed-upon page skeleton with responsive layout, design system tokens, and placeholder components for form controls, error banners, SSO/password-reset entry points, and loading states. Wire the page into navigation behind the feature flag without impacting existing traffic, and document smoke-test results that prove legacy flows remain intact. Ensure base accessibility scaffolding (landmarks, focus order, keyboard traps) is in place and collaborate with design to validate visual parity, capturing gaps for follow-up.",
      "acceptance_criteria": [
        "Feature-flagged route reachable in non-production environments with regression smoke notes confirming existing login paths are unaffected",
        "Responsive layout implemented with approved design system primitives and design sign-off documented with screenshots for target breakpoints",
        "Placeholder elements, loading states, and accessibility scaffolding (semantic landmarks, focus management, aria hooks) implemented and documented",
        "Open UX or component gaps captured as tracked issues linked from the ticket"
      ]
    },
    {
      "title": "Integrate Authentication Logic and Observability",
      "description": "Connect the login form to the authentication service per the defined contract, handling happy path, invalid credentials, lockout, and network failure scenarios with secure, localized messaging. Implement client-side validation, rate limiting, and form state controls (loading, disablement, retries) that satisfy security guidance. Instrument telemetry for attempts, failures, successes, and lockouts, ensuring events flow to staging analytics. Coordinate with auth/backend teams for any API or environment configuration updates, and document the data flow for privacy review.",
      "acceptance_criteria": [
        "Form submission authenticates against the target staging environment using the agreed API contract, with lockout and error flows verified",
        "Client-side validation enforcing required fields, password rules, retry limits, and secure error copy that avoids leaking sensitive detail",
        "Telemetry events for success, failure, and lockout visible in staging analytics dashboards with sample event IDs attached",
        "Security/privacy review sign-off recorded, including documentation of data flows, environment/secrets configuration changes, and residual risks"
      ]
    },
    {
      "title": "Automated Test, Accessibility, and Telemetry Verification",
      "description": "Create automated coverage for the login experience: unit tests for validation logic, integration tests for API interactions and error paths, and end-to-end tests that exercise feature-flag toggling and primary flows. Execute automated (e.g., axe) and targeted manual accessibility audits validating keyboard navigation, screen reader announcements, and focus management. Partner with QA on the cross-browser/device matrix, recording findings and follow-ups. Configure telemetry alert thresholds and validate them by injecting test events, capturing the runbook for monitoring.",
      "acceptance_criteria": [
        "Unit, integration, and end-to-end tests added to CI with passing runs and updated coverage metrics reported",
        "Automated and manual accessibility audits executed with no outstanding critical issues and remediation notes captured",
        "Cross-browser and device matrix executed with QA sign-off or tracked follow-up items linked to owners",
        "Telemetry alert thresholds configured, verified via test events, and documented with runbook steps in the knowledge base"
      ]
    },
    {
      "title": "Finalize Documentation and Launch Readiness",
      "description": "Update user-facing documentation, support runbooks, and internal onboarding materials to reflect the new login experience, including feature flag management and rollback instructions. Prepare release notes, outline the staged rollout plan with success metrics, and confirm monitoring dashboards and alerts are ready. Ensure linting, typing, security scans, and required approvals are green. Facilitate a go/no-go checkpoint with product, design, QA, security, and support, capturing decisions and outstanding watch items.",
      "acceptance_criteria": [
        "Documentation, support runbooks, and release notes updated with reviewer approvals and linked from the ticket",
        "Feature flag plan, staged rollout steps, success metrics, and rollback procedure completed in the launch checklist",
        "All linting, type checks, security scans, and required CI gates passing for the login feature branch",
        "Stakeholder go/no-go decision recorded with sign-off from product, design, QA, security, and support, including any launch watch items"
      ]
    }
  ]
}
```
