# Feel the AGI Plan

_Last updated: 2025-10-31 18:20Z_

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
| [COD-2025-0018](../tickets/COD-2025-0018-auth-telemetry-operational-validation-observability-handoff.md) | Auth Telemetry Operational Validation & Observability Handoff | Done | P1 |
| [COD-2025-0019](../tickets/COD-2025-0019-enterprise-support-runbooks-training-enablement.md) | Enterprise Support Runbooks & Training Enablement | Backlog | P1 |
| [COD-2025-0020](../tickets/COD-2025-0020-resilience-regression-chaos-and-dr-validation.md) | Resilience Regression, Chaos, and DR Validation | Backlog | P1 |
| [COD-2025-0021](../tickets/COD-2025-0021-launch-readiness-review-production-enablement.md) | Launch Readiness Review & Production Enablement | Backlog | P1 |
| [COD-2025-0002](../tickets/COD-2025-0002-implement-feature-flagged-responsive-login-shell.md) | Implement Feature-Flagged Responsive Login Shell | Backlog | P1 |
| [COD-2025-0003](../tickets/COD-2025-0003-integrate-authentication-logic-and-observability.md) | Integrate Authentication Logic and Observability | Backlog | P1 |
| [COD-2025-0004](../tickets/COD-2025-0004-automated-test-accessibility-and-telemetry-verification.md) | Automated Test, Accessibility, and Telemetry Verification | Backlog | P1 |
| [COD-2025-0005](../tickets/COD-2025-0005-finalize-documentation-and-launch-readiness.md) | Finalize Documentation and Launch Readiness | Backlog | P1 |
| [COD-2025-0007](../tickets/COD-2025-0007-wire-responsive-shell-to-auth-services-behind-feature-flag.md) | Wire Responsive Shell to Auth Services Behind Feature Flag | Backlog | P1 |
| [COD-2025-0008](../tickets/COD-2025-0008-quality-verification-accessibility-and-operational-hardening.md) | Quality Verification, Accessibility, and Operational Hardening | Backlog | P1 |
| [COD-2025-0009](../tickets/COD-2025-0009-launch-readiness-runbooks-and-progressive-rollout-plan.md) | Launch Readiness, Runbooks, and Progressive Rollout Plan | Backlog | P1 |
| [COD-2025-0011](../tickets/COD-2025-0011-enterprise-docs-runbooks-and-support-enablement.md) | Enterprise Docs, Runbooks, and Support Enablement | Backlog | P1 |
| [COD-2025-0012](../tickets/COD-2025-0012-launch-readiness-progressive-rollout-and-post-launch-monitor.md) | Launch Readiness, Progressive Rollout, and Post-Launch Monitoring | Backlog | P1 |
| [COD-2025-0014](../tickets/COD-2025-0014-implement-auth-telemetry-pipeline-alert-policies.md) | Implement Auth Telemetry Pipeline & Alert Policies | Backlog | P1 |
| [COD-2025-0015](../tickets/COD-2025-0015-enterprise-runbooks-support-enablement-and-training.md) | Enterprise Runbooks, Support Enablement, and Training | Backlog | P1 |
| [COD-2025-0016](../tickets/COD-2025-0016-enterprise-regression-chaos-and-dr-validation.md) | Enterprise Regression, Chaos, and DR Validation | Backlog | P1 |
| [COD-2025-0017](../tickets/COD-2025-0017-launch-readiness-review-production-enablement.md) | Launch Readiness Review & Production Enablement | Backlog | P1 |

## Status Totals

- Active: 0
- Backlog: 16
- Done: 5

## Source Plan

```json
{"tickets":[{"title":"Auth Telemetry Operational Validation & Observability Handoff","description":"Validate the end-to-end auth telemetry pipeline with downstream consumers, ensuring coverage, data quality, and alert fidelity before broader enablement. Partner with Data Engineering, SecOps, and SRE to confirm stream-to-warehouse ingest, populate dashboards, and exercise alert policies against seeded failure modes. Capture gaps plus ownership so subsequent enablement work has clear inputs.","acceptance_criteria":["Key auth flow events (login, MFA, password reset, admin override) appear in warehouse tables within agreed latency SLAs and match the contract schema, with Data Engineering and SRE sign-off","Grafana/Looker dashboards for auth KPIs render with live data, include named operational owners, and document metric definitions in `/docs/observability/auth-telemetry.md`","Alert policies fire and auto-resolve in staging during seeded failure drills, with SecOps approval recorded in the validation doc","Validation summary in `/docs/observability/auth-telemetry.md` lists any open issues with owners, severity, and target resolution dates"]},{"title":"Enterprise Support Runbooks & Training Enablement","description":"Translate validated telemetry insights into actionable L1/L2 runbooks, escalation matrices, and training assets. Coordinate with Support Ops to map incident workflows, integrate knowledge articles into Zendesk/ServiceNow, and pilot the materials to confirm readiness and tool alignment.","acceptance_criteria":["Ops runbooks for auth incidents published in `/docs/runbooks/auth/`, covering detection, triage, and escalation flows, with Support Ops and SecOps approvals","Training deck and recorded walkthrough linked from the enablement portal and referenced in the repository README, with pilot completion sign-off","Zendesk/ServiceNow knowledge articles live with tagged owners, review cadence, and cross-links to telemetry dashboards and runbooks","Pilot dry-run feedback logged, all Sev-blocker items resolved or tracked with owners and due dates prior to starting resilience validation work"]},{"title":"Resilience Regression, Chaos, and DR Validation","description":"Execute the enterprise regression battery, run targeted chaos experiments on telemetry dependencies, and validate DR playbooks against RTO/RPO commitments. Coordinate with QA Automation, Chaos Engineering, and Infra to ensure findings are remediated or tracked ahead of launch gating.","acceptance_criteria":["Full auth regression suite run on staging with results archived under `/reports/auth-regression/`, and no Sev1/Sev2 defects left open without an approved waiver","Chaos experiments covering queue outages, downstream datastore latency, and alert channel failures executed, with findings and mitigations documented and assigned owners","DR drill results meet stated RTO/RPO targets, with Infra and Compliance approvals captured","Observability dashboards updated with resilience metrics and QA validation notes attached; any monitoring gaps are ticketed with owners and due dates"]},{"title":"Launch Readiness Review & Production Enablement","description":"Aggregate outputs from prior tickets into a launch readiness packet covering telemetry health, support preparedness, resilience posture, and compliance attestations. Facilitate the cross-functional go/no-go, confirming rollout logistics, rollback paths, and post-launch coverage.","acceptance_criteria":["Launch readiness checklist completed with linked evidence for testing, lint, accessibility, observability, documentation, and runbooks; all blocking gaps closed or waivers approved","Go/No-Go meeting notes filed in `/docs/release/readiness-auth.md`, including decision log and approvals from Product, Security, SRE, and Support leadership","Rollback and contingency plan reviewed by on-call leads, attached to the deployment README, and contact tree confirmed","Post-launch monitoring and communications plan distributed to stakeholders with acknowledgments recorded, and on-call rotations staffed for the launch window"]}]}
```
