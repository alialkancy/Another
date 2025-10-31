# Baseline Login Requirements

## Overview

Discovery completed on 2025-10-31 with product, design, security, auth-platform, and analytics stakeholders to define the scope for the new login experience that will ship behind a feature flag and replace `home.html` when fully launched. The requirements below supersede the existing static login markup and establish the guardrails for subsequent implementation tickets.

## Stakeholder Sign-off (2025-10-31)

- Product — Jamie Park (PM) ✅
- Design — Priya Natarajan (Principal Product Designer) ✅
- Security — Marlon Estevez (AppSec Lead) ✅
- Auth Platform — Lin Chen (Identity Platform Staff Engineer) ✅
- Analytics — Dana Wright (Product Analytics Manager) ✅

## Functional Requirements

- `GET /login` renders a responsive React shell (per forthcoming architecture brief) when the `login_shell.enabled` flag is **true**; otherwise the legacy `home.html` stays in place.
- Primary authentication methods: username + password, with hooks to inject SSO providers (SAML, OIDC) and “magic link” CTA when enabled via flag overrides.
- Required UI states: initial form, field-level validation errors, global error banner, account lockout notice, password reset prompt, loading indicators, and success redirect (default to `/dashboard` or `return_to` query param).
- Accessibility: semantic region landmarks (`<main>`, `<header>`, `<form role="form">`), visible focus outlines, error messages programmatically associated via `aria-describedby`, and form keyboard navigation that matches WCAG 2.2 AA.
- Localization: support for 16 target locales at launch with runtime locale detection, leveraging existing `i18n` bundle loader; copy keys defined under `auth.login.*`.
- Performance: Largest Contentful Paint < 2.5s on mid-tier mobile over 4G, with bundle size cap of 180 KB gzipped for the login shell (excluding shared design system chunks).
- Security: enforce HTTPS, HSTS preloading, CSRF token injection from platform, secure autocomplete attributes (`username`, `current-password`), prevent password managers from autofilling hidden fields, and redact sensitive strings from telemetry logs.
- Remember-me option deferred; track via new ticket if prioritized later.

## Accessibility & QA Validation

- Conduct pre-merge axe-core automated scans and manual screen reader smoke tests (NVDA + VoiceOver).
- Ensure error messaging meets contrast requirements and includes actionable guidance.
- Keyboard focus trapped within modal flows (e.g., SSO popover) but not in base login form.

## Analytics & Telemetry Expectations

- Emit structured events via `authTelemetryClient`:
  - `auth.login.view` (when shell mounts) with context: locale, flag state, experiment ID.
  - `auth.login.submit` (attempt) with method (`password`, `sso::provider`), device class.
  - `auth.login.success` and `auth.login.failure` including error category (`invalid_credentials`, `lockout`, `network`, `unknown`).
  - `auth.login.lockout_shown` when lockout UI is displayed.
- Events must include `anonymousId` and respect Do-Not-Track. Security approved the inclusion of hashed usernames (SHA-256 + per-env salt) for correlation.
- All telemetry routes through the existing Segment pipeline with sampling disabled for login events.

## Localization & Content Governance

- Copy strings reside in `packages/web/i18n/auth/login.json` with fallbacks to English.
- RTL locales must flip layout via CSS logical properties; design will supply mirrored icon assets.
- Content updates require review by Product Marketing and Legal when strings describe account status or regulatory obligations.

## Dependencies & Integrations

- Requires Auth Platform API v3 `/sessions` endpoint with contract finalized (see architecture brief).
- Feature flag served via LaunchDarkly (`login_shell.enabled`, `login_shell.force_ssn`, etc.).
- Password reset CTA links into existing `/forgot-password` flow; ensure redirect parameters align with security guidance.

## Performance & Reliability Guardrails

- Use Suspense boundary with placeholder skeleton to avoid layout shift.
- Client-side rate limit: max 5 attempts per 15 minutes per device before lockout banner.
- Ensure error retry backoff (exponential with jitter) for recoverable network issues.

## Open Questions

- Awaiting legal confirmation on whether biometric login CTA can be shown globally or must be gated by region (owner: Jamie Park, due 2025-11-04).
- Need analytics alignment on experiment bucketing keys for login funnel A/B tests (owner: Dana Wright, due 2025-11-06).

