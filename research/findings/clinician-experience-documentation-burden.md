---
title: Clinician Experience & Documentation Burden
date: 2026-10-13
type: synthesis
status: synthesized
researcher: Priya Patel
tags:
  - ambient-scribe
  - baseline
  - burnout
  - chart-review
  - clinician-experience
  - clinician-workflow
  - dashboard
  - documentation
  - documentation-burden
  - high-acuity
  - information-architecture
  - nursing
  - survey
  - trust-in-ai
  - usability
  - project-cross-cutting
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
  nurses — not accuracy or privacy as originally hypothesized.
- **Documentation burden is real and quantifiable, not just anecdotal.** The September baseline
  found documentation burden is physicians' #1 self-selected burnout driver (52%, ahead of patient
  volume at 31%), with 64% doing regular after-hours "pajama time" charting (avg. 1.2 hrs/day). The
  session recommends it as the official pre-AI baseline for measuring Compass AI's impact at 6 and
  12 months post-rollout.
  **Caveat:** the September survey mentioned the AI initiative explicitly in its framing, while the
  February survey didn't — any comparison between the two datasets needs to account for that framing
  difference, not treat them as a clean before/after.
- **Alert fatigue is an emerging risk, not yet realized.** The May dashboard test found that 5 of 6
  participants expected AI-flagged "care gap" badges to become background noise within a week if
  flagging precision isn't improved — 2 of the 3 example flags shown were judged clinically
  low-value. The care-coordination alert triage testing later echoed this alert-fatigue concern
  (see [care-coordination-triage.md](care-coordination-triage.md)). That session judged the two
  "likely the same underlying tuning problem" — an inference it recommended sharing with the
  care-gap model's Data Science team, not something either session tested.

Recommendation: do not ship the care-gap flagging feature until precision is validated against
clinical review, and use the September survey as the fixed baseline instrument for future
comparisons rather than re-wording the questions.

## Since GA: 2026 Nurse Interviews
Four 1:1 interviews between March and October 2026 asked registered nurses, all new to this
research, about documentation after the ambient scribe went GA in January 2026: a primary care
clinic nurse (P138), an ICU nurse (P140), a medical-surgical night nurse (P141) and a telemetry
nurse (P145). The scribe drafts visit notes for physicians, NPs and PAs only; no nurse uses it for
their own documentation and nurse charting is manual, so what nurses said about AI drafting nursing
notes is expectation, not experience. Every figure below is an informal participant estimate or
recollection, not a count or a rate.

- **The September figures are physician-only.** The 52%, 31%, 64% and 1.2 hours a day above
  describe physicians and should not be read as describing nurses. The September baseline's roster
  lists registered nurses among its respondents, but its notes report these figures for physicians
  only, and whether nurse results exist is not recorded.
- **Nurses chart after the shift too, with no nurse figure.** A medical-surgical night nurse
  regularly finishes notes after handoff, "most shifts, thirty to forty-five minutes", mostly
  narrative and end-of-shift reassessments deferred whenever a patient needed something (informal
  self-estimate; 2026-07-21, HIGH). That is one nurse on one unit, not comparable to the physician
  figures; they described fatigue, not burnout, and no burnout measure was used.
- **The voice concern has two readings.** The February 2025 survey framed it as nurses losing their
  own narrative voice. An ICU nurse described the narrative as a handoff safety artifact, where
  they record what worried them and what the next nurse should watch, and expected that a nurse at
  the end of a twelve-hour shift would accept an AI draft of it rather than rewrite it (2026-05-28,
  HIGH; the expectation, MEDIUM). A clinic nurse who reads scribe-drafted provider notes placed the
  concern in other people's notes: they read less like the provider, so it is harder to tell what
  the provider meant to emphasise (2026-03-17, MEDIUM). This complicates the survey's framing, but
  it doesn't show which reading is more common: the two readings come from different nurses, and
  neither is a count.
- **Nurses who read scribe-drafted notes act on the plan.** The clinic nurse now reads the whole
  note before a callback, because plan items said during the visit sometimes land in the body
  rather than the plan ("a few times a week", an informal impression; 2026-03-17, HIGH). If the
  plan is incomplete, they message the provider before calling the patient, which delays the
  callback.
- **Start-of-shift chart review follows urgency, not the chart's sections.** A telemetry nurse
  reviews each chart in the order of what could hurt the patient soonest (medications due,
  overnight telemetry events and trends, labs, then the night nurse's narrative, progress notes
  last), at "about five minutes a patient" on an assignment of four (informal estimate;
  2026-10-13, MEDIUM). They would expect an AI summary to order items by what needs action first,
  link each to its source, say what it covered, sit next to the patient list, and leave the night
  nurse's narrative as written (2026-10-13, MEDIUM and LOW; an expectation, nothing shown). This
  adds a nurse view to the May 2025 test's information-architecture evidence, whose roster had no
  nurses.

Still open after the 2026 interviews: how much time nurses spend charting (nothing measured);
whether skepticism varies with tenure (the February survey's cross-tab hasn't been run, and one
newer nurse's view can't answer it); whether the survey's ICU and ED skepticism holds beyond one
ICU interview; and how often plan items land outside the plan in scribe-drafted notes.

## Evidence Trail
- **2025-02-11** — [Survey — Nursing Staff Attitudes Toward AI-Assisted Documentation](../raw/2025-02-11-survey-nursing-attitudes-ai-documentation/session-notes.md) *(`survey`)*
- **2025-05-06** — [Usability Test — Clinician Dashboard Redesign (v1)](../raw/2025-05-06-usability-test-clinician-dashboard-redesign-v1/session-notes.md) *(`usability-test`)*
- **2025-09-09** — [Survey — Clinician Burnout & Documentation Burden Baseline](../raw/2025-09-09-survey-clinician-burnout-documentation-burden-baseline/session-notes.md) *(`survey`)*
- **2026-03-17** — [Interview — Clinic Nurse on Reading Scribe-Drafted Visit Notes](../raw/2026-03-17-interview-clinic-nurse-reading-scribe-drafted-notes/session-notes.md) *(`interview`)*
- **2026-05-28** — [Interview — ICU Nurse on the Handoff Narrative](../raw/2026-05-28-interview-icu-nurse-handoff-narrative/session-notes.md) *(`interview`)*
- **2026-07-21** — [Interview — Med-Surg Night Nurse on Charting Load](../raw/2026-07-21-interview-med-surg-night-nurse-charting-load/session-notes.md) *(`interview`)*
- **2026-10-13** — [Interview — Telemetry Nurse on Start-of-Shift Chart Review](../raw/2026-10-13-interview-telemetry-nurse-start-of-shift-chart-review/session-notes.md) *(`interview`)*

## Related Findings
- [Ambient AI Scribe](ambient-scribe.md)
- [Care Coordination & Alert Triage](care-coordination-triage.md)
