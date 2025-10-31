# Login Observability Implementation Plan

Version: 1.0.0  
Published: 2025-10-31 16:30Z  
Author: Feel the AGI Implementation Team

## Executive Summary

Codifies the execution path for delivering the approved login observability blueprint. Aligns the platform SRE, security, data platform, and support workstreams so telemetry, access, and escalation capabilities land ahead of the enterprise launch window scheduled for the week of 2025-11-18.

## Cross-Team Review Sign-off

| Discipline | Representative | Review Date | Outcome | Notes |
| --- | --- | --- | --- | --- |
| Platform SRE | Quinn Harper | 2025-10-31 | ✅ Approved | Sequencing updated to unblock Redis cluster cutover. |
| Security | Marlon Estevez | 2025-10-31 | ✅ Approved | Privacy guardrails align with hashed username policy. |
| Data Platform | Dana Wright | 2025-10-31 | ✅ Approved | Segment schema gates and retention confirmed. |
| Support | Jordan Lee | 2025-10-31 | ✅ Approved | Support runbook updates tracked for Training Sprint 2025-11-12. |

## Alignment Highlights

- **Data flows:** Shell emits events via Segment > Kafka > Snowflake with Prometheus counters and OTEL traces from the gateway. Normalized schemas derived from `login-observability-spec.md`.
- **Emission formats:** JSON payloads adhere to `auth.login.*` schema v2; OpenTelemetry spans export via OTLP/gRPC; metrics remain Prometheus-exposition. Sampling policies match blueprint.
- **Retention & access:** Metrics 13 months, logs 30/400 days, traces 7/14 days; RBAC groups `Auth-Platform-Viewer`, `Security-OnCall`, and new `Support-Observers` scope provisioned per IAM plan (§Dependency Matrix).
- **Escalation paths:** PagerDuty services `Auth Platform Primary`, `SRE Edge`, `Security On-Call`, with Slack channels `#auth-incidents`, `#feature-flags`, `#login-support`. First-responder rotation documented in support enablement plan (pending ticket COD-2025-0015).

## Sequencing Plan (Aligned to Release Calendar)

| Milestone | Owner | Window | Dependencies | Deliverables |
| --- | --- | --- | --- | --- |
| Instrumentation freeze | Lin Chen (Auth Platform) | 2025-11-04 | Auth API v3 GA, OTEL exporters merged | Gateway metrics + traces behind `login_shell.observability` flag. |
| Client telemetry QA | Alex Gomez (Frontend) | 2025-11-05 | Localization bundle refresh, Segment schema approval | Event validation scripts, redaction checks, CI verification job. |
| IAM & access provisioning | Priya Natarajan (IAM) | 2025-11-06 | Support role matrix, Security SCIM sync | Service accounts, RBAC groups, audit of data lake entitlements. |
| Dashboard/alert shakedown | Quinn Harper (SRE) | 2025-11-08 | Redis cluster go-live, LaunchDarkly webhooks | Grafana dashboards, alert tuning, synthetic traffic burn-in. |
| Support runbook updates | Jordan Lee (Support) | 2025-11-12 | Dashboard shakedown, Incident tooling integrations | Updated runbooks, escalation tree, help-center macros. |
| Cross-functional validation checkpoint | Feel the AGI Program | 2025-11-13 | Previous milestones | Sign-off meeting notes, risk review, go/no-go gate inputs. |
| Launch readiness dry run | Feel the AGI + Release Mgmt | 2025-11-15 | Chaos & DR rehearsal scheduled | PagerDuty simulation, rollback drill, final data export QA. |
| Enterprise launch window | Release Mgmt | Week of 2025-11-18 | All acceptance checks closed | Feature flag ramp, observability war room staffed. |

## Execution Streams

1. **Telemetry Delivery:** Complete instrumentation, schema validation, and data pipeline monitoring. Includes staging and production sampling configuration updates.
2. **Access Controls:** Provision new IAM groups, audit shared service accounts, and file break-glass access procedures with Security.
3. **Incident Readiness:** Wire LaunchDarkly hooks, PagerDuty services, Slack channels, and document escalation trees. Integrate with existing incident postmortem tooling.
4. **Documentation & Enablement:** Refresh runbooks, knowledge base, and onboarding decks. Confirm support training attendance and comprehension captured in ticket COD-2025-0015.
5. **Validation & Go-Live:** Execute synthetic and manual checks, run go/no-go meeting, and schedule launch day command-center coverage.

## Dependency Matrix

| Dependency | Scope | Owner | Landing Date | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| `login_shell.observability` flag | LaunchDarkly feature flag to gate new telemetry | Rina Sato (Feature Ops) | 2025-11-03 | In progress | Requires incident webhook (#auth-incidents) to auto-subscribe. |
| OTEL collector service account | `svc-auth-otel` with least-privilege access to telemetry sinks | Priya Natarajan (IAM) | 2025-11-06 | Not started | IAM policy draft reviewed by Security. |
| Support read-only dashboards | RBAC scope `Support-Observers` + Grafana team mapping | Jordan Lee (Support) | 2025-11-07 | Pending | Requires IAM group creation and SSO assertion update. |
| PagerDuty integrations | Auth Platform, SRE Edge, Security On-Call services linked to LaunchDarkly + Grafana | Quinn Harper (SRE) | 2025-11-08 | Pending | Use service hooks defined in incident playbook v2. |
| Segment schema promotion | `auth.login.*` events promoted to prod dataset with retention policy | Dana Wright (Data Platform) | 2025-11-05 | Pending | DQ checks block enabling prod flag. |
| Snowflake role `ROLE_AUTH_TELEMETRY_RW` | Enables controlled data platform writes from ETL | Abhi Patel (Data Platform) | 2025-11-06 | Not started | Must pass security review for masked columns. |
| Elastic ingest pipeline | Update ingest pipeline `auth-login-v2` with hash validation | Marlon Estevez (Security) | 2025-11-07 | In progress | Adds automated PII detection alert. |
| Synthetic monitor credentials | Vault-issued service account `svc-login-synthetic` | Quinn Harper (SRE) | 2025-11-08 | Pending | Used by synthetic login tests pre/post launch. |

## Coordination & Communication

- Weekly observability sync (Tuesdays 16:00Z) co-led by Quinn Harper and Feel the AGI; minutes stored in `/docs/login/meeting-notes/` (to be created next sprint).
- Daily launch war room starting 2025-11-18 with rotating SRE/Security/Support leads.
- Status updates posted to `#project-login` Slack channel with focus on dependency matrix burndown and risk register changes.

## Next Actions

1. Track dependency matrix progress in `/docs/login/dependencies-risk-register.md`.
2. Ensure risks and handoffs remain current ahead of validation checkpoint.
3. Transition implementation ownership to COD-2025-0014 once instrumentation tasks move to execution.

