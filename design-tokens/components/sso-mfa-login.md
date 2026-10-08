---
title: SSO / MFA Login
component_id: sso-mfa-login
status: generated
generated_from: Figma (via sync_figma_tokens.py — not yet built; hand-authored here to match intended shape)
---

# SSO / MFA Login

**Figma node:** `N/A — platform/security component, not in Figma`

## Variants
- badge-tap
- manual-mfa

## States
- default
- session-timeout-warning

## Code mapping
`platform/auth/LoginFlow.tsx`

## Related Research Findings
- [Scope Boundaries And Workflow Fit](../../research/findings/scope-boundaries-and-workflow-fit.md)
- [Ambient Scribe](../../research/findings/ambient-scribe.md)

## Notes
Planned 15-minute re-auth timeout (vs. clinical ops' expectation of 4 hours) is unresolved as of the 2025-05-20 interview, as is the behavior of an in-progress ambient scribe recording session on forced re-auth. The 2026-02-17 contextual inquiry records IT Security confirming a 10-minute idle timeout that is not adjustable per-feature; how that idle timeout relates to the planned 15-minute re-auth isn't recorded. That session also studied the recording-on-lock behavior, and a paused, draft-preserved recovery flow is designed and in review (`user-flows/ambient-scribe-session-lock-recovery.md`).
