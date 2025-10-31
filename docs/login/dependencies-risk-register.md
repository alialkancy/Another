# Login Experience Dependency & Risk Register

_Last updated: 2025-10-31_

## 1. Dependency Tracker

| Item | Description | Owner | Target Date | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| Auth API v3 availability | `/api/auth/v3/sessions` endpoint promoted to staging/prod | Lin Chen (Auth Platform) | 2025-11-07 | On track | Contract signed off; load testing queued. |
| LaunchDarkly flag setup | `login_shell.*` flags created and seeded | Rina Sato (Feature Ops) | 2025-10-30 | Complete | Need SDK key rotation doc before prod. |
| Flag incident webhooks | Configure LaunchDarkly hooks to `#auth-incidents` and PagerDuty | Rina Sato (Feature Ops) | 2025-11-02 | In progress | Required for observability alerting policy. |
| Design system tokens | Updated focus ring + spacing tokens | Priya Natarajan (Design) | 2025-11-03 | At risk | Dependent on design QA bandwidth. |
| i18n bundle refresh | Add `auth.login` namespace to translation pipeline | Leo Martin (Localization) | 2025-11-06 | On track | Vendor delivery expected 2025-11-05. |
| Telemetry schema approval | Segment schema for login events | Dana Wright (Analytics) | 2025-11-05 | Pending review | Security signed off on hashed username field. |
| Compliance review | Privacy & regulatory assessment | Marlon Estevez (Security) | 2025-11-08 | Not started | Needs data flow doc (captured in architecture brief). |
| CAPTCHA service integration | Toggleable captcha for high-risk flows | Evelyn Soto (Security Engineering) | 2025-11-09 | Blocked | Vendor SLA change pending legal review. |
| IdP metadata rotation | Refresh OIDC/SAML metadata with new MTLS certs | Lin Chen (Identity Platform) | 2025-11-04 | On track | Certs issued 2025-10-28; waiting on staging deploy. |
| Session Redis cluster | Provision Redis 7.2 w/ TLS for session caching | Quinn Harper (SRE) | 2025-11-03 | In progress | Terraform plan ready; awaiting change window approval. |
| Gateway migration | Apply DB migration `20251031_add_session_audit` | Maya Ortiz (Platform) | 2025-11-05 | Not started | Requires 30 min maintenance window. |

## 2. Risk Register

| ID | Risk | Impact | Likelihood | Owner | Mitigation | Trigger |
| --- | --- | --- | --- | --- | --- | --- |
| R1 | Auth API latency spikes during rollout | High | Medium | Lin Chen | Run pre-prod load test, configure autoscaling alerts, stage rollout with canary users | P95 latency > 250 ms for 5 min |
| R2 | Localization bundle delay causing untranslated strings | Medium | Medium | Leo Martin | Provide English fallback copy, add QA check in build pipeline | Vendor delivery slips past 2025-11-06 |
| R3 | CAPTCHA vendor contract unsigned | High | Medium | Evelyn Soto | Engage legal escalation, build soft dependency path that hides captcha CTA until ready | Legal review not signed by 2025-11-05 |
| R4 | Telemetry event schema rejected by data governance | Medium | Low | Dana Wright | Present hashed username privacy analysis, align on retention policy | Governance meeting notes request revisions |
| R5 | Accessibility regression from new focus styles | Medium | Medium | Priya Natarajan | Pair QA + design for focus testing, add automated axe checks to CI | axe scan reports contrast/focus failure |
| R6 | Rollback fails because legacy HTML diverges | High | Low | Feel the AGI team | Nightly job to sync `home.html` snapshot to `/static/login-legacy.html`, manual verification checklist | Legacy snapshot older than 7 days |
| R7 | Redis cluster deployment delayed impacting session TTL guarantees | High | Medium | Quinn Harper | Schedule change window with SRE, prepare fallback to SQL session store, add smoke test post-launch | Change approval slips past 2025-11-04 |
| R8 | IdP metadata rotation misses MTLS certificate cutover | High | Low | Lin Chen | Stage rotation by 2025-11-03, validate handshake in staging, fallback to legacy certificate for 24 hrs | MTLS cert expires 2025-11-05 without update |

## 3. Compliance & Privacy Items

- Data minimization: confirm hashed username salting approach documented for auditors (Owner: Marlon Estevez, Due: 2025-11-04).
- Audit retention: ensure login events forwarded to compliance warehouse with 30-day TTL (Owner: Dana Wright, Due: 2025-11-10).
- Regional policy: Determine if biometric CTA allowed in EU; consult Legal (Owner: Jamie Park, Due: 2025-11-04).
- Consent management: verify login telemetry honors opt-out flag from consent service (Owner: Lin Chen, Due: 2025-11-06).

## 4. Open Questions

1. Do we require explicit customer notification for the UI overhaul in regulated markets? (Owner: Support PM, Due: 2025-11-07)
2. Should the login shell expose recovery code entry for MFA on day one or defer to follow-up ticket? (Owner: Product/Security, Due: 2025-11-05)
3. Are there legacy clients relying on query params only present in `home.html` that must be preserved? (Owner: Auth Platform, Discovery by 2025-11-03)
