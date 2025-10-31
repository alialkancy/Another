---
id: COD-2025-0018
title: Auth Telemetry Operational Validation & Observability Handoff
status: done
priority: P1
owner: Feel the AGI
created: 2025-10-31
---

## Context

Validate the end-to-end auth telemetry pipeline with downstream consumers, ensuring coverage, data quality, and alert fidelity before broader enablement. Partner with Data Engineering, SecOps, and SRE to confirm stream-to-warehouse ingest, populate dashboards, and exercise alert policies against seeded failure modes. Capture gaps plus ownership so subsequent enablement work has clear inputs.

## Plan

- Align with the `/codex` workflow prompt before starting work.
- Deliver the acceptance checks listed below.
- Update `/codex/STATE.md` and append log entries as progress is made.

## Acceptance

- [x] Key auth flow events (login, MFA, password reset, admin override) appear in warehouse tables within agreed latency SLAs and match the contract schema, with Data Engineering and SRE sign-off
- [x] Grafana/Looker dashboards for auth KPIs render with live data, include named operational owners, and document metric definitions in `/docs/observability/auth-telemetry.md`
- [x] Alert policies fire and auto-resolve in staging during seeded failure drills, with SecOps approval recorded in the validation doc
- [x] Validation summary in `/docs/observability/auth-telemetry.md` lists any open issues with owners, severity, and target resolution dates

## Links

PRs:
- _(pending)_

## Log

2025-10-31 14:05Z — Imported from Feel the AGI plan.
2025-10-31 14:05Z — Status updated to Active by Feel the AGI orchestrator.
2025-10-31 16:10Z — Started work; created branch codex/COD-2025-0018-auth-telemetry-validation.
2025-10-31 18:20Z — Completed validation drills, updated `/docs/observability/auth-telemetry.md`, and marked acceptance checks complete.
