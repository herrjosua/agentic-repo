---
title: Clinician Experience & Documentation Burden
date: 2025-09-09
type: synthesis
status: synthesized
tags:
  - baseline
  - burnout
  - clinician-experience
  - dashboard
  - documentation-burden
  - information-architecture
  - nursing
  - survey
  - trust-in-ai
  - usability
related_components:
  - ambient-scribe-widget
  - care-gap-badge
  - clinician-dashboard
related_findings:
  - ambient-scribe.md
  - care-coordination-triage.md
---

# Clinician Experience & Documentation Burden

## Overview
Three sessions trace clinician sentiment and documentation burden across the year: a nursing
attitudes survey (Feb 2025, before AI framing was introduced), a clinician dashboard usability test
(May 2025), and an org-wide burnout/documentation-burden baseline survey (Sep 2025, which
explicitly referenced the AI initiative).

- **The top volunteered concern was not accuracy or privacy — it was voice.** In February, "losing
  my clinical narrative voice / it will sound robotic" was the most common open-ended concern among
  nurses, ahead of accuracy or trust concerns that were originally hypothesized to dominate.
- **Documentation burden is real and quantifiable, not just anecdotal.** The September baseline
  found documentation burden is physicians' #1 self-selected burnout driver (52%, ahead of patient
  volume at 31%), with 64% doing regular after-hours "pajama time" charting (avg. 1.2 hrs/day). This
  is now the official pre-AI baseline for measuring Compass AI's impact at 6 and 12 months post-GA.
  **Caveat:** the September survey mentioned the AI initiative explicitly in its framing, while the
  February survey didn't — any comparison between the two datasets needs to account for that framing
  difference, not treat them as a clean before/after.
- **Alert fatigue is an emerging risk, not yet realized.** The May dashboard test found that 5 of 6
  participants expected AI-flagged "care gap" badges to become background noise within a week if
  flagging precision isn't improved — 2 of the 3 example flags shown were judged clinically
  low-value. This is the same alert-fatigue pattern later confirmed in the care-coordination alert
  triage testing (see [care-coordination-triage.md](care-coordination-triage.md)), suggesting it's a
  property of how these flagging models are currently tuned generally, not a one-off UI problem.

Recommendation: do not ship the care-gap flagging feature until precision is validated against
clinical review, and use the September survey as the fixed baseline instrument for future
comparisons rather than re-wording the questions.

## Evidence Trail
- **2025-02-11** — [Survey — Nursing Staff Attitudes Toward AI-Assisted Documentation](../raw/2025-02-11-survey-nursing-attitudes-ai-documentation/session-notes.md) *(`survey`)*
- **2025-05-06** — [Usability Test — Clinician Dashboard Redesign (v1)](../raw/2025-05-06-usability-test-clinician-dashboard-redesign-v1/session-notes.md) *(`usability-test`)*
- **2025-09-09** — [Survey — Clinician Burnout & Documentation Burden Baseline](../raw/2025-09-09-survey-clinician-burnout-documentation-burden-baseline/session-notes.md) *(`survey`)*

## Related Findings
- [Ambient AI Scribe](ambient-scribe.md)
- [Care Coordination & Alert Triage](care-coordination-triage.md)
