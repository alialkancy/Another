# Feel the AGI Plan

_Last updated: 2025-10-31 14:15Z_

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
| [COD-2025-0022](../tickets/COD-2025-0022-enterprise-support-workflow-discovery-gap-analysis.md) | Enterprise Support Workflow Discovery & Gap Analysis | Active | P1 |
| [COD-2025-0023](../tickets/COD-2025-0023-author-enterprise-support-runbooks-training-curriculum.md) | Author Enterprise Support Runbooks & Training Curriculum | Backlog | P1 |
| [COD-2025-0024](../tickets/COD-2025-0024-support-tooling-integration-access-enablement.md) | Support Tooling Integration & Access Enablement | Backlog | P1 |
| [COD-2025-0025](../tickets/COD-2025-0025-resilience-regression-chaos-and-dr-validation.md) | Resilience Regression, Chaos, and DR Validation | Backlog | P1 |
| [COD-2025-0026](../tickets/COD-2025-0026-pilot-support-simulation-content-iteration.md) | Pilot Support Simulation & Content Iteration | Backlog | P1 |
| [COD-2025-0027](../tickets/COD-2025-0027-launch-readiness-review-production-enablement.md) | Launch Readiness Review & Production Enablement | Backlog | P1 |
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
| [COD-2025-0019](../tickets/COD-2025-0019-enterprise-support-runbooks-training-enablement.md) | Enterprise Support Runbooks & Training Enablement | Backlog | P1 |
| [COD-2025-0020](../tickets/COD-2025-0020-resilience-regression-chaos-and-dr-validation.md) | Resilience Regression, Chaos, and DR Validation | Backlog | P1 |
| [COD-2025-0021](../tickets/COD-2025-0021-launch-readiness-review-production-enablement.md) | Launch Readiness Review & Production Enablement | Backlog | P1 |

## Status Totals

- Active: 1
- Backlog: 21
- Done: 5

## Source Plan

```json
{"tickets":[{"title":"Enterprise Support Workflow Discovery & Gap Analysis","description":"Inventory current enterprise customer support touchpoints, tooling integrations, and escalation paths to confirm scope for the new runbooks. Partner with Support Ops, SRE, Security, and Compliance to capture SLAs, audit obligations, and telemetry expectations, documenting gaps that could block enablement. Produce a signed-off blueprint outlining prioritized workflows, required integrations, data retention needs, and RACI for subsequent build efforts.","acceptance_criteria":["Discovery findings, workflow maps, and RACI documented in shared design doc reviewed by Support Ops, SRE, Security, and Compliance","Gap list prioritized with risk level, owners, and mitigation timelines captured in tracker","Blueprint captures tooling integrations, data flows, telemetry/audit requirements, and dependency assumptions with traceable IDs","Programme director and Legal/Compliance provide written approval confirming SLA alignment and data-handling scope"]},{"title":"Author Enterprise Support Runbooks & Training Curriculum","description":"Using the approved blueprint, draft detailed L1-L3 runbooks across observability, auth, and DR scenarios with tooling procedures and guardrails. Build companion training curriculum (slides, labs, knowledge checks) aligned to Support Ops competencies and integrate artifacts into the LMS. Ensure language, access controls, and retention policies meet enterprise standards, and socialize the change log for downstream validation tickets.","acceptance_criteria":["Runbooks versioned in repo/docs with cross-links to blueprint requirement IDs and observability dashboards","Training curriculum uploaded to LMS with role-based access, completion tracking, and knowledge checks requiring ≥80% mastery","Documentation receives DocOps, Support Ops, and Compliance review sign-offs covering data handling and audit language","Runbook and training change log maintained with outstanding follow-ups noted for pilot and resilience tickets"]},{"title":"Support Tooling Integration & Access Enablement","description":"Configure and validate the PagerDuty, Slack, observability, and incident management integrations referenced in the runbooks. Confirm Support tier access, telemetry instrumentation, and data retention settings match enterprise guardrails. Deliver operational documentation so Support can execute workflows without engineering intervention.","acceptance_criteria":["Integration configurations (PagerDuty schedules, Slack channels/apps, observability dashboards, incident tooling) validated in staging and documented in repo/ops or runbook appendix","Support L1-L3 access and permissions confirmed with evidence (screenshots/logs) and exceptions tracked with remediation dates","Telemetry dashboards, alerts, and runbook deep links deployed with monitoring enabled and test events recorded","Operational handover notes and rollback procedures stored with acknowledgement from Support Ops and SRE"]},{"title":"Resilience Regression, Chaos, and DR Validation","description":"Execute the resilience validation suite with SRE, covering chaos experiments on auth pathways, DR failover drills, and observability regression checks. Confirm runbooks mirror observed behaviours, capture deviations as defects, and integrate fixes. Provide a consolidated report of scope, results, and remediation tracking in incident tooling and CI.","acceptance_criteria":["Chaos experiments, DR drills, and regression tests executed with logs and dashboards linked in repo/tests or shared runbook appendix","No Sev-High defects remain open; Sev-Medium items have owners, mitigation plan, and target dates captured","Updated resilience validation report circulated with acknowledgements from SRE, Security, and Support Ops","Runbooks and training materials updated for any behavioural drift with new version tags and change summary logged","Automated or scheduled resilience checks registered in CI/monitoring with latest run artifacts green"]},{"title":"Pilot Support Simulation & Content Iteration","description":"Facilitate a pilot session with Support SMEs running end-to-end scenarios using finalized runbooks and tooling. Measure workflow adherence, response times, and clarity while capturing qualitative feedback. Fold learnings into updated assets and secure stakeholder approval for GA rollout.","acceptance_criteria":["Pilot agenda, scenarios, and participant roster published; attendance, recordings, and telemetry snapshots stored","Feedback backlog populated with severity, owner, and due date; all high/medium findings resolved or accepted with mitigation before GA","Tooling integrations exercised end-to-end with incident lifecycle traces attached as evidence","Runbooks and training curriculum updated per pilot outcomes with version history and release notes distributed to Support","Support leadership, Documentation, and Programme director record go/no-go decision for general rollout"]},{"title":"Launch Readiness Review & Production Enablement","description":"Conduct the final launch readiness review spanning support enablement, resilience outcomes, documentation, observability, and communications. Verify catalogue updates, release notes, accessibility checks, and operational dashboards meet go-live standards. Confirm all QA, security, compliance, and training sign-offs are recorded, update the release checklist, and communicate launch approvals to stakeholders.","acceptance_criteria":["Comprehensive readiness checklist completed with signatures from Support, SRE, Security, Compliance, Product, and Legal","Latest release candidate shows green CI/CD pipeline, linting, unit/integration tests, security and accessibility scans, and observability alarms","Internal and external release communications approved, archived, and distribution plan executed; hypercare schedule published","Change management record updated with launch decision, cutover window, rollback plan, and stakeholder distribution list","Post-launch monitoring and retro plan (T+1/T+7) documented with owners and success metrics"]}]}
```
