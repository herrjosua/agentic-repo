---
title: Interview — Telemetry Nurse on Start-of-Shift Chart Review
date: 2026-10-13
type: interview
status: raw
researcher: Priya Patel
tags:
  - nursing
  - chart-review
  - clinician-workflow
  - information-architecture
related_components: []
related_findings:
  - ../../findings/clinician-experience-documentation-burden.md
---

# Interview — Telemetry Nurse on Start-of-Shift Chart Review

## Objective
The information-architecture evidence in `clinician-experience-documentation-burden.md` comes from the May 2025 dashboard test, whose roster lists physicians, a nurse practitioner and a physician assistant but no nurses; participants there preferred flags inline with the patient list over a separate panel (2025-05-06-usability-test-clinician-dashboard-redesign-v1/session-notes.md:31). The nurse sessions since then cover the handoff narrative (ICU, May 2026) and after-shift charting (medical-surgical, July 2026), but none describes how an inpatient nurse reviews the chart when they pick up their patients. This session asked a telemetry nurse how they review the chart at the start of a day shift, and what they would expect of an AI chart summary, which doesn't exist.

## Method
- **Method:** 1:1 interview, 45 min
- **Researcher:** Priya Patel
- **Full participant roster:** see `participants.md` in this folder
- **Context:** The participant is a registered nurse on a step-down telemetry unit, working day shift, mid-career. Their charting is manual and no AI feature is used in their own work; the ambient scribe, GA since January 2026, drafts notes for physicians, NPs and PAs only. Everything they said about an AI chart summary is an expectation, not experience: the only summary concept in the corpus, the chart-review summary panel, is unbuilt and was scoped for care coordinators, and it was not described or shown in this session. They did not take part in any earlier session. They are not P141, the medical-surgical night nurse interviewed in July 2026, and not P140, the ICU nurse interviewed in May 2026.

## Key Findings
- **[MEDIUM]** *(start-of-shift order)* They review each patient's chart in a fixed order, around the verbal report from the night nurse: the report first, then active orders, the medications due in the first hours of the shift, overnight telemetry events and vital-sign trends, the latest labs, then the night nurse's narrative note, and the provider progress notes last, if there is time. The order follows what could hurt the patient soonest, not the chart's sections, so they open several screens per patient to assemble it. They put it at "about five minutes a patient, more for a new admission" on a typical assignment of four; that is an informal estimate, not timed.
- **[MEDIUM]** *(expectation of an AI summary)* What they would expect of a summary at the start of a shift: items ordered by what needs action first (medications due, telemetry events, pending labs, new orders), each linked to where it came from in the chart, and a plain statement of what the summary covered, because a summary that leaves things out without saying so would send them back through the whole chart. They would not want it to replace the night nurse's narrative, which they read anyway because it carries what the night nurse was worried about. This is an expectation of a tool that doesn't exist; nothing was shown.
- **[LOW]** *(where it sits)* They would want any summary next to the patient list they start the shift from, not in a separate place they have to go looking for. This is consistent with the May 2025 dashboard test's preference for information inline with the patient list, and adds a nurse view to it; it came up once and wasn't explored.

## Representative Quotes
> "I go in the order things can hurt somebody. What's due, what the monitor caught overnight, then labs. Progress notes are last, if I get to them."
> — Registered Nurse (telemetry), P145

> "If it summarizes, it has to tell me what it didn't look at. Otherwise I'm going through the whole chart again anyway."
> — Registered Nurse (telemetry), P145

## Recommendations
1. When `clinician-experience-documentation-burden.md` is next revised, add a nurse view to its information-architecture evidence: at the start of a shift, this nurse orders chart review by what needs action soonest, not by chart section.
2. If an AI chart summary for inpatient nurses is ever scoped, test ordering by time to action, links back to the source, a statement of what it covered, and keeping the night nurse's narrative as written rather than summarized.
3. Keep this separate from the care coordinators' "what changed" concept: this nurse's needs come from a shift handoff, and nothing here was tested against that concept.

## Follow-ups / Open Questions
- How long start-of-shift chart review takes is not measured; "about five minutes a patient" is one nurse's estimate, on one unit.
- Whether night-shift nurses, or nurses on other units, review the chart in the same order is not known; this is one interview.
- Whether a summary would save time or add another screen to check is untested; no such summary exists.
- Whether the provider notes they read are scribe-drafted didn't come up and is not known.

## Related
- Synthesized into: [clinician-experience-documentation-burden.md](../../findings/clinician-experience-documentation-burden.md)
