---
title: Contextual Inquiry — Session Lock During Active Ambient Scribe Dictation
date: 2026-02-17
type: contextual-inquiry
status: raw
tags:
  - ambient-scribe
  - sso
  - mfa
  - authentication
  - phi
related_components:
  - ambient-scribe-widget
  - encounter-view
related_findings:
  - ../../findings/ambient-scribe.md
  - ../../findings/governance-and-phi.md
  - ../../findings/ambient-scribe-post-ga-refinements.md
---

# Contextual Inquiry — Session Lock During Active Ambient Scribe Dictation

## Objective
`encounter-view.md`'s component notes flag the `locked` state's interaction with an in-progress
ambient scribe recording as an open edge case, raised as a side note in the 2025-05-20 SSO/MFA
interview but never directly studied. This session shadows clinicians through their normal
SSO/MFA idle-timeout window while actively dictating, to observe what actually happens today and
what they expect/want instead.

## Method
- **Method:** Contextual inquiry / shadowing, 5 clinicians observed through at least one natural
  idle-timeout event during a real or simulated dictation session, plus 1 IT Security stakeholder
  interviewed on the technical constraints
- **Researcher:** Priya Patel
- **Full participant roster:** see `participants.md` in this folder

## Key Findings
- **[CRITICAL]** *(silent draft loss)* In the current build, a session lock mid-recording simply
  freezes the ambient-scribe widget with no message; 4 of 5 clinicians assumed the draft was lost
  and started re-dictating from scratch after re-authenticating, even though the draft is
  server-side and actually survives the lock.
- **[HIGH]** *(no explicit paused state)* There is no visual distinction between "recording,"
  "frozen because locked," and "actually stopped" — participants could not tell which state they
  were in without asking a shadowing observer.
- **[MEDIUM]** *(re-auth friction stacks)* Clinicians already re-authenticate frequently for
  unrelated reasons (badge-tap SSO renewals); a lock during dictation is perceived as "one more
  annoying re-login," not as a distinct, expected safety behavior — this framing gap likely
  drives the abandon-and-redictate behavior above as much as the missing UI does.
- **[LOW]** *(IT Security confirms feasibility)* IT Security confirmed the 10-minute idle timeout
  is not adjustable per-feature, but confirmed an explicit "paused, draft preserved" UI state is
  technically straightforward to add without changing the timeout policy itself.

## Representative Quotes
> "I genuinely thought I'd lost it. I've just gotten used to starting over when the screen locks,
> so I didn't even try to check."
> — Physician, Family Medicine, P31

> "If it said 'paused, nothing lost, just log back in,' I'd believe it and wait. Right now it just
> looks broken."
> — Nurse Practitioner, P33

> "The timeout window itself is a hard policy constraint, but what the screen tells the clinician
> during that window is entirely a product decision — that part isn't locked down."
> — IT Security stakeholder

## Recommendations
1. Add an explicit "paused — draft preserved, re-authenticate to resume" state to the
   `encounter-view`/`ambient-scribe-widget` lock interaction, replacing the current silent freeze.
2. Do not attempt to change or extend the idle-timeout policy itself — per IT Security, treat it
   as fixed and solve this entirely at the UI-messaging layer.
3. Pair the new state with brief messaging that reframes the lock as an expected safety behavior
   rather than an unrelated login interruption, to counter the "one more annoying re-login"
   framing found here.

## Follow-ups / Open Questions
- Confirm with IT Security whether the same "paused, preserved" messaging pattern should extend
  to other session-timeout-adjacent surfaces beyond ambient scribe.
- Re-test the abandon-and-redictate behavior once the explicit paused state ships, to confirm it
  actually changes clinician behavior and not just their stated understanding.

## Related
- Synthesized into: [ambient-scribe-post-ga-refinements.md](../../findings/ambient-scribe-post-ga-refinements.md)
