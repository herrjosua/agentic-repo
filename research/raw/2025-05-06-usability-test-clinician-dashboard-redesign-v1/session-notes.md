---
title: Usability Test — Clinician Dashboard Redesign (v1)
date: 2025-05-06
type: usability-test
status: raw
tags:
  - dashboard
  - usability
  - clinician-experience
  - information-architecture
related_components:
  - clinician-dashboard
  - care-gap-badge
related_findings:
  - ../../findings/clinician-experience-documentation-burden.md
---

# Usability Test — Clinician Dashboard Redesign (v1)

## Objective
Test a redesigned clinician home dashboard that surfaces AI-flagged items (abnormal results, care gaps) alongside the standard patient list, to see if the new information hierarchy helps or adds noise.

## Method
- **Method:** Moderated usability test, task-based, 50 min/session
- **Researcher:** Priya Patel
- **Full participant roster:** see `participants.md` in this folder

## Key Findings
- **[HIGH]** *(alert fatigue)* 5 of 6 participants said the new AI-flagged 'care gap' badges would likely become background noise within a week if the flagging threshold isn't tuned, since 2 of the 3 example flags shown were judged clinically low-value.
- **[MEDIUM]** *(information architecture)* Participants generally liked having flags inline with the patient list rather than in a separate panel, but wanted a way to dismiss/snooze a flag per patient.
- **[MEDIUM]** *(trust)* Participants wanted to know the flag's underlying logic ('why is this flagged?') available on hover/click, not just the flag itself.
- **[MEDIUM]** *(visual design)* Badge color scheme was confused with existing acuity color-coding already used elsewhere in the EHR, creating a risk of misreading a documentation-quality flag as a clinical-acuity flag.
- **[LOW]** *(positive signal)* Participants responded well to the reduced number of clicks to get from dashboard to chart (2 clicks vs. 4 in the current system).

## Representative Quotes
> "If two out of three of these flags are junk, I'm going to start ignoring all of them, including the one that actually matters. That's worse than no flag at all."
> — Physician, P27

> "Don't reuse red/yellow/green for this. That already means something else to me on this exact screen."
> — Nurse Practitioner, P29

## Recommendations
1. Do not ship the care-gap flagging feature until precision is meaningfully improved and validated against clinical review, given the explicit alert-fatigue risk raised.
2. Change the flag badge visual system to something clearly distinct from the existing acuity color convention.
3. Add a 'why flagged' explanation and per-flag dismiss/snooze control before next round of testing.

## Follow-ups / Open Questions
- Get current false-positive rate on the care-gap model from Data Science before scheduling v2 testing.
- Coordinate with design system team on a non-conflicting badge treatment.

## Related
- Synthesized into: [clinician-experience-documentation-burden.md](../../findings/clinician-experience-documentation-burden.md)
