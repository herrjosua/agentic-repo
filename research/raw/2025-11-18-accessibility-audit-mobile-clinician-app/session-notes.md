---
title: Accessibility Audit — Mobile Clinician App (Low Vision & Motor Impairment Focus)
date: 2025-11-18
type: accessibility-audit
status: raw
tags:
  - accessibility
  - mobile
  - low-vision
  - motor-impairment
related_components:
  - mobile-app-alert-list
  - alert-triage-queue
related_findings:
  - ../../findings/accessibility-cross-cutting.md
---

# Accessibility Audit — Mobile Clinician App (Low Vision & Motor Impairment Focus)

## Objective
Assess mobile clinician app accessibility for low vision and motor impairment specifically, ahead of the app becoming a secondary surface for Compass AI features like alert triage.

## Method
- **Method:** Manual audit + 2 participant walkthroughs (low vision, limited fine motor control), iOS + Android
- **Researcher:** Priya Patel
- **Full participant roster:** see `participants.md` in this folder

## Key Findings
- **[HIGH]** *(touch target size)* Several action icons in the alert triage list (a Compass AI surface, per the August findings) are 32x32px, below the 44x44px minimum recommended for reliable use by the motor-impairment participant, who mis-tapped adjacent icons repeatedly.
- **[HIGH]** *(text scaling)* App text does not respect the OS-level dynamic text size setting; the low-vision participant's usual 200% system text setting had no effect within the app, forcing reliance on pinch-zoom which broke the layout.
- **[MEDIUM]** *(voiceover labeling)* Several icon-only buttons lack accessible labels, announced only as 'button' by VoiceOver.
- **[MEDIUM]** *(color-only status)* Same red/yellow/green-only status pattern flagged in the March legacy audit also appears here, suggesting it may be a broader design system gap rather than isolated to one surface.

## Representative Quotes
> "I set my phone to 200% text everywhere else. In this app it's like that setting doesn't exist."
> — Clinician, low vision, P103

> "Those little icons in the alert list, I hit the wrong one probably one in four times. On a good day."
> — Clinician, limited fine motor control, P105

## Recommendations
1. Fix touch target sizing on the alert triage icons as a priority, since it directly affects a live Compass AI feature (linking to August findings).
2. Implement support for OS-level dynamic text sizing; this is likely a systemic app issue, not specific to any one screen.
3. Note the recurring color-only status pattern (now found in 3 separate audits: legacy console, design system, mobile app) as a candidate for a single, org-wide design system fix rather than three separate ones.

## Follow-ups / Open Questions
- Confirm whether the color-only status issue has a single shared root component across surfaces, which would make for one fix instead of three.

## Related
- Synthesized into: [accessibility-cross-cutting.md](../../findings/accessibility-cross-cutting.md)
