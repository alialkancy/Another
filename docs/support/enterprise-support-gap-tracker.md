# Enterprise Support Gap Tracker

_Last updated: 2025-10-31 15:20Z_

| Gap ID | Description | Related Requirements | Risk Level | Owner | Mitigation Plan | Target Date | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| GAP-01 | Slack escalation app signing secret rotates manually; automation cannot enforce 30-day policy. | BP-REQ-002 | High | SRE (Priya Desai) | Automate secret rotation via Secrets Manager job; add validation hook in CI. | 2025-11-07 | In Progress |
| GAP-02 | Zendesk macro `ENT-TRIAGE-01` lacks audit trail for field overrides. | BP-ES-001, BP-REQ-001 | Medium | Support Ops (Alex Rivera) | Enable macro change logging; export weekly diff to Compliance archive. | 2025-11-14 | Planned |
| GAP-03 | ServiceNow playbook `SN-PB-401` version drift vs. documented workflow. | BP-ES-002 | High | Programme Office (Morgan Lee) | Freeze current playbook version; align change control with Support Ops governance. | 2025-11-05 | In Progress |
| GAP-04 | Data residency controls for support attachments not enforced in legacy S3 bucket. | BP-ES-003, BP-REQ-005 | High | Security (Jordan Kim) | Migrate attachments to region-locked bucket; update IAM policies and retention scripts. | 2025-11-21 | Planned |
| GAP-05 | Observability dashboard `SUP-ENT-01` missing MTBF visualization and severity drill-down. | BP-ES-002, BP-REQ-004 | Medium | SRE (Telemetry Guild) | Extend dashboard modules; backfill historic incidents for trendline continuity. | 2025-11-18 | Planned |
| GAP-06 | Compliance Splunk index `cmp-support-pd` ingest pipeline lacks automated failure alerts. | BP-REQ-004, BP-REQ-005 | Medium | Compliance (Jamie Chen) | Add heartbeat alert and PagerDuty route `compliance-alerts`; document in runbook appendix. | 2025-11-12 | In Progress |

## Prioritization Notes

- High-risk gaps (GAP-01, GAP-03, GAP-04) require closure before runbook enablement freeze on 2025-11-22.
- Medium-risk items are scheduled but monitored weekly; escalate to Programme Director if timelines slip by >3 days.

## Tracking Cadence

- Reviewed during joint Support Ops/SRE stand-up every Tuesday.
- Formal status export shared with Compliance and Programme Director each Friday via Confluence report `ENT-SUPPORT-GAPS`.
