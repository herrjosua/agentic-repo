---
title: Care Coordination & Alert Triage
date: 2025-08-26
type: synthesis
status: synthesized
tags:
  - alert-fatigue
  - alert-triage
  - baseline
  - care-coordination
  - chart-review
  - usability
  - workflow
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

- **The baseline shaped what got built.** Coordinators explicitly said they didn't want full
  AI summarization (they already distrust the EHR's existing auto-summary tool after it missed
  medication changes twice) — what they wanted was "what changed since I last looked." The August
  alert-triage concept is a variant of that same idea applied to alert prioritization rather than
  chart summarization.
- **The triage ranking works, but not for the reason initially expected.** It was faster
  (6.5 min vs. 9 min to clear a 20-item queue), but 4 of 5 participants disagreed with at least one
  ranking decision, generally because the model weighted recency over coordinators' own sense of
  patient-history-driven risk — echoing the alert-fatigue concern raised separately in the May
  clinician dashboard testing (see
  [clinician-experience-documentation-burden.md](clinician-experience-documentation-burden.md)).
  There was also no way to capture *why* a coordinator overrode a ranking, which both loses a
  model-improvement signal and undercuts the sense of agency the supervisor specifically flagged as
  a risk (fast-but-wrong being worse than slow-but-right in this workflow).
- **This is also where the mobile accessibility touch-target finding lands** — the alert-triage icon
  set audited in November is the same feature tested here in August (see
  [accessibility-cross-cutting.md](accessibility-cross-cutting.md)).

Recommendation: add lightweight override-reason capture before further ranking-model tuning, and
share it with whoever owns the care-gap flagging model tuning, since it's likely the same underlying
problem.

## Evidence Trail
- **2025-01-29** — [Contextual Inquiry — Manual Chart Review Baseline (Care Coordinators)](../raw/2025-01-29-contextual-inquiry-chart-review-baseline/session-notes.md) *(`contextual-inquiry`)*
- **2025-08-26** — [Usability Test — AI Alert Triage for Care Coordination](../raw/2025-08-26-usability-test-alert-triage-ai-care-coordination/session-notes.md) *(`usability-test`)*

## Related Findings
- [Clinician Experience & Documentation Burden](clinician-experience-documentation-burden.md)
