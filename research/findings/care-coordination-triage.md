---
title: Care Coordination & Alert Triage
date: 2025-08-26
type: synthesis
status: synthesized
researcher: Priya Patel
tags:
  - alert-fatigue
  - alert-triage
  - baseline
  - care-coordination
  - chart-review
  - usability
  - workflow
  - project-care-coordination
related_components:
  - alert-triage-queue
  - chart-review-summary-panel
related_findings:
  - clinician-experience-documentation-burden.md
---

# Care Coordination & Alert Triage

## Overview
Two sessions bookend this topic: a baseline contextual inquiry of manual chart review (Jan 2025,
before any AI concept existed) and a usability test of an AI-ranked alert triage queue (Aug 2025).

- **The baseline recommended a narrow scope.** Coordinators already distrusted the EHR's
  auto-generated after-visit summaries, having caught them omitting recently changed medications
  twice in the past quarter. One coordinator (P05) said: "If it could just tell me what changed
  since I last touched this chart, that alone would save me time. I don't need it to think for
  me." The session recommended scoping an early AI concept around 'what changed since last review'
  rather than full summarization.
- **The AI-ranked queue was faster, but most participants disagreed with its ranking.** In this
  simulated test, triage of a 20-item queue was faster with AI ranking present (avg 6.5 min) than
  with a chronological queue (avg 9 min), but 4 of 5 participants disagreed with the AI's top-3
  ranking on at least one of three test queues, generally because the model weighted recency more
  heavily than coordinators' own sense of clinical risk — echoing the alert-fatigue concern raised separately in the May
  clinician dashboard testing (see
  [clinician-experience-documentation-burden.md](clinician-experience-documentation-burden.md)).
  There was also no way to capture *why* a coordinator overrode a ranking, so that correction
  signal isn't captured anywhere for future model improvement. Separately, the supervisor (P79)
  worried that speed gains could mask a coordinator rubber-stamping the AI order without real
  judgment: "fast and wrong is worse than slow and right in this job." The study's own
  recommendation adds that override-reason capture would give coordinators a sense of agency the
  current design lacks.
- **This is also where the mobile accessibility touch-target finding lands** — the alert-triage icon
  set audited in November is the same feature tested here in August (see
  [accessibility-cross-cutting.md](accessibility-cross-cutting.md)).

Recommendation: add lightweight override-reason capture before further ranking-model tuning, and
share it with whoever owns the care-gap flagging model tuning, since it's likely the same underlying
problem.

## Evidence Trail
- **2025-01-29** — [Contextual Inquiry — Manual Chart Review Baseline (Care Coordinators)](../raw/2025-01-29-contextual-inquiry-chart-review-baseline/session-notes.md) *(`contextual-inquiry`)*
- **2025-08-26** — [Usability Test — AI Alert Triage for Care Coordination](../raw/2025-08-26-usability-test-alert-triage-ai-care-coordination/session-notes.md) *(`usability-test`)*
- **2025-11-18** — [Accessibility Audit — Mobile Clinician App (Low Vision & Motor Impairment Focus)](../raw/2025-11-18-accessibility-audit-mobile-clinician-app/session-notes.md) *(`accessibility-audit`)*

## Related Findings
- [Clinician Experience & Documentation Burden](clinician-experience-documentation-burden.md)
