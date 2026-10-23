---
title: Shared-workstation re-authentication, 15 minutes or 4 hours
date: 2026-10-23
status: draft
decision_status: not-decided
decision_status_source:
  - research/raw/2025-05-20-interview-it-security-sso-mfa-modernization/session-notes.md:35-36
  - research/findings/scope-boundaries-and-workflow-fit.md:64-68
  - design-tokens/components/sso-mfa-login.md:28
date_decided: not recorded
decided_by: not recorded
superseded_by: ""
evidence:
  - source: research/raw/2025-05-20-interview-it-security-sso-mfa-modernization/session-notes.md
    lines: "30,32,35-36,43"
  - source: research/raw/2026-02-17-session-lock-during-dictation/session-notes.md
    lines: "49-51"
  - source: research/findings/scope-boundaries-and-workflow-fit.md
    lines: "59-68"
tags:
  - sso
  - mfa
  - authentication
  - security
  - clinician-workflow
  - project-cross-cutting
related_findings:
  - scope-boundaries-and-workflow-fit.md
related_components:
  - sso-mfa-login
---

# Shared-workstation re-authentication, 15 minutes or 4 hours

## Decision
not recorded. No record states a decision. The question on record is whether shared
workstations require re-authentication every 15 minutes, as a planned MFA rollout would
introduce, or keep the current 4 hours
(`research/raw/2025-05-20-interview-it-security-sso-mfa-modernization/session-notes.md:30`).

Decision status: not decided. The IT Security engineer, P31, said: "Security wants 15 minutes,
clinical ops wants 4 hours, and nobody's told me yet who wins that argument, but I have to build
for one of them" (same file, `:35-36`). The finding calls the 15-minute figure a planned policy
still disputed as of May 2025 (`research/findings/scope-boundaries-and-workflow-fit.md:64-65`), and
the `sso-mfa-login` component notes call it unresolved as of that interview
(`design-tokens/components/sso-mfa-login.md:28`).

## Alternatives considered
- Re-authenticate every 15 minutes: the position the raw note attributes to Security
  (`research/raw/2025-05-20-interview-it-security-sso-mfa-modernization/session-notes.md:35`).
  It was flagged internally as likely to cause clinician pushback (same file, `:30`).
- Keep 4 hours: the position the raw note attributes to clinical ops (same file, `:35`).

Neither is recorded as chosen.

## Rationale
**Evidence basis:** Mixed. The dispute, the two positions and the open edge case are Observed in
the cited raw lines. That no decision was made later is Inferred: no later record states one.

not recorded, because no decision is recorded. What the corpus holds is context:
- If an ambient scribe session is mid-recording when a forced re-authentication happens, the
  design had no defined behavior and could lose the draft
  (`research/raw/2025-05-20-interview-it-security-sso-mfa-modernization/session-notes.md:32`).
- By February 2026, IT Security confirmed a 10-minute idle timeout that is not adjustable per
  feature (`research/raw/2026-02-17-session-lock-during-dictation/session-notes.md:49-51`). The raw
  notes don't say whether that settles this dispute or is a separate idle-lock setting
  (`research/findings/scope-boundaries-and-workflow-fit.md:65-68`).

## Conditions to revisit
not recorded. The session recommended a joint decision meeting between Security and Clinical Ops
on the timeout conflict before MFA rollout
(`research/raw/2025-05-20-interview-it-security-sso-mfa-modernization/session-notes.md:43`).
Whether it happened is not recorded.

## Not recorded
- The decision: not recorded.
- Who decided: not recorded.
- When it was decided: not recorded.
- Whether the recommended Security and Clinical Ops meeting happened: not recorded.
- Whether the 10-minute idle timeout is the same setting as the 15-minute re-authentication:
  not recorded.
