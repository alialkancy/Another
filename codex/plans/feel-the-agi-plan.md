# Feel the AGI Plan

_Last updated: 2025-10-31 13:49Z_

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
| [COD-2025-0010](../tickets/COD-2025-0010-responsive-shell-auth-hardening-qa-sign-off.md) | Responsive Shell Auth Hardening & QA Sign-off | Active | P1 |
| [COD-2025-0011](../tickets/COD-2025-0011-enterprise-docs-runbooks-and-support-enablement.md) | Enterprise Docs, Runbooks, and Support Enablement | Backlog | P1 |
| [COD-2025-0012](../tickets/COD-2025-0012-launch-readiness-progressive-rollout-and-post-launch-monitor.md) | Launch Readiness, Progressive Rollout, and Post-Launch Monitoring | Backlog | P1 |
| [COD-2025-0002](../tickets/COD-2025-0002-implement-feature-flagged-responsive-login-shell.md) | Implement Feature-Flagged Responsive Login Shell | Backlog | P1 |
| [COD-2025-0003](../tickets/COD-2025-0003-integrate-authentication-logic-and-observability.md) | Integrate Authentication Logic and Observability | Backlog | P1 |
| [COD-2025-0004](../tickets/COD-2025-0004-automated-test-accessibility-and-telemetry-verification.md) | Automated Test, Accessibility, and Telemetry Verification | Backlog | P1 |
| [COD-2025-0005](../tickets/COD-2025-0005-finalize-documentation-and-launch-readiness.md) | Finalize Documentation and Launch Readiness | Backlog | P1 |
| [COD-2025-0007](../tickets/COD-2025-0007-wire-responsive-shell-to-auth-services-behind-feature-flag.md) | Wire Responsive Shell to Auth Services Behind Feature Flag | Backlog | P1 |
| [COD-2025-0008](../tickets/COD-2025-0008-quality-verification-accessibility-and-operational-hardening.md) | Quality Verification, Accessibility, and Operational Hardening | Backlog | P1 |
| [COD-2025-0009](../tickets/COD-2025-0009-launch-readiness-runbooks-and-progressive-rollout-plan.md) | Launch Readiness, Runbooks, and Progressive Rollout Plan | Backlog | P1 |

## Status Totals

- Active: 1
- Backlog: 9
- Done: 2

## Source Plan

```json
{"tickets":[{"title":"Responsive Shell Auth Hardening & QA Sign-off","description":"Exercise the responsive shell end-to-end with the feature flag enabled in staging and internal dogfood, validating auth flows, responsive breakpoints, accessibility, and telemetry before exposing external traffic. Partner with Identity, Design, and QA to capture regressions, confirm observability coverage, and ensure any gaps have owners or fixes merged.","acceptance_criteria":["Test matrix covering primary and edge auth flows across desktop/mobile viewports, major browsers, and failure scenarios is reviewed and signed off by QA with run results attached","Session refresh, MFA, sign-out, and error recovery paths pass in staging and internal dogfood with the responsive shell flag on, with captured evidence of expected telemetry events/traces","Automated and manual accessibility checks (including keyboard navigation and screen reader smoke tests) show no new blockers; any issues have fixes merged or tracked with owners and target dates","Observability dashboards and alerts for responsive shell auth traffic are validated against the approved spec using live or replayed traces, with gaps triaged and resolved","Final hardening changes are merged with Identity and Frontend approvals, all regression gates are green, and outstanding findings are documented with explicit owners and follow-up tickets"]},{"title":"Enterprise Docs, Runbooks, and Support Enablement","description":"Translate the validated responsive shell behavior into public documentation, internal runbooks, and support assets that reflect the new auth experience and feature flag controls. Coordinate with Docs, Support, and SRE to ensure troubleshooting guidance, escalation paths, and instrumentation references are current.","acceptance_criteria":["Customer-facing knowledge base article and admin guide updates are merged with Docs and Support approvals, referencing responsive shell behavior and flag controls","SRE runbooks and on-call decision trees cover responsive shell-specific auth anomalies, required telemetry dashboards, and rollback procedures, with SRE sign-off","Support macros or troubleshooting playbooks are refreshed, reviewed by Tier 1/2 leads, and an enablement session (live or recorded) is delivered with attendance captured and notes shared","All documentation, runbooks, and enablement materials are linked in the release ticket with final copy edits complete and stakeholders acknowledging receipt"]},{"title":"Launch Readiness, Progressive Rollout, and Post-Launch Monitoring","description":"Drive the final go/no-go for the responsive shell by ensuring quality gates, flag configuration, rollout sequencing, and operational readiness are in place. Align with Product, Identity, Security, Release Engineering, and SRE on rollout execution, rollback triggers, and post-launch monitoring.","acceptance_criteria":["Release candidate commit has passing unit, integration, end-to-end, accessibility, and lint suites with evidence captured in the release ticket","Feature flag configuration for progressive rollout (cohorts, ramp percentages, timeline) and rollback plan (circuit breakers, clear owners) are documented and merged","Launch checklist is completed with explicit go/no-go approvals from Product, Identity, Security, SRE, Support, and Design (if required)","Post-launch monitoring dashboard and alert thresholds are validated in production-like traffic, with on-call ownership acknowledged for the launch window","Post-launch review cadence, success metrics, and communication plan (status updates, incident escalation channel) are scheduled and shared with stakeholders"]}]}
```
