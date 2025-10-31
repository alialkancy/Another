# Login Experience Architecture Brief

Prepared: 2025-10-31  
Author: Feel the AGI Implementation Team

## 1. Scope & Goals

Replace the static `home.html` login form with a modular React-based experience that can be gradually enabled via feature flags, integrates with Auth Platform API v3, and provides robust telemetry, accessibility, and localization support.

## 2. UI Composition & Routing

- Entry route: `GET /login`. Server performs flag check:
  - `login_shell.enabled == false` → serve legacy static HTML (current `home.html`).
  - `login_shell.enabled == true` → serve SPA bundle (`login-shell.js`) bootstrapping React tree.
- Layout:
  - `LoginPage` (top-level) renders `GlobalHeader`, `LoginCard`, and optional `PromoPanel`.
  - `LoginCard` subdivides into `CredentialForm`, `SsoOptions`, `PasswordResetLink`, `LockoutNotice`, and `FooterLinks`.
  - Shared UI components sourced from Design System (`@org/design-system`) for buttons, inputs, banners, loading spinner.
- Responsive breakpoints: `<=600px` (single column), `601-1024px` (card centered with optional illustration), `>1024px` (two-column layout with marketing pane).
- Localization: leverage `react-intl` wrapper; all textual content uses message IDs.

## 3. State Management

- Use `React Query` for async mutations and caching (`useMutation` for `createSession`).
- UI state slices:
  - `formState`: fields, validation errors, submission status (idle|submitting|success|error).
  - `authState`: lockout status, MFA requirements (future), last attempted username.
  - `featureFlags`: sourced from LaunchDarkly SDK with SSR-provided bootstrap payload.
- Context providers: `AuthTelemetryProvider`, `FeatureFlagProvider`, `LocalizationProvider`.
- Client-side validation implemented via shared `validators` package to maintain parity with signup page rules.

## 4. Service/API Interactions

- Primary API: `POST /api/auth/v3/sessions`
  - Request: `{ username, password, client_id, context: { locale, device, captchaToken? } }`
  - Response (200): `{ sessionId, redirectUrl?, mfaRequired?, userProfile { userId, name } }`
  - Response (4xx/5xx): standard error schema `{ error: { code, message, detail?, retryAfter? } }`
- Lockout check: `GET /api/auth/v3/users/{username}/lockout` prior to enabling submit button after 3 failures.
- CSRF token fetched from `GET /api/auth/v1/csrf` and cached.
- Captcha service (v3) invoked after 2 consecutive failures when flag `login_shell.enforce_captcha` enabled.

## 5. Data Contracts

- Frontend consumes `AuthSession` model defined in `/contracts/auth-session.json`.
- Telemetry payload contract maintained in `/analytics/contracts/login.json`.
- Form validation errors align with `AuthErrorCode` enum (`INVALID_CREDENTIALS`, `LOCKED_OUT`, `ACCOUNT_DISABLED`, `MFA_REQUIRED`, `RATE_LIMITED`, `SERVER_ERROR`).

## 6. Error Handling Strategy

- Categorize errors into `userError`, `securityBlock`, `systemError` for UI messaging.
- Show `LockoutNotice` when error code == `LOCKED_OUT`; disable submit and direct to support.
- Network failures trigger retry banner with `Retry` CTA using exponential backoff.
- Unknown errors default to generic localized copy, with error ID surfaced for support.
- All errors logged to Sentry with sanitized context and correlation ID from backend.

## 7. Feature Flag Strategy

- Flags managed via LaunchDarkly:
  - `login_shell.enabled` (Boolean): master switch for new experience.
  - `login_shell.enable_sso` (Boolean): toggles SSO providers.
  - `login_shell.enforce_captcha` (Boolean): enforces captcha after threshold.
  - `login_shell.experiment_bucket` (String): cohort assignment for analytics.
- Server provides initial flag values in HTML payload; client rehydrates via LD SDK.
- Fallback behavior: if flags fail to load within 2s, default to disabled state and hard refresh to legacy HTML if critical config missing.

## 8. Telemetry & Observability

- Instrumented via `authTelemetryClient` (Segment) and Sentry:
  - Each event includes `correlationId` from backend response headers.
  - Attach performance marks (`login_shell_loaded`, `login_submit_start`, `login_response_received`) for Web Vitals correlation.
- Logging:
  - Client logs suppressed unless `debug` flag toggled; errors escalate to Sentry with severity mapping.
- Monitoring dashboards: build Looker board combining telemetry events and backend response metrics.

## 9. Rollback & Kill Switch

- Rollback by disabling `login_shell.enabled`; legacy HTML served immediately.
- Bundles remain deployable but inert when flag disabled.
- If client bundle fails hard (runtime error on mount), fallback script replaces SPA root with legacy HTML fetched from `/static/login-legacy.html`.
- Maintain canary environment; flag rollout phases: internal → staging → 5% prod → 50% → 100%.

## 10. Compliance & Privacy Considerations

- PII handling: only hashed usernames stored client-side for telemetry; session token handled via secure, httpOnly cookie (set by backend).
- GDPR/CCPA: ensure consent banner intercept does not block login; analytics respects user opt-outs.
- Audit logging: success/failure events forwarded to compliance data lake with 30-day retention.
- Accessibility documentation retained for VPAT refresh.

## 11. Testing Strategy Overview

- Unit tests: validation utils, flag-driven UI gating.
- Integration tests: session creation, error flows with mocked API.
- E2E tests: run in Playwright across desktop/mobile viewports; include flag toggles.
- Load testing: k6 scenario hitting `/api/auth/v3/sessions` with 95th percentile latency target < 350 ms under 200 RPS.

## 12. Dependencies & Owners

- Auth Platform API v3 — Owner: Lin Chen — Available in staging 2025-11-07.
- LaunchDarkly flag config — Owner: Feature Ops (Rina Sato) — Created 2025-10-30.
- Design tokens update (focus styles) — Owner: Priya Natarajan — Delivery due 2025-11-03.
- Telemetry schema approval — Owner: Dana Wright — Due 2025-11-05.
- Compliance review — Owner: Marlon Estevez — Due 2025-11-08.

