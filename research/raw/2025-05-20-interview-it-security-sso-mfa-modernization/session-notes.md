---
title: Interview — IT Security on SSO/MFA Modernization Impact
date: 2025-05-20
type: interview
status: raw
tags:
  - security
  - sso
  - mfa
  - authentication
  - clinician-workflow
related_components:
  - sso-mfa-login
  - ambient-scribe-widget
related_findings:
  - ../../findings/scope-boundaries-and-workflow-fit.md
---

# Interview — IT Security on SSO/MFA Modernization Impact

## Objective
Understand planned SSO/MFA changes and their anticipated impact on clinical workflow before any AI feature is layered on top of authentication-dependent sessions.

## Method
- **Method:** 1:1 interview, 40 min
- **Researcher:** Priya Patel
- **Full participant roster:** see `participants.md` in this folder

## Key Findings
- **[HIGH]** *(session timeout)* Planned MFA rollout would introduce a shared-workstation re-authentication requirement every 15 minutes, down from the current 4 hours — flagged internally as likely to cause clinician pushback based on prior rollout feedback, independent of any AI feature.
- **[MEDIUM]** *(badge-tap workflow)* Most units already use badge-tap proximity login for shared workstations; new MFA plan hasn't yet been confirmed to work with the existing badge-tap hardware.
- **[MEDIUM]** *(AI session risk)* If an AI ambient scribe session is mid-recording when a forced re-auth occurs, current design has no defined behavior — could lose the in-progress draft.

## Representative Quotes
> "Security wants 15 minutes, clinical ops wants 4 hours, and nobody's told me yet who wins that argument, but I have to build for one of them."
> — IT Security Engineer, P31

> "Nobody's asked what happens to an active AI recording session if the screen locks mid-visit. That's going to be a real incident the first time it happens."
> — IT Security Engineer, P31

## Recommendations
1. Flag the ambient-scribe-mid-recording + forced-reauth interaction to the ambient scribe engineering team immediately as an unhandled edge case.
2. Push for a joint decision meeting between Security and Clinical Ops on the session timeout conflict before MFA rollout, independent of Compass AI.

## Follow-ups / Open Questions
- Confirm badge-tap hardware compatibility with new MFA plan.
- Get the ambient scribe team's answer on session-loss behavior into a future usability test script.

## Related
- Synthesized into: [scope-boundaries-and-workflow-fit.md](../../findings/scope-boundaries-and-workflow-fit.md)
