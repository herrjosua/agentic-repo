---
title: Scope Boundaries & Workflow Fit
date: 2025-10-07
type: synthesis
status: synthesized
tags:
  - 42-cfr-part-2
  - authentication
  - baseline
  - behavioral-health
  - clinician-workflow
  - ed
  - high-acuity
  - intake
  - mfa
  - phi
  - security
  - sensitive-notes
  - sso
  - workflow
related_components:
  - ambient-scribe-widget
  - ed-intake-form
  - sso-mfa-login
related_findings:
  - governance-and-phi.md
---

# Scope Boundaries & Workflow Fit

## Overview
Three sessions across the year are grouped here because their common output was a "don't build
this yet, or don't build it here" conclusion — which the December executive retro specifically
praised as valuable in its own right.

- **ED intake (contextual inquiry, Apr 2025):** peak-hour interruption frequency (every 2-4 minutes)
  makes any AI tool requiring sustained review attention a poor fit for ED intake nurses
  specifically during peak windows. The one positive signal — insurance-card-photo pre-fill for
  registration clerks — was carved out as a smaller, separate, lower-risk candidate instead.
- **SSO/MFA modernization (interview, May 2025):** independent of any AI feature, a planned
  15-minute forced re-authentication conflicts with clinical ops' expectation of a 4-hour session —
  and nobody had yet defined what happens to an in-progress ambient scribe recording session if a
  forced re-auth interrupts it mid-visit. This was flagged as an unhandled edge case for the
  ambient scribe team (see [ambient-scribe.md](ambient-scribe.md)) rather than something to solve
  in this session.
- **Behavioral health (contextual inquiry, Oct 2025):** reiterated, independently, the same "no
  structured way to flag a 42 CFR Part 2-protected note" platform gap first identified in the July
  HIM research (see [him-coding-and-billing.md](him-coding-and-billing.md)) — and added a harder
  constraint on top: any AI tool listening to or drafting behavioral health notes needs a dedicated
  legal/consent review that hasn't started yet. This population was formally excluded from the
  near-term ambient scribe rollout as a result.

Recommendation: keep these three exclusions as explicit, documented scope boundaries in the 2026
roadmap (per the December retro) rather than informal assumptions that could quietly erode.

## Evidence Trail
- **2025-04-22** — [Contextual Inquiry — Emergency Department Intake Shadowing](../raw/2025-04-22-contextual-inquiry-ed-intake-shadowing/session-notes.md) *(`contextual-inquiry`)*
- **2025-05-20** — [Interview — IT Security on SSO/MFA Modernization Impact](../raw/2025-05-20-interview-it-security-sso-mfa-modernization/session-notes.md) *(`interview`)*
- **2025-10-07** — [Contextual Inquiry — Behavioral Health Unit, Sensitive Note Handling](../raw/2025-10-07-contextual-inquiry-behavioral-health-sensitive-notes/session-notes.md) *(`contextual-inquiry`)*

## Related Findings
- [AI Governance, PHI & Compliance](governance-and-phi.md)
