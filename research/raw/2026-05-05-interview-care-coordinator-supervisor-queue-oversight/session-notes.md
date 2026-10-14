---
title: Interview — Care Coordinator Supervisor on Queue Oversight
date: 2026-05-05
type: interview
status: raw
researcher: Priya Patel
tags:
  - care-coordination
  - alert-triage
  - alert-fatigue
  - trust-in-ai
  - audit-trail
related_components:
  - alert-triage-queue
related_findings:
  - ../../findings/care-coordination-triage.md
---

# Interview — Care Coordinator Supervisor on Queue Oversight

## Objective
Get a care coordinator supervisor's view of what oversight they would need if alerts were AI-ranked, following up the August 2025 supervisor's concern that speed gains could mask rubber-stamping, and the override-reason capture designed after that test. The participant is a different person from P79, the supervisor in the August 2025 test.

## Method
- **Method:** 1:1 interview, 45 min
- **Researcher:** Priya Patel
- **Full participant roster:** see `participants.md` in this folder
- **Context:** The participant leads an ambulatory care coordination team. Their team works the chronological queue; the AI-ranked queue hasn't been built, and the override-reason capture wireflow is designed and in review, not built. They had not seen the August 2025 screens before; they reacted to a description of the ranked queue and the override-reason flow in this session. They did not take part in any earlier session.

## Key Findings
- **[HIGH]** *(oversight)* If alerts were AI-ranked, they would want a record of the order each coordinator was shown and what the coordinator did with each alert, so they could look back at a case when something went wrong. They would also use override reasons for coaching, to see how a coordinator is judging risk, not only for model tuning. That raises a question the current design doesn't settle: the wireflow logs reasons for model-tuning review and says they are "not surfaced to other coordinators", but doesn't say whether supervisors see them.
- **[MEDIUM]** *(alert volume)* They estimated that heavy days run "maybe 30 to 60 alerts" per coordinator, and that many of them are administrative rather than clinical. This is their informal estimate; no queue data was reviewed in this session.
- **[MEDIUM]** *(rubber-stamping)* They shared the August 2025 supervisor's worry that a ranked order could be followed without judgement, but said they'd only know if it was happening by looking at what coordinators did with the order. This is a perspective, not a measurement; nothing about how often coordinators follow a ranking has been measured.

## Representative Quotes
> "If something goes wrong, I need to see what order they were shown and what they did with it. Otherwise I'm coaching blind."
> — Care Coordinator Supervisor, P132

> "The reasons are the useful part for me. They tell me how someone's thinking about risk."
> — Care Coordinator Supervisor, P132

## Recommendations
1. Decide who can see override reasons (model-tuning review only, or supervisors as well) before the reason-capture wireflow leaves review, and say so in the design.
2. If a ranked queue is piloted, record the order shown and each coordinator's action, so rubber-stamping can be looked for in data rather than assumed.

## Follow-ups / Open Questions
- How often coordinators would follow a ranked order without judgement is not measured, and can't be until something is built and logged.
- Real alert volumes per coordinator are not known; the 30 to 60 figure is one supervisor's estimate.
- Whether the override-capture idea was shared with the Data Science team working on the care-gap flagging model, as the August 2025 session suggested, isn't recorded.

## Related
- Synthesized into: [care-coordination-triage.md](../../findings/care-coordination-triage.md)
