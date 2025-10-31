# Login Observability Specification

Version: 1.0.0  
Last Updated: 2025-10-31 13:44Z  
Document Owner: Feel the AGI Implementation Team

## Revision History

| Version | Date | Author | Notes |
| --- | --- | --- | --- |
| 1.0.0 | 2025-10-31 | Feel the AGI | Initial observability baseline for login shell rollout. |

## Stakeholders & Approvals

| Role | Name | Team | Approval Date |
| --- | --- | --- | --- |
| Data Platform Lead | Dana Wright | Data Platform | 2025-10-31 |
| Observability Lead | Quinn Harper | SRE / Observability | 2025-10-31 |

## 1. Objectives

Provide end-to-end visibility into login flow health across the responsive shell, Auth Gateway, and IdP. Observability must enable rapid detection of auth failures, rate limits, latency regressions, and flag misconfigurations while aligning with privacy and retention policies.

## 2. Metrics

| Metric ID | Description | Source | Dimensions | Target / Threshold | Owner |
| --- | --- | --- | --- | --- | --- |
| `auth.login.attempts` | Count of login submissions | Shell → Segment → Metrics pipeline | `env`, `device`, `flag_state`, `correlationId` | Watch for spikes > 3σ | Product Analytics |
| `auth.login.success_rate` | Successful attempts / total | Auth Gateway Counter | `env`, `idp_cluster`, `flag_state` | Alert if < 98% over 5 min | Auth Platform |
| `auth.login.error_rate` | Errors by category | Gateway | `error_code`, `env`, `flag_state` | Alert if `SERVER_ERROR` > 2% over 5 min | SRE |
| `auth.login.latency.p95` | P95 latency per env | Gateway (Prometheus histogram) | `env`, `idp_cluster` | Alert if > 350ms for 5 min | Auth Platform |
| `auth.login.retry_count` | Client retry attempts | Shell telemetry | `env`, `error_type` | Alert if retries > 0.5 per attempt | Frontend Lead |
| `auth.login.rate_limited` | Count of 429 responses | Gateway | `env`, `origin_ip_range` | Alert if > 100/min in prod | Security Eng |
| `auth.login.flag_override` | Flag toggles & overrides | LaunchDarkly webhook → Metrics | `flag_key`, `actor`, `env` | Notify on off-hours toggles | Feature Ops |
| `auth.login.session_ttl` | Observed session lifetime | Gateway | `env` | Alert if < 20 min average | Auth Platform |

## 3. Logs

- **Structured Log Schema (`auth-gateway`):**
  - `timestamp`, `level`, `service`, `correlationId`, `requestId`, `userHash`, `flagState`, `result` (`success`, `error`, `rate_limited`), `errorCode`, `latencyMs`.
  - PII: only hashed username (`userHash`) and anonymized IP (/24) stored.
- **Shell Console Logs (only in debug mode):** disabled in production; errors forwarded to Sentry with scrubbed payload.
- **Retention:** 30 days hot in Elastic, 400 days warm archive (security requirement).
- **Access:** restricted to `Auth-Platform-Viewer` or higher RBAC; SRE handles audit logging.

## 4. Traces

- **Tracing Tool:** OpenTelemetry with Jaeger backend (prod) and Grafana Tempo (staging).
- **Span Topology:**
  - `shell.login.submit` (client) — includes attributes `flag_state`, `device`, `locale`.
  - `gateway.session.create` (server) — child span, exports `http.status_code`, `idp_cluster`, `retry_count`.
  - `idp.authenticate` (external) — recorded via gateway instrumentation; redacts credentials.
- **Correlation:** Use shared `correlationId` propagated via headers (`x-correlation-id`).
- **Sampling:** 100% in staging; 10% tail-based sampling in prod with bias towards error spans.
- **Trace Retention:** 7 days prod, 14 days staging.

## 5. Dashboards

| Dashboard | Location | Description | Owner | SLA |
| --- | --- | --- | --- | --- |
| `Login Overview` | Grafana folder `Auth/Login` | Aggregated success/error/latency metrics, feature flag overlay | Auth Platform | Update within 1 hr of schema changes |
| `Login Reliability` | Grafana `SRE Ops` | Rate limit, retry, IdP health, circuit breaker status | SRE | 24/7 availability |
| `Login Experiment` | Looker `Growth` | Segmented conversion by experiment cohort | Product Analytics | Business hours |
| `Flag Toggle Audit` | LaunchDarkly Insights | Historical flag changes with actor/context | Feature Ops | On change |

## 6. Alerts & Thresholds

| Alert | Condition | Channel | Runbook | Owner |
| --- | --- | --- | --- | --- |
| `Login Success Drop` | `auth.login.success_rate < 98%` for 5 min | PagerDuty: Auth Platform Primary | `runbooks/login-auth.md` | Auth Platform |
| `Latency Regression` | `auth.login.latency.p95 > 350ms` for 5 min | PagerDuty: SRE Edge | `runbooks/login-perf.md` | SRE |
| `IdP Degradation` | `IDP_UNAVAILABLE` errors > 20/min | Slack `#auth-incidents` | `runbooks/idp-fallback.md` | Identity Platform |
| `Rate Limit Surge` | `auth.login.rate_limited > 100/min` for 10 min | PagerDuty: Security On-Call | `runbooks/security-rate-limit.md` | Security Eng |
| `Flag Override After Hours` | Flag change between 02:00–06:00 local | Slack `#feature-flags` | `runbooks/flag-audit.md` | Feature Ops |

Alerts integrate with centralized incident tracking; each includes escalation policy to secondary on-call within 10 minutes.

## 7. Sampling & Data Retention

- Metrics retained 13 months (prod) and 6 months (non-prod).
- Traces per §4 retention.
- Logs per §3 retention.
- Telemetry events in Segment retained 25 months; hashed usernames rotated quarterly.
- Sampling guardrails: never sample out security-critical events (`auth.login.failure`, `auth.login.rate_limited`).

## 8. Ownership & Responsibilities

| Area | Primary Owner | Backup Owner | Notes |
| --- | --- | --- | --- |
| Metrics pipeline | Dana Wright | Abhi Patel | Ensure schema changes reviewed within 2 business days. |
| Gateway instrumentation | Lin Chen | Maya Ortiz | Maintain OTEL exporters. |
| Frontend telemetry | Alex Gomez | Priya Natarajan | Validate client event payloads and privacy filters. |
| Dashboards & alerts | Quinn Harper | Isla Reed | Keep Grafana/Looker assets current; audit quarterly. |

## 9. Compliance & Privacy Alignment

- Event schemas reviewed with Security (Marlon Estevez) and Privacy (Maya Ortiz) — no raw credentials stored.
- Data residency: EU telemetry forwarded to EU data plane; dashboards filtered accordingly.
- Sentry error scrubbing rules updated to redact username, IP, sessionId.
- Consent: front-end suppresses non-essential telemetry when consent flag false.

## 10. Implementation Checklist

- [x] Metrics defined and registered in Prometheus + Segment catalog.
- [x] Tracing instrumentation code path identified (backend, frontend).
- [x] Alert rules configured in Grafana OnCall.
- [ ] Synthetic login monitor to be activated post-implementation (tracked under COD-2025-0008).
